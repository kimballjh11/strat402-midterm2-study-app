"""Game Theory Exercise (S19/S20, graded, submitted by the student Nov 12). Scenario and all percentages are the professor's;
2019 ad revenue rounded per the instructions: Facebook $70B, Twitter $3B. Payoffs in $ millions, change in annual ad revenue."""
from common import table

SRC = "Game Theory Exercise (your submitted answers, payoffs rechecked)"
ROWS = COLS = ["Ban", "Don't Ban"]
# (Facebook, Twitter); rows Facebook, columns Twitter
P1 = [[(-350, -3), (-350, 23)], [(-277, -3), (-280, -12)]]
P3 = [[(-350, -3), (-350, 29)], [(-137, -3), (-420, -18)]]
def matrix(pay):
    return table(["Facebook \\ Twitter", "Ban", "Don't Ban"], [[r] + [f"{a}, {b}" for a, b in pay[i]] for i, r in enumerate(ROWS)])
# Twitter moves first; payoffs (Twitter, Facebook)
def tree(pay):
    return {"players": ["Twitter", "Facebook"], "tree": {"p": 0, "children": [
        {"a": "Ban", "n": {"p": 1, "children": [{"a": "Ban", "pay": [pay[0][0][1], pay[0][0][0]]}, {"a": "Don't Ban", "pay": [pay[1][0][1], pay[1][0][0]]}]}},
        {"a": "Don't Ban", "n": {"p": 1, "children": [{"a": "Ban", "pay": [pay[0][1][1], pay[0][1][0]]}, {"a": "Don't Ban", "pay": [pay[1][1][1], pay[1][1][0]]}]}}]}}
T2, T3 = tree(P1), tree(P3)

SETUP = ("Facebook and Twitter decide in 2019 whether to ban political ads. Political ads are 0.5% of Facebook's ad revenue ($70B, so $350M) and 0.1% of Twitter's ($3B, so $3M). "
         "A firm that does not ban faces a 10% chance of a fine of 4% of ad revenue (expected fine $280M for Facebook, $12M for Twitter). If Twitter bans and Facebook does not, Twitter's political ads go to Facebook. "
         "If Facebook bans and Twitter does not, 10% of Facebook's political ad revenue ($35M) goes to Twitter. Payoffs are the change in ad revenue in $ millions.")
SETUP3 = ("Part 3 changes only the regulation risk: if both firms don't ban, each faces a 15% chance (expected fines $420M and $18M); if only one firm doesn't ban, that firm faces 5% ($140M and $6M). A firm that bans faces no risk.")

W = {
"S19-02": [{"title": "Game Theory Exercise Part 1: building the matrix", "problem": SETUP + " Put Facebook on the rows and fill in each cell as (Facebook, Twitter).",
  "steps": ["Expected fine for not banning = 10% × 4% × ad revenue: Facebook 0.004 × 70,000 = 280; Twitter 0.004 × 3,000 = 12.",
            "Both ban: each loses its political ads: (-350, -3).",
            "Facebook bans, Twitter doesn't: Facebook -350; Twitter gains 35 and bears its 12 fine: 35 - 12 = 23.",
            "Twitter bans, Facebook doesn't: Twitter -3; Facebook gains 3 and bears 280: -277.",
            "Neither bans: only the expected fines: (-280, -12)."],
  "answer": matrix(P1)}],
"S19-03": [{"title": "Game Theory Exercise Part 1: dominant strategies", "problem": "Using the Part 1 matrix (Facebook rows, Twitter columns):\n\n" + matrix(P1) + "\n\nDoes either firm have a dominant strategy?",
  "steps": ["Facebook: if Twitter bans, Don't Ban -277 > Ban -350; if Twitter doesn't, Don't Ban -280 > -350. Same answer both times.",
            "Twitter: if Facebook bans, Don't Ban 23 > -3; if Facebook doesn't, Ban -3 > -12. The answer changes."],
  "answer": "Facebook: Don't Ban is dominant (its $280M expected fine is less than the $350M it would give up). Twitter has no dominant strategy."}],
"S19-04": [{"title": "Game Theory Exercise Part 1: Nash equilibrium", "problem": "Same Part 1 matrix. Find the Nash equilibrium.",
  "steps": ["Facebook plays its dominant strategy, Don't Ban.", "Twitter's best response to Don't Ban is Ban (-3 > -12).", "Check: neither can gain by switching alone."],
  "answer": "(Facebook Don't Ban, Twitter Ban) = (-277, -3), which matches what actually happened in 2019."},
 {"title": "Game Theory Exercise Part 3: two equilibria", "problem": SETUP3 + "\n\n" + matrix(P3) + "\n\nFind every pure-strategy Nash equilibrium.",
  "steps": ["Facebook: Ban if Twitter doesn't (-350 > -420); Don't Ban if Twitter bans (-137 > -350).",
            "Twitter: Don't Ban if Facebook bans (29 > -3); Ban if Facebook doesn't (-3 > -18).",
            "Each wants the opposite of the other, so no one has a dominant strategy."],
  "answer": "Two equilibria: (Facebook Ban, Twitter Don't Ban) = (-350, 29) and (Facebook Don't Ban, Twitter Ban) = (-137, -3). The one-shot game alone cannot say which happens."}],
"S20-06": [{"title": "Game Theory Exercise Part 2: Twitter moves first", "problem": "Same payoffs as Part 1, but Twitter decides first and Facebook observes. Payoffs (Twitter, Facebook): Ban/Ban (-3, -350); Ban/Don't (-3, -277); Don't/Ban (23, -350); Don't/Don't (-12, -280). Find the SPE.",
  "steps": ["Facebook after Twitter bans: Don't Ban -277 > -350.", "Facebook after Twitter doesn't: Don't Ban -280 > -350.", "Twitter compares Ban (-3) with Don't Ban (-12) and bans."],
  "answer": "Twitter bans, Facebook doesn't: (-3, -277), the same as the Part 1 Nash equilibrium, because Facebook (the follower) has a dominant strategy."},
 {"title": "Game Theory Exercise Part 3: Twitter moves first", "problem": "Part 3 payoffs (Twitter, Facebook): Ban/Ban (-3, -350); Ban/Don't (-3, -137); Don't/Ban (29, -350); Don't/Don't (-18, -420). Find the SPE.",
  "steps": ["Facebook after Twitter bans: Don't Ban -137 > -350.", "Facebook after Twitter doesn't ban: Ban -350 > -420.", "Twitter compares Ban (-3) with Don't Ban (29) and does not ban."],
  "answer": "Twitter doesn't ban, Facebook bans: (29, -350). Moving first lets Twitter pick its favorite of the two Part 3 equilibria."}],
"S20-08": [{"title": "Game Theory Exercise: when does the order of moves matter?", "problem": "Compare Parts 1 and 2 (same outcome) with Part 3 (the sequential game picks one of two equilibria).",
  "steps": ["Parts 1 and 2: Facebook has a dominant strategy, so it does the same thing whatever Twitter does; moving first gives Twitter nothing.",
            "Part 3: the regulation rule removes Facebook's dominant strategy; each firm's best move is the opposite of its rival's.",
            "Then the first mover can commit and force the follower to give in: a first-mover advantage."],
  "answer": "Sequential and simultaneous games predict the same outcome when the follower has a dominant strategy (or the one-shot game has a unique equilibrium that is also the leader's best choice). They can differ when the follower's best response depends on the leader's move."}],
}
def add(lessons):
    for L in lessons:
        extra = [w for w in W.get(L["id"], []) if w["title"] not in {x["title"] for x in L["worked"]}]
        L["worked"] = L["worked"] + extra
        if L["id"] in W: L["sources"]["exercise"] = SRC
