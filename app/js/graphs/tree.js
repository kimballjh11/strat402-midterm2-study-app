// Extensive form game tree with backward induction. Terminal payoffs are editable; the subgame perfect choice at
// every decision node is drawn green and the equilibrium path is bold.
// params: {players: ["A","B"], tree: {p: 0, children: [{a: "Enter", n: {p: 1, children: [{a: "Fight", pay: [-1, 1]}, ...]}}, {a: "Stay out", pay: [0, 10]}]}}
(function (M2) {
  const G = M2.G, C = G.C;
  const NS = "http://www.w3.org/2000/svg";
  M2.graphs.tree = function (holder, params) {
    const pr = Object.assign({ players: ["Entrant", "Incumbent"], tree: { p: 0, children: [
      { a: "Enter", n: { p: 1, children: [{ a: "Fight", pay: [-1, 1] }, { a: "Accommodate", pay: [5, 5] }] } },
      { a: "Stay out", pay: [0, 10] }] } }, params);
    const root = JSON.parse(JSON.stringify(pr.tree));
    const svg = document.createElementNS(NS, "svg"); holder.append(svg);
    const edit = document.createElement("div"); edit.className = "g-controls"; holder.append(edit);
    const out = G.readout(holder);

    // backward induction: returns the payoff vector of the node, stores the chosen child index
    function solve(n) {
      if (n.pay) return n.pay;
      const vals = n.children.map(c => solve(c.n || c));
      let best = 0;
      vals.forEach((v, i) => { if (v[n.p] > vals[best][n.p]) best = i; });
      n.best = best; n.val = vals[best];
      return n.val;
    }
    // layout: leaves get consecutive x slots, parents sit above the middle of their children
    function layout(n, depth, st) {
      n.depth = depth;
      if (n.pay) { n.x = st.leaf++; return; }
      n.children.forEach(c => { const k = c.n || c; layout(k, depth + 1, st); });
      const xs = n.children.map(c => (c.n || c).x);
      n.x = (Math.min(...xs) + Math.max(...xs)) / 2;
    }
    const leaves = [];
    (function collect(n) { if (n.pay) leaves.push(n); else n.children.forEach(c => { if (c.pay) c.leafOf = true; collect(c.n || c); }); })(root);
    leaves.forEach((lf, i) => {
      const row = document.createElement("div"); row.className = "g-ctl";
      const lab = document.createElement("label"); lab.textContent = "Ending " + (i + 1); row.append(lab);
      [0, 1].forEach(k => {
        const inp = document.createElement("input"); inp.type = "number"; inp.value = lf.pay[k]; inp.title = pr.players[k];
        inp.addEventListener("input", () => { if (inp.value !== "" && isFinite(+inp.value)) { lf.pay[k] = +inp.value; draw(); } });
        row.append(inp);
      });
      edit.append(row);
    });

    function draw() {
      solve(root);
      const st = { leaf: 0 }; layout(root, 0, st);
      let depth = 0; (function d(n) { depth = Math.max(depth, n.depth); if (!n.pay) n.children.forEach(c => d(c.n || c)); })(root);
      const W = 640, H = 90 + depth * 110, X = x => 50 + x * (W - 100) / Math.max(1, st.leaf - 1), Y = d => 30 + d * 110;
      svg.setAttribute("viewBox", `0 0 ${W} ${H}`); svg.innerHTML = "";
      const add = (tag, a) => { const e = document.createElementNS(NS, tag); for (const k in a) e.setAttribute(k, a[k]); svg.append(e); return e; };
      const txt = (x, y, s, a) => { const t = add("text", Object.assign({ x, y, fill: C.text, "font-size": 13, "text-anchor": "middle" }, a || {})); t.textContent = s; };
      let li = 0;
      (function draw1(n, onPath) {
        if (n.pay) { li++; txt(X(n.x), Y(n.depth) + 18, `(${n.pay.join(", ")})`, { fill: onPath ? C.c : C.text, "font-weight": onPath ? 700 : 400 }); txt(X(n.x), Y(n.depth) + 34, "Ending " + li, { fill: C.muted, "font-size": 11 }); return; }
        n.children.forEach((c, i) => {
          const k = c.n || c, chosen = i === n.best;
          add("line", { x1: X(n.x), y1: Y(n.depth), x2: X(k.x), y2: Y(k.depth), stroke: chosen ? C.c : C.line, "stroke-width": chosen && onPath ? 4 : chosen ? 2.5 : 1.5 });
          txt((X(n.x) + X(k.x)) / 2 + (X(k.x) < X(n.x) ? -10 : 10), (Y(n.depth) + Y(k.depth)) / 2 - 4, c.a, { fill: chosen ? C.c : C.muted, "text-anchor": X(k.x) < X(n.x) ? "end" : "start" });
          draw1(k, onPath && chosen);
        });
        add("circle", { cx: X(n.x), cy: Y(n.depth), r: 6, fill: C.a });
        txt(X(n.x), Y(n.depth) - 12, pr.players[n.p], { fill: C.a, "font-weight": 600 });
      })(root, true);
      const path = []; let n = root;
      while (!n.pay) { const c = n.children[n.best]; path.push(`${pr.players[n.p]}: ${c.a}`); n = c.n || c; }
      out.innerHTML = `Subgame perfect equilibrium path: <b>${path.join(", then ")}</b>. Payoffs (${pr.players.join(", ")}) = <b>(${n.pay.join(", ")})</b>. ` +
        "Solve from the last move backward: at each node the mover picks the branch with the higher payoff for them. A threat that the mover would not carry out at that node is not credible.";
    }
    draw();
  };
})(globalThis.M2 = globalThis.M2 || {});
