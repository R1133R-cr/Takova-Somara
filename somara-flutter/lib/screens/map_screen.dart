import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/content.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/hopscotch_board.dart';
import '../widgets/roby.dart';
import 'lesson_screen.dart';

/// A amarelinha. Corre de baixo para cima — ENTRADA em baixo, META em cima —
/// como o jogo de rua a que se refere, e ao contrário do scroll de cima para
/// baixo típico das apps do género.
class MapScreen extends StatefulWidget {
  const MapScreen({super.key});
  @override
  State<MapScreen> createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen> with SingleTickerProviderStateMixin {
  late final AnimationController _glow;
  final _scroll = ScrollController();
  bool _centrouInicial = false;

  static const _rowH = 124.0;
  static const _cellW = 78.0;
  static const _cellH = 74.0;
  static const _lateral = 108.0; // amplitude máxima da onda
  static const _padTopo = 96.0;
  static const _padBase = 92.0;

  @override
  void initState() {
    super.initState();
    _glow = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1600),
    )..repeat(reverse: true);
  }

  @override
  void dispose() {
    _glow.dispose();
    _scroll.dispose();
    super.dispose();
  }

  /// Fase da onda: radianos por nível. 2π/6 fecha uma volta completa a cada
  /// seis níveis — cerca de um S inteiro por ecrã, que é o que faz a
  /// amarelinha ler como cobra. Com passo menor a onda demora tanto a virar
  /// que os primeiros níveis caem todos do mesmo lado e o ecrã fica torto;
  /// com passo maior volta a ser um ziguezague de esquerda para direita.
  static const _passoOnda = 1.047; // 2π/6

  /// Com o rótulo por baixo do quadrado (e não ao lado), a largura toda fica
  /// livre para a onda. Só se guarda uma margem pequena para o quadrado
  /// inclinado não encostar à borda.
  double _amplitude(double largura) =>
      math.min(_lateral, largura / 2 - _cellW / 2 - 18);

  /// Deslocamento lateral do nível i. É a onda que faz o tabuleiro
  /// serpentear como uma cobra em vez de saltar de lado para lado.
  double _desvio(int i, double largura) =>
      math.sin(i * _passoOnda) * _amplitude(largura);

  /// Converte o índice do nível na posição do quadrado no tabuleiro.
  /// O índice 0 fica em baixo, por isso a altura conta ao contrário.
  Rect _rectDe(int i, int total, double largura) {
    final centroX = largura / 2 + _desvio(i, largura);
    final y = _padTopo + (total - 1 - i) * _rowH;
    return Rect.fromCenter(
      center: Offset(centroX, y + _cellH / 2),
      width: _cellW,
      height: _cellH,
    );
  }

  /// Inclinação do quadrado: alinhada com a tangente da onda naquele ponto.
  /// Sem isto os quadrados ficam direitos sobre uma linha curva, o que dá
  /// logo o aspecto de caixas pousadas em cima de um caminho, em vez de um
  /// tabuleiro riscado no chão a acompanhar a curva.
  double _inclinacao(int i, double largura) {
    final derivada = math.cos(i * _passoOnda) * _amplitude(largura) * _passoOnda;
    // A subida é constante (_rowH por nível), logo o ângulo do percurso sai
    // do declive lateral face a essa subida. Limitado para nunca exagerar.
    return (math.atan2(derivada, _rowH) * 0.55).clamp(-0.34, 0.34);
  }

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final niveis = st.niveis;
    final actual = st.nivelActual;
    final alturaTotal = _padTopo + niveis.length * _rowH + _padBase;

    return Column(
      children: [
        _tabsDisciplina(st),
        Expanded(
          child: LayoutBuilder(
            builder: (context, box) {
              final largura = box.maxWidth;

              final cells = [
                for (var i = 0; i < niveis.length; i++)
                  BoardCell(
                    rect: _rectDe(i, niveis.length, largura),
                    index: i,
                    angle: _inclinacao(i, largura),
                    state: st.nivelFeito(i)
                        ? CellState.done
                        : (i == actual ? CellState.current : CellState.locked),
                  ),
              ];

              // Ao entrar, centra no quadrado onde o Roby está — sem animação,
              // para não parecer que a app "saltou" sozinha ao abrir.
              if (!_centrouInicial) {
                _centrouInicial = true;
                WidgetsBinding.instance.addPostFrameCallback((_) {
                  if (!_scroll.hasClients) return;
                  final alvo = cells[actual].rect.center.dy - box.maxHeight / 2;
                  _scroll.jumpTo(alvo.clamp(0.0, _scroll.position.maxScrollExtent));
                });
              }

              return SingleChildScrollView(
                controller: _scroll,
                child: SizedBox(
                  height: alturaTotal,
                  width: largura,
                  child: Stack(
                    clipBehavior: Clip.none,
                    children: [
                      Positioned.fill(
                        child: AnimatedBuilder(
                          animation: _glow,
                          builder: (_, _) => CustomPaint(
                            painter: HopscotchPainter(
                              cells: cells,
                              glow: _glow.value,
                            ),
                          ),
                        ),
                      ),
                      _marcador(
                        largura: largura,
                        y: 26,
                        child: _badgeMeta(st),
                      ),
                      _marcador(
                        largura: largura,
                        y: alturaTotal - _padBase + 26,
                        child: _badgeEntrada(),
                      ),
                      for (var i = 0; i < niveis.length; i++)
                        ..._quadrado(st, cells[i], niveis[i], largura),
                      RobyToken(
                        position: cells[actual].rect.center,
                        pose: RobyPose.token,
                        size: 58,
                      ),
                    ],
                  ),
                ),
              );
            },
          ),
        ),
      ],
    );
  }

  List<Widget> _quadrado(
    AppState st,
    BoardCell cell,
    ({Unidade unit, Nivel nivel}) lv,
    double largura,
  ) {
    final bloqueado = cell.state == CellState.locked;
    final feito = cell.state == CellState.done;
    final r = cell.rect;

    return [
      // Número (ou ✓) por cima do quadrado pintado.
      Positioned(
        left: r.left,
        top: r.top,
        width: r.width,
        height: r.height,
        child: Material(
          color: Colors.transparent,
          child: InkWell(
            borderRadius: BorderRadius.circular(14),
            onTap: bloqueado
                ? null
                : () => Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (_) => LessonScreen(indice: cell.index),
                      ),
                    ),
            child: Center(
              // O número acompanha a inclinação do quadrado; se ficasse a
              // direito dentro de uma casa torta, denunciava logo que a
              // casa é um rectângulo rodado e não um risco no chão.
              child: Transform.rotate(
                angle: cell.angle,
                child: Opacity(
                  opacity: bloqueado ? 0.45 : 1,
                  child: feito
                      ? const Icon(Icons.check_rounded, color: Colors.white, size: 34)
                      : Text(
                          '${cell.index + 1}',
                          style: TextStyle(
                            fontSize: 26,
                            fontWeight: FontWeight.w700,
                            color: cell.state == CellState.current
                                ? S.onChart
                                : S.chart,
                          ),
                        ),
                ),
              ),
            ),
          ),
        ),
      ),
      // Rótulo centrado por baixo do quadrado. Ao lado obrigava a apertar a
      // onda para caber o texto; por baixo pertence visivelmente àquela casa
      // e deixa a largura toda para a amarelinha serpentear.
      Positioned(
        left: r.center.dx - 68,
        top: r.bottom + 4,
        width: 136,
        child: Opacity(
          opacity: bloqueado ? 0.45 : 1,
          child: Text(
            lv.nivel.titulo,
            textAlign: TextAlign.center,
            maxLines: 2,
            overflow: TextOverflow.ellipsis,
            style: const TextStyle(fontSize: 12.5, color: S.txSoft, height: 1.25),
          ),
        ),
      ),
    ];
  }

  Widget _marcador({required double largura, required double y, required Widget child}) =>
      Positioned(top: y, left: 0, width: largura, child: Center(child: child));

  Widget _badgeMeta(AppState st) => Column(
        children: [
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 9),
            decoration: BoxDecoration(
              color: S.chart,
              borderRadius: BorderRadius.circular(S.rPill),
              boxShadow: const [BoxShadow(color: S.chart600, offset: Offset(0, 5))],
            ),
            child: const Text('★ META',
                style: TextStyle(
                    color: S.onChart, fontWeight: FontWeight.w700, fontSize: 16)),
          ),
          const SizedBox(height: 8),
          Text('${st.curso.disciplina} · ${st.curso.classe}',
              style: const TextStyle(color: S.txSoft, fontSize: 12)),
        ],
      );

  Widget _badgeEntrada() => Container(
        padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 7),
        decoration: BoxDecoration(
          border: Border.all(color: S.line, width: 2, style: BorderStyle.solid),
          borderRadius: BorderRadius.circular(S.rPill),
        ),
        child: const Text('ENTRADA',
            style: TextStyle(color: S.txSoft, fontSize: 13, letterSpacing: 1.6)),
      );

  Widget _tabsDisciplina(AppState st) => Padding(
        padding: const EdgeInsets.fromLTRB(18, 14, 18, 6),
        child: Row(
          children: [
            for (final c in st.cursosVisiveis)
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 4),
                  child: GestureDetector(
                    onTap: () => st.trocarCurso(c.id),
                    child: AnimatedContainer(
                      duration: const Duration(milliseconds: 220),
                      curve: SCurves.ease,
                      padding: const EdgeInsets.symmetric(vertical: 11),
                      decoration: BoxDecoration(
                        color: c.id == st.cursoId ? S.chart : S.surface,
                        border: Border.all(
                          color: c.id == st.cursoId ? S.chart : S.line,
                          width: 2,
                        ),
                        borderRadius: BorderRadius.circular(S.rPill),
                      ),
                      child: Text(
                        c.disciplina,
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          color: c.id == st.cursoId ? S.onChart : S.txSoft,
                          fontWeight: FontWeight.w600,
                          fontSize: 15,
                        ),
                      ),
                    ),
                  ),
                ),
              ),
          ],
        ),
      );
}
