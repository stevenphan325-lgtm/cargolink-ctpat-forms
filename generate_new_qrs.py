import os, sys, qrcode
from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding='utf-8')

forms_dir = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS"
logo_path = os.path.join(r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\00_BO_BANNER_VA_LOGO_CARGOLINK", "Cargolink_Logo_Vector_HighRes.png")

targets = {
    'qr_doc7_labor.png': 'https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/doc_labor_salary_rules.html',
    'qr_doc8_csr.png': 'https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/doc_csr_human_rights.html',
    'qr_doc9_cyber.png': 'https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/doc_cyber_route_security.html',
    'qr_doc10_pccc.png': 'https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/doc_occupational_safety_pccc.html',
}

has_logo = os.path.exists(logo_path)
if has_logo:
    logo_img = Image.open(logo_path).convert('RGBA')

for fname, url in targets.items():
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img_qr = qr.make_image(fill_color='#071A36', back_color='white').convert('RGBA')
    
    if has_logo:
        qr_w, qr_h = img_qr.size
        logo_size = int(qr_w * 0.16)
        logo_thumb = logo_img.copy()
        logo_thumb.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
        lw, lh = logo_thumb.size
        
        pad = 6
        box_img = Image.new('RGBA', (lw + pad*2, lh + pad*2), 'white')
        draw = ImageDraw.Draw(box_img)
        draw.rectangle([0, 0, lw + pad*2 - 1, lh + pad*2 - 1], outline='#071A36', width=2)
        box_img.paste(logo_thumb, (pad, pad), logo_thumb)
        
        pos = ((qr_w - box_img.size[0]) // 2, (qr_h - box_img.size[1]) // 2)
        img_qr.paste(box_img, pos)
        
    out_path = os.path.join(forms_dir, fname)
    img_qr.save(out_path, format='PNG')
    print(f'Generated: {fname} -> {url}')
