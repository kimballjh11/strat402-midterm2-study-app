from common import *
def num(los, stem, ans, explain, verify, unit=""): return {"los": los, "type": "num", "kind": "calc", "stem": stem, "answer": ans, "unit": unit, "tol": 0.01, "explain": explain, "verify": verify}
def mc(los, kind, stem, choices, ans, explain): return {"los": los, "type": "mc", "kind": kind, "stem": stem, "choices": choices, "answer": ans, "explain": explain}
DATA = table(["2022 Q2", "Daily active users (millions)", "Ad revenue ($ millions)", "Operating expense ($ millions)"],
             [["Meta (Facebook)", "1,970", "28,152", "20,464"], ["Twitter", "237.8", "1,076", "1,520"], ["Snapchat", "347", "1,111", "1,512"]])
cases = [
 {"id": "S18-case1", "title": "Meta, Twitter and Snapchat", "los": ["S18-04", "S18-01", "S18-09", "S18-10"],
  "stem": "From the Barriers to Entry exercise data, 2022 Q2 (Snapchat's revenue is all advertising).\n\n" + DATA,
  "parts": [
   num(["S18-04"], "What was Meta's advertising revenue per daily user?", 14.29, "28,152 / 1,970 = $14.29 per user for the quarter.", {"f": "ratio", "num": 28152, "den": 1970}, "$"),
   num(["S18-04"], "What was Twitter's profit per user (ad revenue minus operating expense, per user)?", -1.87, "Ad revenue per user = 1,076 / 237.8 = $4.52. Cost per user = 1,520.4 / 237.8 = $6.39. Profit = -$1.87.", {"f": "profit_per", "rev": 1076.003, "cost": 1520.422, "users": 237.8}, "$"),
   mc(["S18-04", "S18-09"], "apply", "What best explains why Meta earns about three times Twitter's ad revenue per user?", ["Network effects: more users and data make each user more valuable to advertisers", "Economies of scope in hardware", "Limit pricing against Twitter", "A patent on social networking"], 0,
      "More users bring more data for targeting and more reach for advertisers, so each user brings in more ad revenue."),
   mc(["S18-01", "S18-09"], "apply", "Meta's operating expenses were about 63% of revenue in 2021 Q4 versus about 89% for Twitter. Which barrier best explains Meta's lower cost share?", ["Economies of scale: mostly fixed infrastructure spread over far more users", "Penetration pricing", "Predatory pricing", "Brand advertising"], 0,
      "Data centers, R&D and administration behave like fixed costs; spread over about 2 billion users they are a smaller share of sales."),
   mc(["S18-10"], "apply", "Meta launched Threads in 2023, letting Instagram users join with one tap and keep their followers. Which strategy from Strategies to Crack Well-Guarded Markets is this primarily?", ["Leverage existing assets", "Create a market niche", "Reconfigure the value chain", "Directly attack the market leader"], 0,
      "It used Instagram's user base and social graph, assets Meta already had, to get past Twitter's network effects.")]},
 {"id": "S18-case2", "title": "The razor industry", "los": ["S18-09", "S18-10", "S18-05", "S18-06"],
  "stem": "From the S18 slides (pp. 24 to 25). Razors earned about 60% gross margins and were 9% of P&G's sales but 16% of its profits. Gillette spent $200 million marketing ProGlide with FlexBall. Dollar Shave Club entered with a $20,000 low-budget YouTube video and sold razors by monthly subscription online.",
  "parts": [
   mc(["S18-09"], "concept", "Why would Dollar Shave Club want to enter this market?", ["High margins and profits signal that an entrant could earn above-normal returns", "The market had no incumbents", "Razors have strong network effects", "Gillette's patents had all expired"], 0, "Profits attract entry: 60% gross margins are the honey pot."),
   mc(["S18-09"], "apply", "Which barriers to entry did Gillette's position mainly rest on?", ["Brand and reputation, plus control of retail shelf space", "Network effects", "Learning curves only", "Government licenses"], 0, "A $200 million ad budget and store distribution are brand and shelf-space barriers."),
   mc(["S18-10"], "apply", "Selling online by subscription and marketing with a cheap viral video instead of TV ads and store shelves is mainly which strategy?", ["Reconfigure the value chain", "Leverage existing assets", "Directly attack the market leader", "Limit pricing"], 0, "DSC changed the activities that deliver value to customers (marketing, distribution, sales), bypassing Gillette's strongholds."),
   mc(["S18-05", "S18-06"], "apply", "Suppose, after DSC entered, Gillette had cut its razor prices below its own variable cost in the online channel to force DSC out, planning to raise them later. What would that be?", ["Predatory pricing", "Limit pricing", "Penetration pricing", "Economies of scope"], 0, "Below cost, aimed at a rival already in the market, with recoupment later."),
   mc(["S18-05"], "apply", "Suppose instead that, before DSC entered, Gillette had kept its prices below the monopoly level (but above its cost) to make entry look unprofitable. What would that be?", ["Limit pricing", "Predatory pricing", "Penetration pricing", "A learning curve"], 0, "Below the monopoly price, above own cost, aimed at a potential entrant.")]},
 {"id": "S18-case3", "title": "Drone startup", "los": ["S18-02", "S18-01", "S18-07"],
  "stem": "SkyCo builds delivery drones. Its first drone cost $1,000 to build and it is on an 80% learning curve. It has built 64 drones so far. Its plant and software cost $200,000 per year regardless of output, plus parts that are included in the learning curve cost.",
  "parts": [
   num(["S18-02"], "What did SkyCo's 8th drone cost to build?", 512, "3 doublings (1, 2, 4, 8): 1,000 × 0.8^3 = $512.", {"f": "learn", "C1": 1000, "rate": 0.8, "n": 8}, "$"),
   num(["S18-02"], "What did its 64th drone cost?", 262.144, "6 doublings: 1,000 × 0.8^6 = 1,000 × 0.262144 = $262.14.", {"f": "learn", "C1": 1000, "rate": 0.8, "n": 64}, "$"),
   num(["S18-01"], "If SkyCo spreads its $200,000 fixed cost over 400 drones this year, what is the fixed cost per drone?", 500, "200,000 / 400 = $500 per drone. At 100 drones it would be $2,000: economies of scale.", {"f": "ratio", "num": 200000, "den": 400}, "$"),
   mc(["S18-02"], "apply", "A rival plans to enter by hiring SkyCo's lead production engineers. Why does this threaten SkyCo's learning-curve barrier?", ["Learning is a barrier only if knowledge does not spill over to rivals", "It raises SkyCo's fixed cost", "It creates network effects for the rival", "It is predatory pricing"], 0, "Slide p. 34 and Quiz 8 Q2: no spillovers is the key assumption."),
   mc(["S18-07", "S18-02"], "apply", "SkyCo prices its drones below current unit cost to win a big early contract. Which reason from the S18 slides fits?", ["To descend the learning curve faster and lock in a first-mover cost lead", "Predatory pricing against an existing rival", "Limit pricing above cost", "Economies of scope"], 0, "Slide p. 34: price aggressively to descend the learning curve faster.")]}]
write_cases("S18", cases)
print("cases", len(cases), sum(len(c["parts"]) for c in cases))
