/* ============================================================
   SOMARA — Cloud (Firebase): contas + sincronização de progresso
   Só fica activo se firebase-config.js tiver uma configuração
   real (ver instruções nesse ficheiro). Caso contrário devolve
   um stub inofensivo — a app continua 100% funcional apenas
   com localStorage, como antes.
   ============================================================ */
window.SOMARA_CLOUD = (function () {
  function stub(reason) {
    return {
      available: false,
      reason: reason || "não configurado",
      onChange: function () {},
      signUp: function () { return Promise.reject(new Error("Contas na nuvem não estão configuradas.")); },
      signIn: function () { return Promise.reject(new Error("Contas na nuvem não estão configuradas.")); },
      signOutUser: function () { return Promise.resolve(); },
      pushState: function () {},
      pullState: function () { return Promise.resolve(null); },
      currentUser: function () { return null; }
    };
  }

  try {
    var cfg = window.SOMARA_FIREBASE_CONFIG || {};
    var configured = !!(cfg.apiKey && cfg.apiKey.indexOf("COLA_AQUI") === -1 && cfg.projectId && cfg.projectId.indexOf("COLA_AQUI") === -1);
    if (!configured) return stub("config por preencher");
    if (typeof firebase === "undefined") return stub("SDK do Firebase não carregou (sem rede?)");

    firebase.initializeApp(cfg);
    var auth = firebase.auth();
    var db = firebase.firestore();
    var pushTimer = null;

    function docFor(uid) { return db.collection("learners").doc(uid); }
    function signUp(email, pass) { return auth.createUserWithEmailAndPassword(email, pass); }
    function signIn(email, pass) { return auth.signInWithEmailAndPassword(email, pass); }
    function signOutUser() { return auth.signOut(); }
    function currentUser() { return auth.currentUser; }
    function onChange(cb) { auth.onAuthStateChanged(cb); }

    /* Escrita com debounce (evita gravar a cada tecla) */
    function pushState(state) {
      var u = auth.currentUser; if (!u) return;
      clearTimeout(pushTimer);
      pushTimer = setTimeout(function () {
        var payload = Object.assign({}, state, { updatedAt: firebase.firestore.FieldValue.serverTimestamp() });
        docFor(u.uid).set(payload, { merge: true }).catch(function () { /* falha silenciosa: fica só local, tenta na próxima */ });
      }, 1200);
    }
    function pullState() {
      var u = auth.currentUser; if (!u) return Promise.resolve(null);
      return docFor(u.uid).get().then(function (snap) { return snap.exists ? snap.data() : null; }).catch(function () { return null; });
    }

    return { available: true, onChange: onChange, signUp: signUp, signIn: signIn, signOutUser: signOutUser, pushState: pushState, pullState: pullState, currentUser: currentUser };
  } catch (e) {
    return stub("erro ao iniciar (" + (e && e.message) + ")");
  }
})();
