import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A 8ª classe inteira — o segundo ano do secundário coberto por completo.
///
/// Os testes de cada disciplina estão nos seus ficheiros. Este guarda o que
/// só se vê olhando para a classe toda: quantas disciplinas são, quais são,
/// e quais entram aqui pela primeira vez.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  List<Curso> da8() =>
      c.cursos.where((x) => x.classe == '8ª classe').toList();

  test('o plano de estudos da 8ª classe está coberto por inteiro', () {
    expect(
      da8().map((x) => x.disciplina).toSet(),
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
        'Agropecuária',
        'TIC',
      },
    );
    expect(da8(), hasLength(13));
  });

  test('a Física, a Química e o Francês entram aqui, e a 7ª não os tem', () {
    // As dez da 7ª mais três: os programas de Física e de Química só têm
    // colunas para a 8ª e a 9ª, e o de Francês só tem planos para a 8ème e
    // a 9ème. É na 8ª que começam.
    final na7 = c.cursos
        .where((x) => x.classe == '7ª classe')
        .map((x) => x.disciplina)
        .toSet();
    final na8 = da8().map((x) => x.disciplina).toSet();
    expect(na8.difference(na7), {'Física', 'Química', 'Francês'});
    expect(na7.difference(na8), isEmpty,
        reason: 'nenhuma disciplina da 7ª desaparece na 8ª');
  });

  test('todas as disciplinas da 8ª declaram a fonte, e nenhuma é provisória',
      () {
    // Nenhum curso desta classe saiu de um livro do aluno: não há livros
    // do aluno da 8ª publicados. Saíram todos de programas de ensino do
    // INDE, e isso tem de estar dito curso a curso.
    for (final curso in da8()) {
      expect(curso.fonte, isNotNull, reason: curso.id);
      expect(curso.fonte, contains('INDE'), reason: curso.id);
      expect(curso.fonte, contains('não traz exercícios'), reason: curso.id);
      expect(curso.provisorio, isFalse,
          reason: '${curso.id} tem fonte oficial: não é provisório');
    }
  });

  test('cada disciplina da 8ª tem matéria em todos os níveis', () {
    for (final curso in da8()) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          expect(n.materia, isNotNull,
              reason: '${curso.id}:${u.id}:${n.id} sem matéria');
        }
      }
    }
  });

  test('as línguas estrangeiras falam português no enunciado', () {
    // O Inglês e o Francês têm a mesma regra: a voz é portuguesa, o
    // enunciado é português, e a língua aprendida fica nas opções.
    for (final id in const ['ing-8c', 'fra-8c']) {
      final curso = c.cursos.firstWhere((x) => x.id == id);
      expect(curso.fonte, contains('a voz da app é portuguesa'),
          reason: id);
    }
  });
}
