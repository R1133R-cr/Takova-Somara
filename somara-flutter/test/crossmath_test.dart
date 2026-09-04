import 'dart:math';
import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/crossmath.dart';
import 'package:somara/models/escadaria.dart';

/// O gerador de Crossmath.
///
/// O que estes testes guardam é uma coisa só: **um puzzle não pode ter duas
/// respostas certas**. Se tiver, a app dá errado a uma criança que acertou —
/// e numa app que ensina não há defeito pior. Como os puzzles são gerados ao
/// acaso, não chega verificar um.
void main() {
  /// Degraus espalhados pela escadaria. Substituíram as três dificuldades
  /// fixas: já não se escolhe Fácil, Médio ou Difícil — sobe-se.
  const degraus = [1, 25, 100, 250, 500, 750, nivelMaximo];

  test('as seis contas fecham em qualquer grelha gerada', () {
    final g = GeradorCrossmath(Random(7));
    for (final n in degraus) {
      for (var i = 0; i < 200; i++) {
        final p = g.doNivel(n);
        for (final (esq, dir, res) in Crossmath.equacoes) {
          expect(
            p.valores[esq] + p.valores[dir],
            p.valores[res],
            reason: 'nível $n: $esq + $dir != $res em ${p.valores}',
          );
        }
      }
    }
  });

  test('cada puzzle gerado tem uma só solução', () {
    final g = GeradorCrossmath(Random(11));
    for (final n in degraus) {
      for (var i = 0; i < 200; i++) {
        final p = g.doNivel(n);
        expect(
          GeradorCrossmath.determinaSolucaoUnica(p.dadas),
          isTrue,
          reason: 'nível $n: pistas ${p.dadas} não fixam a solução',
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
      // E a escadaria nunca desce abaixo das quatro, em nenhum dos mil
      // degraus.
      for (var n = 1; n <= nivelMaximo; n++) {
        expect(crossmathNo(n).pistas, greaterThanOrEqualTo(4), reason: '$n');
      }
    });
  });

  test('os números não passam do tecto da dificuldade', () {
    // É isto que separa a 1ª classe da 6ª. Uma soma até 150 posta à frente
    // de quem está a aprender a contar até 20 não é um desafio, é um muro.
    final g = GeradorCrossmath(Random(3));
    for (final n in degraus) {
      for (var i = 0; i < 100; i++) {
        final p = g.doNivel(n);
        expect(p.valores.reduce(max), lessThanOrEqualTo(crossmathNo(n).tecto),
            reason: 'nível $n');
        expect(p.valores.reduce(min), greaterThan(0),
            reason: 'nível $n: sem casas a zero nem negativas');
      }
    }
  });

  test('o degrau nota-se no número de casas por descobrir', () {
    final g = GeradorCrossmath(Random(5));
    for (final n in degraus) {
      expect(g.doNivel(n).porDescobrir, 9 - crossmathNo(n).pistas,
          reason: 'nível $n');
    }
    expect(crossmathNo(1).pistas,
        greaterThan(crossmathNo(nivelMaximo).pistas));
  });

  test('os degraus de cima são mesmo maiores do que os de baixo', () {
    // O tecto do valor livre estava travado em 99, e por isso o canto nunca
    // passava de 396: do nível 400 para cima os puzzles eram todos iguais
    // uns aos outros, por muito que a escadaria dissesse outra coisa.
    final g = GeradorCrossmath(Random(9));
    var maiorEmBaixo = 0, maiorEmCima = 0;
    for (var i = 0; i < 200; i++) {
      final a = g.doNivel(1).valores.reduce(max);
      final b = g.doNivel(nivelMaximo).valores.reduce(max);
      if (a > maiorEmBaixo) maiorEmBaixo = a;
      if (b > maiorEmCima) maiorEmCima = b;
    }
    expect(maiorEmBaixo, lessThanOrEqualTo(crossmathNo(1).tecto));
    expect(crossmathNo(1).tecto, lessThan(30),
        reason: 'o primeiro degrau tem de caber em quem conta até 20');
    expect(maiorEmCima, greaterThan(500),
        reason: 'o último degrau nunca chegou perto do seu tecto');
  });

  test('conferir aceita a solução e aponta o que está errado', () {
    final p = GeradorCrossmath(Random(2)).doNivel(100);
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
