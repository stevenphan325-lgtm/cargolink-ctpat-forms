# -*- coding: utf-8 -*-
import os, sys, shutil, glob

sys.stdout.reconfigure(encoding='utf-8')

ARTIFACT_DIR = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163"
BASE_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026"
ASSETS_DIR = os.path.join(BASE_DIR, "00_BO_BANNER_VA_LOGO_CARGOLINK")
QR_DIR = os.path.join(BASE_DIR, "CTPAT_QR_FORMS")

# Mapping definitions
mapping = [
    {
        "pattern": "*anh_mau_kiem_tra_xe_17_diem*",
        "target_name": "HS15-06_ANH_MAU_KIEM_TRA_XE_17_DIEM.png",
        "folder": "15. Phương tiện và bảo dưỡng",
        "title": "Bằng chứng 01: Quy trình kiểm tra an ninh xe tải 17 điểm C-TPAT",
        "finding": "Finding 21 & Sheet 14 (Phương tiện & Niêm phong chì seal)",
        "desc": "Tài xế mặc áo phản quang, đội nón bảo hộ dùng đèn pin chuyên dụng kiểm tra chốt khóa niêm phong Seal container và các điểm trọng yếu quanh xe trước khi xuất bến."
    },
    {
        "pattern": "*anh_mau_bai_xe_cctv_cargolink*",
        "target_name": "HS01-05_ANH_MAU_BAI_XE_CCTV_CARGOLINK.png",
        "folder": "01. Hồ sơ và năng lực doanh nghiệp",
        "title": "Bằng chứng 02: Toàn cảnh bãi xe logistics, tường rào 2.6m & cột CCTV",
        "finding": "Finding 3 & Finding 25 (Hạ tầng bãi xe & Hiện trạng phương tiện)",
        "desc": "Bãi xe diện tích 2.500m² tại Bình Tân, hàng rào thép gai kiên cố cao 2.6m, trạm kiểm soát an ninh barie và các cột camera CCTV hồng ngoại bao quát."
    },
    {
        "pattern": "*anh_mau_do_nong_do_con_tai_xe*",
        "target_name": "HS03-08_ANH_MAU_DO_NONG_DO_CON_TAI_XE.png",
        "folder": "03. Hồ sơ nhân viên và tài xế",
        "title": "Bằng chứng 03: Kiểm tra nồng độ cồn và xét nghiệm ma túy tài xế",
        "finding": "Finding 23 & Sheet 14 (Chính sách Zero Tolerance)",
        "desc": "Bảo vệ trạm gác dùng máy đo nồng độ cồn điện tử cho tài xế thổi kiểm tra trước mỗi chuyến đi; sổ nhật ký ghi nhận và bộ que test ma túy 4 chỉ số."
    },
    {
        "pattern": "*anh_mau_cabin_xe_dan_hotline_qr*",
        "target_name": "HS18-06_ANH_MAU_CABIN_DAN_HOTLINE_VA_QR.png",
        "folder": "18. Chậm trễ và sự cố",
        "title": "Bằng chứng 04: Nhãn dán Hotline khẩn cấp và Bộ Decal 3 QR Code trong cabin",
        "finding": "Finding 17, 18, 20 & Finding 24 (Trực quan hóa cabin xe)",
        "desc": "Decal phản quang Hotline 24/7 dán góc phải kính chắn gió; bộ 3 tem QR Code (Đào tạo, Khiếu nại bảo mật, Sổ tay kiểm tra xe) dán trang trọng tại táp-lô và cửa cabin."
    },
    {
        "pattern": "*anh_mau_tu_so_cuu_pccc_van_phong*",
        "target_name": "HS14-08_ANH_MAU_TU_SO_CUU_PCCC_VAN_PHONG.png",
        "folder": "14. An toàn cơ sở và công việc",
        "title": "Bằng chứng 05: Trạm an toàn PCCC, Tủ sơ cứu First Aid và Văn phòng xanh",
        "finding": "Finding 1, 12, 14 & Sheet 14 (PCCC & Y tế)",
        "desc": "Tủ thuốc sơ cứu gắn tường không khóa, bình chữa cháy ABC/CO2 có vạch sơn phản quang vàng đen, đèn Exit dạ quang trên cửa và nhãn tiết kiệm điện 10 phút."
    },
    {
        "pattern": "*anh_mau_diem_tap_ket_so_tan*",
        "target_name": "HS14-08_ANH_MAU_DIEM_TAP_KET_SO_TAN_PCCC.png",
        "folder": "14. An toàn cơ sở và công việc",
        "title": "Bằng chứng 06: Điểm tập kết sơ tán PCCC song ngữ Anh - Thái ngoài trời",
        "finding": "Finding 13 & Sheet 14.11 (Assembly Point)",
        "desc": "Biển kim loại sơn tĩnh điện xanh lá cây cắm ngoài trời tại khoảng sân rộng trước bãi xe: 'ASSEMBLY POINT / จุดรวมพล / ĐIỂM TẬP KẾT SƠ TÁN', không cản trở xe cứu hộ."
    },
    {
        "pattern": "*anh_mau_tu_ho_so_bao_mat_ke_toan*",
        "target_name": "HS02-05_ANH_MAU_TU_HO_SO_BAO_MAT_KE_TOAN.png",
        "folder": "02. Tuyển dụng và tiếp nhận",
        "title": "Bằng chứng 07: Tủ sắt chống cháy bảo mật hồ sơ do Kế toán trưởng quản lý",
        "finding": "Finding 4 (Bảo mật hồ sơ nhân viên)",
        "desc": "Tủ sắt chống cháy khóa mã số có dán nhãn 'HỒ SƠ BẢO MẬT - KẾ TOÁN TRƯỞNG QUẢN LÝ', Sổ bàn giao lưu trữ hồ sơ và camera an ninh giám sát cửa tủ."
    },
    {
        "pattern": "*anh_mau_phieu_cong_viec_job_sheet_xe*",
        "target_name": "HS16-04_ANH_MAU_JOB_SHEET_THEO_XE.png",
        "folder": "16. Thông tin xe và theo dõi chuyến",
        "title": "Bằng chứng 08: Phiếu công việc Job Sheet có số chạy duy nhất liên kết C-TPAT",
        "finding": "Finding 15 & Finding 28 (Truy xuất nguồn gốc & Lộ trình)",
        "desc": "Tài xế cầm bảng kẹp hồ sơ chứa Job Sheet mã 'JOB-CGL-2026-00892', đối chiếu mã Route 'RT-NV-CATLAI-01' và trạm dừng Petrolimex chỉ định cạnh xe 50H-082.35."
    },
    {
        "pattern": "*anh_mau_khu_vuc_hut_thuoc_rieng_biet*",
        "target_name": "HS14-08_ANH_MAU_KHU_VUC_HUT_THUOC_RIENG_BIET.png",
        "folder": "14. An toàn cơ sở và công việc",
        "title": "Bằng chứng 09: Khu vực hút thuốc riêng biệt ngoài trời cách xe 15m",
        "finding": "Finding 14 & Sheet 14.12 (Designated Smoking Area)",
        "desc": "Góc sân thoáng gió cách bãi đỗ xe container trên 15m, có vạch kẻ vàng, biển chỉ dẫn song ngữ, xô cát dập tàn thuốc và bình chữa cháy CO2 trang bị sẵn."
    },
    {
        "pattern": "*anh_mau_he_thong_camera_cctv_man_hinh*",
        "target_name": "HS20-06_ANH_MAU_HE_THONG_CAMERA_CCTV_180_NGAY.png",
        "folder": "20. An ninh cơ sở, xe và container",
        "title": "Bằng chứng 10: Phòng điều hành CCTV 14 mắt & Nâng cấp lưu trữ 180 ngày",
        "finding": "Finding 19 & Finding 26 (CCTV Surveillance 6 Months)",
        "desc": "Màn hình trung tâm chia 14 kênh camera bao quát 100% bãi xe, đầu ghi NVR chuyên dụng cùng 2 ổ cứng Seagate SkyHawk AI 16TB đảm bảo lưu trữ video trên 180 ngày."
    },
    {
        "pattern": "*anh_mau_cap_cong_ho_so_kiem_tra_xe*",
        "target_name": "HS15-06_ANH_MAU_CAP_CONG_HO_SO_KIEM_TRA_XE.png",
        "folder": "15. Phương tiện và bảo dưỡng",
        "title": "Bằng chứng 11: Cặp còng hồ sơ kiểm tra an ninh xe theo ngày & biển số",
        "finding": "Finding 21 (Hệ thống cặp file vật lý)",
        "desc": "Kệ sắt lưu trữ dãy cặp còng gáy xanh navy 'CGL-CTPAT-VEHICLE-INSP-2026' phân loại từng biển số xe; biên bản giấy kèm ảnh chụp 4 góc xe và niêm phong seal."
    },
    {
        "pattern": "*anh_mau_lop_dao_tao_an_ninh_ctpat*",
        "target_name": "HS09-06_ANH_MAU_LOP_DAO_TAO_AN_NINH_CTPAT.png",
        "folder": "09. Đào tạo nhân viên",
        "title": "Bằng chứng 12: Khóa đào tạo bồi dưỡng định kỳ An ninh C-TPAT & Luật giao thông",
        "finding": "Finding 9 & Finding 31 (Đào tạo & Sát hạch C-TPAT)",
        "desc": "Giảng viên an toàn trình bày slide C-TPAT 2026, đội ngũ lái xe tham gia học tập nghiêm túc, ký danh sách điểm danh và làm bài kiểm tra nhận thức an ninh."
    },
    {
        "pattern": "*anh_mau_bao_duong_xe_tai_garage*",
        "target_name": "HS15-07_ANH_MAU_BAO_DUONG_XE_GARAGE.png",
        "folder": "15. Phương tiện và bảo dưỡng",
        "title": "Bằng chứng 13: Bảo dưỡng phương tiện định kỳ tại Garage chuyên nghiệp",
        "finding": "Finding 22 (Bảo dưỡng định kỳ theo kế hoạch)",
        "desc": "Kỹ thuật viên xưởng cơ khí kiểm tra động cơ, hệ thống phanh hơi và áp suất lốp theo Checklist kỹ thuật định kỳ 2026; xưởng có khay hứng dầu chống tràn đổ."
    },
    {
        "pattern": "*anh_mau_sao_ke_luong_ngan_hang*",
        "target_name": "HS10-04_ANH_MAU_SAO_KE_LUONG_NGAN_HANG.png",
        "folder": "10. Tiền lương và làm thêm",
        "title": "Bằng chứng 14: Chứng từ sao kê ngân hàng & Bằng chứng chi trả lương lái xe",
        "finding": "Finding 10 (Minh bạch lương thưởng & Trách nhiệm xã hội)",
        "desc": "Giấy ủy nhiệm chi có dấu đỏ ngân hàng Vietcombank, bảng tổng hợp thanh toán lương qua tài khoản của 7 lái xe và phiếu lương có chữ ký tươi từng tháng."
    },
    {
        "pattern": "*anh_mau_nha_ve_sinh_nam_nu_rieng_biet*",
        "target_name": "HS14-01_ANH_MAU_NHA_VE_SINH_NAM_NU_DAT_CHUAN.png",
        "folder": "14. An toàn cơ sở và công việc",
        "title": "Bằng chứng 15: Nhà vệ sinh nam nữ riêng biệt đạt chuẩn phúc lợi & ISO",
        "finding": "Sheet 14.40 - 14.45 (Phúc lợi & Vệ sinh môi trường)",
        "desc": "Khu vệ sinh Nam - Nữ tách biệt, vách ngăn kín từ sàn đến trần, bồn rửa tay có xà phòng diệt khuẩn, gương soi, nước sạch và thùng rác nắp đậy đạp chân inox."
    }
]

print("--- SCANNING AND COPYING EVIDENCE PHOTOS ---")
copied_items = []

for item in mapping:
    matches = glob.glob(os.path.join(ARTIFACT_DIR, item["pattern"]))
    if matches:
        src = matches[0]
        # Target 1: ASSETS_DIR
        t1 = os.path.join(ASSETS_DIR, item["target_name"])
        shutil.copy2(src, t1)
        
        # Target 2: Folder
        t2 = os.path.join(BASE_DIR, item["folder"], item["target_name"])
        shutil.copy2(src, t2)
        
        # Target 3: QR_DIR
        t3 = os.path.join(QR_DIR, item["target_name"])
        shutil.copy2(src, t3)
        
        copied_items.append({
            "title": item["title"],
            "finding": item["finding"],
            "desc": item["desc"],
            "filename": item["target_name"],
            "rel_path": f"{item['folder']}/{item['target_name']}".replace("\\", "/")
        })
        print(f"✅ Copied: {item['target_name']}")
    else:
        print(f"⏳ Waiting for pattern: {item['pattern']}")

print(f"\nTotal Copied: {len(copied_items)}/{len(mapping)}")
