/**
 * Koon Wing Product — enquiry form endpoint.
 *
 * Takes the POST from the contact form and hands it to the client's own
 * mailcow server, so an enquiry never passes through a third party.
 *
 * SMTP is spoken directly over a TCP socket. Port 465 with implicit TLS,
 * not 587 — STARTTLS is unreliable inside Workers (startTls() hangs), and
 * port 25 is blocked outbound.
 */

import { connect } from 'cloudflare:sockets';

const ALLOWED_ORIGINS = [
  'https://koonwingproduct.com.mo',
  'https://www.koonwingproduct.com.mo',
  'https://zenith3561.github.io',
];

const FIELDS = [
  ['name', 'Name'],
  ['company', 'Company'],
  ['email', 'Email'],
  ['phone', 'Phone'],
  ['product', 'Product'],
  ['qty', 'Quantity'],
  ['deadline', 'Needed by'],
];

const cors = (origin) => ({
  'Access-Control-Allow-Origin': ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0],
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Max-Age': '86400',
});

const json = (body, status, origin) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...cors(origin) },
  });

/* ── minimal SMTP client ───────────────────────────────────────────────── */
class Smtp {
  constructor(socket) {
    this.writer = socket.writable.getWriter();
    this.reader = socket.readable.getReader();
    this.enc = new TextEncoder();
    this.dec = new TextDecoder();
    this.buf = '';
  }

  async read() {
    // An SMTP reply ends with "NNN " (space, not hyphen) on its last line.
    for (;;) {
      const done = /^\d{3} [^\n]*\r?\n$|\n\d{3} [^\n]*\r?\n$/.test(this.buf);
      if (this.buf && done) break;
      const { value, done: closed } = await this.reader.read();
      if (closed) break;
      this.buf += this.dec.decode(value, { stream: true });
    }
    const out = this.buf;
    this.buf = '';
    return out;
  }

  async cmd(line, expect) {
    if (line !== null) await this.writer.write(this.enc.encode(line + '\r\n'));
    const reply = await this.read();
    const code = parseInt(reply.slice(0, 3), 10);
    if (!expect.includes(code)) {
      throw new Error(`SMTP ${code}: ${reply.trim().slice(0, 160)}`);
    }
    return reply;
  }

  async close() {
    try { await this.writer.close(); } catch (_) { /* already gone */ }
  }
}

function b64(str) {
  const bytes = new TextEncoder().encode(str);
  let bin = '';
  bytes.forEach((b) => { bin += String.fromCharCode(b); });
  return btoa(bin);
}

/* Fold a header value that may contain non-ASCII into RFC 2047 encoded words. */
function encodeHeader(value) {
  // eslint-disable-next-line no-control-regex
  if (/^[\x20-\x7E]*$/.test(value)) return value;
  return '=?UTF-8?B?' + b64(value) + '?=';
}

/* A bare "." on its own line ends DATA, so any real one must be doubled. */
const dotStuff = (body) => body.replace(/\r?\n\./g, '\r\n..');

async function sendMail(env, { subject, body, replyTo }) {
  const socket = connect(
    { hostname: env.SMTP_HOST, port: 465 },
    { secureTransport: 'on', allowHalfOpen: false },
  );
  const smtp = new Smtp(socket);
  try {
    await smtp.cmd(null, [220]);
    await smtp.cmd(`EHLO ${env.SMTP_HOST}`, [250]);
    await smtp.cmd('AUTH LOGIN', [334]);
    await smtp.cmd(b64(env.SMTP_USER), [334]);
    await smtp.cmd(b64(env.SMTP_PASS), [235]);
    await smtp.cmd(`MAIL FROM:<${env.SMTP_USER}>`, [250]);
    await smtp.cmd(`RCPT TO:<${env.MAIL_TO}>`, [250, 251]);
    await smtp.cmd('DATA', [354]);

    const headers = [
      `From: Koon Wing website <${env.SMTP_USER}>`,
      `To: <${env.MAIL_TO}>`,
      replyTo ? `Reply-To: <${replyTo}>` : null,
      `Subject: ${encodeHeader(subject)}`,
      `Date: ${new Date().toUTCString()}`,
      `Message-ID: <${crypto.randomUUID()}@koonwingproduct.com.mo>`,
      'MIME-Version: 1.0',
      'Content-Type: text/plain; charset=UTF-8',
      'Content-Transfer-Encoding: base64',
    ].filter(Boolean).join('\r\n');

    const encoded = b64(body).replace(/(.{76})/g, '$1\r\n');
    await smtp.cmd(`${headers}\r\n\r\n${dotStuff(encoded)}\r\n.`, [250]);
    await smtp.cmd('QUIT', [221]);
  } finally {
    await smtp.close();
  }
}

/* ── request handling ──────────────────────────────────────────────────── */
export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: cors(origin) });
    }
    if (request.method !== 'POST') {
      return json({ error: 'method not allowed' }, 405, origin);
    }
    if (origin && !ALLOWED_ORIGINS.includes(origin)) {
      return json({ error: 'origin not allowed' }, 403, origin);
    }

    let data;
    try {
      const ct = request.headers.get('Content-Type') || '';
      data = ct.includes('application/json')
        ? await request.json()
        : Object.fromEntries(await request.formData());
    } catch (_) {
      return json({ error: 'could not read the form' }, 400, origin);
    }

    // Honeypot: a real person never fills a field they cannot see.
    if ((data.website || '').trim()) return json({ ok: true }, 200, origin);

    const get = (k) => String(data[k] ?? '').trim().slice(0, 2000);
    const name = get('name');
    const email = get('email');
    const message = get('msg');

    if (!name || !email || !message) {
      return json({ error: 'name, email and message are required' }, 400, origin);
    }
    if (!/^[^@\s]+@[^@\s.]+\.[^@\s]+$/.test(email)) {
      return json({ error: 'that email address does not look right' }, 400, origin);
    }

    const lines = FIELDS
      .map(([key, label]) => [label, get(key)])
      .filter(([, v]) => v)
      .map(([label, v]) => `${label}: ${v}`)
      .join('\n');

    const body =
      `${lines}\n\n${message}\n\n` +
      `— sent from the enquiry form at koonwingproduct.com.mo\n`;

    try {
      await sendMail(env, {
        subject: `Enquiry from ${get('company') || name}`,
        body,
        replyTo: email,
      });
    } catch (err) {
      console.log('send failed:', err && err.message);
      return json({ error: 'could not send just now' }, 502, origin);
    }

    return json({ ok: true }, 200, origin);
  },
};
