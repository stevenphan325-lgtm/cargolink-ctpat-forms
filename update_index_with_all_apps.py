# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
forms_dir = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS"
index_path = os.path.join(forms_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Upgraded tools grid snippet for index.html
tools_grid_index = """
  <!-- SECTION: 10 DIGITAL OPERATIONAL TOOLS -->
  <div style="background: white; border-radius: 16px; border: 1.5px solid var(--border); padding: 24px; margin-bottom: 28px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03);">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px; border-bottom: 2px solid #E2E8F0; padding-bottom: 12px;">
      <div>
        <span style="background: #E0E7FF; color: #3730A3; font-size: 11px; font-weight: 800; padding: 3px 10px; border-radius: 12px; text-transform: uppercase;">SỐ HÓA HOÀN TOÀN KHÔNG DÙNG GIẤY</span>
        <h2 style="font-size: 18px; font-weight: 800; color: var(--primary); margin-top: 4px;">🛠️ BỘ CÔNG CỤ VẬN HÀNH SỐ HÓA & BIỂU MẪU ĐIỆN TỬ (DIGITAL APPS)</h2>
      </div>
      <a href="portal_driver.html#operational-tools" style="background: var(--primary); color: white; text-decoration: none; padding: 8px 14px; border-radius: 6px; font-size: 12.5px; font-weight: 700;">Xem chi tiết tại Cổng Tra Cứu ➔</a>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px;">
      <a href="app_vehicle_inspection.html" style="text-decoration: none; background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 10px; padding: 14px; color: var(--text-main); display: block; transition: 0.15s;">
        <div style="font-size: 11px; font-weight: 700; color: var(--accent); text-transform: uppercase;">🚚 KIỂM TRA PHƯƠNG TIỆN</div>
        <div style="font-weight: 800; font-size: 13.5px; margin: 4px 0; color: var(--primary);">Kiểm Tra Xe 7 & 17 Điểm</div>
        <div style="font-size: 12px; color: #64748B;">Checklist an ninh xe tải có chữ ký điện tử</div>
      </a>

      <a href="app_seal_vvtt_log.html" style="text-decoration: none; background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 10px; padding: 14px; color: var(--text-main); display: block; transition: 0.15s;">
        <div style="font-size: 11px; font-weight: 700; color: #1E3A8A; text-transform: uppercase;">🔒 QUẢN LÝ NIÊM PHONG</div>
        <div style="font-weight: 800; font-size: 13.5px; margin: 4px 0; color: var(--primary);">Kiểm Tra Seal VVTT & Cắt Seal</div>
        <div style="font-size: 12px; color: #64748B;">4 bước View-Verify-Tug-Twist chuẩn C-TPAT</div>
      </a>

      <a href="app_alcohol_test_log.html" style="text-decoration: none; background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 10px; padding: 14px; color: var(--text-main); display: block; transition: 0.15s;">
        <div style="font-size: 11px; font-weight: 700; color: #059669; text-transform: uppercase;">🛡️ AN TOÀN GIAO THÔNG</div>
        <div style="font-weight: 800; font-size: 13.5px; margin: 4px 0; color: var(--primary);">Nồng Độ Cồn 0.00 & Ma Túy</div>
        <div style="font-size: 12px; color: #64748B;">Kiểm soát 100% tài xế trước xuất bến</div>
      </a>

      <a href="app_incident_rapid_report.html" style="text-decoration: none; background: #FEF2F2; border: 1px solid #FCA5A5; border-radius: 10px; padding: 14px; color: var(--text-main); display: block; transition: 0.15s;">
        <div style="font-size: 11px; font-weight: 700; color: #DC2626; text-transform: uppercase;">🚨 BÁO CÁO 15 PHÚT</div>
        <div style="font-weight: 800; font-size: 13.5px; margin: 4px 0; color: #991B1B;">Sự Cố & Chậm ETA Khẩn Cấp</div>
        <div style="font-size: 12px; color: #7F1D1D;">Định vị GPS tự động + Gọi cứu hộ 24/7</div>
      </a>

      <a href="app_trip_dispatch_log.html" style="text-decoration: none; background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 10px; padding: 14px; color: var(--text-main); display: block; transition: 0.15s;">
        <div style="font-size: 11px; font-weight: 700; color: var(--primary-light); text-transform: uppercase;">📋 ĐIỀU ĐỘ XE</div>
        <div style="font-weight: 800; font-size: 13.5px; margin: 4px 0; color: var(--primary);">Lệnh Điều Xe Tuyến NV</div>
        <div style="font-size: 12px; color: #64748B;">Giám sát lộ trình, trạm dừng phê duyệt</div>
      </a>

      <a href="app_ppe_pccc_log.html" style="text-decoration: none; background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 10px; padding: 14px; color: var(--text-main); display: block; transition: 0.15s;">
        <div style="font-size: 11px; font-weight: 700; color: #D97706; text-transform: uppercase;">🧯 PCCC & BẢO HỘ</div>
        <div style="font-weight: 800; font-size: 13.5px; margin: 4px 0; color: var(--primary);">Kiểm Tra PPE & PCCC Xe</div>
        <div style="font-size: 12px; color: #64748B;">Bình chữa cháy, túi cứu thương, nón bảo hộ</div>
      </a>

      <a href="app_visitor_gate_log.html" style="text-decoration: none; background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 10px; padding: 14px; color: var(--text-main); display: block; transition: 0.15s;">
        <div style="font-size: 11px; font-weight: 700; color: #475569; text-transform: uppercase;">🏷️ AN NINH CỔNG</div>
        <div style="font-weight: 800; font-size: 13.5px; margin: 4px 0; color: var(--primary);">Nhật Ký Khách Ra Vào Bãi</div>
        <div style="font-size: 12px; color: #64748B;">Cấp phát thẻ khách C-TPAT, ghi nhận giờ ra vào</div>
      </a>

      <a href="app_green_office_log.html" style="text-decoration: none; background: #F0FDF4; border: 1px solid #86EFAC; border-radius: 10px; padding: 14px; color: var(--text-main); display: block; transition: 0.15s;">
        <div style="font-size: 11px; font-weight: 700; color: #166534; text-transform: uppercase;">🌿 VĂN PHÒNG XANH</div>
        <div style="font-weight: 800; font-size: 13.5px; margin: 4px 0; color: #064E3B;">Sổ Năng Lượng & Môi Trường</div>
        <div style="font-size: 12px; color: #15803D;">Theo dõi điện, nước, giấy in, giảm phát thải</div>
      </a>

      <a href="app_subcontractor_eval.html" style="text-decoration: none; background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 10px; padding: 14px; color: var(--text-main); display: block; transition: 0.15s;">
        <div style="font-size: 11px; font-weight: 700; color: #4338CA; text-transform: uppercase;">🤝 THẦU PHỤ C-TPAT</div>
        <div style="font-weight: 800; font-size: 13.5px; margin: 4px 0; color: var(--primary);">Đánh Giá Nhà Xe Phụ</div>
        <div style="font-size: 12px; color: #64748B;">Thang điểm 100 thẩm định an ninh đối tác</div>
      </a>

      <a href="app_ctpat_audit_checklist.html" style="text-decoration: none; background: #EFF6FF; border: 1.5px solid #60A5FA; border-radius: 10px; padding: 14px; color: var(--text-main); display: block; transition: 0.15s;">
        <div style="font-size: 11px; font-weight: 700; color: #1D4ED8; text-transform: uppercase;">🏆 SẴN SÀNG KIỂM TOÁN</div>
        <div style="font-weight: 800; font-size: 13.5px; margin: 4px 0; color: var(--primary);">Checklist Tự Kiểm Toán C-TPAT</div>
        <div style="font-size: 12px; color: #1E40AF;">Đối chiếu 12 tiêu chuẩn tiếp đoàn NV Apparel</div>
      </a>
    </div>
  </div>
"""

# Insert before footer in index.html
if "<!-- SECTION: 10 DIGITAL OPERATIONAL TOOLS -->" not in content:
    content = content.replace('<div class="footer">', tools_grid_index + '\n  <div class="footer">')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html with 10 Digital Operational Tools section successfully!")
