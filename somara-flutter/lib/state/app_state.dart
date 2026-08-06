import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/content.dart';

/// Estado do aluno — o equivalente ao localStorage `somara_state_v2` da
/// versão web, mas tipado e persistido com shared_preferences.
class AppState extends ChangeNotifier {
  static const _key = 'somara_state_v1';
  static const maxLives = 5;
  static const xpPorAcerto = 10;
  static const xpPorNivel = 20;

  late Conteudo conteudo;
  bool pronto = false;

  String nome = '';
  String classe = '1ª classe';
  bool onboarded = false;
  int xp = 0;
  int streak = 1;
  int lives = maxLives;
  String cursoId = '';

  /// chave "cursoId:unitId:nivelId" → percentagem de acertos
  final Map<String, int> progresso = {};

  Curso get curso =>
      conteudo.cursos.firstWhere((c) => c.id == cursoId, orElse: () => conteudo.cursos.first);

  List<({Unidade unit, Nivel nivel})> get niveis => curso.niveisEmSequencia;

  String chaveDe(Unidade u, Nivel n) => '${curso.id}:${u.id}:${n.id}';

  bool nivelFeito(int i) {
    final lv = niveis[i];
    return progresso.containsKey(chaveDe(lv.unit, lv.nivel));
  }

  /// Índice do primeiro nível por fazer — é onde o Roby está pousado.
  int get nivelActual {
    for (var i = 0; i < niveis.length; i++) {
      if (!nivelFeito(i)) return i;
    }
    return niveis.length - 1; // curso todo feito: fica no último
  }

  Future<void> carregar() async {
    conteudo = await Conteudo.carregar();
    cursoId = conteudo.cursos.first.id;

    final prefs = await SharedPreferences.getInstance();
    final raw = prefs.getString(_key);
    if (raw != null) {
      try {
        final j = json.decode(raw) as Map<String, dynamic>;
        nome = (j['nome'] ?? '') as String;
        classe = (j['classe'] ?? '1ª classe') as String;
        onboarded = (j['onboarded'] ?? false) as bool;
        xp = (j['xp'] ?? 0) as int;
        streak = (j['streak'] ?? 1) as int;
        lives = (j['lives'] ?? maxLives) as int;
        final savedCurso = j['cursoId'] as String?;
        if (savedCurso != null &&
            conteudo.cursos.any((c) => c.id == savedCurso)) {
          cursoId = savedCurso;
        }
        final p = (j['progresso'] as Map?) ?? {};
        p.forEach((k, v) => progresso['$k'] = v as int);
      } catch (_) {
        // Estado corrompido: recomeça limpo em vez de rebentar o arranque.
      }
    }
    pronto = true;
    notifyListeners();
  }

  Future<void> _gravar() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(
      _key,
      json.encode({
        'nome': nome,
        'classe': classe,
        'onboarded': onboarded,
        'xp': xp,
        'streak': streak,
        'lives': lives,
        'cursoId': cursoId,
        'progresso': progresso,
      }),
    );
  }

  void trocarCurso(String id) {
    cursoId = id;
    notifyListeners();
    _gravar();
  }

  void concluirOnboarding(String nomeAluno, String classeAluno) {
    nome = nomeAluno;
    classe = classeAluno;
    onboarded = true;
    notifyListeners();
    _gravar();
  }

  void perderVida() {
    if (lives > 0) lives--;
    notifyListeners();
    _gravar();
  }

  void concluirNivel(int i, int acertos, int total) {
    final lv = niveis[i];
    final pct = total == 0 ? 0 : (acertos * 100 / total).round();
    progresso[chaveDe(lv.unit, lv.nivel)] = pct;
    xp += acertos * xpPorAcerto + xpPorNivel;
    notifyListeners();
    _gravar();
  }

  void reporVidas() {
    lives = maxLives;
    notifyListeners();
    _gravar();
  }
}
