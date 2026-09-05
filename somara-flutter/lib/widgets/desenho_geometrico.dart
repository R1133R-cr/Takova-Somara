import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../models/content.dart';
import '../theme.dart';

/// Desenha a figura de uma pergunta de geometria.
///
/// Porque é desenhada em código e não uma imagem: a figura **nasce da
/// pergunta**. Mudar "5 cm de lado" para "8 cm" redesenha sozinho, com a
/// medida certa escrita no sítio certo. Com imagens, cada pergunta nova
/// exigia um desenho novo à mão, e nenhuma delas se adaptaria ao ecrã de
/// um telemóvel barato.
///
/// E havia uma pergunta que sem isto era impossível de responder:
/// "Quantos lados tem esta figura?" mostrava quatro réguas em vez de um
/// quadrado.
class DesenhoGeometrico extends StatelessWidget {
  final Figura figura;

  /// Altura reservada. As figuras são pequenas de propósito — a pergunta e
  /// as opções continuam a ser o que importa.
  final double altura;

  const DesenhoGeometrico({
    super.key,
    required this.figura,
    this.altura = 150,
  });

  @override
  Widget build(BuildContext context) => Padding(
    padding: const EdgeInsets.symmetric(vertical: 6),
    child: SizedBox(
      height: altura,
      width: double.infinity,
      child: CustomPaint(painter: _Pintor(figura)),
    ),
  );
}

class _Pintor extends CustomPainter {
  final Figura f;
  _Pintor(this.f);

  static const _traco = 3.0;

  @override
  void paint(Canvas canvas, Size size) {
    final linha = Paint()
      ..color = S.chart
      ..strokeWidth = _traco
      ..style = PaintingStyle.stroke
      ..strokeJoin = StrokeJoin.round;
    final dentro = Paint()..color = S.chart.withValues(alpha: 0.13);

    // Margem para as medidas escritas à volta caberem.
    const margem = 34.0;
    final campo = Rect.fromLTWH(
      margem,
      14,
      size.width - margem * 2,
      size.height - 34,
    );

    switch (f.forma) {
      case FormaGeo.quadrado:
        _quadrilatero(canvas, campo, 1, 1, linha, dentro);
      case FormaGeo.rectangulo:
        _quadrilatero(canvas, campo, f.a, f.b ?? f.a, linha, dentro);
      case FormaGeo.triangulo:
        _triangulo(canvas, campo, linha, dentro);
      case FormaGeo.circulo:
        _circulo(canvas, campo, linha, dentro);
      case FormaGeo.cubo:
        _cubo(canvas, campo, linha, dentro);
      case FormaGeo.trapezio:
        _trapezio(canvas, campo, linha, dentro);
      case FormaGeo.losango:
        _losango(canvas, campo, linha, dentro);
    }
  }

  /// Trapézio: base maior em [a], base menor em [b].
  ///
  /// A altura não cabe nos dois números que a figura guarda, e por isso é
  /// dita no enunciado e não desenhada. O que a figura tem de mostrar é a
  /// forma — duas bases paralelas de tamanhos diferentes —, porque é isso
  /// que distingue um trapézio de um rectângulo aos olhos de quem ainda
  /// não sabe qual é qual.
  void _trapezio(Canvas canvas, Rect campo, Paint linha, Paint dentro) {
    final maior = f.a;
    final menor = f.b ?? f.a * 0.6;
    final w = campo.width;
    final h = w * 0.5 > campo.height ? campo.height : w * 0.5;
    final c = campo.center;
    final meiaMaior = w / 2;
    // A base menor guarda a proporção da maior: se o enunciado diz 10 e 6,
    // a de cima tem de SER mais curta, e nesta medida.
    final meiaMenor = meiaMaior * (menor / maior);

    final p = Path()
      ..moveTo(c.dx - meiaMaior, c.dy + h / 2)
      ..lineTo(c.dx + meiaMaior, c.dy + h / 2)
      ..lineTo(c.dx + meiaMenor, c.dy - h / 2)
      ..lineTo(c.dx - meiaMenor, c.dy - h / 2)
      ..close();
    canvas.drawPath(p, dentro);
    canvas.drawPath(p, linha);

    _medida(canvas, f.medidaDe(f.a), Offset(c.dx, c.dy + h / 2 + 16));
    if (f.b != null) {
      _medida(canvas, f.medidaDe(f.b!), Offset(c.dx, c.dy - h / 2 - 14));
    }
  }

  /// Losango: diagonal maior em [a], diagonal menor em [b].
  ///
  /// Aqui as duas medidas são mesmo as duas diagonais, e desenham-se as
  /// duas — é delas que sai a área, e ver as linhas cruzadas ajuda mais do
  /// que a fórmula escrita.
  void _losango(Canvas canvas, Rect campo, Paint linha, Paint dentro) {
    final maior = f.a;
    final menor = f.b ?? f.a;
    var w = campo.width;
    var h = w * (menor / maior);
    if (h > campo.height) {
      h = campo.height;
      w = h * (maior / menor);
    }
    final c = campo.center;

    final p = Path()
      ..moveTo(c.dx - w / 2, c.dy)
      ..lineTo(c.dx, c.dy - h / 2)
      ..lineTo(c.dx + w / 2, c.dy)
      ..lineTo(c.dx, c.dy + h / 2)
      ..close();
    canvas.drawPath(p, dentro);
    canvas.drawPath(p, linha);

    // As diagonais a tracejado leve, para se ver o que as medidas medem.
    final fina = Paint()
      ..color = linha.color.withValues(alpha: 0.45)
      ..strokeWidth = 1.5;
    canvas.drawLine(
        Offset(c.dx - w / 2, c.dy), Offset(c.dx + w / 2, c.dy), fina);
    canvas.drawLine(
        Offset(c.dx, c.dy - h / 2), Offset(c.dx, c.dy + h / 2), fina);

    _medida(canvas, f.medidaDe(f.a), Offset(c.dx, c.dy + h / 2 + 16));
    if (f.b != null) {
      _medida(canvas, f.medidaDe(f.b!), Offset(c.dx - w / 2 - 20, c.dy),
          rodado: true);
    }
  }

  /// Um rectângulo com a proporção certa entre os lados.
  ///
  /// A proporção importa: um rectângulo de 8 por 3 desenhado quadrado
  /// ensinaria à criança que as medidas escritas não querem dizer nada.
  void _quadrilatero(
    Canvas canvas,
    Rect campo,
    double largura,
    double alturaMedida,
    Paint linha,
    Paint dentro,
  ) {
    final proporcao = largura / alturaMedida;
    var w = campo.width;
    var h = w / proporcao;
    if (h > campo.height) {
      h = campo.height;
      w = h * proporcao;
    }
    final r = Rect.fromCenter(center: campo.center, width: w, height: h);
    final rr = RRect.fromRectAndRadius(r, const Radius.circular(4));
    canvas.drawRRect(rr, dentro);
    canvas.drawRRect(rr, linha);

    _medida(canvas, f.medidaDe(f.a), Offset(r.center.dx, r.bottom + 16));
    if (f.b != null && f.forma != FormaGeo.quadrado) {
      _medida(canvas, f.medidaDe(f.b!), Offset(r.left - 20, r.center.dy),
          rodado: true);
    } else if (f.forma == FormaGeo.quadrado) {
      // No quadrado a medida do lado vale para todos, e escrevê-la nos
      // quatro lados só encheria o desenho.
      _medida(canvas, f.medidaDe(f.a), Offset(r.left - 20, r.center.dy),
          rodado: true);
    }
  }

  void _triangulo(Canvas canvas, Rect campo, Paint linha, Paint dentro) {
    final base = f.a;
    final alt = f.b ?? f.a;
    final proporcao = base / alt;
    var w = campo.width;
    var h = w / proporcao;
    if (h > campo.height) {
      h = campo.height;
      w = h * proporcao;
    }
    final c = campo.center;
    final p = Path()
      ..moveTo(c.dx - w / 2, c.dy + h / 2)
      ..lineTo(c.dx + w / 2, c.dy + h / 2)
      ..lineTo(c.dx, c.dy - h / 2)
      ..close();
    canvas.drawPath(p, dentro);
    canvas.drawPath(p, linha);

    _medida(canvas, f.medidaDe(base), Offset(c.dx, c.dy + h / 2 + 16));

    if (f.b != null) {
      // A altura desenha-se a tracejado, como no quadro: é uma linha
      // auxiliar e não um lado da figura.
      final topo = Offset(c.dx, c.dy - h / 2);
      final pe = Offset(c.dx, c.dy + h / 2);
      final tracejado = Paint()
        ..color = S.txSoft
        ..strokeWidth = 1.6
        ..style = PaintingStyle.stroke;
      for (var y = topo.dy; y < pe.dy; y += 10) {
        canvas.drawLine(
          Offset(c.dx, y),
          Offset(c.dx, math.min(y + 5, pe.dy)),
          tracejado,
        );
      }
      _medida(canvas, f.medidaDe(alt), Offset(c.dx + 26, c.dy));
    }
  }

  void _circulo(Canvas canvas, Rect campo, Paint linha, Paint dentro) {
    final raio = math.min(campo.width, campo.height) / 2;
    final c = campo.center;
    canvas.drawCircle(c, raio, dentro);
    canvas.drawCircle(c, raio, linha);

    // O raio marcado com uma seta do centro para fora: é o que a pergunta
    // usa, e sem ele a criança não sabe qual das medidas é qual.
    final ponta = Offset(c.dx + raio, c.dy);
    canvas.drawLine(
      c,
      ponta,
      Paint()
        ..color = S.gold
        ..strokeWidth = 2,
    );
    canvas.drawCircle(c, 3.5, Paint()..color = S.gold);
    _medida(
      canvas,
      f.medidaDe(f.a),
      Offset(c.dx + raio / 2, c.dy - 14),
      cor: S.gold,
    );
  }

  /// Um cubo em perspectiva simples, com a aresta marcada.
  void _cubo(Canvas canvas, Rect campo, Paint linha, Paint dentro) {
    final lado = math.min(campo.width, campo.height) * 0.62;
    final desvio = lado * 0.34;
    final c = campo.center;
    final frente = Rect.fromCenter(
      center: Offset(c.dx - desvio / 2, c.dy + desvio / 2),
      width: lado,
      height: lado,
    );

    Offset atras(Offset p) => Offset(p.dx + desvio, p.dy - desvio);

    canvas.drawRect(frente, dentro);
    // As três arestas escondidas ficam mais claras, como num desenho de
    // quadro — vê-se que o cubo é sólido sem parecer um emaranhado.
    final fraca = Paint()
      ..color = S.chart.withValues(alpha: 0.4)
      ..strokeWidth = 1.8
      ..style = PaintingStyle.stroke;
    canvas.drawRect(
      Rect.fromPoints(atras(frente.topLeft), atras(frente.bottomRight)),
      fraca,
    );
    for (final p in [frente.topLeft, frente.bottomRight, frente.bottomLeft]) {
      canvas.drawLine(p, atras(p), fraca);
    }
    canvas.drawRect(frente, linha);
    canvas.drawLine(frente.topRight, atras(frente.topRight), linha);
    canvas.drawLine(
      atras(frente.topLeft),
      atras(frente.topRight),
      linha,
    );
    canvas.drawLine(
      atras(frente.topRight),
      atras(frente.bottomRight),
      linha,
    );

    _medida(canvas, f.medidaDe(f.a), Offset(frente.center.dx, frente.bottom + 16));
  }

  void _medida(
    Canvas canvas,
    String texto,
    Offset onde, {
    bool rodado = false,
    Color cor = S.tx,
  }) {
    if (texto.isEmpty) return;
    final tp = TextPainter(
      text: TextSpan(
        text: texto,
        style: TextStyle(
          color: cor,
          fontSize: 13.5,
          fontWeight: FontWeight.w700,
        ),
      ),
      textDirection: TextDirection.ltr,
    )..layout();

    canvas.save();
    canvas.translate(onde.dx, onde.dy);
    if (rodado) canvas.rotate(-math.pi / 2);
    tp.paint(canvas, Offset(-tp.width / 2, -tp.height / 2));
    canvas.restore();
  }

  @override
  bool shouldRepaint(_Pintor old) => old.f != f;
}
