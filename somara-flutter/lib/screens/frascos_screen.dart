import 'dart:async';
import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import '../models/carteira.dart';
import '../models/escadaria.dart';
import '../models/frascos.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/mesa_de_frascos.dart';
import '../widgets/roby.dart';

/// «Water R Sort»: arrumar os líquidos até cada frasco ter uma cor só.
///
/// É o único joguinho que não ensina matéria nenhuma, e isso é deliberado.
/// O que treina é planear com antecedência: uma jogada que resolve agora
/// pode fechar a única saída daqui a três, e a criança tem de ver isso
/// antes de tocar. É a mesma cabeça que a conta de dividir pede, sem ser
/// uma conta de dividir.
///
/// O que se compra com ouro, e o que não se compra
/// -----------------------------------------------
/// Um frasco extra, saltar o nível, e desfazer depois dos três de graça —
/// tudo pago com o ouro que se ganha a estudar. Não há anúncios, e não é
/// por esquecimento: um anúncio descarrega-se, e em Lichinga paga-se ao
/// megabyte; traz uma dependência pesada que pode partir a app numa
/// actualização; e mostra a crianças de nove anos o que uma rede de
/// anúncios decidir. O ouro já existe, já se ganha a estudar, e é a única
/// moeda que faz sentido aqui.
class FrascosScreen extends StatefulWidget {
  /// Por onde começar. Nulo entra pelo degrau guardado no estado.
  final int? nivel;

  const FrascosScreen({super.key, this.nivel});

  @override
  State<FrascosScreen> createState() => _FrascosScreenState();
}

class _FrascosScreenState extends State<FrascosScreen>
    with TickerProviderStateMixin {
  late Frascos _jogo;
  late int _nivel;

  /// O frasco levantado à espera de destino.
  int? _seleccionado;

  /// As mesas anteriores, para o Desfazer. Guarda-se a mesa inteira e não a
  /// jogada: são meia dúzia de listas curtas, e desfazer passa a ser voltar
  /// atrás em vez de calcular o contrário de um despejo.
  final _historico = <Frascos>[];

  int _jogadas = 0;

  /// Quantos Desfazer já se usaram neste nível. Os primeiros três são de
  /// graça.
  int _desfeitos = 0;

  /// Frascos extra comprados para este nível. Sobrevivem ao Recomeçar —
  /// foram pagos — e morrem quando o nível muda.
  int _extras = 0;

  /// Verdadeiro entre ganhar e o degrau seguinte entrar.
  bool _aPassar = false;

  late final AnimationController _anim;
  late final AnimationController _brilho;
  int? _brilhoEm;

  /// O despejo a decorrer, sem o tempo — o tempo vem de [_anim].
  ({int de, int para, int quantos, CorDoLiquido cor, Offset? desde})?
      _emCurso;

  Arrasto? _arrasto;
  int? _alvo;

  @override
  void initState() {
    super.initState();
    _anim = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 920),
    );
    _brilho = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 700),
    );
    Sons.i.definirAmbiente(Trilha.relaxar);
    _nivel = widget.nivel ?? context.read<AppState>().nivelDe(Jogo.frascos);
    _montarNivel();
  }

  @override
  void dispose() {
    _anim.dispose();
    _brilho.dispose();
    Sons.i.definirAmbiente(Trilha.principal);
    super.dispose();
  }

  void _montarNivel() {
    var mesa = Frascos.doNivel(_nivel);
    for (var i = 0; i < _extras; i++) {
      mesa = mesa.comFrascoVazio();
    }
    _jogo = mesa;
    _historico.clear();
    _seleccionado = null;
    _emCurso = null;
    _arrasto = null;
    _alvo = null;
    _jogadas = 0;
    _desfeitos = 0;
    _aPassar = false;
  }

  /// Muda de degrau: o que foi comprado para este nível fica cá.
  void _irParaONivel(int nivel) {
    _nivel = nivel;
    _extras = 0;
    _montarNivel();
  }

  /// Empancado: ainda não ganhou e já não há jogada nenhuma.
  bool get _preso => !_jogo.ganho && !_jogo.temJogada;

  bool get _ocupado => _emCurso != null || _aPassar;

  bool get _desfazerEDeGraca => _desfeitos < PrecoNosFrascos.desfazeresGratis;

  // ------------------------------------------------------------ toque

  void _tocar(int i) {
    if (_ocupado || _jogo.ganho) return;

    final escolhido = _seleccionado;
    if (escolhido == null) {
      // Levantar um frasco vazio não leva a lado nenhum.
      if (_jogo.frascos[i].vazio) return;
      Sons.i.toque();
      setState(() => _seleccionado = i);
      return;
    }

    if (escolhido == i) {
      Sons.i.toque();
      setState(() => _seleccionado = null);
      return;
    }

    if (_jogo.podeDespejar(escolhido, i)) {
      unawaited(_despejar(escolhido, i));
      return;
    }

    // Não dava. Em vez de não fazer nada — que a criança lê como o jogo
    // estar avariado — passa-se a escolha para o frasco em que ela tocou.
    Sons.i.errado();
    setState(() => _seleccionado = _jogo.frascos[i].vazio ? null : i);
  }

  // ---------------------------------------------------------- arrasto

  void _aoArrastar(int i, Offset centro, int? alvo) {
    if (_ocupado || _jogo.ganho || _jogo.frascos[i].vazio) return;
    setState(() {
      _seleccionado = i;
      _arrasto = (frasco: i, centro: centro);
      _alvo = alvo;
    });
  }

  void _aoLargar(int i, int? alvo) {
    final a = _arrasto;
    if (a == null) return;
    setState(() {
      _arrasto = null;
      _alvo = null;
    });
    if (alvo != null && alvo != i && _jogo.podeDespejar(i, alvo)) {
      unawaited(_despejar(i, alvo, desde: a.centro));
    } else if (alvo != null && alvo != i) {
      // Largou em cima de um frasco onde não dá. Fica levantado, à espera
      // de outro destino — e ouve-se que não deu.
      Sons.i.errado();
    }
  }

  // ---------------------------------------------------------- despejo

  Future<void> _despejar(int de, int para, {Offset? desde}) async {
    final quantos = _jogo.quantosDespeja(de, para);
    final cor = _jogo.frascos[de].topo!;

    _historico.add(_jogo);
    setState(() {
      _emCurso = (de: de, para: para, quantos: quantos, cor: cor, desde: desde);
      _seleccionado = null;
    });

    Sons.i.toque();
    await _anim.forward(from: 0);
    if (!mounted) return;

    final depois = _jogo.despejar(de, para);
    setState(() {
      _jogo = depois;
      _emCurso = null;
      _jogadas++;
    });

    final destino = depois.frascos[para];
    if (destino.cheio && destino.deUmaCor) {
      Sons.i.certo();
      HapticFeedback.lightImpact();
      _brilhoEm = para;
      unawaited(_brilho.forward(from: 0));
    }

    if (depois.ganho) {
      Sons.i.nivel();
      // Arrumar uma cor vale como uma resposta certa de lição.
      context.read<AppState>().concluirTreino(depois.params.cores);
      unawaited(_passarAoSeguinte());
    }
  }

  Future<void> _passarAoSeguinte() async {
    setState(() => _aPassar = true);
    await Future<void>.delayed(const Duration(milliseconds: 1600));
    if (!mounted) return;
    final proximo = context.read<AppState>().subirNivelDe(Jogo.frascos);
    setState(() => _irParaONivel(proximo));
  }

  // --------------------------------------------------------- ajudas

  Future<void> _desfazer() async {
    if (_ocupado || _historico.isEmpty) return;
    if (!_desfazerEDeGraca) {
      final pagou = await _pedirOuro(
        titulo: 'Desfazer',
        texto: 'Os ${PrecoNosFrascos.desfazeresGratis} de graça deste nível '
            'já foram. A partir daqui cada Desfazer custa '
            '${PrecoNosFrascos.desfazer} moeda de ouro.',
        preco: PrecoNosFrascos.desfazer,
      );
      if (!pagou || !mounted) return;
    }
    Sons.i.toque();
    setState(() {
      _jogo = _historico.removeLast();
      _seleccionado = null;
      _jogadas = math.max(0, _jogadas - 1);
      _desfeitos++;
    });
  }

  /// Volta ao tabuleiro com que ela começou. É o mesmo porque o nível é
  /// determinista — ver [Frascos.doNivel]. Os frascos comprados ficam.
  void _recomecar() {
    if (_ocupado) return;
    Sons.i.toque();
    setState(_montarNivel);
  }

  Future<void> _comprarFrasco() async {
    if (_ocupado || _extras >= PrecoNosFrascos.maximoDeExtras) return;
    final pagou = await _pedirOuro(
      titulo: 'Frasco extra',
      texto: 'Mais um frasco vazio na mesa, só para este nível. Fica cá '
          'mesmo que recomeces.',
      preco: PrecoNosFrascos.frascoExtra,
    );
    if (!pagou || !mounted) return;
    Sons.i.certo();
    setState(() {
      _extras++;
      _jogo = _jogo.comFrascoVazio();
      // O histórico também ganha o frasco: desfazer uma jogada não pode
      // tirar da mesa o que ela pagou.
      for (var i = 0; i < _historico.length; i++) {
        _historico[i] = _historico[i].comFrascoVazio();
      }
      _seleccionado = null;
    });
  }

  Future<void> _saltar() async {
    if (_ocupado || _nivel >= nivelMaximo) return;
    final pagou = await _pedirOuro(
      titulo: 'Saltar o nível',
      texto: 'Passas já para o nível ${_nivel + 1}. Não conta como treino '
          'nem paga ouro — é só para não ficares aqui parado.',
      preco: PrecoNosFrascos.saltar,
    );
    if (!pagou || !mounted) return;
    Sons.i.salto();
    final proximo = context.read<AppState>().subirNivelDe(Jogo.frascos);
    setState(() => _irParaONivel(proximo));
  }

  /// Pergunta, cobra, e diz se cobrou. Quando o ouro não chega, explica
  /// quanto falta e de onde vem — a resposta a «não dá» nunca é só «não».
  Future<bool> _pedirOuro({
    required String titulo,
    required String texto,
    required int preco,
  }) async {
    final st = context.read<AppState>();
    final tem = st.carteira.gc;
    final chega = tem >= preco;

    final sim = await showModalBottomSheet<bool>(
      context: context,
      backgroundColor: S.gm900,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(S.rLg)),
      ),
      builder: (ctx) => _FolhaDeCompra(
        titulo: titulo,
        texto: texto,
        preco: preco,
        tem: tem,
        chega: chega,
      ),
    );
    if (sim != true || !chega) return false;
    return st.gastar(Moeda.gc, preco);
  }

  // ------------------------------------------------------------ ecrã

  @override
  Widget build(BuildContext context) {
    final ouro = context.watch<AppState>().carteira.gc;

    return Scaffold(
      backgroundColor: S.gm950,
      appBar: AppBar(
        backgroundColor: S.gm950,
        foregroundColor: S.tx,
        elevation: 0,
        title: Text(
          'Water R Sort · Nível $_nivel',
          style: const TextStyle(fontSize: 16),
        ),
        actions: [
          Padding(
            padding: const EdgeInsets.only(right: 12),
            child: Center(child: _ChipDeOuro(ouro)),
          ),
        ],
      ),
      body: SafeArea(
        child: Column(
          children: [
            _cabecalho(),
            Expanded(
              child: Padding(
                padding: const EdgeInsets.fromLTRB(12, 6, 12, 6),
                child: Container(
                  decoration: BoxDecoration(
                    color: S.gm900,
                    border: Border.all(color: S.line, width: 1.5),
                    borderRadius: BorderRadius.circular(S.rLg),
                  ),
                  padding: const EdgeInsets.fromLTRB(10, 22, 10, 12),
                  child: AnimatedBuilder(
                    animation: Listenable.merge([_anim, _brilho]),
                    builder: (context, _) {
                      final c = _emCurso;
                      return MesaDeFrascos(
                        jogo: _jogo,
                        seleccionado: _seleccionado,
                        despejo: c == null
                            ? null
                            : (
                                de: c.de,
                                para: c.para,
                                quantos: c.quantos,
                                cor: c.cor,
                                t: _anim.value,
                                desde: c.desde,
                              ),
                        arrasto: _arrasto,
                        alvo: _alvo,
                        alvoServe: _alvo != null &&
                            _arrasto != null &&
                            _jogo.podeDespejar(_arrasto!.frasco, _alvo!),
                        brilho: _brilho.isAnimating && _brilhoEm != null
                            ? (frasco: _brilhoEm!, t: _brilho.value)
                            : null,
                        aoTocar: _tocar,
                        aoArrastar: _aoArrastar,
                        aoLargar: _aoLargar,
                      );
                    },
                  ),
                ),
              ),
            ),
            if (_jogo.ganho) _fim() else _rodape(),
          ],
        ),
      ),
    );
  }

  Widget _cabecalho() {
    final (icone, cor, texto) = _dizer();
    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 2, 16, 2),
      child: Row(
        children: [
          Icon(icone, color: cor, size: 18),
          const SizedBox(width: 8),
          Expanded(
            child: Text(
              texto,
              style: TextStyle(
                color: cor,
                fontSize: 13.5,
                fontWeight: _jogo.ganho || _preso
                    ? FontWeight.w700
                    : FontWeight.w400,
                height: 1.3,
              ),
            ),
          ),
        ],
      ),
    );
  }

  (IconData, Color, String) _dizer() {
    if (_jogo.ganho) {
      return (
        Icons.celebration_rounded,
        S.chart,
        'Arrumado! ${contagemDeJogadas(_jogadas)}.',
      );
    }
    if (_preso) {
      return (
        Icons.lock_rounded,
        S.gold,
        'Já não há jogada possível. Desfaz, recomeça, ou compra um frasco '
            'extra.',
      );
    }
    if (_arrasto != null) {
      if (_alvo == null) {
        return (
          Icons.pan_tool_alt_rounded,
          S.txSoft,
          'Arrasta até ao frasco onde queres despejar.',
        );
      }
      final serve = _jogo.podeDespejar(_arrasto!.frasco, _alvo!);
      return serve
          ? (Icons.check_circle_rounded, S.green300, 'Larga para despejar.')
          : (
              Icons.block_rounded,
              S.life,
              'Aqui não dá: só para um frasco vazio ou com a mesma cor em '
                  'cima.',
            );
    }
    if (_seleccionado != null) {
      return (
        Icons.touch_app_rounded,
        S.txSoft,
        'Agora toca no frasco para onde queres despejar — ou arrasta-o.',
      );
    }
    return (
      Icons.lightbulb_outline_rounded,
      S.txSoft,
      'Deixa cada frasco com uma cor só. Toca num frasco e depois no '
          'destino, ou arrasta-o.',
    );
  }

  Widget _rodape() {
    final extrasEsgotados = _extras >= PrecoNosFrascos.maximoDeExtras;
    final ultimo = _nivel >= nivelMaximo;
    return Padding(
      padding: const EdgeInsets.fromLTRB(12, 2, 12, 10),
      child: Column(
        children: [
          Text(
            'Cores arrumadas: ${_jogo.coresFeitas} de ${_jogo.params.cores}'
            '${_jogadas > 0 ? "  ·  ${contagemDeJogadas(_jogadas)}" : ""}',
            textAlign: TextAlign.center,
            style: const TextStyle(color: S.txMut, fontSize: 12.5),
          ),
          const SizedBox(height: 8),
          // IntrinsicHeight para os quatro ficarem da mesma altura: um
          // rotulo sem detalhe por baixo ("Recomecar") nao pode deixar o
          // botao mais baixo do que os vizinhos. Sem ele, o stretch de uma
          // Row dentro de uma Column pede altura infinita e rebenta.
          IntrinsicHeight(
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
              Expanded(
                child: _Accao(
                  icone: Icons.undo_rounded,
                  rotulo: 'Desfazer',
                  detalhe: _desfazerEDeGraca
                      ? '${PrecoNosFrascos.desfazeresGratis - _desfeitos} '
                          'grátis'
                      : '${PrecoNosFrascos.desfazer} GC',
                  activo: _historico.isNotEmpty && !_ocupado,
                  aoTocar: _desfazer,
                ),
              ),
              const SizedBox(width: 6),
              Expanded(
                child: _Accao(
                  icone: Icons.refresh_rounded,
                  rotulo: 'Recomeçar',
                  detalhe: '',
                  activo: (_jogadas > 0 || _historico.isNotEmpty) && !_ocupado,
                  aoTocar: _recomecar,
                ),
              ),
              const SizedBox(width: 6),
              Expanded(
                child: _Accao(
                  icone: Icons.science_rounded,
                  rotulo: 'Frasco extra',
                  detalhe: extrasEsgotados
                      ? 'máx. ${PrecoNosFrascos.maximoDeExtras}'
                      : '${PrecoNosFrascos.frascoExtra} GC',
                  activo: !extrasEsgotados && !_ocupado,
                  aoTocar: _comprarFrasco,
                  pago: !extrasEsgotados,
                ),
              ),
              const SizedBox(width: 6),
              Expanded(
                child: _Accao(
                  icone: Icons.skip_next_rounded,
                  rotulo: 'Saltar',
                  detalhe: ultimo ? 'último' : '${PrecoNosFrascos.saltar} GC',
                  activo: !ultimo && !_ocupado,
                  aoTocar: _saltar,
                  pago: !ultimo,
                ),
              ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _fim() => Padding(
        padding: const EdgeInsets.fromLTRB(16, 0, 16, 14),
        child: Row(
          children: [
            Image.asset(RobyPose.orgulhoso.path, width: 64),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Nível $_nivel feito!',
                    style: const TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.w700,
                      color: S.chart,
                    ),
                  ),
                  const SizedBox(height: 3),
                  Text(
                    _nivel >= nivelMaximo
                        ? 'Chegaste ao fim da escadaria.'
                        : 'Vem aí o ${_nivel + 1}…',
                    style: const TextStyle(color: S.txSoft, fontSize: 13.5),
                  ),
                ],
              ),
            ),
          ],
        ),
      );
}

/// «1 jogada» e «7 jogadas». O singular importa: a app fala português a
/// crianças que estão a aprender a escrevê-lo.
String contagemDeJogadas(int n) => n == 1 ? '1 jogada' : '$n jogadas';

/// O saldo de ouro, na barra de cima.
class _ChipDeOuro extends StatelessWidget {
  final int ouro;
  const _ChipDeOuro(this.ouro);

  @override
  Widget build(BuildContext context) => Container(
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
        decoration: BoxDecoration(
          color: S.gm900,
          border: Border.all(color: S.gold.withValues(alpha: 0.6), width: 1.5),
          borderRadius: BorderRadius.circular(S.rPill),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Icon(Icons.monetization_on_rounded, color: S.gold, size: 17),
            const SizedBox(width: 5),
            Text(
              '$ouro',
              style: const TextStyle(
                color: S.gold,
                fontSize: 14,
                fontWeight: FontWeight.w800,
              ),
            ),
          ],
        ),
      );
}

/// Um botão do rodapé: ícone, nome, e por baixo o que custa ou quantos
/// restam. Apagado quando não há nada a fazer com ele — um Desfazer que não
/// desfaz nada mente à criança sobre o que aconteceu.
class _Accao extends StatelessWidget {
  final IconData icone;
  final String rotulo;
  final String detalhe;
  final bool activo;
  final bool pago;
  final VoidCallback aoTocar;

  const _Accao({
    required this.icone,
    required this.rotulo,
    required this.detalhe,
    required this.activo,
    required this.aoTocar,
    this.pago = false,
  });

  @override
  Widget build(BuildContext context) => GestureDetector(
        onTap: activo ? aoTocar : null,
        behavior: HitTestBehavior.opaque,
        child: Opacity(
          opacity: activo ? 1 : 0.38,
          child: Container(
            padding: const EdgeInsets.symmetric(vertical: 7, horizontal: 4),
            decoration: BoxDecoration(
              color: S.gm900,
              border: Border.all(
                color: pago && activo ? S.gold.withValues(alpha: 0.55) : S.line,
                width: 1.5,
              ),
              borderRadius: BorderRadius.circular(S.rMd),
            ),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(icone, color: pago ? S.gold : S.chart, size: 20),
                const SizedBox(height: 2),
                // Encolhe em vez de partir: "Recomeçar" a 12 px não cabe em
                // setenta pixels num telemóvel barato.
                FittedBox(
                  fit: BoxFit.scaleDown,
                  child: Text(
                    rotulo,
                    maxLines: 1,
                    style: const TextStyle(
                      color: S.tx,
                      fontSize: 12,
                      fontWeight: FontWeight.w700,
                    ),
                  ),
                ),
                if (detalhe.isNotEmpty)
                  FittedBox(
                    fit: BoxFit.scaleDown,
                    child: Text(
                      detalhe,
                      maxLines: 1,
                      style: TextStyle(
                        color: pago ? S.gold : S.txMut,
                        fontSize: 10.5,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
              ],
            ),
          ),
        ),
      );
}

/// A folha que pergunta antes de cobrar.
class _FolhaDeCompra extends StatelessWidget {
  final String titulo;
  final String texto;
  final int preco;
  final int tem;
  final bool chega;

  const _FolhaDeCompra({
    required this.titulo,
    required this.texto,
    required this.preco,
    required this.tem,
    required this.chega,
  });

  @override
  Widget build(BuildContext context) => SafeArea(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(22, 18, 22, 20),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Expanded(
                    child: Text(
                      titulo,
                      style: const TextStyle(
                        color: S.tx,
                        fontSize: 19,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                  ),
                  const Icon(Icons.monetization_on_rounded,
                      color: S.gold, size: 20),
                  const SizedBox(width: 4),
                  Text(
                    '$preco',
                    style: const TextStyle(
                      color: S.gold,
                      fontSize: 18,
                      fontWeight: FontWeight.w800,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 8),
              Text(
                texto,
                style: const TextStyle(
                  color: S.txSoft,
                  fontSize: 14.5,
                  height: 1.4,
                ),
              ),
              const SizedBox(height: 10),
              Text(
                chega
                    ? 'Tens $tem. Ficas com ${tem - preco}.'
                    : 'Tens $tem — faltam-te ${preco - tem}. O ouro ganha-se '
                        'a estudar: cada nível da amarelinha paga.',
                style: TextStyle(
                  color: chega ? S.txMut : S.gold,
                  fontSize: 13.5,
                  height: 1.4,
                  fontWeight: chega ? FontWeight.w400 : FontWeight.w600,
                ),
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Expanded(
                    child: _botao(
                      chega ? 'Agora não' : 'Está bem',
                      () => Navigator.of(context).pop(false),
                      cor: S.surface,
                      corTexto: S.txSoft,
                    ),
                  ),
                  if (chega) ...[
                    const SizedBox(width: 10),
                    Expanded(
                      flex: 2,
                      child: _botao(
                        'Confirmar',
                        () => Navigator.of(context).pop(true),
                        cor: S.chart,
                        corTexto: S.onChart,
                      ),
                    ),
                  ],
                ],
              ),
            ],
          ),
        ),
      );

  Widget _botao(
    String texto,
    VoidCallback aoTocar, {
    required Color cor,
    required Color corTexto,
  }) =>
      GestureDetector(
        onTap: () {
          Sons.i.toque();
          aoTocar();
        },
        child: Container(
          height: 48,
          decoration: BoxDecoration(
            color: cor,
            border: Border.all(color: S.line, width: 1.5),
            borderRadius: BorderRadius.circular(S.rMd),
          ),
          alignment: Alignment.center,
          child: Text(
            texto,
            style: TextStyle(
              fontSize: 16,
              fontWeight: FontWeight.w700,
              color: corTexto,
            ),
          ),
        ),
      );
}
