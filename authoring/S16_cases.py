from common import *
def num(los, stem, ans, explain, verify, unit=""): return {"los": los, "type": "num", "kind": "calc", "stem": stem, "answer": ans, "unit": unit, "tol": 0.01, "explain": explain, "verify": verify}
def mc(los, kind, stem, choices, ans, explain): return {"los": los, "type": "mc", "kind": kind, "stem": stem, "choices": choices, "answer": ans, "explain": explain}
CD = {"A": 10, "a": 0.5, "b": 0.5}
cases = [
 {"id": "S16-case1", "title": "Roller production (in-class exercise)", "los": ["S16-05", "S16-06"],
  "stem": "From the S16 in-class exercise. Labor is paid $12 per hour and the last worker hired produced 84 rollers per hour. The company rents roller cutters and crimping machines for $15 per hour, and the marginal product of capital is 120 rollers per hour.",
  "parts": [
   num(["S16-05"], "What is the bang for the buck of labor, MP_L / w?", 7, "84 / 12 = 7 rollers per dollar.", {"f": "ratio", "num": 84, "den": 12}, "rollers per $"),
   num(["S16-05"], "What is the bang for the buck of capital, MP_K / r?", 8, "120 / 15 = 8 rollers per dollar.", {"f": "ratio", "num": 120, "den": 15}, "rollers per $"),
   mc(["S16-05"], "apply", "Is the firm using the cost-minimizing combination of capital and labor?", ["No, because MP_L/w and MP_K/r are not equal", "Yes, because MP_K is larger than MP_L", "Yes, because both inputs have positive marginal products", "No, because labor is cheaper than capital"], 0,
      "The professor's answer: no, the bang for the buck is not equal (7 vs 8). A bigger raw MP or a lower price alone does not settle it."),
   mc(["S16-05"], "apply", "Should the firm increase or decrease the capital it uses?", ["Increase capital, because it gives more output per dollar", "Decrease capital, because it costs more per hour", "Keep capital the same", "Decrease capital, because MP_K will fall"], 0,
      "8 > 7, so each dollar moved to capital adds more rollers than it costs in labor output. As it adds capital MP_K falls until the ratios are equal."),
   mc(["S16-06"], "apply", "If the rental rate on capital increases, what happens to the cost-minimizing mix?", ["Less capital and more labor", "More capital and less labor", "No change", "Less of both at the same output"], 0,
      "The professor's answer: invest less in capital and more in labor. A higher r makes the isocost flatter, so the tangency slides toward labor.")]},
 {"id": "S16-case2", "title": "Hundred-unit kitchen", "los": ["S16-01", "S16-02", "S16-05", "S16-06"],
  "stem": "Built on the S16 slides example (pp. 39 to 40). A kitchen produces with \\(Q = 10K^{0.5}L^{0.5}\\) and must make 100 meals per day. Labor costs w = $40 and capital rents for r = $10.",
  "parts": [
   num(["S16-01"], "On the Q = 100 isoquant, how much capital is needed with L = 25?", 4, "\\(100 = 10\\sqrt{K}\\sqrt{25} = 50\\sqrt{K}\\), so \\(\\sqrt{K} = 2\\) and K = 4. The isoquant is K = 100/L.", {"f": "iso_k", **CD, "Q": 100, "L": 25}, "units of capital"),
   num(["S16-02"], "What is the MRTS at L = 25, K = 4?", 0.16, "MRTS = K/L for equal exponents = 4/25 = 0.16. Equivalently MP_L/MP_K = 2/12.5 = 0.16.", {"f": "cd_mrts", **CD, "K": 4, "L": 25}),
   num(["S16-05"], "At L = 25, K = 4, MP_K = 12.5. What is MP_K / r?", 1.25, "12.5 / 10 = 1.25. MP_L/w is only 2/40 = 0.05, so capital is the far better deal.", {"f": "cd_bang", **CD, "K": 4, "L": 25, "price": 10, "wrt": "K"}, "meals per $"),
   num(["S16-06"], "What is the cost-minimizing amount of labor?", 5, "Tangency: K/L = w/r = 4, so K = 4L. \\(100 = 10\\sqrt{4L^2} = 20L\\), L = 5. The slides' table shows (5, 20) is where MP_L/w = MP_K/r = 0.25.", {"f": "costmin_L", **CD, "Q": 100, "w": 40, "r": 10}, "units of labor"),
   num(["S16-06"], "What is the minimum cost of producing 100 meals?", 400, "L = 5, K = 20. C = 40(5) + 10(20) = $400. At (25, 4) the same output costs 40(25) + 10(4) = $1,040.", {"f": "costmin_C", **CD, "Q": 100, "w": 40, "r": 10}, "$"),
   num(["S16-06"], "The rental rate rises to $40. What is the new cost-minimizing amount of labor?", 10, "Now K/L = 40/40 = 1, so K = L and 10L = 100: L = 10, K = 10. Capital got more expensive, so the kitchen uses less capital (20 to 10) and more labor (5 to 10).", {"f": "costmin_L", **CD, "Q": 100, "w": 40, "r": 40}, "units of labor")]},
 {"id": "S16-case3", "title": "A $1,000 isocost", "los": ["S16-04"],
  "stem": "Built on the S16 slides isocost example (pp. 31 to 34). A firm budgets C = $1,000. Labor costs w = $10 per hour and capital rents for r = $25 per hour. Capital is on the vertical axis.",
  "parts": [
   num(["S16-04"], "What is the most labor the firm can hire with no capital?", 100, "C/w = 1,000/10 = 100.", {"f": "ratio", "num": 1000, "den": 10}, "labor hours"),
   num(["S16-04"], "What is the most capital it can rent with no labor?", 40, "C/r = 1,000/25 = 40.", {"f": "ratio", "num": 1000, "den": 25}, "machine hours"),
   num(["S16-04"], "What is the slope of the isocost line?", -0.4, "-w/r = -10/25 = -0.4.", {"f": "ratio", "num": -10, "den": 25}),
   num(["S16-04"], "The budget rises 50% to $1,500. What is the new capital intercept?", 60, "C/r = 1,500/25 = 60. The slope stays -0.4: a budget change is a parallel shift.", {"f": "ratio", "num": 1500, "den": 25}, "machine hours"),
   mc(["S16-04", "S16-06"], "apply", "Back at $1,000, the wage doubles to $20. What happens to the isocost line?", ["The labor intercept falls to 50, the capital intercept stays at 40, and the line gets steeper", "Both intercepts halve", "The capital intercept falls to 20", "The line gets flatter"], 0,
      "C/w = 1,000/20 = 50, C/r is still 40, and the slope -20/25 = -0.8 is steeper. Halving both intercepts is a budget cut, not a price change.")]}]
write_cases("S16", cases)
print("cases", len(cases), sum(len(c["parts"]) for c in cases))
