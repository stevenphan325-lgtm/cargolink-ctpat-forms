# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
output_dir = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS"

# 1. TOOL 2: app_seal_vvtt_log.html
tool2_html = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Biên Bản Kiểm Tra Niêm Phong Seal VVTT & Bàn Giao Cắt Seal | Cargolink C-TPAT</title>
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
    .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-bottom: 16px; }
    .field-group { margin-bottom: 14px; }
    label { display: block; font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
    input[type="text"], input[type="date"], input[type="time"], select, textarea {
      width: 100%; padding: 9px 12px; font-size: 13.5px; border: 1.5px solid var(--border); border-radius: 8px; background: #FFF; outline: none;
    }
    input:focus, select:focus, textarea:focus { border-color: var(--primary-light); }
    .chk-table { width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 13px; }
    .chk-table th { background: #071A36; color: white; padding: 10px 12px; text-align: left; font-size: 12px; text-transform: uppercase; }
    .chk-table td { padding: 10px 12px; border-bottom: 1px solid #E2E8F0; vertical-align: middle; }
    .chk-table tr:nth-child(even) { background: #F8FAFC; }
    .status-opt { display: flex; gap: 12px; align-items: center; }
    .status-opt label { display: flex; align-items: center; gap: 4px; font-size: 12.5px; font-weight: 600; cursor: pointer; margin-bottom: 0; }
    .status-pass { color: var(--success); }
    .status-fail { color: var(--danger); }
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
    .step-badge { background: #E0E7FF; color: #3730A3; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 6px; }
  </style>
</head>
<body>

<div class="container">
  <div class="conf-banner">🔒 TÀI LIỆU LƯU HÀNH NỘI BỘ — CARGOLINK EXPRESS (E-SEAL VVTT LOG)</div>

  <div class="header">
    <a href="portal_driver.html" class="nav-back">⬅ Quay lại Cổng Tra Cứu</a>
    <span class="badge">QUY TRÌNH QUẢN LÝ NIÊM PHONG SEAL (HS17-06 & WI-SEC-001)</span>
    <h1>BIÊN BẢN KIỂM TRA NIÊM PHONG SEAL VVTT & BÀN GIAO CẮT SEAL ĐIỆN TỬ</h1>
    <p>Áp dụng cho tất cả chuyến xe vận chuyển hàng hóa xuất nhập khẩu của Nhà máy NV APPAREL</p>
  </div>

  <form id="sealForm" class="form-body" onsubmit="handleSealSubmit(event)">
    <div class="section-title">1. Thông tin chuyến hàng & Niêm phong Seal</div>
    <div class="grid-2">
      <div class="field-group">
        <label>Khách hàng / Nhà máy:</label>
        <input type="text" id="customerName" value="Công ty TNHH May Mặc NV (NV Apparel)" readonly>
      </div>
      <div class="field-group">
        <label>Số Bill / Booking / Delivery Note (DN):</label>
        <input type="text" id="docNumber" placeholder="VD: DN-NV-2026-088" required>
      </div>
      <div class="field-group">
        <label>Biển số xe đầu kéo / Xe tải:</label>
        <select id="truckPlate" required>
          <option value="51C-964.55">51C-964.55 (Isuzu 2.5T)</option>
          <option value="51D-882.14">51D-882.14 (Hino 5T)</option>
          <option value="50H-123.68">50H-123.68 (Isuzu 8T)</option>
          <option value="51C-774.92">51C-774.92 (Hyundai 3.5T)</option>
        </select>
      </div>
      <div class="field-group">
        <label>Số Rơ-moóc / Số Container (nếu có):</label>
        <input type="text" id="contNumber" placeholder="VD: 51R-089.12 / TCLU 984512-3">
      </div>
      <div class="field-group">
        <label>Số Seal C-TPAT High Security (ISO 17712):</label>
        <input type="text" id="sealNumber" placeholder="VD: CGL-982147 / NV-2026-0042" required style="font-weight: 700; color: #1E3A8A;">
      </div>
      <div class="field-group">
        <label>Chủng loại Seal niêm phong:</label>
        <select id="sealType" required>
          <option value="Seal cối (Bolt Seal C-TPAT ISO 17712)">Seal cối (Bolt Seal C-TPAT ISO 17712)</option>
          <option value="Seal cáp thép bấm (Cable Seal 3.5mm-5mm)">Seal cáp thép bấm (Cable Seal 3.5mm-5mm)</option>
          <option value="Seal nhựa có khóa kim loại (Dây rút)">Seal nhựa có khóa kim loại (Dây rút)</option>
        </select>
      </div>
    </div>

    <div class="section-title">2. Quy trình kiểm tra Seal 4 bước chuẩn VVTT (View - Verify - Tug - Twist)</div>
    <div style="background: #EFF6FF; border-left: 4px solid #2563EB; padding: 10px 14px; border-radius: 6px; font-size: 12.5px; color: #1E40AF; margin-bottom: 14px;">
      Bắt buộc thực hiện đầy đủ 4 bước VVTT trước khi xe rời điểm đóng hàng và trước khi cắt seal tại điểm giao hàng.
    </div>

    <table class="chk-table">
      <thead>
        <tr>
          <th style="width: 80px;">Bước</th>
          <th>Nội dung thao tác kiểm tra VVTT</th>
          <th style="width: 170px;">Kết quả</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="step-badge">V - View</span></td>
          <td><strong>Quan sát bằng mắt:</strong> Kiểm tra chốt khóa, thân seal, tai khóa xem có dấu hiệu cạy phá, mài mòn, dán keo, tráo đổi hay biến dạng không.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="vvtt_v" value="PASS" checked> ĐẠT</label>
              <label class="status-fail"><input type="radio" name="vvtt_v" value="FAIL"> BẤT THƯỜNG</label>
            </div>
          </td>
        </tr>
        <tr>
          <td><span class="step-badge">V - Verify</span></td>
          <td><strong>Xác thực thông tin:</strong> So khớp chính xác 100% từng ký tự và số seri in khắc trên thân seal với Phiếu xuất kho / Lệnh điều xe.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="vvtt_ver" value="PASS" checked> TRÙNG KHỚP</label>
              <label class="status-fail"><input type="radio" name="vvtt_ver" value="FAIL"> SAI LỆCH</label>
            </div>
          </td>
        </tr>
        <tr>
          <td><span class="step-badge">T - Tug</span></td>
          <td><strong>Giật kéo kiểm tra lực:</strong> Cầm chắc thân seal và giật mạnh theo hướng mở để đảm bảo chốt ngàm khóa đã gài chặt, không bị tuột.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="vvtt_t1" value="PASS" checked> CHẮC CHẮN</label>
              <label class="status-fail"><input type="radio" name="vvtt_t1" value="FAIL"> TUỘT/LỎNG</label>
            </div>
          </td>
        </tr>
        <tr>
          <td><span class="step-badge">T - Twist</span></td>
          <td><strong>Xoay kiểm tra khớp:</strong> Xoay tròn thân seal và đầu cối sang hai bên để đảm bảo không bị xoay tròn tự do hoặc lỏng chân chốt.</td>
          <td>
            <div class="status-opt">
              <label class="status-pass"><input type="radio" name="vvtt_t2" value="PASS" checked> ĐẠT CHUẨN</label>
              <label class="status-fail"><input type="radio" name="vvtt_t2" value="FAIL"> KHÔNG ĐẠT</label>
            </div>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="section-title">3. Nhật ký thời gian & Tình trạng bàn giao cắt Seal</div>
    <div class="grid-2">
      <div class="field-group">
        <label>Thời gian bấm niêm phong seal:</label>
        <div style="display: flex; gap: 8px;">
          <input type="date" id="sealDate" required>
          <input type="time" id="sealTime" required>
        </div>
      </div>
      <div class="field-group">
        <label>Thời gian cắt seal tại kho đích:</label>
        <div style="display: flex; gap: 8px;">
          <input type="date" id="cutDate">
          <input type="time" id="cutTime">
        </div>
      </div>
      <div class="field-group" style="grid-column: 1 / -1;">
        <label>Ghi chú tình trạng hàng hóa & Thùng xe khi cắt seal:</label>
        <textarea id="sealNotes" placeholder="VD: Seal nguyên vẹn 100%, không bị xước cạy, hàng hóa bên trong đầy đủ theo packing list, không có côn trùng hay ẩm ướt."></textarea>
      </div>
    </div>

    <div class="section-title">4. Chữ ký số xác nhận hai bên (Digital Signatures)</div>
    <div class="grid-2">
      <div>
        <label>Tài xế Cargolink kiểm tra & Ký tên:</label>
        <div class="sig-box">
          <canvas id="sigDriver"></canvas>
          <div class="sig-btns"><button type="button" class="btn-clear" onclick="clearSig('sigDriver')">Ký lại</button></div>
        </div>
      </div>
      <div>
        <label>Đại diện Kho NV Apparel / Bảo vệ giám sát ký tên:</label>
        <div class="sig-box">
          <canvas id="sigCustomer"></canvas>
          <div class="sig-btns"><button type="button" class="btn-clear" onclick="clearSig('sigCustomer')">Ký lại</button></div>
        </div>
      </div>
    </div>

    <button type="submit" class="btn-submit">🔒 XÁC NHẬN & LƯU BIÊN BẢN SEAL VVTT ĐIỆN TỬ</button>
  </form>

  <div class="footer">
    CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM — HỆ THỐNG KIỂM SOÁT NIÊM PHONG C-TPAT<br>
    Quy trình tuân thủ tiêu chuẩn Hải quan Hoa Kỳ (U.S. CBP C-TPAT) & ISO 17712 High Security
  </div>
</div>

<div id="modalSuccess" class="modal-overlay">
  <div class="modal-box">
    <div style="font-size: 40px; margin-bottom: 10px;">✅</div>
    <h3 style="color: var(--primary); margin-bottom: 8px;">BIÊN BẢN SEAL ĐÃ ĐƯỢC LƯU</h3>
    <p style="font-size: 13px; color: var(--muted); margin-bottom: 14px;">Mã xác thực biên bản điện tử:</p>
    <div id="sealCodeText" style="font-size: 18px; font-weight: 800; color: var(--accent); background: #F8FAFC; padding: 10px; border-radius: 8px; border: 1.5px dashed var(--border); margin-bottom: 16px;">SEAL-2026-0000</div>
    <p style="font-size: 12px; color: var(--muted); margin-bottom: 18px;">Dữ liệu đã được mã hóa lưu trữ offline trên thiết bị và đồng bộ hệ thống điều độ Cargolink 24/7.</p>
    <div>
      <button class="btn-print" onclick="window.print()">🖨 In / Lưu PDF</button>
      <button class="btn-close" onclick="closeModal()">Đóng</button>
    </div>
  </div>
</div>

<script>
  function initNow() {
    const d = new Date();
    document.getElementById('sealDate').value = d.toISOString().split('T')[0];
    document.getElementById('sealTime').value = d.toTimeString().slice(0,5);
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
    initCanvas('sigDriver');
    initCanvas('sigCustomer');
  });

  function clearSig(id) {
    const c = document.getElementById(id);
    c.getContext('2d').clearRect(0, 0, c.width, c.height);
  }

  async function handleSealSubmit(e) {
    e.preventDefault();
    const code = 'SEAL-2026-' + Math.floor(1000 + Math.random() * 9000);
    const record = {
      form_type: 'seal_vvtt_inspection_log',
      reference_code: code,
      doc_number: document.getElementById('docNumber').value,
      truck_plate: document.getElementById('truckPlate').value,
      cont_number: document.getElementById('contNumber').value,
      seal_number: document.getElementById('sealNumber').value,
      seal_type: document.getElementById('sealType').value,
      vvtt_view: document.querySelector('input[name="vvtt_v"]:checked').value,
      vvtt_verify: document.querySelector('input[name="vvtt_ver"]:checked').value,
      vvtt_tug: document.querySelector('input[name="vvtt_t1"]:checked').value,
      vvtt_twist: document.querySelector('input[name="vvtt_t2"]:checked').value,
      seal_date: document.getElementById('sealDate').value,
      seal_time: document.getElementById('sealTime').value,
      cut_date: document.getElementById('cutDate').value,
      cut_time: document.getElementById('cutTime').value,
      notes: document.getElementById('sealNotes').value,
      submitted_at: new Date().toISOString()
    };

    try {
      const list = JSON.parse(localStorage.getItem('cgl_seal_logs') || '[]');
      list.push(record);
      localStorage.setItem('cgl_seal_logs', JSON.stringify(list));
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

    document.getElementById('sealCodeText').innerText = code;
    document.getElementById('modalSuccess').style.display = 'flex';
  }

  function closeModal() {
    document.getElementById('modalSuccess').style.display = 'none';
  }
</script>
</body>
</html>
"""

with open(os.path.join(output_dir, "app_seal_vvtt_log.html"), "w", encoding="utf-8") as f:
    f.write(tool2_html)

print("Tool 2: app_seal_vvtt_log.html created successfully.")
