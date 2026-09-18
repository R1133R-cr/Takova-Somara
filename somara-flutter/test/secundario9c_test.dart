import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A 9ª classe inteira — e com ela o 1º ciclo do secundário.
///
/// Os testes de cada disciplina estão nos seus ficheiros. Este guarda o que
/// só se vê olhando para a classe toda: quantas são, quais são, e quais
/// não estão e porquê.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  List<Curso> da9() =>
      c.cursos.where((x) => x.classe == '9ª classe').toList();

  test('o plano de estudos da 9ª classe está coberto por inteiro', () {
    expect(
      da9().map((x) => x.disciplina).toSet(),
      {
        'Matemática',
        'Português',
        'Inglês',
        'Francês',
        'História',
        'Geografia',
        'Biologia',
        'Física',
        'Química',
        'Educação Visual',
        'Educação Física',
      },
    );
    expect(da9(), hasLength(11));
  });

  test('a TIC e a Agropecuária não estão — e não é esquecimento', () {
    // O programa das TIC chama-se «7ª e 8ª Classe» e acaba na 8ª. O de
    // Agropecuária tem colunas para a 7ª e a 8ª, e plano temático só para
    // elas. Nenhum dos dois tem 9ª classe.
    final na9 = da9().map((x) => x.disciplina).toSet();
    final na8 = c.cursos
        .where((x) => x.classe == '8ª classe')
        .map((x) => x.disciplina)
        .toSet();
    expect(na8.difference(na9), {'TIC', 'Agropecuária'});
    expect(na9.difference(na8), isEmpty,
        reason: 'a 9ª não traz disciplinas novas');
  });

  test('todas as disciplinas da 9ª declaram a fonte, e nenhuma é provisória',
      () {
    for (final curso in da9()) {
      expect(curso.fonte, contains('INDE'), reason: curso.id);
      expect(curso.fonte, contains('não traz exercícios'), reason: curso.id);
      expect(curso.provisorio, isFalse, reason: curso.id);
    }
  });

  test('cada disciplina da 9ª tem matéria em todos os níveis', () {
    for (final curso in da9()) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          expect(n.materia, isNotNull,
              reason: '${curso.id}:${u.id}:${n.id} sem matéria');
        }
      }
    }
  });

  test('o 1º ciclo do secundário está completo: 7ª, 8ª e 9ª', () {
    int conta(String classe) =>
        c.cursos.where((x) => x.classe == classe).length;
    expect(conta('7ª classe'), 10);
    expect(conta('8ª classe'), 13);
    expect(conta('9ª classe'), 11);
  });
}
