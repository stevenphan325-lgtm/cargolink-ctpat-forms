# -*- coding: utf-8 -*-
import os, sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026"
FORMS_DIR = os.path.join(BASE_DIR, "CTPAT_QR_FORMS")
ASSETS_DIR = os.path.join(BASE_DIR, "00_BO_BANNER_VA_LOGO_CARGOLINK")
TARGET_DIR = os.path.join(BASE_DIR, "16. Thông tin xe và theo dõi chuyến")
DOCX_OUT = os.path.join(TARGET_DIR, "HS16-02 - Bảng mã QR các công cụ vận hành số hóa và biểu mẫu điện tử C-TPAT.docx")
PNG_OUT_TARGET = os.path.join(TARGET_DIR, "HS16-02 - Bảng mã QR các công cụ vận hành số hóa và biểu mẫu điện tử C-TPAT.png")
POSTER_PNG_OUT = os.path.join(ASSETS_DIR, "HS16-02_POSTER_MA_QR_10_CONG_CU_VAN_HANH_SO_HOA_C_TPAT.png")
BRAIN_DIR = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163"

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
        s.top_margin = Inches(0.4)
        s.bottom_margin = Inches(0.4)
        s.left_margin = Inches(0.4)
        s.right_margin = Inches(0.4)

    # Document Control
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
    r0_2 = p0.add_run("HỆ THỐNG CÔNG CỤ VẬN HÀNH SỐ HÓA & BIỂU MẪU ĐIỆN TỬ C-TPAT — TUYẾN NV APPAREL")
    r0_2.bold = True
    r0_2.font.name = "Times New Roman"
    r0_2.font.size = Pt(12)
    r0_2.font.color.rgb = ACCENT

    info_data = [
        ("Mã tài liệu:", "CGL-QR-OPS-2026", "Lần ban hành:", "02 (Số hóa toàn diện)"),
        ("Ngày áp dụng:", "02/01/2026", "Phân loại:", "TÀI LIỆU LƯU HÀNH NỘI BỘ"),
    ]
    for r_idx, row_data in enumerate(info_data):
        r = tbl_ctrl.rows[r_idx + 1]
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

    for row in tbl_ctrl.rows:
        for cell in row.cells:
            set_cell_border(cell, color="CBD5E1", sz="4")

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(10)
    p_title.paragraph_format.space_after = Pt(2)
    run_t = p_title.add_run("DANH MỤC 10 CÔNG CỤ VẬN HÀNH SỐ HÓA & MÃ QR TRUY CẬP TRỰC TIẾP")
    run_t.bold = True
    run_t.font.name = "Times New Roman"
    run_t.font.size = Pt(13)
    run_t.font.color.rgb = NAVY

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(8)
    r_sub = p_sub.add_run("Áp dụng cho 100% Lái xe, Điều độ viên, Cán bộ An toàn và Bảo vệ bãi xe — Thay thế hoàn toàn hồ sơ giấy")
    r_sub.italic = True
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = GRAY

    # Table of 10 tools
    tools_data = [
        ("1. Kiểm Tra An Ninh Xe 7/17 Điểm", "qr_app1_inspection.png", "app_vehicle_inspection.html", "Checklist kiểm tra 7 điểm xe tải & 17 điểm rơ-moóc trước chuyến đi theo chuẩn WI-SEC-001, tích hợp chữ ký số."),
        ("2. Kiểm Tra Niêm Phong Seal VVTT", "qr_app2_seal.png", "app_seal_vvtt_log.html", "Thực hiện 4 bước View - Verify - Tug - Twist đối với Seal High Security ISO 17712, đại diện Kho NV và Tài xế ký bàn giao."),
        ("3. Sổ Kiểm Tra Nồng Độ Cồn & Ma Túy", "qr_app3_alcohol.png", "app_alcohol_test_log.html", "Kiểm tra trước khi nhận lệnh: Đo nồng độ cồn (0.00 mg/L) và test sàng lọc 5 nhóm chất ma túy âm tính (-) theo ISO 39001."),
        ("4. Báo Cáo Sự Cố 15 Phút Khẩn Cấp", "qr_app4_incident.png", "app_incident_rapid_report.html", "Kích hoạt trong 15 phút khi chậm ETA, xe hỏng, seal đứt, bám đuôi. Lấy tọa độ GPS tự động và gọi khẩn cấp 24/7."),
        ("5. Lệnh Điều Xe Điện Tử Tuyến NV", "qr_app5_dispatch.png", "app_trip_dispatch_log.html", "Phát lệnh điều xe điện tử, quản lý lộ trình từ Nhà máy NV đến Cảng Cát Lái/Tân Sơn Nhất, trạm dừng phê duyệt."),
        ("6. Kiểm Tra PCCC & Trang Bị PPE", "qr_app6_ppe.png", "app_ppe_pccc_log.html", "Kiểm tra định kỳ bình chữa cháy MFZ4/CO2 áp kế xanh, tam giác phản quang, túi sơ cứu và bảo hộ lao động mũi thép."),
        ("7. Sổ Nhật Ký Kiểm Soát Cổng Bãi Xe", "qr_app7_visitor.png", "app_visitor_gate_log.html", "Đăng ký khách, nhà thầu, phương tiện ra vào bãi xe điều độ C-TPAT, cấp phát thẻ khách và kiểm tra an ninh."),
        ("8. Sổ Năng Lượng & Văn Phòng Xanh", "qr_app8_green.png", "app_green_office_log.html", "Theo dõi chỉ số điện (kWh), nước sạch (m³), giấy in A4, rác thải tái chế và định mức dầu xe chuẩn ISO 14001."),
        ("9. Bảng Đánh Giá Nhà Xe Thầu Phụ", "qr_app9_subcontractor.png", "app_subcontractor_eval.html", "Thang điểm 100 thẩm định năng lực an ninh đối tác vận tải: GPKD, bảo hiểm, 100% xe GPS, lý lịch tư pháp tài xế."),
        ("10. Checklist Tự Kiểm Toán C-TPAT", "qr_app10_audit.png", "app_ctpat_audit_checklist.html", "Đối chiếu toàn diện 12 tiêu chuẩn an ninh C-TPAT Hải quan Hoa Kỳ, tự động chấm điểm sẵn sàng tiếp đoàn NV Apparel."),
    ]

    tbl_apps = doc.add_table(rows=5, cols=4)
    tbl_apps.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_apps.autofit = False

    widths = [Inches(1.05), Inches(2.6), Inches(1.05), Inches(2.6)]

    for idx, (title, qr_file, html_file, desc) in enumerate(tools_data):
        row_idx = idx // 2
        col_offset = (idx % 2) * 2

        cell_qr = tbl_apps.rows[row_idx].cells[col_offset]
        cell_info = tbl_apps.rows[row_idx].cells[col_offset + 1]

        qr_path = os.path.join(FORMS_DIR, qr_file)
        p_qr = cell_qr.paragraphs[0]
        p_qr.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if os.path.exists(qr_path):
            p_qr.add_run().add_picture(qr_path, width=Inches(0.9), height=Inches(0.9))

        p_inf = cell_info.paragraphs[0]
        p_inf.paragraph_format.space_before = Pt(2)
        p_inf.paragraph_format.space_after = Pt(2)
        r_t = p_inf.add_run(f"{title}\n")
        r_t.bold = True
        r_t.font.name = "Times New Roman"
        r_t.font.size = Pt(9.5)
        r_t.font.color.rgb = NAVY

        r_d = p_inf.add_run(f"{desc}\n")
        r_d.font.name = "Times New Roman"
        r_d.font.size = Pt(8.5)
        r_d.font.color.rgb = RGBColor(51, 65, 85)

        r_u = p_inf.add_run(f"🌐 Link: .../{html_file}")
        r_u.font.name = "Courier New"
        r_u.font.size = Pt(7.5)
        r_u.font.color.rgb = ACCENT

        set_cell_bg(cell_qr, "F8FAFC")
        set_cell_bg(cell_info, "FFFFFF")

    for row in tbl_apps.rows:
        for i, cell in enumerate(row.cells):
            cell.width = widths[i]
            set_cell_border(cell, color="CBD5E1", sz="4")

    # 3-Tier Sign-off Block
    p_sign_hdr = doc.add_paragraph()
    p_sign_hdr.paragraph_format.space_before = Pt(12)
    p_sign_hdr.paragraph_format.space_after = Pt(2)

    tbl_sign = doc.add_table(rows=2, cols=3)
    tbl_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_sign.autofit = False

    roles = [
        ("NGƯỜI SOẠN THẢO", "Lưu Thị Ngọc Bích\n(Chuyên viên Nhân sự / QMS)"),
        ("NGƯỜI SOÁT XÉT", "Phan Công Thành\n(Trưởng BP Vận tải & An toàn)"),
        ("NGƯỜI PHÊ DUYỆT & ĐÓNG DẤU", "NGUYỄN TẤT THẮNG\n(Giám đốc Điều hành)"),
    ]

    seal_path = os.path.join(ASSETS_DIR, "Cargolink_Seal_Director_Signature.png")

    for col_idx, (role_title, person) in enumerate(roles):
        c_hdr = tbl_sign.rows[0].cells[col_idx]
        p_h = c_hdr.paragraphs[0]
        p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_h = p_h.add_run(role_title)
        r_h.bold = True
        r_h.font.name = "Times New Roman"
        r_h.font.size = Pt(9.5)
        r_h.font.color.rgb = NAVY
        set_cell_bg(c_hdr, "F1F5F9")

        c_body = tbl_sign.rows[1].cells[col_idx]
        p_b = c_body.paragraphs[0]
        p_b.alignment = WD_ALIGN_PARAGRAPH.CENTER

        if col_idx == 2 and os.path.exists(seal_path):
            p_b.add_run().add_picture(seal_path, width=Inches(1.2))
        else:
            p_b.add_run("\n\n(Đã ký điện tử)\n\n")

        p_p = c_body.add_paragraph()
        p_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_p = p_p.add_run(person)
        r_p.bold = True
        r_p.font.name = "Times New Roman"
        r_p.font.size = Pt(9)
        r_p.font.color.rgb = NAVY

    for row in tbl_sign.rows:
        for cell in row.cells:
            cell.width = Inches(2.4)
            set_cell_border(cell, color="CBD5E1", sz="4")

    doc.save(DOCX_OUT)
    print(f"Created Word Document: {DOCX_OUT}")

def create_poster_png():
    W, H = 2480, 3508
    img = Image.new('RGB', (W, H), 'white')
    draw = ImageDraw.Draw(img)

    def get_font(size, bold=False):
        font_names = ["timesbd.ttf" if bold else "times.ttf", "arialbd.ttf" if bold else "arial.ttf", "segoeuib.ttf" if bold else "segoeui.ttf"]
        for fn in font_names:
            try:
                return ImageFont.truetype(fn, size)
            except Exception:
                continue
        return ImageFont.load_default()

    # Header Banner
    draw.rectangle([0, 0, W, 400], fill='#071A36')
    draw.rectangle([0, 400, W, 415], fill='#D4441E')

    logo_path = os.path.join(ASSETS_DIR, "Cargolink_Logo_Vector_HighRes.png")
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert('RGBA')
        logo.thumbnail((450, 140), Image.Resampling.LANCZOS)
        img.paste(logo, (80, 80), logo)

    draw.text((560, 75), "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM", font=get_font(34, bold=True), fill='#FFFFFF')
    draw.text((560, 130), "HỆ THỐNG AN NINH CHUỖI CUNG ỨNG C-TPAT & QUẢN LÝ VẬN TẢI ISO 9001 / ISO 39001", font=get_font(24, bold=False), fill='#CBD5E1')
    draw.text((560, 180), "TRỤ SỞ: LẦU 6, SỐ 84 BẠCH ĐẰNG, P. TÂN SƠN HÒA, TP. HỒ CHÍ MINH | MST: 0313492159", font=get_font(20, bold=False), fill='#94A3B8')

    # Poster Title
    draw.rectangle([80, 440, W - 80, 560], fill='#F1F5F9', outline='#CBD5E1', width=3)
    draw.text((W//2, 465), "BẢNG MÃ QR CÁC CÔNG CỤ VẬN HÀNH SỐ HÓA & BIỂU MẪU ĐIỆN TỬ C-TPAT", font=get_font(38, bold=True), fill='#071A36', anchor='mt')
    draw.text((W//2, 520), "100% Paperless — Quét mã QR bằng điện thoại di động để kê khai, kiểm tra và ký số trực tuyến", font=get_font(22, bold=False), fill='#64748B', anchor='mt')

    # Grid of 10 tools (5 rows x 2 cols)
    tools = [
        ("1. KIỂM TRA XE 7/17 ĐIỂM", "qr_app1_inspection.png", "Checklist kiểm tra 7 điểm xe tải & 17 điểm rơ-moóc trước chuyến đi theo chuẩn WI-SEC-001 có ký số.", "#071A36"),
        ("2. KIỂM TRA SEAL VVTT & CẮT SEAL", "qr_app2_seal.png", "Kiểm tra 4 bước View - Verify - Tug - Twist chuẩn C-TPAT đối với Seal High Security ISO 17712.", "#D4441E"),
        ("3. SỔ KIỂM TRA CỒN 0.00 & MA TÚY", "qr_app3_alcohol.png", "Kiểm soát trước chuyến đi: Nồng độ cồn hơi thở cam kết 0.00 mg/L và test 5 nhóm chất ma túy âm tính.", "#059669"),
        ("4. BÁO CÁO SỰ CỐ 15 PHÚT KHẨN CẤP", "qr_app4_incident.png", "Kích hoạt trong 15 phút khi chậm ETA >15p, hỏng xe, sự cố seal, nghi vấn cạy phá. Định vị GPS tự động.", "#DC2626"),
        ("5. LỆNH ĐIỀU XE ĐIỆN TỬ TUYẾN NV", "qr_app5_dispatch.png", "Lệnh điều xe điện tử CGL-DSP, giám sát lộ trình Nhà máy NV - Cảng Cát Lái/Tân Sơn Nhất, trạm dừng Petrolimex.", "#0B3C5D"),
        ("6. KIỂM TRA PCCC & TRANG BỊ PPE", "qr_app6_ppe.png", "Kiểm tra bình chữa cháy MFZ4 cabin/thùng xe, tam giác phản quang, túi sơ cứu và trang bị bảo hộ lái xe.", "#D97706"),
        ("7. NHẬT KÝ KIỂM SOÁT CỔNG BÃI XE", "qr_app7_visitor.png", "Đăng ký thông tin khách, nhà thầu, cấp phát thẻ khách C-TPAT, ghi nhận giờ vào/ra bảo vệ cổng an ninh.", "#475569"),
        ("8. SỔ NĂNG LƯỢNG & VĂN PHÒNG XANH", "qr_app8_green.png", "Theo dõi điện, nước, giấy in A4, rác thải tái chế và định mức dầu xe chuẩn môi trường ISO 14001.", "#166534"),
        ("9. ĐÁNH GIÁ NHÀ XE PHỤ THẦU PHỤ", "qr_app9_subcontractor.png", "Bộ tiêu chí 100 điểm thẩm định nhà thầu phụ vận tải: GPKD, bảo hiểm, 100% xe GPS, lý lịch tư pháp lái xe.", "#4338CA"),
        ("10. CHECKLIST TỰ KIỂM TOÁN C-TPAT", "qr_app10_audit.png", "Đối chiếu toàn diện 12 tiêu chuẩn Hải quan Hoa Kỳ, chấm điểm tự động mức độ sẵn sàng tiếp đoàn NV Apparel.", "#1D4ED8"),
    ]

    start_y = 590
    card_h = 470
    card_w = (W - 80*2 - 40) // 2  # 2 cols

    for idx, (title, qr_file, desc, color_code) in enumerate(tools):
        col = idx % 2
        row = idx // 2
        x = 80 + col * (card_w + 40)
        y = start_y + row * (card_h + 20)

        # Draw card container
        draw.rectangle([x, y, x + card_w, y + card_h], fill='#FFFFFF', outline='#CBD5E1', width=3)
        draw.rectangle([x, y, x + card_w, y + 60], fill=color_code)
        draw.text((x + card_w // 2, y + 16), title, font=get_font(24, bold=True), fill='#FFFFFF', anchor='mt')

        # Paste QR
        qr_p = os.path.join(FORMS_DIR, qr_file)
        if os.path.exists(qr_p):
            qr_img = Image.open(qr_p).convert('RGBA')
            qr_img.thumbnail((320, 320), Image.Resampling.LANCZOS)
            img.paste(qr_img, (x + 30, y + 90), qr_img)

        # Draw text on right of card
        text_x = x + 380
        text_w = card_w - 410

        draw.text((text_x, y + 110), "QUY CHUẨN C-TPAT & ISO", font=get_font(18, bold=True), fill=color_code)
        
        # Word wrap desc
        words = desc.split()
        lines = []
        cur_line = ""
        for w in words:
            test = cur_line + (" " if cur_line else "") + w
            if len(test) < 28:
                cur_line = test
            else:
                lines.append(cur_line)
                cur_line = w
        if cur_line:
            lines.append(cur_line)

        for l_idx, l in enumerate(lines[:5]):
            draw.text((text_x, y + 155 + l_idx * 38), l, font=get_font(21, bold=False), fill='#334155')

        draw.rectangle([text_x, y + 360, x + card_w - 30, y + 420], fill='#F1F5F9', outline='#CBD5E1', width=2)
        draw.text((text_x + 15, y + 375), "📱 Quét mã để thao tác ngay ➔", font=get_font(20, bold=True), fill='#071A36')

    # Footer
    draw.rectangle([0, H - 260, W, H], fill='#071A36')
    draw.rectangle([0, H - 260, W, H - 250], fill='#D4441E')

    draw.text((W//2, H - 220), "TRUNG TÂM TIẾP NHẬN & ĐIỀU HÀNH VẬN TẢI CARGOLINK EXPRESS 24/7", font=get_font(26, bold=True), fill='#FFFFFF', anchor='mt')
    draw.text((W//2, H - 175), "Hotline Điều độ: 077 871 9936 (Ms. Bích) | Hotline An toàn: 088 6464 988 (Mr. Thành) | Khẩn cấp 24/7: 0943 46 46 46", font=get_font(23, bold=False), fill='#CBD5E1', anchor='mt')
    draw.text((W//2, H - 130), "Truy cập trực tuyến 24/7: https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/portal_driver.html", font=get_font(21, bold=True), fill='#FED7AA', anchor='mt')

    # Save outputs
    img.save(PNG_OUT_TARGET, format='PNG')
    img.save(POSTER_PNG_OUT, format='PNG')
    brain_poster = os.path.join(BRAIN_DIR, "HS16-02_POSTER_MA_QR_10_CONG_CU_VAN_HANH_SO_HOA_C_TPAT.png")
    img.save(brain_poster, format='PNG')
    print(f"Created Poster PNG in Target Dir: {PNG_OUT_TARGET}")
    print(f"Created Poster PNG in Assets Dir: {POSTER_PNG_OUT}")
    print(f"Copied Poster PNG to Brain Dir: {brain_poster}")

create_docx()
create_poster_png()
