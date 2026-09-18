import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A História da 8ª classe — do Antigo Regime ao Imperialismo.
///
/// O programa do INDE mete Moçambique dentro de todas as unidades: a
/// expansão portuguesa e o tráfico, os prazos da Zambézia, a partilha
/// imperialista, Ngungunhane e o Barué. É isso que aqui se guarda: que a
/// História da 8ª não é a História da Europa com uma nota de rodapé.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso his8() => c.cursos.firstWhere((x) => x.id == 'his-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in his8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  String tudo() => [
        for (final q in perguntas()) ...[
          q.q,
          if (q is QChoice) ...q.options,
          if (q is QMatch) ...q.pairs.expand((p) => [p.$1, p.$2]),
        ],
      ].join('\n');

  test('as quatro unidades do programa, pela ordem dele', () {
    expect(
      his8().units.map((u) => u.titulo).toList(),
      [
        'A formação do sistema capitalista',
        'África e Moçambique na época das revoluções',
        'A Revolução Industrial e o movimento operário',
        'Do capitalismo industrial ao imperialismo',
      ],
    );
    // A primeira ocupa dois trimestres no INDE, e por isso é a maior.
    expect(his8().units.first.niveis.length, greaterThanOrEqualTo(4));
  });

  test('a fonte diz o programa e as páginas', () {
    expect(his8().fonte, contains('INDE'));
    expect(his8().fonte, contains('pp. 24-34'));
    expect(his8().provisorio, isFalse);
  });

  test('Moçambique está em todas as unidades', () {
    for (final u in his8().units) {
      final texto = [
        for (final n in u.niveis)
          for (final q in n.questoes) ...[
            q.q,
            if (q is QChoice) ...q.options,
            if (q is QMatch) ...q.pairs.expand((p) => [p.$1, p.$2]),
          ],
      ].join('\n');
      expect(texto, contains('Moçambique'), reason: u.titulo);
    }
  });

  test('as datas que se decoram estão lá, e são respostas escritas', () {
    // 1498, 1787, 1789, 1895: as quatro que o programa põe no centro.
    final datas = perguntas()
        .whereType<QInput>()
        .map((q) => q.a)
        .where((a) => RegExp(r'^\d{4}$').hasMatch(a))
        .toSet();
    expect(datas, containsAll(['1498', '1787', '1789', '1895']));
  });

  test('a resistência africana tem nomes, não só a palavra', () {
    final t = tudo();
    for (final nome in const ['Ngungunhane', 'Barué', 'Isandlwana']) {
      expect(t, contains(nome), reason: 'falta $nome');
    }
  });
}
