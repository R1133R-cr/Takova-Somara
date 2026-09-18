import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Educação Física da 8ª classe.
///
/// Cinco unidades: as que a tabela da p. 23 do programa do INDE dá à 8ª.
/// O Andebol, que é a unidade IV do ciclo, é da 7ª e não está aqui; o
/// Basquetebol e o Futebol são novos. E vale o critério da 7ª: a app não
/// corre, por isso pergunta-se o que o corpo precisa de saber antes —
/// regras, técnica, segurança.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso edf8() => c.cursos.firstWhere((x) => x.id == 'edf-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in edf8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as cinco unidades da 8ª, pela ordem do plano temático', () {
    expect(
      edf8().units.map((u) => u.titulo).toList(),
      [
        'Danças e jogos educativos',
        'Ginástica',
        'Atletismo',
        'Basquetebol',
        'Futebol',
      ],
    );
  });

  test('o Andebol é da 7ª e o Basquetebol é da 8ª', () {
    final na7 = c.cursos
        .firstWhere((x) => x.id == 'edf-7c')
        .units
        .map((u) => u.titulo);
    expect(na7, contains('Andebol'));
    expect(na7, isNot(contains('Basquetebol')));
    expect(edf8().units.map((u) => u.titulo), isNot(contains('Andebol')));
  });

  test('a fonte diz o programa e as páginas', () {
    expect(edf8().fonte, contains('INDE'));
    expect(edf8().fonte, contains('pp. 23-32'));
    expect(edf8().provisorio, isFalse);
  });

  test('as danças são as de Moçambique, com a zona certa', () {
    final pares = perguntas()
        .whereType<QMatch>()
        .expand((q) => q.pairs.map((p) => '${p.$1} → ${p.$2}'))
        .toList();
    expect(pares, contains('Nhau → Niassa e Tete'));
    expect(pares, contains('Mapiko → Cabo Delgado'));
  });

  test('as quatro fases do salto em comprimento estão pela ordem', () {
    final salto = perguntas()
        .whereType<QMatch>()
        .firstWhere((q) => q.pairs.any((p) => p.$1 == 'Chamada'));
    expect(
      salto.pairs.map((p) => p.$1).toList(),
      ['Corrida de balanço', 'Chamada', 'Voo', 'Queda'],
    );
  });
}
