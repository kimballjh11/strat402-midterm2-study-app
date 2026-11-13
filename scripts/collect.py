#!/usr/bin/env python3
"""Copy the Midterm 2 source files into ./sources/raw so the rest of the build never reads outside this folder.
Usage: python3 scripts/collect.py [output_dir]"""
import shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent      # M2-STUDY-APP
ROOT = HERE.parent                                   # zStrat 402
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "sources" / "raw"
SESSIONS = [15, 16, 18, 19, 20, 21, 22]
SKIP_NAMES = {".DS_Store", "MEBS.jpg"}
IMG_EXT = {".png", ".jpg", ".jpeg", ".svg", ".gif"}

def copy(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

copied, notes = {}, []
for n in SESSIONS:
    dirs = sorted(ROOT.glob(f"Session {n:02d} - *"))
    if not dirs:
        notes.append(f"S{n}: folder not found"); continue
    d = dirs[0]
    cnt = 0
    for f in d.rglob("*"):
        if not f.is_file() or f.name in SKIP_NAMES:
            continue
        rel = f.relative_to(d)
        if f.suffix.lower() in IMG_EXT and f.stat().st_size < 20000:
            continue                                # tiny logos and thumbnails
        copy(f, OUT / f"S{n}" / rel)
        cnt += 1
    copied[f"S{n}"] = cnt

# Midterm 2 module files
m = next(iter(sorted(ROOT.glob("Session 23 - *"))), None)
if m:
    for f in m.iterdir():
        if f.is_file() and f.name != ".DS_Store":
            copy(f, OUT / "S23" / f.name)
    copied["S23"] = sum(1 for _ in (OUT / "S23").glob("*"))
idx = ROOT / "Midterm 2 - Readings, Videos & Links Index.html"
if idx.exists():
    copy(idx, OUT / "S23" / idx.name)

# Earlier material used only for inline refreshers (cost, demand, profit maximization, math review)
prereq = 0
wt = ROOT / "work" / "text"
if wt.exists():
    for pat in ["S05-*.txt", "STRAT-402-Math-Review.txt", "S06-*.txt", "S07-*.txt", "S08-*.txt", "S10-*.txt"]:
        for f in wt.glob(pat):
            copy(f, OUT / "prereq" / f.name); prereq += 1
copied["prereq"] = prereq
eq = next(iter(sorted(ROOT.glob("Midterm Exam 1 Equation Sheet (2).pdf"))), None)
if eq:
    copy(eq, OUT / "S23" / "Equation Sheet (Exam 1 version).pdf")

expect = {
    "S15": ["Slides", "Reading Quiz", "Textbook Study Notes", "J Dawgs"],
    "S16": ["Slides", "Reading Quiz", "Textbook Study Notes", "Cost Minimization", "Production Functions"],
    "S18": ["Slides", "Reading Quiz", "Textbook Study Notes", "Crack Well-Guarded"],
    "S19": ["Slides", "Reading Quiz", "Textbook Study Notes"],
    "S20": ["Slides", "Reading Quiz", "Textbook Study Notes", "Game Theory Exercise"],
    "S21": ["Slides", "Reading Quiz", "Textbook Study Notes", "Oligopoly Exercise"],
    "S22": ["Slides", "Reading Quiz", "Textbook Study Notes", "Rivalry"],
}
print("Copied files per bucket:", copied)
for s, kws in expect.items():
    names = " | ".join(p.name for p in (OUT / s).rglob("*") if p.is_file()) if (OUT / s).exists() else ""
    missing = [k for k in kws if k.lower() not in names.lower()]
    if missing:
        notes.append(f"{s}: not found yet -> {', '.join(missing)}")
print("\nNot present (expected for S21 and S22 until class materials arrive):")
for x in notes: print("  ", x)
