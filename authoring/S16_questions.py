from common import *
B = Bank()
def cd_iso(A, a, b, Q, L): return (Q / (A * L ** b)) ** (1 / a)

# ---------------- S16-01 isoquant ----------------
lo = "S16-01"
B.mc(lo, [lo], "concept", "An isoquant shows:", ["All combinations of inputs that produce the same output", "All combinations of inputs that cost the same", "How output changes as one input increases", "The maximum output from each level of labor"], 0,
     "Iso-quant = same quantity. Same cost is an isocost. Output as one input rises is a total product curve.")
B.mc(lo, [lo], "concept", "With K on the vertical axis and L on the horizontal axis, an isoquant farther from the origin represents:", ["A higher level of output", "A lower level of output", "A higher cost", "The same output with less capital"], 0,
     "More of both inputs means more output, so isoquants farther out are higher output. Cost is shown by isocosts.")
B.tf(lo, [lo], "concept", "True or false: Moving along a single isoquant, output stays constant.", True, "True. Every point on an isoquant produces the same quantity; only the input mix changes.")
B.mc(lo, [lo, "S15-11"], "concept", "Which isoquant shape goes with a Cobb-Douglas production function?", ["Convex curve", "Straight line", "L-shape", "Upward sloping line"], 0,
     "Cobb-Douglas: convex. Linear: straight line. Leontief: L-shape. Isoquants slope down because giving up one input requires more of the other.")
B.tf(lo, [lo], "concept", "True or false: To graph a Cobb-Douglas isoquant with K on the vertical axis, you set Q equal to the target output and solve the production function for K.", True,
     "True. That is the slides' method (pp. 24 to 25): plug in the target, then solve for K as a function of L.")
B.mc(lo, [lo], "concept", "Two isoquants for the same production function cross each other. What is wrong?", ["Isoquants of one production function cannot cross, since the crossing point would produce two output levels at once", "Nothing; isoquants usually cross", "They must be isocosts instead", "Only Leontief isoquants can cross"], 0,
     "Each input combination gives one maximum output, so it cannot lie on two different isoquants.")
B.num(lo, [lo], "\\(Q = 2K^{0.5}L^{0.5}\\) and the target is Q = 100. How much capital is needed with L = 50?", cd_iso(2, .5, .5, 100, 50),
      "Isoquant: \\(K = (100 / (2L^{0.5}))^2 = 2500/L\\). With L = 50, K = 2500/50 = 50.", {"f": "iso_k", "A": 2, "a": 0.5, "b": 0.5, "Q": 100, "L": 50}, unit="units of capital")
B.num(lo, [lo], "\\(Q = K^{0.5}L^{0.5}\\) and the target is Q = 60. How much capital is needed with L = 90?", cd_iso(1, .5, .5, 60, 90),
      "\\(K = (60/L^{0.5})^2 = 3600/L = 3600/90 = 40\\).", {"f": "iso_k", "A": 1, "a": 0.5, "b": 0.5, "Q": 60, "L": 90}, unit="units of capital")
B.num(lo, [lo], "\\(Q = 4K^{0.25}L^{0.75}\\) and the target is Q = 64. How much capital is needed with L = 16?", cd_iso(4, .25, .75, 64, 16),
      "Divide by 4: \\(K^{0.25} = 16/L^{0.75}\\). \\(16^{0.75} = 8\\), so \\(K^{0.25} = 2\\) and \\(K = 2^4 = 16\\). Raise to the 4th power because 1/0.25 = 4.", {"f": "iso_k", "A": 4, "a": 0.25, "b": 0.75, "Q": 64, "L": 16}, unit="units of capital")
B.num(lo, [lo, "S15-07"], "\\(Q = 2K + 4L\\) and the target is Q = 100. How much capital is needed with L = 15?", 20,
      "Linear isoquant: \\(K = (Q - bL)/a = (100 - 60)/2 = 20\\).", {"f": "lin_iso_k", "a": 2, "b": 4, "Q": 100, "L": 15}, unit="units of capital")
B.mc(lo, [lo], "apply", "A manager forecasts demand of 100 units next month and has the isoquant for Q = 100. What does the isoquant tell her?", ["Every mix of capital and labor that would meet the target", "The single cheapest mix of capital and labor", "How much she can spend on inputs", "How many units she will sell"], 0,
     "The isoquant lists all mixes that make 100 units (slides p. 26). Picking the cheapest one requires isocost lines and input prices.")
B.mc(lo, [lo], "apply", "A firm moves from (L = 10, K = 40) to (L = 20, K = 20) and output stays at 200. What happened?", ["It moved along one isoquant, substituting labor for capital", "It moved to a higher isoquant", "It moved to a lower isoquant", "It moved along an isocost line"], 0,
     "Same output means the same isoquant. More L and less K is substitution of labor for capital. Whether cost changed depends on prices, which are not given.")

B.mc(lo, [lo], "apply", "Klarna's average month needs a fixed number of resolved conversations. On a graph with AI hours (K) up and agent hours (L) across, Klarna's actual mix sits on that isoquant. A cheaper mix that resolves the same number of conversations would be:", ["Another point on the same isoquant", "A point on a higher isoquant", "A point on a lower isoquant", "The origin"], 0,
     "Same output means the same isoquant. Cost minimization picks a point along it; it never moves you to a different output level.")
B.mc(lo, [lo, "S15-09"], "concept", "A log-linear regression of ln(Q) on ln(K) and ln(L) gives an intercept of 1.5, a coefficient of 0.3 on ln(K) and 0.6 on ln(L). What is the Cobb-Douglas production function?", ["\\(Q = e^{1.5}K^{0.3}L^{0.6}\\)", "\\(Q = 1.5K^{0.3}L^{0.6}\\)", "\\(Q = e^{1.5}K^{0.6}L^{0.3}\\)", "\\(Q = 1.5 + 0.3K + 0.6L\\)"], 0,
     "ln(Q) = ln(A) + a ln(K) + b ln(L), so a is the ln(K) coefficient, b the ln(L) coefficient, and A = e^(intercept) (slides pp. 41 to 42). Forgetting to exponentiate the intercept is the common slip.")
B.tf(lo, ["S15-09"], "concept", "True or false: You estimate a Cobb-Douglas production function with a linear regression after taking the natural log of output and both inputs.", True,
     "True. Logs turn \\(Q = AK^aL^b\\) into ln(Q) = ln(A) + a ln(K) + b ln(L), which is linear in the logs.")

# ---------------- S16-02 MRTS ----------------
lo = "S16-02"
B.mc(lo, [lo], "concept", "The MRTS (as defined on the equation sheet) is:", ["MP_L / MP_K", "MP_K / MP_L", "w / r", "MP_L × MP_K"], 0,
     "MRTS_KL = MP_L / MP_K. w/r is the input price ratio, which the MRTS equals only at the cost minimum.")
B.mc(lo, [lo], "concept", "Graphically, the MRTS is:", ["The absolute value of the slope of the isoquant", "The slope of the isocost line", "The height of the isoquant", "The slope of the total product curve"], 0,
     "MRTS is the isoquant's slope in absolute value. The isocost slope is -w/r. The slope of total product is MP.")
B.tf(lo, [lo], "concept", "True or false: The MRTS measures how many units of capital one more unit of labor can replace while keeping output constant.", True, "True. That is the substitution rate along an isoquant.")
B.mc(lo, [lo, "S15-11"], "concept", "For a Leontief production function, the MRTS is:", ["Undefined", "Constant at b/a", "bK/(aL)", "Zero everywhere"], 0, "The slides list Leontief MRTS as N/A: there is no substitution.")
B.mc(lo, [lo], "concept", "For \\(Q = K^aL^b\\), the MRTS simplifies to:", ["\\(\\frac{bK}{aL}\\)", "\\(\\frac{aK}{bL}\\)", "\\(\\frac{b}{a}\\)", "\\(\\frac{aL}{bK}\\)"], 0,
     "MP_L / MP_K = bK^aL^{b-1} / (aK^{a-1}L^b) = bK/(aL). b/a is the linear MRTS. aK/(bL) swaps the exponents.")
B.num(lo, [lo], "\\(Q = K^{0.5}L^{0.5}\\). What is the MRTS at K = 40 and L = 10?", 4,
      "MRTS = bK/(aL) = 0.5(40)/(0.5(10)) = 40/10 = 4.", {"f": "cd_mrts", "A": 1, "a": 0.5, "b": 0.5, "K": 40, "L": 10})
B.num(lo, [lo], "\\(Q = K^{0.25}L^{0.75}\\). What is the MRTS at K = 20 and L = 30?", 0.75 * 20 / (0.25 * 30),
      "MRTS = bK/(aL) = 0.75(20)/(0.25(30)) = 15/7.5 = 2.", {"f": "cd_mrts", "A": 1, "a": 0.25, "b": 0.75, "K": 20, "L": 30})
B.num(lo, [lo], "MP_L = 30 and MP_K = 12. What is the MRTS?", 2.5, "MRTS = MP_L / MP_K = 30/12 = 2.5.", {"f": "ratio", "num": 30, "den": 12})
B.num(lo, [lo, "S15-07"], "\\(Q = 5K + 15L\\). What is the MRTS at K = 2 and L = 8?", 3, "Linear: MRTS = b/a = 15/5 = 3, the same at every K and L.", {"f": "ratio", "num": 15, "den": 5})
B.mc(lo, [lo], "apply", "At a firm's current mix the MRTS is 3. What does that mean?", ["One more unit of labor can replace 3 units of capital without changing output", "One more unit of capital can replace 3 units of labor", "Labor costs 3 times as much as capital", "Output rises by 3 if the firm adds a worker"], 0,
     "MRTS = MP_L/MP_K = 3: a worker adds as much as 3 units of capital, so one more worker lets you drop 3 units of K. Prices are a separate ratio (w/r). The rise in output from a worker is MP_L, not the MRTS.")
B.mc(lo, [lo], "apply", "A factory with \\(Q = K^{0.5}L^{0.5}\\) uses K = 50 and L = 10. Its manager says each worker could replace 5 machines. Is that right?", ["Yes, MRTS = K/L = 5", "No, MRTS = L/K = 0.2", "No, MRTS = 1 because the exponents are equal", "No, MRTS is undefined"], 0,
     "With equal exponents MRTS = bK/(aL) = K/L = 50/10 = 5. Equal exponents do not make it 1; that only happens when K = L.")
B.mc(lo, [lo], "apply", "Klarna substitutes AI assistant hours (K) for human agent hours (L) while keeping conversations resolved the same. Which concept measures the trade-off at its current mix?", ["The MRTS", "The isocost slope", "Average product of labor", "Value marginal product"], 0,
     "The rate of substituting one input for another at constant output is the MRTS. The isocost slope involves prices, not productivity.")

# ---------------- S16-03 diminishing MRTS ----------------
lo = "S16-03"
B.mc(lo, [lo], "concept", "The law of diminishing MRTS says that:", ["For every unit decrease in one input, increasing amounts of the other input are needed to keep output the same", "Output falls as more of an input is used", "The isocost line gets flatter as the budget grows", "Each worker adds less output than the one before"], 0,
     "That is the slides' definition (p. 16). Each worker adding less is diminishing marginal returns, related but a different concept.")
B.mc(lo, [lo], "concept", "Which production function's isoquants show a diminishing MRTS?", ["Cobb-Douglas", "Linear", "Leontief", "All three"], 0,
     "Cobb-Douglas MRTS = bK/(aL) falls as L rises. Linear MRTS is constant and Leontief MRTS is undefined.")
B.tf(lo, [lo], "concept", "True or false: A diminishing MRTS is what makes Cobb-Douglas isoquants convex (bowed toward the origin).", True, "True. The slope flattens as you move right, which is the convex shape.")
B.tf(lo, [lo, "S15-07"], "concept", "True or false: A linear production function obeys the law of diminishing MRTS.", False, "False. Linear MRTS = b/a is constant at every point.")
B.mc(lo, [lo], "concept", "The S16 slides explain the law of diminishing MRTS by pointing to:", ["Diminishing marginal returns", "Economies of scale", "Rising input prices", "Network effects"], 0,
     "As you add more of one input its marginal product falls, so it takes more and more of it to replace the other input (slide p. 19).")
B.mc(lo, [lo], "concept", "Moving down and to the right along a convex isoquant (more L, less K), the MRTS:", ["Falls", "Rises", "Stays the same", "Becomes negative infinity"], 0,
     "With more labor and less capital, MP_L falls and MP_K rises, so MP_L/MP_K falls.")
B.num(lo, [lo], "Points on one isoquant (Q = 100): A (L = 4, K = 3), B (L = 3, K = 4), C (L = 2, K = 6), D (L = 1, K = 9). How many units of capital replace the unit of labor given up going from C to D?", 3,
      "K rises from 6 to 9 when L falls from 2 to 1: 3 units of capital. From A to B it took only 1. That growing amount is the law of diminishing MRTS.", {"f": "diff", "x1": 6, "x2": 9}, unit="units of capital", kind="calc")
B.num(lo, [lo, "S16-02"], "\\(Q = K^{0.5}L^{0.5}\\) along the isoquant Q = 20 (so K = 400/L). What is the MRTS at L = 10?", 4,
      "K = 400/10 = 40. MRTS = K/L = 40/10 = 4.", {"f": "cd_mrts", "A": 1, "a": 0.5, "b": 0.5, "K": 40, "L": 10}, kind="calc")
B.num(lo, [lo, "S16-02"], "Same isoquant (Q = 20, K = 400/L). What is the MRTS at L = 40?", 0.25,
      "K = 400/40 = 10. MRTS = 10/40 = 0.25. It fell from 4 at L = 10 to 0.25 at L = 40: diminishing MRTS.", {"f": "cd_mrts", "A": 1, "a": 0.5, "b": 0.5, "K": 10, "L": 40}, kind="calc")
B.mc(lo, [lo], "apply", "A restaurant replaces cooks with kitchen robots one at a time. The first robot replaces 4 cooks, the next replaces 3, then 2. This pattern reflects:", ["Diminishing MRTS", "Constant MRTS", "Negative marginal returns", "Fixed proportions"], 0,
     "Each additional unit of capital replaces less labor: the substitution rate falls. Constant MRTS would mean every robot replaces the same number.")
B.mc(lo, [lo], "apply", "Why do most firms use some of both capital and labor instead of going all-in on one?", ["With diminishing MRTS, replacing the last bits of one input takes huge amounts of the other", "Because isocosts are curved", "Because MRTS is always 1", "Because inputs are perfect substitutes"], 0,
     "As one input gets scarce it becomes very hard to replace, so the cheapest mix uses some of both. Isocosts are straight lines. Perfect substitutes would allow all-in.")
B.mc(lo, [lo], "apply", "A firm's isoquant is a straight line. A consultant warns about diminishing MRTS as it automates. Is the warning relevant?", ["No, a straight-line isoquant means a constant MRTS", "Yes, every isoquant has diminishing MRTS", "Yes, because the isoquant slopes down", "No, because the MRTS is undefined"], 0,
     "A straight-line isoquant (linear production) has a constant MRTS. Downward slope alone does not imply diminishing MRTS. Undefined MRTS is Leontief.")

B.tf(lo, [lo], "concept", "True or false: Along a Cobb-Douglas isoquant, the MRTS is higher where the firm uses little labor and lots of capital.", True,
     "True. MRTS = bK/(aL) is large when K is large and L is small, which is the steep upper left of the isoquant.")
B.mc(lo, [lo], "apply", "Klarna's AI assistant handles routine chats well, but disputes and fraud still need a person. As Klarna replaces more agents with AI, what does diminishing MRTS predict?", ["Each additional agent removed takes more AI hours to replace", "Each agent removed takes fewer AI hours to replace", "AI hours replace agents at a constant rate", "Output rises as agents are removed"], 0,
     "The last agents handle the hard cases the AI is worst at, so replacing them takes more and more AI hours. A constant rate would mean perfect substitutes.")

# ---------------- S16-04 isocost ----------------
lo = "S16-04"
B.mc(lo, [lo], "concept", "An isocost line shows:", ["All input combinations with the same total cost", "All input combinations with the same output", "The cost of each additional unit of output", "The wage paid to each worker"], 0,
     "Iso-cost = same cost: C = wL + rK. Same output is an isoquant. Cost of an extra unit is marginal cost.")
B.mc(lo, [lo], "concept", "With K on the vertical axis, the vertical intercept of the isocost line is:", ["C/r", "C/w", "-w/r", "w/r"], 0,
     "Setting L = 0 in K = C/r - (w/r)L gives K = C/r, the most capital the budget buys. C/w is the horizontal intercept and -w/r is the slope.")
B.tf(lo, [lo], "concept", "True or false: If the budget C rises and input prices stay the same, the isocost line shifts out parallel to the old line.", True, "True. The slope -w/r does not depend on C; both intercepts grow by the same percentage.")
B.mc(lo, [lo, "S16-06"], "concept", "Holding C and r fixed, the wage rises. The isocost line:", ["Becomes steeper; the horizontal intercept moves in", "Becomes flatter; the horizontal intercept moves out", "Shifts out in parallel", "Becomes steeper; the vertical intercept moves up"], 0,
     "Slope -w/r grows in magnitude and C/w shrinks. C/r is unchanged, so the vertical intercept stays put.")
B.tf(lo, [lo], "concept", "True or false: The isocost equation C = wL + rK is printed on the equation sheet.", False, "False. Only the slope -w/r is on the sheet. Know C = wL + rK and the intercepts.")
B.num(lo, [lo], "Budget $1,000, wage $10, rental rate $25. What is the most labor the firm can hire if it uses no capital?", 100,
      "C/w = 1,000/10 = 100 labor hours (slides p. 31).", {"f": "ratio", "num": 1000, "den": 10}, unit="labor hours")
B.num(lo, [lo], "Budget $1,000, wage $10, rental rate $25. What is the slope of the isocost line (K on the vertical axis)?", -0.4,
      "Slope = -w/r = -10/25 = -0.4.", {"f": "ratio", "num": -10, "den": 25})
B.num(lo, [lo], "Budget $1,500, wage $30, rental rate $50. What is the most capital the firm can rent if it hires no labor?", 30,
      "C/r = 1,500/50 = 30 units of capital.", {"f": "ratio", "num": 1500, "den": 50}, unit="units of capital")
B.num(lo, [lo], "A firm spends on 20 workers at $15 each and 10 machines at $40 each. What is its total cost on this isocost?", 700,
      "C = wL + rK = 15(20) + 40(10) = 300 + 400 = $700.", {"f": "cost", "w": 15, "L": 20, "r": 40, "K": 10}, unit="$")
B.num(lo, [lo], "Budget $1,000, rental rate $25. The wage doubles from $10 to $20. What is the new maximum amount of labor?", 50,
      "C/w = 1,000/20 = 50, down from 100 (slides p. 34). The vertical intercept stays at 40.", {"f": "ratio", "num": 1000, "den": 20}, unit="labor hours")
B.mc(lo, [lo], "apply", "A CEO cuts the weekly production budget by 50%. Prices are unchanged. What happens to the isocost line?", ["It shifts in parallel; both intercepts halve", "It rotates around the vertical intercept", "It becomes steeper", "It does not change"], 0,
     "Only C changed, so the slope -w/r is the same and both intercepts, C/w and C/r, are cut in half (slides p. 33).")
B.mc(lo, [lo], "apply", "Union negotiations lower the wage while machine rental rates stay the same. On a graph with K vertical, the firm's isocost:", ["Pivots out along the labor axis and gets flatter", "Pivots up along the capital axis and gets steeper", "Shifts in parallel", "Does not move"], 0,
     "Lower w raises C/w (horizontal intercept moves out) and reduces w/r (flatter). C/r is unchanged.")
B.mc(lo, [lo], "apply", "AI software rental prices fall while wages stay the same. Which intercept of the isocost line (K = AI hours on the vertical axis) changes?", ["The vertical intercept rises", "The horizontal intercept rises", "Both intercepts fall", "Neither"], 0,
     "C/r rises when r falls, so the vertical intercept moves up. C/w is unchanged.")

# ---------------- S16-05 cost-min rule ----------------
lo = "S16-05"
B.mc(lo, [lo], "concept", "A firm minimizes the cost of producing a given output when:", ["MP_L / w = MP_K / r", "MP_L = MP_K", "w = r", "MP_L / MP_K = r / w"], 0,
     "Equal marginal product per dollar (bang for the buck). Equal MPs or equal prices are not the rule. MP_L/MP_K = r/w flips the price ratio; it should be w/r.")
B.mc(lo, [lo], "concept", "At the cost-minimizing input mix, the isoquant and the isocost are:", ["Tangent: MRTS = w/r", "Crossing at a right angle", "Parallel everywhere", "Both straight lines"], 0, "At the cheapest point on the isoquant, the lowest isocost just touches it, so their slopes are equal: MRTS = w/r.")
B.tf(lo, [lo], "concept", "True or false: If MP_K / r > MP_L / w, the firm can lower its cost of producing the same output by using more capital and less labor.", True,
     "True. Each dollar moved from labor to capital adds more output than it takes away.")
B.tf(lo, [lo], "concept", "True or false: The cost-minimizing input rule MP_L / w = MP_K / r is printed on the equation sheet.", False, "False. The sheet has the MRTS and the isocost slope, not the rule that sets them equal.")
B.mc(lo, [lo], "concept", "The professor calls MP/price for each input the:", ["Bang for the buck", "Marginal rate of substitution", "Average product", "Isocost slope"], 0, "Slides p. 38: marginal product (bang) per dollar spent (buck).")
B.num(lo, [lo], "Labor costs $12 per hour and the last worker made 84 rollers per hour. What is MP_L / w?", 7,
      "84 / 12 = 7 rollers per dollar (in-class exercise).", {"f": "ratio", "num": 84, "den": 12}, unit="units per $")
B.num(lo, [lo], "Capital rents for $15 per hour and MP_K = 120 rollers per hour. What is MP_K / r?", 8,
      "120 / 15 = 8 rollers per dollar (in-class exercise). Since 8 > 7 for labor, use more capital.", {"f": "ratio", "num": 120, "den": 15}, unit="units per $")
B.num(lo, [lo], "\\(Q = 10K^{0.5}L^{0.5}\\), w = $40, r = $10. At (L, K) = (10, 10), what is MP_K / r?", 0.5,
      "MP_K = 0.5 × 10 × L^0.5 / K^0.5 = 5 × 1 = 5. MP_K/r = 5/10 = 0.5. Compare MP_L/w = 5/40 = 0.125: capital gives more per dollar.", {"f": "cd_bang", "A": 10, "a": 0.5, "b": 0.5, "K": 10, "L": 10, "price": 10, "wrt": "K"}, unit="units per $")
B.mc(lo, [lo], "apply", "w = $20, r = $50, MP_L = 60, MP_K = 150. Is the firm cost minimizing?", ["Yes, both inputs give 3 units per dollar", "No, use more labor", "No, use more capital", "Cannot tell without output"], 0,
     "60/20 = 3 and 150/50 = 3. Equal bang for the buck, so the mix is cost minimizing.")
B.mc(lo, [lo], "apply", "w = $25, r = $40, MP_L = 50, MP_K = 120. What should the firm do?", ["Use more capital and less labor", "Use more labor and less capital", "Keep the same mix", "Cut both inputs"], 0,
     "MP_L/w = 2 and MP_K/r = 3. Capital gives more per dollar, so shift toward capital.")
B.mc(lo, [lo], "apply", "w = $30, r = $20, MP_L = 90, MP_K = 40. What should the firm do?", ["Use more labor and less capital", "Use more capital and less labor", "Keep the same mix", "Use only capital"], 0,
     "MP_L/w = 3 and MP_K/r = 2. Labor gives more per dollar, so shift toward labor.",
     trap="Raw MP_L (90) beats MP_K (40), but that is not why; compare per dollar.")
B.mc(lo, [lo], "apply", "A firm has MP_L/w = MP_K/r. It hires more workers and keeps capital fixed. With diminishing marginal returns, how do the bang-for-the-buck ratios compare now?", ["MP_L/w < MP_K/r", "MP_L/w > MP_K/r", "They stay equal", "Both ratios rise"], 0,
     "Adding labor lowers MP_L, so labor now gives less per dollar than capital. The new mix is not the cheapest way to make its new output level.")

# ---------------- S16-06 optimal input substitution ----------------
lo = "S16-06"
B.mc(lo, [lo], "concept", "When the price of an input rises, a cost-minimizing firm will:", ["Use less of that input and more of the other", "Use more of that input", "Keep the same mix", "Use less of both inputs at the same output"], 0,
     "The firm substitutes toward the input that became relatively cheaper.")
B.tf(lo, [lo], "concept", "True or false: In the in-class exercise, if the rental rate on capital increases, the firm should use less capital and more labor.", True, "True. That is the professor's answer to question 3.")
B.mc(lo, [lo], "concept", "For a Leontief production function, how does the cost-minimizing input mix respond to a higher wage?", ["It does not change; inputs are used in fixed proportions", "Less labor, more capital", "More labor, less capital", "The firm uses only capital"], 0,
     "With no substitution the mix is fixed by the recipe. Total cost rises, but the ratio stays the same.")
B.mc(lo, [lo], "concept", "For a linear production function, the cost-minimizing mix is usually:", ["A corner: only the input with the higher MP per dollar", "A tangency with both inputs", "Equal amounts of both inputs", "Whatever the firm used before"], 0,
     "Linear isoquants are straight, so the cheapest point is at an end: all of the input with the higher MP/price.")
B.tf(lo, [lo], "concept", "True or false: A wage cut makes the isocost line flatter, so the tangency with the isoquant moves to a point with more labor and less capital.", True, "True.")
B.num(lo, [lo], "\\(Q = 10K^{0.5}L^{0.5}\\), target Q = 100, w = $40, r = $10. What is the cost-minimizing amount of labor?", 5,
      "Tangency: K/L = w/r = 4, so K = 4L. Then 10√(4L·L) = 20L = 100, L = 5.", {"f": "costmin_L", "A": 10, "a": 0.5, "b": 0.5, "Q": 100, "w": 40, "r": 10}, unit="units of labor")
B.num(lo, [lo], "Same setup (\\(Q = 10K^{0.5}L^{0.5}\\), Q = 100, w = $40, r = $10). What is the minimum total cost?", 400,
      "L = 5, K = 20. C = 40(5) + 10(20) = $400. That matches the slides' table: (5, 20) is the only mix with equal bang for the buck.", {"f": "costmin_C", "A": 10, "a": 0.5, "b": 0.5, "Q": 100, "w": 40, "r": 10}, unit="$")
B.num(lo, [lo], "Same setup, but the rental rate rises from $10 to $40. What is the new cost-minimizing amount of capital?", 10,
      "Now K/L = 40/40 = 1, so K = L. 10L = 100, L = 10, K = 10. Capital fell from 20 to 10 because it got more expensive.", {"f": "costmin_K", "A": 10, "a": 0.5, "b": 0.5, "Q": 100, "w": 40, "r": 40}, unit="units of capital")
B.num(lo, [lo], "\\(Q = 2K^{0.5}L^{0.5}\\), target Q = 200, w = $16, r = $4. What is the cost-minimizing amount of capital?", 200,
      "K = (w/r)L = 4L. 2 × 2L = 200, L = 50, K = 200.", {"f": "costmin_K", "A": 2, "a": 0.5, "b": 0.5, "Q": 200, "w": 16, "r": 4}, unit="units of capital")
B.num(lo, [lo, "S15-07"], "\\(Q = 4K + 2L\\). w = $10 and r = $30. What is the lowest cost of producing 120 units?", min(120 / 4 * 30, 120 / 2 * 10),
      "Compare per dollar: MP_K/r = 4/30 = 0.133, MP_L/w = 2/10 = 0.2. Labor is the better deal, so use only labor: L = 120/2 = 60, cost = 60 × $10 = $600. Using only capital would cost 30 × $30 = $900.", {"f": "linear_cost", "a": 4, "b": 2, "Q": 120, "w": 10, "r": 30}, unit="$")
B.num(lo, [lo, "S15-08"], "\\(Q = \\min(2K, 4L)\\). w = $20 and r = $50. What is the lowest cost of producing 80 units?", 20 * 20 + 50 * 40,
      "Fixed proportions: L = Q/4 = 20 and K = Q/2 = 40. Cost = 20(20) + 50(40) = 400 + 2,000 = $2,400. Prices do not change the mix.", {"f": "leontief_cost", "a": 2, "b": 4, "Q": 80, "w": 20, "r": 50}, unit="$")
B.mc(lo, [lo], "apply", "Minimum wages rise sharply in a city. Fast food chains respond by installing ordering kiosks. This is an example of:", ["Optimal input substitution toward capital", "Diminishing marginal returns to labor", "A parallel shift of the isocost line", "A Leontief technology"], 0,
     "Labor got relatively more expensive, so firms substitute capital (kiosks) for labor. Leontief would not allow substitution.")
B.mc(lo, [lo], "apply", "Klarna learns AI assistant hours are getting cheaper while agent wages hold steady. To minimize cost at the same output, Klarna should:", ["Use more AI hours and fewer agent hours", "Use more agent hours and fewer AI hours", "Keep the mix unchanged", "Cut both inputs"], 0,
     "A lower r raises MP_K/r, so capital (AI hours) is a better deal; substitute toward it.")

if __name__ == "__main__": print(B.write())
