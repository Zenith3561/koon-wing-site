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
