import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// O Inglês da 8ª classe.
///
/// A regra que este teste guarda é a da 7ª: a voz da app é portuguesa,
/// por isso os enunciados são em português e o inglês fica nas opções e
/// nos pares, que se lêem e não se ouvem. E as nove unidades do Grade 8
/// do programa estão as nove, pela ordem dele.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso ing8() => c.cursos.firstWhere((x) => x.id == 'ing-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in ing8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as nove unidades do Grade 8, pela ordem do programa', () {
    expect(
      ing8().units.map((u) => u.titulo).toList(),
      [
        'O inglês em Moçambique',
        'Medicina moderna e tradicional',
        'Costumes e tradições',
        'A agricultura',
        'As compras',
        'Turismo e vida selvagem',
        'Cuidar do planeta',
        'Saúde e forma física',
        'Ofícios e profissões',
      ],
    );
  });

  test('a fonte diz o programa e as páginas', () {
    expect(ing8().fonte, contains('INDE'));
    expect(ing8().fonte, contains('Grade 8'));
    expect(ing8().fonte, contains('pp. 31-46'));
    expect(ing8().provisorio, isFalse);
  });

  test('os enunciados são em português: o inglês vai entre aspas ou nas opções', () {
    // Um enunciado pode citar uma frase portuguesa entre «», mas nunca
    // uma palavra inglesa solta: a voz lê-la-ia à portuguesa.
    final inglesSolto = RegExp(
      r'\b(the|and|is|are|you|what|where|how|with|this|that)\b',
      caseSensitive: false,
    );
    for (final q in perguntas()) {
      final semCitacoes = q.q.replaceAll(RegExp('«[^»]*»'), '');
      expect(inglesSolto.hasMatch(semCitacoes), isFalse,
          reason: 'inglês solto num enunciado: "${q.q}"');
    }
  });

  test('o inglês está nas opções, e a certa é sempre a primeira', () {
    final escolhas = perguntas().whereType<QChoice>().toList();
    expect(escolhas.length, greaterThanOrEqualTo(40));
    for (final q in escolhas) {
      expect(q.a, 0, reason: 'a certa não é a primeira: "${q.q}"');
    }
    final todas = escolhas.expand((q) => q.options).join('\n');
    for (final frase in const [
      'She works in a hotel',
      'If it rains, we will stay at home',
      'We must respect the elders',
      'The fish is dried in the sun',
      'How much is this shirt',
      'Gorongosa is the most famous park in Mozambique',
      'If I were president, I would protect the forests',
      'One child, three children',
      'She is a nurse, isn\'t she',
    ]) {
      expect(todas, contains(frase), reason: 'falta "$frase"');
    }
  });

  test('os pares ligam português a inglês', () {
    final pares = perguntas().whereType<QMatch>().toList();
    expect(pares.length, greaterThanOrEqualTo(12));
    final direitos = pares.expand((q) => q.pairs.map((p) => p.$2)).toList();
    expect(direitos, contains('South Africa'));
    expect(direitos, contains('Hoe'));
    expect(direitos, contains('Elephant'));
    expect(direitos, contains('Nurse'));
  });
}
