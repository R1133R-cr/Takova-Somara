import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme.dart';

enum CellState { done, current, locked }

/// De que lado da fita fica uma casa de complemento.
enum Lado { esquerdo, direito }

/// Uma casa da amarelinha — um troço da fita, não um quadrado solto.
class BoardCell {
  final int index;
  final CellState state;

  /// Meio da casa, sobre a linha central da fita. É aqui que o Roby pousa.
  final Offset centro;

  /// Direcção da fita neste ponto, em radianos. O número da casa acompanha-a,
  /// senão lê-se logo que a casa é um rectângulo pousado sobre uma curva.
  final double angulo;

  /// O contorno da casa, já com o tremido do giz.
  final Path contorno;

  const BoardCell({
    required this.index,
    required this.state,
    required this.centro,
    required this.angulo,
    required this.contorno,
  });
}

/// Uma casa pendurada ao lado da fita: matéria, treino — o que complementa
/// aquele nível sem fazer avançar o percurso.
class BoardSide {
  final Offset centro;
  final double angulo;
  final Path contorno;
  final Lado lado;
  final bool activa;

  const BoardSide({
    required this.centro,
    required this.angulo,
    required this.contorno,
    required this.lado,
    required this.activa,
  });
}

/// A geometria da amarelinha.
///
/// A fita é uma faixa de largura constante que serpenteia de baixo para cima,
/// dividida em casas por linhas transversais — como o desenho a lápis de que
/// isto veio. Antes eram quadrados soltos ligados por um tracejado, e lia-se
/// como caixas pousadas num caminho em vez de um percurso riscado no chão.
///
/// Vive fora do pintor porque o ecrã precisa da mesma geometria: onde pousar
/// o Roby, de que lado sobra espaço para o rótulo, onde pendurar as casas de
/// complemento.
class Fita {
  final int casas;
  final double largura;

  /// Altura de cada casa, medida na vertical (não ao longo da curva).
  static const alturaCasa = 164.0;

  /// Espaço antes da primeira casa e depois da última — onde ficam os
  /// letreiros de ENTRADA e META.
  static const padBase = 96.0;
  static const padTopo = 104.0;

  /// Radianos de onda por casa. 2π/6 fecha uma volta completa a cada seis
  /// casas: com nove casas dá um S e meio, que é a forma do desenho. Com
  /// passo menor a fita quase não vira; com maior volta a ser ziguezague.
  static const _passo = 1.047;

  late final double larguraFita;
  late final double amplitude;
  late final double alturaTotal;

  Fita({required this.casas, required this.largura}) {
    larguraFita = math.min(140.0, largura * 0.34);
    // 0,74 e não a folga toda: a fita tem largura, e onde a onda está mais
    // inclinada os cantos de uma casa saem bastante para fora da linha do
    // meio. Com a amplitude no máximo, a casa de cima ficava cortada pela
    // berma do ecrã. Isto também baixa o declive — e é o declive que faz o
    // texto dentro da casa ir parar aos 40°, onde deixa de se ler.
    final folga = math.max(0.0, largura / 2 - larguraFita / 2 - 16);
    amplitude = folga * 0.74;
    alturaTotal = padBase + casas * alturaCasa + padTopo;
  }

  /// Posição na linha central para um t contínuo (0 = entrada, [casas] = meta).
  Offset centro(double t) => Offset(
    largura / 2 + math.sin(t * _passo) * amplitude,
    alturaTotal - padBase - t * alturaCasa,
  );

  /// Normal unitária à curva — a direcção em que a fita tem largura.
  Offset _normal(double t) {
    // A curva sobe alturaCasa por unidade de t e desloca-se lateralmente
    // segundo a derivada do seno.
    final dx = math.cos(t * _passo) * amplitude * _passo;
    const dy = -alturaCasa;
    final n = math.sqrt(dx * dx + dy * dy);
    // Perpendicular a (dx, dy), normalizada.
    return Offset(-dy / n, dx / n);
  }

  /// Ângulo da fita naquele ponto — a inclinação verdadeira da curva.
  double angulo(double t) =>
      math.atan2(math.cos(t * _passo) * amplitude * _passo, alturaCasa);

  /// O ângulo com que se escreve dentro da casa.
  ///
  /// O texto não herda a inclinação toda de propósito. Onde a onda vira, a
  /// fita chega aos 40° e um título de duas linhas nesse ângulo deixa de se
  /// ler — a criança teria de rodar o telemóvel. Um número aguenta bem a
  /// inclinação toda; uma frase não. Fica a meio caminho: acompanha a curva
  /// o suficiente para pertencer à casa, sem sair da horizontal.
  double anguloDoTexto(double t) => angulo(t).clamp(-0.30, 0.30);

  Offset margem(double t, double meiaLargura) => centro(t) + _normal(t) * meiaLargura;

  /// Ruído estável: mesma entrada, mesmo desvio, sempre. Se fosse aleatório
  /// a cada frame, a fita fervia no ecrã em vez de parecer riscada a giz.
  static double _tremido(int semente, int ponto, double quanto) {
    final h = math.sin(semente * 127.1 + ponto * 311.7) * 43758.5453;
    return (h - h.floor() - 0.5) * 2 * quanto;
  }

  Offset _comTremido(Offset p, int semente, int ponto, double quanto) => Offset(
    p.dx + _tremido(semente, ponto, quanto),
    p.dy + _tremido(semente, ponto + 97, quanto),
  );

  /// Bordo da fita entre dois valores de t, amostrado em [passos] pontos.
  List<Offset> _bordo(double de, double ate, double meiaLargura, int passos,
      {double tremido = 1.6, int semente = 0}) {
    return [
      for (var i = 0; i <= passos; i++)
        _comTremido(
          margem(de + (ate - de) * i / passos, meiaLargura),
          semente,
          i,
          tremido,
        ),
    ];
  }

  static Path _porPontos(List<Offset> pts, {bool fechar = false}) {
    final p = Path();
    if (pts.isEmpty) return p;
    p.moveTo(pts.first.dx, pts.first.dy);
    for (var i = 1; i < pts.length; i++) {
      p.lineTo(pts[i].dx, pts[i].dy);
    }
    if (fechar) p.close();
    return p;
  }

  /// O contorno fechado de uma casa: bordo esquerdo a subir, bordo direito a
  /// descer. As duas casas vizinhas partilham a mesma linha transversal, e é
  /// isso que faz a fita ler como uma só peça em vez de nove.
  ///
  /// Sem tremido nenhum, de propósito. Este contorno é o que se pinta por
  /// dentro; o giz que se vê por cima tem o seu próprio desvio. Se ambos
  /// tremessem, tremeriam de maneira diferente e o verde ficava a espreitar
  /// por fora da linha.
  Path contornoDaCasa(int i) {
    final m = larguraFita / 2;
    final esq = _bordo(i.toDouble(), i + 1.0, -m, 8, tremido: 0);
    final dir = _bordo(i + 1.0, i.toDouble(), m, 8, tremido: 0);
    return _porPontos([...esq, ...dir], fechar: true);
  }

  /// Os dois bordos compridos da fita, de ponta a ponta. Desenhados como uma
  /// linha só — é o traço contínuo que o desenho tem.
  (Path, Path) get bordosCompridos {
    final m = larguraFita / 2;
    final n = casas * 6;
    return (
      _porPontos(_bordo(0, casas.toDouble(), -m, n, semente: 7)),
      _porPontos(_bordo(0, casas.toDouble(), m, n, semente: 13)),
    );
  }

  /// A linha que separa duas casas.
  Path divisoria(int i) {
    final m = larguraFita / 2;
    return _porPontos([
      _comTremido(margem(i.toDouble(), -m), i + 61, 0, 1.4),
      _comTremido(margem(i.toDouble(), m), i + 61, 1, 1.4),
    ]);
  }

  /// Comprimento do ramo que sai da fita até ao meio da casa lateral.
  static const _bracoLateral = 86.0;

  /// De que lado é que sobra espaço, na altura [t].
  ///
  /// Com a fita a ondular a sério num ecrã de telemóvel, no ponto mais
  /// afastado da onda um dos lados fica com uns 16 px — não chega para nada.
  /// Por isso o que se pergunta não é "esquerda ou direita" mas "onde é que
  /// há espaço", e as casas de complemento vão todas para lá.
  Lado ladoComEspaco(double t) =>
      centro(t).dx > largura / 2 ? Lado.esquerdo : Lado.direito;

  /// A casa de complemento pendurada na altura [t] da fita.
  ///
  /// É um losango achatado, como no desenho: encosta à fita e aponta para
  /// fora, para se ler como um ramo do percurso e não como outra casa dele.
  ({Offset centro, double angulo, Path contorno}) casaLateral(
    double t,
    Lado lado,
  ) {
    final sinal = lado == Lado.esquerdo ? -1.0 : 1.0;
    final base = margem(t, sinal * larguraFita / 2);
    final fora = margem(t, sinal * (larguraFita / 2 + _bracoLateral));
    final meio = Offset((base.dx + fora.dx) / 2, (base.dy + fora.dy) / 2);

    // As duas pontas do losango, afastadas ao longo da fita.
    final desvio = meio - centro(t);
    final acima = centro(t + 0.22) + desvio * 0.94;
    final abaixo = centro(t - 0.22) + desvio * 0.94;

    final semente = (t * 10).round();
    final pts = [
      _comTremido(base, semente, 0, 1.5),
      _comTremido(abaixo, semente, 1, 1.5),
      _comTremido(fora, semente, 2, 1.5),
      _comTremido(acima, semente, 3, 1.5),
    ];
    return (
      centro: meio,
      angulo: anguloDoTexto(t),
      contorno: _porPontos(pts, fechar: true),
    );
  }
}

/// Pinta a fita a giz.
class HopscotchPainter extends CustomPainter {
  final Fita fita;
  final List<BoardCell> cells;
  final List<BoardSide> laterais;
  final double glow; // 0..1 — pulsar da casa actual

  HopscotchPainter({
    required this.fita,
    required this.cells,
    required this.laterais,
    required this.glow,
  });

  @override
  void paint(Canvas canvas, Size size) {
    if (cells.isEmpty) return;

    // 1. O enchimento de cada casa. Vai primeiro para os traços de giz
    // ficarem por cima e a fita se ler como uma peça só.
    for (final cell in cells) {
      switch (cell.state) {
        case CellState.done:
          canvas.drawPath(cell.contorno, Paint()..color = S.green500);
        case CellState.current:
          canvas.drawPath(
            cell.contorno,
            Paint()
              ..color = S.chart.withValues(alpha: 0.20 * glow)
              ..maskFilter = MaskFilter.blur(BlurStyle.normal, 12 + 12 * glow),
          );
          canvas.drawPath(cell.contorno, Paint()..color = S.chart);
        case CellState.locked:
          canvas.drawPath(
            cell.contorno,
            Paint()..color = Colors.white.withValues(alpha: 0.025),
          );
      }
    }

    // 2. As divisórias entre casas. Ficam por baixo dos bordos compridos,
    // que são o traço que segura a forma toda.
    final giz = Paint()
      ..color = Colors.white.withValues(alpha: 0.42)
      ..strokeWidth = 2.6
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round;

    for (var i = 1; i < cells.length; i++) {
      canvas.drawPath(fita.divisoria(i), giz);
    }

    // 3. Os dois bordos compridos, de ponta a ponta e sem interrupção.
    final (esq, dir) = fita.bordosCompridos;
    final bordo = Paint()
      ..color = Colors.white.withValues(alpha: 0.5)
      ..strokeWidth = 3.2
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round
      ..strokeJoin = StrokeJoin.round;
    canvas.drawPath(esq, bordo);
    canvas.drawPath(dir, bordo);

    // 4. As casas de complemento, penduradas de lado.
    for (final l in laterais) {
      canvas.drawPath(
        l.contorno,
        Paint()
          ..color = (l.activa ? S.chart : Colors.white).withValues(
            alpha: l.activa ? 0.13 : 0.03,
          ),
      );
      canvas.drawPath(
        l.contorno,
        Paint()
          ..color = (l.activa ? S.chart : Colors.white).withValues(
            alpha: l.activa ? 0.72 : 0.28,
          )
          ..strokeWidth = 2.4
          ..style = PaintingStyle.stroke
          ..strokeCap = StrokeCap.round
          ..strokeJoin = StrokeJoin.round,
      );
    }
  }

  @override
  bool shouldRepaint(HopscotchPainter old) =>
      old.glow != glow ||
      old.cells.length != cells.length ||
      old.laterais.length != laterais.length ||
      !_mesmosEstados(old.cells, cells);

  bool _mesmosEstados(List<BoardCell> a, List<BoardCell> b) {
    for (var i = 0; i < a.length; i++) {
      if (a[i].state != b[i].state || a[i].centro != b[i].centro) return false;
    }
    return true;
  }
}
