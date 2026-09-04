# -*- coding: utf-8 -*-
"""Generate the Koon Wing Product static site (6 pages) from the photo manifest."""
import json, os, io

SITE = r"C:\Users\tyron\OneDrive - Speedy Three Limited\0 AI Coding\Projects\website-service\clients\koon-wing\site"
MAN = json.load(open(os.path.join(SITE, "assets", "manifest.json")))

TBC = '<span class="tbc">To be confirmed 待確認</span>'

SERIES = [
    dict(key="lapel-pin", en="Enamel Lapel Pins", cn="琺瑯襟章",
         group="badges",
         blurb="Die-struck or die-cast pins finished in soft or hard enamel. The format most corporate "
               "programmes start with — small, giftable, and instantly recognisable on a jacket.",
         build="Zinc alloy or brass base · soft / hard enamel · polished gold, nickel or black plating",
         options="Butterfly clutch, magnetic back, rubber back or safety pin · individual boxing · custom shape",
         tags=["Enamel", "Die-struck", "Plated"]),
    dict(key="keychain", en="Acrylic Keychains", cn="亞加力匙扣",
         group="badges",
         blurb="Clear acrylic charms with full-colour artwork printed through. Suits illustration-led "
               "brands, artist series and event merchandise where colour matters more than metal.",
         build="Cast acrylic 3 mm · full-colour UV print · optional epoxy dome",
         options="Split ring, lobster clasp or ball chain · single charm or matched sets · printed backer card",
         tags=["Acrylic", "UV print", "Full colour"]),
    dict(key="tie-clip", en="Tie Clips & Formal Accessories", cn="領帶夾及禮儀配飾",
         group="desk",
         blurb="Weighted formal accessories for executive gifting, long-service awards and hospitality "
               "uniforms. Engraving keeps the piece quiet enough to wear every day.",
         build="Stainless steel or brass · polished, brushed or PVD finish",
         options="Laser or diamond-drag engraving · enamel inlay · velvet-lined presentation box",
         tags=["Steel", "Engraved", "Boxed"]),
    dict(key="pen", en="Metal Ball Pens", cn="金屬原子筆",
         group="desk",
         blurb="A weighted metal pen is still the most-used corporate gift there is. Soft-touch barrels "
               "hold branding cleanly and feel more considered than a printed plastic body.",
         build="Brass barrel · soft-touch or lacquer coating · chrome trim · standard refill",
         options="Laser engraving or pad printing · gift box or sleeve · matched notebook sets",
         tags=["Brass", "Soft-touch", "Engraved"]),
    dict(key="bookmark", en="Filigree Metal Bookmarks", cn="金屬鏤空書籤",
         group="desk",
         blurb="Photo-etched openwork in plated metal, finished with a silk tassel. A low-cost, "
               "high-perceived-value piece for museums, publishers and cultural programmes.",
         build="Photo-etched stainless steel or brass · gold or rose-gold plating · silk tassel",
         options="Custom pattern from your artwork · bead colour matching · paper or fabric gift box",
         tags=["Etched", "Plated", "Tassel"]),
    dict(key="bottle-opener", en="Bottle Openers", cn="開瓶器",
         group="bar",
         blurb="Wood-and-metal openers built for craft drinks brands, bars and hospitality gifting — "
               "the kind of object that stays on a counter rather than in a drawer.",
         build="Beech or walnut handle · cast metal head · enamel badge inlay",
         options="Branded badge or engraved handle · kraft, wood or rigid gift box",
         tags=["Wood", "Cast metal", "Badge"]),
    dict(key="coaster-metal", en="Brushed Metal Coasters", cn="拉絲金屬杯墊",
         group="bar",
         blurb="Spun aluminium coasters with a brushed face and a soft base. Reads as product, not "
               "merchandise — suited to specialty coffee, spirits and design-led retail.",
         build="Spun aluminium · brushed and anodised face · cork or felt base",
         options="Enamel or printed centre · single or boxed set of four · printed outer carton",
         tags=["Aluminium", "Brushed", "Cork base"]),
    dict(key="coaster-enamel", en="Gold-Rim Enamel Coasters", cn="金邊琺瑯杯墊",
         group="bar",
         blurb="A heavier, dressier coaster: filled enamel inside a plated rim. Built for hotel, "
               "private-club and premium hospitality programmes.",
         build="Brass or zinc alloy body · filled enamel face · gold-tone plated rim · felt base",
         options="Pantone-matched enamel · engraved rim · rigid boxed sets",
         tags=["Enamel", "Gold rim", "Boxed set"]),
    dict(key="coaster-acrylic", en="Acrylic Print Coasters", cn="亞加力印花杯墊",
         group="bar",
         blurb="Artwork sealed inside cast acrylic, so illustration and colour stay sharp. The natural "
               "companion to an acrylic keychain range in the same artist series.",
         build="Cast acrylic block · embedded full-colour print · polished edges",
         options="Hexagon, round or square · single or set · matching pins and keychains",
         tags=["Acrylic", "Embedded print", "Sets"]),
    dict(key="flask", en="Insulated Flasks & Drinkware", cn="保溫瓶及飲品器具",
         group="bar",
         blurb="Double-wall stainless drinkware in a matte finish. The higher-ticket item in most "
               "corporate gift sets, and the one people actually keep using.",
         build="Stainless steel · double-wall vacuum construction · powder-coat or matte finish",
         options="Laser engraving or full-wrap print · capacity options · rigid gift box",
         tags=["Stainless", "Vacuum", "Matte"]),
]
BY_KEY = {s["key"]: s for s in SERIES}

GROUPS = [
    dict(key="badges", en="Badges, Pins & Keychains", cn="襟章 · 匙扣",
         desc="Small-format identity pieces — enamel pins, acrylic charms and everything a brand hands "
              "out in volume.", hero=("lapel-pin", 2), members=["lapel-pin", "keychain"]),
    dict(key="desk", en="Desk & Personal", cn="桌上 · 個人配飾",
         desc="Pens, tie clips and bookmarks: considered objects for executive gifting, awards and "
              "long-service recognition.", hero=("pen", 4), members=["tie-clip", "pen", "bookmark"]),
    dict(key="bar", en="Barware, Coasters & Drinkware", cn="酒具 · 杯墊 · 飲品器具",
         desc="Openers, coasters and insulated drinkware for hospitality, retail and premium gift sets.",
         hero=("coaster-enamel", 5), members=["bottle-opener", "coaster-metal", "coaster-enamel",
                                              "coaster-acrylic", "flask"]),
]

NAV = [
    ("index.html", "Home", "首頁"),
    ("products.html", "Products", "產品"),
    ("showcase.html", "Showcase", "設計樣本"),
    ("about.html", "About", "關於我們"),
    ("partnership.html", "Partnership", "商業合作"),
    ("contact.html", "Contact", "聯絡我們"),
]


def img(series, n, sm=False):
    """Return the src for photo n (1-based) of a series."""
    item = MAN[series][n - 1]
    return item["sm"] if sm else item["full"]


def head(title, desc, page):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>
{nav(page)}
<main id="main">"""


def nav(page):
    links = "".join(
        f'\n        <a class="navlink" href="{h}"{" aria-current=page" if h == page else ""}>'
        f'<span>{en}</span><span class="cn">{cn}</span></a>'
        for h, en, cn in NAV)
    return f"""<header class="topnav">
  <div class="container topnav-inner">
    <a class="brand" href="index.html" aria-label="Koon Wing Product — home">
      <img src="assets/img/logo-mark.svg" alt="" width="38" height="38">
      <span class="brand-txt"><span class="mark">KOON WING</span><br><span class="sub">PRODUCT</span></span>
    </a>
    <button class="navtoggle" type="button" aria-expanded="false" aria-label="Menu">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18" stroke-linecap="round"/></svg>
    </button>
    <nav aria-label="Main">{links}
      <a class="btn btn-primary nav-cta" href="contact.html">Request a Quote</a>
    </nav>
  </div>
</header>"""


FOOT_PROD = "".join(
    f'<li><a href="products.html#{s["key"]}">{s["en"]}</a></li>' for s in SERIES[:5])

FOOTER = f"""</main>
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <img class="flogo" src="assets/img/logo-lockup-light.svg" alt="Koon Wing Product" width="200" height="78">
        <p class="about">Custom metal and plastic gifts, designed and managed from Hong Kong —
          from first sketch to boxed delivery.</p>
      </div>
      <div>
        <h4>Products</h4>
        <ul>{FOOT_PROD}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About us 關於我們</a></li>
          <li><a href="showcase.html">Design samples 設計樣本</a></li>
          <li><a href="partnership.html">Partnership 商業合作</a></li>
          <li><a href="contact.html">Contact 聯絡我們</a></li>
        </ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul>
          <li>{TBC}</li>
          <li>Hong Kong</li>
        </ul>
      </div>
    </div>
    <div class="footer-base">
      <span>© 2026 Koon Wing Product. All rights reserved.</span>
      <span>Hong Kong · 香港</span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
"""


def cta(title, cn, body):
    return f"""<section class="section">
  <div class="container">
    <div class="cta">
      <div>
        <h2>{title}</h2>
        <p class="cn-sub" style="color:var(--accent-hi)">{cn}</p>
        <p>{body}</p>
      </div>
      <div class="btn-row" style="margin:0">
        <a class="btn btn-gold" href="contact.html">Request a Quote</a>
        <a class="btn btn-ghost" style="border-color:rgba(255,255,255,.3);color:#fff" href="products.html">See products</a>
      </div>
    </div>
  </div>
</section>"""


ICONS = {
    "pencil": '<path d="M4 20h4L20 8a2.8 2.8 0 0 0-4-4L4 16v4Z"/>',
    "layers": '<path d="M12 3 3 8l9 5 9-5-9-5Z"/><path d="M3 14l9 5 9-5"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "box": '<path d="M3 8v9l9 4 9-4V8l-9-4-9 4Z"/><path d="M3 8l9 4 9-4"/><path d="M12 12v9"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01" stroke-linecap="round"/>',
}


def feat(icon, h, cn, p):
    return f"""<div class="feat">
      <svg class="ico" viewBox="0 0 24 24" aria-hidden="true">{ICONS[icon]}</svg>
      <h3>{h}</h3><p class="cn-sub" style="margin:0">{cn}</p><p>{p}</p>
    </div>"""


STEPS = [
    ("01", "Brief &amp; concept", "接洽與概念", "You send a sketch, a reference sample or just a budget and a "
     "deadline. We come back with formats that fit."),
    ("02", "Design &amp; artwork", "設計與圖稿", "Artwork is drawn up to production spec — line weights, enamel "
     "separations, plating and engraving areas."),
    ("03", "Tooling &amp; sample", "開模與打樣", "Tooling is cut and a physical pre-production sample is sent "
     "for your written sign-off before anything runs."),
    ("04", "Production &amp; QC", "生產與品檢", "The approved sample is the reference. Goods are inspected "
     "against it before they leave the factory."),
    ("05", "Packing &amp; delivery", "包裝與交付", "Boxed, cartoned and shipped to Hong Kong or direct to your "
     "market, with the paperwork your side needs."),
]


def steps_html():
    return "".join(
        f'<div class="step"><span class="n">STEP {n}</span><h3>{h}</h3>'
        f'<p class="cn-sub" style="margin:4px 0 0">{cn}</p><p>{p}</p></div>'
        for n, h, cn, p in STEPS)


# ─────────────────────────────────────────────────────── HOME
def page_home():
    cards = ""
    for g in GROUPS:
        s, n = g["hero"]
        cards += f"""
      <a class="card" href="products.html#{g['members'][0]}">
        <div class="card-media"><img src="{img(s, n, True)}" alt="{g['en']}" loading="lazy" width="760" height="570"></div>
        <div class="card-body">
          <span class="card-idx">{g['key'].upper()}</span>
          <h3>{g['en']}</h3>
          <p class="cn-sub" style="margin:0">{g['cn']}</p>
          <p>{g['desc']}</p>
          <div class="tags">{"".join(f'<span class="tag">{BY_KEY[m]["en"]}</span>' for m in g['members'])}</div>
        </div>
      </a>"""

    strip = "".join(
        f'<a href="showcase.html" class="shot" style="display:block">'
        f'<img src="{img(k, n, True)}" alt="{BY_KEY[k]["en"]}" loading="lazy" width="760" height="570"></a>'
        for k, n in [("lapel-pin", 6), ("bookmark", 4), ("coaster-acrylic", 3),
                     ("flask", 5), ("bottle-opener", 2), ("tie-clip", 1),
                     ("coaster-metal", 4), ("keychain", 3)])

    return head("Koon Wing Product · Custom Metal &amp; Plastic Gifts, Hong Kong",
                "Hong Kong design and production house for custom metal and plastic gifts — enamel pins, "
                "keychains, coasters, drinkware and desk pieces. Design to boxed delivery.",
                "index.html") + f"""
<section class="hero">
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">Custom gifts · Hong Kong</p>
      <h1>Objects people<br>actually <span>keep.</span></h1>
      <p class="cn-sub" style="font-size:16px;letter-spacing:.18em">訂製金屬及塑膠禮品 · 由設計到出貨</p>
      <p class="lead">Koon Wing Product designs and produces custom metal and plastic gifts from Hong Kong —
        enamel pins, acrylic charms, coasters, barware and desk pieces. You bring the brand and the deadline;
        we handle artwork, tooling, sampling, production and packing.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="contact.html">Request a Quote</a>
        <a class="btn btn-ghost" href="showcase.html">See design samples →</a>
      </div>
      <div class="hero-meta">
        <span>Metal · Enamel · Acrylic</span><span>Design to delivery</span><span>Based in Hong Kong</span>
      </div>
    </div>
    <figure class="hero-figure" style="margin:0">
      <img src="{img('lapel-pin', 3)}" alt="Enamel lapel pin presented in a gift box"
           width="1400" height="1050" fetchpriority="high">
    </figure>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">What we make</p>
      <h2>Three families,<br>one production standard.</h2>
      <p class="cn-sub">三大產品系列 · 同一生產標準</p>
      <p class="lead">Most programmes are built from these formats — on their own, or combined into a
        matched gift set that shares one artwork and one finish.</p>
    </div>
    <div class="grid-3">{cards}
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Why Koon Wing</p>
      <h2>Small enough to answer,<br>organised enough to deliver.</h2>
      <p class="cn-sub">回應快 · 交付穩</p>
    </div>
    <div class="grid-4">
      {feat("pencil", "Design done here", "香港設計", "Artwork and structural design are handled in Hong Kong, in your timezone, in English or Chinese.")}
      {feat("layers", "Vetted production partners", "合作工廠生產", "We do not run a factory. We place work with specialist manufacturers and stay accountable for the result.")}
      {feat("check", "Sample before production", "先打樣後生產", "Nothing runs until you have approved a physical pre-production sample in writing.")}
      {feat("box", "Packed the way you sell it", "連包裝交付", "Retail boxing, gift sets and outer cartons are specified with the product, not bolted on afterwards.")}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">How we work</p>
      <h2>From sketch to packed carton.</h2>
      <p class="cn-sub">由概念到出貨 · 五個階段</p>
    </div>
    <div class="steps">{steps_html()}</div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head" style="margin-bottom:var(--gap-lg)">
      <p class="eyebrow">Design samples</p>
      <h2>What the finishes look like.</h2>
      <p class="cn-sub">成品效果一覽</p>
      <p class="lead">A selection of design samples produced to show materials, plating and packaging
        options. These are demonstration pieces, not client work.</p>
    </div>
    <div class="gallery" style="grid-template-columns:repeat(auto-fill,minmax(190px,1fr))">{strip}</div>
    <div class="btn-row"><a class="btn btn-ghost" href="showcase.html">View all samples →</a></div>
  </div>
</section>

{cta("Tell us what you need made.", "告訴我們您想製作的產品",
     "Send a sketch, a reference photo or a rough spec. We will come back with formats, "
     "finishes and an indicative quotation.")}
""" + FOOTER


# ─────────────────────────────────────────────────────── PRODUCTS
def page_products():
    rows = ""
    for i, s in enumerate(SERIES):
        n = len(MAN[s["key"]])
        pics = [1, 2, 3] if n >= 3 else list(range(1, n + 1))
        media = "".join(
            f'<img src="{img(s["key"], p, True)}" alt="{s["en"]} — view {p}" loading="lazy" width="760" height="570">'
            for p in pics)
        rev = " rev" if i % 2 else ""
        rows += f"""
    <article class="prow{rev}" id="{s['key']}">
      <div class="prow-media">{media}</div>
      <div class="prow-body">
        <p class="eyebrow">{i + 1:02d} · {s['group'].upper()}</p>
        <h2 style="font-size:clamp(24px,2.6vw,34px)">{s['en']}</h2>
        <p class="cn-sub">{s['cn']}</p>
        <p class="lead" style="font-size:16px;margin-top:var(--gap-md)">{s['blurb']}</p>
        <table class="spec" style="margin-top:var(--gap-md)">
          <tbody>
            <tr><th>Typical build 常用結構</th><td>{s['build']}</td></tr>
            <tr><th>Options 可選項</th><td>{s['options']}</td></tr>
            <tr><th>Order size 訂購量</th><td>Flexible — tell us your quantity and we will quote it</td></tr>
          </tbody>
        </table>
        <div class="btn-row"><a class="btn btn-ghost" href="contact.html">Quote this format →</a></div>
      </div>
    </article>"""

    return head("Products · Koon Wing Product",
                "Custom enamel pins, acrylic keychains, tie clips, metal pens, bookmarks, bottle openers, "
                "coasters and insulated drinkware.", "products.html") + f"""
<section class="pagehead">
  <div class="container">
    <p class="eyebrow">Our products</p>
    <h1>Ten formats we build most often.</h1>
    <p class="cn-sub" style="font-size:15px">我們的產品系列</p>
    <p class="lead">Each format below can be made to your artwork, your finish and your packaging.
      Specifications listed are the common build and the options available — final specification is
      confirmed on your sample before production.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="container">{rows}
  </div>
</section>
{cta("Not sure which format fits?", "不確定哪一款適合？",
     "Send us the budget, the quantity and who is receiving it. We will suggest two or three formats "
     "that work and quote them side by side.")}
""" + FOOTER


# ─────────────────────────────────────────────────────── SHOWCASE
def page_showcase():
    fbtns = '<button class="filter" data-filter="all" aria-pressed="true">All samples 全部</button>'
    fbtns += "".join(
        f'<button class="filter" data-filter="{s["key"]}" aria-pressed="false">{s["en"]}</button>'
        for s in SERIES)
    shots = ""
    for s in SERIES:
        for n in range(1, len(MAN[s["key"]]) + 1):
            shots += f"""
      <figure class="shot" data-series="{s['key']}" data-full="{img(s['key'], n)}"
              data-caption="{s['en']} 樣本 {n:02d}" tabindex="0" role="button"
              aria-label="Open {s['en']} sample {n:02d}">
        <img src="{img(s['key'], n, True)}" alt="{s['en']} design sample {n:02d}" loading="lazy" width="760" height="570">
        <figcaption>{s['en']} · {s['cn']}</figcaption>
      </figure>"""

    total = sum(len(MAN[s["key"]]) for s in SERIES)
    return head("Design Samples · Koon Wing Product",
                "Design samples showing materials, plating, enamel and packaging options across ten "
                "custom gift formats.", "showcase.html") + f"""
<section class="pagehead">
  <div class="container">
    <p class="eyebrow">Design samples</p>
    <h1>Finishes, materials<br>and packaging.</h1>
    <p class="cn-sub" style="font-size:15px">設計樣本</p>
    <p class="lead">{total} sample images across ten formats, produced to demonstrate what each material,
      plating and packaging option looks like in the hand.</p>
    <div class="notice" style="margin-top:var(--gap-lg);max-width:62ch">
      <svg viewBox="0 0 24 24" aria-hidden="true">{ICONS['info']}</svg>
      <p><strong>These are design samples, not client work.</strong> Any brand names, logos or packaging
        text visible in these images are illustrative only and do not represent real customers or orders.
        <span class="cn">此為設計樣本，圖中品牌名稱僅作示範用途，並非實際客戶個案。</span></p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:var(--gap-xl)">
  <div class="container">
    <div class="filters">{fbtns}</div>
    <div class="gallery">{shots}
    </div>
  </div>
</section>

<div class="lb" role="dialog" aria-modal="true" aria-label="Sample viewer">
  <button class="lb-btn lb-close" type="button" aria-label="Close">&times;</button>
  <button class="lb-btn lb-prev" type="button" aria-label="Previous">&#8249;</button>
  <img src="" alt="">
  <button class="lb-btn lb-next" type="button" aria-label="Next">&#8250;</button>
  <p class="lb-cap"></p>
</div>

{cta("Want a sample in your own branding?", "以貴公司品牌打樣",
     "We can produce a pre-production sample in your artwork and finish before you commit to a "
     "production run.")}
""" + FOOTER


# ─────────────────────────────────────────────────────── ABOUT
def page_about():
    return head("About · Koon Wing Product",
                "Koon Wing Product is a Hong Kong design and sourcing house for custom metal and plastic "
                "gifts.", "about.html") + f"""
<section class="pagehead">
  <div class="container">
    <p class="eyebrow">About us</p>
    <h1>A Hong Kong design<br>and sourcing house.</h1>
    <p class="cn-sub" style="font-size:15px">關於我們</p>
  </div>
</section>

<section class="section">
  <div class="container grid-2" style="align-items:start;gap:clamp(28px,5vw,72px)">
    <div>
      <h2 style="font-size:clamp(24px,2.8vw,34px)">What we do</h2>
      <p class="cn-sub">我們的業務</p>
      <p class="lead" style="margin-top:var(--gap-md)">Koon Wing Product takes a brand's idea for a
        physical gift and carries it through to boxed, delivered goods. That means artwork prepared to
        production spec, tooling cut, a physical sample approved, production placed with the right
        specialist factory, and quality checked against the approved sample before shipping.</p>
      <p class="lead" style="margin-top:var(--gap-md)">We are deliberately direct about the model:
        <strong>we do not own a factory.</strong> We design and manage in Hong Kong, and we place
        production with manufacturing partners in mainland China who specialise in the exact process a
        piece needs — die-striking and enamelling are not the same trade as acrylic casting or vacuum
        drinkware. Being independent of any single plant is what lets us put a job where it will come
        out best, rather than where it happens to fit.</p>
    </div>
    <div>
      <figure style="margin:0">
        <img src="{img('bookmark', 4)}" alt="Etched metal bookmark detail"
             style="border-radius:var(--radius-lg);width:100%" loading="lazy" width="1400" height="1050">
      </figure>
      <table class="spec" style="margin-top:var(--gap-lg)">
        <tbody>
          <tr><th>Based in</th><td>Hong Kong 香港</td></tr>
          <tr><th>Model</th><td>Design and project management in Hong Kong; production placed with partner factories</td></tr>
          <tr><th>Materials</th><td>Zinc alloy, brass, stainless steel, aluminium, cast acrylic, wood</td></tr>
          <tr><th>Processes</th><td>Die-striking, die-casting, enamelling, plating, photo-etching, laser engraving, UV print</td></tr>
          <tr><th>Order sizes</th><td>Flexible — quoted per project</td></tr>
          <tr><th>Working languages</th><td>English · 繁體中文 · 普通話</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">How we work</p>
      <h2>Five stages, one approved sample.</h2>
      <p class="cn-sub">五個階段 · 一個確認樣本</p>
      <p class="lead">The approved physical sample is the contract. Everything produced afterwards is
        checked against it, which is what stops the familiar problem of goods arriving a shade off, a
        gram light, or in the wrong box.</p>
    </div>
    <div class="steps">{steps_html()}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Straight answers</p>
      <h2>What you should ask us.</h2>
      <p class="cn-sub">您應該向我們查證的事</p>
    </div>
    <div class="grid-3">
      <div class="feat"><h3>“Do you make it yourselves?”</h3>
        <p class="cn-sub" style="margin:0">「產品是你們自己生產的嗎？」</p>
        <p>No. We design and manage; specialist partner factories produce. We stay responsible for the
          spec, the sample and the inspection.</p></div>
      <div class="feat"><h3>“What is the minimum order?”</h3>
        <p class="cn-sub" style="margin:0">「最低訂購量是多少？」</p>
        <p>It depends entirely on the format and the tooling involved. Tell us the quantity you actually
          want and we will tell you honestly whether it is workable.</p></div>
      <div class="feat"><h3>“Are those your clients in the photos?”</h3>
        <p class="cn-sub" style="margin:0">「相片中的是你們的客戶嗎？」</p>
        <p>No. Every brand name shown on this site is an illustrative design sample, produced to
          demonstrate finishes. We will not claim work we have not done.</p></div>
    </div>
  </div>
</section>

{cta("Start with a conversation.", "由一次洽談開始",
     "No forms to fill in first. Send what you have — a sketch, a photo, a budget — and we will tell "
     "you what is realistic.")}
""" + FOOTER


# ─────────────────────────────────────────────────────── PARTNERSHIP
def page_partnership():
    return head("Business Partnerships · Koon Wing Product",
                "OEM and ODM custom gift production, private label programmes, corporate gifting and "
                "retail supply from Hong Kong.", "partnership.html") + f"""
<section class="pagehead">
  <div class="container">
    <p class="eyebrow">Business partnerships</p>
    <h1>Ways of working<br>together.</h1>
    <p class="cn-sub" style="font-size:15px">商業合作機會</p>
    <p class="lead">Whether you need one gift for one campaign or an ongoing range carrying your own
      label, the process is the same — the difference is how much of it you want to own.</p>
  </div>
</section>

<section class="section">
  <div class="container grid-3">
    <div class="card"><div class="card-media"><img src="{img('lapel-pin', 5, True)}" alt="Enamel pins" loading="lazy" width="760" height="570"></div>
      <div class="card-body"><span class="card-idx">01 · OEM</span><h3>Make to your design</h3>
        <p class="cn-sub" style="margin:0">按你的設計生產</p>
        <p>You supply the artwork or CAD. We prepare it to production spec, tool it, sample it and run it.
          You own the design and the tooling.</p></div></div>
    <div class="card"><div class="card-media"><img src="{img('coaster-acrylic', 6, True)}" alt="Acrylic coasters" loading="lazy" width="760" height="570"></div>
      <div class="card-body"><span class="card-idx">02 · ODM</span><h3>Design it with you</h3>
        <p class="cn-sub" style="margin:0">共同設計開發</p>
        <p>You bring a brand and a brief; we develop the object — format, materials, finish and packaging —
          and take it through to production.</p></div></div>
    <div class="card"><div class="card-media"><img src="{img('flask', 1, True)}" alt="Insulated flask" loading="lazy" width="760" height="570"></div>
      <div class="card-body"><span class="card-idx">03 · Private label</span><h3>Your label, our range</h3>
        <p class="cn-sub" style="margin:0">自有品牌供貨</p>
        <p>Take formats we already build and carry them under your own brand and packaging for retail or
          continuity programmes.</p></div></div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Who this suits</p>
      <h2>Buyers we are built for.</h2>
    </div>
    <div class="grid-4">
      {feat("box", "Corporate gifting", "企業禮品", "Staff recognition, client gifts, conference and anniversary programmes needing one coherent set.")}
      {feat("pencil", "Brands &amp; creators", "品牌與創作者", "Artist series, merchandise drops and brand collectibles where artwork fidelity matters.")}
      {feat("layers", "Retail &amp; hospitality", "零售與款待業", "Coasters, barware and drinkware produced to a retail finish, boxed ready to sell.")}
      {feat("check", "Agencies &amp; event planners", "代理與活動策劃", "One point of contact who will give you a straight timeline instead of an optimistic one.")}
    </div>
  </div>
</section>

<section class="section">
  <div class="container grid-2" style="gap:clamp(28px,5vw,72px);align-items:start">
    <div>
      <p class="eyebrow">What we need from you</p>
      <h2 style="font-size:clamp(24px,2.8vw,34px)">Four things get you a quote.</h2>
      <p class="cn-sub">報價所需的四項資料</p>
      <table class="spec" style="margin-top:var(--gap-lg)">
        <tbody>
          <tr><th>1 · The object</th><td>A format, a sketch, or a reference photo of something similar</td></tr>
          <tr><th>2 · The quantity</th><td>The number you actually want — not a rounded-up guess</td></tr>
          <tr><th>3 · The deadline</th><td>The date it must be in hand, and where in the world that is</td></tr>
          <tr><th>4 · The budget</th><td>A per-unit ceiling, so we specify to it instead of around it</td></tr>
        </tbody>
      </table>
      <div class="btn-row"><a class="btn btn-primary" href="contact.html">Send an enquiry</a></div>
    </div>
    <div>
      <p class="eyebrow">What you get back</p>
      <h2 style="font-size:clamp(24px,2.8vw,34px)">A spec, a price and a real date.</h2>
      <p class="cn-sub">規格、價格與實際交期</p>
      <p class="lead" style="margin-top:var(--gap-md)">A written specification of the piece as we would
        build it, an indicative unit price at your quantity, the tooling cost if any, and a production
        timeline with the sampling stage shown separately — because that is the stage that usually moves.</p>
      <p class="lead" style="margin-top:var(--gap-md)">If your quantity or deadline is not workable, we
        will say so at that point rather than after you have paid a deposit.</p>
    </div>
  </div>
</section>

{cta("Let's scope your programme.", "共同規劃您的項目",
     "Tell us the object, the quantity, the deadline and the budget. You will get a specification and "
     "an indicative price back.")}
""" + FOOTER


# ─────────────────────────────────────────────────────── CONTACT
def page_contact():
    opts = "".join(f'<option>{s["en"]}</option>' for s in SERIES)
    return head("Contact · Koon Wing Product",
                "Request a quotation for custom metal and plastic gifts from Koon Wing Product, Hong Kong.",
                "contact.html") + f"""
<section class="pagehead">
  <div class="container">
    <p class="eyebrow">Contact us</p>
    <h1>Tell us what<br>you need made.</h1>
    <p class="cn-sub" style="font-size:15px">聯絡我們</p>
    <p class="lead">The more of the four basics you can give us — object, quantity, deadline, budget —
      the more useful the first reply will be.</p>
  </div>
</section>

<section class="section">
  <div class="container grid-2" style="gap:clamp(28px,5vw,72px);align-items:start">
    <div>
      <h2 style="font-size:clamp(22px,2.4vw,30px)">Send an enquiry</h2>
      <p class="cn-sub">提交查詢</p>
      <p class="form-note" style="margin-top:var(--gap-sm)">Fields marked <em style="color:var(--accent);font-style:normal">*</em> are required.</p>
      <form action="#" method="post" novalidate>
        <div class="grid-2" style="gap:var(--gap-md)">
          <div class="field"><label for="name">Name 姓名 <em>*</em></label>
            <input id="name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="company">Company 公司</label>
            <input id="company" name="company" type="text" autocomplete="organization"></div>
        </div>
        <div class="grid-2" style="gap:var(--gap-md)">
          <div class="field"><label for="email">Email 電郵 <em>*</em></label>
            <input id="email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="phone">Phone / WhatsApp 電話</label>
            <input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel"></div>
        </div>
        <div class="grid-2" style="gap:var(--gap-md)">
          <div class="field"><label for="product">Product format 產品類別</label>
            <select id="product" name="product"><option>Not sure yet — advise me</option>{opts}</select></div>
          <div class="field"><label for="qty">Quantity 數量</label>
            <input id="qty" name="qty" type="text" inputmode="numeric" placeholder="e.g. 500"></div>
        </div>
        <div class="field"><label for="deadline">Date needed in hand 到貨日期</label>
          <input id="deadline" name="deadline" type="text" placeholder="e.g. mid-November, Hong Kong"></div>
        <div class="field"><label for="msg">What are you making? 產品內容 <em>*</em></label>
          <textarea id="msg" name="msg" required
            placeholder="Describe the piece, or paste a reference link. Budget per unit is helpful."></textarea></div>
        <button class="btn btn-primary" type="submit">Send enquiry</button>
        <p class="form-note" style="margin-top:var(--gap-md)">
          <strong>Note:</strong> this form is not connected yet — the receiving address and mail service
          still need to be set up before launch.</p>
      </form>
    </div>

    <div>
      <h2 style="font-size:clamp(22px,2.4vw,30px)">Direct</h2>
      <p class="cn-sub">直接聯絡</p>
      <table class="spec" style="margin-top:var(--gap-md)">
        <tbody>
          <tr><th>Email 電郵</th><td>{TBC}</td></tr>
          <tr><th>Phone 電話</th><td>{TBC}</td></tr>
          <tr><th>WhatsApp</th><td>{TBC}</td></tr>
          <tr><th>Address 地址</th><td>Hong Kong 香港<br><span class="tbc">Full address to be confirmed 詳細地址待確認</span></td></tr>
          <tr><th>Hours 辦公時間</th><td>Monday – Friday, Hong Kong time</td></tr>
        </tbody>
      </table>
      <figure style="margin:var(--gap-xl) 0 0">
        <img src="{img('lapel-pin', 1)}" alt="Enamel lapel pin on slate"
             style="border-radius:var(--radius-lg);width:100%" loading="lazy" width="1400" height="1050">
      </figure>
    </div>
  </div>
</section>
""" + FOOTER


PAGES = {
    "index.html": page_home,
    "products.html": page_products,
    "showcase.html": page_showcase,
    "about.html": page_about,
    "partnership.html": page_partnership,
    "contact.html": page_contact,
}

for fn, gen in PAGES.items():
    html = gen()
    with io.open(os.path.join(SITE, fn), "w", encoding="utf-8") as f:
        f.write(html)
    print(fn, len(html))
