from common import *
from S20_lessons import KEL, PUTIN, TRADE, ENTRY
B = Bank()

def pvc(c, i): return c + c / i
def pvd(d, n, i): return d + n / i
def istar(c, d, n): return (c - n) / (d - c)

def spe(node, players):
    """Backward induction. Returns (payoff tuple, list of 'Player: action' along the path)."""
    if "pay" in node: return tuple(node["pay"]), []
    best = None
    for ch in node["children"]:
        sub = ch["n"] if "n" in ch else ch
        pay, path = spe(sub, players)
        if best is None or pay[node["p"]] > best[0][node["p"]]: best = (pay, [f"{players[node['p']]}: {ch['a']}"] + path)
    return best

def tree_txt(g):
    """Plain text outline of a tree for question stems."""
    P = g["players"]; lines = []
    def walk(node, prefix):
        for ch in node["children"]:
            sub = ch.get("n")
            label = prefix + [f"{P[node['p']]} {ch['a']}"]
            if sub is None: lines.append("- " + " → ".join(label) + f": ({', '.join(map(str, ch['pay']))})")
            else: walk(sub, label)
    walk(g["tree"], [])
    return f"Payoffs: ({', '.join(P)}).\n\n" + "\n".join(lines)

def spe_mc(lo, los, intro, g, explain, wrong):
    pay, path = spe(g["tree"], g["players"])
    right = ", then ".join(path) + f" ({', '.join(map(str, pay))})"
    B.mc(lo, los, "calc", intro + "\n\n" + tree_txt(g) + "\n\nWhat is the subgame perfect equilibrium outcome?", [right] + wrong, 0, explain)
    return pay

def T(players, tree): return {"players": players, "tree": tree}

# ---------------- S20-01 infinitely repeated games ----------------
lo = "S20-01"
B.mc(lo, [lo], "concept", "An infinitely repeated game is:", ["A game played over and over forever, with payoffs received each time it is played", "A game with infinitely many players", "A game played once with infinite payoffs", "A game in which players move one after another"], 0, "Slides p. 31.")
B.mc(lo, [lo], "concept", "Why can collusion be sustained in an infinitely repeated game but not in a one-shot game?", ["A player who defects can be punished in later periods", "Cheating is illegal in repeated games", "Payoffs are larger in repeated games", "Players have no dominant strategy"], 0, "Slides p. 31: players that defect can be punished in subsequent periods.")
B.mc(lo, [lo], "concept", "According to the slides, a player should defect when:", ["The present value of cheating is greater than the present value of collusion", "The one-time payoff from cheating is positive", "The rival has a dominant strategy", "The interest rate is zero"], 0, "Slides p. 33.")
B.mc(lo, [lo], "concept", "What happens to the present value of a payment received every year forever when the interest rate rises?", ["It falls", "It rises", "It stays the same", "It becomes infinite"], 0, "PV = payment / i. A bigger i means a smaller PV: the future counts for less.")
B.tf(lo, [lo], "concept", "True or false: A higher discount (interest) rate makes cheating on a collusive agreement more attractive.", True, "True. The future punishment is worth less today, so the one-time gain from cheating weighs more.")
B.mc(lo, [lo], "concept", "In the formula PV cheat = 15 + 2/i for Kellogg's, what does the 2 represent?", ["The payoff each period after General Mills starts punishing", "The one-time gain from cheating", "The interest rate", "General Mills' payoff from colluding"], 0, "After cheating, both advertise forever and Kellogg's earns 2 per period.")
B.num(lo, [lo], "Kellogg's versus General Mills (slides p. 34):\n\n" + KEL + "\n\nAt i = 10%, what is the present value of colluding (not advertising) forever, counting this period's payoff?", 132,
      "PV collude = 12 + 12/0.10 = 12 + 120 = 132.", {"f": "pvc", "c": 12, "i": 0.10})
B.num(lo, [lo], "Same Kellogg's game at i = 10%. What is the present value of cheating this period, then being punished forever?", 35,
      "PV cheat = 15 + 2/0.10 = 15 + 20 = 35.", {"f": "pvd", "d": 15, "n": 2, "i": 0.10})
B.num(lo, [lo, "S20-03"], "Comprehension Quiz 9 Q6 numbers ($ billions): neither advertises 4 each; the lone advertiser 44; both advertise 0 each. At i = 12%, what is the present value of colluding?", 37.33,
      "PV collude = 4 + 4/0.12 = 4 + 33.33 = 37.33. Cheating is worth 44 + 0/0.12 = 44, so Kellogg's defects.", {"f": "pvc", "c": 4, "i": 0.12}, unit="$ billions")
B.num(lo, [lo], "A firm earns $50 every year forever starting next year. At an interest rate of 20%, what is that stream worth today?", 250,
      "Perpetuity: 50 / 0.20 = 250. (No payment today, so nothing is added.)", {"f": "perp", "c": 50, "i": 0.20}, unit="$")
B.num(lo, [lo], "Two airlines collude on a route and each earns $30 million per year. If one cheats it earns $55 million this year, then $10 million per year forever. At i = 25%, what is the present value of cheating?", 95,
      "PV cheat = 55 + 10/0.25 = 55 + 40 = 95. (PV collude = 30 + 30/0.25 = 150, so they keep colluding.)", {"f": "pvd", "d": 55, "n": 10, "i": 0.25}, unit="$ millions")
cq = pvc(30, 0.25); dq = pvd(55, 10, 0.25)
B.mc(lo, [lo, "S20-03"], "calc", "Same airlines at i = 25%: collude 30 per year forever; cheat 55 once then 10 per year. Should an airline cheat?", ["No: colluding is worth 150 and cheating 95", "Yes: 55 is more than 30", "Yes: cheating is worth 150", "It cannot be determined without the rival's payoffs"], 0,
     f"PV collude = 30 + 30/0.25 = {fmt(cq)}. PV cheat = 55 + 10/0.25 = {fmt(dq)}. Collude.")
B.mc(lo, [lo], "apply", "A firm's owner becomes very impatient and now discounts the future at 300% a year. What does this do to its collusive agreement with a rival?", ["Makes cheating more likely, because future punishment is worth little to it", "Makes collusion more stable", "Has no effect", "Forces the rival to cheat first"], 0, "With a high i, the future punishment term (payoff / i) shrinks.")
B.mc(lo, [lo], "apply", "Two cereal firms have colluded on advertising for decades. Which change would most threaten that collusion?", ["The one-time gain from cheating grows much larger", "Interest rates fall", "The punishment payoff falls", "The game is expected to last forever"], 0, "A bigger temptation (cheat minus collude) raises the PV of cheating relative to colluding.")

# ---------------- S20-02 finitely repeated ----------------
lo = "S20-02"
B.mc(lo, [lo], "concept", "In a game repeated a KNOWN finite number of times, how do players treat the last period?", ["As a one-shot game, since no one can be punished afterward", "As a cooperative game", "As an infinitely repeated game", "As a sequential game"], 0, "Slides p. 28.")
B.mc(lo, [lo], "concept", "According to the slides, finite repeated games:", ["Always collapse back to a one-shot simultaneous game", "Always sustain collusion", "Have no equilibrium", "Turn into sequential games"], 0, "Slides p. 28.")
B.mc(lo, [lo], "concept", "Why does a player have an incentive to break a promise in the second-to-last period of a finitely repeated game?", ["There is no effective punishment in the last period, because both defect then anyway", "The payoffs are larger in that period", "The rival cannot see the move", "Promises are illegal"], 0, "Slides p. 28.")
B.tf(lo, [lo], "concept", "True or false: In a prisoner's dilemma repeated exactly 100 times with a known end, firms should cooperate in the first 99 periods and cheat only in the last.", False, "False. Backward induction unravels cooperation from period 100 all the way back to period 1.")
B.mc(lo, [lo], "concept", "Cooperation can survive in a finitely repeated game when:", ["Players do not know when the game will end", "The last period is announced in advance", "There is only one period", "Payoffs are listed in a tree"], 0, "With an uncertain end there is always a chance of future punishment (textbook).")
B.tf(lo, [lo], "concept", "True or false: The unraveling argument for finitely repeated games uses backward induction, starting from the final period.", True, "True. Solve the last period first, then step back.")
B.mc(lo, [lo, "S20-07"], "apply", "Your only rival announces it will close its store in two weeks. You have kept prices high together for years. What does game theory predict?", ["Collusion breaks down now, since the game has a known end", "Prices stay high until the rival closes", "You should raise prices further", "Nothing changes"], 0, "Like Comprehension Quiz 9 Q7: a known final period removes the threat of punishment.")
B.mc(lo, [lo], "apply", "An employee has announced she will retire in three weeks. Why might her effort drop?", ["The end-of-period problem: there is no future relationship to protect", "Her pay rises", "She has a dominant strategy to work", "The game is infinitely repeated"], 0, "The textbook's end-of-period problem. Firms respond with things like retirement bonuses or references.")
B.mc(lo, [lo], "apply", "A tourist-area street vendor will never see a customer again. Which statement fits?", ["The vendor has an incentive to sell low-quality goods, since there is no repeat business to lose", "The vendor will always sell high quality", "Customers can punish the vendor next period", "This is an infinitely repeated game"], 0, "One-shot interactions remove the reputation incentive.")
B.mc(lo, [lo], "apply", "How could a firm reduce the end-of-period problem with a worker who will leave in a year?", ["Pay part of compensation as a bonus at the end, or make future references depend on performance", "Announce the exact last day to everyone", "Pay everything up front", "Shorten the notice period"], 0, "Making something depend on the last periods keeps a future reward in play.")
B.mc(lo, [lo, "S20-01"], "apply", "Gas stations A and B will compete for exactly 10 weeks before a highway bypass closes their road. Each week's game is a prisoner's dilemma with a unique Nash equilibrium (both price low). What happens in week 1?", ["Both price low", "Both price high, then low in week 10", "Both price high every week", "They alternate"], 0, "Week 10 is one-shot, so both price low; then week 9 has nothing to protect, and so on back to week 1.")
B.mc(lo, [lo], "apply", "Which change would make collusion between two firms easier to sustain?", ["The firms are unsure when their competition will end", "A regulator announces the market will close on a fixed date", "One firm says it will exit next month", "The game is played only once"], 0, "Uncertain end = always a chance of future punishment.")
B.tf(lo, [lo], "apply", "True or false: Visa and Mastercard playing the fee game for exactly two periods would both lower fees in both periods.", True, "True (slides p. 28). The second period is one-shot; the first has no effective punishment.")

B.mc(lo, [lo], "concept", "What condition makes a finitely repeated game unravel to the one-shot outcome in every period?", ["The final period is known and the one-shot game has a unique Nash equilibrium", "The players are patient", "The payoffs are large", "Players move sequentially"], 0, "Both conditions are needed for the backward-induction argument.")
B.mc(lo, [lo, "S20-01"], "apply", "Each year there is a 10% chance that a new law ends two firms' market. Compared with a market that ends on a known date, collusion is:", ["Easier to sustain, since every period may be followed by another", "Harder to sustain", "Impossible", "Required by law"], 0, "An uncertain end works like an infinite horizon with extra discounting (textbook).")

# ---------------- S20-03 trigger strategies ----------------
lo = "S20-03"
B.mc(lo, [lo], "concept", "A trigger strategy is:", ["A strategy contingent on past play, in which a particular past action triggers a different action", "A strategy chosen at random", "A strategy that never changes", "The first move in a sequential game"], 0, "Slides p. 31.")
B.mc(lo, [lo], "concept", "Under a grim trigger strategy, what does a firm do after its rival cheats once?", ["Plays the one-shot Nash (punishment) strategy forever", "Forgives it next period", "Exits the market", "Cheats once, then cooperates"], 0, "The threat of permanent punishment is what makes cheating unattractive.")
B.mc(lo, [lo], "concept", "In i* = (π_c − π_n) / (π_d − π_c), what does the denominator measure?", ["The one-time gain from cheating", "The per-period loss from punishment", "The interest rate", "The collusive payoff"], 0, "Cheat payoff minus collusive payoff, earned once.")
B.mc(lo, [lo], "concept", "Collusion with trigger strategies is sustainable when the interest rate is:", ["At or below the threshold i*", "Above the threshold i*", "Exactly zero only", "Any value"], 0, "Low interest rates make the future punishment matter.")
B.tf(lo, [lo], "concept", "True or false: For a trigger strategy to work, cheating must be detected so the rival knows to punish.", True, "True. Undetected cheating cannot trigger punishment.")
B.num(lo, [lo, "S20-01"], "Kellogg's versus General Mills (slides p. 35):\n\n" + KEL + "\n\nAt what interest rate is Kellogg's indifferent between colluding and cheating? Answer as a decimal.", 3.33,
      "15 + 2/i = 12 + 12/i, so 3 = 10/i and i = 10/3 = 3.33 (333%).", {"f": "istar", "c": 12, "d": 15, "n": 2})
B.num(lo, [lo], "Comprehension Quiz 9 Q6 numbers: collude 4, cheat 44 once, punishment 0. What is the highest interest rate at which collusion holds? Answer as a decimal.", 0.10,
      "i* = (4 − 0) / (44 − 4) = 4/40 = 0.10. At 12% the firm defects.", {"f": "istar", "c": 4, "d": 44, "n": 0})
B.num(lo, [lo], "Colluding pays $20 per period. Cheating pays $45 once, then $5 per period forever. What is the highest interest rate at which collusion holds? Answer as a decimal.", 0.60,
      "i* = (20 − 5) / (45 − 20) = 15/25 = 0.60.", {"f": "istar", "c": 20, "d": 45, "n": 5})
B.num(lo, [lo], "Two shipping firms collude and each earns $8 million per year. A cheater earns $14 million once, then $2 million per year forever. Find i*. Answer as a decimal.", 1.0,
      "i* = (8 − 2) / (14 − 8) = 6/6 = 1.0 (100%).", {"f": "istar", "c": 8, "d": 14, "n": 2})
B.mc(lo, [lo], "calc", "Collude pays 10 per period; cheat pays 30 once, then 4 forever. At i = 40%, should a firm collude?", ["No: i* = 0.30, so 40% is too high", "Yes: i* = 0.30, so collusion holds", "Yes: 10 + 10/0.4 = 35 beats 30", "No: cheating always wins"], 0,
     f"i* = (10 − 4)/(30 − 10) = 0.30. Check: collude 10 + 10/0.4 = {fmt(pvc(10, 0.4))}; cheat 30 + 4/0.4 = {fmt(pvd(30, 4, 0.4))}. Cheat wins.")
B.mc(lo, [lo], "apply", "A firm can raise the payoff it gets in the punishment phase (for example, by having a cheaper backup product). What does that do to collusion?", ["Makes collusion harder: punishment hurts less, so i* falls", "Makes collusion easier", "No effect on i*", "Makes cheating impossible"], 0, "π_n rises, so (π_c − π_n) falls and so does i*.")
B.mc(lo, [lo, "S20-07"], "apply", "A price-matching guarantee punishes a rival's price cut automatically. How does this relate to trigger strategies?", ["It makes punishment fast and certain, supporting collusion", "It makes cheating more profitable", "It is a mixed strategy", "It ends the repeated game"], 0, "A punishment mechanism (slides p. 37).")
B.mc(lo, [lo], "apply", "Why must a trigger-strategy punishment be the one-shot Nash outcome (or something else each firm would actually carry out)?", ["Otherwise the threat to punish is not credible", "Because punishments must be illegal", "Because the slides require it", "Because the game is finite"], 0, "The one-shot Nash outcome has each firm best-responding, so it will really happen.")

# ---------------- S20-04 sequential games ----------------
lo = "S20-04"
B.mc(lo, [lo], "concept", "In a sequential-move game:", ["One player moves after observing another player's move", "Players move without knowledge of each other's moves", "All players move at the same time", "Moves are random"], 0, "Observation is the key. Reading Quiz Q3 offers the simultaneous definition as a false statement.")
B.mc(lo, [lo], "concept", "How do you solve a sequential game?", ["Backward induction: start at the last move and work toward the first", "Start with the first mover's biggest payoff", "Find the dominant strategy in a matrix", "Randomize"], 0, "Reading Quiz Q5.")
B.mc(lo, [lo], "concept", "A sequential game is usually drawn as:", ["A game tree (extensive form)", "A payoff matrix only", "A demand curve", "An isoquant"], 0, "Trees show who moves when.")
B.tf(lo, [lo], "concept", "True or false: Two players who move at different times are in a simultaneous game if the second mover cannot see what the first did.", True, "True. What matters is information, not the clock.")
B.mc(lo, [lo], "concept", "Why does the first mover in a sequential game look ahead?", ["It anticipates how the later player will respond to each choice", "It cannot change its decision", "It always earns the largest payoff", "The later player moves randomly"], 0, "Looking forward, reasoning backward.")
B.mc(lo, [lo], "apply", "A startup launches an app; the market leader sees it and then decides whether to cut prices. What type of game is this?", ["Sequential", "Simultaneous", "One-shot simultaneous with no information", "Mixed strategy"], 0, "The leader observes the launch first.")
B.mc(lo, [lo], "apply", "In the slides' Crimea game, who moves first?", ["Putin, deciding whether to invade", "Obama, deciding whether to sanction", "Both at once", "Neither"], 0, "Obama chooses after seeing Putin's choice.")
B.mc(lo, [lo, "S20-08"], "apply", "Which business situation is best modeled as a sequential game?", ["A union makes a wage offer and management accepts or rejects it", "Two firms submit sealed bids on the same day", "Two stores set prices without seeing each other's ads", "A coin toss"], 0, "Management sees the offer before responding.")
B.mc(lo, [lo], "apply", "Can the same payoffs give a different outcome when played sequentially instead of simultaneously?", ["Yes; the order of moves and what players observe can change the equilibrium", "No; payoffs alone determine outcomes", "Only with three players", "Only if both have dominant strategies"], 0, "That is why firms care about moving first or second.")

# ---------------- S20-05 extensive form ----------------
lo = "S20-05"
B.mc(lo, [lo], "concept", "Which of these is NOT shown in an extensive-form game?", ["The market interest rate", "The players", "The order of moves", "The payoffs"], 0, "A tree shows players, information, strategies, sequence and payoffs.")
B.mc(lo, [lo], "concept", "In a game tree, a decision node represents:", ["A point where a player chooses an action", "A final payoff", "The interest rate", "A random draw"], 0, "Branches out of the node are the actions.")
B.mc(lo, [lo], "concept", "In a game tree, the payoffs appear:", ["At the end of each path", "At the first node only", "In a separate matrix", "Above each branch label"], 0, "Each complete path ends in a payoff vector.")
B.tf(lo, [lo], "concept", "True or false: The extensive form shows the sequence of moves, which a normal-form matrix does not.", True, "True. That is why sequential games use trees.")
B.mc(lo, [lo], "concept", "In the Putin and Obama tree, payoffs are listed (Putin, Obama). What does (10, −5) mean?", ["Putin invades and Obama does not sanction: Putin gets 10, Obama −5", "Putin does not invade", "Obama gets 10", "Both get 10"], 0, "First number = first mover.")
B.mc(lo, [lo], "apply", "In the trade game (payoffs US, China), the US threatens, China resists, and the US imposes tariffs. What are the payoffs?", ["(−2, −2)", "(4, 4)", "(6, 2)", "(2, 6)"], 0, "Slides p. 61.")
B.mc(lo, [lo], "apply", "In the trade game, what is China's payoff if the US makes no threat?", ["6", "2", "4", "−2"], 0, "No threat: (US 2, China 6). China ranked this outcome first.")
B.mc(lo, [lo], "apply", "How many decision nodes does the slides' trade game have?", ["3 (US, China, then US again)", "2", "1", "4"], 0, "US threat decision, China's response, and the US decision after resistance.")
B.mc(lo, [lo, "S20-08"], "apply", "Firm A decides whether to introduce a product; if it does, Firm B decides whether to clone it. How many possible outcomes (end points) does this tree have?", ["3", "4", "2", "6"], 0, "Don't introduce; Introduce and clone; Introduce and don't clone.")
B.mc(lo, [lo], "apply", "The slides turned rankings into payoffs. The US ranked Concede 1st, Back down 2nd, No threat 3rd, Impose 4th. Which payoffs match?", ["Concede 6, Back down 4, No threat 2, Impose −2", "Concede −2, Back down 2, No threat 4, Impose 6", "All equal to 4", "Concede 2, Back down 4, No threat 6, Impose −2"], 0, "Higher rank, higher number: 6 > 4 > 2 > −2.")

# ---------------- S20-06 SPE ----------------
lo = "S20-06"
B.mc(lo, [lo], "concept", "A subgame perfect equilibrium:", ["Is a Nash equilibrium in which every player's choice is optimal at every point in the tree", "Is any Nash equilibrium", "Requires players to move simultaneously", "Ignores the last mover"], 0, "Only credible threats survive.")
B.mc(lo, [lo], "concept", "A threat is credible when:", ["Carrying it out is in the threatener's interest at the moment it must act", "It is stated loudly", "It hurts the other player", "It is written in a contract the threatener can ignore"], 0, "Otherwise rational opponents ignore it.")
B.tf(lo, [lo], "concept", "True or false: Every subgame perfect equilibrium is a Nash equilibrium, but not every Nash equilibrium is subgame perfect.", True, "True. Some Nash equilibria rely on non-credible threats.")
B.mc(lo, [lo], "concept", "When solving for the SPE, where do you start?", ["At the last decisions in the tree", "At the first mover's best payoff", "At the middle node", "At the largest number in the tree"], 0, "Backward induction.")
B.tf(lo, [lo], "concept", "True or false: In the trade game, the US threat to impose tariffs if China resists is credible.", False, "False. After resistance, imposing pays the US −2 and backing down 4, so it backs down.")
spe_mc(lo, [lo, "S20-04", "S20-05"], "The slides' Crimea game.", PUTIN, "Obama: Sanction (−2) beats Don't (−5). Putin: Invade gives 2, Don't invade gives −5. Putin invades and Obama sanctions.",
       ["Putin: Invade, then Obama: Don't sanction (10, -5)", "Putin: Don't invade (-5, 5)", "Putin: Invade, then Obama: Sanction (10, -5)"])
spe_mc(lo, [lo, "S20-04", "S20-05"], "The slides' trade game.", TRADE, "Last move: US after resistance, Back down 4 > Impose −2. China: Resist (4) > Concede (2). US: Threat (4) > No threat (2).",
       ["US: Threat, then China: Concede (6, 2)", "US: No threat (2, 6)", "US: Threat, then China: Resist, then US: Impose (-2, -2)"])
INNOV = T(["Firm A", "Firm B"], {"p": 0, "children": [{"a": "Introduce", "n": {"p": 1, "children": [{"a": "Clone", "pay": [2, 15]}, {"a": "Don't clone", "pay": [8, 1]}]}}, {"a": "Don't introduce", "pay": [0, 0]}]})
spe_mc(lo, [lo, "S20-08"], "Comprehension Quiz 9 Q9 innovation game.", INNOV, "B: Clone 15 > 1. A: Introduce gives 2 > 0.",
       ["Firm A: Introduce, then Firm B: Don't clone (8, 1)", "Firm A: Don't introduce (0, 0)", "Firm A: Introduce, then Firm B: Clone (8, 1)"])
BOOK = T(["A", "B"], {"p": 0, "children": [{"a": "Up", "n": {"p": 1, "children": [{"a": "Up", "pay": [10, 15]}, {"a": "Down", "pay": [5, 5]}]}}, {"a": "Down", "n": {"p": 1, "children": [{"a": "Up", "pay": [0, 0]}, {"a": "Down", "pay": [6, 20]}]}}]})
spe_mc(lo, [lo, "S20-05"], "Textbook-style tree (Figure 10-1 numbers).", BOOK, "B after Up: Up 15 > 5. B after Down: Down 20 > 0. A compares Up (10) with Down (6) and picks Up.",
       ["A: Down, then B: Down (6, 20)", "A: Up, then B: Down (5, 5)", "A: Down, then B: Up (0, 0)"])
p_, _ = spe(PUTIN["tree"], PUTIN["players"])
B.num(lo, [lo], "In the Crimea game, what is Putin's payoff in the subgame perfect equilibrium?", p_[0], "Obama sanctions after an invasion (−2 > −5), so invading gives Putin 2, better than −5.", {"f": "spe", "g": PUTIN, "who": 0})
p_, _ = spe(TRADE["tree"], TRADE["players"])
B.num(lo, [lo], "In the trade game, what is China's payoff in the subgame perfect equilibrium?", p_[1], "Threat, Resist, Back down: (4, 4).", {"f": "spe", "g": TRADE, "who": 1})
THREE = T(["Leader", "Follower"], {"p": 0, "children": [{"a": "Expand", "n": {"p": 1, "children": [{"a": "Match", "n": {"p": 0, "children": [{"a": "Cut price", "pay": [1, 2]}, {"a": "Hold price", "pay": [5, 4]}]}}, {"a": "Stay small", "pay": [9, 3]}]}}, {"a": "Wait", "pay": [4, 6]}]})
p_, path = spe(THREE["tree"], THREE["players"])
B.num(lo, [lo, "S20-04"], "A three-stage game.\n\n" + tree_txt(THREE) + "\n\nWhat is the Leader's payoff in the subgame perfect equilibrium?", p_[0],
      "Last move (Leader after Match): Hold 5 > Cut 1. Follower: Match leads to 4, Stay small gives 3, so Match. Leader: Expand leads to 5, Wait gives 4, so Expand. Outcome (5, 4).", {"f": "spe", "g": THREE, "who": 0})
B.mc(lo, [lo], "apply", "A landlord threatens to evict a tenant who pays rent one day late, but eviction would cost the landlord far more than the late fee. Should the tenant believe the threat?", ["No: carrying it out would hurt the landlord, so it is not credible", "Yes: all threats are credible", "Yes: the landlord moves second", "Only if it is said twice"], 0, "Ask what the threatener would actually do when the time comes.")

# ---------------- S20-07 collusion factors ----------------
lo = "S20-07"
B.mc(lo, [lo], "concept", "Which list matches the slides' factors that influence collusion?", ["Number of firms, firm size, history of the market, punishment mechanisms", "Price, quantity, cost, demand", "Advertising, branding, location, patents", "Interest rates, taxes, tariffs, wages"], 0, "Slides p. 37.")
B.mc(lo, [lo], "concept", "Which form of collusion is illegal?", ["Explicit collusion such as price fixing, bid rigging and market allocation", "Tacit collusion through signaling", "Both forms", "Neither form"], 0, "Slides p. 38.")
B.mc(lo, [lo], "concept", "Tacit collusion is:", ["Firms reaching collusive outcomes indirectly, such as through signaling", "A written price-fixing contract", "A merger", "A government price ceiling"], 0, "Legal and common (slides p. 38).")
B.mc(lo, [lo], "concept", "How does the number of firms affect collusion?", ["Fewer firms make it easier to monitor and punish, so collusion is easier", "More firms make collusion easier", "It has no effect", "Only one firm can collude"], 0, "With n firms there are n(n − 1) monitoring relationships.")
B.mc(lo, [lo], "concept", "Why does firm size matter for collusion?", ["A small firm may lack capacity to punish a large rival that cheats", "Large firms cannot collude", "Size only matters for advertising", "Small firms always cheat"], 0, "Punishment must be possible.")
B.num(lo, [lo], "Using the textbook's count n(n − 1), how many monitoring relationships are there among 5 firms?", 20, "5 × 4 = 20 (versus 2 with two firms).", {"f": "nn1", "n": 5})
B.mc(lo, [lo], "apply", "In 2014 Apple, Google, Intel and Adobe settled a suit over agreements not to poach each other's workers. What kind of collusion is that?", ["Explicit collusion", "Tacit collusion", "Not collusion", "A mixed strategy"], 0, "Slides p. 39: direct agreements.")
B.mc(lo, [lo], "apply", "Airlines publicly talk about 'capacity discipline' on earnings calls, and rivals hold back new flights. What kind of collusion is that most like?", ["Tacit collusion through signaling", "Explicit price fixing", "Bid rigging", "Market allocation by contract"], 0, "Slides pp. 40 to 41.")
B.mc(lo, [lo], "apply", "In which market is tacit collusion most likely?", ["Two firms with publicly posted prices and a long history together", "Twenty firms with secret negotiated prices", "A market with frequent new entrants", "A one-time government auction"], 0, "Few firms, visible prices and history all help.")
B.mc(lo, [lo, "S20-01"], "apply", "Interest rates rise sharply. All else equal, what happens to tacit collusion?", ["It becomes harder to sustain", "It becomes easier to sustain", "No change", "It becomes explicit"], 0, "Future punishment is worth less.")
B.mc(lo, [lo], "apply", "A firm's prices are listed on a price comparison website that rivals check every day. How does this affect collusion?", ["Cheating is seen quickly, so collusion is easier to sustain", "Collusion becomes impossible", "It makes collusion illegal", "No effect"], 0, "Quick detection means quick punishment (Comprehension Quiz 9 Q7 setting).")

# ---------------- S20-08 business applications ----------------
lo = "S20-08"
B.mc(lo, [lo], "concept", "An incumbent threatens to start a price war if a rival enters. When is that threat credible?", ["When fighting pays the incumbent more than accommodating after entry occurs", "Whenever it is announced", "When the entrant is small", "Never"], 0, "Check the incumbent's payoffs at its own node.")
B.mc(lo, [lo], "concept", "How can an incumbent make an entry-deterring threat credible?", ["Make a commitment that changes its own payoffs, such as building extra capacity", "Repeat the threat louder", "Lower its price after entry only if it loses money", "Ask the entrant to stay out"], 0, "A commitment changes the payoff from fighting.")
B.mc(lo, [lo], "concept", "Why do patents encourage innovation, in game theory terms?", ["They remove the rival's option to clone, so introducing pays", "They raise the interest rate", "They make the game simultaneous", "They guarantee a monopoly price forever"], 0, "In the innovation game, cloning can make introducing unprofitable.")
B.mc(lo, [lo], "concept", "In a one-shot take-it-or-leave-it bargaining game, who gets most of the surplus?", ["The player who makes the offer", "The player who responds", "They always split evenly", "Neither gets anything"], 0, "The responder prefers any positive amount to nothing.")
B.tf(lo, [lo], "concept", "True or false: A responder's threat to reject any offer below half is credible in a one-shot take-it-or-leave-it game.", False, "False. Once the offer is made, accepting a small positive amount beats getting nothing.")
B.mc(lo, [lo], "apply", "Entry game (Entrant, Incumbent): Stay out (0, 12); Enter and Fight (−3, 2); Enter and Accommodate (4, 6). What is the SPE?", ["Enter, Accommodate", "Stay out", "Enter, Fight", "There is none"], 0, "Incumbent: Accommodate 6 > Fight 2. Entrant: Enter 4 > 0.")
B.mc(lo, [lo], "apply", "Same entry game, but the incumbent first commits so that fighting pays it 8. What is the SPE now?", ["Entrant stays out (0, 12)", "Enter, Accommodate (4, 6)", "Enter, Fight (−3, 8)", "No equilibrium"], 0, "Fight 8 > Accommodate 6, so entering pays −3 < 0.")
B.num(lo, [lo, "S20-06"], "A buyer makes a take-it-or-leave-it offer on how to split $200 of surplus, in $1 steps. The seller accepts any positive amount. How much does the buyer keep in the SPE?", 199,
      "Seller accepts $1 (better than $0). Buyer keeps 200 − 1 = $199.", {"f": "diff", "x1": 1, "x2": 200}, unit="$")
g = T(["Entrant", "Incumbent"], {"p": 0, "children": [{"a": "Enter", "n": {"p": 1, "children": [{"a": "Fight", "pay": [-2, 3]}, {"a": "Accommodate", "pay": [5, 7]}]}}, {"a": "Stay out", "pay": [0, 15]}]})
pe, _ = spe(g["tree"], g["players"])
B.num(lo, [lo, "S20-06"], "Entry game:\n\n" + tree_txt(g) + "\n\nWhat does the incumbent earn in the SPE?", pe[1], "Incumbent: Accommodate 7 > Fight 3. Entrant: Enter 5 > 0. The incumbent earns 7, not the 15 it would get if the entrant stayed out.", {"f": "spe", "g": g, "who": 1})
B.num(lo, [lo], "Same entry game: Stay out (0, 15); Enter/Fight (−2, F); Enter/Accommodate (5, 7). The incumbent's threat to fight becomes credible once F is greater than what value?", 7,
      "Fighting is credible when F > 7 (the accommodate payoff). Any F of 8 or more deters entry.", {"f": "diff", "x1": 0, "x2": 7})
B.num(lo, [lo, "S20-06"], "Pepsi and Coke (Comprehension Quiz 9 Q10 numbers): if PepsiCo introduces, Coca-Cola can Fight (each earns $100 million) or Acquiesce (Coke $275 million, Pepsi $227 million). How much more does Coca-Cola earn by acquiescing than by fighting?", 175,
      "275 − 100 = $175 million, so the threat to fight is not credible.", {"f": "diff", "x1": 100, "x2": 275}, unit="$ millions")
B.mc(lo, [lo], "apply", "A firm decides whether to develop a new drug. Without a patent, a rival clones it: (developer 2, rival 15) versus (developer 8, rival 1) if no clone; not developing pays (0, 0). Development costs rise by 3 in every outcome where it develops. What happens?", ["The firm does not develop: introducing now pays −1 < 0", "The firm still develops", "The rival does not clone", "Both earn 8"], 0, "Rival still clones (15 > 1), so developing pays 2 − 3 = −1, worse than 0. A patent that blocks cloning would restore 8 − 3 = 5.")
B.mc(lo, [lo], "apply", "A union says it will strike for a year unless it gets a raise, but a strike would cost workers far more than the raise. If management believes the threat is not credible, what does game theory predict?", ["Management refuses the raise", "Management gives the raise", "The union strikes", "Both exit"], 0, "Non-credible threats should not change behavior.")

# ---------------- Game Theory Exercise (submitted) ----------------
import GTX
p, _ = spe(GTX.T2["tree"], GTX.T2["players"])
spe_mc("S20-06", ["S20-06", "S20-04", "S20-05"], "Game Theory Exercise Part 2: Twitter decides first whether to ban political ads; Facebook observes.", GTX.T2,
       "Facebook doesn't ban after either Twitter move (-277 > -350, -280 > -350). Twitter compares -3 (Ban) with -12 (Don't Ban) and bans.",
       ["Twitter: Don't Ban, then Facebook: Ban (23, -350)", "Twitter: Ban, then Facebook: Ban (-3, -350)", "Twitter: Don't Ban, then Facebook: Don't Ban (-12, -280)"])
spe_mc("S20-06", ["S20-06", "S20-08"], "Game Theory Exercise Part 3 (new regulation risk): Twitter decides first; Facebook observes.", GTX.T3,
       "Facebook: Don't Ban after a Twitter ban (-137 > -350); Ban after Twitter doesn't (-350 > -420). Twitter compares -3 with 29 and does not ban.",
       ["Twitter: Ban, then Facebook: Don't Ban (-3, -137)", "Twitter: Ban, then Facebook: Ban (-3, -350)", "Twitter: Don't Ban, then Facebook: Don't Ban (-18, -420)"])
p3, _ = spe(GTX.T3["tree"], GTX.T3["players"])
B.num("S20-06", ["S20-06"], "Game Theory Exercise Part 3 with Twitter moving first. What is Twitter's payoff ($ millions) in the subgame perfect equilibrium?", p3[0],
      "Twitter doesn't ban, Facebook bans (-350 > -420), Twitter gets 35 - 6 = 29.", {"f": "spe", "g": GTX.T3, "who": 0}, unit="$ millions")
B.mc("S20-08", ["S20-08", "S20-04"], "concept", "In the Game Theory Exercise, why did Twitter moving first change nothing in Part 2 but change the outcome in Part 3?",
     ["In Part 2 Facebook had a dominant strategy; in Part 3 its best response depended on Twitter's move", "Twitter's payoffs were larger in Part 2", "Part 3 was a repeated game", "Facebook moved first in Part 3"], 0,
     "A first mover gains only when the follower's best response depends on what the leader does.")
B.mc("S20-04", ["S20-04", "S20-08"], "concept", "When do a sequential game and a one-shot simultaneous game predict the same outcome?",
     ["When the follower has a dominant strategy, so its move does not depend on the leader's", "Whenever payoffs are negative", "Only with three players", "Never"], 0,
     "Game Theory Exercise Part 2: Facebook's dominant Don't Ban made the order irrelevant.")

if __name__ == "__main__": print(B.write())
