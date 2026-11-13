from common import *
from S19_lessons import VISA, DILL, MON2
def num(los, stem, ans, explain, verify, unit=""): return {"los": los, "type": "num", "kind": "calc", "stem": stem, "answer": ans, "unit": unit, "tol": 0.01, "explain": explain, "verify": verify}
def mc(los, kind, stem, choices, ans, explain): return {"los": los, "type": "mc", "kind": kind, "stem": stem, "choices": choices, "answer": ans, "explain": explain}
DP = [[[2, 1], [4, 2]], [[6, 4], [3, 5]]]; VP = [[[2, 2], [4, 1]], [[1, 4], [3, 3]]]; MP = [[[6, 3], [8, 0]], [[10, 3], [2, 4]]]
cases = [
 {"id": "S19-case1", "title": "Dillard's vs. Nordstrom (in-class exercise)", "los": ["S19-02", "S19-03", "S19-04", "S19-06"],
  "stem": "From the S19 in-class exercise. Dillard's (rows) and Nordstrom (columns) each choose which clothing line to feature. Payoffs: (Dillard's, Nordstrom).\n\n" + DILL,
  "parts": [
   mc(["S19-03"], "calc", "Does Dillard's have a dominant strategy?", ["No: Women's is best if Nordstrom picks Girl's, Girl's is best if Nordstrom picks Women's", "Yes: Women's", "Yes: Girl's", "Yes: both"], 0, "Against Girl's: 6 > 2 (Women's). Against Women's: 4 > 3 (Girl's). The best response changes."),
   mc(["S19-03"], "calc", "Does Nordstrom have a dominant strategy?", ["Yes: Women's", "Yes: Girl's", "No", "Only if Dillard's picks Girl's"], 0, "Against Girl's: 2 > 1. Against Women's: 5 > 4. Women's both times."),
   mc(["S19-04"], "calc", "What is the Nash equilibrium?", ["Dillard's Girl's, Nordstrom Women's", "Dillard's Women's, Nordstrom Girl's", "Dillard's Women's, Nordstrom Women's", "Dillard's Girl's, Nordstrom Girl's"], 0, "Nordstrom plays Women's; Dillard's best response is Girl's (4 > 3)."),
   num(["S19-02", "S19-04"], "What is Dillard's payoff in the Nash equilibrium?", 4, "Cell (Girl's, Women's) = (4, 2). First number = Dillard's.", {"f": "cell", "pay": DP, "i": 0, "j": 1, "who": 0}),
   mc(["S19-06"], "apply", "Dillard's would love the 6 in (Women's, Girl's). Why can't it get there?", ["Nordstrom would not pick Girl's, since Women's is its dominant strategy", "Dillard's cannot choose Women's", "6 is Nordstrom's payoff", "The game has no equilibrium"], 0, "Put yourself in your rival's shoes: Nordstrom always picks Women's.")]},
 {"id": "S19-case2", "title": "Visa vs. Mastercard", "los": ["S19-01", "S19-03", "S19-04", "S19-06"],
  "stem": "From the S19 slides. Visa (rows) and Mastercard (columns) each decide, without seeing the other's choice, whether to lower merchant fees. Payoffs: (Visa, Mastercard).\n\n" + VISA,
  "parts": [
   mc(["S19-01"], "concept", "What kind of game is this?", ["Simultaneous-move, one-shot", "Sequential-move", "Repeated", "Coordination"], 0, "Neither sees the other's choice, and it is analyzed as played once."),
   mc(["S19-03"], "calc", "What should Visa do?", ["Lower its fee: it is dominant (2 > 1 and 4 > 3)", "Maintain its fee: 3 is better than 2", "Randomize", "It depends on Mastercard"], 0, "Slide p. 22."),
   mc(["S19-04"], "calc", "What is the Nash equilibrium?", ["Both lower fees (2, 2)", "Both maintain fees (3, 3)", "Visa lowers, Mastercard maintains (4, 1)", "There is none"], 0, "Both play their dominant strategy Lower."),
   num(["S19-06"], "How much combined payoff do Visa and Mastercard give up in equilibrium compared with both maintaining fees?", 2, "Both maintain: 3 + 3 = 6. Equilibrium: 2 + 2 = 4. Loss: 2.", {"f": "pd_loss", "pay": VP}),
   mc(["S19-06"], "apply", "Could they collude to maintain fees in a one-shot game?", ["No: each would have an incentive to defect and lower its fee", "Yes: both are better off", "Yes: maintaining is dominant", "No: maintaining is not allowed"], 0, "Slide p. 36. Defecting from (3, 3) to Lower pays 4.")]},
 {"id": "S19-case3", "title": "Monitoring the warehouse", "los": ["S19-04", "S19-05"],
  "stem": "A warehouse manager (Boss, rows) decides whether to monitor; a worker (Employee, columns) decides whether to work or shirk. Payoffs: (Boss, Employee).\n\n" + MON2,
  "parts": [
   mc(["S19-04"], "calc", "Is there a pure-strategy Nash equilibrium?", ["No: in every cell one player wants to switch", "Yes: (Monitor, Work)", "Yes: (Don't Monitor, Shirk)", "Yes: two of them"], 0, "(Monitor, Work): boss switches to Don't (10 > 6). (Don't, Work): employee shirks (4 > 3). (Don't, Shirk): boss monitors (8 > 2). (Monitor, Shirk): employee works (3 > 0)."),
   num(["S19-05"], "With what probability should the boss monitor?", 0.25, "Make the employee indifferent: Work = 3; Shirk = 4(1 - p). 3 = 4 - 4p, p = 0.25.", {"f": "mix_p", "pay": MP}, "probability"),
   num(["S19-05"], "With what probability should the employee work?", 0.6, "Make the boss indifferent: Monitor = 6q + 8(1 - q) = 8 - 2q; Don't = 10q + 2(1 - q) = 2 + 8q. q = 0.6.", {"f": "mix_q", "pay": MP}, "probability"),
   num(["S19-05"], "What is the boss's expected payoff in the mixed equilibrium?", 6.8, "With q = 0.6: Monitor = 6(0.6) + 8(0.4) = 6.8 (Don't gives the same).", {"f": "mix_val_row", "pay": MP})]}]
import GTX
P1L = [[list(c) for c in r] for r in GTX.P1]
cases.append({"id": "S19-case4", "title": "Political ads: Facebook vs. Twitter (Game Theory Exercise Part 1)", "los": ["S19-01", "S19-02", "S19-03", "S19-04"],
  "stem": "From the professor's Game Theory Exercise (your submitted answers). " + GTX.SETUP + " Facebook is on the rows, payoffs (Facebook, Twitter):\n\n" + GTX.matrix(GTX.P1),
  "parts": [
   mc(["S19-01"], "concept", "How do both firms first view the decision in Part 1?", ["As a one-shot simultaneous game", "As a sequential game", "As an infinitely repeated game", "As a coordination game"], 0, "Each decides without knowing the other's choice."),
   num(["S19-02"], "What is Facebook's expected regulatory fine if it does not ban ($ millions)?", 280, "10% × 4% × 70,000 = 280.", {"f": "fine", "p": 0.10, "rate": 0.04, "rev": 70000}),
   mc(["S19-03"], "calc", "Which firm has a dominant strategy?", ["Only Facebook: Don't Ban", "Only Twitter: Ban", "Both players", "Neither player"], 0, "Facebook: -277 > -350 and -280 > -350. Twitter's best response changes."),
   mc(["S19-04"], "calc", "What is the Nash equilibrium?", ["Facebook Don't Ban, Twitter Ban (-277, -3)", "Neither bans (-280, -12)", "Facebook Ban, Twitter Don't Ban (-350, 23)", "Both ban (-350, -3)"], 0, "Twitter best-responds to Facebook's dominant Don't Ban with Ban (-3 > -12). It matches 2019."),
   num(["S19-04"], "What is Twitter's payoff in the Nash equilibrium ($ millions)?", -3, "Twitter gives up its $3M of political ads.", {"f": "cell", "pay": P1L, "i": 1, "j": 0, "who": 1})]})
write_cases("S19", cases)
print("cases", len(cases), sum(len(c["parts"]) for c in cases))
