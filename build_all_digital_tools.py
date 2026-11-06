# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding='utf-8')
forms_dir = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\CTPAT_QR_FORMS"

# Common CSS Template
CSS_COMMON = """
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
      --warning: #D97706;
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

    .form-body { padding: 24px 20px; }
    .section-title { font-size: 14px; font-weight: 800; color: var(--primary); text-transform: uppercase; margin-bottom: 14px; padding-bottom: 6px; border-bottom: 2px solid #E2E8F0; display: flex; align-items: center; gap: 8px; }
    .section-title::before { content: ""; display: inline-block; width: 4px; height: 16px; background: var(--accent); border-radius: 2px; }

    .grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-bottom: 16px; }
    .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-bottom: 16px; }
    .field-group { margin-bottom: 14px; }
    label { display: block; font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
    input[type="text"], input[type="date"], input[type="time"], input[type="number"], select, textarea {
      width: 100%; padding: 9px 12px; font-size: 13.5px; border: 1.5px solid var(--border); border-radius: 8px; background: #FFF; outline: none;
    }
    input:focus, select:focus, textarea:focus { border-color: var(--primary-light); }
    textarea { min-height: 80px; resize: vertical; }

    .chk-table { width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 13px; }
    .chk-table th { background: #071A36; color: white; padding: 10px 12px; text-align: left; font-size: 12px; text-transform: uppercase; }
    .chk-table td { padding: 10px 12px; border-bottom: 1px solid #E2E8F0; vertical-align: middle; }
    .chk-table tr:nth-child(even) { background: #F8FAFC; }

    .status-opt { display: flex; gap: 12px; align-items: center; }
    .status-opt label { display: flex; align-items: center; gap: 4px; font-size: 12.5px; font-weight: 600; cursor: pointer; margin-bottom: 0; }
    .status-pass { color: var(--success); }
    .status-fail { color: var(--danger); }
    .status-warn { color: var(--warning); }

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
    .nav-back { display: inline-block; margin-bottom: 12px; color: #93C5FD; text-decoration: none; font-weight: 700; font-size: 13px; }
    .notice-box { background: #EFF6FF; border-left: 4px solid #2563EB; padding: 10px 14px; border-radius: 6px; font-size: 12.5px; color: #1E40AF; margin-bottom: 16px; }
"""

print("Common CSS defined successfully.")
