# -*- coding: utf-8 -*-
import sys, urllib.request

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    # 3 Main Forms & Hub
    "https://continent-msie-goals-watt.trycloudflare.com/index.html",
    "https://continent-msie-goals-watt.trycloudflare.com/portal_driver.html",
    "https://continent-msie-goals-watt.trycloudflare.com/form1_satisfaction.html",
    "https://continent-msie-goals-watt.trycloudflare.com/form2_knowledge.html",
    "https://continent-msie-goals-watt.trycloudflare.com/form3_complaints.html",
    # 10 Digital Operational Tools
    "https://continent-msie-goals-watt.trycloudflare.com/app_vehicle_inspection.html",
    "https://continent-msie-goals-watt.trycloudflare.com/app_seal_vvtt_log.html",
    "https://continent-msie-goals-watt.trycloudflare.com/app_alcohol_test_log.html",
    "https://continent-msie-goals-watt.trycloudflare.com/app_incident_rapid_report.html",
    "https://continent-msie-goals-watt.trycloudflare.com/app_trip_dispatch_log.html",
    "https://continent-msie-goals-watt.trycloudflare.com/app_ppe_pccc_log.html",
    "https://continent-msie-goals-watt.trycloudflare.com/app_visitor_gate_log.html",
    "https://continent-msie-goals-watt.trycloudflare.com/app_green_office_log.html",
    "https://continent-msie-goals-watt.trycloudflare.com/app_subcontractor_eval.html",
    "https://continent-msie-goals-watt.trycloudflare.com/app_ctpat_audit_checklist.html",
    # 10 Policy Documents
    "https://continent-msie-goals-watt.trycloudflare.com/doc_ctpat_inspection.html",
    "https://continent-msie-goals-watt.trycloudflare.com/doc_emergency_sop.html",
    "https://continent-msie-goals-watt.trycloudflare.com/doc_traffic_safety.html",
    "https://continent-msie-goals-watt.trycloudflare.com/doc_green_office.html",
    "https://continent-msie-goals-watt.trycloudflare.com/doc_whistleblower.html",
    "https://continent-msie-goals-watt.trycloudflare.com/doc_staff_handbook.html",
    "https://continent-msie-goals-watt.trycloudflare.com/doc_labor_salary_rules.html",
    "https://continent-msie-goals-watt.trycloudflare.com/doc_csr_human_rights.html",
    "https://continent-msie-goals-watt.trycloudflare.com/doc_cyber_route_security.html",
    "https://continent-msie-goals-watt.trycloudflare.com/doc_occupational_safety_pccc.html",
]

print("Verifying 25 Live URLs across the suite...")
success = 0
for u in urls:
    name = u.split("/")[-1]
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=8)
        if res.status == 200:
            print(f"  [200 OK] {name}")
            success += 1
        else:
            print(f"  [{res.status}] {name}")
    except Exception as e:
        print(f"  [FAIL] {name}: {e}")

print(f"\nResult: {success}/{len(urls)} URLs verified with HTTP 200 OK!")
