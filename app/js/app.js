// Router (#/s15, #/s15/S15-04, #/queue, #/mock), sidebar, keyboard dispatch, export and import.
(function (M2) {
  const R = M2.render, h = (...a) => R.h(...a), E = M2.engine;
  const SESSIONS = [15, 16, 18, 19, 20, 21, 22];
  let current = null;

  M2.go = function (hash) { if (location.hash === hash) M2.route(); else location.hash = hash; };

  function sidebar() {
    const D = M2.D, p = M2.store.get(), side = document.getElementById("side");
    side.innerHTML = "";
    side.append(h("button.primary.continue", { type: "button", text: "Continue", onclick: () => M2.goNextUnmastered() }));
    const nav = h("nav");
    for (const n of SESSIONS) {
      const los = D.objectives.filter(o => o.session === n);
      const pending = (D.config.pending_sessions || []).includes(n);
      const done = los.filter(o => E.mastery(p, o.id).mastered).length;
      const name = los[0] ? los[0].topic : "";
      nav.append(h("a" + (current === "s" + n ? ".cur" : ""), { href: "#/s" + n }, h("span", { text: `S${n} ${name}` }),
        h("span.count", { text: pending ? "pending materials" : `${done}/${los.length}` })));
    }
    nav.append(h("a" + (current === "queue" ? ".cur" : ""), { href: "#/queue" }, h("span", { text: "Missed queue" }), h("span.count", { text: String(p.queue.length) })));
    nav.append(h("a" + (current === "mock" ? ".cur" : ""), { href: "#/mock" }, h("span", { text: "Mock exam" }), h("span.count", { text: p.mock ? "in progress" : "" })));
    side.append(nav);
    const file = h("input", { type: "file", accept: "application/json,.json", hidden: true });
    file.addEventListener("change", () => {
      if (!file.files[0]) return;
      M2.store.importFile(file.files[0], err => { flash(err ? "Import failed: " + err.message : "Progress imported."); M2.route(); });
    });
    side.append(h("div.foot", {},
      h("button", { type: "button", text: "Export", onclick: () => M2.store.exportFile() }),
      h("button", { type: "button", text: "Import", onclick: () => file.click() }), file,
      h("div.built", { text: "Content built " + new Date(D.built).toLocaleString() })));
  }

  function flash(t) { const f = document.getElementById("flash"); f.textContent = t; f.hidden = !t; }

  function home(main) {
    const D = M2.D, p = M2.store.get();
    main.append(h("h1", { text: "STRAT 402 Midterm 2" }));
    const o = M2.firstUnmastered();
    main.append(h("p", { text: o ? `Next unmastered objective: ${o.id} ${o.short}. Press Continue or Enter.` : "Every objective in the build is mastered." }));
    const t = h("table.qt", {}, h("tr", {}, h("th", { text: "Session" }), h("th", { text: "Mastered" }), h("th", { text: "Questions" })));
    for (const n of SESSIONS) {
      const los = D.objectives.filter(x => x.session === n);
      const nq = D.questions.filter(q => (q.los || []).some(l => E.sessionOf(l) === n)).length;
      t.append(h("tr", {}, h("td", {}, h("a", { href: "#/s" + n, text: `S${n} ${los[0] ? los[0].topic : ""}` })),
        h("td", { text: `${los.filter(x => E.mastery(p, x.id).mastered).length} of ${los.length}` }), h("td", { text: String(nq) })));
    }
    main.append(t);
    main.append(h("div.sec-title", { text: "Keys" }), h("p.muted", { text: "1 to 9 or A to D choose. T and F answer true or false. Enter submits a number or moves on. N also moves on. Click a practice block to give it the keyboard." }));
    M2.homeEnter = () => M2.goNextUnmastered();
  }

  M2.route = function () {
    const main = document.getElementById("main");
    const hash = location.hash || "#/";
    let m;
    M2.homeEnter = null;
    if ((m = /^#\/s(\d+)(?:\/(S\d+-\d+))?$/.exec(hash))) {
      const key = "s" + m[1];
      if (current !== key || !document.getElementById("mixed")) {
        current = key; main.innerHTML = ""; M2.active = null; M2.renderSession(main, +m[1]);
      }
      const target = m[2] && document.getElementById("lo-" + m[2]);
      if (target) {
        target.scrollIntoView({ block: "start" });
        const b = M2.blocks[m[2]]; if (b) b.focus();
        setTimeout(() => target.scrollIntoView({ block: "start" }), 250);      // again after fonts and math settle
      } else window.scrollTo(0, 0);
    } else if (hash === "#/queue") {
      current = "queue"; main.innerHTML = ""; M2.active = null;
      const p = M2.store.get();
      main.append(h("h1", { text: "Missed queue" }), h("p.muted", { text: `${p.queue.length} items. An item leaves after 2 correct answers in a row.` }));
      const b = M2.Practice(main, { queueOnly: true, scope: [] }); b.focus();
    } else if (hash === "#/mock") {
      current = "mock"; main.innerHTML = ""; M2.active = null; M2.renderMock(main); window.scrollTo(0, 0);
    } else {
      current = null; main.innerHTML = ""; M2.active = null; home(main);
    }
    flash("");
    sidebar();
  };

  document.addEventListener("keydown", e => {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const t = e.target;
    const typing = t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" || t.tagName === "SELECT");
    const cardInput = M2.active && M2.active.card && t === M2.active.card.input;
    if (typing && !cardInput) return;              // graph sliders and number boxes keep their keys
    if (e.key === "Escape") return;
    if (!M2.active && M2.homeEnter && e.key === "Enter") { e.preventDefault(); M2.homeEnter(); return; }
    if (M2.active) M2.active.key(e);
  });

  M2.bus && M2.bus.addEventListener("progress", () => { M2.refreshReadouts(); sidebar(); });

  window.addEventListener("hashchange", M2.route);
  window.addEventListener("DOMContentLoaded", () => {
    if (!window.M2DATA) { document.getElementById("main").textContent = "app/data/data.js is missing. Run: node scripts/build_data.js"; return; }
    M2.D = E.prepare(window.M2DATA);
    M2.route();
  });
})(globalThis.M2 = globalThis.M2 || {});
