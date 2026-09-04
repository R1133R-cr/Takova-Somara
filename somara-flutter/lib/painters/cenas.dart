import 'package:flutter/material.dart';

import '../theme.dart';

/// Os cenários das perguntas de Ciências.
///
/// Desenhados em código, como as figuras de geometria e as manchas de cor
/// já são. Não é teimosia: um desenho que nasce dos dados acompanha o tema,
/// não desfoca num ecrã grande, não pesa nada, e — o que mais importa — as
/// posições dos alvos e o desenho vêm do mesmo sítio, e por isso não podem
/// ficar desalinhados.
///
/// ## O mapa de Moçambique não está aqui, e é de propósito
///
/// O §10 pedia-o. Desenhar de cabeça o contorno das províncias dava um mapa
/// **errado** do país da criança, num livro de escola. Um mapa errado é pior
/// do que nenhum: entra pelos olhos e fica. Entra quando houver contornos a
/// sério de onde os tirar.
enum Cena {
  /// Pilha, fios e lâmpada. A lâmpada acende quando o circuito fecha.
  circuito('O circuito eléctrico'),

  /// Raiz, caule, folha, flor e fruto.
  planta('As partes da planta'),

  /// Um tronco com os órgãos por dentro.
  corpo('Os órgãos do corpo'),

  /// Sol, planta, animal que come a planta, animal que come o animal.
  cadeia('A cadeia alimentar');

  final String rotulo;
  const Cena(this.rotulo);
}

/// Desenha o fundo de uma cena.
class FundoDaCena extends CustomPainter {
  final Cena cena;

  /// Verdadeiro quando todos os alvos estão certos. Só a [Cena.circuito] usa:
  /// é o momento em que a lâmpada acende, e é o que faz a criança perceber
  /// que o circuito serve para alguma coisa.
  final bool completa;

  const FundoDaCena({required this.cena, this.completa = false});

  @override
  void paint(Canvas canvas, Size size) {
    switch (cena) {
      case Cena.circuito:
        _circuito(canvas, size);
      case Cena.planta:
        _planta(canvas, size);
      case Cena.corpo:
        _corpo(canvas, size);
      case Cena.cadeia:
        _cadeia(canvas, size);
    }
  }

  Paint get _traco => Paint()
    ..color = S.txSoft
    ..strokeWidth = 3
    ..strokeCap = StrokeCap.round
    ..style = PaintingStyle.stroke;

  Paint _cheio(Color c) => Paint()
    ..color = c
    ..style = PaintingStyle.fill;

  /// Um quadrado de fio à volta, com falhas onde as peças entram.
  void _circuito(Canvas canvas, Size size) {
    final r = Rect.fromLTWH(
      size.width * 0.14,
      size.height * 0.20,
      size.width * 0.72,
      size.height * 0.58,
    );
    // Os quatro lados, com um corte a meio de cada um dos que levam peça.
    final t = _traco;
    canvas.drawLine(r.topLeft, Offset(r.left + r.width * 0.30, r.top), t);
    canvas.drawLine(Offset(r.left + r.width * 0.70, r.top), r.topRight, t);
    canvas.drawLine(r.topRight, Offset(r.right, r.top + r.height * 0.30), t);
    canvas.drawLine(
      Offset(r.right, r.top + r.height * 0.70),
      r.bottomRight,
      t,
    );
    canvas.drawLine(r.bottomRight, r.bottomLeft, t);
    canvas.drawLine(r.bottomLeft, Offset(r.left, r.top + r.height * 0.70), t);
    canvas.drawLine(Offset(r.left, r.top + r.height * 0.30), r.topLeft, t);

    // O brilho da lâmpada, só com o circuito fechado.
    if (completa) {
      final centro = Offset(r.left + r.width * 0.5, r.top);
      for (var i = 3; i >= 1; i--) {
        canvas.drawCircle(
          centro,
          size.width * 0.05 * i,
          _cheio(S.gold.withValues(alpha: 0.10 * (4 - i))),
        );
      }
    }
  }

  void _planta(Canvas canvas, Size size) {
    final chao = size.height * 0.78;
    final meio = size.width * 0.5;

    // A terra.
    canvas.drawRect(
      Rect.fromLTWH(0, chao, size.width, size.height - chao),
      _cheio(S.surface2),
    );
    canvas.drawLine(
      Offset(0, chao),
      Offset(size.width, chao),
      _traco..color = S.txMut,
    );

    // O caule.
    canvas.drawLine(
      Offset(meio, chao),
      Offset(meio, size.height * 0.24),
      Paint()
        ..color = S.green500
        ..strokeWidth = 5
        ..strokeCap = StrokeCap.round,
    );
    // As raízes.
    for (final dx in [-0.10, 0.0, 0.10]) {
      canvas.drawLine(
        Offset(meio, chao),
        Offset(meio + size.width * dx, size.height * 0.94),
        Paint()
          ..color = S.txMut
          ..strokeWidth = 2.5
          ..strokeCap = StrokeCap.round,
      );
    }
    // Duas folhas e uma flor.
    for (final lado in [-1.0, 1.0]) {
      canvas.drawOval(
        Rect.fromCenter(
          center: Offset(meio + lado * size.width * 0.14, size.height * 0.50),
          width: size.width * 0.22,
          height: size.height * 0.12,
        ),
        _cheio(S.green300.withValues(alpha: 0.75)),
      );
    }
    canvas.drawCircle(
      Offset(meio, size.height * 0.20),
      size.width * 0.07,
      _cheio(S.gold.withValues(alpha: 0.85)),
    );
  }

  void _corpo(Canvas canvas, Size size) {
    // Um tronco simples, com cabeça. Não é anatomia: é o sítio onde as
    // peças vão, e tem de se ler de relance num ecrã de 320.
    final meio = size.width * 0.5;
    canvas.drawCircle(
      Offset(meio, size.height * 0.13),
      size.height * 0.10,
      _traco,
    );
    final tronco = RRect.fromRectAndRadius(
      Rect.fromCenter(
        center: Offset(meio, size.height * 0.58),
        width: size.width * 0.46,
        height: size.height * 0.62,
      ),
      Radius.circular(size.width * 0.12),
    );
    canvas.drawRRect(tronco, _traco);
  }

  void _cadeia(Canvas canvas, Size size) {
    // Quatro casas EMPILHADAS, com setas para baixo. Em fila não cabiam num
    // telemóvel de 320: quatro caixas de noventa e seis píxeis não entram em
    // duzentos e oitenta. A seta é o conteúdo — diz quem come quem, e sem
    // ela isto era só quatro caixas.
    final x = size.width * 0.5;
    const paragens = [0.14, 0.38, 0.62, 0.86];
    for (var i = 0; i < paragens.length - 1; i++) {
      final y1 = size.height * (paragens[i] + 0.10);
      final y2 = size.height * (paragens[i + 1] - 0.10);
      canvas.drawLine(Offset(x, y1), Offset(x, y2), _traco);
      final ponta = Path()
        ..moveTo(x, y2)
        ..lineTo(x - size.width * 0.03, y2 - size.height * 0.035)
        ..lineTo(x + size.width * 0.03, y2 - size.height * 0.035)
        ..close();
      canvas.drawPath(ponta, _cheio(S.txSoft));
    }
  }

  @override
  bool shouldRepaint(FundoDaCena velho) =>
      velho.cena != cena || velho.completa != completa;
}
