# -*- coding: utf-8 -*-
"""Core pages: home, about, service hub, pricing, process, projects, FAQ, contact, legal."""
from blocks import cta, faq, boxes, steps, pricing, fill, TESTIMONIALS

HERO = """<div class="hero"><div class="wrap">
<h1>Thiết kế website &amp; <em>dịch vụ SEO</em><br>trọn gói cho doanh nghiệp</h1>
<p class="sub">WiThemes thiết kế website chuẩn SEO, tải nhanh, chạy tốt trên điện thoại — và đưa
website đó lên trang nhất Google bằng một quy trình SEO có báo cáo hằng tháng.
Trọn gói từ 2.500.000đ, bàn giao trong 7–15 ngày.</p>
<div class="badges">
  <span>Miễn phí: Hosting 1 năm</span>
  <span>Miễn phí: Tên miền .com</span>
  <span>Miễn phí: SSL</span>
  <span>Miễn phí: Audit SEO 27 điểm</span>
</div>
<div class="cta">
  <a class="btn btn-g" href="/lien-he/">Nhận báo giá trong 24h</a>
  <a class="btn btn-o" href="/bang-gia/">Xem bảng giá</a>
  <a class="btn btn-r" href="tel:0900000000">Gọi 0900 000 000</a>
</div>
</div></div>"""

HOME_BODY = """
<div class="sec"><div class="wrap">
  <div class="sectitle"><div class="stars">★★★★★</div>
    <h2>Vì sao doanh nghiệp cần một website chuẩn SEO?</h2>
    <p>Một website đẹp mà không ai tìm thấy thì cũng chỉ là tấm danh thiếp điện tử.
    Chúng tôi làm website để nó được tìm thấy, và được tìm thấy trước đối thủ.</p>
  </div>
  {{why}}
</div></div>

<div class="sec alt"><div class="wrap">
  <div class="sectitle"><div class="stars">★★★★★</div>
    <h2>Giải pháp website &amp; SEO của WiThemes</h2>
    <p>Tám dịch vụ, một đầu mối. Bạn có thể đặt riêng từng phần hoặc làm trọn gói
    website + SEO để tiết kiệm 15–20% chi phí.</p>
  </div>
  <div class="grid g4">
    <div class="box left"><h3>Thiết kế website</h3>
      <p>Website giới thiệu doanh nghiệp, chuẩn SEO ngay từ khi dựng, tải dưới 3 giây.</p>
      <p><a href="/dich-vu/thiet-ke-website/">Chi tiết dịch vụ →</a></p></div>
    <div class="box left"><h3>Website bán hàng</h3>
      <p>Giỏ hàng, thanh toán, quản lý đơn, đồng bộ tồn kho và vận chuyển.</p>
      <p><a href="/dich-vu/thiet-ke-website-ban-hang/">Chi tiết dịch vụ →</a></p></div>
    <div class="box left"><h3>Landing page</h3>
      <p>Trang đích một mục tiêu, tối ưu tỷ lệ chuyển đổi cho chiến dịch quảng cáo.</p>
      <p><a href="/dich-vu/thiet-ke-landing-page/">Chi tiết dịch vụ →</a></p></div>
    <div class="box left"><h3>SEO tổng thể</h3>
      <p>Kéo toàn bộ traffic tự nhiên của website đi lên, không chỉ vài từ khóa lẻ.</p>
      <p><a href="/dich-vu/dich-vu-seo-tong-the/">Chi tiết dịch vụ →</a></p></div>
    <div class="box left"><h3>SEO từ khóa</h3>
      <p>Cam kết thứ hạng cho nhóm từ khóa bạn chọn, thanh toán theo kết quả.</p>
      <p><a href="/dich-vu/seo-tu-khoa/">Chi tiết dịch vụ →</a></p></div>
    <div class="box left"><h3>SEO Local</h3>
      <p>Lên top bản đồ Google cho cửa hàng, phòng khám, showroom trong bán kính 5km.</p>
      <p><a href="/dich-vu/seo-local-google-maps/">Chi tiết dịch vụ →</a></p></div>
    <div class="box left"><h3>Audit website</h3>
      <p>Soi 27 điểm kỹ thuật, nội dung và backlink, trả về báo cáo hành động.</p>
      <p><a href="/dich-vu/audit-website/">Chi tiết dịch vụ →</a></p></div>
    <div class="box left"><h3>Tối ưu tốc độ</h3>
      <p>Đưa điểm PageSpeed lên 90+ và Core Web Vitals về ngưỡng xanh.</p>
      <p><a href="/dich-vu/toi-uu-toc-do-website/">Chi tiết dịch vụ →</a></p></div>
  </div>
</div></div>

{{cta}}

<div class="sec"><div class="wrap">
  <div class="sectitle"><div class="stars">★★★★★</div>
    <h2>Bảng giá thiết kế website trọn gói</h2>
    <p>Giá đã bao gồm hosting năm đầu, chứng chỉ SSL và hướng dẫn sử dụng.
    Không phát sinh sau khi ký hợp đồng.</p>
  </div>
  {{pricing}}
  <p style="text-align:center;margin-top:18px">
    <a class="btn btn-b" href="/bang-gia/">Xem chi tiết bảng giá &amp; gói SEO</a></p>
</div></div>

<div class="sec alt"><div class="wrap">
  <div class="sectitle"><div class="stars">★★★★★</div>
    <h2>Quy trình 6 bước</h2>
    <p>Bạn luôn biết dự án đang ở bước nào và bước tiếp theo cần gì ở bạn.</p></div>
  {{steps}}
  <p style="text-align:center;margin-top:18px">
    <a class="btn btn-g" href="/quy-trinh/">Xem quy trình đầy đủ</a></p>
</div></div>

<div class="sec"><div class="wrap">
  <div class="sectitle"><div class="stars">★★★★★</div>
    <h2>Khách hàng nói gì</h2></div>
  {{tm}}
</div></div>

<div class="sec alt"><div class="wrap">
  <div class="sectitle"><div class="stars">★★★★★</div>
    <h2>Kiến thức website &amp; SEO</h2>
    <p>Chúng tôi viết lại những gì thực sự dùng trong dự án, không sao chép.</p></div>
  <div class="cardlist">
    <div class="card"><div class="cb"><h3><a href="/kien-thuc/seo-la-gi/">SEO là gì? Hiểu đúng trước khi tiêu tiền</a></h3>
      <p>SEO không phải mẹo vặt để lừa Google. Bài này giải thích cơ chế xếp hạng và
      những gì bạn thực sự mua khi thuê dịch vụ SEO.</p>
      <a class="btn btn-g btn-sm" href="/kien-thuc/seo-la-gi/">Đọc tiếp</a></div></div>
    <div class="card"><div class="cb"><h3><a href="/kien-thuc/checklist-seo-onpage/">Checklist SEO onpage 27 điểm</a></h3>
      <p>Danh sách kiểm tra chúng tôi chạy trên mọi website trước khi bàn giao —
      bạn có thể tự soi website của mình.</p>
      <a class="btn btn-g btn-sm" href="/kien-thuc/checklist-seo-onpage/">Đọc tiếp</a></div></div>
    <div class="card"><div class="cb"><h3><a href="/kien-thuc/core-web-vitals-la-gi/">Core Web Vitals là gì?</a></h3>
      <p>LCP, INP, CLS: ba chỉ số Google dùng để đo trải nghiệm trang, và ngưỡng
      nào mới được coi là đạt.</p>
      <a class="btn btn-g btn-sm" href="/kien-thuc/core-web-vitals-la-gi/">Đọc tiếp</a></div></div>
  </div>
</div></div>

<div class="sec"><div class="wrap"><div class="cols">
<div class="content">
<h2>WiThemes – công ty thiết kế website và SEO tại TP. Hồ Chí Minh</h2>
<p>WiThemes thành lập tháng 7/2024, trụ sở tại Phường Tân Định, TP. Hồ Chí Minh.
Chúng tôi làm hai việc và chỉ hai việc: <strong>dựng website</strong> và
<strong>đưa website lên top tìm kiếm</strong>. Không ôm đồm chạy quảng cáo,
không bán phần mềm, không làm thương hiệu chung chung.</p>
<p>Điểm khác biệt nằm ở chỗ hai việc đó do cùng một đội làm. Người viết code biết
người làm SEO sẽ cần gì: cấu trúc heading sạch, URL ngắn, breadcrumb có dữ liệu
cấu trúc, ảnh nén sẵn, không chèn thư viện JavaScript thừa. Vì vậy website bàn giao
xong là đã sẵn sàng để SEO, thay vì phải đập ra làm lại sau sáu tháng.</p>
<h3>Chúng tôi phù hợp với ai?</h3>
<ul>
  <li>Doanh nghiệp vừa và nhỏ cần một website nghiêm túc thay cho trang Facebook.</li>
  <li>Cửa hàng, nhà hàng, spa, phòng khám muốn khách tìm thấy trên Google Maps.</li>
  <li>Website cũ chạy chậm, không lên hạng, cần audit và làm lại phần kỹ thuật.</li>
  <li>Đơn vị đã có website nhưng cần một đội SEO đi đường dài, có báo cáo rõ ràng.</li>
</ul>
<h3>Chúng tôi không phù hợp với ai?</h3>
<p>Nếu bạn cần lên top sau hai tuần, hoặc cần một website 500.000đ, chúng tôi không
phải lựa chọn đúng. SEO là công việc tính bằng tháng, và một website làm cẩu thả sẽ
tốn của bạn nhiều hơn số tiền tiết kiệm được lúc đầu.</p>
<p>Xem thêm: <a href="/gioi-thieu/">giới thiệu về WiThemes</a>,
<a href="/quy-trinh/">quy trình làm việc</a>,
<a href="/du-an/">một vài dự án đã thực hiện</a>.</p>
{{faq}}
</div>
{{sidebar}}
</div></div></div>
"""

WHY = boxes([
    ("🏆", "Khẳng định uy tín", "Khách hàng tra tên công ty trước khi liên hệ. Không có website, bạn mất điểm ngay từ vòng đầu."),
    ("🕐", "Bán hàng 24/7", "Website không nghỉ trưa, không nghỉ lễ. Form và chatbox nhận yêu cầu cả lúc bạn đang ngủ."),
    ("📈", "Traffic không mất phí click", "Quảng cáo dừng là hết khách. Thứ hạng tự nhiên vẫn kéo khách về sau khi ngừng chi tiền."),
    ("🎯", "Nền tảng để chạy marketing", "Có website mới chạy được remarketing, đo chuyển đổi và gom dữ liệu khách hàng."),
])

STEPS6 = steps([
    ("Tiếp nhận yêu cầu", "Trao đổi qua điện thoại hoặc gặp trực tiếp: bạn bán gì, khách là ai, đối thủ là ai."),
    ("Khảo sát &amp; lên kế hoạch", "Phân tích đối thủ, chốt sơ đồ trang, danh sách tính năng và bộ từ khóa mục tiêu."),
    ("Báo giá &amp; ký hợp đồng", "Báo giá trọn gói kèm tiến độ. Tạm ứng 50%, phần còn lại thanh toán khi bàn giao."),
    ("Thiết kế giao diện", "Bạn duyệt bản thiết kế trước khi lập trình. Sửa tối đa 3 vòng, không tính phí."),
    ("Lập trình &amp; tối ưu", "Dựng website, nhập nội dung, chạy checklist SEO onpage 27 điểm và đo tốc độ."),
    ("Bàn giao &amp; đồng hành", "Bàn giao mã nguồn, hướng dẫn quản trị, bảo hành 12 tháng và hỗ trợ khi cần."),
])

HOME_FAQ, HOME_FAQ_LD = faq([
    ("Thiết kế website mất bao lâu?",
     "Website giới thiệu 5–7 trang: 7–10 ngày làm việc. Website doanh nghiệp: 10–15 ngày. "
     "Website bán hàng hoặc thiết kế riêng từ Figma: 20–30 ngày. Mốc thời gian được ghi vào hợp đồng."),
    ("Chi phí thiết kế website là bao nhiêu?",
     "Trọn gói từ 2.500.000đ cho gói cơ bản đến 8.000.000đ cho website bán hàng. Dự án thiết kế "
     "riêng từ 25.000.000đ. Xem chi tiết tại trang bảng giá."),
    ("SEO bao lâu thì lên top?",
     "Từ khóa ngách ít cạnh tranh: 2–3 tháng. Từ khóa dịch vụ ở thành phố lớn: 4–8 tháng. "
     "Không ai đảm bảo được mốc chính xác; ai hứa 2 tuần lên top là đang bán cho bạn rủi ro."),
    ("Tôi có được sở hữu mã nguồn không?",
     "Có. Sau khi thanh toán đủ, bạn nhận toàn bộ mã nguồn, cơ sở dữ liệu và tài khoản quản trị. "
     "Chúng tôi không khóa website để giữ khách."),
    ("Website có tự sửa nội dung được không?",
     "Được. Bạn có trang quản trị tiếng Việt để đăng bài, sửa sản phẩm, đổi ảnh và thông tin liên hệ "
     "mà không cần biết lập trình. Chúng tôi có buổi hướng dẫn 60 phút khi bàn giao."),
    ("Có hỗ trợ sau khi bàn giao không?",
     "Bảo hành 12 tháng cho lỗi kỹ thuật. Ngoài ra có gói chăm sóc website hằng tháng nếu bạn muốn "
     "chúng tôi cập nhật, sao lưu và theo dõi tốc độ định kỳ."),
])

HOME = {
    "slug": "/",
    "title": "Thiết kế website &amp; dịch vụ SEO trọn gói | WiThemes",
    "desc": "WiThemes – công ty thiết kế website chuẩn SEO và dịch vụ SEO tại TP.HCM. "
            "Trọn gói từ 2.500.000đ, tặng hosting và tên miền, bàn giao 7–15 ngày.",
    "h1": "WiThemes",
    "sidebar": False,
    "hero": HERO,
    "body": fill(HOME_BODY, why=WHY, cta=cta(), pricing=pricing(),
                 steps=STEPS6, tm=TESTIMONIALS, faq=HOME_FAQ),
    "ld": [HOME_FAQ_LD],
}

ABOUT = {
    "slug": "/gioi-thieu/",
    "title": "Giới thiệu WiThemes – công ty thiết kế website và SEO",
    "desc": "WiThemes thành lập 7/2024 tại TP. Hồ Chí Minh, chuyên thiết kế website chuẩn SEO "
            "và dịch vụ SEO cho doanh nghiệp vừa và nhỏ.",
    "h1": "Giới thiệu WiThemes",
    "crumb": [],
    "body": """
<h2>Chúng tôi là ai</h2>
<p>WiThemes là công ty thiết kế website và SEO, thành lập tháng 7/2024, trụ sở tại
114 Điện Biên Phủ, Phường Tân Định, Thành phố Hồ Chí Minh. Mã số thuế 0318552411.</p>
<p>Đội ngũ hiện tại gồm những người làm giao diện, lập trình và SEO đã đi qua vài trăm
website trước khi công ty ra đời. Chúng tôi cố tình giữ quy mô nhỏ để mỗi dự án đều có
một người chịu trách nhiệm từ đầu đến cuối, thay vì chuyền tay qua bốn bộ phận.</p>

<h2>Chúng tôi làm gì</h2>
<p>Hai mảng, và chúng bổ trợ cho nhau:</p>
<ul>
  <li><strong><a href="/dich-vu/thiet-ke-website/">Thiết kế website</a></strong> – từ website
  giới thiệu doanh nghiệp, <a href="/dich-vu/thiet-ke-website-ban-hang/">website bán hàng</a>
  đến <a href="/dich-vu/thiet-ke-landing-page/">landing page</a> cho chiến dịch quảng cáo.</li>
  <li><strong><a href="/dich-vu/dich-vu-seo-tong-the/">Dịch vụ SEO</a></strong> – SEO tổng thể,
  <a href="/dich-vu/seo-tu-khoa/">SEO từ khóa</a>,
  <a href="/dich-vu/seo-local-google-maps/">SEO Local trên Google Maps</a>,
  <a href="/dich-vu/audit-website/">audit</a> và
  <a href="/dich-vu/toi-uu-toc-do-website/">tối ưu tốc độ</a>.</li>
</ul>

<h2>Cách chúng tôi làm việc</h2>
<p>Ba nguyên tắc, viết ra để bạn có cái mà đối chiếu:</p>
<h3>1. Báo giá trọn gói, không phát sinh</h3>
<p>Phạm vi công việc được liệt kê trong hợp đồng. Nếu bạn phát sinh yêu cầu mới, chúng tôi
báo giá phần thêm trước khi làm, không âm thầm tính vào cuối dự án.</p>
<h3>2. Bàn giao là bàn giao thật</h3>
<p>Mã nguồn, cơ sở dữ liệu, tài khoản quản trị, tài khoản hosting đều thuộc về bạn. Chúng tôi
không giữ chìa khóa để ràng buộc khách hàng ở lại.</p>
<h3>3. Số liệu thay cho lời hứa</h3>
<p>Mỗi tháng bạn nhận một báo cáo: thứ hạng từ khóa, lưu lượng tự nhiên, số form gửi về, và
việc đã làm trong tháng. Nếu chỉ số đi ngang, chúng tôi nói rõ vì sao và đổi cách làm.</p>

<h2>Vài con số</h2>
<table>
<thead><tr><th>Chỉ tiêu</th><th>Thực tế</th></tr></thead>
<tbody>
<tr><td>Thành lập</td><td>Tháng 7/2024</td></tr>
<tr><td>Thời gian bàn giao trung bình</td><td>12 ngày làm việc</td></tr>
<tr><td>Điểm PageSpeed mobile khi bàn giao</td><td>Tối thiểu 85/100</td></tr>
<tr><td>Thời gian bảo hành</td><td>12 tháng</td></tr>
<tr><td>Thời gian phản hồi hỗ trợ</td><td>Trong ngày làm việc</td></tr>
</tbody>
</table>

<h2>Bước tiếp theo</h2>
<p>Nếu bạn đang cân nhắc, cách nhanh nhất là gửi cho chúng tôi địa chỉ website hiện tại
(nếu có) và mô tả ngắn về việc bạn muốn đạt được. Chúng tôi trả lời kèm nhận xét cụ thể,
miễn phí, không kèm điều kiện.</p>
<p><a class="btn btn-g" href="/lien-he/">Gửi yêu cầu tư vấn</a></p>
""",
}

SERVICE_HUB = {
    "slug": "/dich-vu/",
    "title": "Dịch vụ thiết kế website và SEO | WiThemes",
    "desc": "Danh sách dịch vụ WiThemes: thiết kế website chuẩn SEO, website bán hàng, "
            "landing page, SEO tổng thể, SEO từ khóa, SEO Local, audit và tối ưu tốc độ.",
    "h1": "Dịch vụ của WiThemes",
    "crumb": [],
    "body": """
<h2>Tám dịch vụ, một đầu mối</h2>
<p>Bạn có thể đặt riêng từng dịch vụ, hoặc gộp website và SEO thành một hợp đồng để
tiết kiệm 15–20% chi phí và tránh cảnh hai nhà cung cấp đổ lỗi cho nhau.</p>

<h2>Nhóm thiết kế website</h2>
<table>
<thead><tr><th>Dịch vụ</th><th>Phù hợp với</th><th>Giá từ</th><th>Thời gian</th></tr></thead>
<tbody>
<tr><td><a href="/dich-vu/thiet-ke-website/">Thiết kế website chuẩn SEO</a></td>
    <td>Doanh nghiệp cần website giới thiệu nghiêm túc</td><td>2.500.000đ</td><td>7–15 ngày</td></tr>
<tr><td><a href="/dich-vu/thiet-ke-website-ban-hang/">Thiết kế website bán hàng</a></td>
    <td>Shop, thương hiệu bán trực tiếp cho khách lẻ</td><td>8.000.000đ</td><td>20–30 ngày</td></tr>
<tr><td><a href="/dich-vu/thiet-ke-landing-page/">Thiết kế landing page</a></td>
    <td>Chiến dịch quảng cáo, ra mắt sản phẩm</td><td>3.000.000đ</td><td>5–7 ngày</td></tr>
</tbody>
</table>

<h2>Nhóm SEO</h2>
<table>
<thead><tr><th>Dịch vụ</th><th>Phù hợp với</th><th>Giá từ</th><th>Thời gian thấy kết quả</th></tr></thead>
<tbody>
<tr><td><a href="/dich-vu/dich-vu-seo-tong-the/">SEO tổng thể</a></td>
    <td>Website nhiều sản phẩm/dịch vụ, muốn tăng traffic toàn diện</td>
    <td>12.000.000đ/tháng</td><td>3–6 tháng</td></tr>
<tr><td><a href="/dich-vu/seo-tu-khoa/">SEO từ khóa</a></td>
    <td>Cần lên top một nhóm từ khóa cụ thể</td>
    <td>5.000.000đ/tháng</td><td>2–6 tháng</td></tr>
<tr><td><a href="/dich-vu/seo-local-google-maps/">SEO Local – Google Maps</a></td>
    <td>Cửa hàng, phòng khám, showroom có địa chỉ vật lý</td>
    <td>4.000.000đ/tháng</td><td>1–3 tháng</td></tr>
</tbody>
</table>

<h2>Nhóm kỹ thuật</h2>
<table>
<thead><tr><th>Dịch vụ</th><th>Phù hợp với</th><th>Giá từ</th><th>Thời gian</th></tr></thead>
<tbody>
<tr><td><a href="/dich-vu/audit-website/">Audit website</a></td>
    <td>Website đã chạy nhưng không lên hạng, không rõ vì sao</td>
    <td>3.000.000đ</td><td>5 ngày làm việc</td></tr>
<tr><td><a href="/dich-vu/toi-uu-toc-do-website/">Tối ưu tốc độ website</a></td>
    <td>Website tải chậm, điểm PageSpeed thấp, khách thoát sớm</td>
    <td>4.000.000đ</td><td>5–10 ngày</td></tr>
</tbody>
</table>

<h2>Không chắc nên chọn gì?</h2>
<p>Trả lời ba câu này là ra:</p>
<ol>
  <li><strong>Bạn đã có website chưa?</strong> Chưa → nhóm thiết kế. Rồi → nhóm SEO hoặc kỹ thuật.</li>
  <li><strong>Khách của bạn ở đâu?</strong> Đến tận nơi → SEO Local. Toàn quốc → SEO tổng thể.</li>
  <li><strong>Bạn cần kết quả trong bao lâu?</strong> Dưới 1 tháng → landing page + quảng cáo.
  Trên 3 tháng → SEO.</li>
</ol>
<p>Hoặc để chúng tôi xem website của bạn và nói thẳng cái gì đáng làm trước:
<a href="/lien-he/">gửi yêu cầu tại đây</a>.</p>
""",
}

PRICING_PAGE = {
    "slug": "/bang-gia/",
    "title": "Bảng giá thiết kế website và dịch vụ SEO 2026 | WiThemes",
    "desc": "Bảng giá thiết kế website trọn gói từ 2.500.000đ và bảng giá dịch vụ SEO "
            "từ 4.000.000đ/tháng. Giá rõ ràng, không phát sinh, đã gồm hosting và SSL.",
    "h1": "Bảng giá thiết kế website &amp; SEO",
    "crumb": [],
    "sidebar": False,
    "body": """
<div class="sec"><div class="wrap">
<div class="sectitle"><div class="stars">★★★★★</div><h2>Bảng giá thiết kế website</h2>
<p>Giá trọn gói, đã bao gồm hosting năm đầu, chứng chỉ SSL, buổi hướng dẫn quản trị
và bảo hành. Chưa bao gồm 8% thuế GTGT nếu xuất hóa đơn.</p></div>
{{pricing}}
</div></div>

<div class="sec alt"><div class="wrap"><div class="cols"><div class="content">
<h2>Bảng giá dịch vụ SEO</h2>
<p>SEO tính theo tháng, hợp đồng tối thiểu 6 tháng vì dưới mốc đó gần như không kịp
thấy kết quả có ý nghĩa.</p>
<table>
<thead><tr><th>Gói</th><th>Phạm vi</th><th>Nội dung/tháng</th><th>Chi phí/tháng</th></tr></thead>
<tbody>
<tr><td><strong>SEO Local</strong></td>
    <td>Google Business Profile + 5–10 từ khóa khu vực</td><td>4 bài</td><td>4.000.000đ</td></tr>
<tr><td><strong>SEO từ khóa</strong></td>
    <td>10–20 từ khóa mục tiêu do bạn chọn</td><td>8 bài</td><td>5.000.000đ</td></tr>
<tr><td><strong>SEO tổng thể</strong></td>
    <td>Toàn bộ website, không giới hạn từ khóa</td><td>16 bài</td><td>12.000.000đ</td></tr>
<tr><td><strong>SEO doanh nghiệp</strong></td>
    <td>Nhiều chi nhánh / nhiều ngôn ngữ</td><td>Theo kế hoạch</td><td>Liên hệ</td></tr>
</tbody>
</table>

<h2>Chi phí duy trì hằng năm</h2>
<p>Từ năm thứ hai trở đi, bạn chỉ trả phí duy trì. Bạn có thể tự mua và tự quản lý nếu muốn —
chúng tôi bàn giao đầy đủ thông tin.</p>
<table>
<thead><tr><th>Khoản mục</th><th>Chi phí/năm</th><th>Ghi chú</th></tr></thead>
<tbody>
<tr><td>Tên miền .com</td><td>320.000đ</td><td>Năm đầu miễn phí với gói Pro trở lên</td></tr>
<tr><td>Tên miền .vn</td><td>750.000đ</td><td>Cần giấy tờ đăng ký chủ thể</td></tr>
<tr><td>Hosting website giới thiệu</td><td>900.000đ</td><td>Năm đầu miễn phí</td></tr>
<tr><td>Hosting website bán hàng</td><td>1.800.000đ</td><td>Băng thông và dung lượng cao hơn</td></tr>
<tr><td>Chứng chỉ SSL</td><td>0đ</td><td>Let's Encrypt, tự động gia hạn</td></tr>
<tr><td>Chăm sóc website (tùy chọn)</td><td>500.000đ/tháng</td><td>Cập nhật, sao lưu, theo dõi tốc độ</td></tr>
</tbody>
</table>

<h2>Những gì làm giá thay đổi</h2>
<ul>
  <li><strong>Số lượng trang và sản phẩm.</strong> Nhập liệu 50 sản phẩm khác hẳn 5.000 sản phẩm.</li>
  <li><strong>Thiết kế riêng hay dùng mẫu.</strong> Thiết kế từ đầu trên Figma cộng thêm 8–15 triệu.</li>
  <li><strong>Tính năng đặc thù.</strong> Đặt lịch, tính vận chuyển theo vùng, đồng bộ kho, đa ngôn ngữ.</li>
  <li><strong>Nội dung.</strong> Bạn tự cung cấp thì miễn phí; chúng tôi viết thì 250.000đ/bài 1.000 chữ.</li>
  <li><strong>Độ cạnh tranh từ khóa.</strong> Với SEO, "sửa máy lạnh quận 7" và "vé máy bay giá rẻ"
  là hai thế giới khác nhau.</li>
</ul>

<h2>Điều khoản thanh toán</h2>
<ol>
  <li>Tạm ứng 50% khi ký hợp đồng.</li>
  <li>30% khi duyệt xong giao diện.</li>
  <li>20% còn lại khi bàn giao và nghiệm thu.</li>
</ol>
<p>Hợp đồng SEO thanh toán vào đầu mỗi tháng, có thể dừng sau khi hết cam kết tối thiểu
với thông báo trước 15 ngày.</p>
{{faq}}
<p><a class="btn btn-r" href="/lien-he/">Nhận báo giá cho dự án của bạn</a></p>
</div>{{sidebar}}</div></div></div>
{{cta}}
""",
}

_PRICE_FAQ, _PRICE_FAQ_LD = faq([
    ("Giá trên đã là giá cuối chưa?",
     "Với các gói website liệt kê ở trên thì đúng — đó là giá trọn gói cho đúng phạm vi mô tả. "
     "Chi phí chỉ thay đổi nếu bạn yêu cầu thêm tính năng hoặc thêm số lượng trang, và luôn được "
     "báo giá trước khi làm."),
    ("Có phải trả phí duy trì hằng tháng cho website không?",
     "Không bắt buộc. Website chỉ cần tên miền và hosting hằng năm. Gói chăm sóc 500.000đ/tháng "
     "là tùy chọn dành cho khách không muốn tự cập nhật và sao lưu."),
    ("Ký hợp đồng SEO tối thiểu bao lâu?",
     "6 tháng. Dưới mốc này thường chưa đủ để nội dung mới được đánh giá và xếp hạng, nên cam kết "
     "ngắn hơn sẽ không công bằng cho cả hai bên."),
    ("Có xuất hóa đơn VAT không?",
     "Có. Giá niêm yết chưa bao gồm 8% thuế GTGT; nếu bạn cần hóa đơn, phần thuế được cộng vào "
     "hợp đồng."),
])
PRICING_PAGE["body"] = fill(PRICING_PAGE["body"], pricing=pricing(),
                            faq=_PRICE_FAQ, cta=cta())
PRICING_PAGE["ld"] = [_PRICE_FAQ_LD]

PROCESS = {
    "slug": "/quy-trinh/",
    "title": "Quy trình thiết kế website và triển khai SEO | WiThemes",
    "desc": "Quy trình 6 bước của WiThemes: tiếp nhận yêu cầu, khảo sát, báo giá, thiết kế, "
            "lập trình và bàn giao — kèm mốc thời gian và việc bạn cần chuẩn bị.",
    "h1": "Quy trình làm việc",
    "crumb": [],
    "body": """
<h2>Sáu bước, và bạn cần gì ở mỗi bước</h2>
<p>Phần lớn dự án chậm tiến độ không phải vì lập trình, mà vì thiếu nội dung hoặc chờ duyệt.
Bảng dưới ghi rõ ai làm gì để tránh chuyện đó.</p>

<table>
<thead><tr><th>Bước</th><th>WiThemes làm</th><th>Bạn cần chuẩn bị</th><th>Thời gian</th></tr></thead>
<tbody>
<tr><td>1. Tiếp nhận yêu cầu</td>
    <td>Hỏi về sản phẩm, khách hàng, đối thủ, ngân sách</td>
    <td>Logo, thông tin công ty, website đối thủ bạn thích</td><td>1 ngày</td></tr>
<tr><td>2. Khảo sát &amp; kế hoạch</td>
    <td>Phân tích đối thủ, dựng sơ đồ trang, chốt bộ từ khóa</td>
    <td>Duyệt sơ đồ trang</td><td>2–3 ngày</td></tr>
<tr><td>3. Báo giá &amp; hợp đồng</td>
    <td>Báo giá trọn gói, tiến độ, điều khoản bảo hành</td>
    <td>Ký hợp đồng, tạm ứng 50%</td><td>1 ngày</td></tr>
<tr><td>4. Thiết kế giao diện</td>
    <td>Thiết kế trang chủ và 2–3 trang tiêu biểu</td>
    <td>Phản hồi trong 3 ngày, tối đa 3 vòng sửa</td><td>3–7 ngày</td></tr>
<tr><td>5. Lập trình &amp; tối ưu</td>
    <td>Dựng website, nhập nội dung, chạy checklist 27 điểm</td>
    <td>Gửi nội dung và hình ảnh</td><td>5–15 ngày</td></tr>
<tr><td>6. Bàn giao</td>
    <td>Bàn giao mã nguồn, hướng dẫn 60 phút, kích hoạt bảo hành</td>
    <td>Nghiệm thu, thanh toán phần còn lại</td><td>1 ngày</td></tr>
</tbody>
</table>

<h2>Quy trình SEO hằng tháng</h2>
<p>Với hợp đồng SEO, chu kỳ lặp lại theo tháng và luôn kết thúc bằng một báo cáo:</p>
{{steps}}

<h2>Bạn nhận được gì trong báo cáo tháng</h2>
<ul>
  <li>Bảng thứ hạng từ khóa: vị trí đầu tháng, cuối tháng, chênh lệch.</li>
  <li>Lưu lượng tự nhiên từ Google Search Console: hiển thị, click, CTR.</li>
  <li>Số lượt gọi, form gửi và tin nhắn phát sinh từ kênh tự nhiên.</li>
  <li>Danh sách việc đã làm: bài viết, chỉnh sửa kỹ thuật, backlink.</li>
  <li>Kế hoạch tháng sau và những gì cần bạn duyệt.</li>
</ul>

<blockquote>Nếu một tháng chỉ số đi lùi, báo cáo vẫn ghi đúng như vậy kèm giả thuyết nguyên nhân.
Che số liệu xấu chỉ làm bạn phát hiện muộn hơn.</blockquote>

<h2>Cam kết tiến độ</h2>
<p>Nếu dự án chậm tiến độ do lỗi của chúng tôi, mỗi ngày chậm được giảm 1% giá trị hợp đồng,
tối đa 10%. Điều khoản này nằm trong hợp đồng, không phải lời nói miệng.</p>
<p>Xem thêm <a href="/bang-gia/">bảng giá</a> và
<a href="/cau-hoi-thuong-gap/">câu hỏi thường gặp</a>.</p>
""",
}
PROCESS["body"] = fill(PROCESS["body"], steps=steps([
    ("Phân tích &amp; lập kế hoạch", "Rà từ khóa, đối thủ, khoảng trống nội dung của tháng."),
    ("Tối ưu kỹ thuật", "Sửa lỗi index, tốc độ, dữ liệu cấu trúc, liên kết nội bộ."),
    ("Sản xuất nội dung", "Viết mới và cập nhật bài cũ theo ý định tìm kiếm."),
    ("Xây dựng liên kết", "Đặt bài trên báo và trang uy tín, không dùng hệ thống spam."),
    ("Đo lường", "Theo dõi thứ hạng, traffic và chuyển đổi hằng tuần."),
    ("Báo cáo &amp; điều chỉnh", "Gửi báo cáo, họp 30 phút, chốt kế hoạch tháng kế tiếp."),
]))

PROJECTS = {
    "slug": "/du-an/",
    "title": "Dự án website đã thực hiện | WiThemes",
    "desc": "Một vài giao diện website tham khảo thuộc các lĩnh vực nhà hàng, spa và "
            "cửa hàng bánh — minh họa phong cách thiết kế WiThemes hướng tới.",
    "h1": "Dự án &amp; giao diện tham khảo",
    "crumb": [],
    "sidebar": False,
    "body": """
<div class="sec"><div class="wrap"><div class="cols"><div class="content">
<h2>Một vài giao diện website tham khảo</h2>
<p>Dưới đây là các giao diện chúng tôi lấy làm tham chiếu về bố cục và trải nghiệm khi
tư vấn cho khách. Đây là website của các đơn vị khác, không phải sản phẩm do WiThemes
thực hiện — chúng tôi để ở đây để bạn hình dung phong cách mà chúng tôi hướng tới.</p>

<div class="cardlist">
  <div class="card">
    <img src="/assets/site-restaurant.jpg" alt="Giao diện website nhà hàng Ý với ảnh lớn và thực đơn rõ ràng" loading="lazy">
    <div class="cb"><h3>Nhà hàng</h3>
    <p>Ảnh món ăn cỡ lớn, thực đơn dễ đọc trên điện thoại, nút đặt bàn bám theo màn hình.</p></div>
  </div>
  <div class="card">
    <img src="/assets/site-spa.jpg" alt="Giao diện website spa với tông màu trầm và mục đặt lịch" loading="lazy">
    <div class="cb"><h3>Spa &amp; chăm sóc sức khỏe</h3>
    <p>Tông màu trầm, bảng dịch vụ kèm giá, biểu mẫu đặt lịch ngắn gọn ba trường.</p></div>
  </div>
  <div class="card">
    <img src="/assets/site-bakery.jpg" alt="Giao diện website tiệm bánh với lưới sản phẩm" loading="lazy">
    <div class="cb"><h3>Tiệm bánh &amp; cửa hàng</h3>
    <p>Lưới sản phẩm gọn, giỏ hàng đơn giản, ưu tiên tốc độ tải trên mạng di động.</p></div>
  </div>
</div>

<h2>Chúng tôi thiết kế cho những ngành nào?</h2>
<div class="grid g4" style="margin-top:14px">
  <div class="box"><div class="ico">🍜</div><h3>Nhà hàng &amp; cà phê</h3><p>Thực đơn, đặt bàn, chi nhánh.</p></div>
  <div class="box"><div class="ico">💆</div><h3>Spa &amp; thẩm mỹ</h3><p>Bảng dịch vụ, đặt lịch, khuyến mãi.</p></div>
  <div class="box"><div class="ico">🏗️</div><h3>Xây dựng &amp; nội thất</h3><p>Thư viện công trình, báo giá.</p></div>
  <div class="box"><div class="ico">🏥</div><h3>Phòng khám</h3><p>Chuyên khoa, bác sĩ, đặt hẹn.</p></div>
  <div class="box"><div class="ico">🎓</div><h3>Giáo dục</h3><p>Khóa học, đăng ký, học liệu.</p></div>
  <div class="box"><div class="ico">🏠</div><h3>Bất động sản</h3><p>Dự án, bộ lọc, bản đồ.</p></div>
  <div class="box"><div class="ico">👗</div><h3>Thời trang</h3><p>Bộ sưu tập, size, giỏ hàng.</p></div>
  <div class="box"><div class="ico">🚚</div><h3>Vận tải &amp; logistics</h3><p>Tra cứu, bảng cước.</p></div>
</div>

<h2>Muốn xem bản demo cho ngành của bạn?</h2>
<p>Cho chúng tôi biết lĩnh vực và ba website bạn thấy đẹp, chúng tôi gửi lại đề xuất bố cục
kèm báo giá. Xem trước <a href="/bang-gia/">bảng giá</a> hoặc
<a href="/quy-trinh/">quy trình làm việc</a>.</p>
<p><a class="btn btn-g" href="/lien-he/">Yêu cầu demo miễn phí</a></p>
</div>%(sidebar)s</div></div></div>
""".replace("%(sidebar)s", "{{sidebar}}"),
}

FAQ_ITEMS = [
    ("Thiết kế website là gì?",
     "Là toàn bộ quá trình dựng nên một trang web hoàn chỉnh: lên cấu trúc thông tin, thiết kế "
     "giao diện, lập trình, nhập nội dung, tối ưu tốc độ và đưa lên tên miền. Một website được "
     "thiết kế tử tế phải đọc được trên điện thoại, tải nhanh và cho phép chủ website tự cập nhật."),
    ("Thiết kế web chuẩn SEO nghĩa là gì?",
     "Nghĩa là ngay từ khi dựng, website đã đáp ứng các yêu cầu kỹ thuật để Google hiểu và xếp hạng: "
     "một thẻ H1 duy nhất mỗi trang, cấu trúc heading đúng thứ bậc, URL ngắn và có dấu gạch nối, "
     "thẻ tiêu đề và mô tả riêng cho từng trang, dữ liệu có cấu trúc, sitemap.xml, ảnh có thẻ alt "
     "và được nén, tốc độ tải dưới 3 giây, giao diện responsive."),
    ("Tôi cần chuẩn bị gì trước khi làm website?",
     "Bốn thứ: logo (file gốc nếu có), thông tin công ty và liên hệ, danh sách sản phẩm/dịch vụ, "
     "và hình ảnh thật của bạn. Nếu chưa có nội dung, chúng tôi có thể viết giúp với chi phí "
     "250.000đ cho mỗi bài khoảng 1.000 chữ."),
    ("Website có tự quản trị được không?",
     "Được. Bạn có trang quản trị tiếng Việt để đăng bài, sửa sản phẩm, đổi banner và thông tin "
     "liên hệ. Khi bàn giao có một buổi hướng dẫn 60 phút và tài liệu hướng dẫn dạng video."),
    ("Bao lâu thì website lên top Google?",
     "Bản thân việc có website mới không đưa bạn lên top. Sau khi website được index (1–2 tuần), "
     "thứ hạng phụ thuộc vào nội dung và độ cạnh tranh: từ khóa ngách 2–3 tháng, từ khóa dịch vụ "
     "ở thành phố lớn 4–8 tháng."),
    ("Có cam kết thứ hạng không?",
     "Với gói SEO từ khóa, chúng tôi cam kết số lượng từ khóa vào top 10 sau thời hạn thỏa thuận; "
     "nếu không đạt, phần chưa đạt được bù thêm thời gian triển khai. Chúng tôi không cam kết vị "
     "trí số 1 cho một từ khóa cụ thể — không đơn vị nào kiểm soát được điều đó."),
    ("Website có bị mất khi ngừng hợp tác không?",
     "Không. Mã nguồn, cơ sở dữ liệu và tên miền đứng tên bạn. Khi kết thúc hợp tác, chúng tôi bàn "
     "giao đầy đủ và hỗ trợ chuyển sang đơn vị mới nếu bạn cần."),
    ("Cần đặt cọc bao nhiêu?",
     "50% khi ký hợp đồng, 30% khi duyệt giao diện, 20% khi nghiệm thu. Với hợp đồng SEO thì "
     "thanh toán theo tháng, vào đầu kỳ."),
    ("Bảo hành website gồm những gì?",
     "12 tháng cho các lỗi kỹ thuật phát sinh từ phần chúng tôi bàn giao: lỗi hiển thị, lỗi chức "
     "năng, lỗi bảo mật do cấu hình. Không bao gồm nội dung bạn tự thêm hoặc plugin bên thứ ba "
     "bạn tự cài."),
    ("Website có chạy tốt trên điện thoại không?",
     "Có. Mọi dự án đều được kiểm tra trên các độ phân giải phổ biến từ 360px trở lên, và điểm "
     "PageSpeed mobile tối thiểu 85/100 khi bàn giao."),
    ("Tôi đã có website rồi, có cần làm lại không?",
     "Chưa chắc. Hãy đặt một buổi audit trước — nếu vấn đề chỉ nằm ở tốc độ, cấu trúc heading hay "
     "thiếu nội dung, sửa sẽ rẻ hơn làm lại nhiều. Chúng tôi chỉ đề nghị làm lại khi nền tảng cũ "
     "thực sự cản trở."),
    ("WiThemes có nhận khách ngoài TP.HCM không?",
     "Có. Phần lớn dự án làm việc từ xa qua điện thoại, email và Zalo. Chúng tôi nhận khách trên "
     "toàn quốc; với khách ở TP.HCM có thể gặp trực tiếp nếu cần."),
]

_FAQ_HTML, _FAQ_LD = faq(FAQ_ITEMS)

FAQ_PAGE = {
    "slug": "/cau-hoi-thuong-gap/",
    "title": "Câu hỏi thường gặp về thiết kế website và SEO | WiThemes",
    "desc": "12 câu hỏi khách hàng hay hỏi nhất về chi phí, thời gian, cam kết thứ hạng, "
            "bảo hành và quyền sở hữu mã nguồn khi thiết kế website và làm SEO.",
    "h1": "Câu hỏi thường gặp",
    "crumb": [],
    "body": """
<p>Đây là những câu chúng tôi trả lời gần như mỗi tuần. Nếu câu của bạn không có ở đây,
<a href="/lien-he/">gửi cho chúng tôi</a> — câu trả lời sẽ được bổ sung vào trang này.</p>
""" + _FAQ_HTML + """
<h2>Vẫn còn thắc mắc?</h2>
<p>Gọi <a href="tel:0900000000">0900 000 000</a> hoặc gửi câu hỏi qua
<a href="/lien-he/">biểu mẫu liên hệ</a>. Chúng tôi trả lời trong ngày làm việc.</p>
""",
    "ld": [_FAQ_LD],
}

CONTACT = {
    "slug": "/lien-he/",
    "title": "Liên hệ WiThemes – nhận báo giá thiết kế website &amp; SEO",
    "desc": "Liên hệ WiThemes: hotline 0900 000 000, email info@withemes.com, văn phòng tại "
            "114 Điện Biên Phủ, Phường Tân Định, TP. Hồ Chí Minh. Gửi yêu cầu báo giá miễn phí.",
    "h1": "Liên hệ &amp; nhận báo giá",
    "crumb": [],
    "body": """
<h2>Gửi yêu cầu báo giá</h2>
<p>Điền biểu mẫu bên dưới, chúng tôi phản hồi trong 24 giờ làm việc kèm báo giá sơ bộ.
Trường có dấu <i style="color:#e02b20">*</i> là bắt buộc.</p>

<form class="cf" action="/lien-he/cam-on/" method="get">
  <div class="row">
    <div>
      <label for="ten">Họ và tên <i>*</i></label>
      <input type="text" id="ten" name="ten" placeholder="Nguyễn Văn A" required>
    </div>
    <div>
      <label for="sdt">Số điện thoại <i>*</i></label>
      <input type="tel" id="sdt" name="sdt" placeholder="09xx xxx xxx" required>
    </div>
  </div>
  <div class="row">
    <div>
      <label for="email">Email</label>
      <input type="email" id="email" name="email" placeholder="ban@congty.com">
    </div>
    <div>
      <label for="web">Website hiện tại (nếu có)</label>
      <input type="url" id="web" name="web" placeholder="https://">
    </div>
  </div>
  <label for="dichvu">Dịch vụ quan tâm <i>*</i></label>
  <select id="dichvu" name="dichvu" required>
    <option value="">— Chọn dịch vụ —</option>
    <option>Thiết kế website chuẩn SEO</option>
    <option>Thiết kế website bán hàng</option>
    <option>Thiết kế landing page</option>
    <option>Dịch vụ SEO tổng thể</option>
    <option>Dịch vụ SEO từ khóa</option>
    <option>SEO Local – Google Maps</option>
    <option>Audit website</option>
    <option>Tối ưu tốc độ website</option>
    <option>Chưa rõ, cần tư vấn</option>
  </select>
  <label for="nganhang">Ngân sách dự kiến</label>
  <select id="nganhang" name="nganhang">
    <option value="">— Chọn mức ngân sách —</option>
    <option>Dưới 5 triệu</option>
    <option>5 – 10 triệu</option>
    <option>10 – 25 triệu</option>
    <option>Trên 25 triệu</option>
    <option>Chưa xác định</option>
  </select>
  <label for="noidung">Mô tả yêu cầu</label>
  <textarea id="noidung" name="noidung" rows="5"
    placeholder="Bạn kinh doanh gì, muốn website làm được việc gì, có website mẫu nào bạn thích?"></textarea>
  <div class="submit">
    <button class="btn btn-r" type="submit">Gửi yêu cầu ngay</button>
  </div>
  <p class="note">Biểu mẫu này là bản demo giao diện, dữ liệu không được lưu lại và không gửi đi
  đâu cả. Để liên hệ thật, vui lòng dùng email <a href="mailto:info@withemes.com">info@withemes.com</a>
  hoặc gọi hotline.</p>
</form>

<h2>Thông tin liên hệ</h2>
<table>
<tbody>
<tr><th style="width:180px">Công ty</th><td>WiThemes</td></tr>
<tr><th>Mã số thuế</th><td>0318552411</td></tr>
<tr><th>Địa chỉ</th><td>Tầng trệt, 114 Điện Biên Phủ, Phường Tân Định, Thành phố Hồ Chí Minh</td></tr>
<tr><th>Email</th><td><a href="mailto:info@withemes.com">info@withemes.com</a></td></tr>
<tr><th>Hotline</th><td><a href="tel:0900000000">0900 000 000</a></td></tr>
<tr><th>Giờ làm việc</th><td>Thứ 2 – Thứ 6: 8h30 – 18h00 · Thứ 7: 8h30 – 12h00</td></tr>
</tbody>
</table>

<h2>Gửi yêu cầu thế nào cho nhanh?</h2>
<p>Ba thông tin giúp chúng tôi báo giá chính xác ngay lần đầu:</p>
<ol>
  <li>Bạn kinh doanh gì và khách hàng của bạn là ai.</li>
  <li>Hai hoặc ba website bạn thấy đẹp (kể cả của đối thủ).</li>
  <li>Mốc thời gian bạn muốn website đi vào hoạt động.</li>
</ol>
<p>Chưa rõ nên chọn dịch vụ nào? Xem <a href="/dich-vu/">danh sách dịch vụ</a> hoặc
<a href="/bang-gia/">bảng giá</a> trước.</p>
""",
}

THANKS = {
    "slug": "/lien-he/cam-on/",
    "title": "Cảm ơn bạn đã liên hệ | WiThemes",
    "desc": "Cảm ơn bạn đã gửi yêu cầu tới WiThemes. Chúng tôi sẽ phản hồi trong 24 giờ làm việc.",
    "h1": "Cảm ơn bạn!",
    "crumb": [("/lien-he/", "Liên hệ")],
    "noindex": True,
    "body": """
<h2>Yêu cầu đã được gửi đi</h2>
<div class="note">Lưu ý: biểu mẫu trên website này là bản demo giao diện — dữ liệu bạn nhập
<strong>không được lưu và không gửi tới đâu</strong>. Nếu bạn thực sự cần liên hệ, vui lòng
email <a href="mailto:info@withemes.com">info@withemes.com</a> hoặc gọi
<a href="tel:0900000000">0900 000 000</a>.</div>
<p>Trong lúc chờ, bạn có thể xem thêm:</p>
<ul>
  <li><a href="/bang-gia/">Bảng giá thiết kế website và SEO</a></li>
  <li><a href="/quy-trinh/">Quy trình làm việc 6 bước</a></li>
  <li><a href="/cau-hoi-thuong-gap/">Câu hỏi thường gặp</a></li>
  <li><a href="/kien-thuc/">Kiến thức website &amp; SEO</a></li>
</ul>
<p><a class="btn btn-g" href="/">Về trang chủ</a></p>
""",
}

TERMS = {
    "slug": "/dieu-khoan/",
    "title": "Điều khoản sử dụng | WiThemes",
    "desc": "Điều khoản sử dụng website withemes.com: quyền sở hữu nội dung, phạm vi sử dụng, "
            "giới hạn trách nhiệm và liên kết bên thứ ba.",
    "h1": "Điều khoản sử dụng",
    "crumb": [],
    "body": """
<p>Khi truy cập và sử dụng website withemes.com, bạn đồng ý với các điều khoản dưới đây.
Nếu không đồng ý, vui lòng ngừng sử dụng website.</p>

<h2>1. Quyền sở hữu nội dung</h2>
<p>Toàn bộ nội dung trên website — văn bản, hình ảnh, giao diện, bố cục — thuộc quyền sở hữu
của WiThemes, trừ khi có ghi chú khác. Bạn có thể xem, tải và in cho mục đích cá nhân,
phi thương mại. Việc sao chép, đăng lại hoặc sử dụng cho mục đích thương mại cần có sự đồng ý
bằng văn bản của chúng tôi.</p>

<h2>2. Sử dụng website</h2>
<p>Bạn đồng ý không sử dụng website vào các mục đích trái pháp luật, không cố gắng truy cập
trái phép vào hệ thống, không phát tán mã độc, không thu thập dữ liệu tự động ở quy mô gây
ảnh hưởng tới hoạt động của website.</p>

<h2>3. Biểu mẫu liên hệ</h2>
<p>Biểu mẫu trên trang <a href="/lien-he/">Liên hệ</a> hiện là bản demo giao diện: dữ liệu bạn
nhập không được lưu trữ và không được gửi đi. Vui lòng không nhập thông tin nhạy cảm vào
biểu mẫu này.</p>

<h2>4. Thông tin báo giá</h2>
<p>Giá niêm yết trên website mang tính tham khảo cho phạm vi công việc mô tả kèm theo, và có
thể thay đổi theo yêu cầu thực tế của từng dự án. Giá chính thức là giá ghi trong hợp đồng
hoặc báo giá được chúng tôi gửi bằng văn bản.</p>

<h2>5. Giới hạn trách nhiệm</h2>
<p>Nội dung trên website được cung cấp "nguyên trạng". Chúng tôi cố gắng bảo đảm thông tin
chính xác và cập nhật nhưng không cam kết website hoạt động không gián đoạn hoặc không có lỗi.
WiThemes không chịu trách nhiệm cho thiệt hại phát sinh từ việc sử dụng hoặc không thể sử dụng
website này.</p>

<h2>6. Liên kết tới website khác</h2>
<p>Website có thể chứa liên kết tới trang của bên thứ ba. Chúng tôi không kiểm soát và không
chịu trách nhiệm về nội dung hay chính sách của các trang đó.</p>

<h2>7. Thay đổi điều khoản</h2>
<p>Chúng tôi có thể cập nhật điều khoản này bất cứ lúc nào. Phiên bản mới có hiệu lực kể từ
khi được đăng trên website. Cập nhật lần gần nhất: 12/08/2026.</p>

<h2>8. Liên hệ</h2>
<p>Thắc mắc về điều khoản sử dụng, vui lòng gửi tới
<a href="mailto:info@withemes.com">info@withemes.com</a>. Xem thêm
<a href="/chinh-sach-bao-mat/">chính sách bảo mật</a>.</p>
""",
}

PRIVACY = {
    "slug": "/chinh-sach-bao-mat/",
    "title": "Chính sách bảo mật | WiThemes",
    "desc": "Chính sách bảo mật của withemes.com: thông tin chúng tôi thu thập, cách sử dụng, "
            "cookie, Google Analytics và quyền của bạn đối với dữ liệu.",
    "h1": "Chính sách bảo mật",
    "crumb": [],
    "body": """
<p>Chính sách này mô tả cách website withemes.com thu thập, sử dụng và bảo vệ thông tin của
người truy cập.</p>

<h2>1. Thông tin chúng tôi thu thập</h2>
<ul>
  <li><strong>Thông tin bạn chủ động cung cấp:</strong> khi bạn gửi email hoặc gọi điện cho
  chúng tôi. Lưu ý biểu mẫu trên trang Liên hệ là bản demo và không lưu dữ liệu.</li>
  <li><strong>Dữ liệu truy cập ẩn danh:</strong> trang bạn xem, thời gian xem, loại thiết bị,
  trình duyệt, nguồn truy cập — thu thập qua Google Analytics.</li>
</ul>

<h2>2. Mục đích sử dụng</h2>
<p>Thông tin được dùng để phản hồi yêu cầu của bạn, cải thiện nội dung và trải nghiệm website,
và thống kê lượng truy cập. Chúng tôi không bán, không trao đổi thông tin của bạn cho bên thứ ba
vì mục đích thương mại.</p>

<h2>3. Cookie và Google Analytics</h2>
<p>Website sử dụng Google Analytics 4 để đo lượng truy cập. Công cụ này đặt cookie trên trình
duyệt của bạn và ghi nhận dữ liệu ở dạng tổng hợp. Bạn có thể chặn cookie trong cài đặt trình
duyệt hoặc cài tiện ích từ chối Google Analytics; website vẫn hoạt động bình thường.</p>

<h2>4. Lưu trữ và bảo mật</h2>
<p>Website được phục vụ qua kết nối mã hóa HTTPS. Email liên hệ được lưu trong hộp thư của
công ty và chỉ những người phụ trách mới truy cập được. Chúng tôi không lưu trữ thông tin
thanh toán trên website.</p>

<h2>5. Quyền của bạn</h2>
<p>Bạn có quyền yêu cầu biết thông tin nào của bạn chúng tôi đang lưu, yêu cầu sửa hoặc xóa
thông tin đó. Gửi yêu cầu tới <a href="mailto:info@withemes.com">info@withemes.com</a>,
chúng tôi xử lý trong vòng 7 ngày làm việc.</p>

<h2>6. Trẻ em</h2>
<p>Website không hướng tới trẻ em dưới 13 tuổi và chúng tôi không cố ý thu thập thông tin của
nhóm tuổi này.</p>

<h2>7. Thay đổi chính sách</h2>
<p>Chính sách có thể được cập nhật; phiên bản mới có hiệu lực khi đăng trên website.
Cập nhật lần gần nhất: 12/08/2026.</p>

<h2>8. Liên hệ</h2>
<p>Mọi câu hỏi về chính sách bảo mật, vui lòng gửi tới
<a href="mailto:info@withemes.com">info@withemes.com</a>. Xem thêm
<a href="/dieu-khoan/">điều khoản sử dụng</a>.</p>
""",
}

CORE = [HOME, ABOUT, SERVICE_HUB, PRICING_PAGE, PROCESS, PROJECTS, FAQ_PAGE,
        CONTACT, THANKS, TERMS, PRIVACY]
