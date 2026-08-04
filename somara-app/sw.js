/* SOMARA — service worker (offline / PWA)
   Estratégia mista:
   - App shell (HTML/JS/CSS/manifest) — muda com actualizações —
     usa NETWORK-FIRST: online, vai sempre buscar a versão mais
     recente (e actualiza a cache); só usa a cache se estiver
     offline. Sem isto, um utilizador que já tenha a app instalada
     ficaria preso na versão antiga para sempre (cache-first nunca
     revalida). Ficheiros pesados que nunca mudam (fontes, imagens
     do Roby) continuam CACHE-FIRST — mais rápido, sem desperdiçar
     rede a repetir o que já se sabe que não muda.
   Bump CACHE só é necessário se ASSETS mudar de lista. */
var CACHE = "somara-v3";
var APP_SHELL = [
  "./", "index.html", "manifest.webmanifest",
  "assets/css/somara.css",
  "assets/js/content.js", "assets/js/app.js",
  "assets/js/firebase-config.js", "assets/js/cloud.js"
];
var STATIC_ASSETS = [
  "assets/fonts/Melfira-Regular.ttf",
  "assets/img/roby-hero.png", "assets/img/roby-feliz.png", "assets/img/roby-triste.png",
  "assets/img/roby-confiante.png", "assets/img/roby-graduate.png",
  "assets/img/somara-icon-64.png", "assets/img/somara-icon-180.png",
  "assets/img/somara-icon-192.png", "assets/img/somara-icon-512.png", "assets/img/somara-icon-512-maskable.png"
];

self.addEventListener("install", function (e) {
  e.waitUntil(
    caches.open(CACHE)
      .then(function (c) { return c.addAll(APP_SHELL.concat(STATIC_ASSETS)); })
      .then(function () { return self.skipWaiting(); })
  );
});
self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (ks) {
    return Promise.all(ks.map(function (k) { if (k !== CACHE) return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

function isAppShell(url) {
  var path = url.pathname.replace(/^.*\/somara-app\//, "");
  return APP_SHELL.some(function (a) { return path === a || path === a.replace("./", "") || url.pathname.endsWith("/" + a); }) || path === "" || path === "/";
}

self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET") return;
  var url = new URL(req.url);
  if (url.origin !== location.origin) return; /* CDNs (fontes Google, Firebase): deixa ir direito à rede */

  if (isAppShell(url) || req.mode === "navigate") {
    /* network-first: sempre a versão mais recente quando há rede */
    e.respondWith(
      fetch(req).then(function (res) {
        if (res && res.ok) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(req, copy); }); }
        return res;
      }).catch(function () { return caches.match(req).then(function (hit) { return hit || caches.match("index.html"); }); })
    );
    return;
  }

  /* cache-first: assets estáticos que nunca mudam */
  e.respondWith(
    caches.match(req).then(function (hit) {
      return hit || fetch(req).then(function (res) {
        if (res && res.ok) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(req, copy); }); }
        return res;
      });
    })
  );
});
