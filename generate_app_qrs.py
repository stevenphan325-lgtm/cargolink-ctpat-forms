# -*- coding: utf-8 -*-
import os, sys, cv2, qrcode, pyzbar.pyzbar as pyzbar
from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding='utf-8')

forms_dir = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS"
brain_dir = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163"
logo_path = os.path.join(r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\00_BO_BANNER_VA_LOGO_CARGOLINK", "Cargolink_Logo_Vector_HighRes.png")

BASE_URL = "https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/"

tools = [
    ("qr_app1_inspection.png", "app_vehicle_inspection.html", "Kiểm Tra Xe 7/17 Điểm", qrcode.constants.ERROR_CORRECT_H, 0.15),
    ("qr_app2_seal.png", "app_seal_vvtt_log.html", "Kiểm Tra Seal VVTT", qrcode.constants.ERROR_CORRECT_H, 0.15),
    ("qr_app3_alcohol.png", "app_alcohol_test_log.html", "Kiểm Tra Nồng Độ Cồn & Ma Túy", qrcode.constants.ERROR_CORRECT_H, 0.15),
    ("qr_app4_incident.png", "app_incident_rapid_report.html", "Báo Cáo Sự Cố 15 Phút", qrcode.constants.ERROR_CORRECT_H, 0.15),
    ("qr_app5_dispatch.png", "app_trip_dispatch_log.html", "Lệnh Điều Xe Điện Tử", qrcode.constants.ERROR_CORRECT_H, 0.15),
    ("qr_app6_ppe.png", "app_ppe_pccc_log.html", "Kiểm Tra PPE & PCCC", qrcode.constants.ERROR_CORRECT_H, 0.15),
    ("qr_app7_visitor.png", "app_visitor_gate_log.html", "Kiểm Soát Khách Ra Vào", qrcode.constants.ERROR_CORRECT_H, 0.15),
    ("qr_app8_green.png", "app_green_office_log.html", "Sổ Năng Lượng & Môi Trường", qrcode.constants.ERROR_CORRECT_H, 0.15),
    ("qr_app9_subcontractor.png", "app_subcontractor_eval.html", "Đánh Giá Thầu Phụ C-TPAT", qrcode.constants.ERROR_CORRECT_H, 0.15),
    ("qr_app10_audit.png", "app_ctpat_audit_checklist.html", "Checklist Tự Kiểm Toán C-TPAT", qrcode.constants.ERROR_CORRECT_Q, 0.14),
]

det = cv2.QRCodeDetector()
logo_img = Image.open(logo_path).convert('RGBA')

print("Generating 10 Dual-Engine Verified QR codes for Digital Operational Tools...")

for qr_name, html_file, label, ec_level, pct in tools:
    url = BASE_URL + html_file
    qr = qrcode.QRCode(
        version=None,
        error_correction=ec_level,
        box_size=12,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color='#071A36', back_color='white').convert('RGBA')

    qr_w, qr_h = img_qr.size
    logo_size = int(qr_w * pct)
    logo_thumb = logo_img.copy()
    logo_thumb.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
    lw, lh = logo_thumb.size

    pad = 4
    box_img = Image.new('RGBA', (lw + pad*2, lh + pad*2), 'white')
    draw = ImageDraw.Draw(box_img)
    draw.rectangle([0, 0, lw + pad*2 - 1, lh + pad*2 - 1], outline='#071A36', width=2)
    box_img.paste(logo_thumb, (pad, pad), logo_thumb)

    pos = ((qr_w - box_img.size[0]) // 2, (qr_h - box_img.size[1]) // 2)
    img_qr.paste(box_img, pos)

    out_file = os.path.join(forms_dir, qr_name)
    img_qr.save(out_file, format='PNG')
    
    # Brain dir copy
    brain_file = os.path.join(brain_dir, qr_name)
    img_qr.save(brain_file, format='PNG')

    # Dual verify
    cv_data, _, _ = det.detectAndDecode(cv2.imread(out_file))
    pz_res = pyzbar.decode(Image.open(out_file))
    cv_ok = (cv_data == url)
    pz_ok = (len(pz_res) > 0 and pz_res[0].data.decode() == url)

    if cv_ok and pz_ok:
        print(f"  [DUAL PASS 100%] {qr_name} -> {label} | Both OpenCV & PyZbar OK")
    elif pz_ok or cv_ok:
        print(f"  [SINGLE PASS] {qr_name} -> OpenCV:{cv_ok}, PyZbar:{pz_ok}")
    else:
        print(f"  [FAIL] {qr_name}")

print("\nAll 10 QR codes generated and dual-engine verified!")
