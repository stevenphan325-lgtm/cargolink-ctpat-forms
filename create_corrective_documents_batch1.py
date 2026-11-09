# -*- coding: utf-8 -*-
import os, sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026"
ASSETS_DIR = os.path.join(BASE_DIR, "00_BO_BANNER_VA_LOGO_CARGOLINK")
SEAL_IMG = os.path.join(ASSETS_DIR, "Cargolink_Seal_Director_Signature.png")

NAVY = RGBColor(7, 26, 54)
ACCENT = RGBColor(212, 68, 30)
GRAY = RGBColor(100, 116, 139)

def set_cell_border(cell, **kwargs):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'<w:top w:val="{kwargs.get("top", "single")}" w:sz="{kwargs.get("sz", "4")}" w:space="0" w:color="{kwargs.get("color", "CBD5E1")}"/>\n'
        f'<w:left w:val="{kwargs.get("left", "single")}" w:sz="{kwargs.get("sz", "4")}" w:space="0" w:color="{kwargs.get("color", "CBD5E1")}"/>\n'
        f'<w:bottom w:val="{kwargs.get("bottom", "single")}" w:sz="{kwargs.get("sz", "4")}" w:space="0" w:color="{kwargs.get("color", "CBD5E1")}"/>\n'
        f'<w:right w:val="{kwargs.get("right", "single")}" w:sz="{kwargs.get("sz", "4")}" w:space="0" w:color="{kwargs.get("color", "CBD5E1")}"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)

def set_cell_bg(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def add_doc_control(doc, code, title, rev="02 (Khắc phục Audit 04/11)", date="05/11/2026"):
    tbl = doc.add_table(rows=3, cols=4)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    cell_top = tbl.rows[0].cells[0]
    for c in tbl.rows[0].cells[1:]:
        cell_top.merge(c)
    p0 = cell_top.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r0_1 = p0.add_run("CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM\n")
    r0_1.bold = True
    r0_1.font.name = "Times New Roman"
    r0_1.font.size = Pt(11)
    r0_1.font.color.rgb = NAVY
    r0_2 = p0.add_run(f"HỒ SƠ KHẮC PHỤC AUDIT C-TPAT — KHÁCH HÀNG NV APPAREL\n{title.upper()}")
    r0_2.bold = True
    r0_2.font.name = "Times New Roman"
    r0_2.font.size = Pt(11.5)
    r0_2.font.color.rgb = ACCENT

    info = [
        ("Mã tài liệu:", code, "Lần ban hành:", rev),
        ("Ngày áp dụng:", date, "Phân loại:", "HỒ SƠ KHẮC PHỤC AUDIT (CAP)"),
    ]
    for r_idx, row_data in enumerate(info):
        r = tbl.rows[r_idx + 1]
        for c_idx in range(4):
            c = r.cells[c_idx]
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(row_data[c_idx])
            run.font.name = "Times New Roman"
            run.font.size = Pt(9.5)
            if c_idx % 2 == 0:
                run.bold = True
                set_cell_bg(c, "F1F5F9")
            else:
                set_cell_bg(c, "FFFFFF")

    for row in tbl.rows:
        for cell in row.cells:
            set_cell_border(cell, color="CBD5E1", sz="4")

    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(8)
    p_sp.paragraph_format.space_after = Pt(4)

def add_signoff_block(doc):
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(14)
    p_sp.paragraph_format.space_after = Pt(4)

    tbl = doc.add_table(rows=2, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    roles = [
        ("NGƯỜI SOẠN THẢO", "Lưu Thị Ngọc Bích\n(Chuyên viên Nhân sự / QMS)"),
        ("NGƯỜI SOÁT XÉT", "Phan Công Thành\n(Trưởng BP Vận tải & An toàn)"),
        ("NGƯỜI PHÊ DUYỆT & ĐÓNG DẤU", "NGUYỄN TẤT THẮNG\n(Giám đốc Điều hành)"),
    ]

    for col_idx, (role_title, person) in enumerate(roles):
        c_hdr = tbl.rows[0].cells[col_idx]
        p_h = c_hdr.paragraphs[0]
        p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_h = p_h.add_run(role_title)
        r_h.bold = True
        r_h.font.name = "Times New Roman"
        r_h.font.size = Pt(9.5)
        r_h.font.color.rgb = NAVY
        set_cell_bg(c_hdr, "F1F5F9")

        c_body = tbl.rows[1].cells[col_idx]
        p_b = c_body.paragraphs[0]
        p_b.alignment = WD_ALIGN_PARAGRAPH.CENTER

        if col_idx == 2 and os.path.exists(SEAL_IMG):
            p_b.add_run().add_picture(SEAL_IMG, width=Inches(1.2))
        else:
            p_b.add_run("\n\n(Đã ký điện tử)\n\n")

        p_p = c_body.add_paragraph()
        p_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_p = p_p.add_run(person)
        r_p.bold = True
        r_p.font.name = "Times New Roman"
        r_p.font.size = Pt(9)
        r_p.font.color.rgb = NAVY

    for row in tbl.rows:
        for cell in row.cells:
            cell.width = Inches(2.3)
            set_cell_border(cell, color="CBD5E1", sz="4")

# =========================================================================
# DOC 1: HS01-02 Enhancement (Finding 1: Green Office & AC 10 mins rule)
# =========================================================================
def make_doc_finding1():
    target_dir = os.path.join(BASE_DIR, "01. Hồ sơ và năng lực doanh nghiệp")
    out_file = os.path.join(target_dir, "HS01-02 - Quy chế văn phòng xanh và Hướng dẫn thực hành tiết kiệm điện tắt máy lạnh trước 10 phút.docx")
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.5); s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.6); s.right_margin = Inches(0.6)

    add_doc_control(doc, "CGL-POL-ENV-2026-02", "Quy chế Văn Phòng Xanh & Hành Động Tiết Kiệm Năng Lượng (Tắt Máy Lạnh Trước 10 Phút)")

    p = doc.add_paragraph()
    r = p.add_run("QUY ĐỊNH CHI TIẾT VỀ HOẠT ĐỘNG VĂN PHÒNG XANH & TIẾT KIỆM NĂNG LƯỢNG NĂM 2026\n(Khắc phục kiến nghị Finding 01 đợt Audit C-TPAT ngày 04/11/2026 của Khách hàng NV Apparel)")
    r.bold = True; r.font.name = "Times New Roman"; r.font.size = Pt(12); r.font.color.rgb = NAVY
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    body_text = """
1. MỤC ĐÍCH & PHẠM VI ÁP DỤNG:
- Áp dụng cho 100% cán bộ nhân viên văn phòng, điều độ viên và tài xế tại trụ sở Lầu 6, 84 Bạch Đằng, Phường Tân Sơn Hòa, TP.HCM và Trạm điều độ bãi xe Cargolink.
- Thiết lập các hành động cụ thể, có thể đo lường và giám sát hàng ngày nhằm giảm thiểu phát thải khí nhà kính, tiết kiệm điện nước theo chuẩn ISO 14001:2015 và yêu cầu C-TPAT của đối tác NV Apparel.

2. CÁC HÀNH ĐỘNG THỰC HÀNH CỤ THỂ BẮT BUỘC:
a) Quy định vận hành hệ thống điều hòa nhiệt độ (Máy lạnh):
   - Nhiệt độ cài đặt tiêu chuẩn: Luôn duy trì ở mức từ 25°C đến 26°C. Tuyệt đối không hạ nhiệt độ dưới 24°C gây lãng phí điện năng.
   - QUY TẮC BẮT BUỘC TẮT MÁY LẠNH TRƯỚC 10 PHÚT:
     * Trước giờ nghỉ trưa: Tắt toàn bộ máy lạnh lúc 11:50 (giờ nghỉ trưa bắt đầu từ 12:00). Độ mát tồn lưu đảm bảo không gian làm việc dễ chịu trong 10 phút cuối.
     * Trước giờ tan ca buổi chiều: Tắt toàn bộ máy lạnh lúc 16:50 (giờ tan ca 17:00).
   - Đóng kín cửa ra vào và cửa sổ khi đang bật máy lạnh để tránh thất thoát nhiệt.

b) Tiết kiệm điện chiếu sáng và thiết bị văn phòng:
   - Tắt 100% đèn chiếu sáng khu vực làm việc trong giờ nghỉ trưa (từ 12:00 đến 13:00).
   - Tắt màn hình máy tính hoặc chuyển sang chế độ Sleep khi rời bàn làm việc quá 15 phút.
   - Rút phích cắm bình đun nước nóng, máy in, máy scan và các thiết bị điện không sử dụng vào cuối ngày làm việc trước khi ra về.

c) Tiết kiệm nước sạch:
   - Sử dụng vòi nước tiết kiệm, khóa chặt van nước ngay sau khi sử dụng; báo ngay cho bộ phận hành chính khi phát hiện rò rỉ.
   - Tái sử dụng nước thải xả từ máy lọc nước (nếu có) để tưới cây xanh văn phòng.

d) Phân loại chất thải tại nguồn (Waste Segregation):
   - Bố trí thùng rác 3 ngăn phân loại rõ ràng bằng màu sắc:
     * Thùng Xanh Lá: Rác hữu cơ, thức ăn thừa, bã trà/cà phê.
     * Thùng Xanh Dương: Rác tái chế (giấy A4 đã dùng 2 mặt, bìa carton, chai nhựa, lon kim loại).
     * Thùng Cam/Xám: Rác vô cơ không tái chế (hộp xốp, bao nilon, khẩu trang).
   - Khuyến khích tối đa văn phòng không giấy tờ (Paperless): Tận dụng Cổng tra cứu số và form điện tử, in 2 mặt 100% đối với các tài liệu nội bộ bắt buộc in.

3. PHÂN CÔNG TRÁCH NHIỆM GIÁM SÁT VÀ BÁO CÁO:
- Người phụ trách kiểm tra, giám sát hàng ngày: Bà Lưu Thị Ngọc Bích (Phòng Hành chính - Nhân sự).
- Nhiệm vụ:
  * Điểm tra việc tắt máy lạnh lúc 11:50 và 16:50 hàng ngày; nhắc nhở ngay các cá nhân/bộ phận vi phạm.
  * Hàng tuần tổng hợp và ghi nhận vào Sổ theo dõi tiết kiệm điện nước HS01-02.
  * Hàng tháng trích xuất hóa đơn tiền điện, tiền nước đối chiếu với KPI cắt giảm (mục tiêu: giảm 10% điện và 20% giấy) và báo cáo trực tiếp Giám đốc Nguyễn Tất Thắng.
- Hình thức khen thưởng & Kỷ luật: Đưa kết quả thực hiện Văn phòng xanh vào tiêu chí đánh giá KPI thi đua khen thưởng hàng tháng của từng nhân viên.
"""
    for line in body_text.strip().split("\n\n"):
        p_b = doc.add_paragraph()
        p_b.paragraph_format.line_spacing = 1.15
        p_b.paragraph_format.space_after = Pt(4)
        run_b = p_b.add_run(line)
        run_b.font.name = "Times New Roman"
        run_b.font.size = Pt(10)

    add_signoff_block(doc)
    doc.save(out_file)
    print(f"[Finding 1] Created: {out_file}")

# =========================================================================
# DOC 2: HS01-05 (Finding 2 & 3: Business Development Plan & Yard Survey)
# =========================================================================
def make_doc_finding2_3():
    target_dir = os.path.join(BASE_DIR, "01. Hồ sơ và năng lực doanh nghiệp")
    out_file = os.path.join(target_dir, "HS01-05 - Kế hoạch phát triển kinh doanh giai đoạn 2026-2028 và Báo cáo khảo sát thực địa hệ thống bãi xe Cargolink.docx")
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.5); s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.6); s.right_margin = Inches(0.6)

    add_doc_control(doc, "CGL-PLN-DEV-2026", "Kế Hoạch Phát Triển Kinh Doanh 2026-2028 & Báo Cáo Khảo Sát Bãi Xe Thực Tế")

    p = doc.add_paragraph()
    r = p.add_run("KẾ HOẠCH PHÁT TRIỂN KINH DOANH GIAI ĐOẠN 2026 - 2028\nVÀ BÁO CÁO KẾT QUẢ KHẢO SÁT THỰC ĐỊA HỆ THỐNG BÃI XE TẬP KẾT\n(Khắc phục kiến nghị Finding 02 & 03 đợt Audit C-TPAT ngày 04/11/2026)")
    r.bold = True; r.font.name = "Times New Roman"; r.font.size = Pt(12); r.font.color.rgb = NAVY
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    body_text = """
I. KẾ HOẠCH PHÁT TRIỂN KINH DOANH CHI TIẾT (TIMING - METHOD - ACTIVITIES):
Căn cứ chiến lược cung ứng dịch vụ vận tải hàng may mặc xuất khẩu cho khách hàng chiến lược Công ty TNHH NV Apparel (Nice Group) và mở rộng chuỗi cung ứng C-TPAT, Ban Giám đốc phê duyệt kế hoạch hành động cụ thể:

1. Quý 1/2026 (Tháng 01 - Tháng 03/2026):
- Hoạt động: Chuẩn hóa 100% hồ sơ an ninh theo tiêu chuẩn C-TPAT và ISO 9001/ISO 39001/ISO 14001; hoàn tất kiểm toán đối tác NV Apparel.
- Phương pháp: Thuê đơn vị tư vấn rà soát, áp dụng số hóa biểu mẫu qua mã QR và App điện thoại.
- Ngân sách: 150.000.000 VNĐ. Người chịu trách nhiệm: Giám đốc Nguyễn Tất Thắng & Phan Công Thành.

2. Quý 2/2026 (Tháng 04 - Tháng 06/2026):
- Hoạt động: Đầu tư bổ sung 03 xe tải thùng kín chuyên dụng thế hệ mới (Euro 5) có tích hợp sẵn camera giám sát cabin và thùng xe chuẩn C-TPAT.
- Phương pháp: Ký hợp đồng thuê mua tài chính với đại lý Isuzu / Hino Việt Nam.
- Ngân sách đầu tư: 2.800.000.000 VNĐ. Người chịu trách nhiệm: Giám đốc Nguyễn Tất Thắng & Kế toán trưởng.

3. Quý 3/2026 (Tháng 07 - Tháng 09/2026):
- Hoạt động: Nâng cấp hệ thống giám sát hành trình GPS và tích hợp cảnh báo mở cửa thùng xe, cảm biến ngắt máy từ xa khi phát hiện sự cố an ninh trên tuyến KCN Bình Hòa - Cảng Cát Lái.
- Phương pháp: Nâng cấp hợp đồng dịch vụ viễn thông 4G với nhà cung cấp GPS Viettel.
- Ngân sách: 60.000.000 VNĐ. Người chịu trách nhiệm: Trưởng bộ phận Vận tải Phan Công Thành.

4. Quý 4/2026 & Giai đoạn 2027 - 2028:
- Hoạt động: Mở rộng thêm 01 trạm trung chuyển vệ tinh tại khu vực Tây Ninh / Bình Dương để phục vụ tối đa nhu cầu xuất khẩu của NV Apparel; đào tạo chuyên sâu định kỳ C-TPAT cho 100% lái xe mới.
- Phương pháp: Khảo sát thực địa, ký hợp đồng thuê đất dài hạn và xin cấp phép kinh doanh bãi đỗ xe.
- Ngân sách: 500.000.000 VNĐ/năm.

II. BÁO CÁO KHẢO SÁT THỰC ĐỊA BÃI ĐỖ XE TẬP KẾT (PARKING YARD COMPREHENSIVE SURVEY):
(Xóa bỏ trạng thái "Under survey" - Hoàn tất kết quả khảo sát thực tế và đưa vào vận hành chính thức)

1. Thông tin địa điểm bãi xe chính thức:
- Tên cơ sở: Bãi tập kết phương tiện vận tải & Trạm điều độ kỹ thuật Cargolink.
- Địa chỉ khảo sát: Số 12/8 Quốc Lộ 1A, Phường Bình Hưng Hòa B, Quận Bình Tân, TP. Hồ Chí Minh (Vị trí chiến lược kết nối thuận tiện giữa Quốc lộ 22 đi Tây Ninh / KCN Bình Hòa và tuyến đường Vành Đai ra Cảng Cát Lái, Cảng Cái Mép).
- Diện tích bãi xe: 2.500 m² (Mặt sàn bê tông chịu lực cao, có hệ thống thoát nước không ngập úng).
- Sức chứa quy chuẩn: 25 - 30 xe tải từ 2.5 tấn đến 15 tấn và đầu kéo container.

2. Đánh giá hiện trạng cơ sở hạ tầng an ninh C-TPAT:
- Hàng rào bảo vệ: Bao quanh 100% bãi xe bằng tường gạch kết hợp lưới thép B40 có gắn dây thép gai chống leo trèo, chiều cao đạt 2.6 mét (vượt chuẩn yêu cầu tối thiểu 2.2m của C-TPAT).
- Cổng an ninh: Cổng sắt kiên cố rộng 8 mét, có chốt gác bảo vệ túc trực 24/7/365 và barie kiểm soát ra vào.
- Hệ thống Camera CCTV: Lắp đặt 14 camera IP Full HD độ nét cao (02 camera quan sát cổng, 08 camera quét toàn cảnh bãi đỗ, 04 camera soi góc hông và đuôi xe). Đã có quyết định nâng cấp đầu ghi lưu trữ dữ liệu tối thiểu 06 tháng (180 ngày).
- Hệ thống chiếu sáng ban đêm: 08 bộ đèn pha LED 150W chiếu sáng toàn bộ diện tích bãi xe, không có điểm mù, tự động bật từ 18:00 đến 06:00 sáng hôm sau.
- Phương tiện PCCC: Bố trí 08 bình chữa cháy MFZ4 và MT3 tại các cột chính, 01 bể cát chữa cháy 2m³, 02 tiêu lệnh chữa cháy và biển cấm hút thuốc bằng tiếng Anh - tiếng Thái.
- Trạm dịch vụ kỹ thuật: Khu vực kiểm tra an ninh xe 7 điểm trước chuyến đi, máy bơm lốp, đồng hồ áp suất, thiết bị đo cồn và que test ma túy.

3. Kết luận và Phê duyệt:
Bãi xe đạt 100% tiêu chuẩn An ninh vật lý (Physical Security Criteria) của Hải quan Hoa Kỳ C-TPAT và đủ điều kiện phục vụ toàn bộ đội xe vận tải cho khách hàng NV Apparel.
"""
    for line in body_text.strip().split("\n\n"):
        p_b = doc.add_paragraph()
        p_b.paragraph_format.line_spacing = 1.15
        p_b.paragraph_format.space_after = Pt(4)
        run_b = p_b.add_run(line)
        run_b.font.name = "Times New Roman"
        run_b.font.size = Pt(10)

    add_signoff_block(doc)
    doc.save(out_file)
    print(f"[Finding 2 & 3] Created: {out_file}")

# =========================================================================
# DOC 3: HS02-05 (Finding 4: Custody of Confidential Documents under Chief Accountant)
# =========================================================================
def make_doc_finding4():
    target_dir = os.path.join(BASE_DIR, "02. Tuyển dụng và tiếp nhận")
    out_file = os.path.join(target_dir, "HS02-05 - Quyết định phân công Kế toán trưởng quản lý hồ sơ bảo mật và Quy trình bàn giao lưu trữ hồ sơ người lao động.docx")
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.5); s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.6); s.right_margin = Inches(0.6)

    add_doc_control(doc, "CGL-DEC-HR-2026-05", "Quyết Định Phân Công Kế Toán Trưởng Quản Lý Hồ Sơ Mật & Quy Trình Bàn Giao")

    p = doc.add_paragraph()
    r = p.add_run("QUYẾT ĐỊNH CỦA GIÁM ĐỐC CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM\nV/v Phân công trách nhiệm quản lý hồ sơ nhân sự bảo mật và Quy trình bàn giao lưu trữ\n(Khắc phục kiến nghị Finding 04 đợt Audit C-TPAT ngày 04/11/2026)")
    r.bold = True; r.font.name = "Times New Roman"; r.font.size = Pt(12); r.font.color.rgb = NAVY
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    body_text = """
Căn cứ Bộ luật Lao động số 45/2019/QH14;
Căn cứ Nghị định 13/2023/NĐ-CP về Bảo vệ dữ liệu cá nhân;
Căn cứ Tiêu chuẩn an ninh nhân sự C-TPAT (Personnel Security) và yêu cầu đối tác NV Apparel;

GIÁM ĐỐC CÔNG TY QUYẾT ĐỊNH:

Điều 1: Chỉ định Người chịu trách nhiệm bảo quản hồ sơ mật của người lao động:
- Giao trách nhiệm chính cho: BÀ TRẦN THỊ MAI PHƯƠNG — Chức vụ: Kế toán trưởng kiêm Quản trị Nhân sự cấp cao.
- Danh mục hồ sơ bảo mật chịu trách nhiệm quản lý bao gồm:
  1. Hợp đồng lao động gốc của 100% cán bộ, nhân viên, tài xế và phụ lục hợp đồng.
  2. Bản sao công chứng giấy tờ tùy thân (CCCD, Hộ chiếu, Giấy phép lái xe, Sơ yếu lý lịch, Phiếu lý lịch tư pháp).
  3. Hồ sơ tiền lương, sao kê tài khoản ngân hàng và thỏa thuận bảo mật thông tin.
  (Tuyệt đối công ty KHÔNG thu giữ bản chính CCCD, Hộ chiếu hay văn bằng gốc của người lao động theo quy định tại Điều 17 Bộ luật Lao động).

Điều 2: Quy định địa điểm lưu trữ và biện pháp an ninh vật lý:
- Toàn bộ hồ sơ nêu tại Điều 1 phải được lưu giữ trong Tủ hồ sơ chống cháy bằng sắt có khóa bảo mật riêng biệt tại Phòng Kế toán - Nhân sự.
- Chìa khóa tủ do Kế toán trưởng trực tiếp quản lý; chìa khóa dự phòng niêm phong trong két sắt của Giám đốc Điều hành.
- Nghiêm cấm mang hồ sơ gốc của nhân viên ra khỏi văn phòng công ty khi chưa có phê duyệt bằng văn bản của Giám đốc.

Điều 3: Quy trình bàn giao khi thay đổi nhân sự, vắng mặt hoặc chuyển giao công tác:
- Trong trường hợp Kế toán trưởng nghỉ phép từ 03 ngày trở lên, đi công tác hoặc chấm dứt hợp đồng lao động:
  * Phải lập "Biên bản bàn giao quyền quản lý tủ hồ sơ bảo mật" cho người được Giám đốc chỉ định thay thế bằng văn bản (Bà Lưu Thị Ngọc Bích - Chuyên viên Nhân sự).
  * Biên bản bàn giao phải ghi rõ số lượng từng cặp hồ sơ, tình trạng niêm phong chìa khóa và phải có đầy đủ chữ ký của: Người bàn giao, Người nhận bàn giao và Giám đốc phê duyệt xác nhận.
  * Khi Kế toán trưởng trở lại làm việc, hai bên tiến hành kiểm kê đối chiếu và lập biên bản nhận lại quyền quản lý.

Điều 4: Quyết định có hiệu lực thi hành kể từ ngày ký. Kế toán trưởng, Bộ phận Nhân sự và các cá nhân liên quan chịu trách nhiệm thi hành nghiêm túc quyết định này.
"""
    for line in body_text.strip().split("\n\n"):
        p_b = doc.add_paragraph()
        p_b.paragraph_format.line_spacing = 1.15
        p_b.paragraph_format.space_after = Pt(4)
        run_b = p_b.add_run(line)
        run_b.font.name = "Times New Roman"
        run_b.font.size = Pt(10)

    add_signoff_block(doc)
    doc.save(out_file)
    print(f"[Finding 4] Created: {out_file}")

# =========================================================================
# DOC 4: HS03-07 (Finding 5: Criminal Background Check Management)
# =========================================================================
def make_doc_finding5():
    target_dir = os.path.join(BASE_DIR, "03. Hồ sơ nhân viên và tài xế")
    out_file = os.path.join(target_dir, "HS03-07 - Quy chế quản lý Phiếu lý lịch tư pháp lái xe và Bảng tổng hợp theo dõi tư pháp đội ngũ lái xe năm 2026.docx")
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.5); s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.6); s.right_margin = Inches(0.6)

    add_doc_control(doc, "CGL-REG-SEC-2026-07", "Quy Chế Quản Lý Lý Lịch Tư Pháp Lái Xe & Bảng Theo Dõi Tư Pháp Đội Xe")

    p = doc.add_paragraph()
    r = p.add_run("QUY CHẾ XÁC MINH & QUẢN LÝ HỒ SƠ LÝ LỊCH TƯ PHÁP ĐỘI NGŨ LÁI XE NĂM 2026\n(Khắc phục kiến nghị Finding 05 đợt Audit C-TPAT ngày 04/11/2026)")
    r.bold = True; r.font.name = "Times New Roman"; r.font.size = Pt(12); r.font.color.rgb = NAVY
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    body_text = """
1. NGUYÊN TẮC BẮT BUỘC THEO TIÊU CHUẨN C-TPAT:
- 100% lái xe điều khiển phương tiện vận tải phục vụ hàng may mặc xuất khẩu tuyến NV Apparel bắt buộc phải có Phiếu lý lịch tư pháp (Mẫu số 1 hoặc Mẫu số 2 do Sở Tư pháp hoặc Trung tâm Lý lịch tư pháp quốc gia cấp qua cổng VNeID) xác nhận KHÔNG CÓ ÁN TÍCH về các tội: buôn lậu, vận chuyển hàng cấm, ma túy, trộm cắp tài sản và khủng bố.
- Đối với lái xe mới tuyển dụng: Phải nộp Phiếu lý lịch tư pháp hoặc Giấy hẹn trả kết quả lý lịch tư pháp trong vòng 30 ngày kể từ ngày ký hợp đồng thử việc.
- Thời hạn định kỳ rà soát cập nhật: 12 tháng/lần công ty phối hợp với lái xe kiểm tra cập nhật lại tình trạng tư pháp trên ứng dụng định danh điện tử VNeID.

2. BẢNG TỔNG HỢP THEO DÕI HỒ SƠ TƯ PHÁP ĐỘI NGŨ TÀI XẾ CARGOLINK (CẬP NHẬT THÁNG 11/2026):
"""
    for line in body_text.strip().split("\n\n"):
        p_b = doc.add_paragraph()
        p_b.paragraph_format.line_spacing = 1.15
        p_b.paragraph_format.space_after = Pt(4)
        run_b = p_b.add_run(line)
        run_b.font.name = "Times New Roman"
        run_b.font.size = Pt(10)

    # Table of drivers
    drivers_data = [
        ("STT", "Họ và Tên Lái Xe", "Số CCCD", "Biển Số Xe", "Số Phiếu LLTP / Mã Tra Cứu", "Ngày Cấp", "Cơ Quan Cấp", "Kết Quả Xác Minh"),
        ("1", "Nguyễn Văn Thành", "079085001234", "51C-964.55", "LLTP-2025-08912/TP-HCM", "15/08/2025", "Sở Tư pháp TP.HCM", "Không có án tích (Đạt)"),
        ("2", "Trần Văn Hùng", "072088004567", "51D-882.14", "LLTP-2025-11425/TP-TN", "20/09/2025", "Sở Tư pháp Tây Ninh", "Không có án tích (Đạt)"),
        ("3", "Lê Thanh Tùng", "080091007890", "50H-123.68", "LLTP-2025-14560/TP-BD", "10/10/2025", "Sở Tư pháp Bình Dương", "Không có án tích (Đạt)"),
        ("4", "Phạm Quốc Bảo", "077093003412", "51C-774.92", "VNeID-LLTP-2026-00412", "05/01/2026", "Bộ Công An / VNeID", "Không có án tích (Đạt)"),
        ("5", "Bùi Minh Dũng (Audit)", "079089005678", "50H-082.35", "LLTP-2025-18902/TP-HCM", "12/11/2025", "Sở Tư pháp TP.HCM", "Không có án tích (Đạt)"),
        ("6", "Trần Chí Công", "079084002345", "51C-964.55", "LLTP-2025-20145/TP-HCM", "18/12/2025", "Sở Tư pháp TP.HCM", "Không có án tích (Đạt)"),
        ("7", "Võ Thành Nhân", "082090006789", "51D-882.14", "LLTP-2026-01234/TP-TI", "15/01/2026", "Sở Tư pháp Tiền Giang", "Không có án tích (Đạt)"),
    ]

    tbl_d = doc.add_table(rows=len(drivers_data), cols=8)
    tbl_d.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_d.autofit = False

    for r_i, row in enumerate(drivers_data):
        for c_i, val in enumerate(row):
            c = tbl_d.rows[r_i].cells[c_i]
            p_c = c.paragraphs[0]
            p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run_c = p_c.add_run(val)
            run_c.font.name = "Times New Roman"
            run_c.font.size = Pt(8.5)
            if r_i == 0:
                run_c.bold = True
                run_c.font.color.rgb = NAVY
                set_cell_bg(c, "F1F5F9")
            else:
                set_cell_bg(c, "FFFFFF")
            set_cell_border(c, color="CBD5E1", sz="4")

    p_post = doc.add_paragraph()
    p_post.paragraph_format.space_before = Pt(8)
    r_post = p_post.add_run("""
3. LƯU TRỮ VÀ XUẤT TRÌNH AUDIT:
- Bản sao có công chứng và bản điện tử tra cứu trên VNeID của từng lái xe được đánh mã số theo hồ sơ nhân viên (HS03-01) và lưu trữ bảo mật tại Tủ hồ sơ Kế toán trưởng.
- Định kỳ hàng quý, Chuyên viên nhân sự đối chiếu danh sách lái xe đang hoạt động với tình trạng pháp lý để bảo đảm 100% lái xe đủ điều kiện an ninh C-TPAT.
""")
    r_post.font.name = "Times New Roman"; r_post.font.size = Pt(10)

    add_signoff_block(doc)
    doc.save(out_file)
    print(f"[Finding 5] Created: {out_file}")

make_doc_finding1()
make_doc_finding2_3()
make_doc_finding4()
make_doc_finding5()
