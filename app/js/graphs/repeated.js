// Trigger strategy calculator for an infinitely repeated game (professor's S20 convention):
// PV collude = pi_c + pi_c / i,  PV cheat = pi_d + pi_n / i,  indifferent at i* = (pi_c - pi_n) / (pi_d - pi_c).
// params: {coop, cheat, nash, i}  defaults are the Kellogg's example from the S20 slides.
(function (M2) {
  const G = M2.G, C = G.C;
  M2.graphs.repeated = function (holder, params) {
    const pr = Object.assign({ coop: 12, cheat: 15, nash: 2, i: 0.10 }, params);
    const v = G.controls(holder, [
      { key: "coop", label: "Collude payoff", min: 0, max: 100, step: 1, value: pr.coop },
      { key: "cheat", label: "Cheat payoff (once)", min: 0, max: 150, step: 1, value: pr.cheat },
      { key: "nash", label: "Punishment payoff", min: 0, max: 100, step: 1, value: pr.nash },
      { key: "i", label: "Interest rate i", min: 0.01, max: 6, step: 0.01, value: pr.i }], draw);
    const P = G.plot(holder, { h: 300, xlabel: "Interest (discount) rate i", ylabel: "Present value", title: "Present value of colluding vs cheating" });
    const out = G.readout(holder);
    function draw() {
      const pvC = i => v.coop + v.coop / i, pvD = i => v.cheat + v.nash / i;
      const istar = v.cheat > v.coop ? (v.coop - v.nash) / (v.cheat - v.coop) : Infinity;
      const xmax = Math.max(v.i * 1.5, isFinite(istar) ? istar * 2 : 2, 0.5);
      const xmin = Math.min(0.02, v.i / 2);
      P.o.xmin = xmin;
      P.clear(xmax, Math.max(pvC(Math.max(xmin, xmax / 8)), pvD(Math.max(xmin, xmax / 8))) * 1.1, 0);
      P.fn(pvC, C.c, xmin, xmax); P.fn(pvD, C.d, xmin, xmax);
      if (isFinite(istar) && istar > 0) { P.vline(istar, C.b, "4 4", "i* = " + G.fmt(istar, 3)); P.dot(istar, pvC(istar), C.b); }
      P.vline(v.i, C.a, "2 3", "your i");
      P.legend([["PV collude = π_c + π_c / i", C.c], ["PV cheat = π_d + π_n / i", C.d]]);
      const a = pvC(v.i), b = pvD(v.i);
      out.innerHTML = `At i = ${G.fmt(v.i, 3)}: PV collude = ${G.fmt(v.coop)} + ${G.fmt(v.coop)}/${G.fmt(v.i, 3)} = <b>${G.fmt(a)}</b>; ` +
        `PV cheat = ${G.fmt(v.cheat)} + ${G.fmt(v.nash)}/${G.fmt(v.i, 3)} = <b>${G.fmt(b)}</b>. ` +
        (a >= b ? "Colluding is worth more: the trigger strategy sustains collusion." : "Cheating is worth more: collusion breaks down.") +
        (isFinite(istar) ? ` Indifferent at i* = (π_c − π_n)/(π_d − π_c) = <b>${G.fmt(istar, 4)}</b>; collusion holds for any i ≤ i*. Discount factor δ = 1/(1 + i).` : " Cheating pays no more than colluding, so nobody cheats.");
    }
    draw();
  };
})(globalThis.M2 = globalThis.M2 || {});
