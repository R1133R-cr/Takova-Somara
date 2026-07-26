/* ============================================================
   TAKOVA — Camada de pirilampos bioluminescentes
   Pontos de luz quente (verde-dourado) que vagueiam sozinhos,
   piscam como pirilampos e são atraídos calmamente para o
   cursor (sem colar, mantendo distância). Canvas + rAF, mistura
   "lighter" no canvas e "screen" sobre a página (acende só no
   escuro). Leve e com bom desempenho. Respeita reduced-motion.
   ============================================================ */
(function () {
  "use strict";

  var mq = window.matchMedia;
  if (mq && mq("(prefers-reduced-motion: reduce)").matches) return; // acessibilidade: não anima

  var coarse = mq && mq("(pointer: coarse)").matches;
  var canvas, ctx, W = 0, H = 0, DPR = 1, raf = 0, last = 0;
  var sprites = [], flies = [];
  var pointer = { x: -9999, y: -9999, active: false };

  function rand(a, b) { return a + Math.random() * (b - a); }

  /* Sprite de brilho radial pré-renderizado (desenhado uma vez). */
  function makeSprite(stops) {
    var s = document.createElement("canvas"), size = 64;
    s.width = s.height = size;
    var c = s.getContext("2d");
    var g = c.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2);
    for (var i = 0; i < stops.length; i++) g.addColorStop(stops[i][0], stops[i][1]);
    c.fillStyle = g; c.fillRect(0, 0, size, size);
    return s;
  }

  function makeFly() {
    return {
      x: rand(0, W || 1200), y: rand(0, H || 800),
      vx: rand(-0.15, 0.15), vy: rand(-0.15, 0.15),
      ang: rand(0, Math.PI * 2),
      size: rand(0.7, 1.7),
      sprite: Math.random() < 0.5 ? 0 : 1,
      phase: rand(0, Math.PI * 2),
      blink: rand(0.5, 1.3)
    };
  }

  function targetCount() {
    var n = Math.round((W * H) / 52000);
    return Math.max(10, Math.min(coarse ? 16 : 26, n));
  }
  function adjust() {
    var t = targetCount();
    while (flies.length < t) flies.push(makeFly());
    if (flies.length > t) flies.length = t;
  }

  var resizeT;
  function onResize() { clearTimeout(resizeT); resizeT = setTimeout(resize, 150); }
  function resize() {
    var de = document.documentElement;
    W = de.clientWidth || window.innerWidth || 0;
    H = window.innerHeight || de.clientHeight || 0;
    if (W < 32) W = 1200;   // viewport ainda sem largura real (ex.: iframe colapsado) → usa um padrão sensato
    if (H < 32) H = 800;
    DPR = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.floor(W * DPR);
    canvas.height = Math.floor(H * DPR);
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    adjust();
  }

  function onMove(e) { pointer.x = e.clientX; pointer.y = e.clientY; pointer.active = true; }
  function onTouch(e) { if (e.touches && e.touches[0]) { pointer.x = e.touches[0].clientX; pointer.y = e.touches[0].clientY; pointer.active = true; } }

  var REACH = 240, STANDOFF = 78;
  function frame(t) {
    raf = requestAnimationFrame(frame);
    var dt = last ? Math.min((t - last) / 16.67, 2.2) : 1; last = t;
    ctx.clearRect(0, 0, W, H);
    ctx.globalCompositeOperation = "lighter";

    for (var i = 0; i < flies.length; i++) {
      var f = flies[i];

      /* vaguear: deriva suave de direcção */
      f.ang += (Math.random() - 0.5) * 0.3 * dt;
      f.vx += Math.cos(f.ang) * 0.02 * dt;
      f.vy += Math.sin(f.ang) * 0.02 * dt;

      /* atracção calma ao cursor, mantendo distância */
      if (pointer.active) {
        var dx = pointer.x - f.x, dy = pointer.y - f.y;
        var d = Math.sqrt(dx * dx + dy * dy);
        if (d < REACH && d > 0.001) {
          var nx = dx / d, ny = dy / d, force;
          if (d > STANDOFF) force = 0.045 * (1 - d / REACH);   /* puxa para perto */
          else force = -0.05 * (1 - d / STANDOFF);             /* afasta se colar */
          f.vx += nx * force * dt; f.vy += ny * force * dt;
        }
      }

      /* amortecimento + limite de velocidade (calmo) */
      f.vx *= 0.93; f.vy *= 0.93;
      var sp = Math.sqrt(f.vx * f.vx + f.vy * f.vy);
      var max = pointer.active ? 1.3 : 0.7;
      if (sp > max) { f.vx = f.vx / sp * max; f.vy = f.vy / sp * max; }
      f.x += f.vx * dt; f.y += f.vy * dt;

      /* envolve nas margens */
      if (f.x < -40) f.x = W + 40; else if (f.x > W + 40) f.x = -40;
      if (f.y < -40) f.y = H + 40; else if (f.y > H + 40) f.y = -40;

      /* piscar: maioritariamente fraco, com picos curtos */
      f.phase += 0.03 * f.blink * dt;
      var s = Math.sin(f.phase);
      var b = 0.12 + 0.88 * (s > 0 ? s * s * s : 0);

      var spr = sprites[f.sprite];
      var glow = 7 + f.size * 15;
      ctx.globalAlpha = b * 0.85;
      ctx.drawImage(spr, f.x - glow, f.y - glow, glow * 2, glow * 2);
      var cr = f.size * 2.4;
      ctx.globalAlpha = Math.min(1, b * 1.25);
      ctx.drawImage(spr, f.x - cr, f.y - cr, cr * 2, cr * 2);
    }
    ctx.globalAlpha = 1;
  }

  function start() { if (!raf) { last = 0; raf = requestAnimationFrame(frame); } }
  function stop() { if (raf) { cancelAnimationFrame(raf); raf = 0; } }

  function init() {
    canvas = document.createElement("canvas");
    canvas.setAttribute("aria-hidden", "true");
    var st = canvas.style;
    st.position = "fixed"; st.inset = "0"; st.width = "100%"; st.height = "100%";
    st.pointerEvents = "none"; st.zIndex = "40"; st.mixBlendMode = "screen";
    document.body.appendChild(canvas);
    ctx = canvas.getContext("2d");

    sprites = [
      makeSprite([[0, "rgba(255,246,210,1)"], [0.22, "rgba(228,205,120,0.5)"], [0.55, "rgba(150,190,90,0.16)"], [1, "rgba(0,0,0,0)"]]),
      makeSprite([[0, "rgba(240,255,212,1)"], [0.22, "rgba(170,215,110,0.5)"], [0.55, "rgba(110,165,80,0.15)"], [1, "rgba(0,0,0,0)"]])
    ];

    resize();
    window.addEventListener("resize", onResize, { passive: true });
    window.addEventListener("mousemove", onMove, { passive: true });
    window.addEventListener("touchmove", onTouch, { passive: true });
    window.addEventListener("mouseout", function (e) { if (!e.relatedTarget) pointer.active = false; }, { passive: true });
    window.addEventListener("blur", function () { pointer.active = false; });
    document.addEventListener("visibilitychange", function () { if (document.hidden) stop(); else start(); });
    window.addEventListener("load", resize);
    if (window.ResizeObserver) { try { new ResizeObserver(onResize).observe(document.documentElement); } catch (e) {} }
    start();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
