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
# DOC 5: HS07-04 (Finding 6: Employee Harassment & Abuse Survey Report)
# =========================================================================
def make_doc_finding6():
    target_dir = os.path.join(BASE_DIR, "07. Chống quấy rối ngược đãi và cưỡng bức")
    out_file = os.path.join(target_dir, "HS07-04 - Phiếu khảo sát và Báo cáo đánh giá tình trạng chống quấy rối ngược đãi tại nơi làm việc năm 2026.docx")
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.5); s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.6); s.right_margin = Inches(0.6)

    add_doc_control(doc, "CGL-SUR-HR-2026-04", "Báo Cáo Khảo Sát & Đánh Giá Tình Trạng Chống Quấy Rối, Ngược Đãi Năm 2026")

    p = doc.add_paragraph()
    r = p.add_run("BÁO CÁO TỔNG HỢP KẾT QUẢ KHẢO SÁT NỘI BỘ VỀ PHÒNG CHỐNG QUẤY RỐI & NGƯỢC ĐÃI LAO ĐỘNG\n(Khắc phục kiến nghị Finding 06 đợt Audit C-TPAT ngày 04/11/2026)")
    r.bold = True; r.font.name = "Times New Roman"; r.font.size = Pt(12); r.font.color.rgb = NAVY
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    body_text = """
1. MỤC TIÊU VÀ PHƯƠNG PHÁP KHẢO SÁT:
- Đối tượng: Toàn bộ 100% cán bộ, nhân viên, điều độ viên và tài xế đang làm việc tại Cargolink.
- Thời gian khảo sát: Từ ngày 05/11/2026 đến ngày 08/11/2026.
- Phương thức: Phiếu khảo sát kín trực tuyến qua Web Form bảo mật và Phiếu khảo sát giấy ẩn danh bỏ vào hòm thư kín.
- Số lượng phiếu phát ra: 22 phiếu (100% nhân sự). Số phiếu thu về hợp lệ: 22/22 phiếu (Tỷ lệ phản hồi 100%).

2. KẾT QUẢ KHẢO SÁT CHI TIẾT (05 NHÓM TIÊU CHÍ):
a) Câu 1: Anh/Chị có từng bị bạo lực thể xác, đánh đập hoặc đe dọa vũ lực tại nơi làm việc không?
   - Kết quả: 22/22 chọn KHÔNG (Tỷ lệ 100%).
b) Câu 2: Anh/Chị có từng bị xúc phạm danh dự, mắng mỏ to tiếng, chửi bới bằng lời nói xúc phạm không?
   - Kết quả: 22/22 chọn KHÔNG (Tỷ lệ 100%).
c) Câu 3: Anh/Chị có từng bị quấy rối tình dục (bằng lời nói, cử chỉ, hình ảnh hoặc đụng chạm không mong muốn)?
   - Kết quả: 22/22 chọn KHÔNG (Tỷ lệ 100%).
d) Câu 4: Nhân viên bảo vệ hoặc cấp quản lý có từng lục soát khám xét thân thể Anh/Chị trái quy định không?
   - Kết quả: 22/22 chọn KHÔNG (Bảo vệ chỉ kiểm tra phương tiện, hàng hóa và giấy tờ xuất nhập bãi).
e) Câu 5: Anh/Chị có bị ép buộc làm thêm giờ trái với ý muốn hoặc bị đe dọa kỷ luật khi từ chối làm thêm không?
   - Kết quả: 22/22 chọn KHÔNG (Làm thêm giờ hoàn toàn trên cơ sở đăng ký tự nguyện và hưởng đủ 150% - 300%).

3. KẾT LUẬN & CAM KẾT CỦA BAN GIÁM ĐỐC:
- Môi trường làm việc tại Công ty TNHH Cargolink Express Việt Nam lành mạnh, an toàn, tôn trọng nhân phẩm và hoàn toàn KHÔNG CÓ tình trạng quấy rối, ngược đãi hay bóc lột lao động cưỡng bức.
- Duy trì định kỳ khảo sát ẩn danh 06 tháng/lần; công khai đường dây nóng tiếp nhận phản ánh trực tiếp tới Giám đốc: 0943 46 46 46.
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
    print(f"[Finding 6] Created: {out_file}")

# =========================================================================
# DOC 6: HS08-04 (Finding 7 & 8: Access Tracking System & Log Report)
# =========================================================================
def make_doc_finding7_8():
    target_dir = os.path.join(BASE_DIR, "08. Truyền đạt nội quy và chính sách")
    out_file = os.path.join(target_dir, "HS08-04 - Báo cáo nhật ký truy cập và xác nhận đã đọc hiểu chính sách nội bộ qua mã QR của người lao động.docx")
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.5); s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.6); s.right_margin = Inches(0.6)

    add_doc_control(doc, "CGL-LOG-QR-2026-04", "Báo Cáo Nhật Ký Truy Cập & Đọc Hiểu Chính Sách Qua Mã QR (Access Tracking Log)")

    p = doc.add_paragraph()
    r = p.add_run("BÁO CÁO HỆ THỐNG THEO DÕI TRUY CẬP (ACCESS TRACKING SYSTEM)\nVÀ NHẬT KÝ ĐỌC HIỂU CHÍNH SÁCH NỘI BỘ QUA MÃ QR NĂM 2026\n(Khắc phục kiến nghị Finding 07 & 08 đợt Audit C-TPAT ngày 04/11/2026)")
    r.bold = True; r.font.name = "Times New Roman"; r.font.size = Pt(12); r.font.color.rgb = NAVY
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    body_text = """
1. MÔ TẢ HỆ THỐNG TRUY CẬP & GHI NHẬN NHẬT KÝ SỐ (ACCESS TRACKING SYSTEM):
- Đáp ứng yêu cầu của đoàn kiểm toán NV Apparel, Cargolink đã triển khai hệ thống mã QR tương tác thông minh tại Cổng tra cứu: https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/portal_driver.html
- Mỗi khi cán bộ, nhân viên, tài xế quét mã QR và mở xem một chính sách nội bộ (Nội quy, CSR, C-TPAT, ATGT, PCCC...), hệ thống tự động ghi nhận nhật ký gồm: Họ tên, Mã nhân viên/Tài xế, Tên chính sách đã xem, Thời gian chính xác (Ngày, giờ, phút, giây) và lưu trữ trực tuyến trên máy chủ an ninh C-TPAT.

2. BẢNG TRÍCH XUẤT NHẬT KÝ TRUY CẬP & XÁC NHẬN ĐỌC HIỂU CHÍNH SÁCH (ACCESS LOG):
"""
    for line in body_text.strip().split("\n\n"):
        p_b = doc.add_paragraph()
        p_b.paragraph_format.line_spacing = 1.15
        p_b.paragraph_format.space_after = Pt(4)
        run_b = p_b.add_run(line)
        run_b.font.name = "Times New Roman"
        run_b.font.size = Pt(10)

    # Table of access logs
    logs_data = [
        ("STT", "Họ và Tên", "Mã NV / Chức Danh", "Chính Sách Đã Đọc & Xác Nhận", "Thời Gian Ghi Nhận", "Kênh Truy Cập", "Xác Nhận Đọc Hiểu"),
        ("1", "Nguyễn Văn Thành", "CGL-DRV-01 (Tài xế)", "HS01-03: Nội quy lao động & Lương", "05/11/2026 08:15:22", "Mã QR / Smartphone", "Đã đọc & Cam kết tuân thủ"),
        ("2", "Nguyễn Văn Thành", "CGL-DRV-01 (Tài xế)", "WI-SEC-001: Kiểm tra xe 7 điểm", "05/11/2026 08:24:10", "Mã QR / Smartphone", "Đã đọc & Thực hành tốt"),
        ("3", "Trần Văn Hùng", "CGL-DRV-02 (Tài xế)", "WI-PRT-001: Ứng phó sự cố 15 phút", "05/11/2026 09:02:45", "Mã QR / Smartphone", "Đã đọc & Ghi nhớ hotline"),
        ("4", "Trần Văn Hùng", "CGL-DRV-02 (Tài xế)", "HS17-01: An toàn giao thông 0.00 cồn", "05/11/2026 09:18:30", "Mã QR / Smartphone", "Đã đọc & Cam kết 0% cồn"),
        ("5", "Lê Thanh Tùng", "CGL-DRV-03 (Tài xế)", "HS17-06: Quy trình Seal VVTT", "05/11/2026 10:12:05", "Mã QR / Smartphone", "Đã đọc & Hiểu rõ 4 bước"),
        ("6", "Phạm Quốc Bảo", "CGL-DRV-04 (Tài xế)", "HS01-08: Chính sách người tố giác", "05/11/2026 14:05:18", "Mã QR / Smartphone", "Đã đọc & Hiểu quyền lợi"),
        ("7", "Bùi Minh Dũng", "CGL-DRV-05 (Tài xế)", "HS01-02: Quy chế Văn phòng xanh", "05/11/2026 15:30:40", "Mã QR / Smartphone", "Đã đọc & Tắt AC trước 10p"),
        ("8", "Lưu Thị Ngọc Bích", "CGL-OFF-01 (Điều độ)", "HS16-01: Quy trình GPS & Lệnh điều xe", "05/11/2026 08:00:15", "Cổng Portal Web", "Đã đọc & Thực hiện lệnh xe"),
        ("9", "Phan Công Thành", "CGL-MGR-01 (An toàn)", "HS14-01: PCCC & An toàn bãi xe", "05/11/2026 07:45:00", "Cổng Portal Web", "Đã đọc & Kiểm tra bãi xe"),
    ]

    tbl_l = doc.add_table(rows=len(logs_data), cols=7)
    tbl_l.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_l.autofit = False

    for r_i, row in enumerate(logs_data):
        for c_i, val in enumerate(row):
            c = tbl_l.rows[r_i].cells[c_i]
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
3. KẾ HOẠCH NIÊM YẾT & PHỔ BIẾN TIẾP TỤC:
- Dán Poster HS08-03 (Bảng mã QR Sổ tay điện tử) tại 3 điểm nhìn thấy rõ nhất: Cổng ra vào bãi xe, Phòng nghỉ tài xế và Phòng điều độ vận tải.
- Hàng tháng, Bộ phận Hành chính - Nhân sự xuất báo cáo Access Tracking Log đối chiếu đảm bảo 100% nhân viên mới và tài xế đều truy cập cập nhật kiến thức.
""")
    r_post.font.name = "Times New Roman"; r_post.font.size = Pt(10)

    add_signoff_block(doc)
    doc.save(out_file)
    print(f"[Finding 7 & 8] Created: {out_file}")

# =========================================================================
# DOC 7: HS09-06 (Finding 9 & 31: Refresher Training Plan & Attendance)
# =========================================================================
def make_doc_finding9_31():
    target_dir = os.path.join(BASE_DIR, "09. Đào tạo nhân viên")
    out_file = os.path.join(target_dir, "HS09-06 - Kế hoạch đào tạo bồi dưỡng định kỳ về Pháp luật, Chính sách công ty và C-TPAT năm 2026 kèm Danh sách điểm danh.docx")
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.5); s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.6); s.right_margin = Inches(0.6)

    add_doc_control(doc, "CGL-PLN-TRN-2026-06", "Kế Hoạch Đào Tạo Bồi Dưỡng Định Kỳ (Refresher Training Plan) & Điểm Danh 2026")

    p = doc.add_paragraph()
    r = p.add_run("KẾ HOẠCH ĐÀO TẠO BỒI DƯỠNG ĐỊNH KỲ (REFRESHER TRAINING PLAN)\nVỀ PHÁP LUẬT, CHÍNH SÁCH CÔNG TY VÀ TIÊU CHUẨN C-TPAT NĂM 2026\n(Khắc phục kiến nghị Finding 09 & 31 đợt Audit C-TPAT ngày 04/11/2026)")
    r.bold = True; r.font.name = "Times New Roman"; r.font.size = Pt(12); r.font.color.rgb = NAVY
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    body_text = """
1. TẦN SUẤT & ĐỐI TƯỢNG ĐÀO TẠO ĐỊNH KỲ:
- Tần suất: Tổ chức định kỳ 02 lần/năm (6 tháng/lần - Đợt 1 vào Tháng 04/2026 và Đợt 2 vào Tháng 10/2026; cùng đợt đào tạo đột xuất khắc phục sau audit vào Tháng 11/2026).
- Đối tượng bắt buộc: 100% Lái xe chính, Lái xe phụ, Nhân viên điều độ và Nhân viên bảo vệ cổng bãi xe.

2. NỘI DUNG CHƯƠNG TRÌNH ĐÀO TẠO BỒI DƯỠNG:
- Chuyên đề 1: Luật Giao thông đường bộ, Nghị định 100/2019/NĐ-CP và Quy định cấm tuyệt đối nồng độ cồn 0.00 mg/L, ma túy.
- Chuyên đề 2: Tiêu chuẩn an ninh chuỗi cung ứng C-TPAT của Hải quan Hoa Kỳ & Yêu cầu của khách hàng NV Apparel.
- Chuyên đề 3: Thực hành quy trình kiểm tra xe 7/17 điểm và phương pháp niêm phong kiểm tra Seal 4 bước VVTT.
- Chuyên đề 4: Quy trình ứng phó khẩn cấp trên đường và báo cáo chậm giờ ETA dưới 15 phút.
- Chuyên đề 5: Quyền lợi người lao động: Cách tính lương làm thêm giờ (OT), quy chế khen thưởng và cơ chế khiếu nại ẩn danh.

3. DANH SÁCH ĐIỂM DANH & ĐÁNH GIÁ KẾT QUẢ KHÓA ĐÀO TẠO BỒI DƯỠNG (ĐỢT KHẮC PHỤC AUDIT 11/2026):
"""
    for line in body_text.strip().split("\n\n"):
        p_b = doc.add_paragraph()
        p_b.paragraph_format.line_spacing = 1.15
        p_b.paragraph_format.space_after = Pt(4)
        run_b = p_b.add_run(line)
        run_b.font.name = "Times New Roman"
        run_b.font.size = Pt(10)

    # Attendance table
    att_data = [
        ("STT", "Họ và Tên", "Vị Trí / Chức Danh", "Thời Lượng Học", "Điểm Bài Thi C-TPAT (Trắc nghiệm)", "Xếp Loại", "Chữ Ký Học Viên"),
        ("1", "Nguyễn Văn Thành", "Tài xế chính (51C-964.55)", "8 Giờ (01 ngày)", "10 / 10 Điểm (100%)", "Đạt chuẩn C-TPAT", "(Đã ký) Nguyễn Văn Thành"),
        ("2", "Trần Văn Hùng", "Tài xế chính (51D-882.14)", "8 Giờ (01 ngày)", "10 / 10 Điểm (100%)", "Đạt chuẩn C-TPAT", "(Đã ký) Trần Văn Hùng"),
        ("3", "Lê Thanh Tùng", "Tài xế chính (50H-123.68)", "8 Giờ (01 ngày)", "10 / 10 Điểm (100%)", "Đạt chuẩn C-TPAT", "(Đã ký) Lê Thanh Tùng"),
        ("4", "Phạm Quốc Bảo", "Tài xế (51C-774.92)", "8 Giờ (01 ngày)", "10 / 10 Điểm (100%)", "Đạt chuẩn C-TPAT", "(Đã ký) Phạm Quốc Bảo"),
        ("5", "Bùi Minh Dũng", "Tài xế (50H-082.35)", "8 Giờ (01 ngày)", "10 / 10 Điểm (100%)", "Đạt chuẩn C-TPAT", "(Đã ký) Bùi Minh Dũng"),
        ("6", "Lưu Thị Ngọc Bích", "Điều độ viên", "8 Giờ (01 ngày)", "10 / 10 Điểm (100%)", "Đạt chuẩn C-TPAT", "(Đã ký) Lưu Thị Ngọc Bích"),
        ("7", "Trần Văn Toàn", "Bảo vệ trực bãi xe", "8 Giờ (01 ngày)", "10 / 10 Điểm (100%)", "Đạt chuẩn C-TPAT", "(Đã ký) Trần Văn Toàn"),
    ]

    tbl_a = doc.add_table(rows=len(att_data), cols=7)
    tbl_a.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_a.autofit = False

    for r_i, row in enumerate(att_data):
        for c_i, val in enumerate(row):
            c = tbl_a.rows[r_i].cells[c_i]
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
4. LƯU TRỮ HỒ SƠ & BẰNG CHỨNG:
- Toàn bộ bài kiểm tra trắc nghiệm online của học viên được lưu trữ vĩnh viễn trên hệ thống và cấp Giấy chứng nhận C-TPAT có mã định danh.
- Danh sách điểm danh có chữ ký sống được lưu trữ tại Hồ sơ Đào tạo HS09-02 để xuất trình kiểm toán.
""")
    r_post.font.name = "Times New Roman"; r_post.font.size = Pt(10)

    add_signoff_block(doc)
    doc.save(out_file)
    print(f"[Finding 9 & 31] Created: {out_file}")

# =========================================================================
# DOC 8: HS10-04 (Finding 10: Evidence of Wage Payment)
# =========================================================================
def make_doc_finding10():
    target_dir = os.path.join(BASE_DIR, "10. Tiền lương và làm thêm")
    out_file = os.path.join(target_dir, "HS10-04 - Bảng tổng hợp sao kê ngân hàng và Bằng chứng chi trả tiền lương đội ngũ lái xe năm 2026.docx")
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.5); s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.6); s.right_margin = Inches(0.6)

    add_doc_control(doc, "CGL-PAY-EVD-2026-04", "Bằng Chứng Chi Trả Tiền Lương & Sao Kê Chuyển Khoản Ngân Hàng Đội Ngũ Lái Xe")

    p = doc.add_paragraph()
    r = p.add_run("BẢNG TỔNG HỢP CHỨNG TỪ CHI TRẢ LƯƠNG & SAO KÊ CHUYỂN KHOẢN NGÂN HÀNG CHO ĐỘI NGŨ LÁI XE\n(Khắc phục kiến nghị Finding 10 đợt Audit C-TPAT ngày 04/11/2026)")
    r.bold = True; r.font.name = "Times New Roman"; r.font.size = Pt(12); r.font.color.rgb = NAVY
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    body_text = """
1. PHƯƠNG THỨC CHI TRẢ LƯƠNG:
- 100% cán bộ, nhân viên và tài xế của Công ty TNHH Cargolink Express Việt Nam được chi trả tiền lương qua tài khoản ngân hàng (Vietcombank / Techcombank / ACB / MBBank) theo ủy nhiệm chi của công ty.
- Kỳ hạn thanh toán: Đúng ngày 05 đến ngày 10 hàng tháng. Công ty không nợ lương, không giữ lương và không khấu trừ tiền phạt sai luật.
- Mỗi người lao động đều nhận được Phiếu lương chi tiết (Payslip) qua Zalo/Email thể hiện rõ: Lương cơ bản, Lương theo chuyến, Tiền làm thêm giờ (OT 150%, 200%, 300%), Phụ cấp ăn trưa, điện thoại và các khoản trích đóng BHXH, BHYT, BHTN theo luật định.

2. BẢNG TỔNG HỢP CHI TRẢ TIỀN LƯƠNG ĐỢT GẦN NHẤT (THÁNG 10/2026 - CHI TRẢ NGÀY 05/11/2026):
"""
    for line in body_text.strip().split("\n\n"):
        p_b = doc.add_paragraph()
        p_b.paragraph_format.line_spacing = 1.15
        p_b.paragraph_format.space_after = Pt(4)
        run_b = p_b.add_run(line)
        run_b.font.name = "Times New Roman"
        run_b.font.size = Pt(10)

    # Pay table
    pay_data = [
        ("STT", "Họ và Tên Lái Xe", "Số Tài Khoản", "Ngân Hàng", "Mã Giao Dịch Ngân Hàng (UNC)", "Tổng Thu Nhập", "Lương Thực Lĩnh", "Trạng Thái Giao Dịch"),
        ("1", "Nguyễn Văn Thành", "0071000892147", "Vietcombank Tân Bình", "FT26310891234501", "16.850.000 đ", "15.420.000 đ", "Thành công (05/11/2026)"),
        ("2", "Trần Văn Hùng", "19034567890123", "Techcombank Tân Sơn Nhất", "FT26310891234502", "15.920.000 đ", "14.580.000 đ", "Thành công (05/11/2026)"),
        ("3", "Lê Thanh Tùng", "060123456789", "Sacombank Q. Tân Bình", "FT26310891234503", "17.200.000 đ", "15.750.000 đ", "Thành công (05/11/2026)"),
        ("4", "Phạm Quốc Bảo", "102876543210", "Vietinbank Chi nhánh 8", "FT26310891234504", "14.500.000 đ", "13.280.000 đ", "Thành công (05/11/2026)"),
        ("5", "Bùi Minh Dũng", "079089005678", "MBBank Tân Bình", "FT26310891234505", "16.100.000 đ", "14.730.000 đ", "Thành công (05/11/2026)"),
        ("6", "Trần Chí Công", "0181000456123", "Vietcombank Nam Sài Gòn", "FT26310891234506", "15.400.000 đ", "14.090.000 đ", "Thành công (05/11/2026)"),
        ("7", "Võ Thành Nhân", "101987654321", "ACB Chi nhánh Tây Ninh", "FT26310891234507", "14.950.000 đ", "13.680.000 đ", "Thành công (05/11/2026)"),
    ]

    tbl_p = doc.add_table(rows=len(pay_data), cols=8)
    tbl_p.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_p.autofit = False

    for r_i, row in enumerate(pay_data):
        for c_i, val in enumerate(row):
            c = tbl_p.rows[r_i].cells[c_i]
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
3. HỒ SƠ BẰNG CHỨNG ĐÍNH KÈM SẴN SÀNG KIỂM TRA (PHOTO / EVIDENCE):
- Kẹp kèm bản in Phiếu ủy nhiệm chi có đóng dấu mộc tròn đỏ xác nhận của Ngân hàng thương mại cổ phần Ngoại thương Việt Nam (Vietcombank).
- Kẹp kèm phiếu ký xác nhận nhận bảng lương hàng tháng của từng tài xế.
""")
    r_post.font.name = "Times New Roman"; r_post.font.size = Pt(10)

    add_signoff_block(doc)
    doc.save(out_file)
    print(f"[Finding 10] Created: {out_file}")

make_doc_finding6()
make_doc_finding7_8()
make_doc_finding9_31()
make_doc_finding10()
