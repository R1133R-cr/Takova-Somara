import 'dart:async';
import 'dart:convert';
import 'dart:math' as math;
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/bolsa_de_tempo.dart';
import '../models/campanha.dart';
import '../models/carteira.dart';
import '../models/coleccao.dart';
import '../models/conquista.dart';
import '../models/content.dart';
import '../models/escadaria.dart';
import '../models/sorte.dart';
import '../models/sequencia.dart';
import '../services/conteudo_remoto.dart';
import '../services/nuvem.dart';
import '../services/sons.dart';
import '../widgets/roby.dart';

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

  /// Em que degrau da escadaria vai cada joguinho.
  ///
  /// Cada jogo tem a sua — não há nível global do aluno. Começa no 1 e sobe
  /// um por nível concluído, até [nivelMaximo].
  final Map<Jogo, int> _niveisDosJogos = {};

  int nivelDe(Jogo jogo) => _niveisDosJogos[jogo] ?? 1;

  /// Sobe um degrau. Devolve o nível novo.
  ///
  /// Nunca desce e nunca passa do tecto: a escadaria é uma promessa, e uma
  /// promessa que anda para trás não é promessa nenhuma.
  int subirNivelDe(Jogo jogo) {
    final novo = math.min(nivelDe(jogo) + 1, nivelMaximo);
    if (novo != nivelDe(jogo)) {
      _niveisDosJogos[jogo] = novo;
      _verificarConquistas();
      notifyListeners();
      _gravar();
    }
    return novo;
  }

  /// Guardados pelo NOME do jogo e não pelo índice do enum: acrescentar um
  /// joguinho no meio da lista não pode fazer a criança perder o nível do
  /// Pomar por ele ter passado a ser o terceiro em vez do segundo.
  Map<String, int> _niveisParaJson() =>
      {for (final e in _niveisDosJogos.entries) e.key.name: e.value};

  void _lerNiveisDosJogos(Map? j) {
    if (j == null) return;
    for (final jogo in Jogo.values) {
      final v = j[jogo.name];
      if (v is int && v >= 1) {
        _niveisDosJogos[jogo] = math.min(v, nivelMaximo);
      }
    }
  }

  /* ---------------- Tempo de jogo ----------------
     Os corações limitam os exercícios; a bolsa limita os jogos. São coisas
     separadas de propósito, e o estudo NUNCA é travado por esta. Ver
     [BolsaDeTempo] para o porquê do tecto diário. */

  BolsaDeTempo _bolsa = const BolsaDeTempo(dia: '');

  /// O relógio da app. Só os testes lhe mexem — sem isto não há maneira de
  /// provar que a bolsa se repõe à meia-noite, nem que sete dias seguidos
  /// de estudo dão um cristal, sem esperar sete dias.
  ///
  /// É um só de propósito. Enquanto a sequência lia `DateTime.now()` e o
  /// marco da semana lia este, as duas datas podiam estar em anos
  /// diferentes e o cristal da semana nunca chegava.
  @visibleForTesting
  DateTime Function() relogio = DateTime.now;

  /// Há um jogo aberto (mesmo que a app esteja minimizada).
  bool _aJogar = false;

  /// Desde quando é que o relógio corre. Nulo com a app em segundo plano:
  /// é assim que o tempo pára quando o ecrã se apaga.
  DateTime? _correDesde;

  String get _hoje => Sequencia.iso(relogio());

  Duration get _decorrido {
    final desde = _correDesde;
    if (desde == null) return Duration.zero;
    final d = relogio().difference(desde);
    return d.isNegative ? Duration.zero : d;
  }

  /// A bolsa de hoje, já reposta se o dia virou.
  BolsaDeTempo get bolsa => _bolsa.noDia(_hoje);

  /// Quanto tempo de jogo ainda há, contando o jogo que está a decorrer.
  Duration get tempoDeJogo {
    final falta = bolsa.restante - _decorrido;
    return falta.isNegative ? Duration.zero : falta;
  }

  bool get podeJogar => tempoDeJogo > Duration.zero;

  /// Fecha a conta do que se jogou até agora.
  void _assentarTempo() {
    final d = _decorrido;
    _correDesde = null;
    if (d <= Duration.zero) return;
    _bolsa = bolsa.comGasto(d);
  }

  /// Um jogo abriu: o relógio arranca.
  void entrarNoJogo() {
    // Se este for o primeiro acto do dia, a corrente do "primeiro a escola"
    // parte-se aqui — e é por isso que se regista o jogo e não só o estudo.
    _registarActo(estudo: false);
    _bolsa = bolsa;
    _aJogar = true;
    _correDesde = relogio();
  }

  /// O jogo fechou: assenta o gasto e guarda.
  void sairDoJogo() {
    if (!_aJogar) return;
    _assentarTempo();
    _aJogar = false;
    notifyListeners();
    _gravar();
  }

  /// A app foi para segundo plano. O tempo de jogo pára aqui — a criança
  /// que atende uma chamada a meio do Pomar não paga por essa chamada.
  void pausarTempoDeJogo() {
    if (!_aJogar || _correDesde == null) return;
    _assentarTempo();
    _gravar();
  }

  /// A app voltou à frente. Só reata se ainda houver um jogo aberto.
  void retomarTempoDeJogo() {
    if (!_aJogar || _correDesde != null) return;
    _correDesde = relogio();
  }

  /// Estudar enche a bolsa.
  ///
  /// Chamada de [concluirNivel]. Não é chamada pelo treino nem pelos
  /// joguinhos: jogar para ganhar tempo de jogo seria um círculo, e a
  /// bolsa deixava de querer dizer nada.
  void _ganharTempoDeJogo(Duration d) {
    _bolsa = bolsa.comGanho(d);
  }

  /* ---------------- Moedas, loja e colecção ----------------
     O Ouro entra todos os dias e sai depressa; o Cristal é raro e guarda-se.
     Ver [Carteira] para o porquê de serem duas. */

  Carteira _carteira = const Carteira();
  Coleccao _coleccao = const Coleccao();

  /// Os marcos que já foram pagos, para não pagarem duas vezes.
  ///
  /// Um só conjunto para todos os tipos (`unidade:...`, `semana:3`), com uma
  /// só regra de fusão — união. Com um contador por tipo, refazer uma
  /// unidade ou sincronizar dois telemóveis dava cristais do ar.
  final Set<String> _marcosPagos = {};

  Carteira get carteira => _carteira;
  Coleccao get coleccao => _coleccao;

  /// A cara do Roby que a criança escolheu. Cai na de fábrica se a escolhida
  /// não for dela.
  RobyPose get robyEscolhido => _coleccao.roby;

  /// Paga um marco uma vez só. Devolve verdadeiro se pagou agora.
  bool _pagarMarco(String chave, Moeda moeda, int quanto) {
    if (!_marcosPagos.add(chave)) return false;
    _carteira = _carteira.comGanho(moeda, quanto);
    return true;
  }

  /// O que aconteceu a uma tentativa de compra.
  ///
  /// Um enum e não um booleano porque as três recusas pedem frases
  /// diferentes, e "não deu" à frente de uma criança que juntou cristais
  /// durante duas semanas não é resposta.
  ResultadoDaCompra comprar(ItemDaLoja item) {
    if (!item.consumivel && _coleccao.compradas.contains(item.id)) {
      return ResultadoDaCompra.jaTem;
    }
    // Minutos comprados entram na mesma bolsa e respeitam o mesmo tecto.
    // Vender tempo que o tecto ia deitar fora seria vender nada.
    if (item.tempo != null && bolsa.noTecto) return ResultadoDaCompra.noTecto;

    final paga = _carteira.comGasto(item.moeda, item.preco);
    if (paga == null) return ResultadoDaCompra.semSaldo;
    _carteira = paga;

    if (item.tempo != null) {
      _ganharTempoDeJogo(item.tempo!);
    } else {
      _coleccao = _coleccao.com(item.id);
      // Uma cara acabada de comprar veste-se sozinha. Comprá-la e não a ver
      // em lado nenhum seria o pior momento possível para pedir mais um
      // toque à criança.
      final p = item.pose;
      if (p != null) _coleccao = _coleccao.aUsar(p);
    }

    notifyListeners();
    _gravar();
    return ResultadoDaCompra.feito;
  }

  /// Veste uma pose já comprada, ou volta à de fábrica com nulo.
  void escolherRoby(RobyPose? pose) {
    final nova = _coleccao.aUsar(pose);
    if (nova.escolhida == _coleccao.escolhida) return;
    _coleccao = nova;
    notifyListeners();
    _gravar();
  }

  /* ---------------- Campanha semanal ----------------
     O único sítio da app com prazo. Ver [Campanha]. */

  /// Em que dia é que cada nível foi concluído (chave → ISO).
  ///
  /// O `progresso` guarda a nota, mas não a data — e sem data não há maneira
  /// de saber o que é que a criança estudou *na semana passada*, que é
  /// exactamente o que a campanha precisa de saber.
  final Map<String, String> _estudadoEm = {};

  Campanha? _campanha;

  /// A última segunda-feira em que se procurou material. Sem isto, uma
  /// semana sem campanha era reavaliada a cada toque.
  String? _semanaVerificada;

  Campanha? get campanha => _campanha;

  /// Há campanha por fazer esta semana?
  bool get temCampanhaPorFazer => _campanha != null && !_campanha!.feita;

  /// As perguntas da campanha, resolvidas no currículo de agora.
  ///
  /// Uma pergunta que tenha desaparecido numa actualização de conteúdo cai
  /// aqui em silêncio — é melhor uma campanha com dezassete perguntas do que
  /// um ecrã que rebenta.
  List<Questao> get perguntasDaCampanha {
    final c = _campanha;
    if (c == null) return const [];
    final querem = c.enunciados.toSet();
    final achadas = <String, Questao>{};
    for (final curso in conteudo.cursos) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          for (final q in n.questoes) {
            if (querem.contains(q.q)) achadas.putIfAbsent(q.q, () => q);
          }
        }
      }
    }
    return [
      for (final e in c.enunciados)
        if (achadas[e] != null) achadas[e]!,
    ];
  }

  /// Os enunciados dos níveis concluídos numa janela de dias.
  List<String> _enunciadosEstudadosEntre(String de, String ate) {
    final chaves = {
      for (final e in _estudadoEm.entries)
        if (e.value.compareTo(de) >= 0 && e.value.compareTo(ate) < 0) e.key,
    };
    if (chaves.isEmpty) return const [];

    final fora = <String>[];
    for (final curso in conteudo.cursos) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          if (chaves.contains('${curso.id}:${u.id}:${n.id}')) {
            fora.addAll(n.questoes.map((q) => q.q));
          }
        }
      }
    }
    return fora;
  }

  /// Monta a campanha da semana, se ainda não houver uma.
  ///
  /// Corre uma vez por semana e não a cada toque: a campanha é da segunda e
  /// não muda até domingo. Uma que aparecesse a meio da semana quebrava a
  /// única coisa que a define, que é ter prazo.
  void verificarCampanha() {
    final semana = segundaDe(relogio());
    if (_campanha?.semana == semana || _semanaVerificada == semana) return;
    _semanaVerificada = semana;

    final segunda = DateTime.parse(semana);
    String recuar(int dias) =>
        Sequencia.iso(segunda.subtract(Duration(days: dias)));

    final erros = paraRever.map((q) => q.q).toList();
    final semente = sementeDaSemana(semana);

    // A semana passada primeiro. Se não deu nada — férias, doença, um
    // telemóvel emprestado — recua-se mais uma. Duas e pára: puxar de um
    // mês atrás já não é rever, é começar outra vez.
    var enunciados = escolherPerguntas(
      dosErros: erros,
      doEstudo: _enunciadosEstudadosEntre(recuar(7), semana),
      semente: semente,
    );
    if (enunciados.isEmpty) {
      enunciados = escolherPerguntas(
        dosErros: erros,
        doEstudo: _enunciadosEstudadosEntre(recuar(14), recuar(7)),
        semente: semente,
      );
    }

    _campanha = enunciados.isEmpty
        ? null
        : Campanha(semana: semana, enunciados: enunciados);
    notifyListeners();
    _gravar();
  }

  /// Fecha a campanha e paga o que ela valer.
  ///
  /// Só uma vez: refazê-la não paga outra vez. O prazo é semanal e o prémio
  /// também — senão bastava repeti-la cinco vezes para encher as sortes.
  void concluirCampanha(int acertos, int total) {
    final c = _campanha;
    if (c == null || c.feita) return;
    final fechada = c.comResultado(acertos, total);
    _campanha = fechada;
    for (var i = 0; i < fechada.sortesGanhas; i++) {
      _sortes = _sortes.comGanho();
    }
    notifyListeners();
    _gravar();
  }

  /* ---------------- Sortes ----------------
     A ajuda que se ganha a estudar e se gasta a jogar. Ver [Sortes]. */

  Sortes _sortes = const Sortes();

  Sortes get sortes => _sortes;

  /// Gasta uma sorte. Devolve falso quando não há nenhuma.
  bool gastarSorte() {
    final resto = _sortes.aGastar();
    if (resto == null) return false;
    _sortes = resto;
    notifyListeners();
    _gravar();
    return true;
  }

  /* ---------------- Conquistas ----------------
     Medalhas por marcos. Ver [Conquista]; a faixa que as mostra é o
     `widgets/faixa_conquista.dart`. */

  final Set<Conquista> _conquistas = {};

  /// As que ainda não foram mostradas à criança. Uma fila e não uma só: um
  /// nível pode fechar a unidade, a disciplina e a classe ao mesmo tempo.
  final List<Conquista> _porMostrar = [];

  Set<Conquista> get conquistas => Set.unmodifiable(_conquistas);
  bool ganhou(Conquista c) => _conquistas.contains(c);

  Conquista? get proximaConquista =>
      _porMostrar.isEmpty ? null : _porMostrar.first;

  /// Tira a primeira da fila. Chamado pela faixa quando começa a mostrá-la.
  Conquista? tirarConquista() =>
      _porMostrar.isEmpty ? null : _porMostrar.removeAt(0);

  /// Só para os testes: põe uma medalha na fila sem a ganhar.
  ///
  /// Serve para pôr a faixa a mostrar a de título mais comprido em todos os
  /// tamanhos de ecrã. Sem isto, só se conseguia ver a faixa das medalhas
  /// fáceis — e é justamente a comprida que transborda.
  @visibleForTesting
  void encomendarFaixa(Conquista c) {
    _porMostrar.add(c);
    notifyListeners();
  }

  /// Perguntas que estavam nos Guardados e passaram a certas.
  int _recuperadas = 0;

  /* ---- O que só se vê de dentro de um jogo ----
     Duas medalhas do §2 dependem de coisas que acontecem a meio de um
     nível, e não de um degrau da escadaria. Os jogos avisam por aqui. */

  int _especiaisNoPomar = 0;
  int _sopasPerfeitas = 0;

  /// O Pomar acabou de criar uma peça especial.
  void registarPecaEspecial() {
    _especiaisNoPomar++;
    _verificarConquistas();
    notifyListeners();
    _gravar();
  }

  /// Uma sopa fechada sem uma única selecção errada.
  void registarSopaPerfeita() {
    _sopasPerfeitas++;
    _verificarConquistas();
    notifyListeners();
    _gravar();
  }

  /* ---- Estudar antes de jogar ----
     Guarda-se o primeiro acto de cada dia, e não a ordem toda: o que
     interessa é se a criança abriu a escola antes da sala de jogos, e o
     terceiro ou quarto acto do dia já não diz nada sobre isso. */

  /// O dia a que o registo abaixo pertence.
  String? _diaDoActo;

  /// Dias a fio em que o primeiro acto foi estudar.
  int _diasAEstudarPrimeiro = 0;

  /// O último dia contado, para saber se a corrente se partiu.
  String? _ultimoDiaAEstudarPrimeiro;

  void _registarActo({required bool estudo}) {
    final hoje = _hoje;
    if (_diaDoActo == hoje) return; // já se sabe como o dia começou
    _diaDoActo = hoje;

    if (!estudo) {
      // Jogou primeiro: a corrente parte-se hoje.
      _diasAEstudarPrimeiro = 0;
      _ultimoDiaAEstudarPrimeiro = null;
      return;
    }

    final ontem = Sequencia.iso(relogio().subtract(const Duration(days: 1)));
    _diasAEstudarPrimeiro =
        _ultimoDiaAEstudarPrimeiro == ontem ? _diasAEstudarPrimeiro + 1 : 1;
    _ultimoDiaAEstudarPrimeiro = hoje;
  }

  /// Os números de que as condições precisam.
  RetratoDoAluno get retrato {
    var unidades = 0, disciplinas = 0, classes = 0;
    final feitasPorClasse = <String, int>{};
    final cursosPorClasse = <String, int>{};

    for (final c in conteudo.cursos) {
      cursosPorClasse[c.classe] = (cursosPorClasse[c.classe] ?? 0) + 1;
      var todasAsUnidades = c.units.isNotEmpty;
      for (final u in c.units) {
        final feita = u.niveis.isNotEmpty &&
            u.niveis.every((n) => progresso.containsKey('${c.id}:${u.id}:${n.id}'));
        if (feita) {
          unidades++;
        } else {
          todasAsUnidades = false;
        }
      }
      if (todasAsUnidades) {
        disciplinas++;
        feitasPorClasse[c.classe] = (feitasPorClasse[c.classe] ?? 0) + 1;
      }
    }
    for (final entrada in cursosPorClasse.entries) {
      if (feitasPorClasse[entrada.key] == entrada.value) classes++;
    }

    return RetratoDoAluno(
      niveis: progresso.length,
      unidades: unidades,
      disciplinas: disciplinas,
      classes: classes,
      perfeitos: progresso.values.where((v) => v == 100).length,
      recuperadas: _recuperadas,
      diasSeguidos: streak,
      diasAEstudarPrimeiro: _diasAEstudarPrimeiro,
      especiaisNoPomar: _especiaisNoPomar,
      sopasPerfeitas: _sopasPerfeitas,
      degraus: {for (final j in Jogo.values) j: nivelDe(j)},
    );
  }

  /// Lê medalhas de uma lista de nomes, ignorando as que já não existem.
  ///
  /// Uma conquista apagada numa versão futura não pode rebentar o arranque
  /// de quem a tinha ganho.
  void _lerConquistas(List? nomes) {
    for (final n in (nomes ?? const []).cast<String>()) {
      for (final c in Conquista.values) {
        if (c.name == n) _conquistas.add(c);
      }
    }
  }

  /// Vê o que se ganhou de novo, paga os cristais e põe na fila da faixa.
  ///
  /// Com [mostrar] falso não entra nada na fila. É assim que se chama uma
  /// vez ao arrancar: quem já tinha meia classe feita quando esta versão
  /// chegou recebe as medalhas e os cristais que merecia, mas não leva com
  /// vinte faixas seguidas na cara.
  void _verificarConquistas({bool mostrar = true}) {
    final ganhas = conquistasDe(retrato);
    for (final c in Conquista.values) {
      if (!ganhas.contains(c) || !_conquistas.add(c)) continue;
      if (c.cristais > 0) {
        _pagarMarco('conquista:${c.name}', Moeda.cc, c.cristais);
      }
      if (mostrar) _porMostrar.add(c);
    }
  }

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
      _recuperadas++;
      _verificarConquistas();
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
  int get streak => _sequencia.visivelEm(relogio());

  /// As unidades com vocabulário que a criança já começou a estudar.
  ///
  /// Basta **um** nível feito para a sopa da matéria abrir. Exigir a unidade
  /// inteira deixava o jogo escondido justamente de quem mais precisava de
  /// rever — e as palavras da unidade são as mesmas do primeiro ao último
  /// nível.
  List<({Curso curso, Unidade unidade})> get unidadesComPalavras => [
    for (final c in conteudo.cursos)
      for (final u in c.units)
        if (u.palavras.length >= 4 &&
            u.niveis.any(
              (n) => progresso.containsKey('${c.id}:${u.id}:${n.id}'),
            ))
          (curso: c, unidade: u),
  ];

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
        _lerNiveisDosJogos(j['jogos'] as Map?);
        _bolsa = BolsaDeTempo.deJson(j['bolsa'] as Map<String, dynamic>?) ??
            _bolsa;
        _carteira = Carteira.deJson(j['carteira'] as Map<String, dynamic>?);
        _coleccao = Coleccao.deJson(j['coleccao'] as Map<String, dynamic>?);
        _marcosPagos.addAll(((j['marcos'] as List?) ?? []).cast<String>());
        _sortes = Sortes.deJson(j['sortes'] as Map<String, dynamic>?);
        ((j['estudadoEm'] as Map?) ?? {})
            .forEach((k, v) => _estudadoEm['$k'] = '$v');
        _campanha = Campanha.deJson(j['campanha'] as Map<String, dynamic>?);
        _semanaVerificada = j['semanaVerificada'] as String?;
        _lerConquistas(j['conquistas'] as List?);
        _recuperadas = (j['recuperadas'] ?? 0) as int;
        _especiaisNoPomar = (j['especiais'] ?? 0) as int;
        _sopasPerfeitas = (j['sopasPerfeitas'] ?? 0) as int;
        _diasAEstudarPrimeiro = (j['estudouPrimeiro'] ?? 0) as int;
        _ultimoDiaAEstudarPrimeiro = j['diaEstudouPrimeiro'] as String?;
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
    // Sem mostrar: quem já tinha meia classe feita quando esta versão
    // chegou recebe as medalhas e os cristais que merecia, mas não leva com
    // vinte faixas seguidas na cara ao abrir a app.
    _verificarConquistas(mostrar: false);
    verificarCampanha();
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
        'jogos': _niveisParaJson(),
        'bolsa': bolsa.paraJson(),
        'carteira': _carteira.paraJson(),
        'coleccao': _coleccao.paraJson(),
        'marcos': _marcosPagos.toList()..sort(),
        'sortes': _sortes.paraJson(),
        'estudadoEm': _estudadoEm,
        'campanha': _campanha?.paraJson(),
        'semanaVerificada': _semanaVerificada,
        'conquistas': _conquistas.map((c) => c.name).toList()..sort(),
        'recuperadas': _recuperadas,
        'especiais': _especiaisNoPomar,
        'sopasPerfeitas': _sopasPerfeitas,
        'estudouPrimeiro': _diasAEstudarPrimeiro,
        'diaEstudouPrimeiro': _ultimoDiaAEstudarPrimeiro,
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
    'jogos': _niveisParaJson(),
    'bolsa': bolsa.paraJson(),
    'carteira': _carteira.paraJson(),
    'coleccao': _coleccao.paraJson(),
    'marcos': _marcosPagos.toList()..sort(),
    'sortes': _sortes.paraJson(),
    'estudadoEm': _estudadoEm,
    'campanha': _campanha?.paraJson(),
    'conquistas': _conquistas.map((c) => c.name).toList()..sort(),
    'recuperadas': _recuperadas,
    'especiais': _especiaisNoPomar,
    'sopasPerfeitas': _sopasPerfeitas,
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

    // O degrau de cada joguinho fica pelo mais alto dos dois. Jogar sem rede
    // num telemóvel e depois entrar na conta não pode fazer descer a
    // escadaria — é a mesma regra do XP e do progresso.
    final jN = (n['jogos'] as Map?) ?? {};
    for (final jogo in Jogo.values) {
      final v = jN[jogo.name];
      if (v is int) {
        _niveisDosJogos[jogo] =
            math.min(math.max(nivelDe(jogo), v), nivelMaximo);
      }
    }

    // A bolsa junta-se pelo maior dos dois em cada número — o que se
    // estudou noutro telemóvel conta, e o que lá se jogou também. Ver
    // [BolsaDeTempo.fundirCom].
    final bN = BolsaDeTempo.deJson(n['bolsa'] as Map<String, dynamic>?);
    if (bN != null) _bolsa = bolsa.fundirCom(bN.noDia(_hoje));

    // A carteira fica pelo maior de cada total (ganho e gasto de cada
    // moeda), a colecção junta-se por união e os marcos também: comprar uma
    // cara noutro telemóvel não a pode fazer desaparecer, e um marco já pago
    // não pode voltar a pagar.
    _carteira = _carteira.fundirCom(
      Carteira.deJson(n['carteira'] as Map<String, dynamic>?),
    );
    _coleccao = _coleccao.fundirCom(
      Coleccao.deJson(n['coleccao'] as Map<String, dynamic>?),
    );
    _marcosPagos.addAll(((n['marcos'] as List?) ?? []).cast<String>());

    // As medalhas juntam-se e NUNCA desaparecem: um telemóvel com A e B e
    // outro com B e C ficam os dois com A, B e C. Uma medalha que some numa
    // sincronização é a coisa que faz uma criança deixar de acreditar no
    // ecrã. O mesmo vale para o que já se recuperou dos Guardados.
    // As datas de estudo juntam-se, ficando a mais recente de cada nível:
    // um nível refeito noutro telemóvel entra na campanha desta semana.
    ((n['estudadoEm'] as Map?) ?? {}).forEach((k, v) {
      final chave = '$k', dia = '$v';
      final aqui = _estudadoEm[chave];
      if (aqui == null || dia.compareTo(aqui) > 0) _estudadoEm[chave] = dia;
    });

    final cN = Campanha.deJson(n['campanha'] as Map<String, dynamic>?);
    _campanha = _campanha?.fundirCom(cN) ?? cN;

    _sortes = _sortes.fundirCom(
      Sortes.deJson(n['sortes'] as Map<String, dynamic>?),
    );
    _lerConquistas(n['conquistas'] as List?);
    _recuperadas = math.max(_recuperadas, (n['recuperadas'] ?? 0) as int);
    _especiaisNoPomar =
        math.max(_especiaisNoPomar, (n['especiais'] ?? 0) as int);
    _sopasPerfeitas =
        math.max(_sopasPerfeitas, (n['sopasPerfeitas'] ?? 0) as int);

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
    _sequencia = _sequencia.comActividadeEm(relogio());
    _verificarConquistas();
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
    final hoje = Sequencia.iso(relogio());
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
    _estudadoEm[chave] = _hoje;
    xp += acertos * xpPorAcerto + xpPorNivel;
    // Sem um único erro rende mais. É o que faz a criança voltar a um nível
    // que já passou para o fazer melhor, em vez de o passar à tangente.
    _ganharTempoDeJogo(
      pct == 100 ? BolsaDeTempo.porNivelPerfeito : BolsaDeTempo.porNivel,
    );
    // Ouro sempre, e nunca zero: quem tropeçou num nível difícil já teve o
    // castigo de o ter tropeçado.
    _carteira = _carteira.comGanho(Moeda.gc, Carteira.ouroPorNivel(pct));
    // Sem um único erro: mais uma sorte para gastar nos jogos. É a única
    // porta que existe entre a escola e a ajuda lá dentro.
    if (pct == 100) _sortes = _sortes.comGanho();
    _sequencia = _sequencia.comActividadeEm(relogio());
    _registarActo(estudo: true);
    _pagarMarcosDeCristal(lv.unit);
    _verificarConquistas();
    unawaited(Nuvem.i.contarLicao());
    notifyListeners();
    _gravar();
  }

  /// Os cristais, que só saem em marcos.
  ///
  /// Dois, por agora: fechar uma unidade inteira sem um único erro, e cada
  /// sete dias seguidos de estudo. Os das conquistas entram quando elas
  /// existirem (§2 do SPEC).
  void _pagarMarcosDeCristal(Unidade unidade) {
    final perfeita = unidade.niveis.every(
      (n) => (progresso[chaveDe(unidade, n)] ?? 0) == 100,
    );
    if (perfeita) {
      _pagarMarco(
        'unidade:${curso.id}:${unidade.id}',
        Moeda.cc,
        Carteira.cristalPorUnidadePerfeita,
      );
    }

    // Uma semana seguida vale um cristal, e a segunda semana vale outro. Os
    // marcos ficam guardados pelo NÚMERO da semana, e não por um contador:
    // assim quem já tinha vinte e um dias antes desta versão não recebe três
    // cristais de uma vez, e quem perde a sequência e recomeça não volta a
    // ser pago pela primeira.
    final semanas = _sequencia.visivelEm(relogio()) ~/ 7;
    for (var w = 1; w <= semanas; w++) {
      _pagarMarco('semana:$w', Moeda.cc, Carteira.cristalPorSemanaSeguida);
    }
  }

  void reporVidas() {
    lives = maxLives;
    notifyListeners();
    _gravar();
  }
}
