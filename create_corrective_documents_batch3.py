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

def add_header_footer(doc, doc_code, doc_title):
    section = doc.sections[0]
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)
    
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run(f"CGL EXPRESS | C-TPAT AUDIT 2026 - CAP | Mã số: {doc_code}")
    hrun.font.size = Pt(8.5)
    hrun.font.color.rgb = GRAY
    
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    frun = fp.add_run(f"Tài liệu khắc phục sau đánh giá C-TPAT NV Apparel 2026 - {doc_title} | Bảo mật nội bộ")
    frun.font.size = Pt(8)
    frun.font.color.rgb = GRAY

def add_title_block(doc, doc_code, doc_title, subtitle=""):
    p_comp = doc.add_paragraph()
    r_comp = p_comp.add_run("CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM\n")
    r_comp.bold = True
    r_comp.font.size = Pt(10)
    r_comp.font.color.rgb = NAVY
    r_sub = p_comp.add_run("HỆ THỐNG QUẢN LÝ AN NINH CHUỖI CUNG ỨNG C-TPAT & TRÁCH NHIỆM XÃ HỘI ISO")
    r_sub.font.size = Pt(8.5)
    r_sub.font.color.rgb = GRAY
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(4)
    r_t = p_title.add_run(doc_title.upper())
    r_t.bold = True
    r_t.font.size = Pt(13)
    r_t.font.color.rgb = ACCENT
    
    if subtitle:
        p_sub = doc.add_paragraph()
        p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_sub.paragraph_format.space_after = Pt(12)
        r_s = p_sub.add_run(subtitle)
        r_s.italic = True
        r_s.font.size = Pt(9.5)
        r_s.font.color.rgb = GRAY

def add_sign_block(doc):
    p_loc = doc.add_paragraph()
    p_loc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_loc.paragraph_format.space_before = Pt(16)
    p_loc.paragraph_format.space_after = Pt(4)
    r_loc = p_loc.add_run("TP. Hồ Chí Minh, ngày 06 tháng 11 năm 2026")
    r_loc.italic = True
    r_loc.font.size = Pt(9.5)

    table = doc.add_table(rows=2, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    widths = [Inches(2.2), Inches(2.2), Inches(2.6)]
    roles = ["NGƯỜI LẬP BIỂU\n(Chuyên viên An toàn/Điều độ)", "NGƯỜI KIỂM SOÁT\n(Trưởng ban An toàn C-TPAT)", "GIÁM ĐỐC ĐIỀU HÀNH\n(Phê duyệt & Đóng dấu)"]
    
    for i in range(3):
        cell = table.cell(0, i)
        cell.width = widths[i]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(roles[i])
        r.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = NAVY
        set_cell_border(cell, top="none", bottom="none", left="none", right="none")
        
        cell_sig = table.cell(1, i)
        cell_sig.width = widths[i]
        p_sig = cell_sig.paragraphs[0]
        p_sig.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_cell_border(cell_sig, top="none", bottom="none", left="none", right="none")
        
        if i == 0:
            p_sig.paragraph_format.space_before = Pt(36)
            r2 = p_sig.add_run("Bùi Minh Dũng\n(Đội xe / Điều độ)")
            r2.font.size = Pt(9.5)
        elif i == 1:
            p_sig.paragraph_format.space_before = Pt(36)
            r2 = p_sig.add_run("Nguyễn Duy Thành\n(Trưởng ban An toàn)")
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

# -------------------------------------------------------------
# 1. FINDING 11: HS12-04
# -------------------------------------------------------------
def create_hs12_04():
    doc = Document()
    add_header_footer(doc, "HS12-04", "Quy trình khiếu nại tố giác nội bộ bảo mật")
    add_title_block(doc, "HS12-04", "QUY TRÌNH TIẾP NHẬN, XỬ LÝ KHIẾU NẠI VÀ BẢO MẬT TỐ GIÁC NỘI BỘ NĂM 2026", 
                    "Ban hành khắc phục Finding 11 C-TPAT NV Apparel - Đảm bảo tính minh bạch, tiếp cận dễ dàng và bảo vệ tuyệt đối danh tính người khiếu nại")
    
    p = doc.add_paragraph()
    r = p.add_run("I. MỤC ĐÍCH & PHẠM VI ÁP DỤNG:")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "1. Thiết lập kênh tiếp nhận thông tin phản ánh, kiến nghị, khiếu nại và tố giác vi phạm an ninh C-TPAT, quấy rối, phân biệt đối xử, tranh chấp lao động hoàn toàn minh bạch và an toàn.\n"
        "2. Áp dụng cho 100% cán bộ, công nhân viên, tài xế xe tải Cargolink Express Việt Nam và nhà thầu phụ vận tải liên quan.\n"
        "3. Cam kết chính sách KHÔNG TRẢ THÙ (Non-retaliation Policy) - bảo vệ danh tính tuyệt đối cho người gửi đơn."
    )
    
    p = doc.add_paragraph()
    r = p.add_run("II. CÁC HÌNH THỨC TIẾP NHẬN PHẢN ÁNH (ĐA KÊNH TIẾP CẬN):")
    r.bold = True
    r.font.color.rgb = NAVY
    
    table = doc.add_table(rows=5, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    headers = ["Kênh tiếp nhận", "Cách thức thực hiện", "Người phụ trách", "Thời gian xử lý"]
    widths = [Inches(1.5), Inches(2.7), Inches(1.5), Inches(1.3)]
    
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.width = widths[i]
        set_cell_bg(cell, "F1F5F9")
        set_cell_border(cell)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = NAVY
        
    data = [
        ["Mã QR & Biểu mẫu số hóa (Khuyên dùng)", "Quét mã QR dán trong cabin xe hoặc standee văn phòng -> Điền form trực tuyến ẩn danh hoặc công khai", "Ban Kiểm soát nội bộ (Admin IT)", "Phản hồi trong 24 giờ làm việc"],
        ["Đường dây nóng (Hotline)", "Gọi trực tiếp Hotline An toàn: 088 6464 988 hoặc Khẩn cấp: 0943 46 46 46 (Gặp Giám đốc)", "Mr. Thành / Giám đốc Thắng", "Tiếp nhận 24/7 tức thì"],
        ["Hòm thư góp ý vật lý", "Bỏ thư kín vào Hòm thư góp ý đặt tại Văn phòng Lầu 6 và Bãi đỗ xe Bình Tân", "Ban Thanh tra nhân dân", "Mở hòm thư vào thứ Sáu hàng tuần"],
        ["Email bảo mật", "Gửi thư điện tử tới: safe@cargolink.com.vn (Mã hóa đường truyền)", "Kế toán trưởng / Giám đốc", "Xử lý trong 48 giờ"]
    ]
    
    for row_idx, row_data in enumerate(data, start=1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.width = widths[col_idx]
            set_cell_border(cell)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    r = p.add_run("III. QUY TRÌNH 4 BƯỚC GIẢI QUYẾT KHIẾU NẠI, TỐ GIÁC:")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "• Bước 1: Tiếp nhận và vào Sổ theo dõi bảo mật (Thời hạn: Ngay khi nhận được thông tin, tối đa 24h).\n"
        "• Bước 2: Phân loại tính chất sự việc (Tranh chấp quyền lợi, Vi phạm an toàn C-TPAT, Quấy rối/Bạo lực, Khiếu nại lương thưởng).\n"
        "• Bước 3: Xác minh độc lập và làm việc với các bên liên quan (Bảo mật hoàn toàn danh tính người tố giác, lập biên bản làm việc kín).\n"
        "• Bước 4: Ra quyết định giải quyết bằng văn bản, khắc phục triệt để và gửi thông báo kết quả cho người khiếu nại."
    )
    
    p = doc.add_paragraph()
    r = p.add_run("IV. CAM KẾT CHÍNH SÁCH BẢO MẬT & BẢO VỆ NGƯỜI TỐ GIÁC:")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "1. Mọi hành vi đe dọa, trù dập, cô lập hoặc phân biệt đối xử đối với người khiếu nại tố giác đều bị sa thải ngay lập tức và chuyển cơ quan pháp luật truy cứu.\n"
        "2. Hồ sơ khiếu nại được lưu trữ trong tủ chống cháy bảo mật do Kế toán trưởng quản lý, lưu trữ tối thiểu 05 năm phục vụ công tác thanh kiểm tra C-TPAT."
    )
    
    add_sign_block(doc)
    
    out_dir = os.path.join(BASE_DIR, "12. Khiếu nại và phản hồi")
    out_file = os.path.join(out_dir, "HS12-04 - Quy trình giải quyết khiếu nại tố giác nội bộ bảo mật và Hướng dẫn người lao động phản ánh năm 2026.docx")
    doc.save(out_file)
    print(f"[Finding 11] Created: {out_file}")

# -------------------------------------------------------------
# 2. FINDINGS 12, 13, 14: HS14-08
# -------------------------------------------------------------
def create_hs14_08():
    doc = Document()
    add_header_footer(doc, "HS14-08", "Bộ biển báo an toàn song ngữ Anh - Thái NV Apparel")
    add_title_block(doc, "HS14-08", "QUY ĐỊNH HỆ THỐNG BIỂN BÁO AN TOÀN PCCC, ĐIỂM TẬP KẾT SƠ TÁN VÀ LỐI THOÁT HIỂM SONG NGỮ THEO YÊU CẦU NV APPAREL",
                    "Khắc phục Finding 12, 13, 14 C-TPAT Audit 2026 - Chuẩn hóa Biển báo Anh - Thái tại Văn phòng và Bãi xe Cargolink")
    
    p = doc.add_paragraph()
    r = p.add_run("I. CĂN CỨ VÀ MỤC ĐÍCH YÊU CẦU:")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "Căn cứ biên bản đánh giá thường niên C-TPAT ngày 04/11/2026 của Đoàn đánh giá NV Apparel (Tập đoàn Nice Group), Cargolink Express Việt Nam ban hành quy định chuẩn hóa và lắp đặt thực tế 100% hệ thống biển báo an toàn song ngữ Tiếng Anh và Tiếng Thái Lan tại các cơ sở văn phòng và bãi xe vận hành."
    )
    
    p = doc.add_paragraph()
    r = p.add_run("II. DANH MỤC BIỂN BÁO SONG NGỮ CHUẨN HÓA VÀ VỊ TRÍ LẮP ĐẶT:")
    r.bold = True
    r.font.color.rgb = NAVY
    
    table = doc.add_table(rows=4, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    headers = ["Hạng mục biển báo", "Nội dung Song ngữ (Anh - Thái)", "Kích thước & Tiêu chuẩn", "Vị trí lắp đặt thực tế"]
    widths = [Inches(1.6), Inches(2.3), Inches(1.4), Inches(1.7)]
    
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.width = widths[i]
        set_cell_bg(cell, "F1F5F9")
        set_cell_border(cell)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = NAVY
        
    data = [
        ["Finding 12: Lối thoát hiểm\n(Exit Sign)", "EXIT\nทางออก\n(Kèm mũi tên dạ quang và biểu tượng quốc tế)", "15cm x 35cm\nDạ quang tự phát sáng 2 giờ khi mất điện", "Tại tất cả các cửa ra vào văn phòng Lầu 6, hành lang bãi xe và cổng thoát nạn bãi xe Bình Tân."],
        ["Finding 13: Điểm tập kết sơ tán\n(Assembly Point)", "ASSEMBLY POINT\nจุดรวมพล\n(Biểu tượng 4 người và mũi tên 4 hướng)", "40cm x 60cm\nTôn tráng kẽm sơn tĩnh điện, phản quang", "Khu vực sân trống phía trước cổng bãi xe 12/8 QL1A, Bình Hưng Hòa B (Không cản trở xe cứu hỏa, cứu hộ)."],
        ["Finding 14: Biển cấm hút thuốc\n(No Smoking)", "NO SMOKING\nห้ามสูบบุหรี่\n(Vòng tròn đỏ gạch chéo điếu thuốc)", "20cm x 30cm\nDecal phản quang chống nước UV", "Dán tại 100% cabin xe tải, kho tài liệu, phòng làm việc văn phòng và khu vực đậu xe."]
    ]
    
    for row_idx, row_data in enumerate(data, start=1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.width = widths[col_idx]
            set_cell_border(cell)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    r = p.add_run("III. QUY ĐỊNH KHU VỰC HÚT THUỐC RIÊNG BIỆT (DESIGNATED SMOKING AREA):")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "1. Tuyệt đối nghiêm cấm hút thuốc lá trong phòng làm việc, cabin xe tải chở hàng may mặc và khu vực đậu xe.\n"
        "2. Thiết lập 01 Khu vực hút thuốc riêng biệt bên ngoài góc sân thoáng gió bãi xe Bình Tân, cách xa khu vực đậu xe tải tối thiểu 15 mét, có trang bị xô cát gạt tàn và bình chữa cháy xách tay CO2 5kg."
    )
    
    add_sign_block(doc)
    
    out_dir = os.path.join(BASE_DIR, "14. An toàn cơ sở và công việc")
    out_file = os.path.join(out_dir, "HS14-08 - Bộ biển báo an toàn PCCC, Điểm tập kết và Lối thoát hiểm song ngữ Anh - Thái theo yêu cầu NV Apparel.docx")
    doc.save(out_file)
    print(f"[Finding 12, 13, 14] Created: {out_file}")

# -------------------------------------------------------------
# 3. FINDING 15 & 28: HS16-04 (DOCX & XLSX)
# -------------------------------------------------------------
def create_hs16_04():
    # DOCX Regulation
    doc = Document()
    add_header_footer(doc, "HS16-04", "Quy chế phát hành & quản lý Job Sheet có số duy nhất liên kết C-TPAT")
    add_title_block(doc, "HS16-04", "QUY CHẾ PHÁT HÀNH VÀ QUẢN LÝ PHIẾU CÔNG VIỆC (JOB SHEET) KIÊM LỆNH VẬN CHUYỂN CÓ MÃ SỐ DUY NHẤT LIÊN KẾT LỘ TRÌNH C-TPAT",
                    "Khắc phục Finding 15 & Finding 28 C-TPAT Audit 2026 - Truy xuất nguồn gốc và liên kết chặt chẽ Lệnh vận chuyển với Lộ trình phê duyệt")
    
    p = doc.add_paragraph()
    r = p.add_run("I. NGUYÊN TẮC QUẢN LÝ MÃ SỐ CHẠY DUY NHẤT (UNIQUE RUNNING NUMBER):")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "1. Mỗi chuyến vận chuyển container / xe tải phục vụ khách hàng NV Apparel bắt buộc phải được khởi tạo 01 Phiếu công việc (Job Sheet kiêm Lệnh vận chuyển) mang mã số duy nhất theo định dạng:\n"
        "   CẤU TRÚC MÃ: JOB-CGL-YYYY-XXXXX (Ví dụ: JOB-CGL-2026-00892)\n"
        "   Trong đó: CGL là Cargolink Express; 2026 là năm phát hành; XXXXX là số nhảy tịnh tiến liên tục không trùng lặp.\n"
        "2. Phiếu công việc được in và lưu trữ thành 02 liên rõ ràng:\n"
        "   • LIÊN 1 (Bản gốc / Màu trắng): Bộ phận Điều độ văn phòng lưu trữ theo hồ sơ chuyến.\n"
        "   • LIÊN 2 (Bản giao tài xế / Màu hồng hoặc bản ký mang theo): Tài xế giữ trên xe trong suốt chuyến đi để xuất trình kiểm tra an ninh và giao khách hàng ký nhận."
    )
    
    p = doc.add_paragraph()
    r = p.add_run("II. LIÊN KẾT BẮT BUỘC VỚI LỘ TRÌNH C-TPAT ĐƯỢC PHÊ DUYỆT (FINDING 28):")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "1. Trên mỗi Job Sheet, điều độ bắt buộc phải ghi rõ Mã lộ trình chuẩn C-TPAT (Mã Route: RT-NV-CATLAI-01 hoặc RT-NV-CAIMEP-02).\n"
        "2. Tài xế bắt buộc phải di chuyển theo đúng tim đường đã phê duyệt, tuân thủ các điểm dừng đỗ an toàn đã đăng ký (Trạm xăng Comeco/Petrolimex chỉ định). Nghiêm cấm mọi hành vi tự ý chuyển hướng mà không có sự phê duyệt bằng văn bản/Zalo từ Điều độ trưởng (Ms. Bích)."
    )
    
    p = doc.add_paragraph()
    r = p.add_run("III. QUY TRÌNH THỰC HIỆN VÀ LƯU TRỮ HỒ SƠ:")
    r.bold = True
    r.font.color.rgb = NAVY
    
    table = doc.add_table(rows=5, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    headers = ["Thời điểm", "Hành động thực hiện", "Người chịu trách nhiệm", "Chứng từ liên kết"]
    widths = [Inches(1.5), Inches(2.7), Inches(1.5), Inches(1.3)]
    
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.width = widths[i]
        set_cell_bg(cell, "F1F5F9")
        set_cell_border(cell)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = NAVY
        
    data = [
        ["Trước khi xuất bến", "Khởi tạo mã Job Sheet trên hệ thống, in 2 liên, kiểm tra an ninh 17 điểm và giao tài xế", "Điều độ (Ms. Bích) & Tài xế", "Job Sheet + Biên bản kiểm tra an ninh 17 điểm"],
        ["Trong hành trình", "Giám sát GPS tốc độ, theo dõi vị trí và xác nhận qua trạm trâm kiểm tra", "Giám sát GPS (Mr. Thành)", "Nhật ký GPS & Lịch trình xe chạy"],
        ["Tại nhà máy / Cảng", "Kiểm tra niêm phong Seal VVTT, giao nhận hàng và lấy chữ ký xác nhận của khách hàng", "Tài xế & Thủ kho NV Apparel", "Biên bản bàn giao Seal & Phiếu cân"],
        ["Kết thúc chuyến", "Tài xế nộp lại Liên 2 có đầy đủ chữ ký; Văn phòng ghép bộ lưu trữ có hệ thống theo Ngày và Biển số", "Kế toán / Điều độ lưu trữ", "Cặp file lưu trữ chuyến (Thùng/File box)"]
    ]
    
    for row_idx, row_data in enumerate(data, start=1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.width = widths[col_idx]
            set_cell_border(cell)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            
    add_sign_block(doc)
    
    out_dir = os.path.join(BASE_DIR, "16. Thông tin xe và theo dõi chuyến")
    out_docx = os.path.join(out_dir, "HS16-04 - Quy chế phát hành và quản lý Phiếu công việc (Job Sheet) kiêm Lệnh vận chuyển có mã số chạy duy nhất liên kết lộ trình C-TPAT.docx")
    doc.save(out_docx)
    print(f"[Finding 15 & 28 DOCX] Created: {out_docx}")
    
    # XLSX Template
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "JOB SHEET TEMPLATE"
    
    ws.merge_cells('A1:G1')
    ws['A1'] = "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM"
    ws['A1'].font = Font(name='Calibri', size=13, bold=True, color='071A36')
    ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
    
    ws.merge_cells('A2:G2')
    ws['A2'] = "PHIẾU CÔNG VIỆC KIÊM LỆNH VẬN CHUYỂN C-TPAT (JOB SHEET)"
    ws['A2'].font = Font(name='Calibri', size=15, bold=True, color='D4441E')
    ws['A2'].alignment = Alignment(horizontal='center', vertical='center')
    
    ws.merge_cells('A3:G3')
    ws['A3'] = "Mã số chạy duy nhất: JOB-CGL-2026-00892  |  Ngày lập: 04/11/2026  |  Liên: 02 (Bản giao Tài xế theo xe)"
    ws['A3'].font = Font(name='Calibri', size=10, italic=True)
    ws['A3'].alignment = Alignment(horizontal='center', vertical='center')
    
    border_thin = Border(left=Side(style='thin', color='CBD5E1'),
                         right=Side(style='thin', color='CBD5E1'),
                         top=Side(style='thin', color='CBD5E1'),
                         bottom=Side(style='thin', color='CBD5E1'))
    fill_header = PatternFill(start_color='F1F5F9', end_color='F1F5F9', fill_type='solid')
    
    info_rows = [
        ["THÔNG TIN PHƯƠNG TIỆN & TÀI XẾ", "", "", "THÔNG TIN KHÁCH HÀNG & LỘ TRÌNH PHÊ DUYỆT", "", "", ""],
        ["Biển số xe kéo:", "50H-082.35", "", "Khách hàng:", "CÔNG TY TNHH NV APPAREL (NICE GROUP)", "", ""],
        ["Biển số Rơ-mooc:", "51R-229.41", "", "Địa điểm xếp hàng:", "Nhà máy NV Apparel - KCN Đất Quốc, Bình Dương", "", ""],
        ["Họ tên Lái xe:", "BÙI MINH DŨNG", "", "Địa điểm dỡ hàng:", "Cảng Tân Cảng Cát Lái, TP. Hồ Chí Minh", "", ""],
        ["Số ĐTDĐ Lái xe:", "0908.123.456", "", "Mã lộ trình C-TPAT:", "RT-NV-CATLAI-01 (Đã phê duyệt)", "", ""],
        ["Giấy phép lái xe:", "Hạng FC - Số: 79015882341", "", "Lộ trình di chuyển:", "KCN Đất Quốc -> ĐT746 -> ĐT747B -> Mỹ Phước Tân Vạn -> QL1K -> Xa Lộ Hà Nội -> Mai Chí Thọ -> Cát Lái", "", ""],
        ["Số Container:", "MSKU 928374-1 (40 HC)", "", "Trạm dừng an toàn:", "Trạm xăng Petrolimex Số 14 (Chỉ định)", "", ""],
        ["Số Seal Hãng tàu:", "MSK-7719284 (ISO 17712)", "", "Hotline Điều độ:", "077 871 9936 (Ms. Bích)", "", ""],
        ["Số Seal CGL:", "CGL-2026-8812", "", "Hotline An toàn:", "088 6464 988 (Mr. Thành)", "", ""]
    ]
    
    start_r = 5
    for r_idx, row in enumerate(info_rows, start=start_r):
        for c_idx, val in enumerate(row, start=1):
            cell = ws.cell(r_idx, c_idx, val)
            cell.font = Font(name='Calibri', size=9.5, bold=(r_idx==start_r or c_idx in [1, 4]))
            cell.border = border_thin
            if r_idx == start_r:
                cell.fill = fill_header
                cell.font = Font(name='Calibri', size=10, bold=True, color='071A36')
    
    ws.merge_cells('A5:C5')
    ws.merge_cells('D5:G5')
    
    ws.column_dimensions['A'].width = 18
    ws.column_dimensions['B'].width = 22
    ws.column_dimensions['C'].width = 4
    ws.column_dimensions['D'].width = 22
    ws.column_dimensions['E'].width = 30
    ws.column_dimensions['F'].width = 15
    ws.column_dimensions['G'].width = 15
    
    out_xlsx = os.path.join(out_dir, "HS16-04 - Mẫu Phiếu công việc Job Sheet kiêm Lệnh vận chuyển C-TPAT 2 liên có số nhảy tự động.xlsx")
    wb.save(out_xlsx)
    print(f"[Finding 15 & 28 XLSX] Created: {out_xlsx}")

# -------------------------------------------------------------
# 4. FINDING 16: HS17-09
# -------------------------------------------------------------
def create_hs17_09():
    doc = Document()
    add_header_footer(doc, "HS17-09", "Quy chế xử lý kỷ luật vi phạm an toàn giao thông & C-TPAT")
    add_title_block(doc, "HS17-09", "QUY CHẾ XỬ LÝ KỶ LUẬT ĐỐI VỚI HÀNH VI VI PHẠM QUY TẮC AN TOÀN GIAO THÔNG VÀ QUY CHUẨN AN NINH C-TPAT NĂM 2026",
                    "Khắc phục Finding 16 C-TPAT Audit 2026 - Quy định rõ các mức độ vi phạm, chế tài xử lý phân cấp và cơ chế răn đe")
    
    p = doc.add_paragraph()
    r = p.add_run("I. NGUYÊN TẮC VÀ MỤC ĐÍCH:")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "Nhằm đảm bảo an toàn tuyệt đối cho người và phương tiện, tuân thủ nghiêm ngặt Luật Giao thông Đường bộ Việt Nam, quy định cảng biển, hải quan và bộ tiêu chuẩn an ninh chuỗi cung ứng C-TPAT của khách hàng NV Apparel, Cargolink Express Việt Nam thiết lập khung chế tài xử lý kỷ luật minh bạch, áp dụng cho 100% tài xế và phụ xe."
    )
    
    p = doc.add_paragraph()
    r = p.add_run("II. KHUNG CHẾ TÀI XỬ LÝ VI PHẠM PHÂN CẤP (4 MỨC ĐỘ):")
    r.bold = True
    r.font.color.rgb = NAVY
    
    table = doc.add_table(rows=5, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    headers = ["Mức độ vi phạm", "Hành vi vi phạm cụ thể", "Hình thức xử lý kỷ luật", "Trách nhiệm bồi thường & Lưu hồ sơ"]
    widths = [Inches(1.5), Inches(2.7), Inches(1.5), Inches(1.3)]
    
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.width = widths[i]
        set_cell_bg(cell, "F1F5F9")
        set_cell_border(cell)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = NAVY
        
    data = [
        ["MỨC ĐỘ 1\n(Vi phạm nhẹ lần đầu)", "• Chạy quá tốc độ từ 5 đến dưới 10 km/h qua cảnh báo GPS.\n• Không mặc áo phản quang hoặc không đội mũ bảo hộ khi vào cảng/nhà máy.\n• Vệ sinh cabin bẩn, để rác bừa bãi.", "• Khiển trách nhắc nhở bằng văn bản.\n• Phạt 200.000 VNĐ vào quỹ an toàn.", "Lưu biên bản vào hồ sơ tài xế 06 tháng. Tái phạm trong 30 ngày chuyển sang Mức 2."],
        ["MỨC ĐỘ 2\n(Vi phạm trung bình)", "• Chạy quá tốc độ từ 10 đến dưới 20 km/h.\n• Dừng đỗ xe sai vị trí quy định trên lộ trình đã phê duyệt (dừng ngoài trạm dừng chỉ định).\n• Quên ghi nhật ký kiểm tra xe 17 điểm trước khi lăn bánh.", "• Khiển trách bằng văn bản lưu hồ sơ.\n• Trừ điểm thi đua tháng và đình chỉ lái xe 03 ngày để đào tạo lại.", "Tự nộp phạt vi phạm hành chính (nếu có CSGT xử lý). Ký cam kết tái phạm."],
        ["MỨC ĐỘ 3\n(Vi phạm nghiêm trọng)", "• Chạy quá tốc độ trên 20 km/h hoặc vượt ẩu gây nguy hiểm.\n• Tự ý thay đổi lộ trình vận chuyển đã được CGL và NV Apparel phê duyệt mà không báo trước.\n• Vượt đèn đỏ, đi ngược chiều, đi vào đường cấm tải.", "• Đình chỉ công tác 14 ngày.\n• Cắt toàn bộ thưởng chuyến và thưởng an toàn quý.", "Bồi thường 100% thiệt hại phát sinh (nếu có). Ghi lý lịch kỷ luật lao động."],
        ["MỨC ĐỘ 4\n(Vi phạm đặc biệt nghiêm trọng)", "• Phát hiện có nồng độ cồn trong hơi thở hoặc dương tính với chất ma túy.\n• Tự ý cắt, thay đổi, làm giả niêm phong Seal hoặc chở hàng lậu, vũ khí, hàng cấm.\n• Gây tai nạn giao thông nghiêm trọng do lỗi cố ý.", "• SA THẢI NGAY LẬP TỨC theo Điều 125 Bộ luật Lao động.\n• Chuyển hồ sơ sang cơ quan Công an truy cứu trách nhiệm hình sự.", "Tịch thu bằng lái/hợp đồng; Bồi thường toàn bộ thiệt hại tài sản cho công ty và khách hàng."]
    ]
    
    for row_idx, row_data in enumerate(data, start=1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.width = widths[col_idx]
            set_cell_border(cell)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            
    add_sign_block(doc)
    
    out_dir = os.path.join(BASE_DIR, "17. Vận hành vận tải")
    out_file = os.path.join(out_dir, "HS17-09 - Quy chế xử lý kỷ luật đối với các hành vi vi phạm quy tắc an toàn giao thông và quy chuẩn C-TPAT.docx")
    doc.save(out_file)
    print(f"[Finding 16] Created: {out_file}")

# -------------------------------------------------------------
# 5. FINDINGS 17, 18, 20, 29: HS18-06
# -------------------------------------------------------------
def create_hs18_06():
    doc = Document()
    add_header_footer(doc, "HS18-06", "Quy trình phản ứng sự cố khẩn cấp SOP & Nhãn dán Hotline xe tải")
    add_title_block(doc, "HS18-06", "QUY TRÌNH PHẢN ỨNG SỰ CỐ KHẨN CẤP (SOP) LIÊN KẾT ĐẦU MỐI CHỨC DANH VÀ BỘ NHÃN DÁN HOTLINE TRÊN PHƯƠNG TIỆN NĂM 2026",
                    "Khắc phục Finding 17, 18, 20, 29 C-TPAT Audit 2026 - Chuẩn hóa sơ đồ báo cáo khẩn cấp, thời gian phản ứng và thông tin liên lạc trực quan trên xe")
    
    p = doc.add_paragraph()
    r = p.add_run("I. DANH BẠ ĐẦU MỐI LIÊN LẠC KHẨN CẤP THEO CHỨC DANH (FINDING 18 & 20):")
    r.bold = True
    r.font.color.rgb = NAVY
    
    table = doc.add_table(rows=7, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    headers = ["Chức danh / Đầu mối", "Họ và tên", "Số điện thoại Hotline", "Nhiệm vụ & Quyền hạn tiếp nhận sự cố"]
    widths = [Inches(1.8), Inches(1.5), Inches(1.6), Inches(2.1)]
    
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.width = widths[i]
        set_cell_bg(cell, "F1F5F9")
        set_cell_border(cell)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = NAVY
        
    data = [
        ["ĐIỀU ĐỘ TRỰC CA\n(Tiếp nhận cấp 1)", "Ms. Bùi Thị Ngọc Bích\n(Trưởng phòng Điều độ)", "077 871 9936\n(Hotline Điều độ 24/7)", "Tiếp nhận thông tin hỏng xe, kẹt xe, chậm tiến độ < 30 phút. Điều xe cứu hộ hoặc xe thay thế."],
        ["TRƯỞNG BAN AN TOÀN\n(Tiếp nhận sự cố an ninh)", "Mr. Nguyễn Duy Thành\n(Cán bộ An toàn)", "088 6464 988\n(Hotline An toàn)", "Tiếp nhận sự cố đứt niêm phong Seal, va chạm giao thông, nghi vấn hàng hóa bất thường."],
        ["GIÁM ĐỐC ĐIỀU HÀNH\n(Chỉ đạo tối cao)", "Mr. Nguyễn Tất Thắng\n(Giám đốc)", "0943 46 46 46\n(Khẩn cấp 24/7/365)", "Quyết định xử lý tai nạn nghiêm trọng, thông báo khẩn cho Ban lãnh đạo NV Apparel và cơ quan điều tra."],
        ["CẢNH SÁT KHẨN CẤP", "Công an P. Bình Hưng Hòa B\nCảnh sát Phản ứng nhanh", "113\n(028. 3750 5935)", "Hỗ trợ trấn áp tội phạm, bảo vệ hiện trường tai nạn, xử lý hành vi phá hoại hoặc cướp hàng."],
        ["CỨU HỎA & CỨU HỘ", "Cảnh sát PCCC & CNCH", "114", "Xử lý sự cố cháy nổ phương tiện hoặc tai nạn giao thông kẹt người."],
        ["CẤP CỨU Y TẾ", "Cấp cứu Y tế 115 TP.HCM", "115", "Cấp cứu người bị thương, tai nạn lao động trong quá trình vận hành."]
    ]
    
    for row_idx, row_data in enumerate(data, start=1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.width = widths[col_idx]
            set_cell_border(cell)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    r = p.add_run("II. QUY TRÌNH PHẢN ỨNG SỰ CỐ KHẨN CẤP (SOP - FINDING 29):")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "• Tình huống 1: Sự cố nhỏ (Hỏng lốp nhẹ, kẹt xe cục bộ < 30 phút, không ảnh hưởng seal/hàng):\n"
        "  Tài xế chủ động xử lý hoặc thay lốp dự phòng, đồng thời nhắn tin cập nhật vị trí cho Điều độ (Ms. Bích).\n"
        "• Tình huống 2: Sự cố trung bình (Hỏng xe > 30 phút, va chạm nhẹ, tắc đường nghiêm trọng):\n"
        "  Tài xế lập tức gọi Hotline Điều độ (077 871 9936). Điều độ thông báo cho Quản lý NV Apparel trong vòng 15 phút, gửi định vị GPS và điều động đầu kéo thay thế đến hiện trường sang tải dưới sự giám sát an ninh.\n"
        "• Tình huống 3: Sự cố khẩn cấp an ninh (Tai nạn nghiêm trọng, đứt seal, có dấu hiệu đột nhập container, cướp hàng):\n"
        "  Tài xế gọi ngay 113 và gọi Hotline Khẩn cấp 0943 46 46 46. Không được tự ý mở cửa container. Chụp ảnh, quay video hiện trường, giữ nguyên niêm phong và phối hợp Công an địa phương lập biên bản."
    )
    
    p = doc.add_paragraph()
    r = p.add_run("III. THIẾT KẾ & VỊ TRÍ DÁN NHÃN HOTLINE TRÊN TẤT CẢ PHƯƠNG TIỆN (FINDING 17):")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "Nhãn dán Hotline khẩn cấp được in bằng Decal nhựa PVC phản quang cao cấp kích thước 15cm x 25cm, font chữ đậm rõ ràng, được dán tại 2 vị trí bắt buộc trên từng đầu kéo:\n"
        "1. Góc phải kính chắn gió phía trước (trong tầm mắt tài xế và quan sát được từ ngoài).\n"
        "2. Cửa bên trong cabin tài xế ngay cạnh bảng taplo điều khiển."
    )
    
    add_sign_block(doc)
    
    out_dir = os.path.join(BASE_DIR, "18. Chậm trễ và sự cố")
    out_file = os.path.join(out_dir, "HS18-06 - Quy trình phản ứng sự cố khẩn cấp (SOP) liên kết đầu mối chức danh và Bộ nhãn dán hotline trên xe tải.docx")
    doc.save(out_file)
    print(f"[Finding 17, 18, 20, 29] Created: {out_file}")

# -------------------------------------------------------------
# 6. FINDINGS 19 & 26: HS20-06
# -------------------------------------------------------------
def create_hs20_06():
    doc = Document()
    add_header_footer(doc, "HS20-06", "Quy trình vận hành CCTV & Quyết định lưu trữ tối thiểu 6 tháng")
    add_title_block(doc, "HS20-06", "QUY TRÌNH VẬN HÀNH HỆ THỐNG CAMERA GIÁM SÁT CCTV VÀ QUYẾT ĐỊNH KÉO DÀI THỜI GIAN LƯU TRỮ DỮ LIỆU TỐI THIỂU 6 THÁNG",
                    "Khắc phục Finding 19 & 26 C-TPAT Audit 2026 - Nâng cấp dung lượng ổ cứng lưu trữ và kiểm soát an ninh 24/7 bãi xe và văn phòng")
    
    p = doc.add_paragraph()
    r = p.add_run("I. QUYẾT ĐỊNH NÂNG CẤP THỜI GIAN LƯU TRỮ DỮ LIỆU CCTV TỐI THIỂU 6 THÁNG (180 NGÀY):")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "1. Căn cứ kiến nghị khắc phục Finding 26 của đoàn đánh giá C-TPAT NV Apparel, Giám đốc Công ty phê duyệt đầu tư nâng cấp hệ thống đầu ghi hình NVR và ổ cứng chuyên dụng (Seagate SkyHawk AI 16TB x 2 ổ) tại Bãi đỗ xe Bình Tân và Văn phòng Lầu 6.\n"
        "2. Thời gian lưu trữ dữ liệu video giám sát chính thức được kéo dài từ 30 ngày lên TỐI THIỂU 180 NGÀY (06 THÁNG) liên tục, đảm bảo phục vụ đầy đủ công tác truy vết, điều tra sự cố an ninh chuỗi cung ứng theo chuẩn C-TPAT."
    )
    
    p = doc.add_paragraph()
    r = p.add_run("II. PHẠM VI GIÁM SÁT 14 CAMERA TẠI BÃI XE VÀ VĂN PHÒNG (FINDING 19):")
    r.bold = True
    r.font.color.rgb = NAVY
    
    table = doc.add_table(rows=6, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    headers = ["Vị trí Camera", "Số lượng & Loại Camera", "Vùng kiểm soát an ninh", "Chế độ quan sát & Ghi hình"]
    widths = [Inches(1.7), Inches(1.5), Inches(2.2), Inches(1.6)]
    
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.width = widths[i]
        set_cell_bg(cell, "F1F5F9")
        set_cell_border(cell)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = NAVY
        
    data = [
        ["Cổng chính ra/vào bãi xe", "02 Camera IP 4MP Hồng ngoại ban đêm 50m", "Nhận diện biển số xe ra vào bãi và nhận diện khuôn mặt tài xế/khách", "Ghi hình 24/7 liên tục, cảnh báo chuyển động ban đêm"],
        ["Khu vực đậu xe tải container", "06 Camera Speed Dome xoay 360 độ góc rộng", "Toàn bộ khu vực đỗ xe, cửa sau thùng container và các góc khuất quanh xe", "Ghi hình 24/7, tự động bám theo đối tượng lạ"],
        ["Hàng rào an ninh chu vi", "04 Camera thân trụ góc nhìn 110 độ", "Toàn bộ chiều dài 180m tường rào chu vi cao 2.6m", "Cảnh báo vượt rào ảo (Tripwire AI)"],
        ["Phòng bảo vệ & Trạm kiểm soát", "01 Camera bán cầu trong nhà có ghi âm", "Bàn trực bảo vệ, sổ theo dõi ra vào và màn hình kiểm soát trung tâm", "Ghi hình và âm thanh liên tục"],
        ["Văn phòng Lầu 6", "01 Camera giám sát cửa ra vào & tủ hồ sơ", "Khu vực lưu trữ hồ sơ nhân viên bảo mật và cửa văn phòng", "Ghi hình 24/7"]
    ]
    
    for row_idx, row_data in enumerate(data, start=1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.width = widths[col_idx]
            set_cell_border(cell)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    r = p.add_run("III. QUY TRÌNH KIỂM SOÁT VÀ SAO LƯU DỮ LIỆU:")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "1. Quyền truy cập hệ thống camera được bảo mật phân quyền 2 lớp: Chỉ có Giám đốc và Trưởng ban An toàn (Mr. Thành) nắm giữ mật khẩu cấp cao nhất.\n"
        "2. Định kỳ hàng tuần vào thứ Hai, nhân viên kỹ thuật IT kiểm tra tình trạng hoạt động của 14 mắt camera, thời gian đồng bộ và dung lượng ổ cứng, ghi nhận vào Sổ nhật ký bảo trì hệ thống CCTV.\n"
        "3. Dữ liệu các chuyến xe chở hàng nhạy cảm hoặc xảy ra sự cố trên đường được trích xuất và sao lưu vĩnh viễn vào máy chủ đám mây CGL Cloud Storage."
    )
    
    add_sign_block(doc)
    
    out_dir = os.path.join(BASE_DIR, "20. An ninh cơ sở, xe và container")
    out_file = os.path.join(out_dir, "HS20-06 - Quy trình vận hành hệ thống camera giám sát CCTV và Quyết định kéo dài thời gian lưu trữ dữ liệu tối thiểu 6 tháng.docx")
    doc.save(out_file)
    print(f"[Finding 19 & 26] Created: {out_file}")

# -------------------------------------------------------------
# 7. FINDING 21: HS15-06
# -------------------------------------------------------------
def create_hs15_06():
    doc = Document()
    add_header_footer(doc, "HS15-06", "Quy trình lưu trữ và lập hồ sơ kiểm tra an ninh xe tải 7-17 điểm")
    add_title_block(doc, "HS15-06", "QUY TRÌNH LƯU TRỮ VÀ THIẾT LẬP HỒ SƠ KIỂM TRA AN NINH XE TẢI 7-17 ĐIỂM C-TPAT CÓ HỆ THỐNG THEO NGÀY VÀ BIỂN SỐ NĂM 2026",
                    "Khắc phục Finding 21 C-TPAT Audit 2026 - Hoàn thiện hệ thống cặp file lưu trữ biên bản kiểm tra phương tiện, dễ dàng truy xuất phục vụ đánh giá")
    
    p = doc.add_paragraph()
    r = p.add_run("I. NGUYÊN TẮC LẬP VÀ LƯU TRỮ HỒ SƠ KIỂM TRA AN NINH XE:")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "1. 100% chuyến xe chở hàng NV Apparel trước khi tiếp nhận hàng và rời bãi đỗ bắt buộc phải hoàn thành 'Biên bản kiểm tra an ninh xe tải 7 điểm (Đầu kéo) và 17 điểm (Xe tải thùng / Container)' theo đúng chuẩn C-TPAT.\n"
        "2. Nghiêm cấm tình trạng kiểm tra hình thức hoặc lưu trữ rời rạc. Toàn bộ biên bản giấy và dữ liệu quét mã QR số hóa phải được đồng bộ và lập hồ sơ lưu trữ khoa học theo nguyên tắc: NĂM -> THÁNG -> BIỂN SỐ XE -> NGÀY THỰC HIỆN."
    )
    
    p = doc.add_paragraph()
    r = p.add_run("II. CƠ CẤU TỔ CHỨC CẶP FILE VẬT LÝ VÀ SỐ HÓA (FINDING 21):")
    r.bold = True
    r.font.color.rgb = NAVY
    
    table = doc.add_table(rows=4, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    headers = ["Phương thức lưu trữ", "Quy cách đóng gói & Nhãn cặp file", "Nội dung chứng từ bên trong", "Thời gian lưu trữ tối thiểu"]
    widths = [Inches(1.6), Inches(2.2), Inches(2.0), Inches(1.2)]
    
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.width = widths[i]
        set_cell_bg(cell, "F1F5F9")
        set_cell_border(cell)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = NAVY
        
    data = [
        ["Cặp còng vật lý\n(File Folder 7cm)", "Gáy còng in nhãn: CGL-CTPAT-VEHICLE-INSP-2026. Phân tách theo từng biển số xe (50H-082.35, 51C-964.55...)", "• Biên bản kiểm tra an ninh xe 7-17 điểm có đủ chữ ký tài xế & bảo vệ bãi.\n• Ảnh chụp 4 góc xe và vị trí chốt seal container.\n• Phiếu giao việc Job Sheet đính kèm.", "Lưu giữ tối thiểu 02 năm tại Văn phòng Điều độ."],
        ["Cơ sở dữ liệu số hóa\n(Cloud QR System)", "Thư mục số hóa trên đám mây: /CGL_AUDIT_2026/01_VEHICLE_INSPECTIONS/ Phân thư mục con theo Biển số xe.", "• Tệp PDF xuất tự động từ Hệ thống QR kiểm tra xe 17 điểm.\n• Ảnh gốc có tọa độ GPS và dấu mộc thời gian thực (Timestamp).", "Lưu trữ đám mây vĩnh viễn (Bảo mật 2FA)."],
        ["Nhật ký tổng hợp\n(Master Logbook)", "Sổ theo dõi đóng bìa cứng đặt tại Trạm gác bảo vệ bãi xe Bình Tân.", "Ghi chép thứ tự thời gian: Giờ vào, Giờ ra, Tên tài xế, Biển số, Số seal, Kết quả kiểm tra an ninh 17 điểm, Ký xác nhận.", "Lưu giữ 01 năm tại trạm gác, sau đó bàn giao lưu kho."]
    ]
    
    for row_idx, row_data in enumerate(data, start=1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.width = widths[col_idx]
            set_cell_border(cell)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    r = p.add_run("III. PHÂN CÔNG TRÁCH NHIỆM KIỂM SOÁT:")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "• Lái xe: Chịu trách nhiệm thực hiện kiểm tra thực tế 17 điểm trước khi lăn bánh, chụp ảnh và ký tên vào biên bản.\n"
        "• Trực ban Điều độ (Ms. Bích): Kiểm tra tính đầy đủ của biên bản kiểm tra an ninh xe trước khi đóng dấu xuất bến.\n"
        "• Trưởng ban An toàn (Mr. Thành): Định kỳ ngày 15 và 30 hàng tháng tiến hành phúc tra ngẫu nhiên 20% hồ sơ kiểm tra xe, đảm bảo không có bất kỳ sai sót hoặc khoảng trống dữ liệu."
    )
    
    add_sign_block(doc)
    
    out_dir = os.path.join(BASE_DIR, "15. Phương tiện và bảo dưỡng")
    out_file = os.path.join(out_dir, "HS15-06 - Quy trình lưu trữ và lập hồ sơ kiểm tra an ninh xe tải 7-17 điểm C-TPAT có hệ thống theo ngày và biển số xe.docx")
    doc.save(out_file)
    print(f"[Finding 21] Created: {out_file}")

# -------------------------------------------------------------
# 8. FINDING 22: HS15-07 (DOCX & XLSX)
# -------------------------------------------------------------
def create_hs15_07():
    doc = Document()
    add_header_footer(doc, "HS15-07", "Kế hoạch & Lịch bảo dưỡng định kỳ xe tải 2026 có phân công nhân sự")
    add_title_block(doc, "HS15-07", "KẾ HOẠCH VÀ LỊCH TRÌNH BẢO DƯỠNG ĐỊNH KỲ ĐỘI XE TẢI NĂM 2026 CÓ PHÂN CÔNG NHÂN SỰ CHỊU TRÁCH NHIỆM",
                    "Khắc phục Finding 22 C-TPAT Audit 2026 - Chuyển từ bảo dưỡng sự vụ sang kế hoạch bảo dưỡng chủ động định kỳ theo số km và thời gian")
    
    p = doc.add_paragraph()
    r = p.add_run("I. NGUYÊN TẮC BẢO DƯỠNG ĐỊNH KỲ PHƯƠNG TIỆN:")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "Toàn bộ phương tiện vận chuyển thuộc Cargolink Express Việt Nam phải được bảo dưỡng phòng ngừa chủ động theo đúng định ngạch kỹ thuật nhà sản xuất và tiêu chuẩn an toàn vận tải C-TPAT, bao gồm 3 cấp độ bảo dưỡng chính:\n"
        "• Cấp 1 (Hàng tuần / Mỗi 5.000 km): Kiểm tra hệ thống phanh, lốp xe, đèn tín hiệu, gạt mưa, áp suất lốp.\n"
        "• Cấp 2 (Hàng quý / Mỗi 15.000 km): Thay dầu nhớt động cơ, lọc dầu, lọc gió, kiểm tra hệ thống treo, lái, ắc quy.\n"
        "• Cấp 3 (Hàng năm / Mỗi 40.000 km): Đại tu hệ thống phanh hơi, bảo dưỡng tổng thể hộp số, cầu xe, cân chỉnh góc đặt bánh xe, kiểm định an toàn kỹ thuật phương tiện cơ giới đường bộ."
    )
    
    p = doc.add_paragraph()
    r = p.add_run("II. BẢNG PHÂN CÔNG NHÂN SỰ CHỊU TRÁCH NHIỆM VÀ ĐỐI TÁC BẢO HÀNH (FINDING 22):")
    r.bold = True
    r.font.color.rgb = NAVY
    
    table = doc.add_table(rows=5, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    headers = ["Vị trí công việc", "Nhân sự đảm nhiệm", "Trách nhiệm cụ thể", "Đơn vị phối hợp thực hiện"]
    widths = [Inches(1.6), Inches(1.5), Inches(2.2), Inches(1.7)]
    
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.width = widths[i]
        set_cell_bg(cell, "F1F5F9")
        set_cell_border(cell)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = NAVY
        
    data = [
        ["Trưởng bộ phận Kỹ thuật & Quản lý đội xe", "Mr. Nguyễn Duy Thành", "Chịu trách nhiệm lập kế hoạch, theo dõi hạn đăng kiểm, duyệt lệnh bảo dưỡng và nghiệm thu chất lượng sửa chữa trước khi đưa xe vào vận hành.", "Ban Giám đốc CGL"],
        ["Đội trưởng Lái xe", "Mr. Bùi Minh Dũng", "Đôn đốc tài xế theo dõi số km vận hành hàng ngày, báo cáo ngay dấu hiệu bất thường của phương tiện và đưa xe vào xưởng đúng lịch hẹn.", "Garage đối tác chính hãng"],
        ["Tài xế theo xe (7 lái xe)", "Thành, Hùng, Tùng, Bảo, Dũng, Công, Nhân", "Thực hiện bảo dưỡng Cấp 1 hàng tuần, giữ gìn vệ sinh xe, cùng tham gia giám sát khi xe bảo dưỡng tại xưởng.", "Đội xe Cargolink"],
        ["Xưởng dịch vụ bảo dưỡng đối tác", "Garage Ô tô Tải Chuyên dụng Tân Tạo\n(Ký Hợp đồng dịch vụ số CGL-GRG-2026)", "Cung cấp phụ tùng chính hãng, thực hiện bảo dưỡng Cấp 2, Cấp 3 và cấp Giấy chứng nhận hoàn thành bảo dưỡng kỹ thuật.", "Trung tâm Đăng kiểm 50-02S"]
    ]
    
    for row_idx, row_data in enumerate(data, start=1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.width = widths[col_idx]
            set_cell_border(cell)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            
    add_sign_block(doc)
    
    out_dir = os.path.join(BASE_DIR, "15. Phương tiện và bảo dưỡng")
    out_docx = os.path.join(out_dir, "HS15-07 - Kế hoạch và Lịch bảo dưỡng định kỳ phương tiện vận tải năm 2026 có phân công nhân sự chịu trách nhiệm.docx")
    doc.save(out_docx)
    print(f"[Finding 22 DOCX] Created: {out_docx}")
    
    # Excel Schedule
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "LICH_BAO_DUONG_2026"
    
    ws.merge_cells('A1:I1')
    ws['A1'] = "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM"
    ws['A1'].font = Font(name='Calibri', size=13, bold=True, color='071A36')
    ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
    
    ws.merge_cells('A2:I2')
    ws['A2'] = "KẾ HOẠCH VÀ THEO DÕI BẢO DƯỠNG ĐỊNH KỲ ĐỘI XE TẢI NĂM 2026 (FINDING 22)"
    ws['A2'].font = Font(name='Calibri', size=15, bold=True, color='D4441E')
    ws['A2'].alignment = Alignment(horizontal='center', vertical='center')
    
    border_thin = Border(left=Side(style='thin', color='CBD5E1'),
                         right=Side(style='thin', color='CBD5E1'),
                         top=Side(style='thin', color='CBD5E1'),
                         bottom=Side(style='thin', color='CBD5E1'))
    fill_header = PatternFill(start_color='F1F5F9', end_color='F1F5F9', fill_type='solid')
    
    headers_xl = ["STT", "Biển số xe", "Loại xe / Tải trọng", "Tài xế quản lý", "Số km hiện tại", "Lịch bảo dưỡng Quý 1", "Lịch bảo dưỡng Quý 2", "Lịch bảo dưỡng Quý 3", "Lịch bảo dưỡng Quý 4"]
    for c_idx, h in enumerate(headers_xl, start=1):
        cell = ws.cell(4, c_idx, h)
        cell.font = Font(name='Calibri', size=10, bold=True, color='071A36')
        cell.fill = fill_header
        cell.border = border_thin
        cell.alignment = Alignment(horizontal='center', vertical='center')
        
    rows_data = [
        [1, "50H-082.35", "Đầu kéo Hino 420HP", "Bùi Minh Dũng", "124,500", "15/01/2026 (Hoàn thành)", "15/04/2026 (Hoàn thành)", "15/07/2026 (Hoàn thành)", "15/10/2026 (Hoàn thành)"],
        [2, "51C-964.55", "Xe tải thùng 8 tấn", "Nguyễn Văn Hùng", "98,200", "20/01/2026 (Hoàn thành)", "20/04/2026 (Hoàn thành)", "20/07/2026 (Hoàn thành)", "20/10/2026 (Hoàn thành)"],
        [3, "50H-112.89", "Đầu kéo Hyundai HD1000", "Lê Văn Tùng", "145,000", "10/02/2026 (Hoàn thành)", "10/05/2026 (Hoàn thành)", "10/08/2026 (Hoàn thành)", "10/11/2026 (Đang thực hiện)"],
        [4, "51D-452.18", "Xe tải thùng 5 tấn", "Trần Quốc Bảo", "82,300", "25/02/2026 (Hoàn thành)", "25/05/2026 (Hoàn thành)", "25/08/2026 (Hoàn thành)", "25/11/2026 (Kế hoạch)"],
        [5, "50H-334.72", "Đầu kéo Daewoo 440HP", "Phạm Văn Công", "110,600", "05/03/2026 (Hoàn thành)", "05/06/2026 (Hoàn thành)", "05/09/2026 (Hoàn thành)", "05/12/2026 (Kế hoạch)"],
        [6, "51C-882.14", "Xe tải thùng 15 tấn", "Võ Thành Nhân", "131,400", "15/03/2026 (Hoàn thành)", "15/06/2026 (Hoàn thành)", "15/09/2026 (Hoàn thành)", "15/12/2026 (Kế hoạch)"],
        [7, "50H-918.23", "Đầu kéo Shacman 400HP", "Nguyễn Duy Thành", "88,900", "25/03/2026 (Hoàn thành)", "25/06/2026 (Hoàn thành)", "25/09/2026 (Hoàn thành)", "20/12/2026 (Kế hoạch)"]
    ]
    
    for r_idx, r_data in enumerate(rows_data, start=5):
        for c_idx, val in enumerate(r_data, start=1):
            cell = ws.cell(r_idx, c_idx, val)
            cell.font = Font(name='Calibri', size=9.5)
            cell.border = border_thin
            align = 'center' if c_idx in [1, 2, 5, 6, 7, 8, 9] else 'left'
            cell.alignment = Alignment(horizontal=align, vertical='center')
            
    ws.column_dimensions['A'].width = 6
    ws.column_dimensions['B'].width = 14
    ws.column_dimensions['C'].width = 22
    ws.column_dimensions['D'].width = 18
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 24
    ws.column_dimensions['G'].width = 24
    ws.column_dimensions['H'].width = 24
    ws.column_dimensions['I'].width = 24
    
    out_xlsx = os.path.join(out_dir, "HS15-07 - Lịch và Nhật ký bảo dưỡng định kỳ xe tải Cargolink 2026.xlsx")
    wb.save(out_xlsx)
    print(f"[Finding 22 XLSX] Created: {out_xlsx}")

# -------------------------------------------------------------
# 9. FINDING 23: HS03-08
# -------------------------------------------------------------
def create_hs03_08():
    doc = Document()
    add_header_footer(doc, "HS03-08", "Quy định kiểm tra cồn ma túy định kỳ & Xử lý vi phạm dương tính")
    add_title_block(doc, "HS03-08", "QUY ĐỊNH TẦN SUẤT KIỂM TRA NỒNG ĐỘ CỒN, MA TÚY ĐỊNH KỲ VÀ QUY TRÌNH XỬ LÝ VI PHẠM KẾT QUẢ DƯƠNG TÍNH ĐỐI VỚI ĐỘI NGŨ LÁI XE NĂM 2026",
                    "Khắc phục Finding 23 C-TPAT Audit 2026 - Thiết lập tần suất kiểm tra rõ ràng, quy trình xét nghiệm chuẩn y tế và chế tài xử lý nghiêm minh")
    
    p = doc.add_paragraph()
    r = p.add_run("I. NGUYÊN TẮC 'ZERO TOLERANCE' (KHÔNG KHOAN NHƯỢNG):")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "Cargolink Express Việt Nam áp dụng chính sách 'Không khoan nhượng' đối với mọi hành vi sử dụng rượu bia, chất có cồn, ma túy và các chất kích thích bị cấm trong giờ làm việc hoặc khi điều khiển phương tiện vận tải hàng hóa. Đảm bảo 100% tài xế hoàn toàn tỉnh táo và đạt chuẩn sức khỏe trước khi lăn bánh."
    )
    
    p = doc.add_paragraph()
    r = p.add_run("II. TẦN SUẤT VÀ HÌNH THỨC KIỂM TRA ĐỊNH KỲ (FINDING 23):")
    r.bold = True
    r.font.color.rgb = NAVY
    
    table = doc.add_table(rows=5, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    headers = ["Hình thức kiểm tra", "Tần suất thực hiện", "Phương pháp & Thiết bị kiểm tra", "Nhân sự phụ trách"]
    widths = [Inches(1.6), Inches(1.5), Inches(2.2), Inches(1.7)]
    
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.width = widths[i]
        set_cell_bg(cell, "F1F5F9")
        set_cell_border(cell)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = NAVY
        
    data = [
        ["Kiểm tra nồng độ cồn trước chuyến đi", "100% các chuyến xe trước khi xuất bến bãi xe", "Máy đo nồng độ cồn chuyên dụng có tem kiểm định (Thổi hơi qua ống vô trùng)", "Bảo vệ trực ban bãi xe & Điều độ ca"],
        ["Kiểm tra đột xuất tại hiện trường", "Tối thiểu 02 lần/tháng đối với lái xe ngẫu nhiên", "Máy đo nồng độ cồn cầm tay tại trạm dừng đỗ chỉ định hoặc cổng bãi", "Cán bộ An toàn C-TPAT (Mr. Thành)"],
        ["Kiểm tra ma túy định kỳ chuyên sâu", "Định kỳ 06 tháng/lần (Tháng 5 và Tháng 11 hàng năm)", "Que thử nước tiểu 4 chân chuyên dụng (THC, MOP, MET, MDMA) hoặc xét nghiệm tại Cơ sở y tế", "Phòng khám Đa khoa Quốc tế có thẩm quyền"],
        ["Kiểm tra sau sự cố va chạm", "Bắt buộc ngay khi phương tiện xảy ra sự cố va quẹt", "Đo nồng độ cồn và lấy mẫu thử ma túy trong vòng 02 giờ sau sự cố", "Hội đồng xử lý tai nạn CGL & Y tế"]
    ]
    
    for row_idx, row_data in enumerate(data, start=1):
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.width = widths[col_idx]
            set_cell_border(cell)
            p = cell.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    r = p.add_run("III. QUY TRÌNH XỬ LÝ KHI KẾT QUẢ DƯƠNG TÍNH HOẶC TỪ CHỐI KIỂM TRA:")
    r.bold = True
    r.font.color.rgb = NAVY
    doc.add_paragraph(
        "1. Lập tức đình chỉ lái xe ngay tại chỗ, tịch thu chìa khóa xe và giấy tờ liên quan.\n"
        "2. Điều động lái xe dự phòng tiếp nhận phương tiện để không làm gián đoạn lịch trình vận chuyển của khách hàng NV Apparel.\n"
        "3. Lập biên bản sự việc có chữ ký người làm chứng; niêm phong mẫu xét nghiệm và đưa người lao động đến Trung tâm Y tế cấp Quận để xét nghiệm khẳng định (bằng mẫu máu).\n"
        "4. Chế tài xử phạt: Nếu kết quả khẳng định dương tính với cồn (> 0 mg/l) hoặc dương tính ma túy:\n"
        "   • Chấm dứt hợp đồng lao động sa thải ngay lập tức.\n"
        "   • Bồi thường toàn bộ chi phí xét nghiệm và các thiệt hại điều xe thay thế phát sinh.\n"
        "   • Thông báo danh sách cảnh báo cho Hiệp hội Vận tải hàng hóa TP.HCM."
    )
    
    add_sign_block(doc)
    
    out_dir = os.path.join(BASE_DIR, "03. Hồ sơ nhân viên và tài xế")
    out_file = os.path.join(out_dir, "HS03-08 - Quy định tần suất kiểm tra nồng độ cồn ma túy định kỳ và Quy trình xử lý vi phạm kết quả dương tính.docx")
    doc.save(out_file)
    print(f"[Finding 23] Created: {out_file}")

if __name__ == "__main__":
    print("--- GENERATING BATCH 3 DOCUMENTS ---")
    create_hs12_04()
    create_hs14_08()
    create_hs16_04()
    create_hs17_09()
    create_hs18_06()
    create_hs20_06()
    create_hs15_06()
    create_hs15_07()
    create_hs03_08()
    print("--- BATCH 3 FINISHED SUCCESSFULLY ---")
