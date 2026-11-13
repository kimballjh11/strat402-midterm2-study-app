// Editable payoff matrix (2x2 or 3x3). Highlights best responses, finds dominant strategies, pure Nash equilibria,
// and for 2x2 the mixed strategy probabilities that make each player indifferent.
// params: {players: ["Row","Column"], rows: ["Up","Down"], cols: ["Left","Right"], pay: [[[r,c],[r,c]],[[r,c],[r,c]]]}
(function (M2) {
  const G = M2.G;
  M2.graphs.payoff = function (holder, params) {
    const pr = Object.assign({ players: ["Firm A", "Firm B"], rows: ["Low price", "High price"], cols: ["Low price", "High price"],
      pay: [[[0, 0], [12, -1]], [[-1, 12], [10, 10]]] }, params);
    const pay = pr.pay.map(r => r.map(c => c.slice()));
    const nR = pr.rows.length, nC = pr.cols.length;
    const tbl = document.createElement("table"); tbl.className = "g-matrix";
    holder.append(tbl);
    const out = G.readout(holder);
    const note = document.createElement("div"); note.className = "caption";
    note.textContent = `Edit any payoff. First number: ${pr.players[0]} (rows). Second: ${pr.players[1]} (columns). Green number = best response. Outlined cell = Nash equilibrium.`;
    holder.append(note);

    function analyze() {
      const brR = [], brC = [];
      for (let j = 0; j < nC; j++) { const m = Math.max(...pay.map(r => r[j][0])); brR.push(pay.map(r => r[j][0] === m)); }
      for (let i = 0; i < nR; i++) { const m = Math.max(...pay[i].map(c => c[1])); brC.push(pay[i].map(c => c[1] === m)); }
      const ne = [];
      for (let i = 0; i < nR; i++) for (let j = 0; j < nC; j++) if (brR[j][i] && brC[i][j]) ne.push([i, j]);
      // strictly dominant: best against every opponent strategy, strictly
      const domR = [...Array(nR).keys()].find(i => [...Array(nR).keys()].every(k => k === i || [...Array(nC).keys()].every(j => pay[i][j][0] > pay[k][j][0])));
      const domC = [...Array(nC).keys()].find(j => [...Array(nC).keys()].every(k => k === j || [...Array(nR).keys()].every(i => pay[i][j][1] > pay[i][k][1])));
      return { brR, brC, ne, domR, domC };
    }

    function draw() {
      const A = analyze();
      tbl.innerHTML = "";
      const h0 = tbl.insertRow(); h0.insertCell(); h0.insertCell();
      const th = document.createElement("th"); th.colSpan = nC; th.textContent = pr.players[1]; h0.append(th);
      const h1 = tbl.insertRow(); h1.insertCell(); h1.insertCell();
      pr.cols.forEach(c => { const t = document.createElement("th"); t.textContent = c; h1.append(t); });
      for (let i = 0; i < nR; i++) {
        const tr = tbl.insertRow();
        if (i === 0) { const t = document.createElement("th"); t.rowSpan = nR; t.textContent = pr.players[0]; tr.append(t); }
        const t = document.createElement("th"); t.textContent = pr.rows[i]; tr.append(t);
        for (let j = 0; j < nC; j++) {
          const td = tr.insertCell(); td.className = "g-cell" + (A.ne.some(([a, b]) => a === i && b === j) ? " ne" : "");
          [0, 1].forEach(k => {
            const inp = document.createElement("input"); inp.type = "number"; inp.value = pay[i][j][k];
            if ((k === 0 && A.brR[j][i]) || (k === 1 && A.brC[i][j])) inp.style.color = "#5fb878";
            inp.addEventListener("change", () => { if (isFinite(+inp.value) && inp.value !== "") { pay[i][j][k] = +inp.value; draw(); } });
            td.append(inp); if (k === 0) td.append(", ");
          });
        }
      }
      let s = "";
      s += `${pr.players[0]}: ${A.domR != null ? `dominant strategy <b>${pr.rows[A.domR]}</b>` : "no dominant strategy"}. `;
      s += `${pr.players[1]}: ${A.domC != null ? `dominant strategy <b>${pr.cols[A.domC]}</b>` : "no dominant strategy"}. `;
      s += A.ne.length ? `Pure strategy Nash equilibri${A.ne.length > 1 ? "a" : "um"}: <b>${A.ne.map(([i, j]) => `(${pr.rows[i]}, ${pr.cols[j]})`).join(", ")}</b>. ` : "No pure strategy Nash equilibrium. ";
      if (nR === 2 && nC === 2) {
        const b = (i, j) => pay[i][j][1], a = (i, j) => pay[i][j][0];
        const dp = b(0, 0) - b(1, 0) - b(0, 1) + b(1, 1), dq = a(0, 0) - a(0, 1) - a(1, 0) + a(1, 1);
        const p = dp ? (b(1, 1) - b(1, 0)) / dp : NaN, q = dq ? (a(1, 1) - a(0, 1)) / dq : NaN;
        if (p > 0 && p < 1 && q > 0 && q < 1)
          s += `Mixed equilibrium: ${pr.players[0]} plays ${pr.rows[0]} with probability <b>${G.fmt(p, 3)}</b> (makes ${pr.players[1]} indifferent); ${pr.players[1]} plays ${pr.cols[0]} with probability <b>${G.fmt(q, 3)}</b>.`;
      }
      out.innerHTML = s;
    }
    draw();
  };
})(globalThis.M2 = globalThis.M2 || {});
