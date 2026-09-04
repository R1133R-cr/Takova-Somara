import 'package:flutter/material.dart';

import '../models/content.dart';
import '../theme.dart';

/// As tintas de uma pergunta de Educação Visual, mostradas a sério.
///
/// «Amarelo + Azul = ?» com as duas manchas de cor à vista, e um ponto de
/// interrogação no lugar do resultado. A criança vê as tintas antes de
/// escolher — que é o contrário de decorar três palavras.
///
/// As manchas são redondas e não quadradas de propósito: uma gota de tinta
/// é redonda, e o quadrado leria-se como um botão para carregar.
class MostraCores extends StatelessWidget {
  final Cores cores;

  const MostraCores({super.key, required this.cores});

  @override
  Widget build(BuildContext context) {
    if (!cores.temMistura) return const SizedBox.shrink();

    final pecas = <Widget>[];
    for (var i = 0; i < cores.mistura.length; i++) {
      if (i > 0) pecas.add(const _Sinal('+'));
      pecas.add(_Gota(cor: Color(cores.mistura[i])));
    }
    pecas.add(const _Sinal('='));
    pecas.add(const _Incognita());

    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 10),
      // Em vez de Row: numa pergunta com três tintas e num telemóvel
      // estreito, a linha passava a largura do ecrã.
      child: Wrap(
        alignment: WrapAlignment.center,
        crossAxisAlignment: WrapCrossAlignment.center,
        spacing: 6,
        runSpacing: 6,
        children: pecas,
      ),
    );
  }
}

class _Gota extends StatelessWidget {
  final Color cor;
  const _Gota({required this.cor});

  @override
  Widget build(BuildContext context) => Container(
        width: 58,
        height: 58,
        decoration: BoxDecoration(
          color: cor,
          shape: BoxShape.circle,
          // A borda clara existe para o branco e os tons muito claros não
          // desaparecerem no fundo escuro da app.
          border: Border.all(color: S.line, width: 2),
        ),
      );
}

class _Incognita extends StatelessWidget {
  const _Incognita();

  @override
  Widget build(BuildContext context) => Container(
        width: 58,
        height: 58,
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: S.surface,
          shape: BoxShape.circle,
          border: Border.all(color: S.chart, width: 2),
        ),
        child: const Text(
          '?',
          style: TextStyle(
            fontSize: 26,
            fontWeight: FontWeight.w700,
            color: S.chart,
          ),
        ),
      );
}

class _Sinal extends StatelessWidget {
  final String texto;
  const _Sinal(this.texto);

  @override
  Widget build(BuildContext context) => Text(
        texto,
        style: const TextStyle(
          fontSize: 24,
          fontWeight: FontWeight.w700,
          color: S.txSoft,
        ),
      );
}

/// A mancha de cor que acompanha uma resposta.
///
/// Vai ao lado do nome e não em vez dele: a criança escolhe pela cor e lê o
/// nome ao mesmo tempo, e é assim que fica a saber que aquilo se chama
/// violeta.
class GotaDaOpcao extends StatelessWidget {
  final Color cor;
  const GotaDaOpcao({super.key, required this.cor});

  @override
  Widget build(BuildContext context) => Container(
        width: 30,
        height: 30,
        margin: const EdgeInsets.only(right: 12),
        decoration: BoxDecoration(
          color: cor,
          shape: BoxShape.circle,
          border: Border.all(color: S.line, width: 1.5),
        ),
      );
}
