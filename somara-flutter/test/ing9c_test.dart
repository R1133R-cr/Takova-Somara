import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// O Inglês da 9ª classe.
///
/// As nove unidades do Grade 9 do programa do INDE, pela ordem dele. A
/// regra é a da 7ª e da 8ª: a voz é portuguesa, o enunciado é português e
/// o inglês fica nas opções e nos pares.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso ing9() => c.cursos.firstWhere((x) => x.id == 'ing-9c');

  Iterable<Questao> perguntas() sync* {
    for (final u in ing9().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as nove unidades do Grade 9, pela ordem do programa', () {
    expect(
      ing9().units.map((u) => u.titulo).toList(),
      [
        'O inglês no mundo dos negócios',
        'A importância da educação',
        'Direitos humanos e género',
        'A economia e a agricultura',
        'Fazer negócio',
        'Disciplinas e profissões futuras',
        'Ciência e tecnologia no século XXI',
        'Pessoas famosas e de sucesso',
        'A vida depois da escola',
      ],
    );
    expect(ing9().fonte, contains('Grade 9'));
    expect(ing9().fonte, contains('pp. 48-63'));
    expect(ing9().provisorio, isFalse);
  });

  test('os enunciados são em português: o inglês vai entre aspas ou nas opções', () {
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

  test('a gramática do Grade 9 está nas opções, e a certa é a primeira', () {
    final escolhas = perguntas().whereType<QChoice>().toList();
    for (final q in escolhas) {
      expect(q.a, 0, reason: 'a certa não é a primeira: "${q.q}"');
    }
    final certas = escolhas.map((q) => q.options[q.a]).join('\n');
    for (final frase in const [
      'English is as important as Portuguese',
      'I have been studying for two hours',
      'Neither the father nor the mother can hit the children',
      'Cashew is exported to India',
      'A doctor is a person who treats sick people',
      'I had never used a computer before 2020',
      'He said that he was a teacher',
      'If I had money, I would open a shop',
    ]) {
      expect(certas, contains(frase), reason: 'falta "$frase"');
    }
  });

  test('as figuras moçambicanas estão na unidade das pessoas famosas', () {
    final pares = perguntas()
        .whereType<QMatch>()
        .expand((q) => q.pairs.map((p) => p.$1))
        .toList();
    expect(pares, containsAll(['Maria de Lurdes Mutola', 'Malangatana', 'Eduardo Mondlane']));
  });
}
