import 'package:firebase_core/firebase_core.dart';

/// O ÚNICO ficheiro a editar para ligar as contas e o progresso na nuvem.
///
/// Enquanto estiver por preencher, a app funciona exactamente como sempre
/// funcionou: tudo local, sem contas, sem rede. Isso não é um modo degradado
/// — é o modo normal em Lichinga, e continua a ser o que uma criança sem
/// dados móveis usa todos os dias.
///
/// ---------------------------------------------------------------------
/// Como preencher (grátis nesta escala, uns cinco minutos)
/// ---------------------------------------------------------------------
/// 1. https://console.firebase.google.com → "Adicionar projecto" → nome
///    "Somara" → criar. Podes recusar o Google Analytics: a medição desta
///    app não usa esse SDK (ver [Nuvem], os contadores vão no próprio
///    documento do aluno).
///
/// 2. Build → Authentication → "Get started" → separador "Sign-in method"
///    → activar "Email/Password".
///
/// 3. Build → Firestore Database → "Create database" → região
///    `europe-west` (é a mais perto de Moçambique com preço baixo) → modo
///    de produção. Depois, no separador "Rules", colar o conteúdo de
///    `firestore.rules` (está na raiz de somara-flutter/) e publicar.
///    Sem esse passo os dados ficam abertos a qualquer pessoa.
///
/// 4. ⚙️ Project settings → "Your apps" → ícone do Android → nome do
///    pacote **mz.co.takova.somara** → registar → descarregar o
///    `google-services.json`.
///
/// 5. Abrir esse ficheiro num editor de texto e copiar para aqui em baixo:
///
///      projectId          ← project_info.project_id
///      messagingSenderId  ← project_info.project_number
///      storageBucket      ← project_info.storage_bucket
///      appId              ← client[0].client_info.mobilesdk_app_id
///      apiKey             ← client[0].api_key[0].current_key
///
///    O `google-services.json` em si não é preciso para nada: a app não
///    usa o plugin de Gradle da Google de propósito, porque esse plugin
///    faz a compilação falhar quando o ficheiro não existe — e isso
///    tirava-nos a garantia de que a app compila e corre sem Firebase
///    nenhum.
///
/// A apiKey do Firebase **não é um segredo**. É normal e seguro ela ficar
/// visível no código do cliente; quem protege os dados são as regras do
/// Firestore do passo 3, não esta chave.
class FirebaseConfig {
  static const _porPreencher = 'COLA_AQUI';

  static const apiKey = 'AIzaSyBTNIWHZ-zB986JZ_7YFKPSvcgymytKItk';
  static const appId = '1:508333957634:android:1e737996ef2ffdd0cbbd1b';
  static const messagingSenderId = '508333957634';
  static const projectId = 'somara-1133';
  static const storageBucket = 'somara-1133.firebasestorage.app';

  /// Verdadeiro quando os campos essenciais já lá estão.
  ///
  /// Só se olha para estes três: sem eles não há ligação possível, e o
  /// storageBucket nem sequer é usado (não guardamos ficheiros).
  static bool get configurado =>
      apiKey != _porPreencher &&
      appId != _porPreencher &&
      projectId != _porPreencher;

  static FirebaseOptions get opcoes => const FirebaseOptions(
    apiKey: apiKey,
    appId: appId,
    messagingSenderId: messagingSenderId,
    projectId: projectId,
    storageBucket: storageBucket,
  );
}
