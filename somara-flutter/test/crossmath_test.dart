import 'dart:math';
import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/crossmath.dart';

/// O gerador de Crossmath.
///
/// O que estes testes guardam é uma coisa só: **um puzzle não pode ter duas
/// respostas certas**. Se tiver, a app dá errado a uma criança que acertou —
/// e numa app que ensina não há defeito pior. Como os puzzles são gerados ao
/// acaso, não chega verificar um.
void main() {
  test('as seis contas fecham em qualquer grelha gerada', () {
    final g = GeradorCrossmath(Random(7));
    for (final dif in Dificuldade.values) {
      for (var i = 0; i < 200; i++) {
        final p = g.gerar(dif);
        for (final (esq, dir, res) in Crossmath.equacoes) {
          expect(
            p.valores[esq] + p.valores[dir],
            p.valores[res],
            reason: '${dif.rotulo}: $esq + $dir != $res em ${p.valores}',
          );
        }
      }
    }
  });

  test('cada puzzle gerado tem uma só solução', () {
    final g = GeradorCrossmath(Random(11));
    for (final dif in Dificuldade.values) {
      for (var i = 0; i < 200; i++) {
        final p = g.gerar(dif);
        expect(
          GeradorCrossmath.determinaSolucaoUnica(p.dadas),
          isTrue,
          reason: '${dif.rotulo}: pistas ${p.dadas} não fixam a solução',
        );
      }
    }
  });

  group('o teste rápido concorda com a força bruta', () {
    // O que a app usa é característica de matriz — rápido, mas não é
    // evidente à primeira vista que esteja certo. A força bruta é
    // evidentemente correcta e lenta de mais para o ecrã. Aqui confrontam-se
    // uma com a outra, num tecto pequeno onde a lenta ainda é viável.
    const tecto = 16;

    test('em todas as combinações de quatro pistas', () {
      final valores = GeradorCrossmath.grelhaDe(2, 3, 1, 4); // soma 10
      var comparadas = 0;

      for (var mascara = 0; mascara < 512; mascara++) {
        final dadas = [
          for (var i = 0; i < 9; i++) (mascara >> i) & 1 == 1,
        ];
        if (dadas.where((d) => d).length != 4) continue;

        final pistas = [
          for (var i = 0; i < 9; i++) dadas[i] ? valores[i] : null,
        ];
        final porForca = GeradorCrossmath.contarSolucoes(pistas, tecto);
        final porAlgebra = GeradorCrossmath.determinaSolucaoUnica(dadas);

        expect(porAlgebra, porForca == 1, reason: 'pistas $dadas');
        comparadas++;
      }

      expect(comparadas, 126, reason: 'as 126 escolhas de 4 entre 9');
    });

    test('três pistas nunca chegam', () {
      // Cada casa é combinação linear de quatro valores livres: com três
      // equações fica sempre uma família de soluções. Um puzzle assim
      // parece mais difícil e é apenas impossível.
      for (var mascara = 0; mascara < 512; mascara++) {
        final dadas = [for (var i = 0; i < 9; i++) (mascara >> i) & 1 == 1];
        if (dadas.where((d) => d).length != 3) continue;
        expect(GeradorCrossmath.determinaSolucaoUnica(dadas), isFalse);
      }
      expect(Dificuldade.values.map((d) => d.pistas).reduce(min),
          greaterThanOrEqualTo(4));
    });
  });

  test('os números não passam do tecto da dificuldade', () {
    // É isto que separa a 1ª classe da 6ª. Uma soma até 150 posta à frente
    // de quem está a aprender a contar até 20 não é um desafio, é um muro.
    final g = GeradorCrossmath(Random(3));
    for (final dif in Dificuldade.values) {
      for (var i = 0; i < 100; i++) {
        final p = g.gerar(dif);
        expect(p.valores.reduce(max), lessThanOrEqualTo(dif.tecto),
            reason: dif.rotulo);
        expect(p.valores.reduce(min), greaterThan(0),
            reason: '${dif.rotulo}: sem casas a zero nem negativas');
      }
    }
  });

  test('a dificuldade nota-se no número de casas por descobrir', () {
    final g = GeradorCrossmath(Random(5));
    for (final dif in Dificuldade.values) {
      expect(g.gerar(dif).porDescobrir, 9 - dif.pistas, reason: dif.rotulo);
    }
    expect(Dificuldade.facil.pistas, greaterThan(Dificuldade.dificil.pistas));
  });

  test('conferir aceita a solução e aponta o que está errado', () {
    final p = GeradorCrossmath(Random(2)).gerar(Dificuldade.medio);
    expect(p.conferir(p.valores), isEmpty);

    final vazia = p.dadas.indexOf(false);

    // Uma casa por preencher conta como errada, não como aceite.
    final incompleta = List<int?>.from(p.valores)..[vazia] = null;
    expect(p.conferir(incompleta), [vazia]);

    final errada = List<int?>.from(p.valores)..[vazia] = p.valores[vazia] + 1;
    expect(p.conferir(errada), [vazia]);
  });

  test('o puzzle do print resolve-se e é único', () {
    // O que veio do Facebook: 8 e 15 em cima, 9 e 24 em baixo — os quatro
    // cantos. A solução é 8+7=15 / 1+8=9 / 9+15=24.
    const cantos = [true, false, true, false, false, false, true, false, true];
    expect(GeradorCrossmath.determinaSolucaoUnica(cantos), isTrue);

    const pistas = <int?>[8, null, 15, null, null, null, 9, null, 24];
    expect(GeradorCrossmath.contarSolucoes(pistas, 24), 1);
    expect(GeradorCrossmath.grelhaDe(8, 7, 1, 8),
        [8, 7, 15, 1, 8, 9, 9, 15, 24]);
  });
}
