import os, sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026"
FORMS_DIR = os.path.join(BASE_DIR, "CTPAT_QR_FORMS")
ASSETS_DIR = os.path.join(BASE_DIR, "00_BO_BANNER_VA_LOGO_CARGOLINK")
TARGET_DIR = os.path.join(BASE_DIR, "08. Truyền đạt nội quy và chính sách")
DOCX_OUT = os.path.join(TARGET_DIR, "HS08-03 - Bảng mã QR tra cứu Sổ tay điện tử và Quy định an ninh cho Tài xế và CBNV.docx")

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

def create_docx():
    doc = Document()
    for s in doc.sections:
        s.top_margin = Inches(0.6)
        s.bottom_margin = Inches(0.6)
        s.left_margin = Inches(0.6)
        s.right_margin = Inches(0.6)

    # DOCUMENT CONTROL BOX
    tbl_ctrl = doc.add_table(rows=3, cols=4)
    tbl_ctrl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ctrl.autofit = False

    cell_top = tbl_ctrl.rows[0].cells[0]
    for c in tbl_ctrl.rows[0].cells[1:]:
        cell_top.merge(c)
    p0 = cell_top.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r0_1 = p0.add_run("CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM\n")
    r0_1.bold = True
    r0_1.font.name = "Times New Roman"
    r0_1.font.size = Pt(11)
    r0_1.font.color.rgb = NAVY
    r0_2 = p0.add_run("HỆ THỐNG QUẢN LÝ TIÊU CHUẨN ISO 9001 / ISO 14001 / ISO 39001 / ISO 45001 & C-TPAT 2026")
    r0_2.font.name = "Times New Roman"
    r0_2.font.size = Pt(9.5)
    r0_2.font.color.rgb = GRAY
    set_cell_bg(cell_top, "F1F5F9")
    set_cell_border(cell_top, sz="4", color="CBD5E1")

    c_title = tbl_ctrl.rows[1].cells[0]
    c_title.merge(tbl_ctrl.rows[1].cells[1])
    pt = c_title.paragraphs[0]
    rt1 = pt.add_run("TÊN VĂN BẢN / DOCUMENT TITLE:\n")
    rt1.font.name = "Times New Roman"
    rt1.font.size = Pt(8.5)
    rt1.font.color.rgb = GRAY
    rt2 = pt.add_run("Bảng Mã QR Tra Cứu Sổ Tay Điện Tử & Toàn Bộ Chính Sách Công Ty\n(Driver & Staff Digital Handbook & Comprehensive Policy Portal)")
    rt2.bold = True
    rt2.font.name = "Times New Roman"
    rt2.font.size = Pt(10)
    rt2.font.color.rgb = NAVY
    set_cell_border(c_title, sz="4", color="CBD5E1")

    c_cat = tbl_ctrl.rows[1].cells[2]
    c_cat.merge(tbl_ctrl.rows[1].cells[3])
    pc = c_cat.paragraphs[0]
    rc1 = pc.add_run("PHÂN LOẠI & BẢO MẬT / CLASSIFICATION:\n")
    rc1.font.name = "Times New Roman"
    rc1.font.size = Pt(8.5)
    rc1.font.color.rgb = GRAY
    rc2 = pc.add_run("LƯU HÀNH NỘI BỘ (INTERNAL USE ONLY)\nTRUYỀN ĐẠT CHÍNH SÁCH SỐ HÓA C-TPAT")
    rc2.bold = True
    rc2.font.name = "Times New Roman"
    rc2.font.size = Pt(9.5)
    rc2.font.color.rgb = ACCENT
    set_cell_border(c_cat, sz="4", color="CBD5E1")

    meta = [
        ("MÃ TÀI LIỆU / DOC ID:", "CGL-COM-POL-03"),
        ("PHIÊN BẢN / VERSION:", "v2.0 - 2026"),
        ("NGÀY HIỆU LỰC / DATE:", "02/01/2026"),
        ("TRẠNG THÁI / STATUS:", "Chính thức ban hành")
    ]
    for idx, (lbl, val) in enumerate(meta):
        cell = tbl_ctrl.rows[2].cells[idx]
        pm = cell.paragraphs[0]
        r1 = pm.add_run(lbl + "\n")
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(8)
        r1.font.color.rgb = GRAY
        r2 = pm.add_run(val)
        r2.bold = True
        r2.font.name = "Times New Roman"
        r2.font.size = Pt(9)
        set_cell_border(cell, sz="4", color="CBD5E1")

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # TITLE HEADING
    p_h = doc.add_paragraph()
    p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_h = p_h.add_run("BẢNG TỔNG HỢP MÃ QR TRA CỨU SỔ TAY ĐIỆN TỬ, NỘI QUY VÀ CHÍNH SÁCH CÔNG TY\n[TÀI LIỆU LƯU HÀNH NỘI BỘ — DÀNH CHO TOÀN THỂ CÔNG NHÂN VIÊN & ĐỘI XE CARGOLINK]")
    r_h.bold = True
    r_h.font.name = "Times New Roman"
    r_h.font.size = Pt(12.5)
    r_h.font.color.rgb = NAVY

    # PURPOSE & LEGAL NOTICE
    p_pur = doc.add_paragraph()
    r_pur = p_pur.add_run("1. BẢN CHẤT PHÁP LÝ & QUY ĐỊNH LƯU HÀNH NỘI BỘ / LEGAL FRAMEWORK\n")
    r_pur.bold = True
    r_pur.font.name = "Times New Roman"
    r_pur.font.size = Pt(11)
    r_pur.font.color.rgb = NAVY
    
    bullets = [
        "Quy định Lưu hành nội bộ: Toàn bộ Nội quy lao động, Sổ tay nhân viên và các Chính sách an ninh, môi trường, an toàn giao thông là tài liệu LƯU HÀNH NỘI BỘ. Toàn thể 100% người lao động và lái xe Cargolink có quyền và nghĩa vụ đọc hiểu, nắm vững và thực thi nghiêm túc.",
        "Hình thức truyền đạt số hóa (Digital Communication): Việc tạo mã QR và cổng số di động giúp người lao động và lái xe dễ dàng tra cứu 24/7 trên điện thoại, đáp ứng tuyệt đối tiêu chuẩn đánh giá C-TPAT và kiểm toán chuỗi cung ứng của đối tác NV APPAREL.",
        "Bảo vệ bản quyền & Bí mật kinh doanh: Nghiêm cấm sao chép, trích dẫn, phát tán hoặc cung cấp các tài liệu chính sách nội bộ này cho bên thứ ba ngoài mục đích thực hiện hợp đồng vận chuyển với khách hàng."
    ]
    for b in bullets:
        p_b = doc.add_paragraph(style='List Bullet')
        rb = p_b.add_run(b)
        rb.font.name = "Times New Roman"
        rb.font.size = Pt(9.5)
        p_b.paragraph_format.space_after = Pt(2)

    # MASTER QR DIRECTORY TABLE
    p_tab_hdr = doc.add_paragraph()
    r_tab_hdr = p_tab_hdr.add_run("\n2. DANH MỤC MÃ QR TRA CỨU ĐẦY ĐỦ CÁC CHUYÊN ĐỀ / MASTER QR DIRECTORY\n")
    r_tab_hdr.bold = True
    r_tab_hdr.font.name = "Times New Roman"
    r_tab_hdr.font.size = Pt(11)
    r_tab_hdr.font.color.rgb = NAVY

    qr_list = [
        ("Mã QR 0", "portal_driver.html", "qr_portal_driver.png",
         "CỔNG TRA CỨU SỐ TỔNG HỢP (PORTAL HUB)",
         "Cổng trung tâm tra cứu toàn bộ 10 cẩm nang nghiệp vụ an ninh, số hotline 24/7 và 3 biểu mẫu trực tuyến."),
        ("Mã QR 1", "doc_labor_salary_rules.html", "qr_doc7_labor.png",
         "NỘI QUY LAO ĐỘNG, TIỀN LƯƠNG & KỶ LUẬT (HS01-03 / HS10-01)",
         "Thời giờ làm việc, ca kíp lái xe tối đa 10h/ngày, làm thêm giờ tự nguyện 150%-300%, quy chế thưởng và kỷ luật."),
        ("Mã QR 2", "doc_csr_human_rights.html", "qr_doc8_csr.png",
         "BỘ CHUẨN NHÂN QUYỀN & CSR (HS04, HS05, HS06, HS07, HS08)",
         "Cấm tuyệt đối lao động trẻ em, chống lao động cưỡng bức, bình đẳng giới, chế độ thai sản và chống quấy rối."),
        ("Mã QR 3", "doc_staff_handbook.html", "qr_doc6_handbook.png",
         "SỔ TAY NHÂN VIÊN & QUY TẮC ỨNG XỬ CARGOLINK",
         "Quyền lợi BHXH, văn hóa doanh nghiệp, quy chuẩn đồng phục thẻ tên lịch sự khi giao nhận hàng tại NV Apparel."),
        ("Mã QR 4", "doc_whistleblower.html", "qr_doc5_whistleblower.png",
         "CHÍNH SÁCH BẢO VỆ NGƯỜI TỐ GIÁC (HS01-08)",
         "Cam kết không trù dập/trả thù, bảo vệ 100% người báo cáo vi phạm an ninh, kênh tố giác ẩn danh và hotline Giám đốc."),
        ("Mã QR 5", "doc_ctpat_inspection.html", "qr_doc1_inspection.png",
         "KIỂM TRA XE 7/17 ĐIỂM & SEAL VVTT (WI-SEC-001)",
         "Quy trình gõ búa, kiểm tra 7 điểm xe tải, 17 điểm container, và 4 bước kiểm tra niêm phong Seal ISO 17712."),
        ("Mã QR 6", "doc_emergency_sop.html", "qr_doc2_emergency.png",
         "SỔ TAY SỰ CỐ KHẨN CẤP TRÊN ĐƯỜNG 24/7 (WI-PRT-001)",
         "Ứng phó khi bị theo dõi, cướp hàng, tai nạn va chạm, hỏng xe, mất GPS, đứt seal. Báo cáo trong vòng 15 phút."),
        ("Mã QR 7", "doc_cyber_route_security.html", "qr_doc9_cyber.png",
         "AN NINH MẠNG, LỘ TRÌNH & NÔNG NGHIỆP C-TPAT (HS19-01)",
         "Bảo mật thông tin đơn hàng NĐ 13, cấm đăng mạng xã hội, quy định trạm dừng đỗ an toàn và an ninh nông nghiệp."),
        ("Mã QR 8", "doc_traffic_safety.html", "qr_doc3_safety.png",
         "AN TOÀN GIAO THÔNG & CẤM RƯỢU BIA, MA TÚY (ISO 39001)",
         "Chính sách Zero Tolerance nồng độ cồn 0.0 mg/L, lái xe tối đa 4h liên tục, xét nghiệm 5 nhóm chất ma túy định kỳ."),
        ("Mã QR 9", "doc_occupational_safety_pccc.html", "qr_doc10_pccc.png",
         "AN TOÀN LAO ĐỘNG (PPE) & PCCC BÃI XE (ISO 45001)",
         "Bắt buộc mang giày bảo hộ, áo phản quang, mũ cứng; quy trình 4 bước chữa cháy tại chỗ và sơ cấp cứu."),
        ("Mã QR 10", "doc_green_office.html", "qr_doc4_green.png",
         "VĂN PHÒNG XANH & MÔI TRƯỜNG VẬN TẢI (ISO 14001)",
         "Tiết kiệm điện nước, in 2 mặt, phân loại rác 3 ngăn, tắt động cơ khi dừng đỗ quá 5 phút, xử lý dầu nhớt thải."),
        ("Mã QR 11", "form2_knowledge.html", "qr_form2.png",
         "BÀI THI TRẮC NGHIỆM AN NINH C-TPAT TRỰC TUYẾN",
         "10 câu trắc nghiệm an ninh C-TPAT kiểm tra định kỳ tài xế. Tự động chấm điểm và cấp Chứng chỉ điện tử khi đạt >= 80%."),
        ("Mã QR 12", "form3_complaints.html", "qr_form3.png",
         "HỘP THƯ GÓP Ý & KHIẾU NẠI C-TPAT NV (FOR TRUCK DRIVER ONLY)",
         "Biểu mẫu Google Form chính thức của NV Apparel dành riêng cho Tài xế xe tải (For your truck Driver only) gửi góp ý và tố giác an ninh.")
    ]

    tbl_qr = doc.add_table(rows=len(qr_list) + 1, cols=4)
    tbl_qr.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_qr.autofit = False

    headers = ["STT / Mã QR", "Hình Ảnh Mã QR (Scan)", "Tên Tài Liệu & Phân Loại Quy Trình", "Nội Dung Tóm Tắt & Đường Link Public"]
    col_widths = [Inches(0.9), Inches(1.2), Inches(2.3), Inches(2.8)]

    for c_idx, h_text in enumerate(headers):
        cell = tbl_qr.rows[0].cells[c_idx]
        cell.width = col_widths[c_idx]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.bold = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_bg(cell, "071A36")
        set_cell_border(cell, sz="4", color="CBD5E1")

    base_url = "https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/"
    for r_idx, (tag, html_file, qr_png, title, desc) in enumerate(qr_list, start=1):
        row = tbl_qr.rows[r_idx]
        
        c0 = row.cells[0]
        c0.width = col_widths[0]
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(f"{r_idx}\n({tag})")
        r0.bold = True
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(8.5)
        r0.font.color.rgb = NAVY
        set_cell_border(c0, sz="4", color="CBD5E1")

        c1 = row.cells[1]
        c1.width = col_widths[1]
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        qr_path = os.path.join(FORMS_DIR, qr_png)
        if os.path.exists(qr_path):
            p1.add_run().add_picture(qr_path, width=Inches(1.05))
        set_cell_border(c1, sz="4", color="CBD5E1")

        c2 = row.cells[2]
        c2.width = col_widths[2]
        p2 = c2.paragraphs[0]
        r2 = p2.add_run(title)
        r2.bold = True
        r2.font.name = "Times New Roman"
        r2.font.size = Pt(9)
        r2.font.color.rgb = NAVY
        set_cell_border(c2, sz="4", color="CBD5E1")

        c3 = row.cells[3]
        c3.width = col_widths[3]
        p3 = c3.paragraphs[0]
        r3_d = p3.add_run(desc + "\n")
        r3_d.font.name = "Times New Roman"
        r3_d.font.size = Pt(8)
        r3_d.font.color.rgb = GRAY
        
        full_url = base_url + html_file
        r3_u = p3.add_run(full_url)
        r3_u.font.name = "Times New Roman"
        r3_u.font.size = Pt(7.5)
        r3_u.font.color.rgb = ACCENT
        r3_u.underline = True
        set_cell_border(c3, sz="4", color="CBD5E1")

    # SIGN-OFF BLOCK
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    tbl_sign = doc.add_table(rows=2, cols=3)
    tbl_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_sign.autofit = False

    sign_headers = ["NGƯỜI SOẠN THẢO (Prepared by)", "NGƯỜI SOÁT XÉT (Reviewed by)", "NGƯỜI PHÊ DUYỆT & ĐÓNG DẤU (Approved & Sealed by)"]
    for idx, sh in enumerate(sign_headers):
        c = tbl_sign.rows[0].cells[idx]
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(sh)
        r.bold = True
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)
        r.font.color.rgb = NAVY
        set_cell_bg(c, "F1F5F9")
        set_cell_border(c, sz="4", color="CBD5E1")

    c_s0 = tbl_sign.rows[1].cells[0]
    p_s0 = c_s0.paragraphs[0]
    p_s0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_s0.add_run("Ngày ký: 02/01/2026\n\n\n").font.size = Pt(9)
    r_n0 = p_s0.add_run("Lưu Thị Ngọc Bích\n")
    r_n0.bold = True
    r_n0.font.size = Pt(10)
    p_s0.add_run("Chuyên viên QMS / Nhân sự\n(Đã ký số / Lưu hồ sơ)").font.size = Pt(8.5)
    set_cell_border(c_s0, sz="4", color="CBD5E1")

    c_s1 = tbl_sign.rows[1].cells[1]
    p_s1 = c_s1.paragraphs[0]
    p_s1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_s1.add_run("Ngày ký: 02/01/2026\n\n\n").font.size = Pt(9)
    r_n1 = p_s1.add_run("Phan Công Thành\n")
    r_n1.bold = True
    r_n1.font.size = Pt(10)
    p_s1.add_run("Trưởng Bộ phận Vận tải & An toàn\n(Đã soát xét / Phê chuẩn)").font.size = Pt(8.5)
    set_cell_border(c_s1, sz="4", color="CBD5E1")

    c_s2 = tbl_sign.rows[1].cells[2]
    p_s2 = c_s2.paragraphs[0]
    p_s2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_s2.add_run("Ngày ký: 02/01/2026\n").font.size = Pt(9)
    
    stamp_img = os.path.join(ASSETS_DIR, "Cargolink_Director_Signature_and_Seal.png")
    if os.path.exists(stamp_img):
        p_s2.add_run().add_picture(stamp_img, width=Inches(1.8))
        
    r_dir = p_s2.add_run("\nNGUYỄN TẤT THẮNG\n")
    r_dir.bold = True
    r_dir.font.size = Pt(10.5)
    r_dir.font.color.rgb = NAVY
    p_s2.add_run("GIÁM ĐỐC ĐẠI DIỆN PHÁP LUẬT\nCÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM").font.size = Pt(8.5)
    set_cell_border(c_s2, sz="4", color="CBD5E1")

    doc.save(DOCX_OUT)
    print(f"[SUCCESS] Re-generated comprehensive DOCX: {DOCX_OUT}")

if __name__ == "__main__":
    create_docx()
