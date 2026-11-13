from common import *
from S15_lessons import EXPONENTS, PARTIAL

DIM = table(["Point", "Q", "L", "K", "ΔL", "ΔK", "MRTS = ΔK/ΔL"], [["A", 100, 4, 3, "", "", ""], ["B", 100, 3, 4, -1, 1, -1], ["C", 100, 2, 6, -1, 2, -2], ["D", 100, 1, 9, -1, 3, -3]])
BANG = table(["(L, K)", "MP_L", "MP_K", "w", "r", "MP_L / w", "MP_K / r"], [["25, 4", 2, 12.5, 40, 10, 0.050, 1.250], ["10, 10", 5, 5, 40, 10, 0.125, 0.500], ["5, 20", 10, 2.5, 40, 10, 0.250, 0.250]])
SOLVE_K = {"title": "Solving an equation for K", "body": r"To graph an isoquant you rewrite \(Q = AK^aL^b\) as K in terms of L. Divide both sides by \(AL^b\): \(K^a = \frac{Q}{AL^b}\). Then undo the exponent \(a\) by raising both sides to \(1/a\): $$K = \left(\frac{Q}{AL^b}\right)^{1/a}$$ For \(a = 0.5\), \(1/a = 2\): square. For \(a = 0.25\), \(1/a = 4\): raise to the 4th power."}
TWO_EQ = {"title": "Two equations, two unknowns, by substitution", "body": r"Cost minimization gives two equations: the tangency condition (like \(K = 4L\)) and the output target (like \(10K^{0.5}L^{0.5} = 100\)). Substitute the first into the second so only L is left: \(10(4L)^{0.5}L^{0.5} = 10 \times 2 \times L = 20L = 100\), so \(L = 5\). Then go back: \(K = 4 \times 5 = 20\)."}
SLOPE = {"title": "Slope and intercepts of a line", "body": r"A line \(K = m L + c\) has slope \(m\) (rise over run) and vertical intercept \(c\) (the value of K when L = 0). The horizontal intercept is where \(K = 0\). For the isocost \(K = \frac{C}{r} - \frac{w}{r}L\): slope \(-\frac{w}{r}\), vertical intercept \(\frac{C}{r}\), horizontal intercept \(\frac{C}{w}\)."}

LESSONS = [
{"id": "S16-01", "title": "Isoquants", "calc": True,
 "plain": r"""In the long run a manager can change both capital and labor. Usually there are many ways to make the same output: lots of machines and few workers, or few machines and lots of workers. An **isoquant** ("iso" = same, "quant" = quantity) is the line that connects every combination of K and L that gives the **same** output.

Draw it with labor on the horizontal axis and capital on the vertical axis. Facts to know:
- Each isoquant is one output level. **Isoquants farther from the origin mean more output.** Closer to the origin means less (Reading Quiz Q3 is a false statement saying the opposite).
- Shape depends on the production function: straight line for linear, convex curve for Cobb-Douglas, L-shape for Leontief.
- An isoquant does NOT show different output levels; along one isoquant output is constant (Reading Quiz Q1).

**Graphing an isoquant (S16 slides pp. 24 to 25).** Fix Q at the target and solve the production function for K. With \(Q = 2K^{0.5}L^{0.5}\) and Q = 100:
$$100 = 2K^{0.5}L^{0.5} \;\Rightarrow\; K^{0.5} = \frac{100}{2L^{0.5}} = \frac{50}{L^{0.5}} \;\Rightarrow\; K = \frac{2500}{L}$$
Points on it: (L, K) = (25, 100), (50, 50), (100, 25).""",
 "why": "The isoquant shows a manager every way to hit a production target. Choosing the cheapest point on it is cost minimization (S16-05). Comprehension Quiz 7 Q6 asks you to write the isoquant equation.",
 "definition": "An isoquant is a line that defines the combinations of inputs that yield the same level of output.",
 "formulas": [{"name": "Cobb-Douglas isoquant solved for K", "tex": r"K = \left(\frac{Q}{AL^b}\right)^{1/a}", "onSheet": False, "note": "Derive it: plug in the target Q and solve the production function for K."},
              {"name": "Linear isoquant", "tex": r"K = \frac{Q - bL}{a}", "onSheet": False},
              {"name": "Leontief isoquant corner", "tex": r"L = \frac{Q}{b},\; K = \frac{Q}{a}", "onSheet": False}],
 "derivation": r"Comprehension Quiz 7 Q6: \(Q = 4K^{0.25}L^{0.75}\), target 400. Divide by 4: \(100 = K^{0.25}L^{0.75}\). Divide by \(L^{0.75}\): \(K^{0.25} = 100/L^{0.75}\). Raise to the 4th power: \(K = (100/L^{0.75})^4\).",
 "math": [SOLVE_K, EXPONENTS],
 "worked": [{"title": "Graphing the slide isoquant", "problem": r"\(Q = 2K^{0.5}L^{0.5}\), target Q = 100. How much capital is needed with L = 20? With L = 125?",
   "steps": [r"Isoquant: \(K = 2500/L\) (solved above).", r"L = 20: \(K = 2500/20 = 125\).", r"L = 125: \(K = 2500/125 = 20\).", r"Check: \(2\sqrt{125}\sqrt{20} = 2\sqrt{2500} = 2(50) = 100\)."], "answer": "K = 125 with 20 workers; K = 20 with 125 workers."}],
 "graph": {"component": "isoquant", "params": {"form": "cd", "a": 0.5, "b": 0.5, "Q": 100, "L": 50}, "caption": r"Q = 2K^0.5 L^0.5. The blue curve is Q = 100: K = 2500/L. The lighter curves are higher output, farther from the origin."},
 "traps": ["Isoquants farther from the origin are HIGHER output. Closer to the origin is less.",
           "An isoquant holds output constant. It does not show different output levels.",
           "When solving for K, divide by the constant in front first. Quiz 7 Q6 offers (400/L^0.75)^4, which forgets to divide by 4.",
           "Use the exponent on L inside and 1/(exponent on K) outside. Quiz 7 Q6 offers L^0.25, the exponent on capital, as a wrong choice."],
 "sources": {"slides": "S16 Production II, pp. 8 to 12, 24 to 26", "read": "Ch. 5 pp. 148 to 150", "exercise": "Production Functions workbook; Klarna production exercise Q4", "quiz": "Reading Quiz Q1, Q3; Comprehension Quiz 7 Q6"}},

{"id": "S16-02", "title": "Marginal rate of technical substitution (MRTS)", "calc": True,
 "plain": r"""Moving along an isoquant means giving up some of one input and making up for it with the other. The **marginal rate of technical substitution** says at what rate: how many units of capital one more unit of labor can replace while output stays the same.
$$MRTS_{KL} = \frac{MP_L}{MP_K}$$
It is the **absolute value of the slope** of the isoquant (Reading Quiz Q2: both the substitution rate and the absolute slope). The slides write it as \(MP_L / MP_K = \partial K / \partial L \approx \Delta K / \Delta L\).

Why the ratio of marginal products: one more worker adds \(MP_L\) units. To keep output fixed you must drop that many units' worth of capital, which is \(MP_L / MP_K\) units of K.

By production function:
- Linear: \(MRTS = b/a\), constant.
- Cobb-Douglas: \(MRTS = \frac{bK}{aL}\), changes along the isoquant.
- Leontief: undefined.

Example: \(Q = K^{0.5}L^{0.5}\) at K = 20, L = 5 gives \(MRTS = K/L = 4\): one more worker can replace 4 units of capital.""",
 "why": "The MRTS is the slope that cost minimization compares with the input price ratio w/r (S16-05).",
 "definition": "The MRTS is the rate at which a producer can substitute between two inputs and maintain the same level of output. It equals MP_L / MP_K, the absolute value of the slope of the isoquant.",
 "formulas": [{"name": "MRTS", "tex": r"MRTS_{KL} = \frac{MP_L}{MP_K}", "onSheet": True},
              {"name": "Cobb-Douglas MRTS", "tex": r"MRTS = \frac{bK^aL^{b-1}}{aK^{a-1}L^b} = \frac{bK}{aL}", "onSheet": False, "note": "The ratio MP_L/MP_K is on the sheet; the simplified bK/(aL) you derive with exponent rules."},
              {"name": "Linear MRTS", "tex": r"MRTS = \frac{b}{a}", "onSheet": False}],
 "derivation": r"Along an isoquant output does not change: \(MP_L\,\Delta L + MP_K\,\Delta K = 0\). Rearranged: \(-\frac{\Delta K}{\Delta L} = \frac{MP_L}{MP_K}\). The left side is the absolute slope of the isoquant.",
 "math": [EXPONENTS],
 "worked": [{"title": "Cobb-Douglas MRTS", "problem": r"\(Q = K^{0.25}L^{0.75}\). Find the MRTS at K = 30, L = 10.",
   "steps": [r"\(MRTS = \frac{bK}{aL} = \frac{0.75 \times 30}{0.25 \times 10}\).", r"\(= \frac{22.5}{2.5} = 9\)."], "answer": "MRTS = 9: one more unit of labor replaces 9 units of capital at this point."},
  {"title": "Linear MRTS (Comprehension Quiz 7 Q5)", "problem": r"\(Q = 4K + L\). MRTS at K = 1, L = 4?", "steps": [r"\(MP_L = 1\), \(MP_K = 4\).", r"\(MRTS = 1/4\), at every point."], "answer": "1/4."}],
 "graph": {"component": "isoquant", "params": {"form": "cd", "a": 0.5, "b": 0.5, "Q": 100, "L": 50}, "caption": "The dashed line is tangent to the isoquant; its slope (absolute value) is the MRTS. Slide the point to see the MRTS change."},
 "traps": ["MRTS is MP_L / MP_K, not MP_K / MP_L. Labor on top.",
           "MRTS is about substituting INPUTS while holding OUTPUT constant, not substituting outputs (Reading Quiz Q2 distractor).",
           "The slope of the isoquant is negative; the MRTS is its absolute value.",
           "For linear production the MRTS does not depend on K and L.",
           "In bK/(aL) keep a with K and b with L: b (labor's exponent) goes on top with K."],
 "sources": {"slides": "S16 Production II, pp. 13 to 15", "read": "Ch. 5 pp. 149 to 150", "exercise": "Production Functions workbook", "quiz": "Reading Quiz Q2; Comprehension Quiz 7 Q5"}},

{"id": "S16-03", "title": "Law of diminishing MRTS", "calc": False,
 "plain": r"""The S16 slides define it this way: for every unit decrease in one input of production, increasing amounts of another input must be employed to produce the same level of output.

Slides' table (all points make Q = 100):

""" + DIM + r"""

Going from A to D, each time labor drops by one unit, it takes 1, then 2, then 3 extra units of capital to keep output at 100. Read the other way (moving right along the isoquant), each extra worker replaces less and less capital. That is a falling MRTS.

**Why it happens (slide p. 19): diminishing marginal returns.** As you pile on capital, each extra unit of capital adds less output, so you need more and more capital to replace each worker you remove.

**Which functions have it.** Cobb-Douglas does: its isoquant is convex (bowed toward the origin) and \(MRTS = bK/(aL)\) falls as L rises and K falls. Linear does not: its MRTS is constant. Leontief does not: its MRTS is undefined.""",
 "why": "Diminishing MRTS is what makes isoquants convex, so the tangency with the isocost line is a true minimum. It also explains why firms rarely go all-in on one input.",
 "definition": "Law of diminishing MRTS: for every unit decrease in one input of production, increasing amounts of another input must be employed to produce the same level of output. Equivalently, the MRTS falls as you move down and to the right along an isoquant.",
 "formulas": [{"name": "MRTS between two points", "tex": r"MRTS \approx \left|\frac{\Delta K}{\Delta L}\right|", "onSheet": False}],
 "derivation": r"For Cobb-Douglas, \(MRTS = \frac{bK}{aL}\). Moving right along the isoquant, L rises and K falls, so the ratio K/L falls and the MRTS falls.",
 "math": [],
 "worked": [{"title": "Reading the slides' table", "problem": "Using the table above, how much capital does it take to replace the 2nd unit of labor (going from C at L = 2 to D at L = 1)? Compare it with replacing the 4th unit (A to B).",
   "steps": ["C to D: K goes from 6 to 9, so 3 units of capital replace one unit of labor.", "A to B: K goes from 3 to 4, so 1 unit of capital replaces one unit of labor.", "The fewer workers you have, the more capital it takes to replace another one."],
   "answer": "3 units versus 1 unit: diminishing MRTS."}],
 "graph": {"component": "isoquant", "params": {"form": "cd", "a": 0.5, "b": 0.5, "Q": 100, "L": 20}, "caption": "Move the point to the right along the convex isoquant: the tangent gets flatter and the MRTS readout falls. Switch to Linear: the MRTS stays constant."},
 "traps": ["Diminishing MRTS is a property of convex (Cobb-Douglas) isoquants, not of linear or Leontief ones.",
           "It does not mean output is falling. Output is constant along the isoquant.",
           "The cause the slides give is diminishing marginal returns to the input being added."],
 "sources": {"slides": "S16 Production II, pp. 16 to 19", "read": "Ch. 5 pp. 149 to 150", "exercise": "Production Functions workbook"}},

{"id": "S16-04", "title": "Isocost lines", "calc": True,
 "plain": r"""An **isocost** line shows every combination of inputs that costs the same total amount. Total cost is labor cost plus capital cost:
$$C = wL + rK$$
\(w\) is the wage (price of labor) and \(r\) is the rental rate (price of capital). To graph it with K on the vertical axis, solve for K (slides p. 28):
$$K = \frac{C}{r} - \frac{w}{r}L$$
- **Vertical intercept** \(C/r\): the most capital the budget buys if you hire no labor.
- **Horizontal intercept** \(C/w\): the most labor if you use no capital.
- **Slope** \(-w/r\) (on the equation sheet).

**How it moves** (slides pp. 30 to 34, budget $1,000, w = $10, r = $25):
- Max labor = 1000/10 = 100 hours, max capital = 1000/25 = 40 machine hours, slope = -0.4.
- Budget up 50% to $1,500: parallel shift out (intercepts 150 and 60, same slope). Budget down: parallel shift in.
- Wage doubles to $20: max labor falls to 50, max capital stays 40. The line pivots around the vertical intercept and gets steeper (slope -0.8).
- Wage falls: horizontal intercept moves out, line flatter (Quiz 7 Q9).
- Rental rate rises: vertical intercept falls, slope gets flatter in magnitude (Reading Quiz Q5).""",
 "why": "The isocost is the cost side of the long-run decision. The cheapest way to make a target output is on the lowest isocost that still touches the isoquant.",
 "definition": "An isocost is a line that defines the combinations of inputs that will cost the producer the same amount of money: C = wL + rK.",
 "formulas": [{"name": "Isocost equation", "tex": r"C = wL + rK", "onSheet": False},
              {"name": "Solved for K", "tex": r"K = \frac{C}{r} - \frac{w}{r}L", "onSheet": False},
              {"name": "Slope of the isocost", "tex": r"-\frac{w}{r}", "onSheet": True},
              {"name": "Intercepts", "tex": r"L_{max} = \frac{C}{w},\qquad K_{max} = \frac{C}{r}", "onSheet": False}],
 "derivation": r"From \(C = wL + rK\): subtract wL, \(rK = C - wL\); divide by r, \(K = C/r - (w/r)L\).",
 "math": [SLOPE],
 "worked": [{"title": "Slides pp. 30 to 34", "problem": "Budget $1,000, w = $10, r = $25. Find the intercepts and slope. Then the wage doubles to $20: what changes?",
   "steps": ["Max labor = C/w = 1000/10 = 100. Max capital = C/r = 1000/25 = 40.", "Slope = -w/r = -10/25 = -0.4.", "Wage $20: max labor = 1000/20 = 50, max capital still 40, slope = -20/25 = -0.8 (steeper)."],
   "answer": "Intercepts 100 (L) and 40 (K), slope -0.4. After the wage doubles: 50 and 40, slope -0.8."}],
 "graph": {"component": "costmin", "params": {"A": 2, "a": 0.5, "b": 0.5, "Q": 100, "w": 10, "r": 25, "L": 60}, "caption": "Drag w and r and watch the green isocost pivot. A change in C alone (the target Q here) shifts it in parallel."},
 "traps": ["The slope is -w/r, not -r/w. The wage is on top when L is on the horizontal axis.",
           "Max labor is C/w (horizontal intercept); max capital is C/r (vertical intercept). Do not swap them.",
           "A budget change shifts the line in parallel. A price change rotates it around the OTHER input's intercept.",
           "When w falls the line gets FLATTER and the horizontal intercept moves OUT; the vertical intercept does not change (Quiz 7 Q9)."],
 "sources": {"slides": "S16 Production II, pp. 27 to 34", "read": "Ch. 5 pp. 150 to 151", "exercise": "Cost Minimization exercise", "quiz": "Reading Quiz Q4, Q5; Comprehension Quiz 7 Q9"}},

{"id": "S16-05", "title": "The cost-minimizing input rule", "calc": True,
 "plain": r"""To make a target output at the lowest cost, pick the point on the isoquant that touches the lowest possible isocost. At that point the two lines are **tangent**, so their slopes match:
$$MRTS = \frac{MP_L}{MP_K} = \frac{w}{r}$$
Rearranged, this is the professor's **"bang for the buck"** rule: the marginal product per dollar must be the same for every input.
$$\frac{MP_L}{w} = \frac{MP_K}{r}$$

**Using it.** Compute both ratios.
- Equal: you are cost minimizing.
- \(MP_K/r > MP_L/w\): a dollar on capital buys more output than a dollar on labor. Use **more capital and less labor**.
- \(MP_L/w > MP_K/r\): use **more labor and less capital**.

As you shift toward an input its marginal product falls (diminishing returns), so the ratios move toward each other until they are equal.

**In-class exercise.** Labor costs $12/hour and the last worker made 84 rollers; capital rents for $15/hour with MP_K = 120. \(MP_L/w = 84/12 = 7\), \(MP_K/r = 120/15 = 8\). Not equal, so not cost minimizing. Capital gives more bang for the buck: **increase capital**.

**Slides' table** (\(Q = 10K^{0.5}L^{0.5}\), Q = 100, w = $40, r = $10):

""" + BANG + r"""

Only (L, K) = (5, 20) has equal ratios, and it is the cheapest: $40(5) + $10(20) = $400, versus $500 at (10, 10) and $1,040 at (25, 4).""",
 "why": "The professor lists it among the things he will ask: find an isocost and the MRTS, compare marginal product per dollar, and find the cost-minimizing input mix. Quiz 7 Q7 and Q8 and practice exam Q4, Q18 and Q19 use it.",
 "definition": "To minimize the cost of production, a firm should employ inputs so that the MRTS (slope of the isoquant) equals the ratio of input prices (slope of the isocost): MP_L / MP_K = w / r, or equivalently MP_L / w = MP_K / r.",
 "formulas": [{"name": "Tangency form", "tex": r"\frac{MP_L}{MP_K} = \frac{w}{r}", "onSheet": False, "note": "The sheet has MRTS = MP_L / MP_K and the isocost slope -w/r, but not the rule that sets them equal."},
              {"name": "Bang for the buck", "tex": r"\frac{MP_L}{w} = \frac{MP_K}{r}", "onSheet": False}],
 "derivation": r"Suppose \(MP_K/r = 8\) and \(MP_L/w = 7\). Move $1 from labor to capital: you lose 7 units of output and gain 8, so output rises with the same budget. Equivalently, you can make the same output for less money. You keep moving until no switch helps, which is when the two ratios are equal.",
 "math": [],
 "worked": [{"title": "In-class exercise (professor's solution)", "problem": "w = $12, MP_L = 84 rollers/hour, r = $15, MP_K = 120 rollers/hour. Is the firm cost minimizing? What should it do?",
   "steps": [r"\(MP_L/w = 84/12 = 7\) rollers per dollar.", r"\(MP_K/r = 120/15 = 8\) rollers per dollar.", "7 ≠ 8, so the firm is not minimizing cost.", "Capital gives more output per dollar, so shift spending toward capital."],
   "answer": "No. Increase capital (and use less labor)."},
  {"title": "Comprehension Quiz 7 Q7 and Q8", "problem": "w = $10, r = $25, MP_L = 40, MP_K = 125. Cost minimizing? Increase or decrease capital?",
   "steps": [r"\(40/10 = 4\), \(125/25 = 5\).", "Not equal: not cost minimizing.", "Capital's ratio is higher: increase capital."], "answer": "No; increase capital."}],
 "graph": {"component": "costmin", "params": {"A": 10, "a": 0.5, "b": 0.5, "Q": 100, "w": 40, "r": 10, "L": 10}, "caption": "The slides' setup: Q = 10K^0.5 L^0.5 = 100, w = $40, r = $10. Move the trial point: the readout compares MP_L/w and MP_K/r and names the cheaper direction. The minimum is L = 5, K = 20, cost $400."},
 "traps": ["Compare marginal product PER DOLLAR, not raw marginal products. MP_K = 120 > MP_L = 84 alone does not decide anything.",
           "If MP_K/r is bigger, use MORE capital. Students often flip the direction.",
           "MP_L/MP_K = w/r is the same condition as MP_L/w = MP_K/r. Both are correct forms.",
           "The rule is not on the equation sheet. Only the MRTS formula and the isocost slope are."],
 "sources": {"slides": "S16 Production II, pp. 35 to 40", "read": "Ch. 5 pp. 151 to 153", "exercise": "Cost Minimization exercise (rollers); Klarna exercise Q5", "quiz": "Comprehension Quiz 7 Q7, Q8"}},

{"id": "S16-06", "title": "Optimal input substitution", "calc": True,
 "plain": r"""When an input's price changes, the cheapest way to make the same output changes too. The firm **substitutes toward the input that became relatively cheaper**.
- Wage falls: \(MP_L/w\) rises, labor is a better deal, so use **more labor and less capital** (Quiz 7 Q10). The isocost gets flatter and touches the isoquant further right.
- Rental rate rises: use **less capital and more labor** (in-class exercise, question 3).

**Solving for the cost-minimizing mix with Cobb-Douglas.** For \(Q = AK^aL^b\):
1. Tangency: \(\frac{MP_L}{MP_K} = \frac{bK}{aL} = \frac{w}{r}\), so \(K = \frac{a\,w}{b\,r}L\).
2. Substitute into the output target and solve for L.
3. Get K from step 1, then cost \(C = wL + rK\).

Slides' example: \(Q = 10K^{0.5}L^{0.5} = 100\), w = $40, r = $10.
1. \(K = \frac{0.5 \times 40}{0.5 \times 10}L = 4L\).
2. \(10(4L)^{0.5}L^{0.5} = 10 \times 2L = 20L = 100\), so L = 5.
3. K = 20, C = 40(5) + 10(20) = $400.

If the rental rate rises to $40: \(K = L\), \(10L = 100\), L = 10 and K = 10. Capital fell from 20 to 10 and labor rose from 5 to 10. Cost is now $800.

**Other production functions.**
- Linear: no tangency. Compare \(MP_L/w = b/w\) with \(MP_K/r = a/r\) and use only the input with the higher ratio (a corner).
- Leontief: no substitution at all. Use \(L = Q/b\) and \(K = Q/a\) whatever the prices; cost is \(wQ/b + rQ/a\).""",
 "why": "Firms react to wage and price changes by changing their input mix, for example replacing labor with automation when wages rise. Practice exam Q18 and Reading Quiz Q5 test the direction.",
 "definition": "Optimal input substitution: to minimize the cost of producing a given output, a firm uses more of an input whose relative price has declined and less of an input whose relative price has increased.",
 "formulas": [{"name": "Cobb-Douglas tangency path", "tex": r"\frac{bK}{aL} = \frac{w}{r} \;\Rightarrow\; K = \frac{a\,w}{b\,r}\,L", "onSheet": False},
              {"name": "Total cost at the optimum", "tex": r"C^* = wL^* + rK^*", "onSheet": False},
              {"name": "Linear: corner rule", "tex": r"\text{use only K if } \frac{a}{r} > \frac{b}{w},\ \text{only L if } \frac{b}{w} > \frac{a}{r}", "onSheet": False},
              {"name": "Leontief cost", "tex": r"C = w\frac{Q}{b} + r\frac{Q}{a}", "onSheet": False}],
 "derivation": r"With a = b = 0.5 the tangency path is \(K = (w/r)L\). Substitute into \(Q = AK^{0.5}L^{0.5}\): \(Q = A\sqrt{w/r}\,L\), so \(L^* = \frac{Q}{A\sqrt{w/r}}\) and \(K^* = \frac{w}{r}L^*\).",
 "math": [TWO_EQ, EXPONENTS],
 "worked": [{"title": "Price change", "problem": r"\(Q = 2K^{0.5}L^{0.5}\), target Q = 200, w = $16, r = $4. Find L*, K* and cost. Then w falls to $4.",
   "steps": [r"Tangency: \(K = (w/r)L = 4L\).", r"\(2\sqrt{4L \cdot L} = 2 \times 2L = 4L = 200\), so \(L = 50\), \(K = 200\).", "Cost = 16(50) + 4(200) = 800 + 800 = $1,600.", r"w = $4: \(K = L\), \(2L = 200\), L = 100, K = 100, cost = 4(100) + 4(100) = $800.", "Cheaper labor: labor rises from 50 to 100 and capital falls from 200 to 100."],
   "answer": "L* = 50, K* = 200, C = $1,600. After the wage falls: L* = 100, K* = 100, C = $800."}],
 "graph": {"component": "costmin", "params": {"A": 10, "a": 0.5, "b": 0.5, "Q": 100, "w": 40, "r": 10, "L": 5}, "caption": "Raise r from 10 to 40: the tangency point slides from (L 5, K 20) to (L 10, K 10). The firm substitutes labor for the now pricier capital."},
 "traps": ["When an input gets MORE expensive, use LESS of it and more of the other one.",
           "A wage cut makes the isocost flatter, so the tangency moves to MORE labor, not more capital (Quiz 7 Q10).",
           "With a ≠ b, K = (a w)/(b r) L. Do not drop the exponent ratio.",
           "Linear production gives a corner: all of the input with the higher MP per dollar, none of the other.",
           "Leontief ignores prices when choosing the mix: the ratio is fixed."],
 "sources": {"slides": "S16 Production II, pp. 35 to 40", "read": "Ch. 5 pp. 153 to 156 (Figure 5-10)", "exercise": "Cost Minimization exercise question 3; Klarna exercise Q5", "quiz": "Reading Quiz Q5; Comprehension Quiz 7 Q9, Q10"}},
]
for L in LESSONS: write_lesson(L)
write_session("S16", {"overview": "Session 16 is the long run of production, when both capital and labor can change. An isoquant shows every input mix that makes the same output, and the MRTS is its slope: how much capital one more worker replaces. The isocost line shows every mix that costs the same. The cheapest way to make a target output is where they touch, which gives the bang-for-the-buck rule MP_L/w = MP_K/r. When an input's price changes, the firm substitutes toward the cheaper input. The professor will ask you to find an isocost and the MRTS, compare marginal product per dollar, and find the cost-minimizing mix by hand. The sheet has MRTS = MP_L/MP_K and the isocost slope -w/r; the cost-minimizing rule itself must be memorized."})
print([L["id"] for L in LESSONS])
