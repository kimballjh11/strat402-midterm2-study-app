from common import *
from S19_lessons import mat, VISA, DILL, MON, MON2, COORD, GOLD, ADV
B = Bank()

def nash(pay):
    R, C = len(pay), len(pay[0]); out = []
    for i in range(R):
        for j in range(C):
            if pay[i][j][0] == max(pay[k][j][0] for k in range(R)) and pay[i][j][1] == max(pay[i][k][1] for k in range(C)): out.append((i, j))
    return out
def dom_row(pay):
    R, C = len(pay), len(pay[0])
    for i in range(R):
        if all(pay[i][j][0] > pay[k][j][0] for j in range(C) for k in range(R) if k != i): return i
    return None
def dom_col(pay):
    R, C = len(pay), len(pay[0])
    for j in range(C):
        if all(pay[i][j][1] > pay[i][k][1] for i in range(R) for k in range(C) if k != j): return j
    return None
def mixed(pay):
    """p = P(row plays top) making column indifferent; q = P(column plays left) making row indifferent."""
    c11, c12, c21, c22 = pay[0][0][1], pay[0][1][1], pay[1][0][1], pay[1][1][1]
    r11, r12, r21, r22 = pay[0][0][0], pay[0][1][0], pay[1][0][0], pay[1][1][0]
    p = (c22 - c21) / ((c11 - c21) - (c12 - c22)); q = (r22 - r12) / ((r11 - r12) - (r21 - r22))
    return p, q

def ne_mc(lo, los, kind, intro, rp, cp, rows, cols, pay, explain):
    """MC: which cell is the Nash equilibrium. Answer computed, not typed."""
    ne = nash(pay); assert len(ne) == 1, (intro, ne)
    i, j = ne[0]
    cells = [(a, b) for a in range(len(rows)) for b in range(len(cols))]
    others = [c for c in cells if c != (i, j)][:3]
    ch = [f"{rp} {rows[a]}, {cp} {cols[b]}" for a, b in [(i, j)] + others]
    B.mc(lo, los, kind, intro + "\n\n" + mat(rp, cp, rows, cols, pay) + "\n\nWhat is the Nash equilibrium?", ch, 0, explain)

PD = [[(0, 0), (12, -1)], [(-1, 12), (10, 10)]]
UNI = [[(8, 3), (12, 9)], [(5, 6), (4, 2)]]
BOOK = [[(10, 20), (15, 8)], [(-10, 7), (10, 10)]]

# ---------------- S19-01 simultaneous-move games ----------------
lo = "S19-01"
B.mc(lo, [lo], "concept", "In a simultaneous-move game:", ["Each player decides without knowing the other's decision", "One player moves after seeing the other's move", "Players must move at exactly the same moment", "The game is always played once"], 0,
     "What matters is information: neither knows the other's choice. Moving after observing is sequential. One-shot versus repeated is a separate question.")
B.mc(lo, [lo], "concept", "What does interdependence mean in game theory?", ["Each player's payoff depends on the other players' choices", "Players cooperate by law", "Players move in sequence", "Payoffs are always equal"], 0, "A firm's best move depends on its rivals' moves.")
B.mc(lo, [lo], "concept", "Which three elements make up a game?", ["Players, strategies and payoffs", "Price, quantity and cost", "Supply, demand and equilibrium", "Rows, columns and totals"], 0, "Who decides, what they can choose, and what each outcome pays.")
B.tf(lo, [lo], "concept", "True or false: A one-shot game is played only once, while a repeated game is played more than once.", True, "True. Repeated games are Session 20.")
B.mc(lo, [lo], "concept", "Why is game theory especially useful for oligopoly?", ["A few firms' profits depend on each other's actions", "Firms in oligopoly are price takers", "There is only one firm", "Products are always identical"], 0, "In perfect competition firms are too small to affect each other; a monopolist has no rival.")
B.mc(lo, [lo], "apply", "Two construction firms submit sealed bids for a city contract. Neither sees the other's bid before the deadline. What kind of game is this?", ["Simultaneous-move, one-shot", "Sequential-move, one-shot", "Sequential-move, repeated", "Not a game"], 0, "Sealed bids mean neither knows the other's choice; this contract is bid once.")
B.mc(lo, [lo], "apply", "A grocery chain waits to see its rival's weekly ad before setting its own sale prices. What kind of game is this week's pricing decision?", ["Sequential-move", "Simultaneous-move", "Mixed strategy", "Coordination"], 0, "It observes the rival's choice before deciding.")
B.mc(lo, [lo, "S19-06"], "apply", "Visa and Mastercard each decide whether to lower merchant fees, without knowing what the other will announce. Why is game theory needed to predict Visa's choice?", ["Visa's best fee depends on what Mastercard does", "Visa is a monopoly", "Visa's fee does not affect its profit", "Mastercard always moves first"], 0, "Interdependence: each card network's profit depends on both fees.")

B.tf(lo, [lo], "concept", "True or false: A simultaneous-move game is a game in which players make decisions without knowledge of the other players' decisions.", True, "True. It is about information, not the clock.")
B.mc(lo, [lo, "S19-06"], "apply", "Coke and Pepsi each set their summer prices in sealed plans sent to retailers on the same day. Later in the year they will set prices again. How should you model this summer's decision?", ["A simultaneous-move game (one round of a repeated game)", "A sequential-move game", "A monopoly decision", "A game with one player"], 0, "Neither sees the other's plan before committing. The yearly repetition makes it part of a repeated game (S20).")
B.mc(lo, [lo], "apply", "Facebook and Twitter each decide in 2019 whether to ban political ads, without knowing the other's decision. In the Game Theory Exercise Part 1, how is this first modeled?", ["As a one-shot simultaneous game", "As a sequential game with Twitter first", "As a repeated game", "As a mixed strategy game"], 0, "Part 1 sets it up as a one-shot simultaneous game; Part 2 re-models it as a sequential game with Twitter moving first.")

# ---------------- S19-02 normal form ----------------
lo = "S19-02"
B.mc(lo, [lo], "concept", "In a payoff matrix, the first number in each cell is:", ["The row player's payoff", "The column player's payoff", "The sum of both payoffs", "The probability of that outcome"], 0, "By convention: row player first, column player second.")
B.tf(lo, [lo], "concept", "True or false: A normal-form game must have exactly two strategies for each player.", False, "False. A player can have 3 or more strategies (a 3 by 3 matrix, for example).")
B.mc(lo, [lo], "concept", "The normal form is best suited to which kind of game?", ["Simultaneous-move games", "Sequential-move games only", "Games with one player", "Repeated games only"], 0, "Sequential games are usually drawn as game trees (extensive form, S20).")
B.mc(lo, [lo], "concept", "To compare the column player's payoffs from its two strategies, you:", ["Hold the row fixed and compare the second numbers across that row", "Hold the column fixed and compare the first numbers down that column", "Add the numbers in each cell", "Compare the first numbers across a row"], 0, "The column player chooses a column, so you look across a row at its (second) numbers.")
B.mc(lo, [lo], "concept", "In the Visa (rows) versus Mastercard (columns) matrix, the cell (Lower, Maintain) shows (4, 1). What does the 1 mean?", ["Mastercard earns 1 when Visa lowers and Mastercard maintains", "Visa earns 1 when it lowers", "Both earn 1", "Mastercard earns 1 when it lowers"], 0, "Second number = column player = Mastercard.")
B.num(lo, [lo], "Using the Visa matrix:\n\n" + VISA + "\n\nWhat does Mastercard earn if Visa maintains its fee and Mastercard lowers its fee?", 4, "Row Maintain Fee, column Lower Fee: cell (1, 4). Second number = Mastercard = 4.", {"f": "cell", "pay": [[[2, 2], [4, 1]], [[1, 4], [3, 3]]], "i": 1, "j": 0, "who": 1}, kind="apply")
B.num(lo, [lo], "Using the Dillard's (rows) versus Nordstrom (columns) matrix:\n\n" + DILL + "\n\nWhat does Dillard's earn if Dillard's features Women's and Nordstrom features Girl's?", 6, "Row Women's, column Girl's: (6, 4). First number = Dillard's = 6.", {"f": "cell", "pay": [[[2, 1], [4, 2]], [[6, 4], [3, 5]]], "i": 1, "j": 0, "who": 0}, kind="apply")
B.mc(lo, [lo], "apply", "Two firms choose High or Low output. If both choose High, A earns 1 and B earns 2. If A chooses High and B Low, A earns 20 and B earns 5. Writing A on the rows, which cell is (High, Low)?", ["(20, 5)", "(5, 20)", "(1, 2)", "(2, 1)"], 0, "Row player A first: A's 20, then B's 5.")

# ---------------- S19-03 dominant strategy ----------------
lo = "S19-03"
B.mc(lo, [lo], "concept", "A dominant strategy is:", ["A strategy that gives the highest payoff regardless of the opponent's action", "The strategy that gives the highest number in the matrix", "The strategy the opponent is currently playing", "A strategy that guarantees the best worst case"], 0, "Best against EVERY opposing choice. The best worst case is the secure (maximin) strategy.")
B.tf(lo, [lo], "concept", "True or false: Every player in every game has a dominant strategy.", False, "False. Dillard's has none in the in-class exercise.")
B.mc(lo, [lo], "concept", "If you have no dominant strategy but your rival does, the textbook says you should:", ["Assume the rival plays its dominant strategy and choose your best response to it", "Pick randomly", "Copy the rival's strategy", "Choose your secure strategy"], 0, "Put yourself in your rival's shoes.")
B.mc(lo, [lo], "concept", "A secure (maximin) strategy:", ["Guarantees the highest payoff in the worst case", "Is always the same as a dominant strategy", "Maximizes the opponent's payoff", "Is the Nash equilibrium"], 0, "It is cautious and can ignore what a rational rival will actually do.")
B.mc(lo, [lo], "concept", "A strategy is dominated if:", ["Another strategy gives a higher payoff against every opposing choice", "It gives a negative payoff somewhere", "The rival prefers it", "It is never part of an equilibrium in any game"], 0, "A rational player never plays a strictly dominated strategy, so it can be crossed out.")
for (stem, rp, cp, rows, cols, pay) in [
    ("Firm X (rows) and Firm Y (columns):", "X", "Y", ["Top", "Bottom"], ["Left", "Right"], UNI),
    ("Player A (rows) and Player B (columns):", "A", "B", ["Up", "Down"], ["Left", "Right"], BOOK),
    ("Dillard's (rows) and Nordstrom (columns):", "Dillard's", "Nordstrom", ["Girl's", "Women's"], ["Girl's", "Women's"], [[(2, 1), (4, 2)], [(6, 4), (3, 5)]])]:
    dr, dc = dom_row(pay), dom_col(pay)
    right = f"Only {rp} ({rows[dr]})" if dr is not None and dc is None else f"Only {cp} ({cols[dc]})" if dc is not None and dr is None else "Both" if dr is not None else "Neither"
    opts = [f"Only {rp} ({rows[dr if dr is not None else 0]})", f"Only {cp} ({cols[dc if dc is not None else 0]})", "Both players", "Neither player"]
    key = 0 if right.startswith("Only " + rp) else 1 if right.startswith("Only " + cp) else 2 if right == "Both" else 3
    rowtxt = "; ".join(f"vs {c}: {rows[max(range(2), key=lambda i: pay[i][j][0])]}" for j, c in enumerate(cols))
    coltxt = "; ".join(f"vs {r}: {cols[max(range(2), key=lambda j: pay[i][j][1])]}" for i, r in enumerate(rows))
    B.mc(lo, [lo, "S19-02"], "calc", stem + "\n\n" + mat(rp, cp, rows, cols, pay) + "\n\nWho has a dominant strategy?", opts, key,
         f"{rp}'s best responses: {rowtxt}. {cp}'s best responses: {coltxt}. A player whose best response never changes has a dominant strategy.")
B.mc(lo, [lo], "apply", "Using the Visa matrix:\n\n" + VISA + "\n\nWhy is Lower Fee dominant for Visa?", ["It pays more whether Mastercard lowers (2 > 1) or maintains (4 > 3)", "It gives Visa the highest number in the table", "Mastercard lowers its fee", "It maximizes the total payoff"], 0, "Slide p. 22: no matter what Mastercard does, Visa's best option is to lower.")
B.mc(lo, [lo], "apply", "Nordstrom's dominant strategy is to feature Women's. What should Dillard's do?\n\n" + DILL, ["Feature Girl's, its best response to Women's (4 > 3)", "Feature Women's, since 6 is the biggest payoff", "Randomize 50/50", "Copy Nordstrom"], 0, "Expect the rival to play its dominant strategy and best-respond. 6 is only available if Nordstrom picks Girl's, which it will not.")
B.mc(lo, [lo], "apply", "In the 3 by 3 game below, which column strategy is strictly dominated?\n\n" + mat("Row", "Column", ["Top", "Middle", "Bottom"], ["Left", "Center", "Right"], [[(4, 3), (5, 1), (6, 2)], [(2, 1), (8, 4), (3, 6)], [(3, 0), (9, 6), (2, 8)]]),
     ["Center (Right beats it in every row)", "Left", "Right", "None"], 0, "Column payoffs: Center 1, 4, 6 versus Right 2, 6, 8. Right is higher in every row.")

# ---------------- S19-04 Nash equilibrium ----------------
lo = "S19-04"
B.mc(lo, [lo], "concept", "A Nash equilibrium is a set of strategies in which:", ["No player can improve his or her payoff by unilaterally changing strategy", "Both players get their highest possible payoff", "Players can improve by changing together", "Each player uses a dominant strategy"], 0, "Slide p. 32. It need not be the best outcome, and players need not have dominant strategies.")
B.tf(lo, [lo], "concept", "True or false: A Nash equilibrium is always the outcome that gives the players the highest combined payoff.", False, "False. In the Visa game the equilibrium (2, 2) is worse for both than (3, 3).")
B.tf(lo, [lo], "concept", "True or false: A game can have more than one pure-strategy Nash equilibrium.", True, "True. Coordination games have several.")
B.mc(lo, [lo], "concept", "In the underline method, a cell is a Nash equilibrium when:", ["Both numbers in it are underlined as best responses", "Its first number is the largest in the matrix", "Its two numbers are equal", "At least one number is underlined"], 0, "Each player must be best-responding to the other.")
B.mc(lo, [lo, "S19-06"], "concept", "Visa and Mastercard would both be better off maintaining fees. Why can't they agree to do so in a one-shot game?", ["Each has an incentive to defect from the agreement", "Agreements are always illegal", "Maintaining is a dominant strategy", "Payoffs are unknown"], 0, "Slide p. 36: both would have an incentive to defect.")
ne_mc(lo, [lo], "calc", "Visa (rows) and Mastercard (columns), from the slides:", "Visa", "Mastercard", ["Lower", "Maintain"], ["Lower", "Maintain"], [[(2, 2), (4, 1)], [(1, 4), (3, 3)]],
      "Both have the dominant strategy Lower, so (Lower, Lower) = (2, 2). At (Maintain, Maintain) each could switch to Lower and get 4.")
ne_mc(lo, [lo], "calc", "Dillard's (rows) and Nordstrom (columns), from the in-class exercise:", "Dillard's", "Nordstrom", ["Girl's", "Women's"], ["Girl's", "Women's"], [[(2, 1), (4, 2)], [(6, 4), (3, 5)]],
      "Nordstrom's dominant strategy is Women's; Dillard's best response is Girl's (4 > 3). Check Nordstrom: given Girl's, Women's 2 > 1.")
ne_mc(lo, [lo], "calc", "Firm X (rows) and Firm Y (columns):", "X", "Y", ["Top", "Bottom"], ["Left", "Right"], UNI,
      "Top is dominant for X (8 > 5, 12 > 4). Y's best response to Top is Right (9 > 3).")
ne_mc(lo, [lo], "calc", "Player A (rows) and Player B (columns), textbook Table 10-1:", "A", "B", ["Up", "Down"], ["Left", "Right"], BOOK,
      "Up is dominant for A (10 > -10, 15 > 10). B's best response to Up is Left (20 > 8).")
ne_mc(lo, [lo], "calc", "Row (rows) and Column (columns), a 3 by 3 game:", "Row", "Column", ["Top", "Middle", "Bottom"], ["Left", "Center", "Right"], [[(4, 3), (5, 1), (6, 2)], [(2, 1), (8, 4), (3, 6)], [(3, 0), (9, 6), (2, 8)]],
      "Underline: Row's best vs Left is Top (4), vs Center Bottom (9), vs Right Top (6). Column's best vs Top is Left (3), vs Middle Right (6), vs Bottom Right (8). Only (Top, Left) has both.")
B.mc(lo, [lo], "calc", "How many pure-strategy Nash equilibria does this game have?\n\n" + COORD, ["2", "1", "0", "4"], 0, "(USB-C, USB-C) and (Proprietary, Proprietary): matching is each firm's best response.")
B.mc(lo, [lo], "calc", "How many pure-strategy Nash equilibria does the employee monitoring game have?\n\n" + MON, ["0", "1", "2", "4"], 0, "Every cell has one player who wants to switch, so there is no pure equilibrium. Players randomize.")

B.mc(lo, [lo], "apply", "Two coffee chains each pick a new store location: Downtown or Campus. Each earns 5 if they pick different spots and 2 if they pick the same spot. Which outcomes are Nash equilibria?", ["(Downtown, Campus) and (Campus, Downtown)", "(Downtown, Downtown) only", "(Campus, Campus) only", "There is none"], 0, "If the rival is Downtown, your best is Campus (5 > 2), and vice versa. Splitting up is stable either way.")
B.mc(lo, [lo, "S19-06"], "apply", "In a Nash equilibrium, a manager says, \"We could earn more if our rival changed its price.\" Does that mean the outcome is not a Nash equilibrium?", ["No; Nash only requires that no player gains by changing ITS OWN strategy", "Yes; any player who could earn more means no equilibrium", "Yes; equilibria maximize total profit", "No; Nash equilibria require both players to earn the same"], 0, "The test is unilateral deviation, not whether a better outcome exists.")

# ---------------- S19-05 mixed strategies ----------------
lo = "S19-05"
B.mc(lo, [lo], "concept", "A mixed (randomized) strategy is:", ["Randomizing over actions to keep rivals from predicting your move", "Choosing the action with the highest average payoff", "Mixing two products in one market", "Alternating actions in a fixed pattern"], 0, "Slide p. 44. A fixed pattern is predictable, which defeats the purpose.")
B.mc(lo, [lo], "concept", "When are mixed strategies most useful?", ["When there is no pure-strategy Nash equilibrium", "When both players have dominant strategies", "In coordination games where both want to match", "When payoffs are all equal"], 0, "Monitoring, penalty kicks, rock paper scissors: each side gains by being unpredictable.")
B.tf(lo, [lo], "concept", "True or false: In a mixed strategy equilibrium, each player randomizes so that the OTHER player is indifferent between his or her actions.", True, "True. If the other player strictly preferred one action, you could be exploited.")
B.mc(lo, [lo], "concept", "Which slide example is a game with no pure-strategy Nash equilibrium?", ["Employee monitoring", "Visa versus Mastercard", "Dillard's versus Nordstrom", "Kellogg's versus General Mills"], 0, "The others each have a pure equilibrium.")
B.tf(lo, [lo], "concept", "True or false: The mixed strategy formulas are printed on the equation sheet.", False, "False. Set up the expected payoffs and solve.")
B.mc(lo, [lo], "concept", "In the Princess Bride scene, why should Westley not always poison the same cup?", ["If Vizzini could predict it, he would drink from the safe cup", "Poison only works in one cup", "Westley has a dominant strategy", "The game has a pure Nash equilibrium"], 0, "Predictability is exploited in a game with no pure equilibrium.")
p, q = mixed([[(6, 3), (8, 0)], [(10, 3), (2, 4)]]); assert abs(p - 0.25) < 1e-9 and abs(q - 0.6) < 1e-9
B.num(lo, [lo], "Boss (rows) and Employee (columns):\n\n" + MON2 + "\n\nThe boss monitors with probability p. What value of p makes the employee indifferent between working and shirking?", p,
      "Employee's payoff from Work: 3p + 3(1 - p) = 3. From Shirk: 0p + 4(1 - p) = 4 - 4p. Set equal: 3 = 4 - 4p, p = 0.25.", {"f": "mix_p", "pay": [[[6, 3], [8, 0]], [[10, 3], [2, 4]]]})
B.num(lo, [lo], "Same game. The employee works with probability q. What value of q makes the boss indifferent between monitoring and not?", q,
      "Boss from Monitor: 6q + 8(1 - q) = 8 - 2q. From Don't: 10q + 2(1 - q) = 2 + 8q. Set equal: 6 = 10q, q = 0.6.", {"f": "mix_q", "pay": [[[6, 3], [8, 0]], [[10, 3], [2, 4]]]})
B.num(lo, [lo], "Same game. In the mixed equilibrium (q = 0.6), what is the boss's expected payoff?", 8 - 2 * 0.6,
      "Monitor: 6(0.6) + 8(0.4) = 3.6 + 3.2 = 6.8. Don't monitor gives the same: 10(0.6) + 2(0.4) = 6.8.", {"f": "mix_val_row", "pay": [[[6, 3], [8, 0]], [[10, 3], [2, 4]]]})
B.num(lo, [lo], "Employee monitoring from the slides:\n\n" + MON + "\n\nWith what probability should the boss monitor?", 0.5,
      "Employee: Work = 1p - 1(1 - p) = 2p - 1; Shirk = -1p + 1(1 - p) = 1 - 2p. Equal when p = 0.5.", {"f": "mix_p", "pay": [[[-1, 1], [1, -1]], [[1, -1], [-1, 1]]]})
B.num(lo, [lo], "A kicker shoots Left with probability p. The chance of scoring is 0.4 if kicker Left and goalie Left, 0.9 if Left/Right, 0.8 if Right/Left, 0.3 if Right/Right. What p makes the goalie indifferent between diving Left and Right?", 0.5,
      "Goalie Left: scoring = 0.4p + 0.8(1 - p) = 0.8 - 0.4p. Goalie Right: 0.9p + 0.3(1 - p) = 0.3 + 0.6p. Equal: 0.5 = p.", {"f": "mix_p", "pay": [[[0.4, 0.6], [0.9, 0.1]], [[0.8, 0.2], [0.3, 0.7]]]})
B.mc(lo, [lo], "apply", "A tax agency audits some returns at random rather than following a published rule. Which concept explains this?", ["A mixed strategy keeps taxpayers from predicting audits", "A dominant strategy", "A coordination game", "Limit pricing"], 0, "A predictable rule would let cheaters avoid it, like the monitoring game.")
B.mc(lo, [lo], "apply", "In a mixed strategy equilibrium, the boss's monitoring probability is determined by:", ["The employee's payoffs", "The boss's own payoffs", "Which payoff is largest", "The average of all payoffs"], 0, "It must make the employee indifferent, so it is pinned down by the employee's payoffs.")
B.mc(lo, [lo], "apply", "A boss monitors 60% of the time. At that rate the employee strictly prefers to work. Is the boss using the equilibrium mix?", ["No; in equilibrium the employee is indifferent, so the boss could monitor less and save cost", "Yes; the employee works", "Yes; any mix is an equilibrium", "No; the boss should always monitor"], 0, "If the employee strictly prefers working, the boss is monitoring more than needed.")

# ---------------- S19-06 applications ----------------
lo = "S19-06"
B.mc(lo, [lo], "concept", "In a prisoner's dilemma:", ["Each player's dominant strategy leads to an outcome worse for both than cooperating", "Players have no dominant strategies", "There are many Nash equilibria", "Cooperation is the equilibrium"], 0, "Visa and Mastercard: (Lower, Lower) = (2, 2) versus (3, 3).")
B.mc(lo, [lo], "concept", "Why do firms in a coordination game not want to cheat once they agree on a standard?", ["Matching the other's choice is already each firm's best response", "Cheating is illegal", "Coordination games have no equilibrium", "They have a dominant strategy to defect"], 0, "Unlike pricing, the agreed outcome is itself a Nash equilibrium.")
B.mc(lo, [lo], "concept", "When does advertising become a prisoner's dilemma?", ["When ads mostly steal customers from rivals rather than grow the market", "When ads grow total demand a lot", "When only one firm can advertise", "When advertising is free"], 0, "Both advertise, the effects cancel, and both earn less.")
B.mc(lo, [lo], "concept", "In Golden Balls, why is Steal never worse than Split for a player?", ["Steal pays the whole jackpot if the other splits and the same zero if the other steals", "Split always pays zero", "Players must split by rule", "Steal is dominated"], 0, "Steal gives 100 vs 50 if the other splits and 0 vs 0 if the other steals.")
B.mc(lo, [lo], "concept", "Why are Nash bargaining outcomes hard to predict?", ["Every split that exactly uses the pie is an equilibrium", "There is no equilibrium", "Only a 50-50 split is an equilibrium", "One side always gets everything"], 0, "Many equilibria; stalemates are common.")
ne_mc(lo, [lo, "S19-04"], "calc", "Kellogg's (rows) and General Mills (columns), $ billions (Comprehension Quiz 9):", "Kellogg's", "General Mills", ["Advertise", "Don't"], ["Advertise", "Don't"], [[(0, 0), (44, -4)], [(-4, 44), (4, 4)]],
      "Advertise is dominant for each (0 > -4, 44 > 4). Both advertise and earn 0, although both would earn 4 by not advertising.")
ne_mc(lo, [lo, "S19-04"], "calc", "Two firms set prices (textbook-style pricing game):", "Firm A", "Firm B", ["Low price", "High price"], ["Low price", "High price"], PD,
      "Low is dominant for each (0 > -1, 12 > 10), so both price low at (0, 0), even though (10, 10) is better for both.")
B.num(lo, [lo], "In the pricing game where both pricing low pays (0, 0) and both pricing high pays (10, 10), how much combined profit do the two firms lose by ending up at the Nash equilibrium?", 20,
      "Cooperative total 10 + 10 = 20; equilibrium total 0 + 0 = 0. They lose 20.", {"f": "pd_loss", "pay": [[[0, 0], [12, -1]], [[-1, 12], [10, 10]]]})
B.num(lo, [lo], "Kellogg's versus General Mills ($ billions): both advertise (0, 0); neither (4, 4); one advertises (44, -4). How much does Kellogg's gain by defecting (advertising) if General Mills keeps an agreement not to advertise?", 40,
      "Keeping the agreement: 4. Defecting: 44. Gain 44 - 4 = $40 billion this period, which is why the one-shot agreement fails.", {"f": "diff", "x1": 4, "x2": 44}, unit="$ billions")
B.num(lo, [lo], "Two networks each earn 40 if both pick USB-C or both pick a proprietary plug, and 5 each if they mismatch. If they fail to coordinate, how much does each lose compared with coordinating?", 35,
      "40 - 5 = 35 each. The challenge is reaching an equilibrium, not resisting cheating.", {"f": "diff", "x1": 5, "x2": 40})
B.mc(lo, [lo], "apply", "Two airlines each decide whether to cut fares on a route for the holidays. Each earns more by cutting if the other does not, but both earn less if both cut than if neither does. What should you predict in a one-shot game?", ["Both cut fares", "Neither cuts", "One cuts and one does not", "They randomize"], 0, "Cutting is dominant for each: a pricing prisoner's dilemma.")
B.mc(lo, [lo], "apply", "Two appliance makers must choose an outlet voltage. Each earns 100 if they match and 0 if they do not. What helps them reach a good outcome?", ["Communicating or a government standard", "Secret randomization", "Predatory pricing", "Always choosing the opposite of the rival"], 0, "A coordination game: agreement helps, and once agreed, no one cheats.")

# ---------------- Game Theory Exercise (submitted) ----------------
import GTX
B.mc("S19-04", ["S19-04", "S19-03"], "calc", "Game Theory Exercise Part 1 (payoffs in $ millions, Facebook, Twitter):\n\n" + GTX.matrix(GTX.P1) + "\n\nWhat is the Nash equilibrium?",
     ["Facebook Don't Ban, Twitter Ban (-277, -3)", "Both ban (-350, -3)", "Neither bans (-280, -12)", "Facebook Ban, Twitter Don't Ban (-350, 23)"], 0,
     "Facebook's Don't Ban is dominant; Twitter's best response to it is Ban (-3 > -12).")
B.mc("S19-03", ["S19-03"], "calc", "Game Theory Exercise Part 1:\n\n" + GTX.matrix(GTX.P1) + "\n\nWho has a dominant strategy?",
     ["Only Facebook (Don't Ban)", "Only Twitter (Ban)", "Both players", "Neither player"], 0,
     "Facebook: -277 > -350 and -280 > -350. Twitter: 23 > -3 if Facebook bans, but -3 > -12 if it doesn't, so no dominant strategy.")
B.num("S19-02", ["S19-02"], "Game Theory Exercise Part 1: Facebook bans political ads and Twitter does not. Twitter receives 10% of Facebook's $350M political ad revenue and faces a 10% chance of a fine of 4% of its $3,000M ad revenue. What is Twitter's payoff ($ millions)?", 23,
      "Gain 0.10 × 350 = 35. Expected fine 0.10 × 0.04 × 3,000 = 12. Payoff 35 - 12 = 23.", {"f": "cell", "pay": [[list(c) for c in r] for r in GTX.P1], "i": 0, "j": 1, "who": 1}, unit="$ millions")
B.num("S19-02", ["S19-02"], "Game Theory Exercise Part 1: Twitter bans and Facebook does not. Facebook picks up Twitter's $3M of political ads and faces a 10% chance of a fine of 4% of its $70,000M ad revenue. What is Facebook's payoff ($ millions)?", -277,
      "Expected fine 0.10 × 0.04 × 70,000 = 280. Payoff 3 - 280 = -277.", {"f": "cell", "pay": [[list(c) for c in r] for r in GTX.P1], "i": 1, "j": 0, "who": 0}, unit="$ millions")
B.mc("S19-04", ["S19-04"], "calc", "Game Theory Exercise Part 3 (regulation risk 15% if both don't ban, 5% if only one doesn't):\n\n" + GTX.matrix(GTX.P3) + "\n\nHow many pure-strategy Nash equilibria are there?",
     ["Two: (Ban, Don't Ban) and (Don't Ban, Ban)", "One: (Don't Ban, Ban)", "One: both ban", "None"], 0,
     "Each firm's best response is the opposite of its rival's: Facebook -350 > -420 and -137 > -350; Twitter 29 > -3 and -3 > -18.")
B.tf("S19-03", ["S19-03", "S19-04"], "apply", "True or false: In Game Theory Exercise Part 3, Facebook still has a dominant strategy.", False,
     "False. It bans if Twitter doesn't (-350 > -420) and doesn't ban if Twitter bans (-137 > -350).")

if __name__ == "__main__": print(B.write())
