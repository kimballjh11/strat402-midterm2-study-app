"""S21 independent checks: every optimum found by golden-section search on the profit function itself
(no closed-form reaction functions). Cournot by iterating numeric best responses to a fixed point; Stackelberg by
nested search (leader searches over Q1, follower's numeric best response inside); collusion by maximizing joint profit."""
import sys
from lib import *

def price(a, b, Q): return a - b * Q
def best(a, b, c, other):
    hi = max(a / b, 1.0)
    return argmax_cont(lambda q: (price(a, b, q + other) - c) * q, 0, hi)
def cournot(a, b, c1, c2):
    q1 = q2 = 0.0
    for _ in range(200): q1 = best(a, b, c1, q2); q2 = best(a, b, c2, q1)
    P = price(a, b, q1 + q2); return {"q1": q1, "q2": q2, "P": P, "pi1": (P - c1) * q1, "pi2": (P - c2) * q2}
def stack(a, b, c1, c2):
    lead = lambda q1: (price(a, b, q1 + best(a, b, c2, q1)) - c1) * q1
    q1 = argmax_cont(lead, 0, a / b, 120); q2 = best(a, b, c2, q1); P = price(a, b, q1 + q2)
    return {"q1": q1, "q2": q2, "P": P, "pi1": (P - c1) * q1, "pi2": (P - c2) * q2}
def collude(a, b, c):
    Q = argmax_cont(lambda Q: (price(a, b, Q) - c) * Q, 0, a / b); P = price(a, b, Q)
    return {"q1": Q / 2, "P": P, "pi1": (P - c) * Q / 2}

def solve(v):
    f, a, b, c1, c2, w = v["f"], v["a"], v["b"], v["c1"], v["c2"], v["who"]
    if f == "cournot": return cournot(a, b, c1, c2)[w]
    if f == "stack": return stack(a, b, c1, c2)[w]
    if f == "collude": return collude(a, b, c1)[w]
    if f == "br": return best(a, b, c1, v["q2"])
    if f == "cheat":
        q = best(a, b, c1, v["quota"]); return (price(a, b, q + v["quota"]) - c1) * q

C = Checker()
for q in load_static("S21"):
    if "verify" not in q: C.fails.append(f"{q['id']}: num question without verify spec"); continue
    C.check(q["id"], q["answer"], solve(q["verify"]), q.get("tol", 0.01))
for gid, rows in load_samples("S21-").items():
    for r in rows:
        p, a = r["params"], r["answer"]; lab = f"{gid} seed {r['seed']}"
        if gid == "S21-02-g1": want = cournot(p["a"], p["b"], p["c1"], p["c2"])[p["ask"]]
        elif gid == "S21-04-g1": want = best(p["a"], p["b"], p["c1"], p["q2"])
        elif gid == "S21-03-g1": want = stack(p["a"], p["b"], p["c1"], p["c2"])[p["ask"]]
        elif gid == "S21-06-g1":
            cl = collude(p["a"], p["b"], p["c"]); q = best(p["a"], p["b"], p["c"], cl["q1"]); ch = (price(p["a"], p["b"], q + cl["q1"]) - p["c"]) * q
            want = {"collude": cl["pi1"], "cheat": ch, "gain": ch - cl["pi1"]}[p["ask"]]
        else: C.fails.append(f"{gid}: no checker written"); break
        C.check(lab, a, want, r.get("tol") or 0.01)
sys.exit(C.report("S21"))
