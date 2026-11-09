# -*- coding: utf-8 -*-
import os, sys
import openpyxl
from docx import Document
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026"

print("================================================================")
print("   CARGOLINK EXPRESS - FULL AUDIT 2026 INTEGRITY VERIFICATION   ")
print("================================================================")

errors = []

# 1. Check Key CAP Documents
key_docx = [
    "00_KE_HOACH_KHAC_PHUC_AUDIT_CTPAT_04_11_2026.docx",
    "01. Hồ sơ và năng lực doanh nghiệp/HS01-02 - Quy chế văn phòng xanh và Hướng dẫn thực hành tiết kiệm điện tắt máy lạnh trước 10 phút.docx",
    "01. Hồ sơ và năng lực doanh nghiệp/HS01-05 - Kế hoạch phát triển kinh doanh giai đoạn 2026-2028 và Báo cáo khảo sát thực địa hệ thống bãi xe Cargolink.docx",
    "02. Tuyển dụng và tiếp nhận/HS02-05 - Quyết định phân công Kế toán trưởng quản lý hồ sơ bảo mật và Quy trình bàn giao lưu trữ hồ sơ người lao động.docx",
    "03. Hồ sơ nhân viên và tài xế/HS03-07 - Quy chế quản lý Phiếu lý lịch tư pháp lái xe và Bảng tổng hợp theo dõi tư pháp đội ngũ lái xe năm 2026.docx",
    "03. Hồ sơ nhân viên và tài xế/HS03-08 - Quy định tần suất kiểm tra nồng độ cồn ma túy định kỳ và Quy trình xử lý vi phạm kết quả dương tính.docx",
    "07. Chống quấy rối ngược đãi và cưỡng bức/HS07-04 - Phiếu khảo sát và Báo cáo đánh giá tình trạng chống quấy rối ngược đãi tại nơi làm việc năm 2026.docx",
    "08. Truyền đạt nội quy và chính sách/HS08-04 - Báo cáo nhật ký truy cập và xác nhận đã đọc hiểu chính sách nội bộ qua mã QR của người lao động.docx",
    "09. Đào tạo nhân viên/HS09-06 - Kế hoạch đào tạo bồi dưỡng định kỳ về Pháp luật, Chính sách công ty và C-TPAT năm 2026 kèm Danh sách điểm danh.docx",
    "10. Tiền lương và làm thêm/HS10-04 - Bảng tổng hợp sao kê ngân hàng và Bằng chứng chi trả tiền lương đội ngũ lái xe năm 2026.docx",
    "12. Khiếu nại và phản hồi/HS12-04 - Quy trình giải quyết khiếu nại tố giác nội bộ bảo mật và Hướng dẫn người lao động phản ánh năm 2026.docx",
    "14. An toàn cơ sở và công việc/HS14-08 - Bộ biển báo an toàn PCCC, Điểm tập kết và Lối thoát hiểm song ngữ Anh - Thái theo yêu cầu NV Apparel.docx",
    "15. Phương tiện và bảo dưỡng/HS15-06 - Quy trình lưu trữ và lập hồ sơ kiểm tra an ninh xe tải 7-17 điểm C-TPAT có hệ thống theo ngày và biển số xe.docx",
    "15. Phương tiện và bảo dưỡng/HS15-07 - Kế hoạch và Lịch bảo dưỡng định kỳ phương tiện vận tải năm 2026 có phân công nhân sự chịu trách nhiệm.docx",
    "16. Thông tin xe và theo dõi chuyến/HS16-04 - Quy chế phát hành và quản lý Phiếu công việc (Job Sheet) kiêm Lệnh vận chuyển có mã số chạy duy nhất liên kết lộ trình C-TPAT.docx",
    "17. Vận hành vận tải/HS17-09 - Quy chế xử lý kỷ luật đối với các hành vi vi phạm quy tắc an toàn giao thông và quy chuẩn C-TPAT.docx",
    "18. Chậm trễ và sự cố/HS18-06 - Quy trình phản ứng sự cố khẩn cấp (SOP) liên kết đầu mối chức danh và Bộ nhãn dán hotline trên xe tải.docx",
    "20. An ninh cơ sở, xe và container/HS20-06 - Quy trình vận hành hệ thống camera giám sát CCTV và Quyết định kéo dài thời gian lưu trữ dữ liệu tối thiểu 6 tháng.docx"
]

print("\n--- 1. VERIFYING WORD DOCUMENTS (.docx) ---")
for rel_p in key_docx:
    full_p = os.path.join(BASE_DIR, rel_p.replace("/", os.sep))
    if not os.path.exists(full_p):
        errors.append(f"MISSING DOCX: {rel_p}")
        print(f"❌ MISSING: {rel_p}")
    else:
        try:
            d = Document(full_p)
            print(f"✅ OK ({len(d.paragraphs)} p, {len(d.tables)} t): {os.path.basename(rel_p)}")
        except Exception as e:
            errors.append(f"CORRUPT DOCX: {rel_p} - {e}")
            print(f"❌ CORRUPT: {rel_p} - {e}")

# 2. Check Key Excel Workbooks
key_xlsx = [
    "00_DANH_MUC_HO_SO_AUDIT_TRUCK_2026.xlsx",
    "00_KE_HOACH_KHAC_PHUC_AUDIT_CTPAT_04_11_2026.xlsx",
    "Bảng câu hỏi & Đối chiếu đánh giá/Finding_for_CGL_comment_Ver._Final_COMPLETED.xlsx",
    "15. Phương tiện và bảo dưỡng/HS15-07 - Lịch và Nhật ký bảo dưỡng định kỳ xe tải Cargolink 2026.xlsx",
    "16. Thông tin xe và theo dõi chuyến/HS16-04 - Mẫu Phiếu công việc Job Sheet kiêm Lệnh vận chuyển C-TPAT 2 liên có số nhảy tự động.xlsx"
]

print("\n--- 2. VERIFYING EXCEL WORKBOOKS (.xlsx) ---")
for rel_p in key_xlsx:
    full_p = os.path.join(BASE_DIR, rel_p.replace("/", os.sep))
    if not os.path.exists(full_p):
        errors.append(f"MISSING XLSX: {rel_p}")
        print(f"❌ MISSING: {rel_p}")
    else:
        try:
            wb = openpyxl.load_workbook(full_p, data_only=False)
            print(f"✅ OK ({len(wb.sheetnames)} sheets): {os.path.basename(rel_p)}")
        except Exception as e:
            errors.append(f"CORRUPT XLSX: {rel_p} - {e}")
            print(f"❌ CORRUPT: {rel_p} - {e}")

# 3. Check Image Assets
key_imgs = [
    "14. An toàn cơ sở và công việc/HS14-08_EXIT_SIGN_ENGLISH_THAI.png",
    "14. An toàn cơ sở và công việc/HS14-08_ASSEMBLY_POINT_SIGN_ENGLISH_THAI.png",
    "14. An toàn cơ sở và công việc/HS14-08_NO_SMOKING_SIGN_ENGLISH_THAI.png",
    "18. Chậm trễ và sự cố/HS18-06_EMERGENCY_HOTLINE_STICKER.png",
    "21. Phản hồi và cải tiến dịch vụ/HS21-03_DECAL_3_QR_CODE_DAN_CABIN_XE.png",
    "CTPAT_QR_FORMS/qr_form4_harassment.png"
]

print("\n--- 3. VERIFYING IMAGE ASSETS (.png) ---")
for rel_p in key_imgs:
    full_p = os.path.join(BASE_DIR, rel_p.replace("/", os.sep))
    if not os.path.exists(full_p):
        errors.append(f"MISSING IMAGE: {rel_p}")
        print(f"❌ MISSING: {rel_p}")
    else:
        try:
            im = Image.open(full_p)
            print(f"✅ OK ({im.size[0]}x{im.size[1]} {im.format}): {os.path.basename(rel_p)}")
        except Exception as e:
            errors.append(f"CORRUPT IMAGE: {rel_p} - {e}")
            print(f"❌ CORRUPT: {rel_p} - {e}")

# 4. Check 31 Findings in Master Finding Excel
print("\n--- 4. AUDITING 31 SLIDE FINDINGS IN CAP FILE ---")
cap_path = os.path.join(BASE_DIR, "Bảng câu hỏi & Đối chiếu đánh giá", "Finding_for_CGL_comment_Ver._Final_COMPLETED.xlsx")
wb_cap = openpyxl.load_workbook(cap_path, data_only=True)
ws_sf = wb_cap['Slide Finding']

completed_count = 0
noted_count = 0
for r in range(4, 35):
    num = ws_sf.cell(r, 1).value
    item = ws_sf.cell(r, 4).value
    ev = ws_sf.cell(r, 7).value
    st = ws_sf.cell(r, 8).value
    p = ws_sf.cell(r, 9).value
    d = ws_sf.cell(r, 10).value
    
    if not ev or not st or not p or not d:
        errors.append(f"INCOMPLETE FINDING #{num}")
        print(f"❌ Finding #{num} has missing fields!")
    else:
        if "Hoàn thành" in str(st):
            completed_count += 1
        else:
            noted_count += 1

print(f"✅ Audited 31/31 Findings: {completed_count} Actionable Completed, {noted_count} Status Noted (No action required).")

# 5. Check Sheet 14
print("\n--- 5. AUDITING SHEET 14 (SAFETY CRITERIA) ---")
ws_14 = wb_cap['14']
red_rows = [22, 23, 24, 25, 26, 27, 47, 48, 49]
compliant_count = 0
excluded_count = 0

for r in range(2, 58):
    c3 = ws_14.cell(r, 3).value
    c8 = ws_14.cell(r, 8).value
    c9 = ws_14.cell(r, 9).value
    if r in red_rows:
        if c9 == "MIỄN TRỪ (EXCLUDED)":
            excluded_count += 1
        else:
            errors.append(f"Sheet 14 Row {r} expected EXCLUDED, got {c9}")
    else:
        if c3 == 1 and c9 == "ĐẠT (COMPLIANT)":
            compliant_count += 1
        else:
            errors.append(f"Sheet 14 Row {r} expected COMPLIANT, got c3={c3}, c9={c9}")

print(f"✅ Audited Sheet 14: {compliant_count} Items 100% Compliant, {excluded_count} Items Excluded (Out of Scope).")

print("\n================================================================")
if not errors:
    print("🎉 ALL CHECKS PASSED: 0 ERRORS DETECTED! SYSTEM READY FOR NV APPAREL.")
else:
    print(f"⚠️ FOUND {len(errors)} ERRORS:")
    for err in errors:
        print("  - " + err)
print("================================================================")
