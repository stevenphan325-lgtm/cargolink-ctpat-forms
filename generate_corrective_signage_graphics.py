# -*- coding: utf-8 -*-
import os, sys
import qrcode
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026"
ASSETS_DIR = os.path.join(BASE_DIR, "00_BO_BANNER_VA_LOGO_CARGOLINK")
ARTIFACT_DIR = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163"

FONT_PATH = "C:/Windows/Fonts/tahoma.ttf"
FONT_BOLD_PATH = "C:/Windows/Fonts/tahomabd.ttf"
if not os.path.exists(FONT_BOLD_PATH):
    FONT_BOLD_PATH = FONT_PATH

def get_font(size, bold=False):
    fp = FONT_BOLD_PATH if bold else FONT_PATH
    return ImageFont.truetype(fp, size)

# -------------------------------------------------------------
# 1. EXIT SIGN (ENGLISH + THAI + VIETNAMESE)
# -------------------------------------------------------------
def make_exit_sign():
    # Green ISO 7010 background #008751
    w, h = 1200, 500
    img = Image.new("RGB", (w, h), color="#008751")
    draw = ImageDraw.Draw(img)
    
    # White border
    draw.rectangle([15, 15, w-15, h-15], outline="white", width=6)
    
    # Running man / Door icon representation
    # Draw simple door + running man
    draw.rectangle([60, 80, 200, 420], outline="white", width=8) # Door frame
    # Running man head
    draw.ellipse([140, 110, 180, 150], fill="white")
    # Torso
    draw.line([(160, 150), (130, 260)], fill="white", width=14)
    # Arms
    draw.line([(150, 180), (110, 210)], fill="white", width=10)
    draw.line([(150, 180), (190, 220)], fill="white", width=10)
    # Legs
    draw.line([(130, 260), (100, 370)], fill="white", width=12)
    draw.line([(130, 260), (170, 320), (210, 360)], fill="white", width=12)
    
    # Right arrow
    arrow_pts = [(230, 250), (280, 200), (280, 230), (330, 230), (330, 270), (280, 270), (280, 300)]
    draw.polygon(arrow_pts, fill="white")
    
    # Text: EXIT / ทางออก / LỐI THOÁT
    f_en = get_font(130, bold=True)
    f_th = get_font(95, bold=True)
    f_vn = get_font(50, bold=False)
    
    draw.text((370, 60), "EXIT", fill="white", font=f_en)
    draw.text((370, 210), "ทางออก", fill="white", font=f_th)
    draw.text((375, 360), "LỐI THOÁT HIỂM  |  CARGOLINK EXPRESS", fill="#E2E8F0", font=f_vn)
    
    # Save
    out1 = os.path.join(BASE_DIR, "14. An toàn cơ sở và công việc", "HS14-08_EXIT_SIGN_ENGLISH_THAI.png")
    out2 = os.path.join(ASSETS_DIR, "HS14-08_EXIT_SIGN_ENGLISH_THAI.png")
    out3 = os.path.join(ARTIFACT_DIR, "HS14-08_EXIT_SIGN_ENGLISH_THAI.png")
    img.save(out1)
    img.save(out2)
    img.save(out3)
    print(f"[Exit Sign] Created: {out1}")

# -------------------------------------------------------------
# 2. ASSEMBLY POINT SIGN (ENGLISH + THAI + VIETNAMESE)
# -------------------------------------------------------------
def make_assembly_sign():
    # Green ISO 7010 background #008751
    w, h = 1000, 1100
    img = Image.new("RGB", (w, h), color="#008751")
    draw = ImageDraw.Draw(img)
    
    # White border
    draw.rectangle([20, 20, w-20, h-20], outline="white", width=8)
    
    # Assembly symbol in a white box or directly
    box_w = 400
    box_x = (w - box_w) // 2
    box_y = 70
    draw.rectangle([box_x, box_y, box_x + box_w, box_y + box_w], outline="white", width=6)
    
    # Arrows pointing to center from 4 corners
    # Top-Left arrow
    draw.polygon([(box_x+30, box_y+30), (box_x+90, box_y+50), (box_x+50, box_y+90)], fill="white")
    # Top-Right arrow
    draw.polygon([(box_x+box_w-30, box_y+30), (box_x+box_w-90, box_y+50), (box_x+box_w-50, box_y+90)], fill="white")
    # Bottom-Left arrow
    draw.polygon([(box_x+30, box_y+box_w-30), (box_x+90, box_y+box_w-50), (box_x+50, box_y+box_w-90)], fill="white")
    # Bottom-Right arrow
    draw.polygon([(box_x+box_w-30, box_y+box_w-30), (box_x+box_w-90, box_y+box_w-50), (box_x+box_w-50, box_y+box_w-90)], fill="white")
    
    # Center people (3 figures)
    # Figure center
    draw.ellipse([(box_x+180, box_y+130), (box_x+220, box_y+170)], fill="white")
    draw.line([(box_x+200, box_y+170), (box_x+200, box_y+250)], fill="white", width=12)
    # Figure left
    draw.ellipse([(box_x+130, box_y+160), (box_x+165, box_y+195)], fill="white")
    draw.line([(box_x+147, box_y+195), (box_x+147, box_y+265)], fill="white", width=10)
    # Figure right
    draw.ellipse([(box_x+235, box_y+160), (box_x+270, box_y+195)], fill="white")
    draw.line([(box_x+252, box_y+195), (box_x+252, box_y+265)], fill="white", width=10)
    
    # Text English
    f_title = get_font(72, bold=True)
    f_thai = get_font(90, bold=True)
    f_vn = get_font(52, bold=True)
    f_sub = get_font(34, bold=False)
    
    # Center-align text
    def draw_centered_text(y, text, font, fill="white"):
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((w - tw)//2, y), text, fill=fill, font=font)
        
    draw_centered_text(520, "ASSEMBLY POINT", f_title)
    draw_centered_text(630, "จุดรวมพล", f_thai)
    draw_centered_text(770, "ĐIỂM TẬP KẾT SƠ TÁN", f_vn)
    draw_centered_text(870, "BÃI XE CARGOLINK EXPRESS - 12/8 QL1A, BÌNH HƯNG HÒA B", f_sub, fill="#F1F5F9")
    draw_centered_text(930, "TUÂN THỦ QUY CHUẨN AN TOÀN C-TPAT & PCCC 2026", f_sub, fill="#E2E8F0")
    
    out1 = os.path.join(BASE_DIR, "14. An toàn cơ sở và công việc", "HS14-08_ASSEMBLY_POINT_SIGN_ENGLISH_THAI.png")
    out2 = os.path.join(ASSETS_DIR, "HS14-08_ASSEMBLY_POINT_SIGN_ENGLISH_THAI.png")
    out3 = os.path.join(ARTIFACT_DIR, "HS14-08_ASSEMBLY_POINT_SIGN_ENGLISH_THAI.png")
    img.save(out1)
    img.save(out2)
    img.save(out3)
    print(f"[Assembly Point Sign] Created: {out1}")

# -------------------------------------------------------------
# 3. NO SMOKING SIGN (ENGLISH + THAI + VIETNAMESE)
# -------------------------------------------------------------
def make_no_smoking_sign():
    w, h = 900, 1000
    img = Image.new("RGB", (w, h), color="white")
    draw = ImageDraw.Draw(img)
    
    # Border
    draw.rectangle([15, 15, w-15, h-15], outline="#CBD5E1", width=4)
    
    # Red circle with slash
    cx, cy, r = 450, 260, 180
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline="#DC2626", width=28)
    
    # Cigarette inside
    # cigarette body
    draw.rectangle([cx-100, cy-15, cx+90, cy+15], fill="#334155")
    # cigarette filter
    draw.rectangle([cx-120, cy-15, cx-85, cy+15], fill="#EA580C")
    # smoke lines
    draw.arc([cx+95, cy-45, cx+135, cy+15], 270, 90, fill="#94A3B8", width=6)
    draw.arc([cx+115, cy-75, cx+155, cy-15], 90, 270, fill="#94A3B8", width=6)
    
    # Red slash across
    draw.line([cx - 127, cy - 127, cx + 127, cy + 127], fill="#DC2626", width=28)
    
    # Texts
    f_en = get_font(76, bold=True)
    f_th = get_font(85, bold=True)
    f_vn = get_font(52, bold=True)
    f_note = get_font(28, bold=False)
    
    def draw_centered_text(y, text, font, fill="#0F172A"):
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((w - tw)//2, y), text, fill=fill, font=font)
        
    draw_centered_text(500, "NO SMOKING", f_en, fill="#DC2626")
    draw_centered_text(600, "ห้ามสูบบุหรี่", f_th, fill="#DC2626")
    draw_centered_text(730, "CẤM HÚT THUỐC LÁ", f_vn, fill="#0F172A")
    draw_centered_text(810, "Áp dụng trong toàn bộ Cabin xe tải, Văn phòng và Bãi xe CGL", f_note, fill="#475569")
    draw_centered_text(850, "Khu vực hút thuốc riêng biệt đặt cách xa tối thiểu 15 mét", f_note, fill="#475569")
    draw_centered_text(910, "CARGOLINK EXPRESS VIETNAM - C-TPAT COMPLIANCE", f_note, fill="#071A36")
    
    out1 = os.path.join(BASE_DIR, "14. An toàn cơ sở và công việc", "HS14-08_NO_SMOKING_SIGN_ENGLISH_THAI.png")
    out2 = os.path.join(ASSETS_DIR, "HS14-08_NO_SMOKING_SIGN_ENGLISH_THAI.png")
    out3 = os.path.join(ARTIFACT_DIR, "HS14-08_NO_SMOKING_SIGN_ENGLISH_THAI.png")
    img.save(out1)
    img.save(out2)
    img.save(out3)
    print(f"[No Smoking Sign] Created: {out1}")

# -------------------------------------------------------------
# 4. EMERGENCY HOTLINE STICKER (CABIN TRUCK & YARD)
# -------------------------------------------------------------
def make_hotline_sticker():
    w, h = 1200, 750
    img = Image.new("RGB", (w, h), color="white")
    draw = ImageDraw.Draw(img)
    
    # Outer border & header banner
    draw.rectangle([10, 10, w-10, h-10], outline="#D4441E", width=8)
    draw.rectangle([10, 10, w-10, 140], fill="#071A36")
    
    # Header text
    f_h1 = get_font(42, bold=True)
    f_h2 = get_font(26, bold=False)
    
    draw.text((30, 25), "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM", fill="white", font=f_h1)
    draw.text((30, 85), "ĐƯỜNG DÂY NÓNG KHẨN CẤP & BÁO CÁO SỰ CỐ C-TPAT (EMERGENCY HOTLINE)", fill="#F97316", font=f_h2)
    
    # 2-column contact cards
    cards = [
        ("ĐIỀU ĐỘ VẬN HÀNH (DISPATCH 24/7)", "Ms. Lưu Thị Ngọc Bích (Trưởng phòng Điều độ)", "077 871 9936", "#EFF6FF", "#1E40AF"),
        ("AN TOÀN C-TPAT & KỸ THUẬT XE", "Mr. Phan Công Thành (Trưởng ban An toàn)", "088 6464 988", "#FEF2F2", "#DC2626"),
        ("KHẨN CẤP 24/7/365 & BAN GIÁM ĐỐC", "Mr. Nguyễn Tất Thắng (Giám đốc)", "0943 46 46 46", "#FEFCE8", "#B45309"),
        ("CƠ QUAN CHỨC NĂNG KHẨN CẤP", "Cảnh sát phản ứng nhanh / PCCC / Cấp cứu y tế", "113  |  114  |  115", "#F0FDF4", "#15803D")
    ]
    
    f_card_title = get_font(25, bold=True)
    f_card_name = get_font(22, bold=False)
    f_card_phone = get_font(38, bold=True)
    
    positions = [
        (40, 160, 580, 260),
        (620, 160, 540, 260),
        (40, 440, 580, 260),
        (620, 440, 540, 260)
    ]
    
    for (title, name, phone, bg, text_col), (x, y, cw, ch) in zip(cards, positions):
        draw.rectangle([x, y, x+cw, y+ch], fill=bg, outline="#CBD5E1", width=3)
        draw.rectangle([x, y, x+cw, y+45], fill=text_col)
        draw.text((x+15, y+8), title, fill="white", font=f_card_title)
        draw.text((x+20, y+70), name, fill="#334155", font=f_card_name)
        draw.text((x+20, y+130), phone, fill=text_col, font=f_card_phone)
        draw.text((x+20, y+205), "Gọi ngay khi hỏng xe, va chạm hoặc đứt seal niêm phong", fill="#64748B", font=get_font(18))
        
    out1 = os.path.join(BASE_DIR, "18. Chậm trễ và sự cố", "HS18-06_EMERGENCY_HOTLINE_STICKER.png")
    out2 = os.path.join(ASSETS_DIR, "HS18-06_EMERGENCY_HOTLINE_STICKER.png")
    out3 = os.path.join(ARTIFACT_DIR, "HS18-06_EMERGENCY_HOTLINE_STICKER.png")
    img.save(out1)
    img.save(out2)
    img.save(out3)
    print(f"[Hotline Sticker] Created: {out1}")

# -------------------------------------------------------------
# 5. DECAL 3 QR CODES FOR TRUCK (FINDING 24)
# -------------------------------------------------------------
def make_3_qr_decal():
    w, h = 1200, 600
    img = Image.new("RGB", (w, h), color="white")
    draw = ImageDraw.Draw(img)
    
    # Outer frame
    draw.rectangle([10, 10, w-10, h-10], outline="#071A36", width=6)
    # Header
    draw.rectangle([10, 10, w-10, 110], fill="#071A36")
    draw.text((30, 25), "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM", fill="white", font=get_font(32, bold=True))
    draw.text((30, 68), "HỆ THỐNG MÃ QR ĐIỆN TỬ DÀNH RIÊNG CHO ĐỘI NGŨ LÁI XE & KHÁCH HÀNG (TRUCK CABIN QR CODES)", fill="#38BDF8", font=get_font(20))
    
    # 3 QR codes definitions
    # QR 1: Knowledge survey
    qr1_url = "https://thangcargolink.github.io/cargolink-ctpat-portal/form1_training.html"
    # QR 2: Driver Complaints & Suggestions (Google Form official)
    qr2_url = "https://docs.google.com/forms/d/1WDy9kSA-TzIavBlsSNgcMvU4Wcm0p8yomeZPZ-HgOzo/preview"
    # QR 3: Driver Portal (Vehicle Inspection 17 points)
    qr3_url = "https://thangcargolink.github.io/cargolink-ctpat-portal/portal_driver.html"
    
    items = [
        ("✍️ ĐÀO TẠO & KHẢO SÁT C-TPAT", "CTPAT Training & Knowledge Survey\n(Cập nhật kiến thức định kỳ)", qr1_url, "#0284C7"),
        ("📬 GÓP Ý & TỐ GIÁC BẢO MẬT", "Grievance, Suggestions & Complaints\n(Google Form bảo mật 100%)", qr2_url, "#DC2626"),
        ("🚚 SỔ TAY TÀI XẾ & KIỂM TRA XE", "7-17 Point Vehicle Inspection\n(Kiểm tra an ninh trước chuyến đi)", qr3_url, "#16A34A")
    ]
    
    col_w = 360
    for idx, (title, sub, url, col) in enumerate(items):
        x = 40 + idx * 380
        # Draw column card
        draw.rectangle([x, 130, x+col_w, h-30], fill="#F8FAFC", outline=col, width=3)
        draw.rectangle([x, 130, x+col_w, 185], fill=col)
        
        # Title
        draw.text((x+15, 142), title, fill="white", font=get_font(18, bold=True))
        
        # Generate QR image
        qr = qrcode.QRCode(box_size=6, border=2)
        qr.add_data(url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        qr_img = qr_img.resize((200, 200))
        img.paste(qr_img, (x + (col_w-200)//2, 205))
        
        # Subtext
        lines = sub.split('\n')
        draw.text((x+15, 430), lines[0], fill="#0F172A", font=get_font(16, bold=True))
        if len(lines) > 1:
            draw.text((x+15, 460), lines[1], fill="#64748B", font=get_font(14))
        draw.text((x+15, 510), "Quét bằng Camera điện thoại", fill=col, font=get_font(15, bold=True))
        
    out1 = os.path.join(BASE_DIR, "21. Phản hồi và cải tiến dịch vụ", "HS21-03_DECAL_3_QR_CODE_DAN_CABIN_XE.png")
    out2 = os.path.join(ASSETS_DIR, "HS21-03_DECAL_3_QR_CODE_DAN_CABIN_XE.png")
    out3 = os.path.join(ARTIFACT_DIR, "HS21-03_DECAL_3_QR_CODE_DAN_CABIN_XE.png")
    img.save(out1)
    img.save(out2)
    img.save(out3)
    print(f"[3-QR Decal] Created: {out1}")

if __name__ == "__main__":
    print("--- GENERATING SIGNAGE & DECALS GRAPHICS ---")
    make_exit_sign()
    make_assembly_sign()
    make_no_smoking_sign()
    make_hotline_sticker()
    make_3_qr_decal()
    print("--- ALL GRAPHICS GENERATED SUCCESSFULLY ---")
