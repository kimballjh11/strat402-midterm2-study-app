from common import *
CL = list(range(8)); CQ = [0, 8, 20, 36, 48, 56, 60, 58]
CT = table(["Workers (L)", "Cars washed per day (Q)"], [[l, q] for l, q in zip(CL, CQ)])
def num(los, stem, ans, explain, verify, unit=""): return {"los": los, "type": "num", "kind": "calc", "stem": stem, "answer": ans, "unit": unit, "tol": 0.01, "explain": explain, "verify": verify}
def mc(los, kind, stem, choices, ans, explain): return {"los": los, "type": "mc", "kind": kind, "stem": stem, "choices": choices, "answer": ans, "explain": explain}
V = lambda f, **k: dict(f=f, L=CL, Q=CQ, **k)
cases = [
 {"id": "S15-case1", "title": "Sparkle Car Wash", "los": ["S15-03", "S15-04", "S15-05", "S15-06", "S15-10"],
  "stem": "Sparkle Car Wash has two wash bays (capital is fixed) and is deciding how many attendants to schedule. Each wash sells for $15 and attendants earn $100 per day.\n\n" + CT,
  "parts": [
   num(["S15-04"], "What is the marginal product of the 3rd attendant?", 16, "MP = Q(3) - Q(2) = 36 - 20 = 16 cars.", V("table_mp", at=3), "cars"),
   num(["S15-03"], "What is the average product of labor with 4 attendants?", 12, "AP = 48 / 4 = 12 cars per attendant.", V("table_ap", at=4), "cars per attendant"),
   mc(["S15-05"], "apply", "Over what range of attendants does Sparkle experience diminishing marginal returns?", ["Attendants 4 to 6", "Attendants 1 to 3", "Attendants 7 and above", "36 to 60 cars"], 0,
      "MPs: 8, 12, 16, 12, 8, 4, -2. MP rises through attendant 3, falls but stays positive for 4 to 6, and is negative at 7. 36 to 60 is a range of output, not labor."),
   num(["S15-06"], "What is the value marginal product of the 5th attendant?", 120, "MP of the 5th = 56 - 48 = 8 cars. VMP = $15 × 8 = $120.", V("table_vmp", at=5, P=15), "$"),
   num(["S15-10"], "How many attendants maximize profit?", 5, "VMPs: $120, $180, $240, $180, $120, $60, -$30. Hire while VMP ≥ $100: attendant 5 ($120) yes, attendant 6 ($60) no. Hire 5.", V("table_hire", P=15, w=100), "attendants")]},
 {"id": "S15-case2", "title": "Ridgeline Office Chairs", "los": ["S15-02", "S15-03", "S15-09", "S15-10", "S15-11"],
  "stem": "Ridgeline makes office chairs. Engineers estimate the production function \\(Q = 4K^{0.5}L^{0.5}\\), where K is machines and L is worker-days. The plant has 25 machines and cannot add more this quarter. Chairs sell for $60 and the wage is $150 per worker-day.",
  "parts": [
   num(["S15-02", "S15-09"], "How many chairs are produced with 16 worker-days?", 80, "Q = 4 × √25 × √16 = 4 × 5 × 4 = 80.", {"f": "cd_q", "A": 4, "a": 0.5, "b": 0.5, "K": 25, "L": 16}, "chairs"),
   num(["S15-09", "S15-04"], "What is the marginal product of labor at 16 worker-days?", 2.5, "MP_L = 4 × 0.5 × K^0.5 × L^-0.5 = 2 × 5 / 4 = 2.5 chairs.", {"f": "cd_mp", "A": 4, "a": 0.5, "b": 0.5, "K": 25, "L": 16, "wrt": "L"}, "chairs"),
   num(["S15-03"], "What is the average product of labor at 16 worker-days?", 5, "AP = Q / L = 80 / 16 = 5 chairs per worker-day.", {"f": "cd_ap", "A": 4, "a": 0.5, "b": 0.5, "K": 25, "L": 16}, "chairs per worker-day"),
   num(["S15-10"], "What is the profit-maximizing number of worker-days?", 16, "MP_L = 10 / √L. VMP = 60 × 10 / √L = 600 / √L. Set = 150: √L = 4, L = 16.", {"f": "cd_hire", "A": 4, "a": 0.5, "b": 0.5, "K": 25, "P": 60, "w": 150}, "worker-days"),
   num(["S15-10"], "The wage rises to $200. What is the new profit-maximizing number of worker-days?", 9, "600 / √L = 200, so √L = 3 and L = 9. A higher wage means less labor.", {"f": "cd_hire", "A": 4, "a": 0.5, "b": 0.5, "K": 25, "P": 60, "w": 200}, "worker-days"),
   mc(["S15-11"], "concept", "What does this production function assume about machines and workers?", ["They are imperfect substitutes", "They are perfect substitutes", "They must be used in fixed proportions", "Machines add nothing once workers are hired"], 0,
      "Cobb-Douglas allows some, but not perfect, substitution between inputs.")]},
 {"id": "S15-case3", "title": "Fresh Fold Sandwich Line", "los": ["S15-07", "S15-08", "S15-04"],
  "stem": "Fresh Fold's sandwich line follows \\(Q = \\min(20K, 10L)\\), where K is ovens and L is workers. It currently has 3 ovens and 5 workers.",
  "parts": [
   num(["S15-08"], "How many sandwiches does the line produce per hour?", 50, "Q = min(20 × 3, 10 × 5) = min(60, 50) = 50. Labor binds.", {"f": "leontief_q", "a": 20, "b": 10, "K": 3, "L": 5}, "sandwiches"),
   num(["S15-08", "S15-04"], "What is the marginal product of a 6th worker?", 10, "min(60, 60) = 60, up from 50. MP = 10.", {"f": "leontief_mp", "a": 20, "b": 10, "K": 3, "L": 5, "wrt": "L"}, "sandwiches"),
   num(["S15-08"], "With 5 workers, what is the marginal product of a 4th oven?", 0, "min(80, 50) = 50. No change: labor binds, so the oven's MP is 0.", {"f": "leontief_mp", "a": 20, "b": 10, "K": 3, "L": 5, "wrt": "K"}, "sandwiches"),
   num(["S15-08"], "If Fresh Fold buys a 4th oven, how many workers does it need so neither input is wasted?", 8, "No waste when 20K = 10L: 80 = 10L, L = 8.", {"f": "leontief_ratio", "a": 20, "b": 10, "K": 4}, "workers"),
   num(["S15-07"], "Suppose instead the technology were linear, \\(Q = 20K + 10L\\). How much would a 4th oven add?", 20, "For a linear function MP_K is the coefficient on K: 20, regardless of how many workers there are.", {"f": "linear_mp", "a": 20, "b": 10, "K": 3, "L": 5, "wrt": "K"}, "sandwiches")]}]
write_cases("S15", cases)
print("cases", len(cases), sum(len(c["parts"]) for c in cases))
