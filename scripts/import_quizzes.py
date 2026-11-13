#!/usr/bin/env python3
"""Import professor quiz questions VERBATIM (never retyped) into content/questions/pro/.
Maps each question to learning objectives using the study guide columns (reference/objectives.json).
Handles Reading Quizzes (HTML export) and Comprehension Quizzes (Canvas New Quizzes mhtml export).
Safe to re-run after new quiz files are ingested. Usage: python3 scripts/import_quizzes.py"""
import json, re, glob
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
objs = json.loads((HERE / "reference" / "objectives.json").read_text())
QZ = HERE / "sources" / "quizzes"
OUT = HERE / "content" / "questions" / "pro"; OUT.mkdir(parents=True, exist_ok=True)

def find_quiz(label):
    """'Session 15 quiz' -> reading quiz file; 'Quiz 7' -> comprehension quiz file. Latest attempt wins."""
    m = re.match(r"Session (\d+) quiz", label or "")
    if m: pat = f"*Session_{m.group(1)}_Reading_Quiz*"
    else:
        m = re.match(r"Quiz (\d+)", label or "")
        if not m: return None
        pat = f"*Comprehension_Quiz_{m.group(1)}[_.]*"
    files = sorted(glob.glob(str(QZ / f"{pat}.json")))
    return files[-1] if files else None

# (quiz label, question number) -> [LO ids]
want = {}
for o in objs:
    for kind in ("reading_quiz", "comprehension_quiz"):
        for ref in o[kind]:
            for q in ref["q"]:
                want.setdefault((ref["quiz"], q), []).append(o["id"])

# kind is metadata, not question text: classify calculation and application questions so the mix rules count them right
KIND = {"Quiz 7 Q1": "calc", "Quiz 7 Q2": "apply", "Quiz 7 Q3": "calc", "Quiz 7 Q4": "calc", "Quiz 7 Q5": "calc", "Quiz 7 Q6": "calc",
        "Quiz 7 Q7": "calc", "Quiz 7 Q8": "apply", "Quiz 7 Q9": "concept", "Quiz 7 Q10": "concept",
        "Quiz 8 Q3": "apply", "Quiz 8 Q4": "apply", "Quiz 8 Q5": "apply",
        "Quiz 9 Q1": "apply", "Quiz 9 Q2": "apply", "Quiz 9 Q3": "apply", "Quiz 9 Q4": "apply", "Quiz 9 Q5": "apply", "Quiz 9 Q6": "apply",
        "Quiz 9 Q7": "apply", "Quiz 9 Q8": "apply", "Quiz 9 Q9": "apply", "Quiz 9 Q10": "apply"}

by_file, missing = {}, []
for (label, n), los in sorted(want.items()):
    f = find_quiz(label)
    if not f: missing.append(f"{label} Q{n}"); continue
    d = json.loads(Path(f).read_text())
    q = next((x for x in d["questions"] if x["n"] == n), None)
    if not q: missing.append(f"{label} Q{n} (not in file)"); continue
    if "answers" in q:                                   # reading quiz format
        ch = [a["text"] for a in q["answers"]]
        corr = [i for i, a in enumerate(q["answers"]) if a["correct"]]
        typ = "tf" if q["type"].startswith("true_false") else ("multi" if len(corr) > 1 else "mc")
        expl = " ".join(q["feedback"])
    else:                                                # comprehension quiz format
        ch = q["options"]; corr = [i for i, c in enumerate(ch) if c in q["correct"]]
        typ = "tf" if q["type"] == "True/False" else ("multi" if len(corr) > 1 else "mc")
        expl = " ".join(q["feedback"])
    rec = {"id": f"PRO-{re.sub(r'[^A-Za-z0-9]+','',label)}-Q{n}", "los": sorted(set(los)), "type": typ, "kind": KIND.get(f"{label} Q{n}", "concept"),
           "diff": 2, "stem": q["text"], "choices": ch, "answer": corr[0] if len(corr) == 1 else corr,
           "explain": expl, "source": "professor", "verbatim": True, "origin": f"{label} Q{n}"}
    if q.get("tables"):                                  # stem holds [[TABLE k]] markers, the app renders rec["tables"][k]
        rec["tables"] = q["tables"]
    if not ch or not corr or q.get("type") in ("Numeric", "Fill in the Blank", "Formula", "Essay"):
        rec["needs_review"] = True                       # numeric or odd formats: Claude must review against raw_lines
    session = re.search(r"(\d+)", label).group(1)
    by_file.setdefault(f"{label.split()[0]}{session}".replace("Session", "S"), []).append(rec)

for name, recs in by_file.items():
    (OUT / f"{name}.json").write_text(json.dumps(recs, indent=1))
print({k: len(v) for k, v in by_file.items()}, "| not available yet:", missing)
