from common import *
from S15_lessons import JD_MD, JD_TABLE, EXPONENTS, PARTIAL, POWER

COMPARE = table(["", "Linear", "Cobb-Douglas", "Leontief (fixed proportions)"], [
    ["Equation", "Q = aK + bL", "Q = K^a L^b", "Q = min(aK, bL)"],
    ["Slide example", "Q = 4K + 1L", "Q = K^0.5 L^0.5", "Q = min(1K, 1L)"],
    ["Isoquant shape", "Straight line", "Convex curve", "L-shaped"],
    ["MRTS formula", "MP_L / MP_K = b / a", "MP_L / MP_K = bK / (aL)", "N/A"],
    ["MRTS behavior", "Constant", "Changes", "Undefined"],
    ["Substitutability of inputs", "Perfect", "Imperfect (some)", "None"]])

LESSONS = [
{"id": "S15-07", "title": "Linear production function", "calc": True,
 "plain": r"""A **linear** production function adds up the inputs, each with its own weight:
$$Q = aK + bL$$
Each unit of capital always adds \(a\) units of output and each worker always adds \(b\), no matter how many you already have. So the marginal products are constant: \(MP_K = a\) and \(MP_L = b\). There are no diminishing returns.

Because each input contributes a fixed amount, the inputs are **perfect substitutes**. In the slide example \(Q = 4K + 1L\), one machine does the work of 4 workers, always. You could produce with only machines or only workers. A call center where one software license does exactly the work of 3 agents behaves this way.

Graphed with K on the vertical axis, every combination that gives the same output lies on a **straight line** (an isoquant, covered fully in Session 16). The rate at which you can trade L for K never changes, so the MRTS \(= b/a\) is constant.""",
 "why": "Recognizing the form tells you instantly how the inputs relate: constant MP, perfect substitutes, and in Session 16 a corner solution where the firm uses only the input with the higher MP per dollar.",
 "definition": "A linear production function, \\(Q = aK + bL\\), assumes a perfect linear relationship between all inputs and total output: each input has a constant marginal product and the inputs are perfect substitutes.",
 "formulas": [{"name": "Linear production function and its marginal products", "tex": r"Q = aK + bL,\quad MP_K = a,\quad MP_L = b", "onSheet": True},
              {"name": "MRTS for linear", "tex": r"MRTS_{KL} = \frac{MP_L}{MP_K} = \frac{b}{a}", "onSheet": True, "note": "The sheet has MRTS = MP_L / MP_K; for linear that is b/a at every point."}],
 "derivation": r"\(\frac{\partial}{\partial L}(aK + bL) = b\) because aK does not change with L and the derivative of bL is b. Same idea for K.",
 "math": [],
 "worked": [{"title": "Comprehension Quiz 7 setup", "problem": r"\(Q = 4K + L\). Find output, \(MP_L\), \(MP_K\) and the MRTS at \(K = 1\), \(L = 4\).",
   "steps": [r"Output: \(4(1) + 4 = 8\).", r"\(MP_L = 1\) and \(MP_K = 4\), the coefficients.", r"\(MRTS = MP_L/MP_K = 1/4\).", "The values K = 1 and L = 4 do not matter for MP or MRTS. They are the same everywhere."],
   "answer": "Q = 8, MP_L = 1, MP_K = 4, MRTS = 1/4 at every point."}],
 "graph": {"component": "isoquant", "params": {"form": "linear", "a": 4, "b": 1, "Q": 40, "L": 20}, "caption": "Linear isoquants are straight lines. The dashed tangent has the same slope everywhere: constant MRTS."},
 "traps": ["MP for a linear function is the coefficient, not the coefficient times the input. MP_L for Q = 4K + L is 1, not L.",
           "The MRTS does not depend on K and L for a linear function. A choice saying 'it varies with K and L' is wrong (Quiz 7 Q5).",
           "Perfect substitutes means a constant trade rate, not a one for one trade. With Q = 4K + L, one K replaces 4 L.",
           "A linear production function has no diminishing marginal returns."],
 "sources": {"slides": "S15 Production I, pp. 32 to 34", "read": "Ch. 5 pp. 146 to 147", "exercise": "Production Functions workbook, Linear tab", "quiz": "Comprehension Quiz 7 Q5"}},

{"id": "S15-08", "title": "Leontief (fixed proportions) production function", "calc": True,
 "plain": r"""A **Leontief** production function says inputs must be used in a fixed recipe:
$$Q = \min(aK, bL)$$
Output is the SMALLER of \(aK\) and \(bL\). Think of one driver per truck. Ten trucks and 7 drivers move only 7 loads. Adding an 8th truck adds nothing, because there is nobody to drive it. The inputs are **perfect complements** and there is **no substitutability**: you cannot replace a driver with extra trucks.

Consequences:
- The input that gives the smaller number is the **binding** one. Adding more of it raises output.
- Adding more of the non-binding input adds nothing: its marginal product is 0.
- No waste happens only when \(aK = bL\). That is the corner of the L-shaped isoquant.
- The MRTS is undefined (the slides write N/A): there is no rate at which the inputs trade off.""",
 "why": "Fixed proportions show up in real operations (one worker per machine, one chef per station). The manager's job is to buy inputs in the right ratio, since any excess of one input is wasted money.",
 "definition": "A Leontief (fixed proportions) production function, \\(Q = \\min(aK, bL)\\), assumes inputs are used in fixed proportions, so there is no substitutability between them.",
 "formulas": [{"name": "Leontief", "tex": r"Q = \min(aK, bL)", "onSheet": False, "note": "Not on the equation sheet. Output is the smaller of aK and bL."},
              {"name": "No-waste ratio", "tex": r"aK = bL \;\Rightarrow\; \frac{K}{L} = \frac{b}{a}", "onSheet": False}],
 "derivation": r"If \(aK < bL\), capital binds, so \(Q = aK\). One more unit of capital raises Q by \(a\) (until it stops binding). One more worker leaves \(Q = aK\) unchanged, so \(MP_L = 0\).",
 "math": [],
 "worked": [{"title": "Sandwich line", "problem": r"A sandwich line has \(Q = \min(20K, 10L)\), where K is ovens and L is workers. With 3 ovens and 5 workers, what is output? What does a 6th worker add? What does a 4th oven add?",
   "steps": [r"\(Q = \min(20 \times 3, 10 \times 5) = \min(60, 50) = 50\). Labor binds.", r"6th worker: \(\min(60, 60) = 60\). Output rises by 10.", r"4th oven with 5 workers: \(\min(80, 50) = 50\). Output does not change, MP of the oven is 0.", r"No waste requires \(20K = 10L\), so \(L = 2K\): 3 ovens need 6 workers."],
   "answer": "Q = 50. A 6th worker adds 10. A 4th oven adds 0."}],
 "graph": {"component": "isoquant", "params": {"form": "leontief", "a": 20, "b": 10, "Q": 60, "L": 6}, "caption": "Leontief isoquants are L-shaped. Moving right from the corner (more labor) or up (more capital) leaves output unchanged."},
 "traps": ["Output is the MINIMUM of aK and bL, not the sum and not the product.",
           "Remember to multiply by the coefficients before comparing. min(20K, 10L) with K = 3, L = 5 compares 60 and 50, not 3 and 5.",
           "The extra unit of the non-binding input has marginal product zero, not a.",
           "MRTS is undefined (N/A) for Leontief. Do not compute b/a.",
           "Leontief is NOT on the equation sheet."],
 "sources": {"slides": "S15 Production I, pp. 32 to 34", "read": "Ch. 5 p. 147", "exercise": "Production Functions workbook, Leontief tab"}},

{"id": "S15-09", "title": "Cobb-Douglas production function", "calc": True,
 "plain": r"""The **Cobb-Douglas** production function multiplies the inputs, each raised to a power:
$$Q = K^aL^b$$
Sometimes there is a constant in front, \(Q = AK^aL^b\) (Herman Miller in Quiz 7 has \(Q = 2K^{0.5}L^{0.5}\)).

Key features:
- Inputs are **imperfect substitutes**: you can trade capital for labor, but the more labor you already have, the more labor it takes to replace one unit of capital. The isoquant is a **convex curve**.
- With an exponent below 1 (like 0.5), each input has **diminishing marginal product**: every extra worker adds less than the one before.
- You need some of both inputs. If either is 0, output is 0.
- The marginal products are on the equation sheet: \(MP_K = aK^{a-1}L^b\) and \(MP_L = bK^aL^{b-1}\). With a constant \(A\) in front, multiply each MP by \(A\).
- The MRTS changes along the isoquant: \(MRTS = \frac{MP_L}{MP_K} = \frac{bK}{aL}\).""",
 "why": "Cobb-Douglas is the professor's main production function for calculations. The Practice Midterm 2 column of the study guide links this objective to six practice exam questions (Q15 to Q20), more than any other S15 objective.",
 "definition": "A Cobb-Douglas production function, \\(Q = K^aL^b\\), assumes some, but not perfect, substitutability between inputs.",
 "formulas": [{"name": "Cobb-Douglas", "tex": r"Q = K^aL^b", "onSheet": True},
              {"name": "Marginal products", "tex": r"MP_K = aK^{a-1}L^b,\qquad MP_L = bK^aL^{b-1}", "onSheet": True},
              {"name": "With a constant A in front", "tex": r"Q = AK^aL^b \;\Rightarrow\; MP_L = bAK^aL^{b-1}", "onSheet": False, "note": "Not printed on the sheet. A is just a multiplier, so it carries through the derivative."},
              {"name": "MRTS for Cobb-Douglas", "tex": r"MRTS = \frac{MP_L}{MP_K} = \frac{bK^aL^{b-1}}{aK^{a-1}L^b} = \frac{bK}{aL}", "onSheet": True, "note": "The sheet has MRTS = MP_L / MP_K. The simplified bK/(aL) comes from the exponent rules."}],
 "derivation": r"""Start with \(Q = K^aL^b\) and treat K as a constant. Power rule on \(L^b\): \(\frac{\partial Q}{\partial L} = K^a \cdot bL^{b-1}\).

MRTS simplification: divide \(bK^aL^{b-1}\) by \(aK^{a-1}L^b\). Same base, subtract exponents: \(K^{a-(a-1)} = K^1\) and \(L^{(b-1)-b} = L^{-1}\). So \(MRTS = \frac{b}{a}\cdot\frac{K}{L}\).""",
 "math": [EXPONENTS, PARTIAL],
 "worked": [{"title": "S15 slides p. 44", "problem": r"\(Q = K^{0.25}L^{0.75}\). Find \(MP_L\) and \(MP_K\) at \(K = 81\), \(L = 16\).",
   "steps": [r"\(MP_L = 0.75K^{0.25}L^{-0.25} = 0.75\,(K/L)^{0.25} = 0.75 \times (81/16)^{0.25} = 0.75 \times 1.5 = 1.125\).", r"\(MP_K = 0.25K^{-0.75}L^{0.75} = 0.25\,(L/K)^{0.75} = 0.25 \times (16/81)^{0.75}\).", r"\((16/81)^{0.25} = 2/3\), so \((16/81)^{0.75} = (2/3)^3 = 8/27 = 0.2963\). \(MP_K = 0.0741\)."],
   "answer": "MP_L = 1.125, MP_K = 0.0741."},
  {"title": "With a constant (Comprehension Quiz 7 Q4)", "problem": r"\(Q = 2K^{0.5}L^{0.5}\) with \(K = 9\). Find \(MP_L\) as a function of L.",
   "steps": [r"\(MP_L = 2 \times 0.5 \times K^{0.5}L^{-0.5} = K^{0.5}/L^{0.5}\).", r"With \(K = 9\): \(MP_L = 3/\sqrt{L}\). At \(L = 100\), \(MP_L = 0.3\)."],
   "answer": "MP_L = 3 / √L."}],
 "graph": [{"component": "isoquant", "params": {"form": "cd", "a": 0.5, "b": 0.5, "Q": 100, "L": 50}, "caption": "Cobb-Douglas isoquants (here Q = 2K^0.5 L^0.5) are convex. Slide the point right: the MRTS readout falls."},
           {"component": "production", "params": {"form": "cd", "A": 2, "K": 9, "alpha": 0.5, "beta": 0.5, "P": 400, "w": 120, "Lmax": 160}, "caption": "Short run with K fixed at 9: MP_L falls at every L (diminishing returns everywhere when b < 1)."}],
 "traps": ["a goes with K and b goes with L. Mixing them up gives MP_K when you wanted MP_L.",
           "Subtract 1 from the exponent of the input you differentiate, and leave the other input's exponent alone.",
           "If the function has a constant in front (2K^0.5 L^0.5), multiply the MP by it. The sheet formula has no constant.",
           "L^-0.25 means 1 / L^0.25, not -L^0.25.",
           "Cobb-Douglas is imperfect substitution. Perfect substitution is linear; no substitution is Leontief (Reading Quiz Q5)."],
 "sources": {"slides": "S15 Production I, pp. 32 to 44", "read": "Ch. 5 pp. 146 to 148", "exercise": "Production Functions workbook, Cobb-Douglas tab", "quiz": "Reading Quiz Q5; Comprehension Quiz 7 Q4, Q6"}},

{"id": "S15-10", "title": "Profit-maximizing input usage", "calc": True,
 "plain": r"""How many workers should you hire? Use the rule the slides use for studying: keep going while the **marginal benefit** of one more unit is at least its **marginal cost**, and stop where they are equal.
$$MB = MC \;\Rightarrow\; P \times MP_L = w \;\Rightarrow\; VMP_L = w$$
The marginal benefit of a worker is the value of what they add, \(VMP_L\). The marginal cost is the wage \(w\).

**From a table.** Compute \(VMP_L\) for each worker and hire every worker whose VMP is at least the wage, stopping at the last one where \(VMP \ge w\) on the downward part of the VMP column. J Dawgs: price $4, wage $8, VMPs are $28, $48, $56, $52, $36, $8, then negative. The 6th worker's VMP is exactly $8 = w, so hire **6 workers** (the professor's answer). A 7th would add -$32 of value and cost $8.

**From a formula.** Write \(MP_L\), set \(P \times MP_L = w\), solve for L. Herman Miller (Quiz 7 Q4): \(Q = 2K^{0.5}L^{0.5}\), \(K = 9\), \(P = 400\), \(w = 120\). \(MP_L = 3/\sqrt{L}\), so \(400 \times 3/\sqrt{L} = 120\), \(\sqrt{L} = 10\), \(L = 100\).""",
 "why": "This is the first thing the professor says he will ask: use a production function to calculate the profit-maximizing amount of an input. It also appears in Reading Quiz Q4, Quiz 7 Q3 and Q4, and the practice exam (Q2, Q17).",
 "definition": "A manager maximizes profit with respect to an input by using it up to the point where its value marginal product equals its price: \\(VMP_L = w\\) for labor.",
 "formulas": [{"name": "Profit-maximizing labor", "tex": r"VMP_L = P \times MP_L = w", "onSheet": False, "note": "Not on the sheet. MP_L itself is on the sheet."},
              {"name": "Profit-maximizing capital", "tex": r"VMP_K = P \times MP_K = r", "onSheet": False},
              {"name": "Short-run Cobb-Douglas shortcut (b < 1, K fixed)", "tex": r"L^* = \left(\frac{P\,b\,A\,K^a}{w}\right)^{\frac{1}{1-b}}", "onSheet": False, "note": "Only a check. Solving P × MP_L = w step by step is what the exam rewards."}],
 "derivation": r"""Profit from labor is \(\pi = P \cdot Q(L) - wL - \text{fixed costs}\). Adding one worker changes revenue by \(P \times MP_L\) and cost by \(w\). If \(P \times MP_L > w\), the worker adds more than they cost: hire. If \(P \times MP_L < w\): do not. Profit is highest where they are equal. With calculus: \(\frac{d\pi}{dL} = P\frac{dQ}{dL} - w = 0\).

Fixed costs (like the $8,000 Herman Miller already spent on equipment) are sunk. They do not change \(VMP_L\) or \(w\), so they do not change the hiring decision.""",
 "math": [POWER, {"title": "Solving an equation with a square root", "body": r"Isolate the root, then square both sides. \(\frac{1200}{\sqrt{L}} = 120\). Multiply both sides by \(\sqrt{L}\): \(1200 = 120\sqrt{L}\). Divide by 120: \(\sqrt{L} = 10\). Square: \(L = 100\)."}],
 "worked": [{"title": "J Dawgs (professor's solution)", "problem": "Hot dogs sell for $4.00 and the wage is $8.00. How many workers should J Dawgs hire?\n\n" + JD_MD,
   "steps": ["VMP column (4 × MP): $28, $48, $56, $52, $36, $8, -$32, -$84.", "Hire while VMP ≥ $8 on the falling part of the column.", "Worker 6: VMP = $8 = wage. Worker 7: VMP = -$32 < $8."],
   "answer": "6 workers. With six workers VMP (MB) and the wage (MC) are both $8."},
  {"title": "Herman Miller chairs (Comprehension Quiz 7 Q4)", "problem": r"\(Q = 2K^{0.5}L^{0.5}\), K fixed at 9, chairs sell for $400, wage $120 per day. Profit-maximizing labor?",
   "steps": [r"\(MP_L = 2(0.5)K^{0.5}L^{-0.5} = 3/\sqrt{L}\) with K = 9.", r"\(VMP_L = 400 \times 3/\sqrt{L} = 1200/\sqrt{L}\).", r"Set equal to the wage: \(1200/\sqrt{L} = 120\), so \(\sqrt{L} = 10\).", r"\(L = 100\). The $8,000 already spent on equipment is sunk and does not matter."],
   "answer": "100 workers (worker-days)."},
  {"title": "Wage rises at J Dawgs", "problem": "Same table, but the wage is $40. How many workers?",
   "steps": ["VMPs: $28, $48, $56, $52, $36, $8.", "Worker 1 has VMP $28 < $40, but that is in the increasing-returns range: workers 2 to 4 more than pay for themselves, so do not stop at 0.", "On the falling part: worker 4 VMP $52 ≥ $40, worker 5 VMP $36 < $40."],
   "answer": "4 workers. A higher wage means fewer workers."}],
 "graph": {"component": "production", "params": {"form": "table", "table": JD_TABLE, "P": 4, "w": 8}, "caption": "Raise the wage: L* falls. Raise the price of hot dogs: VMP rises and L* rises."},
 "traps": ["Set VMP = w, not MP = w. Quiz 7 Q3 has P = $1 so they look the same; with any other price they differ.",
           "Sunk or fixed costs (equipment already bought) do not change how many workers to hire.",
           "If the answer is a square root, square it. In the Herman Miller problem 10 is the square root of L; L = 100.",
           "Use the falling part of the VMP column. A low VMP for the very first worker (increasing returns) is not a reason to hire nobody.",
           "Do not hire to the point where total product peaks. That ignores the wage."],
 "sources": {"slides": "S15 Production I, p. 30", "read": "Ch. 5 pp. 142 to 145", "exercise": "J Dawgs question 4", "quiz": "Reading Quiz Q4; Comprehension Quiz 7 Q3, Q4"}},

{"id": "S15-11", "title": "Comparing linear, Leontief and Cobb-Douglas", "calc": False,
 "plain": r"""The slides compare the three production functions side by side. Learn this table; most conceptual questions about the three forms come straight from it.

""" + COMPARE + r"""

How to tell which one a business story describes:
- **Linear (perfect substitutes):** one input can fully replace the other at a fixed rate. "A robot does the work of 3 workers, always." Constant marginal products.
- **Leontief (no substitution):** inputs must be combined in a fixed ratio. "One pilot per plane." Extra of one input alone adds nothing.
- **Cobb-Douglas (imperfect substitutes):** you can trade one input for the other, but it gets harder the further you push it. Both inputs are needed and each has diminishing marginal product.""",
 "why": "Exams ask you to match a function to its isoquant shape, MRTS behavior, or substitutability, and to recognize the right form in a business scenario.",
 "definition": "Linear: perfect substitutes, straight-line isoquant, constant MRTS. Cobb-Douglas: imperfect substitutes, convex isoquant, MRTS that changes. Leontief: no substitution, L-shaped isoquant, MRTS undefined.",
 "formulas": [{"name": "Linear", "tex": r"Q = aK + bL,\quad MRTS = \frac{b}{a}", "onSheet": True},
              {"name": "Cobb-Douglas", "tex": r"Q = K^aL^b,\quad MRTS = \frac{bK}{aL}", "onSheet": True},
              {"name": "Leontief", "tex": r"Q = \min(aK, bL),\quad MRTS\ \text{undefined}", "onSheet": False}],
 "derivation": "",
 "math": [],
 "worked": [{"title": "Classify the technology", "problem": "A trucking firm needs exactly one driver for each truck. A bakery can swap one dough mixer for 2 bakers at any scale. A farm uses land and labor, and the more labor it adds to a fixed plot, the less each extra worker adds. Which production function fits each?",
   "steps": ["Trucking: fixed one-to-one ratio, no substitution. Leontief, Q = min(K, L).", "Bakery: a constant trade rate between inputs. Linear, Q = aK + bL with a = 2b.", "Farm: substitution is possible and each input shows diminishing marginal product. Cobb-Douglas."],
   "answer": "Leontief, linear, Cobb-Douglas."}],
 "graph": {"component": "isoquant", "params": {"form": "cd", "a": 0.5, "b": 0.5, "Q": 100, "L": 50}, "caption": "Use the Function menu to switch between linear, Leontief and Cobb-Douglas and compare isoquant shapes and MRTS."},
 "traps": ["Linear is PERFECT substitution, not 'some' substitution. Cobb-Douglas is the 'some, but not perfect' one.",
           "Leontief has NO substitution. Its isoquant is L-shaped, not a straight line.",
           "Only Cobb-Douglas has an MRTS that changes along the isoquant. Linear is constant; Leontief is undefined.",
           "Fixed proportions is another name for Leontief."],
 "sources": {"slides": "S15 Production I, pp. 32 to 35", "read": "Ch. 5 pp. 146 to 148", "exercise": "Production Functions workbook", "quiz": "Reading Quiz Q5; Comprehension Quiz 7 Q5"}},
]
for L in LESSONS: write_lesson(L)
write_session("S15", {"overview": "Session 15 is the short run of production: capital is fixed and the only choice is how much labor to use. You learn the production function, then the three productivity measures computed from it (total, average and marginal product), the pattern of increasing, diminishing and negative marginal returns, and the hiring rule VMP = wage. The session ends with the three algebraic forms (linear, Leontief, Cobb-Douglas) and how they differ in substitutability. Production is about a quarter of Midterm 2, and the professor lists the profit-maximizing input calculation first among the things he will ask. VMP and the hiring rule are not on the equation sheet, so they must be memorized; MP, AP and the Cobb-Douglas marginal products are on it."})
print("lessons", [L["id"] for L in LESSONS])
