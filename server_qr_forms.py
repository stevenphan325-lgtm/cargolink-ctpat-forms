import os, sys, json
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

FORMS_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS"
SUBMISSIONS_FILE = os.path.join(FORMS_DIR, "submissions.json")
PORT = 8080

class CargolinkFormHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FORMS_DIR, **kwargs)

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

def run_server():
    server_address = ('0.0.0.0', PORT)
    httpd = HTTPServer(server_address, CargolinkFormHandler)
    print(f"Cargolink C-TPAT QR Form Server is actively listening on http://0.0.0.0:{PORT}...")
    print(f"Serving directory: {FORMS_DIR}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")

if __name__ == "__main__":
    run_server()
