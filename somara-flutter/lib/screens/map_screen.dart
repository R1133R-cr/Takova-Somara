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

  static const _rowH = 118.0;
  static const _cellW = 78.0;
  static const _cellH = 74.0;
  static const _lateral = 54.0; // desvio para os lados, alternado
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

  /// Converte o índice do nível na posição do quadrado no tabuleiro.
  /// O índice 0 fica em baixo, por isso a altura conta ao contrário.
  Rect _rectDe(int i, int total, double largura) {
    final centroX = largura / 2 + (i.isEven ? -_lateral : _lateral);
    final y = _padTopo + (total - 1 - i) * _rowH;
    return Rect.fromCenter(
      center: Offset(centroX, y + _cellH / 2),
      width: _cellW,
      height: _cellH,
    );
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
    final aEsquerda = r.center.dx < largura / 2;

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
      // Rótulo ao lado, do lado oposto ao desvio do quadrado.
      Positioned(
        left: aEsquerda ? r.right + 12 : null,
        right: aEsquerda ? null : largura - r.left + 12,
        top: r.center.dy - 18,
        width: 122,
        child: Opacity(
          opacity: bloqueado ? 0.45 : 1,
          child: Text(
            lv.nivel.titulo,
            textAlign: aEsquerda ? TextAlign.left : TextAlign.right,
            style: const TextStyle(fontSize: 12.5, color: S.txSoft, height: 1.3),
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
            for (final c in st.conteudo.cursos)
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
