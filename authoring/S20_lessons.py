from common import *
from S19_lessons import mat

KEL = mat("Kellogg's", "General Mills", ["Don't advertise", "Advertise"], ["Don't advertise", "Advertise"], [[(12, 12), (-1, 15)], [(15, -1), (2, 2)]])
VISA = mat("Visa", "Mastercard", ["Lower Fee", "Maintain Fee"], ["Lower Fee", "Maintain Fee"], [[(2, 2), (4, 1)], [(1, 4), (3, 3)]])
PV = {"title": "Present value of a payoff that lasts forever", "body": r"A payoff \(\pi\) received every period forever, starting next period, is worth \(\pi / i\) today, where i is the interest (discount) rate. Example: $12 a year forever at 10% is worth \(12 / 0.10 = \$120\). Add today's payoff if it starts now: \(12 + 12/0.10 = \$132\). A higher i makes future payoffs worth less: at 50%, \(12/0.5 = \$24\)."}
SOLVE_I = {"title": "Solving for the interest rate", "body": r"Set the two present values equal and solve for i. \(15 + \frac{2}{i} = 12 + \frac{12}{i}\). Move the numbers to one side and the 1/i terms to the other: \(15 - 12 = \frac{12}{i} - \frac{2}{i}\), so \(3 = \frac{10}{i}\). Multiply both sides by i and divide by 3: \(i = \frac{10}{3} = 3.33\), or 333%."}
TREE = {"title": "Reading a game tree", "body": "Start at the first node (the first mover). Each branch is an action. The next node shows who moves next. Payoffs at the ends are listed in the order stated in the problem, usually the first mover first. To solve, start at the LAST decisions and work back toward the start."}

PUTIN = {"players": ["Putin", "Obama"], "tree": {"p": 0, "children": [{"a": "Invade", "n": {"p": 1, "children": [{"a": "Sanction", "pay": [2, -2]}, {"a": "Don't sanction", "pay": [10, -5]}]}}, {"a": "Don't invade", "pay": [-5, 5]}]}}
TRADE = {"players": ["US", "China"], "tree": {"p": 0, "children": [{"a": "Threat", "n": {"p": 1, "children": [{"a": "Resist", "n": {"p": 0, "children": [{"a": "Impose", "pay": [-2, -2]}, {"a": "Back down", "pay": [4, 4]}]}}, {"a": "Concede", "pay": [6, 2]}]}}, {"a": "No threat", "pay": [2, 6]}]}}
ENTRY = {"players": ["Entrant", "Incumbent"], "tree": {"p": 0, "children": [{"a": "Enter", "n": {"p": 1, "children": [{"a": "Fight", "pay": [-3, 2]}, {"a": "Accommodate", "pay": [4, 6]}]}}, {"a": "Stay out", "pay": [0, 12]}]}}

LESSONS = [
{"id": "S20-01", "title": "Infinitely repeated games", "calc": True,
 "plain": r"""In a one-shot game, collusion falls apart because cheating has no future cost (Visa and Mastercard both lower fees). But real rivals meet again and again. An **infinitely repeated game** is a game that is **played over and over again forever, and in which players receive payoffs during each play of the game** (slides p. 31).

**Is collusion sustainable?** Yes. Collusion is sustainable because **players that defect can be punished in subsequent periods** (p. 31). The punishment plan is a **trigger strategy** (S20-03).

**Kellogg's versus General Mills** (slides pp. 30 to 35):

""" + KEL + r"""

In one play, Advertise is dominant and both earn 2. If they collude by not advertising forever, each earns 12 every period. If Kellogg's cheats, it earns 15 once, and then General Mills punishes by advertising forever, so Kellogg's earns 2 every period after.

**Would it ever make sense to defect?** It depends on how much the firm values money now versus money in the future, measured with a **discount rate** i. The higher the discount rate, the more each future payoff is discounted. **A player should defect if the present value of cheating is greater than the present value of collusion** (p. 33).

**The professor's present values** (p. 34), with i = 10%:
- PV cheating = payoff now + payoffs in the future = \(15 + \frac{2}{i} = 15 + \frac{2}{0.10} = 35\)
- PV collusion = \(12 + \frac{12}{i} = 12 + \frac{12}{0.10} = 132\)
- 132 > 35, so Kellogg's should keep colluding.

**Indifference rate** (p. 35): set them equal. \(15 + \frac{2}{i} = 12 + \frac{12}{i}\) gives \(3 = \frac{10}{i}\), so \(i = 3.33\), or 333%. Kellogg's would only cheat if it discounted the future at more than 333% per period.

The value of a perpetuity (a payment forever) is the payment divided by the interest rate (slides p. 36). This is not on the equation sheet.""",
 "why": "Practice exam Q25 and Comprehension Quiz 9 Q6 and Q7 test whether collusion holds. The calculation is short and very testable.",
 "definition": "An infinitely repeated game is a game that is played over and over again forever and in which players receive payoffs during each play of the game.",
 "formulas": [{"name": "PV of colluding forever (starting now)", "tex": r"PV_{collude} = \pi_c + \frac{\pi_c}{i}", "onSheet": False},
              {"name": "PV of cheating once, then punishment forever", "tex": r"PV_{cheat} = \pi_d + \frac{\pi_n}{i}", "onSheet": False, "note": "π_d = one-time payoff from defecting; π_n = punishment (one-shot Nash) payoff each later period."},
              {"name": "Perpetuity", "tex": r"PV = \frac{\pi}{i}", "onSheet": False, "note": "A payment every period forever, starting next period."}],
 "derivation": r"A payment \(\pi\) every period starting next period is worth \(\frac{\pi}{1+i} + \frac{\pi}{(1+i)^2} + \dots\). This geometric series sums to \(\frac{\pi}{i}\). Adding this period's payment gives \(\pi + \frac{\pi}{i} = \pi\frac{1+i}{i}\), the textbook's form.",
 "math": [PV, SOLVE_I],
 "worked": [{"title": "Comprehension Quiz 9 Q6", "problem": "Kellogg's and General Mills: both advertise 0 each; neither 4 each; the advertiser alone 44 and the other -4 ($ billions). Infinitely repeated with trigger strategies, i = 12%. Collude or defect?",
   "steps": ["PV collude = 4 + 4/0.12 = 4 + 33.33 = 37.33.", "PV cheat = 44 + 0/0.12 = 44.", "44 > 37.33."], "answer": "Defect. The one-time gain (40) is bigger than the future loss (4 per year, worth 33.33)."}],
 "graph": {"component": "repeated", "params": {"coop": 12, "cheat": 15, "nash": 2, "i": 0.10}, "caption": "The Kellogg's example. Raise the interest rate past 333% and cheating becomes worth more than colluding."},
 "traps": ["Use the PUNISHMENT payoff (one-shot Nash) for the future periods after cheating, not the collusive payoff.",
           "The professor's convention: today's payoff plus payoff/i for the future, on both sides.",
           "A HIGHER interest rate makes cheating MORE attractive, because the future punishment is worth less.",
           "Collusion can be sustained only because there is a future; in a one-shot game it fails."],
 "sources": {"slides": "S20 Game Theory II pp. 27, 30 to 36", "read": "Ch. 10 pp. 318 to 323", "exercise": "", "quiz": "Comprehension Quiz 9 Q6, Q7; Practice exam Q25"}},

{"id": "S20-02", "title": "Finitely repeated games", "calc": False,
 "plain": r"""What if the game is repeated, but only a known number of times? Take Visa and Mastercard over **two periods** (slides p. 28):

""" + VISA + r"""

- **Second (last) period:** it is the last period, so both players treat it as a **one-shot game**: no one can be punished for defecting afterward. Both lower fees.
- **First period:** a player has an incentive to break a promise in the second-to-last period, since there is **no effective punishment** in the last period (everyone already defects then). So both defect in period 1 too.
- **Conclusion (p. 28): finite repeated games will always collapse back to a one-shot simultaneous game.** This works backward from the end however many periods there are (10, 100, 1,000): cooperation unravels from the last period to the first.

This applies when the one-shot game has a **unique** Nash equilibrium and the **final period is known**.

**Comprehension Quiz 9 Q7.** You and your only rival have kept camera prices high through tacit collusion. You learn the rival will exit in one month. The game now has a known final period and no future punishment, so you should **defect and cut prices now**.

**When the end is uncertain** (textbook): if each period has some probability of being the last, cooperation can survive, much like the infinite game, because there is always a chance of future punishment.

**End-of-period problems** (textbook): a worker who has announced that she is quitting has little reason to work hard in her last weeks; a traveling seller who will never see the customer again has an incentive to sell junk. Good fixes make the relationship outlast the final period, like references and reputation.

The slides title the next page the "Underwear Bomber" Rule (p. 29); the page has no text, so the rule to know is the one stated on p. 28.""",
 "why": "Practice exam Q9 and Q12 and Comprehension Quiz 9 Q7 test the known-end unraveling logic.",
 "definition": "A finitely repeated game is a game that is played a finite number of times. When the final period is known and the one-shot game has a unique Nash equilibrium, it collapses back to the one-shot outcome in every period.",
 "formulas": [{"name": "PV of colluding when each period ends the game with probability θ", "tex": r"PV_{collude} = \frac{\pi_c}{\theta}", "onSheet": False, "note": "Textbook, uncertain end. Not needed for the known-end logic."}],
 "derivation": "Backward induction: the last period is a one-shot game, so both defect. Knowing that, nothing a player does in the second-to-last period can be rewarded or punished later, so it is also a one-shot game. Repeat back to period 1.",
 "math": [],
 "worked": [{"title": "Ten-period pricing game", "problem": "Two gas stations will compete for exactly 10 weeks before the road closes. Each week the one-shot game is a prisoner's dilemma with a unique equilibrium (both price low). What happens in week 1?",
   "steps": ["Week 10 is the last: both price low.", "Week 9: nothing can punish cheating in week 10, since both price low anyway. Both price low.", "Repeat back to week 1."], "answer": "Both price low in every week, including week 1."}],
 "traps": ["A KNOWN last period unravels cooperation all the way back to the first period.",
           "If the end is UNCERTAIN, cooperation can survive.",
           "When a rival announces it is leaving, the collusion game has a known end: expect defection (Quiz 9 Q7)."],
 "sources": {"slides": "S20 Game Theory II pp. 25 to 29", "read": "Ch. 10 pp. 323 to 328", "exercise": "", "quiz": "Comprehension Quiz 9 Q7; Practice exam Q9, Q12"}},

{"id": "S20-03", "title": "Trigger strategies", "calc": True,
 "plain": r"""A **trigger strategy** is a strategy that is **contingent on the last play of the game** and in which **some past particular action "triggers" a different action by a player** (slides p. 31).

The standard version (grim trigger): **cooperate as long as the rival has always cooperated; if the rival ever cheats, play the one-shot Nash strategy forever after.** The threat of losing the collusive payoff forever is what keeps everyone honest.

**When does a trigger strategy sustain collusion?** Compare the present values (professor's convention):
$$\underbrace{\pi_c + \frac{\pi_c}{i}}_{\text{collude}} \;\ge\; \underbrace{\pi_d + \frac{\pi_n}{i}}_{\text{cheat}}$$
where \(\pi_c\) is the collusive payoff per period, \(\pi_d\) the one-time payoff from defecting, and \(\pi_n\) the punishment (one-shot Nash) payoff per period after.

Rearranged, collusion holds when the interest rate is low enough:
$$i \le i^* = \frac{\pi_c - \pi_n}{\pi_d - \pi_c}$$
- Numerator: what you lose **every** future period once punishment starts.
- Denominator: what you gain **once** by cheating.

**Kellogg's** (slides p. 35): \(i^* = \frac{12 - 2}{15 - 12} = \frac{10}{3} = 333\%\).

**Comprehension Quiz 9 Q6:** \(i^* = \frac{4 - 0}{44 - 4} = 0.10\). At i = 12% > 10%, Kellogg's should defect.

Neither formula is on the equation sheet; setting the two present values equal (as on slide p. 35) always works.""",
 "why": "The trigger strategy calculation is the main computation in S20 (practice exam Q25, Comprehension Quiz 9 Q6).",
 "definition": "A trigger strategy is a strategy that is contingent on the last play of the game and in which some past particular action triggers a different action by a player.",
 "formulas": [{"name": "Collusion condition", "tex": r"\pi_c + \frac{\pi_c}{i} \ge \pi_d + \frac{\pi_n}{i}", "onSheet": False},
              {"name": "Highest interest rate that sustains collusion", "tex": r"i^* = \frac{\pi_c - \pi_n}{\pi_d - \pi_c}", "onSheet": False, "note": "Collusion holds if i ≤ i*."}],
 "derivation": r"Start from \(\pi_c + \frac{\pi_c}{i} \ge \pi_d + \frac{\pi_n}{i}\). Subtract \(\pi_c\) and \(\frac{\pi_n}{i}\) from both sides: \(\frac{\pi_c - \pi_n}{i} \ge \pi_d - \pi_c\). Multiply by i and divide by \(\pi_d - \pi_c\): \(i \le \frac{\pi_c - \pi_n}{\pi_d - \pi_c}\).",
 "math": [PV, SOLVE_I],
 "worked": [{"title": "Threshold interest rate", "problem": "Colluding pays $20 per period. Cheating pays $45 once, then $5 per period forever under punishment. What is the highest interest rate at which collusion holds? Should a firm collude at i = 25%?",
   "steps": [r"\(i^* = \frac{20 - 5}{45 - 20} = \frac{15}{25} = 0.60\), or 60%.", "At 25%: PV collude = 20 + 20/0.25 = 100. PV cheat = 45 + 5/0.25 = 65.", "100 > 65, consistent with 25% < 60%."], "answer": "Collusion holds for any i up to 60%; at 25% the firm colludes."}],
 "graph": {"component": "repeated", "params": {"coop": 20, "cheat": 45, "nash": 5, "i": 0.25}, "caption": "Slide the interest rate: below 60% the present value of colluding beats cheating."},
 "traps": ["The NUMERATOR is collude minus punishment; the DENOMINATOR is cheat minus collude. Flipping them is the classic error.",
           "Collusion holds when i is BELOW the threshold, not above.",
           "The punishment must be credible: the one-shot Nash payoff is credible because each firm is best-responding."],
 "sources": {"slides": "S20 Game Theory II pp. 31 to 36", "read": "Ch. 10 pp. 318 to 323", "exercise": "", "quiz": "Comprehension Quiz 9 Q6; Practice exam Q25"}},

{"id": "S20-04", "title": "Sequential games", "calc": False,
 "plain": r"""In a **sequential-move game**, one player moves first and the next player moves **after observing** that move. (Reading Quiz Q3: a game where players decide without knowing the others' decisions is NOT sequential; that is simultaneous.)

Examples: a firm decides whether to enter a market, then the incumbent decides whether to fight. A country threatens tariffs, then its trading partner decides whether to resist.

**The slides' Crimea question** (p. 42): in early 2014 Putin threatened to invade Crimea. How could we have predicted what he would do? Model it as a sequential game: Putin chooses first (Invade or Don't Invade), and then Obama chooses (Sanction or Don't Sanction).

**How to solve: backward induction** (Reading Quiz Q5: true). Start at the end of the game, figure out what the last mover will do at each of his or her decision points, then step back to the earlier mover, who anticipates those responses.

**Why the order matters.** Moving first can be an advantage (a first-mover advantage, S18-07): the leader can choose knowing how the follower will respond. Sometimes the follower has the advantage. The same payoffs can give a different outcome as a sequential game than as a simultaneous game.

**Sequential games versus the normal form.** Sequential games are drawn as trees (**extensive form**, S20-05), not matrices.""",
 "why": "Comprehension Quiz 9 Q8 to Q10, Reading Quiz Q3 and Q5 and practice exam Q27 and Q28 all use sequential games.",
 "definition": "A sequential-move game is a game in which one player makes a move after observing the other player's move.",
 "formulas": [], "derivation": "", "math": [TREE],
 "worked": [{"title": "Simultaneous or sequential?", "problem": "Classify: (a) two firms submit sealed bids; (b) a startup launches, then the market leader decides whether to cut prices; (c) a union makes a wage offer and management accepts or rejects.",
   "steps": ["(a) Neither sees the other's bid: simultaneous.", "(b) The leader sees the launch first: sequential.", "(c) Management sees the offer first: sequential."], "answer": "Simultaneous, sequential, sequential."}],
 "graph": {"component": "tree", "params": PUTIN, "caption": "Putin moves first; Obama sees the choice and responds. Payoffs: (Putin, Obama)."},
 "traps": ["Sequential = the later player OBSERVES the earlier move. If not observed, the game is simultaneous even if the moves happen at different times.",
           "Solve sequential games from the END (backward induction), not from the start.",
           "The first number in a sequential game's payoffs usually belongs to the first mover, but always check the problem's stated order."],
 "sources": {"slides": "S20 Game Theory II pp. 42 to 48", "read": "Ch. 10 pp. 328 to 330", "exercise": "Game Theory Exercise Part 2", "quiz": "Reading Quiz Q3, Q5; Comprehension Quiz 9 Q8 to Q10"}},

{"id": "S20-05", "title": "Extensive-form representation", "calc": False,
 "plain": r"""The **extensive form** is a **game tree**. It shows four things (slides pp. 43 to 48), all of which are elements of an extensive-form game (Reading Quiz Q4):
1. **Players**: who moves at each decision node (circles labeled P and O).
2. **Strategies**: the branches out of each node (Invade or Don't Invade; Sanction or Don't Sanction).
3. **Payoffs**: at the end of each path.
4. **Sequence**: the order of moves, from left to right.

**The slides' tree (Putin and Obama), payoffs (Putin, Obama):**
- Putin: **Invade** → Obama: **Sanction** → (2, -2)
- Putin: **Invade** → Obama: **Don't Sanction** → (10, -5)
- Putin: **Don't Invade** → (-5, 5)

**Reading payoffs.** The first number goes with the first mover (Putin), the second with Obama. If Putin invades and Obama does not sanction, Putin gets 10 and Obama gets -5.

**Trump, tariffs and trade** (pp. 56 to 69), payoffs (US, China):
- US: **No threat** → (2, 6)
- US: **Threat** → China: **Concede** → (6, 2)
- US: **Threat** → China: **Resist** → US: **Impose** → (-2, -2), or **Back down** → (4, 4)

The slides built these payoffs by ranking each side's preferences (US: concede 1st, back down 2nd, no threat 3rd, impose 4th; China: no threat 1st, back down 2nd, concede 3rd, impose last) and turning the ranks into numbers.""",
 "why": "Reading Quiz Q4 and practice exam Q27 test the elements of a game tree; Comprehension Quiz 9 Q8 asks you to sketch one.",
 "definition": "The extensive-form representation of a game summarizes the players, the information available to them at each stage, the strategies available to them, the sequence of moves, and the payoffs resulting from alternative strategies.",
 "formulas": [], "derivation": "", "math": [TREE],
 "worked": [{"title": "Sketch a tree from a story (Comprehension Quiz 9 Q9)", "problem": "Firm A decides whether to introduce a new product. Firm B then decides whether to clone it. Introduce and clone: (A 2, B 15). Introduce, no clone: (8, 1). Don't introduce: (0, 0). Draw the tree.",
   "steps": ["First node: A chooses Introduce or Don't introduce.", "Don't introduce ends the game at (0, 0).", "After Introduce, B's node: Clone → (2, 15) or Don't clone → (8, 1)."], "answer": "Two decision nodes (A, then B) and three end points. Solving it is S20-06."}],
 "graph": {"component": "tree", "params": TRADE, "caption": "The trade game from the slides. Payoffs: (US, China). Edit a payoff to see how the solution changes."},
 "traps": ["The extensive form includes players, strategies, payoffs AND sequence (Reading Quiz Q4: all are elements).",
           "Follow the branch order: a payoff at the end of a path depends on every move along it.",
           "Check which player's payoff is listed first."],
 "sources": {"slides": "S20 Game Theory II pp. 43 to 48, 56 to 61", "read": "Ch. 10 pp. 328 to 330 (Figure 10-1)", "exercise": "Game Theory Exercise Parts 2 and 3", "quiz": "Reading Quiz Q4; Comprehension Quiz 9 Q8, Q9"}},

{"id": "S20-06", "title": "Subgame perfect equilibrium", "calc": True,
 "plain": r"""A **subgame perfect equilibrium** (SPE) is a set of strategies where **every player's choice is a best response at every point in the tree**, including points that are never reached. Equivalently (textbook): a Nash equilibrium that involves **only credible threats**. You find it with **backward induction**.

**Putin and Obama** (slides pp. 49 to 55), payoffs (Putin, Obama):
1. Obama's decision (after an invasion): Sanction gives Obama -2, Don't Sanction gives -5. **Obama sanctions.**
2. Putin anticipates that. Invade leads to (2, -2), so Putin gets 2. Don't Invade gives Putin -5. **Putin invades.**
3. **SPE: Putin invades, Obama sanctions**: (2, -2).

**Trump and Xi** (pp. 56 to 69), payoffs (US, China):
1. Last move, US after China resists: Impose gives the US -2, Back down gives 4. **The US backs down.**
2. China, after a threat: Resist leads to (4, 4), so China gets 4; Concede gives China 2. **China resists.**
3. US at the start: Threat leads to (4, 4), so the US gets 4; No threat gives 2. **The US threatens.**
4. **SPE: the US threatens, China resists, the US backs down**: (4, 4).

The US threat to impose tariffs is **not credible**: when the time comes, imposing pays the US less than backing down, and China knows it.

**Credible versus non-credible threats.** A threat is credible only if carrying it out is in the threatener's interest at that point. Nash equilibria that rely on non-credible threats are not subgame perfect. Lesson: do not let non-credible threats change your behavior.""",
 "why": "Practice exam Q27 and Q28 and Comprehension Quiz 9 Q9 and Q10 ask for the subgame perfect outcome.",
 "definition": "A subgame perfect equilibrium is a condition describing a set of strategies that constitutes a Nash equilibrium and allows no player to improve his or her own payoff at any stage of the game by changing strategies; it involves only credible threats.",
 "formulas": [], "derivation": "", "math": [TREE],
 "worked": [{"title": "Innovation game (Comprehension Quiz 9 Q9)", "problem": "A decides whether to introduce; then B decides whether to clone. Introduce and clone: (2, 15). Introduce, no clone: (8, 1). Don't introduce: (0, 0). Find the SPE.",
   "steps": ["B after Introduce: Clone 15 > Don't clone 1. B clones.", "A: Introduce leads to (2, 15), so A gets 2; Don't introduce gives 0. 2 > 0, A introduces."], "answer": "A introduces, B clones: (2, 15)."},
  {"title": "Pepsi and Coke (Comprehension Quiz 9 Q10)", "problem": "If PepsiCo introduces a lemon-lime drink, Coca-Cola can Fight (both earn $100 million) or Acquiesce (Coca-Cola $275 million, PepsiCo $227 million). Is fighting credible?",
   "steps": ["At Coca-Cola's node: Acquiesce 275 > Fight 100.", "So Coca-Cola will acquiesce; fighting is not a credible threat.", "PepsiCo compares 227 from introducing with its status quo payoff and introduces."], "answer": "PepsiCo introduces and Coca-Cola acquiesces."}],
 "graph": {"component": "tree", "params": PUTIN, "caption": "Backward induction: Obama's best reply after an invasion is to sanction (-2 > -5); anticipating that, Putin invades (2 > -5). Green branches are the SPE choices."},
 "traps": ["Solve from the LAST move backward. Starting from the first mover's biggest payoff is the classic error (Putin's 10 is never reached).",
           "Specify a choice at EVERY decision node, including nodes off the equilibrium path.",
           "A threat that the threatener would not carry out when the time comes is not credible and is ignored in the SPE.",
           "A Nash equilibrium is not always subgame perfect; an SPE is always a Nash equilibrium."],
 "sources": {"slides": "S20 Game Theory II pp. 49 to 69", "read": "Ch. 10 pp. 328 to 332", "exercise": "Game Theory Exercise Parts 2 and 3", "quiz": "Reading Quiz Q5; Comprehension Quiz 9 Q9, Q10; Practice exam Q27, Q28"}},

{"id": "S20-07", "title": "Factors that influence the likelihood of collusion", "calc": False,
 "plain": r"""**What is collusion?** Secret or illegal cooperation or conspiracy, especially in order to cheat or deceive others (slides p. 38). Two forms:
- **Explicit collusion** (illegal and uncommon): price fixing, bid rigging, market allocation. Slide example: Apple, Google, Intel and Adobe settling a 2014 suit over agreements not to poach each other's workers (p. 39).
- **Implicit or tacit collusion** (legal and common): signaling. Firms reach collusive outcomes indirectly, by learning from experience how each other will behave (Reading Quiz Q2: true). Slide examples: airline "capacity discipline" (2015) and the Justice Department probing United, American, Delta and Southwest for collusion (pp. 40 to 41).

**Factors that influence collusion** (slides p. 37):
1. **Number of firms.** Fewer firms make collusion easier: it is easier to watch a few rivals and to punish cheaters. (Textbook: with n firms there are n(n - 1) monitoring relationships; 2 firms need 2, 5 firms need 20.)
2. **Firm size.** Punishment must be possible: a small firm may not have the capacity to punish a large rival by stealing its customers.
3. **History of the market.** Firms that have learned how rivals behave, and have seen punishments carried out before, can sustain collusion more easily.
4. **Punishment mechanisms.** Practices that make punishment quick and automatic, like price-matching guarantees, support collusion.

**From the trigger strategy math (S20-03):** collusion is easier when
- the **present value of cheating is less than the present value of collusion** (Reading Quiz Q1),
- the **interest rate is low** (firms care about the future),
- the gain from cheating is small and the punishment is harsh,
- cheating is **seen quickly** (Comprehension Quiz 9 Q7: prices visible on a comparison site made tacit collusion easy to sustain).""",
 "why": "Reading Quiz Q1 and Q2, Comprehension Quiz 9 Q7 and practice exam Q11, Q12 and Q26 test what makes collusion more or less likely.",
 "definition": "Collusion is cooperation among rivals to raise joint profits. Explicit collusion (price fixing, bid rigging, market allocation) is illegal; tacit collusion (signaling, learning how rivals behave) is legal. It is more likely with few firms, firms able to punish, a market history of cooperation, and effective punishment mechanisms.",
 "formulas": [], "derivation": "", "math": [],
 "worked": [{"title": "Which market colludes more easily?", "problem": "Market A: 2 firms, prices posted online daily, the same managers for 20 years, low interest rates. Market B: 15 firms, secret negotiated prices, frequent new entrants. Where is tacit collusion more likely?",
   "steps": ["Number of firms: A has 2, B has 15.", "Detection: A's prices are public; B's are secret, so cheating is hard to see.", "History: A's managers know each other's behavior.", "Patience: low interest rates in A make future punishment matter."], "answer": "Market A."}],
 "traps": ["Collusion is EASIER with FEWER firms and LOWER interest rates (Reading Quiz Q1 offers 'many players' and 'higher interest rate' as wrong answers).",
           "Explicit collusion is illegal; tacit collusion (signaling) is legal.",
           "Charging one price to all customers is not one of the factors (it is a distractor in Reading Quiz Q1)."],
 "sources": {"slides": "S20 Game Theory II pp. 37 to 41", "read": "Ch. 10 pp. 321 to 323 (factors affecting collusion)", "exercise": "", "quiz": "Reading Quiz Q1, Q2; Comprehension Quiz 9 Q7; Practice exam Q11, Q12, Q26"}},

{"id": "S20-08", "title": "Sequential games in business: entry, innovation, bargaining", "calc": True,
 "plain": r"""**1. Market entry and deterrence.** An entrant decides In or Out; if In, the incumbent decides Fight or Accommodate. Example (payoffs Entrant, Incumbent): Out → (0, 12); In and Fight → (-3, 2); In and Accommodate → (4, 6).
- Backward induction: after entry the incumbent compares Fight 2 vs Accommodate 6 and accommodates.
- So the entrant compares In (4) with Out (0) and enters. **SPE: In, Accommodate.**
- The incumbent's threat to fight is **not credible**. To deter entry, it must change the payoffs with a **commitment** (for example, building capacity that makes fighting cheaper, S18-05 and S18-07).

**2. Innovation.** A firm decides whether to introduce a product; a rival decides whether to clone it. In Comprehension Quiz 9 Q9 the rival clones (15 > 1), and the first firm still introduces (2 > 0). If cloning makes introducing unprofitable, the firm will not innovate, which is why **patents** that block cloning encourage innovation.

**3. Bargaining.** A proposer makes a take-it-or-leave-it offer; the responder accepts or rejects (both get 0). The responder prefers any positive amount to 0, so the proposer offers the smallest amount and keeps almost everything. A threat to reject a small offer is not credible. **The player who can make a credible take-it-or-leave-it offer captures most of the surplus.** If counteroffers are possible, the advantage shrinks.

**4. Policy and strategy.** The slides apply the same logic to Putin and Crimea, Trump's tariff threats, and social media and misinformation (p. 70; the Game Theory Exercise Parts 2 and 3 model the political ads decision with Twitter moving first).

**5. Sequential versus simultaneous.** Turning a simultaneous game into a sequential one can change the outcome, which is why firms race to commit first (or wait to move second).""",
 "why": "Practice exam Q13 and Q27 to Q29 and Comprehension Quiz 9 Q8 to Q10 apply sequential games to entry, innovation and bargaining.",
 "definition": "Sequential games can be applied to business decisions such as market entry (credible versus non-credible deterrence), innovation (cloning and patents) and bargaining (take-it-or-leave-it offers).",
 "formulas": [], "derivation": "", "math": [TREE],
 "worked": [{"title": "Entry deterrence with commitment", "problem": "Same entry game: Out (0, 12); In/Fight (-3, 2); In/Accommodate (4, 6). The incumbent can first sign contracts that make fighting pay it 8 instead of 2 if entry happens. Does that deter entry?",
   "steps": ["After entry the incumbent now compares Fight 8 vs Accommodate 6: it fights.", "The entrant compares In (-3) with Out (0) and stays out.", "Incumbent earns 12 instead of 6."], "answer": "Yes. The commitment makes the threat credible, so the entrant stays out."},
  {"title": "Bargaining over $100", "problem": "A buyer makes a take-it-or-leave-it offer to split $100 of surplus in $1 steps. The seller accepts or rejects (both get $0). What is the SPE?",
   "steps": ["Seller accepts any offer of $1 or more ($1 > $0).", "Buyer offers $1 and keeps $99."], "answer": "Buyer offers $1, seller accepts: ($99, $1)."}],
 "graph": {"component": "tree", "params": ENTRY, "caption": "Entry game, payoffs (Entrant, Incumbent). Change Fight's incumbent payoff to 8 to see a commitment deter entry."},
 "traps": ["An incumbent's threat to fight is credible only if fighting pays it more than accommodating AFTER entry.",
           "In take-it-or-leave-it bargaining the proposer gets most of the surplus; the responder's threat to reject is not credible.",
           "Patents matter because they change the rival's payoff from cloning."],
 "sources": {"slides": "S20 Game Theory II pp. 42 to 70", "read": "Ch. 10 pp. 330 to 337", "exercise": "Game Theory Exercise Parts 2 and 3", "quiz": "Comprehension Quiz 9 Q8 to Q10; Practice exam Q13, Q27 to Q29"}},
]
import GTX; GTX.add(LESSONS)
for L in LESSONS: write_lesson(L)
write_session("S20", {"overview": "Session 20 adds time to game theory. When a prisoner's dilemma is repeated forever, trigger strategies can sustain collusion: compare the present value of colluding (pi_c + pi_c/i) with cheating once and being punished (pi_d + pi_n/i). When the last period is known, cooperation unravels back to the one-shot outcome. Collusion is more likely with few firms, firms able to punish, a history of cooperation and good punishment mechanisms. In sequential games, drawn as trees, the subgame perfect equilibrium is found by backward induction and ignores threats that are not credible. The same logic applies to entry, innovation and bargaining."})
print([L["id"] for L in LESSONS])
