from common import *
def num(los, stem, ans, explain, verify, unit=""): return {"los": los, "type": "num", "kind": "calc", "stem": stem, "answer": ans, "unit": unit, "tol": 0.01, "explain": explain, "verify": verify}
def mc(los, kind, stem, choices, ans, explain): return {"los": los, "type": "mc", "kind": kind, "stem": stem, "choices": choices, "answer": ans, "explain": explain}
def DV(al, be, ga, c, who, **k): return {"f": "dbert", "al": al, "be": be, "ga": ga, "c": c, "who": who, **k}
cases = [
 {"id": "S22-case1", "title": "Two ski resorts (differentiated Bertrand)", "los": ["S22-02", "S22-03", "S22-04"],
  "stem": "A made-up example in Bryce's form. Two ski resorts near the same city set day-pass prices. Each resort's daily demand (hundreds of skiers) is Q_i = 80 - p_i + p_j, and each has marginal cost $20 per skier.",
  "parts": [
   mc(["S22-03"], "apply", "Which oligopoly model fits?", ["Differentiated Bertrand", "Standard Bertrand", "Cournot", "Stackelberg"], 0, "Price competition, differentiated products (Bryce p. 10)."),
   mc(["S22-02"], "calc", "What is resort 1's reaction function?", ["p_1 = (100 + p_2)/2", "p_1 = (80 - p_2)/2", "p_1 = 100 - p_2", "p_1 = 20"], 0, "p_1 = (a + p_2 + c)/2 = (80 + p_2 + 20)/2."),
   num(["S22-02"], "What is the equilibrium price?", 100, "p = a + c = 80 + 20 = $100.", DV(80, 1, 1, 20, "p"), "$"),
   num(["S22-04"], "Resort 2 raises its price to $120. What is resort 1's best price?", 110, "(80 + 120 + 20)/2 = $110.", DV(80, 1, 1, 20, "br", pj=120), "$"),
   num(["S22-02"], "What is each resort's equilibrium profit (in $ hundreds)?", 6400, "Q = 80; profit (100 - 20) × 80 = 6,400.", DV(80, 1, 1, 20, "pi"))]},
 {"id": "S22-case2", "title": "Selling an identical part online (standard Bertrand)", "los": ["S22-01", "S22-03", "S22-04"],
  "stem": "A made-up example. Two online sellers offer the identical replacement part. Buyers see both prices on a comparison site and have no switching costs. Market demand is Q = 1,000 - 10P.",
  "parts": [
   mc(["S22-03"], "apply", "Which model fits?", ["Standard Bertrand", "Differentiated Bertrand", "Cournot", "Stackelberg"], 0, "Identical goods, visible prices."),
   num(["S22-01"], "If both have marginal cost $20, what is the equilibrium price?", 20, "P = MC.", {"f": "bert", "A": 1000, "k": 10, "c1": 20, "c2": 20, "who": "P"}, "$"),
   num(["S22-04"], "Seller 2's cost rises to $30 while seller 1's stays $20. About how much does seller 1 earn? (Treat 'just below $30' as $30.)", 7000, "Price just under $30, Q = 700, profit (30 - 20) × 700.", {"f": "bert", "A": 1000, "k": 10, "c1": 20, "c2": 30, "who": "pi1"}, "$"),
   mc(["S22-04"], "apply", "Back at equal costs, what could seller 1 do to earn positive profit?", ["Differentiate the part or add switching costs (warranty, bundled service)", "Raise price above $20", "Lower price below $20", "Produce more"], 0, "Escaping the Bertrand trap.")]},
 {"id": "S22-case3", "title": "Comparing the four models (textbook market)", "los": ["S22-01", "S22-04", "S21-06"],
  "stem": "From the textbook's model comparison: P = 1,000 - (Q_1 + Q_2), each firm's cost C_i = 4Q_i.",
  "parts": [
   num(["S22-01"], "What is the price under standard Bertrand?", 4, "P = MC = $4.", {"f": "model_price", "a": 1000, "b": 1, "c": 4, "model": "Bertrand"}, "$"),
   num(["S22-04"], "What is the price under Cournot?", 336, "Each 332, Q = 664, P = $336.", {"f": "model_price", "a": 1000, "b": 1, "c": 4, "model": "Cournot"}, "$"),
   num(["S22-04"], "What is the price under Stackelberg?", 253, "498 + 249 = 747, P = $253.", {"f": "model_price", "a": 1000, "b": 1, "c": 4, "model": "Stackelberg"}, "$"),
   mc(["S22-04"], "concept", "Which ordering of total output is correct?", ["Collusion < Cournot < Stackelberg < Bertrand", "Bertrand < Stackelberg < Cournot < Collusion", "Cournot < Collusion < Bertrand < Stackelberg", "All equal"], 0, "498, 664, 747, 996.")]}]
write_cases("S22", cases)
print("cases", len(cases), sum(len(c["parts"]) for c in cases))
