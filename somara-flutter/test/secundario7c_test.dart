import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A 7ª classe inteira — o primeiro ano do secundário coberto por completo.
///
/// Os testes de cada disciplina estão nos seus ficheiros. Este guarda o que
/// só se vê olhando para a classe toda: quantas disciplinas são, quais são,
/// e — sobretudo — **quais não são e porquê**.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  List<Curso> da7() =>
      c.cursos.where((x) => x.classe == '7ª classe').toList();

  test('o plano de estudos da 7ª classe está coberto por inteiro', () {
    expect(
      da7().map((x) => x.disciplina).toSet(),
      {
        'Matemática',
        'Português',
        'Inglês',
        'História',
        'Geografia',
        'Biologia',
        'Educação Visual',
        'Educação Física',
        'Agropecuária',
        'TIC',
      },
    );
  });

  test('a Física, a Química e o Francês não estão — e não é esquecimento',
      () {
    // A página do MozEstuda lista treze programas debaixo da 7ª classe, e
    // eu próprio disse ao utilizador que faltavam nove disciplinas. Estava
    // errado: os documentos são do 1º ciclo inteiro e estão arquivados em
    // cada classe.
    //
    // Os programas de Física e de Química não mencionam a 7ª classe uma
    // única vez — as tabelas de conteúdos de ambos têm colunas para a 8ª e
    // a 9ª e mais nada. O de Francês tem planos temáticos para a 8ème e a
    // 9ème, e nenhum para a 7ª.
    //
    // As três começam na 8ª classe. Se um dia entrarem nesta, é porque o
    // currículo mudou — e então este teste é o sítio onde se dá por isso.
    final na7 = da7().map((x) => x.disciplina).toSet();
    for (final fora in const ['Física', 'Química', 'Francês']) {
      expect(na7, isNot(contains(fora)),
          reason: '$fora começa na 8ª classe, não na 7ª');
    }
    expect(da7(), hasLength(10));
  });

  test('todas as disciplinas da 7ª declaram a fonte, e nenhuma é provisória',
      () {
    // Nenhum curso desta classe saiu de um livro do aluno: não há livros
    // do aluno da 7ª publicados. Saíram todos de programas de ensino do
    // INDE, e isso tem de estar dito curso a curso.
    for (final curso in da7()) {
      expect(curso.fonte, isNotNull, reason: curso.id);
      expect(curso.fonte, contains('INDE'), reason: curso.id);
      expect(curso.fonte, contains('não traz exercícios'), reason: curso.id);
      expect(curso.provisorio, isFalse,
          reason: '${curso.id} tem fonte oficial: não é provisório');
    }
  });

  test('cada disciplina da 7ª tem matéria em todos os níveis', () {
    for (final curso in da7()) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          expect(n.materia, isNotNull,
              reason: '${curso.id}:${u.id}:${n.id} sem matéria');
        }
      }
    }
  });

  test('o Inglês não põe frases inglesas na boca de uma voz portuguesa', () {
    // A app tem uma só voz e é portuguesa. O enunciado é o que ela lê; as
    // opções são o que a criança lê. Uma frase inglesa no enunciado sairia
    // com fonética portuguesa e ensinaria a pronúncia errada.
    //
    // A regra é sobre FRASES: uma palavra solta — «o plural de book» — é
    // inevitável numa disciplina de línguas e fica perto do que devia ser.
    final ing = c.cursos.firstWhere((x) => x.id == 'ing-7c');
    final palavraInglesa = RegExp(
      r'\b(the|is|are|am|was|were|you|your|his|her|they|we|and|of|to|in|'
      r'on|do|does|not|what|how|where|who|this|that|there)\b',
      caseSensitive: false,
    );
    for (final u in ing.units) {
      for (final n in u.niveis) {
        for (final q in n.questoes) {
          final quantas = palavraInglesa.allMatches(q.q).length;
          expect(quantas, lessThan(2),
              reason: 'o enunciado "${q.q}" tem inglês a mais para a voz');
        }
      }
    }
  });

  test('e o Inglês tem mesmo inglês nas opções', () {
    // O contrário do teste anterior: se o inglês desaparecesse das opções
    // também, sobrava uma disciplina de línguas sem língua nenhuma.
    final ing = c.cursos.firstWhere((x) => x.id == 'ing-7c');
    var comIngles = 0;
    for (final u in ing.units) {
      for (final n in u.niveis) {
        for (final q in n.questoes) {
          if (q is QChoice &&
              q.options.any((o) => RegExp(r'^[A-Za-z ,?!\x27-]+$')
                  .hasMatch(o))) {
            comIngles++;
          }
        }
      }
    }
    expect(comIngles, greaterThan(30),
        reason: 'poucas perguntas com inglês nas opções');
  });

  test('as siglas da 7ª que a voz teria de soletrar estão tratadas', () {
    // «TIC» lida como palavra sairia «tique». É o nome da disciplina, e
    // diz-se «tê-i-cê». O tratamento vive no tools/pronuncia.py e é
    // testado lá; isto guarda o outro lado — que a sigla existe mesmo no
    // conteúdo e portanto a regra tem trabalho para fazer.
    final tic = c.cursos.firstWhere((x) => x.id == 'tic-7c');
    final usaASigla = [
      for (final u in tic.units)
        for (final n in u.niveis)
          for (final q in n.questoes)
            if (RegExp(r'\bTIC\b').hasMatch(q.q)) q.q,
    ];
    expect(usaASigla, isNotEmpty);
  });
}
