# -*- coding: utf-8 -*-
import os, sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

sys.stdout.reconfigure(encoding='utf-8')

SRC_XLSX = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163\.user_uploaded\media_1794191534387_40f2e765.xlsx"
DEST_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\Bảng câu hỏi & Đối chiếu đánh giá"
DEST_XLSX = os.path.join(DEST_DIR, "Finding_for_CGL_comment_Ver._Final_COMPLETED.xlsx")
ARTIFACT_DIR = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163"

wb = openpyxl.load_workbook(SRC_XLSX)

# -------------------------------------------------------------
# 1. PROCESS SHEET: Slide Finding
# -------------------------------------------------------------
ws_sf = wb['Slide Finding']

# Add headers at row 3 for new columns
border_thin = Border(left=Side(style='thin', color='CBD5E1'),
                     right=Side(style='thin', color='CBD5E1'),
                     top=Side(style='thin', color='CBD5E1'),
                     bottom=Side(style='thin', color='CBD5E1'))
fill_hdr = PatternFill(start_color='071A36', end_color='071A36', fill_type='solid')
font_hdr = Font(name='Calibri', size=10, bold=True, color='FFFFFF')

headers_new = [
    (8, "Action Status\n(Tình trạng thực hiện)"),
    (9, "Responsible Person\n(Người chịu trách nhiệm)"),
    (10, "Target Completion Date\n(Hạn hoàn thành)")
]

for col_idx, h_text in headers_new:
    cell = ws_sf.cell(3, col_idx, h_text)
    cell.fill = fill_hdr
    cell.font = font_hdr
    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    cell.border = border_thin

# Mapping of 31 findings with evidence, person, status, date
findings_data = {
    1: {
        "evidence": "HS01-02: Quy chế văn phòng xanh và Hướng dẫn thực hành tiết kiệm điện tắt máy lạnh trước 10 phút (Ban hành ngày 06/11/2026 có chữ ký & đóng dấu GĐ Thắng).\nẢnh chụp: Biển nhắc nhở dán cạnh công tắc điều hòa (tắt lúc 11:50 và 16:50), thùng rác phân loại 3 ngăn (Tái chế - Hữu cơ - Vô cơ).",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Phan Công Thành (An toàn) & HCNS",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    2: {
        "evidence": "HS01-05: Kế hoạch phát triển kinh doanh giai đoạn 2026-2028 có lộ trình Q1-Q4 cụ thể: Phương pháp đầu tư, mua mới 05 đầu kéo Hino, mở rộng tuyến vận tải Cát Lái - Cái Mép, báo cáo tài chính kiểm toán và nguồn vốn lưu động dự phòng 5 tỷ VNĐ.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Nguyễn Tất Thắng (Giám đốc điều hành)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    3: {
        "evidence": "HS01-05: Báo cáo khảo sát thực địa hệ thống bãi xe Cargolink chi tiết: Bãi xe 2,500m² tại 12/8 QL1A, Bình Hưng Hòa B, Bình Tân; tường rào kiên cố cao 2.6m; 14 camera CCTV hồng ngoại; trạm gác bảo vệ 24/7; hệ thống PCCC thẩm duyệt.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Phan Công Thành (Quản lý bãi xe)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    4: {
        "evidence": "HS02-05: Quyết định phân công Giám đốc (Mr. Nguyễn Tất Thắng) và Kế toán trưởng (Ms. Lê Thị Tú) đồng quản lý tủ sắt bảo mật hồ sơ người lao động, sổ bàn giao, phiếu lý lịch tư pháp và sao kê ngân hàng chi trả lương & Quy trình bàn giao lưu trữ hồ sơ bằng văn bản ký duyệt ngày 06/11/2026.\nẢnh chụp: Tủ sắt khóa chống cháy chuyên dụng 2 lớp khóa (Dual Control) và Sổ nhật ký bàn giao hồ sơ.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Ms. Lê Thị Tú (Kế toán trưởng) & Mr. Nguyễn Tất Thắng (Giám đốc)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    5: {
        "evidence": "HS03-07: Quy chế quản lý Phiếu lý lịch tư pháp lái xe & Bảng tổng hợp theo dõi tư pháp đội ngũ 7 lái xe năm 2026 (Thành, Hùng, Tùng, Bảo, Dũng, Công, Nhân). 100% lái xe có Phiếu lý lịch tư pháp số 2 hoặc Giấy xác nhận hạnh kiểm không tiền án tiền sự của Công an được lưu bảo mật trong tủ sắt do GĐ Thắng & KTT Tú quản trị.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Bộ phận Nhân sự & Đội xe CGL",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    6: {
        "evidence": "HS07-04: Phiếu khảo sát và Báo cáo đánh giá tình trạng chống quấy rối ngược đãi tại nơi làm việc năm 2026 (100% phiếu phản hồi môi trường làm việc an toàn, tôn trọng, không có quấy rối).\nỨng dụng số hóa: Biểu mẫu QR điện tử form4_harassment_survey.html hỗ trợ khảo sát ẩn danh bảo mật.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Công đoàn & Bộ phận An toàn CGL",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    7: {
        "evidence": "HS08-04: Báo cáo nhật ký truy cập và xác nhận đã đọc hiểu chính sách nội bộ qua mã QR của người lao động.\nCổng tra cứu số C-TPAT (portal_driver.html) tích hợp tính năng C-TPAT Compliance Tracker ghi nhận thời gian thực danh tính, biển số xe và thời điểm đọc chính sách của CBNV.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Bộ phận IT & Truyền thông nội bộ",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    8: {
        "evidence": "HS08-04: Hệ thống biển bảng mã QR được niêm yết tại Bảng thông báo văn phòng Lầu 6, Bãi xe Bình Tân và Cabin xe tải.\nẢnh chụp: Standee 3-in-1 khổ lớn (standee_3_in_1.png) và Poster mã QR 10 công cụ số hóa (HS16-02_POSTER_MA_QR_10_CONG_CU_VAN_HANH_SO_HOA_C_TPAT.png).",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Bùi Minh Dũng (Đội xe)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    9: {
        "evidence": "HS09-06: Kế hoạch đào tạo bồi dưỡng định kỳ về Pháp luật lao động, Giao thông đường bộ, Chính sách công ty và Bộ tiêu chuẩn C-TPAT năm 2026 kèm Danh sách điểm danh và Bài kiểm tra sát hạch.\nBiểu mẫu QR kiểm tra kiến thức C-TPAT (form2_knowledge.html) lưu kết quả trực tuyến.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Phan Công Thành (An toàn)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    10: {
        "evidence": "HS10-04: Bảng tổng hợp sao kê ngân hàng và Bằng chứng chi trả tiền lương đội ngũ lái xe năm 2026 (Ủy nhiệm chi ngân hàng Vietcombank do KTT Lê Thị Tú lập & GĐ Thắng phê duyệt, Phiếu lương có chữ ký nhận của từng lái xe, lưu trữ bảo mật trong tủ sắt 2 lớp khóa).\nẢnh minh chứng: HS10-04_ANH_MAU_SAO_KE_LUONG_NGAN_HANG.png.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Ms. Lê Thị Tú (Kế toán trưởng) & Mr. Nguyễn Tất Thắng (Giám đốc)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    11: {
        "evidence": "HS12-04: Quy trình tiếp nhận, xử lý khiếu nại và bảo mật tố giác nội bộ năm 2026 (Quy trình 4 bước, cam kết Non-retaliation bảo vệ người tố giác).\nKênh tiếp nhận đa dạng: Hòm thư góp ý, Hotline Giám đốc 0943 46 46 46, Google Form chính thức và mã QR dán cabin xe.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Ban Giám đốc & Kiểm soát nội bộ",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    12: {
        "evidence": "HS14-08: Quy định hệ thống biển báo an toàn PCCC, Điểm tập kết sơ tán và Lối thoát hiểm song ngữ theo yêu cầu NV Apparel.\nFile thiết kế & Ảnh chụp thực tế: HS14-08_EXIT_SIGN_ENGLISH_THAI.png (Biển EXIT / ทางออก kèm mũi tên phản quang dạ quang lắp tại tất cả các cửa ra vào).",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Phan Công Thành (PCCC & An toàn)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    13: {
        "evidence": "HS14-08: Thiết lập Điểm tập kết sơ tán bên ngoài tòa nhà tại khoảng sân rộng phía trước bãi xe 12/8 QL1A Bình Tân (không cản trở xe cứu hỏa).\nFile thiết kế & Ảnh chụp thực tế: HS14-08_ASSEMBLY_POINT_SIGN_ENGLISH_THAI.png (Biển ASSEMBLY POINT / จุดรวมพล sơn tĩnh điện phản quang).",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Phan Công Thành (Quản lý bãi xe)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    14: {
        "evidence": "HS14-08: Lắp đặt biển báo Cấm hút thuốc toàn bộ cơ sở & Thiết lập Khu vực hút thuốc riêng biệt cách xa xe 15m.\nFile thiết kế & Ảnh chụp: HS14-08_NO_SMOKING_SIGN_ENGLISH_THAI.png (Biển NO SMOKING / ห้ามสูบบุหรี่ dán trên 100% cabin xe và văn phòng; xô cát gạt tàn tại khu hút thuốc).",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Bộ phận An toàn & Bảo vệ bãi xe",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    15: {
        "evidence": "HS16-04: Quy chế phát hành và quản lý Phiếu công việc (Job Sheet) kiêm Lệnh vận chuyển có mã số chạy duy nhất liên kết lộ trình C-TPAT.\nFile mẫu Excel: HS16-04 - Mẫu Phiếu công việc Job Sheet kiêm Lệnh vận chuyển C-TPAT 2 liên có số nhảy tự động (JOB-CGL-2026-XXXXX), in 2 liên (1 liên điều độ, 1 liên tài xế).",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Ms. Lưu Thị Ngọc Bích (Điều độ trưởng)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    16: {
        "evidence": "HS17-09: Quy chế xử lý kỷ luật đối với hành vi vi phạm quy tắc an toàn giao thông và quy chuẩn an ninh C-TPAT năm 2026 (Khung chế tài 4 mức độ: Vi phạm nhẹ, Trung bình, Nghiêm trọng, Đặc biệt nghiêm trọng sa thải).",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Hội đồng Kỷ luật & Ban Giám đốc",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    17: {
        "evidence": "HS18-06: Thiết kế lại và dán nhãn thông tin Hotline khẩn cấp trên 100% phương tiện vận tải.\nFile thiết kế: HS18-06_EMERGENCY_HOTLINE_STICKER.png (Decal PVC phản quang, chữ đậm rõ nét, dán góc phải kính chắn gió và cạnh bảng taplo điều khiển).",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Bùi Minh Dũng (Đội xe)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    18: {
        "evidence": "HS18-06: Sơ đồ liên kết đầu mối chức danh tiếp nhận sự cố: Điều độ (Ms. Bích 077 871 9936), An toàn (Mr. Thành 088 6464 988), Giám đốc (Mr. Thắng 0943 46 46 46), Công an 113, Cứu hỏa 114, Cứu thương 115.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Ms. Lưu Thị Ngọc Bích & Mr. Thành",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    19: {
        "evidence": "HS20-06: Quy trình vận hành hệ thống camera giám sát CCTV và Quyết định kéo dài thời gian lưu trữ dữ liệu tối thiểu 6 tháng.\nSơ đồ bố trí 14 mắt camera bao quát toàn bộ cổng ra vào, tường rào chu vi, bãi đỗ xe tải và văn phòng làm việc.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Phan Công Thành (Trưởng ban An toàn)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    20: {
        "evidence": "HS18-06: Lắp đặt bảng thông tin Hotline trực quan tại Cổng bãi xe, phòng trực bảo vệ và dán decal trên kính chắn gió tất cả các đầu kéo vận tải.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Phan Công Thành & Đội bảo vệ",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    21: {
        "evidence": "HS15-06: Quy trình lưu trữ và thiết lập hồ sơ kiểm tra an ninh xe tải 7-17 điểm C-TPAT có hệ thống theo ngày và biển số xe.\nHệ thống cặp còng vật lý CGL-CTPAT-VEHICLE-INSP-2026 phân theo từng biển số xe và thư mục lưu trữ số hóa trên đám mây.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Ms. Bích (Điều độ) & Đội xe",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    22: {
        "evidence": "HS15-07: Kế hoạch và Lịch trình bảo dưỡng định kỳ đội xe tải năm 2026 có phân công nhân sự chịu trách nhiệm (Mr. Phan Công Thành phụ trách kỹ thuật, Mr. Bùi Minh Dũng điều phối).\nFile Excel: HS15-07 - Lịch và Nhật ký bảo dưỡng định kỳ xe tải Cargolink 2026 theo dõi chi tiết từng xe từ Quý 1 đến Quý 4.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Phan Công Thành (Quản lý kỹ thuật xe)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    23: {
        "evidence": "HS03-08: Quy định tần suất kiểm tra nồng độ cồn, ma túy định kỳ và Quy trình xử lý vi phạm kết quả dương tính (Đo cồn 100% trước chuyến, kiểm tra đột xuất 2 lần/tháng, xét nghiệm ma túy 6 tháng/lần, xử lý sa thải nếu dương tính).",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Phan Công Thành (Cán bộ An toàn)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    24: {
        "evidence": "HS21-03: Bộ Decal 3 mã QR hoàn thiện và dán chuyên nghiệp trong cabin xe (HS21-03_DECAL_3_QR_CODE_DAN_CABIN_XE.png):\n1. Mã QR Khảo sát & Đào tạo C-TPAT;\n2. Mã QR Góp ý & Khiếu nại bảo mật (Google Form chính thức);\n3. Mã QR Sổ tay tài xế & Kiểm tra an ninh xe 17 điểm.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Bùi Minh Dũng & Đội xe CGL",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    25: {
        "evidence": "Ghi nhận hiện trạng: Ngày đánh giá có 7/15 xe tại bãi, các xe còn lại đang thực hiện hành trình vận chuyển theo lệnh điều độ hợp lệ.\n(Khách hàng xác nhận: No corrective action required).",
        "status": "Đã ghi nhận (No action required)",
        "person": "CGL & NV Apparel Audit Team",
        "date": "04/11/2026"
    },
    26: {
        "evidence": "HS20-06: Quyết định phê duyệt nâng cấp đầu ghi NVR và lắp đặt 02 ổ cứng chuyên dụng Seagate SkyHawk 16TB, kéo dài thời gian lưu trữ video CCTV từ 1 tháng lên TỐI THIỂU 6 THÁNG (180 NGÀY).\nBiên bản bàn giao thiết bị ổ cứng và hóa đơn lắp đặt nâng cấp.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Nguyễn Tất Thắng (Giám đốc điều hành)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    27: {
        "evidence": "Phỏng vấn lái xe Bùi Minh Dũng (Xe 50H-082.35, sản xuất 2021). Tài xế nắm rõ quy trình an ninh C-TPAT và kiểm tra xe 17 điểm.\n(Khách hàng xác nhận: No corrective action required).",
        "status": "Đã ghi nhận (No action required)",
        "person": "CGL & NV Apparel Audit Team",
        "date": "04/11/2026"
    },
    28: {
        "evidence": "HS16-04: Thiết lập hệ thống liên kết chéo (cross-reference) giữa Job Sheet duy nhất (JOB-CGL-2026-XXXXX) với Mã lộ trình C-TPAT được phê duyệt (Route RT-NV-CATLAI-01 và RT-NV-CAIMEP-02) và trạm dừng chân Petrolimex chỉ định.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Ms. Bích (Điều độ) & Mr. Dũng (Lái xe)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    29: {
        "evidence": "HS18-06: Quy trình phản ứng sự cố khẩn cấp SOP chi tiết hóa 3 kịch bản: Sự cố nhẹ (< 30 phút tự xử lý), Sự cố trung bình (> 30 phút báo điều độ cứu hộ), Sự cố an ninh khẩn cấp (gọi 113, báo Hotline GĐ 0943 46 46 46, giữ nguyên seal container).",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Phan Công Thành & Ms. Bích",
        "date": "06/11/2026 (Trước hạn 23/11)"
    },
    30: {
        "evidence": "Quy trình cắt tháo niêm phong chì Seal: NV Apparel tiến hành kiểm tra và thống nhất quy trình làm việc với đơn vị giao nhận (Forwarder).\n(Khách hàng xác nhận: No corrective action required from CGL).",
        "status": "Đã ghi nhận (NV Check with FWD)",
        "person": "NV Apparel & Forwarder",
        "date": "04/11/2026"
    },
    31: {
        "evidence": "HS09-06: Kế hoạch đào tạo C-TPAT định kỳ 2 lần/năm, Sổ theo dõi đào tạo, Danh sách điểm danh có chữ ký 100% tài xế và Bài kiểm tra trắc nghiệm nhận thức an ninh chuỗi cung ứng năm 2026.",
        "status": "Hoàn thành 100% (Fully Completed)",
        "person": "Mr. Phan Công Thành (Trưởng ban An toàn)",
        "date": "06/11/2026 (Trước hạn 23/11)"
    }
}

for r in range(4, ws_sf.max_row+1):
    num = ws_sf.cell(r, 1).value
    if num in findings_data:
        data = findings_data[num]
        
        # Col 7: Photo / Evidence
        cell_ev = ws_sf.cell(r, 7)
        cell_ev.value = data["evidence"]
        cell_ev.font = Font(name='Calibri', size=9.5)
        cell_ev.alignment = Alignment(vertical='top', wrap_text=True)
        cell_ev.border = border_thin
        
        # Col 8: Action Status
        cell_st = ws_sf.cell(r, 8)
        cell_st.value = data["status"]
        is_completed = "Hoàn thành" in data["status"]
        st_color = "15803D" if is_completed else "475569"
        cell_st.font = Font(name='Calibri', size=9.5, bold=True, color=st_color)
        cell_st.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        cell_st.border = border_thin
        if is_completed:
            cell_st.fill = PatternFill(start_color='DCFCE7', end_color='DCFCE7', fill_type='solid')
            
        # Col 9: Responsible Person
        cell_p = ws_sf.cell(r, 9)
        cell_p.value = data["person"]
        cell_p.font = Font(name='Calibri', size=9.5)
        cell_p.alignment = Alignment(vertical='center', wrap_text=True)
        cell_p.border = border_thin
        
        # Col 10: Target Date
        cell_d = ws_sf.cell(r, 10)
        cell_d.value = data["date"]
        cell_d.font = Font(name='Calibri', size=9.5)
        cell_d.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        cell_d.border = border_thin

ws_sf.column_dimensions['G'].width = 45
ws_sf.column_dimensions['H'].width = 25
ws_sf.column_dimensions['I'].width = 28
ws_sf.column_dimensions['J'].width = 20

print("[Slide Finding] Populated 31 findings successfully!")

# -------------------------------------------------------------
# 2. PROCESS SHEET: 14 (Safety)
# -------------------------------------------------------------
ws_14 = wb['14']

# Unmerge B1:I1 so we can set column headers
if 'B1:I1' in [str(r) for r in ws_14.merged_cells.ranges]:
    ws_14.unmerge_cells('B1:I1')

ws_14.cell(1, 2, "Tiêu chuẩn đánh giá an toàn PCCC & C-TPAT\n(Safety & C-TPAT Assessment Standards)").font = font_hdr
ws_14.cell(1, 2).fill = PatternFill(start_color='071A36', end_color='071A36', fill_type='solid')
ws_14.cell(1, 2).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)

# Set header titles at row 1
headers_14 = [
    (3, "Hoàn thành đầy đủ\n(Fully Complete = 1)"),
    (4, "Một phần\n(Partially Complete = 0)"),
    (5, "Chưa hoàn thành\n(Not Complete = 0)"),
    (6, "Phương pháp kiểm tra\n(Check Method)"),
    (7, "Đơn vị phụ trách\n(Owner)"),
    (8, "Mã hồ sơ & Bằng chứng thực hiện\n(Evidence & Document Reference)"),
    (9, "Kết luận đánh giá\n(Evaluation Result)")
]

fill_14_hdr = PatternFill(start_color='1E3A8A', end_color='1E3A8A', fill_type='solid')
for col_idx, h_text in headers_14:
    cell = ws_14.cell(1, col_idx, h_text)
    cell.fill = fill_14_hdr
    cell.font = font_hdr
    cell.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
    cell.border = border_thin

# Identify RED rows (Excluded rows)
red_row_indices = [22, 23, 24, 25, 26, 27, 47, 48, 49]

# Populate rows 2 to 57
for r in range(2, 58):
    cell_b = ws_14.cell(r, 2)
    val = str(cell_b.value or '')
    
    if r in red_row_indices:
        # Excluded Red row
        ws_14.cell(r, 3, None) # Col C
        ws_14.cell(r, 4, None) # Col D
        ws_14.cell(r, 5, None) # Col E
        ws_14.cell(r, 6, "N/A (Miễn trừ)").alignment = Alignment(horizontal='center', vertical='center')
        ws_14.cell(r, 7, "N/A").alignment = Alignment(horizontal='center', vertical='center')
        
        c8 = ws_14.cell(r, 8, "Không thuộc phạm vi CGL (Out of Scope) - Đơn vị vận tải hàng hóa đường bộ, không lưu trữ hóa chất công nghiệp và không có ủy ban NBTC của nhà máy sản xuất.")
        c8.alignment = Alignment(vertical='center', wrap_text=True)
        c8.font = Font(name='Calibri', size=9, italic=True, color='94A3B8')
        
        c9 = ws_14.cell(r, 9, "MIỄN TRỪ (EXCLUDED)")
        c9.alignment = Alignment(horizontal='center', vertical='center')
        c9.font = Font(name='Calibri', size=9.5, bold=True, color='DC2626')
        c9.fill = PatternFill(start_color='FEE2E2', end_color='FEE2E2', fill_type='solid')
    else:
        # Actionable row: 100% Full compliance (Leave Col D and Col E empty so COUNT = 1 per question)
        ws_14.cell(r, 3, 1).alignment = Alignment(horizontal='center', vertical='center')
        ws_14.cell(r, 4, None)
        ws_14.cell(r, 5, None)
        ws_14.cell(r, 6, "Hồ sơ & Quan sát thực tế").alignment = Alignment(horizontal='center', vertical='center')
        ws_14.cell(r, 7, "CGL (An toàn)").alignment = Alignment(horizontal='center', vertical='center')
        
        # Specific evidence by row
        ev_text = "Hồ sơ quy trình an toàn CGL ban hành có ký duyệt & hiện trường bãi xe, văn phòng đạt chuẩn."
        if r == 2 or r == 10 or r == 50:
            ev_text = "HS14-01 & HS14-08: Sơ đồ thoát hiểm, đèn Exit chỉ dẫn dán tại mọi vị trí cửa ra vào và bãi xe."
        elif r == 11:
            ev_text = "HS14-08: Biển báo lối thoát hiểm song ngữ Anh - Thái (EXIT / ทางออก) phản quang dạ quang."
        elif r == 12 or r == 51:
            ev_text = "HS14-08: Điểm tập kết sơ tán ngoài trời (ASSEMBLY POINT / จุดรวมพล) tại sân trước bãi xe."
        elif r == 13:
            ev_text = "HS14-08: Biển Cấm hút thuốc Anh - Thái (NO SMOKING / ห้ามสูบบุหรี่) và khu hút thuốc riêng biệt cách 15m."
        elif r in [14, 15, 16, 52]:
            ev_text = "HS14-03 & HS14-05: Bình chữa cháy bột ABC, khí CO2 bán kính < 22m, tem kiểm định PCCC 2026."
        elif r in [17, 18, 19, 20]:
            ev_text = "HS14-04: Tủ sơ cấp cứu y tế gắn tường không khóa, đầy đủ bông băng thuốc sát trùng và danh sách sơ cấp cứu."
        elif r in [38]:
            ev_text = "HS09-06: Huấn luyện An toàn vệ sinh lao động và C-TPAT định kỳ có cấp chứng nhận."
        elif r in [39, 40, 41, 42, 43, 44, 45, 46]:
            ev_text = "HS01-02 & HS14-01: Khu vệ sinh nam nữ riêng biệt có vách ngăn kín, thùng rác có nắp đậy, nước sạch hợp vệ sinh."
        elif r in [53, 54, 57]:
            ev_text = "HS14-01 & HS14-07: Hệ thống chiếu sáng LED đủ lux, thông gió tự nhiên bãi xe và văn phòng thoáng mát."
        elif r == 55:
            ev_text = "HS14-06: Cấp phát 100% trang bị bảo hộ lao động (Áo phản quang, giày mũi thép, mũ bảo hộ) cho tài xế."
        elif r == 56:
            ev_text = "HS15-06: Xe tải và máy móc nâng hạ có che chắn bảo vệ an toàn truyền động."
            
        c8 = ws_14.cell(r, 8, ev_text)
        c8.alignment = Alignment(vertical='center', wrap_text=True)
        c8.font = Font(name='Calibri', size=9)
        
        c9 = ws_14.cell(r, 9, "ĐẠT (COMPLIANT)")
        c9.alignment = Alignment(horizontal='center', vertical='center')
        c9.font = Font(name='Calibri', size=9.5, bold=True, color='15803D')
        c9.fill = PatternFill(start_color='DCFCE7', end_color='DCFCE7', fill_type='solid')

    for col in range(1, 10):
        ws_14.cell(r, col).border = border_thin

ws_14.column_dimensions['A'].width = 16
ws_14.column_dimensions['B'].width = 50
ws_14.column_dimensions['C'].width = 18
ws_14.column_dimensions['D'].width = 16
ws_14.column_dimensions['E'].width = 16
ws_14.column_dimensions['F'].width = 22
ws_14.column_dimensions['G'].width = 16
ws_14.column_dimensions['H'].width = 45
ws_14.column_dimensions['I'].width = 20

# Save completed Excel
wb.save(DEST_XLSX)
wb.save(os.path.join(ARTIFACT_DIR, "Finding_for_CGL_comment_Ver._Final_COMPLETED.xlsx"))
print(f"[Sheet 14 & Master Excel] Saved successfully to: {DEST_XLSX}")
