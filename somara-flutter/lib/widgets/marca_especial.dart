import 'dart:math';

import 'package:flutter/material.dart';

import '../models/pomar.dart';
import '../theme.dart';

/// O que distingue uma peça especial de uma peça comum, à vista.
///
/// Marcas por baixo do produto e não outro desenho: a criança tem de
/// continuar a ver que aquilo é uma manga, senão deixa de poder planear com
/// ela. A marca diz o que a peça faz — as riscas apontam para onde vai
/// limpar.
///
/// Vive num ficheiro seu e não dentro do ecrã do Pomar por uma razão
/// prática: dentro do ecrã era um método privado do State e não havia
/// maneira de o desenhar num teste. Uma peça especial só aparece depois de
/// um quatro-em-linha, e um tabuleiro sorteado não oferece isso quando se
/// quer. Assim as quatro marcas podem ser postas lado a lado e vistas.
class MarcaDeEspecial extends StatelessWidget {
  final Especial especial;

  /// O lado da casa do tabuleiro. Tudo aqui é medido a partir dele, para a
  /// marca acompanhar o tamanho da peça em qualquer telemóvel.
  final double lado;

  const MarcaDeEspecial({
    super.key,
    required this.especial,
    required this.lado,
  });

  @override
  Widget build(BuildContext context) {
    switch (especial) {
      case Especial.riscadoH:
      case Especial.riscadoV:
        return Transform.rotate(
          angle: especial == Especial.riscadoH ? 0 : pi / 2,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              for (var k = 0; k < 3; k++) ...[
                Container(
                  width: lado * 0.78,
                  height: 3,
                  color: S.chart.withValues(alpha: 0.85),
                ),
                if (k < 2) SizedBox(height: lado * 0.13),
              ],
            ],
          ),
        );

      case Especial.embrulho:
        return Container(
          width: lado * 0.82,
          height: lado * 0.82,
          decoration: BoxDecoration(
            border: Border.all(color: S.gold, width: 3),
            borderRadius: BorderRadius.circular(6),
            boxShadow: [
              BoxShadow(color: S.gold.withValues(alpha: 0.45), blurRadius: 9),
            ],
          ),
        );

      case Especial.sol:
        return Container(
          width: lado * 0.86,
          height: lado * 0.86,
          decoration: BoxDecoration(
            shape: BoxShape.circle,
            gradient: const SweepGradient(
              colors: [S.gold, S.chart, S.life, S.green300, S.gold],
            ),
            boxShadow: [
              BoxShadow(color: S.gold.withValues(alpha: 0.6), blurRadius: 12),
            ],
          ),
        );

      case Especial.nenhuma:
        return const SizedBox.shrink();
    }
  }
}
