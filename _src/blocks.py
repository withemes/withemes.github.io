# -*- coding: utf-8 -*-
"""Reusable HTML fragments for the WiThemes site."""

PHONE = "0900 000 000"


def fill(tpl, **kw):
    """Token substitution: {{name}} -> value. Safe with literal % in Vietnamese copy."""
    for k, v in kw.items():
        tpl = tpl.replace("{{%s}}" % k, v)
    return tpl


def cta(title="Cần một website ra đơn và lên top Google?",
        text="Gửi yêu cầu, chúng tôi khảo sát và báo giá trọn gói trong 24 giờ làm việc."):
    return """<div class="ctastrip"><div class="wrap">
<h2>%s</h2><p>%s</p>
<a class="btn btn-r" href="/lien-he/">Nhận báo giá miễn phí</a>
<a class="btn btn-b" href="tel:0900000000">Gọi %s</a>
</div></div>""" % (title, text, PHONE)


def faq(items):
    """items: list of (question, answer_html). Returns (html, jsonld)."""
    html = ["<h2>Câu hỏi thường gặp</h2>"]
    for q, a in items:
        html.append('<details><summary>%s</summary><div class="a">%s</div></details>' % (q, a))
    ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
            for q, a in items
        ],
    }
    return "\n".join(html), ld


def strip(html):
    out, keep = [], True
    for ch in html:
        if ch == "<":
            keep = False
        elif ch == ">":
            keep = True
        elif keep:
            out.append(ch)
    return "".join(out).strip()


def service_ld(name, desc, price=None):
    d = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": name,
        "name": name,
        "description": desc,
        "areaServed": {"@type": "Country", "name": "Việt Nam"},
        "provider": {"@type": "Organization", "name": "WiThemes",
                     "url": "https://withemes.com/"},
    }
    if price:
        d["offers"] = {"@type": "Offer", "price": price, "priceCurrency": "VND"}
    return d


def article_ld(headline, desc, slug, date="2026-08-12"):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": headline,
        "description": desc,
        "datePublished": date,
        "dateModified": date,
        "inLanguage": "vi",
        "author": {"@type": "Organization", "name": "WiThemes"},
        "publisher": {"@type": "Organization", "name": "WiThemes",
                      "logo": {"@type": "ImageObject",
                               "url": "https://withemes.com/apple-touch-icon.png"}},
        "mainEntityOfPage": "https://withemes.com" + slug,
    }


def boxes(items, cls="g4"):
    """items: list of (icon, title, text)."""
    out = ['<div class="grid %s">' % cls]
    for ico, t, txt in items:
        out.append('<div class="box"><div class="ico">%s</div><h3>%s</h3><p>%s</p></div>'
                   % (ico, t, txt))
    out.append("</div>")
    return "".join(out)


def steps(items):
    out = ['<div class="steps">']
    for t, txt in items:
        out.append('<div class="step"><h3>%s</h3><p>%s</p></div>' % (t, txt))
    out.append("</div>")
    return "".join(out)


PLANS = [
    ("CƠ BẢN", "2.500.000", "vnđ / trọn gói", False, [
        ("Website giới thiệu 5–7 trang", True),
        ("Giao diện mẫu, tùy chỉnh màu &amp; logo", True),
        ("Chuẩn mobile (responsive)", True),
        ("Cài đặt SSL miễn phí", True),
        ("Tặng hosting 1 năm", True),
        ("Tặng tên miền .com 1 năm", False),
        ("Chuẩn SEO onpage nâng cao", False),
        ("Viết nội dung 10 bài", False),
        ("Bảo hành 6 tháng", True),
    ]),
    ("PRO", "4.500.000", "vnđ / trọn gói", True, [
        ("Website doanh nghiệp 10–15 trang", True),
        ("Thiết kế giao diện riêng theo brand", True),
        ("Chuẩn mobile (responsive)", True),
        ("Cài đặt SSL miễn phí", True),
        ("Tặng hosting 1 năm", True),
        ("Tặng tên miền .com 1 năm", True),
        ("Chuẩn SEO onpage nâng cao", True),
        ("Viết nội dung 10 bài", False),
        ("Bảo hành 12 tháng", True),
    ]),
    ("VIP", "8.000.000", "vnđ / trọn gói", False, [
        ("Website bán hàng không giới hạn trang", True),
        ("Thiết kế giao diện riêng theo brand", True),
        ("Giỏ hàng, thanh toán, quản lý đơn", True),
        ("Cài đặt SSL miễn phí", True),
        ("Tặng hosting 1 năm", True),
        ("Tặng tên miền .com 1 năm", True),
        ("Chuẩn SEO onpage nâng cao", True),
        ("Viết nội dung 10 bài", True),
        ("Bảo hành 12 tháng", True),
    ]),
    ("THIẾT KẾ RIÊNG", "từ 25.000.000", "vnđ / dự án", False, [
        ("Wireframe &amp; thiết kế Figma từ đầu", True),
        ("Nghiên cứu đối thủ &amp; hành vi người dùng", True),
        ("Tính năng theo yêu cầu riêng", True),
        ("Tối ưu tốc độ chuyên sâu", True),
        ("Tặng hosting 1 năm", True),
        ("Tặng tên miền .com 1 năm", True),
        ("Chuẩn SEO onpage nâng cao", True),
        ("Viết nội dung 10 bài", True),
        ("Bảo hành 12 tháng", True),
    ]),
]


def pricing(plans=None):
    plans = plans or PLANS
    out = ['<div class="grid g4">']
    for name, amt, unit, hot, feats in plans:
        lis = "".join('<li%s>%s</li>' % ("" if ok else ' class="no"', f) for f, ok in feats)
        out.append("""<div class="price%s">%s
  <div class="ph"><h3>Gói %s</h3></div>
  <div class="amt"><b>%s</b><small>%s</small></div>
  <ul>%s</ul>
  <div class="pf"><a class="btn %s btn-sm" href="/lien-he/">Đăng ký gói này</a></div>
</div>""" % (" hot" if hot else "",
             '<span class="ribbon">Bán chạy</span>' if hot else "",
             name, amt, unit, lis, "btn-r" if hot else "btn-g"))
    out.append("</div>")
    return "".join(out)


TESTIMONIALS = """<div class="grid g3">
  <div class="tm"><div class="stars">★★★★★</div>
    <p>“Website mới tải nhanh hơn hẳn, khách đặt bàn qua form tăng rõ rệt sau hai tháng.”</p>
    <b>Anh Hoàng</b> – chuỗi nhà hàng, Quận 1</div>
  <div class="tm"><div class="stars">★★★★★</div>
    <p>“Bên mình cần lên top các từ khóa dịch vụ ở TP.HCM, sau 5 tháng đã vào top 3 được 12 từ.”</p>
    <b>Chị Ngân</b> – spa &amp; thẩm mỹ</div>
  <div class="tm"><div class="stars">★★★★★</div>
    <p>“Báo giá rõ ràng, bàn giao đúng hẹn, sau bàn giao vẫn hỗ trợ sửa lặt vặt.”</p>
    <b>Anh Tuấn</b> – công ty xây dựng</div>
</div>"""
