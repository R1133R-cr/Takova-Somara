import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// O Francês da 8ª classe — o primeiro Francês da app.
///
/// O programa do INDE é do 1º ciclo do secundário e, para o Francês, o
/// 1º ciclo são a 8ª e a 9ª: a 7ª não o tem. E a regra do Inglês vale
/// aqui: a voz da app é portuguesa, os enunciados são em português e o
/// francês fica nas opções e nos pares.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso fra8() => c.cursos.firstWhere((x) => x.id == 'fra-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in fra8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as duas unidades da 8ème, pela ordem do programa', () {
    expect(
      fra8().units.map((u) => u.titulo).toList(),
      ['Os meus amigos e eu', 'A escola e o dia-a-dia'],
    );
    // Os nove temas do programa: três na primeira (o primeiro em duas
    // aulas) e seis na segunda.
    expect(fra8().units[0].niveis.length, 4);
    expect(fra8().units[1].niveis.length, 6);
  });

  test('o Francês começa na 8ª: a 7ª não o tem', () {
    expect(
      c.cursos.where((x) => x.classe == '7ª classe').map((x) => x.disciplina),
      isNot(contains('Francês')),
    );
    expect(fra8().classe, '8ª classe');
    expect(fra8().fonte, contains('8ème'));
    expect(fra8().provisorio, isFalse);
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

  test('o francês está nas opções, e a certa é sempre a primeira', () {
    final escolhas = perguntas().whereType<QChoice>().toList();
    expect(escolhas.length, greaterThanOrEqualTo(28));
    for (final q in escolhas) {
      expect(q.a, 0, reason: 'a certa não é a primeira: "${q.q}"');
    }
    final todas = escolhas.expand((q) => q.options).join('\n');
    for (final frase in const [
      "Je m'appelle Amina",
      'Tu as quatorze ans',
      "Il n'est pas français",
      'Paulo est plus grand que João',
      'Ouvrez le livre',
      'Je me lève à six heures',
      "Il n'y a pas d'ordinateur",
      'Son sac à dos est grand et vert',
    ]) {
      expect(todas, contains(frase), reason: 'falta "$frase"');
    }
  });

  test('os pares ligam português a francês', () {
    final pares = perguntas().whereType<QMatch>().toList();
    expect(pares.length, greaterThanOrEqualTo(18));
    final direitos = pares.expand((q) => q.pairs.map((p) => p.$2)).toList();
    expect(direitos, contains('Bonjour'));
    expect(direitos, contains('Lundi'));
    expect(direitos, contains('Le tableau'));
    expect(direitos, contains('Janvier'));
  });
}
