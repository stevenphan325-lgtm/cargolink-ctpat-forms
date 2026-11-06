import os, sys, qrcode
from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding='utf-8')

forms_dir = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS"
logo_path = os.path.join(r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\00_BO_BANNER_VA_LOGO_CARGOLINK", "Cargolink_Logo_Vector_HighRes.png")

# Google Form URL from client
target_url = "https://docs.google.com/forms/d/1WDy9kSA-TzIavBlsSNgcMvU4Wcm0p8yomeZPZ-HgOzo/viewform"

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4,
)
qr.add_data(target_url)
qr.make(fit=True)
img_qr = qr.make_image(fill_color='#071A36', back_color='white').convert('RGBA')

if os.path.exists(logo_path):
    logo_img = Image.open(logo_path).convert('RGBA')
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

out_path = os.path.join(forms_dir, "qr_form3.png")
img_qr.save(out_path, format='PNG')
print(f"Generated new qr_form3.png pointing directly to: {target_url}")
