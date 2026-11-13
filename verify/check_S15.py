"""Independent check of every S15 numeric answer (static questions, case parts, 200 samples per generator)."""
import sys
from lib import *

def table_solver(v):
    L, Q = v["L"], v["Q"]
    mp = [None] + [Q[i] - Q[i - 1] for i in range(1, len(Q))]
    f = v["f"]
    if f == "table_q": return Q[v["at"]]
    if f == "table_mp": return mp[v["at"]]
    if f == "table_ap": return Q[v["at"]] / L[v["at"]]
    if f == "table_vmp": return v["P"] * mp[v["at"]]
    if f == "tp_max": return L[largest_argmax(Q)]
    if f == "ap_max":
        ap = [-1] + [Q[i] / L[i] for i in range(1, len(L))]; return L[largest_argmax(ap)]
    if f == "table_hire":            # brute force: profit at every staffing level, largest maximizer
        return L[largest_argmax([v["P"] * Q[i] - v["w"] * L[i] for i in range(len(L))])]
    if f == "first_diminishing": return next(i for i in range(2, len(mp)) if mp[i] < mp[i - 1])
    if f == "first_negative": return next(i for i in range(1, len(mp)) if mp[i] < 0)
    if f == "count_diminishing": return sum(1 for i in range(2, len(mp)) if mp[i] < mp[i - 1] and mp[i] >= 0)
    if f == "last_increasing": return max(i for i in range(1, len(mp)) if i == 1 or mp[i] > mp[i - 1])
    return None

def spec_solver(v):
    f = v["f"]
    if f.startswith("table_") or f in ("tp_max", "ap_max", "first_diminishing", "first_negative", "count_diminishing", "last_increasing"): return table_solver(v)
    if f == "poly_q": return sum(c * v["at"] ** i for i, c in enumerate(v["coef"]))
    if f in ("cd_q", "cd_mp", "cd_ap", "cd_vmp", "cd_hire"):
        q = cd(v["A"], v["a"], v["b"])
        if f == "cd_q": return q(v["K"], v["L"])
        if f == "cd_ap": return q(v["K"], v["L"]) / v["L"]
        if f == "cd_mp": return deriv(lambda x: q(v["K"], x), v["L"]) if v["wrt"] == "L" else deriv(lambda x: q(x, v["L"]), v["K"])
        if f == "cd_vmp": return v["P"] * deriv(lambda x: q(v["K"], x), v["L"])
        if f == "cd_hire": return argmax_cont(lambda L: v["P"] * q(v["K"], L) - v["w"] * L, 1e-9, 1e7)
    if f == "linear_q": return v["a"] * v["K"] + v["b"] * v["L"]
    if f == "linear_mp":
        g = lambda K, L: v["a"] * K + v["b"] * L
        return g(v["K"], v["L"] + 1) - g(v["K"], v["L"]) if v["wrt"] == "L" else g(v["K"] + 1, v["L"]) - g(v["K"], v["L"])
    if f == "leontief_q": return min(v["a"] * v["K"], v["b"] * v["L"])
    if f == "leontief_mp":
        g = lambda K, L: min(v["a"] * K, v["b"] * L)
        return g(v["K"], v["L"] + 1) - g(v["K"], v["L"]) if v["wrt"] == "L" else g(v["K"] + 1, v["L"]) - g(v["K"], v["L"])
    if f == "leontief_ratio":           # smallest L (step 0.01) that makes labor no longer binding
        L = 0.0
        while v["b"] * L < v["a"] * v["K"] - 1e-9: L += 0.01
        return round(L, 2)
    if f == "ratio": return v["num"] / v["den"]
    return None

C = Checker()
for q in load_static("S15"):
    if "verify" not in q: C.fails.append(f"{q['id']}: num question without verify spec"); continue
    C.check(q["id"], q["answer"], spec_solver(q["verify"]), q.get("tol", 0.01))

def cubic_table(p):
    Ls = list(range(len(p["Qs"]))) if "Qs" in p else None
    Q = lambda L: -p["c"] * L ** 3 + p["b"] * L ** 2 + p["a"] * L
    return Q

S = load_samples("S15-")
for gid, rows in S.items():
    for r in rows:
        p, a = r["params"], r["answer"]
        if gid == "S15-02-g1": want = -p["c"] * p["L"] ** 3 + p["b"] * p["L"] ** 2 + p["a"] * p["L"]
        elif gid in ("S15-04-g1", "S15-03-g1", "S15-05-g1", "S15-06-g1", "S15-10-g1"):
            Q = cubic_table(p); Ls = list(range(len(p["Qs"]))); Qs = [Q(L) for L in Ls]
            if Qs != p["Qs"]: C.fails.append(f"{gid} seed {r['seed']}: table does not match the stated function")
            v = {"L": Ls, "Q": Qs}
            if gid == "S15-04-g1": v.update(f="table_mp", at=p["n"])
            if gid == "S15-03-g1": v.update(f="table_ap", at=p["n"])
            if gid == "S15-05-g1": v.update(f="first_diminishing")
            if gid == "S15-06-g1": v.update(f="table_vmp", at=p["n"], P=p["P"])
            if gid == "S15-10-g1": v.update(f="table_hire", P=p["P"], w=p["w"])
            want = table_solver(v)
        elif gid == "S15-10-g2": want = spec_solver(dict(f="cd_hire", **p))
        elif gid == "S15-09-g1": want = spec_solver(dict(f="cd_mp", **p))
        elif gid == "S15-08-g1":
            want = spec_solver(dict(f="leontief_q", **p)) if p["ask"] == "Q" else spec_solver(dict(f="leontief_mp", wrt="L" if p["ask"] == "MPL" else "K", **p))
        elif gid == "S15-07-g1":
            want = spec_solver(dict(f="linear_q", **p)) if p["ask"] == "Q" else spec_solver(dict(f="linear_mp", wrt="L" if p["ask"] == "MPL" else "K", **p))
        else: C.fails.append(f"{gid}: no checker written"); break
        C.check(f"{gid} seed {r['seed']}", a, want, r.get("tol") or 0.01)
sys.exit(C.report("S15"))
