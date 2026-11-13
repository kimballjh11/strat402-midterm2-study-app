// Barriers to entry graphs. view: "ac" (economies of scale and minimum efficient scale), "learning" (learning curve),
// "network" (network effects and critical mass). No view given: all three.
// params: {view, F, c, d, demand, C1, rate, k, price, N}
(function (M2) {
  const G = M2.G, C = G.C;

  function ac(holder, pr) {
    const v = G.controls(holder, [
      { key: "F", label: "Fixed cost F", min: 100, max: 20000, step: 100, value: pr.F },
      { key: "c", label: "Unit cost c", min: 0, max: 50, step: 0.5, value: pr.c },
      { key: "d", label: "Rising cost d", min: 0.001, max: 0.5, step: 0.001, value: pr.d },
      { key: "demand", label: "Market Q", min: 50, max: 5000, step: 10, value: pr.demand }], draw);
    const P = G.plot(holder, { h: 300, xlabel: "Output Q", ylabel: "Average cost", title: "Economies of scale and minimum efficient scale" });
    const out = G.readout(holder);
    function draw() {
      const AC = Q => v.F / Q + v.c + v.d * Q, mes = Math.sqrt(v.F / v.d), acMin = AC(mes);
      const xmax = Math.max(mes * 2.5, v.demand * 1.1);
      P.clear(xmax, AC(mes * 0.25) * 1.1, 0);
      P.band(0, mes, C.c, "economies of scale"); P.band(mes, xmax, C.d, "diseconomies");
      P.fn(AC, C.a, 1); P.dot(mes, acMin, C.c, "MES"); P.vline(v.demand, C.b, "6 4", "market size");
      const n = v.demand / mes;
      out.innerHTML = `AC(Q) = F/Q + c + dQ. Minimum efficient scale MES = √(F/d) = <b>${G.fmt(mes)}</b> at AC = $${G.fmt(acMin)}. ` +
        `The market supports about <b>${G.fmt(n, 1)}</b> firms at MES. An entrant at Q = ${G.fmt(mes / 4)} pays AC = $${G.fmt(AC(mes / 4))}, ` +
        `${G.fmt(AC(mes / 4) - acMin)} more per unit than an incumbent at MES. Large MES relative to the market is a barrier to entry.`;
    }
    draw();
  }

  function learning(holder, pr) {
    const v = G.controls(holder, [
      { key: "C1", label: "First unit cost", min: 10, max: 1000, step: 10, value: pr.C1 },
      { key: "rate", label: "Learning rate", min: 0.6, max: 1, step: 0.01, value: pr.rate },
      { key: "N", label: "Units shown", min: 8, max: 512, step: 8, value: pr.N }], draw);
    const P = G.plot(holder, { h: 300, xlabel: "Cumulative units produced", ylabel: "Cost of unit n", title: "Learning curve" });
    const out = G.readout(holder);
    function draw() {
      const b = Math.log(v.rate) / Math.log(2), cost = n => v.C1 * Math.pow(n, b);
      P.clear(v.N, v.C1 * 1.05, 0);
      P.fn(cost, C.a, 1, v.N);
      for (let n = 1; n <= v.N; n *= 2) P.dot(n, cost(n), C.b, n <= 8 || n === v.N ? "$" + G.fmt(cost(n)) : null);
      out.innerHTML = `A ${Math.round(v.rate * 100)}% learning curve: each time cumulative output doubles, unit cost falls to ${Math.round(v.rate * 100)}% of its old level. ` +
        `Cost of unit n = C₁ · n^b with b = log(rate)/log 2 = <b>${G.fmt(b, 4)}</b>. Unit ${v.N} costs $${G.fmt(cost(v.N))}. ` +
        `The incumbent is far down the curve; a new entrant starts at $${G.fmt(v.C1)}. The barrier holds only if the incumbent keeps that knowledge to itself.`;
    }
    draw();
  }

  function network(holder, pr) {
    const v = G.controls(holder, [
      { key: "k", label: "Value per other user", min: 0.01, max: 2, step: 0.01, value: pr.k },
      { key: "price", label: "Price or cost to join", min: 1, max: 200, step: 1, value: pr.price },
      { key: "N", label: "Potential users", min: 50, max: 2000, step: 10, value: pr.N }], draw);
    const P = G.plot(holder, { h: 300, xlabel: "Users n", ylabel: "Dollars per user", title: "Network effects and critical mass" });
    const out = G.readout(holder);
    function draw() {
      const crit = v.price / v.k;
      P.clear(v.N, Math.max(v.k * v.N, v.price) * 1.1, 0);
      P.fn(n => v.k * n, C.a); P.hline(v.price, C.d, "6 4", "price to join");
      if (crit <= v.N) { P.dot(crit, v.price, C.c, "critical mass"); P.band(crit, v.N, C.c, "network grows"); P.band(0, crit, C.d, "network stalls"); }
      out.innerHTML = `Each user's value rises with the number of users: value = k · n. People join only when value exceeds the price, so a network needs ` +
        `<b>${G.fmt(crit, 0)}</b> users (critical mass = price / k) before it sustains itself. ` +
        (crit > v.N ? "Critical mass is larger than the market: this network never takes off." : "An incumbent past critical mass is hard to dislodge, since a new network starts with no users.");
    }
    draw();
  }

  M2.graphs.scale = function (holder, params) {
    const pr = Object.assign({ F: 5000, c: 10, d: 0.02, demand: 2000, C1: 500, rate: 0.8, N: 64, k: 0.1, price: 30 }, params);
    const views = { ac, learning, network };
    const list = pr.view ? [pr.view] : ["ac", "learning", "network"];
    for (const name of list) { const box = document.createElement("div"); holder.append(box); views[name](box, pr); }
  };
})(globalThis.M2 = globalThis.M2 || {});
