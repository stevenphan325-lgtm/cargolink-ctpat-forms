# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
brain_dir = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163"
artifact_file = os.path.join(brain_dir, "cargolink_driver_staff_qr_portal.html")

with open(artifact_file, "r", encoding="utf-8") as f:
    html = f.read()

# Add new tab button
old_tabs = """    <button class="tab-btn active" onclick="switchTab(0)">📱 1. Toàn Bộ 10 Sổ Tay Số & Mã QR (Scan & Đọc)</button>
    <button class="tab-btn" onclick="switchTab(1)">📋 2. Bản Chất Pháp Lý & Quy Định "Lưu Hành Nội Bộ"</button>
    <button class="tab-btn" onclick="switchTab(2)">📊 3. Bảng Rà Soát & Đối Chiếu Toàn Bộ Hồ Sơ</button>
    <button class="tab-btn" onclick="switchTab(3)">🚨 4. Đường Dây Nóng Khẩn Cấp 24/7</button>"""

new_tabs = """    <button class="tab-btn active" onclick="switchTab(0)">🛠️ 1. 10 Công Cụ Vận Hành Số Hóa & Biểu Mẫu Điện Tử</button>
    <button class="tab-btn" onclick="switchTab(1)">📱 2. 10 Sổ Tay Số & Chính Sách Nội Bộ</button>
    <button class="tab-btn" onclick="switchTab(2)">📋 3. Pháp Lý & Lưu Hành Nội Bộ (NĐ 13/2023)</button>
    <button class="tab-btn" onclick="switchTab(3)">📊 4. Đối Chiếu Rà Soát Toàn Bộ 134 Hồ Sơ</button>
    <button class="tab-btn" onclick="switchTab(4)">🚨 5. Đường Dây Nóng Khẩn Cấp 24/7</button>"""

if old_tabs in html:
    html = html.replace(old_tabs, new_tabs)

# Content for 10 Operational Tools
tab_tools_html = """  <!-- TAB 0: 10 CÔNG CỤ VẬN HÀNH SỐ HÓA -->
  <div id="tab0" class="tab-content active">
    <div style="background: white; border: 2px solid var(--accent); border-radius: 12px; padding: 18px 24px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
      <div>
        <span style="background: var(--accent); color: white; font-size: 10.5px; font-weight: 700; padding: 2px 8px; border-radius: 10px; text-transform: uppercase;">100% PAPERLESS AUDIT READY</span>
        <h2 style="font-size: 18px; color: var(--primary); margin: 4px 0;">BỘ CÔNG CỤ VẬN HÀNH SỐ HÓA & BIỂU MẪU ĐIỆN TỬ CARGOLINK</h2>
        <p style="font-size: 13px; color: #475569;">Số hóa toàn bộ quy trình kiểm tra xe, seal VVTT, đo nồng độ cồn, báo cáo sự cố 15 phút, lệnh điều xe và tự kiểm toán C-TPAT có chữ ký số điện tử.</p>
      </div>
      <a href="https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/portal_driver.html#operational-tools" target="_blank" class="btn-link accent" style="padding: 10px 18px; font-size: 13px;">MỞ TRÊN ĐIỆN THOẠI ➔</a>
    </div>

    <div class="grid-qr">
      <!-- Tool 1 -->
      <div class="qr-card">
        <div>
          <span style="font-size: 11px; font-weight: 700; color: #D4441E;">🚚 WI-SEC-001 / HS16-01</span>
          <h3 style="font-size: 14.5px; color: var(--primary); margin: 4px 0 6px 0;">Kiểm Tra Xe 7 Điểm & 17 Điểm</h3>
        </div>
        <div class="qr-box">
          <img src="qr_app1_inspection.png" alt="QR App 1">
          <div class="qr-info">
            <strong>Checklist kiểm an ninh xe tải</strong>
            Lốp xe, gầm xe, bình dầu, cabin, chốt cửa, vách thùng trước khi xuất bãi và bốc hàng NV.
          </div>
        </div>
        <a href="https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/app_vehicle_inspection.html" target="_blank" class="btn-link">Mở Phiếu Kiểm Tra Xe ➔</a>
      </div>

      <!-- Tool 2 -->
      <div class="qr-card">
        <div>
          <span style="font-size: 11px; font-weight: 700; color: #1E3A8A;">🔒 HS17-06 / ISO 17712</span>
          <h3 style="font-size: 14.5px; color: var(--primary); margin: 4px 0 6px 0;">Kiểm Tra Seal VVTT & Cắt Seal</h3>
        </div>
        <div class="qr-box">
          <img src="qr_app2_seal.png" alt="QR App 2">
          <div class="qr-info">
            <strong>4 Bước Chuẩn Seal VVTT</strong>
            View (Nhìn) - Verify (So khớp) - Tug (Giật kéo) - Twist (Xoay). Đại diện Kho NV & Tài xế ký số.
          </div>
        </div>
        <a href="https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/app_seal_vvtt_log.html" target="_blank" class="btn-link accent">Mở Biên Bản Seal VVTT ➔</a>
      </div>

      <!-- Tool 3 -->
      <div class="qr-card">
        <div>
          <span style="font-size: 11px; font-weight: 700; color: #059669;">🛡️ HS03-05 / ISO 39001</span>
          <h3 style="font-size: 14.5px; color: var(--primary); margin: 4px 0 6px 0;">Nồng Độ Cồn 0.00 & Test Ma Túy</h3>
        </div>
        <div class="qr-box">
          <img src="qr_app3_alcohol.png" alt="QR App 3">
          <div class="qr-info">
            <strong>Kiểm soát 100% trước giờ chạy</strong>
            Nồng độ cồn hơi thở tuyệt đối 0.00 mg/L và que test nhanh sàng lọc 5 chất ma túy âm tính (-).
          </div>
        </div>
        <a href="https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/app_alcohol_test_log.html" target="_blank" class="btn-link" style="background: #059669;">Mở Sổ Kiểm Tra Cồn ➔</a>
      </div>

      <!-- Tool 4 -->
      <div class="qr-card" style="border-color: #FCA5A5;">
        <div>
          <span style="font-size: 11px; font-weight: 700; color: #DC2626;">🚨 HS18-01 / WI-PRT-001</span>
          <h3 style="font-size: 14.5px; color: #991B1B; margin: 4px 0 6px 0;">Báo Cáo Sự Cố Chậm ETA 15 Phút</h3>
        </div>
        <div class="qr-box" style="background: #FEF2F2;">
          <img src="qr_app4_incident.png" alt="QR App 4">
          <div class="qr-info">
            <strong style="color: #991B1B;">Kích hoạt trong 15 phút</strong>
            Trễ hẹn >15p, hỏng máy, seal đứt, nghi ngờ bám đuôi. Lấy tọa độ GPS tự động + Gọi hotline 24/7.
          </div>
        </div>
        <a href="https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/app_incident_rapid_report.html" target="_blank" class="btn-link" style="background: #DC2626;">Phát Báo Cáo Sự Cố ➔</a>
      </div>

      <!-- Tool 5 -->
      <div class="qr-card">
        <div>
          <span style="font-size: 11px; font-weight: 700; color: #0B3C5D;">📋 HS16-01 / DISPATCH</span>
          <h3 style="font-size: 14.5px; color: var(--primary); margin: 4px 0 6px 0;">Lệnh Điều Xe Tuyến NV Apparel</h3>
        </div>
        <div class="qr-box">
          <img src="qr_app5_dispatch.png" alt="QR App 5">
          <div class="qr-info">
            <strong>Giám sát hành trình trực tuyến</strong>
            Cấp lệnh điều xe điện tử, lộ trình cố định Nhà máy NV - Cảng, trạm dừng phê duyệt C-TPAT.
          </div>
        </div>
        <a href="https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/app_trip_dispatch_log.html" target="_blank" class="btn-link">Mở Lệnh Điều Xe ➔</a>
      </div>

      <!-- Tool 6 -->
      <div class="qr-card">
        <div>
          <span style="font-size: 11px; font-weight: 700; color: #D97706;">🧯 HS14-01 / ISO 45001</span>
          <h3 style="font-size: 14.5px; color: var(--primary); margin: 4px 0 6px 0;">Kiểm Tra PCCC & Bảo Hộ (PPE) Xe</h3>
        </div>
        <div class="qr-box">
          <img src="qr_app6_ppe.png" alt="QR App 6">
          <div class="qr-info">
            <strong>An toàn thiết bị trên xe</strong>
            Bình chữa cháy MFZ4 cabin & thùng xe (áp kế xanh), tam giác phản quang, túi cứu thương, nón bảo hộ.
          </div>
        </div>
        <a href="https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/app_ppe_pccc_log.html" target="_blank" class="btn-link">Mở Sổ Kiểm Tra PCCC ➔</a>
      </div>

      <!-- Tool 7 -->
      <div class="qr-card">
        <div>
          <span style="font-size: 11px; font-weight: 700; color: #475569;">🏷️ HS13-01 / CỔNG BÃI XE</span>
          <h3 style="font-size: 14.5px; color: var(--primary); margin: 4px 0 6px 0;">Sổ Kiểm Soát Cổng Ra Vào Bãi Xe</h3>
        </div>
        <div class="qr-box">
          <img src="qr_app7_visitor.png" alt="QR App 7">
          <div class="qr-info">
            <strong>Kiểm soát khách & xe ngoài</strong>
            Đăng ký CCCD khách, đơn vị công tác, biển số xe, cấp phát thẻ khách C-TPAT và ghi giờ ra/vào.
          </div>
        </div>
        <a href="https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/app_visitor_gate_log.html" target="_blank" class="btn-link">Mở Sổ Nhật Ký Cổng ➔</a>
      </div>

      <!-- Tool 8 -->
      <div class="qr-card">
        <div>
          <span style="font-size: 11px; font-weight: 700; color: #166534;">🌿 HS01-02 / ISO 14001</span>
          <h3 style="font-size: 14.5px; color: var(--primary); margin: 4px 0 6px 0;">Sổ Năng Lượng & Văn Phòng Xanh</h3>
        </div>
        <div class="qr-box" style="background: #F0FDF4;">
          <img src="qr_app8_green.png" alt="QR App 8">
          <div class="qr-info">
            <strong>Đo lường phát thải carbon</strong>
            Ghi nhận điện (kWh), nước sạch (m³), giấy in A4, rác tái chế và định mức dầu xe để tự động tính KPI.
          </div>
        </div>
        <a href="https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/app_green_office_log.html" target="_blank" class="btn-link" style="background: #059669;">Mở Sổ Văn Phòng Xanh ➔</a>
      </div>

      <!-- Tool 9 -->
      <div class="qr-card">
        <div>
          <span style="font-size: 11px; font-weight: 700; color: #4338CA;">🤝 HS02-01 / ĐỐI TÁC C-TPAT</span>
          <h3 style="font-size: 14.5px; color: var(--primary); margin: 4px 0 6px 0;">Đánh Giá Năng Lực Nhà Xe Phụ</h3>
        </div>
        <div class="qr-box">
          <img src="qr_app9_subcontractor.png" alt="QR App 9">
          <div class="qr-info">
            <strong>Thang điểm 100 thẩm định thầu phụ</strong>
            GPKD, bảo hiểm hàng hóa, 100% xe GPS trực tuyến, hồ sơ tư pháp lái xe, cam kết niêm phong seal.
          </div>
        </div>
        <a href="https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/app_subcontractor_eval.html" target="_blank" class="btn-link">Mở Đánh Giá Thầu Phụ ➔</a>
      </div>

      <!-- Tool 10 -->
      <div class="qr-card" style="border: 2px solid #0B3C5D;">
        <div>
          <span style="font-size: 11px; font-weight: 700; color: #1D4ED8;">🏆 C-TPAT AUDIT READY</span>
          <h3 style="font-size: 14.5px; color: var(--primary); margin: 4px 0 6px 0;">Checklist Tự Kiểm Toán C-TPAT</h3>
        </div>
        <div class="qr-box" style="background: #EFF6FF;">
          <img src="qr_app10_audit.png" alt="QR App 10">
          <div class="qr-info">
            <strong>12 Tiêu chuẩn tiếp đoàn thanh tra</strong>
            Đối chiếu toàn diện 12 tiêu chí an ninh chuỗi cung ứng, tự động chấm % sẵn sàng và lập Action Plan.
          </div>
        </div>
        <a href="https://stevenphan325-lgtm.github.io/cargolink-ctpat-forms/app_ctpat_audit_checklist.html" target="_blank" class="btn-link accent">Mở Checklist Tự Kiểm Toán ➔</a>
      </div>
    </div>
  </div>
"""

# Re-index existing tabs:
# tab0 -> tab1
# tab1 -> tab2
# tab2 -> tab3
# tab3 -> tab4
html = html.replace('id="tab0" class="tab-content active"', 'id="tab1" class="tab-content"')
html = html.replace('id="tab1" class="tab-content"', 'id="tab2" class="tab-content"')
html = html.replace('id="tab2" class="tab-content"', 'id="tab3" class="tab-content"')
html = html.replace('id="tab3" class="tab-content"', 'id="tab4" class="tab-content"')

# Insert tab_tools_html right before id="tab1"
if '<!-- TAB 0: 10 CÔNG CỤ VẬN HÀNH SỐ HÓA -->' not in html:
    html = html.replace('<div id="tab1" class="tab-content">', tab_tools_html + '\n  <div id="tab1" class="tab-content">')

with open(artifact_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated cargolink_driver_staff_qr_portal.html artifact successfully with 10 Digital Operational Tools tab!")
