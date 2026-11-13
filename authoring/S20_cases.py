from common import *
from S20_lessons import KEL, TRADE
def num(los, stem, ans, explain, verify, unit=""): return {"los": los, "type": "num", "kind": "calc", "stem": stem, "answer": ans, "unit": unit, "tol": 0.01, "explain": explain, "verify": verify}
def mc(los, kind, stem, choices, ans, explain): return {"los": los, "type": "mc", "kind": kind, "stem": stem, "choices": choices, "answer": ans, "explain": explain}
STREAM = {"players": ["StreamCo", "FlixNet"], "tree": {"p": 0, "children": [{"a": "Launch ad tier", "n": {"p": 1, "children": [{"a": "Copy", "pay": [3, 7]}, {"a": "Don't copy", "pay": [9, 2]}]}}, {"a": "Don't launch", "pay": [4, 4]}]}}
cases = [
 {"id": "S20-case1", "title": "Kellogg's vs. General Mills, forever", "los": ["S20-01", "S20-02", "S20-03"],
  "stem": "From the S20 slides. Kellogg's (rows) and General Mills (columns) decide whether to advertise. Payoffs: (Kellogg's, General Mills).\n\n" + KEL + "\n\nThey play this game every year. Each uses a trigger strategy: keep not advertising unless the other ever advertises, then advertise forever.",
  "parts": [
   mc(["S20-01"], "concept", "In a single play of this game, what happens?", ["Both advertise and earn 2 each", "Neither advertises and both earn 12", "Kellogg's advertises alone", "There is no equilibrium"], 0, "Advertise is dominant for each (15 > 12, 2 > -1)."),
   num(["S20-01"], "At i = 10%, what is Kellogg's present value of colluding (not advertising) forever?", 132, "12 + 12/0.10 = 132.", {"f": "pvc", "c": 12, "i": 0.10}),
   num(["S20-01"], "At i = 10%, what is Kellogg's present value of cheating?", 35, "15 + 2/0.10 = 35.", {"f": "pvd", "d": 15, "n": 2, "i": 0.10}),
   num(["S20-03"], "At what interest rate (as a decimal) is Kellogg's indifferent?", 3.33, "15 + 2/i = 12 + 12/i, so 3 = 10/i, i = 3.33 (333%).", {"f": "istar", "c": 12, "d": 15, "n": 2}),
   mc(["S20-02"], "apply", "Suppose instead both firms know the cereal market will be banned after exactly 5 years. What happens?", ["Both advertise every year", "Neither advertises for 4 years, then both advertise", "Neither ever advertises", "They alternate"], 0, "Known end: year 5 is one-shot, and cooperation unravels back to year 1 (slides p. 28).")]},
 {"id": "S20-case2", "title": "Tariff threats (slides trade game)", "los": ["S20-04", "S20-05", "S20-06"],
  "stem": "From the S20 slides. The US decides whether to threaten tariffs. If it threatens, China concedes or resists. If China resists, the US imposes tariffs or backs down. Payoffs (US, China): No threat (2, 6); Threat, Concede (6, 2); Threat, Resist, Impose (-2, -2); Threat, Resist, Back down (4, 4).",
  "parts": [
   mc(["S20-05"], "concept", "How many decision nodes does this tree have?", ["3", "2", "4", "1"], 0, "US, China, then US again."),
   mc(["S20-06"], "calc", "If China resists, what will the US do?", ["Back down (4 > -2)", "Impose (-2 > 4)", "Threaten again", "Concede"], 0, "Last move first."),
   mc(["S20-06"], "calc", "Anticipating that, what does China do after a threat?", ["Resist (4 > 2)", "Concede (2 > 4)", "Impose", "Nothing"], 0, "Resisting leads to (4, 4)."),
   num(["S20-06"], "What is the US payoff in the subgame perfect equilibrium?", 4, "Threat leads to Resist and Back down: 4, better than No threat (2).", {"f": "spe", "g": TRADE, "who": 0}),
   mc(["S20-06"], "concept", "Why does the US end up backing down?", ["Its threat to impose tariffs is not credible", "China moves first", "Tariffs are illegal", "The US has a dominant strategy to impose"], 0, "When the time comes, imposing pays the US less than backing down.")]},
 {"id": "S20-case3", "title": "StreamCo's ad tier (extra practice)", "los": ["S20-04", "S20-06", "S20-08"],
  "stem": "A made-up example. StreamCo decides whether to launch a cheaper ad-supported tier. If it launches, rival FlixNet decides whether to copy it. Payoffs (StreamCo, FlixNet): Don't launch (4, 4); Launch, Copy (3, 7); Launch, Don't copy (9, 2).",
  "parts": [
   mc(["S20-04"], "concept", "Why is this a sequential game?", ["FlixNet sees StreamCo's choice before deciding", "Both decide at the same time", "It is repeated forever", "Payoffs are random"], 0, "Observation of the earlier move."),
   mc(["S20-06"], "calc", "What does FlixNet do if StreamCo launches?", ["Copy (7 > 2)", "Don't copy (2 > 7)", "Exit", "Randomize"], 0, "Compare FlixNet's payoffs at its node."),
   num(["S20-06"], "What is StreamCo's payoff in the subgame perfect equilibrium?", 4, "Launch leads to Copy: StreamCo gets 3 < 4 from not launching. StreamCo does not launch.", {"f": "spe", "g": STREAM, "who": 0}),
   mc(["S20-08"], "apply", "What would change StreamCo's decision?", ["Something that stops copying, like an exclusive contract or patent, so launching pays 9", "A louder announcement", "Moving second", "Raising FlixNet's payoff from copying"], 0, "Like patents in the innovation game: remove the rival's clone option.")]}]
import GTX
cases.append({"id": "S20-case4", "title": "Political ads, Twitter moves first (Game Theory Exercise Parts 2 and 3)", "los": ["S20-04", "S20-05", "S20-06", "S20-08"],
  "stem": "From the professor's Game Theory Exercise (your submitted answers). Twitter decides first whether to ban political ads; Facebook observes and responds. Payoffs (Twitter, Facebook), $ millions.\n\nPart 2: Ban/Ban (-3, -350); Ban/Don't Ban (-3, -277); Don't Ban/Ban (23, -350); Don't Ban/Don't Ban (-12, -280).\n\nPart 3 (new regulation risk): Ban/Ban (-3, -350); Ban/Don't Ban (-3, -137); Don't Ban/Ban (29, -350); Don't Ban/Don't Ban (-18, -420).",
  "parts": [
   mc(["S20-05"], "concept", "How many end points does each tree have?", ["4", "3", "2", "6"], 0, "Two Twitter choices, each followed by two Facebook choices."),
   mc(["S20-06"], "calc", "What is the Part 2 subgame perfect equilibrium?", ["Twitter Ban, Facebook Don't Ban (-3, -277)", "Twitter Don't Ban, Facebook Ban (23, -350)", "Twitter Don't Ban, Facebook Don't Ban (-12, -280)", "Twitter Ban, Facebook Ban (-3, -350)"], 0, "Facebook never bans; Twitter prefers -3 to -12."),
   num(["S20-06"], "In Part 3, what is Twitter's payoff in the subgame perfect equilibrium?", 29, "Facebook bans after Twitter doesn't (-350 > -420), so Don't Ban gives Twitter 29 > -3.", {"f": "spe", "g": GTX.T3, "who": 0}),
   num(["S20-06"], "In Part 3, what is Facebook's payoff in the subgame perfect equilibrium?", -350, "Twitter doesn't ban; Facebook bans.", {"f": "spe", "g": GTX.T3, "who": 1}),
   mc(["S20-08"], "apply", "Why does moving first help Twitter in Part 3 but not in Part 2?", ["In Part 3 Facebook's best move depends on Twitter's, so Twitter can commit and force Facebook to ban", "Twitter's payoffs are bigger in Part 3", "Facebook moves first in Part 3", "Part 3 is repeated"], 0, "In Part 2 Facebook's Don't Ban is dominant, so order does not matter.")]})
write_cases("S20", cases)
print("cases", len(cases), sum(len(c["parts"]) for c in cases))
