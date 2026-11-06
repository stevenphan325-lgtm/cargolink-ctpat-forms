import os

p = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163\scratch\create_qr_posters.py"
with open(p, 'r', encoding='utf-8') as f:
    c = f.read()

old_cols = """    cols_data = [
        ("Phiếu Đánh Giá Mức Độ Hài Lòng Dịch Vụ CGL", "C-TPAT CUSTOMER SATISFACTION SURVEY", "qr_form1.png", "#071A36", "https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/form1_satisfaction.html"),
        ("NV CTPAT Knowledge Survey", "SECURITY KNOWLEDGE ASSESSMENT", "qr_form2.png", "#D4441E", "https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/form2_knowledge.html"),
        ("NV CTPAT – Suggestions and Complaints", "WHISTLEBLOWER & INCIDENT REPORT", "qr_form3.png", "#0B3C5D", "https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/form3_complaints.html")
    ]"""

new_cols = """    cols_data = [
        ("Đánh Giá Hài Lòng Dịch Vụ CGL", "SERVICE SATISFACTION (EVERY 3 MONTHS)", "qr_form1.png", "#071A36", "https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/form1_satisfaction.html"),
        ("NV CTPAT Knowledge Survey", "SECURITY KNOWLEDGE ASSESSMENT", "qr_form2.png", "#D4441E", "https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/form2_knowledge.html"),
        ("Hộp Thư Góp Ý & Khiếu Nại NV", "FOR YOUR TRUCK DRIVER ONLY", "qr_form3.png", "#0B3C5D", "https://docs.google.com/forms/d/1WDy9kSA-TzIavBlsSNgcMvU4Wcm0p8yomeZPZ-HgOzo/viewform")
    ]"""

if old_cols in c:
    c = c.replace(old_cols, new_cols)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print("SUCCESS: Updated cols_data in create_qr_posters.py")
else:
    print("Target cols_data not matched")
