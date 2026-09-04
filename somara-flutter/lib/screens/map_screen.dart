import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/content.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/hopscotch_board.dart';
import '../widgets/roby.dart';
import '../widgets/sem_vidas.dart';
import 'lesson_screen.dart';
import 'materia_screen.dart';

/// O que se pendura ao lado da casa onde o Roby está.
enum _Complemento { materia, treino }

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

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final niveis = st.niveis;
    final actual = st.nivelActual;

    return Column(
      children: [
        _tabsDisciplina(st),
        Expanded(
          child: LayoutBuilder(
            builder: (context, box) {
              final fita = Fita(casas: niveis.length, largura: box.maxWidth);

              final cells = [
                for (var i = 0; i < niveis.length; i++)
                  BoardCell(
                    index: i,
                    centro: fita.centro(i + 0.5),
                    angulo: fita.anguloDoTexto(i + 0.5),
                    contorno: fita.contornoDaCasa(i),
                    state: st.nivelFeito(i)
                        ? CellState.done
                        : (i == actual ? CellState.current : CellState.locked),
                  ),
              ];

              // As duas casas de complemento acompanham o Roby: ficam sempre
              // no nível onde a criança está, que é para onde ela olha. Postas
              // em todos os níveis, dezoito losangos enchiam o tabuleiro de
              // ruído e a fita deixava de se ler.
              //
              // As duas juntas são a resposta à queixa da fase C — as
              // perguntas eram desafiantes e pouco recompensadoras. Agora há
              // um caminho antes do salto: lê a matéria, ensaia sem risco, e
              // só depois faz o nível a valer. O treino usa as perguntas
              // deste mesmo nível de propósito: ensaiar noutra coisa não
              // prepara para esta.
              final lado = fita.ladoComEspaco(actual + 0.5);
              final complementos = [
                (t: actual + 0.82, tipo: _Complemento.materia),
                (t: actual + 0.18, tipo: _Complemento.treino),
              ];
              final nivelActual = niveis[actual].nivel;
              final laterais = [
                for (final c in complementos)
                  () {
                    final g = fita.casaLateral(c.t, lado);
                    return BoardSide(
                      centro: g.centro,
                      angulo: g.angulo,
                      contorno: g.contorno,
                      lado: lado,
                      activa: switch (c.tipo) {
                        _Complemento.materia => nivelActual.materia != null,
                        _Complemento.treino => nivelActual.questoes.isNotEmpty,
                      },
                    );
                  }(),
              ];

              // Centra na casa onde o Roby está — sem animação, para não
              // parecer que a app "saltou" sozinha. Repete-se sempre que o
              // tabuleiro muda, não só na primeira vez.
              final assinatura = '${st.cursoId}:${niveis.length}';
              if (_centradoEm != assinatura) {
                _centradoEm = assinatura;
                WidgetsBinding.instance.addPostFrameCallback((_) {
                  if (!_scroll.hasClients) return;
                  final alvo = cells[actual].centro.dy - box.maxHeight / 2;
                  _scroll.jumpTo(
                    alvo.clamp(0.0, _scroll.position.maxScrollExtent),
                  );
                });
              }

              return SingleChildScrollView(
                controller: _scroll,
                child: SizedBox(
                  height: fita.alturaTotal,
                  width: fita.largura,
                  child: Stack(
                    clipBehavior: Clip.none,
                    children: [
                      Positioned.fill(
                        child: AnimatedBuilder(
                          animation: _glow,
                          builder: (_, _) => CustomPaint(
                            painter: HopscotchPainter(
                              fita: fita,
                              cells: cells,
                              laterais: laterais,
                              glow: _glow.value,
                            ),
                          ),
                        ),
                      ),
                      _marcador(
                        largura: fita.largura,
                        y: 24,
                        child: _badgeMeta(st),
                      ),
                      _marcador(
                        largura: fita.largura,
                        y: fita.alturaTotal - Fita.padBase + 30,
                        child: _badgeEntrada(),
                      ),
                      for (var i = 0; i < niveis.length; i++)
                        _casa(st, fita, cells[i], niveis[i]),
                      for (var i = 0; i < laterais.length; i++)
                        _casaLateral(st, laterais[i], complementos[i].tipo),
                      RobyToken(
                        position: cells[actual].centro,
                        // A cara que a criança comprou e vestiu. É aqui que
                        // ela a vê — é para isto que se juntam cristais.
                        pose: st.robyEscolhido,
                        size: 58,
                        // O som sai quando os pés tocam a casa, não quando a
                        // animação acaba — a mola de recuperação ainda corre
                        // um bocado depois disso.
                        onLand: Sons.i.salto,
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
    Sons.i.toque();
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
    final lv = st.niveis[indice];
    final materia = lv.nivel.materia;

    // Da primeira vez, a matéria vem antes da pergunta. Depois de o nível
    // estar feito não se repete a aula sem se pedir — quem quiser relê-la
    // tem a casa lateral sempre lá.
    if (materia != null && !st.nivelFeito(indice)) {
      Navigator.of(context).push(
        MaterialPageRoute(
          builder: (ctx) => MateriaScreen(
            titulo: lv.nivel.titulo,
            materia: materia,
            aoComecar: () => Navigator.of(ctx).pushReplacement(
              MaterialPageRoute(builder: (_) => LessonScreen(indice: indice)),
            ),
          ),
        ),
      );
      return;
    }

    Navigator.of(
      context,
    ).push(MaterialPageRoute(builder: (_) => LessonScreen(indice: indice)));
  }

  /// Abre uma casa de complemento do nível onde o Roby está.
  void _abrirComplemento(AppState st, _Complemento tipo) {
    Sons.i.toque();
    final lv = st.niveis[st.nivelActual];
    switch (tipo) {
      case _Complemento.materia:
        final m = lv.nivel.materia;
        if (m == null) return;
        Navigator.of(context).push(
          MaterialPageRoute(
            builder: (_) => MateriaScreen(titulo: lv.nivel.titulo, materia: m),
          ),
        );
      case _Complemento.treino:
        // Treinar o nível outra vez sem o refazer no mapa — e sem gastar
        // corações, que é o que distingue treinar de avançar.
        final qs = [...lv.nivel.questoes]..shuffle();
        if (qs.isEmpty) return;
        Navigator.of(context).push(
          MaterialPageRoute(
            builder: (_) => LessonScreen(
              indice: -1,
              avulsas: qs,
              titulo: 'Treino · ${lv.nivel.titulo}',
            ),
          ),
        );
    }
  }

  /// Uma casa da fita: o número e o nome do nível, lá dentro.
  ///
  /// O texto vai dentro da fita e não ao lado dela. Ao lado era onde estava
  /// antes, e chocava sempre com o giz — a fita ondula, o rótulo não, e mais
  /// cedo ou mais tarde cruzavam-se. Dentro, os 140 px de largura da fita
  /// chegam para duas linhas e as margens ficam livres para os complementos.
  Widget _casa(
    AppState st,
    Fita fita,
    BoardCell cell,
    ({Unidade unit, Nivel nivel}) lv,
  ) {
    final bloqueado = cell.state == CellState.locked;
    final feito = cell.state == CellState.done;
    final actual = cell.state == CellState.current;

    // Sobre o verde e o chartreuse o texto tem de ser escuro; sobre o fundo
    // quase preto de uma casa por abrir, claro.
    final corTexto = feito
        ? Colors.white
        : actual
        ? S.onChart
        : S.txSoft.withValues(alpha: 0.5);

    return Positioned(
      left: cell.centro.dx - fita.larguraFita / 2,
      top: cell.centro.dy - Fita.alturaCasa / 2,
      width: fita.larguraFita,
      height: Fita.alturaCasa,
      // GestureDetector e não InkWell: a onda circular do Material ficava
      // desenhada em cima da casa — e ficava lá, porque o toque abre logo
      // uma rota nova e a animação não chega a fechar. Um círculo cinzento
      // num risco de giz também nunca foi o efeito certo.
      child: GestureDetector(
        behavior: HitTestBehavior.opaque,
        onTap: bloqueado ? null : () => _abrirNivel(st, cell.index),
        // O conteúdo acompanha a inclinação da fita; a direito dentro de uma
        // casa torta, denunciava logo que a fita é um desenho por baixo.
        child: Transform.rotate(
          angle: cell.angulo,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Na casa do Roby o número fica escondido atrás das pernas
              // dele. O Roby já diz onde a criança está.
              if (!actual)
                feito
                    ? const Icon(
                        Icons.check_rounded,
                        color: Colors.white,
                        size: 30,
                      )
                    : Text(
                        '${cell.index + 1}',
                        style: TextStyle(
                          fontSize: 26,
                          fontWeight: FontWeight.w700,
                          color: S.chart.withValues(alpha: 0.55),
                        ),
                      ),
              if (!actual) const SizedBox(height: 2),
              // Na casa actual o nome desce, para não ficar debaixo do Roby.
              if (actual) const SizedBox(height: 46),
              Padding(
                // Folga generosa: o texto está rodado dentro de uma faixa
                // inclinada, e os cantos das linhas compridas são o que
                // primeiro passa para fora do giz.
                padding: const EdgeInsets.symmetric(horizontal: 13),
                child: Text(
                  lv.nivel.titulo,
                  textAlign: TextAlign.center,
                  maxLines: 3,
                  overflow: TextOverflow.ellipsis,
                  style: TextStyle(
                    fontSize: 11,
                    height: 1.18,
                    fontWeight: actual || feito
                        ? FontWeight.w700
                        : FontWeight.w500,
                    color: corTexto,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  /// Uma casa de complemento, pendurada ao lado da fita.
  ///
  /// São os ramos do desenho: não fazem avançar o percurso, servem para
  /// voltar à matéria ou treinar aquele nível outra vez.
  Widget _casaLateral(AppState st, BoardSide side, _Complemento tipo) {
    const w = 96.0, h = 62.0;
    return Positioned(
      left: side.centro.dx - w / 2,
      top: side.centro.dy - h / 2,
      width: w,
      height: h,
      child: GestureDetector(
        behavior: HitTestBehavior.opaque,
        onTap: side.activa ? () => _abrirComplemento(st, tipo) : null,
        child: Transform.rotate(
          angle: side.angulo,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(
                tipo == _Complemento.materia
                    ? Icons.menu_book_rounded
                    : Icons.fitness_center_rounded,
                size: 19,
                color: side.activa
                    ? S.chart
                    : S.txMut.withValues(alpha: 0.55),
              ),
              const SizedBox(height: 3),
              Text(
                tipo == _Complemento.materia ? 'Matéria' : 'Treino',
                style: TextStyle(
                  fontSize: 11,
                  fontWeight: FontWeight.w700,
                  color: side.activa
                      ? S.chart
                      : S.txMut.withValues(alpha: 0.55),
                ),
              ),
            ],
          ),
        ),
      ),
    );
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
      onTap: () {
        Sons.i.toque();
        st.trocarCurso(c.id);
      },
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
