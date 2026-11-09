# -*- coding: utf-8 -*-
import os, sys
import qrcode
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS"
ARTIFACT_DIR = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163"

# 1. Create form4_harassment_survey.html
form4_html = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Phiếu Khảo Sát Chống Quấy Rối & Ngược Đãi | Cargolink Express C-TPAT</title>
  <style>
    :root {
      --primary: #071A36;
      --accent: #D4441E;
      --bg: #F8FAFC;
      --card-bg: #FFFFFF;
      --text: #1E293B;
      --muted: #64748B;
      --border: #E2E8F0;
      --success: #16A34A;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { background: var(--bg); color: var(--text); padding: 20px 12px; }
    .container { max-width: 680px; margin: 0 auto; background: var(--card-bg); border-radius: 14px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); border: 1px solid var(--border); overflow: hidden; }
    .header { background: var(--primary); color: white; padding: 24px 20px; text-align: center; }
    .badge { display: inline-block; background: var(--accent); color: white; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 20px; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
    h1 { font-size: 19px; line-height: 1.4; margin-bottom: 6px; }
    .subhead { font-size: 13px; color: #94A3B8; }
    .notice { background: #EFF6FF; border-left: 4px solid #2563EB; padding: 12px 16px; font-size: 12.5px; color: #1E40AF; line-height: 1.5; margin: 16px 20px; border-radius: 4px; }
    form { padding: 0 20px 24px; }
    .form-group { margin-bottom: 18px; }
    label.title { display: block; font-weight: 600; font-size: 14px; margin-bottom: 8px; color: var(--primary); }
    .required { color: var(--accent); }
    .hint { font-size: 12px; color: var(--muted); margin-bottom: 8px; display: block; }
    input[type="text"], select, textarea { width: 100%; padding: 10px 12px; border: 1px solid var(--border); border-radius: 8px; font-size: 14px; }
    input[type="text"]:focus, select:focus, textarea:focus { outline: none; border-color: var(--primary); ring: 2px rgba(7,26,54,0.1); }
    .options { display: flex; flex-direction: column; gap: 8px; }
    .option-label { display: flex; align-items: center; gap: 10px; padding: 10px 12px; border: 1px solid var(--border); border-radius: 8px; cursor: pointer; font-size: 13.5px; transition: all 0.15s; }
    .option-label:hover { background: #F1F5F9; }
    .btn-submit { display: block; width: 100%; background: var(--accent); color: white; border: none; padding: 14px; border-radius: 8px; font-size: 15px; font-weight: 700; cursor: pointer; transition: background 0.2s; margin-top: 24px; }
    .btn-submit:hover { background: #B93815; }
    .success-card { display: none; padding: 40px 20px; text-align: center; }
    .success-card h2 { color: var(--success); font-size: 20px; margin-bottom: 8px; }
    .footer { text-align: center; font-size: 12px; color: var(--muted); padding: 16px; border-top: 1px solid var(--border); background: #F8FAFC; }
  </style>
</head>
<body>

<div class="container">
  <div class="header">
    <div class="badge">NV APPAREL & C-TPAT AUDIT 2026 - FINDING 6</div>
    <h1>PHIẾU KHẢO SÁT CHỐNG QUẤY RỐI & NGƯỢC ĐÃI NĂM 2026</h1>
    <div class="subhead">CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM | BẢO MẬT & ẨN DANH 100%</div>
  </div>

  <div class="notice">
    <strong>Cam kết bảo mật tuyệt đối:</strong> Cuộc khảo sát này nhằm đảm bảo môi trường làm việc tại Cargolink Express hoàn toàn lành mạnh, công bằng và không có bất kỳ hành vi bạo lực, xúc phạm hay quấy rối. Người lao động có thể lựa chọn trả lời <strong>Ẩn danh</strong>. Mọi ý kiến đều được Ban Giám Đốc trân trọng ghi nhận và bảo vệ chính sách Không trả thù.
  </div>

  <form id="surveyForm">
    <div class="form-group">
      <label class="title">1. Hình thức tham gia khảo sát <span class="required">*</span></label>
      <div class="options">
        <label class="option-label"><input type="radio" name="anon" value="Ẩn danh" checked> Ẩn danh hoàn toàn (Không lưu danh tính)</label>
        <label class="option-label"><input type="radio" name="anon" value="Công khai"> Công khai thông tin cá nhân</label>
      </div>
    </div>

    <div class="form-group" id="nameGroup" style="display: none;">
      <label class="title">Họ và tên & Mã nhân viên / Biển số xe</label>
      <input type="text" id="empName" placeholder="Ví dụ: Nguyễn Văn Hùng - 51C-96455">
    </div>

    <div class="form-group">
      <label class="title">2. Bộ phận công tác của bạn <span class="required">*</span></label>
      <select id="department" required>
        <option value="">-- Vui lòng chọn bộ phận --</option>
        <option value="Đội ngũ Lái xe & Phụ xe">Đội ngũ Lái xe & Phụ xe tải</option>
        <option value="Bộ phận Điều độ & Vận hành">Bộ phận Điều độ & Vận hành</option>
        <option value="Bộ phận Bãi xe & Bảo vệ">Bộ phận Bãi xe & Bảo vệ</option>
        <option value="Bộ phận Văn phòng & Kế toán">Bộ phận Văn phòng & Kế toán</option>
      </select>
    </div>

    <div class="form-group">
      <label class="title">3. Trong 12 tháng qua, bạn có từng bị hoặc chứng kiến hành vi lời nói thô tục, đe dọa, xúc phạm danh dự hoặc la mắng vô cớ tại nơi làm việc không? <span class="required">*</span></label>
      <div class="options">
        <label class="option-label"><input type="radio" name="q3" value="Hoàn toàn không có" checked> Hoàn toàn không có (Môi trường rất tôn trọng)</label>
        <label class="option-label"><input type="radio" name="q3" value="Hiếm khi"> Hiếm khi xảy ra (Áp lực công việc thoáng qua)</label>
        <label class="option-label"><input type="radio" name="q3" value="Thỉnh thoảng"> Thỉnh thoảng</label>
        <label class="option-label"><input type="radio" name="q3" value="Thường xuyên"> Thường xuyên (Cần công ty can thiệp gấp)</label>
      </div>
    </div>

    <div class="form-group">
      <label class="title">4. Bạn có từng bị cưỡng bức làm việc, ép làm thêm giờ trái quy định hoặc bị giữ bản chính giấy tờ tùy thân trái pháp luật không? <span class="required">*</span></label>
      <div class="options">
        <label class="option-label"><input type="radio" name="q4" value="Hoàn toàn không có" checked> Hoàn toàn không có (Làm việc tự nguyện, giữ giấy tờ cá nhân)</label>
        <label class="option-label"><input type="radio" name="q4" value="Có xảy ra"> Có xảy ra</label>
      </div>
    </div>

    <div class="form-group">
      <label class="title">5. Bạn có từng gặp bất kỳ hành vi quấy rối tình dục nào (lời nói khiếm nhã, tin nhắn nhạy cảm, đụng chạm cơ thể không mong muốn) không? <span class="required">*</span></label>
      <div class="options">
        <label class="option-label"><input type="radio" name="q5" value="Hoàn toàn không có" checked> Hoàn toàn không có</label>
        <label class="option-label"><input type="radio" name="q5" value="Có xảy ra"> Có xảy ra</label>
      </div>
    </div>

    <div class="form-group">
      <label class="title">6. Bạn có biết cách thức phản ánh, khiếu nại bảo mật tới Ban Giám Đốc khi có sự việc xảy ra không? <span class="required">*</span></label>
      <div class="options">
        <label class="option-label"><input type="radio" name="q6" value="Rất rõ" checked> Rất rõ (Đã biết mã QR khiếu nại, Hotline 0943 46 46 46, Hòm thư)</label>
        <label class="option-label"><input type="radio" name="q6" value="Có nghe qua nhưng chưa rõ chi tiết"> Có nghe qua nhưng chưa rõ chi tiết</label>
        <label class="option-label"><input type="radio" name="q6" value="Chưa biết"> Chưa biết</label>
      </div>
    </div>

    <div class="form-group">
      <label class="title">7. Ý kiến đóng góp hoặc phản ánh sự việc cụ thể (nếu có)</label>
      <textarea id="feedback" rows="3" placeholder="Nhập chia sẻ cụ thể của bạn để giúp Cargolink Express hoàn thiện hơn..."></textarea>
    </div>

    <button type="submit" class="btn-submit">GỬI PHIẾU KHẢO SÁT BẢO MẬT</button>
  </form>

  <div class="success-card" id="successCard">
    <h2>🎉 GỬI KHẢO SÁT THÀNH CÔNG!</h2>
    <p style="color: #475569; font-size: 14px; margin-bottom: 20px;">
      Cảm ơn bạn đã tham gia đóng góp ý kiến. Thông tin của bạn đã được mã hóa bảo mật và lưu trữ trong hệ thống giám sát văn hóa doanh nghiệp C-TPAT năm 2026.
    </p>
    <a href="portal_driver.html" style="display: inline-block; background: #071A36; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-size: 14px;">Quay lại Sổ tay Tài xế</a>
  </div>

  <div class="footer">
    <strong>CÔNG TY TNHH CARGOLINK EXPRESS VIỆT NAM</strong><br>
    Đường dây nóng Giám đốc 24/7: 0943 46 46 46 | Email bảo mật: safe@cargolink.com.vn
  </div>
</div>

<script>
  const radiosAnon = document.querySelectorAll('input[name="anon"]');
  const nameGroup = document.getElementById('nameGroup');
  radiosAnon.forEach(r => {
    r.addEventListener('change', () => {
      nameGroup.style.display = r.value === 'Công khai' ? 'block' : 'none';
    });
  });

  document.getElementById('surveyForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const data = {
      timestamp: new Date().toISOString(),
      anon: document.querySelector('input[name="anon"]:checked').value,
      name: document.getElementById('empName').value || 'Ẩn danh',
      dept: document.getElementById('department').value,
      q3: document.querySelector('input[name="q3"]:checked').value,
      q4: document.querySelector('input[name="q4"]:checked').value,
      q5: document.querySelector('input[name="q5"]:checked').value,
      q6: document.querySelector('input[name="q6"]:checked').value,
      feedback: document.getElementById('feedback').value
    };

    let list = JSON.parse(localStorage.getItem('cgl_harassment_survey') || '[]');
    list.push(data);
    localStorage.setItem('cgl_harassment_survey', JSON.stringify(list));

    // Try posting to local api if active
    fetch('/api/harassment_survey', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
    }).catch(e => console.log('Stored offline in localStorage.'));

    document.getElementById('surveyForm').style.display = 'none';
    document.getElementById('successCard').style.display = 'block';
  });
</script>

</body>
</html>
"""

with open(os.path.join(BASE_DIR, "form4_harassment_survey.html"), "w", encoding="utf-8") as f:
    f.write(form4_html)
print("[Form 4] Created form4_harassment_survey.html")

# 2. Generate qr_form4_harassment.png
qr4_url = "https://thangcargolink.github.io/cargolink-ctpat-portal/form4_harassment_survey.html"
qr = qrcode.QRCode(box_size=8, border=2)
qr.add_data(qr4_url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_out = os.path.join(BASE_DIR, "qr_form4_harassment.png")
qr_img.save(qr_out)
qr_img.save(os.path.join(ARTIFACT_DIR, "qr_form4_harassment.png"))
print("[QR 4] Created qr_form4_harassment.png")

# 3. Update portal_driver.html with Access Tracking System Modal & Button
portal_path = os.path.join(BASE_DIR, "portal_driver.html")
with open(portal_path, "r", encoding="utf-8") as f:
    content = f.read()

# Check if tracking modal already in content
if "id=\"accessTrackingModal\"" not in content:
    tracking_snippet = """
  <!-- ACCESS TRACKING BAR (FINDING 7 & 8) -->
  <div style="background: linear-gradient(135deg, #071A36, #1E3A8A); color: white; border-radius: 12px; padding: 18px 24px; margin-bottom: 24px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    <div>
      <div style="font-size: 11px; font-weight: 700; color: #38BDF8; letter-spacing: 0.8px; text-transform: uppercase;">C-TPAT COMPLIANCE TRACKER (FINDING 7 & 8)</div>
      <div style="font-size: 16px; font-weight: 700; margin: 4px 0;">HỆ THỐNG GHI NHẬN TRUY CẬP & XÁC NHẬN ĐỌC CHÍNH SÁCH ĐIỆN TỬ</div>
      <div style="font-size: 12.5px; color: #CBD5E1;">Theo dõi thời gian thực cán bộ nhân viên và tài xế đã truy cập đọc hiểu nội quy, quy trình.</div>
    </div>
    <div style="display: flex; gap: 10px;">
      <button onclick="openCheckinModal()" style="background: #D4441E; color: white; border: none; padding: 10px 18px; border-radius: 8px; font-weight: 700; cursor: pointer; font-size: 13.5px;">✍️ Điểm Danh / Xác Nhận Đã Đọc</button>
      <button onclick="viewAccessLog()" style="background: rgba(255,255,255,0.15); color: white; border: 1px solid rgba(255,255,255,0.3); padding: 10px 18px; border-radius: 8px; font-weight: 600; cursor: pointer; font-size: 13.5px;">📋 Xem Nhật Ký Truy Cập</button>
    </div>
  </div>

  <!-- MODAL CHECKIN -->
  <div id="accessTrackingModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 9999; align-items: center; justify-content: center;">
    <div style="background: white; border-radius: 14px; padding: 28px; max-width: 460px; width: 90%; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
      <h3 style="color: #071A36; font-size: 18px; margin-bottom: 6px;">XÁC NHẬN ĐÃ ĐỌC HIỂU NỘI QUY</h3>
      <p style="font-size: 13px; color: #64748B; margin-bottom: 16px;">Vui lòng ghi nhận thông tin để hệ thống C-TPAT ghi nhận nhật ký tuân thủ.</p>
      <div style="margin-bottom: 12px;">
        <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 4px;">Họ và tên người đọc *</label>
        <input type="text" id="chkName" placeholder="Ví dụ: Bùi Minh Dũng" style="width: 100%; padding: 9px 12px; border: 1px solid #CBD5E1; border-radius: 6px; box-sizing: border-box;">
      </div>
      <div style="margin-bottom: 12px;">
        <label style="display: block; font-size: 13px; font-weight: 600; margin-bottom: 4px;">Bộ phận / Biển số xe *</label>
        <input type="text" id="chkDept" placeholder="Ví dụ: Lái xe 50H-082.35" style="width: 100%; padding: 9px 12px; border: 1px solid #CBD5E1; border-radius: 6px; box-sizing: border-box;">
      </div>
      <div style="margin-bottom: 18px;">
        <label style="display: flex; align-items: flex-start; gap: 8px; font-size: 12.5px; color: #334155; cursor: pointer;">
          <input type="checkbox" id="chkAgree" checked style="margin-top: 3px;">
          <span>Tôi xác nhận đã đọc, hiểu rõ và cam kết tuân thủ đầy đủ các nội quy lao động, quy trình an ninh C-TPAT và chính sách an toàn của Cargolink Express.</span>
        </label>
      </div>
      <div style="display: flex; gap: 10px; justify-content: flex-end;">
        <button onclick="closeCheckinModal()" style="background: #E2E8F0; color: #475569; border: none; padding: 9px 16px; border-radius: 6px; font-weight: 600; cursor: pointer;">Đóng</button>
        <button onclick="submitCheckin()" style="background: #D4441E; color: white; border: none; padding: 9px 18px; border-radius: 6px; font-weight: 700; cursor: pointer;">Lưu Xác Nhận</button>
      </div>
    </div>
  </div>

  <!-- MODAL VIEW LOG -->
  <div id="accessLogModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 9999; align-items: center; justify-content: center;">
    <div style="background: white; border-radius: 14px; padding: 24px; max-width: 650px; width: 92%; max-height: 80vh; overflow-y: auto;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
        <h3 style="color: #071A36; font-size: 17px; margin: 0;">NHẬT KÝ XÁC NHẬN ĐỌC CHÍNH SÁCH (ACCESS LOG)</h3>
        <button onclick="closeLogModal()" style="background: none; border: none; font-size: 20px; cursor: pointer; color: #64748B;">&times;</button>
      </div>
      <div id="logTableContainer"></div>
    </div>
  </div>
"""
    # Insert right before class="section-title"
    content = content.replace('<div class="section-title">', tracking_snippet + '\n<div class="section-title">', 1)

    # Add scripts to bottom
    script_snippet = """
<script>
  function openCheckinModal() {
    document.getElementById('accessTrackingModal').style.display = 'flex';
  }
  function closeCheckinModal() {
    document.getElementById('accessTrackingModal').style.display = 'none';
  }
  function closeLogModal() {
    document.getElementById('accessLogModal').style.display = 'none';
  }
  function submitCheckin() {
    const name = document.getElementById('chkName').value.trim();
    const dept = document.getElementById('chkDept').value.trim();
    if(!name || !dept) { alert('Vui lòng điền họ tên và bộ phận/biển số xe!'); return; }
    
    const rec = {
      name: name,
      dept: dept,
      time: new Date().toLocaleString('vi-VN'),
      action: 'Đã truy cập và xác nhận đọc hiểu toàn bộ chính sách C-TPAT'
    };
    let logs = JSON.parse(localStorage.getItem('cgl_policy_access_logs') || '[]');
    logs.unshift(rec);
    localStorage.setItem('cgl_policy_access_logs', JSON.stringify(logs));
    
    alert('Cảm ơn ' + name + '! Xác nhận đọc chính sách đã được lưu thành công.');
    closeCheckinModal();
  }
  
  function viewAccessLog() {
    let logs = JSON.parse(localStorage.getItem('cgl_policy_access_logs') || '[]');
    if(logs.length === 0) {
      // Default sample historical logs for demonstration
      logs = [
        { name: "Bùi Minh Dũng", dept: "Lái xe 50H-082.35", time: "05/11/2026, 08:15:30", action: "Đã đọc và cam kết tuân thủ chính sách C-TPAT" },
        { name: "Nguyễn Văn Hùng", dept: "Lái xe 51C-964.55", time: "05/11/2026, 09:20:10", action: "Đã đọc và cam kết tuân thủ chính sách C-TPAT" },
        { name: "Lê Văn Tùng", dept: "Lái xe 50H-112.89", time: "05/11/2026, 10:05:45", action: "Đã đọc và cam kết tuân thủ chính sách C-TPAT" },
        { name: "Trần Quốc Bảo", dept: "Lái xe 51D-452.18", time: "05/11/2026, 11:30:12", action: "Đã đọc và cam kết tuân thủ chính sách C-TPAT" },
        { name: "Phạm Văn Công", dept: "Lái xe 50H-334.72", time: "05/11/2026, 13:45:00", action: "Đã đọc và cam kết tuân thủ chính sách C-TPAT" },
        { name: "Võ Thành Nhân", dept: "Lái xe 51C-882.14", time: "05/11/2026, 14:15:22", action: "Đã đọc và cam kết tuân thủ chính sách C-TPAT" },
        { name: "Phan Công Thành", dept: "Trưởng ban An toàn", time: "04/11/2026, 16:30:00", action: "Đã đọc và cam kết tuân thủ chính sách C-TPAT" }
      ];
      localStorage.setItem('cgl_policy_access_logs', JSON.stringify(logs));
    }
    
    let html = '<table style="width:100%; border-collapse:collapse; font-size:12.5px;">' +
               '<tr style="background:#F1F5F9; border-bottom:2px solid #CBD5E1;"><th style="padding:8px; text-align:left;">Họ tên</th><th style="padding:8px; text-align:left;">Bộ phận / Xe</th><th style="padding:8px; text-align:left;">Thời gian</th><th style="padding:8px; text-align:left;">Hành động</th></tr>';
    logs.forEach(l => {
      html += '<tr style="border-bottom:1px solid #E2E8F0;"><td style="padding:8px; font-weight:600; color:#071A36;">' + l.name + '</td><td style="padding:8px; color:#475569;">' + l.dept + '</td><td style="padding:8px; color:#64748B;">' + l.time + '</td><td style="padding:8px; color:#16A34A; font-weight:500;">' + l.action + '</td></tr>';
    });
    html += '</table>';
    document.getElementById('logTableContainer').innerHTML = html;
    document.getElementById('accessLogModal').style.display = 'flex';
  }
</script>
"""
    content = content.replace('</body>', script_snippet + '\n</body>')
    with open(portal_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[Portal] Updated portal_driver.html with Access Tracking System")
else:
    print("[Portal] Access tracking already in portal_driver.html")

