"""Authoring helpers: build lesson, question and case dicts in Python (raw strings keep TeX intact) and write JSON."""
import json, re, hashlib, random
from pathlib import Path
APP = Path(__file__).resolve().parent.parent
BAD = re.compile(r"—|--")          # no em dashes or double hyphens in authored text

def _lint(obj, where):
    if isinstance(obj, str):
        txt = re.sub(r"(?m)^\|[\s:|-]+\|?$", "", obj)          # markdown table separator rows are fine
        if BAD.search(txt): raise ValueError(f"em dash or double hyphen in {where}: {obj[:80]}")
    elif isinstance(obj, dict):
        for k, v in obj.items(): _lint(v, f"{where}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj): _lint(v, f"{where}[{i}]")

def write_lesson(L):
    _lint(L, L["id"])
    (APP / "content" / "lessons").mkdir(parents=True, exist_ok=True)
    (APP / "content" / "lessons" / f"{L['id']}.json").write_text(json.dumps(L, indent=1, ensure_ascii=False))

PIN = re.compile(r"^(all |none|both|neither|cannot tell|all three|all of)", re.I)
def shuffle_choices(stem, choices, answer):
    """Deterministic shuffle seeded by the stem so the key is not always A. Options like 'All three' or 'Cannot tell' stay last."""
    rnd = random.Random(int(hashlib.sha1(stem.encode()).hexdigest()[:8], 16))
    idx = list(range(len(choices)))
    free = [i for i in idx if not PIN.match(choices[i].strip())]
    pinned = [i for i in idx if i not in free]
    rnd.shuffle(free); order = free + pinned
    return [choices[i] for i in order], order.index(answer)

class Bank:
    """Collects questions per primary objective file. ids: <LO>-q001..."""
    def __init__(self): self.files = {}
    def _add(self, lo, rec):
        lst = self.files.setdefault(lo, [])
        rec = {"id": f"{lo}-q{len(lst) + 1:03d}", **rec}
        _lint(rec, rec["id"]); lst.append(rec); return rec
    def mc(self, lo, los, kind, stem, choices, answer, explain, trap=None, diff=2):
        assert 0 <= answer < len(choices)
        choices, answer = shuffle_choices(stem, choices, answer)
        r = {"los": los, "type": "mc", "kind": kind, "diff": diff, "stem": stem, "choices": choices, "answer": answer, "explain": explain, "source": "generated", "verbatim": False}
        if trap: r["trap"] = trap
        return self._add(lo, r)
    def tf(self, lo, los, kind, stem, answer_true, explain, trap=None, diff=1):
        r = {"los": los, "type": "tf", "kind": kind, "diff": diff, "stem": stem, "choices": ["True", "False"], "answer": 0 if answer_true else 1, "explain": explain, "source": "generated", "verbatim": False}
        if trap: r["trap"] = trap
        return self._add(lo, r)
    def num(self, lo, los, stem, answer, explain, verify, unit="", tol=0.01, kind="calc", trap=None, diff=2):
        r = {"los": los, "type": "num", "kind": kind, "diff": diff, "stem": stem, "answer": answer, "unit": unit, "tol": tol, "explain": explain, "verify": verify, "source": "generated", "verbatim": False}
        if trap: r["trap"] = trap
        return self._add(lo, r)
    def write(self):
        d = APP / "content" / "questions"; d.mkdir(parents=True, exist_ok=True)
        for lo, lst in self.files.items(): (d / f"{lo}.json").write_text(json.dumps(lst, indent=1, ensure_ascii=False))
        return {lo: len(v) for lo, v in self.files.items()}

def write_cases(session, cases):
    _lint(cases, session)
    for c in cases:
        for i, p in enumerate(c["parts"]):
            if p.get("type") == "mc": p["choices"], p["answer"] = shuffle_choices(p["stem"], p["choices"], p["answer"])
            p.setdefault("id", f"{c['id']}-p{i + 1}"); p.setdefault("source", "generated"); p.setdefault("verbatim", False); p.setdefault("diff", 2)
    d = APP / "content" / "cases"; d.mkdir(parents=True, exist_ok=True)
    (d / f"{session}.json").write_text(json.dumps(cases, indent=1, ensure_ascii=False))

def write_session(session, info):
    _lint(info, session)
    d = APP / "content" / "sessions"; d.mkdir(parents=True, exist_ok=True)
    (d / f"{session}.json").write_text(json.dumps(info, indent=1, ensure_ascii=False))

def table(header, rows):
    """Markdown pipe table."""
    out = ["| " + " | ".join(map(str, header)) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(map(str, r)) + " |" for r in rows]
    return "\n".join(out)

def fmt(x, d=2):
    if abs(x - round(x)) < 1e-9: return f"{int(round(x)):,}"
    return f"{x:,.{d}f}".rstrip("0").rstrip(".")
