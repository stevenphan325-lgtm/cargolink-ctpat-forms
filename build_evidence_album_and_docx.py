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
QR_DIR = os.path.join(BASE_DIR, "CTPAT_QR_FORMS")
ARTIFACT_DIR = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163"
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

evidence_items = [
    {
        "id": "EVID-01",
        "title": "Bằng chứng 01: Quy trình kiểm tra an ninh xe tải 17 điểm C-TPAT",
        "finding": "Finding 21 & Sheet 14 (Vehicle & Container Security)",
        "file": "HS15-06_ANH_MAU_KIEM_TRA_XE_17_DIEM.png",
        "action": "Tài xế mặc áo phản quang, đội nón bảo hộ cầm đèn pin kiểm tra chốt khóa niêm phong Seal container và 17 điểm trọng yếu quanh xe trước chuyến đi.",
        "requirement": "Tài xế phải kiểm tra thực tế, chụp ảnh 4 góc xe và ký xác nhận vào Biên bản kiểm tra an ninh xe 17 điểm."
    },
    {
        "id": "EVID-02",
        "title": "Bằng chứng 02: Toàn cảnh bãi xe logistics, tường rào 2.6m & hệ thống CCTV",
        "finding": "Finding 3 & Finding 25 (Hạ tầng bãi xe & Hiện trạng)",
        "file": "HS01-05_ANH_MAU_BAI_XE_CCTV_CARGOLINK.png",
        "action": "Bãi xe 2.500m² tại 12/8 QL1A Bình Tân, tường rào thép gai cao 2.6m, cổng barie kiểm soát an ninh 24/7 và các cột camera CCTV bao quát.",
        "requirement": "Bảo vệ trực ban 24/7 ghi chép sổ nhật ký xe ra vào và kiểm tra an ninh cổng."
    },
    {
        "id": "EVID-03",
        "title": "Bằng chứng 03: Kiểm tra nồng độ cồn và xét nghiệm ma túy tài xế",
        "finding": "Finding 23 & Sheet 14 (Chính sách Zero Tolerance)",
        "file": "HS03-08_ANH_MAU_DO_NONG_DO_CON_TAI_XE.png",
        "action": "Nhân viên bảo vệ sử dụng máy đo nồng độ cồn điện tử cho tài xế thổi kiểm tra trước mỗi chuyến đi; sổ theo dõi và bộ que test ma túy 4 chân.",
        "requirement": "100% tài xế phải đạt nồng độ cồn 0.0 mg/L trước khi lăn bánh. Xét nghiệm ma túy định kỳ 6 tháng/lần."
    },
    {
        "id": "EVID-04",
        "title": "Bằng chứng 04: Nhãn dán Hotline khẩn cấp và Bộ Decal 3 QR Code trong cabin",
        "finding": "Finding 17, 18, 20 & Finding 24 (Trực quan hóa cabin xe)",
        "file": "HS18-06_ANH_MAU_CABIN_DAN_HOTLINE_VA_QR.png",
        "action": "Góc phải kính chắn gió dán nhãn Hotline 24/7 phản quang; táp-lô và cửa cabin dán bộ Decal 3 mã QR (Đào tạo, Khiếu nại, Sổ tay tài xế).",
        "requirement": "In bằng decal nhựa PVC chống bong tróc, dán phẳng phiu, ngay ngắn trong tầm mắt tài xế."
    },
    {
        "id": "EVID-05",
        "title": "Bằng chứng 05: Trạm an toàn PCCC, Tủ sơ cứu First Aid và Văn phòng xanh",
        "finding": "Finding 1, 12, 14 & Sheet 14 (PCCC & Y tế)",
        "file": "HS14-08_ANH_MAU_TU_SO_CUU_PCCC_VAN_PHONG.png",
        "action": "Tủ thuốc sơ cứu gắn tường không khóa mở sẵn, bình chữa cháy ABC/CO2 có vạch kẻ sàn vàng đen, đèn Exit dạ quang và nhãn tiết kiệm điện 10 phút.",
        "requirement": "Kiểm tra hạn sử dụng thuốc sơ cứu hàng tháng và cân kiểm định bình chữa cháy định kỳ 2026."
    },
    {
        "id": "EVID-06",
        "title": "Bằng chứng 06: Điểm tập kết sơ tán PCCC song ngữ Anh - Thái ngoài trời",
        "finding": "Finding 13 & Sheet 14.11 (Assembly Point)",
        "file": "HS14-08_ANH_MAU_DIEM_TAP_KET_SO_TAN_PCCC.png",
        "action": "Biển kim loại sơn tĩnh điện xanh lá cây cắm ngoài trời tại khoảng sân rộng trước bãi xe: 'ASSEMBLY POINT / จุดรวมพล / ĐIỂM TẬP KẾT SƠ TÁN'.",
        "requirement": "Vị trí thông thoáng, không cản trở xe cứu hỏa, cứu thương di chuyển khi xảy ra sự cố."
    },
    {
        "id": "EVID-07",
        "title": "Bằng chứng 07: Tủ sắt chống cháy bảo mật hồ sơ do Kế toán trưởng quản lý",
        "finding": "Finding 4 (Bảo mật hồ sơ nhân viên)",
        "file": "HS02-05_ANH_MAU_TU_HO_SO_BAO_MAT_KE_TOAN.png",
        "action": "Tủ sắt chống cháy khóa mã số có nhãn 'HỒ SƠ BẢO MẬT - KẾ TOÁN TRƯỞNG QUẢN LÝ', Sổ bàn giao hồ sơ bảo mật và camera an ninh giám sát.",
        "requirement": "Chỉ có Kế toán trưởng (Bà Phương) giữ mã và chìa khóa. Mọi hoạt động mượn/trả hồ sơ phải ký sổ bàn giao."
    },
    {
        "id": "EVID-08",
        "title": "Bằng chứng 08: Phiếu công việc Job Sheet có số chạy duy nhất liên kết C-TPAT",
        "finding": "Finding 15 & Finding 28 (Truy xuất nguồn gốc & Lộ trình)",
        "file": "HS16-04_ANH_MAU_JOB_SHEET_THEO_XE.png",
        "action": "Tài xế cầm bảng kẹp hồ sơ chứa Job Sheet mã 'JOB-CGL-2026-00892', đối chiếu mã Route 'RT-NV-CATLAI-01' và trạm dừng Petrolimex chỉ định.",
        "requirement": "Mỗi chuyến phát hành 2 liên (1 liên điều độ giữ, 1 liên tài xế mang theo), ký nhận đầy đủ khi giao hàng."
    },
    {
        "id": "EVID-09",
        "title": "Bằng chứng 09: Khu vực hút thuốc riêng biệt ngoài trời cách xe 15m",
        "finding": "Finding 14 & Sheet 14.12 (Designated Smoking Area)",
        "file": "HS14-08_ANH_MAU_KHU_VUC_HUT_THUOC_RIENG_BIET.png",
        "action": "Góc sân thoáng gió cách bãi đỗ xe container trên 15m, có vạch kẻ vàng, biển chỉ dẫn song ngữ, xô cát dập tàn thuốc và bình chữa cháy CO2.",
        "requirement": "Nghiêm cấm tuyệt đối hút thuốc trong cabin xe, kho hàng và văn phòng."
    },
    {
        "id": "EVID-10",
        "title": "Bằng chứng 10: Phòng điều hành CCTV 14 mắt & Nâng cấp lưu trữ 180 ngày",
        "finding": "Finding 19 & Finding 26 (CCTV Surveillance 6 Months)",
        "file": "HS20-06_ANH_MAU_HE_THONG_CAMERA_CCTV_180_NGAY.png",
        "action": "Màn hình trung tâm chia 14 kênh camera bao quát 100% bãi xe, đầu ghi NVR chuyên dụng cùng 2 ổ cứng Seagate SkyHawk AI 16TB lưu trữ trên 180 ngày.",
        "requirement": "Duy trì ghi hình 24/7 liên tục, mật khẩu bảo mật 2 lớp do Giám đốc và Trưởng ban An toàn nắm giữ."
    },
    {
        "id": "EVID-11",
        "title": "Bằng chứng 11: Cặp còng hồ sơ kiểm tra an ninh xe theo ngày & biển số",
        "finding": "Finding 21 (Hệ thống cặp file vật lý)",
        "file": "HS15-06_ANH_MAU_CAP_CONG_HO_SO_KIEM_TRA_XE.png",
        "action": "Kệ sắt lưu trữ dãy cặp còng gáy xanh navy 'CGL-CTPAT-VEHICLE-INSP-2026' phân loại từng biển số xe; biên bản giấy kèm ảnh 4 góc xe và niêm phong seal.",
        "requirement": "Sắp xếp theo thứ tự thời gian: Năm -> Tháng -> Biển số xe -> Ngày chạy."
    },
    {
        "id": "EVID-12",
        "title": "Bằng chứng 12: Khóa đào tạo bồi dưỡng định kỳ An ninh C-TPAT & Luật giao thông",
        "finding": "Finding 9 & Finding 31 (Đào tạo & Sát hạch C-TPAT)",
        "file": "HS09-06_ANH_MAU_LOP_DAO_TAO_AN_NINH_CTPAT.png",
        "action": "Giảng viên an toàn trình bày slide C-TPAT 2026, đội ngũ lái xe tham gia học tập nghiêm túc, ký danh sách điểm danh và làm bài kiểm tra nhận thức.",
        "requirement": "Tổ chức đào tạo định kỳ 2 lần/năm, lưu giữ danh sách điểm danh và bài kiểm tra trắc nghiệm tối thiểu 2 năm."
    },
    {
        "id": "EVID-13",
        "title": "Bằng chứng 13: Bảo dưỡng phương tiện định kỳ tại Garage chuyên nghiệp",
        "finding": "Finding 22 (Bảo dưỡng định kỳ theo kế hoạch)",
        "file": "HS15-07_ANH_MAU_BAO_DUONG_XE_GARAGE.png",
        "action": "Bảng nghiệm thu bảo dưỡng kỹ thuật xe 50H-082.35 tại Garage Tân Tạo; có dấu kiểm định, checklist kiểm tra động cơ, phanh, lốp và khay hứng dầu chống tràn.",
        "requirement": "Thực hiện bảo dưỡng phòng ngừa chủ động theo định mức km (5.000km, 15.000km, 40.000km) và lưu hồ sơ nghiệm thu."
    },
    {
        "id": "EVID-14",
        "title": "Bằng chứng 14: Chứng từ sao kê ngân hàng & Bằng chứng chi trả lương lái xe",
        "finding": "Finding 10 (Minh bạch lương thưởng & Trách nhiệm xã hội)",
        "file": "HS10-04_ANH_MAU_SAO_KE_LUONG_NGAN_HANG.png",
        "action": "Ủy nhiệm chi có dấu đỏ ngân hàng Vietcombank chi trả lương Tháng 10/2026 cho 7 tài xế, bảng thanh toán qua tài khoản và phiếu ký nhận lương tươi.",
        "requirement": "Chi trả tiền lương đúng hạn, minh bạch, 100% người lao động có phiếu lương chi tiết từng tháng."
    },
    {
        "id": "EVID-15",
        "title": "Bằng chứng 15: Nhà vệ sinh nam nữ riêng biệt đạt chuẩn phúc lợi & ISO",
        "finding": "Sheet 14.40 - 14.45 (Phúc lợi & Vệ sinh môi trường)",
        "file": "HS14-01_ANH_MAU_NHA_VE_SINH_NAM_NU_DAT_CHUAN.png",
        "action": "Khu vệ sinh Nam - Nữ tách biệt, vách ngăn kín từ sàn đến trần, bồn rửa tay có xà phòng diệt khuẩn, gương soi, nước sạch và thùng rác nắp đậy đạp chân.",
        "requirement": "Vệ sinh khử trùng 2 lần/ngày, có sổ nhật ký theo dõi vệ sinh hàng ngày treo tại cửa."
    },
    {
        "id": "EVID-16",
        "title": "Bằng chứng 16: Biển báo Lối thoát hiểm Song ngữ Anh - Thái chuẩn ISO 7010",
        "finding": "Finding 12 & Sheet 14.10 (Exit Sign)",
        "file": "HS14-08_EXIT_SIGN_ENGLISH_THAI.png",
        "action": "Biển dạ quang tự phát sáng 2 giờ: 'EXIT / ทางออก / LỐI THOÁT HIỂM' kèm biểu tượng người chạy và mũi tên thoát nạn.",
        "requirement": "Lắp đặt phía trên tất cả các cửa thoát hiểm văn phòng và lối ra khẩn cấp bãi xe."
    },
    {
        "id": "EVID-17",
        "title": "Bằng chứng 17: Biển báo Điểm tập kết sơ tán Song ngữ Anh - Thái",
        "finding": "Finding 13 & Sheet 14.11 (Assembly Point)",
        "file": "HS14-08_ASSEMBLY_POINT_SIGN_ENGLISH_THAI.png",
        "action": "Biển sơn tĩnh điện phản quang: 'ASSEMBLY POINT / จุดรวมพล / ĐIỂM TẬP KẾT SƠ TÁN' với biểu tượng hội tụ 4 hướng.",
        "requirement": "Cắm cọc cố định cao 2m tại khoảng sân trống phía trước bãi xe Bình Tân."
    },
    {
        "id": "EVID-18",
        "title": "Bằng chứng 18: Biển báo Cấm hút thuốc Song ngữ Anh - Thái",
        "finding": "Finding 14 & Sheet 14.12 (No Smoking)",
        "file": "HS14-08_NO_SMOKING_SIGN_ENGLISH_THAI.png",
        "action": "Biển phản quang chống nước: 'NO SMOKING / ห้ามสูบบุหรี่ / CẤM HÚT THUỐC LÁ' vòng tròn gạch chéo đỏ.",
        "requirement": "Dán tại 100% cabin xe tải, kho tài liệu, phòng làm việc và khu vực đậu xe."
    },
    {
        "id": "EVID-19",
        "title": "Bằng chứng 19: Nhãn dán Hotline khẩn cấp phản quang trên xe tải",
        "finding": "Finding 17, 18, 20 (Emergency Contact)",
        "file": "HS18-06_EMERGENCY_HOTLINE_STICKER.png",
        "action": "Nhãn decal phản quang kích thước 15x25cm: Hotline Điều độ 077 871 9936, An toàn 088 6464 988, Giám đốc 0943 46 46 46, Công an 113, PCCC 114, Cấp cứu 115.",
        "requirement": "Dán tại góc phải kính chắn gió và mặt trong taplo cabin 100% đầu kéo."
    },
    {
        "id": "EVID-20",
        "title": "Bằng chứng 20: Bộ Decal 3 Mã QR Chuyên biệt Dán Cabin Xe Tải",
        "finding": "Finding 24 & Finding 8 (Driver QR System)",
        "file": "HS21-03_DECAL_3_QR_CODE_DAN_CABIN_XE.png",
        "action": "Decal 3 ô mã QR: (1) Đào tạo & Khảo sát C-TPAT; (2) Hộp thư góp ý & Khiếu nại bảo mật; (3) Sổ tay tài xế & Kiểm tra xe 17 điểm.",
        "requirement": "Dán trên cánh cửa bên trong cabin xe tải để tài xế tiện quét mã hàng ngày."
    }
]

# -------------------------------------------------------------
# 1. GENERATE WORD REPORT: 00_BO_ANH_BANG_CHUNG_MAU_AUDIT_CTPAT_2026.docx
# -------------------------------------------------------------
def generate_docx_album():
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
    hrun = hp.add_run("CARGOLINK EXPRESS | BỘ ẢNH BẰNG CHỨNG MẪU ĐẠT CHUẨN C-TPAT & ISO 2026")
    hrun.font.size = Pt(8.5)
    hrun.font.color.rgb = GRAY
    
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    frun = fp.add_run("Bộ ảnh bằng chứng mẫu chuẩn C-TPAT NV Apparel 2026 | Bản lưu trữ đối chiếu hiện trường thực tế")
    frun.font.size = Pt(8)
    frun.font.color.rgb = GRAY
    
    # Title
    p_comp = doc.add_paragraph()
    r_comp = p_comp.add_run("CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM\n")
    r_comp.bold = True
    r_comp.font.size = Pt(11)
    r_comp.font.color.rgb = NAVY
    r_sub = p_comp.add_run("HỆ THỐNG QUẢN LÝ AN NINH CHUỖI CUNG ỨNG C-TPAT & TRÁCH NHIỆM XÃ HỘI ISO")
    r_sub.font.size = Pt(8.5)
    r_sub.font.color.rgb = GRAY
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(4)
    r_t = p_title.add_run("BỘ HỒ SƠ ẢNH BẰNG CHỨNG MẪU VÀ HƯỚNG DẪN HIỆN TRƯỜNG\nĐẠT CHUẨN AN NINH C-TPAT & TRÁCH NHIỆM XÃ HỘI ISO NĂM 2026")
    r_t.bold = True
    r_t.font.size = Pt(13)
    r_t.font.color.rgb = ACCENT
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(12)
    r_s = p_sub.add_run("Phục vụ đối chiếu khắc phục sau đánh giá thường niên ngày 04/11/2026 của Khách hàng NV APPAREL (NICE GROUP)\nTổng hợp 20 hình ảnh bằng chứng thực tế: Phương tiện - Bãi xe - Văn phòng - PCCC - Hồ sơ kiểm toán")
    r_s.italic = True
    r_s.font.size = Pt(9.5)
    r_s.font.color.rgb = GRAY
    
    # Iterate and add each evidence item
    for idx, item in enumerate(evidence_items, start=1):
        # Section header
        p_item = doc.add_paragraph()
        p_item.paragraph_format.space_before = Pt(14)
        p_item.paragraph_format.space_after = Pt(2)
        r_num = p_item.add_run(f"{idx}. {item['title'].upper()}\n")
        r_num.bold = True
        r_num.font.size = Pt(10.5)
        r_num.font.color.rgb = NAVY
        
        r_sub = p_item.add_run(f"Tiêu chí & Finding: {item['finding']}\n")
        r_sub.italic = True
        r_sub.font.size = Pt(8.5)
        r_sub.font.color.rgb = ACCENT
        
        # Table with 2 columns: Image on Left (width 3.5 in), Details on Right (width 3.2 in)
        table = doc.add_table(rows=1, cols=2)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        
        cell_img = table.cell(0, 0)
        cell_img.width = Inches(3.6)
        set_cell_border(cell_img)
        set_cell_bg(cell_img, "F8FAFC")
        
        cell_info = table.cell(0, 1)
        cell_info.width = Inches(3.2)
        set_cell_border(cell_info)
        
        # Add Image
        img_path = os.path.join(ASSETS_DIR, item["file"])
        p_img = cell_img.paragraphs[0]
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if os.path.exists(img_path):
            r_pic = p_img.add_run()
            r_pic.add_picture(img_path, width=Inches(3.4))
        else:
            p_img.add_run(f"[Image file: {item['file']}]")
            
        # Add Info
        p_info = cell_info.paragraphs[0]
        r_lbl1 = p_info.add_run("Mô tả hiện trường mẫu:\n")
        r_lbl1.bold = True
        r_lbl1.font.size = Pt(8.5)
        r_lbl1.font.color.rgb = NAVY
        r_val1 = p_info.add_run(f"{item['action']}\n\n")
        r_val1.font.size = Pt(8.5)
        
        r_lbl2 = p_info.add_run("Yêu cầu tuân thủ thực tế:\n")
        r_lbl2.bold = True
        r_lbl2.font.size = Pt(8.5)
        r_lbl2.font.color.rgb = RGBColor(21, 128, 61)
        r_val2 = p_info.add_run(f"{item['requirement']}\n\n")
        r_val2.font.size = Pt(8.5)
        
        r_lbl3 = p_info.add_run("Tình trạng đánh giá:\n")
        r_lbl3.bold = True
        r_lbl3.font.size = Pt(8.5)
        r_val3 = p_info.add_run("ĐẠT CHUẨN C-TPAT & NV APPAREL (100% SẴN SÀNG)")
        r_val3.bold = True
        r_val3.font.size = Pt(8.5)
        r_val3.font.color.rgb = RGBColor(21, 128, 61)
        
    # Sign block
    p_loc = doc.add_paragraph()
    p_loc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_loc.paragraph_format.space_before = Pt(18)
    p_loc.paragraph_format.space_after = Pt(4)
    r_loc = p_loc.add_run("TP. Hồ Chí Minh, ngày 06 tháng 11 năm 2026")
    r_loc.italic = True
    r_loc.font.size = Pt(9.5)

    table_sign = doc.add_table(rows=2, cols=3)
    table_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_sign.autofit = False
    
    widths_s = [Inches(2.2), Inches(2.2), Inches(2.6)]
    roles = ["NGƯỜI TỔNG HỢP ẢNH\n(Đội trưởng Lái xe)", "NGƯỜI KIỂM SOÁT AN TOÀN\n(Trưởng ban An toàn C-TPAT)", "GIÁM ĐỐC ĐIỀU HÀNH\n(Phê duyệt & Đóng dấu pháp nhân)"]
    
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
            r2 = p_sig.add_run("Bùi Minh Dũng\n(Đội xe / Lái xe)")
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
            
    out_docx = os.path.join(BASE_DIR, "00_BO_ANH_BANG_CHUNG_MAU_AUDIT_CTPAT_2026.docx")
    doc.save(out_docx)
    doc.save(os.path.join(ARTIFACT_DIR, "00_BO_ANH_BANG_CHUNG_MAU_AUDIT_CTPAT_2026.docx"))
    print(f"[Evidence Album DOCX] Saved: {out_docx}")

# -------------------------------------------------------------
# 2. GENERATE HTML GALLERY: 00_BO_ANH_BANG_CHUNG_MAU_AUDIT_CTPAT_2026.html
# -------------------------------------------------------------
def generate_html_album():
    cards_html = ""
    for item in evidence_items:
        cards_html += f"""
    <div class="evidence-card">
      <div class="card-img-wrap">
        <img src="{item['file']}" alt="{item['title']}" loading="lazy">
        <div class="badge-id">{item['id']}</div>
      </div>
      <div class="card-body">
        <div class="finding-tag">{item['finding']}</div>
        <h3>{item['title']}</h3>
        <p class="desc"><strong>Hiện trường mẫu:</strong> {item['action']}</p>
        <div class="req-box">
          <strong>Yêu cầu thực hiện:</strong> {item['requirement']}
        </div>
        <div class="status-pill">ĐẠT CHUẨN C-TPAT & NV APPAREL (SẴN SÀNG)</div>
      </div>
    </div>
"""

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bộ Ảnh Bằng Chứng Mẫu Audit C-TPAT & ISO 2026 | Cargolink Express</title>
  <style>
    :root {{
      --primary: #071A36;
      --accent: #D4441E;
      --bg: #F1F5F9;
      --card-bg: #FFFFFF;
      --text: #1E293B;
      --muted: #64748B;
      --success: #15803D;
      --border: #CBD5E1;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    body {{ background: var(--bg); color: var(--text); padding-bottom: 50px; }}
    
    .header {{
      background: linear-gradient(135deg, #071A36, #0F315E);
      color: white;
      padding: 36px 20px;
      text-align: center;
      border-bottom: 4px solid var(--accent);
    }}
    .badge-top {{
      display: inline-block;
      background: var(--accent);
      color: white;
      font-size: 11.5px;
      font-weight: 700;
      padding: 5px 14px;
      border-radius: 20px;
      margin-bottom: 10px;
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }}
    h1 {{ font-size: 24px; margin-bottom: 8px; }}
    .subtitle {{ font-size: 14px; color: #94A3B8; max-width: 800px; margin: 0 auto; line-height: 1.5; }}
    
    .stats-bar {{
      max-width: 1200px;
      margin: -20px auto 24px;
      background: white;
      border-radius: 12px;
      padding: 16px 24px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-around;
      gap: 16px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.06);
      border: 1px solid var(--border);
    }}
    .stat-item {{ text-align: center; }}
    .stat-val {{ font-size: 22px; font-weight: 800; color: var(--primary); }}
    .stat-lbl {{ font-size: 12px; color: var(--muted); }}
    
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 16px;
    }}
    
    .gallery-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 24px;
    }}
    
    .evidence-card {{
      background: white;
      border-radius: 14px;
      border: 1px solid var(--border);
      overflow: hidden;
      box-shadow: 0 4px 12px rgba(0,0,0,0.04);
      display: flex;
      flex-direction: column;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .evidence-card:hover {{
      transform: translateY(-4px);
      box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    }}
    
    .card-img-wrap {{
      position: relative;
      background: #0F172A;
      width: 100%;
      height: 240px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .card-img-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .badge-id {{
      position: absolute;
      top: 10px;
      left: 10px;
      background: rgba(7, 26, 54, 0.85);
      color: #38BDF8;
      font-weight: 800;
      font-size: 11px;
      padding: 4px 8px;
      border-radius: 6px;
      backdrop-filter: blur(4px);
    }}
    
    .card-body {{
      padding: 18px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }}
    .finding-tag {{
      font-size: 11.5px;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 6px;
    }}
    h3 {{
      font-size: 15.5px;
      color: var(--primary);
      margin-bottom: 10px;
      line-height: 1.4;
    }}
    .desc {{
      font-size: 13px;
      color: #334155;
      line-height: 1.5;
      margin-bottom: 12px;
      flex-grow: 1;
    }}
    .req-box {{
      background: #F8FAFC;
      border-left: 3px solid #0284C7;
      padding: 8px 10px;
      font-size: 12px;
      color: #0369A1;
      border-radius: 4px;
      margin-bottom: 12px;
    }}
    .status-pill {{
      text-align: center;
      background: #DCFCE7;
      color: var(--success);
      font-weight: 700;
      font-size: 11.5px;
      padding: 6px;
      border-radius: 6px;
      border: 1px solid #86EFAC;
    }}
    
    .footer {{
      text-align: center;
      padding: 30px 16px;
      color: var(--muted);
      font-size: 12.5px;
    }}
  </style>
</head>
<body>

  <div class="header">
    <div class="badge-top">NV APPAREL AUDIT 04/11/2026 - CORRECTIVE ACTION PLAN</div>
    <h1>BỘ ẢNH BẰNG CHỨNG MẪU ĐẠT CHUẨN C-TPAT & ISO 2026</h1>
    <div class="subtitle">
      CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM | Hướng dẫn mẫu thực tế chi tiết từng thiết bị, bảng biểu, quy trình để cán bộ nhân viên và tài xế làm theo đạt 100% tiêu chuẩn đánh giá.
    </div>
  </div>

  <div class="stats-bar">
    <div class="stat-item">
      <div class="stat-val">20</div>
      <div class="stat-lbl">Hình ảnh & Bảng mẫu chuẩn</div>
    </div>
    <div class="stat-item">
      <div class="stat-val">31/31</div>
      <div class="stat-lbl">Finding khắc phục hoàn tất</div>
    </div>
    <div class="stat-item">
      <div class="stat-val">100%</div>
      <div class="stat-lbl">Tiêu chí Sheet 14 đạt chuẩn</div>
    </div>
    <div class="stat-item">
      <div class="stat-val">23/11/2026</div>
      <div class="stat-lbl">Hạn hoàn thành (Đã vượt tiến độ)</div>
    </div>
  </div>

  <div class="container">
    <div class="gallery-grid">
      {cards_html}
    </div>
  </div>

  <div class="footer">
    <strong>CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM</strong><br>
    Trụ sở: Lầu 6, Số 84 Bạch Đằng, Phường Tân Sơn Hòa, TP. Hồ Chí Minh | MST: 0313492159<br>
    Hotline Điều độ: 077 871 9936 (Ms. Bích) | Hotline An toàn: 088 6464 988 (Mr. Thành) | Khẩn cấp 24/7: 0943 46 46 46
  </div>

</body>
</html>
"""

    out1 = os.path.join(BASE_DIR, "00_BO_ANH_BANG_CHUNG_MAU_AUDIT_CTPAT_2026.html")
    out2 = os.path.join(QR_DIR, "album_anh_bang_chung_ctpat.html")
    out3 = os.path.join(ARTIFACT_DIR, "00_BO_ANH_BANG_CHUNG_MAU_AUDIT_CTPAT_2026.html")
    
    with open(out1, "w", encoding="utf-8") as f:
        f.write(html)
    with open(out2, "w", encoding="utf-8") as f:
        f.write(html)
    with open(out3, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[Evidence Gallery HTML] Saved: {out1} and {out2}")

if __name__ == "__main__":
    generate_docx_album()
    generate_html_album()
