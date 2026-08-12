import 'dart:async';
import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/content.dart';
import '../models/sequencia.dart';
import '../services/conteudo_remoto.dart';

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
  int lives = maxLives;
  Sequencia _sequencia = const Sequencia();
  String cursoId = '';

  /// chave "cursoId:unitId:nivelId" → percentagem de acertos
  final Map<String, int> progresso = {};

  /// Perguntas que a criança errou, guardadas para rever.
  ///
  /// É o conjunto de treino com mais valor que existe: exercitar o que já se
  /// sabe não ensina nada. Guarda-se o enunciado porque é o que identifica a
  /// pergunta mesmo que ela mude de nível numa actualização de conteúdo.
  final Set<String> erradas = {};

  void marcarErrada(String enunciado) {
    if (erradas.add(enunciado)) {
      notifyListeners();
      _gravar();
    }
  }

  /// Chamado quando a criança acerta a pergunta numa revisão: sai da lista.
  void marcarAprendida(String enunciado) {
    if (erradas.remove(enunciado)) {
      notifyListeners();
      _gravar();
    }
  }

  /// Todas as perguntas da classe actual, de todas as disciplinas.
  List<Questao> get _todasDaClasse => conteudo.cursos
      .where((c) => c.classe == classe)
      .expand((c) => c.units)
      .expand((u) => u.niveis)
      .expand((n) => n.questoes)
      .toList();

  /// As perguntas erradas que ainda existem no currículo.
  List<Questao> get paraRever =>
      _todasDaClasse.where((q) => erradas.contains(q.q)).toList();

  /// Perguntas dos níveis já concluídos, para treinar sem avançar no mapa.
  /// Sem níveis concluídos não há nada para treinar — e é assim que deve ser:
  /// treina-se o que já se aprendeu.
  List<Questao> perguntasDeTreino({int quantas = 10}) {
    final feitas = <Questao>[];
    for (final curso in conteudo.cursos.where((c) => c.classe == classe)) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          if (progresso.containsKey('${curso.id}:${u.id}:${n.id}')) {
            feitas.addAll(n.questoes);
          }
        }
      }
    }
    feitas.shuffle();
    return feitas.take(quantas).toList();
  }

  int get niveisConcluidos => progresso.length;

  int get niveisDaClasse => conteudo.cursos
      .where((c) => c.classe == classe)
      .expand((c) => c.units)
      .expand((u) => u.niveis)
      .length;

  /// Só as disciplinas da classe do aluno. Sem isto, um aluno da 1ª classe
  /// veria também os separadores da 2ª e podia entrar em exercícios que
  /// ainda não sabe fazer. Se a classe escolhida ainda não tiver conteúdo
  /// (3ª, por agora), mostra tudo em vez de deixar o ecrã vazio.
  List<Curso> get cursosVisiveis {
    final daClasse = conteudo.cursos.where((c) => c.classe == classe).toList();
    return daClasse.isEmpty ? conteudo.cursos : daClasse;
  }

  Curso get curso => cursosVisiveis.firstWhere(
        (c) => c.id == cursoId,
        orElse: () => cursosVisiveis.first,
      );

  List<({Unidade unit, Nivel nivel})> get niveis => curso.niveisEmSequencia;

  String chaveDe(Unidade u, Nivel n) => '${curso.id}:${u.id}:${n.id}';

  /// Dias seguidos de estudo. Conta níveis concluídos, não aberturas da app,
  /// como o roadmap pede. A contagem vive em [Sequencia], que é testada à
  /// parte com meses inteiros de calendário.
  int get streak => _sequencia.visivelEm(DateTime.now());

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

  /// Fica verdadeiro quando se descarregou conteúdo novo. Só entra em vigor
  /// na próxima abertura: trocar os níveis debaixo dos pés de quem está a
  /// jogar seria desconcertante.
  bool haConteudoNovo = false;

  Future<void> carregar() async {
    conteudo = await ConteudoRemoto.carregar();
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
        _sequencia = Sequencia.deJson(j['sequencia'] as Map<String, dynamic>?);
        lives = (j['lives'] ?? maxLives) as int;
        final savedCurso = j['cursoId'] as String?;
        if (savedCurso != null &&
            conteudo.cursos.any((c) => c.id == savedCurso)) {
          cursoId = savedCurso;
        }
        // A classe é lida acima; se a disciplina guardada não pertencer a
        // ela, cai na primeira da classe em vez de abrir um curso errado.
        if (!cursosVisiveis.any((c) => c.id == cursoId)) {
          cursoId = cursosVisiveis.first.id;
        }
        final p = (j['progresso'] as Map?) ?? {};
        p.forEach((k, v) => progresso['$k'] = v as int);
        erradas.addAll(((j['erradas'] as List?) ?? []).cast<String>());
        _diaDasVidas = j['diaDasVidas'] as String?;
      } catch (_) {
        // Estado corrompido: recomeça limpo em vez de rebentar o arranque.
      }
    }
    _reporVidasSeMudouODia();
    pronto = true;
    notifyListeners();

    // Só agora se vai à rede: a app já abriu e a criança já pode jogar.
    // Sem `await` de propósito — isto corre por trás e nunca atrasa nada.
    unawaited(_procurarConteudoNovo());
  }

  Future<void> _procurarConteudoNovo() async {
    final houve = await ConteudoRemoto.procurarActualizacao(conteudo.versao);
    if (houve) {
      haConteudoNovo = true;
      notifyListeners();
    }
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
        'sequencia': _sequencia.paraJson(),
        'lives': lives,
        'cursoId': cursoId,
        'progresso': progresso,
        'erradas': erradas.toList(),
        'diaDasVidas': _diaDasVidas,
      }),
    );
  }

  /// Muda a classe do aluno já com a app a correr.
  ///
  /// Antes só se podia mudar reinstalando: um irmão mais novo não conseguia
  /// sequer experimentar. O progresso de cada classe fica guardado à parte,
  /// porque a chave inclui o curso — voltar atrás não apaga nada.
  void mudarClasse(String novaClasse) {
    if (novaClasse == classe) return;
    classe = novaClasse;
    final daClasse = conteudo.cursos.where((c) => c.classe == classe);
    if (daClasse.isNotEmpty) cursoId = daClasse.first.id;
    notifyListeners();
    _gravar();
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
    // A disciplina guardada pode ser de outra classe (ex.: mudou de 1ª para
    // 2ª). Repõe na primeira disciplina da classe nova.
    if (!cursosVisiveis.any((c) => c.id == cursoId)) {
      cursoId = cursosVisiveis.first.id;
    }
    notifyListeners();
    _gravar();
  }

  /// Dia em que as vidas foram repostas pela última vez.
  String? _diaDasVidas;

  /// Repõe as vidas se o dia mudou.
  ///
  /// Sem isto o contador descia até zero e ficava lá para sempre, sem
  /// consequência nenhuma — um número no ecrã que não queria dizer nada.
  /// Repor todos os dias mantém a promessa (errar custa) sem trancar a
  /// criança fora da app, que seria o pior dos dois mundos numa app de
  /// escola.
  void _reporVidasSeMudouODia() {
    final hoje = Sequencia.iso(DateTime.now());
    if (_diaDasVidas == hoje) return;
    _diaDasVidas = hoje;
    lives = maxLives;
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
    _sequencia = _sequencia.comActividadeEm(DateTime.now());
    notifyListeners();
    _gravar();
  }

  void reporVidas() {
    lives = maxLives;
    notifyListeners();
    _gravar();
  }
}
