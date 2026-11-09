# -*- coding: utf-8 -*-
import os, sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
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

def create_cap_docx():
    doc = Document()
    
    # Page setup
    section = doc.sections[0]
    section.top_margin = Inches(0.6)
    section.bottom_margin = Inches(0.6)
    section.left_margin = Inches(0.7)
    section.right_margin = Inches(0.7)
    
    # Header & Footer
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("CARGOLINK EXPRESS VIETNAM | C-TPAT AUDIT CORRECTIVE ACTION PLAN (CAP) 2026")
    hrun.font.size = Pt(8.5)
    hrun.font.color.rgb = GRAY
    
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    frun = fp.add_run("Báo cáo kế hoạch hành động khắc phục sau đánh giá C-TPAT NV Apparel 2026 | Deadline: 23/11/2026 | Bản chính thức lưu trữ nội bộ và nộp khách hàng")
    frun.font.size = Pt(8)
    frun.font.color.rgb = GRAY
    
    # Title Block
    p_comp = doc.add_paragraph()
    r_comp = p_comp.add_run("CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM\n")
    r_comp.bold = True
    r_comp.font.size = Pt(11)
    r_comp.font.color.rgb = NAVY
    r_sub = p_comp.add_run("Trụ sở: Lầu 6, Số 84 Bạch Đằng, P. Tân Sơn Hòa, Q. Tân Bình, TP.HCM | MST: 0313492159\nHotline Điều độ: 077 871 9936 | Hotline An toàn: 088 6464 988 | Khẩn cấp 24/7: 0943 46 46 46")
    r_sub.font.size = Pt(8.5)
    r_sub.font.color.rgb = GRAY
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(14)
    p_title.paragraph_format.space_after = Pt(4)
    r_t = p_title.add_run("BÁO CÁO KẾ HOẠCH HÀNH ĐỘNG KHẮC PHỤC TOÀN DIỆN\nSAU ĐÁNH GIÁ AN NINH C-TPAT THƯỜNG NIÊN NĂM 2026")
    r_t.bold = True
    r_t.font.size = Pt(14)
    r_t.font.color.rgb = ACCENT
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(14)
    r_s = p_sub.add_run("Kính gửi: BAN CHUYÊN GIA ĐÁNH GIÁ C-TPAT - CÔNG TY TNHH NV APPAREL (TẬP ĐOÀN NICE GROUP)\nCăn cứ biên bản đánh giá thực tế ngày 04/11/2026 - Thời hạn hoàn thành: 23/11/2026")
    r_s.italic = True
    r_s.font.size = Pt(9.5)
    r_s.font.color.rgb = GRAY
    
    # Section I
    p = doc.add_paragraph()
    r = p.add_run("I. TỔNG QUAN VÀ CAM KẾT CỦA BAN LÃNH ĐẠO CARGOLINK EXPRESS:")
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "Công ty TNHH Cargolink Express Việt Nam trân trọng gửi lời cảm ơn sâu sắc tới Ban đánh giá an ninh C-TPAT của Công ty TNHH NV Apparel (Tập đoàn Nice Group) đã tiến hành đợt đánh giá thường niên ngày 04/11/2026 tại văn phòng và hệ thống phương tiện bãi xe của Cargolink.\n\n"
        "Ngay sau khi tiếp nhận bảng tổng hợp kiến nghị (Slide Finding & Sheet 14) từ đại diện khách hàng, Ban Giám Đốc Cargolink đã triệu tập cuộc họp khẩn cấp, thành lập Ban Đặc trách Khắc phục C-TPAT 2026 do Giám đốc Nguyễn Tất Thắng trực tiếp chỉ đạo, phối hợp chặt chẽ cùng Trưởng ban An toàn Phan Công Thành, Kế toán trưởng Lê Thị Tú và Trưởng phòng Điều độ Bùi Thị Ngọc Bích.\n\n"
        "Cargolink cam kết tuân thủ 100% 5 yêu cầu cốt lõi của khách hàng:\n"
        "1. Hoàn thành toàn diện Sheet 14 (An toàn cơ sở & công việc), phân tách rõ các hạng mục hóa chất / nhà máy màu đỏ được miễn trừ và đạt điểm tuyệt đối 100% đối với các tiêu chí thuộc phạm vi nhà vận tải.\n"
        "2. Khắc phục triệt để 31 Finding trong Slide Finding, ban hành đầy đủ chính sách và đưa vào thực tế vận hành.\n"
        "3. Chuẩn bị đầy đủ hình ảnh, bằng chứng vật lý, thiết bị, nhãn dán cabin và hệ thống biển báo song ngữ Anh - Thái.\n"
        "4. 100% chính sách được văn bản hóa chuẩn ISO, có chữ ký của người có thẩm quyền và đóng dấu pháp nhân công ty.\n"
        "5. Hoàn tất toàn bộ hồ sơ trước thời hạn quy định 23/11/2026 (Hoàn thành sớm ngày 06/11/2026)."
    )
    
    # Section II: 31 Findings Matrix
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    r = p.add_run("II. BẢNG TỔNG HỢP BIỆN PHÁP KHẮC PHỤC CHI TIẾT 31 SLIDE FINDING (CAP MATRIX):")
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = NAVY
    
    # Table of 31 findings
    # Read findings from completed excel to ensure exact match
    comp_xlsx = os.path.join(BASE_DIR, "Bảng câu hỏi & Đối chiếu đánh giá", "Finding_for_CGL_comment_Ver._Final_COMPLETED.xlsx")
    wb_temp = openpyxl.load_workbook(comp_xlsx, data_only=True)
    ws_temp = wb_temp['Slide Finding']
    
    table = doc.add_table(rows=1, cols=6)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    headers = ["No.", "Hạng mục đánh giá & Finding", "Hành động khắc phục của CGL", "Chứng từ / Hồ sơ chứng minh", "Ảnh chụp / Bằng chứng thực tế", "Tình trạng & Hạn"]
    widths = [Inches(0.4), Inches(1.5), Inches(2.2), Inches(1.4), Inches(1.5), Inches(0.9)]
    
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.width = widths[i]
        set_cell_bg(cell, "071A36")
        set_cell_border(cell)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(8)
        r.font.color.rgb = RGBColor(255, 255, 255)
        
    for r_idx in range(4, ws_temp.max_row+1):
        num = ws_temp.cell(r_idx, 1).value
        sec = str(ws_temp.cell(r_idx, 3).value or '')
        item = str(ws_temp.cell(r_idx, 4).value or '')
        finding = str(ws_temp.cell(r_idx, 5).value or '')
        ca = str(ws_temp.cell(r_idx, 6).value or '')
        ev = str(ws_temp.cell(r_idx, 7).value or '')
        st = str(ws_temp.cell(r_idx, 8).value or '')
        
        row_cells = table.add_row().cells
        
        # Col 0: No
        row_cells[0].width = widths[0]
        set_cell_border(row_cells[0])
        p0 = row_cells[0].paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(str(num))
        r0.bold = True
        r0.font.size = Pt(8)
        
        # Col 1: Section & Finding
        row_cells[1].width = widths[1]
        set_cell_border(row_cells[1])
        p1 = row_cells[1].paragraphs[0]
        r1_s = p1.add_run(f"[{sec}]\n")
        r1_s.bold = True
        r1_s.font.size = Pt(7.5)
        r1_s.font.color.rgb = NAVY
        r1_f = p1.add_run(finding)
        r1_f.font.size = Pt(7.5)
        
        # Col 2: CA
        row_cells[2].width = widths[2]
        set_cell_border(row_cells[2])
        p2 = row_cells[2].paragraphs[0]
        r2 = p2.add_run(ca)
        r2.font.size = Pt(7.5)
        
        # Col 3: Doc code
        doc_ref = "Hồ sơ CGL ban hành"
        for code in ["HS01-02", "HS01-05", "HS02-05", "HS03-07", "HS03-08", "HS07-04", "HS08-04", "HS09-06", "HS10-04", "HS12-04", "HS14-08", "HS15-06", "HS15-07", "HS16-04", "HS17-09", "HS18-06", "HS20-06", "HS21-03"]:
            if code in ev:
                doc_ref = code
                break
        if num in [25, 27, 30]: doc_ref = "N/A (Khách hàng xác nhận)"
        
        row_cells[3].width = widths[3]
        set_cell_border(row_cells[3])
        p3 = row_cells[3].paragraphs[0]
        r3 = p3.add_run(doc_ref)
        r3.bold = True
        r3.font.size = Pt(8)
        r3.font.color.rgb = ACCENT
        
        # Col 4: Evidence & Photo
        row_cells[4].width = widths[4]
        set_cell_border(row_cells[4])
        p4 = row_cells[4].paragraphs[0]
        r4 = p4.add_run(ev[:250] + ("..." if len(ev) > 250 else ""))
        r4.font.size = Pt(7.5)
        
        # Col 5: Status
        row_cells[5].width = widths[5]
        set_cell_border(row_cells[5])
        p5 = row_cells[5].paragraphs[0]
        p5.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r5 = p5.add_run(st)
        r5.bold = True
        r5.font.size = Pt(7.5)
        if "Hoàn thành" in st:
            r5.font.color.rgb = RGBColor(21, 128, 61)
            set_cell_bg(row_cells[5], "DCFCE7")
            
    # Section III: Sheet 14 Breakdown
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    r = p.add_run("III. BÁO CÁO KẾT QUẢ KHẮC PHỤC SHEET 14 (AN TOÀN CƠ SỞ & CÔNG VIỆC):")
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "1. Danh mục 9 hạng mục màu đỏ được MIỄN TRỪ (Không thuộc phạm vi áp dụng của CGL):\n"
        "   • Hóa chất (14.21, 14.22, 14.23, 14.24, 14.25, 14.26): Cargolink là nhà vận chuyển trang phục may mặc thành phẩm đóng container kín, hoàn toàn không lưu trữ, chiết rót hay sử dụng hóa chất công nghiệp độc hại.\n"
        "   • Ủy ban & Cán bộ chuyên trách nhà máy (14.46, 14.47, 14.48): Là yêu cầu đối với cơ sở sản xuất có ủy ban NBTC, không áp dụng cho đơn vị vận tải dịch vụ.\n\n"
        "2. Danh mục 47 hạng mục áp dụng thực tế (ĐẠT ĐIỂM TUYỆT ĐỐI 100%):\n"
        "   • Lối thoát hiểm (14.1 - 14.10): Lắp đặt hệ thống biển EXIT song ngữ Anh - Thái (EXIT / ทางออก), đèn sự cố tự phát sáng 2 giờ và dán sơ đồ thoát hiểm tại tất cả các cửa ra vào.\n"
        "   • Điểm tập kết sơ tán (14.11, 14.50): Quy hoạch và cắm biển ASSEMBLY POINT / จุดรวมพล tại sân trước bãi xe Bình Tân rộng 2.500m².\n"
        "   • Phòng chống hút thuốc (14.12): Niêm yết biển NO SMOKING / ห้ามสูบบุหรี่ trên 100% phương tiện và văn phòng; bố trí khu vực hút thuốc cách xa bãi xe 15m.\n"
        "   • Phòng cháy chữa cháy (14.13 - 14.15, 14.51): Bố trí bình chữa cháy bột ABC 8kg và CO2 5kg với bán kính bảo vệ < 22.5m, kiểm định PCCC định kỳ 2026.\n"
        "   • Sơ cấp cứu & Phúc lợi (14.16 - 14.20, 14.38 - 14.45): Trang bị tủ thuốc sơ cứu gắn tường không khóa, nước sạch, nhà vệ sinh nam nữ riêng biệt có vách kín từ sàn đến trần và thùng rác nắp đậy."
    )
    
    # Section IV: Physical Evidence & Digital Portal
    p = doc.add_paragraph()
    r = p.add_run("IV. HỆ THỐNG CÔNG CỤ SỐ HÓA & BIỂN BÁO TRỰC QUAN ĐÃ TRIỂN KHAI THỰC TẾ:")
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "• Hệ thống biển báo an toàn song ngữ Anh - Thái: Đã sản xuất và lắp đặt hoàn thiện tại cơ sở bãi xe và văn phòng (HS14-08_EXIT_SIGN, HS14-08_ASSEMBLY_POINT, HS14-08_NO_SMOKING).\n"
        "• Nhãn dán Hotline khẩn cấp: In Decal PVC phản quang dán trên kính chắn gió và taplo 100% đầu kéo (HS18-06_EMERGENCY_HOTLINE_STICKER).\n"
        "• Decal 3 mã QR chuyên biệt cho tài xế: Dán trong cabin xe để quét Đào tạo C-TPAT, Góp ý khiếu nại bảo mật và Sổ tay kiểm tra xe 17 điểm (HS21-03_DECAL_3_QR_CODE).\n"
        "• Nâng cấp hệ thống CCTV bãi xe: Trang bị 2 ổ cứng Seagate SkyHawk AI 16TB, đảm bảo lưu trữ liên tục 180 ngày (6 tháng) cho toàn bộ 14 mắt camera giám sát.\n"
        "• Cổng tra cứu số C-TPAT Compliance: Hoạt động trực tuyến 24/7/365 trên nền tảng GitHub Pages & Cloudflare tunnel, tích hợp C-TPAT Access Tracker ghi nhận nhật ký đọc chính sách của người lao động."
    )
    
    # Sign block
    p_loc = doc.add_paragraph()
    p_loc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_loc.paragraph_format.space_before = Pt(16)
    p_loc.paragraph_format.space_after = Pt(4)
    r_loc = p_loc.add_run("TP. Hồ Chí Minh, ngày 06 tháng 11 năm 2026")
    r_loc.italic = True
    r_loc.font.size = Pt(9.5)

    table_sign = doc.add_table(rows=2, cols=3)
    table_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_sign.autofit = False
    
    widths_s = [Inches(2.2), Inches(2.2), Inches(2.6)]
    roles = ["NGƯỜI LẬP BÁO CÁO\n(Tài xế / Trưởng đội xe)", "NGƯỜI KIỂM SOÁT\n(Trưởng ban An toàn C-TPAT)", "ĐẠI DIỆN PHÁP LUẬT CÔNG TY\n(Giám đốc điều hành - Phê duyệt & Đóng dấu)"]
    
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
            r2 = p_sig.add_run("Bùi Minh Dũng\n(Đội trưởng Lái xe)")
            r2.font.size = Pt(9.5)
        elif i == 1:
            p_sig.paragraph_format.space_before = Pt(36)
            r2 = p_sig.add_run("Phan Công Thành\n(Trưởng ban An toàn)")
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
            
    out_docx = os.path.join(BASE_DIR, "00_KE_HOACH_KHAC_PHUC_AUDIT_CTPAT_04_11_2026.docx")
    doc.save(out_docx)
    doc.save(os.path.join(ARTIFACT_DIR, "00_KE_HOACH_KHAC_PHUC_AUDIT_CTPAT_04_11_2026.docx"))
    print(f"[Master CAP DOCX] Saved: {out_docx}")

def create_cap_xlsx():
    comp_xlsx = os.path.join(BASE_DIR, "Bảng câu hỏi & Đối chiếu đánh giá", "Finding_for_CGL_comment_Ver._Final_COMPLETED.xlsx")
    wb_temp = openpyxl.load_workbook(comp_xlsx)
    
    out_xlsx = os.path.join(BASE_DIR, "00_KE_HOACH_KHAC_PHUC_AUDIT_CTPAT_04_11_2026.xlsx")
    wb_temp.save(out_xlsx)
    wb_temp.save(os.path.join(ARTIFACT_DIR, "00_KE_HOACH_KHAC_PHUC_AUDIT_CTPAT_04_11_2026.xlsx"))
    print(f"[Master CAP XLSX] Saved: {out_xlsx}")

if __name__ == "__main__":
    create_cap_docx()
    create_cap_xlsx()
