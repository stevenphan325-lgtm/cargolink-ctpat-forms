# -*- coding: utf-8 -*-
import os, sys, shutil
from docx import Document
import openpyxl

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\steve\OneDrive\audit truck\AUDIT TRUCK 2026"
ARTIFACT_DIR = r"C:\Users\steve\.gemini\antigravity\brain\3fd565a3-4c2a-4c18-a7a1-797e899ae163"

# Name mappings
# 1. Nguyễn Duy Thành -> Phan Công Thành
# 2. Trần Thị Mai Phương -> Lê Thị Tú (Kế toán trưởng) & Nguyễn Tất Thắng (Giám đốc)
# 3. Mai Phương -> Lê Thị Tú

def replace_in_docx(doc_path):
    doc = Document(doc_path)
    changed = False
    
    def repl(text):
        nonlocal changed
        orig = text
        text = text.replace("Nguyễn Duy Thành", "Phan Công Thành")
        text = text.replace("Trần Thị Mai Phương", "Lê Thị Tú (Kế toán trưởng) và Nguyễn Tất Thắng (Giám đốc)")
        text = text.replace("Mai Phương", "Lê Thị Tú")
        if text != orig:
            changed = True
        return text

    for p in doc.paragraphs:
        for r in p.runs:
            if "Nguyễn Duy Thành" in r.text or "Trần Thị Mai Phương" in r.text or "Mai Phương" in r.text:
                r.text = repl(r.text)
                
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        if "Nguyễn Duy Thành" in r.text or "Trần Thị Mai Phương" in r.text or "Mai Phương" in r.text:
                            r.text = repl(r.text)
                            
    if changed:
        doc.save(doc_path)
        # Also copy to artifact if in root
        if os.path.dirname(doc_path) == BASE_DIR:
            shutil.copy2(doc_path, os.path.join(ARTIFACT_DIR, os.path.basename(doc_path)))
        print(f"✅ Updated DOCX: {os.path.basename(doc_path)}")

def replace_in_xlsx(xlsx_path):
    wb = openpyxl.load_workbook(xlsx_path)
    changed = False
    
    for sheet in wb.sheetnames:
        ws = wb[sheet]
        for r in range(1, ws.max_row+1):
            for c in range(1, ws.max_column+1):
                val = ws.cell(r, c).value
                if isinstance(val, str):
                    orig = val
                    val = val.replace("Nguyễn Duy Thành", "Phan Công Thành")
                    val = val.replace("Trần Thị Mai Phương", "Lê Thị Tú (KTT) & Nguyễn Tất Thắng (GĐ)")
                    val = val.replace("Mai Phương", "Lê Thị Tú")
                    if val != orig:
                        ws.cell(r, c).value = val
                        changed = True
                        
    if changed:
        wb.save(xlsx_path)
        if os.path.dirname(xlsx_path) == BASE_DIR:
            shutil.copy2(xlsx_path, os.path.join(ARTIFACT_DIR, os.path.basename(xlsx_path)))
        print(f"✅ Updated XLSX: {os.path.basename(xlsx_path)}")

def replace_in_text_file(txt_path):
    try:
        with open(txt_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        orig = content
        content = content.replace("Nguyễn Duy Thành", "Phan Công Thành")
        content = content.replace("Trần Thị Mai Phương", "Lê Thị Tú (Kế toán trưởng) và Nguyễn Tất Thắng (Giám đốc)")
        content = content.replace("Mai Phương", "Lê Thị Tú")
        
        if content != orig:
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(content)
            if os.path.dirname(txt_path) == BASE_DIR:
                shutil.copy2(txt_path, os.path.join(ARTIFACT_DIR, os.path.basename(txt_path)))
            print(f"✅ Updated Text/MD/HTML: {os.path.basename(txt_path)}")
    except Exception as e:
        print(f"❌ Error in {txt_path}: {e}")

if __name__ == "__main__":
    print("--- UPDATING PERSONNEL NAMES ACROSS ALL FILES ---")
    
    for root, dirs, files in os.walk(BASE_DIR):
        if ".git" in root: continue
        for f in files:
            if f.startswith("~$"): continue
            p = os.path.join(root, f)
            ext = os.path.splitext(f)[1].lower()
            if ext == ".docx":
                replace_in_docx(p)
            elif ext == ".xlsx":
                replace_in_xlsx(p)
            elif ext in [".md", ".html", ".py", ".txt"]:
                replace_in_text_file(p)
                
    print("--- FINISHED IN-PLACE TEXT REPLACEMENTS ---")
