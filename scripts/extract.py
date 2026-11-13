#!/usr/bin/env python3
"""Turn everything in sources/raw into plain text and structured quiz JSON.
Outputs: sources/text/*.txt, sources/quizzes/*.json, sources/index.md
Needs: pip3 install beautifulsoup4 openpyxl pypdf python-docx   (pdftotext is used when present)
Usage: python3 scripts/extract.py [raw_dir] [out_dir]"""
import sys, re, json, html, shutil, subprocess, zipfile, email
from email import policy
from pathlib import Path
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent.parent
RAW = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "sources" / "raw"
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "sources"
TXT, QZ = OUT / "text", OUT / "quizzes"
TXT.mkdir(parents=True, exist_ok=True); QZ.mkdir(parents=True, exist_ok=True)

def slug(p: Path) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", str(p.relative_to(RAW).with_suffix(""))).strip("_")

def pdf_pages(p: Path):
    if shutil.which("pdftotext"):
        out = subprocess.run(["pdftotext", "-layout", str(p), "-"], capture_output=True, text=True).stdout
        pages = out.split("\f")
        if pages and not pages[-1].strip(): pages = pages[:-1]
        return pages
    from pypdf import PdfReader
    return [pg.extract_text() or "" for pg in PdfReader(str(p)).pages]

def html_to_text(raw: str) -> str:
    s = BeautifulSoup(raw, "html.parser")
    for t in s(["script", "style"]): t.decompose()
    for br in s.find_all("br"): br.replace_with("\n")
    for t in s.find_all(["p", "li", "tr", "h1", "h2", "h3", "h4", "div"]): t.append("\n")
    txt = html.unescape(s.get_text(" "))
    txt = re.sub(r"[ \t]+", " ", txt); txt = re.sub(r"\n\s*\n+", "\n\n", txt)
    return txt.strip()

def docx_text(p: Path) -> str:
    try:
        import docx
        d = docx.Document(str(p)); parts = [x.text for x in d.paragraphs]
        for t in d.tables:
            for r in t.rows: parts.append(" | ".join(c.text for c in r.cells))
        return "\n".join(parts)
    except Exception:
        x = zipfile.ZipFile(p).read("word/document.xml").decode("utf8", "ignore")
        x = re.sub(r"</w:p>", "\n", x); return html.unescape(re.sub(r"<[^>]+>", "", x))

def xlsx_text(p: Path) -> str:
    import openpyxl, warnings
    warnings.simplefilter("ignore")
    wf = openpyxl.load_workbook(p, data_only=False); wv = openpyxl.load_workbook(p, data_only=True)
    out = []
    for ws in wf:
        v = wv[ws.title]
        out.append(f"## SHEET: {ws.title} ({ws.max_row} rows x {ws.max_column} cols)")
        for row in ws.iter_rows():
            for c in row:
                if c.value is None and not c.comment: continue
                val = v[c.coordinate].value
                if isinstance(c.value, str) and c.value.startswith("="):
                    line = f"{c.coordinate}: {val!r}  [formula {c.value}]"
                else:
                    line = f"{c.coordinate}: {c.value!r}"
                if c.comment: line += f"  [comment: {c.comment.text.strip()!r}]"
                out.append(line)
    return "\n".join(out)

def mhtml_html_parts(p: Path):
    msg = email.message_from_bytes(p.read_bytes(), policy=policy.default)
    for part in msg.walk():
        if part.get_content_type() == "text/html":
            try: yield part.get_payload(decode=True).decode("utf-8", "replace")
            except Exception: pass

def parse_new_quiz(raw: str):
    """Canvas New Quizzes results page (Comprehension Quizzes). Text-pattern parser, raw lines are kept for checking."""
    raw = re.sub(r"<sup>(.*?)</sup>", r"^\1", raw, flags=re.S)   # keep exponents inline: K<sup>0.5</sup> -> K^0.5
    raw = re.sub(r"<sub>(.*?)</sub>", r"_\1", raw, flags=re.S)   # MP<sub>L</sub> -> MP_L
    s = BeautifulSoup(raw, "html.parser")
    for t in s(["script", "style"]): t.decompose()
    tables = []                                          # keep tables as rows of cells; the text gets a marker line
    for tb in s.find_all("table"):
        rows = [[{"t": c.get_text(" ", strip=True), "r": int(c.get("rowspan", 1) or 1), "c": int(c.get("colspan", 1) or 1), "h": c.name == "th"}
                 for c in tr.find_all(["td", "th"])] for tr in tb.find_all("tr")]
        tb.replace_with(s.new_string(f"\n[[TABLE {len(tables)}]]\n")); tables.append(rows)
    lines = [l.strip() for l in s.get_text("\n", strip=True).split("\n") if l.strip()]
    segs, cur = [], None
    for l in lines:
        m = re.match(r"Results for question (\d+)\.", l)
        if m: cur = {"n": int(m.group(1)), "lines": []}; segs.append(cur)
        elif cur is not None: cur["lines"].append(l)
    res = []
    for sg in segs:
        L = sg["lines"]
        pts = next((l for l in L if re.search(r"\d+(\.\d+)? / \d+(\.\d+)? point", l)), "")
        ti = next((i for i, l in enumerate(L) if l in ("Multiple Choice", "True/False", "Multiple Answer", "Numeric", "Fill in the Blank", "Essay", "Matching", "Ordering", "Categorization", "Formula", "Hot Spot", "Stimulus")), None)
        qtype = L[ti] if ti is not None else ""
        body = L[ti + 1:] if ti is not None else L
        fb_i = next((i for i, l in enumerate(body) if l == "Feedback"), len(body))
        main, feedback = body[:fb_i], [l for l in body[fb_i + 1:] if l != "General Feedback"]
        ma = [i for i, l in enumerate(main) if l == "Correct answer:"]
        options, stem, correct = [], [], []
        if qtype in ("Multiple Choice", "True/False", "Multiple Answer") and (ma or any("Not Selected" in l for l in main)):
            first_marker = min([i for i, l in enumerate(main) if l.endswith("Not Selected") or l.endswith("Selected")] + ma + [len(main)])
            seq, i = [], 0
            # option boundary: the line before the first marker (or first line after the label) starts options
            if ma and ma[0] < min([i for i, l in enumerate(main) if l.endswith("Selected")] + [len(main)]):
                start = ma[0]
            else:
                start = max(0, min(i for i, l in enumerate(main) if l.endswith("Selected")) - 1)
            stem = main[:start]
            j = start
            while j < len(main):
                l = main[j]
                if l == "Correct answer:":
                    k, grp = j + 1, []
                    while k < len(main) and not main[k].endswith("Selected"): grp.append(main[k]); k += 1
                    if k < len(main) and grp:      # last item before the marker is an ordinary option
                        correct += grp[:-1]; options += grp
                    else:
                        correct += grp; options += grp
                    j = k
                elif l.endswith("Selected"):
                    j += 1
                else:
                    if j + 1 < len(main) and main[j + 1].endswith("Selected"): options.append(l)
                    j += 1
        else:
            stem = main
        used = sorted({int(m) for l in L for m in re.findall(r"\[\[TABLE (\d+)\]\]", l)})
        res.append({"n": sg["n"], "tables": {str(k): tables[k] for k in used}, "type": qtype, "points": pts, "text": " ".join(stem), "options": options,
                    "correct": correct if correct else ([x for x in main[ma[0] + 1:]] if ma and not options else []),
                    "feedback": feedback, "raw_lines": L})
    return res

def parse_quiz_html(raw: str):
    s = BeautifulSoup(raw, "html.parser"); res = []
    title = (s.find("title").get_text(strip=True) if s.find("title") else "")
    for qd in s.select("div.display_question"):
        name = qd.select_one(".question_name"); qt = qd.select_one("div.question_text.user_content") or qd.select_one(".question_text")
        types = [c for c in qd.get("class", []) if c.endswith("_question") and c != "display_question"]
        answers = []
        for a in qd.select("div.answer"):
            t = ""
            for sel in (".answer_html", ".answer_text"):
                e = a.select_one(sel)
                if e and e.get_text(strip=True): t = e.get_text(" ", strip=True); break
            cls = a.get("class", [])
            if not t and not any(x in cls for x in ("correct_answer", "selected_answer")): continue
            cm = a.select_one(".answer_comment_html") or a.select_one(".answer_comment")
            answers.append({"text": t, "correct": "correct_answer" in cls, "selected": "selected_answer" in cls,
                            "comment": cm.get_text(" ", strip=True) if cm else ""})
        feedback = [c.get_text(" ", strip=True) for c in qd.select(".quiz_comment") if c.get_text(strip=True)]
        res.append({"n": int(re.sub(r"\D", "", name.get_text()) or 0) if name else len(res) + 1,
                    "qid": qd.get("id", ""), "type": types[0] if types else "",
                    "user_correct": "correct" in qd.get("class", []) and "incorrect" not in qd.get("class", []),
                    "text": qt.get_text(" ", strip=True) if qt else "", "answers": answers, "feedback": feedback})
    return title, res

def write(name: str, text: str):
    (TXT / f"{name}.txt").write_text(text, encoding="utf8")

index, lowtext = [], {}
for p in sorted(RAW.rglob("*")):
    if not p.is_file(): continue
    ext, name = p.suffix.lower(), slug(p)
    try:
        if ext == ".pdf":
            pages = pdf_pages(p)
            write(name, "\n".join(f"\n=== PAGE {i} ===\n{t.strip()}" for i, t in enumerate(pages, 1)))
            low = [i for i, t in enumerate(pages, 1) if len(t.strip()) < 120]
            if low: lowtext[str(p.relative_to(RAW))] = low
            index.append((p, f"pdf {len(pages)} pages, {len(low)} low-text pages (figures)"))
        elif ext in (".html", ".htm"):
            raw = p.read_text(errors="ignore")
            if "Results for question" in raw:                      # New Quizzes results page saved as .html
                qs = parse_new_quiz(raw)
                (QZ / f"{name}.json").write_text(json.dumps({"source": str(p.relative_to(RAW)), "title": "New Quizzes results", "questions": qs}, indent=1), encoding="utf8")
                index.append((p, f"quiz json (new quizzes html), {len(qs)} questions"))
            elif "display_question" in raw:
                title, qs = parse_quiz_html(raw)
                (QZ / f"{name}.json").write_text(json.dumps({"source": str(p.relative_to(RAW)), "title": title, "questions": qs}, indent=1), encoding="utf8")
                index.append((p, f"quiz json, {len(qs)} questions"))
            else:
                t = html_to_text(raw); write(name, t); index.append((p, f"html text, {len(t)} chars"))
        elif ext == ".mhtml":
            seen, allq, title = set(), [], ""
            for h in mhtml_html_parts(p):
                if "Results for question" in h:
                    nq = parse_new_quiz(h)
                    for q in nq:
                        if q["n"] not in seen: seen.add(q["n"]); allq.append(q)
                    title = title or "New Quizzes results"
                elif "display_question" in h:
                    t2, qs = parse_quiz_html(h); title = title or t2
                    for q in qs:
                        if q["qid"] not in seen: seen.add(q["qid"]); allq.append(q)
            (QZ / f"{name}.json").write_text(json.dumps({"source": str(p.relative_to(RAW)), "title": title, "questions": allq}, indent=1), encoding="utf8")
            index.append((p, f"quiz json (mhtml), {len(allq)} questions"))
        elif ext == ".docx":
            t = docx_text(p); write(name, t); index.append((p, f"docx text, {len(t)} chars"))
        elif ext in (".xlsx", ".xlsm"):
            t = xlsx_text(p); write(name, t); index.append((p, f"xlsx dump, {len(t)} chars"))
        elif ext in (".txt", ".md", ".csv"):
            t = p.read_text(errors="ignore"); write(name, t); index.append((p, f"text, {len(t)} chars"))
        elif ext in (".png", ".jpg", ".jpeg", ".svg", ".gif"):
            index.append((p, "image: view it directly with the Read tool when a lesson needs it"))
        else:
            index.append((p, "skipped (unsupported type)"))
    except Exception as e:
        index.append((p, f"ERROR {e!r}"))

lines = ["# Source index (generated by scripts/extract.py)", ""]
for p, note in index: lines.append(f"- {p.relative_to(RAW)}: {note}")
lines += ["", "## PDF pages with little text (probably figures, view the page image if the lesson needs it)"]
for k, v in lowtext.items(): lines.append(f"- {k}: pages {v}")
(OUT / "index.md").write_text("\n".join(lines), encoding="utf8")
print("\n".join(lines[:80])); print(f"... {len(index)} files processed. See {OUT/'index.md'}")
