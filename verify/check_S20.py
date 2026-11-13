"""S20 independent checks: present values by summing the discounted series term by term, threshold rates by bisection on
the PV difference, subgame perfect outcomes by brute force over every pure strategy profile (keeping only profiles where
no player gains by changing its action at any node, reached or not)."""
import sys, itertools
from lib import *

def pv_series(first, later, i, T=None):
    tot, disc = first, 1.0
    while True:
        disc /= (1 + i); term = later * disc; tot += term
        if abs(term) < 1e-12 or disc < 1e-15: return tot
def istar(c, d, n):
    f = lambda i: pv_series(c, c, i) - pv_series(d, n, i)   # positive while collusion holds
    lo, hi = 0.01, 50.0
    for _ in range(80):
        m = (lo + hi) / 2
        if f(m) > 0: lo = m
        else: hi = m
    return (lo + hi) / 2

def nodes(t, out=None):
    out = [] if out is None else out
    if "pay" in t: return out
    out.append(t)
    for c in t["children"]: nodes(c["n"] if "n" in c else c, out)
    return out
def play(t, prof, ids):
    while "pay" not in t:
        c = t["children"][prof[ids[id(t)]]]; t = c["n"] if "n" in c else c
    return t["pay"]
def spe_brute(t):
    ns = nodes(t); ids = {id(n): k for k, n in enumerate(ns)}; res = []
    for prof in itertools.product(*[range(len(n["children"])) for n in ns]):
        ok = True
        for k, n in enumerate(ns):          # subgame rooted at each node: the mover cannot gain by deviating there
            base = play(n, prof, ids)[n["p"]]
            for a in range(len(n["children"])):
                alt = list(prof); alt[k] = a
                if play(n, alt, ids)[n["p"]] > base: ok = False
        if ok: res.append(play(t, prof, ids))
    return res

def solve(v):
    f = v["f"]
    if f == "pvc": return pv_series(v["c"], v["c"], v["i"])
    if f == "pvd": return pv_series(v["d"], v["n"], v["i"])
    if f == "perp": return pv_series(0, v["c"], v["i"])
    if f == "istar": return istar(v["c"], v["d"], v["n"])
    if f == "spe":
        r = spe_brute(v["g"]["tree"]); assert len({tuple(x) for x in r}) == 1, r
        return r[0][v["who"]]
    if f == "nn1": return v["n"] * (v["n"] - 1)
    if f == "diff": return v["x2"] - v["x1"]

C = Checker()
for q in load_static("S20"):
    if "verify" not in q: C.fails.append(f"{q['id']}: num question without verify spec"); continue
    C.check(q["id"], q["answer"], solve(q["verify"]), q.get("tol", 0.01))

for gid, rows in load_samples("S20-").items():
    for r in rows:
        p, a = r["params"], r["answer"]; lab = f"{gid} seed {r['seed']}"
        if gid == "S20-01-g1":
            pc, pd = pv_series(p["c"], p["c"], p["i"]), pv_series(p["d"], p["n"], p["i"])
            if p["ask"] == "decide":
                txt = r["choices"][a]; C.check(lab, 1, 1 if txt.startswith("Collude" if pc > pd else "Cheat") and ("%.2f" % max(pc, pd)).rstrip("0").rstrip(".") in txt.replace(",", "") else 0); continue
            want = pc if p["ask"] == "collude" else pd
        elif gid == "S20-03-g1": want = istar(p["c"], p["d"], p["n"])
        elif gid == "S20-06-g1":
            res = spe_brute(p["tree"])
            if len({tuple(x) for x in res}) != 1: C.fails.append(f"{lab}: SPE outcome not unique"); continue
            want = res[0][p["who"]]
        elif gid == "S20-08-g1":
            g = {"p": 0, "children": [{"a": "Enter", "n": {"p": 1, "children": [{"a": "Fight", "pay": [p["fE"], p["fI"]]}, {"a": "Acc", "pay": [p["aE"], p["aI"]]}]}}, {"a": "Out", "pay": [0, p["mono"]]}]}
            out = spe_brute(g)[0]; stay = out == [0, p["mono"]]
            txt = r["choices"][a]; C.check(lab, 1, 1 if txt.startswith("The entrant stays out: fighting" if stay else "The entrant enters and the incumbent accommodates") else 0); continue
        else: C.fails.append(f"{gid}: no checker written"); break
        C.check(lab, a, want, r.get("tol") or 0.01)
sys.exit(C.report("S20"))
