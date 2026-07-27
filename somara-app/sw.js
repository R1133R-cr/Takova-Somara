/* SOMARA — service worker (offline / PWA)
   Cache-first para o app shell + assets. Fallback à rede e,
   se falhar tudo, ao index.html. Bump CACHE ao mudar assets. */
var CACHE = "somara-v1";
var ASSETS = [
  "./", "index.html", "manifest.webmanifest",
  "assets/css/somara.css",
  "assets/js/content.js", "assets/js/app.js",
  "assets/fonts/Melfira-Regular.ttf",
  "assets/img/roby-hero.png", "assets/img/roby-feliz.png", "assets/img/roby-triste.png",
  "assets/img/roby-graduate.png", "assets/img/somara-emblem.png",
  "assets/img/somara-icon-180.png", "assets/img/somara-icon-64.png"
];

self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(ASSETS); }).then(function () { return self.skipWaiting(); }));
});
self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (ks) {
    return Promise.all(ks.map(function (k) { if (k !== CACHE) return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});
self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET") return;
  e.respondWith(
    caches.match(req).then(function (hit) {
      return hit || fetch(req).then(function (res) {
        try {
          if (res && res.ok && new URL(req.url).origin === location.origin) {
            var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(req, copy); });
          }
        } catch (err) {}
        return res;
      }).catch(function () { return caches.match("index.html"); });
    })
  );
});
