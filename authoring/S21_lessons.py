from common import *

DERIV = {"title": "Marginal revenue with two firms", "body": r"Revenue for firm 1 is price times its own quantity: \(R_1 = P \cdot Q_1 = [a - b(Q_1 + Q_2)]Q_1 = aQ_1 - bQ_1^2 - bQ_1Q_2\). Take the derivative with respect to \(Q_1\), treating \(Q_2\) as a fixed number: the derivative of \(aQ_1\) is a, of \(bQ_1^2\) is \(2bQ_1\), of \(bQ_1Q_2\) is \(bQ_2\). So \(MR_1 = a - 2bQ_1 - bQ_2\). Tiny example: P = 10 - (Q_1 + Q_2) gives \(MR_1 = 10 - 2Q_1 - Q_2\)."}
SOLVE2 = {"title": "Solving two reaction functions together", "body": r"Substitute one into the other. With \(Q_1 = 5 - \tfrac{1}{2}Q_2\) and \(Q_2 = 5 - \tfrac{1}{2}Q_1\): \(Q_1 = 5 - \tfrac{1}{2}(5 - \tfrac{1}{2}Q_1) = 2.5 + \tfrac{1}{4}Q_1\). Subtract \(\tfrac{1}{4}Q_1\): \(\tfrac{3}{4}Q_1 = 2.5\), so \(Q_1 = 10/3 \approx 3.33\). Then \(Q_2 = 5 - \tfrac{1}{2}(3.33) = 3.33\). With identical firms you can skip the algebra: set \(Q_1 = Q_2 = q\) in one reaction function."}
PROFIT = {"title": "Profit with constant marginal cost", "body": r"With cost \(C = cQ\) and no fixed cost, profit is \((P - c) \times Q\). Example: P = $336, c = $4, Q = 332: profit = 332 × 332 = $110,224."}

BOOK = table(["Model", "Outputs", "Total Q", "Price", "Profit per firm"], [
    ["Collusion", "249 each", "498", "$502", "$124,002 each"],
    ["Cournot", "332 each", "664", "$336", "$110,224 each"],
    ["Stackelberg (firm 1 leads)", "498 and 249", "747", "$253", "Leader $124,002, follower $62,001"],
    ["Bertrand", "498 each", "996", "$4", "$0"]])
FIG1 = table(["Goods are", "Quantity", "Price", "Lead time"], [["Homogeneous", "Cournot", "Bertrand (standard)", "Stackelberg"], ["Differentiated", "(less common)", "Differentiated Bertrand", "(less common)"]])

LESSONS = [
{"id": "S21-01", "title": "Oligopoly", "calc": False,
 "plain": r"""An **oligopoly** is a market with a **few** firms. The professor's reading (Bryce, *Rivalry in Oligopoly*, p. 1) puts it between monopoly (one firm) and perfect competition (many firms): from two firms (a **duopoly**) up to maybe 8 to 12, perhaps as many as 15. When there are so many firms that each becomes a price taker, it is no longer an oligopoly.

**The key feature is interdependence.** If one firm's actions move the market price and quantity enough to change the other firms' prospects, the firms are interdependent, and the market is usually an oligopoly (Bryce p. 1). Each firm maximizes profit by considering how rivals will react to its moves.

**Where does the reasoning stop?** Firm 1 reasons: if I do a, Firm 2 does b; then I must do c; then they do d... It ends at a **Nash equilibrium**: each firm is playing its best response to the others, and no one wants to deviate (Bryce p. 1). In practice firms reason through the game before they play and go straight to the equilibrium (Bryce pp. 1 to 2; example: corn wet milling firms choosing high-fructose corn syrup capacity in 1972).

**Oligopolists still set MR = MC.** The difference: their best price or quantity **depends on the price or quantity chosen by rivals** (Bryce p. 3). The full schedule of best responses is called a **reaction function** (S21-04).

**Beliefs matter** (textbook). A firm's demand depends on whether rivals match its price changes. If rivals match, demand is less elastic; if not, it is more elastic. The right model depends on what the firm believes rivals will do.

**Examples from the Session 21 reading quiz** (professor's feedback): wireless carriers (AT&T, T-Mobile, Verizon), credit cards (American Express, Discover, Mastercard, Visa) and airlines (American, Delta, Southwest, United) are oligopolies. **Self-storage is not**: despite a few big names like Public Storage and Extra Space Storage, most of the thousands of self-storage companies are locally owned.

**Tacit collusion** (Bryce p. 2): because firms meet again and again with no certain end, they may avoid price wars without any agreement. Full-fare airlines match each other's fare hikes and fare sales; Delta broke that norm in 2005 to compete with discount carriers. Disruptive entrants (Amazon in bookselling) often ignore the norms.

**Strategic variables** (Bryce p. 3): the levers firms compete with, such as price, quantity (capacity), lead time, and non-price tools (frequent flier programs, coupons, locations). Which lever matters most decides which oligopoly model fits (S21-05).""",
 "why": "Every oligopoly question starts by recognizing interdependence and which model applies. Practice exam Q14.",
 "definition": "Oligopoly is a market structure in which a few firms (from two up to perhaps 8 to 15) produce most of the output and their actions are interdependent: each firm's best decision depends on how rivals respond.",
 "formulas": [], "derivation": "", "math": [],
 "worked": [{"title": "Is it an oligopoly?", "problem": "Classify: (a) three national wireless carriers; (b) thousands of wheat farmers; (c) the only electric utility in a city; (d) four ski resorts near Salt Lake City.",
   "steps": ["(a) Few firms, each move affects the others: oligopoly.", "(b) Each farmer is a price taker: perfect competition.", "(c) One firm: monopoly.", "(d) Few firms with overlapping customers: oligopoly (Bryce calls it differentiated Bertrand)."], "answer": "Oligopoly, perfect competition, monopoly, oligopoly."}],
 "traps": ["A few famous big firms do not make an oligopoly: self-storage has big names but thousands of local owners (Session 21 reading quiz Q1).",
           "The number of firms alone does not decide it: the test is whether firms' actions are interdependent.",
           "Oligopolists still maximize profit with MR = MC; what differs is that MR depends on rivals' choices.",
           "Tacit collusion (keying off rivals without an agreement) is legal; explicit agreements are not (S20-07)."],
 "sources": {"slides": "S21 slides not posted", "read": "Ch. 9: Introduction; Conditions for Oligopoly; The Role of Beliefs; Bryce, Rivalry in Oligopoly pp. 1 to 3", "exercise": "", "quiz": "Session 21 Reading Quiz Q1; Practice exam Q14"}},

{"id": "S21-02", "title": "Cournot oligopoly", "calc": True,
 "plain": r"""In a **Cournot oligopoly**, firms compete by choosing **how much to produce** (quantity), at the same time, and let the price float on the demand curve (Bryce p. 4).

**Textbook conditions:** (1) few firms serving many consumers; (2) homogeneous or differentiated products; (3) each firm believes rivals will **hold their output constant** if it changes its output; (4) barriers to entry.

**Where it fits** (Bryce p. 4): commodity markets like oil and agriculture. OPEC's members set output targets: a Cournot cartel. Corn wet milling capacity (1972) is another example.

**How to solve it** (setting MR = MC):
1. Write firm 1's revenue with demand \(P = a - b(Q_1 + Q_2)\) and find \(MR_1 = a - bQ_2 - 2bQ_1\).
2. Set \(MR_1 = MC_1 = c_1\) and solve for \(Q_1\): this is firm 1's **reaction function**, \(Q_1 = \frac{a - c_1}{2b} - \frac{1}{2}Q_2\).
3. Do the same for firm 2.
4. The **Cournot equilibrium** is where the two reaction functions cross: neither firm wants to change its output given the other's (a Nash equilibrium in quantities).

**Textbook Demonstration Problem 9-4:** \(P = 10 - (Q_1 + Q_2)\), zero costs.
- \(MR_1 = 10 - Q_2 - 2Q_1\). Set equal to 0: \(Q_1 = 5 - \frac{1}{2}Q_2\). Likewise \(Q_2 = 5 - \frac{1}{2}Q_1\).
- Solve: \(Q_1 = Q_2 = 10/3\). Total \(Q = 20/3\), price \(P = 10 - 20/3 = 10/3\).

**Shortcut for identical costs:** each firm produces \(\frac{a - c}{3b}\). (Unequal costs: \(Q_1 = \frac{a - 2c_1 + c_2}{3b}\).) None of these formulas is on the equation sheet; derive from MR = MC if you forget.

**Compared with other structures:** Cournot output is above the monopoly (collusion) level and below the competitive level, so P > MC. With more firms, price falls toward MC (textbook).

**Collusion is tempting but unstable.** Splitting the monopoly output earns more for both, but it is hard to achieve for **two** reasons (Session 21 reading quiz Q5): it is **often prohibited by law**, AND **every firm has an incentive to cheat given that the others follow the agreement**. If firm 2 sticks to its quota, firm 1's reaction function says produce more (Bryce p. 6). That is why OPEC members exceed their quotas.""",
 "why": "Practice exam Q14 and Q31 to Q34 and Comprehension Quiz 10 Q1 to Q5 are expected to test Cournot.",
 "definition": "Cournot oligopoly: a few firms producing homogeneous or differentiated products choose output simultaneously, each believing rivals hold output constant, with barriers to entry. Equilibrium is where the reaction functions intersect.",
 "formulas": [{"name": "Marginal revenue in Cournot duopoly", "tex": r"MR_1 = a - bQ_2 - 2bQ_1", "onSheet": False},
              {"name": "Cournot reaction function", "tex": r"Q_1 = \frac{a - c_1}{2b} - \frac{1}{2}Q_2", "onSheet": False},
              {"name": "Cournot output, identical costs", "tex": r"Q_1 = Q_2 = \frac{a - c}{3b}", "onSheet": False, "note": "Shortcut. Derive it if unsure."}],
 "derivation": r"Set \(MR_1 = c_1\): \(a - bQ_2 - 2bQ_1 = c_1\), so \(Q_1 = \frac{a - c_1}{2b} - \frac{Q_2}{2}\). With identical firms, put \(Q_2 = Q_1 = q\): \(q = \frac{a - c}{2b} - \frac{q}{2}\), so \(\frac{3}{2}q = \frac{a - c}{2b}\) and \(q = \frac{a - c}{3b}\).",
 "math": [DERIV, SOLVE2, PROFIT],
 "worked": [{"title": "Textbook comparison market", "problem": "P = 1,000 - (Q_1 + Q_2), each firm's cost is C = 4Q. Find the Cournot outputs, price and profit.",
   "steps": [r"Reaction: \(Q_1 = \frac{1000 - 4}{2} - \frac{1}{2}Q_2 = 498 - \frac{1}{2}Q_2\).", r"Identical firms: \(q = \frac{1000 - 4}{3} = 332\).", "Q = 664, P = 1,000 - 664 = $336.", "Profit = (336 - 4) × 332 = $110,224 each."], "answer": "332 each, P = $336, profit $110,224 each."}],
 "graph": {"component": "reaction", "params": {"mode": "quantity", "a": 1000, "b": 1, "c1": 4, "c2": 4}, "caption": "The textbook's comparison market. The reaction functions cross at the Cournot point (332, 332)."},
 "traps": ["MR for one firm has 2b on its OWN quantity and b on the rival's.",
           "Firms in Cournot choose QUANTITY; price comes from the demand curve.",
           "Cournot output per firm is (a - c)/(3b), not (a - c)/(2b) (that is the monopoly or Stackelberg leader output).",
           "Each firm assumes the rival's output stays fixed.",
           "Why is Cournot collusion hard? BOTH reasons: it is often illegal AND each firm wants to cheat (Session 21 reading quiz Q5)."],
 "sources": {"slides": "S21 slides not posted", "read": "Ch. 9: Cournot Oligopoly; Bryce pp. 4 to 6", "exercise": "Oligopoly Exercise (not yet available)", "quiz": "Session 21 Reading Quiz Q2, Q4, Q5; Comprehension Quiz 10 Q1 to Q5 (not yet available); Practice exam Q14, Q31 to Q34"}},

{"id": "S21-03", "title": "Stackelberg oligopoly", "calc": True,
 "plain": r"""In a **Stackelberg oligopoly**, one firm (the **leader**) chooses its output **first**; the other (the **follower**) sees it and then chooses its own output.

**Textbook conditions:** (1) few firms serving many consumers; (2) homogeneous or differentiated products; (3) a single firm, the leader, chooses an output before all other firms; (4) the followers take the leader's output as given; (5) barriers to entry.

**Bryce's description** (p. 8): a race to build or expand capacity in which one firm makes its capacity choice before the others. The follower builds a smaller plant and the leader a larger one: **a first-mover advantage** in which the leader takes a greater market share. Bryce calls it competition in **lead time** and gives no formal model.

**How to solve it** (backward induction, like S20):
1. The follower uses its ordinary Cournot reaction function: \(Q_2 = \frac{a - c_2}{2b} - \frac{1}{2}Q_1\).
2. The leader plugs that into the demand curve and maximizes its own profit. Result (textbook): \(Q_1 = \frac{a + c_2 - 2c_1}{2b}\). With identical costs this is \(\frac{a - c}{2b}\), the monopoly output.
3. Put \(Q_1\) into the follower's reaction function to get \(Q_2\).

**Textbook Demonstration Problem 9-6:** \(P = 50 - (Q_1 + Q_2)\), costs \(2Q_1\) and \(2Q_2\), firm 1 leads.
- Follower: \(Q_2 = 24 - \frac{1}{2}Q_1\).
- Leader: \(Q_1 = \frac{50 + 2 - 4}{2} = 24\).
- Follower: \(Q_2 = 24 - 12 = 12\). Price \(P = 50 - 36 = 14\).

**Compared with Cournot:** the leader produces more and earns more; the follower produces less and earns less; total output is higher and price lower. Textbook example (Inside Business 9-2): early generative AI firms raced to launch first with high volume.""",
 "why": "Practice exam Q35 and Comprehension Quiz 10 Q6 are expected to test Stackelberg; the Session 22 reading quiz Q4 and Q5 also cover it.",
 "definition": "Stackelberg oligopoly: a leader chooses output before the other firms; followers take the leader's output as given and maximize profit; few firms, homogeneous or differentiated products, barriers to entry.",
 "formulas": [{"name": "Stackelberg leader output", "tex": r"Q_1 = \frac{a + c_2 - 2c_1}{2b}", "onSheet": False},
              {"name": "Follower output (its Cournot reaction function)", "tex": r"Q_2 = \frac{a - c_2}{2b} - \frac{1}{2}Q_1", "onSheet": False}],
 "derivation": r"Leader profit: \(\pi_1 = \left[a - b\left(Q_1 + \frac{a - c_2}{2b} - \frac{Q_1}{2}\right)\right]Q_1 - c_1Q_1 = \left[\frac{a + c_2}{2} - \frac{b}{2}Q_1\right]Q_1 - c_1Q_1\). Derivative: \(\frac{a + c_2}{2} - bQ_1 - c_1 = 0\), so \(Q_1 = \frac{a + c_2 - 2c_1}{2b}\).",
 "math": [DERIV, PROFIT],
 "worked": [{"title": "Textbook comparison market", "problem": "P = 1,000 - (Q_1 + Q_2), C = 4Q for each firm, firm 1 leads. Find outputs, price and profits.",
   "steps": [r"Leader: \(Q_1 = \frac{1000 + 4 - 8}{2} = 498\).", r"Follower: \(Q_2 = \frac{1000 - 4}{2} - \frac{1}{2}(498) = 498 - 249 = 249\).", "Q = 747, P = 1,000 - 747 = $253.", "Leader profit (253 - 4) × 498 = $124,002; follower (253 - 4) × 249 = $62,001."],
   "answer": "Leader 498, follower 249, P = $253. The leader earns double the follower and more than a Cournot firm ($110,224)."}],
 "graph": {"component": "reaction", "params": {"mode": "quantity", "a": 50, "b": 1, "c1": 2, "c2": 2}, "caption": "Demonstration Problem 9-6. The Stackelberg point (24, 12) lies on the follower's reaction function, to the right of the Cournot point."},
 "traps": ["The follower uses its Cournot reaction function; the leader does NOT use its own reaction function.",
           "With identical costs, the leader produces the monopoly output (a - c)/(2b) and the follower half of that.",
           "Stackelberg total output is higher (price lower) than Cournot.",
           "Moving first only helps if the commitment is real (capacity already built)."],
 "sources": {"slides": "S21 slides not posted", "read": "Ch. 9: Stackelberg Oligopoly; Bryce p. 8", "exercise": "Oligopoly Exercise (not yet available)", "quiz": "Session 22 Reading Quiz Q4, Q5; Comprehension Quiz 10 Q6 (not yet available); Practice exam Q35"}},

{"id": "S21-04", "title": "Reaction function", "calc": True,
 "plain": r"""A **reaction function** (best-response function) gives a firm's profit-maximizing choice for **every** choice the rival might make. Bryce (p. 3): "a strategy is a set of actions for every possible rival move. For oligopolists, another name for the complete set of responses is a reaction function."

**In quantity competition (Cournot):** \(Q_1 = r_1(Q_2)\).
- If the rival produces 0, you produce the **monopoly** output (where \(R_1\) hits your own axis).
- As the rival produces more, the price falls and your MR falls, so you produce **less**: Cournot reaction functions **slope downward** (Bryce p. 5).
- Linear case: \(Q_1 = \frac{a - c_1}{2b} - \frac{1}{2}Q_2\). Each extra unit from the rival lowers your best output by half a unit.

**Bryce's footnote 6:** with \(P = a - q_1 - q_2\) and marginal cost c, revenue is \(aq_1 - q_1^2 - q_1q_2\), so \(MR = a - 2q_1 - q_2\), and setting MR = c gives \(q_1^* = \frac{a - q_2 - c}{2}\).

**The adjustment story** (Bryce p. 6): firm 1 thinks of producing its monopoly output; firm 2 best-responds (point a); firm 1 best-responds to that (b); and so on until point e, where reaction functions cross. That crossing is the **Cournot-Nash equilibrium**.

**Shifting the reaction function** (textbook Figure 9-8): a lower marginal cost raises \(\frac{a - c}{2b}\), so the reaction function shifts **out**. That firm produces more and the rival less. Example: \(P = 10 - Q\), MC = 2 for both gives (8/3, 8/3); if firm 2's MC falls to 0, the equilibrium becomes (2, 4).

**Isoprofit curves** (textbook): all output pairs that give a firm the same profit. Each one peaks where it crosses the firm's reaction function; curves closer to the firm's monopoly point mean higher profit.

**In price competition (differentiated Bertrand, S22):** reaction functions in prices slope **upward**.""",
 "why": "Practice exam Q31 and Q36 and Comprehension Quiz 10 Q1 are expected to use reaction functions.",
 "definition": "A reaction function gives a firm's profit-maximizing choice (output or price) for each possible choice of its rival.",
 "formulas": [{"name": "Cournot reaction function", "tex": r"Q_1 = r_1(Q_2) = \frac{a - c_1}{2b} - \frac{1}{2}Q_2", "onSheet": False}],
 "derivation": r"From \(MR_1 = a - bQ_2 - 2bQ_1 = c_1\): move \(2bQ_1\) to one side, \(2bQ_1 = a - c_1 - bQ_2\), and divide by 2b.",
 "math": [DERIV, SOLVE2],
 "worked": [{"title": "Best response to a rival's output", "problem": "P = 120 - 2(Q_1 + Q_2), MC = $20 for both. Find firm 1's reaction function and its best output if firm 2 produces 20.",
   "steps": [r"\(MR_1 = 120 - 2Q_2 - 4Q_1\). Set equal to 20.", r"\(4Q_1 = 100 - 2Q_2\), so \(Q_1 = 25 - \frac{1}{2}Q_2\).", r"If \(Q_2 = 20\): \(Q_1 = 25 - 10 = 15\)."], "answer": "Q_1 = 25 - 0.5 Q_2; best response to 20 is 15."},
  {"title": "Cost cut shifts the reaction function (textbook Figure 9-8)", "problem": "P = 10 - (Q_1 + Q_2), MC = 2 for both. Then firm 2's MC falls to 0. Find the equilibrium before and after.",
   "steps": [r"Before: \(q = \frac{10 - 2}{3} = 8/3\) each.", r"After: \(Q_1 = \frac{10 - 2(2) + 0}{3} = 2\), \(Q_2 = \frac{10 - 0 + 2}{3} = 4\).", r"Check on reaction functions: \(Q_1 = 4 - \frac{1}{2}(4) = 2\) and \(Q_2 = 5 - \frac{1}{2}(2) = 4\)."], "answer": "From (8/3, 8/3) to (2, 4): the lower-cost firm expands and the rival shrinks."}],
 "graph": {"component": "reaction", "params": {"mode": "quantity", "a": 10, "b": 1, "c1": 2, "c2": 2}, "caption": "Textbook Figure 9-8 setup. Lower firm 2's MC to 0 and watch its reaction function shift out."},
 "traps": ["A Cournot reaction function gives best OUTPUT for given OUTPUT levels of the rival, not input levels (Session 21 reading quiz Q3 is false for that reason).",
           "Cournot (quantity) reaction functions slope DOWN; differentiated Bertrand (price) reaction functions slope UP.",
           "Where your reaction function meets your own axis is the monopoly output, not zero.",
           "A lower own cost shifts your reaction function out; it does not move along it.",
           "The slope is -1/2 in the linear case: a 10 unit rise in rival output cuts your best output by 5."],
 "sources": {"slides": "S21 slides not posted", "read": "Ch. 9: Cournot Oligopoly (reaction functions, isoprofit curves, changes in marginal cost); Bryce pp. 3, 5 to 6", "exercise": "Oligopoly Exercise (not yet available)", "quiz": "Session 21 Reading Quiz Q3; Comprehension Quiz 10 Q1 (not yet available); Practice exam Q31, Q36"}},

{"id": "S21-05", "title": "Identifying Cournot or Stackelberg conditions", "calc": False,
 "plain": r"""To decide which model fits, look at **what firms compete with** (the strategic variable), **whether goods are alike**, and **who moves when**.

**Bryce's Figure 1, Types of Competition in Oligopoly** (p. 4):

""" + FIG1 + r"""

**Cournot fits when** (textbook conditions plus Bryce):
- a few firms serve many consumers, with barriers to entry;
- firms choose **output or capacity** and let the price float (commodities: oil, agriculture co-ops, corn wet milling);
- they choose **at the same time**;
- each believes rivals hold output constant.

**Stackelberg fits when:**
- the same, but **one firm commits to its output first** and the others see it before choosing (a race to build capacity where one firm clearly moves first, Bryce p. 8).
- The leader must be able to commit: built plants, signed contracts, launched products.

**Not Cournot or Stackelberg:**
- If firms set **prices** for identical goods and buyers see all prices: standard **Bertrand** (S22).
- If firms set **prices** for somewhat different goods: **differentiated Bertrand** (S22), the most common type today (Bryce p. 8).
- **Sweezy** (optional in the reading): firms believe rivals match price cuts but not price increases, giving a kinked demand curve and sticky prices.

**Bryce's three questions** (pp. 9 to 10): (1) How many firms are meaningfully in direct competition? (2) How much do the firms' target customers overlap? (3) What is the primary strategic variable (price, quantity, lead time, features)?""",
 "why": "Practice exam Q14 and Comprehension Quiz 10 Q4 and Q5 are expected to ask which model describes a market.",
 "definition": "A market fits Cournot when a few firms with barriers to entry choose quantities simultaneously, each taking rivals' outputs as given; it fits Stackelberg when one firm commits to its quantity first and followers take that output as given.",
 "formulas": [], "derivation": "", "math": [],
 "worked": [{"title": "Classify three markets", "problem": "(a) Four large potash mines each decide how much to mine this year without seeing the others' plans. (b) An established chipmaker finishes a giant new fab before a rival decides how big its fab will be. (c) Two online sellers of the same phone charger set prices on a comparison site.",
   "steps": ["(a) Quantity, simultaneous, homogeneous: Cournot.", "(b) Quantity (capacity), one firm commits first: Stackelberg.", "(c) Price, identical goods, buyers see all prices: standard Bertrand."], "answer": "Cournot, Stackelberg, standard Bertrand."}],
 "traps": ["'Each manager charges a price that is a best response to the rival's price' is NOT Cournot; Cournot is quantity as a best response to the rival's quantity (Session 21 reading quiz Q4).",
           "Quantity versus price is the first question: Cournot and Stackelberg are quantity (capacity) models.",
           "Simultaneous quantity choice = Cournot; sequential with a committed leader = Stackelberg.",
           "Cournot allows homogeneous OR differentiated goods in the textbook's conditions; Bryce's figure puts the classic case in homogeneous goods.",
           "Bryce: Stackelberg is the least realistic model and the professor's reading gives it no formal model."],
 "sources": {"slides": "S21 slides not posted", "read": "Ch. 9: Conditions for Oligopoly; Cournot; Stackelberg; Bryce pp. 3 to 4, 8 to 10", "exercise": "Oligopoly Exercise (not yet available)", "quiz": "Session 21 Reading Quiz Q2, Q4; Comprehension Quiz 10 Q4, Q5 (not yet available); Practice exam Q14"}},

{"id": "S21-06", "title": "Optimal decisions and competitor responses (Cournot and Stackelberg)", "calc": True,
 "plain": r"""This objective puts S21-02 to S21-04 to work. The typical exam steps:

**1. Best response to a given rival output.** Use your reaction function. Rival makes \(Q_2\); you make \(Q_1 = \frac{a - c_1}{2b} - \frac{1}{2}Q_2\).

**2. Cournot equilibrium.** Solve both reaction functions; with identical costs each makes \(\frac{a - c}{3b}\). Price from demand, profit \((P - c)Q\).

**3. Stackelberg.** Leader \(Q_1 = \frac{a + c_2 - 2c_1}{2b}\), follower from its reaction function.

**4. Collusion and cheating.** Joint monopoly: \(Q = \frac{a - c}{2b}\), split evenly. If the rival keeps its quota, your best response is on your reaction function, which is **more** than the quota: cheating pays in a one-shot game (S20 explains when repetition holds it together).

**5. Predicting responses.** A cost cut shifts your reaction function out: you produce more and your rival responds by producing less. A bigger rival output means you produce less.

**The textbook's comparison** of one market, \(P = 1{,}000 - (Q_1 + Q_2)\), \(C_i = 4Q_i\):

""" + BOOK + r"""

**Pattern:** output rises and price falls from collusion to Cournot to Stackelberg to Bertrand. The Stackelberg leader earns as much as a colluding firm; the follower earns the least among the quantity models; Bertrand firms earn zero.""",
 "why": "Practice exam Q31 to Q35 and Comprehension Quiz 10 Q1 to Q3, Q5 and Q6 are expected to be calculations like these.",
 "definition": "Optimal decisions in quantity oligopolies come from setting MR = MC given rivals' outputs (Cournot) or given the follower's reaction function (Stackelberg leader); rivals respond along their reaction functions.",
 "formulas": [{"name": "Cournot output with unequal costs", "tex": r"Q_1 = \frac{a - 2c_1 + c_2}{3b}", "onSheet": False},
              {"name": "Joint monopoly (collusion) output", "tex": r"Q_M = \frac{a - c}{2b}", "onSheet": False, "note": "From MR = a - 2bQ = c; each colluder makes half."}],
 "derivation": r"Unequal costs: substitute \(Q_2 = \frac{a - c_2}{2b} - \frac{Q_1}{2}\) into \(Q_1 = \frac{a - c_1}{2b} - \frac{Q_2}{2}\): \(Q_1 = \frac{a - c_1}{2b} - \frac{a - c_2}{4b} + \frac{Q_1}{4}\), so \(\frac{3}{4}Q_1 = \frac{a - 2c_1 + c_2}{4b}\) and \(Q_1 = \frac{a - 2c_1 + c_2}{3b}\).",
 "math": [DERIV, SOLVE2, PROFIT],
 "worked": [{"title": "Collusion and cheating", "problem": "P = 120 - 2(Q_1 + Q_2), MC = $20 for both. (a) Cournot outputs and profit. (b) Collusive outputs and profit. (c) Firm 1's profit if it cheats while firm 2 keeps its quota.",
   "steps": [r"(a) \(q = \frac{100}{6} = 16.67\); Q = 33.33, P = $53.33; profit = 33.33 × 16.67 = $555.56 each.", r"(b) \(MR = 120 - 4Q = 20\) gives Q = 25 (12.5 each), P = $70; profit = 50 × 12.5 = $625 each.", r"(c) \(Q_1 = 25 - \frac{1}{2}(12.5) = 18.75\); Q = 31.25, P = $57.50; profit = 37.5 × 18.75 = $703.13."],
   "answer": "Cheating earns $703.13 > $625, so the cartel is unstable in a one-shot game."},
  {"title": "Unequal costs", "problem": "P = 100 - (Q_1 + Q_2), MC_1 = $10, MC_2 = $25. Find the Cournot outputs and price.",
   "steps": [r"\(Q_1 = \frac{100 - 20 + 25}{3} = 35\).", r"\(Q_2 = \frac{100 - 50 + 10}{3} = 20\).", "P = 100 - 55 = $45."], "answer": "Low-cost firm 35, high-cost firm 20, P = $45."}],
 "graph": {"component": "reaction", "params": {"mode": "quantity", "a": 120, "b": 2, "c1": 20, "c2": 20}, "caption": "The table under the graph compares collusion, Cournot, Stackelberg and Bertrand for the same market. Change the costs to see the responses."},
 "traps": ["Collusion splits the MONOPOLY output (a - c)/(2b), not the Cournot output.",
           "A cheater's best response comes from its reaction function with the rival at the quota.",
           "Profit is (P - c) × own Q, using the market price from total output.",
           "Lower own cost: produce more; the rival responds by producing less (not more)."],
 "sources": {"slides": "S21 slides not posted", "read": "Ch. 9: Cournot; Stackelberg; Comparing Oligopoly Models", "exercise": "Oligopoly Exercise (not yet available)", "quiz": "Session 21 Reading Quiz Q5; Comprehension Quiz 10 Q1 to Q3, Q5, Q6 (not yet available); Practice exam Q31 to Q35"}},
]
for L in LESSONS: write_lesson(L)
write_session("S21", {"overview": "Session 21 starts oligopoly: a few interdependent firms, each maximizing profit with MR = MC while accounting for rivals. In Cournot, firms choose quantities at the same time; each firm's reaction function gives its best output for every rival output, and the equilibrium is where they cross. In Stackelberg, a leader commits to output first and the follower responds, so the leader produces and earns more. Collusion (splitting monopoly output) earns more but invites cheating.",
  "provisional": "**Provisional.** The S21 slides were not posted and there are no class notes yet. The Session 21 reading quiz (5 professor questions) is included. These lessons are built from the textbook (Ch. 9, pp. 274 to 292), the professor's assigned reading *Rivalry in Oligopoly* (Bryce), and the study guide objectives. Worked numbers labeled textbook come from the book; others are made up for practice. Update with /ingest when the Oligopoly Exercise, Comprehension Quiz 10 or review materials arrive."})
print([L["id"] for L in LESSONS])
