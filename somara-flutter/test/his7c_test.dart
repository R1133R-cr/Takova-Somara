import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A História da 7ª classe — a primeira História separada da app.
///
/// Da 4ª à 6ª classe a História vem dentro das **Ciências Sociais**, num
/// curso só com a Geografia, que é como o ensino primário a dá. No
/// secundário separam-se: são duas disciplinas com dois programas do INDE.
/// Quem olhar para a lista de cursos e estranhar que a 7ª não tenha
/// Ciências Sociais encontra aqui a razão.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso his7() => c.cursos.firstWhere((x) => x.id == 'his-7c');

  test('as quatro unidades estão pela ordem do programa', () {
    // Ao contrário do Português, aqui a ordem do curso é a do programa: é
    // cronológica, e a História só faz sentido pela ordem em que aconteceu.
    expect(
      his7().units.map((u) => u.titulo).toList(),
      [
        'A História como ciência',
        'A origem e a evolução do Homem',
        'A agricultura e os primeiros Estados',
        'Reinos e impérios africanos',
      ],
    );
    for (final u in his7().units) {
      expect(u.niveis, hasLength(3), reason: u.titulo);
    }
  });

  test('a fonte é o programa do INDE, e diz que não é um livro', () {
    expect(his7().fonte, contains('INDE'));
    expect(his7().fonte, contains('não traz exercícios'));
    expect(his7().provisorio, isFalse);
  });

  test('a História separa-se das Ciências Sociais no secundário', () {
    final noPrimario = c.cursos
        .where((x) => x.classe != '7ª classe')
        .map((x) => x.disciplina)
        .toSet();
    final na7 = c.cursos
        .where((x) => x.classe == '7ª classe')
        .map((x) => x.disciplina)
        .toSet();

    expect(noPrimario, contains('Ciências Sociais'),
        reason: 'no primário a História vem dentro das Ciências Sociais');
    expect(noPrimario, isNot(contains('História')));
    expect(na7, contains('História'));
    expect(na7, isNot(contains('Ciências Sociais')),
        reason: 'no secundário são duas disciplinas, não uma');
  });

  test('o programa do INDE está mesmo coberto', () {
    // Os conteúdos que o programa numera. Isto não prova que estão bem
    // ensinados — prova que nenhum ficou de fora quando as quatro unidades
    // do INDE viraram doze aulas.
    final tudo = [
      for (final u in his7().units)
        for (final n in u.niveis) ...[
          n.titulo,
          for (final q in n.questoes) ...[
            q.q,
            if (q is QChoice) ...q.options,
            if (q is QMatch)
              for (final par in q.pairs) ...[par.$1, par.$2],
          ],
        ],
    ].join(' ').toLowerCase();

    for (final assunto in const [
      'fonte', 'oral', 'arqueologia', 'antropologia', 'século', 'década',
      'milénio', 'criação', 'evolução', 'hominização', 'rift', 'fogo',
      'nómada', 'sedentári', 'agricultura', 'domesticação', 'excedente',
      'nilo', 'faraó', 'mesopotâmia', 'hamurábi', 'cuneiforme', 'pólis',
      'democracia', 'escrav', 'khoisan', 'bantu', 'ferro', 'zimbabwe',
      'mutapa', 'zambeze', 'swahili', 'ghana', 'mali', 'songhai',
      'timbuctu', 'transaariano',
    ]) {
      expect(tudo, contains(assunto),
          reason: '"$assunto" é conteúdo do programa e não aparece no curso');
    }
  });

  test('nenhum enunciado entrega a resposta', () {
    // Apanhou uma: «Uma carta ESCRITA há cem anos é uma fonte:», com
    // «Escrita» por resposta certa. A palavra estava no enunciado, e
    // respondia-se sem saber nada de História.
    //
    // PORQUE É QUE ISTO NÃO É UM TESTE GERAL. Corri a mesma regra sobre o
    // currículo inteiro: 58 acertos, e quase todos legítimos. «Qual é o
    // maior: 6, 8 ou 10?» TEM de conter o 10; «PATO começa pela sílaba…»
    // TEM de conter o PA. Onde a resposta sai de dados que o enunciado
    // apresenta, a repetição é o exercício.
    //
    // A regra só vale onde a resposta é o NOME de um conceito, que é o
    // caso desta disciplina. Alargá-la ao currículo todo dava 58 falsos
    // alarmes e acabaria desligada.
    for (final u in his7().units) {
      for (final n in u.niveis) {
        for (final q in n.questoes) {
          if (q is! QChoice) continue;
          final certa = q.options[q.a].toLowerCase();
          expect(q.q.toLowerCase().contains(certa), isFalse,
              reason: 'o enunciado "${q.q}" contém a resposta certa');
        }
      }
    }
  });
}
