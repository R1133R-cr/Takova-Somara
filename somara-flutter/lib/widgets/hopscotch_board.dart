import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme.dart';

enum CellState { done, current, locked }

class BoardCell {
  final Rect rect;
  final int index;
  final CellState state;

  /// Inclinação do quadrado, em radianos, alinhada com a direcção do
  /// percurso naquele ponto. É isto que faz o tabuleiro serpentear em vez
  /// de parecer uma escada de caixas direitas.
  final double angle;

  const BoardCell({
    required this.rect,
    required this.index,
    required this.state,
    this.angle = 0,
  });
}

/// Desenha a amarelinha como giz no chão, não como caixas de CSS.
///
/// O que faz parecer desenhado à mão é o traço nunca ser perfeito: cada
/// linha leva um desvio pequeno e *determinístico* (semeado pelo índice do
/// quadrado), por isso treme como giz mas não se mexe entre repintagens —
/// se fosse aleatório a cada frame, o tabuleiro fervia no ecrã.
class HopscotchPainter extends CustomPainter {
  final List<BoardCell> cells;
  final double glow; // 0..1 — pulsar do quadrado actual

  HopscotchPainter({required this.cells, required this.glow});

  /// Ruído estável: mesma entrada, mesmo desvio, sempre.
  double _wobble(int seed, int point, double amount) {
    final h = math.sin(seed * 127.1 + point * 311.7) * 43758.5453;
    return (h - h.floor() - 0.5) * 2 * amount;
  }

  Path _chalkRect(Rect r, int seed, {double amount = 2.4, double angle = 0}) {
    // Cantos com desvio + lados ligeiramente arqueados, como quem risca
    // depressa no cimento. O quadrado roda em torno do próprio centro para
    // acompanhar a curva do percurso.
    final p = Path();
    final c = [
      Offset(r.left + _wobble(seed, 0, amount), r.top + _wobble(seed, 1, amount)),
      Offset(r.right + _wobble(seed, 2, amount), r.top + _wobble(seed, 3, amount)),
      Offset(r.right + _wobble(seed, 4, amount), r.bottom + _wobble(seed, 5, amount)),
      Offset(r.left + _wobble(seed, 6, amount), r.bottom + _wobble(seed, 7, amount)),
    ];
    p.moveTo(c[0].dx, c[0].dy);
    for (var i = 0; i < 4; i++) {
      final a = c[i], b = c[(i + 1) % 4];
      final mid = Offset(
        (a.dx + b.dx) / 2 + _wobble(seed, 10 + i, amount * 1.3),
        (a.dy + b.dy) / 2 + _wobble(seed, 20 + i, amount * 1.3),
      );
      p.quadraticBezierTo(mid.dx, mid.dy, b.dx, b.dy);
    }
    p.close();
    if (angle == 0) return p;
    final m = Matrix4.identity()
      ..translateByDouble(r.center.dx, r.center.dy, 0, 1)
      ..rotateZ(angle)
      ..translateByDouble(-r.center.dx, -r.center.dy, 0, 1);
    return p.transform(m.storage);
  }

  /// Curva suave que passa por todos os centros, de baixo para cima.
  /// Usa o ponto médio entre centros consecutivos como fim de cada segmento
  /// quadrático, com o próprio centro como ponto de controlo — é a forma
  /// mais simples de obter uma linha sem cotovelos a passar por N pontos.
  Path _serpentina() {
    final p = Path();
    if (cells.length < 2) return p;
    final pts = cells.map((c) => c.rect.center).toList();
    p.moveTo(pts.first.dx, pts.first.dy);
    for (var i = 1; i < pts.length - 1; i++) {
      final medio = Offset(
        (pts[i].dx + pts[i + 1].dx) / 2,
        (pts[i].dy + pts[i + 1].dy) / 2,
      );
      p.quadraticBezierTo(pts[i].dx, pts[i].dy, medio.dx, medio.dy);
    }
    p.lineTo(pts.last.dx, pts.last.dy);
    return p;
  }

  @override
  void paint(Canvas canvas, Size size) {
    if (cells.isEmpty) return;

    // 1. O rasto: uma só linha contínua que serpenteia por todos os
    // quadrados. Antes eram segmentos rectos entre centros, o que dava
    // cotovelos; a curva suave é o que faz a amarelinha ondular como uma
    // cobra em vez de ziguezaguear.
    final trail = Paint()
      ..color = Colors.white.withValues(alpha: 0.13)
      ..strokeWidth = 3
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round;
    _dashedPath(canvas, _serpentina(), trail, dash: 10, gap: 9);

    // 2. Os quadrados.
    for (final cell in cells) {
      final seed = cell.index + 1;
      final path = _chalkRect(cell.rect, seed, angle: cell.angle);

      switch (cell.state) {
        case CellState.done:
          canvas.drawPath(path, Paint()..color = S.green500);
          canvas.drawPath(
            path,
            Paint()
              ..color = S.green700
              ..strokeWidth = 3
              ..style = PaintingStyle.stroke,
          );
        case CellState.current:
          // Halo pulsante — o olho vai direito ao sítio onde se joga a seguir.
          canvas.drawPath(
            path,
            Paint()
              ..color = S.chart.withValues(alpha: 0.18 * glow)
              ..maskFilter = MaskFilter.blur(BlurStyle.normal, 10 + 10 * glow),
          );
          canvas.drawPath(path, Paint()..color = S.chart);
          canvas.drawPath(
            path,
            Paint()
              ..color = S.chart600
              ..strokeWidth = 3.5
              ..style = PaintingStyle.stroke,
          );
        case CellState.locked:
          canvas.drawPath(
            path,
            Paint()..color = Colors.white.withValues(alpha: 0.025),
          );
          _dashedPath(
            canvas,
            path,
            Paint()
              ..color = Colors.white.withValues(alpha: 0.34)
              ..strokeWidth = 3
              ..style = PaintingStyle.stroke,
          );
      }
    }
  }

  void _dashedPath(Canvas canvas, Path path, Paint paint,
      {double dash = 9, double gap = 7}) {
    for (final metric in path.computeMetrics()) {
      var d = 0.0;
      while (d < metric.length) {
        final end = math.min(d + dash, metric.length);
        canvas.drawPath(metric.extractPath(d, end), paint);
        d = end + gap;
      }
    }
  }

  @override
  bool shouldRepaint(HopscotchPainter old) =>
      old.glow != glow || old.cells.length != cells.length ||
      !_sameStates(old.cells, cells);

  bool _sameStates(List<BoardCell> a, List<BoardCell> b) {
    for (var i = 0; i < a.length; i++) {
      if (a[i].state != b[i].state || a[i].rect != b[i].rect) return false;
    }
    return true;
  }
}
