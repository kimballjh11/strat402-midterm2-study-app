from common import *
from S21_questions import cournot, stack, collude
B = Bank()

def dbr(al, be, ga, c, pj): return (al + be * c + ga * pj) / (2 * be)
def deq(al, be, ga, c): return (al + be * c) / (2 * be - ga)
def DV(al, be, ga, c, who, **k): return {"f": "dbert", "al": al, "be": be, "ga": ga, "c": c, "who": who, **k}
def bert(A, k, c1, c2):
    """Standard Bertrand with market demand Q = A - kP. Low-cost firm 1 prices at min(c2, its monopoly price)."""
    pm = (A / k + c1) / 2; p = c1 if c1 == c2 else min(c2, pm); Q = A - k * p
    return {"P": p, "Q": Q, "pi1": 0 if c1 == c2 else (p - c1) * Q}

# ---------------- S22-01 standard Bertrand ----------------
lo = "S22-01"
B.mc(lo, [lo], "concept", "Standard Bertrand oligopoly is competition in:", ["Price among sellers of homogeneous goods", "Quantity among sellers of homogeneous goods", "Lead time", "Price among sellers of differentiated goods"], 0, "Bryce p. 6.")
B.mc(lo, [lo], "concept", "In standard Bertrand with identical marginal costs, the equilibrium price is:", ["Equal to marginal cost", "The monopoly price", "Halfway between MC and the monopoly price", "Above average total cost"], 0, "Bryce p. 7: P1 = P2 = MC1 = MC2.")
B.mc(lo, [lo], "concept", "Why does undercutting continue until price reaches marginal cost?", ["Pricing slightly below the rival takes the whole market instead of half", "Costs fall as price falls", "The government requires it", "Consumers prefer higher prices"], 0, "Bryce p. 7: the race to the bottom.")
B.mc(lo, [lo], "concept", "With unequal costs and identical goods, the low-cost firm prices:", ["Just below the high-cost firm's marginal cost", "At its own marginal cost", "At the monopoly price always", "Above the rival's price"], 0, "Bryce p. 7: it maximizes profit per unit while taking the whole market.")
B.mc(lo, [lo], "concept", "How can capacity constraints change the standard Bertrand outcome?", ["Undercutting is pointless if you cannot serve the extra customers, so prices above MC may be sustainable", "They force price below MC", "They have no effect", "They make the market Cournot"], 0, "Bryce p. 7.")
B.tf(lo, [lo], "concept", "True or false: In standard Bertrand, two firms are enough to reach the perfectly competitive price.", True, "True. The textbook calls this the Bertrand trap.")
B.mc(lo, [lo], "concept", "Which is NOT a condition for a contestable market (textbook)?", ["Large sunk costs of entry", "All producers have the same technology", "Consumers respond quickly to price changes", "Incumbents cannot quickly cut price after entry"], 0, "Contestable markets need NO sunk costs.")
B.mc(lo, [lo], "apply", "According to Bryce, why are Bertrand markets more common today?", ["The Internet lets consumers see most prices, making many markets commodity-like", "Products are more differentiated", "There are fewer firms", "Switching costs are higher"], 0, "Bryce p. 6.")
B.mc(lo, [lo], "apply", "On a price comparison site, the textbook reports the gap between the two lowest prices was about 22% with two sellers and under 3% with more than 20. What does this show?", ["Real markets behave more like Bertrand as sellers are added", "Prices rise with more sellers", "Bertrand theory is exactly right with two sellers", "Online markets are monopolies"], 0, "Inside Business 9-3.")
B.mc(lo, [lo], "apply", "Why do Kellogg's and General Mills spend heavily on advertising corn flakes, according to the textbook?", ["To make consumers see the products as different and escape pricing at marginal cost", "To raise switching costs to zero", "To create a Cournot market", "To signal low prices"], 0, "Eliminating the perception of identical products escapes the Bertrand trap.")
B.mc(lo, [lo], "apply", "A firm can buy a truck for $100,000 and resell it for $80,000 if it exits. How does this sunk cost affect entry?", ["The $20,000 that cannot be recovered can deter entry if incumbents would cut prices", "It makes the market contestable", "It has no effect", "It lowers marginal cost"], 0, "Textbook sunk-cost example.")
r = bert(1000, 10, 20, 30)
B.num(lo, [lo, "S22-04"], "Two sellers of an identical part face market demand Q = 1,000 - 10P. Firm 1's MC is $20, firm 2's is $30. Consumers see all prices. About how much profit does firm 1 earn? (Treat 'just below $30' as $30.)", r["pi1"],
      "Firm 1 prices just under $30 and sells Q = 1,000 - 300 = 700. Profit ≈ (30 - 20) × 700 = $7,000. Its monopoly price (60) is higher, so $30 is the binding price.", {"f": "bert", "A": 1000, "k": 10, "c1": 20, "c2": 30, "who": "pi1"}, unit="$")
r = bert(500, 5, 15, 15)
B.num(lo, [lo], "Two identical sellers with marginal cost $15 face market demand Q = 500 - 5P and compete in price. What is the equilibrium price?", r["P"], "Equal costs: P = MC = $15.", {"f": "bert", "A": 500, "k": 5, "c1": 15, "c2": 15, "who": "P"}, unit="$")
B.num(lo, [lo], "Same market (Q = 500 - 5P, both MC = $15). How many units does each firm sell?", r["Q"] / 2, "Q = 500 - 75 = 425, split evenly: 212.5 each. Profit is zero.", {"f": "bert_half", "A": 500, "k": 5, "c1": 15, "c2": 15})
B.num(lo, [lo], "Textbook sunk-cost example: an entrant would lose $2,000 a month for six months while waiting for customers to switch. How much is sunk?", 12000, "2,000 × 6 = $12,000.", {"f": "mult", "x": 2000, "y": 6}, unit="$")
B.mc(lo, [lo], "calc", "Textbook lab experiment: MC = $2, monopoly price $100. With two sellers, theory predicts $2 but winning prices averaged about $27. With three or four sellers they averaged about $9. What does this show?", ["Prices fall quickly toward MC as sellers are added, though not as sharply as theory predicts", "Theory is exactly right", "More sellers raise prices", "Bertrand never applies"], 0, "Dufwenberg and Gneezy, textbook Inside Business 9-3.")

# ---------------- S22-02 differentiated Bertrand ----------------
lo = "S22-02"
B.mc(lo, [lo], "concept", "Differentiated Bertrand is competition in:", ["Price among sellers of moderately differentiated goods", "Quantity among sellers of identical goods", "Lead time", "Price among sellers of identical goods"], 0, "Bryce p. 8.")
B.mc(lo, [lo], "concept", "According to Bryce, which is the most common type of oligopoly today?", ["Differentiated Bertrand", "Cournot", "Standard Bertrand", "Stackelberg"], 0, "Bryce p. 8.")
B.mc(lo, [lo], "concept", "Price reaction functions in differentiated Bertrand slope:", ["Upward: a higher rival price raises your best price", "Downward", "Vertically", "They are flat"], 0, "Prices are strategic complements.")
B.mc(lo, [lo], "concept", "Why can firms in differentiated Bertrand keep prices above marginal cost without colluding?", ["Loyal customers keep buying even when a rival is cheaper", "Prices are regulated", "They choose quantities", "They collude explicitly"], 0, "Bryce p. 8: the Coke drinker who pays 10 cents beside a free Pepsi.")
B.mc(lo, [lo], "concept", "If prices somehow start above the differentiated Bertrand equilibrium, what happens?", ["They fall, but only to the equilibrium, not to marginal cost", "They fall to marginal cost", "They keep rising", "Nothing"], 0, "Bryce p. 9.")
B.tf(lo, [lo], "concept", "True or false: Even if its rival gives its product away, a differentiated Bertrand firm can charge a positive price.", True, "True: p min > 0 (Bryce p. 8).")
B.mc(lo, [lo], "concept", "How does the textbook compare differentiated Bertrand with monopolistic competition?", ["Both price above MC, but barriers to entry let Bertrand oligopolists keep profits in the long run", "They are identical", "Bertrand firms earn zero profit", "Monopolistic competition has upward reaction functions"], 0, "Textbook appendix.")
for (a, c) in [(60, 10), (80, 20), (100, 0)]:
    B.num(lo, [lo, "S22-04"], f"Bryce's demand: Q_i = {a} - p_i + p_j for each firm, marginal cost ${c}. What is the equilibrium price?", a + c,
          f"Reaction: p_i = ({a} + p_j + {c})/2. Symmetric: p = ({a + c} + p)/2, so p = a + c = ${a + c}.", DV(a, 1, 1, c, "p"), unit="$")
B.num(lo, [lo], "Bryce's demand Q_i = 60 - p_i + p_j, MC = $10. What is each firm's profit in equilibrium?", (70 - 10) * 60, "p = $70; Q = 60 - 70 + 70 = 60; profit = 60 × 60 = $3,600.", DV(60, 1, 1, 10, "pi"), unit="$")
B.num(lo, [lo], "q_1 = 100 - 2p_1 + p_2 (symmetric for firm 2), MC = $10. What is the equilibrium price?", deq(100, 2, 1, 10), "p_1 = (100 + 20 + p_2)/4 = 30 + 0.25p_2. Symmetric: 0.75p = 30, p = $40.", DV(100, 2, 1, 10, "p"), unit="$")
B.mc(lo, [lo], "apply", "Which market best fits differentiated Bertrand?", ["Ski resorts near Salt Lake City", "Two online sellers of the same USB cable", "Oil producers setting output", "A city water utility"], 0, "Price competition with differentiated products (Bryce p. 10).")
B.mc(lo, [lo], "apply", "Pepsi raises its price. In differentiated Bertrand, what should Coke do?", ["Raise its price, by less than Pepsi did", "Cut its price", "Keep its price", "Raise its price by more than Pepsi"], 0, "Upward-sloping reaction function with slope below 1.")
B.mc(lo, [lo], "apply", "A desktop computer maker builds a strong brand following. How does this affect its pricing in a differentiated Bertrand market?", ["It can charge a higher price, since fewer customers switch when rivals are cheaper", "It must price at MC", "It must cut price", "It becomes a Cournot firm"], 0, "More differentiation, more pricing power.")

# ---------------- S22-03 identify conditions ----------------
lo = "S22-03"
B.mc(lo, [lo], "concept", "Bryce's first question for determining market structure is:", ["How many firms are meaningfully engaged in direct competition?", "What is the interest rate?", "Who moved first?", "What is the HHI?"], 0, "Bryce p. 9.")
B.mc(lo, [lo], "concept", "Bryce's second question asks:", ["What percentage of the firms' target customer base overlaps?", "What is each firm's marginal cost?", "How old is the industry?", "Are prices regulated?"], 0, "Bryce p. 10.")
B.mc(lo, [lo], "concept", "Bryce's third question, which identifies the type of competition, asks:", ["What is the primary strategic variable?", "How many firms are there?", "What is the market's growth rate?", "Who is the leader?"], 0, "Bryce p. 10: price, programs, features, lead time, or quantity.")
B.mc(lo, [lo], "concept", "Which combination identifies standard Bertrand?", ["Price competition, homogeneous goods, buyers see all prices", "Quantity competition, homogeneous goods", "Price competition, differentiated goods", "One firm commits output first"], 0, "Bryce's Figure 1.")
B.mc(lo, [lo], "concept", "Which combination identifies differentiated Bertrand?", ["Price competition with moderately differentiated goods", "Quantity competition with identical goods", "Lead time competition", "Perfect competition"], 0, "Bryce's Figure 1.")
B.tf(lo, [lo], "concept", "True or false: Defining a market too broadly (for example, all gas stations in a large city) can hide the real oligopoly at local intersections.", True, "True (Bryce p. 9).")
B.mc(lo, [lo], "apply", "Airlines compete mainly on fares but also differ in routes, schedules and frequent flier programs. Which model does Bryce conclude fits?", ["Differentiated Bertrand", "Standard Bertrand", "Cournot", "Stackelberg"], 0, "Bryce p. 10.")
B.mc(lo, [lo], "apply", "Several online sellers list the identical model of a graphics card on a price comparison site; buyers sort by price and there are no switching costs. Which model fits?", ["Standard Bertrand", "Differentiated Bertrand", "Cournot", "Stackelberg"], 0, "Identical goods, fully visible prices.")
B.mc(lo, [lo], "apply", "Cell phone carriers compete on national networks. What does Bryce say about their market?", ["It is national in scale: an oligopoly", "It is local to each intersection", "It is perfectly competitive", "It is a monopoly"], 0, "Bryce p. 9.")
B.mc(lo, [lo], "apply", "Salt Lake ski resorts and high-end Colorado resorts both attract East Coast vacation skiers. What does this suggest?", ["At one level they may be in an oligopoly together because their target customers overlap", "They never compete", "They are in standard Bertrand", "They are a cartel"], 0, "Bryce p. 10, question 2.")
B.mc(lo, [lo], "apply", "Coke and Pepsi compete mainly through prices and promotions, and each has loyal drinkers. Which model fits?", ["Differentiated Bertrand", "Standard Bertrand", "Cournot", "Stackelberg"], 0, "Bryce lists cola as an example.")
B.mc(lo, [lo], "apply", "Two wheat cooperatives each decide how much grain to release, and the market price adjusts. Which model fits?", ["Cournot", "Standard Bertrand", "Differentiated Bertrand", "Stackelberg"], 0, "Quantity is the strategic variable.")
B.mc(lo, [lo], "apply", "Two gas stations face each other at the same intersection, sell the same fuel and post prices on big signs. Which model is the best starting point?", ["Standard Bertrand", "Cournot", "Stackelberg", "Monopoly"], 0, "Identical good, visible prices, price competition at a local intersection.")
B.mc(lo, [lo], "apply", "Which observation would make you doubt that a price-competitive market is standard Bertrand?", ["Firms keep prices well above cost and customers stay loyal when a rival is cheaper", "Prices equal marginal cost", "Buyers compare all prices online", "Products are identical"], 0, "That points to differentiation (or capacity limits).")
B.mc(lo, [lo], "apply", "Car makers compete on price, features and brand. Which model does Bryce list them under?", ["Differentiated Bertrand", "Standard Bertrand", "Cournot", "Stackelberg"], 0, "Bryce p. 8.")

# ---------------- S22-04 optimal decisions ----------------
lo = "S22-04"
B.mc(lo, [lo], "concept", "In Bryce's differentiated Bertrand model, if your rival raises its price by $10, your best price rises by:", ["$5", "$10", "$20", "$0"], 0, "p_i = (a + p_j + c)/2: slope one half.")
B.mc(lo, [lo], "concept", "Ranking price from highest to lowest in the textbook comparison:", ["Collusion, Cournot, Stackelberg, Bertrand", "Bertrand, Stackelberg, Cournot, Collusion", "Cournot, Collusion, Stackelberg, Bertrand", "Stackelberg, Cournot, Bertrand, Collusion"], 0, "$502, $336, $253, $4.")
B.mc(lo, [lo], "concept", "In standard Bertrand with equal costs, what happens if one firm raises its price above marginal cost?", ["It loses all its sales to the rival", "It earns more profit", "The rival follows", "Nothing"], 0, "Bryce p. 7: raising price from MC is very costly.")
B.mc(lo, [lo], "concept", "Your marginal cost rises in a differentiated Bertrand market. How does your rival respond?", ["It raises its price somewhat", "It cuts its price", "It keeps its price", "It exits"], 0, "Your price rises; the rival's reaction function slopes up.")
B.tf(lo, [lo], "concept", "True or false: In the textbook's comparison, Bertrand firms earn the least profit of all four models.", True, "True: zero.")
for (a, c, pj) in [(80, 20, 100), (80, 20, 120), (60, 10, 0)]:
    B.num(lo, [lo, "S22-02"], f"Bryce's demand Q_i = {a} - p_i + p_j, your marginal cost is ${c}. Your rival charges ${pj}. What price maximizes your profit?", (a + pj + c) / 2,
          f"p_i = (a + p_j + c)/2 = ({a} + {pj} + {c})/2 = ${fmt((a + pj + c) / 2)}.", DV(a, 1, 1, c, "br", pj=pj), unit="$")
B.num(lo, [lo, "S22-02"], "q_1 = 100 - 2p_1 + p_2, MC = $10. Your rival charges $60. What is your best price?", dbr(100, 2, 1, 10, 60), "p_1 = (100 + 2(10) + 60)/4 = 180/4 = $45.", DV(100, 2, 1, 10, "br", pj=60), unit="$")
r = cournot(1000, 1, 4, 4)
B.num(lo, [lo, "S21-06"], "Textbook comparison market (P = 1,000 - Q, MC = $4). How much higher is the Cournot price than the Bertrand price?", r["P"] - 4, "Cournot $336, Bertrand $4: difference $332.", {"f": "cournot_minus_mc", "a": 1000, "b": 1, "c": 4}, unit="$")
B.mc(lo, [lo], "apply", "You sell an identical product to a rival with the same costs, and buyers compare prices online. What can you do to earn positive profit?", ["Differentiate your product or add switching costs", "Raise your price", "Match the rival's price above cost", "Produce more"], 0, "The textbook's escapes from the Bertrand trap.")
B.mc(lo, [lo], "apply", "Your cost is $20, your rival's is $30, the goods are identical and buyers see both prices. What price should you set?", ["Just under $30", "$20", "$25", "Your monopoly price, whatever it is"], 0, "Bryce p. 7 (if your monopoly price is above $30).")
B.mc(lo, [lo], "apply", "A ski resort's rival cuts its season pass price by $100. In differentiated Bertrand, what is the resort's best response?", ["Cut its price too, but by less than $100", "Cut by more than $100", "Raise its price", "Ignore it"], 0, "Upward reaction function with slope below 1.")

if __name__ == "__main__": print(B.write())
