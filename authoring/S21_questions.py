from common import *
B = Bank()

def cournot(a, b, c1, c2):
    q1 = (a - 2 * c1 + c2) / (3 * b); q2 = (a - 2 * c2 + c1) / (3 * b); P = a - b * (q1 + q2)
    return {"q1": q1, "q2": q2, "Q": q1 + q2, "P": P, "pi1": (P - c1) * q1, "pi2": (P - c2) * q2}
def stack(a, b, c1, c2):
    q1 = (a + c2 - 2 * c1) / (2 * b); q2 = (a - c2) / (2 * b) - q1 / 2; P = a - b * (q1 + q2)
    return {"q1": q1, "q2": q2, "Q": q1 + q2, "P": P, "pi1": (P - c1) * q1, "pi2": (P - c2) * q2}
def collude(a, b, c):
    Q = (a - c) / (2 * b); P = a - b * Q
    return {"q1": Q / 2, "Q": Q, "P": P, "pi1": (P - c) * Q / 2}
def br(a, b, c1, q2): return (a - c1) / (2 * b) - q2 / 2

def V(f, a, b, c1, c2, who, **k): return {"f": f, "a": a, "b": b, "c1": c1, "c2": c2, "who": who, **k}
def dem(a, b): return f"P = {fmt(a)} - {fmt(b)}(Q_1 + Q_2)" if b != 1 else f"P = {fmt(a)} - (Q_1 + Q_2)"

# ---------------- S21-01 oligopoly ----------------
lo = "S21-01"
B.mc(lo, [lo], "concept", "What is the key feature that makes a market an oligopoly?", ["Firms' actions are interdependent: each firm's best move depends on rivals' responses", "There are exactly two firms", "Products are identical", "The government sets prices"], 0, "Bryce p. 1: interdependence is the key determinant.")
B.mc(lo, [lo], "concept", "According to the professor's reading, roughly how many firms can an oligopoly have?", ["From two up to maybe 8 to 12, perhaps 15", "Exactly one", "At least 50", "Any number, as long as products are identical"], 0, "Bryce p. 1. Once firms become price takers, it is no longer oligopoly.")
B.mc(lo, [lo], "concept", "An oligopoly with exactly two firms is called a:", ["Duopoly", "Monopoly", "Monopsony", "Cartel"], 0, "Duo = two.")
B.mc(lo, [lo], "concept", "How do oligopolists choose their profit-maximizing output or price?", ["They set MR = MC, but MR depends on rivals' choices", "They set price equal to marginal cost", "They copy the largest firm", "They maximize revenue"], 0, "Bryce p. 3: same rule as other firms, but the optimum depends on rivals.")
B.tf(lo, [lo], "concept", "True or false: In the professor's reading, the reasoning chain 'if I do a, they do b, then I do c...' ends at a Nash equilibrium.", True, "True. Each firm plays its best response and no one wants to deviate (Bryce p. 1).")
B.mc(lo, [lo], "concept", "According to the textbook, if rivals match a firm's price changes, the firm's demand is:", ["Less elastic", "More elastic", "Perfectly elastic", "Unaffected"], 0, "Cut price and you gain few customers because rivals cut too; raise it and you lose few because they raise too.")
B.mc(lo, [lo], "concept", "What does Bryce call the levers oligopolists use to compete, such as price, capacity, lead time and frequent flier programs?", ["Strategic variables", "Reaction functions", "Isoprofit curves", "Sunk costs"], 0, "Bryce p. 3.")
B.tf(lo, [lo, "S20-07"], "concept", "True or false: Bryce argues that oligopolists keying off rivals' behavior without any agreement is a legitimate form of collusion that is hard for regulators to detect.", True, "True (Bryce p. 3).")
B.mc(lo, [lo], "apply", "Which market is most likely an oligopoly?", ["Three national wireless carriers", "Thousands of corn farmers selling at the market price", "A city's only water utility", "Hundreds of nail salons in a large metro area"], 0, "Few firms whose moves affect each other.")
B.mc(lo, [lo], "apply", "In January 2005 Delta cut all fares for an indefinite period. How does Bryce describe this?", ["Abandoning the oligopoly norms of full-fare carriers to compete with discount carriers", "A standard tacitly collusive fare sale", "Explicit price fixing", "A Stackelberg leader move"], 0, "Bryce p. 2: full-fare carriers normally run well-defined, temporary fare sales.")
B.mc(lo, [lo], "apply", "Why did 11 corn wet milling firms in 1972 each have to think about rivals when deciding how much high-fructose corn syrup capacity to build?", ["Too much total capacity would push prices too low for anyone to profit", "The government set each firm's capacity", "They had signed a contract", "Corn syrup had no substitutes"], 0, "Bryce pp. 1 to 2: each estimated the market while accounting for rival actions.")
B.mc(lo, [lo], "apply", "A firm raises its price, and its only rival quickly matches. According to Bryce, how might the rival have interpreted the first price increase?", ["As a collusive signal to be matched", "As an invitation to cut price and take share", "As illegal price fixing", "As a sign of exit"], 0, "Bryce p. 2, though a price hike can also signal higher costs (footnote 2).")
B.mc(lo, [lo], "apply", "Why are disruptive entrants like Amazon in bookselling a problem for established oligopolists, according to Bryce?", ["They ignore industry norms, and incumbents' cost structures may not allow an effective response", "They always collude", "They raise prices", "They are regulated"], 0, "Bryce p. 3.")
B.mc(lo, [lo], "apply", "Monitoring rivals becomes harder and retaliation weaker as:", ["The number of firms increases", "Prices are posted online", "Firms meet more often", "The market shrinks to two firms"], 0, "Bryce p. 3: such industries move toward perfect competition.")
B.mc(lo, [lo], "apply", "A gas station in north Provo and one in south Provo sell the same gasoline. According to Bryce, should they be treated as rivals in one oligopoly?", ["No; at one level they do not really compete directly, since competition happens at local intersections", "Yes; same product means same market", "Yes; all Provo stations are one oligopoly", "No; gasoline is a monopoly"], 0, "Bryce p. 9: it is easy to define markets too broadly.")

# ---------------- S21-02 Cournot ----------------
lo = "S21-02"
B.mc(lo, [lo], "concept", "In a Cournot oligopoly, firms compete by choosing:", ["Quantities, simultaneously", "Prices, simultaneously", "Quantities, one after another", "Advertising budgets"], 0, "Bryce p. 4: set output and let the price float.")
B.mc(lo, [lo], "concept", "What does each Cournot firm believe about its rivals?", ["Rivals will hold their output constant if it changes its output", "Rivals will match price cuts", "Rivals will exit", "Rivals will move first"], 0, "Textbook condition 3.")
B.mc(lo, [lo], "concept", "The Cournot equilibrium is where:", ["The firms' reaction functions intersect", "Price equals marginal cost", "One firm produces the monopoly output", "Isoprofit curves are vertical"], 0, "Neither firm wants to change its output given the other's.")
B.mc(lo, [lo], "concept", "Which markets does Bryce say fit Cournot competition?", ["Commodity markets such as oil and agriculture cooperatives", "Ski resorts", "Online sellers of identical chargers", "Airlines"], 0, "Bryce p. 4.")
B.mc(lo, [lo], "concept", "Compared with monopoly, Cournot duopoly has:", ["More output and a lower price, but price still above MC", "Less output and a higher price", "The same output", "Price equal to MC"], 0, "Between monopoly and perfect competition.")
B.tf(lo, [lo], "concept", "True or false: As the number of Cournot firms grows, the market price falls toward marginal cost.", True, "True (textbook).")
for (a, b, c, src) in [(10, 1, 0, "Textbook Demonstration Problem 9-4"), (1000, 1, 4, "The textbook's comparison market")]:
    r = cournot(a, b, c, c)
    B.num(lo, [lo, "S21-06"], f"{src}: {dem(a, b)}, each firm's marginal cost is ${c}. What is each firm's Cournot output?", round(r["q1"], 4),
          f"Each firm makes (a - c)/(3b) = ({a} - {c})/3 = {fmt(r['q1'])}. Check with r_1: Q_1 = {fmt((a - c) / 2)} - 0.5({fmt(r['q2'])}) = {fmt(r['q1'])}.", V("cournot", a, b, c, c, "q1"))
r = cournot(1000, 1, 4, 4)
B.num(lo, [lo], "Textbook comparison market: P = 1,000 - (Q_1 + Q_2), C = 4Q for each firm. What is the Cournot price?", r["P"], "Q = 332 + 332 = 664; P = 1,000 - 664 = $336.", V("cournot", 1000, 1, 4, 4, "P"), unit="$")
B.num(lo, [lo], "Same market. What is each firm's Cournot profit?", r["pi1"], "(336 - 4) × 332 = $110,224.", V("cournot", 1000, 1, 4, 4, "pi1"), unit="$")
r = cournot(120, 2, 20, 20)
B.num(lo, [lo], "P = 120 - 2(Q_1 + Q_2), MC = $20 for both firms. What is the Cournot price?", round(r["P"], 2), "Each makes 100/6 = 16.67; Q = 33.33; P = 120 - 66.67 = $53.33.", V("cournot", 120, 2, 20, 20, "P"), unit="$")
B.mc(lo, [lo], "calc", "P = 90 - (Q_1 + Q_2), MC = $30 for both. What are the Cournot outputs?", ["20 each", "30 each", "15 each", "22.5 each"], 0, "(90 - 30)/3 = 20 each; P = $50. 30 each is (a - c)/(2b), the monopoly or leader output.")
B.mc(lo, [lo], "apply", "Saudi Arabia and Russia each decide how many barrels to pump this month without knowing the other's plan; the world price adjusts to total supply. Which model fits?", ["Cournot", "Standard Bertrand", "Stackelberg", "Sweezy"], 0, "Quantity, simultaneous, homogeneous.")
B.mc(lo, [lo], "apply", "Two Cournot firms agree to split the monopoly output. What will each want to do?", ["Produce more than its quota", "Produce less than its quota", "Keep exactly its quota", "Cut its price to marginal cost"], 0, "Bryce p. 6: given the rival at the quota, a firm's reaction function calls for more output. OPEC members overproduce.")
B.mc(lo, [lo], "apply", "Why do OPEC members often produce more than their quotas, in Cournot terms?", ["Given others keep their quotas, each member's best response is to produce more", "Quotas are illegal", "Oil demand is perfectly elastic", "OPEC is a Stackelberg leader"], 0, "Textbook Inside Business 9-1 and Bryce p. 6.")

# ---------------- S21-03 Stackelberg ----------------
lo = "S21-03"
B.mc(lo, [lo], "concept", "In a Stackelberg oligopoly:", ["A leader chooses output first, and followers take it as given", "All firms choose prices at once", "All firms choose output at once", "Firms collude on output"], 0, "Textbook conditions 3 and 4.")
B.mc(lo, [lo], "concept", "How does the follower choose its output?", ["With its Cournot reaction function, given the leader's output", "It copies the leader", "It produces the monopoly output", "It sets price equal to MC"], 0, "The follower best-responds to the observed leader output.")
B.mc(lo, [lo], "concept", "Compared with Cournot, the Stackelberg leader:", ["Produces more and earns more", "Produces less and earns less", "Produces the same", "Earns zero profit"], 0, "First-mover advantage.")
B.mc(lo, [lo], "concept", "Compared with Cournot, total output in Stackelberg is:", ["Higher, so price is lower", "Lower, so price is higher", "The same", "Zero"], 0, "Textbook comparison: 747 vs 664.")
B.mc(lo, [lo], "concept", "Bryce describes Stackelberg competition as:", ["A race to build capacity in which one firm clearly makes its choice first", "Competition in prices for identical goods", "A cartel", "Competition in advertising"], 0, "Bryce p. 8, competition in lead time.")
B.tf(lo, [lo], "concept", "True or false: With identical costs, the Stackelberg leader produces the same output a monopolist would.", True, "True: (a - c)/(2b). The follower makes half of that.")
r = stack(50, 1, 2, 2)
B.num(lo, [lo, "S21-06"], "Textbook Demonstration Problem 9-6: P = 50 - (Q_1 + Q_2), C_1 = 2Q_1, C_2 = 2Q_2, firm 1 leads. What is the leader's output?", r["q1"],
      "Q_1 = (a + c_2 - 2c_1)/(2b) = (50 + 2 - 4)/2 = 24.", V("stack", 50, 1, 2, 2, "q1"))
B.num(lo, [lo, "S21-06"], "Same problem. What is the follower's output?", r["q2"], "Q_2 = 24 - 0.5(24) = 12.", V("stack", 50, 1, 2, 2, "q2"))
B.num(lo, [lo], "Same problem. What is the market price?", r["P"], "P = 50 - (24 + 12) = $14.", V("stack", 50, 1, 2, 2, "P"), unit="$")
r = stack(1000, 1, 4, 4)
B.num(lo, [lo], "Textbook comparison market (P = 1,000 - Q, MC = 4), firm 1 leads. What is the follower's profit?", r["pi2"], "Leader 498, follower 249, P = $253. Follower profit (253 - 4) × 249 = $62,001.", V("stack", 1000, 1, 4, 4, "pi2"), unit="$")
B.mc(lo, [lo], "calc", "P = 90 - (Q_1 + Q_2), MC = $30 for both, firm 1 leads. What are the outputs?", ["Leader 30, follower 15", "20 each", "Leader 15, follower 30", "Leader 30, follower 30"], 0, "Leader (90 - 30)/2 = 30; follower 30 - 0.5(30) = 15; P = $45.")
B.mc(lo, [lo], "apply", "Which situation best fits Stackelberg?", ["A chipmaker finishes a huge fab before its rival decides how big to build", "Two gas stations post prices at the same time", "Four oil producers pump without seeing each other's plans", "Coke and Pepsi set prices for differentiated colas"], 0, "Quantity commitment made first and observed.")
B.mc(lo, [lo], "apply", "In the textbook's generative AI example, why did OpenAI, Google and Microsoft rush products out early and in high volume?", ["To gain a Stackelberg first-mover advantage that crowds out rivals", "To collude", "Because prices equal MC", "To avoid reaction functions"], 0, "Inside Business 9-2.")
B.mc(lo, [lo], "apply", "A would-be leader announces it 'plans' a big plant but has not started building. The rival builds first. What happens?", ["The announcement is not a commitment, so it gets no leader advantage", "It is still the Stackelberg leader", "Both earn monopoly profit", "The rival must exit"], 0, "Leadership requires a real, observed commitment.")

# ---------------- S21-04 reaction function ----------------
lo = "S21-04"
B.mc(lo, [lo], "concept", "A reaction function shows:", ["A firm's profit-maximizing choice for every possible choice of its rival", "Total industry profit", "The market demand curve", "The equilibrium price only"], 0, "Bryce p. 3: the complete set of best responses.")
B.mc(lo, [lo], "concept", "Why do Cournot reaction functions slope downward?", ["More rival output lowers price and your MR, so your best output falls", "More rival output raises price", "Costs rise with rival output", "They slope upward"], 0, "Bryce p. 5.")
B.mc(lo, [lo], "concept", "If firm 2 produces zero, firm 1's reaction function says produce:", ["The monopoly output", "Zero", "The Cournot output", "The competitive output"], 0, "Where R1 hits the Q1 axis (Bryce p. 5).")
B.mc(lo, [lo], "concept", "If firm 2's marginal cost falls, what happens in Cournot?", ["Firm 2's reaction function shifts out: firm 2 produces more and firm 1 less", "Firm 1's reaction function shifts out", "Nothing changes", "Both produce less"], 0, "Textbook Figure 9-8.")
B.mc(lo, [lo], "concept", "In differentiated Bertrand (price competition), reaction functions:", ["Slope upward", "Slope downward", "Are vertical", "Do not exist"], 0, "A rival's higher price lets you charge more (Bryce p. 8).")
B.tf(lo, [lo], "concept", "True or false: Isoprofit curves for firm 1 peak where they cross firm 1's reaction function.", True, "True (textbook property 3).")
for (a, b, c, q2) in [(120, 2, 20, 20), (10, 1, 0, 4), (1000, 1, 4, 300)]:
    ans = br(a, b, c, q2)
    B.num(lo, [lo, "S21-06"], f"{dem(a, b)}, firm 1's marginal cost is ${c}. If firm 2 produces {q2}, what is firm 1's profit-maximizing output?", ans,
          f"MR_1 = {a} - {fmt(b)}Q_2 - {fmt(2 * b)}Q_1 = {c}, so Q_1 = {fmt((a - c) / (2 * b))} - 0.5Q_2 = {fmt((a - c) / (2 * b))} - {fmt(q2 / 2)} = {fmt(ans)}.", V("br", a, b, c, c, "q1", q2=q2))
B.num(lo, [lo], "Bryce footnote 6: P = a - q_1 - q_2. With a = 100, c = 10 and q_2 = 30, what is firm 1's best output q_1* = (a - q_2 - c)/2?", 30,
      "(100 - 30 - 10)/2 = 30.", V("br", 100, 1, 10, 10, "q1", q2=30))
B.mc(lo, [lo], "calc", "P = 10 - (Q_1 + Q_2), MC = 2 for both. Firm 2's MC falls to 0. What is the new Cournot equilibrium?", ["Q_1 = 2, Q_2 = 4", "Q_1 = 8/3, Q_2 = 8/3", "Q_1 = 4, Q_2 = 2", "Q_1 = 3, Q_2 = 3"], 0,
     "Q_1 = (10 - 4 + 0)/3 = 2; Q_2 = (10 - 0 + 2)/3 = 4 (textbook Figure 9-8).")
B.mc(lo, [lo], "apply", "Your reaction function is Q_1 = 25 - 0.5Q_2. Your rival expands output by 10 units. What should you do?", ["Cut output by 5 units", "Raise output by 10", "Cut output by 10", "Keep output the same"], 0, "Slope -1/2.")
B.mc(lo, [lo], "apply", "In Bryce's adjustment story, firm 1 starts at its monopoly output and firms take turns best-responding. Where does it end?", ["Where the reaction functions intersect (Cournot-Nash equilibrium)", "At the monopoly point", "At zero output", "At price equal to MC"], 0, "Bryce p. 6, point e.")

B.mc(lo, [lo], "apply", "A rival invests in automation that cuts its marginal cost. In a Cournot market, how should you expect your own best output to change?", ["It falls, because the rival's reaction function shifts out and it produces more", "It rises", "It stays the same", "It falls to zero"], 0, "Textbook Figure 9-8 logic from the other side.")

# ---------------- S21-05 identify conditions ----------------
lo = "S21-05"
B.mc(lo, [lo], "concept", "In Bryce's Figure 1, homogeneous goods with competition in quantity is called:", ["Cournot", "Bertrand", "Stackelberg", "Differentiated Bertrand"], 0, "Bryce p. 4.")
B.mc(lo, [lo], "concept", "In Bryce's Figure 1, homogeneous goods with competition in lead time is called:", ["Stackelberg", "Cournot", "Bertrand", "Sweezy"], 0, "Bryce p. 4.")
B.mc(lo, [lo], "concept", "Which condition separates Stackelberg from Cournot?", ["One firm chooses its output before the others", "Products are differentiated", "There are barriers to entry", "Firms set prices"], 0, "Cournot: simultaneous. Stackelberg: leader first.")
B.mc(lo, [lo], "concept", "Which is NOT a textbook condition for Cournot oligopoly?", ["Firms set prices and buyers see all prices", "Few firms serving many consumers", "Each firm believes rivals hold output constant", "Barriers to entry"], 0, "That describes Bertrand.")
B.mc(lo, [lo], "concept", "Which of Bryce's three questions identifies the type of competition (Cournot, Bertrand, and so on)?", ["What is the primary strategic variable?", "How many firms are in the market?", "How much do target customers overlap?", "What is the interest rate?"], 0, "Bryce p. 10, question 3. The first two help define the market.")
B.tf(lo, [lo], "concept", "True or false: In the textbook's conditions, Cournot can apply to homogeneous or differentiated products.", True, "True. Bryce's figure places the classic case under homogeneous goods.")
B.mc(lo, [lo], "concept", "The Sweezy model (optional in the reading) assumes each firm believes rivals will:", ["Match price cuts but not price increases", "Match price increases but not cuts", "Hold output constant", "Move first"], 0, "Gives a kinked demand curve and sticky prices.")
B.mc(lo, [lo], "apply", "Large agricultural cooperatives each decide how much produce to release for sale this season. Which model fits, according to Bryce?", ["Cournot", "Bertrand", "Stackelberg", "Differentiated Bertrand"], 0, "Bryce p. 4: a Cournot overlay on agriculture.")
B.mc(lo, [lo], "apply", "Two firms race to build capacity in a new market, and everyone knows Firm A will finish its plant first. Which model fits?", ["Stackelberg", "Cournot", "Standard Bertrand", "Perfect competition"], 0, "Bryce p. 8.")
B.mc(lo, [lo], "apply", "Ski resorts near Salt Lake City compete mainly on lift ticket prices for somewhat different mountains. Which model fits?", ["Differentiated Bertrand", "Cournot", "Stackelberg", "Standard Bertrand"], 0, "Bryce p. 10: price competition, differentiated products.")
B.mc(lo, [lo], "apply", "Four steel mills each choose this quarter's production, then the market price adjusts. Which model fits?", ["Cournot", "Stackelberg", "Bertrand", "Monopoly"], 0, "Simultaneous quantity choice.")
B.mc(lo, [lo], "apply", "An established cement producer has already built a large kiln. A newcomer sees it and then decides how big a kiln to build. Which model fits?", ["Stackelberg, with the established producer as leader", "Cournot", "Standard Bertrand", "Differentiated Bertrand"], 0, "Observed capacity commitment first.")
B.mc(lo, [lo], "apply", "Airlines compete mainly on fares but also use frequent flier programs and route differences. What does Bryce conclude?", ["Differentiated Bertrand", "Cournot", "Stackelberg", "Perfect competition"], 0, "Bryce p. 10.")
B.mc(lo, [lo], "apply", "Gas station prices barely change after a small drop in wholesale costs, and stations believe rivals match price cuts but not increases. Which model best explains the sticky prices?", ["Sweezy", "Cournot", "Stackelberg", "Standard Bertrand"], 0, "The MR gap at the kink (textbook headline). Sticky prices are not proof of collusion.")
B.mc(lo, [lo], "apply", "To decide whether two firms are in the same oligopoly, Bryce suggests asking:", ["What percentage of their target customers overlap", "Whether they have the same CEO", "Whether they use the same accountant", "Whether their prices are equal"], 0, "Bryce p. 10, question 2.")

# ---------------- S21-06 optimal decisions ----------------
lo = "S21-06"
B.mc(lo, [lo], "concept", "Two Cournot firms collude. What output does each produce?", ["Half the monopoly output", "The Cournot output", "Half the competitive output", "The Stackelberg leader output"], 0, "Bryce p. 6, point m.")
B.mc(lo, [lo], "concept", "In a one-shot game, why does a Cournot cartel break down?", ["Each firm's best response to the rival's quota is to produce more", "Collusion lowers profits", "The leader moves first", "Price equals MC"], 0, "Cheating pays.")
B.mc(lo, [lo], "concept", "Ranking total output from lowest to highest for the same market:", ["Collusion, Cournot, Stackelberg, Bertrand", "Bertrand, Stackelberg, Cournot, Collusion", "Cournot, Collusion, Bertrand, Stackelberg", "Stackelberg, Cournot, Collusion, Bertrand"], 0, "Textbook comparison: 498, 664, 747, 996.")
B.mc(lo, [lo], "concept", "Which firm earns the least among collusion, Cournot and Stackelberg (in the textbook's comparison)?", ["The Stackelberg follower", "The Stackelberg leader", "A Cournot firm", "A colluding firm"], 0, "$62,001 vs $110,224 and $124,002.")
B.mc(lo, [lo], "concept", "Your marginal cost falls in a Cournot duopoly. How does your rival respond?", ["It produces less", "It produces more", "It exits", "It keeps output unchanged"], 0, "Your reaction function shifts out; the new intersection has you higher and the rival lower.")
r = collude(120, 2, 20)
B.num(lo, [lo, "S21-02"], "P = 120 - 2(Q_1 + Q_2), MC = $20 for both. If the firms collude and split the monopoly output, what is each firm's profit?", r["pi1"],
      "MR = 120 - 4Q = 20 gives Q = 25, P = $70. Each makes 12.5 and earns (70 - 20) × 12.5 = $625.", V("collude", 120, 2, 20, 20, "pi1"), unit="$")
q1 = br(120, 2, 20, 12.5); P = 120 - 2 * (q1 + 12.5)
B.num(lo, [lo, "S21-04"], "Same market. Firm 2 keeps its collusive quota of 12.5. If firm 1 cheats with its best response, what is firm 1's profit?", round((P - 20) * q1, 2),
      f"Q_1 = 25 - 0.5(12.5) = 18.75. Q = 31.25, P = 120 - 62.5 = $57.50. Profit = 37.5 × 18.75 = $703.13 > $625.", V("cheat", 120, 2, 20, 20, "pi1", quota=12.5), unit="$")
r = cournot(100, 1, 10, 25)
B.num(lo, [lo, "S21-02"], "P = 100 - (Q_1 + Q_2), MC_1 = $10, MC_2 = $25. What is firm 1's Cournot output?", r["q1"], "Q_1 = (100 - 20 + 25)/3 = 35.", V("cournot", 100, 1, 10, 25, "q1"))
B.num(lo, [lo, "S21-02"], "Same market. What is the Cournot price?", r["P"], "Q_2 = (100 - 50 + 10)/3 = 20. P = 100 - 55 = $45.", V("cournot", 100, 1, 10, 25, "P"), unit="$")
r = collude(1000, 1, 4)
B.num(lo, [lo], "Textbook comparison market (P = 1,000 - Q, MC = 4). Under collusion, what is the price?", r["P"], "MR = 1,000 - 2Q = 4 gives Q = 498; P = $502; 249 each.", V("collude", 1000, 1, 4, 4, "P"), unit="$")
r = stack(200, 2, 20, 20)
B.num(lo, [lo, "S21-03"], "P = 200 - 2(Q_1 + Q_2), MC = $20 for both, firm 1 leads. What is the leader's profit?", r["pi1"], "Leader (200 - 20)/4 = 45; follower 45 - 22.5 = 22.5; P = 200 - 135 = $65; leader profit 45 × 45 = $2,025.", V("stack", 200, 2, 20, 20, "pi1"), unit="$")
B.mc(lo, [lo], "apply", "You are a Cournot duopolist. Your rival just announced a big expansion that it will definitely carry out. What should you do?", ["Reduce your output along your reaction function", "Increase your output by the same amount", "Cut price to marginal cost", "Nothing"], 0, "Reaction functions slope down.")
B.mc(lo, [lo], "apply", "Two firms in a Cournot market are deciding whether to sign a (legal) joint venture that makes one of them the clear first mover on capacity. Which firm benefits?", ["The firm that becomes the leader; the follower earns less than in Cournot", "Both benefit equally", "Neither; profits are the same", "Only the follower"], 0, "Leader earns more, follower less.")
B.mc(lo, [lo], "apply", "You and one rival split a cartel quota. You learn the rival will secretly produce its best response to your quota next month. What is your best move?", ["Expand output along your reaction function; the outcome moves toward Cournot", "Keep your quota", "Cut output", "Raise your price above the cartel price"], 0, "Bryce p. 6: if the other defects, you best-respond too.")

if __name__ == "__main__": print(B.write())
