/* ============================================================
   SOMARA — Configuração do Firebase (contas + sincronização)
   ⚙️ ÚNICO FICHEIRO A EDITAR para activar login e progresso
   sincronizado entre aparelhos (o "painel do encarregado" é,
   na prática, o próprio ecrã de Perfil — visível ao entrar com
   a mesma conta noutro telemóvel/PC).

   SEM isto preenchido, a app funciona exactamente como agora
   (progresso só no aparelho, sem contas) — nada parte.

   Como preencher (grátis, ~5 min):
   1. Vai a https://console.firebase.google.com → "Adicionar projecto"
      → dá-lhe um nome (ex.: "Somara") → cria.
   2. No menu esquerdo: Build → Authentication → "Get started"
      → aba "Sign-in method" → activa "Email/Password".
   3. No menu esquerdo: Build → Firestore Database → "Create database"
      → escolhe uma região perto (ex.: europe-west) → modo produção.
      Depois, no separador "Rules", cola isto e publica:

        rules_version = '2';
        service cloud.firestore {
          match /databases/{database}/documents {
            match /learners/{uid} {
              allow read, write: if request.auth != null && request.auth.uid == uid;
            }
          }
        }

      (Isto garante que cada conta só lê/escreve os SEUS dados.)
   4. No menu esquerdo: ⚙️ Project settings → em baixo "Your apps"
      → ícone "</>" (Web) → regista a app → copia o objecto
      `firebaseConfig` que aparece e cola-o aqui em baixo.

   Nota: o apiKey do Firebase NÃO é secreto — é normal e seguro
   ficar visível no código do lado do cliente. Quem protege os
   dados são as REGRAS do Firestore acima (passo 3), não isto.
   ============================================================ */
window.SOMARA_FIREBASE_CONFIG = {
  apiKey: "COLA_AQUI",
  authDomain: "COLA_AQUI",
  projectId: "COLA_AQUI",
  storageBucket: "COLA_AQUI",
  messagingSenderId: "COLA_AQUI",
  appId: "COLA_AQUI"
};
