import os

forms_dir = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS"
docs = [
    'doc_ctpat_inspection.html', 'doc_emergency_sop.html', 'doc_traffic_safety.html',
    'doc_green_office.html', 'doc_whistleblower.html', 'doc_staff_handbook.html'
]

banner_html = """  <div style="background: #FEF3C7; border: 1.5px dashed #D97706; color: #92400E; padding: 10px 14px; border-radius: 8px; font-size: 12px; font-weight: 700; text-align: center; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.5px;">🔒 TÀI LIỆU LƯU HÀNH NỘI BỘ — CARGOLINK EXPRESS VIỆT NAM (INTERNAL USE ONLY)</div>
"""

disclaimer_html = """  <div style="background: #F1F5F9; border-left: 4px solid #071A36; padding: 12px 16px; border-radius: 6px; font-size: 12px; color: #475569; margin-top: 20px; line-height: 1.5;">
    <strong>THÔNG BÁO BẢO MẬT & LƯU HÀNH NỘI BỘ:</strong><br>
    Tài liệu này thuộc bản quyền của CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM. Toàn thể cán bộ nhân viên và lái xe có nghĩa vụ đọc hiểu, ký cam kết tuân thủ khi ký hợp đồng lao động và định kỳ hàng năm. Nghiêm cấm sao chép, trích dẫn hoặc chuyển giao cho các đơn vị bên ngoài khi chưa được Ban Giám đốc chấp thuận.
  </div>
"""

for d in docs:
    p = os.path.join(forms_dir, d)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        if 'TÀI LIỆU LƯU HÀNH NỘI BỘ' not in c:
            c = c.replace('<body>', '<body>\n' + banner_html, 1)
            # Insert disclaimer right before <div class="footer">
            if '<div class="footer">' in c:
                c = c.replace('<div class="footer">', disclaimer_html + '\n  <div class="footer">', 1)
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f'Updated {d} with internal circulation banner and disclaimer')
        else:
            print(f'{d} already has banner')
