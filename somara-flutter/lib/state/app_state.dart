import 'dart:async';
import 'dart:convert';
import 'dart:math' as math;
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/content.dart';
import '../models/sequencia.dart';
import '../services/conteudo_remoto.dart';
import '../services/nuvem.dart';
import '../services/sons.dart';

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

  /// Som ligado. Fica no estado e não só no serviço porque tem de sobreviver
  /// a fechar a app — e porque num telemóvel partilhado com a família há
  /// alturas em que se quer a app calada e ninguém a quer desligar duas vezes.
  bool som = true;

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
  ///
  /// Uma por enunciado. O mesmo enunciado pode estar em mais do que um nível
  /// (a SADC, por exemplo, é perguntada em dois sítios da 6ª classe), e sem
  /// esta filtragem a lista mostrava a mesma pergunta duas vezes e o
  /// contador dizia 7 quando só havia 6 erros.
  List<Questao> get paraRever {
    final vistas = <String>{};
    return [
      for (final q in _todasDaClasse)
        if (erradas.contains(q.q) && vistas.add(q.q)) q,
    ];
  }

  /// Perguntas dos níveis já concluídos, para treinar sem avançar no mapa.
  /// Sem níveis concluídos não há nada para treinar — e é assim que deve ser:
  /// treina-se o que já se aprendeu.
  List<Questao> perguntasDeTreino({int quantas = 10}) {
    // Uma por enunciado, pela mesma razão que em [paraRever]: apanhar a mesma
    // pergunta duas vezes num treino de dez faz o treino parecer avariado.
    final vistas = <String>{};
    final feitas = <Questao>[];
    for (final curso in conteudo.cursos.where((c) => c.classe == classe)) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          if (progresso.containsKey('${curso.id}:${u.id}:${n.id}')) {
            for (final q in n.questoes) {
              if (vistas.add(q.q)) feitas.add(q);
            }
          }
        }
      }
    }
    feitas.shuffle();
    return feitas.take(quantas).toList();
  }

  /// Níveis concluídos **na classe actual**.
  ///
  /// Conta só a classe porque é sempre comparado com [niveisDaClasse]. A
  /// contagem crua de `progresso` inclui as outras classes, e quem trocasse
  /// da 1ª para a 6ª via "6ª classe · 100% concluída" sem lá ter feito nada.
  int get niveisConcluidos {
    var n = 0;
    for (final c in conteudo.cursos.where((c) => c.classe == classe)) {
      for (final u in c.units) {
        for (final nv in u.niveis) {
          if (progresso.containsKey('${c.id}:${u.id}:${nv.id}')) n++;
        }
      }
    }
    return n;
  }

  /// Tudo o que já se fez, em todas as classes. É o número do Perfil: o
  /// trabalho de um irmão mais velho não desaparece por o mais novo entrar.
  int get niveisConcluidosTotal => progresso.length;

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
        som = (j['som'] ?? true) as bool;
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
        _vezesSemVidas = (j['vezesSemVidas'] ?? 0) as int;
        final ate = j['bloqueadoAte'] as String?;
        _bloqueadoAte = ate == null ? null : DateTime.tryParse(ate);
      } catch (_) {
        // Estado corrompido: recomeça limpo em vez de rebentar o arranque.
      }
    }
    _reporVidasSeMudouODia();
    verificarFimDoBloqueio();
    pronto = true;
    notifyListeners();

    // A trilha só arranca depois de o estado estar lido: quem tinha o som
    // desligado não pode ouvir dois segundos de música antes de a app se
    // lembrar disso.
    await Sons.i.definirLigado(som);
    unawaited(Sons.i.emPrimeiroPlano());

    // Só agora se vai à rede: a app já abriu e a criança já pode jogar.
    // Sem `await` de propósito — isto corre por trás e nunca atrasa nada.
    unawaited(_procurarConteudoNovo());
    unawaited(_retomarSessaoDaNuvem());
  }

  /// Se a sessão da conta ainda estiver aberta, traz o que houver de novo.
  ///
  /// Corre por trás, depois de a app já estar a jogar. A criança não pode
  /// ficar à espera de uma rede fraca para abrir a amarelinha — e se a rede
  /// não responder, fica com o que tem no telemóvel, que é tudo o que
  /// precisa.
  Future<void> _retomarSessaoDaNuvem() async {
    if (!Nuvem.i.temSessao) return;
    final daNuvem = await Nuvem.i.puxar();
    if (daNuvem != null) fundirDaNuvem(daNuvem);
    await Nuvem.i.contarAbertura(Sequencia.iso(DateTime.now()));
  }

  Future<void> _procurarConteudoNovo() async {
    final houve = await ConteudoRemoto.procurarActualizacao(conteudo.versao);
    if (houve) {
      haConteudoNovo = true;
      notifyListeners();
    }
  }

  Future<void> _gravar() async {
    // O telemóvel primeiro, sempre. A nuvem é uma cópia de segurança do
    // que já está gravado aqui, nunca o contrário — se a rede falhar, não
    // se perde nada.
    Nuvem.i.empurrar(paraNuvem());

    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(
      _key,
      json.encode({
        'nome': nome,
        'classe': classe,
        'onboarded': onboarded,
        'som': som,
        'xp': xp,
        'sequencia': _sequencia.paraJson(),
        'lives': lives,
        'cursoId': cursoId,
        'progresso': progresso,
        'erradas': erradas.toList(),
        'diaDasVidas': _diaDasVidas,
        'vezesSemVidas': _vezesSemVidas,
        'bloqueadoAte': _bloqueadoAte?.toIso8601String(),
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

  /* ---------------- Progresso na nuvem ----------------
     Só o que é da criança viaja: o que aprendeu, quanto XP tem, que dias
     estudou. As vidas, o bloqueio e o som ficam de fora de propósito —
     são do aparelho e do momento, não dela. Sincronizar um castigo de
     três horas para o telemóvel da escola seria absurdo. */

  Map<String, dynamic> paraNuvem() => {
    'nome': nome,
    'classe': classe,
    'xp': xp,
    'sequencia': _sequencia.paraJson(),
    'cursoId': cursoId,
    'progresso': progresso,
    'erradas': erradas.toList(),
  };

  /// Junta o que veio da nuvem com o que está no telemóvel.
  ///
  /// Fica sempre com o melhor dos dois, nunca com o mais recente. É a
  /// diferença entre sincronizar e apagar: uma criança que passou a tarde
  /// a jogar sem rede e depois entra na conta não pode ver esse trabalho
  /// desaparecer porque o servidor tinha uma cópia mais antiga.
  ///
  /// O nome e a classe são a excepção, e por uma razão: entrar numa conta
  /// é dizer "sou eu, este telemóvel é novo". Aí o que vale é o que a
  /// conta diz, não o que ficou escrito no aparelho.
  void fundirDaNuvem(Map<String, dynamic> n) {
    final nomeN = (n['nome'] ?? '') as String;
    if (nomeN.trim().isNotEmpty) nome = nomeN;

    final classeN = (n['classe'] ?? '') as String;
    if (classeN.trim().isNotEmpty && conteudo.cursos.any((c) => c.classe == classeN)) {
      classe = classeN;
    }

    xp = math.max(xp, (n['xp'] ?? 0) as int);
    _sequencia = _sequencia.fundirCom(
      Sequencia.deJson(n['sequencia'] as Map<String, dynamic>?),
    );

    // Por nível fica a melhor percentagem. Repetir um nível e sair-se pior
    // não pode apagar o resultado bom que já lá estava.
    final pN = (n['progresso'] as Map?) ?? {};
    pN.forEach((k, v) {
      final chave = '$k';
      final valor = (v as num).toInt();
      progresso[chave] = math.max(progresso[chave] ?? 0, valor);
    });

    // As erradas juntam-se as duas: uma pergunta falhada noutro telemóvel
    // continua por rever neste. Sai da lista quando for acertada.
    erradas.addAll(((n['erradas'] as List?) ?? []).cast<String>());

    final cursoN = n['cursoId'] as String?;
    if (cursoN != null && cursosVisiveis.any((c) => c.id == cursoN)) {
      cursoId = cursoN;
    } else if (!cursosVisiveis.any((c) => c.id == cursoId)) {
      cursoId = cursosVisiveis.first.id;
    }

    notifyListeners();
    _gravar();
  }

  /// Entra na conta e funde os dois lados. Devolve nulo se correu bem, ou
  /// a mensagem a mostrar ao adulto que está a tratar disto.
  Future<String?> entrarNaConta(
    String email,
    String palavra, {
    required bool contaNova,
  }) async {
    try {
      if (contaNova) {
        await Nuvem.i.criarConta(email, palavra);
      } else {
        await Nuvem.i.entrar(email, palavra);
      }
      final daNuvem = await Nuvem.i.puxar();
      if (daNuvem != null) fundirDaNuvem(daNuvem);
      // Sobe já o resultado da fusão: se a app fechasse agora, o que a
      // criança fez offline ficaria só neste telemóvel.
      await Nuvem.i.empurrarJa(paraNuvem());
      await Nuvem.i.contarAbertura(Sequencia.iso(DateTime.now()));
      notifyListeners();
      return null;
    } catch (e) {
      return Nuvem.explicar(e);
    }
  }

  Future<void> sairDaConta() async {
    await Nuvem.i.sair();
    notifyListeners();
  }

  Future<void> definirSom(bool ligado) async {
    som = ligado;
    notifyListeners();
    await Sons.i.definirLigado(ligado);
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

  /* ---- Bloqueio por vidas esgotadas ----
     Cada vez que as vidas acabam no mesmo dia, a espera cresce. Sem isto o
     contador de corações não queria dizer nada: descia a zero e a criança
     continuava a jogar como se nada fosse.

     A escada reinicia todos os dias. Sem esse reinício, uma criança que
     tivesse um mau dia começaria o dia seguinte com três horas de castigo
     por erros da véspera — que é o contrário do que uma app de escola deve
     fazer. */
  static const esperas = [
    Duration(minutes: 5),
    Duration(minutes: 15),
    Duration(minutes: 30),
    Duration(hours: 1),
    Duration(hours: 3),
  ];

  int _vezesSemVidas = 0;
  DateTime? _bloqueadoAte;

  /// Quanto falta até poder recomeçar. Zero quando não há bloqueio.
  Duration get esperaRestante {
    final ate = _bloqueadoAte;
    if (ate == null) return Duration.zero;
    final falta = ate.difference(DateTime.now());
    return falta.isNegative ? Duration.zero : falta;
  }

  bool get bloqueado => esperaRestante > Duration.zero;

  /// Devolve as vidas quando a espera acaba. Chamado ao olhar para o relógio,
  /// e não por um temporizador — a app pode estar fechada durante a espera,
  /// e o que conta é a hora, não o tempo que esteve aberta.
  void verificarFimDoBloqueio() {
    if (_bloqueadoAte == null) return;
    if (esperaRestante > Duration.zero) return;
    _bloqueadoAte = null;
    lives = maxLives;
    notifyListeners();
    _gravar();
  }

  /// A espera que vem a seguir, para se poder avisar antes de acontecer.
  Duration get proximaEspera =>
      esperas[_vezesSemVidas.clamp(0, esperas.length - 1)];

  /// Fecha uma sessão de treino ou revisão.
  ///
  /// Dá XP e conta para a sequência do dia — praticar é estudar. O que não
  /// faz é marcar níveis como concluídos: o Roby não avança na amarelinha
  /// por treinar o que já sabia.
  ///
  /// Existe porque o ecrã de fim mostrava "+XP ganho" em sessões avulsas sem
  /// que esse XP entrasse em lado nenhum — um número inventado à frente da
  /// criança.
  void concluirTreino(int acertos) {
    xp += acertos * xpPorAcerto;
    _sequencia = _sequencia.comActividadeEm(DateTime.now());
    notifyListeners();
    _gravar();
  }

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
    _vezesSemVidas = 0;
    _bloqueadoAte = null;
  }

  /// Perde uma vida. Nas sessões de revisão isto não é chamado — errar a
  /// praticar não pode custar, senão a criança que mais precisa de treinar
  /// é a que fica mais depressa sem poder treinar.
  void perderVida() {
    if (lives <= 0) return;
    lives--;
    if (lives == 0) {
      _bloqueadoAte = DateTime.now().add(proximaEspera);
      _vezesSemVidas++;
    }
    notifyListeners();
    _gravar();
  }

  void concluirNivel(int i, int acertos, int total) {
    final lv = niveis[i];
    final pct = total == 0 ? 0 : (acertos * 100 / total).round();
    // A melhor nota fica. Refazer um nível para treinar não pode baixar o
    // que já se tinha conseguido.
    final chave = chaveDe(lv.unit, lv.nivel);
    progresso[chave] = math.max(progresso[chave] ?? 0, pct);
    xp += acertos * xpPorAcerto + xpPorNivel;
    _sequencia = _sequencia.comActividadeEm(DateTime.now());
    unawaited(Nuvem.i.contarLicao());
    notifyListeners();
    _gravar();
  }

  void reporVidas() {
    lives = maxLives;
    notifyListeners();
    _gravar();
  }
}
