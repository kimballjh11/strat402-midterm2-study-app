from common import *
B = Bank()

def mp(Q): return [None] + [Q[i] - Q[i - 1] for i in range(1, len(Q))]
def tbl(L, Q, extra=None):
    rows = [[l, q] for l, q in zip(L, Q)]
    return table(["Labor (L)", "Output (Q)"], rows)

# Data sets (original, clean numbers)
BL = list(range(9)); BQ = [0, 10, 25, 45, 60, 70, 75, 76, 74]          # bakery
CL = list(range(8)); CQ = [0, 8, 20, 36, 48, 56, 60, 58]                # car wash
WL = list(range(7)); WQ = [0, 3, 8, 12, 15, 17, 18]                      # lawn care
JL = list(range(9)); JQ = [0, 7, 19, 33, 46, 55, 57, 49, 28]             # J Dawgs (professor)
BT, CT, WT, JT = tbl(BL, BQ), tbl(CL, CQ), tbl(WL, WQ), tbl(JL, JQ)
def V(f, L, Q, **k): return dict(f=f, L=L, Q=Q, **k)

# ---------------- S15-01 production function ----------------
lo = "S15-01"
B.mc(lo, [lo], "concept", "Which statement best describes a production function?",
     ["It gives the maximum output that can be produced from a given set of inputs", "It gives the minimum cost of producing each level of output", "It gives the output each worker produces on average", "It gives the revenue earned from each unit of input"], 0,
     "A production function is the maximum output possible from given inputs, Q = f(K, L). Minimum cost is a cost function (Session 16). Output per worker is average product. Revenue from an input is value marginal product.")
B.mc(lo, [lo], "concept", "In the production function \\(Q = f(K, L)\\), what do K and L stand for?",
     ["K is units of capital and L is units of labor", "K is the wage and L is the rental rate of capital", "K is output and L is labor", "K is the number of firms and L is the number of products"], 0,
     "K is capital (machines, grills, buildings) and L is labor (workers or hours), as defined on the S15 slides. The wage and rental rate are prices of inputs, written w and r.")
B.mc(lo, [lo], "concept", "What distinguishes the short run from the long run in production?",
     ["In the short run at least one input is fixed; in the long run all inputs can be changed", "The short run is less than one year and the long run is more than one year", "In the short run all inputs are variable; in the long run capital is fixed", "In the short run output is fixed; in the long run inputs are fixed"], 0,
     "Short run means some input (usually capital) cannot be changed right now. Long run means every input can be adjusted. It is defined by flexibility, not by a calendar length. The other choices reverse the definitions or confuse output with inputs.",
     trap="Short run is not a specific number of months.")
B.tf(lo, [lo], "concept", "True or false: A production function shows the output a firm actually produces, even if its workers are wasting effort.", False,
     "False. The production function is the MAXIMUM output possible from given inputs. A firm wasting effort produces below its production function. Getting the firm onto the production function is the manager's first short-run job.")
B.mc(lo, [lo], "concept", "According to the S15 slides, which is a strategist's LONG-run production task?",
     ["Ensure the firm uses the optimal mix of inputs", "Ensure the firm operates at its maximum level of efficiency", "Ensure the firm uses the correct level of the variable input", "Ensure the firm sells at the highest possible price"], 0,
     "The slides list short-run tasks as (1) operate at maximum efficiency and (2) use the correct level of inputs, and the long-run task as (3) use the optimal mix of inputs. Pricing is not one of the production tasks.")
B.tf(lo, [lo], "concept", "True or false: A production function describes the technology the firm uses to turn inputs into outputs.", True,
     "True. The slides define production as transforming inputs into outputs through some technology, and the production function summarizes that technology.")
B.mc(lo, [lo], "concept", "A production function holds capital fixed at 2 units and lets labor vary. This describes:",
     ["A short-run production decision", "A long-run production decision", "A cost function", "A demand function"], 0,
     "With one input fixed, the firm is in the short run and chooses only labor. Long run would let capital change too. Cost and demand functions are different relationships.")
B.mc(lo, [lo], "apply", "J Dawgs has two grills and cannot add a third before the lunch rush. Its only choice today is how many workers to schedule. Which statement is correct?",
     ["J Dawgs is making a short-run decision because capital is fixed", "J Dawgs is making a long-run decision because labor can change", "J Dawgs cannot use a production function because capital is fixed", "J Dawgs should choose the mix of grills and workers that minimizes cost"], 0,
     "Capital (grills) is fixed, so this is the short run, which is exactly the J Dawgs exercise setup. A production function still applies with K fixed. Choosing the mix of grills and workers is the long-run problem.")
B.mc(lo, [lo], "apply", "A furniture maker is designing a new plant that will open in three years and can choose any number of machines and workers. This is:",
     ["A long-run decision, because all inputs are variable", "A short-run decision, because the plant is not built yet", "A short-run decision, because labor is variable", "Neither, because no output is produced yet"], 0,
     "When every input, including capital, can be chosen, the firm is in the long run. Labor being variable is true in both runs, so it does not make this short run.")
B.mc(lo, [lo], "apply", "Two coffee shops have identical baristas and espresso machines, but shop A serves 300 drinks a day and shop B serves 220 because its baristas are disorganized. Which statement is best?",
     ["Shop B is producing below its production function", "Shop B has a different production function because its output is lower", "Shop A is producing above its production function", "Both shops are on the production function because they use the same inputs"], 0,
     "The production function is the maximum output from those inputs. With the same inputs and technology, B's lower output means it is operating inefficiently, below the function. No firm can produce above its production function.")
B.mc(lo, [lo], "apply", "A manager says, 'Our production function tells us how to price our product.' What is wrong with this statement?",
     ["A production function relates inputs to output; it says nothing about prices", "Nothing; production functions set prices", "A production function only applies in the long run", "A production function only measures labor, not capital"], 0,
     "A production function is a technical relationship between inputs and output. Prices come from demand and market structure. It applies in both runs and includes capital and labor.")
B.mc(lo, [lo], "apply", "Which change would move a firm from the short run into the long run?",
     ["It becomes able to buy or sell machines, not just change its staffing", "It hires two more workers", "It raises its price", "It produces more output with the same inputs"], 0,
     "The long run is when every input, including capital, can be changed. Hiring workers is a short-run change in the variable input. Raising price or producing more is not about which inputs are variable.")

# ---------------- S15-02 total product ----------------
lo = "S15-02"
B.mc(lo, [lo], "concept", "Total product is:", ["The maximum level of output produced with a given amount of inputs", "Output per unit of labor", "The change in output from the last worker", "Total revenue from all units sold"], 0,
     "Total product is Q, the output itself. Output per worker is AP, the change from the last worker is MP, and revenue is price times quantity.")
B.mc(lo, [lo, "S15-04"], "concept", "Total product reaches its maximum where:", ["Marginal product equals zero", "Marginal product is at its maximum", "Average product is at its maximum", "Marginal product equals average product"], 0,
     "Output keeps rising while each extra unit adds something (MP > 0) and falls once MP < 0, so TP peaks where MP = 0. MP is largest where TP is steepest, and MP = AP marks the top of AP, not TP.",
     trap="MP max, AP max and TP max happen at three different input levels, in that order.")
B.tf(lo, [lo], "concept", "True or false: Adding more workers to a fixed amount of capital can reduce total product.", True,
     "True. With negative marginal returns, extra workers crowd the fixed capital and output falls. J Dawgs output drops from 57 with 6 workers to 28 with 8.")
B.tf(lo, [lo], "concept", "True or false: A firm maximizes profit by hiring labor until total product is as large as possible.", False,
     "False. Workers cost money, so the firm stops where VMP = wage, which is before total product peaks unless labor is free.")
B.mc(lo, [lo], "concept", "In the slides' studying example, grade is the total product. What is the input?", ["Hours of study", "Grade points per hour", "The extra points from the last hour", "The exam's difficulty"], 0,
     "Hours studied is the input and the grade is the output. Grade per hour would be average product and extra points from the last hour is marginal product.")
B.num(lo, [lo], "Use the table.\n\n" + BT + "\n\nWhat is total product with 4 workers?", 60,
      "Total product is the Q column at L = 4: 60 units. It is not 60 / 4 (average product, 15) and not 60 - 45 (marginal product, 15).", V("table_q", BL, BQ, at=4), unit="units")
B.num(lo, [lo], "Use the table.\n\n" + BT + "\n\nHow many workers maximize total product?", 7,
      "Scan Q for the largest value: 76 at L = 7. Check MP: the 7th worker adds 1 (positive), the 8th adds -2 (negative), so output peaks at 7.", V("tp_max", BL, BQ), unit="workers")
B.num(lo, [lo, "S15-01"], "A firm's production function with capital fixed is \\(Q = -L^3 + 9L^2 + 2L\\). What is total product with 5 workers?", -125 + 225 + 10,
      "Plug in L = 5: \\(-(5^3) + 9(5^2) + 2(5) = -125 + 225 + 10 = 110\\).", {"f": "poly_q", "coef": [0, 2, 9, -1], "at": 5}, unit="units")
B.mc(lo, [lo, "S15-04"], "apply", "A restaurant manager notices that adding a 9th cook to a kitchen with four burners caused the number of meals served to drop. What does this tell you?",
     ["The 9th cook's marginal product is negative and total product fell", "The 9th cook's marginal product is positive but smaller than the 8th cook's", "Average product must be rising", "Total product is at its maximum with 9 cooks"], 0,
     "If output drops when a cook is added, that cook's MP is negative, so TP fell. Positive but smaller MP would be diminishing returns with output still rising. AP falls when MP is below it, and TP peaked before the 9th cook.")
B.mc(lo, [lo], "apply", "A call center's output rises from 400 to 460 calls when it adds a 6th agent, then to 470 with a 7th. Which statement is true?",
     ["Total product is still rising, but each agent adds less", "Total product is falling", "The 7th agent has negative marginal product", "Total product is at its maximum with 6 agents"], 0,
     "Output went 400, 460, 470: still rising, so TP is not at a max and MP is positive. MP fell from 60 to 10, which is diminishing returns.")
B.mc(lo, [lo], "apply", "A farm doubles its workers on the same field and its harvest goes from 1,000 to 1,500 bushels. A consultant says this proves labor is unproductive. Best response?",
     ["Total product rose by 500, so the added workers were productive, though less than the first group", "The consultant is right because output did not double", "Total product fell", "Average product rose"], 0,
     "Total product rose, so the additional workers had positive marginal product. Output not doubling reflects diminishing returns, not unproductive labor. AP fell from 1,000/n to 1,500/(2n).")

# ---------------- S15-03 average product ----------------
lo = "S15-03"
B.mc(lo, [lo], "concept", "Average product of labor is:", ["Total output divided by the number of workers", "The change in output from the last worker", "The maximum output with given inputs", "Price times marginal product"], 0,
     "AP_L = Q / L (on the equation sheet). The change from the last worker is MP, maximum output is TP, and price times MP is VMP.")
B.mc(lo, [lo, "S15-04"], "concept", "When marginal product is greater than average product, average product is:", ["Rising", "Falling", "At its maximum", "Negative"], 0,
     "A new unit above the current average pulls the average up, like a class grade above your GPA. AP is at its maximum only where MP = AP, and it falls when MP < AP.")
B.mc(lo, [lo, "S15-04"], "concept", "Marginal product crosses average product:", ["At the maximum of average product", "At the maximum of total product", "At the maximum of marginal product", "Where marginal product is zero"], 0,
     "AP rises while MP > AP and falls while MP < AP, so it peaks where MP = AP. TP peaks where MP = 0, and MP peaks earlier, at the end of increasing returns.")
B.tf(lo, [lo], "concept", "True or false: If average product is falling, total product must be falling too.", False,
     "False. AP falls whenever MP < AP. MP can be below AP but still positive, so output keeps rising while the average falls. In J Dawgs, AP falls after 4 workers but Q rises until 6.")
B.tf(lo, [lo], "concept", "True or false: Average product of labor is on the Midterm 2 equation sheet.", True,
     "True. The sheet lists AP_I = Q / I for any input I.")
B.num(lo, [lo], "Use the table.\n\n" + BT + "\n\nWhat is the average product of labor with 3 workers?", 15,
      "AP = Q / L = 45 / 3 = 15 units per worker. Using 20 (the MP of the 3rd worker) is the classic mistake.", V("table_ap", BL, BQ, at=3), unit="units per worker")
B.num(lo, [lo], "Use the J Dawgs table from class.\n\n" + JT + "\n\nWhat is the average product of labor with 5 workers?", 11,
      "AP = 55 / 5 = 11 hot dogs per worker, matching the professor's solution sheet.", V("table_ap", JL, JQ, at=5), unit="hot dogs per worker")
B.num(lo, [lo], "Use the table.\n\n" + CT + "\n\nWhat is the average product of labor with 5 workers? Round to one decimal.", 11.2,
      "AP = 56 / 5 = 11.2 cars per worker.", V("table_ap", CL, CQ, at=5), unit="cars per worker")
B.num(lo, [lo], "Use the table.\n\n" + BT + "\n\nAt how many workers is average product highest? If two levels tie, give the larger.", 4,
      "AP: 10, 12.5, 15, 15, 14, 12.5, ... AP is 15 at both L = 3 and L = 4. The 4th worker's MP is 15, exactly equal to AP, which is where MP crosses AP at AP's top. The larger is 4.", V("ap_max", BL, BQ), unit="workers")
B.num(lo, [lo, "S15-09"], "\\(Q = K^{0.5}L^{0.5}\\) with K = 16 and L = 64. What is the average product of labor?", (16 ** 0.5 * 64 ** 0.5) / 64,
      "Q = √16 × √64 = 4 × 8 = 32. AP_L = Q / L = 32 / 64 = 0.5.", {"f": "cd_ap", "A": 1, "a": 0.5, "b": 0.5, "K": 16, "L": 64}, unit="units per worker")
B.mc(lo, [lo], "apply", "A team's average output is 20 widgets per worker. A new hire produces 12 extra widgets. What happens to the team's average product?",
     ["It falls, because the new worker's marginal product is below the average", "It rises, because output went up", "It stays at 20", "It becomes 12"], 0,
     "Output rises by 12, but 12 is below the average of 20, so the average falls. Rising output does not mean rising average.")
B.mc(lo, [lo], "apply", "A manager wants to report 'how productive our workers are on average this month.' Which measure fits?", ["Average product of labor", "Marginal product of labor", "Total product", "Value marginal product"], 0,
     "Average productivity across the workforce is Q / L. MP describes only the last worker; TP is total output; VMP is the dollar value of the last worker's output.")
B.mc(lo, [lo], "apply", "Store A sells 600 units with 10 workers; store B sells 700 with 14 workers. Which has the higher average product of labor?", ["Store A (60 per worker vs 50)", "Store B, because it sells more", "They are equal", "It cannot be computed without wages"], 0,
     "AP_A = 600 / 10 = 60, AP_B = 700 / 14 = 50. Higher total output does not mean higher AP. Wages are not needed for AP.")

# ---------------- S15-04 marginal product ----------------
lo = "S15-04"
B.mc(lo, [lo], "concept", "Marginal product of labor measures:", ["The change in total output from the last unit of labor", "Total output divided by labor", "The value of output from the last worker", "The maximum output for given labor"], 0,
     "MP_L = ΔQ / ΔL. Q / L is AP; P × MP is VMP; maximum output is total product.")
B.mc(lo, [lo], "concept", "Marginal product is the ______ of the total product curve.", ["Slope", "Height", "Average", "Area underneath"], 0,
     "MP = dQ/dL, the slope of TP. The height of TP is Q itself. Average is AP.")
B.tf(lo, [lo, "S15-05"], "concept", "True or false: If marginal product is falling, total product must be falling.", False,
     "False. Falling but positive MP (diminishing returns) still raises total product, just by less each time. TP falls only when MP is negative.")
B.tf(lo, [lo], "concept", "True or false: To find the marginal product of labor for a production function that includes capital, you treat capital as a constant while taking the derivative with respect to labor.", True,
     "True. MP_L is a partial derivative: hold K fixed and differentiate with respect to L.")
B.mc(lo, [lo, "S15-07"], "concept", "For \\(Q = aK + bL\\), the marginal product of labor is:", ["b", "bL", "a", "a + b"], 0,
     "The derivative of bL with respect to L is b, and aK does not change with L. bL is the contribution of all labor, not the marginal one.")
B.num(lo, [lo], "Use the table.\n\n" + BT + "\n\nWhat is the marginal product of the 5th worker?", 10,
      "MP of the 5th worker = Q(5) - Q(4) = 70 - 60 = 10. Using 70 (total product) or 14 (AP = 70/5) are the common errors.", V("table_mp", BL, BQ, at=5), unit="units")
B.num(lo, [lo], "Use the J Dawgs table.\n\n" + JT + "\n\nWhat is the marginal product of the 3rd worker?", 14,
      "MP = Q(3) - Q(2) = 33 - 19 = 14 hot dogs, matching the professor's MPL column.", V("table_mp", JL, JQ, at=3), unit="hot dogs")
B.num(lo, [lo], "Use the table.\n\n" + CT + "\n\nWhat is the marginal product of the 7th worker?", -2,
      "MP = Q(7) - Q(6) = 58 - 60 = -2. Negative: the 7th worker reduces output.", V("table_mp", CL, CQ, at=7), unit="cars")
B.num(lo, [lo, "S15-09"], "\\(Q = K^{0.5}L^{0.5}\\). What is \\(MP_L\\) at K = 25 and L = 4?", 0.5 * 25 ** 0.5 * 4 ** -0.5,
      "Sheet formula: \\(MP_L = bK^aL^{b-1} = 0.5K^{0.5}L^{-0.5} = 0.5\\sqrt{K}/\\sqrt{L} = 0.5 \\times 5 / 2 = 1.25\\).", {"f": "cd_mp", "A": 1, "a": 0.5, "b": 0.5, "K": 25, "L": 4, "wrt": "L"})
B.mc(lo, [lo], "apply", "A delivery company adds a 10th driver and deliveries rise from 940 to 990 per day. What is the 10th driver's marginal product?", ["50 deliveries", "990 deliveries", "99 deliveries", "94 deliveries"], 0,
     "MP = 990 - 940 = 50. 990 is total product, 99 is AP with 10 drivers, 94 is AP with the old 10 drivers' output divided wrongly.")
B.mc(lo, [lo], "apply", "A manager must choose which department gets one more employee. Which measure should guide the choice?", ["Marginal product (and its value) in each department", "Average product in each department", "Total product in each department", "The number of employees each department already has"], 0,
     "The decision is about ONE more worker, so the relevant number is that worker's added output (MP), ideally in dollars (VMP). A department with high average product may gain little from one more person.")
B.mc(lo, [lo], "apply", "Workers 1, 2 and 3 at a print shop add 30, 40 and 35 posters. A manager says, 'The 3rd worker is less productive than the 2nd, so we have negative returns.' Is this right?",
     ["No. MP fell but is still positive, which is diminishing, not negative, returns", "Yes, because MP fell", "Yes, because total product fell", "No, because MP is increasing"], 0,
     "Total product rose (30, 70, 105). MP fell from 40 to 35 but stayed positive, so this is diminishing marginal returns. Negative returns require MP < 0.")

# ---------------- S15-05 marginal returns ----------------
lo = "S15-05"
B.mc(lo, [lo], "concept", "Increasing marginal returns is the range of input usage over which:", ["Marginal product increases", "Total product increases", "Average product is positive", "Marginal product is positive but falling"], 0,
     "The slides define increasing marginal returns as MP rising. TP increases during both increasing and diminishing returns. MP positive but falling is diminishing returns.")
B.mc(lo, [lo], "concept", "Negative marginal returns is the range over which:", ["Marginal product is negative", "Marginal product is falling", "Average product is falling", "Total product is below its maximum"], 0,
     "Negative returns means each added unit reduces output: MP < 0. Falling MP alone is diminishing returns. AP falling happens whenever MP < AP.")
B.tf(lo, [lo], "concept", "True or false: Diminishing marginal returns means each additional worker reduces total output.", False,
     "False. Under diminishing returns each worker still adds output, just less than the previous one. Reducing output is negative returns.")
B.tf(lo, [lo], "concept", "True or false: Diminishing marginal returns happen because other inputs are held fixed while one input increases.", True,
     "True. With a fixed number of grills, each extra worker has less capital to work with, so their added output eventually falls.")
B.mc(lo, [lo], "concept", "A worker whose marginal product is exactly 0 is in the range of:", ["Diminishing marginal returns", "Negative marginal returns", "Increasing marginal returns", "None of the ranges"], 0,
     "Quiz 7 counts the worker with MP = 0 (L = 7) inside the diminishing range 4 to 7. Negative returns need MP below 0.")
B.num(lo, [lo], "Use the table.\n\n" + BT + "\n\nWhich worker is the FIRST to show diminishing marginal returns (MP lower than the previous worker's)?", 4,
      "MPs: 10, 15, 20, 15, 10, 5, 1, -2. MP rises through worker 3 (20) and falls at worker 4 (15). Diminishing returns begin with the 4th worker.", V("first_diminishing", BL, BQ), unit="th worker")
B.num(lo, [lo], "Use the table.\n\n" + CT + "\n\nWhich worker is the FIRST to show negative marginal returns?", 7,
      "MPs: 8, 12, 16, 12, 8, 4, -2. The first negative MP is the 7th worker's (-2).", V("first_negative", CL, CQ), unit="th worker")
B.num(lo, [lo], "Use the J Dawgs table.\n\n" + JT + "\n\nHow many workers are in the range of diminishing marginal returns (MP falling but not negative)?", 3,
      "MPs: 7, 12, 14, 13, 9, 2, -8, -21. Falling and nonnegative for workers 4, 5 and 6: three workers. The professor's answer: decreasing marginal returns = 4 to 6.", V("count_diminishing", JL, JQ), unit="workers")
B.num(lo, [lo], "Use the table.\n\n" + WT + "\n\nWhat is the LAST worker with increasing marginal returns?", 2,
      "MPs: 3, 5, 4, 3, 2, 1. MP rises from 3 to 5 at worker 2, then falls. Worker 2 is the last with increasing returns.", V("last_increasing", WL, WQ), unit="th worker")
B.mc(lo, [lo], "apply", "Use the table.\n\n" + BT + "\n\nOver what range of labor does the bakery have diminishing marginal returns?", ["4 to 7", "1 to 3", "60 to 76", "8 and above"], 0,
     "MPs for workers 4 to 7 are 15, 10, 5, 1: falling and positive. Workers 1 to 3 are increasing (10, 15, 20). 60 to 76 is a range of OUTPUT, not labor. Worker 8 is negative (-2).",
     trap="Answer with a range of the input, not of output.")
B.mc(lo, [lo], "apply", "A student's exam score rises 10, 12, then 18 points for the first three hours of study and 10, 5, 2 for the next three. When do diminishing returns to studying begin?", ["With the 4th hour", "With the 1st hour", "With the 3rd hour", "Only once the score starts to fall"], 0,
     "MP rises through hour 3 (18) and falls at hour 4 (10). That is the start of diminishing returns, as in the slides' studying table. The score is still rising, so this is not negative returns.")
B.mc(lo, [lo], "apply", "A warehouse keeps adding pickers to the same floor space. Eventually pickers block each other's aisles and total orders filled falls. This last stage is:", ["Negative marginal returns", "Diminishing marginal returns", "Increasing marginal returns", "Constant returns"], 0,
     "Output falling as pickers are added means MP < 0, negative marginal returns.")

# ---------------- S15-06 value marginal product ----------------
lo = "S15-06"
B.mc(lo, [lo], "concept", "Value marginal product of labor equals:", ["Price of output × marginal product of labor", "Wage × marginal product of labor", "Price of output × total product", "Wage ÷ marginal product of labor"], 0,
     "VMP_L = P × MP_L, the dollar value of what the last worker adds. Price times total product is total revenue (the J Dawgs 'total value of output'). The wage is the cost side, not part of VMP.")
B.tf(lo, [lo], "concept", "True or false: Value marginal product is on the equation sheet.", False, "False. The sheet has MP but not VMP. Memorize VMP_L = P × MP_L.")
B.mc(lo, [lo, "S15-10"], "concept", "In the J Dawgs solution, the VMP_L column is labeled MB. Why?", ["It is the marginal benefit of hiring one more worker", "It is the minimum benefit of the whole workforce", "It is the marginal budget for labor", "It is the benefit of the first worker only"], 0,
     "VMP is the extra revenue the next worker brings in, the marginal benefit of hiring. The wage is the marginal cost (MC).")
B.tf(lo, [lo], "concept", "True or false: If the price of the product rises, every worker's value marginal product rises.", True,
     "True. VMP = P × MP, and MP does not depend on the price, so a higher P scales up every VMP.")
B.tf(lo, [lo], "concept", "True or false: A higher wage lowers each worker's value marginal product.", False,
     "False. VMP = P × MP does not include the wage. A higher wage changes the cost of a worker, not the value of what they produce.")
B.num(lo, [lo], "Use the table. Each loaf sells for $2.\n\n" + BT + "\n\nWhat is the value marginal product of the 3rd worker?", 40,
      "MP of the 3rd worker = 45 - 25 = 20 loaves. VMP = $2 × 20 = $40. Using total product (2 × 45 = $90) gives total value of output, not VMP.", V("table_vmp", BL, BQ, at=3, P=2), unit="$")
B.num(lo, [lo], "Use the J Dawgs table. Hot dogs sell for $4.\n\n" + JT + "\n\nWhat is the value marginal product of the 5th worker?", 36,
      "MP = 55 - 46 = 9 hot dogs. VMP = $4 × 9 = $36, matching the professor's solution sheet.", V("table_vmp", JL, JQ, at=5, P=4), unit="$")
B.num(lo, [lo], "Use the table. A car wash sells for $15.\n\n" + CT + "\n\nWhat is the value marginal product of the 4th worker?", 180,
      "MP = 48 - 36 = 12 washes. VMP = $15 × 12 = $180.", V("table_vmp", CL, CQ, at=4, P=15), unit="$")
B.num(lo, [lo, "S15-09"], "\\(Q = 2K^{0.5}L^{0.5}\\) with K = 9 and L = 36. Output sells for $50. What is the value marginal product of labor?", 50 * (2 * 0.5 * 3 / 6),
      "MP_L = 2 × 0.5 × K^0.5 × L^-0.5 = √9 / √36 = 3 / 6 = 0.5. VMP = $50 × 0.5 = $25.", {"f": "cd_vmp", "A": 2, "a": 0.5, "b": 0.5, "K": 9, "L": 36, "P": 50}, unit="$")
B.mc(lo, [lo], "apply", "A bakery's 6th baker adds 30 loaves a day. Loaves sell for $3 and bakers earn $100 a day. What is the 6th baker's VMP, and should the bakery keep that baker?", ["$90; no, the baker adds less value than the $100 wage", "$90; yes, because VMP is positive", "$300; yes", "$3,000; yes"], 0,
     "VMP = $3 × 30 = $90, which is below the $100 wage, so that baker loses the firm $10 a day. A positive VMP is not enough; it must cover the wage.")
B.mc(lo, [lo], "apply", "The price of a firm's product doubles. Holding the wage fixed, what happens to its value marginal product curve and hiring?", ["VMP doubles at every L, so the firm hires more workers", "VMP is unchanged, so hiring is unchanged", "VMP halves, so the firm hires fewer", "MP doubles, so VMP quadruples"], 0,
     "VMP = P × MP, so doubling P doubles VMP for every worker. More workers now satisfy VMP ≥ w. MP depends on technology, not price.")
B.mc(lo, [lo], "apply", "Which pair of numbers does a manager compare when deciding whether to add one more worker?", ["The worker's VMP and the wage", "The worker's MP and the wage", "Total revenue and total cost", "Average product and the wage"], 0,
     "Compare dollars to dollars: VMP (marginal benefit) and the wage (marginal cost). MP is in units, so comparing it to a dollar wage is a units error.")


# ---------------- S15-07 linear ----------------
lo = "S15-07"
B.mc(lo, [lo, "S15-11"], "concept", "A linear production function \\(Q = aK + bL\\) treats capital and labor as:", ["Perfect substitutes", "Perfect complements", "Imperfect substitutes", "Inputs that must be used in fixed proportions"], 0,
     "Each input adds a constant amount, so one can fully replace the other at a fixed rate: perfect substitutes. Perfect complements / fixed proportions is Leontief; imperfect substitutes is Cobb-Douglas.")
B.mc(lo, [lo, "S15-11"], "concept", "The isoquant of a linear production function is:", ["A straight line", "A convex curve", "L-shaped", "A vertical line"], 0,
     "Constant MRTS means a constant slope, so a straight line. Convex is Cobb-Douglas and L-shaped is Leontief.")
B.tf(lo, [lo], "concept", "True or false: A linear production function has diminishing marginal product of labor.", False,
     "False. MP_L = b, a constant, no matter how much labor is used.")
B.tf(lo, [lo], "concept", "True or false: With a linear production function, a firm could produce output using only capital and no labor.", True,
     "True. Q = aK + b(0) = aK > 0. Perfect substitutes means either input alone can produce.")
B.mc(lo, [lo], "concept", "For \\(Q = 4K + L\\), how does the marginal product of capital change as more capital is used?", ["It stays at 4", "It falls", "It rises", "It equals 4K"], 0,
     "MP_K is the coefficient on K, 4, at every level of K. 4K is the total contribution of capital, not the marginal one.")
B.num(lo, [lo], "\\(Q = 4K + 2L\\). What is output with K = 10 and L = 15?", 70,
      "Q = 4(10) + 2(15) = 40 + 30 = 70.", {"f": "linear_q", "a": 4, "b": 2, "K": 10, "L": 15}, unit="units")
B.num(lo, [lo], "\\(Q = 6K + 3L\\). By how much does output rise if the firm adds one more unit of labor?", 3,
      "MP_L = b = 3. Output rises by 3 no matter how much K or L the firm already uses.", {"f": "linear_mp", "a": 6, "b": 3, "K": 1, "L": 1, "wrt": "L"}, unit="units")
B.num(lo, [lo], "\\(Q = 5K + 2L\\). How many units of labor are needed to replace one unit of capital while keeping output the same?", 2.5,
      "One unit of K produces 5 units; one unit of L produces 2. Replacing 5 units of output takes 5 / 2 = 2.5 units of labor.", {"f": "ratio", "num": 5, "den": 2}, unit="units of labor")
B.num(lo, [lo, "S16-02"], "\\(Q = 3K + 9L\\). What is the MRTS (MP_L / MP_K)?", 3,
      "MP_L = 9 and MP_K = 3, so MRTS = 9 / 3 = 3. It is the same at every point.", {"f": "ratio", "num": 9, "den": 3})
B.mc(lo, [lo, "S15-11"], "apply", "A call center finds that one AI license always handles exactly the call volume of 3 human agents. Which production function fits?", ["Linear", "Leontief", "Cobb-Douglas", "None, since software is not capital"], 0,
     "A fixed trade rate (1 license = 3 agents) at any scale means perfect substitutes: linear. Leontief would require a fixed number of agents per license. Software licenses count as capital.")
B.mc(lo, [lo], "apply", "A firm with \\(Q = 10K + 5L\\) is told its workers are less productive than its machines. Which statement is correct?", ["Each machine adds 10 units and each worker adds 5, at every level of use", "Machines add 10 units only until diminishing returns set in", "Workers add nothing once machines are at capacity", "Machines and workers must be used in a 2:1 ratio"], 0,
     "Linear MPs are constant: MP_K = 10, MP_L = 5 always. There are no diminishing returns and no fixed ratio in a linear function.")
B.mc(lo, [lo], "apply", "Two production technologies: (A) \\(Q = 2K + 2L\\), (B) \\(Q = \\min(2K, 2L)\\). A firm has 10 units of capital and 0 workers. Which produces output?", ["Only A", "Only B", "Both", "Neither"], 0,
     "A: 2(10) + 2(0) = 20. B: min(20, 0) = 0, because Leontief needs both inputs. Linear inputs are perfect substitutes.")

# ---------------- S15-08 Leontief ----------------
lo = "S15-08"
B.mc(lo, [lo, "S15-11"], "concept", "A Leontief production function assumes inputs are:", ["Used in fixed proportions, with no substitutability", "Perfect substitutes", "Imperfect substitutes", "Each subject to increasing returns"], 0,
     "Leontief (fixed proportions) has no substitution between inputs. Perfect substitutes is linear; imperfect substitutes is Cobb-Douglas.")
B.mc(lo, [lo, "S15-11"], "concept", "The isoquant for \\(Q = \\min(aK, bL)\\) is:", ["L-shaped", "A straight line", "A convex curve", "A horizontal line"], 0,
     "Extra of one input alone adds nothing, so the isoquant runs flat and vertical from a corner: an L shape.")
B.tf(lo, [lo], "concept", "True or false: For a Leontief production function, the MRTS equals b/a.", False,
     "False. The slides list the Leontief MRTS as N/A (undefined). b/a is the linear MRTS.")
B.tf(lo, [lo], "concept", "True or false: In a Leontief production function, adding more of an input that is already in excess has a marginal product of zero.", True,
     "True. Output is limited by the binding input, so the excess input adds nothing.")
B.mc(lo, [lo], "concept", "Which formula is the Leontief production function?", ["\\(Q = \\min(aK, bL)\\)", "\\(Q = aK + bL\\)", "\\(Q = K^aL^b\\)", "\\(Q = \\max(aK, bL)\\)"], 0,
     "Leontief takes the minimum of aK and bL. The sum is linear, the product of powers is Cobb-Douglas, and max is not a production function used in this course.")
B.mc(lo, [lo], "concept", "Is the Leontief production function on the equation sheet?", ["No", "Yes, with its marginal products", "Yes, but only the MRTS", "Only the isoquant equation"], 0,
     "The sheet has linear and Cobb-Douglas marginal products only. Leontief must be memorized: Q = min(aK, bL).")
B.num(lo, [lo], "\\(Q = \\min(4K, 2L)\\). What is output with K = 5 and L = 12?", 20,
      "Q = min(4 × 5, 2 × 12) = min(20, 24) = 20. Capital binds.", {"f": "leontief_q", "a": 4, "b": 2, "K": 5, "L": 12}, unit="units")
B.num(lo, [lo], "\\(Q = \\min(4K, 2L)\\) with K = 5 and L = 12. What is the marginal product of one more worker?", 0,
      "Now min(20, 26) = 20. Output does not change, so MP_L = 0. Capital is the binding input.", {"f": "leontief_mp", "a": 4, "b": 2, "K": 5, "L": 12, "wrt": "L"}, unit="units")
B.num(lo, [lo], "\\(Q = \\min(3K, L)\\). With K = 10, how many workers are needed so that neither input is wasted?", 30,
      "No waste when 3K = L, so L = 3 × 10 = 30.", {"f": "leontief_ratio", "a": 3, "b": 1, "K": 10}, unit="workers")
B.num(lo, [lo], "\\(Q = \\min(10K, 5L)\\) with K = 4 and L = 6. What is the marginal product of one more unit of capital?", 0,
      "Q = min(40, 30) = 30: labor binds. With K = 5, min(50, 30) = 30. MP_K = 0.", {"f": "leontief_mp", "a": 10, "b": 5, "K": 4, "L": 6, "wrt": "K"}, unit="units")
B.mc(lo, [lo, "S15-11"], "apply", "A trucking company needs exactly one driver per truck. It has 40 trucks and 35 drivers. What happens if it buys 5 more trucks?", ["Nothing; output is limited by the 35 drivers", "Output rises by 5 truckloads", "Output rises by 1/8", "Output falls"], 0,
     "One driver per truck is Leontief: Q = min(trucks, drivers) = min(40, 35) = 35. More trucks leave Q = 35. The firm should hire drivers instead.")
B.mc(lo, [lo, "S15-11"], "apply", "Which business setting best fits a Leontief production function?", ["A bus route that needs exactly one driver for each bus", "A firm where software can replace any number of clerks at a fixed rate", "A farm where adding workers to a fixed field adds less and less", "A firm that can swap capital for labor more easily at some points than others"], 0,
     "Fixed one-to-one requirements are Leontief. A fixed replacement rate is linear. Diminishing returns with substitution is Cobb-Douglas.")
B.mc(lo, [lo], "apply", "A kitchen's output is \\(Q = \\min(20K, 10L)\\) with 3 ovens and 8 workers. The manager wants more meals. What should she add?", ["Workers, because labor is binding", "Ovens, because capital is binding", "Either, both add output", "Neither, the kitchen is at maximum"], 1,
     "Compare 20K = 60 and 10L = 80. Output is 60, limited by ovens. More workers add nothing; a 4th oven raises output to min(80, 80) = 80.")

# ---------------- S15-09 Cobb-Douglas ----------------
lo = "S15-09"
B.mc(lo, [lo, "S15-11"], "concept", "The Cobb-Douglas production function \\(Q = K^aL^b\\) assumes the inputs are:", ["Imperfect substitutes", "Perfect substitutes", "Perfect complements", "Unrelated"], 0,
     "Cobb-Douglas allows some, but not perfect, substitution (Reading Quiz Q5). Perfect substitutes is linear; perfect complements is Leontief.")
B.mc(lo, [lo], "concept", "For \\(Q = K^aL^b\\), the equation sheet gives \\(MP_L\\) as:", ["\\(bK^aL^{b-1}\\)", "\\(aK^{a-1}L^b\\)", "\\(bL^{b-1}\\)", "\\(K^aL^b / L\\)"], 0,
     "Differentiate with respect to L, holding K: bK^aL^{b-1}. aK^{a-1}L^b is MP_K. Dropping K^a forgets that K multiplies the term. K^aL^b / L is average product.")
B.tf(lo, [lo], "concept", "True or false: For \\(Q = K^{0.5}L^{0.5}\\), the marginal product of labor falls as more labor is used with fixed capital.", True,
     "True. MP_L = 0.5K^0.5 / L^0.5, and L is in the denominator, so MP_L falls as L rises: diminishing marginal returns.")
B.tf(lo, [lo], "concept", "True or false: With a Cobb-Douglas production function, the firm can produce output using only labor.", False,
     "False. If K = 0, then K^a = 0 and Q = 0. Both inputs are needed.")
B.mc(lo, [lo, "S15-11"], "concept", "For a Cobb-Douglas production function, the MRTS:", ["Changes along the isoquant", "Is constant", "Is undefined", "Always equals 1"], 0,
     "MRTS = bK / (aL) depends on K and L, so it changes. Constant is linear; undefined is Leontief.")
B.num(lo, [lo], "\\(Q = K^{0.25}L^{0.75}\\). What is \\(MP_L\\) at K = 16 and L = 81? Round to 3 decimals.", 0.75 * 16 ** 0.25 * 81 ** -0.25,
      "MP_L = 0.75 K^0.25 L^-0.25 = 0.75 × (16/81)^0.25 = 0.75 × (2/3) = 0.5.", {"f": "cd_mp", "A": 1, "a": 0.25, "b": 0.75, "K": 16, "L": 81, "wrt": "L"})
B.num(lo, [lo], "\\(Q = K^{0.5}L^{0.5}\\). What is \\(MP_K\\) at K = 4 and L = 36?", 0.5 * 4 ** -0.5 * 36 ** 0.5,
      "MP_K = 0.5 K^-0.5 L^0.5 = 0.5 × √36 / √4 = 0.5 × 6 / 2 = 1.5.", {"f": "cd_mp", "A": 1, "a": 0.5, "b": 0.5, "K": 4, "L": 36, "wrt": "K"})
B.num(lo, [lo], "\\(Q = 3K^{0.5}L^{0.5}\\). What is \\(MP_L\\) at K = 100 and L = 25?", 3 * 0.5 * 10 / 5,
      "With a constant: MP_L = 3 × 0.5 × K^0.5 × L^-0.5 = 1.5 × 10 / 5 = 3. Forgetting the 3 in front gives 1.", {"f": "cd_mp", "A": 3, "a": 0.5, "b": 0.5, "K": 100, "L": 25, "wrt": "L"},
      trap="Multiply by the constant in front; the sheet formula assumes there is none.")
B.num(lo, [lo], "\\(Q = K^{0.5}L^{0.5}\\). What is output with K = 9 and L = 49?", 21,
      "Q = √9 × √49 = 3 × 7 = 21.", {"f": "cd_q", "A": 1, "a": 0.5, "b": 0.5, "K": 9, "L": 49}, unit="units")
B.mc(lo, [lo], "apply", "An economist estimates a factory's production as \\(Q = 5K^{0.3}L^{0.7}\\). Which statement is correct?", ["Labor and capital can substitute for each other, and each has diminishing marginal product", "Labor and capital must be used in a fixed ratio", "One unit of capital always replaces exactly 0.3/0.7 units of labor", "Labor's marginal product is constant at 0.7"], 0,
     "This is Cobb-Douglas (with a constant 5): imperfect substitutes and, with exponents below 1, diminishing MP. Fixed ratio is Leontief. A constant replacement rate or constant MP is linear.")
B.mc(lo, [lo], "apply", "For \\(Q = K^{0.5}L^{0.5}\\) with K fixed at 16, a manager adds workers one at a time. What happens to each new worker's marginal product?", ["It falls with every worker", "It rises with every worker", "It stays constant", "It is zero once L > K"], 0,
     "MP_L = 0.5 × 4 / √L = 2 / √L, which falls as L rises. Constant MP would be linear; zero beyond a ratio would be Leontief.")

# ---------------- S15-10 profit-maximizing input ----------------
lo = "S15-10"
B.mc(lo, [lo, "S15-06"], "concept", "A firm maximizes profit with respect to labor by hiring until:", ["VMP_L = w", "MP_L = w", "AP_L = MP_L", "Total product is at its maximum"], 0,
     "Marginal benefit equals marginal cost: P × MP_L = w. MP_L = w compares units to dollars. AP = MP is the top of AP. TP max ignores the wage.")
B.mc(lo, [lo], "concept", "The S15 slides use studying as an example. When should you stop studying?", ["When the marginal benefit of another hour equals its marginal cost", "When your grade stops rising", "When average points per hour start to fall", "After the first hour with diminishing returns"], 0,
     "The slides answer MB = MC. Stopping where the grade stops rising ignores the cost of time. Falling AP or the start of diminishing returns is not the stopping rule.")
B.tf(lo, [lo], "concept", "True or false: Money a firm has already spent on equipment changes how many workers it should hire in the short run.", False,
     "False. Sunk costs do not change VMP_L or the wage, so they do not change the hiring decision (Quiz 7 Q4 Herman Miller).")
B.tf(lo, [lo], "concept", "True or false: If the wage rises and nothing else changes, the profit-maximizing number of workers falls.", True,
     "True. On the downward part of VMP, a higher wage is crossed at a lower L.")
B.mc(lo, [lo], "concept", "The profit-maximizing rule for capital is:", ["VMP_K = r, the rental rate of capital", "VMP_K = w", "MP_K = MP_L", "P × Q = r × K"], 0,
     "Same logic as labor: P × MP_K = r. The wage is labor's price. MP_K = MP_L is not an optimality rule. P × Q = rK compares totals, not margins.")
B.num(lo, [lo], "Use the table. Loaves sell for $2 and the wage is $10 per worker.\n\n" + BT + "\n\nHow many workers maximize profit?", 6,
      "VMP = $2 × MP: $20, $30, $40, $30, $20, $10, $2, -$4. Hire while VMP ≥ $10 on the falling part: worker 6 has VMP $10 = w; worker 7 has $2 < $10. Hire 6.", V("table_hire", BL, BQ, P=2, w=10), unit="workers")
B.num(lo, [lo], "Use the table. A wash sells for $15 and the wage is $100 per day.\n\n" + CT + "\n\nHow many workers maximize profit?", 5,
      "MPs: 8, 12, 16, 12, 8, 4, -2. VMP = $15 × MP: $120, $180, $240, $180, $120, $60, -$30. Worker 5: $120 ≥ $100. Worker 6: $60 < $100. Hire 5.", V("table_hire", CL, CQ, P=15, w=100), unit="workers")
B.num(lo, [lo], "Use the table. A lawn sells for $40 and the wage is $90 per day.\n\n" + WT + "\n\nHow many workers maximize profit?", 4,
      "MPs: 3, 5, 4, 3, 2, 1. VMP: $120, $200, $160, $120, $80, $40. Worker 4: $120 ≥ $90. Worker 5: $80 < $90. Hire 4.", V("table_hire", WL, WQ, P=40, w=90), unit="workers")
B.num(lo, [lo, "S15-09"], "\\(Q = 2K^{0.5}L^{0.5}\\) with K fixed at 16. Output sells for $30 and the wage is $60. What is the profit-maximizing amount of labor?", (30 * 2 * 0.5 * 4 / 60) ** 2,
      "MP_L = 2(0.5)K^0.5 L^-0.5 = 4 / √L. Set VMP = w: 30 × 4 / √L = 60, so 120 / √L = 60, √L = 2, L = 4.", {"f": "cd_hire", "A": 2, "a": 0.5, "b": 0.5, "K": 16, "P": 30, "w": 60}, unit="units of labor")
B.num(lo, [lo, "S15-09"], "\\(Q = K^{0.5}L^{0.5}\\) with K fixed at 100. Output sells for $20 and the wage is $5. What is the profit-maximizing amount of labor?", (20 * 0.5 * 10 / 5) ** 2,
      "MP_L = 0.5 × 10 / √L = 5 / √L. VMP = 20 × 5 / √L = 100 / √L. Set = 5: √L = 20, L = 400.", {"f": "cd_hire", "A": 1, "a": 0.5, "b": 0.5, "K": 100, "P": 20, "w": 5}, unit="units of labor")
B.mc(lo, [lo], "apply", "At a bakery the 8th baker's VMP is $140 and the daily wage is $120. What should the manager do?", ["Hire the 8th baker and check whether a 9th also has VMP ≥ $120", "Not hire the 8th baker", "Fire bakers until VMP equals AP", "Raise the wage to $140"], 0,
     "VMP > w means the baker adds more value than cost, so hire, then keep checking the next one. Not hiring leaves profit on the table.")
B.mc(lo, [lo], "apply", "A clinic currently has VMP of its last nurse = $300/day and pays $350/day. To maximize profit it should:", ["Use fewer nurses", "Use more nurses", "Keep the same number", "Raise prices until VMP = $0"], 0,
     "VMP < w: the last nurse costs more than the value she adds. Cutting nurses raises MP (diminishing returns) and VMP until VMP = w.")
B.mc(lo, [lo], "apply", "Using the J Dawgs numbers (hire 6 at a $8 wage), what happens if hot dogs rise to $8 each while the wage stays $8?", ["Still 6, since the 7th worker has negative MP", "7, since VMP doubles", "3, since price and wage are equal", "8, to maximize output"], 0,
     "VMP becomes $8 × MP: 56, 96, 112, 104, 72, 16, -64. Worker 6 now has VMP $16 > $8, but worker 7 has negative VMP, so 6 is still optimal.")

# ---------------- S15-11 characteristics ----------------
lo = "S15-11"
B.mc(lo, [lo], "concept", "Match: perfect substitutes, imperfect substitutes, no substitution.", ["Linear, Cobb-Douglas, Leontief", "Leontief, Cobb-Douglas, linear", "Cobb-Douglas, linear, Leontief", "Linear, Leontief, Cobb-Douglas"], 0,
     "Straight from the slides' comparison table: linear = perfect, Cobb-Douglas = imperfect, Leontief = none.")
B.mc(lo, [lo], "concept", "Which production function has an MRTS that changes along the isoquant?", ["Cobb-Douglas", "Linear", "Leontief", "All three"], 0,
     "Cobb-Douglas MRTS = bK/(aL) changes. Linear is constant; Leontief is undefined.")
B.mc(lo, [lo], "concept", "Which isoquant shapes go with linear, Cobb-Douglas and Leontief, in that order?", ["Straight line, convex curve, L-shaped", "Convex curve, straight line, L-shaped", "L-shaped, convex curve, straight line", "Straight line, L-shaped, convex curve"], 0,
     "Linear: straight line. Cobb-Douglas: convex curve. Leontief: L-shaped.")
B.tf(lo, [lo], "concept", "True or false: The Leontief production function is also called the fixed-proportions production function.", True, "True. The slides title it 'Leontief (Fixed-proportions)'.")
B.mc(lo, [lo], "apply", "A dental office needs exactly one hygienist per chair. Adding a chair without a hygienist adds no cleanings. Which production function describes this, and what is its MRTS?", ["Leontief; undefined", "Linear; constant", "Cobb-Douglas; changing", "Leontief; constant"], 0,
     "Fixed one-to-one requirement = Leontief, whose MRTS is N/A (undefined).")
B.mc(lo, [lo], "apply", "A manufacturer can replace workers with robots, but the first robots replace many workers and later robots replace fewer. Which form fits?", ["Cobb-Douglas", "Linear", "Leontief", "None"], 0,
     "Substitution is possible but gets harder: imperfect substitutes and a changing (diminishing) MRTS, which is Cobb-Douglas. Linear would have a constant replacement rate.")

B.mc("S15-09", ["S15-09"], "apply", "A consultant fits \\(Q = K^{0.4}L^{0.6}\\) to a print shop. The owner asks what happens to each new hire's productivity if she keeps adding workers without buying presses. Best answer?", ["Each new worker adds less than the one before, because MP_L = 0.6K^0.4 / L^0.4 falls as L rises", "Each new worker adds exactly 0.6 units", "New workers add nothing until a press is bought", "Each new worker adds more, because L has the larger exponent"], 0,
     "MP_L = 0.6K^0.4 L^-0.4 has L in the denominator, so it falls as L grows: diminishing marginal returns. A constant 0.6 would be linear. Adding nothing until a press is bought would be Leontief. The larger exponent does not make MP rise.")

if __name__ == '__main__': print(B.write())
