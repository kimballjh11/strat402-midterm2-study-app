from common import *
from S21_lessons import BOOK, FIG1

PDERIV = {"title": "Derivative when price is the choice", "body": r"With demand \(q_1 = \alpha - \beta p_1 + \gamma p_2\) and marginal cost c, profit is \(\pi_1 = (p_1 - c)(\alpha - \beta p_1 + \gamma p_2)\). Use the product rule: derivative of the first factor (1) times the second, plus the first times the derivative of the second \((-\beta)\): \(\frac{d\pi_1}{dp_1} = (\alpha - \beta p_1 + \gamma p_2) - \beta(p_1 - c)\). Set it to 0: \(2\beta p_1 = \alpha + \beta c + \gamma p_2\). Tiny example: \(\alpha = 100, \beta = 2, \gamma = 1, c = 10\): \(4p_1 = 120 + p_2\), so \(p_1 = 30 + 0.25p_2\)."}
SYM = {"title": "Symmetric equilibrium in prices", "body": r"If both firms are identical, set \(p_1 = p_2 = p\) in one reaction function. From \(p = 30 + 0.25p\): \(0.75p = 30\), so \(p = 40\). In general \(p^* = \frac{\alpha + \beta c}{2\beta - \gamma}\). With Bryce's demand \(Q_i = a - p_i + p_j\) (\(\beta = \gamma = 1\)): \(p^* = a + c\)."}

LESSONS = [
{"id": "S22-01", "title": "Standard Bertrand oligopoly", "calc": True,
 "plain": r"""**Standard Bertrand oligopoly** is competition in **price** among firms selling **homogeneous** (identical) goods (Bryce p. 6).

**The model's assumptions** (Bryce pp. 6 to 7): two firms with the same technology sell identical products; consumers see all prices; no switching costs, no transaction costs, no capacity constraints; identical marginal costs. Textbook conditions: few firms serving many consumers; identical products at a constant marginal cost; firms compete on price and react optimally to rivals' prices; consumers have perfect information and no transaction costs; barriers to entry.

**The race to the bottom** (Bryce p. 7). Firm 1 sets price P. Firm 2 can price above (sells 0), equal (gets half), or just below (gets the whole market). Undercutting always pays, so each firm undercuts the other, and they stop only at marginal cost. The firms reason through this instantly, so:
$$P_1 = P_2 = MC_1 = MC_2$$
**Each firm earns zero economic profit, even with only two firms.** This is the textbook's "Bertrand trap": the perfectly competitive outcome with no deadweight loss.

**Variations** (Bryce p. 7):
- **Unequal marginal costs:** the low-cost firm takes the whole market by pricing **just below the high-cost firm's marginal cost**, not at its own MC, earning a margin on every unit.
- **Capacity constraints:** a firm that cannot serve the whole market gains nothing by undercutting, so prices above MC may be sustainable.
- **Repeated play:** with no certain end, firms might match instead of undercut, but holding prices above MC is very hard here; entrants or many rivals spoil it.

**Where it fits:** markets where consumers see all prices and goods are truly alike. Bryce: the Internet made many markets commodity-like and Bertrand markets much more common. Textbook evidence (Inside Business 9-3): on a price comparison site, the gap between the two lowest prices averaged 22% with two sellers and under 3% with more than 20.

**Escaping the trap** (textbook): raise switching costs or make buyers see the products as different (why Kellogg's and General Mills advertise their corn flakes).

**Contestable markets** (textbook): if all producers have the same technology, consumers respond quickly, incumbents cannot quickly cut price after entry, and there are **no sunk costs**, then even one incumbent must price at cost, because a hit-and-run entrant would undercut. Sunk costs (costs an entrant cannot recover on exit) protect incumbents.""",
 "why": "Practice exam Q30, Comprehension Quiz 10 Q7 and Q8 and the Session 22 reading quiz Q1 and Q3 are expected to test standard Bertrand.",
 "definition": "Standard Bertrand oligopoly: a few firms selling identical products at constant marginal cost compete on price; consumers have perfect information and no switching or transaction costs. The equilibrium is P = MC with zero economic profit.",
 "formulas": [{"name": "Standard Bertrand equilibrium, equal costs", "tex": r"P_1 = P_2 = MC", "onSheet": False},
              {"name": "Unequal costs (c_1 < c_2)", "tex": r"P \approx c_2, \quad \pi_1 \approx (c_2 - c_1)\,Q(c_2)", "onSheet": False, "note": "Low-cost firm prices just below the rival's MC and serves the whole market (if its monopoly price is higher than c_2)."}],
 "derivation": "Any price above MC can be undercut by a penny to take the whole market, so it is not an equilibrium. A price below MC loses money. Only P = MC survives.",
 "math": [],
 "worked": [{"title": "Unequal costs", "problem": "Two sellers of an identical part face market demand Q = 1,000 - 10P. Firm 1's MC is $20, firm 2's is $30. Consumers see all prices. What price and profits result?",
   "steps": ["Firm 1 prices just below $30 (call it $30).", "Q = 1,000 - 10(30) = 700, all from firm 1.", "Firm 1's profit is about (30 - 20) × 700 = $7,000; firm 2 sells nothing.", "Check: firm 1's monopoly price would be higher than $30, so it does not want to price above $30."],
   "answer": "P just under $30; firm 1 earns about $7,000; firm 2 earns 0."},
  {"title": "Sunk costs and entry (textbook numbers)", "problem": "An entrant must pay $100,000 for a moving truck it could resell for $80,000 on exit. How much of that is sunk?",
   "steps": ["Sunk = what cannot be recovered: 100,000 - 80,000."], "answer": "$20,000 is sunk. If incumbents would cut prices before the entrant earns that back, it stays out."}],
 "graph": {"component": "reaction", "params": {"mode": "quantity", "a": 1000, "b": 1, "c1": 4, "c2": 4}, "caption": "The table under the graph includes the Bertrand row: price equals MC ($4) and profit is zero."},
 "traps": ["Bertrand with identical goods and equal costs gives P = MC with only TWO firms.",
           "With unequal costs the low-cost firm prices just below the RIVAL's MC, not its own.",
           "Bertrand firms choose PRICE; Cournot firms choose quantity.",
           "Capacity constraints and differentiation are the escapes; a contestable market with no sunk costs disciplines even a single firm."],
 "sources": {"slides": "S22 slides not yet available", "read": "Ch. 9: Bertrand Oligopoly; Comparing Oligopoly Models; Contestable Markets; Bryce pp. 6 to 7", "exercise": "Oligopoly Exercise (not yet available)", "quiz": "Session 22 Reading Quiz Q1, Q3; Comprehension Quiz 10 Q7, Q8 (not yet available); Practice exam Q30"}},

{"id": "S22-02", "title": "Differentiated Bertrand oligopoly", "calc": True,
 "plain": r"""**Differentiated Bertrand** is a market where goods are **moderately differentiated** and **price** is the main strategic variable. Bryce (p. 8) calls it **the most common type of oligopoly in today's world**: cola, desktop computers, automobiles, airlines, ski resorts.

**Why prices stay above cost** (Bryce p. 8). Each firm has some loyal customers. Even if Firm 2 gave its product away, Firm 1 could still charge a positive price \(p_1^{min}\) (many loyal Coke drinkers would pay 10 cents for a Coke even with a free Pepsi beside it). Both firms know this, so each can raise price, and when the rival raises its price, you can charge that higher price plus a premium for some customers. Prices rise until the premium consumers will pay is used up.

**Reaction functions in prices slope UPWARD** (strategic complements): a higher rival price raises your best price. Compare Cournot, where quantity reaction functions slope down.

**Bryce's footnote 9.** Demand for firm i: \(Q_i = a - p_i + p_j\). Revenue \(ap_i - p_i^2 + p_ip_j\); setting MR equal to marginal cost gives the reaction function
$$p_i^* = \frac{a + p_j + c}{2}$$
It slopes up, and when \(p_j = 0\), \(p_i = \frac{a + c}{2} > 0\). Solving both reaction functions gives the equilibrium \(p_i = a + c\).

**General linear version:** \(q_1 = \alpha - \beta p_1 + \gamma p_2\) gives \(p_1 = \frac{\alpha + \beta c + \gamma p_2}{2\beta}\) and symmetric equilibrium \(p^* = \frac{\alpha + \beta c}{2\beta - \gamma}\). None of this is on the equation sheet; derive it from profit = (p - c)q.

**The adjustment** (Bryce p. 9): starting from \(p_2 = 0\), firms take turns raising price (points a, b, c) until equilibrium d. The firms are only maximizing profit, not colluding, yet reach high prices. If prices start above equilibrium, they fall, but only to the equilibrium, not to marginal cost.

**Textbook:** each firm faces a downward-sloping demand curve and charges P > MC, like monopolistic competition, but barriers to entry let profits last.""",
 "why": "Practice exam Q36 to Q38, Comprehension Quiz 10 Q9 and Q10 and the Session 22 reading quiz Q2 are expected to test differentiated Bertrand.",
 "definition": "Differentiated Bertrand oligopoly: a few firms selling moderately differentiated products compete on price. Price reaction functions slope upward, and the equilibrium price is above marginal cost.",
 "formulas": [{"name": "Reaction function (Bryce, Q_i = a - p_i + p_j)", "tex": r"p_i^* = \frac{a + p_j + c}{2}", "onSheet": False},
              {"name": "Equilibrium price (Bryce's demand)", "tex": r"p^* = a + c", "onSheet": False},
              {"name": "General symmetric equilibrium", "tex": r"p^* = \frac{\alpha + \beta c}{2\beta - \gamma}", "onSheet": False, "note": "For q_i = α − βp_i + γp_j."}],
 "derivation": r"Profit \(\pi_i = (p_i - c)(a - p_i + p_j)\). Derivative: \((a - p_i + p_j) - (p_i - c) = 0\), so \(p_i = \frac{a + p_j + c}{2}\). Symmetric: \(p = \frac{a + p + c}{2}\), so \(2p = a + p + c\) and \(p = a + c\).",
 "math": [PDERIV, SYM],
 "worked": [{"title": "Bryce's demand", "problem": "Each firm's demand is Q_i = 60 - p_i + p_j, marginal cost $10. Find the reaction function, the equilibrium price, quantity and profit.",
   "steps": [r"\(p_i = \frac{60 + p_j + 10}{2} = 35 + 0.5p_j\).", "Symmetric: p = 35 + 0.5p, so p = $70 (= a + c).", "Q = 60 - 70 + 70 = 60 each.", "Profit = (70 - 10) × 60 = $3,600 each."], "answer": "p = $70, well above MC of $10."},
  {"title": "General form", "problem": "q_1 = 100 - 2p_1 + p_2 (symmetric), MC = $10. Find each firm's price.",
   "steps": [r"\(p_1 = \frac{100 + 20 + p_2}{4} = 30 + 0.25p_2\).", "Symmetric: 0.75p = 30, p = $40.", "q = 100 - 80 + 40 = 60; profit = 30 × 60 = $1,800."], "answer": "$40 each."}],
 "graph": {"component": "reaction", "params": {"mode": "price", "al": 60, "be": 1, "ga": 1, "c": 10}, "caption": "Bryce's demand Q_i = a - p_i + p_j with a = 60, c = 10. Upward-sloping price reaction functions cross at p = a + c = $70."},
 "traps": ["Price reaction functions slope UP; Cournot quantity reaction functions slope DOWN.",
           "Differentiation is why price stays above MC without any collusion.",
           "Even if the rival charges 0, you still charge a positive price (p min).",
           "Equilibrium in Bryce's model is a + c, not (a + c)/2 (that is the best response to a rival price of 0)."],
 "sources": {"slides": "S22 slides not yet available", "read": "Ch. 9 Appendix: Differentiated-Product Bertrand Oligopoly; Bryce pp. 8 to 9", "exercise": "Oligopoly Exercise (not yet available)", "quiz": "Session 22 Reading Quiz Q2; Comprehension Quiz 10 Q9, Q10 (not yet available); Practice exam Q36 to Q38"}},

{"id": "S22-03", "title": "Identifying standard or differentiated Bertrand conditions", "calc": False,
 "plain": r"""Bryce ends the reading with three questions for working out market structure and type of competition (pp. 9 to 10):

1. **How many firms are meaningfully engaged in direct competition?** Markets are easy to define too broadly: gas stations in north and south Provo do not really compete directly; competition happens at local intersections. Cell phone companies compete on national networks, so their market is national.
2. **What percentage of the firms' target customer base overlaps?** High overlap means direct competition. Salt Lake ski resorts overlap a lot (a differentiated Bertrand oligopoly together) and may also compete with high-end Colorado resorts for East Coast vacation skiers.
3. **What is the primary strategic variable?** Price? Programs? Product features? Lead time? Are firms choosing quantity and letting price float, or explicitly setting price? Airlines: the dominant consideration is **price**, so Bertrand; since they are at least slightly differentiated (location, routes, programs), **differentiated Bertrand**.

**Figure 1 again:**

""" + FIG1 + r"""

**Standard Bertrand fits when:** price is the strategic variable, goods are truly homogeneous, consumers see all prices (few information constraints, often online), no switching costs, similar costs.

**Differentiated Bertrand fits when:** price is the strategic variable, but goods differ enough that some customers stay loyal when a rival is cheaper (brands, locations, features, programs).

**Clues the market is NOT standard Bertrand:** prices well above cost that persist, loyal customers, switching costs, capacity limits, or firms choosing output and letting price float (Cournot).""",
 "why": "Practice exam Q14 and Q30, Comprehension Quiz 10 Q8 and Q9 and the Session 22 reading quiz Q1 and Q2 are expected to ask which model fits.",
 "definition": "A firm is in standard Bertrand when it competes on price with identical products and fully informed buyers; it is in differentiated Bertrand when it competes on price with moderately differentiated products.",
 "formulas": [], "derivation": "", "math": [],
 "worked": [{"title": "Apply Bryce's three questions", "problem": "Two regional grocery chains in one city compete mainly with weekly price ads, but shoppers favor the store nearest home and each chain has a loyalty card. What model fits?",
   "steps": ["Firms in direct competition: the two chains in the city.", "Customer overlap: high (same city).", "Strategic variable: price (weekly ads).", "Products are differentiated by location and loyalty programs."], "answer": "Differentiated Bertrand."}],
 "traps": ["Price competition alone does not mean standard Bertrand: check whether goods are truly identical and prices fully visible.",
           "Define the market by who competes directly: not too broad (all gas stations in a state) and not too narrow.",
           "Non-price tools like frequent flier programs differentiate the product, pointing to differentiated Bertrand."],
 "sources": {"slides": "S22 slides not yet available", "read": "Bryce pp. 3 to 4, 6, 8 to 10 (Determining Market Structure and Competition)", "exercise": "Oligopoly Exercise (not yet available)", "quiz": "Session 22 Reading Quiz Q1, Q2; Comprehension Quiz 10 Q8, Q9 (not yet available); Practice exam Q14, Q30"}},

{"id": "S22-04", "title": "Optimal decisions and competitor responses (Bertrand)", "calc": True,
 "plain": r"""**Standard Bertrand decisions:**
- Equal costs: price at marginal cost; any higher price will be undercut. Profit is zero.
- You have lower cost: price just below the rival's marginal cost and take the whole market (unless your monopoly price is even lower).
- You have higher cost: you cannot profitably match; you sell nothing.
- To escape: differentiate, add switching costs, or be capacity constrained.

**Differentiated Bertrand decisions:**
- Your best price depends on the rival's price through your reaction function. With Bryce's demand \(Q_i = a - p_i + p_j\): \(p_i = \frac{a + p_j + c}{2}\).
- **Rival raises price:** you raise yours too, but by **half as much** in Bryce's model.
- **Rival cuts price:** you cut yours, by half as much.
- **Your cost rises:** your reaction function shifts up; the rival responds by raising its price a bit (upward slope).
- Equilibrium with identical firms: \(p = a + c\).

**Comparing the four models** (textbook, \(P = 1{,}000 - (Q_1 + Q_2)\), MC = $4):

""" + BOOK + r"""

**Takeaway** (textbook): the profit you earn depends heavily on which kind of rivalry your industry has, so work out which model describes your market before choosing a strategy.""",
 "why": "Practice exam Q30 and Q36 to Q38 and Comprehension Quiz 10 Q7, Q9 and Q10 are expected to ask for prices and responses.",
 "definition": "Optimal Bertrand decisions: with identical products, price at (or just under the rival's) marginal cost; with differentiated products, set price on your reaction function, which rises with the rival's price.",
 "formulas": [{"name": "Best response to rival price (Bryce)", "tex": r"p_i = \frac{a + p_j + c}{2}", "onSheet": False},
              {"name": "General best response", "tex": r"p_1 = \frac{\alpha + \beta c + \gamma p_2}{2\beta}", "onSheet": False}],
 "derivation": r"From \(\pi_1 = (p_1 - c)(\alpha - \beta p_1 + \gamma p_2)\): \(\frac{d\pi_1}{dp_1} = \alpha - 2\beta p_1 + \gamma p_2 + \beta c = 0\).",
 "math": [PDERIV, SYM],
 "worked": [{"title": "Responding to a rival's price increase", "problem": "Q_i = 80 - p_i + p_j, MC = $20. The rival raises its price from $100 to $120. What should you charge before and after?",
   "steps": [r"Before: \(p = \frac{80 + 100 + 20}{2} = 100\).", r"After: \(p = \frac{80 + 120 + 20}{2} = 110\).", "You raise your price by $10, half the rival's $20 increase."], "answer": "$100, then $110. (Equilibrium is a + c = $100, so the rival's move to $120 is off equilibrium.)"}],
 "graph": {"component": "reaction", "params": {"mode": "price", "al": 80, "be": 1, "ga": 1, "c": 20}, "caption": "Bryce's demand with a = 80, c = 20. The equilibrium is a + c = $100."},
 "traps": ["In differentiated Bertrand, match a rival's price increase only partly (half, in Bryce's model).",
           "In standard Bertrand with equal costs, any price above MC is undercut.",
           "Stackelberg leader and colluding firms tie for the highest profit in the textbook comparison; Bertrand firms earn zero.",
           "Do not mix up the models: price competition with identical goods gives the LOWEST price of all four."],
 "sources": {"slides": "S22 slides not yet available", "read": "Ch. 9: Bertrand Oligopoly; Comparing Oligopoly Models; Appendix; Bryce pp. 6 to 9", "exercise": "Oligopoly Exercise (not yet available)", "quiz": "Session 22 Reading Quiz Q3; Comprehension Quiz 10 Q7, Q9, Q10 (not yet available); Practice exam Q36 to Q38"}},
]
for L in LESSONS: write_lesson(L)
write_session("S22", {"overview": "Session 22 finishes oligopoly with price competition. In standard Bertrand (identical goods, buyers see all prices) undercutting drives price to marginal cost even with two firms; a lower-cost firm prices just under its rival's cost. In differentiated Bertrand, the most common type today, loyal customers let firms price above cost, and price reaction functions slope upward. Bryce's three questions (how many firms compete directly, how much customers overlap, what the main strategic variable is) identify which model fits a market, and the textbook compares all four models on one demand curve.",
  "provisional": "**Provisional.** No S22 slides, class notes or quiz questions yet. These lessons are built from the professor's assigned reading *Rivalry in Oligopoly* (Bryce), the textbook (Ch. 9: Bertrand, Comparing Oligopoly Models, Contestable Markets, Appendix) and the study guide objectives. Worked numbers labeled textbook or Bryce come from those readings; others are made up for practice. Update with /ingest when slides, the Oligopoly Exercise or Comprehension Quiz 10 arrive."})
print([L["id"] for L in LESSONS])
