import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Educação Visual da 9ª classe.
///
/// Sete unidades do programa do INDE, pela ordem dele, da arte
/// moçambicana à perspectiva rigorosa. Duas coisas ficam guardadas: a
/// arte de cá está lá com os nomes certos, e as siglas da perspectiva
/// («PV», «LH», «PF», «LT») só aparecem nos pares, nunca no que a voz lê.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso ev9() => c.cursos.firstWhere((x) => x.id == 'ev-9c');

  Iterable<Questao> perguntas() sync* {
    for (final u in ev9().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as sete unidades do programa, pela ordem dele', () {
    expect(
      ev9().units.map((u) => u.titulo).toList(),
      [
        'Arte moçambicana e universal',
        'Comunicação visual',
        'Desenho geométrico',
        'Projecções ortogonais',
        'Formas em axonometria',
        'Perspectiva visual',
        'Perspectiva rigorosa',
      ],
    );
    expect(ev9().fonte, contains('pp. 34-42'));
    expect(ev9().provisorio, isFalse);
  });

  test('as siglas da perspectiva ficam nos pares', () {
    for (final q in perguntas()) {
      expect(q.q, isNot(matches(RegExp(r'\b(PV|LH|PF|LT|PQ|RP)\b'))),
          reason: 'sigla no enunciado: "${q.q}"');
    }
    final siglas = perguntas()
        .whereType<QMatch>()
        .expand((q) => q.pairs.map((p) => p.$2))
        .toList();
    expect(siglas, containsAll(['PV', 'LH', 'PF', 'LT']));
  });

  test('a arte moçambicana tem os nomes certos', () {
    final pares = perguntas()
        .whereType<QMatch>()
        .expand((q) => q.pairs.map((p) => '${p.$1} → ${p.$2}'))
        .toList();
    expect(pares, contains('Malangatana → Pintura'));
    expect(pares, contains('Alberto Chissano → Escultura'));
  });

  test('as três cónicas estão as três', () {
    final conicas = perguntas()
        .whereType<QMatch>()
        .firstWhere((q) => q.q.contains('curva cónica'))
        .pairs
        .map((p) => p.$1)
        .toList();
    expect(conicas, ['Elipse', 'Parábola', 'Hipérbole']);
  });
}
