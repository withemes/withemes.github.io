# -*- coding: utf-8 -*-
"""The eight service pages."""
from blocks import faq, service_ld

CRUMB = [("/dich-vu/", "Dịch vụ")]


def svc(slug, title, desc, h1, body, ld_name, ld_desc, price, faq_items, img=None):
    f_html, f_ld = faq(faq_items)
    return {
        "slug": slug, "title": title, "desc": desc, "h1": h1,
        "crumb": CRUMB,
        "img": img or "site-restaurant.jpg",
        "body": body + f_html + """
<h2>Bắt đầu thế nào?</h2>
<p>Gửi yêu cầu, chúng tôi khảo sát và báo giá trong 24 giờ làm việc. Không mất phí,
không ràng buộc.</p>
<p><a class="btn btn-r" href="/lien-he/">Nhận báo giá</a>
<a class="btn btn-b" href="/bang-gia/">Xem bảng giá</a></p>""",
        "ld": [service_ld(ld_name, ld_desc, price), f_ld],
    }


WEB = svc(
    "/dich-vu/thiet-ke-website/",
    "Thiết kế website chuẩn SEO trọn gói từ 2.500.000đ | WiThemes",
    "Dịch vụ thiết kế website chuẩn SEO cho doanh nghiệp: giao diện riêng, tải dưới 3 giây, "
    "chuẩn mobile, tặng hosting và tên miền, bàn giao 7–15 ngày, bảo hành 12 tháng.",
    "Thiết kế website chuẩn SEO",
    """
<p>Chúng tôi thiết kế website cho doanh nghiệp vừa và nhỏ với một mục tiêu đơn giản:
website phải <strong>được tìm thấy</strong>, <strong>tải nhanh</strong> và
<strong>tạo ra liên hệ</strong>. Đẹp là điều kiện cần, không phải điều kiện đủ.</p>

<h2>Bạn nhận được gì</h2>
<ul>
  <li>Website 5–15 trang, cấu trúc do chúng tôi tư vấn dựa trên cách khách hàng của bạn tìm kiếm.</li>
  <li>Giao diện tùy chỉnh theo bộ nhận diện: logo, màu, phông chữ, giọng điệu.</li>
  <li>Chuẩn responsive từ màn hình 360px trở lên — kiểm tra thủ công, không chỉ tin công cụ.</li>
  <li>Điểm PageSpeed mobile tối thiểu 85/100 khi bàn giao.</li>
  <li>Trang quản trị tiếng Việt để bạn tự đăng bài, sửa nội dung, đổi ảnh.</li>
  <li>Chứng chỉ SSL, hosting năm đầu, tên miền .com năm đầu (gói Pro trở lên).</li>
  <li>Bàn giao toàn bộ mã nguồn và cơ sở dữ liệu. Bảo hành 12 tháng.</li>
</ul>

<h2>"Chuẩn SEO" ở đây nghĩa là gì?</h2>
<p>Cụm từ này bị lạm dụng đến mức mất nghĩa. Với chúng tôi, nó là một danh sách kiểm tra
27 điểm chạy trên mọi dự án trước khi bàn giao. Một số điểm chính:</p>
<table>
<thead><tr><th>Nhóm</th><th>Tiêu chí</th><th>Ngưỡng đạt</th></tr></thead>
<tbody>
<tr><td>Cấu trúc</td><td>Mỗi trang một thẻ H1 duy nhất, heading đúng thứ bậc</td><td>Toàn bộ số trang</td></tr>
<tr><td>Cấu trúc</td><td>URL ngắn, không dấu, phân cách bằng gạch nối</td><td>Dưới 60 ký tự</td></tr>
<tr><td>Thẻ meta</td><td>Title và description riêng, không trùng lặp</td><td>Toàn bộ số trang</td></tr>
<tr><td>Dữ liệu cấu trúc</td><td>Organization, Breadcrumb, FAQ, Article</td><td>Không lỗi khi kiểm tra</td></tr>
<tr><td>Hình ảnh</td><td>Có thẻ alt, nén WebP, khai báo kích thước</td><td>Toàn bộ ảnh nội dung</td></tr>
<tr><td>Tốc độ</td><td>LCP trên di động</td><td>Dưới 2,5 giây</td></tr>
<tr><td>Thu thập dữ liệu</td><td>robots.txt, sitemap.xml, thẻ canonical</td><td>Có và hợp lệ</td></tr>
<tr><td>Liên kết</td><td>Liên kết nội bộ có văn bản neo mô tả, không link gãy</td><td>0 link 404</td></tr>
</tbody>
</table>
<p>Danh sách đầy đủ có trong bài
<a href="/kien-thuc/checklist-seo-onpage/">checklist SEO onpage 27 điểm</a> — bạn có thể
tự dùng để soi website hiện tại.</p>

<h2>Quy trình và thời gian</h2>
<p>Website giới thiệu 5–7 trang: 7–10 ngày làm việc. Website doanh nghiệp 10–15 trang:
10–15 ngày. Mốc thời gian được ghi vào hợp đồng kèm điều khoản phạt tiến độ.
Xem chi tiết <a href="/quy-trinh/">quy trình 6 bước</a>.</p>

<h2>Chi phí</h2>
<p>Gói Cơ bản 2.500.000đ, gói Pro 4.500.000đ, gói VIP 8.000.000đ, thiết kế riêng từ
25.000.000đ. Bảng so sánh đầy đủ nằm ở trang <a href="/bang-gia/">bảng giá</a>.</p>

<h2>Dịch vụ liên quan</h2>
<p>Đã có website rồi? Cân nhắc <a href="/dich-vu/audit-website/">audit website</a> hoặc
<a href="/dich-vu/toi-uu-toc-do-website/">tối ưu tốc độ</a> trước khi quyết định làm lại.
Muốn website ra đơn ngay? Xem
<a href="/dich-vu/thiet-ke-website-ban-hang/">thiết kế website bán hàng</a>.</p>
""",
    "Thiết kế website chuẩn SEO",
    "Thiết kế website doanh nghiệp chuẩn SEO, tải nhanh, chuẩn mobile, bàn giao mã nguồn.",
    "2500000",
    [("Thiết kế website mất bao lâu?",
      "7–10 ngày làm việc cho website giới thiệu 5–7 trang, 10–15 ngày cho website doanh nghiệp "
      "10–15 trang. Thời gian tính từ khi nhận đủ nội dung và duyệt xong giao diện."),
     ("Tôi chưa có nội dung thì sao?",
      "Chúng tôi có thể viết giúp với chi phí 250.000đ cho mỗi bài khoảng 1.000 chữ, hoặc tạm dùng "
      "nội dung mẫu để bạn thay dần sau khi bàn giao."),
     ("Website có tự sửa được không?",
      "Có. Trang quản trị tiếng Việt cho phép bạn đăng bài, sửa sản phẩm, đổi banner và thông tin "
      "liên hệ mà không cần biết lập trình."),
     ("Sau bàn giao có được hỗ trợ không?",
      "Bảo hành 12 tháng cho lỗi kỹ thuật. Ngoài ra có gói chăm sóc 500.000đ/tháng nếu bạn muốn "
      "chúng tôi cập nhật, sao lưu và theo dõi tốc độ định kỳ.")],
)

SHOP = svc(
    "/dich-vu/thiet-ke-website-ban-hang/",
    "Thiết kế website bán hàng chuyên nghiệp | WiThemes",
    "Thiết kế website bán hàng có giỏ hàng, thanh toán online, quản lý đơn và tồn kho. "
    "Trọn gói từ 8.000.000đ, chuẩn SEO, tối ưu tốc độ, bàn giao 20–30 ngày.",
    "Thiết kế website bán hàng",
    """
<p>Một website bán hàng chỉ có giá trị khi khách <em>hoàn tất được đơn</em>. Vì vậy chúng
tôi tối ưu ngược từ nút "Đặt hàng" trở ra, thay vì từ trang chủ trở vào.</p>

<h2>Tính năng tiêu chuẩn</h2>
<div class="grid g2">
  <div class="box left"><h3>Danh mục &amp; bộ lọc</h3>
    <p>Lọc theo giá, thuộc tính, thương hiệu. Phân trang thân thiện với Google.</p></div>
  <div class="box left"><h3>Giỏ hàng &amp; thanh toán</h3>
    <p>Thanh toán khi nhận hàng, chuyển khoản QR, ví điện tử và cổng thẻ nếu cần.</p></div>
  <div class="box left"><h3>Quản lý đơn hàng</h3>
    <p>Trạng thái đơn, in phiếu giao, thông báo email và tin nhắn cho khách.</p></div>
  <div class="box left"><h3>Kho &amp; biến thể</h3>
    <p>Quản lý tồn theo màu/size, cảnh báo hết hàng, giá khuyến mãi theo thời gian.</p></div>
  <div class="box left"><h3>Vận chuyển</h3>
    <p>Tính phí theo khu vực hoặc nối API đơn vị vận chuyển bạn đang dùng.</p></div>
  <div class="box left"><h3>Đo lường</h3>
    <p>Gắn sẵn Google Analytics 4 và pixel quảng cáo, theo dõi từng bước thanh toán.</p></div>
</div>

<h2>Những chi tiết quyết định tỷ lệ chốt đơn</h2>
<ol>
  <li><strong>Thanh toán ít bước.</strong> Mỗi trường bắt buộc thừa là một phần trăm đơn rơi rớt.
  Chúng tôi giữ tối đa 6 trường và không bắt tạo tài khoản.</li>
  <li><strong>Tốc độ trang sản phẩm.</strong> Ảnh sản phẩm là thứ nặng nhất — nén WebP, tải trễ,
  khai báo kích thước để trang không nhảy layout.</li>
  <li><strong>Thông tin tin cậy.</strong> Chính sách đổi trả, thời gian giao, số điện thoại thật,
  đánh giá sản phẩm — hiển thị ngay trên trang, không giấu ở footer.</li>
  <li><strong>Tìm kiếm nội bộ.</strong> Khách gõ sai chính tả vẫn phải ra đúng sản phẩm.</li>
</ol>

<h2>SEO cho website bán hàng</h2>
<p>Website bán hàng có bài toán SEO riêng: hàng nghìn URL sinh tự động từ bộ lọc, mô tả sản
phẩm trùng nhau, sản phẩm hết hàng bị xóa làm gãy link. Chúng tôi xử lý bằng thẻ canonical
cho URL lọc, dữ liệu cấu trúc Product kèm giá và tình trạng kho, và chuyển hướng 301 cho sản
phẩm ngừng kinh doanh. Muốn đẩy mạnh hơn nữa thì kết hợp
<a href="/dich-vu/dich-vu-seo-tong-the/">SEO tổng thể</a>.</p>

<h2>Chi phí và thời gian</h2>
<table>
<thead><tr><th>Quy mô</th><th>Số sản phẩm</th><th>Chi phí</th><th>Thời gian</th></tr></thead>
<tbody>
<tr><td>Shop nhỏ</td><td>Dưới 100</td><td>8.000.000đ</td><td>20 ngày</td></tr>
<tr><td>Shop vừa</td><td>100 – 1.000</td><td>12.000.000đ</td><td>25 ngày</td></tr>
<tr><td>Thương hiệu</td><td>Trên 1.000, nhiều biến thể</td><td>Từ 25.000.000đ</td><td>30–45 ngày</td></tr>
</tbody>
</table>
<p>Chi phí nhập liệu sản phẩm tính riêng nếu bạn muốn chúng tôi làm: 5.000đ/sản phẩm khi
bạn đã có sẵn ảnh và mô tả.</p>
""",
    "Thiết kế website bán hàng",
    "Thiết kế website thương mại điện tử có giỏ hàng, thanh toán, quản lý đơn và tồn kho.",
    "8000000",
    [("Website có kết nối được với đơn vị vận chuyển không?",
      "Có. Chúng tôi nối API của các đơn vị vận chuyển phổ biến để tính cước tự động và đẩy đơn "
      "sang hệ thống của họ. Phần này tính là tính năng thêm nếu ngoài phạm vi gói."),
     ("Có nhận thanh toán online được không?",
      "Được. Chuyển khoản QR là mặc định; cổng thanh toán thẻ và ví điện tử cần bạn đăng ký tài "
      "khoản doanh nghiệp với nhà cung cấp, chúng tôi hỗ trợ tích hợp."),
     ("Tôi có 3.000 sản phẩm, nhập liệu thế nào?",
      "Nếu bạn có file Excel hoặc dữ liệu từ nền tảng cũ, chúng tôi nhập hàng loạt miễn phí. Nếu "
      "phải nhập tay từng sản phẩm thì tính 5.000đ mỗi sản phẩm."),
     ("Website chịu được bao nhiêu khách cùng lúc?",
      "Hosting tiêu chuẩn trong gói phục vụ tốt khoảng 200 khách đồng thời. Nếu bạn chạy quảng cáo "
      "mạnh hoặc bán flash sale, chúng tôi tư vấn nâng cấp máy chủ trước chiến dịch.")],
    img="site-bakery.jpg",
)

LANDING = svc(
    "/dich-vu/thiet-ke-landing-page/",
    "Thiết kế landing page tối ưu chuyển đổi | WiThemes",
    "Thiết kế landing page cho chiến dịch quảng cáo: một mục tiêu, tải dưới 2 giây, "
    "form ngắn, tối ưu tỷ lệ chuyển đổi. Từ 3.000.000đ, bàn giao 5–7 ngày.",
    "Thiết kế landing page",
    """
<p>Landing page không phải website thu nhỏ. Nó là một trang duy nhất, phục vụ một mục tiêu
duy nhất, và mọi thứ không phục vụ mục tiêu đó đều bị cắt bỏ — kể cả menu điều hướng.</p>

<h2>Khi nào bạn cần landing page?</h2>
<ul>
  <li>Chạy quảng cáo Google hoặc Facebook và cần nơi để đổ lưu lượng về.</li>
  <li>Ra mắt một sản phẩm, khóa học, sự kiện có thời hạn.</li>
  <li>Thử nghiệm một thông điệp bán hàng trước khi đầu tư website đầy đủ.</li>
  <li>Thu danh sách khách hàng tiềm năng để chăm sóc qua email hoặc Zalo.</li>
</ul>

<h2>Cấu trúc một landing page hiệu quả</h2>
<ol>
  <li><strong>Màn hình đầu:</strong> một câu nói rõ bạn bán gì, cho ai, lợi ích gì — cộng một nút.</li>
  <li><strong>Vấn đề:</strong> gọi tên nỗi đau bằng chính ngôn ngữ khách hàng dùng.</li>
  <li><strong>Giải pháp:</strong> sản phẩm của bạn giải quyết ra sao, kèm ảnh thật.</li>
  <li><strong>Bằng chứng:</strong> đánh giá, số liệu, logo đối tác, ảnh trước–sau.</li>
  <li><strong>Xử lý phản đối:</strong> giá, bảo hành, đổi trả, "tôi có hợp không".</li>
  <li><strong>Lời kêu gọi cuối:</strong> lặp lại nút hành động, kèm lý do hành động ngay.</li>
</ol>

<h2>Chúng tôi tối ưu chuyển đổi thế nào</h2>
<p>Không phải bằng cảm tính. Ba việc cụ thể:</p>
<ul>
  <li><strong>Tốc độ.</strong> Landing page tải trên 3 giây mất khoảng một phần ba lượt truy cập
  từ quảng cáo. Chúng tôi giữ mốc dưới 2 giây trên 4G.</li>
  <li><strong>Form ngắn nhất có thể.</strong> Tên và số điện thoại là đủ để gọi lại. Mỗi trường
  thêm vào phải trả lời được câu "thiếu nó thì mất gì".</li>
  <li><strong>Đo lường đến từng nút.</strong> Gắn sự kiện GA4 cho từng nút và từng bước cuộn,
  để tháng sau bạn biết cắt gì và giữ gì.</li>
</ul>

<h2>Chi phí</h2>
<table>
<thead><tr><th>Gói</th><th>Bao gồm</th><th>Chi phí</th><th>Thời gian</th></tr></thead>
<tbody>
<tr><td>Cơ bản</td><td>1 trang, dùng bố cục mẫu, form liên hệ</td><td>3.000.000đ</td><td>5 ngày</td></tr>
<tr><td>Chuẩn</td><td>Thiết kế riêng, viết nội dung bán hàng, gắn GA4 + pixel</td><td>6.000.000đ</td><td>7 ngày</td></tr>
<tr><td>A/B</td><td>Hai phiên bản để thử nghiệm, báo cáo sau 30 ngày</td><td>9.000.000đ</td><td>10 ngày</td></tr>
</tbody>
</table>
<p>Cần cả hệ thống chứ không chỉ một trang? Xem
<a href="/dich-vu/thiet-ke-website/">thiết kế website chuẩn SEO</a>.</p>
""",
    "Thiết kế landing page",
    "Thiết kế trang đích tối ưu chuyển đổi cho chiến dịch quảng cáo.",
    "3000000",
    [("Landing page có SEO được không?",
      "Được, nhưng đó không phải thế mạnh của nó. Landing page thường phục vụ lưu lượng trả phí; "
      "để lên top tự nhiên bạn cần một website có nhiều nội dung hơn."),
     ("Tôi có cần tên miền riêng cho landing page?",
      "Không bắt buộc. Có thể đặt trên tên miền phụ của website hiện tại, ví dụ km.tenmien.com, "
      "và như vậy còn tận dụng được uy tín sẵn có."),
     ("Bao lâu thì biết landing page có hiệu quả?",
      "Cần tối thiểu khoảng 1.000 lượt truy cập để số liệu đủ tin cậy. Với ngân sách quảng cáo "
      "thông thường, mốc đó rơi vào 2–4 tuần.")],
)

SEO_FULL = svc(
    "/dich-vu/dich-vu-seo-tong-the/",
    "Dịch vụ SEO tổng thể website | WiThemes",
    "SEO tổng thể: tối ưu toàn bộ website thay vì vài từ khóa lẻ. Kỹ thuật, nội dung, "
    "liên kết và báo cáo hằng tháng. Từ 12.000.000đ/tháng, cam kết tối thiểu 6 tháng.",
    "Dịch vụ SEO tổng thể",
    """
<p>SEO tổng thể là kéo toàn bộ sức khỏe tìm kiếm của website đi lên: hàng trăm từ khóa dài,
chứ không chỉ năm từ khóa đẹp để khoe trong báo cáo. Cách này chậm hơn lúc đầu nhưng bền hơn,
và ít bị tổn thương khi Google cập nhật thuật toán.</p>

<h2>Bốn nhóm công việc</h2>
<h3>1. Kỹ thuật</h3>
<p>Xử lý những gì cản Google đọc website: lỗi index, trang trùng lặp, chuyển hướng vòng,
sitemap sai, tốc độ, dữ liệu cấu trúc, phiên bản di động. Đây là phần làm trước, vì viết
100 bài trên một website hỏng kỹ thuật là đổ tiền qua cửa sổ.</p>
<h3>2. Nội dung</h3>
<p>Lập bản đồ từ khóa theo ý định tìm kiếm: tìm hiểu, so sánh, mua. Mỗi cụm chủ đề có một
trang trụ cột và các bài vệ tinh trỏ về. Bài cũ được cập nhật thay vì bỏ mặc — thường
rẻ và hiệu quả hơn viết mới.</p>
<h3>3. Liên kết</h3>
<p>Liên kết nội bộ trước, liên kết ngoài sau. Chúng tôi đặt bài trên trang uy tín có thật,
không mua backlink hàng loạt từ hệ thống blog rác — thứ có thể kéo tụt website của bạn.</p>
<h3>4. Đo lường</h3>
<p>Theo dõi thứ hạng, lưu lượng tự nhiên, và quan trọng nhất: số cuộc gọi và form phát sinh
từ kênh tự nhiên. Thứ hạng chỉ là chỉ số trung gian.</p>

<h2>Lộ trình 6 tháng điển hình</h2>
<table>
<thead><tr><th>Giai đoạn</th><th>Trọng tâm</th><th>Kết quả kỳ vọng</th></tr></thead>
<tbody>
<tr><td>Tháng 1</td><td>Audit toàn diện, sửa lỗi kỹ thuật, lập bản đồ từ khóa</td>
    <td>Website sạch lỗi, kế hoạch nội dung 6 tháng</td></tr>
<tr><td>Tháng 2–3</td><td>Xuất bản nội dung trụ cột, tối ưu trang dịch vụ</td>
    <td>Từ khóa dài bắt đầu vào top 20–50</td></tr>
<tr><td>Tháng 4–5</td><td>Mở rộng nội dung vệ tinh, xây liên kết</td>
    <td>Nhóm từ khóa chính vào top 10, lưu lượng tăng 40–80 phần trăm</td></tr>
<tr><td>Tháng 6</td><td>Tối ưu chuyển đổi, cập nhật bài hiệu quả thấp</td>
    <td>Lưu lượng ổn định, chi phí mỗi liên hệ giảm</td></tr>
</tbody>
</table>
<p>Con số trên là kỳ vọng trung bình của các dự án ngành dịch vụ ở mức cạnh tranh vừa,
không phải cam kết. Ngành càng cạnh tranh, lộ trình càng dài.</p>

<h2>Chi phí</h2>
<p>12.000.000đ/tháng cho gói tiêu chuẩn, gồm 16 bài nội dung, tối ưu kỹ thuật liên tục,
xây liên kết và báo cáo hằng tháng. Hợp đồng tối thiểu 6 tháng. Nếu ngân sách nhỏ hơn,
<a href="/dich-vu/seo-tu-khoa/">SEO từ khóa</a> hoặc
<a href="/dich-vu/seo-local-google-maps/">SEO Local</a> hợp lý hơn.</p>

<h2>Chúng tôi không làm gì</h2>
<ul>
  <li>Không mua backlink từ hệ thống PBN hoặc bình luận spam.</li>
  <li>Không nhồi từ khóa vào nội dung đến mức người đọc thấy khó chịu.</li>
  <li>Không tạo hàng loạt trang na ná nhau chỉ để nhắm từ khóa địa phương.</li>
  <li>Không hứa vị trí số 1 cho một từ khóa cụ thể trong một mốc thời gian cố định.</li>
</ul>
""",
    "Dịch vụ SEO tổng thể",
    "Tối ưu toàn diện website để tăng lưu lượng tìm kiếm tự nhiên bền vững.",
    "12000000",
    [("SEO tổng thể khác SEO từ khóa thế nào?",
      "SEO từ khóa nhắm một danh sách từ khóa cố định. SEO tổng thể tối ưu toàn bộ website nên "
      "kéo theo hàng trăm từ khóa dài, bền hơn trước thay đổi thuật toán nhưng cần thời gian và "
      "ngân sách lớn hơn."),
     ("Bao lâu thì thấy kết quả?",
      "Tháng thứ 2–3 thường thấy chuyển động thứ hạng ở từ khóa dài, tháng thứ 4–6 mới rõ ở nhóm "
      "từ khóa chính. Ngành cạnh tranh cao có thể lâu hơn."),
     ("Nếu tôi dừng SEO thì sao?",
      "Thứ hạng không mất ngay. Nội dung đã có vẫn giữ vị trí một thời gian rồi trượt dần khi đối "
      "thủ tiếp tục đầu tư. Khác với quảng cáo, dừng là mất lưu lượng ngay lập tức."),
     ("Có cần đổi website hiện tại không?",
      "Không bắt buộc. Chúng tôi audit trước; chỉ khi nền tảng cũ chặn hẳn khả năng tối ưu thì mới "
      "đề nghị làm lại, và sẽ nói rõ vì sao.")],
    img="site-spa.jpg",
)

SEO_KW = svc(
    "/dich-vu/seo-tu-khoa/",
    "Dịch vụ SEO từ khóa – lên top theo từ khóa mục tiêu | WiThemes",
    "Dịch vụ SEO từ khóa: chọn 10–20 từ khóa mục tiêu, cam kết thứ hạng bằng văn bản, "
    "báo cáo hằng tháng. Từ 5.000.000đ/tháng, phù hợp ngân sách vừa.",
    "Dịch vụ SEO từ khóa",
    """
<p>Bạn biết chính xác khách hàng gõ gì trên Google, và bạn muốn có mặt ở đó. SEO từ khóa
là gói gọn nhất cho nhu cầu đó: chọn một danh sách từ khóa, tập trung nguồn lực vào chúng,
và đo bằng thứ hạng.</p>

<h2>Cách chọn từ khóa</h2>
<p>Đây là bước quan trọng nhất, và cũng là bước hay bị làm ẩu nhất. Chúng tôi chấm mỗi từ
khóa theo bốn tiêu chí:</p>
<table>
<thead><tr><th>Tiêu chí</th><th>Câu hỏi</th><th>Vì sao quan trọng</th></tr></thead>
<tbody>
<tr><td>Lượng tìm kiếm</td><td>Mỗi tháng bao nhiêu người gõ?</td>
    <td>Quá thấp thì lên top cũng không ra khách</td></tr>
<tr><td>Ý định</td><td>Người gõ đang tìm hiểu hay đang muốn mua?</td>
    <td>"Giá thiết kế website" đáng giá hơn "website là gì"</td></tr>
<tr><td>Độ cạnh tranh</td><td>Top 10 hiện tại mạnh cỡ nào?</td>
    <td>Quyết định thời gian và chi phí</td></tr>
<tr><td>Khả năng chuyển đổi</td><td>Trang đích của bạn có thuyết phục không?</td>
    <td>Top 1 mà trang xấu thì vẫn không ra đơn</td></tr>
</tbody>
</table>
<p>Kết quả là một danh sách 10–20 từ khóa được xếp thứ tự ưu tiên, bạn duyệt trước khi
chúng tôi bắt đầu.</p>

<h2>Cam kết thứ hạng</h2>
<p>Chúng tôi cam kết <strong>số lượng</strong> từ khóa vào top 10 sau thời hạn thỏa thuận,
không cam kết vị trí cụ thể cho một từ khóa cụ thể — vì không đơn vị nào kiểm soát được
điều đó. Nếu không đạt, chúng tôi triển khai bù thêm thời gian mà không tính phí.</p>

<h2>Công việc hằng tháng</h2>
<ul>
  <li>8 bài viết mới hoặc bài cập nhật nhắm nhóm từ khóa mục tiêu.</li>
  <li>Tối ưu onpage trang đích: tiêu đề, mô tả, heading, liên kết nội bộ.</li>
  <li>Theo dõi thứ hạng hằng tuần, báo cáo cuối tháng.</li>
  <li>Sửa lỗi kỹ thuật phát sinh ảnh hưởng tới nhóm từ khóa đang chạy.</li>
</ul>

<h2>Chi phí</h2>
<table>
<thead><tr><th>Số từ khóa</th><th>Mức cạnh tranh</th><th>Chi phí/tháng</th><th>Thời hạn cam kết</th></tr></thead>
<tbody>
<tr><td>10 từ</td><td>Thấp – trung bình</td><td>5.000.000đ</td><td>6 tháng</td></tr>
<tr><td>20 từ</td><td>Trung bình</td><td>8.000.000đ</td><td>6 tháng</td></tr>
<tr><td>20 từ</td><td>Cao (ngành cạnh tranh mạnh)</td><td>Từ 12.000.000đ</td><td>9–12 tháng</td></tr>
</tbody>
</table>
<p>Muốn phủ rộng hơn danh sách cố định? Xem
<a href="/dich-vu/dich-vu-seo-tong-the/">SEO tổng thể</a>.</p>
""",
    "Dịch vụ SEO từ khóa",
    "Đưa nhóm từ khóa mục tiêu lên top 10 Google, có cam kết bằng văn bản.",
    "5000000",
    [("Tôi tự chọn từ khóa được không?",
      "Được. Chúng tôi vẫn chấm điểm từng từ và nói rõ từ nào theo chúng tôi là không đáng đầu tư, "
      "nhưng quyết định cuối cùng là của bạn."),
     ("Cam kết cụ thể như thế nào?",
      "Ghi trong hợp đồng: sau N tháng, tối thiểu X trong số từ khóa danh sách vào top 10. Không "
      "đạt thì triển khai bù không tính phí cho tới khi đạt."),
     ("Thứ hạng đo trên thiết bị nào?",
      "Đo trên Google Việt Nam, chế độ ẩn danh, cả máy tính và di động, lấy trung bình 7 ngày để "
      "tránh biến động ngày lẻ.")],
)

SEO_LOCAL = svc(
    "/dich-vu/seo-local-google-maps/",
    "SEO Local – lên top Google Maps cho cửa hàng | WiThemes",
    "Dịch vụ SEO Local: tối ưu Google Business Profile, lên top bản đồ và tìm kiếm khu vực "
    "cho cửa hàng, phòng khám, showroom. Từ 4.000.000đ/tháng, thấy kết quả sau 1–3 tháng.",
    "SEO Local – Google Maps",
    """
<p>Nếu khách phải đến tận nơi mới mua được — nhà hàng, spa, phòng khám, gara, showroom —
thì trận đánh của bạn nằm ở khối bản đồ ba kết quả đầu, không phải ở trang nhất tìm kiếm
thông thường. Đó là địa hạt của SEO Local.</p>

<h2>Ba yếu tố quyết định thứ hạng bản đồ</h2>
<ol>
  <li><strong>Khoảng cách.</strong> Vị trí người tìm so với địa chỉ của bạn. Cái này bạn không đổi được.</li>
  <li><strong>Mức độ liên quan.</strong> Hồ sơ doanh nghiệp mô tả đúng thứ khách đang tìm — cái này
  tối ưu được.</li>
  <li><strong>Độ nổi bật.</strong> Số lượng và chất lượng đánh giá, mức độ được nhắc tới trên các
  trang khác — cái này xây dựng được.</li>
</ol>

<h2>Chúng tôi làm gì</h2>
<div class="grid g2">
  <div class="box left"><h3>Hồ sơ Google Business</h3>
    <p>Chuẩn hóa tên, danh mục chính và phụ, giờ mở cửa, khu vực phục vụ, mô tả có từ khóa.</p></div>
  <div class="box left"><h3>Hình ảnh &amp; bài đăng</h3>
    <p>Ảnh mặt tiền, không gian, sản phẩm; đăng bài khuyến mãi định kỳ để hồ sơ luôn hoạt động.</p></div>
  <div class="box left"><h3>Đánh giá</h3>
    <p>Quy trình xin đánh giá tự nhiên từ khách thật, kịch bản trả lời cả khen lẫn chê.</p></div>
  <div class="box left"><h3>Trích dẫn NAP</h3>
    <p>Đồng bộ tên – địa chỉ – số điện thoại trên các danh bạ, tránh thông tin mâu thuẫn.</p></div>
  <div class="box left"><h3>Trang khu vực</h3>
    <p>Trang riêng cho từng khu vực phục vụ, viết thật, không nhân bản hàng loạt.</p></div>
  <div class="box left"><h3>Dữ liệu cấu trúc</h3>
    <p>Khai báo LocalBusiness kèm tọa độ, giờ mở cửa và khoảng giá trên website.</p></div>
</div>

<h2>Về đánh giá: nói thẳng</h2>
<div class="note">Chúng tôi không mua đánh giá ảo và không nhận yêu cầu này. Google phát hiện
được, và hậu quả là hồ sơ bị hạ hiển thị hoặc khóa — mất nhiều hơn được. Chúng tôi giúp bạn
xây quy trình xin đánh giá từ khách thật, việc này chậm hơn nhưng không có rủi ro.</div>

<h2>Kết quả kỳ vọng</h2>
<table>
<thead><tr><th>Mốc</th><th>Thường thấy</th></tr></thead>
<tbody>
<tr><td>Tháng 1</td><td>Hồ sơ đầy đủ, lượt hiển thị trên bản đồ tăng rõ</td></tr>
<tr><td>Tháng 2</td><td>Vào top 3 bản đồ với các truy vấn có tên khu vực</td></tr>
<tr><td>Tháng 3</td><td>Tăng lượt gọi và lượt chỉ đường; ổn định thứ hạng</td></tr>
</tbody>
</table>

<h2>Chi phí</h2>
<p>4.000.000đ/tháng cho một địa điểm, gồm 4 bài nội dung, quản lý hồ sơ và báo cáo.
Từ địa điểm thứ hai trở đi cộng thêm 1.500.000đ/địa điểm. Kết hợp với
<a href="/dich-vu/thiet-ke-website/">một website chuẩn SEO</a> sẽ nhanh hơn đáng kể.</p>
""",
    "SEO Local Google Maps",
    "Tối ưu hồ sơ Google Business và website để lên top bản đồ theo khu vực.",
    "4000000",
    [("Tôi chưa có hồ sơ Google Business thì sao?",
      "Chúng tôi tạo và xác minh giúp. Google gửi mã xác minh về địa chỉ hoặc yêu cầu quay video "
      "cơ sở; bạn chỉ cần phối hợp một lần."),
     ("Nhiều chi nhánh thì tính thế nào?",
      "Mỗi chi nhánh là một hồ sơ riêng. Địa điểm đầu 4.000.000đ/tháng, từ địa điểm thứ hai cộng "
      "1.500.000đ mỗi địa điểm."),
     ("Có cần website mới làm SEO Local được không?",
      "Không bắt buộc, hồ sơ Google Business vẫn lên được. Nhưng có website với trang khu vực và "
      "dữ liệu cấu trúc thì thứ hạng bản đồ ổn định hơn hẳn.")],
    img="site-spa.jpg",
)

AUDIT = svc(
    "/dich-vu/audit-website/",
    "Dịch vụ audit website – kiểm tra 27 điểm SEO | WiThemes",
    "Audit website 27 điểm: kỹ thuật, nội dung, tốc độ, liên kết. Báo cáo có thứ tự ưu tiên "
    "và ước tính chi phí sửa. 3.000.000đ, trả kết quả sau 5 ngày làm việc.",
    "Audit website",
    """
<p>Website chạy đã lâu, thứ hạng không nhúc nhích, và không ai nói được vì sao. Audit là
buổi khám tổng quát: chúng tôi soi 27 điểm, xếp lỗi theo mức độ nghiêm trọng, và trả về
một danh sách việc cần làm theo thứ tự — kèm ước tính chi phí nếu bạn muốn chúng tôi sửa.</p>

<h2>Phạm vi kiểm tra</h2>
<h3>Kỹ thuật (10 điểm)</h3>
<p>Khả năng thu thập dữ liệu, chỉ mục, robots.txt, sitemap, canonical, chuyển hướng, mã lỗi
HTTP, phiên bản di động, HTTPS, trang trùng lặp.</p>
<h3>Tốc độ &amp; trải nghiệm (5 điểm)</h3>
<p>LCP, INP, CLS, dung lượng trang, số lượng yêu cầu mạng. Đo trên cả dữ liệu phòng thí nghiệm
và dữ liệu người dùng thật nếu có.</p>
<h3>Nội dung (7 điểm)</h3>
<p>Bản đồ từ khóa, ý định tìm kiếm, trùng lặp nội bộ, độ sâu nội dung so với top 10, thẻ tiêu đề
và mô tả, cấu trúc heading, hình ảnh.</p>
<h3>Liên kết (5 điểm)</h3>
<p>Liên kết nội bộ, độ sâu nhấp chuột, liên kết gãy, hồ sơ backlink, văn bản neo bất thường.</p>

<h2>Bạn nhận được gì</h2>
<ul>
  <li>Báo cáo PDF 20–30 trang, viết bằng tiếng Việt dễ hiểu, có ảnh chụp minh họa.</li>
  <li>Bảng lỗi xếp theo mức độ: <strong>chặn</strong> (phải sửa ngay),
  <strong>quan trọng</strong>, <strong>nên làm</strong>.</li>
  <li>Với mỗi lỗi: nó là gì, ảnh hưởng ra sao, sửa thế nào, ai sửa được.</li>
  <li>Danh sách 20 từ khóa có tiềm năng nhất mà website đang bỏ lỡ.</li>
  <li>Buổi họp 60 phút để đi qua báo cáo và trả lời câu hỏi.</li>
</ul>

<h2>Chi phí và thời gian</h2>
<table>
<thead><tr><th>Quy mô website</th><th>Chi phí</th><th>Thời gian</th></tr></thead>
<tbody>
<tr><td>Dưới 100 URL</td><td>3.000.000đ</td><td>5 ngày làm việc</td></tr>
<tr><td>100 – 1.000 URL</td><td>5.000.000đ</td><td>7 ngày làm việc</td></tr>
<tr><td>Trên 1.000 URL</td><td>Từ 8.000.000đ</td><td>10 ngày làm việc</td></tr>
</tbody>
</table>
<div class="note">Nếu sau đó bạn ký hợp đồng <a href="/dich-vu/dich-vu-seo-tong-the/">SEO tổng thể</a>
hoặc <a href="/dich-vu/thiet-ke-website/">thiết kế lại website</a> với chúng tôi, toàn bộ phí
audit được trừ vào hợp đồng.</div>
""",
    "Audit website",
    "Kiểm tra 27 điểm kỹ thuật, nội dung, tốc độ và liên kết của website.",
    "3000000",
    [("Audit khác với công cụ kiểm tra miễn phí thế nào?",
      "Công cụ liệt kê hàng trăm cảnh báo không phân biệt nặng nhẹ. Audit của chúng tôi xếp theo "
      "mức độ ảnh hưởng thực tế tới thứ hạng của chính website bạn, và nói rõ nên sửa cái nào trước."),
     ("Tôi có cần cấp quyền truy cập gì không?",
      "Lý tưởng là Google Search Console và Google Analytics ở quyền xem. Không có cũng làm được "
      "nhưng phần đánh giá hiệu suất sẽ kém chính xác hơn."),
     ("Sau audit tôi có bắt buộc thuê các bạn sửa không?",
      "Không. Báo cáo đủ chi tiết để đội kỹ thuật của bạn tự sửa. Nếu bạn muốn chúng tôi làm, phí "
      "audit được trừ vào hợp đồng tiếp theo.")],
)

SPEED = svc(
    "/dich-vu/toi-uu-toc-do-website/",
    "Dịch vụ tối ưu tốc độ website, đạt PageSpeed 90+ | WiThemes",
    "Tối ưu tốc độ website: giảm thời gian tải, đạt Core Web Vitals ngưỡng xanh và "
    "PageSpeed 90+. Từ 4.000.000đ, hoàn tất trong 5–10 ngày, không đổi giao diện.",
    "Tối ưu tốc độ website",
    """
<p>Website chậm làm hai việc cùng lúc: đuổi khách đi và kéo thứ hạng xuống. Chúng tôi tối ưu
tốc độ mà <strong>không đổi giao diện</strong> — bạn không phải làm quen lại với website
của chính mình.</p>

<h2>Mục tiêu cụ thể</h2>
<table>
<thead><tr><th>Chỉ số</th><th>Ngưỡng đạt</th><th>Ý nghĩa</th></tr></thead>
<tbody>
<tr><td>LCP</td><td>Dưới 2,5 giây</td><td>Nội dung chính hiện ra nhanh</td></tr>
<tr><td>INP</td><td>Dưới 200 mili giây</td><td>Bấm là phản hồi ngay</td></tr>
<tr><td>CLS</td><td>Dưới 0,1</td><td>Trang không nhảy khi đang đọc</td></tr>
<tr><td>PageSpeed mobile</td><td>Từ 90 điểm</td><td>Chỉ số tổng hợp của Google</td></tr>
<tr><td>Dung lượng trang chủ</td><td>Dưới 1,5 MB</td><td>Tải được trên 4G yếu</td></tr>
</tbody>
</table>
<p>Chi tiết ba chỉ số đầu nằm trong bài
<a href="/kien-thuc/core-web-vitals-la-gi/">Core Web Vitals là gì</a>.</p>

<h2>Chúng tôi sửa những gì</h2>
<ol>
  <li><strong>Hình ảnh.</strong> Thủ phạm số một. Nén, chuyển WebP, khai báo kích thước,
  tải trễ ảnh dưới màn hình đầu, chọn đúng độ phân giải cho từng thiết bị.</li>
  <li><strong>Mã nguồn thừa.</strong> Gỡ thư viện JavaScript và CSS không dùng — nhiều website
  tải cả bộ khung 300KB chỉ để chạy một hiệu ứng trượt.</li>
  <li><strong>Bộ nhớ đệm.</strong> Cache phía máy chủ và phía trình duyệt, đặt đúng thời hạn
  cho từng loại tệp.</li>
  <li><strong>Phông chữ.</strong> Giảm số biến thể, nạp trước phông chính, tránh chữ nhấp nháy
  lúc tải.</li>
  <li><strong>Mã theo dõi.</strong> Gom về một trình quản lý thẻ, tải bất đồng bộ, bỏ các mã
  không còn ai xem báo cáo.</li>
  <li><strong>Máy chủ.</strong> Bật nén, HTTP/2, kiểm tra thời gian phản hồi đầu tiên; tư vấn
  đổi hosting nếu vấn đề nằm ở đó.</li>
</ol>

<h2>Cách làm việc</h2>
<p>Chúng tôi sao chép website sang môi trường thử nghiệm, tối ưu ở đó, đo lại, rồi mới áp lên
website thật. Bạn nhận báo cáo trước–sau với số liệu đo từ cùng một công cụ, cùng một điều
kiện mạng.</p>

<h2>Chi phí</h2>
<p>4.000.000đ cho website giới thiệu, 7.000.000đ cho website bán hàng. Nếu sau khi tối ưu
không đạt các ngưỡng cam kết ở bảng trên, chúng tôi hoàn lại toàn bộ phí — điều kiện là bạn
không thay đổi cấu hình hoặc cài thêm plugin trong thời gian thực hiện.</p>
<p>Không chắc vấn đề nằm ở tốc độ hay ở chỗ khác?
<a href="/dich-vu/audit-website/">Audit website</a> sẽ trả lời câu đó.</p>
""",
    "Tối ưu tốc độ website",
    "Tăng tốc website, đạt Core Web Vitals ngưỡng xanh và PageSpeed 90+.",
    "4000000",
    [("Tối ưu tốc độ có làm hỏng giao diện không?",
      "Không. Chúng tôi làm trên bản sao thử nghiệm, đối chiếu từng trang trước khi áp lên website "
      "thật. Nếu một tối ưu nào đó ảnh hưởng hiển thị, chúng tôi bỏ tối ưu đó."),
     ("Website tôi dùng nền tảng khác thì có làm được không?",
      "Phần lớn nền tảng phổ biến đều làm được. Với nền tảng đóng không cho can thiệp mã nguồn, "
      "phạm vi tối ưu hẹp hơn và chúng tôi sẽ nói rõ trước khi báo giá."),
     ("Tốc độ ảnh hưởng thứ hạng nhiều không?",
      "Tốc độ là một trong nhiều yếu tố, không phải yếu tố quyết định. Nhưng nó ảnh hưởng trực tiếp "
      "tới tỷ lệ thoát và tỷ lệ chuyển đổi — thường thấy rõ hơn cả thay đổi thứ hạng.")],
)

SERVICES_PAGES = [WEB, SHOP, LANDING, SEO_FULL, SEO_KW, SEO_LOCAL, AUDIT, SPEED]
