# Koon Wing Product — website

Static site (plain HTML + CSS + one small JS file). No build step needed to serve it;
`_build/build_site.py` regenerates the six pages from the photo manifest if content changes.

## Run locally

```bash
cd site
python -m http.server 8231
# → http://localhost:8231
```

## Deploy

```bash
cd site
npx vercel --prod
```

Nothing to compile — Vercel serves the folder as-is.

## Structure

Two full language versions. English at the root, Chinese under `zh/`.
Both carry the same content — a Chinese page is Chinese all the way down,
not an English page with Chinese headings.

```
site/
├── index.html          Home            (English)
├── products.html       10 product formats, one row each
├── showcase.html       57 design samples, filter + lightbox
├── about.html          Who we are / how we work
├── partnership.html    OEM / ODM / private label
├── contact.html        Enquiry form + direct details
├── zh/                 The same six pages, in Traditional Chinese
├── assets/
│   ├── css/style.css   All styling; design tokens at the top of the file
│   ├── js/main.js      Mobile nav, gallery filter, lightbox
│   ├── img/            Logo (SVG) + favicon
│   ├── products/       57 photos × 2 sizes, WebP
│   └── manifest.json   Photo index used by the generator
└── _build/build_site.py  Page generator — every string as an (en, zh) pair
```

A visitor switches language with the EN / 中文 pill in the navigation, and
each page declares the other language via `<link rel="alternate" hreflang>`
so search engines index them as one site in two languages.

Under a heading, the *other* language appears as a small secondary line.
That is deliberate: it keeps the bilingual look of the design without
leaving a page whose headings and body disagree.

## Editing content

All copy lives in `_build/build_site.py`. Every string is written once as an English/Chinese
pair — `t("English", "中文")` in the page functions, and `en=`/`zh=` blocks in the `SERIES`,
`GROUPS` and `STEPS` lists. Edit there and re-run; both language versions regenerate together:

```bash
python _build/build_site.py
```

Editing the `.html` files directly also works, but the next generator run overwrites them.

## Logo

Redesigned in navy + gold to sit with the product photography. Source files:

| File | Use |
|---|---|
| `assets/img/logo-mark.svg` | Ring mark alone — header, small sizes |
| `assets/img/logo-lockup.svg` | Full lockup, navy — light backgrounds |
| `assets/img/logo-lockup-light.svg` | Full lockup, white/gold — navy backgrounds |
| `assets/img/favicon.svg` | Browser tab |

The original client logo (`WhatsApp Image 2026-07-29 at 03.18.26.jpeg`, 502×420 JPEG,
cream background, no transparency) is too low-resolution for web use. If the client can
supply the vector original, the lockup should be re-cut from it.

## Live

| | |
|---|---|
| English | https://koonwingproduct.com.mo |
| Traditional Chinese | https://koonwingproduct.com.mo/zh/ |
| Enquiry endpoint | https://form.koonwingproduct.com.mo (Cloudflare Worker `koonwing-enquiry`) |
| Mailbox | info@koonwingproduct.com.mo (mailcow on mail.zenithacct.com) |

Hosting is GitHub Pages from `Zenith3561/koon-wing-site`; a push to `main`
rebuilds within about a minute. DNS is Cloudflare, delegated from MONIC.

**Every Cloudflare record for this site must stay DNS-only (grey cloud).**
Turning the proxy on stops GitHub from seeing the request, and the HTTPS
certificate silently fails to renew.

## The enquiry form

`contact.html` posts JSON to the Worker, which speaks SMTP on port 465 to
mailcow as `noreply@koonwingproduct.com.mo` and delivers to `info@`, with the
sender's address as Reply-To. Port 465 specifically — STARTTLS on 587 hangs
inside Workers and port 25 is blocked outbound.

Worker source: `../worker/enquiry-worker.js`. Its secrets (SMTP host, user,
password, destination) are stored on the Worker, not in this repository. If the
mailbox password changes, redeploy the Worker with the new secret.

If the request fails the page falls back to composing the same message in the
visitor's mail app, which is also the no-JS path.

## Still outstanding

1. **SOGo does not know this domain yet.** Mail sends and receives normally, but
   CalDAV/CardDAV returns 401, so desktop clients keep asking for a password.
   Fix: `ssh root@5.189.167.40`, `cd /opt/mailcow-dockerized`,
   `docker compose restart sogo-mailcow`. Workaround: turn off calendar and
   contacts for the account in the mail client.
2. **Product specifications need the client's eye.** The "typical build" and
   "options" rows on `products.html` are written as what *can* be specified, not
   as claims about goods already delivered — but the client should still strike
   anything they would not actually offer.
3. **No phone number** — the client chose not to publish one; the row is absent
   rather than showing a placeholder.

## Content rules applied

No claim appears on this site that has not been verified:

- No founding year, no "since 19xx", no years-of-experience figure.
- No ISO or other certification claim.
- No country count, client count or design count.
- No claim to own a factory — the about page states plainly that production is placed
  with partner manufacturers.
- Every product photograph is labelled as a design sample. Brand names visible inside the
  images (AETHEL, AURELIUS, SILVERSTONE, BARLEY & BRASS, AETHER, ARTIST SERIES) are
  AI-generated and fictional; the showcase page says so explicitly, and the about page
  answers the question directly.
