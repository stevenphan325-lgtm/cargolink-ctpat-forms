# -*- coding: utf-8 -*-
import os, sys
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026"
ASSETS_DIR = os.path.join(BASE_DIR, "00_BO_BANNER_VA_LOGO_CARGOLINK")
QR_DIR = os.path.join(BASE_DIR, "CTPAT_QR_FORMS")
ARTIFACT_DIR = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163"

FONT_PATH = "C:/Windows/Fonts/tahoma.ttf"
FONT_BOLD_PATH = "C:/Windows/Fonts/tahomabd.ttf"
if not os.path.exists(FONT_BOLD_PATH):
    FONT_BOLD_PATH = FONT_PATH

def get_font(size, bold=False):
    fp = FONT_BOLD_PATH if bold else FONT_PATH
    return ImageFont.truetype(fp, size)

def save_to_all(img, filename, subfolder):
    t1 = os.path.join(ASSETS_DIR, filename)
    t2 = os.path.join(BASE_DIR, subfolder, filename)
    t3 = os.path.join(QR_DIR, filename)
    t4 = os.path.join(ARTIFACT_DIR, filename)
    img.save(t1)
    img.save(t2)
    img.save(t3)
    img.save(t4)
    print(f"✅ Generated & Saved: {filename} in {subfolder}")

# 1. HS15-07_ANH_MAU_BAO_DUONG_XE_GARAGE.png
def make_garage_board():
    w, h = 1200, 800
    img = Image.new("RGB", (w, h), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    
    # Outer Border & Header
    draw.rectangle([10, 10, w-10, h-10], outline="#071A36", width=4)
    draw.rectangle([10, 10, w-10, 110], fill="#071A36")
    draw.text((30, 22), "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM", fill="white", font=get_font(28, bold=True))
    draw.text((30, 65), "HỒ SƠ CHỨNG MINH BẢO DƯỠNG ĐỊNH KỲ PHƯƠNG TIỆN TẠI GARAGE ĐỐI TÁC (FINDING 22)", fill="#38BDF8", font=get_font(18))
    
    # Left Box: Maintenance Voucher
    draw.rectangle([40, 140, 580, h-40], fill="white", outline="#CBD5E1", width=2)
    draw.rectangle([40, 140, 580, 190], fill="#0284C7")
    draw.text((60, 152), "PHIẾU BẢO DƯỠNG & NGHIỆM THU KỸ THUẬT XE", fill="white", font=get_font(20, bold=True))
    
    lines_l = [
        ("Garage đối tác:", "GARAGE Ô TÔ TẢI TÂN TẠO (Ký HĐ số CGL-GRG-2026)"),
        ("Biển số xe bảo dưỡng:", "50H-082.35 (Đầu kéo Hino 420HP)"),
        ("Tài xế quản lý xe:", "Bùi Minh Dũng (Điện thoại: 0908.123.456)"),
        ("Số km bảo dưỡng:", "124,500 km (Bảo dưỡng Cấp 2 định kỳ Quý 4/2026)"),
        ("Nội dung thực hiện:", "• Thay dầu nhớt động cơ Castrol Vecton 15W-40"),
        ("", "• Thay lọc nhớt, lọc nhiên liệu, vệ sinh lọc gió"),
        ("", "• Bảo dưỡng tổng thể hệ thống phanh hơi, xả e khí nén"),
        ("", "• Cân chỉnh góc đặt bánh xe, kiểm tra áp suất 10 lốp"),
        ("", "• Kiểm tra hệ thống đèn tín hiệu, cần gạt nước, còi xe"),
        ("Kết luận kỹ thuật:", "Xe đạt tiêu chuẩn an toàn kỹ thuật C-TPAT & Đăng kiểm"),
        ("Ngày nghiệm thu:", "28/10/2026 | Hạn bảo dưỡng kế tiếp: 15/01/2027")
    ]
    y_l = 210
    for label, val in lines_l:
        if label:
            draw.text((60, y_l), label, fill="#071A36", font=get_font(15, bold=True))
            draw.text((230, y_l), val, fill="#1E293B", font=get_font(15))
        else:
            draw.text((230, y_l), val, fill="#475569", font=get_font(14))
        y_l += 35
        
    # Red Stamp simulator
    cx, cy = 480, 660
    draw.ellipse([cx-55, cy-55, cx+55, cy+55], outline="#DC2626", width=3)
    draw.text((cx-45, cy-25), "GARAGE TÂN TẠO", fill="#DC2626", font=get_font(11, bold=True))
    draw.text((cx-35, cy-5), "ĐÃ KIỂM ĐỊNH", fill="#DC2626", font=get_font(12, bold=True))
    draw.text((cx-35, cy+15), "28 - 10 - 2026", fill="#DC2626", font=get_font(11))

    # Right Box: Visual Checklist & Responsible Personnel
    draw.rectangle([620, 140, w-40, h-40], fill="white", outline="#CBD5E1", width=2)
    draw.rectangle([620, 140, w-40, 190], fill="#16A34A")
    draw.text((640, 152), "BẢNG PHÂN CÔNG NHÂN SỰ & QUY CHUẨN XƯỞNG", fill="white", font=get_font(20, bold=True))
    
    right_items = [
        ("1. Cán bộ Kỹ thuật CGL (Mr. Nguyễn Duy Thành)", "Chịu trách nhiệm lập kế hoạch, duyệt phiếu sửa chữa, nghiệm thu chất lượng trước khi xe lăn bánh."),
        ("2. Đội trưởng Lái xe (Mr. Bùi Minh Dũng)", "Theo dõi số km vận hành hàng ngày, đưa xe vào xưởng đúng lịch hẹn, bàn giao và nhận lại xe."),
        ("3. Quy chuẩn An toàn Môi trường tại Xưởng", "• Có khay hứng dầu nhớt chống tràn đổ bảo vệ môi trường.\n• Dầu thải và giẻ lau dính dầu được thu gom riêng biệt.\n• Trang bị bình chữa cháy CO2 và bột ABC tại khu vực sửa xe."),
        ("4. Lưu trữ Chứng từ", "Toàn bộ hóa đơn, phiếu xuất phụ tùng và biên bản nghiệm thu được lưu trong cặp file HS15-07 tối thiểu 02 năm.")
    ]
    y_r = 210
    for title, desc in right_items:
        draw.text((640, y_r), title, fill="#071A36", font=get_font(16, bold=True))
        y_r += 28
        for d_line in desc.split('\n'):
            draw.text((660, y_r), d_line, fill="#334155", font=get_font(14))
            y_r += 24
        y_r += 14

    save_to_all(img, "HS15-07_ANH_MAU_BAO_DUONG_XE_GARAGE.png", "15. Phương tiện và bảo dưỡng")

# 2. HS10-04_ANH_MAU_SAO_KE_LUONG_NGAN_HANG.png
def make_payroll_board():
    w, h = 1200, 800
    img = Image.new("RGB", (w, h), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    
    # Outer Border & Header
    draw.rectangle([10, 10, w-10, h-10], outline="#071A36", width=4)
    draw.rectangle([10, 10, w-10, 110], fill="#071A36")
    draw.text((30, 22), "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM", fill="white", font=get_font(28, bold=True))
    draw.text((30, 65), "BẰNG CHỨNG THANH TOÁN LƯƠNG QUA NGÂN HÀNG & PHIẾU LƯƠNG LÁI XE (FINDING 10)", fill="#38BDF8", font=get_font(18))
    
    # Left: Bank Transfer Slip (Vietcombank)
    draw.rectangle([40, 140, 580, h-40], fill="white", outline="#CBD5E1", width=2)
    draw.rectangle([40, 140, 580, 190], fill="#005A36") # VCB Green
    draw.text((60, 152), "ỦY NHIỆM CHI / LỆNH CHUYỂN TIỀN VIETCOMBANK", fill="white", font=get_font(20, bold=True))
    
    vcb_data = [
        ("Số giao dịch:", "FT26308912384729  |  Ngày: 05/11/2026"),
        ("Đơn vị trả tiền:", "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM"),
        ("Số tài khoản trích nợ:", "0071001234567 tại VCB Tân Bình - TP.HCM"),
        ("Nội dung chuyển tiền:", "Chi trả tiền lương Tháng 10/2026 đội xe tải"),
        ("Tổng số tiền chuyển:", "115.800.000 VNĐ (Bằng chữ: Một trăm mười lăm triệu tám trăm nghìn đồng)"),
        ("Danh sách thụ hưởng:", "7 tài khoản lái xe (Ngân hàng Vietcombank/ACB/MB)"),
        ("Trạng thái giao dịch:", "GIAO DỊCH THÀNH CÔNG (Hạch toán ngày 05/11/2026)")
    ]
    y_v = 210
    for label, val in vcb_data:
        draw.text((60, y_v), label, fill="#071A36", font=get_font(14, bold=True))
        y_v += 24
        draw.text((60, y_v), val, fill="#005A36" if "THÀNH CÔNG" in val else "#1E293B", font=get_font(14, bold=("THÀNH CÔNG" in val)))
        y_v += 32
        
    # VCB Stamp
    cx, cy = 480, 660
    draw.ellipse([cx-55, cy-55, cx+55, cy+55], outline="#DC2626", width=3)
    draw.text((cx-48, cy-25), "VIETCOMBANK", fill="#DC2626", font=get_font(12, bold=True))
    draw.text((cx-40, cy-5), "ĐÃ THANH TOÁN", fill="#DC2626", font=get_font(11, bold=True))
    draw.text((cx-35, cy+15), "05 - 11 - 2026", fill="#DC2626", font=get_font(11))

    # Right: Payroll summary & driver confirmation
    draw.rectangle([620, 140, w-40, h-40], fill="white", outline="#CBD5E1", width=2)
    draw.rectangle([620, 140, w-40, 190], fill="#071A36")
    draw.text((640, 152), "BẢNG KÝ NHẬN PHIẾU LƯƠNG TÀI XẾ (THÁNG 10/2026)", fill="white", font=get_font(20, bold=True))
    
    # Table header
    draw.rectangle([640, 205, w-60, 240], fill="#F1F5F9")
    draw.text((650, 215), "Họ tên Lái xe", fill="#071A36", font=get_font(13, bold=True))
    draw.text((800, 215), "Biển số xe", fill="#071A36", font=get_font(13, bold=True))
    draw.text((910, 215), "Thực lĩnh (VNĐ)", fill="#071A36", font=get_font(13, bold=True))
    draw.text((1040, 215), "Ký nhận", fill="#071A36", font=get_font(13, bold=True))
    
    drivers = [
        ("Bùi Minh Dũng", "50H-082.35", "17.200.000", "Dũng (Đã ký)"),
        ("Nguyễn Văn Hùng", "51C-964.55", "16.500.000", "Hùng (Đã ký)"),
        ("Lê Văn Tùng", "50H-112.89", "16.800.000", "Tùng (Đã ký)"),
        ("Trần Quốc Bảo", "51D-452.18", "15.900.000", "Bảo (Đã ký)"),
        ("Phạm Văn Công", "50H-334.72", "16.400.000", "Công (Đã ký)"),
        ("Võ Thành Nhân", "51C-882.14", "16.100.000", "Nhân (Đã ký)"),
        ("Nguyễn Duy Thành", "50H-918.23", "16.900.000", "Thành (Đã ký)")
    ]
    y_d = 250
    for name, plate, salary, sig in drivers:
        draw.line([(640, y_d-5), (w-60, y_d-5)], fill="#E2E8F0", width=1)
        draw.text((650, y_d), name, fill="#0F172A", font=get_font(13, bold=True))
        draw.text((800, y_d), plate, fill="#475569", font=get_font(13))
        draw.text((910, y_d), salary, fill="#15803D", font=get_font(13, bold=True))
        draw.text((1040, y_d), sig, fill="#0284C7", font=get_font(13, bold=True))
        y_d += 38
        
    draw.rectangle([640, y_d+10, w-60, h-60], fill="#EFF6FF", outline="#93C5FD", width=1)
    draw.text((650, y_d+20), "Kế toán trưởng: Trần Thị Mai Phương | Giám đốc: Nguyễn Tất Thắng", fill="#1E40AF", font=get_font(13, bold=True))
    draw.text((650, y_d+45), "Chứng từ lưu trữ: Cặp còng HS10-04 | Đạt chuẩn Trách nhiệm xã hội ISO/CSR", fill="#475569", font=get_font(12))

    save_to_all(img, "HS10-04_ANH_MAU_SAO_KE_LUONG_NGAN_HANG.png", "10. Tiền lương và làm thêm")

# 3. HS14-01_ANH_MAU_NHA_VE_SINH_NAM_NU_DAT_CHUAN.png
def make_restroom_board():
    w, h = 1200, 800
    img = Image.new("RGB", (w, h), color="#F8FAFC")
    draw = ImageDraw.Draw(img)
    
    # Outer Border & Header
    draw.rectangle([10, 10, w-10, h-10], outline="#071A36", width=4)
    draw.rectangle([10, 10, w-10, 110], fill="#071A36")
    draw.text((30, 22), "CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM", fill="white", font=get_font(28, bold=True))
    draw.text((30, 65), "HỒ SƠ KHU VỆ SINH PHÚC LỢI NAM - NỮ ĐẠT CHUẨN AN TOÀN & ISO (SHEET 14.40 - 14.45)", fill="#38BDF8", font=get_font(18))
    
    # 2 Big Cards: Male & Female Restroom specs
    # Left: Male Restroom
    draw.rectangle([40, 140, 580, 560], fill="white", outline="#3B82F6", width=3)
    draw.rectangle([40, 140, 580, 190], fill="#1E40AF")
    draw.text((60, 152), "🚹 KHU VỆ SINH NAM (MALE RESTROOM)", fill="white", font=get_font(20, bold=True))
    
    specs_male = [
        "• Biển báo Nam có biểu tượng quốc tế rõ ràng gắn tại cửa.",
        "• Cửa phòng và vách ngăn kín từ sàn đến trần đảm bảo riêng tư.",
        "• Bồn tiểu nam có hệ thống van xả nước tự động/gạt nước mạnh.",
        "• Đường thoát sàn có phễu ngăn mùi, lưới chắn chuột & côn trùng.",
        "• Bồn rửa tay có gương, xà phòng rửa tay diệt khuẩn Lifebuoy.",
        "• Thùng rác có nắp đậy đạp chân bằng inox, có lót túi nilon.",
        "• Thông gió tự nhiên và quạt hút gió hoạt động liên tục."
    ]
    y_m = 215
    for s in specs_male:
        draw.text((60, y_m), s, fill="#1E293B", font=get_font(14))
        y_m += 42
        
    # Right: Female Restroom
    draw.rectangle([620, 140, w-40, 560], fill="white", outline="#EC4899", width=3)
    draw.rectangle([620, 140, w-40, 190], fill="#BE185D")
    draw.text((640, 152), "🚺 KHU VỆ SINH NỮ (FEMALE RESTROOM)", fill="white", font=get_font(20, bold=True))
    
    specs_female = [
        "• Biển báo Nữ có biểu tượng quốc tế nổi bật gắn tại cửa.",
        "• Tách biệt hoàn toàn với phòng nam bằng tường gạch kiên cố.",
        "• Buồng vệ sinh khép kín có chốt khóa an toàn bên trong.",
        "• Đầy đủ giấy vệ sinh sạch và vòi xịt vệ sinh áp lực chuẩn.",
        "• Hộp khăn giấy lau tay khô và máy sấy tay tự động.",
        "• Thùng rác chuyên dụng có nắp đậy kín thu gom rác hàng ngày.",
        "• Đèn chiếu sáng LED đủ lux, gương soi toàn thân sáng bóng."
    ]
    y_f = 215
    for s in specs_female:
        draw.text((640, y_f), s, fill="#1E293B", font=get_font(14))
        y_f += 42
        
    # Bottom: Cleaning Logbook & Compliance Banner
    draw.rectangle([40, 590, w-40, h-40], fill="#F0FDF4", outline="#86EFAC", width=2)
    draw.text((60, 610), "NHẬT KÝ VỆ SINH & KHỬ TRÙNG HÀNG NGÀY (DAILY HYGIENE CHECKLIST)", fill="#166534", font=get_font(18, bold=True))
    draw.text((60, 645), "• Tần suất vệ sinh: 02 lần/ngày (07:30 sáng và 13:30 chiều) do nhân viên tạp vụ thực hiện và ký sổ theo dõi.", fill="#334155", font=get_font(14))
    draw.text((60, 675), "• Giám sát kiểm tra: Cán bộ An toàn (Mr. Thành) phúc tra hàng ngày | Không gian sạch sẽ, không mùi, sàn khô ráo chống trơn trượt.", fill="#334155", font=get_font(14))
    draw.text((60, 715), "TUÂN THỦ 100% TIÊU CHUẨN C-TPAT SHEET 14 (14.40 - 14.45) & AN TOÀN LAO ĐỘNG ISO", fill="#15803D", font=get_font(14, bold=True))

    save_to_all(img, "HS14-01_ANH_MAU_NHA_VE_SINH_NAM_NU_DAT_CHUAN.png", "14. An toàn cơ sở và công việc")

if __name__ == "__main__":
    print("--- GENERATING REMAINING EVIDENCE BOARDS ---")
    make_garage_board()
    make_payroll_board()
    make_restroom_board()
    print("--- ALL REMAINING BOARDS GENERATED SUCCESSFULLY ---")
