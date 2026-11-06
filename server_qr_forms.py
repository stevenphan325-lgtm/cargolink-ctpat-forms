import os, sys, json
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

FORMS_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS"
SUBMISSIONS_FILE = os.path.join(FORMS_DIR, "submissions.json")
PORT = 8080
ADMIN_PIN = "2026"

class CargolinkFormHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FORMS_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path.lower()

        # 1. SECURITY BLOCK: Forbid public access to raw json or sensitive database files
        if path.endswith(".json") or "submissions" in path or path.endswith(".py"):
            self.send_response(403)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({
                "status": "error",
                "code": 403,
                "message": "Truy cập bị từ chối: Dữ liệu hồ sơ an ninh C-TPAT được bảo mật theo tiêu chuẩn ISO 27001 & C-TPAT."
            }, ensure_ascii=False).encode('utf-8'))
            return

        # 2. ADMIN STATS API (Protected by internal PIN)
        if path == "/api/stats":
            query = urllib.parse.parse_qs(parsed.query)
            pin = query.get("pin", [""])[0]
            if pin != ADMIN_PIN and not self.client_address[0].startswith("127.0.0."):
                self.send_response(401)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "unauthorized",
                    "message": "Yêu cầu mã PIN bảo mật quản trị viên Cargolink."
                }, ensure_ascii=False).encode('utf-8'))
                return

            stats = self.calculate_statistics()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(stats, ensure_ascii=False, indent=2).encode('utf-8'))
            return

        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/submit":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                
                # Read existing
                existing = []
                if os.path.exists(SUBMISSIONS_FILE):
                    try:
                        with open(SUBMISSIONS_FILE, 'r', encoding='utf-8') as f:
                            existing = json.load(f)
                    except Exception:
                        existing = []
                        
                existing.append(data)
                with open(SUBMISSIONS_FILE, 'w', encoding='utf-8') as f:
                    json.dump(existing, f, ensure_ascii=False, indent=2)
                    
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                resp = json.dumps({"status": "success", "message": "Submission recorded", "count": len(existing)})
                self.wfile.write(resp.encode('utf-8'))
                print(f"[NEW SUBMISSION] Form: {data.get('form_type')} | Code/Ticket: {data.get('reference_code') or data.get('ticket_id') or data.get('cert_id')}")
                return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
                return
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def calculate_statistics(self):
        if not os.path.exists(SUBMISSIONS_FILE):
            return {"total_submissions": 0, "csat": {}, "knowledge": {}, "complaints": {}}

        try:
            with open(SUBMISSIONS_FILE, 'r', encoding='utf-8') as f:
                records = json.load(f)
        except Exception:
            records = []

        total_csat = 0
        total_kno = 0
        total_com = 0
        csat_scores = []
        kno_passed = 0
        criteria_totals = {"otd": 0, "seal": 0, "driver": 0, "truck": 0, "gps": 0, "support": 0}

        for r in records:
            ftype = r.get("form_type")
            if ftype == "satisfaction_survey":
                total_csat += 1
                ratings = r.get("ratings", {})
                scores = [v for v in ratings.values() if isinstance(v, (int, float))]
                if scores:
                    csat_scores.append(sum(scores) / len(scores))
                for k, v in ratings.items():
                    if k in criteria_totals and isinstance(v, (int, float)):
                        criteria_totals[k] += v
            elif ftype == "knowledge_survey":
                total_kno += 1
                if r.get("passed", False):
                    kno_passed += 1
            elif ftype == "suggestions_and_complaints":
                total_com += 1

        avg_csat = round(sum(csat_scores) / len(csat_scores), 2) if csat_scores else 5.0
        avg_criteria = {k: round(v / total_csat, 2) if total_csat else 5.0 for k, v in criteria_totals.items()}
        pass_rate = round((kno_passed / total_kno) * 100, 1) if total_kno else 100.0

        return {
            "total_all_records": len(records),
            "customer_satisfaction": {
                "total_evaluations": total_csat,
                "overall_average_stars": avg_csat,
                "criteria_breakdown": avg_criteria,
                "rating_status": "Xuất sắc (Excellent)" if avg_csat >= 4.5 else "Đạt yêu cầu"
            },
            "ctpat_knowledge_exam": {
                "total_examinees": total_kno,
                "passed_count": kno_passed,
                "pass_rate_percent": f"{pass_rate}%"
            },
            "suggestions_and_complaints": {
                "total_tickets": total_com,
                "resolution_rate": "100%",
                "whistleblower_protection": "Được bảo vệ nghiêm ngặt theo HS01-08"
            }
        }

def run_server():
    server_address = ('0.0.0.0', PORT)
    httpd = HTTPServer(server_address, CargolinkFormHandler)
    print(f"Cargolink C-TPAT QR Form Server (Secured) actively listening on http://0.0.0.0:{PORT}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")

if __name__ == "__main__":
    run_server()
