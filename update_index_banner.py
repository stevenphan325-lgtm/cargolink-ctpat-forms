import os

index_file = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS\index.html"
with open(index_file, 'r', encoding='utf-8') as f:
    content = f.read()

banner = """  <!-- Banner chuyển sang Cổng Tra cứu Tài xế & CBNV -->
  <div style="background: linear-gradient(135deg, #1E293B, #0F172A); color: white; border-radius: 12px; padding: 18px 24px; margin-bottom: 28px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
    <div>
      <span style="background: #D4441E; color: white; font-size: 10.5px; font-weight: 700; padding: 3px 10px; border-radius: 12px; text-transform: uppercase;">DÀNH CHO TÀI XẾ & CBNV</span>
      <h3 style="font-size: 16px; font-weight: 800; margin-top: 6px;">CỔNG TRA CỨU SỔ TAY ĐIỆN TỬ & CHÍNH SÁCH AN NINH C-TPAT</h3>
      <p style="font-size: 12.5px; opacity: 0.85; margin-top: 2px;">6 Cẩm nang số: Kiểm tra xe 7/17 điểm, Seal VVTT, Sự cố khẩn cấp WI-PRT-001, Văn phòng xanh, An toàn giao thông.</p>
    </div>
    <a href="portal_driver.html" style="background: #D4441E; color: white; text-decoration: none; padding: 10px 18px; border-radius: 8px; font-weight: 700; font-size: 13px; white-space: nowrap;">MỞ CỔNG TÀI XẾ & CBNV ➔</a>
  </div>
"""

target = '<div class="grid">'
if "portal_driver.html" not in content and target in content:
    content = content.replace(target, banner + "\n  " + target, 1)
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("SUCCESS: index.html banner updated!")
else:
    print("ALREADY UPDATED or TARGET NOT FOUND")
