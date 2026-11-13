// Question card (shared by practice, queue and mock) and the in-place practice block with keyboard control.
(function (M2) {
  const R = M2.render, h = (...a) => R.h(...a), E = M2.engine;
  const LETTERS = "ABCDEFGHI";
  M2.bus = M2.bus || new EventTarget();
  M2.emit = (type, detail) => M2.bus.dispatchEvent(new CustomEvent(type, { detail }));

  const isTF = q => q.type === "tf" || (q.choices && q.choices.length === 2 && /^true$/i.test(q.choices[0].trim()) && /^false$/i.test(q.choices[1].trim()));

  M2.answerText = function (q) {
    if (q.type === "num") return M2.fmt(q.answer, 4) + (q.unit ? " " + q.unit : "");
    if (q.type === "multi") return q.answer.map(i => LETTERS[i] + ". " + q.choices[i]).join("; ");
    return LETTERS[q.answer] + ". " + q.choices[q.answer];
  };

  // Card: renders one question. mode "practice" gives instant feedback, "exam" only stores the response.
  M2.Card = function (q, opts) {
    opts = opts || {};
    const self = { q, done: false, response: opts.response != null ? opts.response : (q.type === "multi" ? [] : null) };
    const el = h("div.card");
    if (q.caseRef && !opts.hideCase) el.append(h("div.case", { html: `<div class="case-title">${R.esc(q.caseRef.title)}</div>` + R.md(q.caseRef.stem, q.caseRef.tables) }));
    const meta = [];
    if (opts.label) meta.push(opts.label);
    if (q.source === "professor") meta.push("Professor question, " + (q.origin || ""));
    else if (q.source === "generated") meta.push("Fresh variant");
    if (q.caseRef) meta.push("Part " + q.part);
    if (meta.length) el.append(h("div.meta", { text: meta.join("  |  ") }));
    el.append(h("div.stem", { html: R.md(q.stem, q.tables) }));

    const fb = h("div.feedback");
    let choiceEls = [], input = null;
    if (q.type === "num") {
      input = h("input.num", { type: "text", inputmode: "decimal", autocomplete: "off", spellcheck: "false", placeholder: "Answer, then Enter" });
      if (self.response != null) input.value = self.response;
      input.addEventListener("keydown", e => {
        if (e.key === "Enter") { e.preventDefault(); e.stopPropagation(); if (self.done) opts.onNext && opts.onNext(); else self.submit(input.value); }
      });
      input.addEventListener("input", () => { if (opts.mode === "exam") { self.response = input.value; opts.onChange && opts.onChange(self.response); } });
      el.append(h("div.numrow", {}, input, q.unit ? h("span.unit", { text: q.unit }) : null));
    } else {
      const list = h("div.choices");
      q.choices.forEach((c, i) => {
        const key = isTF(q) ? (i === 0 ? "T" : "F") : String(i + 1);
        const b = h("button.choice", { type: "button", onclick: () => self.pick(i) },
          h("span.key", { text: key }), h("span.ctext", { html: R.md(c).replace(/^<p>|<\/p>$/g, "") }));
        choiceEls.push(b); list.append(b);
      });
      el.append(list);
      if (q.type === "multi") el.append(h("div.hint", { text: "Select all that apply, then Enter." }));
    }
    el.append(fb);
    self.el = el; self.input = input;

    function paintSel() {
      choiceEls.forEach((b, i) => b.classList.toggle("sel", q.type === "multi" ? self.response.includes(i) : self.response === i));
    }
    paintSel();

    self.pick = function (i) {
      if (self.done || i < 0 || i >= q.choices.length) return;
      if (q.type === "multi") {
        const k = self.response.indexOf(i);
        k >= 0 ? self.response.splice(k, 1) : self.response.push(i);
        paintSel();
        if (opts.mode === "exam") opts.onChange && opts.onChange(self.response.slice());
        return;
      }
      self.response = i; paintSel();
      if (opts.mode === "exam") { opts.onChange && opts.onChange(i); return; }
      self.submit(i);
    };

    self.submit = function (resp) {
      if (self.done || opts.mode === "exam") return;
      if (resp === undefined) resp = q.type === "num" ? (input && input.value) : self.response;
      const ok = E.check(q, resp);
      if (ok === null) { fb.innerHTML = '<div class="warn">Enter a number. Fractions, %, $ and commas are fine.</div>'; return; }
      self.done = true; self.correct = ok; self.response = resp;
      self.reveal(ok);
      opts.onAnswer && opts.onAnswer(ok, resp);
    };

    // Show the result and explanation. Also used by the mock review.
    self.reveal = function (ok, note) {
      self.done = true;
      el.classList.add(ok ? "is-right" : "is-wrong");
      if (input) input.disabled = true;
      choiceEls.forEach((b, i) => {
        const right = q.type === "multi" ? q.answer.includes(i) : q.answer === i;
        b.classList.toggle("right", right);
        const chosen = q.type === "multi" ? (self.response || []).includes(i) : self.response === i;
        b.classList.toggle("wrong", chosen && !right);
        b.disabled = true;
      });
      let html = `<div class="verdict ${ok ? "ok" : "no"}">${ok ? "Correct" : "Wrong"}</div>`;
      if (!ok) html += `<div class="answer">Correct answer: ${R.esc(M2.answerText(q))}</div>`;
      if (q.type === "num" && self.response != null && self.response !== "") html += `<div class="yours">Your answer: ${R.esc(self.response)}</div>`;
      html += `<div class="explain">${R.md(q.explain, q.tables)}</div>`;
      if (q.trap) html += `<div class="trap"><b>Trap.</b> ${R.md(q.trap).replace(/^<p>|<\/p>$/g, "")}</div>`;
      if (note) html += `<div class="note">${R.esc(note)}</div>`;
      if (opts.mode !== "review") html += `<div class="hint">Enter or N for the next question.</div>`;
      fb.innerHTML = html;
      R.math(fb);
    };

    self.key = function (e) {
      const k = e.key;
      if (self.done) {
        if (k === "Enter" || k === "n" || k === "N") { e.preventDefault(); opts.onNext && opts.onNext(); }
        return;
      }
      if (q.type === "num") {
        if (/^[0-9.\-$]$/.test(k) && document.activeElement !== input) { input.focus(); }
        return;
      }
      if (isTF(q) && /^[tTfF]$/.test(k)) { e.preventDefault(); self.pick(/t/i.test(k) ? 0 : 1); return; }
      if (/^[1-9]$/.test(k)) { e.preventDefault(); self.pick(+k - 1); return; }
      if (/^[a-dA-D]$/.test(k) && !isTF(q)) { e.preventDefault(); self.pick(k.toUpperCase().charCodeAt(0) - 65); return; }
      if (k === "Enter" && q.type === "multi") { e.preventDefault(); self.submit(self.response.slice()); }
    };
    self.focus = function () { if (input && !self.done) input.focus({ preventScroll: true }); };
    return self;
  };

  // Practice block: one question at a time, in place. scope = [LO ids]. Only the active block listens to keys.
  M2.Practice = function (container, opts) {
    const D = M2.D, p = M2.store.get();
    const self = { scope: opts.scope, recent: [], card: null, el: h("div.practice", { tabindex: "0" }) };
    container.append(self.el);
    self.el.addEventListener("mousedown", () => M2.activate(self));
    self.el.addEventListener("focusin", () => M2.activate(self));

    self.next = function () {
      if (self.masteredNow && opts.onMastered) { self.masteredNow = false; opts.onMastered(); return; }
      const pick = opts.queueOnly ? { q: E.pickQueue(D, p, self.recent.slice(-1)), fromQueue: true } : E.next(D, p, self.scope, self.recent);
      self.el.innerHTML = "";
      if (!pick.q) {
        self.el.append(h("div.empty", { text: opts.queueOnly ? "The missed queue is empty." : "No questions for this objective yet." }));
        self.card = null; return;
      }
      E.served(p, pick.fromQueue); M2.store.commit();
      const q = pick.q;
      self.recent.push(q.id); if (self.recent.length > 4) self.recent.shift();
      const los = (q.los || []).join(", ");
      const label = (pick.fromQueue ? "Missed queue item  |  " : "") + los;
      self.card = M2.Card(q, {
        mode: "practice", label,
        onAnswer(ok) {
          const before = self.scope.length === 1 ? E.mastery(p, self.scope[0]).mastered : true;
          E.record(p, q, ok); M2.store.commit();
          if (self.scope.length === 1 && !before && E.mastery(p, self.scope[0]).mastered) {
            self.masteredNow = !!opts.onMastered;
            self.card.el.append(h("div.mastered", { text: `Objective ${self.scope[0]} mastered. Enter moves to the next unmastered objective.` }));
          }
          if (opts.queueOnly) self.card.el.append(h("div.note", { text: `${p.queue.length} left in the queue.` }));
          M2.emit("progress");
        },
        onNext: () => { self.next(); self.focus(); }
      });
      self.el.append(self.card.el);
      R.math(self.card.el);
    };
    self.key = e => self.card && self.card.key(e);
    self.focus = function () {
      M2.activate(self);
      if (self.card && self.card.input && !self.card.done) self.card.focus();
      else self.el.focus({ preventScroll: true });
    };
    self.next();
    return self;
  };

  M2.activate = function (block) {
    if (M2.active && M2.active !== block) M2.active.el.classList.remove("active");
    M2.active = block; block.el.classList.add("active");
  };
})(globalThis.M2 = globalThis.M2 || {});
