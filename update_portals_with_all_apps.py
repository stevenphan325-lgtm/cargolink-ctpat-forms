# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
forms_dir = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS"

# 1. READ portal_driver.html
portal_path = os.path.join(forms_dir, "portal_driver.html")
with open(portal_path, "r", encoding="utf-8") as f:
    portal_content = f.read()

# Define the HTML snippet for NHÓM V (10 Digital Operational Tools)
tools_section_html = """
  <!-- NHÓM V: BỘ CÔNG CỤ VẬN HÀNH SỐ HÓA & BIỂU MẪU ĐIỆN TỬ -->
  <div class="category-title" id="operational-tools">🛠️ NHÓM V: BỘ CÔNG CỤ VẬN HÀNH SỐ HÓA & BIỂU MẪU ĐIỆN TỬ (DIGITAL OPERATIONAL TOOLS)</div>
  <p style="font-size: 13px; color: #64748B; margin-top: -8px; margin-bottom: 16px;">
    Toàn bộ biểu mẫu vận hành, nhật ký kiểm tra, biên bản niêm phong và ứng phó sự cố đã được số hóa 100% không dùng giấy, hỗ trợ ký điện tử và lưu trữ tự động.
  </p>

  <div class="grid">
    <!-- Tool 1: Vehicle 7/17-Point Inspection -->
    <div class="card">
      <div>
        <div class="card-tag">🚚 KIỂM TRA PHƯƠNG TIỆN</div>
        <h3>Phiếu Kiểm Tra An Ninh Xe 7 Điểm & 17 Điểm</h3>
        <div class="card-desc">
          Biên bản kiểm tra an ninh trước chuyến đi theo chuẩn WI-SEC-001 (Lốp xe, gầm xe, bình nhiên liệu, cabin, chốt cửa, vách thùng) có chữ ký số điện tử.
        </div>
      </div>
      <div class="qr-preview">
        <img src="qr_app1_inspection.png" alt="QR Tool 1">
        <div class="qr-caption">Quét mã kiểm tra xe</div>
      </div>
      <a href="app_vehicle_inspection.html" class="btn-action">MỞ PHIẾU KIỂM TRA XE</a>
    </div>

    <!-- Tool 2: Seal VVTT & Handover Log -->
    <div class="card">
      <div>
        <div class="card-tag">🔒 NIÊM PHONG SEAL C-TPAT</div>
        <h3>Biên Bản Kiểm Tra Niêm Phong Seal VVTT & Bàn Giao Cắt Seal</h3>
        <div class="card-desc">
          Kiểm tra 4 bước chuẩn quốc tế VVTT (View - Verify - Tug - Twist) đối với Seal C-TPAT High Security ISO 17712, ghi nhận giờ bấm & cắt seal hai bên cùng ký.
        </div>
      </div>
      <div class="qr-preview">
        <img src="qr_app2_seal.png" alt="QR Tool 2">
        <div class="qr-caption">Quét mã kiểm tra Seal</div>
      </div>
      <a href="app_seal_vvtt_log.html" class="btn-action accent">MỞ BIÊN BẢN SEAL VVTT</a>
    </div>

    <!-- Tool 3: Alcohol & Drug Test Log -->
    <div class="card">
      <div>
        <div class="card-tag">🛡️ AN TOÀN GIAO THÔNG ISO 39001</div>
        <h3>Sổ Kiểm Tra Nồng Độ Cồn & Ma Túy Trước Chuyến Đi</h3>
        <div class="card-desc">
          Kiểm tra 100% lái xe trước xuất bến: Nồng độ cồn hơi thở cam kết tuyệt đối 0.00 mg/L và que thử sàng lọc 5 nhóm chất ma túy âm tính (-).
        </div>
      </div>
      <div class="qr-preview">
        <img src="qr_app3_alcohol.png" alt="QR Tool 3">
        <div class="qr-caption">Quét mã kiểm tra sức khỏe</div>
      </div>
      <a href="app_alcohol_test_log.html" class="btn-action green">MỞ SỔ ĐO NỒNG ĐỘ CỒN</a>
    </div>

    <!-- Tool 4: Incident Rapid Report -->
    <div class="card" style="border-color: #FCA5A5;">
      <div>
        <div class="card-tag" style="color: #DC2626;">🚨 ỨNG PHÓ KHẨN CẤP 15 PHÚT</div>
        <h3 style="color: #991B1B;">Phiếu Báo Cáo Nhanh Sự Cố & Chậm ETA Trong 15 Phút</h3>
        <div class="card-desc">
          Kích hoạt ngay khi trễ giờ >15 phút, gặp sự cố hỏng xe, sự cố seal, nghi vấn cạy phá hoặc tai nạn. Tự động lấy tọa độ GPS định vị hiện trường và gọi nhanh hotline.
        </div>
      </div>
      <div class="qr-preview" style="background: #FEF2F2;">
        <img src="qr_app4_incident.png" alt="QR Tool 4">
        <div class="qr-caption" style="color: #991B1B;">Quét mã báo cáo sự cố khẩn</div>
      </div>
      <a href="app_incident_rapid_report.html" class="btn-action" style="background: #DC2626;">🚨 PHÁT BÁO CÁO SỰ CỐ NGAY</a>
    </div>

    <!-- Tool 5: Trip Dispatch & Route Monitoring -->
    <div class="card">
      <div>
        <div class="card-tag">📋 ĐIỀU ĐỘ & HÀNH TRÌNH</div>
        <h3>Lệnh Điều Xe Điện Tử & Nhật Ký Tuyến NV Apparel</h3>
        <div class="card-desc">
          Cấp phát lệnh điều xe điện tử số hiệu CGL-DSP, xác định lộ trình cố định, điểm dừng đỗ Petrolimex được phê duyệt C-TPAT và cam kết không nhận khách lạ.
        </div>
      </div>
      <div class="qr-preview">
        <img src="qr_app5_dispatch.png" alt="QR Tool 5">
        <div class="qr-caption">Quét mã nhận Lệnh Điều Xe</div>
      </div>
      <a href="app_trip_dispatch_log.html" class="btn-action">MỞ LỆNH ĐIỀU XE ĐIỆN TỬ</a>
    </div>

    <!-- Tool 6: PPE & PCCC Fire Safety Log -->
    <div class="card">
      <div>
        <div class="card-tag">🧯 PCCC & BẢO HỘ LAO ĐỘNG</div>
        <h3>Sổ Kiểm Tra PCCC & Trang Bị Bảo Hộ (PPE) Xe Tải</h3>
        <div class="card-desc">
          Kiểm tra tình trạng áp kế bình chữa cháy bột MFZ4 cabin & thùng xe, 02 tam giác phản quang sự cố, đèn pin tuần tra đêm và bảo hộ lao động mũi thép của lái xe.
        </div>
      </div>
      <div class="qr-preview">
        <img src="qr_app6_ppe.png" alt="QR Tool 6">
        <div class="qr-caption">Quét mã kiểm tra PCCC</div>
      </div>
      <a href="app_ppe_pccc_log.html" class="btn-action">MỞ SỔ KIỂM TRA PPE & PCCC</a>
    </div>

    <!-- Tool 7: Visitor Gate Security Log -->
    <div class="card">
      <div>
        <div class="card-tag">🏷️ AN NINH CỔNG BÃI XE</div>
        <h3>Sổ Nhật Ký Kiểm Soát Khách & Xe Ra Vào Bãi Xe</h3>
        <div class="card-desc">
          Đăng ký thông tin khách đến liên hệ công tác, số CCCD, biển số xe, mục đích làm việc, cấp phát thẻ khách C-TPAT và ghi nhận giờ vào / giờ ra an toàn.
        </div>
      </div>
      <div class="qr-preview">
        <img src="qr_app7_visitor.png" alt="QR Tool 7">
        <div class="qr-caption">Quét mã nhật ký khách</div>
      </div>
      <a href="app_visitor_gate_log.html" class="btn-action">MỞ SỔ NHẬT KÝ CỔNG</a>
    </div>

    <!-- Tool 8: Green Office & Energy Tracker -->
    <div class="card">
      <div>
        <div class="card-tag" style="color: #059669;">🌿 MÔI TRƯỜNG ISO 14001</div>
        <h3>Sổ Theo Dõi Chỉ Số Năng Lượng & Văn Phòng Xanh</h3>
        <div class="card-desc">
          Theo dõi định kỳ mức tiêu thụ điện năng (kWh), nước sạch (m³), giấy in A4, rác thải tái chế và định mức dầu xe để tự động tính toán % cắt giảm phát thải.
        </div>
      </div>
      <div class="qr-preview" style="background: #F0FDF4;">
        <img src="qr_app8_green.png" alt="QR Tool 8">
        <div class="qr-caption">Quét mã theo dõi năng lượng</div>
      </div>
      <a href="app_green_office_log.html" class="btn-action green">MỞ SỔ VĂN PHÒNG XANH</a>
    </div>

    <!-- Tool 9: Subcontractor C-TPAT Audit -->
    <div class="card">
      <div>
        <div class="card-tag">🤝 ĐỐI TÁC CHUỖI CUNG ỨNG</div>
        <h3>Bảng Đánh Giá Năng Lực & An Ninh C-TPAT Nhà Xe Phụ</h3>
        <div class="card-desc">
          Bộ tiêu chí 100 điểm thẩm định nhà thầu phụ vận tải: Giấy phép kinh doanh, bảo hiểm, 100% xe gắn GPS, lý lịch tư pháp lái xe và cam kết bảo mật seal.
        </div>
      </div>
      <div class="qr-preview">
        <img src="qr_app9_subcontractor.png" alt="QR Tool 9">
        <div class="qr-caption">Quét mã đánh giá thầu phụ</div>
      </div>
      <a href="app_subcontractor_eval.html" class="btn-action">MỞ BẢNG ĐÁNH GIÁ THẦU PHỤ</a>
    </div>

    <!-- Tool 10: C-TPAT Internal Self-Audit Checklist -->
    <div class="card" style="border: 2px solid #0B3C5D;">
      <div>
        <div class="card-tag" style="color: #1E3A8A;">🏆 SẴN SÀNG KIỂM TOÁN C-TPAT</div>
        <h3>Checklist Tự Đánh Giá Nội Bộ Sẵn Sàng Kiểm Toán C-TPAT</h3>
        <div class="card-desc">
          Bộ công cụ đối chiếu 12 tiêu chuẩn an ninh Hải quan Hoa Kỳ & Khách hàng NV Apparel, tự động tính điểm mức độ sẵn sàng và lập kế hoạch hành động khắc phục.
        </div>
      </div>
      <div class="qr-preview" style="background: #EFF6FF;">
        <img src="qr_app10_audit.png" alt="QR Tool 10">
        <div class="qr-caption">Quét mã tự kiểm toán nội bộ</div>
      </div>
      <a href="app_ctpat_audit_checklist.html" class="btn-action accent">MỞ CHECKLIST KIỂM TOÁN C-TPAT</a>
    </div>
  </div>
"""

# Insert before disclaimer box or footer
if "<!-- NHÓM V" not in portal_content:
    if '<div class="disclaimer-box">' in portal_content:
        portal_content = portal_content.replace('<div class="disclaimer-box">', tools_section_html + '\n  <div class="disclaimer-box">')
    else:
        portal_content = portal_content.replace('</body>', tools_section_html + '\n</body>')

with open(portal_path, "w", encoding="utf-8") as f:
    f.write(portal_content)

print("Updated portal_driver.html with NHOM V (10 Digital Operational Tools) successfully!")
