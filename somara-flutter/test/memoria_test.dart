import 'dart:math';
import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/memoria.dart';

/// O jogo da memória.
///
/// O defeito que estes testes impedem é subtil e cruel: dois pares iguais
/// no mesmo tabuleiro. A criança junta duas cartas que casam de facto, o
/// jogo recusa, e ela não tem como saber porquê.
void main() {
  test('o tabuleiro traz o número de pares pedido, cada carta com o seu', () {
    for (final b in Baralho.values) {
      for (var s = 0; s < 8; s++) {
        final j = JogoDaMemoria.novo(baralho: b, pares: 6, rnd: Random(s));
        expect(j.cartas.length, 12, reason: '${b.rotulo}/$s');

        final contagem = <int, int>{};
        for (final c in j.cartas) {
          contagem[c.par] = (contagem[c.par] ?? 0) + 1;
        }
        expect(contagem.length, 6, reason: '${b.rotulo}: pares a mais ou a menos');
        for (final n in contagem.values) {
          expect(n, 2, reason: '${b.rotulo}: um par tem $n cartas');
        }
      }
    }
  });

  test('nenhum par se repete no mesmo tabuleiro', () {
    // Dois pares iguais dariam quatro cartas que casam entre si, e a
    // criança que juntasse as "erradas" via o jogo recusar uma jogada certa.
    for (final b in Baralho.values) {
      for (var s = 0; s < 10; s++) {
        final j = JogoDaMemoria.novo(baralho: b, pares: 6, rnd: Random(s));
        final faces = <String>{};
        for (final c in j.cartas) {
          expect(faces.add(c.face), isTrue,
              reason: '${b.rotulo}/$s: "${c.face}" aparece duas vezes');
        }
      }
    }
  });

  group('as contas dos pares estão certas', () {
    /// Junta cada par pelo número que o identifica.
    Map<int, List<String>> porPar(JogoDaMemoria j) {
      final m = <int, List<String>>{};
      for (final c in j.cartas) {
        (m[c.par] ??= []).add(c.face);
      }
      return m;
    }

    test('contar: o número bate com a quantidade de desenhos', () {
      final j = JogoDaMemoria.novo(
          baralho: Baralho.quantidade, pares: 6, rnd: Random(3));
      porPar(j).forEach((_, faces) {
        final numero = faces.firstWhere((f) => int.tryParse(f) != null);
        final desenho = faces.firstWhere((f) => int.tryParse(f) == null);
        // Os emoji usados aqui são todos de um só ponto de código.
        expect(desenho.runes.length, int.parse(numero),
            reason: '$numero não bate com "$desenho"');
      });
    });

    test('somas: o resultado é mesmo a soma', () {
      final j =
          JogoDaMemoria.novo(baralho: Baralho.somas, pares: 6, rnd: Random(5));
      porPar(j).forEach((_, faces) {
        final conta = faces.firstWhere((f) => f.contains('+'));
        final total = faces.firstWhere((f) => !f.contains('+'));
        final partes = conta.split('+').map((x) => int.parse(x.trim()));
        expect(partes.reduce((a, b) => a + b), int.parse(total));
      });
    });

    test('dobros e metades: a conta fecha e dá sempre número inteiro', () {
      // Metade de ímpar daria fracção, e estas crianças ainda não as viram.
      final j =
          JogoDaMemoria.novo(baralho: Baralho.dobros, pares: 6, rnd: Random(7));
      porPar(j).forEach((_, faces) {
        final conta = faces.firstWhere((f) => f.contains('de'));
        final valor = int.parse(faces.firstWhere((f) => !f.contains('de')));
        final n = int.parse(conta.split(' ').last);
        if (conta.startsWith('dobro')) {
          expect(valor, n * 2);
        } else {
          expect(n.isEven, isTrue, reason: 'metade de ímpar: $conta');
          expect(valor, n ~/ 2);
        }
      });
    });
  });

  test('o baralho é embaralhado, não fica com os pares lado a lado', () {
    // Sem embaralhar, a primeira carta e a segunda seriam sempre par e o
    // jogo resolvia-se sem se olhar para nada.
    var seguidos = 0;
    for (var s = 0; s < 20; s++) {
      final j = JogoDaMemoria.novo(
          baralho: Baralho.somas, pares: 6, rnd: Random(s));
      for (var i = 0; i < j.cartas.length - 1; i += 2) {
        if (j.cartas[i].par == j.cartas[i + 1].par) seguidos++;
      }
    }
    expect(seguidos, lessThan(20),
        reason: 'demasiados pares lado a lado — não está embaralhado');
  });

  test('cada baralho diz para que classes serve', () {
    for (final b in Baralho.values) {
      expect(b.rotulo.isNotEmpty, isTrue);
      expect(b.explica.isNotEmpty, isTrue);
      expect(b.classes, contains('classe'));
    }
  });
}
