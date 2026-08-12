#!/usr/bin/env python3
"""Generate the WiThemes static site.

Run:  python3 _src/build.py
Writes plain HTML into the repo root (one index.html per directory).
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SITE = "https://withemes.com"
BRAND = "WiThemes"
PHONE = "0900 000 000"
PHONE_HREF = "0900000000"
EMAIL = "info@withemes.com"
ADDR = "Tầng trệt, 114 Điện Biên Phủ, Phường Tân Định, Thành phố Hồ Chí Minh"
MST = "0318552411"
GA = "G-5EDRYVRH1M"

SERVICES = [
    ("/dich-vu/thiet-ke-website/", "Thiết kế website chuẩn SEO"),
    ("/dich-vu/thiet-ke-website-ban-hang/", "Thiết kế website bán hàng"),
    ("/dich-vu/thiet-ke-landing-page/", "Thiết kế landing page"),
    ("/dich-vu/dich-vu-seo-tong-the/", "Dịch vụ SEO tổng thể"),
    ("/dich-vu/seo-tu-khoa/", "Dịch vụ SEO từ khóa"),
    ("/dich-vu/seo-local-google-maps/", "SEO Local – Google Maps"),
    ("/dich-vu/audit-website/", "Audit website"),
    ("/dich-vu/toi-uu-toc-do-website/", "Tối ưu tốc độ website"),
]

NAV = [
    ("/", "Trang chủ", None),
    ("/gioi-thieu/", "Giới thiệu", None),
    ("/dich-vu/", "Dịch vụ", SERVICES),
    ("/bang-gia/", "Bảng giá", None),
    ("/quy-trinh/", "Quy trình", None),
    ("/du-an/", "Dự án", None),
    ("/kien-thuc/", "Kiến thức", None),
    ("/lien-he/", "Liên hệ", None),
]

KB = [
    ("/kien-thuc/seo-la-gi/", "SEO là gì? Hiểu đúng trước khi tiêu tiền"),
    ("/kien-thuc/checklist-seo-onpage/", "Checklist SEO onpage 27 điểm"),
    ("/kien-thuc/core-web-vitals-la-gi/", "Core Web Vitals là gì?"),
]


def head_extra(page):
    og_img = SITE + "/assets/" + page.get("img", "site-restaurant.jpg")
    url = SITE + page["slug"]
    tags = [
        '<link rel="canonical" href="%s">' % url,
        '<meta property="og:type" content="%s">' % page.get("og_type", "website"),
        '<meta property="og:locale" content="vi_VN">',
        '<meta property="og:site_name" content="%s">' % BRAND,
        '<meta property="og:title" content="%s">' % esc(page["title"]),
        '<meta property="og:description" content="%s">' % esc(page["desc"]),
        '<meta property="og:url" content="%s">' % url,
        '<meta property="og:image" content="%s">' % og_img,
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="robots" content="%s">' % (
            "noindex,follow" if page.get("noindex")
            else "index,follow,max-image-preview:large"),
    ]
    return "\n".join(tags)


def esc(s):
    s = re.sub(r"&(?!#?\w+;)", "&amp;", s)
    return s.replace('"', "&quot;").replace("<", "&lt;")


def plain(s):
    """HTML entities -> plain text, for JSON-LD values."""
    return (s.replace("&amp;", "&").replace("&quot;", '"')
             .replace("&lt;", "<").replace("&gt;", ">").replace("&nbsp;", " "))


def crumbs(page):
    items = [("/", "Trang chủ")] + page.get("crumb", [])
    html = " › ".join(
        '<a href="%s">%s</a>' % (u, t) if i < len(items) - 1 else "<span>%s</span>" % t
        for i, (u, t) in enumerate(items + [(page["slug"], page["h1"])])
    )
    ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": plain(t), "item": SITE + u}
            for i, (u, t) in enumerate(items + [(page["slug"], page["h1"])])
        ],
    }
    return html, ld


def nav_html(slug):
    out = ['<nav class="main"><div class="wrap"><ul>']
    for url, label, sub in NAV:
        cls = ' class="drop"' if sub else ""
        out.append("<li%s><a href=\"%s\">%s%s</a>" % (cls, url, label, " ▾" if sub else ""))
        if sub:
            out.append("<ul>")
            for su, sl in sub:
                out.append('<li><a href="%s">%s</a></li>' % (su, sl))
            out.append("</ul>")
        out.append("</li>")
    out.append("</ul></div></nav>")
    return "".join(out)


def sidebar(slug):
    svc = "".join(
        '<li><a href="%s">%s</a></li>' % (u, t) for u, t in SERVICES if u != slug
    )
    kb = "".join('<li><a href="%s">%s</a></li>' % (u, t) for u, t in KB)
    return """<aside class="side">
  <div class="widget"><h3>Dịch vụ của chúng tôi</h3><ul>%s</ul></div>
  <div class="widget"><div class="callbox">
    <span>TƯ VẤN MIỄN PHÍ 24/7</span>
    <b><a href="tel:%s">%s</a></b>
    <a class="btn btn-g btn-sm" href="/lien-he/">GỬI YÊU CẦU</a>
  </div></div>
  <div class="widget"><h3>Cam kết</h3><div class="inner">
    <ul style="list-style:none;padding:0;margin:0;font-size:13px">
      <li>✔ Báo giá trọn gói, không phát sinh</li>
      <li>✔ Website chuẩn SEO, chuẩn mobile</li>
      <li>✔ Tốc độ tải dưới 3 giây</li>
      <li>✔ Bàn giao toàn bộ mã nguồn</li>
      <li>✔ Bảo hành 12 tháng</li>
    </ul>
  </div></div>
  <div class="widget"><h3>Kiến thức mới</h3><ul>%s</ul></div>
  <div class="widget"><div class="zalo">Chat Zalo: <a href="#">%s</a></div></div>
</aside>""" % (svc, PHONE_HREF, PHONE, kb, PHONE)


FOOTER = """<footer class="site"><div class="wrap">
<div class="cols4">
  <div>
    <h4>%(brand)s</h4>
    <p>Công ty thiết kế website và SEO tại TP. Hồ Chí Minh. Thành lập 7/2024.</p>
    <p>Địa chỉ: %(addr)s</p>
    <p>Email: <a href="mailto:%(email)s">%(email)s</a><br>Hotline: <a href="tel:%(phone_href)s">%(phone)s</a></p>
    <p class="social"><a href="#">Facebook</a><a href="#">Zalo</a><a href="#">YouTube</a><a href="#">LinkedIn</a><a href="#">TikTok</a></p>
  </div>
  <div><h4>Dịch vụ</h4><ul>%(svc)s</ul></div>
  <div><h4>Thông tin</h4><ul>
    <li><a href="/gioi-thieu/">Giới thiệu</a></li>
    <li><a href="/bang-gia/">Bảng giá</a></li>
    <li><a href="/quy-trinh/">Quy trình làm việc</a></li>
    <li><a href="/du-an/">Dự án đã thực hiện</a></li>
    <li><a href="/cau-hoi-thuong-gap/">Câu hỏi thường gặp</a></li>
    <li><a href="/kien-thuc/">Kiến thức SEO</a></li>
    <li><a href="/lien-he/">Liên hệ</a></li>
  </ul></div>
  <div><h4>Chính sách</h4><ul>
    <li><a href="/dieu-khoan/">Điều khoản sử dụng</a></li>
    <li><a href="/chinh-sach-bao-mat/">Chính sách bảo mật</a></li>
    <li><a href="/sitemap.xml">Sitemap</a></li>
  </ul>
  <h4 style="margin-top:16px">Khu vực</h4>
  <p style="font-size:12px">TP. Hồ Chí Minh · Hà Nội · Đà Nẵng · Bình Dương · Cần Thơ</p>
  </div>
</div>
<div class="bottom">
  <div>&copy; 2024–2026 %(brand)s. MST: %(mst)s.</div>
  <div class="r">Thiết kế website &amp; SEO – %(brand)s</div>
</div>
</div></footer>
<div class="float">
  <a class="f1 blink" href="tel:%(phone_href)s" title="Gọi hotline">GỌI</a>
  <a class="f2" href="#" title="Chat Zalo">ZALO</a>
  <a class="f3" href="/lien-he/" title="Gửi yêu cầu">FORM</a>
</div>
<a class="totop" href="#top" title="Lên đầu trang">▲</a>""" % {
    "brand": BRAND, "addr": ADDR, "email": EMAIL, "phone": PHONE,
    "phone_href": PHONE_HREF, "mst": MST,
    "svc": "".join('<li><a href="%s">%s</a></li>' % (u, t) for u, t in SERVICES),
}

TICKER = ('<div class="ticker"><span>★ KHUYẾN MÃI THÁNG NÀY: '
          'TẶNG TRỌN GÓI HOSTING 1 NĂM + TÊN MIỀN .COM CHO MỌI HỢP ĐỒNG '
          'THIẾT KẾ WEBSITE ★ TẶNG AUDIT SEO 27 ĐIỂM TRỊ GIÁ 2.000.000đ ★ '
          'GỌI NGAY ' + PHONE + ' ★</span></div>')


def header(slug):
    return """<div class="topbar"><div class="wrap">
  <span>Email: <a href="mailto:%(email)s">%(email)s</a></span>
  <span>Hotline: <a href="tel:%(ph)s">%(phone)s</a></span>
  <span class="right blink">⚡ ĐANG NHẬN DỰ ÁN THÁNG NÀY – GIẢM 20%%</span>
</div></div>
<header class="head"><div class="wrap">
  <a class="logo" href="/"><b>Wi</b><span>Themes</span>
    <small>Thiết kế website · SEO</small></a>
  <div class="hot">
    <small>Tư vấn miễn phí</small>
    <div class="num"><a href="tel:%(ph)s" style="color:inherit">%(phone)s</a></div>
  </div>
  <a class="btn btn-g" href="/lien-he/">Nhận báo giá</a>
</div></header>
%(nav)s
%(ticker)s""" % {"email": EMAIL, "ph": PHONE_HREF, "phone": PHONE,
                 "nav": nav_html(slug), "ticker": TICKER}


PAGE_TPL = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
%(headx)s
<link rel="stylesheet" href="/style-3.css">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script type="application/ld+json">%(ld)s</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=%(ga)s"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', '%(ga)s');
</script>
</head>
<body id="top">
%(header)s
%(body)s
%(footer)s
</body>
</html>
"""

ORG_LD = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": BRAND,
    "url": SITE + "/",
    "email": EMAIL,
    "telephone": "+84900000000",
    "image": SITE + "/apple-touch-icon.png",
    "priceRange": "2.500.000đ - 25.000.000đ",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "114 Điện Biên Phủ, Phường Tân Định",
        "addressLocality": "Thành phố Hồ Chí Minh",
        "addressCountry": "VN",
    },
    "areaServed": "VN",
    "description": "Công ty thiết kế website và dịch vụ SEO tại TP. Hồ Chí Minh.",
}


def render(page):
    crumb_html, crumb_ld = crumbs(page)
    if page["slug"] == "/":
        top = page["hero"]
    else:
        top = ('<div class="pagehead"><div class="wrap"><h1>%s</h1>'
               '<div class="crumb">%s</div></div></div>' % (page["h1"], crumb_html))
    if page.get("sidebar", True):
        body = ('%s<div class="main"><div class="wrap"><div class="cols">'
                '<div class="content">%s</div>%s</div></div></div>'
                % (top, page["body"], sidebar(page["slug"])))
    else:
        body = top + page["body"].replace("{{sidebar}}", sidebar(page["slug"]))

    lds = [ORG_LD] if page["slug"] == "/" else []
    if page["slug"] != "/":
        lds.append(crumb_ld)
    lds += page.get("ld", [])
    ld = json.dumps(lds[0] if len(lds) == 1 else
                    {"@context": "https://schema.org", "@graph":
                     [{k: v for k, v in x.items() if k != "@context"} for x in lds]},
                    ensure_ascii=False)
    return PAGE_TPL % {
        "title": esc(page["title"]), "desc": esc(page["desc"]),
        "headx": head_extra(page), "ld": ld, "ga": GA,
        "header": header(page["slug"]), "body": body, "footer": FOOTER,
    }


STUB = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Chuyển hướng – %(brand)s</title>
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="%(site)s%(to)s">
<meta http-equiv="refresh" content="0;url=%(to)s">
</head>
<body><p>Trang này đã chuyển sang <a href="%(to)s">%(to)s</a>.</p></body>
</html>
"""

STUBS = {
    "/about/": "/gioi-thieu/",
    "/contact/": "/lien-he/",
    "/projects/": "/du-an/",
    "/terms/": "/dieu-khoan/",
    "/privacy/": "/chinh-sach-bao-mat/",
}


def write(slug, html):
    path = os.path.join(ROOT, slug.strip("/"), "index.html") if slug != "/" \
        else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


def main():
    import pages
    all_pages = pages.PAGES
    slugs = [p["slug"] for p in all_pages]
    assert len(slugs) == len(set(slugs)), "duplicate slug"

    for p in all_pages:
        write(p["slug"], render(p))
    for src, dst in STUBS.items():
        write(src, STUB % {"brand": BRAND, "site": SITE, "to": dst})

    # sitemap
    prio = {"/": "1.0"}
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in all_pages:
        if p.get("noindex"):
            continue
        pr = prio.get(p["slug"], "0.8" if p["slug"].count("/") < 3 else "0.6")
        lines.append("  <url><loc>%s%s</loc><changefreq>monthly</changefreq>"
                     "<priority>%s</priority></url>" % (SITE, p["slug"], pr))
    lines.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)

    old = os.path.join(ROOT, "style-2.css")
    if os.path.exists(old):
        os.remove(old)

    print("built %d pages + %d stubs" % (len(all_pages), len(STUBS)))


if __name__ == "__main__":
    main()
