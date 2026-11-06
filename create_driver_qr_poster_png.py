import os, sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026"
FORMS_DIR = os.path.join(BASE_DIR, "CTPAT_QR_FORMS")
ASSETS_DIR = os.path.join(BASE_DIR, "00_BO_BANNER_VA_LOGO_CARGOLINK")
TARGET_DIR = os.path.join(BASE_DIR, "08. Truyền đạt nội quy và chính sách")
PNG_OUT = os.path.join(TARGET_DIR, "HS08-03 - Bảng mã QR tra cứu Sổ tay điện tử và Quy định an ninh cho Tài xế và CBNV.png")

# A4 at 300 DPI: 2480 x 3508
W, H = 2480, 3508
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

# Try loading Windows system fonts
def get_font(size, bold=False):
    font_names = ["timesbd.ttf" if bold else "times.ttf", "arialbd.ttf" if bold else "arial.ttf", "segoeuib.ttf" if bold else "segoeui.ttf"]
    for fn in font_names:
        try:
            return ImageFont.truetype(fn, size)
        except Exception:
            continue
    return ImageFont.load_default()

font_title = get_font(52, bold=True)
font_sub = get_font(30, bold=False)
font_sec = get_font(36, bold=True)
font_card_title = get_font(26, bold=True)
font_card_desc = get_font(20, bold=False)
font_tag = get_font(18, bold=True)
font_footer = get_font(22, bold=False)
font_footer_bold = get_font(26, bold=True)

# 1. HEADER BANNER
draw.rectangle([0, 0, W, 420], fill='#071A36')
draw.rectangle([0, 420, W, 435], fill='#D4441E')

# Logo in header
logo_path = os.path.join(ASSETS_DIR, "Cargolink_Logo_Vector_HighRes.png")
if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert('RGBA')
    logo.thumbnail((450, 150), Image.Resampling.LANCZOS)
    img.paste(logo, (80, 80), logo)

# Header text
draw.text((580, 75), "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM", font=get_font(34, bold=True), fill='#FFFFFF')
draw.text((580, 130), "HỆ THỐNG AN NINH C-TPAT & QUẢN LÝ CHẤT LƯỢNG ISO 9001 / ISO 14001 / ISO 39001", font=get_font(24, bold=False), fill='#CBD5E1')

draw.text((W // 2, 235), "BẢNG MÃ QR TRA CỨU SỔ TAY ĐIỆN TỬ & CHÍNH SÁCH AN NINH", font=font_title, fill='#FFFFFF', anchor="mm")
draw.text((W // 2, 310), "DÀNH CHO TOÀN BỘ CÔNG NHÂN VIÊN & ĐỘI NGŨ LÁI XE PHỤC VỤ KHÁCH HÀNG NV APPAREL", font=font_sub, fill='#FCD34D', anchor="mm")
draw.text((W // 2, 365), "Quét mã QR bằng Camera điện thoại / Zalo để xem cẩm nang nghiệp vụ và làm bài kiểm tra trực tuyến 24/7", font=get_font(22, bold=False), fill='#E2E8F0', anchor="mm")

# 2. EMERGENCY HOTLINE BAR
draw.rectangle([80, 470, W - 80, 570], fill='#FEF2F2', outline='#DC2626', width=3)
draw.text((120, 495), "🚨 ĐƯỜNG DÂY NÓNG KHẨN CẤP AN NINH 24/7:", font=get_font(28, bold=True), fill='#991B1B')
draw.text((750, 492), "0943 46 46 46", font=get_font(34, bold=True), fill='#DC2626')
draw.text((120, 535), "Hotline Điều độ: 077 871 9936 (Ms. Bích)  |  Hotline An toàn: 088 6464 988 (Mr. Thành)  |  Báo cáo sự cố dưới 15 phút", font=get_font(22, bold=False), fill='#475569')

# 3. 6 DIGITAL GUIDES (3x2 Grid)
draw.text((80, 610), "📘 PHẦN 1: CẨM NANG NGHIỆP VỤ AN NINH & NỘI QUY LAO ĐỘNG (ĐỌC TRỰC TUYẾN)", font=font_sec, fill='#071A36')

cards = [
    ("🚚 QUY TRÌNH HÀNG NGÀY", "Kiểm Tra Xe 7/17 Điểm & Seal VVTT", "Quy trình gõ búa, kiểm tra 7 điểm xe tải, 17 điểm container, và 4 bước kiểm tra niêm phong Seal ISO 17712.", "qr_doc1_inspection.png"),
    ("🚨 ỨNG PHÓ KHẨN CẤP", "Sổ Tay Sự Cố Trên Đường (WI-PRT-001)", "Xử lý khi xe bị bám đuôi, hỏng xe/tai nạn dọc đường, seal bị cạy phá hoặc mất tín hiệu GPS. Hotline 24/7.", "qr_doc2_emergency.png"),
    ("🚫 AN TOÀN ĐƯỜNG BỘ", "An Toàn Giao Thông & Cấm Rượu Bia, Ma Túy", "Chính sách Zero Tolerance nồng độ cồn 0.0 mg/L, lái xe tối đa 4h liên tục, xét nghiệm 5 nhóm chất ma túy định kỳ.", "qr_doc3_safety.png"),
    ("🌱 PHÁT TRIỂN BỀN VỮNG", "Văn Phòng Xanh & Môi Trường Cơ Sở", "Tiết kiệm điện nước, in 2 mặt, phân loại rác 3 ngăn, tắt động cơ khi dừng đỗ, xử lý lốp xe và dầu nhớt thải.", "qr_doc4_green.png"),
    ("🛡️ CHÍNH SÁCH BẢO VỆ", "Bảo Vệ Người Tố Giác (HS01-08)", "Cam kết không trù dập/trả thù, bảo vệ 100% người báo cáo vi phạm an ninh, kênh tố giác ẩn danh và hotline Giám đốc.", "qr_doc5_whistleblower.png"),
    ("🤝 QUYỀN LỢI LAO ĐỘNG", "Sổ Tay Nhân Viên & Quy Tắc Ứng Xử", "Quyền lợi BHXH, làm thêm giờ tự nguyện, chống quấy rối, quy chuẩn tác phong đồng phục thẻ tên với NV Apparel.", "qr_doc6_handbook.png"),
]

start_y = 670
col_w = (W - 160 - 40) // 2 # 2 columns
row_h = 360

for idx, (tag, title, desc, qr_file) in enumerate(cards):
    r = idx // 2
    c = idx % 2
    bx = 80 + c * (col_w + 40)
    by = start_y + r * (row_h + 25)
    
    # Card background
    draw.rectangle([bx, by, bx + col_w, by + row_h], fill='#FFFFFF', outline='#CBD5E1', width=3)
    draw.rectangle([bx, by, bx + 12, by + row_h], fill='#0B3C5D')
    
    # QR code on left of card
    qr_p = os.path.join(FORMS_DIR, qr_file)
    if os.path.exists(qr_p):
        q_img = Image.open(qr_p).convert('RGBA')
        q_img.thumbnail((290, 290), Image.Resampling.LANCZOS)
        img.paste(q_img, (bx + 30, by + 35), q_img)
        draw.text((bx + 175, by + 330), "Quét mã QR", font=get_font(18, bold=True), fill='#64748B', anchor="mm")
        
    # Text on right of card
    tx = bx + 340
    draw.text((tx, by + 30), tag, font=font_tag, fill='#D4441E')
    draw.text((tx, by + 65), title, font=font_card_title, fill='#071A36')
    
    # Wrap description
    words = desc.split()
    line1, line2, line3 = "", "", ""
    for w_item in words:
        if len(line1) + len(w_item) < 36:
            line1 += w_item + " "
        elif len(line2) + len(w_item) < 36:
            line2 += w_item + " "
        else:
            line3 += w_item + " "
            
    draw.text((tx, by + 125), line1.strip(), font=font_card_desc, fill='#334155')
    draw.text((tx, by + 160), line2.strip(), font=font_card_desc, fill='#334155')
    if line3:
        draw.text((tx, by + 195), line3.strip(), font=font_card_desc, fill='#334155')

    draw.rectangle([tx, by + 280, tx + 480, by + 330], fill='#071A36')
    draw.text((tx + 240, by + 305), "ĐỌC TÀI LIỆU TRỰC TUYẾN ➔", font=get_font(18, bold=True), fill='#FFFFFF', anchor="mm")

# 4. SECTION 2: 3 ONLINE INTERACTIVE FORMS
sec2_y = start_y + 3 * (row_h + 25) + 20
draw.text((80, sec2_y), "📝 PHẦN 2: CÁC BIỂU MẪU ĐÁNH GIÁ, KHẢO SÁT & KÊNH TỐ GIÁC 24/7", font=font_sec, fill='#071A36')

form_cards = [
    ("⭐ KHẢO SÁT DỊCH VỤ", "Đánh Giá Hài Lòng CGL (CSAT)", "Dành cho khách hàng NV Apparel đánh giá định kỳ 6 tiêu chí.", "qr_form1.png"),
    ("✍️ KIỂM TRA ĐÀO TẠO", "NV CTPAT Knowledge Exam", "Bài thi trắc nghiệm 10 câu kiểm tra an ninh C-TPAT. Cấp chứng chỉ online.", "qr_form2.png"),
    ("📬 GÓP Ý & TỐ GIÁC", "NV CTPAT Suggestions & Complaints", "Kênh phản ánh sự cố an ninh & khiếu nại ẩn danh 24/7. Cấp Ticket ID.", "qr_form3.png"),
]

col3_w = (W - 160 - 40) // 3
for idx, (tag, title, desc, qr_file) in enumerate(form_cards):
    bx = 80 + idx * (col3_w + 20)
    by = sec2_y + 60
    
    draw.rectangle([bx, by, bx + col3_w, by + 460], fill='#F8FAFC', outline='#CBD5E1', width=3)
    draw.rectangle([bx, by, bx + col3_w, by + 10], fill='#D4441E')
    
    draw.text((bx + col3_w // 2, by + 35), tag, font=font_tag, fill='#D4441E', anchor="mm")
    draw.text((bx + col3_w // 2, by + 75), title, font=get_font(24, bold=True), fill='#071A36', anchor="mm")
    
    qr_p = os.path.join(FORMS_DIR, qr_file)
    if os.path.exists(qr_p):
        q_img = Image.open(qr_p).convert('RGBA')
        q_img.thumbnail((250, 250), Image.Resampling.LANCZOS)
        img.paste(q_img, (bx + (col3_w - 250) // 2, by + 115), q_img)
        
    draw.text((bx + col3_w // 2, by + 390), desc[:40], font=get_font(19, bold=False), fill='#475569', anchor="mm")
    draw.rectangle([bx + 40, by + 415, bx + col3_w - 40, by + 450], fill='#0B3C5D')
    draw.text((bx + col3_w // 2, by + 432), "MỞ BIỂU MẪU ➔", font=get_font(16, bold=True), fill='#FFFFFF', anchor="mm")

# 5. FOOTER & DIRECTOR STAMP
foot_y = H - 360
draw.rectangle([0, foot_y, W, H], fill='#F1F5F9')
draw.line([(0, foot_y), (W, foot_y)], fill='#CBD5E1', width=2)

draw.text((100, foot_y + 40), "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM", font=font_footer_bold, fill='#071A36')
draw.text((100, foot_y + 85), "Trụ sở: Lầu 6, Số 84 Bạch Đằng, Phường Tân Sơn Hòa, TP. Hồ Chí Minh  |  Mã số thuế: 0313492159", font=font_footer, fill='#334155')
draw.text((100, foot_y + 125), "Phòng Quản Lý Chất Lượng QMS & An Ninh Chuỗi Cung Ứng C-TPAT — Tiêu chuẩn áp dụng: ISO 9001 / ISO 14001 / ISO 39001", font=font_footer, fill='#64748B')
draw.text((100, foot_y + 165), "Toàn bộ tài liệu được số hóa công khai tại: https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/portal_driver.html", font=get_font(21, bold=True), fill='#D4441E')

# Director stamp on bottom right
stamp_path = os.path.join(ASSETS_DIR, "Cargolink_Director_Signature_and_Seal.png")
if os.path.exists(stamp_path):
    st_img = Image.open(stamp_path).convert('RGBA')
    st_img.thumbnail((480, 240), Image.Resampling.LANCZOS)
    img.paste(st_img, (W - 550, foot_y + 40), st_img)

img.save(PNG_OUT, format='PNG', quality=95)
print(f"[SUCCESS] Created High-Res Poster PNG: {PNG_OUT}")
