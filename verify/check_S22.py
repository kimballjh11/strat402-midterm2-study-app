"""S22 independent checks. Standard Bertrand: search a 1-cent price grid for prices where no seller gains by deviating.
Differentiated Bertrand: iterate numeric best responses (golden-section search on each firm's profit in its own price).
Model comparison: numeric Cournot fixed point, nested Stackelberg search, joint-profit search (no closed forms)."""
import sys
from lib import *

def bert(A, k, c1, c2):
    Q = lambda p: max(A - k * p, 0)
    if c1 == c2:
        # symmetric grid equilibria: no gain from a one-cent undercut and no gain from raising price (sell zero)
        eq = [p / 100 for p in range(int(c1 * 100), int(A / k * 100)) if (p / 100 - c1) * Q(p / 100) / 2 >= (p / 100 - 0.01 - c1) * Q(p / 100 - 0.01) - 1e-9]
        p = min(eq); return {"P": p, "Q": Q(p), "half": Q(p) / 2, "pi1": 0.0}
    p = argmax_cont(lambda p: (p - c1) * Q(p), c1, c2)   # low-cost firm cannot price above the rival's cost without losing all sales
    return {"P": p, "Q": Q(p), "pi1": (p - c1) * Q(p)}
def dbert(al, be, ga, c):
    dem = lambda pi, pj: al - be * pi + ga * pj
    best = lambda pj: argmax_cont(lambda p: (p - c) * dem(p, pj), c, c + 10 * (al + ga * pj) / be + 10)
    p1 = p2 = c
    for _ in range(200): p1 = best(p2); p2 = best(p1)
    return p1, best, dem
def price(a, b, Q): return a - b * Q
def qbest(a, b, c, other): return argmax_cont(lambda q: (price(a, b, q + other) - c) * q, 0, a / b)
def model_price(a, b, c, model):
    if model == "Bertrand": return bert(a / b, 1 / b, c, c)["P"]
    if model == "Collusion": return price(a, b, argmax_cont(lambda Q: (price(a, b, Q) - c) * Q, 0, a / b))
    if model == "Cournot":
        q1 = q2 = 0.0
        for _ in range(200): q1 = qbest(a, b, c, q2); q2 = qbest(a, b, c, q1)
        return price(a, b, q1 + q2)
    q1 = argmax_cont(lambda q: (price(a, b, q + qbest(a, b, c, q)) - c) * q, 0, a / b, 120)
    return price(a, b, q1 + qbest(a, b, c, q1))

def solve(v):
    f = v["f"]
    if f == "bert": return bert(v["A"], v["k"], v["c1"], v["c2"])[v["who"]]
    if f == "bert_half": return bert(v["A"], v["k"], v["c1"], v["c2"])["half"]
    if f == "mult": return v["x"] * v["y"]
    if f == "dbert":
        p, best, dem = dbert(v["al"], v["be"], v["ga"], v["c"])
        return {"p": p, "pi": (p - v["c"]) * dem(p, p), "br": best(v.get("pj", 0))}[v["who"]]
    if f == "cournot_minus_mc": return model_price(v["a"], v["b"], v["c"], "Cournot") - v["c"]
    if f == "model_price": return model_price(v["a"], v["b"], v["c"], v["model"])

C = Checker()
for q in load_static("S22"):
    if "verify" not in q: C.fails.append(f"{q['id']}: num question without verify spec"); continue
    C.check(q["id"], q["answer"], solve(q["verify"]), q.get("tol", 0.01))
for gid, rows in load_samples("S22-").items():
    for r in rows:
        p, a = r["params"], r["answer"]; lab = f"{gid} seed {r['seed']}"
        if gid == "S22-01-g1":
            res = bert(p["A"], p["k"], p["c1"], p["c2"])
            want = res["P"] if p["ask"] == "P" else res["pi1"] if p["ask"] == "pi1" else (res["Q"] if p["c1"] != p["c2"] else res["half"])
        elif gid == "S22-02-g1":
            pe, best, dem = dbert(p["a"], 1, 1, p["c"]); want = {"p": pe, "q": dem(pe, pe), "pi": (pe - p["c"]) * dem(pe, pe)}[p["ask"]]
        elif gid == "S22-04-g1":
            pe, best, dem = dbert(p["al"], p["be"], p["ga"], p["c"]); want = best(p["pj"]) if p["ask"] == "br" else pe
        elif gid == "S22-04-g2":
            want = model_price(p["a"], p["b"], p["c"], "Stackelberg" if p["model"].startswith("Stackelberg") else p["model"])
        else: C.fails.append(f"{gid}: no checker written"); break
        C.check(lab, a, want, r.get("tol") or 0.01)
sys.exit(C.report("S22"))
