"""Shared independent solvers for verify/check_*.py. Methods deliberately differ from the closed forms used in content:
numeric derivatives, brute-force profit search, direct table arithmetic."""
import json, glob, math
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def load_static(session):
    """Static num questions and case parts for a session, with their verify specs."""
    out = []
    for f in glob.glob(str(HERE / "content" / "questions" / f"{session}-*.json")):
        out += [q for q in json.loads(Path(f).read_text()) if q.get("type") == "num"]
    cf = HERE / "content" / "cases" / f"{session}.json"
    if cf.exists():
        for c in json.loads(cf.read_text()):
            out += [p for p in c["parts"] if p.get("type") == "num"]
    return out

def load_samples(prefix):
    res = {}
    for f in glob.glob(str(HERE / "verify" / "samples" / f"{prefix}*.json")):
        res[Path(f).stem] = json.loads(Path(f).read_text())
    return res

def close(a, b, tol=0.01):
    if b == 0: return abs(a) <= 0.005
    return abs(a - b) <= abs(b) * tol + 1e-9

def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

def argmax_cont(f, lo, hi, iters=200):
    """Golden-section search for the max of a unimodal f on [lo, hi]."""
    g = (math.sqrt(5) - 1) / 2
    a, b = lo, hi
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(iters):
        if f(c) > f(d): b = d
        else: a = c
        c, d = b - g * (b - a), a + g * (b - a)
    return (a + b) / 2

def largest_argmax(vals):
    m = max(vals); return max(i for i, v in enumerate(vals) if abs(v - m) < 1e-9)

def cd(A, a, b):
    return lambda K, L: A * K ** a * L ** b

class Checker:
    def __init__(self): self.n = 0; self.fails = []
    def check(self, label, got, want, tol=0.01):
        self.n += 1
        if want is None or not close(got, want, tol): self.fails.append(f"{label}: content says {got}, independent check says {want}")
    def report(self, name):
        print(f"{name}: {self.n} answers checked, {len(self.fails)} mismatches")
        for f in self.fails: print("  MISMATCH", f)
        return 1 if self.fails else 0
