from common import *

def mat(rowp, colp, rows, cols, pay):
    """Markdown payoff matrix: first number row player, second column player."""
    head = [f"{rowp} \\ {colp}"] + cols
    return table(head, [[r] + [f"{a}, {b}" for a, b in pay[i]] for i, r in enumerate(rows)])

VISA = mat("Visa", "Mastercard", ["Lower Fee", "Maintain Fee"], ["Lower Fee", "Maintain Fee"], [[(2, 2), (4, 1)], [(1, 4), (3, 3)]])
DILL = mat("Dillard's", "Nordstrom", ["Girl's", "Women's"], ["Girl's", "Women's"], [[(2, 1), (4, 2)], [(6, 4), (3, 5)]])
TGT = mat("Target", "Walmart", ["Boy's", "Men's"], ["Boy's", "Men's"], [[(4, 3), (8, 7)], [(2, 5), (5, 4)]])
MON = mat("Boss", "Employee", ["Monitor", "Don't Monitor"], ["Work", "Shirk"], [[(-1, 1), (1, -1)], [(1, -1), (-1, 1)]])
MON2 = mat("Boss", "Employee", ["Monitor", "Don't Monitor"], ["Work", "Shirk"], [[(6, 3), (8, 0)], [(10, 3), (2, 4)]])
BRIDE = table(["Vizzini \\ Westley", "Poison in his own cup", "Poison in Vizzini's cup"], [["Drink from Westley's cup", "Die, Live", "Live, Die"], ["Drink from his own cup", "Live, Die", "Die, Live"]])
COORD = mat("Firm A", "Firm B", ["USB-C", "Proprietary"], ["USB-C", "Proprietary"], [[(40, 40), (5, 5)], [(5, 5), (40, 40)]])
GOLD = mat("Player 1", "Player 2", ["Split", "Steal"], ["Split", "Steal"], [[(50, 50), (0, 100)], [(100, 0), (0, 0)]])
ADV = mat("Kellogg's", "General Mills", ["Advertise", "Don't"], ["Advertise", "Don't"], [[(0, 0), (44, -4)], [(-4, 44), (4, 4)]])
ELIM = mat("Row", "Column", ["Top", "Middle", "Bottom"], ["Left", "Center", "Right"], [[(4, 3), (5, 1), (6, 2)], [(2, 1), (8, 4), (3, 6)], [(3, 0), (9, 6), (2, 8)]])

EV = {"title": "Expected value", "body": r"If an outcome is worth \(x_1\) with probability \(p\) and \(x_2\) with probability \(1 - p\), its expected value is \(p\,x_1 + (1 - p)\,x_2\). Example: a 30% chance of $10 and a 70% chance of $0 is worth \(0.3(10) + 0.7(0) = \$3\) on average."}
LINEAR = {"title": "Solving a linear equation in p", "body": r"Collect the p terms on one side and numbers on the other. Example: \(3 = 4 - 4p\). Subtract 4: \(-1 = -4p\). Divide by \(-4\): \(p = 0.25\). Another: \(8 - 2q = 2 + 8q\). Move terms: \(6 = 10q\), so \(q = 0.6\)."}
READ = {"title": "Reading a payoff matrix", "body": "Each cell has two numbers. The FIRST belongs to the row player, the SECOND to the column player. To compare the row player's options, hold the column fixed and look down that column at the first numbers. To compare the column player's options, hold the row fixed and look across that row at the second numbers."}

LESSONS = [
{"id": "S19-01", "title": "Simultaneous-move games", "calc": False,
 "plain": r"""When there are only a few big firms (an **oligopoly**), each firm's profit depends on what the others do. Visa's best fee depends on Mastercard's fee, and Mastercard's depends on Visa's. That mutual dependence is called **interdependence**, and **game theory** is the tool for thinking it through. That is why game theory is especially useful for oligopoly (Reading Quiz Q1), and not for perfect competition (firms are too small to matter to each other) or monopoly (no rival).

**The pieces of a game:**
- **Players**: the decision makers (Visa and Mastercard).
- **Strategies**: the choices each can make (lower the fee or maintain it).
- **Payoffs**: what each player gets in each outcome (profit).

**Timing:**
- In a **simultaneous-move game**, each player decides **without seeing** the other's decision. It does not have to be at the same instant; what matters is that neither knows the other's choice when deciding. (Reading Quiz Q2: a game where one player moves after observing the other is NOT simultaneous; that is a sequential game, covered in S20.)
- **One-shot** games are played once. **Repeated** games are played over and over (S20).

The slides open with a 2014 Wall Street Journal story: Visa and MasterCard in talks to lower the processing fees paid by Canadian merchants. Each one's best fee depends on what the other does, and neither sees the other's final choice in advance.

Session 19 is about **simultaneous-move, one-shot** games.""",
 "why": "Every game theory question starts by identifying the players, strategies and timing. Practice exam Q6 to Q8 and Comprehension Quiz 9 Q1 to Q3 are simultaneous-move games.",
 "definition": "A simultaneous-move game is a game in which each player makes decisions without knowledge of the other players' decisions.",
 "formulas": [], "derivation": "", "math": [READ],
 "worked": [{"title": "Classify the game", "problem": "Two gas stations on the same corner phone in their prices to headquarters each morning before opening, without seeing each other's sign. Is this simultaneous or sequential? One-shot or repeated?",
   "steps": ["Neither sees the other's price when choosing: simultaneous.", "They do it every morning: repeated. Today's choice taken by itself is a one-shot simultaneous game."], "answer": "Simultaneous; repeated daily (each day alone is a one-shot simultaneous game)."}],
 "graph": {"component": "payoff", "params": {"players": ["Visa", "Mastercard"], "rows": ["Lower Fee", "Maintain Fee"], "cols": ["Lower Fee", "Maintain Fee"], "pay": [[[2, 2], [4, 1]], [[1, 4], [3, 3]]]}, "caption": "The Visa versus Mastercard game from the slides. Each picks a fee without seeing the other's choice."},
 "traps": ["Simultaneous means neither KNOWS the other's choice, not that they move at the same clock time.",
           "A game where one player observes the other's move first is sequential, not simultaneous (Reading Quiz Q2).",
           "Game theory matters most in OLIGOPOLY, where a few firms are interdependent (Reading Quiz Q1)."],
 "sources": {"slides": "S19 Game Theory I pp. 8 to 13", "read": "Ch. 10 pp. 306 to 309", "exercise": "Game Theory Exercise Part 1 (one-shot simultaneous game)", "quiz": "Reading Quiz Q1, Q2; Comprehension Quiz 9 Q1 to Q3"}},

{"id": "S19-02", "title": "Normal-form representation", "calc": False,
 "plain": r"""The **normal form** is a table (a **payoff matrix**) that shows a simultaneous game. It contains three things (Reading Quiz Q3: all of the above):
1. a list of **players**,
2. the **strategies** available to each,
3. the **payoffs** for every combination of strategies.

**Convention:** one player picks a **row**, the other picks a **column**. In each cell, the **first number is the row player's payoff and the second is the column player's**.

The slides' example (pp. 10 to 15):

""" + VISA + r"""

How to read it: if Visa lowers its fee and Mastercard maintains, the cell is (4, 1): Visa earns 4 and Mastercard earns 1. If both maintain, each earns 3.

- **Visa's payoffs** are the first numbers: 2, 4, 1, 3.
- **Mastercard's payoffs** are the second numbers: 2, 1, 4, 3.

A normal-form game can be bigger than 2 by 2. With three strategies each it is a 3 by 3 table, read the same way.""",
 "why": "Every simultaneous-game exam question gives a payoff matrix. Misreading which number belongs to whom is the most common error.",
 "definition": "The normal-form representation of a game indicates the players, their possible strategies, and the payoffs resulting from alternative strategies.",
 "formulas": [], "derivation": "", "math": [READ],
 "worked": [{"title": "Reading the Visa matrix", "problem": "In the Visa versus Mastercard game, what does Mastercard earn if Visa maintains its fee and Mastercard lowers its fee?",
   "steps": ["Visa is the row player: row Maintain Fee.", "Mastercard is the column player: column Lower Fee.", "Cell (1, 4). The second number is Mastercard's."], "answer": "Mastercard earns 4 (and Visa earns 1)."}],
 "graph": {"component": "payoff", "params": {"players": ["Visa", "Mastercard"], "rows": ["Lower Fee", "Maintain Fee"], "cols": ["Lower Fee", "Maintain Fee"], "pay": [[[2, 2], [4, 1]], [[1, 4], [3, 3]]]}, "caption": "Edit any number to see how the analysis changes. First number = Visa (rows), second = Mastercard (columns)."},
 "traps": ["The FIRST number is the ROW player's payoff. Read the stem: some questions put a different firm on the rows.",
           "To compare the row player's choices, look DOWN a column. To compare the column player's choices, look ACROSS a row.",
           "The normal form has players, strategies AND payoffs."],
 "sources": {"slides": "S19 Game Theory I pp. 10 to 15", "read": "Ch. 10 pp. 307 to 309", "exercise": "Game Theory Exercise Part 1 step 3", "quiz": "Reading Quiz Q3; Comprehension Quiz 9 Q1"}},

{"id": "S19-03", "title": "Dominant strategy", "calc": False,
 "plain": r"""A **dominant strategy** is a strategy that results in the **highest payoff to a player regardless of the opponent's actions** (slides p. 22; Reading Quiz Q4). If you have one, play it; you do not need to guess what the rival will do.

**How to check (row player):** for EACH of the opponent's strategies, find your best response. If the same strategy is best every time, it is dominant.

**Visa (slides pp. 16 to 22):**
- If Mastercard lowers: Visa gets 2 from Lower vs 1 from Maintain. Lower is better.
- If Mastercard maintains: Visa gets 4 from Lower vs 3 from Maintain. Lower is better.
- Lower is best either way: **Visa's dominant strategy is to lower its fee.**

**Mastercard (pp. 23 to 29):** compare the second numbers across each row. If Visa lowers: 2 vs 1, Lower. If Visa maintains: 4 vs 3, Lower. **Mastercard also has a dominant strategy to lower.**

**Not every player has one.** Dillard's versus Nordstrom (in-class exercise, pp. 38 to 40):

""" + DILL + r"""

- Dillard's: if Nordstrom picks Girl's, Women's is better (6 > 2); if Nordstrom picks Women's, Girl's is better (4 > 3). The best choice changes, so **Dillard's has no dominant strategy**.
- Nordstrom: if Dillard's picks Girl's, Women's (2 > 1); if Dillard's picks Women's, Women's (5 > 4). **Nordstrom's dominant strategy is Women's.**
- **Put yourself in your rival's shoes** (textbook): Dillard's should expect Nordstrom to play Women's and respond with Girl's (4 > 3).

**Iterated elimination.** A strategy is **dominated** if another strategy is better against everything the rival might do. A rational player never plays it, so you can cross it out and look again. In bigger games this can shrink the table down to the answer.

**Secure (maximin) strategy** (textbook): pick the strategy whose worst case is best. It guarantees a minimum but ignores what the rival will rationally do, so it can cost you.""",
 "why": "Reading Quiz Q4, Comprehension Quiz 9 Q1 and Q2, and practice exam Q6 and Q24 test dominant strategies.",
 "definition": "A dominant strategy is a strategy that results in the highest payoff to a player regardless of the opponent's actions.",
 "formulas": [], "derivation": "", "math": [READ],
 "worked": [{"title": "Comprehension Quiz 9 matrix", "problem": "Target (rows) and Walmart (columns) each promote boy's or men's clothing.\n\n" + TGT + "\n\nWho has a dominant strategy?",
   "steps": ["Target vs Walmart Boy's: Boy's 4 > Men's 2. Vs Walmart Men's: Boy's 8 > Men's 5. Boy's both times: dominant.", "Walmart vs Target Boy's: Men's 7 > Boy's 3. Vs Target Men's: Boy's 5 > Men's 4. Changes: no dominant strategy."],
   "answer": "Only Target has a dominant strategy (promote boy's clothing)."},
  {"title": "Iterated elimination in a 3 by 3", "problem": "Find what survives iterated elimination.\n\n" + ELIM,
   "steps": ["Rows first: no row is worse than another row in every column (for example Top beats Middle under Left but loses under Center).", "Column: Center (1, 4, 6) vs Right (2, 6, 8): Right is higher in every row, so Center is dominated. Cross it out.", "Now rows over Left and Right only: Top (4, 6), Middle (2, 3), Bottom (3, 2). Top beats both, so cross out Middle and Bottom.", "Only Top is left; Column compares Left 3 vs Right 2 and picks Left."],
   "answer": "(Top, Left) with payoffs (4, 3)."}],
 "graph": {"component": "payoff", "params": {"players": ["Dillard's", "Nordstrom"], "rows": ["Girl's", "Women's"], "cols": ["Girl's", "Women's"], "pay": [[[2, 1], [4, 2]], [[6, 4], [3, 5]]]}, "caption": "Dillard's versus Nordstrom. The readout names any dominant strategy: Nordstrom has one, Dillard's does not."},
 "traps": ["A dominant strategy must be best against EVERY opposing choice, not just the one the rival is playing now.",
           "Compare the row player's payoffs DOWN a column (first numbers); compare the column player's ACROSS a row (second numbers).",
           "If one player has no dominant strategy, check the rival: if the rival has one, assume they play it and best-respond.",
           "A dominant strategy does not mean the player gets the highest number in the table."],
 "sources": {"slides": "S19 Game Theory I pp. 16 to 29, 38 to 40", "read": "Ch. 10 pp. 309 to 311", "exercise": "Dillard's vs. Nordstrom in-class exercise; Game Theory Exercise Part 1 step 6", "quiz": "Reading Quiz Q4; Comprehension Quiz 9 Q1, Q2"}},

{"id": "S19-04", "title": "Nash equilibrium", "calc": True,
 "plain": r"""A **Nash equilibrium** is a condition describing a set of strategies in which **no player can improve his or her payoff by unilaterally changing his or her strategy, given the other players' strategies** (slides p. 32). Every player is already playing a best response to everyone else. (Reading Quiz Q5 says the opposite and is false.)

**The underline method** finds every pure-strategy Nash equilibrium:
1. For each **column**, underline the row player's highest first number.
2. For each **row**, underline the column player's highest second number.
3. Any cell with **both** numbers underlined is a Nash equilibrium.

**Visa versus Mastercard** (pp. 30 to 37): both have the dominant strategy Lower, so (Lower, Lower) with payoffs (2, 2) is the Nash equilibrium. **Can either improve?** Both would be better off at (Maintain, Maintain) with (3, 3). **Could they collude?** They would both gain by agreeing beforehand to maintain fees, but the agreement would not hold: each has an incentive to defect, since lowering while the other maintains pays 4. This pattern, where self-interest leads to an outcome worse for both, is a **prisoner's dilemma**.

**Dillard's versus Nordstrom:** Nordstrom's dominant strategy is Women's; Dillard's best response to Women's is Girl's. Nash equilibrium: (Girl's, Women's) = (4, 2).

**A game can have:**
- **one** equilibrium (Visa, Dillard's),
- **several** (coordination games: both pick USB-C, or both pick a proprietary plug),
- **none in pure strategies** (the Princess Bride, employee monitoring). Then players randomize (S19-05).

**Comprehension Quiz 9:** Target (rows) has the dominant strategy Boy's; Walmart's best response to Boy's is Men's (7 > 3). Equilibrium (Boy's, Men's) = (8, 7), and neither has an incentive to deviate.""",
 "why": "Nash equilibrium is the core prediction tool for S19 to S22. Practice exam Q7 and Q24, Reading Quiz Q5 and Comprehension Quiz 9 Q2 and Q3 test it.",
 "definition": "A Nash equilibrium is a condition describing a set of strategies in which no player can improve his or her payoff by unilaterally changing his or her strategy, given the other players' strategies.",
 "formulas": [], "derivation": "", "math": [READ],
 "worked": [{"title": "Underline method", "problem": "Find every Nash equilibrium.\n\n" + COORD,
   "steps": ["Column USB-C: A's best is USB-C (40). Column Proprietary: A's best is Proprietary (40).", "Row USB-C: B's best is USB-C (40). Row Proprietary: B's best is Proprietary (40).", "Both underlined: (USB-C, USB-C) and (Proprietary, Proprietary)."],
   "answer": "Two Nash equilibria. This is a coordination game: the firms only need to agree on one standard, and once agreed neither wants to deviate."},
  {"title": "Prisoner's dilemma check", "problem": "In the Visa game, is the Nash equilibrium the best outcome for the two firms together?",
   "steps": ["Nash equilibrium: (Lower, Lower) = 2 + 2 = 4 total.", "(Maintain, Maintain) = 3 + 3 = 6 total.", "But at (Maintain, Maintain), each could switch to Lower and get 4 > 3."], "answer": "No. Both would prefer (3, 3), but it is not stable: a prisoner's dilemma."}],
 "graph": {"component": "payoff", "params": {"players": ["Visa", "Mastercard"], "rows": ["Lower Fee", "Maintain Fee"], "cols": ["Lower Fee", "Maintain Fee"], "pay": [[[2, 2], [4, 1]], [[1, 4], [3, 3]]]}, "caption": "Green numbers are best responses; the outlined cell has both, so it is a Nash equilibrium. Try making both maintain worth 5 each and see whether it changes."},
 "traps": ["Nash equilibrium means NO player can gain by changing ALONE. It does not mean the outcome is best for the players.",
           "Check BOTH players: a cell is an equilibrium only if both numbers are best responses.",
           "A game can have zero, one or several pure-strategy Nash equilibria.",
           "Collusion in a one-shot prisoner's dilemma fails because each has an incentive to defect."],
 "sources": {"slides": "S19 Game Theory I pp. 30 to 40", "read": "Ch. 10 pp. 311 to 313", "exercise": "Dillard's vs. Nordstrom; Game Theory Exercise Part 1 step 5", "quiz": "Reading Quiz Q5; Comprehension Quiz 9 Q2, Q3; Practice exam Q7, Q24"}},

{"id": "S19-05", "title": "Mixed (randomized) strategy", "calc": True,
 "plain": r"""Some games have **no** pure-strategy Nash equilibrium: whatever you do, the rival wants to do something else, and then you want to switch, and so on. Then the best plan is to be unpredictable.

A **mixed (randomized) strategy** is a strategy whereby a player **randomizes over two or more available actions in order to keep rivals from being able to predict his or her action** (slides p. 44). Examples: rock, paper, scissors; penalty kicks; play calling in football.

**The Princess Bride** (pp. 41 to 43): Westley poisons one cup; Vizzini picks a cup.

""" + BRIDE + r"""

Whatever Westley does, Vizzini wants to do the opposite of what would kill him, and Westley wants to match the cup Vizzini will drink. No cell is stable, so neither should be predictable.

**Employee monitoring** (pp. 45 to 46):

""" + MON + r"""

If the boss always monitors, the employee works, so the boss would rather not monitor. If the boss never monitors, the employee shirks, so the boss wants to monitor. No pure equilibrium.

**How to find the mix (indifference method).** Each player randomizes so that the **other** player is indifferent between his or her options. If the employee strictly preferred one action, the boss could exploit it.

With the slide's numbers everything is symmetric: the boss monitors with probability 1/2 and the employee works with probability 1/2. A non-symmetric version shows the method better:

""" + MON2 + r"""

1. Boss monitors with probability p. Employee's expected payoff from Work: \(3p + 3(1 - p) = 3\). From Shirk: \(0p + 4(1 - p) = 4 - 4p\). Set equal: \(3 = 4 - 4p\), so **p = 0.25**.
2. Employee works with probability q. Boss's expected payoff from Monitor: \(6q + 8(1 - q) = 8 - 2q\). From Don't: \(10q + 2(1 - q) = 2 + 8q\). Set equal: \(8 - 2q = 2 + 8q\), so **q = 0.6**.

Notice the boss's probability comes from the **employee's** payoffs, and the employee's from the **boss's**. The mixed strategy formulas are **not** on the equation sheet.""",
 "why": "Practice exam Q10 maps here. A game with no pure equilibrium is a classic exam setup.",
 "definition": "A mixed (randomized) strategy is a strategy whereby a player randomizes over two or more available actions in order to keep rivals from being able to predict his or her action.",
 "formulas": [{"name": "Indifference condition (column player indifferent)", "tex": r"p\,c_{11} + (1-p)\,c_{21} = p\,c_{12} + (1-p)\,c_{22}", "onSheet": False, "note": "p = probability the ROW player plays the top row; c = the column player's payoffs."},
              {"name": "Solved for p", "tex": r"p = \frac{c_{22} - c_{21}}{(c_{11} - c_{21}) - (c_{12} - c_{22})}", "onSheet": False, "note": "Easier to set up the two expected payoffs and solve than to memorize this."}],
 "derivation": r"Expand \(p c_{11} + (1-p) c_{21} = p c_{12} + (1-p) c_{22}\): \(c_{21} + p(c_{11} - c_{21}) = c_{22} + p(c_{12} - c_{22})\). Collect p: \(p[(c_{11} - c_{21}) - (c_{12} - c_{22})] = c_{22} - c_{21}\). Divide.",
 "math": [EV, LINEAR],
 "worked": [{"title": "Penalty kick", "problem": "A kicker shoots Left or Right; the goalie dives Left or Right. Probabilities of scoring (kicker's payoff; goalie's payoff is 1 minus it): kicker Left/goalie Left 0.4, Left/Right 0.9, Right/Left 0.8, Right/Right 0.3. With what probability should the kicker shoot Left?",
   "steps": ["Kicker shoots Left with probability p. Goalie's payoffs = 1 - scoring.", "Goalie dives Left: scoring chance 0.4p + 0.8(1 - p) = 0.8 - 0.4p.", "Goalie dives Right: 0.9p + 0.3(1 - p) = 0.3 + 0.6p.", "Make the goalie indifferent: 0.8 - 0.4p = 0.3 + 0.6p, so 0.5 = p."],
   "answer": "Shoot Left half the time. Scoring chance is then 0.8 - 0.2 = 0.6 whichever way the goalie dives."}],
 "graph": {"component": "payoff", "params": {"players": ["Boss", "Employee"], "rows": ["Monitor", "Don't Monitor"], "cols": ["Work", "Shirk"], "pay": [[[6, 3], [8, 0]], [[10, 3], [2, 4]]]}, "caption": "No cell is outlined: no pure equilibrium. The readout gives the mixed equilibrium: the boss monitors 25% of the time and the employee works 60% of the time. Edit the payoffs and watch the probabilities move."},
 "traps": ["Each player's mix makes the OTHER player indifferent. Use the opponent's payoffs to find your own probability.",
           "Mixed strategies matter when there is NO pure-strategy equilibrium (or to find additional equilibria).",
           "Randomizing is not 'any random choice': the probabilities are specific.",
           "The mixed strategy formulas are not on the equation sheet; set up the two expected payoffs and solve."],
 "sources": {"slides": "S19 Game Theory I pp. 41 to 46", "read": "Ch. 10 pp. 314 to 315 (monitoring workers)", "exercise": "", "quiz": "Practice exam Q10"}},

{"id": "S19-06", "title": "Applying game theory to pricing, coordination and advertising", "calc": True,
 "plain": r"""The same few matrix patterns show up again and again in business.

**1. Pricing: the prisoner's dilemma.** Each firm's dominant strategy is to price low, so both end up at (Low, Low) even though (High, High) would pay both more. A one-shot agreement to keep prices high fails because each would cheat (Visa and Mastercard fees). Real example: cola makers in India cutting prices before the summer rush.

**2. Advertising.** When advertising mostly steals customers from rivals rather than growing the market, each firm's dominant strategy is to advertise, and their ads cancel out. Comprehension Quiz 9 (Kellogg's versus General Mills, $ billions):

""" + ADV + r"""

Advertise beats Don't for each firm whatever the other does (0 > -4 and 44 > 4), so **both advertise** and each earns 0, although both would earn 4 by not advertising. (Whether they can sustain not advertising when the game repeats is Session 20.)

**3. Coordination.** When both firms do best by matching (compatible standards, plug types, which product line to promote), there are several equilibria. The problem is getting to one: firms talk, an industry group sets a standard, or the government does. Once agreed, no one wants to deviate, unlike the pricing game.

**4. Product choice.** Dillard's and Nordstrom picking which clothing line to feature: Nordstrom has a dominant strategy (Women's), so Dillard's should expect it and pick Girl's.

**5. Golden Balls** (slides pp. 47 to 48): two players each secretly choose Split or Steal. Both split: share the jackpot. One steals: the stealer takes it all. Both steal: both get nothing.

""" + GOLD + r"""

Steal is never worse than Split (100 > 50 if the other splits; 0 = 0 if the other steals), so the game pushes both toward stealing, which is why trust is so hard.

**6. Nash bargaining** (textbook): two sides name how much of a fixed pie they want; if the requests add to more than the pie, there is no deal. Every split that exactly uses the pie is an equilibrium, so outcomes are hard to predict and stalemates are common.

**Method for any business game:** (1) identify players, strategies, timing; (2) build the matrix; (3) look for dominant strategies; (4) find Nash equilibria with the underline method; (5) if none, think about randomizing; (6) ask whether the equilibrium is bad for both (a dilemma) or a coordination problem.""",
 "why": "Comprehension Quiz 9 Q1 to Q6, Reading Quiz Q1 and practice exam Q8 and Q24 ask you to set up and solve business games.",
 "definition": "Game theoretic logic applies to business decisions such as pricing, advertising and coordination: predict what each rival will do by finding dominant strategies and Nash equilibria.",
 "formulas": [], "derivation": "", "math": [READ, EV],
 "worked": [{"title": "Setting up a game from a story", "problem": "Two streaming services each decide whether to drop a controversial show. Each show brings in $200 million (Service A) and $20 million (Service B). Keeping it carries a 10% chance of a $500 million fine for A or a $50 million fine for B. If one drops it and the other keeps it, the one keeping it picks up $10 million of extra viewers from the other. Payoffs are changes in profit ($ millions). Find the equilibrium.",
   "steps": ["Expected fine if kept: A 0.1 × 500 = 50; B 0.1 × 50 = 5.", "Both drop: A -200, B -20. Both keep: A -50, B -5.", "A keeps, B drops: A -50 + 10 = -40, B -20. A drops, B keeps: A -200, B -5 + 10 = 5.", "A: Keep beats Drop against both of B's choices (-50 > -200; -40 > -200): dominant.", "B: against A Keep, Drop -20 vs Keep -5: Keep. Against A Drop, Keep 5 > -20: Keep. B's dominant strategy is also Keep."],
   "answer": "Both keep the show: (A -50, B -5)."}],
 "graph": {"component": "payoff", "params": {"players": ["Kellogg's", "General Mills"], "rows": ["Advertise", "Don't advertise"], "cols": ["Advertise", "Don't advertise"], "pay": [[[0, 0], [44, -4]], [[-4, 44], [4, 4]]]}, "caption": "The Comprehension Quiz 9 advertising game ($ billions). Both advertise in equilibrium even though both would earn more if neither did."},
 "traps": ["In a prisoner's dilemma the equilibrium is WORSE for both than cooperating, but cooperation is not stable in a one-shot game.",
           "In a coordination game, once firms agree, nobody wants to deviate. That is the difference from a pricing game.",
           "Advertising is dominant when it mostly steals rivals' customers; if it grows the whole market the game can change.",
           "Read who is the row player in each story before computing anything."],
 "sources": {"slides": "S19 Game Theory I pp. 9 to 40, 47 to 48", "read": "Ch. 10 pp. 313 to 317", "exercise": "Game Theory Exercise Part 1", "quiz": "Reading Quiz Q1; Comprehension Quiz 9 Q1 to Q6; Practice exam Q8, Q24"}},
]
import GTX; GTX.add(LESSONS)
for L in LESSONS: write_lesson(L)
write_session("S19", {"overview": "Session 19 introduces game theory for oligopoly, where a few firms' profits depend on each other's choices. A simultaneous-move, one-shot game is shown in normal form: a payoff matrix with players, strategies and payoffs (row player's number first). A dominant strategy is best whatever the rival does. A Nash equilibrium is a set of strategies where no one can gain by changing alone; it can be worse for everyone (the prisoner's dilemma, Visa versus Mastercard). When no pure equilibrium exists, players randomize so the rival is indifferent. The same tools apply to pricing, advertising and coordination."})
print([L["id"] for L in LESSONS])
