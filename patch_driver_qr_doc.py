import os

doc_script = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS\create_driver_qr_doc.py"
with open(doc_script, 'r', encoding='utf-8') as f:
    c = f.read()

# Update QR 12 definition
old_qr12 = """        ("Mã QR 12", "form3_complaints.html", "qr_form3.png",
         "KÊNH GÓP Ý, KHIẾU NẠI & TỐ GIÁC ẨN DANH 24/7",
         "Kênh gửi ý kiến đóng góp, phản ánh chậm ETA và tố giác vi phạm an ninh ẩn danh. Tự động cấp mã Ticket ID tra cứu.")"""

new_qr12 = """        ("Mã QR 12", "form3_complaints.html", "qr_form3.png",
         "HỘP THƯ GÓP Ý & KHIẾU NẠI C-TPAT NV (FOR TRUCK DRIVER ONLY)",
         "Biểu mẫu Google Form chính thức của NV Apparel dành riêng cho Tài xế xe tải (For your truck Driver only) gửi góp ý và tố giác an ninh.")"""

if old_qr12 in c:
    c = c.replace(old_qr12, new_qr12)
    with open(doc_script, 'w', encoding='utf-8') as f:
        f.write(c)
    print("SUCCESS: Updated QR 12 in create_driver_qr_doc.py")
else:
    print("QR 12 not matched exactly")
