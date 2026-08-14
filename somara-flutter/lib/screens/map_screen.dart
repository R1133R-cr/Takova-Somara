import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/content.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/hopscotch_board.dart';
import '../widgets/roby.dart';
import '../widgets/sem_vidas.dart';
import 'lesson_screen.dart';

/// A amarelinha. Corre de baixo para cima — ENTRADA em baixo, META em cima —
/// como o jogo de rua a que se refere, e ao contrário do scroll de cima para
/// baixo típico das apps do género.
class MapScreen extends StatefulWidget {
  const MapScreen({super.key});
  @override
  State<MapScreen> createState() => _MapScreenState();
}

class _MapScreenState extends State<MapScreen>
    with SingleTickerProviderStateMixin {
  late final AnimationController _glow;
  final _scroll = ScrollController();

  /// A barra de disciplinas quando não cabem todas no ecrã.
  final _tabScroll = ScrollController();
  final _abaActiva = GlobalKey();

  /// Que disciplina já foi trazida para o meio da barra. Sem isto, a app
  /// abria com o conteúdo de Ciências Sociais no mapa e a pastilha de
  /// Ciências Sociais escondida fora do ecrã, à direita.
  String? _abaCentrada;

  /// Que amarelinha foi centrada da última vez.
  ///
  /// Guarda-se o curso e o número de níveis, não um simples "já centrei":
  /// ao mudar de classe ou de disciplina o tabuleiro é outro, e sem
  /// recentrar a criança ficava a olhar para a parte do mapa onde estava
  /// antes — muitas vezes vazia, sem o Roby à vista.
  String? _centradoEm;

  // 138 e não 124: o quadrado está rodado, e um rectângulo inclinado ocupa
  // mais altura do que a sua caixa direita (ver [_folgaDaRotacao]). Com 124
  // o canto da casa de cima aterrava em cima do rótulo da casa de baixo.
  static const _rowH = 138.0;
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
    _tabScroll.dispose();
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
    final derivada =
        math.cos(i * _passoOnda) * _amplitude(largura) * _passoOnda;
    // A subida é constante (_rowH por nível), logo o ângulo do percurso sai
    // do declive lateral face a essa subida. Limitado para nunca exagerar.
    return (math.atan2(derivada, _rowH) * 0.55).clamp(-0.34, 0.34);
  }

  /// Quanto é que o quadrado inclinado desce abaixo do seu próprio `rect`.
  ///
  /// Rodar um rectângulo aumenta a altura que ele ocupa: a 0,34 rad, os 74 px
  /// de altura passam a ~96, ou seja quase 11 px a transbordar por baixo. O
  /// rótulo tem de começar depois disso, senão o texto fica por baixo do
  /// risco de giz — que foi exactamente o que se via no ecrã.
  double _folgaDaRotacao(double angulo) {
    final a = angulo.abs();
    final alturaRodada = _cellW * math.sin(a) + _cellH * math.cos(a);
    return (alturaRodada - _cellH) / 2;
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

              // Centra no quadrado onde o Roby está — sem animação, para não
              // parecer que a app "saltou" sozinha. Repete-se sempre que o
              // tabuleiro muda, não só na primeira vez.
              final assinatura = '${st.cursoId}:${niveis.length}';
              if (_centradoEm != assinatura) {
                _centradoEm = assinatura;
                WidgetsBinding.instance.addPostFrameCallback((_) {
                  if (!_scroll.hasClients) return;
                  final alvo = cells[actual].rect.center.dy - box.maxHeight / 2;
                  _scroll.jumpTo(
                    alvo.clamp(0.0, _scroll.position.maxScrollExtent),
                  );
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
                      _marcador(largura: largura, y: 26, child: _badgeMeta(st)),
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

  /// Abre um nível, ou explica porque não pode.
  ///
  /// Verifica-se a hora aqui e não só ao arrancar: a espera pode ter acabado
  /// com a app aberta, e nesse caso a criança entra sem ter de fechar nada.
  void _abrirNivel(AppState st, int indice) {
    st.verificarFimDoBloqueio();
    if (st.bloqueado) {
      SemVidas.mostrar(
        context,
        aoRever: () {
          final rever = st.paraRever;
          if (rever.isEmpty) return;
          Navigator.of(context).push(
            MaterialPageRoute(
              builder: (_) => LessonScreen(
                indice: -1,
                avulsas: rever.take(10).toList(),
                titulo: 'Revisão',
              ),
            ),
          );
        },
      );
      return;
    }
    Navigator.of(
      context,
    ).push(MaterialPageRoute(builder: (_) => LessonScreen(indice: indice)));
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
        // GestureDetector e não InkWell: a onda circular do Material ficava
        // desenhada em cima do quadrado — e ficava lá, porque o toque abre
        // logo uma rota nova e a animação não chega a fechar. Um círculo
        // cinzento num risco de giz também nunca foi o efeito certo.
        child: GestureDetector(
          behavior: HitTestBehavior.opaque,
          onTap: bloqueado ? null : () => _abrirNivel(st, cell.index),
          child: Center(
            // O número acompanha a inclinação do quadrado; se ficasse a
            // direito dentro de uma casa torta, denunciava logo que a
            // casa é um rectângulo rodado e não um risco no chão.
            child: Transform.rotate(
              angle: cell.angle,
              child: Opacity(
                opacity: bloqueado ? 0.45 : 1,
                child: feito
                    ? const Icon(
                        Icons.check_rounded,
                        color: Colors.white,
                        size: 34,
                      )
                    // Na casa onde o Roby está, o número fica escondido
                    // atrás das pernas dele e lê-se como um erro de
                    // desenho. O Roby já diz onde a criança está.
                    : cell.state == CellState.current
                    ? const SizedBox.shrink()
                    : Text(
                        '${cell.index + 1}',
                        style: const TextStyle(
                          fontSize: 26,
                          fontWeight: FontWeight.w700,
                          color: S.chart,
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
        top: r.bottom + 4 + _folgaDaRotacao(cell.angle),
        width: 136,
        // A placa por baixo do texto não é enfeite: o risco tracejado que
        // liga as casas passa exactamente por aqui, e sem ela a linha
        // atravessava as letras a meio.
        //
        // O nível bloqueado esbate-se pela cor do texto e não por um
        // Opacity à volta de tudo — o Opacity apanhava também a placa,
        // punha-a a 45% e o giz voltava a aparecer por baixo das letras.
        child: Center(
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 1),
            decoration: BoxDecoration(
              // Opaca de propósito: gm950 é a própria cor do fundo, por
              // isso a placa não se vê — só tapa o risco.
              color: S.gm950,
              borderRadius: BorderRadius.circular(6),
            ),
            child: Text(
              lv.nivel.titulo,
              textAlign: TextAlign.center,
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
              style: TextStyle(
                fontSize: 12.5,
                color: bloqueado ? S.txSoft.withValues(alpha: 0.45) : S.txSoft,
                height: 1.25,
              ),
            ),
          ),
        ),
      ),
    ];
  }

  Widget _marcador({
    required double largura,
    required double y,
    required Widget child,
  }) => Positioned(
    top: y,
    left: 0,
    width: largura,
    child: Center(child: child),
  );

  Widget _badgeMeta(AppState st) => Column(
    children: [
      Container(
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 9),
        decoration: BoxDecoration(
          color: S.chart,
          borderRadius: BorderRadius.circular(S.rPill),
          boxShadow: const [BoxShadow(color: S.chart600, offset: Offset(0, 5))],
        ),
        child: const Text(
          '★ META',
          style: TextStyle(
            color: S.onChart,
            fontWeight: FontWeight.w700,
            fontSize: 16,
          ),
        ),
      ),
      const SizedBox(height: 8),
      Text(
        '${st.curso.disciplina} · ${st.curso.classe}',
        style: const TextStyle(color: S.txSoft, fontSize: 12),
      ),
    ],
  );

  Widget _badgeEntrada() => Container(
    padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 7),
    decoration: BoxDecoration(
      border: Border.all(color: S.line, width: 2, style: BorderStyle.solid),
      borderRadius: BorderRadius.circular(S.rPill),
    ),
    child: const Text(
      'ENTRADA',
      style: TextStyle(color: S.txSoft, fontSize: 13, letterSpacing: 1.6),
    ),
  );

  /// Barra de disciplinas.
  ///
  /// Com duas disciplinas dividem-se o ecrã em partes iguais, que é o que
  /// fica melhor. A partir de três — e a 5ª classe tem quatro — passam a
  /// deslizar na horizontal: espremer quatro nomes na largura de um
  /// telemóvel deixaria "Ciências Naturais" ilegível.
  Widget _tabsDisciplina(AppState st) {
    final cursos = st.cursosVisiveis;
    final espremidas = cursos.length > 2;

    Widget aba(Curso c) => GestureDetector(
      key: c.id == st.cursoId ? _abaActiva : null,
      onTap: () => st.trocarCurso(c.id),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 220),
        curve: SCurves.ease,
        padding: EdgeInsets.symmetric(
          vertical: 11,
          horizontal: espremidas ? 18 : 0,
        ),
        decoration: BoxDecoration(
          color: c.id == st.cursoId ? S.chart : S.surface,
          border: Border.all(
            color: c.id == st.cursoId ? S.chart : S.line,
            width: 2,
          ),
          borderRadius: BorderRadius.circular(S.rPill),
        ),
        child: Text(
          c.rotulo,
          textAlign: TextAlign.center,
          style: TextStyle(
            color: c.id == st.cursoId ? S.onChart : S.txSoft,
            fontWeight: FontWeight.w600,
            fontSize: 15,
          ),
        ),
      ),
    );

    if (espremidas) {
      // Traz a disciplina aberta para o meio da barra. As pastilhas têm
      // larguras diferentes, por isso não há offset para calcular: pede-se
      // ao próprio widget que se mostre.
      if (_abaCentrada != st.cursoId) {
        _abaCentrada = st.cursoId;
        WidgetsBinding.instance.addPostFrameCallback((_) {
          final ctx = _abaActiva.currentContext;
          if (ctx == null || !mounted) return;
          Scrollable.ensureVisible(
            ctx,
            alignment: 0.5,
            duration: const Duration(milliseconds: 260),
            curve: SCurves.ease,
          );
        });
      }

      // A altura tem de acomodar o botão inteiro mais o espaço à volta:
      // 14+6 de margem, 11+11 de enchimento, a linha de texto e a moldura.
      // Com menos do que isto o texto sai cortado em baixo.
      return SizedBox(
        height: 78,
        child: SingleChildScrollView(
          controller: _tabScroll,
          scrollDirection: Axis.horizontal,
          padding: const EdgeInsets.fromLTRB(18, 14, 18, 6),
          child: Row(
            children: [
              for (var i = 0; i < cursos.length; i++) ...[
                if (i > 0) const SizedBox(width: 8),
                Center(child: aba(cursos[i])),
              ],
            ],
          ),
        ),
      );
    }

    return Padding(
      padding: const EdgeInsets.fromLTRB(18, 14, 18, 6),
      child: Row(
        children: [
          for (final c in cursos)
            Expanded(
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: 4),
                child: aba(c),
              ),
            ),
        ],
      ),
    );
  }
}
