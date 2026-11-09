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
ARTIFACT_DIR = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163"

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

def create_next_steps_docx():
    doc = Document()
    
    section = doc.sections[0]
    section.top_margin = Inches(0.6)
    section.bottom_margin = Inches(0.6)
    section.left_margin = Inches(0.7)
    section.right_margin = Inches(0.7)
    
    # Header & Footer
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("CARGOLINK EXPRESS | KẾ HOẠCH HÀNH ĐỘNG TRIỂN KHAI THỰC TẾ AUDIT TRUCK 2026")
    hrun.font.size = Pt(8.5)
    hrun.font.color.rgb = GRAY
    
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    frun = fp.add_run("Kế hoạch hành động 5 giai đoạn triển khai khắc phục C-TPAT NV Apparel | Hạn chót: 23/11/2026")
    frun.font.size = Pt(8)
    frun.font.color.rgb = GRAY
    
    # Title
    p_comp = doc.add_paragraph()
    r_comp = p_comp.add_run("CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM\n")
    r_comp.bold = True
    r_comp.font.size = Pt(11)
    r_comp.font.color.rgb = NAVY
    r_sub = p_comp.add_run("BAN ĐẶC TRÁCH QUẢN LÝ AN NINH C-TPAT & TRÁCH NHIỆM XÃ HỘI ISO")
    r_sub.font.size = Pt(8.5)
    r_sub.font.color.rgb = GRAY
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(4)
    r_t = p_title.add_run("KẾ HOẠCH HÀNH ĐỘNG TRIỂN KHAI THỰC TẾ CHI TIẾT TỪNG BƯỚC\nHOÀN TẤT KIỂM TOÁN C-TPAT & BÀN GIAO CHO KHÁCH HÀNG NV APPAREL")
    r_t.bold = True
    r_t.font.size = Pt(13)
    r_t.font.color.rgb = ACCENT
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(12)
    r_s = p_sub.add_run("Thời gian áp dụng: Từ ngày 09/11/2026 đến ngày 23/11/2026\nPhân công trách nhiệm cụ thể: Ban Giám đốc, Điều độ, An toàn, Đội xe và Kế toán")
    r_s.italic = True
    r_s.font.size = Pt(9.5)
    r_s.font.color.rgb = GRAY
    
    # Roadmap Steps
    steps = [
        ("GIAI ĐOẠN 1: GỬI HỒ SƠ CAP PHẢN HỒI CHÍNH THỨC CHO NV APPAREL (NGÀY 09/11 - 10/11/2026)",
         "Mục tiêu: Báo cáo bằng văn bản chính thức cho Ban đánh giá NV Apparel (Ms. Yui Sudarat) về việc Cargolink đã hoàn thành 100% các nội dung khắc phục.\n\n"
         "Các file gửi kèm email:\n"
         "1. Finding_for_CGL_comment_Ver._Final_COMPLETED.xlsx (File Excel đối chiếu 31 Slide Finding & Sheet 14 đạt chuẩn).\n"
         "2. 00_KE_HOACH_KHAC_PHUC_AUDIT_CTPAT_04_11_2026.docx (Bản Word chính thức có ký duyệt & đóng dấu đỏ GĐ Thắng).\n"
         "3. 00_BO_ANH_BANG_CHUNG_MAU_AUDIT_CTPAT_2026.docx (Báo cáo album 20 hình ảnh bằng chứng mẫu đạt chuẩn).\n"
         "4. Đường link tra cứu trực tuyến: https://thangcargolink.github.io/cargolink-ctpat-portal/album_anh_bang_chung_ctpat.html\n\n"
         "Người phụ trách: Ban Giám đốc (Mr. Thắng) & Bộ phận Điều độ (Ms. Bích)."),
        
        ("GIAI ĐOẠN 2: IN ẤN VẬT TƯ & THI CÔNG HIỆN TRƯỜNG BÃI XE, XE TẢI (NGÀY 11/11 - 13/11/2026)",
         "Mục tiêu: Đưa toàn bộ các quy định và bằng chứng trực quan vào hiện trường thực tế.\n\n"
         "Hành động cụ thể:\n"
         "• In ấn Decal (Gửi xưởng in quảng cáo): In 30 bộ nhãn Hotline khẩn cấp phản quang (15x25cm), 30 bộ decal 3 mã QR dán cabin (12x25cm), 30 tem Cấm hút thuốc (20x30cm).\n"
         "• In ấn Biển kim loại: Biển Lối thoát hiểm dạ quang (15x35cm), Biển Điểm tập kết sơ tán PCCC song ngữ Anh - Thái (40x60cm), Standee 3-in-1 chân sắt (60x160cm).\n"
         "• Thi công trên xe tải: Dán nhãn Hotline góc phải kính chắn gió; dán decal 3 QR code mặt trong cánh cửa cabin của 15 đầu kéo.\n"
         "• Thi công tại bãi xe: Cắm biển Điểm tập kết sơ tán tại sân trước; thiết lập khu hút thuốc cách xe 15m có xô cát và bình CO2; kiểm tra đầu ghi NVR camera lưu trữ 180 ngày.\n\n"
         "Người phụ trách: Cán bộ An toàn (Mr. Thành) & Đội trưởng Lái xe (Mr. Dũng)."),
        
        ("GIAI ĐOẠN 3: ĐÓNG CẶP FILE VẬT LÝ VÀ CHUẨN HÓA HỒ SƠ GIẤY (NGÀY 14/11 - 16/11/2026)",
         "Mục tiêu: Hoàn thiện hệ thống lưu trữ tại văn phòng Lầu 6 và Trạm gác bãi xe để sẵn sàng xuất trình khi chuyên gia kiểm tra thực địa.\n\n"
         "Các cặp file cần hoàn thiện:\n"
         "• Cặp HS01: ĐKKD, Giấy phép vận tải ô tô, Hợp đồng NV Apparel, Kế hoạch kinh doanh 2026-2028.\n"
         "• Cặp HS02 & HS03: Tủ sắt khóa bảo mật, Sổ bàn giao hồ sơ, Phiếu lý lịch tư pháp 7 tài xế, Quy định đo cồn ma túy.\n"
         "• Cặp HS09 & HS10: Danh sách đào tạo C-TPAT có chữ ký, Bài kiểm tra, Sao kê ngân hàng Vietcombank chi trả lương.\n"
         "• Dãy cặp còng HS15: Nhãn gáy CGL-CTPAT-VEHICLE-INSP-2026 phân chia từng biển số xe chứa biên bản kiểm tra 17 điểm.\n"
         "• Cặp HS16: Mẫu Job Sheet kiêm Lệnh vận chuyển có mã chạy duy nhất JOB-CGL-2026-XXXXX liên kết C-TPAT.\n\n"
         "Người phụ trách: Giám đốc (Mr. Thắng), Kế toán trưởng (Ms. Tú) & Trưởng phòng Điều độ (Ms. Bích)."),
        
        ("GIAI ĐOẠN 4: TẬP HUẤN ĐỘI NGŨ LÁI XE & QUẢN TRỊ VẬN HÀNH (NGÀY 17/11 - 19/11/2026)",
         "Mục tiêu: Đảm bảo 100% lái xe và điều độ viên nắm vững quy trình và biết cách trả lời phỏng vấn chuyên nghiệp.\n\n"
         "Nội dung tập huấn (Họp 30 phút tại bãi xe hoặc văn phòng):\n"
         "• Hướng dẫn tài xế nhận Job Sheet, ký xác nhận niêm phong chì seal VVTT và kiểm tra xe 17 điểm trước khi rời bãi.\n"
         "• Hướng dẫn tài xế dùng điện thoại quét mã QR dán trong cabin (thực hành làm khảo sát C-TPAT, gửi khiếu nại bảo mật).\n"
         "• Quán triệt chính sách không cồn (0.0 mg/L) và tuân thủ đúng tim đường lộ trình C-TPAT đã phê duyệt.\n"
         "• Kịch bản trả lời phỏng vấn: Hướng dẫn tài xế trả lời lưu loát về quy trình kiểm tra xe, cách xử lý khi kẹt xe/hỏng hóc.\n\n"
         "Người phụ trách: Trưởng ban An toàn (Mr. Thành) & Đội trưởng Lái xe (Mr. Dũng)."),
        
        ("GIAI ĐOẠN 5: TỔNG DUYỆT NỘI BỘ (MOCK AUDIT) & ĐÓN NHẬN NGHIỆM THU (NGÀY 20/11 - 22/11/2026)",
         "Mục tiêu: Đảm bảo không còn bất kỳ khoảng trống hay sai sót nào trước thời hạn chót 23/11/2026.\n\n"
         "Hành động kiểm tra:\n"
         "• Chạy thử ứng dụng Kiểm toán nội bộ (app_ctpat_audit_checklist.html) rà soát lại toàn bộ 100 tiêu chí đánh giá.\n"
         "• Phúc tra ngẫu nhiên 3 xe tải: Kiểm tra độ bám dính của tem decal, nhãn hotline và biên bản kiểm tra xe trên cabin.\n"
         "• Kiểm tra trạm gác bãi xe: Sổ đo nồng độ cồn, máy đo cồn, tủ sơ cứu, bình chữa cháy kiểm định.\n"
         "• Sẵn sàng đón đoàn chuyên gia NV Apparel phúc tra hiện trường hoặc hoàn tất phê duyệt báo cáo trực tuyến.\n\n"
         "Người phụ trách: Giám đốc Nguyễn Tất Thắng trực tiếp tổng duyệt.")
    ]
    
    for title, content in steps:
        p_step = doc.add_paragraph()
        p_step.paragraph_format.space_before = Pt(12)
        p_step.paragraph_format.space_after = Pt(4)
        r = p_step.add_run(title)
        r.bold = True
        r.font.size = Pt(10.5)
        r.font.color.rgb = NAVY
        
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        cell = table.cell(0, 0)
        cell.width = Inches(6.8)
        set_cell_border(cell)
        set_cell_bg(cell, "F8FAFC")
        
        p = cell.paragraphs[0]
        r_c = p.add_run(content)
        r_c.font.size = Pt(8.5)
        
    # Sign block
    p_loc = doc.add_paragraph()
    p_loc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_loc.paragraph_format.space_before = Pt(16)
    p_loc.paragraph_format.space_after = Pt(4)
    r_loc = p_loc.add_run("TP. Hồ Chí Minh, ngày 09 tháng 11 năm 2026")
    r_loc.italic = True
    r_loc.font.size = Pt(9.5)

    table_sign = doc.add_table(rows=2, cols=3)
    table_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_sign.autofit = False
    
    widths_s = [Inches(2.2), Inches(2.2), Inches(2.6)]
    roles = ["NGƯỜI LẬP KẾ HOẠCH\n(Trưởng ban An toàn C-TPAT)", "ĐIỀU PHỐI VẬN HÀNH\n(Trưởng phòng Điều độ)", "GIÁM ĐỐC ĐIỀU HÀNH\n(Phê duyệt thực hiện & Đóng dấu)"]
    
    for i in range(3):
        cell = table_sign.cell(0, i)
        cell.width = widths_s[i]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(roles[i])
        r.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = NAVY
        set_cell_border(cell, top="none", bottom="none", left="none", right="none")
        
        cell_sig = table_sign.cell(1, i)
        cell_sig.width = widths_s[i]
        p_sig = cell_sig.paragraphs[0]
        p_sig.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_cell_border(cell_sig, top="none", bottom="none", left="none", right="none")
        
        if i == 0:
            p_sig.paragraph_format.space_before = Pt(36)
            r2 = p_sig.add_run("Phan Công Thành\n(Trưởng ban An toàn)")
            r2.font.size = Pt(9.5)
        elif i == 1:
            p_sig.paragraph_format.space_before = Pt(36)
            r2 = p_sig.add_run("Bùi Thị Ngọc Bích\n(Trưởng phòng Điều độ)")
            r2.font.size = Pt(9.5)
        elif i == 2:
            p_sig.paragraph_format.space_before = Pt(4)
            if os.path.exists(SEAL_IMG):
                r_img = p_sig.add_run()
                r_img.add_picture(SEAL_IMG, width=Inches(1.8))
            p_name = cell_sig.add_paragraph()
            p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_name = p_name.add_run("NGUYỄN TẤT THẮNG\nGiám đốc")
            r_name.bold = True
            r_name.font.size = Pt(9.5)
            
    out_docx = os.path.join(BASE_DIR, "00_KE_HOACH_HANH_DONG_TIEP_THEO_AUDIT_2026.docx")
    doc.save(out_docx)
    doc.save(os.path.join(ARTIFACT_DIR, "00_KE_HOACH_HANH_DONG_TIEP_THEO_AUDIT_2026.docx"))
    print(f"[Next Steps DOCX] Saved: {out_docx}")

if __name__ == "__main__":
    create_next_steps_docx()
