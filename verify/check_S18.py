"""S18 independent checks: costs by building total cost tables, learning curves by repeated doubling, networks by counting pairs."""
import sys, itertools
from lib import *

def total_cost(F, c, Q): return F + sum(c for _ in range(int(Q))) if Q == int(Q) and Q < 10**6 else F + c * Q
def learn_unit(C1, rate, n):
    cost, units = C1, 1
    while units < n: units *= 2; cost *= rate
    return cost if units == n else None
def pairs(n): return sum(1 for a, b in itertools.permutations(range(n), 2))

def solve(v):
    f = v["f"]
    if f == "ac": return total_cost(v["F"], v["c"], v["Q"]) / v["Q"]
    if f == "ac_gap": return total_cost(v["F"], v["c"], v["Q1"]) / v["Q1"] - total_cost(v["F"], v["c"], v["Q2"]) / v["Q2"]
    if f == "pct": return 100 * v["num"] / v["den"]
    if f == "learn": return learn_unit(v["C1"], v["rate"], v["n"])
    if f == "learn_from": return v["C"] * v["rate"] ** v["k"]
    if f == "pow": return v["base"] ** v["exp"]
    if f == "ratio": return v["num"] / v["den"]
    if f == "diff": return v["x2"] - v["x1"]
    if f == "add": return v["a"] + v["b"]
    if f == "scope": return (v["c1"] + v["c2"]) - v["c12"]
    if f == "scope_pct": return 100 * ((v["c1"] + v["c2"]) - v["c12"]) / (v["c1"] + v["c2"])
    if f == "conn": return pairs(v["n"])
    if f == "add_conn": return pairs(v["n"] + 1) - pairs(v["n"])
    if f == "profit_per": return v["rev"] / v["users"] - v["cost"] / v["users"]
    return None

C = Checker()
for q in load_static("S18"):
    if "verify" not in q: C.fails.append(f"{q['id']}: num question without verify spec"); continue
    C.check(q["id"], q["answer"], solve(q["verify"]), q.get("tol", 0.01))

for gid, rows in load_samples("S18-").items():
    for r in rows:
        p, a = r["params"], r["answer"]; lab = f"{gid} seed {r['seed']}"
        if gid == "S18-01-g1":
            acs = lambda Q: total_cost(p["F"], p["c"], Q) / Q
            want = {"small": acs(p["Qs"]), "big": acs(p["Qb"]), "gap": acs(p["Qs"]) - acs(p["Qb"])}[p["ask"]]
        elif gid == "S18-02-g1": want = learn_unit(p["C1"], p["rate"], 2 ** p["k"])        # cost ratio depends only on doublings
        elif gid == "S18-04-g1":
            if p["ask"] == "conn": want = pairs(p["n"])
            elif p["ask"] == "add": want = pairs(p["n"] + 1) - pairs(p["n"])
            elif p["ask"] == "rev": want = p["rev"] / p["users"]
            else: want = (p["rev"] - p["cost"]) / p["users"]
        elif gid == "S18-05-g1":
            P, own, ent = p["P"], p["own"], p["ent"]
            key = "Entry is not deterred" if P >= ent else ("Entry is deterred and the incumbent still earns" if P > own else "Entry is deterred, but the price is below")
            C.check(lab, 1, 1 if r["choices"][a].startswith(key) else 0); continue
        else: C.fails.append(f"{gid}: no checker written"); break
        C.check(lab, a, want, r.get("tol") or 0.01)
sys.exit(C.report("S18"))
