import os

# 1. Update index.html
index_file = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS\index.html"
with open(index_file, 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Replace Card 1
old_c1 = """        <div class="card-tag">⭐ YÊU CẦU 1 / REQUEST 1</div>
        <h3>Phiếu Đánh Giá Mức Độ Hài Lòng Dịch Vụ CGL</h3>
        <div class="card-en">C-TPAT Customer Satisfaction Survey</div>
        <div class="card-desc">
          Dành cho đại diện Khách hàng NV APPAREL (Kho, Logistics, An ninh) đánh giá định kỳ 6 tiêu chí: OTD, tính toàn vẹn seal chì, tác phong tài xế, kỹ thuật xe và điều độ 24/7.
        </div>"""

new_c1 = """        <div class="card-tag">⭐ KHẢO SÁT CHẤT LƯỢNG / SERVICE SURVEY</div>
        <h3>Phiếu Đánh Giá Mức Độ Hài Lòng Dịch Vụ CGL</h3>
        <div class="card-en">Quarterly Transportation Service Satisfaction Survey</div>
        <div class="card-desc">
          Khảo sát toàn diện chất lượng dịch vụ vận chuyển (all over service) định kỳ mỗi 3 tháng gửi tới các bộ phận: Logistics, Scan, Store (Kho), Security (An ninh) của NV APPAREL.
        </div>"""

if old_c1 in idx_content:
    idx_content = idx_content.replace(old_c1, new_c1)
    print("Replaced Card 1 in index.html")

# Replace Card 3
old_c3 = """        <div class="card-tag" style="color: #0B3C5D;">🛡️ YÊU CẦU 3 / REQUEST 3</div>
        <h3>NV CTPAT – Suggestions and Complaints</h3>
        <div class="card-en">Whistleblower & Incident Reporting Channel</div>
        <div class="card-desc">
          Kênh tiếp nhận ý kiến đóng góp, phản ánh chậm trễ ETA, khiếu nại chất lượng và tố giác sự cố an ninh C-TPAT. Hỗ trợ gửi ẩn danh bảo mật 100% theo chính sách HS01-08, cấp mã Ticket tra cứu.
        </div>
      </div>
      
      <div class="qr-preview">
        <img src="qr_form3.png" alt="QR Form 3">
        <div class="qr-caption">Quét mã QR để gửi phản ánh</div>
      </div>

      <a href="form3_complaints.html" class="btn-action">Mở Biểu Mẫu 3 (Góp Ý & Khiếu Nại) ➔</a>"""

new_c3 = """        <div class="card-tag" style="color: #0B3C5D;">📬 HỘP THƯ GÓP Ý & KHIẾU NẠI</div>
        <h3>Hộp Thư Góp Ý & Khiếu Nại C-TPAT NV</h3>
        <div class="card-en">NV CTPAT – Suggestions and Complaints (Google Form)</div>
        <div class="card-desc">
          Biểu mẫu trực tuyến chính thức của Khách hàng NV APPAREL tiếp nhận ý kiến đóng góp, khiếu nại dịch vụ và phản ánh an ninh chuỗi cung ứng C-TPAT.
        </div>
      </div>
      
      <div class="qr-preview">
        <img src="qr_form3.png" alt="QR Form 3">
        <div class="qr-caption">Quét mã QR mở Google Form NV</div>
      </div>

      <a href="https://docs.google.com/forms/d/1WDy9kSA-TzIavBlsSNgcMvU4Wcm0p8yomeZPZ-HgOzo/viewform" target="_blank" class="btn-action">Mở Google Form Tiếp Nhận NV ➔</a>"""

if old_c3 in idx_content:
    idx_content = idx_content.replace(old_c3, new_c3)
    print("Replaced Card 3 in index.html")

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(idx_content)

# 2. Update portal_driver.html
portal_file = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS\portal_driver.html"
with open(portal_file, 'r', encoding='utf-8') as f:
    portal_content = f.read()

portal_content = portal_content.replace(
    'form3_complaints.html',
    'https://docs.google.com/forms/d/1WDy9kSA-TzIavBlsSNgcMvU4Wcm0p8yomeZPZ-HgOzo/viewform'
)

with open(portal_file, 'w', encoding='utf-8') as f:
    f.write(portal_content)
print("Updated portal_driver.html with Google Form link")
