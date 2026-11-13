// Session page: overview, then every objective inline (lesson, formulas, graph, traps, practice), then a mixed drill.
(function (M2) {
  const R = M2.render, h = (...a) => R.h(...a), E = M2.engine;

  M2.readout = function (lo) {
    const m = E.mastery(M2.store.get(), lo);
    if (!m.attempts) return "Not started";
    return (m.mastered ? "Mastered. " : "") + `${m.correct} of last ${m.window} correct` + (m.attempts < E.WINDOW ? `, ${m.attempts} of ${E.WINDOW} attempts so far` : "");
  };

  function section(title, body, cls) {
    if (!body) return null;
    return h("div.sec" + (cls ? "." + cls : ""), {}, title ? h("div.sec-title", { text: title }) : null, body);
  }
  const mdDiv = (t, cls) => t ? h("div" + (cls ? "." + cls : ""), { html: R.md(t) }) : null;

  function formulas(list) {
    if (!list || !list.length) return null;
    const box = h("div.formulas");
    for (const f of list) {
      box.append(h("div.formula", {},
        h("div.f-head", {}, h("span.f-name", { text: f.name || "" }),
          h("span.tag" + (f.onSheet ? ".on" : ".off"), { text: f.onSheet ? "On the sheet" : "Not on the sheet, know it cold" })),
        h("div.f-tex", { html: R.tex(f.tex, true) }),
        f.note ? h("div.f-note", { html: R.md(f.note) }) : null));
    }
    return box;
  }

  function worked(list) {
    if (!list || !list.length) return null;
    const box = h("div");
    for (const w of list) {
      const steps = h("ol.steps");
      for (const s of w.steps || []) steps.append(h("li", { html: R.md(s).replace(/^<p>|<\/p>$/g, "") }));
      box.append(h("div.worked", {},
        w.title ? h("div.w-title", { text: w.title }) : null,
        h("div.w-problem", { html: R.md(w.problem) }), steps,
        w.answer ? h("div.w-answer", { html: "<b>Answer.</b> " + R.md(w.answer).replace(/^<p>|<\/p>$/g, "") }) : null));
    }
    return box;
  }

  function graphs(spec) {
    if (!spec) return null;
    const list = Array.isArray(spec) ? spec : [spec];
    const box = h("div");
    for (const g of list) {
      const holder = h("div.graph");
      const fn = M2.graphs && M2.graphs[g.component];
      if (fn) { try { fn(holder, g.params || {}); } catch (e) { holder.textContent = "Graph error: " + e.message; } }
      else holder.textContent = "Graph component '" + g.component + "' is not built yet.";
      if (g.caption) holder.append(h("div.caption", { html: R.md(g.caption) }));
      box.append(holder);
    }
    return box;
  }

  function sourcesLine(s) {
    if (!s) return null;
    const parts = Object.entries(s).filter(([, v]) => v).map(([k, v]) => `${({ slides: "Slides", read: "Reading", exercise: "Exercise", quiz: "Quiz", notes: "Notes" })[k] || k}: ${v}`);
    return parts.length ? h("div.sources", { text: parts.join("  |  ") }) : null;
  }

  M2.blocks = {};          // LO id -> practice block on the current page

  M2.renderSession = function (main, n) {
    const D = M2.D;
    const los = D.objectives.filter(o => o.session === n);
    const pending = (D.config.pending_sessions || []).includes(n);
    const info = (D.sessions || {})["S" + n] || {};
    M2.blocks = {};
    main.append(h("h1", { text: `Session ${n}: ${los[0] ? los[0].topic : ""}` }));
    if (info.provisional) main.append(h("div.banner", { html: R.md(info.provisional) }));
    if (pending) main.append(h("div.banner", { text: "Pending class materials. Professor questions below still count." }));
    if (info.overview) main.append(h("div.overview", { html: R.md(info.overview) }));
    const toc = h("div.toc");
    for (const o of los) toc.append(h("a", { href: `#/s${n}/${o.id}`, text: `${o.id}  ${o.short}` }), h("span.toc-r", { "data-lo": o.id, text: M2.readout(o.id) }), h("br"));
    main.append(toc);

    for (const o of los) {
      const L = D.lessons[o.id];
      const sec = h("section.lo", { id: "lo-" + o.id });
      sec.append(h("div.lo-head", {}, h("h2", { text: `${o.id}  ${L ? L.title : o.short}` }), h("span.readout", { "data-lo": o.id, text: M2.readout(o.id) })));
      sec.append(h("div.lo-text", { text: o.text }));
      if (L) {
        if (L.emphasis) sec.append(h("div.emph", { text: "Emphasized in review materials." }));
        sec.append(
          mdDiv(L.plain, "plain"),
          section("Why it matters", mdDiv(L.why)),
          section("Definition", mdDiv(L.definition, "def")),
          section("Formulas", formulas(L.formulas)),
          section("Derivation", mdDiv(L.derivation)),
          ...(L.math || []).map(m => section("Math refresher: " + m.title, mdDiv(m.body), "refresher")),
          section("Worked example", worked(L.worked)),
          section("Graph", graphs(L.graph)),
          section("Exam traps", L.traps && L.traps.length ? h("ul.traps", {}, L.traps.map(t => h("li", { html: R.md(t).replace(/^<p>|<\/p>$/g, "") }))) : null),
          sourcesLine(L.sources));
      } else sec.append(h("div.empty", { text: "Lesson not written yet." }));
      sec.append(h("div.sec-title", { text: "Practice" }));
      main.append(sec);
      M2.blocks[o.id] = M2.Practice(sec, { scope: [o.id], onMastered: () => M2.goNextUnmastered(o.id) });
    }
    const mixed = h("section.lo", { id: "mixed" }, h("h2", { text: "Session mixed drill" }), h("div.lo-text", { text: "Draws from the weakest objectives first." }));
    main.append(mixed);
    if (los.length) M2.Practice(mixed, { scope: los.map(o => o.id) });
    R.math(main);
  };

  // First unmastered objective in build order, starting after `after` if given.
  M2.firstUnmastered = function (after) {
    const D = M2.D, p = M2.store.get();
    const order = D.objectives.filter(o => (D.config.build_sessions || []).includes(o.session));
    let start = after ? order.findIndex(o => o.id === after) + 1 : 0;
    for (let k = 0; k < order.length; k++) {
      const o = order[(start + k) % order.length];
      if (!E.mastery(p, o.id).mastered) return o;
    }
    return null;
  };

  M2.goNextUnmastered = function (after) {
    const o = M2.firstUnmastered(after);
    if (!o) { alertLine("Every objective in the build is mastered. Try a mock exam."); return; }
    M2.go(`#/s${o.session}/${o.id}`);
  };
  function alertLine(t) { const b = document.getElementById("flash"); if (b) { b.textContent = t; b.hidden = false; } }

  M2.refreshReadouts = function () {
    document.querySelectorAll("[data-lo]").forEach(el => { el.textContent = M2.readout(el.getAttribute("data-lo")); });
  };
})(globalThis.M2 = globalThis.M2 || {});
