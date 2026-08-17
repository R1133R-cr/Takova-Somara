import 'dart:async';
import 'dart:convert';

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

import 'firebase_config.dart';

/// Contas e progresso guardado fora do telemóvel.
///
/// O que isto resolve: uma criança que muda de telemóvel — ou a quem
/// reinstalam a app — perdia meses de trabalho. Em Lichinga um telemóvel
/// passa de mão em mão e formata-se com frequência, e o progresso era a
/// única coisa que não sobrevivia a isso.
///
/// Três regras que não se negoceiam:
///
/// 1. **Sem configuração, a app é a de sempre.** Isto fica inerte e nada
///    parte. Não é um modo degradado: é o modo normal de quem não tem
///    dados móveis, e continua a ser a maioria.
///
/// 2. **A nuvem nunca manda.** Ao entrar, o progresso da nuvem funde-se com
///    o local ficando sempre com o melhor dos dois. Uma sincronização que
///    substituísse o local apagava a tarde de trabalho de quem esteve a
///    jogar offline — que é exactamente o problema que viemos resolver.
///
/// 3. **Falhar é normal e é silencioso.** Rede fraca não pode interromper
///    uma lição. O que não subiu fica em fila e sobe da próxima vez; o
///    Firestore já faz isso sozinho quando está offline.
class Nuvem {
  Nuvem._();
  static final Nuvem i = Nuvem._();

  FirebaseAuth? _auth;
  FirebaseFirestore? _db;
  Timer? _atraso;

  /// O último conteúdo que subiu, para não voltar a subir igual.
  String? _ultimoEnviado;

  /// Verdadeiro quando o Firebase arrancou e há com quem falar.
  bool get disponivel => _auth != null;

  User? get utilizador => _auth?.currentUser;
  bool get temSessao => utilizador != null;
  String? get email => utilizador?.email;

  /// Arranca o Firebase, se estiver configurado.
  ///
  /// Devolve sem fazer nada — e sem se queixar — quando não está. É o
  /// caminho normal enquanto a consola não estiver preenchida.
  Future<void> arrancar() async {
    if (!FirebaseConfig.configurado) return;
    try {
      await Firebase.initializeApp(options: FirebaseConfig.opcoes);
      _auth = FirebaseAuth.instance;
      _db = FirebaseFirestore.instance;
    } catch (e) {
      // Uma app de escola não pode deixar de abrir porque o Firebase não
      // arrancou. Fica local e pronto.
      debugPrint('nuvem: não arrancou ($e)');
      _auth = null;
      _db = null;
    }
  }

  DocumentReference<Map<String, dynamic>>? get _doc {
    final u = utilizador;
    if (u == null) return null;
    return _db?.collection('learners').doc(u.uid);
  }

  /// Mensagens em português para quem está a criar a conta — normalmente o
  /// pai ou o professor, não a criança. Os códigos do Firebase vêm em
  /// inglês e não dizem nada a ninguém.
  static String explicar(Object erro) {
    if (erro is! FirebaseAuthException) {
      return 'Não foi possível ligar. Verifica a internet e tenta outra vez.';
    }
    return switch (erro.code) {
      'invalid-email' => 'Esse email não parece estar certo.',
      'email-already-in-use' => 'Já existe uma conta com esse email. Tenta entrar.',
      'weak-password' => 'A palavra-passe é curta. Usa pelo menos 6 letras ou números.',
      'user-not-found' || 'wrong-password' || 'invalid-credential' =>
        'Email ou palavra-passe errados.',
      'network-request-failed' =>
        'Sem internet. O progresso continua guardado no telemóvel.',
      'too-many-requests' => 'Muitas tentativas seguidas. Espera um bocado.',
      _ => 'Não deu para continuar (${erro.code}).',
    };
  }

  Future<UserCredential> criarConta(String email, String palavra) async {
    final a = _auth;
    if (a == null) throw StateError('nuvem não configurada');
    return a.createUserWithEmailAndPassword(
      email: email.trim(),
      password: palavra,
    );
  }

  Future<UserCredential> entrar(String email, String palavra) async {
    final a = _auth;
    if (a == null) throw StateError('nuvem não configurada');
    return a.signInWithEmailAndPassword(
      email: email.trim(),
      password: palavra,
    );
  }

  Future<void> sair() async {
    _atraso?.cancel();
    // Sem isto, entrar noutra conta a seguir podia não gravar nada: a
    // assinatura do estado anterior ainda cá estaria e a escrita seria
    // saltada por parecer repetida.
    _ultimoEnviado = null;
    await _auth?.signOut();
  }

  /// Lê o que está na nuvem. Devolve nulo se não houver nada — conta nova.
  Future<Map<String, dynamic>?> puxar() async {
    try {
      final d = _doc;
      if (d == null) return null;
      final snap = await d.get();
      return snap.exists ? snap.data() : null;
    } catch (e) {
      debugPrint('nuvem: leitura falhou ($e)');
      return null;
    }
  }

  /// Grava, com atraso.
  ///
  /// Sem o atraso, terminar uma lição de dez perguntas dava dez escritas
  /// seguidas. Com rede fraca isso é lento e caro para quem paga os dados
  /// ao megabyte.
  void empurrar(Map<String, dynamic> estado) {
    final d = _doc;
    if (d == null) return;

    // O estado grava-se no telemóvel a cada mudança, incluindo as que não
    // viajam — perder uma vida, ligar o som. Sem esta comparação, cada uma
    // dessas mandava uma escrita idêntica à anterior, e quem paga os dados
    // ao megabyte pagava-as todas.
    final assinatura = jsonEncode(estado);
    if (assinatura == _ultimoEnviado) return;

    _atraso?.cancel();
    _atraso = Timer(const Duration(milliseconds: 1200), () async {
      try {
        await d.set({
          ...estado,
          'actualizadoEm': FieldValue.serverTimestamp(),
        }, SetOptions(merge: true));
        _ultimoEnviado = assinatura;
      } catch (e) {
        // Não marca como enviado: fica para a próxima tentativa.
        debugPrint('nuvem: escrita falhou ($e)');
      }
    });
  }

  /// Grava já, sem esperar pelo atraso. Para o momento de entrar, em que se
  /// quer a fusão no servidor antes de qualquer outra coisa.
  Future<void> empurrarJa(Map<String, dynamic> estado) async {
    try {
      _atraso?.cancel();
      await _doc?.set({
        ...estado,
        'actualizadoEm': FieldValue.serverTimestamp(),
      }, SetOptions(merge: true));
    } catch (e) {
      debugPrint('nuvem: escrita imediata falhou ($e)');
    }
  }

  /* ---------------- Medição mínima ----------------
     Quantos abriram, quantos terminaram uma lição, quantos voltaram. Só
     isto.

     De propósito sem o SDK de analítica da Google: pesaria mais no APK e
     recolheria identificadores de publicidade e sinais do aparelho sobre
     crianças do ensino primário, para responder a três perguntas que três
     contadores respondem. Estes números ficam no documento do próprio
     aluno, debaixo das mesmas regras que o resto — e vêem-se na consola.

     "Quantos voltaram" sai de [diasActivos]: a lista de dias distintos em
     que a app foi aberta. Uma criança que só abriu no primeiro dia tem um
     dia; quem voltou tem mais. */

  Future<void> contarAbertura(String hojeIso) async {
    try {
      await _doc?.set({
        'aberturas': FieldValue.increment(1),
        'diasActivos': FieldValue.arrayUnion([hojeIso]),
        'ultimaVez': FieldValue.serverTimestamp(),
      }, SetOptions(merge: true));
    } catch (e) {
      debugPrint('nuvem: contador de abertura falhou ($e)');
    }
  }

  Future<void> contarLicao() async {
    try {
      await _doc?.set({
        'licoesTerminadas': FieldValue.increment(1),
      }, SetOptions(merge: true));
    } catch (e) {
      debugPrint('nuvem: contador de lições falhou ($e)');
    }
  }
}
