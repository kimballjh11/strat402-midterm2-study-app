"""S19 independent checks: Nash equilibria by testing every unilateral deviation, dominance by pairwise comparison,
mixed strategies by bisection on the opponent's payoff difference."""
import sys
from lib import *

def is_nash(pay, i, j):
    return all(pay[k][j][0] <= pay[i][j][0] for k in range(len(pay))) and all(pay[i][k][1] <= pay[i][j][1] for k in range(len(pay[0])))
def all_nash(pay): return [(i, j) for i in range(len(pay)) for j in range(len(pay[0])) if is_nash(pay, i, j)]
def dominant_row(pay):
    for i in range(len(pay)):
        if all(pay[i][j][0] > pay[k][j][0] for k in range(len(pay)) if k != i for j in range(len(pay[0]))): return i
def dominant_col(pay):
    for j in range(len(pay[0])):
        if all(pay[i][j][1] > pay[i][k][1] for k in range(len(pay[0])) if k != j for i in range(len(pay))): return j
def root(f):
    lo, hi = 0.0, 1.0
    flo = f(lo)
    for _ in range(200):
        m = (lo + hi) / 2
        if (f(m) > 0) == (flo > 0): lo = m
        else: hi = m
    return (lo + hi) / 2
def mix_p(pay):   # row's top probability making the column player indifferent
    return root(lambda p: (p * pay[0][0][1] + (1 - p) * pay[1][0][1]) - (p * pay[0][1][1] + (1 - p) * pay[1][1][1]))
def mix_q(pay):   # column's left probability making the row player indifferent
    return root(lambda q: (q * pay[0][0][0] + (1 - q) * pay[0][1][0]) - (q * pay[1][0][0] + (1 - q) * pay[1][1][0]))

def solve(v):
    f = v["f"]
    if f == "cell": return v["pay"][v["i"]][v["j"]][v["who"]]
    if f == "fine": return v["p"] * v["rate"] * v["rev"]   # expected fine = probability x fine rate x revenue
    if f == "mix_p": return mix_p(v["pay"])
    if f == "mix_q": return mix_q(v["pay"])
    if f == "mix_val_row":
        q = mix_q(v["pay"]); return q * v["pay"][1][0][0] + (1 - q) * v["pay"][1][1][0]   # use the OTHER row: equal at q
    if f == "pd_loss":
        pay = v["pay"]; (i, j), = all_nash(pay); best = max(a + b for row in pay for a, b in row)
        return best - sum(pay[i][j])
    if f == "diff": return v["x2"] - v["x1"]
    return None

C = Checker()
for q in load_static("S19"):
    if "verify" not in q: C.fails.append(f"{q['id']}: num question without verify spec"); continue
    C.check(q["id"], q["answer"], solve(q["verify"]), q.get("tol", 0.01))

for gid, rows in load_samples("S19-").items():
    for r in rows:
        p, a = r["params"], r["answer"]; lab = f"{gid} seed {r['seed']}"
        if gid == "S19-04-g1":
            ne = all_nash(p["pay"])
            if len(ne) != 1 or list(ne[0]) != p["ne"]: C.fails.append(f"{lab}: not a unique equilibrium at {p['ne']}: {ne}")
            C.n += 1; continue
        if gid == "S19-03-g1":
            dr, dc = dominant_row(p["pay"]), dominant_col(p["pay"])
            want = "Both" if dr is not None and dc is not None else "Neither" if dr is None and dc is None else ("Only" if True else "")
            txt = r["choices"][a]
            ok = (dr is not None and dc is not None and txt.startswith("Both")) or (dr is None and dc is None and txt.startswith("Neither")) or \
                 (dr is not None and dc is None and a == 0) or (dc is not None and dr is None and a == 1)
            C.check(lab, 1, 1 if ok else 0); continue
        if gid == "S19-05-g1":
            if all_nash(p["pay"]): C.fails.append(f"{lab}: has a pure equilibrium")
            want = {"p": mix_p(p["pay"]), "q": mix_q(p["pay"]), "val": solve({"f": "mix_val_row", "pay": p["pay"]})}[p["ask"]]
        elif gid == "S19-06-g1":
            pay = [[[p["both"]] * 2, [p["temp"], p["sucker"]]], [[p["sucker"], p["temp"]], [p["coop"]] * 2]]
            if all_nash(pay) != [(0, 0)]: C.fails.append(f"{lab}: equilibrium is not (first, first)")
            want = 2 * p["coop"] - 2 * p["both"] if p["ask"] == "loss" else pay[0][1][0] - pay[1][1][0]
        else: C.fails.append(f"{gid}: no checker written"); break
        C.check(lab, a, want, r.get("tol") or 0.01)
sys.exit(C.report("S19"))
