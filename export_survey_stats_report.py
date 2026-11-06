import os, sys, json
from datetime import datetime
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026"
FORMS_DIR = os.path.join(BASE_DIR, "CTPAT_QR_FORMS")
SUBMISSIONS_FILE = os.path.join(FORMS_DIR, "submissions.json")
REPORT_EXCEL = os.path.join(BASE_DIR, "21. Phản hồi và cải tiến dịch vụ", "HS21-02 - Báo cáo tổng hợp kết quả đánh giá hài lòng khách hàng NV và khảo sát C-TPAT.xlsx")

def export_report():
    if not os.path.exists(SUBMISSIONS_FILE):
        print("No submissions found yet.")
        return

    with open(SUBMISSIONS_FILE, 'r', encoding='utf-8') as f:
        records = json.load(f)

    wb = openpyxl.Workbook()
    
    # ------------------ SHEET 1: TỔNG HỢP CSAT ------------------
    ws1 = wb.active
    ws1.title = "1. Danh gia Hai long (CSAT)"
    ws1.views.sheetView[0].showGridLines = True

    header_font = Font(name="Times New Roman", size=11, bold=True, color="FFFFFF")
    navy_fill = PatternFill(start_color="071A36", end_color="071A36", fill_type="solid")
    center = Alignment(horizontal="center", vertical="center", wrap_text=True)
    left = Alignment(horizontal="left", vertical="center", wrap_text=True)
    thin_border = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )

    # Title block
    ws1.merge_cells("A1:K1")
    ws1["A1"] = "BÁO CÁO THỐNG KÊ MỨC ĐỘ HÀI LÒNG KHÁCH HÀNG (CSAT) - TUYẾN NV APPAREL"
    ws1["A1"].font = Font(name="Times New Roman", size=14, bold=True, color="071A36")
    ws1["A1"].alignment = center

    headers1 = [
        "STT", "Mã Phiếu", "Thời Gian", "Bộ Phận (NV)", "Người Đánh Giá", 
        "Số Xe CGL", "Đúng Giờ (OTD)", "Seal Chì", "Tài Xế", "Tình Trạng Xe", "ĐTB (Sao)"
    ]
    for col_idx, text in enumerate(headers1, start=1):
        cell = ws1.cell(row=3, column=col_idx, value=text)
        cell.font = header_font
        cell.fill = navy_fill
        cell.alignment = center
        cell.border = thin_border

    row_cur = 4
    stt = 1
    for r in records:
        if r.get("form_type") == "satisfaction_survey":
            ratings = r.get("ratings", {})
            otd = ratings.get("otd", 5)
            seal = ratings.get("seal", 5)
            driver = ratings.get("driver", 5)
            truck = ratings.get("truck", 5)
            avg = round((otd + seal + driver + truck) / 4, 1)

            vals = [
                stt,
                r.get("reference_code", "N/A"),
                r.get("eval_date") or r.get("submitted_at", "")[:10],
                r.get("department", "Kho NV Apparel"),
                r.get("evaluator_name", "Ẩn danh"),
                r.get("truck_plate", "51C-964.55"),
                otd, seal, driver, truck, avg
            ]
            for col_idx, val in enumerate(vals, start=1):
                cell = ws1.cell(row=row_cur, column=col_idx, value=val)
                cell.font = Font(name="Times New Roman", size=10)
                cell.alignment = center if col_idx in [1, 2, 3, 6, 7, 8, 9, 10, 11] else left
                cell.border = thin_border
            row_cur += 1
            stt += 1

    # Auto column width
    for col in ws1.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = openpyxl.utils.get_column_letter(col[0].column)
        ws1.column_dimensions[col_letter].width = max(max_len + 4, 12)

    os.makedirs(os.path.dirname(REPORT_EXCEL), exist_ok=True)
    wb.save(REPORT_EXCEL)
    print(f"[SUCCESS] Exported survey statistics report to: {REPORT_EXCEL}")

if __name__ == "__main__":
    export_report()
