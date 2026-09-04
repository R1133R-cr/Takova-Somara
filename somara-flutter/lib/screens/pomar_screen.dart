import 'dart:async';
import 'dart:math';
import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../models/pomar.dart';
import '../models/rastreio.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/botao_de_sorte.dart';
import '../widgets/marca_especial.dart';
import '../widgets/roby.dart';

/// O Pomar: juntar três ou mais do mesmo produto.
///
/// As peças são manga, banana, coco, milho, tomate e amendoim — o que se vê
/// no mercado, não os rebuçados coloridos do costume. Sem ensinar nada de
/// propósito, o jogo nomeia as coisas do dia-a-dia da criança.
///
/// Não gasta corações e não faz avançar a amarelinha. É para brincar.
class PomarScreen extends StatefulWidget {
  const PomarScreen({super.key});

  @override
  State<PomarScreen> createState() => _PomarScreenState();
}

class _PomarScreenState extends State<PomarScreen>
    with TickerProviderStateMixin {
  static const _jogadas = 20;

  final _rnd = Random();
  late final AnimationController _abanao;

  late Pomar _tabuleiro;
  int _pontos = 0;
  int _restam = _jogadas;

  /// A peça debaixo do dedo, e a vizinha para onde ela vai.
  int? _arrastada;
  int? _alvo;

  /// Onde o dedo pousou e quanto já andou, em píxeis dentro da grelha.
  Offset _inicioDoDedo = Offset.zero;
  Offset _puxao = Offset.zero;

  /// A animação de largar: leva as peças até ao fim da troca, e traz de
  /// volta as que não formaram nada.
  late final AnimationController _solta;
  Offset _puxaoAoLargar = Offset.zero;

  /// As casas a desaparecer neste instante, para se ver a colheita.
  Set<int> _aColher = const {};

  /// Enquanto a cascata corre, o tabuleiro não aceita toques.
  bool _ocupado = false;

  /// Mensagem passageira: baralhámos, fim de jogo, e afins.
  String? _aviso;

  /// Lado de cada casa, guardado no desenho para as estrelinhas saberem
  /// onde nascer.
  double _lado = 48;

  /// Onde o dedo já mexeu neste tabuleiro. É o que a Sorte lê para achar a
  /// composição que a criança ainda não viu.
  final _rastreio = Rastreio();

  /// As casas que a Sorte está a apontar, a vibrar.
  Set<int> _aVibrar = const {};
  late final AnimationController _vibracao;

  /// A quantas jogadas do fim é que a Sorte deixa de ensinar e passa a
  /// salvar. Com folga vibra — a criança vê a composição e faz a jogada; à
  /// justa dá a peça, porque uma dica não chega para quem tem duas jogadas.
  static const _poucasJogadas = 5;

  /// Os festejos a decorrer. Vários ao mesmo tempo numa cascata longa.
  final _festejos = <_Festejo>[];
  late final AnimationController _brilho;

  @override
  void initState() {
    super.initState();
    // A trilha muda ao COMECAR o jogo, nao ao espreitar a sala. Percorrer
    // os separadores e navegar; abrir um jogo e outra coisa, e e so ai que
    // o ambiente tem de mudar.
    Sons.i.definirAmbiente(Trilha.relaxar);
    _abanao = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 380),
    );
    _solta = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 220),
    );
    _brilho = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 850),
    )..addStatusListener((e) {
      // Limpar no fim e não a meio: um festejo apagado enquanto ainda se vê
      // fica a piscar.
      if (e == AnimationStatus.completed && mounted) {
        setState(_festejos.clear);
      }
    });
    _vibracao = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1600),
    )..addStatusListener((e) {
      if (e == AnimationStatus.completed && mounted) {
        setState(() => _aVibrar = const {});
      }
    });
    _tabuleiro = Pomar.novo(rnd: _rnd);
  }

  @override
  void dispose() {
    Sons.i.definirAmbiente(Trilha.principal);
    _abanao.dispose();
    _solta.dispose();
    _brilho.dispose();
    _vibracao.dispose();
    super.dispose();
  }

  bool get _acabou => _restam <= 0;

  /// Que casa está debaixo deste ponto da grelha.
  int? _casaEm(Offset p) {
    final c = (p.dx / _lado).floor();
    final l = (p.dy / _lado).floor();
    if (!_tabuleiro.dentro(l, c)) return null;
    return _tabuleiro.indice(l, c);
  }

  void _comecarArrasto(Offset p) {
    if (_ocupado || _acabou) return;
    final i = _casaEm(p);
    if (i == null) return;
    Sons.i.toque();
    setState(() {
      _arrastada = i;
      _alvo = null;
      _inicioDoDedo = p;
      _puxao = Offset.zero;
    });
  }

  /// Segue o dedo, mas só até à casa do lado.
  ///
  /// Trava-se no eixo dominante de propósito: numa grelha, um dedo que
  /// desliza na diagonal não sabe o que quer, e deixar a peça flutuar em
  /// duas direcções ao mesmo tempo faz o jogo parecer que não percebe o
  /// gesto. Escolhe-se o eixo com mais movimento e ignora-se o outro.
  void _actualizarArrasto(Offset p) {
    final origem = _arrastada;
    if (origem == null || _ocupado || _acabou) return;

    final delta = p - _inicioDoDedo;
    final horizontal = delta.dx.abs() >= delta.dy.abs();
    final avanco = (horizontal ? delta.dx : delta.dy).clamp(-_lado, _lado);

    final l = _tabuleiro.linhaDe(origem);
    final c = _tabuleiro.colunaDe(origem);
    final dl = horizontal ? 0 : avanco.sign.toInt();
    final dc = horizontal ? avanco.sign.toInt() : 0;

    // Um tremor no dedo não é um gesto: só a partir de um quinto da casa é
    // que se considera que ela quis mesmo mexer.
    final querMexer = avanco.abs() > _lado * 0.2;
    final podeIr = querMexer && _tabuleiro.dentro(l + dl, c + dc);

    setState(() {
      _alvo = podeIr ? _tabuleiro.indice(l + dl, c + dc) : null;
      _puxao = podeIr
          ? Offset(horizontal ? avanco : 0, horizontal ? 0 : avanco)
          : Offset.zero;
    });
  }

  Future<void> _largar() async {
    final origem = _arrastada;
    final destino = _alvo;
    if (origem == null || _ocupado || _acabou) {
      setState(() {
        _arrastada = null;
        _alvo = null;
        _puxao = Offset.zero;
      });
      return;
    }

    if (destino == null) {
      setState(() {
        _arrastada = null;
        _puxao = Offset.zero;
      });
      return;
    }

    // Mexer nestas duas casas conta como tê-las olhado, acerte ou não —
    // é isso que tira esta zona do tabuleiro da lista de candidatas da
    // Sorte. Regista-se antes de saber se a troca vale: uma tentativa
    // falhada também é uma zona onde ela já procurou.
    _rastreio.tocar([origem, destino]);

    final valida = _tabuleiro.podeTrocar(origem, destino);

    // A troca desenha-se sempre até ao fim, mesmo quando não vale. É o que
    // o Candy Crush faz e é o que responde à criança: ela vê as peças
    // trocarem e voltarem, em vez de o gesto simplesmente não acontecer.
    _puxaoAoLargar = Offset(
      _puxao.dx.sign * (_puxao.dx == 0 ? 0 : _lado),
      _puxao.dy.sign * (_puxao.dy == 0 ? 0 : _lado),
    );
    setState(() => _ocupado = true);

    await _solta.forward(from: 0);
    if (!mounted) return;

    if (!valida) {
      Sons.i.errado();
      HapticFeedback.heavyImpact();
      _abanao.forward(from: 0);
      await _solta.reverse();
      if (!mounted) return;
      setState(() {
        _arrastada = null;
        _alvo = null;
        _puxao = Offset.zero;
        _puxaoAoLargar = Offset.zero;
        _ocupado = false;
      });
      return;
    }

    // O sol não forma fila: limpa tudo o que for do produto da peça com
    // que foi trocado. É a razão de ser da peça — guarda-se e gasta-se
    // quando se quer, não quando o tabuleiro deixa.
    final doSol = _tabuleiro.colheitaDoSol(origem, destino);

    setState(() {
      _arrastada = null;
      _alvo = null;
      _puxao = Offset.zero;
      _puxaoAoLargar = Offset.zero;
      _restam--;
      if (doSol == null) _tabuleiro = _tabuleiro.trocaCrua(origem, destino);
    });
    _solta.value = 0;

    await _resolverCascata(inicial: doSol, origem: destino);
  }

  /// Colhe, deixa cair, enche — e repete enquanto for formando trios.
  Future<void> _resolverCascata({Set<int>? inicial, int? origem}) async {
    var nivel = 1;
    var forcado = inicial;
    while (mounted) {
      // A colheita normal vem do tabuleiro; a do sol vem de fora. Em ambos
      // os casos passa por `detonar`, que apanha em cadeia as peças
      // especiais que estiverem no caminho.
      final Colheita colheita;
      if (forcado != null) {
        colheita = Colheita(
          limpar: _tabuleiro.detonar(forcado),
          criar: const [],
        );
        forcado = null;
      } else {
        final base = _tabuleiro.analisar(origem: nivel == 1 ? origem : null);
        if (base.vazia) break;
        colheita = Colheita(
          limpar: _tabuleiro.detonar(base.limpar),
          criar: base.criar,
        );
      }
      if (colheita.vazia) break;

      final grupos = colheita.limpar;
      final ganho =
          Pomar.pontosDe(grupos.length) + Pomar.premioDeCascata(nivel);

      // O retorno é imediato e no sítio onde aconteceu: som, tremor,
      // estrelinhas e o número a saltar de onde saíram as peças. Foi o que
      // a pesquisa mostrou ser o essencial nos jogos do género — o prémio
      // tem de se ver onde o olho já está.
      Sons.i.certo();
      final voz = Pomar.vozPara(grupos.length, nivel);
      if (voz != null) Sons.i.voz(voz);

      HapticFeedback.lightImpact();
      // A primeira peça especial vale uma medalha, e só se sabe daqui: é
      // uma coisa que acontece a meio de um nível, não um degrau.
      if (colheita.criar.isNotEmpty) {
        context.read<AppState>().registarPecaEspecial();
      }
      _festejar(grupos, ganho, nivel);

      setState(() => _aColher = grupos);
      await Future.delayed(const Duration(milliseconds: 260));
      if (!mounted) return;

      setState(() {
        _pontos += ganho;
        _aColher = const {};
        _tabuleiro = _tabuleiro.colher(colheita).assentar();
      });
      await Future.delayed(const Duration(milliseconds: 170));
      if (!mounted) return;

      setState(() => _tabuleiro = _tabuleiro.encher(_rnd));
      await Future.delayed(const Duration(milliseconds: 120));
      if (!mounted) return;

      nivel++;
    }

    if (!mounted) return;

    // Tabuleiro sem saída: remexe-se em vez de acabar a partida por azar.
    if (!_tabuleiro.haJogada()) {
      setState(() {
        _tabuleiro = _tabuleiro.baralhar(_rnd);
        _aviso = 'Não havia jogadas. Baralhámos as peças.';
      });
      Timer(const Duration(seconds: 3), () {
        if (mounted) setState(() => _aviso = null);
      });
    }

    setState(() => _ocupado = false);

    if (_acabou) {
      Sons.i.nivel();
      // Os pontos valem XP, com um travão: quinhentos pontos por cada
      // acerto de lição, e nunca mais de oito. Jogar não pode render mais
      // depressa do que estudar — e o travão tem de estar longe do alcance
      // de uma jogada só, senão as outras dezanove não valem nada.
      final ganho = (_pontos / 500).floor().clamp(0, 8);
      if (ganho > 0 && mounted) {
        context.read<AppState>().concluirTreino(ganho);
      }
    }
  }

  /// Marca o sítio da colheita para as estrelinhas e o número saltarem
  /// de lá.
  void _festejar(Set<int> grupos, int ganho, int nivel) {
    var somaL = 0.0, somaC = 0.0;
    for (final i in grupos) {
      somaL += _tabuleiro.linhaDe(i);
      somaC += _tabuleiro.colunaDe(i);
    }
    final centro = Offset(
      (somaC / grupos.length + 0.5) * _lado,
      (somaL / grupos.length + 0.5) * _lado,
    );

    _festejos.add(
      _Festejo(
        centro: centro,
        texto: '+$ganho',
        estrelas: Pomar.estrelasPara(grupos.length),
        grande: grupos.length >= 5 || nivel >= 3,
        semente: _rnd.nextInt(10000),
      ),
    );
    _brilho.forward(from: 0);
  }

  void _recomecar() {
    Sons.i.toque();
    setState(() {
      _tabuleiro = Pomar.novo(rnd: _rnd);
      _pontos = 0;
      _restam = _jogadas;
      _rastreio.limpar();
      _aVibrar = const {};
      _arrastada = null;
      _alvo = null;
      _puxao = Offset.zero;
      _aColher = const {};
      _ocupado = false;
      _aviso = null;
      _festejos.clear();
    });
  }


  /// A Sorte no Pomar: aponta uma composição que a criança ainda não viu.
  ///
  /// Faz uma de duas coisas, e o que decide é quantas jogadas restam. Com
  /// folga, a composição **vibra** — ela vê onde está e faz a jogada, que é
  /// o que a ensina a olhar para o tabuleiro. Já à justa, nasce ali uma
  /// **peça especial**: com duas jogadas no bolso, uma dica não salva
  /// ninguém, e uma ajuda que chega tarde de mais não é ajuda.
  Future<void> _pedirSorte() async {
    if (_ocupado || _acabou) return;

    final jogada = _tabuleiro.jogadaPorTocar(_rastreio);
    final st = context.read<AppState>();

    if (jogada == null) {
      _dizer(semNadaParaMostrar);
      return;
    }
    if (!st.gastarSorte()) return;

    if (_restam > _poucasJogadas) {
      Sons.i.voz('voz-boa.mp3');
      setState(() => _aVibrar = jogada.envolvidas);
      _vibracao.forward(from: 0);
      _dizer('Olha bem para aqui. ${sobramSortes(st.sortes)}');
      return;
    }

    // Poucas jogadas: nasce um embrulho na peça que ela teria de mover. Ao
    // fazer a jogada, o embrulho rebenta o quadrado à volta — chega para
    // fechar a composição de uma vez.
    Sons.i.nivel();
    HapticFeedback.mediumImpact();
    setState(() {
      _tabuleiro = _tabuleiro.comEspecialEm(jogada.de, Especial.embrulho);
      _aVibrar = {jogada.de};
    });
    _vibracao.forward(from: 0);
    _dizer('Uma peça especial para ti. ${sobramSortes(st.sortes)}');
  }

  void _dizer(String texto) {
    ScaffoldMessenger.of(context)
      ..hideCurrentSnackBar()
      ..showSnackBar(
        SnackBar(
          content: Text(texto),
          backgroundColor: S.gm800,
          duration: const Duration(milliseconds: 2400),
        ),
      );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: S.gm950,
      appBar: AppBar(
        backgroundColor: S.gm950,
        foregroundColor: S.tx,
        elevation: 0,
        title: const Text('Pomar', style: TextStyle(fontSize: 17)),
        actions: [
          BotaoDeSorte(
            aoPedir: (_ocupado || _acabou) ? null : _pedirSorte,
          ),
        ],
      ),
      body: SafeArea(
        child: Column(
          children: [
            _placar(),
            if (_aviso != null)
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: Text(
                  _aviso!,
                  textAlign: TextAlign.center,
                  style: const TextStyle(color: S.gold, fontSize: 13.5),
                ),
              ),
            Expanded(
              child: Center(
                child: Padding(
                  padding: const EdgeInsets.all(10),
                  child: AnimatedBuilder(
                    animation: _abanao,
                    builder: (_, filho) {
                      final t = _abanao.value;
                      final dx = t == 0
                          ? 0.0
                          : (1 - t) * 9 * (t * 24 % 2 < 1 ? 1 : -1);
                      return Transform.translate(
                        offset: Offset(dx, 0),
                        child: filho,
                      );
                    },
                    child: _grelha(),
                  ),
                ),
              ),
            ),
            if (_acabou) _fim() else _rodape(),
          ],
        ),
      ),
    );
  }

  Widget _placar() => Padding(
    padding: const EdgeInsets.fromLTRB(20, 0, 20, 10),
    child: Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        _numero('$_pontos', 'pontos', S.chart),
        _numero('$_restam', _restam == 1 ? 'jogada' : 'jogadas',
            _restam <= 3 ? S.life : S.gold),
      ],
    ),
  );

  Widget _numero(String v, String rotulo, Color cor) => Column(
    crossAxisAlignment: CrossAxisAlignment.start,
    children: [
      Text(v,
          style: TextStyle(
              color: cor, fontSize: 26, fontWeight: FontWeight.w800)),
      Text(rotulo, style: const TextStyle(color: S.txMut, fontSize: 12)),
    ],
  );

  Widget _grelha() => LayoutBuilder(
    builder: (context, box) {
      final lado = min(
        box.maxWidth / _tabuleiro.colunas,
        box.maxHeight / _tabuleiro.linhas,
      );
      _lado = lado;
      // O gesto é da grelha inteira e não de cada casa: um arrasto começa
      // numa peça e acaba noutra, e com um detector por casa a primeira
      // ficava com o gesto todo e o dedo deixava de ser seguido ao sair
      // dela.
      return GestureDetector(
        onPanStart: (d) => _comecarArrasto(d.localPosition),
        onPanUpdate: (d) => _actualizarArrasto(d.localPosition),
        onPanEnd: (_) => _largar(),
        onPanCancel: _largar,
        child: SizedBox(
        width: lado * _tabuleiro.colunas,
        height: lado * _tabuleiro.linhas,
        child: Stack(
          children: [
            Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                for (var l = 0; l < _tabuleiro.linhas; l++)
                  Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      for (var c = 0; c < _tabuleiro.colunas; c++)
                        _casa(_tabuleiro.indice(l, c), lado),
                    ],
                  ),
              ],
            ),
            // As estrelinhas por cima do tabuleiro, sem apanhar toques.
            Positioned.fill(
              child: IgnorePointer(
                child: AnimatedBuilder(
                  animation: _brilho,
                  builder: (_, _) => CustomPaint(
                    painter: _PintorDeFestejo(
                      festejos: _festejos,
                      t: _brilho.value,
                      lado: lado,
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
        ),
      );
    },
  );

  /// Quanto é que esta casa anda por causa do arrasto.
  ///
  /// A peça puxada segue o dedo e a vizinha desliza ao contrário: são as
  /// duas a trocar de lugar, não uma a passar por cima da outra.
  Offset _desvioDe(int i) {
    final base = _solta.isAnimating || _solta.value > 0
        ? _puxaoAoLargar * _solta.value
        : _puxao;
    if (i == _arrastada) return base;
    if (i == _alvo) return -base;
    return Offset.zero;
  }

  Widget _casa(int i, double lado) {
    final peca = _tabuleiro.casas[i];
    final puxada = _arrastada == i;
    final aColher = _aColher.contains(i);
    final aVibrar = _aVibrar.contains(i);

    // A vibração da Sorte: um tremor pequeno e repetido, só nas casas
    // apontadas. Um destaque parado perdia-se no meio de quarenta e duas
    // peças coloridas; o que o olho apanha num tabuleiro cheio é movimento.
    final corpo = Container(
        width: lado,
        height: lado,
        padding: const EdgeInsets.all(2.5),
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 160),
          decoration: BoxDecoration(
            // A peça puxada acende-se: é a confirmação de que o dedo a
            // apanhou, e sem ela não se sabe qual das duas se está a mover.
            color: puxada
                ? S.chart.withValues(alpha: 0.24)
                : aVibrar
                ? S.gold.withValues(alpha: 0.22)
                : S.surface.withValues(alpha: 0.55),
            border: Border.all(
              color: puxada
                  ? S.chart
                  : aVibrar
                  ? S.gold
                  : S.line,
              width: puxada || aVibrar ? 2.5 : 1.2,
            ),
            borderRadius: BorderRadius.circular(S.rMd),
          ),
          alignment: Alignment.center,
          child: AnimatedScale(
            // A peça colhida encolhe até desaparecer: sem isto, as peças
            // trocavam de sítio de repente e não se percebia o que tinha
            // acontecido.
            scale: aColher ? 0.1 : 1,
            duration: const Duration(milliseconds: 210),
            curve: Curves.easeInBack,
            child: Stack(
              alignment: Alignment.center,
              children: [
                if (peca != null && peca.eEspecial)
                  MarcaDeEspecial(especial: peca.especial, lado: lado),
                Text(
                  peca?.produto.emoji ?? '',
                  style: TextStyle(fontSize: lado * 0.52),
                ),
              ],
            ),
          ),
        ),
      );

    return Transform.translate(
      offset: _desvioDe(i),
      child: aVibrar
          ? AnimatedBuilder(
              animation: _vibracao,
              builder: (_, filho) {
                final t = _vibracao.value;
                final forca = (1 - t) * lado * 0.10;
                final dx = sin(t * pi * 18) * forca;
                return Transform.translate(
                  offset: Offset(dx, 0),
                  child: filho,
                );
              },
              child: corpo,
            )
          : corpo,
    );
  }

  Widget _rodape() => const Padding(
    padding: EdgeInsets.fromLTRB(20, 4, 20, 16),
    child: Text(
      'Arrasta uma peça para a do lado. Três iguais em linha colhem-se — '
      'quatro ou cinco deixam uma peça especial.',
      textAlign: TextAlign.center,
      style: TextStyle(color: S.txSoft, fontSize: 13, height: 1.35),
    ),
  );

  Widget _fim() => Padding(
    padding: const EdgeInsets.fromLTRB(20, 0, 20, 18),
    child: Column(
      children: [
        Image.asset(RobyPose.orgulhoso.path, width: 84),
        const SizedBox(height: 8),
        Text(
          'Fizeste $_pontos pontos!',
          style: const TextStyle(
            color: S.chart,
            fontSize: 18,
            fontWeight: FontWeight.w700,
          ),
        ),
        const SizedBox(height: 12),
        Row(
          children: [
            Expanded(
              child: _botao('Sair', () => Navigator.of(context).pop(),
                  cor: S.surface, corTexto: S.txSoft),
            ),
            const SizedBox(width: 10),
            Expanded(
              flex: 2,
              child: _botao('Jogar outra vez', _recomecar,
                  cor: S.chart, corTexto: S.onChart),
            ),
          ],
        ),
      ],
    ),
  );

  Widget _botao(
    String texto,
    VoidCallback aoTocar, {
    required Color cor,
    required Color corTexto,
  }) => GestureDetector(
    onTap: aoTocar,
    child: Container(
      height: 50,
      decoration: BoxDecoration(
        color: cor,
        border: Border.all(color: S.line, width: 1.5),
        borderRadius: BorderRadius.circular(S.rMd),
      ),
      alignment: Alignment.center,
      child: Text(
        texto,
        style: TextStyle(
          fontSize: 17,
          fontWeight: FontWeight.w700,
          color: corTexto,
        ),
      ),
    ),
  );
}

/// Uma colheita a ser festejada: onde foi, quanto valeu, e com que estardalhaço.
class _Festejo {
  /// Centro da colheita, em píxeis dentro da grelha.
  final Offset centro;

  /// O número que salta — "+220".
  final String texto;

  final int estrelas;

  /// Cinco peças ou mais, ou cascata funda: merece estrelas maiores e mais
  /// longe. É a diferença entre "acertaste" e "isto foi bom".
  final bool grande;

  /// Semente do desvio das estrelas. Fixa por festejo, para as estrelinhas
  /// não saltarem de sítio a cada frame.
  final int semente;

  const _Festejo({
    required this.centro,
    required this.texto,
    required this.estrelas,
    required this.grande,
    required this.semente,
  });
}

/// Desenha as estrelinhas e o número por cima do tabuleiro.
///
/// Num pintor e não em widgets: são dezenas de figuras a mexer ao mesmo
/// tempo numa cascata longa, e cada uma como widget faria a árvore inteira
/// ser reconstruída a sessenta vezes por segundo num telemóvel barato.
class _PintorDeFestejo extends CustomPainter {
  final List<_Festejo> festejos;
  final double t;
  final double lado;

  _PintorDeFestejo({
    required this.festejos,
    required this.t,
    required this.lado,
  });

  /// Ruído estável: a mesma estrela sai sempre na mesma direcção.
  double _acaso(int semente, int n) {
    final h = math.sin(semente * 12.9898 + n * 78.233) * 43758.5453;
    return h - h.floor();
  }

  /// Uma estrela de cinco pontas, centrada na origem.
  Path _estrela(double raio) {
    final p = Path();
    for (var i = 0; i < 10; i++) {
      final r = i.isEven ? raio : raio * 0.45;
      final a = -math.pi / 2 + i * math.pi / 5;
      final ponto = Offset(math.cos(a) * r, math.sin(a) * r);
      i == 0 ? p.moveTo(ponto.dx, ponto.dy) : p.lineTo(ponto.dx, ponto.dy);
    }
    p.close();
    return p;
  }

  @override
  void paint(Canvas canvas, Size size) {
    if (t <= 0 || festejos.isEmpty) return;

    for (final f in festejos) {
      // As estrelas saem depressa e travam, como faíscas — não voam a
      // velocidade constante, que pareceria confetti a cair.
      final avanco = 1 - math.pow(1 - t, 2.2).toDouble();
      final alcance = (f.grande ? 1.5 : 1.0) * lado * 1.5;

      for (var k = 0; k < f.estrelas; k++) {
        final angulo = _acaso(f.semente, k) * 2 * math.pi;
        final distancia = alcance * (0.45 + _acaso(f.semente, k + 100) * 0.75);
        final raio =
            (f.grande ? 8.0 : 6.0) * (1 - t * 0.55) *
                (0.7 + _acaso(f.semente, k + 200) * 0.6);

        final centro = f.centro +
            Offset(math.cos(angulo), math.sin(angulo)) * distancia * avanco;

        canvas.save();
        canvas.translate(centro.dx, centro.dy);
        canvas.rotate(angulo + t * 2.4);
        canvas.drawPath(
          _estrela(raio),
          Paint()
            ..color = (f.grande ? S.gold : S.chart)
                .withValues(alpha: (1 - t).clamp(0.0, 1.0) * 0.95),
        );
        canvas.restore();
      }

      // O número sobe e desvanece. Sobe pouco: o objectivo é dizer quanto
      // valeu, não tapar o tabuleiro.
      final tp = TextPainter(
        text: TextSpan(
          text: f.texto,
          style: TextStyle(
            fontSize: f.grande ? 24 : 19,
            fontWeight: FontWeight.w800,
            color: (f.grande ? S.gold : S.chart)
                .withValues(alpha: (1 - t * t).clamp(0.0, 1.0)),
            shadows: const [
              Shadow(color: Color(0xCC000000), blurRadius: 6),
            ],
          ),
        ),
        textDirection: TextDirection.ltr,
      )..layout();

      tp.paint(
        canvas,
        f.centro - Offset(tp.width / 2, tp.height / 2 + 34 * avanco),
      );
    }
  }

  @override
  bool shouldRepaint(_PintorDeFestejo old) =>
      old.t != t || old.festejos.length != festejos.length;
}
