import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/algoritmo_escrito.dart';

/// As contas armadas.
///
/// Este é o ficheiro que ensina o **método** e não a resposta, e por isso é
/// aqui que um erro custa mais caro: uma app que mostra um transporte errado
/// não está a falhar um exercício, está a ensinar mal. Um professor corrige;
/// isto repete-se a milhares de crianças sem ninguém dar por ele.
void main() {
  /// Lê a grelha como se lê o caderno: linha a linha, da esquerda para a
  /// direita, com pontos nas casinhas vazias.
  String desenhar(GrelhaDaConta g) {
    final linhas = <String>[];
    for (var l = 0; l < g.linhas; l++) {
      final b = StringBuffer();
      for (var c = 0; c < g.colunas; c++) {
        final casa = g.em(l, c);
        b.write(casa == null ? '.' : casa.texto.padLeft(2, '_'));
        b.write(' ');
      }
      linhas.add(b.toString().trimRight());
    }
    return linhas.join('\n');
  }

  /// As respostas certas, pela ordem em que se preenchem.
  List<String> gabarito(GrelhaDaConta g) =>
      g.aPreencher.map((c) => c.texto).toList();

  group('a grelha está bem formada', () {
    /// Vale para as quatro: nenhuma casinha fora da grelha, nenhuma em cima
    /// de outra. Duas casinhas na mesma posição davam um desenho em que uma
    /// tapava a outra, e a criança escrevia numa que não via.
    void conferir(GrelhaDaConta g, String nome) {
      final ocupadas = <String>{};
      for (final c in g.casas) {
        expect(c.linha, inInclusiveRange(0, g.linhas - 1), reason: '$nome $c');
        expect(c.coluna, inInclusiveRange(0, g.colunas - 1), reason: '$nome $c');
        expect(ocupadas.add('${c.linha}:${c.coluna}'), isTrue,
            reason: '$nome: duas casinhas em ${c.linha},${c.coluna}');
        expect(c.texto, isNotEmpty, reason: '$nome $c');
      }
      for (final t in g.tracos) {
        expect(t.linha, inInclusiveRange(0, g.linhas - 1), reason: nome);
        expect(t.de, lessThanOrEqualTo(t.ate), reason: nome);
        expect(t.ate, lessThan(g.colunas), reason: nome);
      }
    }

    test('adição, em mil pares', () {
      final r = Random(1);
      for (var i = 0; i < 1000; i++) {
        final a = r.nextInt(9999), b = r.nextInt(9999);
        final g = GrelhaDaConta.de(Operacao.adicao, a, b);
        expect(g.resultado, a + b, reason: '$a + $b');
        conferir(g, '$a + $b');
      }
    });

    test('subtracção, em mil pares', () {
      final r = Random(2);
      for (var i = 0; i < 1000; i++) {
        final x = r.nextInt(9999), y = r.nextInt(9999);
        final a = x > y ? x : y, b = x > y ? y : x;
        final g = GrelhaDaConta.de(Operacao.subtraccao, a, b);
        expect(g.resultado, a - b, reason: '$a − $b');
        conferir(g, '$a − $b');
      }
    });

    test('multiplicação, em mil pares', () {
      final r = Random(3);
      for (var i = 0; i < 1000; i++) {
        final a = r.nextInt(999), b = r.nextInt(99);
        final g = GrelhaDaConta.de(Operacao.multiplicacao, a, b);
        expect(g.resultado, a * b, reason: '$a × $b');
        conferir(g, '$a × $b');
      }
    });

    test('divisão, em mil pares', () {
      final r = Random(4);
      for (var i = 0; i < 1000; i++) {
        final a = r.nextInt(9999), b = 1 + r.nextInt(98);
        final g = GrelhaDaConta.de(Operacao.divisao, a, b);
        expect(g.resultado, a ~/ b, reason: '$a ÷ $b');
        expect(g.resto, a % b, reason: '$a ÷ $b');
        conferir(g, '$a ÷ $b');
      }
    });
  });

  group('a adição', () {
    test('o "vai um" fica por cima da coluna onde vai ser somado', () {
      final g = GrelhaDaConta.de(Operacao.adicao, 247, 185);
      expect(desenhar(g), '''
. _1 _1 .
. _2 _4 _7
_+ _1 _8 _5
. _4 _3 _2''');
    });

    test('sem transporte não há casinhas por cima', () {
      final g = GrelhaDaConta.de(Operacao.adicao, 12, 34);
      expect(g.casas.where((c) => c.papel == Papel.transporte), isEmpty);
      expect(gabarito(g), ['6', '4']);
    });

    test('o transporte que faz crescer o número tem lugar', () {
      // 95 + 15 = 110: a soma tem três ordens e os operandos duas. A coluna
      // das centenas existe na mesma, e o "vai um" vai para lá.
      final g = GrelhaDaConta.de(Operacao.adicao, 95, 15);
      expect(g.resultado, 110);
      expect(g.casas.where((c) => c.papel == Papel.transporte), hasLength(2));
      expect(gabarito(g).where((t) => t != '1').length, greaterThan(0));
    });

    test('as respostas certas dão certo, e um dígito trocado dá errado', () {
      final g = GrelhaDaConta.de(Operacao.adicao, 247, 185);
      final certas = gabarito(g);
      expect(g.certa(certas), isTrue);

      final erradas = [...certas];
      final ondeConta = g.aPreencher.indexWhere((c) => c.conta);
      erradas[ondeConta] = '9';
      expect(g.certa(erradas), isFalse);
    });

    test('errar o transporte e acertar o resultado conta como certo', () {
      // A regra do §9: o transporte assinala-se mas não reprova. Quem chega
      // ao resultado certo fez a conta certa, mesmo que tenha somado o "vai
      // um" de cabeça.
      final g = GrelhaDaConta.de(Operacao.adicao, 247, 185);
      final r = gabarito(g);
      final ondeTransporte =
          g.aPreencher.indexWhere((c) => c.papel == Papel.transporte);
      expect(ondeTransporte, greaterThanOrEqualTo(0));
      r[ondeTransporte] = '7';
      expect(g.certa(r), isTrue);
    });

    test('deixar em branco dá errado', () {
      final g = GrelhaDaConta.de(Operacao.adicao, 247, 185);
      expect(g.certa(const []), isFalse);
      expect(g.certa(List.filled(gabarito(g).length, '')), isFalse);
    });
  });

  group('a subtracção', () {
    test('o dígito que empresta fica riscado e o novo valor por cima', () {
      final g = GrelhaDaConta.de(Operacao.subtraccao, 643, 287);
      expect(desenhar(g), '''
. _5 13 13
. _6 _4 _3
_− _2 _8 _7
. _3 _5 _6''');

      // As três ordens de cima estão riscadas: as duas que pediram e a que
      // só emprestou.
      final riscados =
          g.casas.where((c) => c.linha == 1 && c.riscado).toList();
      expect(riscados, hasLength(3));
    });

    test('a ordem que pede E empresta vale treze, não catorze', () {
      // O desenho do SPEC escrevia 14 nas dezenas. Está errado: as dezenas
      // já tinham emprestado uma unidade antes de pedirem, e por isso valem
      // 4 − 1 + 10 = 13. Com 14 a conta não fecha.
      final g = GrelhaDaConta.de(Operacao.subtraccao, 643, 287);
      final dezenas = g.em(0, 2)!;
      expect(dezenas.texto, '13');
      expect(int.parse(dezenas.texto) - 8, 5, reason: 'a ordem tem de fechar');
    });

    test('o empréstimo em cadeia, através dos zeros', () {
      final g = GrelhaDaConta.de(Operacao.subtraccao, 600, 1);
      expect(g.resultado, 599);
      expect(g.em(0, 3)!.texto, '10');
      expect(g.em(0, 2)!.texto, '9');
      expect(g.em(0, 1)!.texto, '5');
    });

    test('sem empréstimo não há nada por cima', () {
      final g = GrelhaDaConta.de(Operacao.subtraccao, 897, 234);
      expect(g.casas.where((c) => c.papel == Papel.transporte), isEmpty);
      expect(g.casas.where((c) => c.riscado), isEmpty);
    });

    test('não se arma uma que dê negativo', () {
      expect(() => GrelhaDaConta.de(Operacao.subtraccao, 3, 9),
          throwsArgumentError);
    });
  });

  group('a multiplicação', () {
    test('os produtos parciais, com o deslocamento à vista', () {
      final g = GrelhaDaConta.de(Operacao.multiplicacao, 24, 13);
      expect(desenhar(g), '''
. . _2 _4
_× . _1 _3
. . _7 _2
. _2 _4 _·
. _3 _1 _2''');
      expect(g.resultado, 312);
    });

    test('com um algarismo no multiplicador não há produtos parciais', () {
      // O primeiro produto JÁ é o resultado. Escrevê-lo duas vezes ensinava
      // um passo do algoritmo que não existe.
      final g = GrelhaDaConta.de(Operacao.multiplicacao, 24, 3);
      expect(g.casas.where((c) => c.papel == Papel.produto), isEmpty);
      expect(gabarito(g), ['2', '7']);
      expect(g.linhas, 3);
    });

    test('por zero dá zero, e arma-se na mesma', () {
      final g = GrelhaDaConta.de(Operacao.multiplicacao, 24, 0);
      expect(g.resultado, 0);
      expect(g.certa(gabarito(g)), isTrue);
    });

    test('o gabarito preenche-se e dá certo', () {
      for (final par in const [(24, 13), (7, 8), (123, 45), (99, 99)]) {
        final g = GrelhaDaConta.de(Operacao.multiplicacao, par.$1, par.$2);
        expect(g.certa(gabarito(g)), isTrue, reason: '${par.$1} × ${par.$2}');
      }
    });
  });

  group('a divisão', () {
    test('a chave, com os abaixamentos', () {
      final g = GrelhaDaConta.de(Operacao.divisao, 144, 12);
      expect(g.resultado, 12);
      expect(g.resto, 0);
      expect(g.barra, 4);
      expect(desenhar(g), '''
. _1 _4 _4 . _1 _2
_− _1 _2 . . . .
. . _2 _4 . _1 _2
_− . _2 _4 . . .
. . . _0 . . .''');
    });

    test('o quociente é do tamanho certo', () {
      final g = GrelhaDaConta.de(Operacao.divisao, 875, 5);
      expect(g.resultado, 175);
      expect(g.casas.where((c) => c.papel == Papel.quociente), hasLength(3));
    });

    test('com resto, o último resto é o resto', () {
      final g = GrelhaDaConta.de(Operacao.divisao, 145, 12);
      expect(g.resultado, 12);
      expect(g.resto, 1);
      final restos = g.casas.where((c) => c.papel == Papel.resto).toList();
      expect(restos.last.texto, '1');
    });

    test('um dividendo menor do que o divisor não parte a grelha', () {
      // 3 a dividir por 5: não há passo nenhum, mas o quociente zero tem de
      // caber na mesma. Sem isto a grelha tinha uma linha e o quociente
      // ficava fora dela.
      final g = GrelhaDaConta.de(Operacao.divisao, 3, 5);
      expect(g.resultado, 0);
      expect(g.linhas, greaterThanOrEqualTo(3));
      for (final c in g.casas) {
        expect(c.linha, lessThan(g.linhas));
      }
    });

    test('não se divide por zero', () {
      expect(
        () => GrelhaDaConta.de(Operacao.divisao, 10, 0),
        throwsArgumentError,
      );
    });

    test('o gabarito preenche-se e dá certo', () {
      for (final par in const [(144, 12), (875, 5), (145, 12), (9, 3)]) {
        final g = GrelhaDaConta.de(Operacao.divisao, par.$1, par.$2);
        expect(g.certa(gabarito(g)), isTrue, reason: '${par.$1} ÷ ${par.$2}');
      }
    });
  });

  group('a ordem de preenchimento', () {
    test('é a do algoritmo: da direita para a esquerda', () {
      final g = GrelhaDaConta.de(Operacao.adicao, 247, 185);
      final ordem = g.aPreencher;
      for (var i = 1; i < ordem.length; i++) {
        final antes = ordem[i - 1], agora = ordem[i];
        expect(
          antes.linha < agora.linha ||
              (antes.linha == agora.linha && antes.coluna > agora.coluna),
          isTrue,
          reason: 'a ordem saltou de $antes para $agora',
        );
      }
    });

    test('as casinhas fixas não entram', () {
      for (final op in Operacao.values) {
        final g = GrelhaDaConta.de(op, 144, 12);
        expect(g.aPreencher.every((c) => c.papel != Papel.fixa), isTrue,
            reason: op.name);
        expect(g.aPreencher, isNotEmpty, reason: op.name);
      }
    });
  });

  test('o enunciado diz-se por extenso', () {
    expect(GrelhaDaConta.de(Operacao.adicao, 247, 185).dito, '247 mais 185');
    expect(
      GrelhaDaConta.de(Operacao.divisao, 144, 12).dito,
      '144 a dividir por 12',
    );
  });
}
