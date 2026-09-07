# -*- coding: utf-8 -*-
"""Generate the Koon Wing Product site in two languages.

English pages sit at the root; Chinese pages sit under zh/.
Every string is defined once as an (en, zh) pair — there is no page that
carries content in one language and headings in the other.
"""
import json, os, io

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAN = json.load(open(os.path.join(SITE, "assets", "manifest.json")))

LANG = "en"          # flipped by the render loop at the bottom


def t(en, zh):
    """Pick the string for the language being rendered."""
    return en if LANG == "en" else zh


def o(en, zh):
    """The *other* language — used for the small secondary line under a heading."""
    return zh if LANG == "en" else en


def A():
    """Prefix for assets: Chinese pages live one directory down."""
    return "" if LANG == "en" else "../"


# ── product series ─────────────────────────────────────────────────────────
SERIES = [
    dict(key="lapel-pin", group="badges",
         en=dict(name="Enamel Lapel Pins",
                 blurb="Die-struck or die-cast pins finished in soft or hard enamel. The format most "
                       "corporate programmes start with — small, giftable, and instantly recognisable "
                       "on a jacket.",
                 build="Zinc alloy or brass base · soft / hard enamel · polished gold, nickel or black plating",
                 options="Butterfly clutch, magnetic back, rubber back or safety pin · individual boxing · custom shape",
                 tags=["Enamel", "Die-struck", "Plated"]),
         zh=dict(name="琺瑯襟章",
                 blurb="以衝壓或壓鑄製成，配軟琺瑯或硬琺瑯。多數企業禮品計劃都由此入手——體積小、方便贈送，"
                       "別在西裝上一眼就認得出。",
                 build="鋅合金或黃銅底材 · 軟／硬琺瑯 · 拋光金色、鎳色或黑色電鍍",
                 options="蝴蝶扣、磁扣、膠扣或安全針 · 獨立盒裝 · 可訂製形狀",
                 tags=["琺瑯", "衝壓", "電鍍"])),
    dict(key="keychain", group="badges",
         en=dict(name="Acrylic Keychains",
                 blurb="Clear acrylic charms with full-colour artwork printed through. Suits "
                       "illustration-led brands, artist series and event merchandise where colour "
                       "matters more than metal.",
                 build="Cast acrylic 3 mm · full-colour UV print · optional epoxy dome",
                 options="Split ring, lobster clasp or ball chain · single charm or matched sets · printed backer card",
                 tags=["Acrylic", "UV print", "Full colour"]),
         zh=dict(name="亞加力匙扣",
                 blurb="透明亞加力配全彩內印圖案。適合以插畫為主的品牌、藝術家系列及活動紀念品——"
                       "重點在色彩表現，而非金屬質感。",
                 build="鑄造亞加力 3 毫米 · 全彩 UV 印刷 · 可加環氧樹脂面層",
                 options="圈扣、龍蝦扣或珠鏈 · 單件或成套 · 可配印刷卡紙",
                 tags=["亞加力", "UV 印刷", "全彩"])),
    dict(key="tie-clip", group="desk",
         en=dict(name="Tie Clips & Formal Accessories",
                 blurb="Weighted formal accessories for executive gifting, long-service awards and "
                       "hospitality uniforms. Engraving keeps the piece quiet enough to wear every day.",
                 build="Stainless steel or brass · polished, brushed or PVD finish",
                 options="Laser or diamond-drag engraving · enamel inlay · velvet-lined presentation box",
                 tags=["Steel", "Engraved", "Boxed"]),
         zh=dict(name="領帶夾及禮儀配飾",
                 blurb="具重量感的正裝配飾，適用於高層贈禮、長期服務獎項及款待業制服。"
                       "以刻字處理，低調得足以日常配戴。",
                 build="不鏽鋼或黃銅 · 拋光、拉絲或 PVD 電鍍",
                 options="鐳射或鑽石刻字 · 琺瑯鑲嵌 · 絨面禮盒",
                 tags=["不鏽鋼", "刻字", "盒裝"])),
    dict(key="pen", group="desk",
         en=dict(name="Metal Ball Pens",
                 blurb="A weighted metal pen is still the most-used corporate gift there is. Soft-touch "
                       "barrels hold branding cleanly and feel more considered than a printed plastic body.",
                 build="Brass barrel · soft-touch or lacquer coating · chrome trim · standard refill",
                 options="Laser engraving or pad printing · gift box or sleeve · matched notebook sets",
                 tags=["Brass", "Soft-touch", "Engraved"]),
         zh=dict(name="金屬原子筆",
                 blurb="有重量的金屬筆，至今仍是使用率最高的企業禮品。柔觸筆桿印上品牌後效果乾淨，"
                       "比塑膠印刷筆身考究得多。",
                 build="黃銅筆桿 · 柔觸或漆面塗層 · 鉻色配件 · 標準筆芯",
                 options="鐳射刻字或移印 · 禮盒或紙套 · 可配套筆記本",
                 tags=["黃銅", "柔觸", "刻字"])),
    dict(key="bookmark", group="desk",
         en=dict(name="Filigree Metal Bookmarks",
                 blurb="Photo-etched openwork in plated metal, finished with a silk tassel. A low-cost, "
                       "high-perceived-value piece for museums, publishers and cultural programmes.",
                 build="Photo-etched stainless steel or brass · gold or rose-gold plating · silk tassel",
                 options="Custom pattern from your artwork · bead colour matching · paper or fabric gift box",
                 tags=["Etched", "Plated", "Tassel"]),
         zh=dict(name="金屬鏤空書籤",
                 blurb="以蝕刻製成的鏤空圖案，加電鍍及絲質流蘇。成本不高但觀感貴重，"
                       "適合博物館、出版社及文化機構。",
                 build="蝕刻不鏽鋼或黃銅 · 金色或玫瑰金電鍍 · 絲質流蘇",
                 options="可依您的圖稿開版 · 配珠顏色可選 · 紙盒或布盒",
                 tags=["蝕刻", "電鍍", "流蘇"])),
    dict(key="bottle-opener", group="bar",
         en=dict(name="Bottle Openers",
                 blurb="Wood-and-metal openers built for craft drinks brands, bars and hospitality "
                       "gifting — the kind of object that stays on a counter rather than in a drawer.",
                 build="Beech or walnut handle · cast metal head · enamel badge inlay",
                 options="Branded badge or engraved handle · kraft, wood or rigid gift box",
                 tags=["Wood", "Cast metal", "Badge"]),
         zh=dict(name="開瓶器",
                 blurb="木配金屬的開瓶器，為精釀飲品品牌、酒吧及款待業贈禮而設——"
                       "屬於會留在檯面、而不是收進抽屜的那種物件。",
                 build="櫸木或胡桃木手柄 · 鑄造金屬頭部 · 琺瑯徽章鑲嵌",
                 options="品牌徽章或手柄刻字 · 牛皮紙盒、木盒或硬盒",
                 tags=["木材", "鑄造金屬", "徽章"])),
    dict(key="coaster-metal", group="bar",
         en=dict(name="Brushed Metal Coasters",
                 blurb="Spun aluminium coasters with a brushed face and a soft base. Reads as product, "
                       "not merchandise — suited to specialty coffee, spirits and design-led retail.",
                 build="Spun aluminium · brushed and anodised face · cork or felt base",
                 options="Enamel or printed centre · single or boxed set of four · printed outer carton",
                 tags=["Aluminium", "Brushed", "Cork base"]),
         zh=dict(name="拉絲金屬杯墊",
                 blurb="旋壓鋁製杯墊，表面拉絲、底部加軟墊。觀感像產品而非贈品，"
                       "適合精品咖啡、烈酒及設計主導的零售品牌。",
                 build="旋壓鋁材 · 拉絲陽極氧化表面 · 軟木或絨底",
                 options="琺瑯或印刷中心圖案 · 單件或四件禮盒 · 可印外盒",
                 tags=["鋁材", "拉絲", "軟木底"])),
    dict(key="coaster-enamel", group="bar",
         en=dict(name="Gold-Rim Enamel Coasters",
                 blurb="A heavier, dressier coaster: filled enamel inside a plated rim. Built for hotel, "
                       "private-club and premium hospitality programmes.",
                 build="Brass or zinc alloy body · filled enamel face · gold-tone plated rim · felt base",
                 options="Pantone-matched enamel · engraved rim · rigid boxed sets",
                 tags=["Enamel", "Gold rim", "Boxed set"]),
         zh=dict(name="金邊琺瑯杯墊",
                 blurb="更厚重、更講究的一款杯墊：電鍍外框內填琺瑯。為酒店、私人會所及"
                       "高端款待業計劃而設。",
                 build="黃銅或鋅合金主體 · 填充琺瑯面 · 金色電鍍外框 · 絨底",
                 options="可依 Pantone 配色 · 外框刻字 · 硬盒成套",
                 tags=["琺瑯", "金邊", "成套"])),
    dict(key="coaster-acrylic", group="bar",
         en=dict(name="Acrylic Print Coasters",
                 blurb="Artwork sealed inside cast acrylic, so illustration and colour stay sharp. The "
                       "natural companion to an acrylic keychain range in the same artist series.",
                 build="Cast acrylic block · embedded full-colour print · polished edges",
                 options="Hexagon, round or square · single or set · matching pins and keychains",
                 tags=["Acrylic", "Embedded print", "Sets"]),
         zh=dict(name="亞加力印花杯墊",
                 blurb="圖案封存於鑄造亞加力之中，插畫與色彩得以維持銳利。"
                       "與同一藝術家系列的亞加力匙扣天然配套。",
                 build="鑄造亞加力磚 · 內嵌全彩印刷 · 拋光邊",
                 options="六角、圓形或方形 · 單件或成套 · 可配同款襟章與匙扣",
                 tags=["亞加力", "內嵌印刷", "成套"])),
    dict(key="flask", group="bar",
         en=dict(name="Insulated Flasks & Drinkware",
                 blurb="Double-wall stainless drinkware in a matte finish. The higher-ticket item in "
                       "most corporate gift sets, and the one people actually keep using.",
                 build="Stainless steel · double-wall vacuum construction · powder-coat or matte finish",
                 options="Laser engraving or full-wrap print · capacity options · rigid gift box",
                 tags=["Stainless", "Vacuum", "Matte"]),
         zh=dict(name="保溫瓶及飲品器具",
                 blurb="雙層不鏽鋼飲品器具，啞面處理。屬企業禮盒中單價較高的一件，"
                       "亦是最多人真正持續使用的一件。",
                 build="不鏽鋼 · 雙層真空結構 · 粉末塗層或啞面處理",
                 options="鐳射刻字或全身印刷 · 多種容量 · 硬盒包裝",
                 tags=["不鏽鋼", "真空", "啞面"])),
]
BY_KEY = {s["key"]: s for s in SERIES}


def sname(s):
    return s[LANG]["name"]


GROUPS = [
    dict(key="badges", hero=("lapel-pin", 2), members=["lapel-pin", "keychain"],
         en=dict(name="Badges, Pins & Keychains",
                 desc="Small-format identity pieces — enamel pins, acrylic charms and everything a "
                      "brand hands out in volume."),
         zh=dict(name="襟章 · 匙扣",
                 desc="小型的品牌識別產品——琺瑯襟章、亞加力吊飾，以及一切需要大量派發的物件。")),
    dict(key="desk", hero=("pen", 4), members=["tie-clip", "pen", "bookmark"],
         en=dict(name="Desk & Personal",
                 desc="Pens, tie clips and bookmarks: considered objects for executive gifting, awards "
                      "and long-service recognition."),
         zh=dict(name="桌上 · 個人配飾",
                 desc="原子筆、領帶夾與書籤：適合高層贈禮、獎項及長期服務表揚的精緻物件。")),
    dict(key="bar", hero=("coaster-enamel", 5),
         members=["bottle-opener", "coaster-metal", "coaster-enamel", "coaster-acrylic", "flask"],
         en=dict(name="Barware, Coasters & Drinkware",
                 desc="Openers, coasters and insulated drinkware for hospitality, retail and premium "
                      "gift sets."),
         zh=dict(name="酒具 · 杯墊 · 飲品器具",
                 desc="開瓶器、杯墊與保溫器具，適用於款待業、零售及高級禮盒。")),
]

STEPS = [
    ("01", "Brief &amp; concept", "接洽與概念",
     "You send a sketch, a reference sample or just a budget and a deadline. We come back with "
     "formats that fit.",
     "您提供草圖、參考樣本，或只給預算與交期，我們回覆可行的產品形式。"),
    ("02", "Design &amp; artwork", "設計與圖稿",
     "Artwork is drawn up to production spec — line weights, enamel separations, plating and "
     "engraving areas.",
     "圖稿按生產規格繪製：線條粗幼、琺瑯分色、電鍍與刻字範圍。"),
    ("03", "Tooling &amp; sample", "開模與打樣",
     "Tooling is cut and a physical pre-production sample is sent for your written sign-off before "
     "anything runs.",
     "開模後寄出實物試產樣本，待您書面確認，才會進入生產。"),
    ("04", "Production &amp; QC", "生產與品檢",
     "The approved sample is the reference. Goods are inspected against it before they leave the "
     "factory.",
     "一切以確認樣本為準。貨品出廠前須逐項對辦檢查。"),
    ("05", "Packing &amp; delivery", "包裝與交付",
     "Boxed, cartoned and shipped to Macau, Hong Kong or direct to your market, with the "
     "side needs.",
     "裝盒、裝箱，運抵澳門、香港或直送目的地市場，並備齊您所需的文件。"),
]

NAV = [
    ("index.html", "Home", "首頁"),
    ("products.html", "Products", "產品"),
    ("showcase.html", "Showcase", "設計樣本"),
    ("about.html", "About", "關於我們"),
    ("partnership.html", "Partnership", "商業合作"),
    ("contact.html", "Contact", "聯絡我們"),
]

ICONS = {
    "pencil": '<path d="M4 20h4L20 8a2.8 2.8 0 0 0-4-4L4 16v4Z"/>',
    "layers": '<path d="M12 3 3 8l9 5 9-5-9-5Z"/><path d="M3 14l9 5 9-5"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "box": '<path d="M3 8v9l9 4 9-4V8l-9-4-9 4Z"/><path d="M3 8l9 4 9-4"/><path d="M12 12v9"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01" stroke-linecap="round"/>',
}


MAIL = '<a href="mailto:info@koonwingproduct.com.mo">info@koonwingproduct.com.mo</a>'


def TBC():
    return '<span class="tbc">%s</span>' % t("To be confirmed", "待確認")


def img(series, n, sm=False):
    item = MAN[series][n - 1]
    return A() + (item["sm"] if sm else item["full"])


def dim(series, n, sm=False):
    """Real intrinsic size — a wrong height attribute stretches the image."""
    item = MAN[series][n - 1]
    return (item["sw"], item["sh"]) if sm else (item["w"], item["h"])


def head(title, desc, page):
    lang = t("en", "zh-Hant")
    alt_en = ("" if LANG == "en" else "../") + page
    alt_zh = ("zh/" if LANG == "en" else "") + page
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="zh-Hant" href="{alt_zh}">
<link rel="icon" href="{A()}assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{A()}assets/css/style.css">
</head>
<body>
<a class="sr-only" href="#main">{t("Skip to content", "跳至內容")}</a>
{nav(page)}
<main id="main">"""


def nav(page):
    links = "".join(
        f'\n        <a class="navlink" href="{h}"{" aria-current=page" if h == page else ""}>'
        f'<span>{t(en, zh)}</span></a>'
        for h, en, zh in NAV)
    switch_href = ("zh/" + page) if LANG == "en" else ("../" + page)
    switch_label = t("中文", "EN")
    switch_title = t("切換至中文版", "View in English")
    return f"""<header class="topnav">
  <div class="container topnav-inner">
    <a class="brand" href="index.html" aria-label="Koon Wing Product">
      <img src="{A()}assets/img/logo-mark.svg" alt="" width="38" height="38">
      <span class="brand-txt"><span class="mark">KOON WING</span><br><span class="sub">PRODUCT</span></span>
    </a>
    <button class="navtoggle" type="button" aria-expanded="false" aria-label="{t('Menu', '選單')}">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18" stroke-linecap="round"/></svg>
    </button>
    <nav aria-label="{t('Main', '主選單')}">{links}
      <a class="langswitch" href="{switch_href}" hreflang="{t('zh-Hant', 'en')}" title="{switch_title}">{switch_label}</a>
      <a class="btn btn-primary nav-cta" href="contact.html">{t("Request a Quote", "索取報價")}</a>
    </nav>
  </div>
</header>"""


def footer():
    prods = "".join(f'<li><a href="products.html#{s["key"]}">{sname(s)}</a></li>' for s in SERIES[:5])
    return f"""</main>
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <img class="flogo" src="{A()}assets/img/logo-lockup-light.svg" alt="Koon Wing Product" width="200" height="78">
        <p class="about">{t("Custom metal and plastic gifts, designed and managed from Macau and Hong Kong — from first sketch to boxed delivery.", "於澳門及香港設計及管理的訂製金屬與塑膠禮品——由第一張草圖，到裝盒交付。")}</p>
      </div>
      <div>
        <h4>{t("Products", "產品")}</h4>
        <ul>{prods}</ul>
      </div>
      <div>
        <h4>{t("Company", "公司")}</h4>
        <ul>
          <li><a href="about.html">{t("About us", "關於我們")}</a></li>
          <li><a href="showcase.html">{t("Design samples", "設計樣本")}</a></li>
          <li><a href="partnership.html">{t("Partnership", "商業合作")}</a></li>
          <li><a href="contact.html">{t("Contact", "聯絡我們")}</a></li>
        </ul>
      </div>
      <div>
        <h4>{t("Get in touch", "聯絡方式")}</h4>
        <ul>
          <li>{MAIL}</li>
          <li>{t("Macau", "澳門")}</li>
          <li><a href="{('zh/' + 'index.html') if LANG == 'en' else '../index.html'}">{t("中文版", "English site")}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-base">
      <span>© 2026 Koon Wing Product. {t("All rights reserved.", "版權所有。")}</span>
      <span>{t("Macau · 澳門", "澳門 · Macau")}</span>
    </div>
  </div>
</footer>
<script src="{A()}assets/js/main.js"></script>
</body>
</html>
"""


def cta(en_h, zh_h, en_p, zh_p):
    return f"""<section class="section">
  <div class="container">
    <div class="cta">
      <div>
        <h2>{t(en_h, zh_h)}</h2>
        <p>{t(en_p, zh_p)}</p>
      </div>
      <div class="btn-row" style="margin:0">
        <a class="btn btn-gold" href="contact.html">{t("Request a Quote", "索取報價")}</a>
        <a class="btn btn-ghost" style="border-color:rgba(255,255,255,.3);color:#fff" href="products.html">{t("See products", "瀏覽產品")}</a>
      </div>
    </div>
  </div>
</section>"""


def feat(icon, en_h, zh_h, en_p, zh_p):
    return f"""<div class="feat">
      <svg class="ico" viewBox="0 0 24 24" aria-hidden="true">{ICONS[icon]}</svg>
      <h3>{t(en_h, zh_h)}</h3><p>{t(en_p, zh_p)}</p>
    </div>"""


def steps_html():
    return "".join(
        f'<div class="step"><span class="n">{t("STEP", "階段")} {n}</span>'
        f'<h3>{t(en_h, zh_h)}</h3>'
        f''
        f'<p>{t(en_p, zh_p)}</p></div>'
        for n, en_h, zh_h, en_p, zh_p in STEPS)


# ── pages ──────────────────────────────────────────────────────────────────
def page_home():
    cards = ""
    for g in GROUPS:
        s, n = g["hero"]
        cards += f"""
      <a class="card" href="products.html#{g['members'][0]}">
        <div class="card-media"><img src="{img(s, n, True)}" alt="{g[LANG]['name']}" loading="lazy"></div>
        <div class="card-body">
          <span class="card-idx">{g['key'].upper()}</span>
          <h3>{g[LANG]['name']}</h3>
          <p class="cn-sub" style="margin:0">{g['zh' if LANG == 'en' else 'en']['name']}</p>
          <p>{g[LANG]['desc']}</p>
          <div class="tags">{"".join(f'<span class="tag">{sname(BY_KEY[m])}</span>' for m in g['members'])}</div>
        </div>
      </a>"""

    strip = "".join(
        f'<a href="showcase.html" class="shot" style="display:block">'
        f'<img src="{img(k, n, True)}" alt="{sname(BY_KEY[k])}" loading="lazy"></a>'
        for k, n in [("lapel-pin", 6), ("bookmark", 4), ("coaster-acrylic", 3), ("flask", 5),
                     ("bottle-opener", 2), ("tie-clip", 1), ("coaster-metal", 4), ("keychain", 3)])

    h1 = t('Objects people<br>actually <span>keep.</span>',
           '值得<span>保留</span><br>的禮品。')

    return head(t("Koon Wing Product · Custom Metal &amp; Plastic Gifts, Macau",
                  "冠榮製品 · 澳門訂製金屬及塑膠禮品"),
                t("Macau and Hong Kong design and production house for custom metal and plastic gifts — enamel "
                  "pins, keychains, coasters, drinkware and desk pieces. Design to boxed delivery.",
                  "澳門及香港的訂製金屬及塑膠禮品設計與生產公司——琺瑯襟章、匙扣、杯墊、飲品器具及桌上文儀用品，由設計到裝盒交付。"),
                "index.html") + f"""
<section class="hero">
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">{t("Custom gifts · Macau &amp; Hong Kong", "訂製禮品 · 澳門及香港")}</p>
      <h1>{h1}</h1>
      <p class="lead">{t("Koon Wing Product designs and produces custom metal and plastic gifts from Macau and Hong Kong — enamel pins, acrylic charms, coasters, barware and desk pieces. You bring the brand and the deadline; we handle artwork, tooling, sampling, production and packing.", "冠榮製品於澳門及香港設計及生產訂製金屬與塑膠禮品——琺瑯襟章、亞加力吊飾、杯墊、酒具及桌上文儀用品。您提供品牌與交期，圖稿、開模、打樣、生產與包裝由我們負責。")}</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="contact.html">{t("Request a Quote", "索取報價")}</a>
        <a class="btn btn-ghost" href="showcase.html">{t("See design samples →", "查看設計樣本 →")}</a>
      </div>
      <div class="hero-meta">
        <span>{t("Metal · Enamel · Acrylic", "金屬 · 琺瑯 · 亞加力")}</span>
        <span>{t("Design to delivery", "由設計到交付")}</span>
        <span>{t("Macau &amp; Hong Kong", "澳門 · 香港")}</span>
      </div>
    </div>
    <figure class="hero-figure" style="margin:0">
      <img src="{img('lapel-pin', 3)}" alt="{t('Enamel lapel pin presented in a gift box', '琺瑯襟章連禮盒')}"
           width="{dim('lapel-pin', 3)[0]}" height="{dim('lapel-pin', 3)[1]}" fetchpriority="high">
    </figure>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">{t("What we make", "我們生產什麼")}</p>
      <h2>{t("Three families,<br>one production standard.", "三大系列，<br>同一生產標準。")}</h2>
      <p class="lead">{t("Most programmes are built from these formats — on their own, or combined into a matched gift set that shares one artwork and one finish.", "多數禮品計劃都由這些形式組成——可以單獨使用，也可以組成共用同一圖稿與同一表面處理的配套禮盒。")}</p>
    </div>
    <div class="grid-3">{cards}
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">{t("Why Koon Wing", "為何選擇冠榮")}</p>
      <h2>{t("Small enough to answer,<br>organised enough to deliver.", "規模夠小，回應夠快；<br>流程夠穩，交付夠準。")}</h2>
    </div>
    <div class="grid-4">
      {feat("pencil", "Design done here", "設計在澳門及香港完成",
            "Artwork and structural design are handled in Macau and Hong Kong, in your timezone, in Chinese or English.",
            "圖稿與結構設計均在澳門及香港處理，與您同一時區，中英文皆可溝通。")}
      {feat("layers", "Vetted production partners", "經篩選的合作工廠",
            "We do not run a factory. We place work with specialist manufacturers and stay accountable for the result.",
            "我們不設自家工廠，而是把工作交予專門的製造商，並為最終成品負責。")}
      {feat("check", "Sample before production", "先確認樣本，後生產",
            "Nothing runs until you have approved a physical pre-production sample in writing.",
            "未經您書面確認實物試產樣本，不會開始任何生產。")}
      {feat("box", "Packed the way you sell it", "按銷售方式包裝",
            "Retail boxing, gift sets and outer cartons are specified with the product, not bolted on afterwards.",
            "零售包裝、禮盒與外箱在產品階段一併訂明，並非事後補做。")}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">{t("How we work", "我們的流程")}</p>
      <h2>{t("From sketch to packed carton.", "由草圖到裝箱出貨。")}</h2>
    </div>
    <div class="steps">{steps_html()}</div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head" style="margin-bottom:var(--gap-lg)">
      <p class="eyebrow">{t("Design samples", "設計樣本")}</p>
      <h2>{t("What the finishes look like.", "實際成品效果。")}</h2>
      <p class="lead">{t("A selection of design samples produced to show materials, plating and packaging options. These are demonstration pieces, not client work.", "以下為一批設計樣本，用以展示材質、電鍍與包裝的選擇。這些是示範用的樣本，並非客戶個案。")}</p>
    </div>
    <div class="gallery" style="grid-template-columns:repeat(auto-fill,minmax(190px,1fr))">{strip}</div>
    <div class="btn-row"><a class="btn btn-ghost" href="showcase.html">{t("View all samples →", "查看全部樣本 →")}</a></div>
  </div>
</section>

{cta("Tell us what you need made.", "告訴我們您想製作的產品。",
     "Send a sketch, a reference photo or a rough spec. We will come back with formats, finishes and an indicative quotation.",
     "提供草圖、參考相片或粗略規格，我們會回覆可行的形式、表面處理及初步報價。")}
""" + footer()


def page_products():
    rows = ""
    for i, s in enumerate(SERIES):
        n = len(MAN[s["key"]])
        pics = [1, 2, 3] if n >= 3 else list(range(1, n + 1))
        media = "".join(
            f'<img src="{img(s["key"], p, True)}" alt="{sname(s)} {p}" loading="lazy" width="{dim(s["key"], p, True)[0]}" height="{dim(s["key"], p, True)[1]}">'
            for p in pics)
        d = s[LANG]
        rows += f"""
    <article class="prow{" rev" if i % 2 else ""}" id="{s['key']}">
      <div class="prow-media">{media}</div>
      <div class="prow-body">
        <p class="eyebrow">{i + 1:02d} · {s['group'].upper()}</p>
        <h2 style="font-size:clamp(24px,2.6vw,34px)">{d['name']}</h2>
        <p class="cn-sub">{s['zh' if LANG == 'en' else 'en']['name']}</p>
        <p class="lead" style="font-size:16px;margin-top:var(--gap-md)">{d['blurb']}</p>
        <table class="spec" style="margin-top:var(--gap-md)">
          <tbody>
            <tr><th>{t("Typical build", "常用結構")}</th><td>{d['build']}</td></tr>
            <tr><th>{t("Options", "可選項目")}</th><td>{d['options']}</td></tr>
            <tr><th>{t("Order size", "訂購量")}</th><td>{t("Flexible — tell us your quantity and we will quote it", "彈性處理——告知數量，我們即可報價")}</td></tr>
          </tbody>
        </table>
        <div class="btn-row"><a class="btn btn-ghost" href="contact.html">{t("Quote this format →", "索取此類報價 →")}</a></div>
      </div>
    </article>"""

    return head(t("Products · Koon Wing Product", "產品 · 冠榮製品"),
                t("Custom enamel pins, acrylic keychains, tie clips, metal pens, bookmarks, bottle "
                  "openers, coasters and insulated drinkware.",
                  "訂製琺瑯襟章、亞加力匙扣、領帶夾、金屬原子筆、書籤、開瓶器、杯墊及保溫器具。"),
                "products.html") + f"""
<section class="pagehead">
  <div class="container">
    <p class="eyebrow">{t("Our products", "我們的產品")}</p>
    <h1>{t("Ten formats we build most often.", "我們最常生產的十種形式。")}</h1>
    <p class="lead">{t("Each format below can be made to your artwork, your finish and your packaging. Specifications listed are the common build and the options available — final specification is confirmed on your sample before production.", "以下每一種形式，均可按您的圖稿、表面處理與包裝製作。所列規格為常見結構及可選項目，最終規格於樣本確認階段落實。")}</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="container">{rows}
  </div>
</section>
{cta("Not sure which format fits?", "不確定哪一款適合？",
     "Send us the budget, the quantity and who is receiving it. We will suggest two or three formats that work and quote them side by side.",
     "告知預算、數量及送禮對象，我們會建議兩三款可行的形式，並列報價供您比較。")}
""" + footer()


def page_showcase():
    fbtns = f'<button class="filter" data-filter="all" aria-pressed="true">{t("All samples", "全部樣本")}</button>'
    fbtns += "".join(
        f'<button class="filter" data-filter="{s["key"]}" aria-pressed="false">{sname(s)}</button>'
        for s in SERIES)
    shots = ""
    for s in SERIES:
        for n in range(1, len(MAN[s["key"]]) + 1):
            cap = f'{sname(s)} {t("sample", "樣本")} {n:02d}'
            shots += f"""
      <figure class="shot" data-series="{s['key']}" data-full="{img(s['key'], n)}"
              data-caption="{cap}" tabindex="0" role="button" aria-label="{cap}">
        <img src="{img(s['key'], n, True)}" alt="{cap}" loading="lazy" width="{dim(s['key'], n, True)[0]}" height="{dim(s['key'], n, True)[1]}">
        <figcaption>{sname(s)}</figcaption>
      </figure>"""

    total = sum(len(MAN[s["key"]]) for s in SERIES)
    return head(t("Design Samples · Koon Wing Product", "設計樣本 · 冠榮製品"),
                t("Design samples showing materials, plating, enamel and packaging options across ten "
                  "custom gift formats.",
                  "十種訂製禮品形式的設計樣本，展示材質、電鍍、琺瑯及包裝的選擇。"),
                "showcase.html") + f"""
<section class="pagehead">
  <div class="container">
    <p class="eyebrow">{t("Design samples", "設計樣本")}</p>
    <h1>{t("Finishes, materials<br>and packaging.", "表面處理、材質<br>與包裝。")}</h1>
    <p class="lead">{t(f"{total} sample images across ten formats, produced to demonstrate what each material, plating and packaging option looks like in the hand.", f"共 {total} 張樣本圖片，涵蓋十種產品形式，用以展示各種材質、電鍍與包裝在實物上的效果。")}</p>
    <div class="notice" style="margin-top:var(--gap-lg);max-width:62ch">
      <svg viewBox="0 0 24 24" aria-hidden="true">{ICONS['info']}</svg>
      <p>{t("<strong>These are design samples, not client work.</strong> Any brand names, logos or packaging text visible in these images are illustrative only and do not represent real customers or orders.", "<strong>此為設計樣本，並非客戶個案。</strong>圖中出現的品牌名稱、標誌及包裝文字僅作示範用途，並不代表真實客戶或訂單。")}</p>
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

<div class="lb" role="dialog" aria-modal="true" aria-label="{t('Sample viewer', '樣本檢視')}">
  <button class="lb-btn lb-close" type="button" aria-label="{t('Close', '關閉')}">&times;</button>
  <button class="lb-btn lb-prev" type="button" aria-label="{t('Previous', '上一張')}">&#8249;</button>
  <img src="" alt="">
  <button class="lb-btn lb-next" type="button" aria-label="{t('Next', '下一張')}">&#8250;</button>
  <p class="lb-cap"></p>
</div>

{cta("Want a sample in your own branding?", "想以貴公司品牌打樣？",
     "We can produce a pre-production sample in your artwork and finish before you commit to a production run.",
     "在您決定量產之前，我們可先按您的圖稿與表面處理製作試產樣本。")}
""" + footer()


def page_about():
    faq = [
        ("“Do you make it yourselves?”", "「產品是你們自己生產的嗎？」",
         "No. We design and manage; specialist partner factories produce. We stay responsible for the "
         "spec, the sample and the inspection.",
         "不是。我們負責設計與管理，由專門的合作工廠生產。規格、樣本與檢查，全由我們負責到底。"),
        ("“What is the minimum order?”", "「最低訂購量是多少？」",
         "It depends entirely on the format and the tooling involved. Tell us the quantity you actually "
         "want and we will tell you honestly whether it is workable.",
         "視乎產品形式及是否需要開模。請告知您實際想要的數量，我們會坦白說明是否可行。"),
        ("“Are those your clients in the photos?”", "「相片中的是你們的客戶嗎？」",
         "No. Every brand name shown on this site is an illustrative design sample, produced to "
         "demonstrate finishes. We will not claim work we have not done.",
         "不是。本網站出現的所有品牌名稱均為示範用的設計樣本，用以展示表面處理效果。我們不會把沒有做過的工作說成做過。"),
    ]
    faq_html = "".join(
        f'<div class="feat"><h3>{t(en_h, zh_h)}</h3>'
        f''
        f'<p>{t(en_p, zh_p)}</p></div>'
        for en_h, zh_h, en_p, zh_p in faq)

    spec = [
        ("Based in", "所在地", "Macau &amp; Hong Kong", "澳門 · 香港"),
        ("Model", "經營模式",
         "Design and project management in Macau; production placed with partner factories",
         "設計及項目管理於澳門進行；生產交予合作工廠"),
        ("Materials", "材質",
         "Zinc alloy, brass, stainless steel, aluminium, cast acrylic, wood",
         "鋅合金、黃銅、不鏽鋼、鋁、鑄造亞加力、木材"),
        ("Processes", "工藝",
         "Die-striking, die-casting, enamelling, plating, photo-etching, laser engraving, UV print",
         "衝壓、壓鑄、琺瑯、電鍍、蝕刻、鐳射刻字、UV 印刷"),
        ("Order sizes", "訂購量", "Flexible — quoted per project", "彈性處理——按項目報價"),
        ("Working languages", "工作語言", "English · 繁體中文 · 普通話", "繁體中文 · English · 普通話"),
    ]
    spec_html = "".join(f"<tr><th>{t(a, b)}</th><td>{t(c, d)}</td></tr>" for a, b, c, d in spec)

    return head(t("About · Koon Wing Product", "關於我們 · 冠榮製品"),
                t("Koon Wing Product is a Macau design and sourcing house for custom metal and "
                  "plastic gifts.",
                  "冠榮製品是一間位於澳門的訂製金屬及塑膠禮品設計與採購公司。"),
                "about.html") + f"""
<section class="pagehead">
  <div class="container">
    <p class="eyebrow">{t("About us", "關於我們")}</p>
    <h1>{t("A Macau design<br>and sourcing house.", "一間澳門的設計<br>與採購公司。")}</h1>
  </div>
</section>

<section class="section">
  <div class="container grid-2" style="align-items:start;gap:clamp(28px,5vw,72px)">
    <div>
      <h2 style="font-size:clamp(24px,2.8vw,34px)">{t("What we do", "我們的業務")}</h2>
      <p class="lead" style="margin-top:var(--gap-md)">{t("Koon Wing Product takes a brand's idea for a physical gift and carries it through to boxed, delivered goods. That means artwork prepared to production spec, tooling cut, a physical sample approved, production placed with the right specialist factory, and quality checked against the approved sample before shipping.", "冠榮製品把品牌對實體禮品的構想，一直做到裝盒交付為止。當中包括：按生產規格準備圖稿、開模、確認實物樣本、把生產交予合適的專門工廠，並在出貨前對照確認樣本檢查品質。")}</p>
      <p class="lead" style="margin-top:var(--gap-md)">{t("We are deliberately direct about the model: <strong>we do not own a factory.</strong> We design and manage across Macau and Hong Kong, and we place production with manufacturing partners in mainland China who specialise in the exact process a piece needs — die-striking and enamelling are not the same trade as acrylic casting or vacuum drinkware. Being independent of any single plant is what lets us put a job where it will come out best, rather than where it happens to fit.", "我們對經營模式說得很直接：<strong>我們沒有自己的工廠。</strong>設計與管理在澳門及香港進行，生產則交予中國內地的合作工廠——衝壓與琺瑯，跟亞加力鑄造或真空保溫器具，本來就不是同一門手藝。正因為不隸屬任何單一工廠，我們才可以把每件工作交到最適合的地方，而不是硬塞進現成的產線。")}</p>
    </div>
    <div>
      <figure style="margin:0">
        <img src="{img('bookmark', 4)}" alt="{t('Etched metal bookmark detail', '金屬蝕刻書籤細節')}"
             style="border-radius:var(--radius-lg);width:100%;height:auto" loading="lazy"
             width="{dim('bookmark', 4)[0]}" height="{dim('bookmark', 4)[1]}">
      </figure>
      <table class="spec" style="margin-top:var(--gap-lg)"><tbody>{spec_html}</tbody></table>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">{t("How we work", "我們的流程")}</p>
      <h2>{t("Five stages, one approved sample.", "五個階段，一個確認樣本。")}</h2>
      <p class="lead">{t("The approved physical sample is the contract. Everything produced afterwards is checked against it, which is what stops the familiar problem of goods arriving a shade off, a gram light, or in the wrong box.", "確認的實物樣本就等於合約。其後生產的一切都以它為準——這正是避免貨品到手時顏色差一點、重量輕一點、或者換了包裝盒的關鍵。")}</p>
    </div>
    <div class="steps">{steps_html()}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">{t("Straight answers", "坦白回答")}</p>
      <h2>{t("What you should ask us.", "您應該向我們查證的事。")}</h2>
    </div>
    <div class="grid-3">{faq_html}</div>
  </div>
</section>

{cta("Start with a conversation.", "由一次洽談開始。",
     "No forms to fill in first. Send what you have — a sketch, a photo, a budget — and we will tell you what is realistic.",
     "不必先填表格。把手上有的資料——草圖、相片、預算——發給我們，我們會告訴您什麼是實際可行的。")}
""" + footer()


def page_partnership():
    modes = [
        ("01 · OEM", "Make to your design", "按您的設計生產", ("lapel-pin", 5),
         "You supply the artwork or CAD. We prepare it to production spec, tool it, sample it and run "
         "it. You own the design and the tooling.",
         "您提供圖稿或 CAD。我們按生產規格整理、開模、打樣及量產。設計與模具歸您所有。"),
        ("02 · ODM", "Design it with you", "共同設計開發", ("coaster-acrylic", 6),
         "You bring a brand and a brief; we develop the object — format, materials, finish and "
         "packaging — and take it through to production.",
         "您提供品牌與需求；我們開發實物——形式、材質、表面處理與包裝——並一直做到量產。"),
        ("03 · Private label", "Your label, our range", "自有品牌供貨", ("flask", 1),
         "Take formats we already build and carry them under your own brand and packaging for retail "
         "or continuity programmes.",
         "沿用我們既有的產品形式，換上您的品牌與包裝，供零售或長期供貨計劃使用。"),
    ]
    cards = "".join(f"""
    <div class="card"><div class="card-media"><img src="{img(k, n, True)}" alt="{t(en_h, zh_h)}" loading="lazy"></div>
      <div class="card-body"><span class="card-idx">{idx}</span><h3>{t(en_h, zh_h)}</h3>
        <p>{t(en_p, zh_p)}</p></div></div>"""
                    for idx, en_h, zh_h, (k, n), en_p, zh_p in modes)

    need = [("1 · The object", "1 · 產品", "A format, a sketch, or a reference photo of something similar",
             "一種形式、一張草圖，或一張類似產品的參考相片"),
            ("2 · The quantity", "2 · 數量", "The number you actually want — not a rounded-up guess",
             "您實際需要的數量——而非概略估算"),
            ("3 · The deadline", "3 · 交期", "The date it must be in hand, and where in the world that is",
             "必須到貨的日期，以及送抵的地點"),
            ("4 · The budget", "4 · 預算", "A per-unit ceiling, so we specify to it instead of around it",
             "每件單價上限，我們會據此訂定規格")]
    need_html = "".join(f"<tr><th>{t(a, b)}</th><td>{t(c, d)}</td></tr>" for a, b, c, d in need)

    return head(t("Business Partnerships · Koon Wing Product", "商業合作 · 冠榮製品"),
                t("OEM and ODM custom gift production, private label programmes, corporate gifting and "
                  "retail supply from Macau.",
                  "澳門的 OEM／ODM 訂製禮品生產、自有品牌計劃、企業禮品及零售供貨。"),
                "partnership.html") + f"""
<section class="pagehead">
  <div class="container">
    <p class="eyebrow">{t("Business partnerships", "商業合作")}</p>
    <h1>{t("Ways of working<br>together.", "合作方式。")}</h1>
    <p class="lead">{t("Whether you need one gift for one campaign or an ongoing range carrying your own label, the process is the same — the difference is how much of it you want to own.", "無論是單次推廣的一款禮品，還是掛上貴公司品牌的長期系列，流程都一樣——分別只在於您希望掌握多少。")}</p>
  </div>
</section>

<section class="section">
  <div class="container grid-3">{cards}
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">{t("Who this suits", "適合的對象")}</p>
      <h2>{t("Buyers we are built for.", "我們適合服務的買家。")}</h2>
    </div>
    <div class="grid-4">
      {feat("box", "Corporate gifting", "企業禮品",
            "Staff recognition, client gifts, conference and anniversary programmes needing one coherent set.",
            "員工表揚、客戶贈禮、會議及周年紀念計劃，需要一套風格一致的禮品。")}
      {feat("pencil", "Brands &amp; creators", "品牌與創作者",
            "Artist series, merchandise drops and brand collectibles where artwork fidelity matters.",
            "藝術家系列、限量周邊及品牌收藏品，重視圖稿還原度。")}
      {feat("layers", "Retail &amp; hospitality", "零售與款待業",
            "Coasters, barware and drinkware produced to a retail finish, boxed ready to sell.",
            "杯墊、酒具及飲品器具，以零售級表面處理製作，包裝好即可上架。")}
      {feat("check", "Agencies &amp; event planners", "代理與活動策劃",
            "One point of contact who will give you a straight timeline instead of an optimistic one.",
            "單一聯絡點，提供務實而非過度樂觀的時間表。")}
    </div>
  </div>
</section>

<section class="section">
  <div class="container grid-2" style="gap:clamp(28px,5vw,72px);align-items:start">
    <div>
      <p class="eyebrow">{t("What we need from you", "我們需要的資料")}</p>
      <h2 style="font-size:clamp(24px,2.8vw,34px)">{t("Four things get you a quote.", "四項資料，即可報價。")}</h2>
      <table class="spec" style="margin-top:var(--gap-lg)"><tbody>{need_html}</tbody></table>
      <div class="btn-row"><a class="btn btn-primary" href="contact.html">{t("Send an enquiry", "提交查詢")}</a></div>
    </div>
    <div>
      <p class="eyebrow">{t("What you get back", "您會收到什麼")}</p>
      <h2 style="font-size:clamp(24px,2.8vw,34px)">{t("A spec, a price and a real date.", "規格、價格與實際交期。")}</h2>
      <p class="lead" style="margin-top:var(--gap-md)">{t("A written specification of the piece as we would build it, an indicative unit price at your quantity, the tooling cost if any, and a production timeline with the sampling stage shown separately — because that is the stage that usually moves.", "一份書面規格，說明我們會如何製作；按您數量計算的初步單價；如需開模則列明模具費；以及一份把打樣階段獨立列出的生產時間表——因為打樣正是最常變動的一環。")}</p>
      <p class="lead" style="margin-top:var(--gap-md)">{t("If your quantity or deadline is not workable, we will say so at that point rather than after you have paid a deposit.", "如果您的數量或交期並不可行，我們會在這個階段直說，而不是等您付了訂金之後才講。")}</p>
    </div>
  </div>
</section>

{cta("Let's scope your programme.", "共同規劃您的項目。",
     "Tell us the object, the quantity, the deadline and the budget. You will get a specification and an indicative price back.",
     "告知產品、數量、交期與預算，我們會回覆一份規格及初步價格。")}
""" + footer()


def page_contact():
    opts = "".join(f"<option>{sname(s)}</option>" for s in SERIES)
    direct = [("Email", "電郵", MAIL),
              ("Address", "地址", t("Room 004, Block B, 7/F, Block 2, Nam Fong Industrial Building,<br>679 Avenida do Dr. Francisco Vieira Machado, Macau", "澳門馬揸度博士大馬路679號<br>南方工業大廈第2座7樓B座004室")),
              ("Hours", "辦公時間", t("Monday – Friday, Macau time (GMT+8)", "星期一至五，澳門時間（GMT+8）"))]
    direct_html = "".join(f"<tr><th>{t(a, b)}</th><td>{c}</td></tr>" for a, b, c in direct)

    return head(t("Contact · Koon Wing Product", "聯絡我們 · 冠榮製品"),
                t("Request a quotation for custom metal and plastic gifts from Koon Wing Product, Macau.",
                  "向澳門冠榮製品索取訂製金屬及塑膠禮品報價。"),
                "contact.html") + f"""
<section class="pagehead">
  <div class="container">
    <p class="eyebrow">{t("Contact us", "聯絡我們")}</p>
    <h1>{t("Tell us what<br>you need made.", "告訴我們<br>您想製作什麼。")}</h1>
    <p class="lead">{t("The more of the four basics you can give us — object, quantity, deadline, budget — the more useful the first reply will be.", "四項基本資料——產品、數量、交期、預算——提供得越齊全，我們第一次回覆就越有用。")}</p>
  </div>
</section>

<section class="section">
  <div class="container grid-2" style="gap:clamp(28px,5vw,72px);align-items:start">
    <div>
      <h2 style="font-size:clamp(22px,2.4vw,30px)">{t("Send an enquiry", "提交查詢")}</h2>
      <p class="form-note" style="margin-top:var(--gap-sm)">{t("Fields marked", "標示")} <em style="color:var(--accent);font-style:normal">*</em> {t("are required.", "的欄位為必填。")}</p>
      <form id="enquiry" action="mailto:info@koonwingproduct.com.mo" method="post"
            enctype="text/plain" novalidate>
        <div class="grid-2" style="gap:var(--gap-md)">
          <div class="field"><label for="name">{t("Name", "姓名")} <em>*</em></label>
            <input id="name" name="name" type="text" autocomplete="name" required></div>
          <div class="field"><label for="company">{t("Company", "公司")}</label>
            <input id="company" name="company" type="text" autocomplete="organization"></div>
        </div>
        <div class="grid-2" style="gap:var(--gap-md)">
          <div class="field"><label for="email">{t("Email", "電郵")} <em>*</em></label>
            <input id="email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="phone">{t("Phone / WhatsApp", "電話／WhatsApp")}</label>
            <input id="phone" name="phone" type="tel" autocomplete="tel" inputmode="tel"></div>
        </div>
        <div class="grid-2" style="gap:var(--gap-md)">
          <div class="field"><label for="product">{t("Product format", "產品類別")}</label>
            <select id="product" name="product"><option>{t("Not sure yet — advise me", "尚未確定——請給建議")}</option>{opts}</select></div>
          <div class="field"><label for="qty">{t("Quantity", "數量")}</label>
            <input id="qty" name="qty" type="text" inputmode="numeric" placeholder="{t('e.g. 500', '例如 500')}"></div>
        </div>
        <div class="field"><label for="deadline">{t("Date needed in hand", "到貨日期")}</label>
          <input id="deadline" name="deadline" type="text" placeholder="{t('e.g. mid-November, Macau', '例如 十一月中，澳門')}"></div>
        <div class="field"><label for="msg">{t("What are you making?", "產品內容")} <em>*</em></label>
          <textarea id="msg" name="msg" required
            placeholder="{t('Describe the piece, or paste a reference link. Budget per unit is helpful.', '描述產品，或貼上參考連結。註明每件預算會更有幫助。')}"></textarea></div>
        <div class="hp" aria-hidden="true">
          <label for="website">Leave this field empty</label>
          <input id="website" name="website" type="text" tabindex="-1" autocomplete="off">
        </div>
        <button class="btn btn-primary" type="submit">{t("Send enquiry", "提交查詢")}</button>
        <p class="form-status" role="status" aria-live="polite" hidden></p>
        <p class="form-note" style="margin-top:var(--gap-md)">
          {t("We usually reply within one business day. You can also write to us directly at", "我們通常於一個工作天內回覆。您亦可直接來信")}
          <a href="mailto:info@koonwingproduct.com.mo">info@koonwingproduct.com.mo</a>{t(".", "。")}</p>
      </form>
    </div>

    <div>
      <h2 style="font-size:clamp(22px,2.4vw,30px)">{t("Direct", "直接聯絡")}</h2>
      <table class="spec" style="margin-top:var(--gap-md)"><tbody>{direct_html}</tbody></table>
      <figure style="margin:var(--gap-xl) 0 0">
        <img src="{img('lapel-pin', 1)}" alt="{t('Enamel lapel pin on slate', '琺瑯襟章')}"
             style="border-radius:var(--radius-lg);width:100%;height:auto" loading="lazy"
             width="{dim('lapel-pin', 1)[0]}" height="{dim('lapel-pin', 1)[1]}">
      </figure>
    </div>
  </div>
</section>
""" + footer()


PAGES = {
    "index.html": page_home,
    "products.html": page_products,
    "showcase.html": page_showcase,
    "about.html": page_about,
    "partnership.html": page_partnership,
    "contact.html": page_contact,
}

if __name__ == "__main__":
    os.makedirs(os.path.join(SITE, "zh"), exist_ok=True)
    for lang in ("en", "zh"):
        LANG = lang
        outdir = SITE if lang == "en" else os.path.join(SITE, "zh")
        for fn, gen in PAGES.items():
            html = gen()
            with io.open(os.path.join(outdir, fn), "w", encoding="utf-8") as f:
                f.write(html)
            print(f"{lang}/{fn:18} {len(html)}")
