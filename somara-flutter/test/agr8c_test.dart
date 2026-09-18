import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Agropecuária da 8ª classe.
///
/// Seis unidades do programa do INDE pela ordem dele: quatro de culturas
/// — hortícolas, leguminosas de grão, raízes e tubérculos, cereais — e
/// duas de criação, coelhos e suínos. As quatro de culturas seguem o
/// mesmo esquema do programa (origem, importância, botânica, variedades,
/// clima e solo, propagação, época, práticas culturais, colheita), e as
/// perguntas também.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso agr8() => c.cursos.firstWhere((x) => x.id == 'agr-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in agr8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as seis unidades do programa, pela ordem dele', () {
    expect(
      agr8().units.map((u) => u.titulo).toList(),
      [
        'Culturas alimentares: as hortícolas',
        'Leguminosas de grão',
        'Raízes e tubérculos',
        'Cultivo dos cereais',
        'Criação de coelhos',
        'Criação de suínos',
      ],
    );
  });

  test('a fonte diz o programa e as páginas', () {
    expect(agr8().fonte, contains('INDE'));
    expect(agr8().fonte, contains('pp. 37-49'));
    expect(agr8().provisorio, isFalse);
  });

  test('as culturas são as do programa, com o nome de cá', () {
    final texto = perguntas()
        .map((q) => q is QMatch
            ? '${q.q} ${q.pairs.expand((p) => [p.$1, p.$2]).join(' ')}'
            : q.q)
        .join('\n');
    for (final cultura in const [
      'nhemba',
      'bóer',
      'Mandioca',
      'Batata-reno',
      'Inhame',
      'mapira',
      'mexoeira',
    ]) {
      expect(texto, contains(cultura), reason: 'falta "$cultura"');
    }
  });

  test('as doenças dos coelhos e dos porcos são as do programa', () {
    final pares = perguntas()
        .whereType<QMatch>()
        .expand((q) => q.pairs.map((p) => p.$1))
        .toList();
    expect(pares, containsAll(['Coccidiose', 'Sarna', 'Coriza']));
    expect(pares, containsAll(['Peste suína africana', 'Mal-rubro']));
  });

  test('há contas de machamba, e dão inteiros', () {
    // Plantas por linha, grãos por cova, estacas por metro, leitões por
    // ano: a agropecuária também se conta.
    final numericas = perguntas()
        .whereType<QInput>()
        .where((q) => RegExp(r'^\d+$').hasMatch(q.a))
        .toList();
    expect(numericas.length, greaterThanOrEqualTo(6));
  });
}
