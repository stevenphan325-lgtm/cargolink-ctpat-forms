import os, sys
import docx
from docx.shared import Inches, Pt, RGBColor
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026"
FORMS_DIR = os.path.join(BASE_DIR, "CTPAT_QR_FORMS")
ASSETS_DIR = os.path.join(BASE_DIR, "00_BO_BANNER_VA_LOGO_CARGOLINK")

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/1WDy9kSA-TzIavBlsSNgcMvU4Wcm0p8yomeZPZ-HgOzo/viewform"

# ==================== 1. UPDATE HS12-03 DOCX ====================
docx_12_03 = os.path.join(BASE_DIR, "12. Khiếu nại và phản hồi", "HS12-03 - Poster mã QR góp ý khiếu nại và khảo sát an ninh C-TPAT.docx")
if os.path.exists(docx_12_03):
    doc = docx.Document(docx_12_03)
    # Update Table 1 instructions
    for row in doc.tables[1].rows:
        for cell in row.cells:
            if "https://stevenphan325-lgtm.github.io" in cell.text:
                for p in cell.paragraphs:
                    if "https://stevenphan325-lgtm.github.io" in p.text:
                        p.text = f"4. Hoặc truy cập trực tiếp biểu mẫu Google Form chính thức: {GOOGLE_FORM_URL}"
                        p.runs[0].font.name = "Times New Roman"
                        p.runs[0].font.size = Pt(8.5)
                        p.runs[0].font.color.rgb = RGBColor(212, 68, 30)
            # Re-insert QR image
            if "QUÉT MÃ" in cell.text:
                # cell paragraphs
                for p in cell.paragraphs:
                    p.clear()
                p = cell.paragraphs[0]
                p.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
                r_img = p.add_run()
                r_img.add_picture(os.path.join(FORMS_DIR, "qr_form3.png"), width=Inches(1.8))
                r_t = p.add_run("\nQUÉT MÃ MỞ GOOGLE FORM\n(SCAN FOR OFFICIAL GOOGLE FORM)")
                r_t.bold = True
                r_t.font.name = "Times New Roman"
                r_t.font.size = Pt(8.5)
                r_t.font.color.rgb = RGBColor(7, 26, 54)
    doc.save(docx_12_03)
    print("SUCCESS: Updated HS12-03.docx with Google Form link and QR")

# ==================== 2. UPDATE HS21-01 DOCX ====================
docx_21_01 = os.path.join(BASE_DIR, "21. Phản hồi và cải tiến dịch vụ", "HS21-01 - Poster mã QR phiếu đánh giá mức độ hài lòng dịch vụ Cargolink.docx")
if os.path.exists(docx_21_01):
    doc = docx.Document(docx_21_01)
    for p in doc.paragraphs:
        if "06 tháng/lần" in p.text:
            p.text = "• Chu kỳ khảo sát: Định kỳ mỗi 03 tháng (Quarterly - Every 3 months) hoặc đột xuất sau các đợt cao điểm giao hàng."
        if "Đối tượng tham gia:" in p.text:
            p.text = "• Đối tượng tham gia: Đại diện 4 Bộ phận trọng yếu: Logistics, Scan, Store (Kho), Security (An ninh) của Nhà máy NV Apparel."
        if "C-TPAT Customer Satisfaction" in p.text:
            p.text = p.text.replace("C-TPAT Customer Satisfaction", "Transportation Service Satisfaction")
    doc.save(docx_21_01)
    print("SUCCESS: Updated HS21-01.docx with 3-month cycle and 4 departments")

# ==================== 3. RE-GENERATE HS12-03 POSTER PNG ====================
png_12_03 = os.path.join(BASE_DIR, "12. Khiếu nại và phản hồi", "HS12-03 - Poster mã QR góp ý khiếu nại và khảo sát an ninh C-TPAT.png")
W, H = 2480, 3508
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

def get_font(size, bold=False):
    for fn in ["timesbd.ttf" if bold else "times.ttf", "arialbd.ttf" if bold else "arial.ttf"]:
        try:
            return ImageFont.truetype(fn, size)
        except Exception:
            continue
    return ImageFont.load_default()

# Header
draw.rectangle([0, 0, W, 420], fill='#071A36')
draw.rectangle([0, 420, W, 435], fill='#D4441E')

logo_path = os.path.join(ASSETS_DIR, "Cargolink_Logo_Vector_HighRes.png")
if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert('RGBA')
    logo.thumbnail((450, 150), Image.Resampling.LANCZOS)
    img.paste(logo, (80, 80), logo)

draw.text((580, 75), "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM", font=get_font(34, bold=True), fill='#FFFFFF')
draw.text((580, 130), "HỆ THỐNG AN NINH CHUỖI CUNG ỨNG C-TPAT & QUẢN LÝ CHẤT LƯỢNG ISO 9001:2015", font=get_font(24, bold=False), fill='#CBD5E1')

draw.text((W // 2, 235), "HỘP THƯ GÓP Ý VÀ KHIẾU NẠI AN NINH C-TPAT", font=get_font(52, bold=True), fill='#FFFFFF', anchor="mm")
draw.text((W // 2, 310), "NV CTPAT – SUGGESTIONS AND COMPLAINTS (OFFICIAL GOOGLE FORMS)", font=get_font(32, bold=False), fill='#FCD34D', anchor="mm")
draw.text((W // 2, 365), "Biểu mẫu tiếp nhận chính thức của Khách hàng NV APPAREL — Bảo mật 100% — Hỗ trợ ẩn danh", font=get_font(22, bold=False), fill='#E2E8F0', anchor="mm")

# Big QR in Center
qr_center = os.path.join(FORMS_DIR, "qr_form3.png")
if os.path.exists(qr_center):
    q_img = Image.open(qr_center).convert('RGBA')
    q_img = q_img.resize((1050, 1050), Image.Resampling.LANCZOS)
    img.paste(q_img, ((W - 1050) // 2, 540), q_img)

draw.text((W // 2, 1640), "QUÉT MÃ QR BẰNG CAMERA ĐIỆN THOẠI / ZALO ĐỂ MỞ GOOGLE FORM", font=get_font(36, bold=True), fill='#071A36', anchor="mm")
draw.text((W // 2, 1700), f"Đường dẫn trực tiếp: {GOOGLE_FORM_URL}", font=get_font(24, bold=False), fill='#D4441E', anchor="mm")

# Content Box
draw.rectangle([120, 1780, W - 120, 2750], fill='#F8FAFC', outline='#CBD5E1', width=3)
draw.text((160, 1820), "📋 NỘI DUNG TIẾP NHẬN & CAM KẾT XỬ LÝ SỰ CỐ / COMPLIANCE COMMITMENT", font=get_font(32, bold=True), fill='#071A36')

lines = [
    "1. Mục đích: Tiếp nhận ý kiến đóng góp, khiếu nại chất lượng dịch vụ vận chuyển và phản ánh sự cố an ninh C-TPAT.",
    "2. Đối tượng tham gia: Khách hàng NV Apparel, các Bộ phận: Logistics, Scan, Store (Kho), Security (An ninh), và đối tác liên quan.",
    "3. Cam kết bảo vệ người tố giác (HS01-08): Bảo mật tuyệt đối 100% danh tính, không trả thù, không trù dập người phản ánh.",
    "4. Tùy chọn gửi ẩn danh: Người gửi có thể chọn không để lại thông tin cá nhân trên Google Form.",
    "5. Thời gian phản hồi cam kết: Xử lý sự cố an ninh C-TPAT trong vòng 2 giờ; phản ánh dịch vụ thông thường trong vòng 24 giờ."
]
y_cur = 1900
for l in lines:
    draw.text((160, y_cur), l, font=get_font(26, bold=False), fill='#334155')
    y_cur += 80

# Emergency Hotlines
draw.rectangle([120, 2800, W - 120, 3050], fill='#FEF2F2', outline='#DC2626', width=3)
draw.text((160, 2830), "🚨 ĐƯỜNG DÂY NÓNG KHẨN CẤP AN NINH 24/7 (24/7 EMERGENCY HOTLINES):", font=get_font(28, bold=True), fill='#991B1B')
draw.text((160, 2890), "• Ban Giám Đốc CGL: 0943 46 46 46   |   • Trưởng ban An toàn (Mr. Thành): 088 6464 988", font=get_font(26, bold=True), fill='#DC2626')
draw.text((160, 2960), "• Điều độ trực ban (Ms. Bích): 077 871 9936   |   • An ninh NV Apparel: Báo ngay Phòng Bảo vệ cổng", font=get_font(24, bold=False), fill='#475569')

# Footer
foot_y = H - 360
draw.rectangle([0, foot_y, W, H], fill='#F1F5F9')
draw.line([(0, foot_y), (W, foot_y)], fill='#CBD5E1', width=2)

draw.text((100, foot_y + 40), "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM", font=get_font(26, bold=True), fill='#071A36')
draw.text((100, foot_y + 85), "Trụ sở: Lầu 6, Số 84 Bạch Đằng, Phường Tân Sơn Hòa, TP. Hồ Chí Minh  |  Mã số thuế: 0313492159", font=get_font(22, bold=False), fill='#334155')
draw.text((100, foot_y + 125), "Chương trình An ninh chuỗi cung ứng C-TPAT hợp tác cùng Khách hàng CÔNG TY TNHH NV APPAREL", font=get_font(22, bold=False), fill='#64748B')
draw.text((100, foot_y + 165), f"Biểu mẫu Google Form: {GOOGLE_FORM_URL}", font=get_font(21, bold=True), fill='#D4441E')

stamp_path = os.path.join(ASSETS_DIR, "Cargolink_Director_Signature_and_Seal.png")
if os.path.exists(stamp_path):
    st_img = Image.open(stamp_path).convert('RGBA')
    st_img.thumbnail((480, 240), Image.Resampling.LANCZOS)
    img.paste(st_img, (W - 550, foot_y + 40), st_img)

img.save(png_12_03, format='PNG', quality=95)
print(f"SUCCESS: Generated High-Res Poster PNG: {png_12_03}")
