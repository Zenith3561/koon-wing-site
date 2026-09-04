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

```
site/
├── index.html          Home
├── products.html       10 product formats, one row each
├── showcase.html       57 design samples, filter + lightbox
├── about.html          Who we are / how we work
├── partnership.html    OEM / ODM / private label
├── contact.html        Enquiry form + direct details
├── assets/
│   ├── css/style.css   All styling; design tokens at the top of the file
│   ├── js/main.js      Mobile nav, gallery filter, lightbox
│   ├── img/            Logo (SVG) + favicon
│   ├── products/       57 photos × 2 sizes, WebP
│   └── manifest.json   Photo index used by the generator
└── _build/build_site.py  Page generator (content lives in here)
```

## Editing content

All copy lives in `_build/build_site.py` — the `SERIES`, `GROUPS` and `STEPS` lists plus the
`page_*()` functions. Edit there and re-run:

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

## Before launch — outstanding items

1. **Contact details** — email, phone, WhatsApp and full address are placeholders
   (`To be confirmed 待確認`). In `_build/build_site.py`, replace the `TBC` constant.
2. **Enquiry form** — posts nowhere. Needs a form endpoint (Formspree, Vercel serverless,
   or a `mailto:` fallback) wired to `<form action>` in `page_contact()`.
3. **Product specifications** — the "Typical build" and "Options" rows on `products.html`
   are written as what *can* be specified, not as claims about goods already delivered.
   The client should still read them and correct anything they would not actually offer.
4. **Domain** — none registered yet.

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
