/* ============================================================
   TAKOVA — site institucional · interacções
   ============================================================ */
(function () {
  "use strict";

  /* ----------------------------------------------------------
     ⚙️  DADOS DE CONTACTO — ÚNICO SÍTIO A EDITAR
     Mete aqui os dados reais da Takova. Tudo o resto do site
     (botões de WhatsApp, rodapé, página de contacto) actualiza
     automaticamente a partir daqui.
     ---------------------------------------------------------- */
  const TAKOVA = {
    whatsapp:      "258840000000",                 // só dígitos, com indicativo 258 (ex.: 25884XXXXXXX)
    whatsappLabel: "+258 84 000 0000",             // como aparece no ecrã
    facebookUrl:   "https://www.facebook.com/TakovaLichinga",
    facebookLabel: "/TakovaLichinga",
    email:         "geral@takova.co.mz",
    location:      "Lichinga, Niassa — Moçambique",
  };

  const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const $  = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.prototype.slice.call((c || document).querySelectorAll(s));

  function waLink(text) {
    const base = "https://wa.me/" + TAKOVA.whatsapp;
    return text ? base + "?text=" + encodeURIComponent(text) : base;
  }

  /* ---- 1 · Preencher dados de contacto em todo o site ---- */
  function hydrateContact() {
    $$("[data-wa]").forEach((a) => {
      a.setAttribute("href", waLink(a.getAttribute("data-wa-text") || "Olá Takova! Gostaria de saber mais sobre os vossos serviços."));
      a.setAttribute("target", "_blank");
      a.setAttribute("rel", "noopener");
    });
    $$(".js-wa-label").forEach((e) => (e.textContent = TAKOVA.whatsappLabel));
    $$(".js-fb").forEach((a) => { a.setAttribute("href", TAKOVA.facebookUrl); a.setAttribute("target", "_blank"); a.setAttribute("rel", "noopener"); });
    $$(".js-fb-label").forEach((e) => (e.textContent = TAKOVA.facebookLabel));
    $$(".js-email").forEach((a) => a.setAttribute("href", "mailto:" + TAKOVA.email));
    $$(".js-email-label").forEach((e) => (e.textContent = TAKOVA.email));
    $$(".js-location").forEach((e) => (e.textContent = TAKOVA.location));
    $$(".js-year").forEach((e) => (e.textContent = new Date().getFullYear()));
  }

  /* ---- 2 · Navegação mobile ---- */
  function initNav() {
    const nav = $(".tk-nav");
    if (!nav) return;
    const toggle = $(".tk-nav-toggle", nav);
    const useEl = toggle ? $(".ic use", toggle) : null;

    function setOpen(open) {
      nav.classList.toggle("menu-open", open);
      if (toggle) {
        toggle.setAttribute("aria-expanded", String(open));
        toggle.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
        if (useEl) useEl.setAttribute("href", "#" + (open ? "i-x" : "i-menu"));
      }
    }
    if (toggle) toggle.addEventListener("click", () => setOpen(!nav.classList.contains("menu-open")));
    $$(".tk-links a", nav).forEach((a) => a.addEventListener("click", () => setOpen(false)));
    window.addEventListener("resize", () => { if (window.innerWidth > 860) setOpen(false); });

    // sombra ao fazer scroll
    const onScroll = () => nav.classList.toggle("scrolled", window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---- 3 · Link activo na navegação ---- */
  function initActiveLink() {
    let page = location.pathname.split("/").pop();
    if (!page) page = "index.html";
    $$(".tk-navlink").forEach((a) => {
      const href = a.getAttribute("href");
      if (href === page || (page === "index.html" && (href === "./" || href === "index.html"))) {
        a.setAttribute("aria-current", "page");
      }
    });
  }

  /* ---- 4 · Revelar ao fazer scroll ---- */
  function initReveal() {
    const els = $$(".reveal");
    if (prefersReduced || !("IntersectionObserver" in window)) {
      els.forEach((e) => e.classList.add("is-visible"));
      return;
    }
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add("is-visible"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    els.forEach((e) => io.observe(e));
  }

  /* ---- 5 · Contadores animados ---- */
  function animateCount(el) {
    const to = parseFloat(el.getAttribute("data-to")) || 0;
    const prefix = el.getAttribute("data-prefix") || "";
    const suffix = el.getAttribute("data-suffix") || "";
    if (prefersReduced) { el.textContent = prefix + to + suffix; return; }
    const dur = 1400, start = performance.now();
    function tick(now) {
      const p = Math.min((now - start) / dur, 1);
      const eased = 1 - Math.pow(1 - p, 3); // easeOutCubic
      el.textContent = prefix + Math.round(to * eased) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  function initCounters() {
    const els = $$(".js-count");
    if (!els.length) return;
    if (!("IntersectionObserver" in window)) { els.forEach(animateCount); return; }
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => { if (en.isIntersecting) { animateCount(en.target); io.unobserve(en.target); } });
    }, { threshold: 0.5 });
    els.forEach((e) => io.observe(e));
  }

  /* ---- 6 · Formulário de contacto → WhatsApp ---- */
  function initContactForm() {
    const form = $("#tk-contact-form");
    if (!form) return;
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const nome = (form.nome.value || "").trim();
      const contacto = (form.contacto.value || "").trim();
      const msg = (form.mensagem.value || "").trim();
      const text =
        "Olá Takova! 👋\n\n" +
        "*Nome:* " + (nome || "—") + "\n" +
        "*Contacto:* " + (contacto || "—") + "\n" +
        "*Preciso de:* " + (msg || "—");
      window.open(waLink(text), "_blank", "noopener");

      const card = form.closest(".tk-form-card") || form.parentNode;
      card.innerHTML =
        '<div class="tk-form-success">' +
          '<div class="ok"><svg class="ic"><use href="#i-check"></use></svg></div>' +
          '<h3>A abrir o WhatsApp…</h3>' +
          '<p>Se a janela não abrir, fale connosco directamente pelo botão de WhatsApp. Respondemos no mesmo dia útil.</p>' +
        '</div>';
    });
  }

  /* ---- 7 · Sincronizar dados estruturados (JSON-LD) com o contacto ---- */
  function updateJsonLd() {
    const el = $('script[type="application/ld+json"]');
    if (!el) return;
    try {
      const d = JSON.parse(el.textContent);
      d.telephone = "+" + TAKOVA.whatsapp;
      d.email = TAKOVA.email;
      d.sameAs = [TAKOVA.facebookUrl];
      el.textContent = JSON.stringify(d);
    } catch (e) { /* JSON-LD ausente ou inválido — ignora */ }
  }

  /* ---- Arranque ---- */
  function init() {
    hydrateContact();
    updateJsonLd();
    initNav();
    initActiveLink();
    initReveal();
    initCounters();
    initContactForm();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();

