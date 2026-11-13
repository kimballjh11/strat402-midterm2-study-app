#!/usr/bin/env python3
"""Parse the Midterm 2 study guide matrix into reference/objectives.json (the master list of what can be tested).
Usage: python3 scripts/objectives.py [study_guide.xlsx] [out.json]"""
import sys, re, json, warnings
from pathlib import Path
import openpyxl
warnings.simplefilter("ignore")
HERE = Path(__file__).resolve().parent.parent
src = Path(sys.argv[1]) if len(sys.argv) > 1 else next((HERE / "sources" / "raw" / "S23").glob("*Study Guide*.xlsx"))
out = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "reference" / "objectives.json"

def qrefs(cell, default_quiz=None):
    """'Q1, Q3' / 'Quiz 7: Q1-Q3' / 'Session 22 quiz: Q4-Q5' -> [{'quiz': label, 'q': [ints]}]"""
    if not cell: return []
    res = []
    for chunk in re.split(r";", str(cell)):
        m = re.match(r"\s*((?:Session \d+ quiz|Quiz \d+)\s*:)?\s*(.*)", chunk.strip())
        label = m.group(1).rstrip(":").strip() if m and m.group(1) else default_quiz
        qs = []
        for a, b in re.findall(r"Q(\d+)(?:\s*[–\-]\s*Q?(\d+))?", m.group(2) if m else chunk):
            a = int(a); b = int(b) if b else a
            qs += list(range(a, b + 1))
        if qs: res.append({"quiz": label, "q": sorted(set(qs))})
    return res

wb = openpyxl.load_workbook(src, data_only=True); ws = wb.active
rows = list(ws.iter_rows(values_only=True))
hdr = next(i for i, r in enumerate(rows) if r and r[0] == "Session")
counts, objs = {}, []
for r in rows[hdr + 1:]:
    if not r or r[0] is None: continue
    s = int(r[0]); counts[s] = counts.get(s, 0) + 1
    text = str(r[2]).strip()
    short = re.sub(r"^Know and understand (the following economic concepts?: )?", "", text)
    short = re.sub(r"^Be able to ", "", short)
    kind = "concept" if text.startswith("Know and understand the following economic concept") else ("skill" if "calculate" in text or "determine" in text else "apply")
    objs.append({
        "id": f"S{s}-{counts[s]:02d}", "session": s, "topic": r[1], "text": text, "short": short, "kind": kind,
        "read": r[3] or "", "reading_quiz": qrefs(r[4], f"Session {s} quiz"), "in_class": [x.strip() for x in re.split(r"(?=Slides:|In-Class Exercise:)", r[5] or "") if x.strip()],
        "comprehension_quiz": qrefs(r[6]), "practice_exam": sorted({int(n) for a, b in re.findall(r"Q(\d+)(?:\s*[–\-]\s*Q?(\d+))?", str(r[7] or "")) for n in range(int(a), int(b or a) + 1)}),
        "spreadsheet": r[8] or ""})
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(objs, indent=1), encoding="utf8")
print(f"{len(objs)} objectives written to {out}", {f"S{k}": v for k, v in counts.items()})
