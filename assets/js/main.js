/* Koon Wing Product — site behaviour
   Pointer events (not mouse) so touch devices behave; no window.confirm anywhere. */
(function () {
  'use strict';

  /* ── mobile nav ─────────────────────────────────────────────── */
  var topnav = document.querySelector('.topnav');
  var toggle = document.querySelector('.navtoggle');
  if (topnav && toggle) {
    toggle.addEventListener('click', function () {
      var open = topnav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    topnav.querySelectorAll('nav a').forEach(function (a) {
      a.addEventListener('click', function () {
        topnav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ── enquiry form ───────────────────────────────────────────────
     Posts to a Cloudflare Worker that hands the message to the company's
     own mail server, so an enquiry never passes through a third party.
     If that call fails the visitor is not left stranded: we fall back to
     composing the same message in their mail app, which is also what the
     form's plain mailto action does when JavaScript is off.           */
  var ENDPOINT = 'https://form.koonwingproduct.com.mo/';
  var form = document.getElementById('enquiry');

  if (form) {
    var status = form.querySelector('.form-status');
    var button = form.querySelector('button[type=submit]');
    var zh = (document.documentElement.lang || '').indexOf('zh') === 0;
    var say = function (text, kind) {
      if (!status) return;
      status.textContent = text;
      status.className = 'form-status ' + kind;
      status.hidden = false;
    };
    var get = function (id) {
      var el = document.getElementById(id);
      return el ? el.value.trim() : '';
    };
    var compose = function () {
      var rows = [
        ['Name', get('name')], ['Company', get('company')], ['Email', get('email')],
        ['Phone', get('phone')], ['Product', get('product')], ['Quantity', get('qty')],
        ['Needed by', get('deadline')]
      ].filter(function (r) { return r[1]; })
        .map(function (r) { return r[0] + ': ' + r[1]; }).join('\n');
      return {
        subject: 'Enquiry from ' + (get('company') || get('name')),
        body: rows + '\n\n' + get('msg') + '\n'
      };
    };

    form.addEventListener('submit', function (e) {
      if (!get('name') || !get('email') || !get('msg')) return;  // let the browser complain
      e.preventDefault();

      var payload = {
        name: get('name'), company: get('company'), email: get('email'),
        phone: get('phone'), product: get('product'), qty: get('qty'),
        deadline: get('deadline'), msg: get('msg'), website: get('website')
      };

      if (button) { button.disabled = true; }
      say(zh ? '傳送中……' : 'Sending…', 'ok');

      fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      }).then(function (r) {
        if (!r.ok) throw new Error('http ' + r.status);
        form.reset();
        say(zh
          ? '已收到您的查詢，我們通常於一個工作天內回覆。'
          : 'Thank you — your enquiry has reached us. We usually reply within one business day.', 'ok');
      }).catch(function () {
        var m = compose();
        say(zh
          ? '無法直接送出。已為您開啟電郵程式，內容已填好，請按傳送。'
          : 'Could not send that directly. Your email app should open with the message ready — please press send.', 'err');
        window.location.href = 'mailto:info@koonwingproduct.com.mo'
          + '?subject=' + encodeURIComponent(m.subject)
          + '&body=' + encodeURIComponent(m.body);
      }).then(function () {
        if (button) { button.disabled = false; }
      });
    });
  }

  /* ── gallery filter ─────────────────────────────────────────── */
  var filters = document.querySelectorAll('.filter');
  var shots = document.querySelectorAll('.gallery .shot');
  if (filters.length && shots.length) {
    filters.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var key = btn.dataset.filter;
        filters.forEach(function (b) {
          b.setAttribute('aria-pressed', b === btn ? 'true' : 'false');
        });
        shots.forEach(function (s) {
          s.hidden = !(key === 'all' || s.dataset.series === key);
        });
        visible = [].slice.call(shots).filter(function (s) { return !s.hidden; });
      });
    });
  }

  /* ── lightbox ───────────────────────────────────────────────── */
  var lb = document.querySelector('.lb');
  if (!lb || !shots.length) return;
  var lbImg = lb.querySelector('img');
  var lbCap = lb.querySelector('.lb-cap');
  var visible = [].slice.call(shots);
  var idx = 0;
  var lastFocus = null;

  function show(i) {
    if (!visible.length) return;
    idx = (i + visible.length) % visible.length;
    var fig = visible[idx];
    lbImg.src = fig.dataset.full;
    lbImg.alt = fig.dataset.caption || '';
    lbCap.textContent = (idx + 1) + ' / ' + visible.length + '  ·  ' + (fig.dataset.caption || '');
  }
  function open(i) {
    lastFocus = document.activeElement;
    show(i);
    lb.classList.add('on');
    document.body.style.overflow = 'hidden';
    lb.querySelector('.lb-close').focus();
  }
  function close() {
    lb.classList.remove('on');
    document.body.style.overflow = '';
    lbImg.removeAttribute('src');
    if (lastFocus) lastFocus.focus();
  }

  shots.forEach(function (fig) {
    fig.addEventListener('click', function () {
      open(visible.indexOf(fig));
    });
  });
  lb.querySelector('.lb-close').addEventListener('click', close);
  lb.querySelector('.lb-prev').addEventListener('click', function (e) { e.stopPropagation(); show(idx - 1); });
  lb.querySelector('.lb-next').addEventListener('click', function (e) { e.stopPropagation(); show(idx + 1); });
  lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
  document.addEventListener('keydown', function (e) {
    if (!lb.classList.contains('on')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(idx - 1);
    if (e.key === 'ArrowRight') show(idx + 1);
  });
})();
