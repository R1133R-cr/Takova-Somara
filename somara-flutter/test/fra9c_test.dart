import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// O Francês da 9ª classe.
///
/// As duas unidades da 9ème do programa do INDE — «Ma famille», com sete
/// temas, e «L'école» outra vez, com dois — numa aula por tema. A regra
/// é a da 8ª: enunciado português, francês nas opções e nos pares.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso fra9() => c.cursos.firstWhere((x) => x.id == 'fra-9c');

  Iterable<Questao> perguntas() sync* {
    for (final u in fra9().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as duas unidades da 9ème, com os nove temas', () {
    expect(
      fra9().units.map((u) => u.titulo).toList(),
      ['A minha família', 'A escola, outra vez'],
    );
    expect(fra9().units[0].niveis.length, 7);
    expect(fra9().units[1].niveis.length, 2);
    expect(fra9().fonte, contains('9ème'));
    expect(fra9().provisorio, isFalse);
  });

  test('os enunciados são em português: o francês vai entre aspas ou nas opções', () {
    final francesSolto = RegExp(
      r'\b(le|la|les|est|et|vous|tu|je|dans|sur|avec|pour)\b',
    );
    for (final q in perguntas()) {
      final semCitacoes = q.q.replaceAll(RegExp('«[^»]*»'), '');
      expect(francesSolto.hasMatch(semCitacoes), isFalse,
          reason: 'francês solto num enunciado: "${q.q}"');
    }
  });

  test('a gramática da 9ème está nas opções certas', () {
    final escolhas = perguntas().whereType<QChoice>().toList();
    for (final q in escolhas) {
      expect(q.a, 0, reason: 'a certa não é a primeira: "${q.q}"');
    }
    final certas = escolhas.map((q) => q.options[q.a]).join('\n');
    for (final frase in const [
      'Ce livre est le mien',
      'Je mange du pain et je bois du lait',
      "Tu veux du riz ? Oui, j'en veux un peu",
      "Il n'y a personne dans la cuisine",
      "Je n'ai rien acheté",
      'Les élèves doivent faire les devoirs',
    ]) {
      expect(certas, contains(frase), reason: 'falta "$frase"');
    }
  });

  test('permissão, proibição e obrigação ligam-se ao regulamento', () {
    final regulamento = perguntas()
        .whereType<QMatch>()
        .firstWhere((q) => q.q.contains('regulamento'));
    expect(regulamento.pairs.map((p) => p.$2).toList(),
        ['Permissão', 'Proibição', 'Obrigação']);
  });
}
