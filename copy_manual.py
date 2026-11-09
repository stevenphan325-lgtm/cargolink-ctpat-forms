# -*- coding: utf-8 -*-
import os, shutil

src = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163\AUDIT_TRUCK_2026_THUC_TE_CHUNG_MINH_BANG_CHUNG_VA_CHUAN_BI.md"
dst = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026\00_HUONG_DAN_CHUAN_BI_THUC_TE_VA_BANG_CHUNG_AUDIT.md"

shutil.copyfile(src, dst)
print("Copied master field manual to project root successfully!")
