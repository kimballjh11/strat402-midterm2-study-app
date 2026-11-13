"""S16 independent checks: isoquants by bisection, MRTS by numeric derivatives, cost minimization by brute-force search along the isoquant."""
import sys
from lib import *

def bisect(f, lo, hi, iters=200):
    """Root of increasing f on [lo, hi]."""
    for _ in range(iters):
        m = (lo + hi) / 2
        if f(m) < 0: lo = m
        else: hi = m
    return (lo + hi) / 2

def iso_k(q, Q, L): return bisect(lambda K: q(K, L) - Q, 0, 1e9)

def cheapest_cd(v):
    """Minimize wL + r*K(L) along the isoquant by a coarse log grid then golden section."""
    q = cd(v["A"], v["a"], v["b"])
    cost = lambda L: v["w"] * L + v["r"] * iso_k(q, v["Q"], L)
    grid = [10 ** (i / 50) for i in range(-150, 351)]
    best = min(grid, key=cost)
    L = argmax_cont(lambda x: -cost(x), best / 1.2, best * 1.2)
    return L, iso_k(q, v["Q"], L), cost(L)

def grid_min_cost(prod, Q, w, r, Lmax, Kmax, n=400):
    """Cheapest (L, K) on a grid that reaches Q; corners and kinks are included because the grids hit Q/a and Q/b."""
    best = None
    Ls = sorted({Lmax * i / n for i in range(n + 1)}); Ks = sorted({Kmax * i / n for i in range(n + 1)})
    for L in Ls:
        for K in Ks:
            if prod(K, L) >= Q - 1e-9:
                c = w * L + r * K
                if best is None or c < best: best = c
                break
    return best

def solve(v):
    f = v["f"]
    if f == "iso_k": return iso_k(cd(v["A"], v["a"], v["b"]), v["Q"], v["L"])
    if f == "lin_iso_k": return bisect(lambda K: v["a"] * K + v["b"] * v["L"] - v["Q"], 0, 1e9)
    if f == "cd_mrts":
        q = cd(v["A"], v["a"], v["b"])
        return deriv(lambda x: q(v["K"], x), v["L"]) / deriv(lambda x: q(x, v["L"]), v["K"])
    if f == "cd_bang":
        q = cd(v["A"], v["a"], v["b"])
        mp = deriv(lambda x: q(v["K"], x), v["L"]) if v["wrt"] == "L" else deriv(lambda x: q(x, v["L"]), v["K"])
        return mp / v["price"]
    if f == "ratio": return v["num"] / v["den"]
    if f == "diff": return v["x2"] - v["x1"]
    if f == "cost": return v["w"] * v["L"] + v["r"] * v["K"]
    if f in ("costmin_L", "costmin_K", "costmin_C"):
        L, K, C = cheapest_cd(v)
        return {"costmin_L": L, "costmin_K": K, "costmin_C": C}[f]
    if f == "linear_cost":
        return grid_min_cost(lambda K, L: v["a"] * K + v["b"] * L, v["Q"], v["w"], v["r"], v["Q"] / v["b"], v["Q"] / v["a"])
    if f == "leontief_cost":
        return grid_min_cost(lambda K, L: min(v["a"] * K, v["b"] * L), v["Q"], v["w"], v["r"], 2 * v["Q"] / v["b"], 2 * v["Q"] / v["a"])
    return None

C = Checker()
for q in load_static("S16"):
    if "verify" not in q: C.fails.append(f"{q['id']}: num question without verify spec"); continue
    C.check(q["id"], q["answer"], solve(q["verify"]), q.get("tol", 0.01))

for gid, rows in load_samples("S16-").items():
    for r in rows:
        p, a = r["params"], r["answer"]; lab = f"{gid} seed {r['seed']}"
        if gid == "S16-01-g1": want = solve(dict(f="iso_k", **p))
        elif gid == "S16-02-g1": want = solve(dict(f="cd_mrts", **p))
        elif gid == "S16-03-g1":
            q = cd(1, 0.5, 0.5); want = iso_k(q, p["Q"], p["L"] - 1) - iso_k(q, p["Q"], p["L"])
        elif gid == "S16-04-g1":
            want = {"maxL": lambda: p["C"] / p["w"], "maxK": lambda: p["C"] / p["r"], "slope": lambda: -p["w"] / p["r"],
                    "cost": lambda: p["w"] * p["L"] + p["r"] * p["K"]}[p["ask"]]()
        elif gid == "S16-05-g1":
            # move $1 from capital to labor: output change = MPL/w - MPK/r
            d = p["MPL"] / p["w"] - p["MPK"] / p["r"]
            text = "Use more labor and less capital" if d > 1e-9 else "Use more capital and less labor" if d < -1e-9 else "Keep the same mix; it is cost minimizing"
            C.check(lab, 1, 1 if r["choices"][a] == text else 0); continue
        elif gid == "S16-06-g1": want = solve(dict(f="costmin_" + p["ask"], **{k: v for k, v in p.items() if k != "ask"}))
        elif gid == "S16-06-g2": want = solve(dict(f="linear_cost", **p))
        elif gid == "S16-06-g3": want = solve(dict(f="leontief_cost", **p))
        else: C.fails.append(f"{gid}: no checker written"); break
        C.check(lab, a, want, r.get("tol") or 0.01)
sys.exit(C.report("S16"))
