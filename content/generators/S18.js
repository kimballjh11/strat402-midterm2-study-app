// S18 Barriers to Entry generators: average cost and scale, learning curves, per-user results, limit pricing. Same seed, same question.
(function () {
  const fmt = (x, d) => M2.fmt(x, d == null ? 2 : d);
  const money = x => (x < 0 ? "-$" : "$") + fmt(Math.abs(x));

  M2.gen({ id: "S18-01-g1", los: ["S18-01", "S18-09"], kind: "calc", make(r) {
    const F = r.pick([1000, 2000, 5000, 10000, 20000, 50000]), c = r.pick([1, 2, 3, 4, 5, 8, 10]);
    const Qs = r.pick([10, 20, 25, 50]), Qb = Qs * r.pick([4, 5, 10, 20]);
    const ac = Q => F / Q + c, ask = r.pick(["small", "big", "gap"]);
    const ans = ask === "small" ? ac(Qs) : ask === "big" ? ac(Qb) : ac(Qs) - ac(Qb);
    const q = ask === "small" ? `What is the entrant's average cost if it sells ${Qs.toLocaleString("en-US")} units?` :
      ask === "big" ? `What is the incumbent's average cost at ${Qb.toLocaleString("en-US")} units?` :
      `An entrant expects to sell ${Qs.toLocaleString("en-US")} units and the incumbent sells ${Qb.toLocaleString("en-US")}. How much higher is the entrant's average cost per unit?`;
    return { type: "num", unit: "$", answer: ans, params: { F, c, Qs, Qb, ask },
      stem: `Producing in this market takes a fixed cost of $${F.toLocaleString("en-US")} per year plus $${c} per unit. ${q}`,
      explain: `ATC = TC/Q = F/Q + c. At ${Qs.toLocaleString("en-US")} units: ${F}/${Qs} + ${c} = ${money(ac(Qs))}. At ${Qb.toLocaleString("en-US")} units: ${F}/${Qb} + ${c} = ${money(ac(Qb))}.${ask === "gap" ? ` Gap = ${money(ans)}.` : ""} Spreading the fixed cost over more units is economies of scale, and it is why a small entrant is at a disadvantage.` };
  } });

  M2.gen({ id: "S18-02-g1", los: ["S18-02"], kind: "calc", make(r) {
    const rate = r.pick([0.7, 0.75, 0.8, 0.85, 0.9]), C1 = r.pick([100, 200, 400, 500, 800, 1000, 2000]);
    const start = r.pick([1, 1, 10, 50, 100]), k = r.int(1, 5), n = start * 2 ** k;
    const ans = C1 * rate ** k, steps = [];
    for (let i = 0; i <= k; i++) steps.push((start * 2 ** i).toLocaleString("en-US"));
    return { type: "num", unit: "$", answer: ans, params: { C1, rate, k, start },
      stem: `${start === 1 ? "The first unit" : `Unit number ${start}`} of a product cost $${C1}. The firm is on a ${Math.round(rate * 100)}% learning curve. What does unit number ${n.toLocaleString("en-US")} cost?`,
      explain: `Count doublings: ${steps.join(", ")} is ${k} doubling${k > 1 ? "s" : ""}. Each doubling multiplies cost by ${rate}. ${C1} × ${rate}^${k} = ${C1} × ${fmt(rate ** k, 4)} = ${money(ans)}. A ${Math.round(rate * 100)}% curve means cost falls TO ${Math.round(rate * 100)}% per doubling, a ${Math.round((1 - rate) * 100)}% drop.` };
  } });

  M2.gen({ id: "S18-04-g1", los: ["S18-04", "S18-09"], kind: "calc", make(r) {
    const ask = r.pick(["rev", "profit", "conn", "add"]);
    if (ask === "conn" || ask === "add") {
      const n = r.pick([5, 8, 10, 12, 20, 25, 40, 50, 100]);
      const ans = ask === "conn" ? n * (n - 1) : 2 * n;
      return { type: "num", unit: "connections", answer: ans, params: { n, ask },
        stem: ask === "conn" ? `A two-way network has ${n} users. How many potential connections does it have?` : `A two-way network has ${n} users. How many new connections does user number ${n + 1} add?`,
        explain: ask === "conn" ? `n(n - 1) = ${n} × ${n - 1} = ${ans}. Each user can connect to each of the others, counted in both directions.` : `A new user adds 2n = 2 × ${n} = ${ans}. Check: ${n + 1} × ${n} - ${n} × ${n - 1} = ${(n + 1) * n} - ${n * (n - 1)} = ${ans}. Every existing user gains, which is the network effect.` };
    }
    const users = r.pick([200, 250, 300, 400, 500, 800, 1000, 1500, 2000]);
    const revPer = r.pick([2, 3, 4, 5, 6, 8, 10, 12, 15]), costPer = r.pick([3, 4, 5, 6, 7, 9, 10]);
    const rev = revPer * users, cost = costPer * users;
    const ans = ask === "rev" ? revPer : revPer - costPer;
    return { type: "num", unit: "$", answer: ans, params: { users, rev, cost, ask },
      stem: `A social media company has ${users.toLocaleString("en-US")} million daily active users, $${rev.toLocaleString("en-US")} million of advertising revenue and $${cost.toLocaleString("en-US")} million of operating expense this quarter. What is its ${ask === "rev" ? "ad revenue per user" : "profit per user (negative for a loss)"}?`,
      explain: `Ad revenue per user = ${rev.toLocaleString("en-US")} / ${users.toLocaleString("en-US")} = $${revPer}. ${ask === "profit" ? `Operating expense per user = ${cost.toLocaleString("en-US")} / ${users.toLocaleString("en-US")} = $${costPer}. Profit per user = ${revPer} - ${costPer} = ${money(ans)}.` : ""} Millions divided by millions gives dollars per user. In 2022 Q2 Meta earned $14.29 per user, Twitter $4.52 and Snapchat $3.20.` };
  } });

  const TXT = { deter: "Entry is deterred and the incumbent still earns a profit: limit pricing", noDeter: "Entry is not deterred: the price is above the entrant's average cost", loss: "Entry is deterred, but the price is below the incumbent's own cost", mono: "This is the monopoly price; it does not limit entry" };
  M2.gen({ id: "S18-05-g1", los: ["S18-05", "S18-06"], kind: "apply", make(r) {
    const own = r.pick([10, 15, 20, 25]), ent = own + r.pick([8, 10, 12, 15, 20]), PM = ent + r.pick([10, 15, 20, 30]);
    const which = r.pick(["deter", "noDeter", "loss", "deter"]);
    const P = which === "deter" ? r.int(own + 1, ent - 1) : which === "noDeter" ? r.int(ent + 1, PM - 1) : r.int(Math.max(1, own - 8), own - 1);
    const choices = r.shuffle([TXT.deter, TXT.noDeter, TXT.loss]).concat([TXT.mono]);
    return { type: "mc", choices, answer: choices.indexOf(TXT[which]), params: { own, ent, PM, P },
      stem: `An incumbent's monopoly price is $${PM} and its average cost is $${own}. A potential entrant's lowest possible average cost is $${ent}. The incumbent sets a price of $${P}. What happens?`,
      explain: `Compare the price with both costs. $${P} ${P < ent ? "<" : ">"} entrant's $${ent}, so entry ${P < ent ? "is" : "is not"} unprofitable. $${P} ${P > own ? ">" : "<"} incumbent's $${own}, so the incumbent ${P > own ? "still earns a profit" : "loses money on each unit"}. ${which === "deter" ? "Below the monopoly price, above own cost, aimed at a potential entrant: limit pricing." : which === "loss" ? "Pricing below its own cost costs the incumbent money; a below-cost price aimed at an existing rival would be predatory pricing." : "To deter entry the price has to fall below the entrant's average cost."}` };
  } });
})();
