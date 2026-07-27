/* ============================================================
   SOMARA — Motor do protótipo (vanilla JS)
   welcome → onboarding → mapa (amarelinha, de baixo p/ cima) →
   lição → completo → perfil. Vidas (5), XP, progresso guardado.
   Dois cursos: Matemática e Português. Mascote: Roby.
   ============================================================ */
(function () {
  "use strict";
  var C = window.SOMARA_CONTENT;
  var KEY = "somara_state_v2";
  var MAXLIVES = 5, XP_OK = 10, XP_LEVEL = 20;

  var def = { onboarded: false, learner: { nome: "", classe: "1ª classe", nivel: "" },
              xp: 0, streak: 1, lives: MAXLIVES, progress: {}, cursoId: C.cursos[0].id };
  var S = load();
  var CURSO = C.cursos.filter(function (c) { return c.id === S.cursoId; })[0] || C.cursos[0];

  function load() { try { return Object.assign({}, def, JSON.parse(localStorage.getItem(KEY)) || {}); } catch (e) { return Object.assign({}, def); } }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }

  var app = document.getElementById("app");
  function $(s, c) { return (c || document).querySelector(s); }
  function esc(x) { return String(x).replace(/[&<>"']/g, function (m) { return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[m]; }); }
  function show(id) {
    document.querySelectorAll(".screen").forEach(function (s) { s.classList.toggle("active", s.id === id); });
    var bar = (id === "screen-map" || id === "screen-profile");
    $("#topbar").style.display = bar ? "flex" : "none";
    if (bar) renderTopbar();
    app.scrollTop = 0;
  }
  function toast(msg) { var t = $("#toast"); t.textContent = msg; t.classList.remove("show"); void t.offsetWidth; t.classList.add("show"); }
  function isNum(a) { return /^-?[0-9]+$/.test(String(a)); }

  /* ---- níveis do curso actual (lista plana) ---- */
  var LEVELS = [];
  function buildLevels() { LEVELS = []; CURSO.units.forEach(function (u) { u.niveis.forEach(function (n) { LEVELS.push({ unit: u, nivel: n }); }); }); }
  function keyOf(lv) { return CURSO.id + ":" + lv.unit.id + ":" + lv.nivel.id; }
  function levelDone(lv) { var k = keyOf(lv); return !!(S.progress[k] && S.progress[k].done); }
  function firstOpen() { for (var i = 0; i < LEVELS.length; i++) if (!levelDone(LEVELS[i])) return i; return LEVELS.length; }
  function statusOf(i) { if (levelDone(LEVELS[i])) return "done"; return i === firstOpen() ? "current" : "locked"; }

  /* ---- topbar ---- */
  function renderTopbar() {
    $("#topbar").innerHTML =
      '<div class="tb-item tb-lives"><span class="ico">❤️</span>' + S.lives + "</div>" +
      '<div class="tb-item tb-xp"><span class="ico">⚡</span>' + S.xp + "</div>" +
      '<div class="tb-item tb-streak"><span class="ico">🔥</span>' + S.streak + "</div>" +
      '<div class="tb-spacer"></div><button class="tb-gear" id="go-profile" aria-label="Perfil">☰</button>';
    $("#go-profile").onclick = function () { renderProfile(); show("screen-profile"); };
  }

  /* ---- welcome (com Roby) ---- */
  function renderWelcome() {
    $("#screen-welcome").innerHTML =
      '<div class="pad center grow welcome">' +
        '<div class="roby-hero"><img src="assets/img/roby-hero.png" alt="Roby, o teu guia" /></div>' +
        '<div class="wordmark">SOMARA</div>' +
        '<div class="tagline">Aprende · Cresce · Brilha</div>' +
        '<p class="sub">Sou o <b>Roby</b>! Vamos aprender matemática e português, nível a nível, como uma amarelinha. Da creche ao superior.</p>' +
        '<div class="actions">' +
          '<button class="sbtn" id="w-start">' + (S.onboarded ? "Continuar" : "Começar") + "</button>" +
          (S.onboarded ? "" : '<button class="link" id="w-have">Já aprendo aqui</button>') +
        "</div>" +
      "</div>";
    $("#w-start").onclick = function () { if (S.onboarded) { buildLevels(); renderMap(); show("screen-map"); } else startOnboarding(); };
    if ($("#w-have")) $("#w-have").onclick = startOnboarding;
  }

  /* ---- onboarding ---- */
  var ob = { step: 0, tmp: {} };
  var STEPS = ["nome", "classe", "nivel", "encarregado"];
  function startOnboarding() { ob = { step: 0, tmp: { classe: "1ª classe" } }; renderOnboarding(); show("screen-onboarding"); }
  function renderOnboarding() {
    var pct = Math.round(ob.step / STEPS.length * 100), body = "";
    if (STEPS[ob.step] === "nome") body = card("Quem vai aprender?", "Diz o teu nome (ou o do teu educando).", '<input class="field" id="f-nome" placeholder="O teu nome" value="' + esc(ob.tmp.nome || "") + '" autocomplete="off" />');
    else if (STEPS[ob.step] === "classe") body = card("Que classe frequenta?", "Vamos começar pelo 1º ciclo.", '<div class="chips" id="f-classe">' + chip("1ª classe", ob.tmp.classe === "1ª classe") + chipOff("2ª classe") + chipOff("3ª classe") + "</div>");
    else if (STEPS[ob.step] === "nivel") body = card("Qual é o teu nível?", "Assim ajustamos a dificuldade.", '<div class="chips" id="f-nivel">' + chip("Estou a começar", ob.tmp.nivel === "Estou a começar") + chip("Já sei um pouco", ob.tmp.nivel === "Já sei um pouco") + chip("Sei bem", ob.tmp.nivel === "Sei bem") + "</div>");
    else body = card("Acompanhamento do encarregado", "Opcional. Enviamos o progresso a quem cuida de ti.", '<input class="field" id="f-enc" placeholder="WhatsApp ou email do encarregado" value="' + esc(ob.tmp.encarregado || "") + '" autocomplete="off" />');
    var last = ob.step === STEPS.length - 1;
    $("#screen-onboarding").innerHTML =
      '<div class="ob-head"><div class="ob-progress"><i style="width:' + pct + '%"></i></div></div>' +
      '<div class="grow scroll pad">' + body + "</div>" +
      '<div class="ob-foot">' + (last ? '<button class="link" id="ob-skip" style="margin-bottom:6px">Saltar</button>' : "") + '<button class="sbtn" id="ob-next">' + (last ? "Concluir" : "Continuar") + "</button></div>";
    wireChips("#f-classe", function (v) { ob.tmp.classe = v; });
    wireChips("#f-nivel", function (v) { ob.tmp.nivel = v; });
    if ($("#ob-skip")) $("#ob-skip").onclick = finishOnboarding;
    $("#ob-next").onclick = onboardNext;
  }
  function card(q, h, i) { return '<h2 class="ob-q">' + q + '</h2><p class="ob-hint">' + h + "</p>" + i; }
  function chip(l, on) { return '<button class="chip" aria-pressed="' + (on ? "true" : "false") + '" data-v="' + esc(l) + '">' + l + "</button>"; }
  function chipOff(l) { return '<button class="chip" disabled style="opacity:.5" aria-pressed="false">' + l + ' <span style="font-size:11px">· em breve</span></button>'; }
  function wireChips(sel, cb) { var b = $(sel); if (!b) return; b.querySelectorAll(".chip:not([disabled])").forEach(function (x) { x.onclick = function () { b.querySelectorAll(".chip").forEach(function (y) { y.setAttribute("aria-pressed", "false"); }); x.setAttribute("aria-pressed", "true"); cb(x.getAttribute("data-v")); }; }); }
  function onboardNext() {
    var k = STEPS[ob.step];
    if (k === "nome") { var v = ($("#f-nome").value || "").trim(); if (!v) { toast("Escreve o teu nome 🙂"); return; } ob.tmp.nome = v; }
    if (k === "nivel" && !ob.tmp.nivel) { toast("Escolhe o teu nível"); return; }
    if (k === "encarregado") { var e = $("#f-enc"); if (e) ob.tmp.encarregado = (e.value || "").trim(); finishOnboarding(); return; }
    ob.step++; renderOnboarding();
  }
  function finishOnboarding() {
    S.learner = { nome: ob.tmp.nome || "Estudante", classe: ob.tmp.classe || "1ª classe", nivel: ob.tmp.nivel || "", encarregado: ob.tmp.encarregado || "" };
    S.onboarded = true; save(); buildLevels(); renderMap(); show("screen-map");
    toast("Vamos lá, " + S.learner.nome.split(" ")[0] + "! ⚡");
  }

  /* ---- MAPA — amarelinha, de baixo para cima ---- */
  function renderMap() {
    buildLevels();
    var tabs = C.cursos.map(function (cu, ci) { return '<button class="disc-tab ' + (cu.id === CURSO.id ? "on" : "") + '" data-ci="' + ci + '">' + esc(cu.disciplina) + "</button>"; }).join("");
    var html = '<div class="meta-marker"><div class="meta-badge">★ META</div><div class="meta-sub">' + esc(CURSO.disciplina) + " · " + esc(CURSO.classe) + "</div></div>";
    for (var i = LEVELS.length - 1; i >= 0; i--) {
      var st = statusOf(i), lv = LEVELS[i], side = (i % 2 === 0) ? "L" : "R";
      html += '<div class="cell-row ' + side + '">' +
        '<button class="cell ' + st + '" data-i="' + i + '" ' + (st === "locked" ? "disabled" : "") + '>' +
          (st === "current" ? '<span class="pedra" title="a tua pedrinha"></span>' : "") +
          '<span class="cell-n">' + (st === "done" ? "✓" : (i + 1)) + "</span>" +
        "</button><span class=\"cell-lab\">" + esc(lv.nivel.titulo) + "</span></div>";
    }
    html += '<div class="entrada-marker"><div class="entrada-badge">ENTRADA</div></div>';
    $("#screen-map").innerHTML = '<div class="disc-tabs">' + tabs + "</div><div class=\"grow scroll amarela\" id=\"amarela\">" + html + "</div>";
    $("#screen-map").querySelectorAll(".disc-tab").forEach(function (b) { b.onclick = function () { CURSO = C.cursos[parseInt(b.getAttribute("data-ci"), 10)]; S.cursoId = CURSO.id; save(); renderMap(); }; });
    var box = $("#amarela");
    box.querySelectorAll(".cell[data-i]").forEach(function (b) { b.onclick = function () { startLesson(parseInt(b.getAttribute("data-i"), 10)); }; });
    requestAnimationFrame(function () { var cur = box.querySelector(".cell.current"); if (cur) cur.scrollIntoView({ block: "center" }); else box.scrollTop = box.scrollHeight; });
  }

  /* ---- LIÇÃO ---- */
  var L = null;
  function startLesson(i) {
    if (S.lives <= 0) { openLives(); return; }
    var lv = LEVELS[i];
    L = { i: i, unit: lv.unit, nivel: lv.nivel, qs: lv.nivel.questoes, idx: 0, ok: 0, phase: "answer", sel: null };
    show("screen-lesson"); renderQuestion();
  }
  function renderQuestion() {
    var q = L.qs[L.idx], prog = Math.round(L.idx / L.qs.length * 100), body = "";
    if (q.t === "count") { var e = ""; for (var j = 0; j < q.n; j++) e += "<span>" + q.emoji + "</span>"; body = "<h2>" + esc(q.q) + '</h2><div class="count-box">' + e + "</div>" + opts(q.options); }
    else if (q.t === "choice") body = "<h2>" + esc(q.q) + "</h2>" + opts(q.options);
    else body = "<h2>" + esc(q.q) + '</h2><input class="field" id="q-input" inputmode="' + (isNum(q.a) ? "numeric" : "text") + '" autocomplete="off" autocapitalize="characters" placeholder="Escreve a resposta" style="margin-top:24px;text-align:center;font-size:24px" />';
    $("#screen-lesson").innerHTML =
      '<div class="lesson-top"><button class="lx-close" id="lx-x" aria-label="Sair">✕</button><div class="lx-bar"><i style="width:' + prog + '%"></i></div><div class="lx-lives" id="lx-lives">❤️ ' + S.lives + "</div></div>" +
      '<div class="q-area grow scroll">' + body + '</div><div id="lx-dock"></div><div class="xp-pop" id="xp-pop"></div>';
    $("#lx-x").onclick = function () { if (confirm("Sair da lição? Este nível não conta.")) { renderMap(); show("screen-map"); } };
    if (q.t === "input") { var inp = $("#q-input"); inp.oninput = function () { $("#dock-btn").disabled = !inp.value.trim(); }; inp.onkeydown = function (ev) { if (ev.key === "Enter" && inp.value.trim()) evaluate(); }; setTimeout(function () { inp.focus(); }, 60); }
    else wireOpts();
    $("#lx-dock").innerHTML = '<div class="pad" style="padding-top:6px"><button class="sbtn" id="dock-btn" disabled>Verificar</button></div>';
    $("#dock-btn").onclick = evaluate;
  }
  function opts(o) { return '<div class="opts" id="opts">' + o.map(function (x, k) { return '<button class="opt" data-k="' + k + '">' + esc(x) + "</button>"; }).join("") + "</div>"; }
  function wireOpts() { $("#opts").querySelectorAll(".opt").forEach(function (b) { b.onclick = function () { if (L.phase !== "answer") return; $("#opts").querySelectorAll(".opt").forEach(function (x) { x.setAttribute("aria-pressed", "false"); }); b.setAttribute("aria-pressed", "true"); L.sel = parseInt(b.getAttribute("data-k"), 10); $("#dock-btn").disabled = false; }; }); }
  function evaluate() {
    var q = L.qs[L.idx], correct;
    if (q.t === "input") { var v = ($("#q-input").value || "").trim(); correct = v.toUpperCase() === String(q.a).trim().toUpperCase(); L.sel = v; }
    else correct = L.sel === q.a;
    L.phase = "feedback";
    if (correct) { L.ok++; S.xp += XP_OK; save(); if (q.t !== "input") mark(L.sel, "correct"); xpPop("+" + XP_OK + " XP"); }
    else { loseLife(); if (q.t !== "input") { mark(L.sel, "wrong"); mark(q.a, "correct"); shake(L.sel); } }
    feedback(correct, q);
  }
  function mark(k, c) { var o = $("#opts"); if (o) { var b = o.querySelector('.opt[data-k="' + k + '"]'); if (b) b.classList.add(c); } }
  function shake(k) { var o = $("#opts"); if (o) { var b = o.querySelector('.opt[data-k="' + k + '"]'); if (b) b.classList.add("shake"); } }
  function xpPop(t) { var p = $("#xp-pop"); if (p) { p.textContent = t; p.classList.remove("go"); void p.offsetWidth; p.classList.add("go"); } }
  function feedback(ok, q) {
    var right = q.t === "input" ? q.a : q.options[q.a];
    var m = ok ? ["Boa! Certíssimo ⚡", "Continua assim!"] : ["Quase!", "Resposta certa: " + esc(right)];
    $("#lx-dock").innerHTML = '<div class="feedback ' + (ok ? "ok" : "no") + '"><div class="fb-row"><div class="fb-face"><img src="assets/img/roby-' + (ok ? "feliz" : "triste") + '.png" alt=""></div><div><div class="fb-t">' + m[0] + '</div><div class="fb-sub">' + m[1] + '</div></div></div><button class="sbtn ' + (ok ? "" : "sbtn--danger") + '" id="dock-btn">Continuar</button></div>';
    $("#dock-btn").onclick = next;
  }
  function next() { if (S.lives <= 0) { openLives(); return; } L.idx++; L.phase = "answer"; L.sel = null; if (L.idx >= L.qs.length) return done(); renderQuestion(); }
  function loseLife() { S.lives = Math.max(0, S.lives - 1); save(); var el = $("#lx-lives"); if (el) { el.textContent = "❤️ " + S.lives; el.classList.add("lost"); setTimeout(function () { el.classList.remove("lost"); }, 500); } }
  function done() {
    var acc = Math.round(L.ok / L.qs.length * 100);
    S.progress[keyOf(L)] = { done: true, acc: acc }; S.xp += XP_LEVEL; save();
    $("#screen-complete").innerHTML =
      '<div class="pad center grow complete" id="complete-inner">' +
        '<div class="roby-card grad"><img src="assets/img/roby-graduate.png" alt="Roby a celebrar" /></div>' +
        "<h1>Nível concluído!</h1><div class=\"sub\">" + esc(L.unit.titulo) + " · " + esc(L.nivel.titulo) + "</div>" +
        '<div class="stat-row"><div class="stat-card xp"><div class="v">+' + (L.ok * XP_OK + XP_LEVEL) + '</div><div class="l">XP ganho</div></div><div class="stat-card acc"><div class="v">' + acc + '%</div><div class="l">Acertos</div></div></div>' +
        '<div style="width:100%;max-width:340px"><button class="sbtn" id="c-next">Continuar</button></div>' +
      "</div>";
    $("#c-next").onclick = function () { renderMap(); show("screen-map"); };
    confetti($("#complete-inner")); show("screen-complete");
  }
  function confetti(host) { var cols = ["#e1ff51", "#2e8b57", "#4da378", "#ecc658", "#ffffff"]; for (var i = 0; i < 28; i++) { var c = document.createElement("i"); c.className = "confetti"; c.style.left = Math.random() * 100 + "%"; c.style.background = cols[i % cols.length]; c.style.animationDuration = (1.6 + Math.random() * 1.4) + "s"; c.style.animationDelay = (Math.random() * 0.5) + "s"; host.appendChild(c); void c.offsetWidth; c.classList.add("go"); } }

  /* ---- PERFIL ---- */
  function renderProfile() {
    var done = 0; C.cursos.forEach(function (cu) { cu.units.forEach(function (u) { u.niveis.forEach(function (n) { var k = cu.id + ":" + u.id + ":" + n.id; if (S.progress[k] && S.progress[k].done) done++; }); }); });
    var ini = (S.learner.nome || "S").trim().charAt(0).toUpperCase();
    var courses = C.cursos.map(function (cu) {
      var lines = cu.units.map(function (u) {
        var tot = u.niveis.length, d = u.niveis.filter(function (n) { var k = cu.id + ":" + u.id + ":" + n.id; return S.progress[k] && S.progress[k].done; }).length, pct = Math.round(d / tot * 100);
        return '<div class="prog-line"><span class="name">' + esc(u.titulo) + '</span><span class="bar"><i style="width:' + pct + '%"></i></span><span class="pct">' + pct + "%</span></div>";
      }).join("");
      return '<div class="card"><div class="k">' + esc(cu.disciplina) + '</div><h4>' + esc(cu.classe) + "</h4>" + lines + "</div>";
    }).join("");
    $("#screen-profile").innerHTML =
      '<div class="lesson-top" style="padding-bottom:0"><button class="lx-close" id="p-back">←</button><div class="lx-bar" style="visibility:hidden"></div></div>' +
      '<div class="grow scroll" style="padding:8px 22px 30px">' +
        '<div class="p-head"><div class="p-avatar">' + esc(ini) + '</div><div><div class="p-name">' + esc(S.learner.nome || "Estudante") + '</div><div class="p-sub">' + esc(S.learner.classe) + (S.learner.nivel ? " · " + esc(S.learner.nivel) : "") + "</div></div></div>" +
        '<div class="p-stats"><div class="p-stat"><div class="v" style="color:var(--chart)">' + S.xp + '</div><div class="l">XP</div></div><div class="p-stat"><div class="v" style="color:var(--gold)">' + S.streak + '</div><div class="l">Dias seguidos</div></div><div class="p-stat"><div class="v" style="color:var(--green-300)">' + done + '</div><div class="l">Níveis</div></div></div>' +
        courses +
        '<div class="card guardian"><div class="k">Para o encarregado</div><h4>Acompanhamento</h4><p style="color:var(--tx-soft);font-size:14px;line-height:1.5;margin:8px 0 0">' + esc((S.learner.nome || "O estudante").split(" ")[0]) + ' já ganhou <b style="color:var(--chart)">' + S.xp + " XP</b> e concluiu <b>" + done + "</b> níveis. " + (S.learner.encarregado ? "Resumo semanal para " + esc(S.learner.encarregado) + "." : "Adicione um contacto para receber o resumo semanal.") + "</p></div>" +
        '<button class="sbtn sbtn--ghost" id="p-reset" style="margin-top:8px">Recomeçar do zero</button>' +
      "</div>";
    $("#p-back").onclick = function () { renderMap(); show("screen-map"); };
    $("#p-reset").onclick = function () { if (confirm("Apagar todo o progresso?")) { localStorage.removeItem(KEY); S = load(); CURSO = C.cursos[0]; renderWelcome(); show("screen-welcome"); } };
  }

  /* ---- modal sem vidas ---- */
  function openLives() {
    var m = $("#modal-lives");
    m.innerHTML = '<div class="sheet"><div class="hearts">🖤🖤🖤🖤🖤</div><h3>Ficaste sem vidas</h3><p>As vidas voltam com o tempo. Vê um anúncio para as recuperar já, ou passa a Somara+.</p><div class="actions"><button class="sbtn" id="lv-ad">▶ Ver anúncio · +5 vidas</button><button class="sbtn sbtn--green" id="lv-buy">Somara+ · vidas ilimitadas</button><button class="link" id="lv-close">Agora não</button></div></div>';
    m.classList.add("open");
    $("#lv-ad").onclick = function () { toast("A ver anúncio…"); setTimeout(function () { S.lives = MAXLIVES; save(); closeLives(); toast("Vidas recuperadas! ❤️"); if ($("#screen-lesson").classList.contains("active")) renderTopbar(); }, 900); };
    $("#lv-buy").onclick = function () { toast("Somara+ chega em breve 💛"); };
    $("#lv-close").onclick = function () { closeLives(); if ($("#screen-lesson").classList.contains("active")) { renderMap(); show("screen-map"); } };
  }
  function closeLives() { $("#modal-lives").classList.remove("open"); }

  /* ---- arranque ---- */
  buildLevels();
  renderWelcome();
  if (S.onboarded) { renderMap(); show("screen-map"); } else show("screen-welcome");
})();
