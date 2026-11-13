from common import *
from S21_questions import cournot, stack, collude, br
def num(los, stem, ans, explain, verify, unit=""): return {"los": los, "type": "num", "kind": "calc", "stem": stem, "answer": ans, "unit": unit, "tol": 0.01, "explain": explain, "verify": verify}
def mc(los, kind, stem, choices, ans, explain): return {"los": los, "type": "mc", "kind": kind, "stem": stem, "choices": choices, "answer": ans, "explain": explain}
def V(f, a, b, c1, c2, who, **k): return {"f": f, "a": a, "b": b, "c1": c1, "c2": c2, "who": who, **k}
co, st, cl = cournot(1000, 1, 4, 4), stack(1000, 1, 4, 4), collude(1000, 1, 4)
q = br(120, 2, 20, 12.5); Pq = 120 - 2 * (q + 12.5)
cases = [
 {"id": "S21-case1", "title": "One market, three models (textbook comparison)", "los": ["S21-02", "S21-03", "S21-06"],
  "stem": "From the textbook's model comparison. Two firms face inverse demand P = 1,000 - (Q_1 + Q_2). Each has cost C_i = 4Q_i (marginal cost $4, no fixed cost).",
  "parts": [
   num(["S21-02", "S21-04"], "If both choose output at the same time, what is each firm's Cournot output?", co["q1"], "Reaction: Q_1 = 498 - 0.5Q_2. Identical firms: (1,000 - 4)/3 = 332.", V("cournot", 1000, 1, 4, 4, "q1")),
   num(["S21-02"], "What is each firm's Cournot profit?", co["pi1"], "P = 1,000 - 664 = $336; (336 - 4) × 332 = $110,224.", V("cournot", 1000, 1, 4, 4, "pi1"), "$"),
   num(["S21-03"], "If firm 1 commits to its output first, how much does it produce?", st["q1"], "(1,000 + 4 - 8)/2 = 498.", V("stack", 1000, 1, 4, 4, "q1")),
   num(["S21-03"], "What price results in the Stackelberg case?", st["P"], "Follower 498 - 249 = 249; Q = 747; P = $253.", V("stack", 1000, 1, 4, 4, "P"), "$"),
   mc(["S21-06"], "calc", "If the firms could legally collude, how would each firm's profit compare with Cournot?", ["$124,002 instead of $110,224", "$110,224 instead of $124,002", "Zero", "The same"], 0, "Collusion: Q = 498, P = $502, 249 each, profit 498 × 249 = $124,002.")]},
 {"id": "S21-case2", "title": "A two-member oil cartel", "los": ["S21-02", "S21-04", "S21-06"],
  "stem": "Two oil producers face inverse demand P = 120 - 2(Q_1 + Q_2) (millions of barrels, $ per barrel). Each has marginal cost $20. They meet to set production quotas.",
  "parts": [
   mc(["S21-04"], "calc", "What is producer 1's reaction function?", ["Q_1 = 25 - 0.5Q_2", "Q_1 = 50 - Q_2", "Q_1 = 30 - 0.5Q_2", "Q_1 = 25 + 0.5Q_2"], 0, "MR_1 = 120 - 2Q_2 - 4Q_1 = 20, so 4Q_1 = 100 - 2Q_2."),
   num(["S21-06"], "If they split the monopoly output, what is each producer's quota?", 12.5, "MR = 120 - 4Q = 20 gives Q = 25; 12.5 each.", V("collude", 120, 2, 20, 20, "q1")),
   num(["S21-06"], "Producer 2 keeps its quota. What is producer 1's best output?", q, "Q_1 = 25 - 0.5(12.5) = 18.75.", V("br", 120, 2, 20, 20, "q1", q2=12.5)),
   num(["S21-06"], "What does producer 1 earn by cheating?", round((Pq - 20) * q, 2), "P = 120 - 2(31.25) = $57.50; (57.50 - 20) × 18.75 = $703.13, more than $625 from keeping the quota.", V("cheat", 120, 2, 20, 20, "pi1", quota=12.5), "$"),
   mc(["S21-02"], "apply", "If both cheat and best-respond to each other, where do they end up?", ["The Cournot equilibrium, 16.67 each at P = $53.33", "The monopoly outcome", "Price equal to $20", "Producer 1 at 25, producer 2 at 0"], 0, "Bryce p. 6: back in the Cournot game.")]},
 {"id": "S21-case3", "title": "Which oligopoly model?", "los": ["S21-01", "S21-05"],
  "stem": "A made-up example. A consultant studies three industries: (A) four potash mines that each set annual output without seeing the others' plans; (B) a market where one battery maker has already built a giant plant and a newcomer is deciding how big to build; (C) two online sellers of an identical phone charger whose prices appear side by side on a comparison site.",
  "parts": [
   mc(["S21-05"], "apply", "Which model fits industry A?", ["Cournot", "Stackelberg", "Standard Bertrand", "Differentiated Bertrand"], 0, "Quantity, simultaneous, homogeneous."),
   mc(["S21-05"], "apply", "Which model fits industry B?", ["Stackelberg", "Cournot", "Standard Bertrand", "Sweezy"], 0, "Committed capacity first, follower observes."),
   mc(["S21-05"], "apply", "Which model fits industry C?", ["Standard Bertrand", "Cournot", "Stackelberg", "Differentiated Bertrand"], 0, "Price, identical goods, buyers see all prices (S22)."),
   mc(["S21-01"], "concept", "What makes all three oligopolies rather than perfectly competitive markets?", ["Each firm's actions affect the others' prospects", "Each has exactly two firms", "Each sells differentiated products", "Prices are regulated"], 0, "Interdependence (Bryce p. 1).")]}]
write_cases("S21", cases)
print("cases", len(cases), sum(len(c["parts"]) for c in cases))
