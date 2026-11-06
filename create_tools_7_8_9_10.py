# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
output_dir = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS"

# ==========================================
# TOOL 7: app_visitor_gate_log.html
# ==========================================
tool7_html = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sổ Nhật Ký Kiểm Soát Khách & Xe Ra Vào Bãi Xe | Cargolink C-TPAT</title>
  <style>
    :root {
      --primary: #071A36;
      --primary-light: #0B3C5D;
      --accent: #D4441E;
      --bg: #F1F5F9;
      --card: #FFFFFF;
      --border: #CBD5E1;
      --text: #0F172A;
      --muted: #64748B;
      --success: #059669;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    body { background-color: var(--bg); color: var(--text); line-height: 1.5; padding: 16px; min-height: 100vh; }
    .container { max-width: 820px; margin: 0 auto; background: var(--card); border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); overflow: hidden; border: 1px solid var(--border); }
    .conf-banner { background: #FEF3C7; border-bottom: 1.5px dashed #D97706; color: #92400E; padding: 10px 14px; font-size: 11.5px; font-weight: 700; text-align: center; text-transform: uppercase; }
    .header { background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%); color: white; padding: 24px 20px; text-align: center; }
    .header .badge { display: inline-block; background: var(--accent); color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; padding: 3px 12px; border-radius: 12px; margin-bottom: 8px; }
    .header h1 { font-size: 20px; font-weight: 800; line-height: 1.3; }
    .header p { font-size: 13px; opacity: 0.9; margin-top: 4px; }
    .nav-back { display: inline-block; margin-bottom: 6px; color: #93C5FD; text-decoration: none; font-weight: 700; font-size: 13px; }
    .form-body { padding: 24px 20px; }
    .section-title { font-size: 14px; font-weight: 800; color: var(--primary); text-transform: uppercase; margin-bottom: 14px; padding-bottom: 6px; border-bottom: 2px solid #E2E8F0; display: flex; align-items: center; gap: 8px; }
    .section-title::before { content: ""; display: inline-block; width: 4px; height: 16px; background: var(--accent); border-radius: 2px; }
    .grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-bottom: 16px; }
    .field-group { margin-bottom: 14px; }
    label { display: block; font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
    input[type="text"], input[type="date"], input[type="time"], select, textarea {
      width: 100%; padding: 9px 12px; font-size: 13.5px; border: 1.5px solid var(--border); border-radius: 8px; background: #FFF; outline: none;
    }
    input:focus, select:focus, textarea:focus { border-color: var(--primary-light); }
    .sig-box { background: #F8FAFC; border: 1.5px dashed var(--border); border-radius: 8px; padding: 14px; text-align: center; margin-top: 10px; }
    canvas { background: white; border: 1px solid #CBD5E1; border-radius: 6px; width: 100%; max-width: 380px; height: 120px; touch-action: none; cursor: crosshair; }
    .sig-btns { margin-top: 6px; }
    .btn-clear { background: #E2E8F0; border: none; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; cursor: pointer; }
    .btn-submit { width: 100%; background: var(--accent); color: white; padding: 14px 20px; font-size: 15px; font-weight: 700; border: none; border-radius: 10px; cursor: pointer; margin-top: 18px; }
    .btn-submit:hover { background: #b83815; }
    .modal-overlay { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.6); z-index: 1000; align-items: center; justify-content: center; padding: 20px; }
    .modal-box { background: white; border-radius: 16px; padding: 28px 20px; max-width: 440px; width: 100%; text-align: center; }
    .btn-print { background: var(--primary); color: white; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600; border: none; cursor: pointer; margin-right: 8px; }
    .btn-close { background: #E2E8F0; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600; border: none; cursor: pointer; }
    .footer { text-align: center; font-size: 11.5px; color: var(--muted); margin-top: 20px; border-top: 1px dashed var(--border); padding-top: 12px; }
  </style>
</head>
<body>

<div class="container">
  <div class="conf-banner">🔒 TÀI LIỆU LƯU HÀNH NỘI BỘ — CARGOLINK EXPRESS (E-VISITOR GATE LOG)</div>

  <div class="header">
    <a href="portal_driver.html" class="nav-back">⬅ Quay lại Cổng Tra Cứu</a>
    <span class="badge">KIỂM SOÁT RA VÀO CỔNG AN NINH (HS13-01)</span>
    <h1>SỔ NHẬT KÝ KIỂM SOÁT KHÁCH & PHƯƠNG TIỆN RA VÀO BÃI XE</h1>
    <p>Kiểm soát 100% người và phương tiện ra vào bãi xe tập kết & trạm điều độ Cargolink</p>
  </div>

  <form id="visForm" class="form-body" onsubmit="handleVisSubmit(event)">
    <div class="section-title">1. Thông tin Khách / Nhà thầu / Đối tác</div>
    <div class="grid-2">
      <div class="field-group">
        <label>Họ và tên Khách đến liên hệ:</label>
        <input type="text" id="visitorName" placeholder="VD: Nguyễn Tuấn Anh" required>
      </div>
      <div class="field-group">
        <label>Số CCCD / CMND / Hộ chiếu:</label>
        <input type="text" id="idCard" placeholder="VD: 079094001234" required>
      </div>
      <div class="field-group">
        <label>Đơn vị công tác / Công ty đại diện:</label>
        <input type="text" id="company" placeholder="VD: Công ty TNHH Vỏ Xe Michelin / Khách hàng NV" required>
      </div>
      <div class="field-group">
        <label>Số điện thoại liên hệ:</label>
        <input type="text" id="phone" placeholder="VD: 0918 222 333" required>
      </div>
    </div>

    <div class="section-title">2. Phương tiện & Mục đích vào Bãi xe</div>
    <div class="grid-2">
      <div class="field-group">
        <label>Loại phương tiện di chuyển:</label>
        <select id="vehicleType" required>
          <option value="Xe máy (Motorbike)">Xe máy cá nhân</option>
          <option value="Ô tô con (Passenger Car)">Ô tô con</option>
          <option value="Xe tải giao phụ tùng/vật tư">Xe tải giao phụ tùng/vật tư</option>
          <option value="Đi bộ (Pedestrian)">Đi bộ</option>
        </select>
      </div>
      <div class="field-group">
        <label>Biển số phương tiện (nếu có):</label>
        <input type="text" id="licensePlate" placeholder="VD: 59P1-998.77">
      </div>
      <div class="field-group">
        <label>Mục đích vào bãi xe / Văn phòng:</label>
        <select id="purpose" required>
          <option value="Giao nhận phụ tùng / Vật tư bảo dưỡng xe">Giao nhận phụ tùng / Vật tư bảo dưỡng xe</option>
          <option value="Bảo trì hệ thống camera / Thiết bị giám sát hành trình">Bảo trì hệ thống camera / GPS</option>
          <option value="Thanh tra / Kiểm toán an ninh đối tác NV Apparel">Thanh tra / Kiểm toán đối tác NV Apparel</option>
          <option value="Liên hệ công tác phòng Điều độ">Liên hệ công tác phòng Điều độ</option>
          <option value="Khác">Mục đích khác</option>
        </select>
      </div>
      <div class="field-group">
        <label>Cán bộ / Bộ phận nội bộ tiếp đón:</label>
        <input type="text" id="hostPerson" value="Mr. Thành (An toàn) / Ms. Bích (Điều độ)" required>
      </div>
    </div>

    <div class="section-title">3. Cấp phát Thẻ Khách C-TPAT & Thời gian</div>
    <div class="grid-2">
      <div class="field-group">
        <label>Số Thẻ Khách C-TPAT cấp phát:</label>
        <select id="badgeNumber" required style="font-weight: 700; color: #1E3A8A;">
          <option value="THẺ KHÁCH SỐ #01 (VISITOR 01)">THẺ KHÁCH SỐ #01 (VISITOR 01)</option>
          <option value="THẺ KHÁCH SỐ #02 (VISITOR 02)">THẺ KHÁCH SỐ #02 (VISITOR 02)</option>
          <option value="THẺ KHÁCH SỐ #03 (VISITOR 03)">THẺ KHÁCH SỐ #03 (VISITOR 03)</option>
          <option value="THẺ KHÁCH SỐ #04 (VISITOR 04)">THẺ KHÁCH SỐ #04 (VISITOR 04)</option>
          <option value="THẺ KHÁCH SỐ #05 (VISITOR 05)">THẺ KHÁCH SỐ #05 (VISITOR 05)</option>
        </select>
      </div>
      <div class="field-group">
        <label>Thiết bị mang theo (Laptop / Thiết bị ghi hình):</label>
        <input type="text" id="devices" placeholder="VD: 01 Laptop Dell / Không mang thiết bị ghi hình">
      </div>
      <div class="field-group">
        <label>Ngày & Giờ vào bãi xe:</label>
        <div style="display: flex; gap: 8px;">
          <input type="date" id="dateIn" required>
          <input type="time" id="timeIn" required>
        </div>
      </div>
      <div class="field-group">
        <label>Giờ ra khỏi bãi xe & Trả thẻ khách:</label>
        <input type="time" id="timeOut" placeholder="Ghi nhận khi khách ra">
      </div>
    </div>

    <div class="section-title">4. Chữ ký số xác nhận (Signatures)</div>
    <div class="grid-2">
      <div>
        <label>Khách đến liên hệ ký tên:</label>
        <div class="sig-box">
          <canvas id="sigVisitor"></canvas>
          <div class="sig-btns"><button type="button" class="btn-clear" onclick="clearSig('sigVisitor')">Ký lại</button></div>
        </div>
      </div>
      <div>
        <label>Bảo vệ / Nhân viên trực cổng ký duyệt:</label>
        <div class="sig-box">
          <canvas id="sigGuard"></canvas>
          <div class="sig-btns"><button type="button" class="btn-clear" onclick="clearSig('sigGuard')">Ký lại</button></div>
        </div>
      </div>
    </div>

    <button type="submit" class="btn-submit">🔒 LƯU NHẬT KÝ KIỂM SOÁT RA VÀO CỔNG</button>
  </form>

  <div class="footer">
    CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM — PHÒNG BẢO VỆ & AN NINH C-TPAT<br>
    Hồ sơ lưu trữ tối thiểu 45 ngày phục vụ đối chiếu kiểm toán C-TPAT và công an khu vực
  </div>
</div>

<div id="modalSuccess" class="modal-overlay">
  <div class="modal-box">
    <div style="font-size: 40px; margin-bottom: 10px;">🏷️</div>
    <h3 style="color: var(--primary); margin-bottom: 8px;">ĐÃ CẤP PHÁT THẺ KHÁCH RA VÀO</h3>
    <p style="font-size: 13px; color: var(--muted); margin-bottom: 14px;">Mã lượt khách ra vào bãi xe:</p>
    <div id="visCodeText" style="font-size: 18px; font-weight: 800; color: var(--accent); background: #F8FAFC; padding: 10px; border-radius: 8px; border: 1.5px dashed var(--border); margin-bottom: 16px;">VIS-2026-0000</div>
    <p style="font-size: 12px; color: var(--muted); margin-bottom: 18px;">Khách bắt buộc đeo thẻ khách trong suốt quá trình lưu lại bãi xe và tuân thủ nội quy an toàn.</p>
    <div>
      <button class="btn-print" onclick="window.print()">🖨 In / Lưu PDF</button>
      <button class="btn-close" onclick="closeModal()">Đóng</button>
    </div>
  </div>
</div>

<script>
  function initNow() {
    const d = new Date();
    document.getElementById('dateIn').value = d.toISOString().split('T')[0];
    document.getElementById('timeIn').value = d.toTimeString().slice(0,5);
  }
  initNow();

  function initCanvas(id) {
    const c = document.getElementById(id);
    const ctx = c.getContext('2d');
    c.width = c.offsetWidth || 340;
    c.height = 120;
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#071A36';
    let drawing = false;

    function getPos(e) {
      const rect = c.getBoundingClientRect();
      const cx = e.touches ? e.touches[0].clientX : e.clientX;
      const cy = e.touches ? e.touches[0].clientY : e.clientY;
      return { x: cx - rect.left, y: cy - rect.top };
    }
    function start(e) { drawing = true; const p = getPos(e); ctx.beginPath(); ctx.moveTo(p.x, p.y); e.preventDefault(); }
    function move(e) { if (!drawing) return; const p = getPos(e); ctx.lineTo(p.x, p.y); ctx.stroke(); e.preventDefault(); }
    function stop() { drawing = false; }

    c.addEventListener('mousedown', start);
    c.addEventListener('mousemove', move);
    window.addEventListener('mouseup', stop);
    c.addEventListener('touchstart', start);
    c.addEventListener('touchmove', move);
    window.addEventListener('touchend', stop);
  }

  window.addEventListener('load', () => {
    initCanvas('sigVisitor');
    initCanvas('sigGuard');
  });

  function clearSig(id) {
    const c = document.getElementById(id);
    c.getContext('2d').clearRect(0, 0, c.width, c.height);
  }

  async function handleVisSubmit(e) {
    e.preventDefault();
    const code = 'VIS-2026-' + Math.floor(1000 + Math.random() * 9000);
    const record = {
      form_type: 'visitor_gate_log',
      reference_code: code,
      visitor_name: document.getElementById('visitorName').value,
      id_card: document.getElementById('idCard').value,
      company: document.getElementById('company').value,
      phone: document.getElementById('phone').value,
      vehicle_type: document.getElementById('vehicleType').value,
      license_plate: document.getElementById('licensePlate').value,
      purpose: document.getElementById('purpose').value,
      host_person: document.getElementById('hostPerson').value,
      badge_number: document.getElementById('badgeNumber').value,
      devices: document.getElementById('devices').value,
      date_in: document.getElementById('dateIn').value,
      time_in: document.getElementById('timeIn').value,
      time_out: document.getElementById('timeOut').value,
      submitted_at: new Date().toISOString()
    };

    try {
      const list = JSON.parse(localStorage.getItem('cgl_visitor_logs') || '[]');
      list.push(record);
      localStorage.setItem('cgl_visitor_logs', JSON.stringify(list));
    } catch(err) {}

    const api = (window.location.origin.includes('github.io') || window.location.protocol === 'file:')
      ? 'https://continent-msie-goals-watt.trycloudflare.com/api/submit'
      : '/api/submit';
    try {
      await fetch(api, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(record)
      });
    } catch(err) {}

    document.getElementById('visCodeText').innerText = code;
    document.getElementById('modalSuccess').style.display = 'flex';
  }

  function closeModal() {
    document.getElementById('modalSuccess').style.display = 'none';
  }
</script>
</body>
</html>
"""

# ==========================================
# TOOL 8: app_green_office_log.html
# ==========================================
tool8_html = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sổ Theo Dõi Chỉ Số Năng Lượng & Văn Phòng Xanh | Cargolink ISO 14001</title>
  <style>
    :root {
      --primary: #064E3B;
      --primary-light: #047857;
      --accent: #D97706;
      --bg: #F0FDF4;
      --card: #FFFFFF;
      --border: #CBD5E1;
      --text: #0F172A;
      --muted: #64748B;
      --success: #059669;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    body { background-color: var(--bg); color: var(--text); line-height: 1.5; padding: 16px; min-height: 100vh; }
    .container { max-width: 820px; margin: 0 auto; background: var(--card); border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); overflow: hidden; border: 1px solid var(--border); }
    .conf-banner { background: #DCFCE7; border-bottom: 1.5px dashed #16A34A; color: #166534; padding: 10px 14px; font-size: 11.5px; font-weight: 700; text-align: center; text-transform: uppercase; }
    .header { background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%); color: white; padding: 24px 20px; text-align: center; }
    .header .badge { display: inline-block; background: #34D399; color: #064E3B; font-size: 11px; font-weight: 800; text-transform: uppercase; padding: 3px 12px; border-radius: 12px; margin-bottom: 8px; }
    .header h1 { font-size: 20px; font-weight: 800; line-height: 1.3; }
    .header p { font-size: 13px; opacity: 0.9; margin-top: 4px; }
    .nav-back { display: inline-block; margin-bottom: 6px; color: #A7F3D0; text-decoration: none; font-weight: 700; font-size: 13px; }
    .form-body { padding: 24px 20px; }
    .section-title { font-size: 14px; font-weight: 800; color: var(--primary); text-transform: uppercase; margin-bottom: 14px; padding-bottom: 6px; border-bottom: 2px solid #E2E8F0; display: flex; align-items: center; gap: 8px; }
    .section-title::before { content: ""; display: inline-block; width: 4px; height: 16px; background: #059669; border-radius: 2px; }
    .grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-bottom: 16px; }
    .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-bottom: 16px; }
    .field-group { margin-bottom: 14px; }
    label { display: block; font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
    input[type="text"], input[type="number"], select {
      width: 100%; padding: 9px 12px; font-size: 13.5px; border: 1.5px solid var(--border); border-radius: 8px; background: #FFF; outline: none;
    }
    input:focus, select:focus { border-color: var(--primary-light); }
    .metric-card { background: #F8FAFC; border: 1.5px solid #E2E8F0; border-radius: 10px; padding: 14px; text-align: center; }
    .metric-card .title { font-size: 12px; font-weight: 700; color: #64748B; text-transform: uppercase; }
    .metric-card .val { font-size: 22px; font-weight: 800; color: var(--primary); margin: 6px 0; }
    .metric-card .target { font-size: 11px; color: #059669; font-weight: 600; }
    .sig-box { background: #F8FAFC; border: 1.5px dashed var(--border); border-radius: 8px; padding: 14px; text-align: center; margin-top: 10px; }
    canvas { background: white; border: 1px solid #CBD5E1; border-radius: 6px; width: 100%; max-width: 380px; height: 120px; touch-action: none; cursor: crosshair; }
    .sig-btns { margin-top: 6px; }
    .btn-clear { background: #E2E8F0; border: none; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; cursor: pointer; }
    .btn-submit { width: 100%; background: #059669; color: white; padding: 14px 20px; font-size: 15px; font-weight: 700; border: none; border-radius: 10px; cursor: pointer; margin-top: 18px; }
    .btn-submit:hover { background: #047857; }
    .modal-overlay { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.6); z-index: 1000; align-items: center; justify-content: center; padding: 20px; }
    .modal-box { background: white; border-radius: 16px; padding: 28px 20px; max-width: 440px; width: 100%; text-align: center; }
    .btn-print { background: var(--primary); color: white; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600; border: none; cursor: pointer; margin-right: 8px; }
    .btn-close { background: #E2E8F0; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600; border: none; cursor: pointer; }
    .footer { text-align: center; font-size: 11.5px; color: var(--muted); margin-top: 20px; border-top: 1px dashed var(--border); padding-top: 12px; }
  </style>
</head>
<body>

<div class="container">
  <div class="conf-banner">🌿 HỆ THỐNG QUẢN LÝ MÔI TRƯỜNG & VĂN PHÒNG XANH — ISO 14001:2015</div>

  <div class="header">
    <a href="portal_driver.html" class="nav-back">⬅ Quay lại Cổng Tra Cứu</a>
    <span class="badge">VĂN PHÒNG XANH & TIẾT KIỆM NĂNG LƯỢNG (HS01-02)</span>
    <h1>SỔ THEO DÕI CHỈ SỐ NĂNG LƯỢNG & MÔI TRƯỜNG ĐIỆN TỬ</h1>
    <p>Theo dõi định kỳ mức tiêu thụ điện, nước, giấy in A4 và rác thải tái chế toàn công ty</p>
  </div>

  <form id="grnForm" class="form-body" onsubmit="handleGrnSubmit(event)">
    <div class="section-title">1. Cơ sở & Kỳ theo dõi báo cáo</div>
    <div class="grid-2">
      <div class="field-group">
        <label>Tháng / Năm báo cáo:</label>
        <select id="reportMonth" required>
          <option value="Tháng 03/2026">Tháng 03/2026</option>
          <option value="Tháng 02/2026">Tháng 02/2026</option>
          <option value="Tháng 01/2026">Tháng 01/2026</option>
        </select>
      </div>
      <div class="field-group">
        <label>Địa điểm / Bộ phận theo dõi:</label>
        <select id="facility" required>
          <option value="Trụ sở Văn phòng (Lầu 6, 84 Bạch Đằng)">Trụ sở Văn phòng (Lầu 6, 84 Bạch Đằng)</option>
          <option value="Bãi xe tập kết & Trạm Điều độ C-TPAT">Bãi xe tập kết & Trạm Điều độ C-TPAT</option>
          <option value="Tổng hợp toàn công ty">Tổng hợp toàn công ty</option>
        </select>
      </div>
    </div>

    <div class="section-title">2. Số liệu Năng lượng & Tiêu thụ Tài nguyên</div>
    <div class="grid-2">
      <div class="field-group">
        <label>Điện năng tiêu thụ (kWh):</label>
        <input type="number" id="elecKwh" value="450" required oninput="calcGreenKPI()">
      </div>
      <div class="field-group">
        <label>Nước sạch tiêu thụ (m³):</label>
        <input type="number" id="waterM3" value="18" required>
      </div>
      <div class="field-group">
        <label>Số ram giấy in A4 sử dụng (ram):</label>
        <input type="number" id="paperReams" value="12" required oninput="calcGreenKPI()">
      </div>
      <div class="field-group">
        <label>Tỷ lệ tài liệu in 2 mặt (%):</label>
        <input type="number" id="duplexRatio" value="85" min="0" max="100" required>
      </div>
      <div class="field-group">
        <label>Rác thải tái chế thu gom (kg bìa/nhựa):</label>
        <input type="number" id="recycleKg" value="42" required>
      </div>
      <div class="field-group">
        <label>Định mức tiêu hao nhiên liệu xe (Lít dầu/100km):</label>
        <input type="number" id="fuelRate" step="0.1" value="14.2" required>
      </div>
    </div>

    <div class="section-title">3. Tự động Đánh giá Tiến độ Mục tiêu ISO 14001</div>
    <div class="grid-3">
      <div class="metric-card">
        <div class="title">Tiết kiệm Điện</div>
        <div class="val" id="elecKpi" style="color: #059669;">-11.2%</div>
        <div class="target">Mục tiêu: Giảm -10% (ĐẠT)</div>
      </div>
      <div class="metric-card">
        <div class="title">Tiết kiệm Giấy A4</div>
        <div class="val" id="paperKpi" style="color: #059669;">-22.5%</div>
        <div class="target">Mục tiêu: Giảm -20% (ĐẠT)</div>
      </div>
      <div class="metric-card">
        <div class="title">Đánh giá chung</div>
        <div class="val" id="overallKpi" style="color: #059669;">XUẤT SẮC</div>
        <div class="target">Chuẩn ISO 14001</div>
      </div>
    </div>

    <div class="section-title">4. Chữ ký số Ban ISO & Môi trường</div>
    <div class="grid-2">
      <div>
        <label>Cán bộ thống kê số liệu ký:</label>
        <div class="sig-box">
          <canvas id="sigOfficer"></canvas>
          <div class="sig-btns"><button type="button" class="btn-clear" onclick="clearSig('sigOfficer')">Ký lại</button></div>
        </div>
      </div>
      <div>
        <label>Trưởng Ban ISO Môi trường phê duyệt:</label>
        <div class="sig-box">
          <canvas id="sigLead"></canvas>
          <div class="sig-btns"><button type="button" class="btn-clear" onclick="clearSig('sigLead')">Ký lại</button></div>
        </div>
      </div>
    </div>

    <button type="submit" class="btn-submit">🌱 LƯU BÁO CÁO VĂN PHÒNG XANH & NĂNG LƯỢNG</button>
  </form>

  <div class="footer">
    CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM — BAN QUẢN LÝ MÔI TRƯỜNG ISO 14001<br>
    Chương trình giảm phát thải Carbon, tối ưu hóa năng lượng và kinh tế tuần hoàn
  </div>
</div>

<div id="modalSuccess" class="modal-overlay">
  <div class="modal-box">
    <div style="font-size: 40px; margin-bottom: 10px;">🌿</div>
    <h3 style="color: #064E3B; margin-bottom: 8px;">ĐÃ LƯU BÁO CÁO MÔI TRƯỜNG</h3>
    <p style="font-size: 13px; color: var(--muted); margin-bottom: 14px;">Mã báo cáo năng lượng điện tử:</p>
    <div id="grnCodeText" style="font-size: 18px; font-weight: 800; color: #059669; background: #DCFCE7; padding: 10px; border-radius: 8px; border: 1.5px dashed #86EFAC; margin-bottom: 16px;">GRN-2026-0000</div>
    <p style="font-size: 12px; color: #064E3B; margin-bottom: 18px;">Dữ liệu đã được tích hợp vào báo cáo giám sát mục tiêu chất lượng và môi trường ISO 14001.</p>
    <div>
      <button class="btn-print" onclick="window.print()">🖨 In / Lưu PDF</button>
      <button class="btn-close" onclick="closeModal()">Đóng</button>
    </div>
  </div>
</div>

<script>
  function calcGreenKPI() {
    const elec = parseFloat(document.getElementById('elecKwh').value) || 0;
    const paper = parseFloat(document.getElementById('paperReams').value) || 0;
    // Benchmark: elec base = 500 kWh, paper base = 15 reams
    const elecSave = ((500 - elec) / 500 * 100).toFixed(1);
    const paperSave = ((15 - paper) / 15 * 100).toFixed(1);

    document.getElementById('elecKpi').innerText = (elecSave > 0 ? '-' : '+') + Math.abs(elecSave) + '%';
    document.getElementById('elecKpi').style.color = elecSave >= 10 ? '#059669' : '#D97706';

    document.getElementById('paperKpi').innerText = (paperSave > 0 ? '-' : '+') + Math.abs(paperSave) + '%';
    document.getElementById('paperKpi').style.color = paperSave >= 20 ? '#059669' : '#D97706';
  }

  function initCanvas(id) {
    const c = document.getElementById(id);
    const ctx = c.getContext('2d');
    c.width = c.offsetWidth || 340;
    c.height = 120;
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#064E3B';
    let drawing = false;

    function getPos(e) {
      const rect = c.getBoundingClientRect();
      const cx = e.touches ? e.touches[0].clientX : e.clientX;
      const cy = e.touches ? e.touches[0].clientY : e.clientY;
      return { x: cx - rect.left, y: cy - rect.top };
    }
    function start(e) { drawing = true; const p = getPos(e); ctx.beginPath(); ctx.moveTo(p.x, p.y); e.preventDefault(); }
    function move(e) { if (!drawing) return; const p = getPos(e); ctx.lineTo(p.x, p.y); ctx.stroke(); e.preventDefault(); }
    function stop() { drawing = false; }

    c.addEventListener('mousedown', start);
    c.addEventListener('mousemove', move);
    window.addEventListener('mouseup', stop);
    c.addEventListener('touchstart', start);
    c.addEventListener('touchmove', move);
    window.addEventListener('touchend', stop);
  }

  window.addEventListener('load', () => {
    initCanvas('sigOfficer');
    initCanvas('sigLead');
    calcGreenKPI();
  });

  function clearSig(id) {
    const c = document.getElementById(id);
    c.getContext('2d').clearRect(0, 0, c.width, c.height);
  }

  async function handleGrnSubmit(e) {
    e.preventDefault();
    const code = 'GRN-2026-' + Math.floor(1000 + Math.random() * 9000);
    const record = {
      form_type: 'green_office_energy_log',
      reference_code: code,
      report_month: document.getElementById('reportMonth').value,
      facility: document.getElementById('facility').value,
      elec_kwh: document.getElementById('elecKwh').value,
      water_m3: document.getElementById('waterM3').value,
      paper_reams: document.getElementById('paperReams').value,
      duplex_ratio: document.getElementById('duplexRatio').value,
      recycle_kg: document.getElementById('recycleKg').value,
      fuel_rate: document.getElementById('fuelRate').value,
      submitted_at: new Date().toISOString()
    };

    try {
      const list = JSON.parse(localStorage.getItem('cgl_green_logs') || '[]');
      list.push(record);
      localStorage.setItem('cgl_green_logs', JSON.stringify(list));
    } catch(err) {}

    const api = (window.location.origin.includes('github.io') || window.location.protocol === 'file:')
      ? 'https://continent-msie-goals-watt.trycloudflare.com/api/submit'
      : '/api/submit';
    try {
      await fetch(api, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(record)
      });
    } catch(err) {}

    document.getElementById('grnCodeText').innerText = code;
    document.getElementById('modalSuccess').style.display = 'flex';
  }

  function closeModal() {
    document.getElementById('modalSuccess').style.display = 'none';
  }
</script>
</body>
</html>
"""

# ==========================================
# TOOL 9: app_subcontractor_eval.html
# ==========================================
tool9_html = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bảng Đánh Giá Năng Lực & An Ninh C-TPAT Nhà Xe Phụ | Cargolink C-TPAT</title>
  <style>
    :root {
      --primary: #071A36;
      --primary-light: #0B3C5D;
      --accent: #D4441E;
      --bg: #F1F5F9;
      --card: #FFFFFF;
      --border: #CBD5E1;
      --text: #0F172A;
      --muted: #64748B;
      --success: #059669;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    body { background-color: var(--bg); color: var(--text); line-height: 1.5; padding: 16px; min-height: 100vh; }
    .container { max-width: 820px; margin: 0 auto; background: var(--card); border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); overflow: hidden; border: 1px solid var(--border); }
    .conf-banner { background: #FEF3C7; border-bottom: 1.5px dashed #D97706; color: #92400E; padding: 10px 14px; font-size: 11.5px; font-weight: 700; text-align: center; text-transform: uppercase; }
    .header { background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%); color: white; padding: 24px 20px; text-align: center; }
    .header .badge { display: inline-block; background: var(--accent); color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; padding: 3px 12px; border-radius: 12px; margin-bottom: 8px; }
    .header h1 { font-size: 20px; font-weight: 800; line-height: 1.3; }
    .header p { font-size: 13px; opacity: 0.9; margin-top: 4px; }
    .nav-back { display: inline-block; margin-bottom: 6px; color: #93C5FD; text-decoration: none; font-weight: 700; font-size: 13px; }
    .form-body { padding: 24px 20px; }
    .section-title { font-size: 14px; font-weight: 800; color: var(--primary); text-transform: uppercase; margin-bottom: 14px; padding-bottom: 6px; border-bottom: 2px solid #E2E8F0; display: flex; align-items: center; gap: 8px; }
    .section-title::before { content: ""; display: inline-block; width: 4px; height: 16px; background: var(--accent); border-radius: 2px; }
    .grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-bottom: 16px; }
    .field-group { margin-bottom: 14px; }
    label { display: block; font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
    input[type="text"], input[type="date"], select {
      width: 100%; padding: 9px 12px; font-size: 13.5px; border: 1.5px solid var(--border); border-radius: 8px; background: #FFF; outline: none;
    }
    input:focus, select:focus { border-color: var(--primary-light); }
    .chk-table { width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 13px; }
    .chk-table th { background: #071A36; color: white; padding: 10px 12px; text-align: left; font-size: 12px; text-transform: uppercase; }
    .chk-table td { padding: 10px 12px; border-bottom: 1px solid #E2E8F0; vertical-align: middle; }
    .chk-table tr:nth-child(even) { background: #F8FAFC; }
    .score-summary { background: #EFF6FF; border: 2px solid #93C5FD; border-radius: 12px; padding: 16px; text-align: center; margin-bottom: 20px; }
    .sig-box { background: #F8FAFC; border: 1.5px dashed var(--border); border-radius: 8px; padding: 14px; text-align: center; margin-top: 10px; }
    canvas { background: white; border: 1px solid #CBD5E1; border-radius: 6px; width: 100%; max-width: 380px; height: 120px; touch-action: none; cursor: crosshair; }
    .sig-btns { margin-top: 6px; }
    .btn-clear { background: #E2E8F0; border: none; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; cursor: pointer; }
    .btn-submit { width: 100%; background: var(--accent); color: white; padding: 14px 20px; font-size: 15px; font-weight: 700; border: none; border-radius: 10px; cursor: pointer; margin-top: 18px; }
    .btn-submit:hover { background: #b83815; }
    .modal-overlay { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.6); z-index: 1000; align-items: center; justify-content: center; padding: 20px; }
    .modal-box { background: white; border-radius: 16px; padding: 28px 20px; max-width: 440px; width: 100%; text-align: center; }
    .btn-print { background: var(--primary); color: white; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600; border: none; cursor: pointer; margin-right: 8px; }
    .btn-close { background: #E2E8F0; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600; border: none; cursor: pointer; }
    .footer { text-align: center; font-size: 11.5px; color: var(--muted); margin-top: 20px; border-top: 1px dashed var(--border); padding-top: 12px; }
  </style>
</head>
<body>

<div class="container">
  <div class="conf-banner">🔒 TÀI LIỆU LƯU HÀNH NỘI BỘ — CARGOLINK EXPRESS (E-SUBCONTRACTOR AUDIT)</div>

  <div class="header">
    <a href="portal_driver.html" class="nav-back">⬅ Quay lại Cổng Tra Cứu</a>
    <span class="badge">AN NINH ĐỐI TÁC KINH DOANH (HS02-01 & HS02-02)</span>
    <h1>BẢNG ĐÁNH GIÁ NĂNG LỰC & AN NINH C-TPAT NHÀ XE PHỤ</h1>
    <p>Quy trình thẩm định và phê duyệt nhà cung cấp dịch vụ vận tải đường bộ theo chuẩn C-TPAT</p>
  </div>

  <form id="subForm" class="form-body" onsubmit="handleSubSubmit(event)">
    <div class="section-title">1. Thông tin Đơn vị Thầu phụ / Nhà xe đối tác</div>
    <div class="grid-2">
      <div class="field-group">
        <label>Tên Công ty / Hộ kinh doanh vận tải:</label>
        <input type="text" id="vendorName" placeholder="VD: Công ty TNHH Vận Tải An Phú Thịnh" required>
      </div>
      <div class="field-group">
        <label>Mã số thuế doanh nghiệp:</label>
        <input type="text" id="taxCode" placeholder="VD: 0314567890" required>
      </div>
      <div class="field-group">
        <label>Người đại diện pháp luật / Giám đốc:</label>
        <input type="text" id="repName" placeholder="VD: Ông Trần Minh Trí" required>
      </div>
      <div class="field-group">
        <label>Số lượng xe tải / Rơ-moóc liên kết:</label>
        <input type="text" id="fleetSize" placeholder="VD: 15 xe tải thùng kín 5T - 15T" required>
      </div>
    </div>

    <div class="section-title">2. Chấm điểm 5 Tiêu chuẩn An ninh C-TPAT (Thang điểm 100)</div>
    <table class="chk-table">
      <thead>
        <tr>
          <th style="width: 35px;">STT</th>
          <th>Tiêu chí đánh giá C-TPAT</th>
          <th style="width: 140px;">Điểm tối đa</th>
          <th style="width: 140px;">Điểm chấm</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td><strong>Hồ sơ Pháp lý & Bảo hiểm:</strong> Đầy đủ GPKD, GP vận tải bằng xe ô tô, bảo hiểm bắt buộc TNDS & bảo hiểm hàng hóa có hiệu lực.</td>
          <td>20 điểm</td>
          <td>
            <select id="s1" onchange="calcSubScore()" required>
              <option value="20">20 điểm (Đầy đủ 100%)</option>
              <option value="15">15 điểm (Thiếu bảo hiểm phụ)</option>
              <option value="10">10 điểm (Cần bổ sung GP)</option>
              <option value="0">0 điểm (Không hợp lệ)</option>
            </select>
          </td>
        </tr>
        <tr>
          <td>2</td>
          <td><strong>An ninh Nhân sự & Lái xe:</strong> 100% lái xe có xác minh lý lịch tư pháp, bằng lái phù hợp, khám sức khỏe không có ma túy.</td>
          <td>20 điểm</td>
          <td>
            <select id="s2" onchange="calcSubScore()" required>
              <option value="20">20 điểm (Đạt chuẩn 100%)</option>
              <option value="15">15 điểm (Đang chờ cấp LLTP)</option>
              <option value="10">10 điểm (Chưa khám ma túy đủ)</option>
              <option value="0">0 điểm (Không hồ sơ)</option>
            </select>
          </td>
        </tr>
        <tr>
          <td>3</td>
          <td><strong>An ninh Phương tiện & GPS:</strong> 100% xe có thiết bị GSHT hoạt động truyền dữ liệu trực tuyến, thực hiện kiểm tra xe 7 điểm.</td>
          <td>20 điểm</td>
          <td>
            <select id="s3" onchange="calcSubScore()" required>
              <option value="20">20 điểm (100% GPS Online)</option>
              <option value="15">15 điểm (Một số xe mất tín hiệu)</option>
              <option value="10">10 điểm (Chưa có checklist 7 điểm)</option>
              <option value="0">0 điểm (Không GPS)</option>
            </select>
          </td>
        </tr>
        <tr>
          <td>4</td>
          <td><strong>Kiểm soát Niêm phong Seal VVTT:</strong> Ký cam kết bảo mật chuỗi cung ứng, tuân thủ quy trình kiểm tra seal VVTT và seal ISO 17712.</td>
          <td>20 điểm</td>
          <td>
            <select id="s4" onchange="calcSubScore()" required>
              <option value="20">20 điểm (Cam kết & Hiểu rõ)</option>
              <option value="15">15 điểm (Cần đào tạo thêm VVTT)</option>
              <option value="10">10 điểm (Chưa ký cam kết C-TPAT)</option>
              <option value="0">0 điểm (Không đồng thuận)</option>
            </select>
          </td>
        </tr>
        <tr>
          <td>5</td>
          <td><strong>Khả năng Phản ứng khẩn cấp:</strong> Có hotline trực 24/7, cam kết kích hoạt báo cáo chậm ETA trong vòng 15 phút.</td>
          <td>20 điểm</td>
          <td>
            <select id="s5" onchange="calcSubScore()" required>
              <option value="20">20 điểm (Đường dây nóng 24/7)</option>
              <option value="15">15 điểm (Trực giờ hành chính)</option>
              <option value="10">10 điểm (Không có quy trình khẩn cấp)</option>
              <option value="0">0 điểm (Không phản hồi)</option>
            </select>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="score-summary">
      <div style="font-size: 13px; font-weight: 700; color: #1E40AF; text-transform: uppercase;">KẾT QUẢ ĐÁNH GIÁ NĂNG LỰC ĐỐI TÁC</div>
      <div style="font-size: 32px; font-weight: 800; color: var(--primary); margin: 6px 0;" id="totalSubScore">100 / 100 ĐIỂM</div>
      <div id="subClassification" style="display: inline-block; background: #DCFCE7; color: #166534; padding: 6px 16px; border-radius: 20px; font-weight: 800; font-size: 14px; border: 1px solid #86EFAC;">
        XẾP HẠNG: LOẠI A — ĐỦ ĐIỀU KIỆN KÝ HỢP ĐỒNG C-TPAT
      </div>
    </div>

    <div class="section-title">3. Chữ ký số Ban Đánh giá & Giám đốc Điều hành</div>
    <div class="grid-2">
      <div>
        <label>Trưởng Ban Thẩm định Đối tác ký:</label>
        <div class="sig-box">
          <canvas id="sigEvaluator"></canvas>
          <div class="sig-btns"><button type="button" class="btn-clear" onclick="clearSig('sigEvaluator')">Ký lại</button></div>
        </div>
      </div>
      <div>
        <label>Đại diện Nhà xe đối tác ký cam kết:</label>
        <div class="sig-box">
          <canvas id="sigVendor"></canvas>
          <div class="sig-btns"><button type="button" class="btn-clear" onclick="clearSig('sigVendor')">Ký lại</button></div>
        </div>
      </div>
    </div>

    <button type="submit" class="btn-submit">✅ PHÊ DUYỆT & LƯU HỒ SƠ THẦU PHỤ C-TPAT</button>
  </form>

  <div class="footer">
    CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM — PHÒNG PHÁP CHẾ & THẨM ĐỊNH THẦU PHỤ<br>
    Đánh giá định kỳ 12 tháng/lần theo tiêu chí an ninh chuỗi cung ứng C-TPAT U.S. Customs
  </div>
</div>

<div id="modalSuccess" class="modal-overlay">
  <div class="modal-box">
    <div style="font-size: 40px; margin-bottom: 10px;">🤝</div>
    <h3 style="color: var(--primary); margin-bottom: 8px;">ĐÃ PHÊ DUYỆT ĐỐI TÁC VẬN TẢI</h3>
    <p style="font-size: 13px; color: var(--muted); margin-bottom: 14px;">Mã thẩm định đối tác C-TPAT:</p>
    <div id="subCodeText" style="font-size: 18px; font-weight: 800; color: var(--accent); background: #F8FAFC; padding: 10px; border-radius: 8px; border: 1.5px dashed var(--border); margin-bottom: 16px;">SUB-2026-0000</div>
    <p style="font-size: 12px; color: var(--muted); margin-bottom: 18px;">Nhà xe thầu phụ đã được phê duyệt đưa vào Danh mục Nhà thầu đạt chuẩn chuỗi cung ứng Cargolink.</p>
    <div>
      <button class="btn-print" onclick="window.print()">🖨 In / Lưu PDF</button>
      <button class="btn-close" onclick="closeModal()">Đóng</button>
    </div>
  </div>
</div>

<script>
  function calcSubScore() {
    const s1 = parseInt(document.getElementById('s1').value) || 0;
    const s2 = parseInt(document.getElementById('s2').value) || 0;
    const s3 = parseInt(document.getElementById('s3').value) || 0;
    const s4 = parseInt(document.getElementById('s4').value) || 0;
    const s5 = parseInt(document.getElementById('s5').value) || 0;
    const total = s1 + s2 + s3 + s4 + s5;

    document.getElementById('totalSubScore').innerText = total + ' / 100 ĐIỂM';
    const tag = document.getElementById('subClassification');

    if (total >= 85) {
      tag.style.background = '#DCFCE7';
      tag.style.color = '#166534';
      tag.style.borderColor = '#86EFAC';
      tag.innerText = 'XẾP HẠNG: LOẠI A — ĐỦ ĐIỀU KIỆN KÝ HỢP ĐỒNG C-TPAT';
    } else if (total >= 70) {
      tag.style.background = '#FEF3C7';
      tag.style.color = '#92400E';
      tag.style.borderColor = '#FCD34D';
      tag.innerText = 'XẾP HẠNG: LOẠI B — CẦN KHẮC PHỤC TRONG 30 NGÀY';
    } else {
      tag.style.background = '#FEE2E2';
      tag.style.color = '#991B1B';
      tag.style.borderColor = '#FCA5A5';
      tag.innerText = 'XẾP HẠNG: LOẠI C — KHÔNG ĐẠT TIÊU CHUẨN AN NINH';
    }
  }

  function initCanvas(id) {
    const c = document.getElementById(id);
    const ctx = c.getContext('2d');
    c.width = c.offsetWidth || 340;
    c.height = 120;
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#071A36';
    let drawing = false;

    function getPos(e) {
      const rect = c.getBoundingClientRect();
      const cx = e.touches ? e.touches[0].clientX : e.clientX;
      const cy = e.touches ? e.touches[0].clientY : e.clientY;
      return { x: cx - rect.left, y: cy - rect.top };
    }
    function start(e) { drawing = true; const p = getPos(e); ctx.beginPath(); ctx.moveTo(p.x, p.y); e.preventDefault(); }
    function move(e) { if (!drawing) return; const p = getPos(e); ctx.lineTo(p.x, p.y); ctx.stroke(); e.preventDefault(); }
    function stop() { drawing = false; }

    c.addEventListener('mousedown', start);
    c.addEventListener('mousemove', move);
    window.addEventListener('mouseup', stop);
    c.addEventListener('touchstart', start);
    c.addEventListener('touchmove', move);
    window.addEventListener('touchend', stop);
  }

  window.addEventListener('load', () => {
    initCanvas('sigEvaluator');
    initCanvas('sigVendor');
    calcSubScore();
  });

  function clearSig(id) {
    const c = document.getElementById(id);
    c.getContext('2d').clearRect(0, 0, c.width, c.height);
  }

  async function handleSubSubmit(e) {
    e.preventDefault();
    const code = 'SUB-2026-' + Math.floor(1000 + Math.random() * 9000);
    const record = {
      form_type: 'subcontractor_ctpat_evaluation',
      reference_code: code,
      vendor_name: document.getElementById('vendorName').value,
      tax_code: document.getElementById('taxCode').value,
      rep_name: document.getElementById('repName').value,
      fleet_size: document.getElementById('fleetSize').value,
      scores: {
        legal_insurance: document.getElementById('s1').value,
        driver_personnel: document.getElementById('s2').value,
        fleet_gps: document.getElementById('s3').value,
        seal_vvtt: document.getElementById('s4').value,
        emergency_hotline: document.getElementById('s5').value,
      },
      total_score: document.getElementById('totalSubScore').innerText,
      classification: document.getElementById('subClassification').innerText,
      submitted_at: new Date().toISOString()
    };

    try {
      const list = JSON.parse(localStorage.getItem('cgl_sub_evals') || '[]');
      list.push(record);
      localStorage.setItem('cgl_sub_evals', JSON.stringify(list));
    } catch(err) {}

    const api = (window.location.origin.includes('github.io') || window.location.protocol === 'file:')
      ? 'https://continent-msie-goals-watt.trycloudflare.com/api/submit'
      : '/api/submit';
    try {
      await fetch(api, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(record)
      });
    } catch(err) {}

    document.getElementById('subCodeText').innerText = code;
    document.getElementById('modalSuccess').style.display = 'flex';
  }

  function closeModal() {
    document.getElementById('modalSuccess').style.display = 'none';
  }
</script>
</body>
</html>
"""

# ==========================================
# TOOL 10: app_ctpat_audit_checklist.html
# ==========================================
tool10_html = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Checklist Tự Đánh Giá Nội Bộ Sẵn Sàng Kiểm Toán C-TPAT | Cargolink Express</title>
  <style>
    :root {
      --primary: #071A36;
      --primary-light: #0B3C5D;
      --accent: #D4441E;
      --bg: #F1F5F9;
      --card: #FFFFFF;
      --border: #CBD5E1;
      --text: #0F172A;
      --muted: #64748B;
      --success: #059669;
      --danger: #DC2626;
      --warning: #D97706;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    body { background-color: var(--bg); color: var(--text); line-height: 1.5; padding: 16px; min-height: 100vh; }
    .container { max-width: 860px; margin: 0 auto; background: var(--card); border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); overflow: hidden; border: 1px solid var(--border); }
    .conf-banner { background: #FEF3C7; border-bottom: 1.5px dashed #D97706; color: #92400E; padding: 10px 14px; font-size: 11.5px; font-weight: 700; text-align: center; text-transform: uppercase; }
    .header { background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%); color: white; padding: 24px 20px; text-align: center; }
    .header .badge { display: inline-block; background: var(--accent); color: white; font-size: 11px; font-weight: 700; text-transform: uppercase; padding: 3px 12px; border-radius: 12px; margin-bottom: 8px; }
    .header h1 { font-size: 20px; font-weight: 800; line-height: 1.3; }
    .header p { font-size: 13px; opacity: 0.9; margin-top: 4px; }
    .nav-back { display: inline-block; margin-bottom: 6px; color: #93C5FD; text-decoration: none; font-weight: 700; font-size: 13px; }
    .form-body { padding: 24px 20px; }
    .section-title { font-size: 14px; font-weight: 800; color: var(--primary); text-transform: uppercase; margin-bottom: 14px; padding-bottom: 6px; border-bottom: 2px solid #E2E8F0; display: flex; align-items: center; gap: 8px; }
    .section-title::before { content: ""; display: inline-block; width: 4px; height: 16px; background: var(--accent); border-radius: 2px; }
    .grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-bottom: 16px; }
    .field-group { margin-bottom: 14px; }
    label { display: block; font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
    input[type="text"], input[type="date"], select, textarea {
      width: 100%; padding: 9px 12px; font-size: 13.5px; border: 1.5px solid var(--border); border-radius: 8px; background: #FFF; outline: none;
    }
    input:focus, select:focus, textarea:focus { border-color: var(--primary-light); }
    textarea { min-height: 80px; }
    .chk-table { width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 13px; }
    .chk-table th { background: #071A36; color: white; padding: 10px 12px; text-align: left; font-size: 12px; text-transform: uppercase; }
    .chk-table td { padding: 10px 12px; border-bottom: 1px solid #E2E8F0; vertical-align: middle; }
    .chk-table tr:nth-child(even) { background: #F8FAFC; }
    .status-opt { display: flex; gap: 10px; align-items: center; }
    .status-opt label { display: flex; align-items: center; gap: 4px; font-size: 12px; font-weight: 700; cursor: pointer; margin-bottom: 0; }
    .status-pass { color: var(--success); }
    .status-fail { color: var(--danger); }
    .audit-meter { background: #EFF6FF; border: 2px solid #93C5FD; border-radius: 12px; padding: 16px; text-align: center; margin-bottom: 20px; }
    .sig-box { background: #F8FAFC; border: 1.5px dashed var(--border); border-radius: 8px; padding: 14px; text-align: center; margin-top: 10px; }
    canvas { background: white; border: 1px solid #CBD5E1; border-radius: 6px; width: 100%; max-width: 380px; height: 120px; touch-action: none; cursor: crosshair; }
    .sig-btns { margin-top: 6px; }
    .btn-clear { background: #E2E8F0; border: none; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 600; cursor: pointer; }
    .btn-submit { width: 100%; background: var(--accent); color: white; padding: 14px 20px; font-size: 15px; font-weight: 700; border: none; border-radius: 10px; cursor: pointer; margin-top: 18px; }
    .btn-submit:hover { background: #b83815; }
    .modal-overlay { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.6); z-index: 1000; align-items: center; justify-content: center; padding: 20px; }
    .modal-box { background: white; border-radius: 16px; padding: 28px 20px; max-width: 440px; width: 100%; text-align: center; }
    .btn-print { background: var(--primary); color: white; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600; border: none; cursor: pointer; margin-right: 8px; }
    .btn-close { background: #E2E8F0; padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600; border: none; cursor: pointer; }
    .footer { text-align: center; font-size: 11.5px; color: var(--muted); margin-top: 20px; border-top: 1px dashed var(--border); padding-top: 12px; }
  </style>
</head>
<body>

<div class="container">
  <div class="conf-banner">🔒 TÀI LIỆU LƯU HÀNH NỘI BỘ — CARGOLINK EXPRESS (INTERNAL C-TPAT AUDIT)</div>

  <div class="header">
    <a href="portal_driver.html" class="nav-back">⬅ Quay lại Cổng Tra Cứu</a>
    <span class="badge">ĐÁNH GIÁ NỘI BỘ CHUỖI CUNG ỨNG (U.S. CBP C-TPAT)</span>
    <h1>CHECKLIST TỰ ĐÁNH GIÁ NỘI BỘ SẴN SÀNG KIỂM TOÁN C-TPAT</h1>
    <p>Đối chiếu toàn diện 12 Tiêu chuẩn An ninh trước đợt thanh tra khách hàng NV APPAREL</p>
  </div>

  <form id="audForm" class="form-body" onsubmit="handleAudSubmit(event)">
    <div class="section-title">1. Thông tin Đợt Tự Kiểm Toán Nội Bộ</div>
    <div class="grid-2">
      <div class="field-group">
        <label>Trưởng đoàn Kiểm toán nội bộ:</label>
        <input type="text" id="leadAuditor" value="Mr. Thành (Trưởng ban An toàn & C-TPAT)" required>
      </div>
      <div class="field-group">
        <label>Thư ký đoàn kiểm toán:</label>
        <input type="text" id="auditorSecretary" value="Ms. Bích (Điều độ vận tải)" required>
      </div>
      <div class="field-group">
        <label>Ngày thực hiện tự đánh giá:</label>
        <input type="date" id="auditDate" required>
      </div>
      <div class="field-group">
        <label>Mục đích kiểm toán:</label>
        <select id="auditPurpose">
          <option value="Sẵn sàng tiếp đoàn thanh tra Khách hàng NV APPAREL">Sẵn sàng tiếp đoàn Khách hàng NV APPAREL</option>
          <option value="Đánh giá định kỳ 6 tháng C-TPAT nội bộ">Đánh giá định kỳ 6 tháng C-TPAT nội bộ</option>
          <option value="Tái chứng nhận ISO 9001 / ISO 39001">Tái chứng nhận ISO 9001 / ISO 39001</option>
        </select>
      </div>
    </div>

    <div class="section-title">2. Bảng đối chiếu 12 Tiêu chí An ninh C-TPAT & NV Vendor Audit</div>
    <table class="chk-table">
      <thead>
        <tr>
          <th style="width: 35px;">STT</th>
          <th>12 Tiêu chí An ninh Chuỗi Cung Ứng C-TPAT</th>
          <th style="width: 170px;">Đánh giá tuân thủ</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td><strong>An ninh Đối tác (Business Partner):</strong> Thẩm định năng lực thầu phụ, cam kết an ninh C-TPAT.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="c1" value="PASS" checked onchange="calcAuditMeter()"> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="c1" value="FAIL" onchange="calcAuditMeter()"> CẦN SỬA</label>
            </div>
          </td>
        </tr>
        <tr>
          <td>2</td>
          <td><strong>An ninh Phương tiện (Conveyance):</strong> Biên bản kiểm tra an ninh xe 7/17 điểm trước mỗi chuyến xe.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="c2" value="PASS" checked onchange="calcAuditMeter()"> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="c2" value="FAIL" onchange="calcAuditMeter()"> CẦN SỬA</label>
            </div>
          </td>
        </tr>
        <tr>
          <td>3</td>
          <td><strong>Kiểm soát Niêm phong Seal:</strong> Quy trình VVTT, sử dụng seal đạt chuẩn High Security ISO 17712.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="c3" value="PASS" checked onchange="calcAuditMeter()"> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="c3" value="FAIL" onchange="calcAuditMeter()"> CẦN SỬA</label>
            </div>
          </td>
        </tr>
        <tr>
          <td>4</td>
          <td><strong>An ninh Vật lý Kho bãi:</strong> Hàng rào kiên cố, camera CCTV 24/7 lưu trữ 45 ngày, đèn chiếu sáng ban đêm.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="c4" value="PASS" checked onchange="calcAuditMeter()"> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="c4" value="FAIL" onchange="calcAuditMeter()"> CẦN SỬA</label>
            </div>
          </td>
        </tr>
        <tr>
          <td>5</td>
          <td><strong>Kiểm soát Ra vào Cổng (Access Controls):</strong> Đeo thẻ nhân viên/khách, sổ nhật ký kiểm soát xe vào bãi.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="c5" value="PASS" checked onchange="calcAuditMeter()"> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="c5" value="FAIL" onchange="calcAuditMeter()"> CẦN SỬA</label>
            </div>
          </td>
        </tr>
        <tr>
          <td>6</td>
          <td><strong>An ninh Nhân sự (Personnel Security):</strong> Xác minh lý lịch tư pháp, hợp đồng lao động, thu hồi thẻ khi nghỉ.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="c6" value="PASS" checked onchange="calcAuditMeter()"> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="c6" value="FAIL" onchange="calcAuditMeter()"> CẦN SỬA</label>
            </div>
          </td>
        </tr>
        <tr>
          <td>7</td>
          <td><strong>An toàn Quy trình & Giám sát GPS:</strong> Giám sát lộ trình xe trực tuyến, dừng đỗ đúng trạm quy định.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="c7" value="PASS" checked onchange="calcAuditMeter()"> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="c7" value="FAIL" onchange="calcAuditMeter()"> CẦN SỬA</label>
            </div>
          </td>
        </tr>
        <tr>
          <td>8</td>
          <td><strong>An ninh Thông tin & NĐ 13/2023/NĐ-CP:</strong> Mật khẩu mạnh, phân quyền dữ liệu, bảo mật thông tin tài xế.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="c8" value="PASS" checked onchange="calcAuditMeter()"> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="c8" value="FAIL" onchange="calcAuditMeter()"> CẦN SỬA</label>
            </div>
          </td>
        </tr>
        <tr>
          <td>9</td>
          <td><strong>Đào tạo Nhận thức C-TPAT:</strong> Huấn luyện định kỳ tài xế, bài thi trắc nghiệm có cấp chứng chỉ.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="c9" value="PASS" checked onchange="calcAuditMeter()"> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="c9" value="FAIL" onchange="calcAuditMeter()"> CẦN SỬA</label>
            </div>
          </td>
        </tr>
        <tr>
          <td>10</td>
          <td><strong>An ninh Nông nghiệp (Agricultural):</strong> Xe sạch sẽ, không có đất cát, rơm rạ, sinh vật ngoại lai.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="c10" value="PASS" checked onchange="calcAuditMeter()"> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="c10" value="FAIL" onchange="calcAuditMeter()"> CẦN SỬA</label>
            </div>
          </td>
        </tr>
        <tr>
          <td>11</td>
          <td><strong>An toàn Giao thông ISO 39001:</strong> Kiểm tra 0.00 mg/L nồng độ cồn & test âm tính ma túy trước giờ chạy.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="c11" value="PASS" checked onchange="calcAuditMeter()"> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="c11" value="FAIL" onchange="calcAuditMeter()"> CẦN SỬA</label>
            </div>
          </td>
        </tr>
        <tr>
          <td>12</td>
          <td><strong>CSR, Nhân quyền & Chống tiêu cực:</strong> Hộp thư tố giác an toàn, cấm lao động trẻ em, cấm cưỡng bức.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="c12" value="PASS" checked onchange="calcAuditMeter()"> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="c12" value="FAIL" onchange="calcAuditMeter()"> CẦN SỬA</label>
            </div>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="audit-meter">
      <div style="font-size: 13px; font-weight: 700; color: #1E40AF; text-transform: uppercase;">MỨC ĐỘ SẴN SÀNG KIỂM TOÁN (AUDIT READINESS SCORE)</div>
      <div style="font-size: 34px; font-weight: 800; color: #059669; margin: 6px 0;" id="auditScoreText">100% (12/12 ĐẠT)</div>
      <div id="auditBadge" style="display: inline-block; background: #DCFCE7; color: #166534; padding: 6px 16px; border-radius: 20px; font-weight: 800; font-size: 14px; border: 1px solid #86EFAC;">
        ✅ ĐỦ ĐIỀU KIỆN TIẾP ĐOÀN THANH TRA NV APPAREL (AUDIT READY)
      </div>
    </div>

    <div class="section-title">3. Kế hoạch hành động khắc phục (Action Plan)</div>
    <div class="field-group">
      <label>Ghi chú các điểm cần lưu ý trước ngày kiểm toán chính thức:</label>
      <textarea id="actionPlan" placeholder="VD: Nhắc nhở tài xế mang đầy đủ thẻ tên có ảnh, kiểm tra áp kế bình chữa cháy xe 51C-964.55 trước giờ đón đoàn...">100% tài xế và nhân viên điều độ đã hoàn thành khóa huấn luyện nhận thức C-TPAT. Toàn bộ hồ sơ bản cứng và bản điện tử đã được chuẩn hóa đồng bộ.</textarea>
    </div>

    <div class="section-title">4. Chữ ký số Ban Kiểm toán & Ban Giám đốc</div>
    <div class="grid-2">
      <div>
        <label>Trưởng đoàn Kiểm toán nội bộ ký:</label>
        <div class="sig-box">
          <canvas id="sigLeadAuditor"></canvas>
          <div class="sig-btns"><button type="button" class="btn-clear" onclick="clearSig('sigLeadAuditor')">Ký lại</button></div>
        </div>
      </div>
      <div>
        <label>Giám đốc Điều hành phê duyệt:</label>
        <div class="sig-box">
          <canvas id="sigDirector"></canvas>
          <div class="sig-btns"><button type="button" class="btn-clear" onclick="clearSig('sigDirector')">Ký lại</button></div>
        </div>
      </div>
    </div>

    <button type="submit" class="btn-submit">📋 LƯU BÁO CÁO TỰ ĐÁNH GIÁ SẴN SÀNG KIỂM TOÁN C-TPAT</button>
  </form>

  <div class="footer">
    CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM — BAN ĐẢM BẢO CHẤT LƯỢNG (QA/QC)<br>
    Báo cáo đối chiếu tuân thủ phục vụ thanh tra an ninh chuỗi cung ứng của Khách hàng NV APPAREL
  </div>
</div>

<div id="modalSuccess" class="modal-overlay">
  <div class="modal-box">
    <div style="font-size: 40px; margin-bottom: 10px;">🏆</div>
    <h3 style="color: var(--primary); margin-bottom: 8px;">ĐÃ LƯU BÁO CÁO TỰ KIỂM TOÁN</h3>
    <p style="font-size: 13px; color: var(--muted); margin-bottom: 14px;">Mã báo cáo kiểm toán nội bộ:</p>
    <div id="audCodeText" style="font-size: 18px; font-weight: 800; color: var(--accent); background: #F8FAFC; padding: 10px; border-radius: 8px; border: 1.5px dashed var(--border); margin-bottom: 16px;">AUD-2026-0000</div>
    <p style="font-size: 12px; color: var(--muted); margin-bottom: 18px;">Hồ sơ năng lực và quy trình an ninh đã sẵn sàng phục vụ thanh tra chính thức từ đối tác NV APPAREL.</p>
    <div>
      <button class="btn-print" onclick="window.print()">🖨 In / Lưu PDF</button>
      <button class="btn-close" onclick="closeModal()">Đóng</button>
    </div>
  </div>
</div>

<script>
  function initNow() {
    const d = new Date();
    document.getElementById('auditDate').value = d.toISOString().split('T')[0];
  }
  initNow();

  function calcAuditMeter() {
    let passCount = 0;
    for (let i = 1; i <= 12; i++) {
      const checked = document.querySelector(`input[name="c${i}"]:checked`);
      if (checked && checked.value === 'PASS') passCount++;
    }
    const pct = Math.round((passCount / 12) * 100);
    document.getElementById('auditScoreText').innerText = `${pct}% (${passCount}/12 ĐẠT)`;
    const badge = document.getElementById('auditBadge');

    if (pct >= 90) {
      badge.style.background = '#DCFCE7';
      badge.style.color = '#166534';
      badge.style.borderColor = '#86EFAC';
      badge.innerText = '✅ ĐỦ ĐIỀU KIỆN TIẾP ĐOÀN THANH TRA NV APPAREL (AUDIT READY)';
    } else {
      badge.style.background = '#FEF3C7';
      badge.style.color = '#92400E';
      badge.style.borderColor = '#FCD34D';
      badge.innerText = '⚠️ CẦN HOÀN THIỆN CÁC ĐIỂM CHƯA ĐẠT TRƯỚC NGÀY KIỂM TOÁN';
    }
  }

  function initCanvas(id) {
    const c = document.getElementById(id);
    const ctx = c.getContext('2d');
    c.width = c.offsetWidth || 340;
    c.height = 120;
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#071A36';
    let drawing = false;

    function getPos(e) {
      const rect = c.getBoundingClientRect();
      const cx = e.touches ? e.touches[0].clientX : e.clientX;
      const cy = e.touches ? e.touches[0].clientY : e.clientY;
      return { x: cx - rect.left, y: cy - rect.top };
    }
    function start(e) { drawing = true; const p = getPos(e); ctx.beginPath(); ctx.moveTo(p.x, p.y); e.preventDefault(); }
    function move(e) { if (!drawing) return; const p = getPos(e); ctx.lineTo(p.x, p.y); ctx.stroke(); e.preventDefault(); }
    function stop() { drawing = false; }

    c.addEventListener('mousedown', start);
    c.addEventListener('mousemove', move);
    window.addEventListener('mouseup', stop);
    c.addEventListener('touchstart', start);
    c.addEventListener('touchmove', move);
    window.addEventListener('touchend', stop);
  }

  window.addEventListener('load', () => {
    initCanvas('sigLeadAuditor');
    initCanvas('sigDirector');
    calcAuditMeter();
  });

  function clearSig(id) {
    const c = document.getElementById(id);
    c.getContext('2d').clearRect(0, 0, c.width, c.height);
  }

  async function handleAudSubmit(e) {
    e.preventDefault();
    const code = 'AUD-2026-' + Math.floor(1000 + Math.random() * 9000);
    const checks = {};
    for (let i = 1; i <= 12; i++) {
      checks[`c${i}`] = document.querySelector(`input[name="c${i}"]:checked`).value;
    }
    const record = {
      form_type: 'ctpat_internal_self_audit',
      reference_code: code,
      lead_auditor: document.getElementById('leadAuditor').value,
      auditor_secretary: document.getElementById('auditorSecretary').value,
      audit_date: document.getElementById('auditDate').value,
      audit_purpose: document.getElementById('auditPurpose').value,
      criteria: checks,
      score_text: document.getElementById('auditScoreText').innerText,
      badge_text: document.getElementById('auditBadge').innerText,
      action_plan: document.getElementById('actionPlan').value,
      submitted_at: new Date().toISOString()
    };

    try {
      const list = JSON.parse(localStorage.getItem('cgl_audit_checklists') || '[]');
      list.push(record);
      localStorage.setItem('cgl_audit_checklists', JSON.stringify(list));
    } catch(err) {}

    const api = (window.location.origin.includes('github.io') || window.location.protocol === 'file:')
      ? 'https://continent-msie-goals-watt.trycloudflare.com/api/submit'
      : '/api/submit';
    try {
      await fetch(api, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(record)
      });
    } catch(err) {}

    document.getElementById('audCodeText').innerText = code;
    document.getElementById('modalSuccess').style.display = 'flex';
  }

  function closeModal() {
    document.getElementById('modalSuccess').style.display = 'none';
  }
</script>
</body>
</html>
"""

with open(os.path.join(output_dir, "app_visitor_gate_log.html"), "w", encoding="utf-8") as f:
    f.write(tool7_html)

with open(os.path.join(output_dir, "app_green_office_log.html"), "w", encoding="utf-8") as f:
    f.write(tool8_html)

with open(os.path.join(output_dir, "app_subcontractor_eval.html"), "w", encoding="utf-8") as f:
    f.write(tool9_html)

with open(os.path.join(output_dir, "app_ctpat_audit_checklist.html"), "w", encoding="utf-8") as f:
    f.write(tool10_html)

print("Tools 7, 8, 9, 10 created successfully.")
