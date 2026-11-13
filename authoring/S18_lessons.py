from common import *

PERCENT = {"title": "Per-unit numbers and percent of sales", "body": r"Per user (or per unit) means divide the total by the count: ad revenue per user = ad revenue / users. Percent of sales means divide a cost by revenue: \(\frac{21{,}086}{33{,}671} = 0.626 = 62.6\%\). Keep the units straight: if revenue is in millions of dollars and users are in millions, the result is dollars per user."}
DOUBLING = {"title": "Doublings and powers of 2", "body": r"Doubling from 1 unit: 2, 4, 8, 16, 32, 64, 128. Going from unit 1 to unit 8 is 3 doublings because \(2^3 = 8\). With an 80% learning curve, each doubling multiplies unit cost by 0.8, so after 3 doublings the cost is \(C_1 \times 0.8^3 = 0.512\,C_1\). From unit 100 to unit 400 is 2 doublings (100, 200, 400)."}
AVG = {"title": "Average cost", "body": r"Average total cost is total cost divided by output: \(ATC = TC/Q\) (on the equation sheet). If TC = F + cQ, then \(ATC = F/Q + c\). The F/Q part shrinks as Q grows, which is why spreading a big fixed cost over more units lowers average cost. Example: F = $10,000, c = $5. At Q = 100, ATC = 100 + 5 = $105. At Q = 1,000, ATC = 10 + 5 = $15."}

META = table(["2022 Q2", "Daily active users (millions)", "Ad revenue ($ millions)", "Ad revenue per user", "Operating expense per user", "Profit per user"],
             [["Meta (Facebook)", "1,970", "28,152", "$14.29", "$10.39", "$3.90"], ["Twitter", "237.8", "1,076", "$4.52", "$6.39", "-$1.87"], ["Snapchat", "347", "1,111", "$3.20", "$4.36", "-$1.16"]])
LP_TABLE = table(["", "Limit pricing", "Predatory pricing"],
                 [["Target", "Potential entrants not yet in the market", "A rival already in the market"],
                  ["Timing", "Before entry, to keep entrants out", "After entry, to drive the rival out"],
                  ["Price", "Below the monopoly price, usually still above the incumbent's cost", "Below cost (usual legal test: below average variable cost)"],
                  ["Profit", "Lower than monopoly profit, but still positive", "Losses now, recouped later"],
                  ["Logic", "Low price signals a low-cost or tough incumbent, so entry looks unprofitable", "Push the rival out, then raise prices to recoup the losses"],
                  ["Legality (US)", "Generally legal: it is just a low price", "Can violate Sherman Act §2 (Brooke Group, 1993: below cost plus a dangerous probability of recoupment)"]])
PRICING = table(["Pricing strategy", "Definition (S18 slides p. 41)"],
                [["Limit pricing", "An incumbent maintains a price below the monopoly level in order to prevent entry"],
                 ["Predatory pricing", "A firm temporarily prices below marginal cost to drive competitors out of the market"],
                 ["Penetration pricing", "A firm charges a low price initially to penetrate a market and gain critical mass of customers; useful when strong network effects are present"]])

LESSONS = [
{"id": "S18-01", "title": "Economies of scale", "calc": True,
 "plain": r"""Some businesses have huge costs that do not depend on how much they sell: a power grid, a data center, a factory, a national ad campaign. The more units a firm sells, the thinner that cost is spread, so the **average cost per unit falls as output grows**. That is **economies of scale**.

The professor's definition (Session 6): **economies of scale exist when long-run average costs decline as output is increased.** Diseconomies of scale exist when long-run average costs rise as output increases.

**Why it is a barrier to entry.** An entrant starts small. If average cost keeps falling until output is large, the small entrant pays much more per unit than the big incumbent and cannot match its price. The S18 slides illustrate this three ways:
- Power lines (p. 29): a utility's network is so costly that one firm can serve a region far more cheaply than two.
- An abandoned truck stop (p. 30): a market can be too small to support even one more firm at a reasonable average cost.
- Figure 8-11 from Baye (p. 31): when one firm serves the whole market at \(Q^M\), its average cost is \(ATC(Q^M)\), below the price \(P^M\). If two firms split the market, each produces \(Q^M/2\) and its average cost \(ATC(Q^M/2)\) is **above** the price, so both would lose money. An entrant can see that entry would split the market and raise everyone's average cost.

A useful term: **minimum efficient scale** (MES) is the smallest output at which long-run average cost reaches its minimum. The larger MES is compared with the whole market, the fewer firms the market can support and the bigger the barrier.

**In the Barriers to Entry exercise**, Meta's cost of revenue (data centers, servers, network) is a much smaller share of sales than Twitter's or Snapchat's, because Meta spreads those mostly fixed costs over about 2 billion daily users.""",
 "why": "Economies of scale are the first structural barrier on the S18 slides and come up again in oligopoly (S21, S22). Exam questions describe a scenario and ask which barrier it shows.",
 "definition": "Economies of scale exist when long-run average costs decline as output is increased. Diseconomies of scale exist when long-run average costs rise as output is increased.",
 "formulas": [{"name": "Average total cost", "tex": r"ATC = \frac{TC}{Q}", "onSheet": True},
              {"name": "Average cost with a fixed cost", "tex": r"ATC = \frac{F}{Q} + c", "onSheet": False, "note": "Follows from ATC = TC/Q with TC = F + cQ."}],
 "derivation": r"With \(TC = F + cQ\), \(ATC = \frac{F + cQ}{Q} = \frac{F}{Q} + c\). As Q grows, \(F/Q\) falls toward zero, so ATC falls toward c. That falling ATC is economies of scale.",
 "math": [AVG],
 "worked": [{"title": "Incumbent versus small entrant", "problem": "A ride-sharing app costs $50 million per year to run (servers, engineering, insurance) plus $4 per ride. The incumbent gives 25 million rides per year. An entrant expects 2 million rides. Compare average costs.",
   "steps": [r"Incumbent: \(ATC = 50{,}000{,}000/25{,}000{,}000 + 4 = 2 + 4 = \$6\) per ride.", r"Entrant: \(ATC = 50{,}000{,}000/2{,}000{,}000 + 4 = 25 + 4 = \$29\) per ride.", "If the incumbent charges $10, it earns $4 per ride while the entrant loses $19 per ride."],
   "answer": "$6 versus $29 per ride. The fixed cost spread over far fewer rides is the entrant's barrier."},
  {"title": "Figure 8-11 logic", "problem": "Market demand at the monopoly price supports 1,000 units. ATC is $8 at 1,000 units and $14 at 500 units. The price is $10. Would a second firm enter if it expects to split the market?",
   "steps": ["One firm: ATC $8 < price $10, profit $2 per unit.", "Two firms, 500 each: ATC $14 > $10, each loses $4 per unit."], "answer": "No. Splitting the market raises average cost above the price."}],
 "graph": {"component": "scale", "params": {"view": "ac", "F": 5000, "c": 5, "d": 0.02, "demand": 1500}, "caption": "Average cost falls while fixed cost is being spread (economies of scale), then rises (diseconomies). Shrink the market or raise the fixed cost and watch how few firms the market supports."},
 "traps": ["Economies of scale are about output **per period** (how big you are now). Learning curves are about **cumulative** output (how much you have ever made). Do not mix them up.",
           "Economies of scale lower AVERAGE cost, not necessarily marginal cost.",
           "Economies of scope is a different idea: savings from producing different products together.",
           "Bigger is not always cheaper: past minimum efficient scale, diseconomies of scale make average cost rise."],
 "sources": {"slides": "S18 Barriers to Entry pp. 29 to 31; S06 Cost slides", "read": "Ch. 5 and Module Group A Module 1", "exercise": "Barriers to Entry Exercise step 6 (cost structure)", "quiz": ""}},

{"id": "S18-02", "title": "Learning curves", "calc": True,
 "plain": r"""The more of something you have ever made, the better you get at making it: workers find shortcuts, engineers fix the process, suppliers adapt. A **learning curve** is a graph of that learning: **cost per unit falls as cumulative production rises** (S18 slides p. 32).
- Learning = declining costs per unit.
- Experience = cumulative production (everything you have produced so far, not output this month).

**The Model T (slide p. 32).** From 1910 to 1925 Ford's cost per unit (in 2013 dollars) fell along the curve \(y = 87{,}244x^{-0.317}\), where x is cumulative production. Each time cumulative production doubled, cost fell to \(2^{-0.317} \approx 0.80\) of its old level, about a 20% drop per doubling. That is an **80% learning curve**.

**Why it is a barrier.** An incumbent far down the curve has low costs. An entrant starts at the top with high costs, so it cannot match the incumbent's price until it has produced a lot.

**Which curve is the bigger barrier (slide p. 33)?** Compare how far costs fall and how long it takes. A curve that drops almost all the way in the first few units is a weak barrier, since an entrant gets there quickly too. A curve that keeps falling over a long range of cumulative output, so the incumbent's lead holds for a long time, is a stronger barrier. A curve that barely falls gives the incumbent little advantage.

**Strategic implications (slide p. 34):**
1. Firms may be willing to **price aggressively to descend the learning curve faster** (sell more now to get cheaper sooner).
2. Learning effects as a barrier **assume no knowledge spillovers or leakage**. If employees leave for rivals or the know-how is easy to copy, the entrant learns for free (Comprehension Quiz 8 Q2: true).""",
 "why": "Comprehension Quiz 8 Q2 tests the spillover condition. Learning also explains why incumbents price low early and why first movers can stay ahead (S18-07).",
 "definition": "A learning curve is a graphical representation of learning that increases with experience: cost per unit declines as cumulative production increases.",
 "formulas": [{"name": "Unit cost after k doublings", "tex": r"C = C_1 \times (\text{rate})^k", "onSheet": False, "note": "An 80% curve has rate 0.8. k = number of times cumulative output has doubled."},
              {"name": "Power form", "tex": r"C(x) = C_1 x^{b},\quad \text{rate} = 2^{b}", "onSheet": False, "note": "Model T: b = -0.317, so the rate is about 0.80."}],
 "derivation": r"If \(C(x) = C_1x^b\), doubling x gives \(C(2x) = C_1(2x)^b = 2^b C_1x^b = 2^b C(x)\). So every doubling multiplies cost by the same factor \(2^b\), the learning rate. For the Model T, \(2^{-0.317} = 0.803\).",
 "math": [DOUBLING],
 "worked": [{"title": "An 80% learning curve", "problem": "The first unit of a new drone costs $1,000 to build. The firm is on an 80% learning curve. What does the 8th unit cost? The 64th?",
   "steps": ["Unit 8 is 3 doublings past unit 1 (1, 2, 4, 8).", r"\(1{,}000 \times 0.8^3 = 1{,}000 \times 0.512 = \$512\).", r"Unit 64 is 6 doublings: \(1{,}000 \times 0.8^6 = 1{,}000 \times 0.262 = \$262\)."],
   "answer": "$512 for unit 8, $262 for unit 64. An entrant starting today pays $1,000 for its first unit."}],
 "graph": {"component": "scale", "params": {"view": "learning", "C1": 1000, "rate": 0.8, "N": 128}, "caption": "Each doubling of cumulative output multiplies unit cost by the learning rate. Lower the rate (faster learning) and the incumbent's lead over a new entrant grows."},
 "traps": ["The x axis is CUMULATIVE production, not output per period. That is the difference from economies of scale.",
           "An 80% learning curve means cost falls TO 80% (a 20% drop) per doubling, not BY 80%.",
           "Learning is only a barrier if knowledge does not spill over to rivals.",
           "A curve that falls very fast and then goes flat is a weak barrier: entrants catch up quickly."],
 "sources": {"slides": "S18 Barriers to Entry pp. 32 to 34", "read": "Module Group A Module 1 (learning-curve effects)", "exercise": "Barriers to Entry Exercise (Meta's experience advantage)", "quiz": "Comprehension Quiz 8 Q2"}},

{"id": "S18-03", "title": "Economies of scope", "calc": False,
 "plain": r"""**Economies of scope** are savings from making **different** products together. If one firm can produce two products more cheaply than two separate firms each producing one, there are economies of scope. The savings come from sharing something: a factory, a brand, a distribution network, customer data, a store.

The S18 slides list economies of scope among the concepts to know (p. 27), and the Session 6 slides list "economies of scale and scope" as a source of cost advantage. The slides give no separate example, so here is the textbook definition (Baye, Ch. 5): economies of scope exist when the total cost of producing two outputs together is less than the cost of producing each one separately:
$$C(Q_1, 0) + C(0, Q_2) > C(Q_1, Q_2)$$

**Why it is a barrier.** A firm already selling related products can add a new one at low extra cost. A one-product entrant has to pay for everything by itself, so it starts at a cost disadvantage.

**Why it also helps entrants.** The same idea is how many entrants get in. "Leverage existing assets" in Strategies to Crack Well-Guarded Markets is economies of scope used as an entry strategy: McDonald's put Redbox DVD kiosks in restaurants it already had, Toys "R" Us used its brand, locations and distribution to open Babies "R" Us, and Costco Home used Costco's brand and member base.

**Scale versus scope:**
- Scale: MORE of the SAME product lowers average cost.
- Scope: making DIFFERENT products TOGETHER lowers total cost.""",
 "why": "Exam questions describe a firm sharing assets across products and ask which concept applies. The usual mix-up is with economies of scale.",
 "definition": "Economies of scope exist when the total cost of producing two products within the same firm is lower than when the products are produced by separate firms: C(Q1, 0) + C(0, Q2) > C(Q1, Q2).",
 "formulas": [{"name": "Economies of scope", "tex": r"C(Q_1, 0) + C(0, Q_2) > C(Q_1, Q_2)", "onSheet": False, "note": "Memorize the idea: separate costs more than together."}],
 "derivation": "",
 "math": [],
 "worked": [{"title": "Testing for economies of scope", "problem": "Making 1,000 phones alone costs $300,000. Making 1,000 tablets alone costs $200,000. Making both in the same plant with shared chips and engineers costs $420,000. Are there economies of scope? How much is saved?",
   "steps": ["Separate: $300,000 + $200,000 = $500,000.", "Together: $420,000.", "$500,000 > $420,000, so yes."], "answer": "Economies of scope; producing together saves $80,000."}],
 "traps": ["Scope is about DIFFERENT products made together. Scale is about MORE of one product.",
           "Economies of scope compare TOTAL costs of the bundle with the sum of separate costs; you do not compare average costs of one product.",
           "Leveraging existing assets to enter a new market is economies of scope in action, so a scope question can be dressed up as an entry strategy question."],
 "sources": {"slides": "S18 Barriers to Entry p. 27 (objective list); S06 Cost slides p. 8", "read": "Ch. 5 (multiple-output cost functions); Strategies to Crack Well-Guarded Markets (leverage existing assets)", "exercise": "", "quiz": ""}},

{"id": "S18-04", "title": "Network effects", "calc": True,
 "plain": r"""A product has **network effects** when it becomes more valuable to each user as more people use it. A phone is useless if no one else has one. A classifieds site is worth visiting only if sellers are there, and worth listing on only if buyers are there.

**Why it is a barrier.** An incumbent with a big network offers more value than any newcomer can, even if the newcomer's product is better, because the newcomer starts with no users. Users stay put because switching alone gains nothing; everyone would have to move together. The textbook calls this **consumer lock-in**.

**Slide examples:**
- **KSL Classifieds** (p. 39): a Utah site owned by the Church defeated Craigslist in Utah. Once the local buyers and sellers were on KSL, Craigslist could not pull them away.
- **Google** (p. 40): more searchers attract more advertisers, which raises revenue per user. In class this was the answer to why Google commands higher advertising revenue per user (Comprehension Quiz 8 Q3: network effects).

**The Barriers to Entry exercise.** Meta, Twitter and Snapchat, 2022 Q2 (computed from the exercise data):

""" + META + r"""

Meta earns about three times the ad revenue per user of Twitter and four times Snapchat's. The more people on the platform, the more data Meta has for targeting and the more advertisers want to reach them, so each user is worth more.

**Textbook ideas (Module 4):**
- A two-way network with n users has \(n(n-1)\) possible connections. Adding one user adds \(2n\) connections, which benefits every existing user.
- **Critical mass**: the number of users needed before the network is attractive enough to keep growing on its own.
- To overcome an incumbent's network, an entrant can use **penetration pricing** (S18-08): price very low or free to reach critical mass (Reading Quiz Q5).""",
 "why": "Network effects drive the Meta exercise, Reading Quiz Q5 and Comprehension Quiz 8 Q3, and they explain why platforms are so hard to enter.",
 "definition": "Network effects exist when the value of a product to each user increases as more people use it.",
 "formulas": [{"name": "Revenue per user", "tex": r"\frac{\text{Ad revenue}}{\text{Users}}", "onSheet": False},
              {"name": "Profit per user", "tex": r"\frac{\text{Revenue}}{\text{Users}} - \frac{\text{Operating expense}}{\text{Users}}", "onSheet": False},
              {"name": "Connections in a two-way network", "tex": r"n(n-1)", "onSheet": False, "note": "Textbook Module 4. A new user adds 2n."}],
 "derivation": r"Each of the n users can connect to each of the other \(n - 1\), and a connection from A to B is counted separately from B to A, so there are \(n(n-1)\). With \(n + 1\) users: \((n+1)n - n(n-1) = n^2 + n - n^2 + n = 2n\) new connections.",
 "math": [PERCENT],
 "worked": [{"title": "Meta's revenue per user", "problem": "In 2022 Q2 Meta had 1,970 million daily users, $28,152 million of ad revenue and $20,464 million of operating expense. Find ad revenue, cost and profit per user.",
   "steps": [r"Ad revenue per user = 28,152 / 1,970 = $14.29.", r"Operating expense per user = 20,464 / 1,970 = $10.39.", "Profit per user = 14.29 - 10.39 = $3.90 (this uses ad revenue only, as in Table 1 of the exercise)."],
   "answer": "$14.29 revenue, $10.39 cost, $3.90 profit per user. Twitter's profit per user was -$1.87."},
  {"title": "Counting connections", "problem": "A messaging network has 10 users. How many possible connections? How many does an 11th user add?",
   "steps": [r"\(10 \times 9 = 90\).", r"New user adds \(2 \times 10 = 20\); check: \(11 \times 10 = 110 = 90 + 20\)."], "answer": "90 connections; the 11th user adds 20."}],
 "graph": {"component": "scale", "params": {"view": "network", "k": 0.2, "price": 40, "N": 600}, "caption": "Each user's value rises with the number of users. Below critical mass the network stalls; above it, it grows on its own. An entrant starts at zero users."},
 "traps": ["Network effects raise value to USERS as the network grows. Economies of scale lower the FIRM's average cost as output grows. Meta has both; the exercise ties its REVENUE advantage to network effects and its COST advantage to scale.",
           "A better product does not beat a big network by itself; users are locked in.",
           "Penetration pricing is the entrant's tool against network effects; predatory pricing is not (it targets a rival, below cost).",
           "Count connections as n(n - 1), not n squared."],
 "sources": {"slides": "S18 Barriers to Entry pp. 39 to 40", "read": "Module Group A Module 4", "exercise": "Barriers to Entry Exercise steps 2 to 5", "quiz": "Reading Quiz Q5; Comprehension Quiz 8 Q3"}},

{"id": "S18-05", "title": "Limit pricing", "calc": False,
 "plain": r"""A monopolist would normally charge the monopoly price \(P^M\). But a high price and fat profits invite entry. **Limit pricing** is when the incumbent deliberately keeps its price **below the monopoly level to prevent entry** (slides p. 41).

**How it works (Figure M1-2, slides p. 43).** The incumbent produces \(Q^L\), more than the monopoly quantity \(Q^M\), so the price falls to \(P^L\). An entrant can only sell to the demand the incumbent leaves over, its **residual demand** (market demand minus \(Q^L\)). If that residual demand lies below the entrant's average cost curve everywhere, there is no output at which the entrant can make a profit, so it stays out.

**Limit versus predatory pricing (slides p. 46):**

""" + LP_TABLE + r"""

**Examples.**
- Airlines and Southwest (slides p. 42, a 2020 Journal of Political Economy model of dynamic limit pricing in airlines): incumbents cut fares on routes Southwest threatens to enter.
- Comprehension Quiz 8 Q5: a drug company lowers prices before its patent expires to signal to generic makers that profits would be minimal. That is limit pricing, not predatory pricing, because the generics have not entered yet.

**The catch (textbook).** A fully informed entrant cares about the price **after** it enters. A low price today only deters entry if it is tied to the entrant's future profits: a commitment (such as large capacity the incumbent will use anyway), learning-curve cost advantages, signaling low costs when the entrant cannot see them, or a reputation for fighting entry. The S18 overview says to focus on the concept, not the textbook's present-value math.""",
 "why": "Reading Quiz Q4 and Comprehension Quiz 8 Q5 test limit pricing directly, and the distinction from predatory pricing is a classic exam question.",
 "definition": "Limit pricing: a strategy where an incumbent maintains a price below the monopoly level in order to prevent entry.",
 "formulas": [{"name": "Entrant's residual demand", "tex": r"D^M - Q^L", "onSheet": False, "note": "Entry is deterred if residual demand is below the entrant's AC at every output."}],
 "derivation": "",
 "math": [],
 "worked": [{"title": "Does the limit price deter entry?", "problem": "An incumbent's monopoly price is $50. Its own average cost is $20. A potential entrant's lowest possible average cost is $32. The incumbent sets a price of $30. Does this deter entry? Is it limit or predatory pricing?",
   "steps": ["The entrant could not cover its $32 average cost at $30, so entry is unprofitable.", "$30 is below the $50 monopoly price but above the incumbent's $20 cost, so the incumbent still earns $10 per unit.", "The entrant has not entered yet."],
   "answer": "Entry is deterred. This is limit pricing: below monopoly price, above own cost, aimed at a potential entrant."}],
 "graph": None,
 "traps": ["Limit pricing targets firms NOT YET in the market. Predatory pricing targets a rival ALREADY in the market.",
           "A limit price is usually still ABOVE the incumbent's cost, so it still earns a profit. Predatory pricing is BELOW cost.",
           "Limit pricing is generally legal. Predatory pricing can violate the Sherman Act.",
           "Penetration pricing is a low price by an ENTRANT or new product to build a customer base, not to block others."],
 "sources": {"slides": "S18 Barriers to Entry pp. 41 to 43, 46", "read": "Module Group A Module 1", "exercise": "", "quiz": "Reading Quiz Q4; Comprehension Quiz 8 Q5"}},

{"id": "S18-06", "title": "Predatory pricing", "calc": False,
 "plain": r"""**Predatory pricing** is when a firm **temporarily prices below marginal cost to drive competitors out of the market** (slides p. 41). It takes losses now in the hope of monopoly profits later: push the rival out, then raise prices to recoup the losses (slides p. 46).

**Legality.** It can violate **Sherman Act §2**. Under **Brooke Group (1993)**, a plaintiff must show pricing below cost plus a dangerous probability of recoupment (the predator can later raise prices enough to make back its losses). Courts usually use **below average variable cost** as the test for "below cost." It is hard to prove, because aggressive but legal competition also looks like low prices.

**Slide examples.** Uber was sued for predatory pricing by a San Francisco taxi company (p. 44). The slides also show iBAHN (p. 45).

**Why it often fails (textbook).** The losses must be recouped later, which only works if the rival actually exits and no one else enters once prices rise. The rival can re-enter, or someone can buy its assets cheaply and come back. It works best for a deep-pocketed firm against a cash-strapped rival. Textbook example: Microsoft gave Internet Explorer away free and bundled it with Windows to cut off Netscape; it lost the antitrust case.

**Compare (slides p. 46):** limit pricing is aimed at potential entrants, before entry, at a price usually still above cost, and is generally legal. Predatory pricing is aimed at an existing rival, after entry, below cost, with losses now and recoupment later.""",
 "why": "The limit versus predatory comparison table (slides p. 46) is built to be tested: target, timing, price, profit, logic, legality.",
 "definition": "Predatory pricing: a strategy where a firm temporarily prices below marginal cost to drive competitors out of the market.",
 "formulas": [],
 "derivation": "",
 "math": [],
 "worked": [{"title": "Classifying a price cut", "problem": "A national chain opens next to a local hardware store and sells hammers at $6 when they cost it $9 each. Once the local store closes, the chain raises the price to $15. Classify it and say what a court would look for.",
   "steps": ["The rival is already in the market: that rules out limit pricing.", "The price is below the chain's cost and the plan is to raise it after the rival exits.", "Court test: price below cost (usually average variable cost) and a dangerous probability of recouping the losses."],
   "answer": "Predatory pricing; potentially illegal under Sherman Act §2."}],
 "graph": None,
 "traps": ["Predatory = BELOW COST, aimed at an EXISTING rival. A low price that is still above cost is not predatory.",
           "Predatory pricing means losses NOW and recoupment LATER. Limit pricing keeps a positive profit throughout.",
           "Penetration pricing can also be below cost, but its goal is to win customers and reach critical mass, not to drive a rival out.",
           "Being below cost is not enough for a legal case: Brooke Group also requires a dangerous probability of recoupment."],
 "sources": {"slides": "S18 Barriers to Entry pp. 41, 44 to 46", "read": "Module Group A Module 2", "exercise": "", "quiz": ""}},

{"id": "S18-07", "title": "First-mover advantage", "calc": False,
 "plain": r"""A **first-mover advantage** is the benefit a firm gets from being first: entering a market, setting capacity, or choosing a strategy before rivals can. The first mover gets to shape the game the others face.

**Where it comes from:**
- **Commitment** (textbook Module 3): moving first and committing, for example by building big capacity, forces rivals to respond to what you already did. The textbook shows that turning a simultaneous game into a sequential one can raise the leader's payoff. The commitment only works if it is **irreversible** and **observable** to rivals. You will see this again in game theory (S19, S20) and Stackelberg oligopoly.
- **Network effects and lock-in** (Module 4): the first network to reach critical mass keeps its users even when a better one arrives. eBay's first-mover advantage beat Yahoo! auctions even though Yahoo! offered free listings.
- **Learning curves**: the first mover has the most cumulative output and the lowest costs.
- **Closing the door behind you** (Strategies to Crack Well-Guarded Markets): once in, an entrant should erect its own barriers: go mainstream quickly, secure scarce inputs or locations, invest preemptively in capacity, generate network effects, or race down the experience curve. JetBlue bought up Embraer's manufacturing capacity for two years when it launched its new jet service. Red Bull did not close the door, and more than 150 me-too brands followed.
- In the Barriers to Entry exercise, Meta's head start (daily users before Twitter and Snapchat reported any) fed its network and learning advantages.

**Second-mover advantage.** Moving first is not always better. A follower can free-ride on the leader's research and customer education, learn from its mistakes and enter with a better or cheaper product. The textbook's Metaverse example: being first means burning money on trial and error.""",
 "why": "Practice exam Q13 is mapped to this objective. It connects barriers to entry to the game theory sessions that follow.",
 "definition": "First-mover advantage: the advantage a firm gains by moving (entering, committing, choosing) before its rivals, which lets it shape their best responses.",
 "formulas": [],
 "derivation": "",
 "math": [],
 "worked": [{"title": "Leader or follower (textbook Table M3-1)", "problem": "Firms A and B each choose Low or High output. Payoffs (A, B): Low/Low (30, 10), Low/High (10, 15), High/Low (20, 5), High/High (1, 2). Simultaneously, Low is A's best choice either way, so B picks High: A gets 10. What happens if A moves first and B sees A's choice?",
   "steps": ["If A picks Low, B compares 10 vs 15 and picks High: A gets 10.", "If A picks High, B compares 5 vs 2 and picks Low: A gets 20.", "A picks High."],
   "answer": "Moving first raises A's payoff from 10 to 20: a first-mover advantage. B falls from 15 to 5."}],
 "graph": None,
 "traps": ["A first-mover advantage needs a commitment rivals can SEE and that cannot be UNDONE. A cheap promise is not a commitment.",
           "Sometimes the second mover wins (free-riding on the leader's R&D). Do not assume first is always better.",
           "First-mover advantage often works THROUGH other barriers: network lock-in, learning curves, scarce inputs."],
 "sources": {"slides": "S18 Barriers to Entry (study guide objective)", "read": "Module Group A Module 3; Strategies to Crack Well-Guarded Markets (closing the door)", "exercise": "Barriers to Entry Exercise", "quiz": "Practice exam Q13"}},

{"id": "S18-08", "title": "Penetration pricing", "calc": False,
 "plain": r"""**Penetration pricing** is when a firm **charges a low price initially to penetrate a market and gain a critical mass of customers**. It is useful **when strong network effects are present** (slides p. 41).

The logic: a network product is worth little until enough people use it, and users are locked into the incumbent. A low price, or a free product, or even paying users to try it, gets enough people to switch at once. Once the network passes critical mass, its own value keeps users and the firm can raise prices or charge the other side of the market.

**Examples:**
- Facebook (slides p. 47): free to users from the start, which built the network that now earns it the highest ad revenue per user (S18-04).
- "Competing Against Free" (slides p. 48), an HBR article by Bryce, Dyer and Hatch on free offerings spreading from online markets to physical ones.
- Reading Quiz Q5: a new social media app is worth little to its first users; penetration pricing (a low price or giving it away to build a critical mass) is the strategy that helps it overcome network effects.
- Textbook: Yahoo! offered free auction listings to pull users from eBay. It failed, because eBay's network and first-mover advantage were too strong. Penetration pricing does not always work.

**How it differs from the other pricing strategies:**

""" + PRICING + r"""

Penetration pricing is about building a customer base. Limit pricing is about keeping potential entrants out. Predatory pricing is about driving an existing rival out.""",
 "why": "Practice exam Q5 is mapped here, and Reading Quiz Q5 asks which strategy beats network effects.",
 "definition": "Penetration pricing: a strategy where a firm charges a low price initially to penetrate a market and gain critical mass of customers; useful when strong network effects are present.",
 "formulas": [],
 "derivation": "",
 "math": [],
 "worked": [{"title": "Choosing a pricing strategy", "problem": "A startup launches a payments app that is only useful if your friends also have it. A dominant app already exists. Which pricing strategy fits, and why not the others?",
   "steps": ["Strong network effects plus an entrenched incumbent: the startup needs critical mass.", "Limit pricing is for an incumbent keeping entrants out; the startup is the entrant.", "Predatory pricing targets a rival to drive it out and risks antitrust; the goal here is to win users."],
   "answer": "Penetration pricing: free or very cheap at first, maybe with a sign-up bonus, until enough users join."}],
 "graph": {"component": "scale", "params": {"view": "network", "k": 0.1, "price": 30, "N": 800}, "caption": "Lower the price to join and critical mass falls. That is what penetration pricing does: it gets a new network past the point where it grows on its own."},
 "traps": ["Penetration pricing is mainly an ENTRANT's or new product's tool for network markets.",
           "Its goal is CUSTOMERS (critical mass), not pushing a rival out (predatory) or keeping entrants away (limit).",
           "It does not always work: Yahoo! auctions failed against eBay's network."],
 "sources": {"slides": "S18 Barriers to Entry pp. 41, 47 to 48", "read": "Module Group A Module 4", "exercise": "", "quiz": "Reading Quiz Q5; Practice exam Q5"}},

{"id": "S18-09", "title": "Common barriers to entry", "calc": False,
 "plain": r"""Profits attract entrants. A market stays profitable only if something keeps entrants out. **A barrier to entry is any factor that** (slides p. 28):
- increases the cost borne by potential entrants after they enter the market, **or**
- decreases the market share potential of entrants upon entering an industry.

Comprehension Quiz 8 Q1: the answer is **both**.

**The barriers on the S18 slides:**
1. **Economies of scale** (pp. 29 to 31): small entrants have higher average cost (S18-01).
2. **Learning curves** (pp. 32 to 34): incumbents are further down the cost curve (S18-02).
3. **Brand and reputation** (pp. 35 to 36): Richard Branson drove a tank through a wall of cans in Times Square to launch Virgin Cola, which never topped 1% of U.S. cola. Gillette versus Dollar Shave Club.
4. **Patents and other legal barriers** (pp. 37 to 38): a Wall Street Journal story (Oct. 2025) on the fight over FICO's dominance of credit scores.
5. **Network effects** (pp. 39 to 40): KSL Classifieds, Google (S18-04).
6. **Pricing strategies** to limit entry or competition (pp. 41 to 48): limit, predatory and penetration pricing.

Other common barriers: **capital requirements** (Reading Quiz Q3 lists it with economies of scale and network effects), **economies of scope**, control of distribution and shelf space. The reading names three barriers that kept newcomers out of soft drinks: **brands, bottling and distribution capabilities, and shelf space**.

**Not a barrier:** buyer price sensitivity (Reading Quiz Q3). That is about demand, not about the extra cost or lower share an entrant faces.

**The razor case (pp. 24 to 25).** Razors earned about 60% gross margins; they were 9% of P&G's sales but 16% of its profits. Gillette spent $200 million marketing ProGlide with FlexBall. Dollar Shave Club entered with a $20,000 low-budget YouTube commercial and sold by subscription online, going around the brand and shelf-space barriers.

**The Meta exercise.** Meta's profit per user beat Twitter's and Snapchat's every year from 2017 to 2021: its revenue advantage reflects network effects, its cost advantage reflects economies of scale, and its head start added learning and first-mover advantages.""",
 "why": "Practice exam Q22, Q23 and Q29, Reading Quiz Q3 and Comprehension Quiz 8 Q1 and Q3 all map here. Expect scenario questions asking which barrier is at work.",
 "definition": "A barrier to entry is any factor that increases the cost borne by potential entrants after they enter the market or decreases the market share potential of entrants upon entering an industry.",
 "formulas": [],
 "derivation": "",
 "math": [PERCENT],
 "worked": [{"title": "Name the barrier", "problem": "Classify: (a) a new airline cannot get landing slots at a busy airport; (b) a new chip maker must spend $20 billion on a plant before selling one chip; (c) a new dating app has no users; (d) a store brand cola cannot get onto grocery shelves.",
   "steps": ["(a) Legal or regulatory barrier (government-controlled access).", "(b) Capital requirements, and economies of scale if the plant only pays off at huge volume.", "(c) Network effects.", "(d) Distribution and shelf space, as in the soft drinks example."],
   "answer": "Legal, capital requirements and scale, network effects, shelf space and distribution."}],
 "graph": {"component": "scale", "params": {"F": 5000, "c": 5, "d": 0.02, "demand": 1500, "C1": 1000, "rate": 0.8, "N": 128, "k": 0.2, "price": 40}, "caption": "Three structural barriers side by side: scale (average cost), learning (cumulative output), and network effects (critical mass)."},
 "traps": ["The definition has TWO parts (higher post-entry cost OR lower share potential); the quiz answer is both.",
           "Buyer price sensitivity is NOT a barrier to entry.",
           "Brand advertising can be a barrier, but the razor case shows it can be bypassed with a cheaper channel.",
           "Match the scenario to the mechanism: cost per unit falls with SIZE (scale), with EXPERIENCE (learning), or value rises with USERS (network)."],
 "sources": {"slides": "S18 Barriers to Entry pp. 24 to 48", "read": "Module Group A Module 1; Strategies to Crack Well-Guarded Markets", "exercise": "Barriers to Entry Exercise", "quiz": "Reading Quiz Q3; Comprehension Quiz 8 Q1, Q3; Practice exam Q22, Q23, Q29"}},

{"id": "S18-10", "title": "Circumventing barriers to entry", "calc": False,
 "plain": r"""The most profitable industries attract about five times as many entrants as the average industry, yet those entrants earn returns about 30% lower than newcomers elsewhere (Bryce and Dyer, Strategies to Crack Well-Guarded Markets, HBR 2007). The few that succeed use **indirect assault**: they avoid the incumbent's strongholds, so incumbents either cannot respond or do not bother.

**Head-on versus indirect:**
- Soft drinks: Virgin Cola attacked Coke and Pepsi directly and never passed 1% of U.S. cola. Red Bull came in with a niche energy drink sold in bars and clubs, then moved into stores once demand pulled it in.
- Video games: Microsoft's Xbox attacked Sony and Nintendo directly and lost about $4.5 billion in five years. Jakks Pacific sold cheap plug-and-play games for kids and casual players and earned about 15% operating margins.

**The three strategies (slides pp. 49 to 50):**
1. **Leverage existing assets**: use what you already have (shelf space, locations, brand, customers, idle capacity), often with a partner's assets, to lower the cost of entry. McDonald's and Redbox kiosks; Toys "R" Us and Babies "R" Us.
2. **Reconfigure the value chain**: change the activities, or their order, that deliver value, often by borrowing a model from another industry or using new technology. Skype, Usana, Netflix.
3. **Create a market niche**: serve a fringe segment that mainstream customers (and so incumbents) do not care about. Red Bull, Skechers.

**Combinations.** Each strategy alone is ordinary; successful entrants combine at least two.
- Reconfigure + niche: the most powerful pair (Skype, Usana).
- Leverage + reconfigure: Walmart and Cott's Sam's Choice soda; Costco Home.
- Leverage + niche: Babies "R" Us; Skechers.
- All three: rare (Jakks Pacific).

**Directly attacking the market leader is NOT one of the strategies** (Reading Quiz Q1). Reading Quiz Q2: Uber used all three (reconfigured the value chain with an app and private drivers, began in a niche of riders poorly served by taxis, leveraged drivers' existing cars). Comprehension Quiz 8 Q4: a company selling cars from a vending machine is primarily **reconfiguring the value chain**.

**Close the door behind you.** Once in, build your own barriers (S18-07).""",
 "why": "Reading Quiz Q1 and Q2, Comprehension Quiz 8 Q4, practice exam Q21 and exercise step 8 (TikTok and Threads) all ask you to name the strategy a company used.",
 "definition": "Firms circumvent barriers to entry by indirect assault: leveraging existing assets, reconfiguring the value chain and creating a market niche, usually in combination, so incumbents cannot or will not respond.",
 "formulas": [],
 "derivation": "",
 "math": [],
 "worked": [{"title": "Classify the entry", "problem": "Netflix first mailed DVDs ordered online instead of renting them in stores, aimed at movie buffs who wanted a big catalog and no late fees. Which strategies?",
   "steps": ["Mailing DVDs ordered from a website instead of running stores changes the activities that deliver value: reconfigure the value chain (the reading names Netflix applying an Amazon-like model to DVD rentals).", "Targeting heavy movie watchers rather than everyone is a niche."],
   "answer": "Reconfigure the value chain plus create a niche, the most powerful pair."}],
 "graph": None,
 "traps": ["Directly attacking the leader is NOT one of the three strategies; head-on entrants (Virgin Cola, Xbox) did badly.",
           "Leveraging assets uses what YOU ALREADY HAVE. Reconfiguring the value chain changes HOW the product is made or delivered. A niche is about WHICH CUSTOMERS you serve.",
           "Successful entrants usually COMBINE at least two strategies.",
           "Acquisitions are not a cheap way in: buyers pay about a 30% premium for the target's future profits."],
 "sources": {"slides": "S18 Barriers to Entry pp. 24 to 26, 49 to 50", "read": "Strategies to Crack Well-Guarded Markets", "exercise": "Barriers to Entry Exercise step 8", "quiz": "Reading Quiz Q1, Q2; Comprehension Quiz 8 Q4; Practice exam Q21"}},
]
for L in LESSONS:
    if L.get("graph") is None: L.pop("graph", None)
    write_lesson(L)
write_session("S18", {"overview": "Session 18 asks why some markets stay profitable and how newcomers break in anyway. A barrier to entry is anything that raises an entrant's costs after it enters or shrinks the share it can win. The structural barriers are economies of scale, learning curves, economies of scope, brand, patents and network effects. Incumbents can also use price: limit pricing keeps potential entrants out, predatory pricing drives an existing rival out, and penetration pricing helps a newcomer reach critical mass. The Bryce and Dyer reading shows how entrants succeed by indirect assault: leverage existing assets, reconfigure the value chain, create a niche, usually in combination. Most of this session is conceptual; the calculations are light (average cost, learning curves, revenue per user)."})
print([L["id"] for L in LESSONS])
