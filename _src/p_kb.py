# -*- coding: utf-8 -*-
"""Knowledge hub + three articles."""
from blocks import faq, article_ld

CRUMB = [("/kien-thuc/", "Kiến thức")]

HUB = {
    "slug": "/kien-thuc/",
    "title": "Kiến thức website &amp; SEO | WiThemes",
    "desc": "Bài viết về SEO và thiết kế website do đội WiThemes tự biên soạn: SEO là gì, "
            "checklist SEO onpage 27 điểm, Core Web Vitals và tốc độ website.",
    "h1": "Kiến thức website &amp; SEO",
    "crumb": [],
    "body": """
<p>Chúng tôi chỉ viết về những gì thực sự dùng trong dự án. Không dịch máy, không viết cho
đủ số bài. Nếu một bài ở đây sai hoặc lỗi thời, <a href="/lien-he/">báo cho chúng tôi</a>.</p>

<h2>Bài viết mới nhất</h2>
<div class="cardlist">
  <div class="card"><div class="cb">
    <h3><a href="/kien-thuc/seo-la-gi/">SEO là gì? Hiểu đúng trước khi tiêu tiền</a></h3>
    <p class="postmeta">12/08/2026 · 8 phút đọc</p>
    <p>Cơ chế xếp hạng của Google, ba nhóm việc trong SEO, và những lời hứa bạn nên nghi ngờ
    khi đọc báo giá.</p>
    <a class="btn btn-g btn-sm" href="/kien-thuc/seo-la-gi/">Đọc bài</a>
  </div></div>
  <div class="card"><div class="cb">
    <h3><a href="/kien-thuc/checklist-seo-onpage/">Checklist SEO onpage 27 điểm</a></h3>
    <p class="postmeta">12/08/2026 · 10 phút đọc</p>
    <p>Danh sách kiểm tra chúng tôi chạy trên mọi website trước khi bàn giao, chia bốn nhóm
    và có ngưỡng đạt rõ ràng.</p>
    <a class="btn btn-g btn-sm" href="/kien-thuc/checklist-seo-onpage/">Đọc bài</a>
  </div></div>
  <div class="card"><div class="cb">
    <h3><a href="/kien-thuc/core-web-vitals-la-gi/">Core Web Vitals là gì?</a></h3>
    <p class="postmeta">12/08/2026 · 7 phút đọc</p>
    <p>LCP, INP, CLS: ba chỉ số đo trải nghiệm trang, ngưỡng nào là đạt và cách sửa từng
    chỉ số khi bị đỏ.</p>
    <a class="btn btn-g btn-sm" href="/kien-thuc/core-web-vitals-la-gi/">Đọc bài</a>
  </div></div>
</div>

<h2>Chủ đề</h2>
<p class="tags">
  <a href="/kien-thuc/seo-la-gi/">SEO cơ bản</a>
  <a href="/kien-thuc/checklist-seo-onpage/">SEO onpage</a>
  <a href="/kien-thuc/core-web-vitals-la-gi/">Tốc độ website</a>
  <a href="/dich-vu/audit-website/">Audit</a>
  <a href="/dich-vu/seo-local-google-maps/">SEO Local</a>
  <a href="/bang-gia/">Chi phí</a>
</p>

<h2>Cần áp dụng vào website của bạn?</h2>
<p>Đọc là một chuyện, làm là chuyện khác. Nếu muốn có người soi giúp,
<a href="/dich-vu/audit-website/">dịch vụ audit</a> trả về đúng danh sách việc cần làm
cho chính website của bạn.</p>
<p><a class="btn btn-r" href="/lien-he/">Đặt lịch audit</a></p>
""",
}

_A1_FAQ, _A1_LD = faq([
    ("SEO có tốn tiền hằng tháng mãi không?",
     "Không nhất thiết. Nhiều doanh nghiệp thuê 6–12 tháng để dựng nền, sau đó tự duy trì bằng "
     "cách đăng bài đều đặn. Nhưng nếu đối thủ vẫn đầu tư còn bạn dừng hẳn, thứ hạng sẽ trượt dần."),
    ("SEO hay chạy quảng cáo tốt hơn?",
     "Hai công cụ khác nhau. Quảng cáo cho kết quả ngay và tắt là hết; SEO chậm nhưng tích lũy. "
     "Ngân sách nhỏ và cần đơn ngay thì chạy quảng cáo trước, song song làm SEO nền."),
    ("Tôi tự làm SEO được không?",
     "Được, với website nhỏ và ngành ít cạnh tranh. Phần onpage và nội dung hoàn toàn tự làm được "
     "nếu bạn chịu khó. Phần kỹ thuật và xây liên kết là chỗ hay cần người có kinh nghiệm."),
])

A1 = {
    "slug": "/kien-thuc/seo-la-gi/",
    "title": "SEO là gì? Hiểu đúng trước khi tiêu tiền | WiThemes",
    "desc": "SEO là gì, Google xếp hạng dựa trên cái gì, ba nhóm công việc trong SEO và "
            "những lời hứa nên nghi ngờ khi đọc báo giá dịch vụ SEO.",
    "h1": "SEO là gì? Hiểu đúng trước khi tiêu tiền",
    "crumb": CRUMB,
    "og_type": "article",
    "body": """
<p class="postmeta">Cập nhật 12/08/2026 · khoảng 8 phút đọc</p>

<p><strong>SEO (Search Engine Optimization)</strong> là việc làm cho website xuất hiện cao hơn
trong kết quả tìm kiếm tự nhiên — phần không phải quảng cáo. Nói ngắn gọn: bạn làm cho trang
của mình trở thành câu trả lời tốt nhất cho một truy vấn, và làm cho Google nhận ra điều đó.</p>

<h2>Google xếp hạng dựa trên cái gì?</h2>
<p>Không ai ngoài Google biết công thức đầy đủ, nhưng ba trụ cột thì đã rõ từ lâu:</p>
<ol>
  <li><strong>Mức độ liên quan.</strong> Trang của bạn có trả lời đúng thứ người ta hỏi không?
  Đây là lý do "ý định tìm kiếm" quan trọng hơn "mật độ từ khóa".</li>
  <li><strong>Độ tin cậy.</strong> Có ai khác trong ngành dẫn link tới bạn không? Website của bạn
  có lịch sử, có thông tin doanh nghiệp rõ ràng không?</li>
  <li><strong>Trải nghiệm.</strong> Trang tải nhanh, đọc được trên điện thoại, không nhảy layout,
  không che nội dung bằng quảng cáo.</li>
</ol>

<h2>Ba nhóm công việc trong SEO</h2>
<h3>SEO kỹ thuật</h3>
<p>Bảo đảm Google đọc được website: không chặn nhầm trong robots.txt, có sitemap, không trùng
lặp nội dung, chuyển hướng đúng, tốc độ đạt ngưỡng. Đây là phần ít thấy nhất nhưng làm sai
thì mọi thứ phía sau đều vô nghĩa.</p>
<h3>SEO nội dung</h3>
<p>Nghiên cứu người ta gõ gì, viết trang trả lời đúng câu đó, và tổ chức các trang thành cụm
chủ đề liên kết với nhau. Phần lớn ngân sách SEO nên nằm ở đây.</p>
<h3>SEO ngoài trang</h3>
<p>Chủ yếu là liên kết từ website khác trỏ về bạn. Một link từ trang uy tín trong ngành giá trị
hơn một trăm link từ blog rác — và một trăm link rác có thể khiến bạn bị phạt.</p>

<h2>Bạn thực sự mua gì khi thuê dịch vụ SEO?</h2>
<p>Không phải mua thứ hạng — vì không ai bán được thứ hạng. Bạn mua <em>thời gian và kinh
nghiệm</em>: người biết nên viết trang nào trước, sửa lỗi kỹ thuật nào trước, và không làm
những việc có thể khiến website bị phạt.</p>

<blockquote>Một cách kiểm tra nhanh khi nghe báo giá: hỏi "tháng đầu tiên các bạn sẽ làm gì?".
Câu trả lời tốt luôn bắt đầu bằng audit và nghiên cứu từ khóa. Câu trả lời đáng lo là
"chúng tôi đi backlink".</blockquote>

<h2>Những lời hứa nên nghi ngờ</h2>
<table>
<thead><tr><th>Lời hứa</th><th>Vì sao đáng ngờ</th></tr></thead>
<tbody>
<tr><td>"Cam kết top 1 sau 1 tháng"</td>
    <td>Không ai kiểm soát được thuật toán. Từ khóa dễ đến mức lên top sau 1 tháng thường là từ
    khóa không ai tìm.</td></tr>
<tr><td>"Chúng tôi là đối tác của Google"</td>
    <td>Google có chương trình đối tác cho quảng cáo, không có cho SEO.</td></tr>
<tr><td>"5.000 backlink giá 2 triệu"</td>
    <td>Link mua hàng loạt gần như chắc chắn đến từ hệ thống spam.</td></tr>
<tr><td>"Không cần sửa website, chỉ cần SEO"</td>
    <td>Nếu website hỏng kỹ thuật, nội dung mới cũng không cứu được.</td></tr>
</tbody>
</table>

<h2>Bao lâu thì có kết quả?</h2>
<p>Với ngành dịch vụ ở mức cạnh tranh vừa: từ khóa dài bắt đầu chuyển động sau 2–3 tháng,
nhóm từ khóa chính vào top 10 sau 4–8 tháng. Website mới hoàn toàn cần thêm thời gian để
Google tích lũy dữ liệu. Xem <a href="/dich-vu/dich-vu-seo-tong-the/">lộ trình 6 tháng
điển hình</a> của chúng tôi.</p>

<h2>Bắt đầu từ đâu?</h2>
<ol>
  <li>Cài Google Search Console và Google Analytics 4 — miễn phí, và không có chúng thì bạn
  đang làm SEO trong bóng tối.</li>
  <li>Chạy <a href="/kien-thuc/checklist-seo-onpage/">checklist onpage 27 điểm</a> trên
  5 trang quan trọng nhất.</li>
  <li>Liệt kê 20 câu hỏi khách hay hỏi, mỗi câu viết một trang trả lời tử tế.</li>
  <li>Đo lại sau 90 ngày trước khi đổi chiến thuật.</li>
</ol>
""" + _A1_FAQ + """
<p>Đọc tiếp: <a href="/kien-thuc/checklist-seo-onpage/">checklist SEO onpage 27 điểm</a> ·
<a href="/kien-thuc/core-web-vitals-la-gi/">Core Web Vitals là gì</a></p>
""",
    "ld": [article_ld("SEO là gì? Hiểu đúng trước khi tiêu tiền",
                      "Giải thích SEO, cơ chế xếp hạng của Google và ba nhóm công việc trong SEO.",
                      "/kien-thuc/seo-la-gi/"), _A1_LD],
}

_A2_FAQ, _A2_LD = faq([
    ("Phải đạt đủ 27 điểm mới lên top được à?",
     "Không. Onpage là điều kiện cần, không phải điều kiện đủ. Đạt đủ giúp bạn không bị mất điểm "
     "vô ích; phần thắng vẫn nằm ở nội dung và độ tin cậy."),
    ("Bao lâu nên chạy lại checklist?",
     "Mỗi quý một lần cho toàn website, và mỗi lần trước khi xuất bản một trang quan trọng."),
    ("Công cụ nào kiểm tra được các điểm này?",
     "Google Search Console, PageSpeed Insights và trình kiểm tra dữ liệu có cấu trúc của Google "
     "là đủ cho phần lớn mục. Website lớn thì cần thêm một công cụ crawl."),
])

A2 = {
    "slug": "/kien-thuc/checklist-seo-onpage/",
    "title": "Checklist SEO onpage 27 điểm (bản dùng thật) | WiThemes",
    "desc": "Checklist SEO onpage 27 điểm chia bốn nhóm — kỹ thuật, nội dung, hình ảnh, liên kết "
            "— kèm ngưỡng đạt cụ thể để bạn tự soi website của mình.",
    "h1": "Checklist SEO onpage 27 điểm",
    "crumb": CRUMB,
    "og_type": "article",
    "body": """
<p class="postmeta">Cập nhật 12/08/2026 · khoảng 10 phút đọc</p>

<p>Đây là danh sách chúng tôi chạy trên mọi website trước khi bàn giao. Không phải lý thuyết
sưu tầm — mỗi mục đều có ngưỡng đạt để không ai cãi nhau được là "đã tối ưu rồi".</p>

<h2>Nhóm 1: Kỹ thuật (10 điểm)</h2>
<table>
<thead><tr><th>#</th><th>Mục kiểm tra</th><th>Ngưỡng đạt</th></tr></thead>
<tbody>
<tr><td>1</td><td>robots.txt không chặn nhầm tài nguyên</td><td>CSS, JS, ảnh đều cho phép</td></tr>
<tr><td>2</td><td>sitemap.xml có và khai báo trong robots.txt</td><td>Chỉ chứa URL trả về mã 200</td></tr>
<tr><td>3</td><td>Thẻ canonical trên mọi trang</td><td>Trỏ về chính nó, tuyệt đối</td></tr>
<tr><td>4</td><td>Không có trang trùng lặp nội dung</td><td>Dưới 10 phần trăm trùng</td></tr>
<tr><td>5</td><td>Chuyển hướng không tạo chuỗi</td><td>Tối đa 1 bước</td></tr>
<tr><td>6</td><td>Không còn liên kết trả về 404</td><td>0 link gãy nội bộ</td></tr>
<tr><td>7</td><td>HTTPS bắt buộc, không nội dung hỗn hợp</td><td>Không cảnh báo trên trình duyệt</td></tr>
<tr><td>8</td><td>Một phiên bản tên miền duy nhất</td><td>www và không-www hợp nhất</td></tr>
<tr><td>9</td><td>Trang 404 tùy chỉnh có lối đi tiếp</td><td>Có menu và ô tìm kiếm</td></tr>
<tr><td>10</td><td>Khai báo ngôn ngữ trong thẻ html</td><td>lang="vi"</td></tr>
</tbody>
</table>

<h2>Nhóm 2: Nội dung &amp; thẻ meta (7 điểm)</h2>
<table>
<thead><tr><th>#</th><th>Mục kiểm tra</th><th>Ngưỡng đạt</th></tr></thead>
<tbody>
<tr><td>11</td><td>Thẻ title riêng cho từng trang</td><td>50–60 ký tự, có từ khóa chính</td></tr>
<tr><td>12</td><td>Meta description riêng cho từng trang</td><td>140–160 ký tự, có lời mời hành động</td></tr>
<tr><td>13</td><td>Một thẻ H1 duy nhất mỗi trang</td><td>Đúng 1, khác thẻ title</td></tr>
<tr><td>14</td><td>Heading đúng thứ bậc</td><td>Không nhảy từ H2 xuống H4</td></tr>
<tr><td>15</td><td>Nội dung đủ sâu so với top 10</td><td>Không thua quá một nửa độ dài trung bình</td></tr>
<tr><td>16</td><td>URL ngắn, không dấu, có gạch nối</td><td>Dưới 60 ký tự</td></tr>
<tr><td>17</td><td>Nội dung trả lời đúng ý định tìm kiếm</td><td>Đối chiếu với 5 kết quả đầu</td></tr>
</tbody>
</table>

<h2>Nhóm 3: Hình ảnh &amp; tốc độ (5 điểm)</h2>
<table>
<thead><tr><th>#</th><th>Mục kiểm tra</th><th>Ngưỡng đạt</th></tr></thead>
<tbody>
<tr><td>18</td><td>Ảnh có thẻ alt mô tả</td><td>Toàn bộ ảnh nội dung</td></tr>
<tr><td>19</td><td>Ảnh nén và dùng định dạng hiện đại</td><td>WebP, dưới 200KB mỗi ảnh</td></tr>
<tr><td>20</td><td>Khai báo width và height cho ảnh</td><td>Tránh nhảy layout</td></tr>
<tr><td>21</td><td>Ảnh dưới màn hình đầu tải trễ</td><td>loading="lazy"</td></tr>
<tr><td>22</td><td>Điểm PageSpeed trên di động</td><td>Từ 85 điểm</td></tr>
</tbody>
</table>

<h2>Nhóm 4: Liên kết &amp; dữ liệu cấu trúc (5 điểm)</h2>
<table>
<thead><tr><th>#</th><th>Mục kiểm tra</th><th>Ngưỡng đạt</th></tr></thead>
<tbody>
<tr><td>23</td><td>Liên kết nội bộ có văn bản neo mô tả</td><td>Không dùng "xem thêm" trơ trọi</td></tr>
<tr><td>24</td><td>Mọi trang quan trọng cách trang chủ tối đa 3 lần nhấp</td><td>Độ sâu ≤ 3</td></tr>
<tr><td>25</td><td>Breadcrumb hiển thị và có dữ liệu cấu trúc</td><td>Không lỗi khi kiểm tra</td></tr>
<tr><td>26</td><td>Dữ liệu cấu trúc phù hợp loại trang</td><td>Organization, Article, FAQ, Product</td></tr>
<tr><td>27</td><td>Thẻ Open Graph cho mạng xã hội</td><td>Có title, description, image</td></tr>
</tbody>
</table>

<h2>Cách dùng checklist này</h2>
<ol>
  <li>Bắt đầu với 5 trang quan trọng nhất, không phải cả website.</li>
  <li>Nhóm 1 làm trước — lỗi kỹ thuật chặn mọi thứ phía sau.</li>
  <li>Ghi lại điểm số trước khi sửa, để 90 ngày sau còn có cái mà so.</li>
  <li>Đừng tối ưu để đạt điểm số công cụ; tối ưu để người đọc thấy dễ chịu.</li>
</ol>

<div class="note">Không có thời gian tự chạy? <a href="/dich-vu/audit-website/">Dịch vụ audit
website</a> của chúng tôi chính là chạy đúng 27 điểm này trên website của bạn và trả về
báo cáo có thứ tự ưu tiên.</div>
""" + _A2_FAQ + """
<p>Đọc tiếp: <a href="/kien-thuc/core-web-vitals-la-gi/">Core Web Vitals là gì</a> ·
<a href="/kien-thuc/seo-la-gi/">SEO là gì</a></p>
""",
    "ld": [article_ld("Checklist SEO onpage 27 điểm",
                      "Danh sách kiểm tra SEO onpage 27 điểm với ngưỡng đạt cụ thể.",
                      "/kien-thuc/checklist-seo-onpage/"), _A2_LD],
}

_A3_FAQ, _A3_LD = faq([
    ("Core Web Vitals ảnh hưởng thứ hạng bao nhiêu?",
     "Nó là một yếu tố xếp hạng nhưng không phải yếu tố lớn. Giá trị thật nằm ở chỗ trang nhanh "
     "giữ được khách: tỷ lệ thoát giảm và tỷ lệ chuyển đổi tăng."),
    ("Điểm PageSpeed 100 có cần thiết không?",
     "Không. Đạt ngưỡng xanh cho cả ba chỉ số là đủ. Chạy theo 100 điểm thường phải hy sinh tính "
     "năng hoặc hình ảnh, không đáng."),
    ("Dữ liệu phòng thí nghiệm khác dữ liệu thực tế thế nào?",
     "PageSpeed Insights mô phỏng một thiết bị và một đường truyền cố định. Báo cáo trải nghiệm "
     "người dùng thật gom số liệu từ khách của bạn trong 28 ngày — đó mới là cái Google dùng."),
])

A3 = {
    "slug": "/kien-thuc/core-web-vitals-la-gi/",
    "title": "Core Web Vitals là gì? LCP, INP, CLS và ngưỡng đạt | WiThemes",
    "desc": "Giải thích Core Web Vitals: LCP, INP, CLS là gì, ngưỡng nào được coi là đạt, "
            "nguyên nhân thường gặp và cách sửa từng chỉ số khi bị đỏ.",
    "h1": "Core Web Vitals là gì?",
    "crumb": CRUMB,
    "og_type": "article",
    "body": """
<p class="postmeta">Cập nhật 12/08/2026 · khoảng 7 phút đọc</p>

<p><strong>Core Web Vitals</strong> là bộ ba chỉ số Google dùng để đo trải nghiệm thực tế của
người dùng trên một trang web: nội dung hiện ra nhanh không, bấm có phản hồi ngay không,
và bố cục có nhảy lung tung khi đang đọc không.</p>

<h2>Ba chỉ số và ngưỡng đạt</h2>
<table>
<thead><tr><th>Chỉ số</th><th>Đo cái gì</th><th>Tốt</th><th>Cần cải thiện</th><th>Kém</th></tr></thead>
<tbody>
<tr><td><strong>LCP</strong><br>Largest Contentful Paint</td>
    <td>Thời điểm phần tử nội dung lớn nhất hiện ra</td>
    <td>≤ 2,5 giây</td><td>2,5 – 4 giây</td><td>&gt; 4 giây</td></tr>
<tr><td><strong>INP</strong><br>Interaction to Next Paint</td>
    <td>Độ trễ từ khi người dùng bấm tới khi màn hình phản hồi</td>
    <td>≤ 200 ms</td><td>200 – 500 ms</td><td>&gt; 500 ms</td></tr>
<tr><td><strong>CLS</strong><br>Cumulative Layout Shift</td>
    <td>Mức độ bố cục xê dịch ngoài ý muốn</td>
    <td>≤ 0,1</td><td>0,1 – 0,25</td><td>&gt; 0,25</td></tr>
</tbody>
</table>
<p>Một trang được coi là đạt khi <strong>cả ba</strong> chỉ số nằm trong ngưỡng tốt ở phân vị
thứ 75 của người dùng thật — nghĩa là 3 trên 4 lượt truy cập phải đạt.</p>

<h2>LCP kém: nguyên nhân và cách sửa</h2>
<ul>
  <li><strong>Ảnh banner quá nặng.</strong> Nén xuống dưới 200KB, dùng WebP, và không đặt
  loading="lazy" cho ảnh nằm ngay màn hình đầu.</li>
  <li><strong>Máy chủ phản hồi chậm.</strong> Nếu thời gian phản hồi đầu tiên trên 600ms,
  vấn đề nằm ở hosting hoặc thiếu cache, không phải ở giao diện.</li>
  <li><strong>Phông chữ chặn hiển thị.</strong> Dùng font-display: swap và nạp trước phông chính.</li>
  <li><strong>CSS hoặc JS chặn kết xuất.</strong> Tách phần CSS cần cho màn hình đầu, hoãn phần
  còn lại.</li>
</ul>

<h2>INP kém: nguyên nhân và cách sửa</h2>
<ul>
  <li><strong>JavaScript làm việc quá lâu trên luồng chính.</strong> Chia nhỏ tác vụ, hoãn những
  gì không cần ngay khi tải.</li>
  <li><strong>Quá nhiều mã theo dõi.</strong> Mỗi pixel quảng cáo là một khoản nợ hiệu năng;
  gỡ những cái không ai còn xem báo cáo.</li>
  <li><strong>Giao diện nặng.</strong> Bảng dữ liệu hàng nghìn dòng, hiệu ứng trượt phức tạp,
  bộ lọc chạy phía trình duyệt — cân nhắc phân trang hoặc xử lý phía máy chủ.</li>
</ul>

<h2>CLS kém: nguyên nhân và cách sửa</h2>
<ul>
  <li><strong>Ảnh không khai báo kích thước.</strong> Luôn đặt thuộc tính width và height.</li>
  <li><strong>Quảng cáo hoặc banner chèn động.</strong> Dành sẵn chỗ trống đúng kích thước.</li>
  <li><strong>Phông chữ thay đổi làm chữ nhảy.</strong> Chọn phông dự phòng có kích thước gần
  giống phông chính.</li>
  <li><strong>Thông báo cookie đẩy nội dung xuống.</strong> Cho nó nổi lên trên thay vì chèn vào
  dòng chảy trang.</li>
</ul>

<h2>Đo ở đâu</h2>
<ol>
  <li><strong>Google Search Console</strong> – mục Core Web Vitals, dữ liệu người dùng thật,
  gom theo nhóm URL. Đây là nguồn đáng tin nhất.</li>
  <li><strong>PageSpeed Insights</strong> – đo nhanh một URL, có cả dữ liệu thật lẫn mô phỏng.</li>
  <li><strong>Chrome DevTools</strong> – tab Performance, để tìm chính xác đoạn mã nào gây chậm.</li>
</ol>

<blockquote>Đo trên máy tính của bạn với mạng cáp quang rồi kết luận "website nhanh mà" là sai lầm
phổ biến nhất. Hãy xem số liệu người dùng thật, phần lớn họ đang dùng 4G trên điện thoại tầm
trung.</blockquote>

<h2>Đáng đầu tư tới đâu?</h2>
<p>Đưa cả ba chỉ số về ngưỡng xanh là mục tiêu hợp lý. Vượt qua mốc đó, mỗi phần trăm cải thiện
thêm tốn công gấp bội mà thu về rất ít. Nếu website của bạn đang đỏ,
<a href="/dich-vu/toi-uu-toc-do-website/">dịch vụ tối ưu tốc độ</a> xử lý đúng danh sách trên
với cam kết ngưỡng đạt.</p>
""" + _A3_FAQ + """
<p>Đọc tiếp: <a href="/kien-thuc/checklist-seo-onpage/">Checklist SEO onpage 27 điểm</a> ·
<a href="/kien-thuc/seo-la-gi/">SEO là gì</a></p>
""",
    "ld": [article_ld("Core Web Vitals là gì?",
                      "Giải thích LCP, INP, CLS, ngưỡng đạt và cách khắc phục từng chỉ số.",
                      "/kien-thuc/core-web-vitals-la-gi/"), _A3_LD],
}

KB_PAGES = [HUB, A1, A2, A3]
