from common import *

JD_L = list(range(9)); JD_Q = [0, 7, 19, 33, 46, 55, 57, 49, 28]          # J Dawgs, professor's workbook
JD_TABLE = [[l, q] for l, q in zip(JD_L, JD_Q)]
jd_rows = []
for l in JD_L:
    q = JD_Q[l]
    mp = "" if l == 0 else JD_Q[l] - JD_Q[l - 1]
    ap = "" if l == 0 else fmt(q / l)
    vmp = "" if l == 0 else f"${4 * mp}"
    jd_rows.append([l, q, mp, ap, vmp, "$8"])
JD_MD = table(["Workers L", "Hot dogs Q", "MP_L", "AP_L", "VMP_L = $4 × MP_L", "Wage"], jd_rows)
STUDY_MD = table(["Hours", "Grade", "MP (extra points)", "Marginal returns"],
                 [[0, 40, "", ""], [1, 50, 10, "Increasing"], [2, 62, 12, "Increasing"], [3, 80, 18, "Increasing"], [4, 90, 10, "Diminishing"],
                  [5, 95, 5, "Diminishing"], [6, 97, 2, "Diminishing"], [7, 98, 1, "Diminishing"], [8, 97, -1, "Negative"], [9, 95, -2, "Negative"], [10, 90, -5, "Negative"]])

SRC = {"slides": "S15 Production I, pp. 19 to 30", "read": "Ch. 5 pp. 138 to 148", "exercise": "J Dawgs"}
POWER = {"title": "The power rule for derivatives", "body": r"A derivative is the slope of a function: how much the output changes when the input rises a tiny bit. For a power of \(x\), bring the exponent down in front and subtract one from it: $$\frac{d}{dx}x^n = n x^{n-1}$$ A constant multiplier stays: \(\frac{d}{dx} 5x^3 = 15x^2\). A plain constant has slope 0. Example: \(Q = 4L^2 + 3.5L\) gives \(\frac{dQ}{dL} = 8L + 3.5\)."}
PARTIAL = {"title": "Partial derivatives: hold the other input fixed", "body": r"With two inputs, \(\frac{\partial Q}{\partial L}\) means: take the derivative with respect to \(L\) and treat \(K\) as an ordinary number. Example: \(Q = K^{0.5}L^{0.5}\). Treat \(K^{0.5}\) like the 5 in \(5L^{0.5}\): $$\frac{\partial Q}{\partial L} = K^{0.5}\cdot 0.5L^{-0.5} = \frac{0.5K^{0.5}}{L^{0.5}}$$"}
EXPONENTS = {"title": "Exponent rules (S15 slides pp. 36 to 42)", "body": r"""- Multiply, same base: add exponents. \(a^x a^y = a^{x+y}\)
- Divide, same base: subtract. \(\frac{a^x}{a^y} = a^{x-y}\)
- Power of a product: \((xy)^a = x^a y^a\)
- Power of a quotient: \(\left(\frac{x}{y}\right)^a = \frac{x^a}{y^a}\)
- Power of a power: multiply. \((a^x)^y = a^{xy}\)
- Zero power: \(x^0 = 1\)
- Negative power is a reciprocal: \(x^{-a} = \frac{1}{x^a}\), so \(L^{-0.5} = \frac{1}{\sqrt{L}}\)
- Fractional power is a root: \(x^{0.5} = \sqrt{x}\), \(x^{0.25} = \sqrt[4]{x}\)

On a calculator: \(16^{0.25}\) is 16, then the \(y^x\) or ^ key, then 0.25. Answer 2."""}
TABLE_MP = {"title": "Marginal product from a table", "body": "Subtract the row above from the current row. The MP of the 4th worker is Q(4) minus Q(3). There is no MP for the first row (L = 0) because nothing came before it. Write MP on the row of the worker who caused the change."}

LESSONS = [
{"id": "S15-01", "title": "Production function", "calc": False,
 "plain": r"""A business turns **inputs** into **output**. A hot dog stand turns grills (capital) and workers (labor) into hot dogs. A **production function** is the rule that says how much output you can get from a given amount of inputs:
$$Q = f(K, L)$$
\(Q\) is output, \(K\) is units of capital (machines, grills, buildings), \(L\) is units of labor (workers or hours). The function stands for the **technology**: the recipe for turning inputs into output.

The word that matters is **maximum**. The production function gives the most output possible from those inputs, assuming nobody wastes effort. A real firm can produce less than that by being sloppy. The manager's first job is to get the firm onto the production function.

**Short run versus long run.** In the short run at least one input is fixed. J Dawgs has 2 grills and cannot add a third this afternoon, so capital is fixed at \(K = 2\) and the only choice is how many workers to hire. In the long run every input can change: the firm can buy more grills, build a bigger stand, or change the mix of capital and labor. Session 15 is mostly short run (choose \(L\) with \(K\) fixed). Session 16 is the long run (choose the best mix of \(K\) and \(L\)).""",
 "why": "The slides list three jobs for a strategist. Short run: (1) operate at maximum efficiency, which means producing on the production function, and (2) use the right amount of each input. Long run: (3) use the optimal mix of inputs. Every later calculation in production starts from the production function.",
 "definition": "A production function defines the relationship between inputs and outputs: the maximum level of output that can be produced with a given amount of inputs, written \\(Q = f(K, L)\\).",
 "formulas": [{"name": "Production function", "tex": r"Q = f(K, L)", "onSheet": False, "note": r"K = units of capital, L = units of labor. The sheet lists specific forms (linear, Cobb-Douglas) but not this general definition."}],
 "derivation": "",
 "math": [],
 "worked": [{"title": "Reading a production function", "problem": r"J Dawgs' production function with 2 grills is \(Q = -0.5L^3 + 4L^2 + 3.5L\). How many hot dogs can 3 workers make? Is this short run or long run?",
   "steps": [r"Plug in \(L = 3\): \(-0.5(27) + 4(9) + 3.5(3) = -13.5 + 36 + 10.5\).", r"\(Q = 33\) hot dogs. This matches the professor's J Dawgs table.", "Capital is fixed at 2 grills, so this is the short run. Only labor can change."],
   "answer": "33 hot dogs, short run."}],
 "graph": {"component": "production", "params": {"form": "cubic", "a": 3.5, "b": 4, "c": 0.5, "P": 4, "w": 8}, "caption": r"J Dawgs as a smooth curve: \(Q = -0.5L^3 + 4L^2 + 3.5L\) with 2 grills. Each point on the top curve is the maximum output for that many workers. The readout L* uses calculus on the smooth curve, so it says 5.51; the professor's table answer is 6 whole workers."},
 "traps": ["The production function is the MAXIMUM output, not any output, not the output per worker (that is average product), and not the change from one more worker (that is marginal product).",
           "It is not a cost function. The minimum cost of producing a given output is a different idea (Session 16, cost minimization).",
           "Short run means at least one input is fixed, not a specific number of months. If the question says capital cannot change, it is the short run.",
           "In \\(Q = f(K, L)\\), K is capital and L is labor. Do not swap them when you take derivatives later."],
 "sources": {"slides": "S15 Production I, pp. 19, 20, 22", "read": "Ch. 5 pp. 138 to 140", "exercise": "J Dawgs (capital fixed at 2 grills)", "quiz": "Reading Quiz Q1; Comprehension Quiz 7 Q4"}},

{"id": "S15-02", "title": "Total product", "calc": True,
 "plain": r"""**Total product** is just output: the number of units the firm produces, \(Q\). In a table it is the output column. On a graph it is the height of the production curve.

The slides' running example is studying for an exam. Hours of study are the input and your grade is the total product:

""" + STUDY_MD + r"""

The grade rises quickly at first, flattens out, and after 7 hours it actually falls because you are exhausted. Total product can go **down** when you add too much of one input while the others stay fixed. Picture 8 workers crowded around J Dawgs' 2 grills: they get in each other's way and output drops from 57 to 28.

**Where total product peaks.** Total product is highest at the point where one more unit of input adds nothing: where marginal product hits zero. Before that point each unit adds output; after it, each unit subtracts output.""",
 "why": "Total product is the starting column for every production table. Average product, marginal product and value marginal product are all computed from it.",
 "definition": "Total product (Q) is the maximum level of output that can be produced with a given amount of inputs.",
 "formulas": [{"name": "Total product", "tex": r"TP = Q = f(K, L)", "onSheet": False, "note": "Read straight from the table or plug the input into the production function."}],
 "derivation": r"Total product is highest where marginal product equals zero. Each unit of input changes total product by its marginal product, so total product keeps rising while MP is positive and starts falling once MP is negative. With calculus: set \(\frac{dQ}{dL} = 0\).",
 "math": [],
 "worked": [{"title": "J Dawgs total product", "problem": "Using the J Dawgs table below, what is total product with 5 workers, and how many workers give the most hot dogs?\n\n" + JD_MD,
   "steps": ["Total product at L = 5 is the Q column: 55 hot dogs.", "Scan the Q column for the largest value: 57 at L = 6.", "Check with marginal product: the 6th worker adds 2 (still positive), the 7th adds -8 (negative). Output peaks at 6."],
   "answer": "Q = 55 with 5 workers. Total product peaks at 57 hot dogs with 6 workers."}],
 "graph": {"component": "production", "params": {"form": "table", "table": JD_TABLE, "P": 4, "w": 8}, "caption": "The J Dawgs table from the professor's workbook. The top panel is total product."},
 "traps": ["Total product is output, not output per worker. If a question asks for output per worker, that is average product.",
           "Total product can fall. Do not assume more workers always means more output.",
           "The maximum of total product is where MP = 0, not where MP is at its maximum and not where AP is at its maximum.",
           "Profit is usually maximized BEFORE total product peaks, because workers cost money. Do not hire to the TP peak unless labor is free."],
 "sources": {"slides": "S15 Production I, pp. 21, 23 to 29", "read": "Ch. 5 pp. 140 to 142", "exercise": "J Dawgs", "quiz": "Comprehension Quiz 7 Q1 to Q3"}},

{"id": "S15-03", "title": "Average product", "calc": True,
 "plain": r"""**Average product** is output per unit of input. For labor:
$$AP_L = \frac{Q}{L}$$
It is a productivity measure: how many hot dogs each worker makes on average. With 4 workers J Dawgs makes 46 hot dogs, so \(AP_L = 46/4 = 11.5\) per worker.

**How AP moves.** Average product rises when the newest worker is more productive than the current average, and falls when the newest worker is less productive. This is the same logic as your GPA: a class grade above your GPA pulls it up, a grade below pulls it down. So:
- If \(MP > AP\), AP is rising.
- If \(MP < AP\), AP is falling.
- MP crosses AP at the top (maximum) of AP.

In J Dawgs, the 4th worker adds 13, more than the average of 11 with three workers, so AP rises to 11.5. The 5th worker adds only 9, below 11.5, so AP falls to 11.""",
 "why": "Average product tells a manager how productive the workforce is on average. It is on the equation sheet. Exams ask you to compute it from a table or a function and to know how it relates to marginal product.",
 "definition": "Average product is the output produced per unit of input: \\(AP_L = Q/L\\).",
 "formulas": [{"name": "Average product of labor", "tex": r"AP_L = \frac{Q}{L}", "onSheet": True},
              {"name": "Average product of capital", "tex": r"AP_K = \frac{Q}{K}", "onSheet": True, "note": "The sheet writes it for any input I: AP_I = Q / I."}],
 "derivation": r"Why MP crosses AP at AP's peak: adding a worker whose output is above the current average must raise the average, and one below must lower it. The average stops rising exactly when the newest worker's output equals the average. That is the top of AP.",
 "math": [],
 "worked": [{"title": "J Dawgs average product", "problem": "Compute average product for 2, 4 and 6 workers. Where is AP highest?\n\n" + JD_MD,
   "steps": [r"\(AP(2) = 19/2 = 9.5\)", r"\(AP(4) = 46/4 = 11.5\)", r"\(AP(6) = 57/6 = 9.5\)", "Scan the AP column: the largest is 11.5 at L = 4.", "Check: the 4th worker's MP (13) is above the old AP (11), the 5th worker's MP (9) is below 11.5. AP peaks at 4."],
   "answer": "AP = 9.5, 11.5 and 9.5. Average product is highest at 4 workers."}],
 "graph": {"component": "production", "params": {"form": "cubic", "a": 3.5, "b": 4, "c": 0.5, "P": 4, "w": 8}, "caption": "Middle panel: MP (yellow) crosses AP (green) at the top of AP. Drag b or c and watch the crossing stay at AP's peak. The readout L* uses calculus on the smooth curve, so it says 5.51; the professor's table answer is 6 whole workers."},
 "traps": ["AP is total output divided by the number of workers, not the change from the last worker. Using the MP column when the question asks for AP is the most common mistake.",
           "Use the total Q at that L, not the Q of the last worker only.",
           "AP falls while MP is still positive. Falling AP does not mean output is falling.",
           "AP is maximized where MP = AP, not where MP is maximized and not where Q is maximized."],
 "sources": {"slides": "S15 Production I, pp. 21, 27", "read": "Ch. 5 pp. 140 to 142", "exercise": "J Dawgs"}},

{"id": "S15-04", "title": "Marginal product", "calc": True,
 "plain": r"""**Marginal product** is the extra output from one more unit of an input, holding the other inputs fixed. "Marginal" in economics always means "the next one" or "the last one".

From a table, subtract: the marginal product of the 4th J Dawgs worker is \(Q(4) - Q(3) = 46 - 33 = 13\) hot dogs.

From a formula, take the derivative: \(MP_L = \frac{\partial Q}{\partial L}\), the slope of the total product curve. The equation sheet gives the ready-made results for the two common forms:
- Linear \(Q = aK + bL\): \(MP_K = a\), \(MP_L = b\). Constant.
- Cobb-Douglas \(Q = K^aL^b\): \(MP_K = aK^{a-1}L^b\), \(MP_L = bK^aL^{b-1}\).

**MP and TP.** MP is the slope of TP. When MP is positive, TP rises. When MP is zero, TP is at its peak. When MP is negative, TP falls.""",
 "why": "Marginal product drives every decision in this unit. Hiring stops where the value of the last worker's marginal product equals the wage (S15-10). The cost minimizing mix compares marginal product per dollar (Session 16).",
 "definition": "Marginal product is the change in total output attributable to the last unit of an input: \\(MP_L = \\Delta Q / \\Delta L\\) or \\(\\partial Q / \\partial L\\).",
 "formulas": [{"name": "Marginal product (general)", "tex": r"MP_I = \frac{\Delta Q}{\Delta I} = \frac{\partial Q}{\partial I}", "onSheet": True},
              {"name": "Linear production function", "tex": r"Q = aK + bL \;\Rightarrow\; MP_K = a,\; MP_L = b", "onSheet": True},
              {"name": "Cobb-Douglas", "tex": r"Q = K^aL^b \;\Rightarrow\; MP_K = aK^{a-1}L^b,\; MP_L = bK^aL^{b-1}", "onSheet": True}],
 "derivation": r"For a cubic like J Dawgs, \(Q = -0.5L^3 + 4L^2 + 3.5L\), the calculus version is \(MP_L = -1.5L^2 + 8L + 3.5\). The professor's J Dawgs solution uses the table difference instead (Q(L) minus Q(L-1)). When a question gives a table, subtract. When it gives a Cobb-Douglas or linear function, use the sheet formula. The two methods give slightly different numbers for a curved function because the difference measures the whole step from L-1 to L.",
 "math": [TABLE_MP, POWER, PARTIAL],
 "worked": [{"title": "From a table (Comprehension Quiz 7 setup)", "problem": "Labor 0 to 6 produces output 0, 50, 150, 300, 400, 450, 475. What is the MP of labor at L = 4?",
   "steps": ["MP at L = 4 is the change from L = 3 to L = 4.", r"\(MP_L = 400 - 300 = 100\)", "400 is total product, not marginal product."], "answer": "100 units."},
  {"title": "From a Cobb-Douglas function (S15 slides p. 44)", "problem": r"\(Q = K^{0.25}L^{0.75}\). Find \(MP_L\), then evaluate at \(K = 16\), \(L = 81\).",
   "steps": [r"Sheet formula: \(MP_L = bK^aL^{b-1} = 0.75K^{0.25}L^{-0.25}\).", r"Rewrite the negative exponent: \(MP_L = 0.75\left(\frac{K}{L}\right)^{0.25}\).", r"\(16^{0.25} = 2\) and \(81^{0.25} = 3\), so \(MP_L = 0.75 \times \frac{2}{3} = 0.5\)."],
   "answer": "MP_L = 0.5 units of output per extra unit of labor."}],
 "graph": {"component": "production", "params": {"form": "cubic", "a": 3.5, "b": 4, "c": 0.5, "P": 4, "w": 8}, "caption": "MP is the slope of the top curve. Where TP is steepest, MP is highest. Where TP is flat at its peak, MP is zero. The readout L* uses calculus on the smooth curve, so it says 5.51; the professor's table answer is 6 whole workers."},
 "traps": ["MP is the CHANGE in output, not the output itself. Quiz 7 lists 400 (total product) as a wrong choice.",
           "The MP of the 4th worker uses rows 3 and 4, not rows 4 and 5.",
           "When taking \\(\\partial Q/\\partial L\\) treat K as a constant. Do not differentiate K.",
           "In Cobb-Douglas, a is the exponent on K and b is on L. MP_L uses b, not a.",
           "Diminishing marginal product does not mean negative marginal product. Output still rises, just by less."],
 "sources": {"slides": "S15 Production I, pp. 21, 26 to 29, 43, 44", "read": "Ch. 5 pp. 140 to 142, 146 to 148", "exercise": "J Dawgs", "quiz": "Reading Quiz Q2; Comprehension Quiz 7 Q1"}},

{"id": "S15-05", "title": "Increasing, diminishing and negative marginal returns", "calc": True,
 "plain": r"""As you add more of one input to a fixed amount of the others, marginal product follows a typical pattern. The slides name three ranges:

- **Increasing marginal returns:** each new unit adds MORE than the one before. MP is rising. Early workers specialize and help each other.
- **Diminishing (decreasing) marginal returns:** each new unit still adds output, but LESS than the one before. MP is falling but not negative. The fixed input (the 2 grills) starts to limit what extra workers can do.
- **Negative marginal returns:** a new unit REDUCES output. MP is below zero. Too many workers crowd the grills.

Studying example from the slides:

""" + STUDY_MD + r"""

**How the professor labels the ranges.** In the J Dawgs solution the MPs are 7, 12, 14, 13, 9, 2, -8, -21 for workers 1 to 8, and the answer is: increasing 0 to 3, decreasing 4 to 6, negative greater than 6. Comprehension Quiz 7 uses the same idea: MPs of 50, 100, 150, then 100, 50, 25, 0, then negative, so diminishing returns is labor 4 to 7. A worker who adds exactly 0 counts as diminishing, not negative.""",
 "why": "Diminishing marginal returns is why a firm cannot just keep adding workers to a fixed plant. It is the reason the marginal product curve slopes down in the range where firms actually operate, and so the reason VMP = wage has a unique answer.",
 "definition": "Increasing marginal returns: the range of input usage over which marginal product increases. Diminishing marginal returns: the range over which marginal product declines. Negative marginal returns: the range over which marginal product is negative.",
 "formulas": [{"name": "Classify each unit by comparing MPs", "tex": r"MP_n > MP_{n-1} \Rightarrow \text{increasing};\quad 0 \le MP_n < MP_{n-1} \Rightarrow \text{diminishing};\quad MP_n < 0 \Rightarrow \text{negative}", "onSheet": False}],
 "derivation": "",
 "math": [TABLE_MP],
 "worked": [{"title": "J Dawgs ranges", "problem": "Classify each J Dawgs worker.\n\n" + JD_MD,
   "steps": ["MP column for workers 1 to 8: 7, 12, 14, 13, 9, 2, -8, -21.", "Workers 1 to 3: each adds more than the one before (7, 12, 14). Increasing.", "Workers 4 to 6: MP falls (13, 9, 2) but stays positive. Diminishing.", "Workers 7 and 8: MP is negative (-8, -21). Negative."],
   "answer": "Increasing marginal returns for L from 0 to 3, diminishing for 4 to 6, negative for more than 6 (the professor's solution)."}],
 "graph": {"component": "production", "params": {"form": "cubic", "a": 3.5, "b": 4, "c": 0.5, "P": 4, "w": 8}, "caption": "Shaded bands mark increasing, diminishing and negative marginal returns. Diminishing returns begin where MP peaks, not where TP peaks. The readout L* uses calculus on the smooth curve, so it says 5.51; the professor's table answer is 6 whole workers."},
 "traps": ["Diminishing returns starts when MP starts FALLING, not when total product starts falling. Output still rises during diminishing returns.",
           "A unit with MP exactly 0 is diminishing, not negative (Quiz 7 counts L = 7 with MP 0 as diminishing).",
           "Ranges are ranges of the INPUT (labor 4 to 7), not ranges of output (400 to 475). Quiz 7 uses output ranges as wrong choices.",
           "Diminishing marginal returns is about adding one input while others are fixed. It is not the same as decreasing returns to scale, which is about growing all inputs together."],
 "sources": {"slides": "S15 Production I, pp. 25 to 29", "read": "Ch. 5 pp. 141 to 142", "exercise": "J Dawgs question 2", "quiz": "Reading Quiz Q3; Comprehension Quiz 7 Q2"}},

{"id": "S15-06", "title": "Value marginal product", "calc": True,
 "plain": r"""Marginal product counts the extra output in units (hot dogs). A manager compares that with the wage, which is in dollars. To compare like with like, turn the extra output into dollars by multiplying by the price of the product:
$$VMP_L = P \times MP_L$$
That is the **value marginal product of labor**: the dollar value of what the last worker produces. At J Dawgs a hot dog sells for $4 and the 3rd worker adds 14 hot dogs, so that worker's \(VMP_L = 4 \times 14 = \$56\).

In the professor's J Dawgs table VMP is labeled MB, the marginal benefit of a worker, and the wage is labeled MC, the marginal cost of a worker.""",
 "why": "VMP is the marginal benefit side of the hiring decision. Hire while the value a worker adds is at least what the worker costs.",
 "definition": "Value marginal product is the value of the output produced by the last unit of an input: \\(VMP_L = P \\times MP_L\\).",
 "formulas": [{"name": "Value marginal product of labor", "tex": r"VMP_L = P \times MP_L", "onSheet": False},
              {"name": "Value marginal product of capital", "tex": r"VMP_K = P \times MP_K", "onSheet": False}],
 "derivation": r"Each extra worker adds \(MP_L\) units, and each unit sells for \(P\) dollars, so the worker adds \(P \times MP_L\) dollars of revenue. This assumes the firm can sell all it makes at the going price P.",
 "math": [],
 "worked": [{"title": "J Dawgs VMP column", "problem": "Hot dogs sell for $4. Compute VMP for workers 1 to 6.\n\n" + JD_MD,
   "steps": ["Multiply each MP by $4.", "Worker 1: 4 × 7 = $28. Worker 2: 4 × 12 = $48. Worker 3: 4 × 14 = $56.", "Worker 4: 4 × 13 = $52. Worker 5: 4 × 9 = $36. Worker 6: 4 × 2 = $8."],
   "answer": "VMP = $28, $48, $56, $52, $36, $8, matching the professor's solution."}],
 "graph": {"component": "production", "params": {"form": "table", "table": JD_TABLE, "P": 4, "w": 8}, "caption": "Bottom panel: VMP (purple) against the wage (red). Change the price P and the whole VMP curve stretches up or down."},
 "traps": ["VMP multiplies MP by the PRICE of output, not by the wage and not by total product.",
           "VMP is not total revenue. Total value of output is P × Q; VMP is P × MP.",
           "VMP is not on the equation sheet. Memorize it.",
           "A higher product price raises VMP for every worker, so the firm hires more. A higher wage does not change VMP at all; it changes the cost side."],
 "sources": {"slides": "S15 Production I, p. 30", "read": "Ch. 5 pp. 142 to 145", "exercise": "J Dawgs questions 3 and 4", "quiz": "Reading Quiz Q4; Comprehension Quiz 7 Q3"}},
]

for L in LESSONS: write_lesson(L)
print("lessons", [L["id"] for L in LESSONS])
