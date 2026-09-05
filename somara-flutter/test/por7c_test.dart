import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// O Português da 7ª classe.
///
/// O que aqui se guarda é a decisão que este curso tomou e que nenhum
/// outro tinha tomado: o programa do INDE organiza a 7ª classe em QUINZE
/// unidades temáticas — cinco tipos de texto a repetirem-se nos três
/// trimestres — e o curso junta-as em CINCO, por tipo de texto.
///
/// Não é uma simplificação: é o mesmo conteúdo cortado pelo outro eixo. A
/// razão está escrita no cabeçalho do `tools/conteudo_por7c.py`. Se um dia
/// alguém achar que o curso está incompleto por ter cinco unidades onde o
/// programa tem quinze, é este teste que explica porquê.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso por7() => c.cursos.firstWhere((x) => x.id == 'por-7c');

  test('as cinco unidades são os cinco tipos de texto do programa', () {
    expect(
      por7().units.map((u) => u.titulo).toList(),
      [
        'Textos normativos',
        'Textos administrativos',
        'Textos jornalísticos',
        'Textos multiuso',
        'Textos literários',
      ],
    );
  });

  test('cada tipo de texto tem os três níveis dos três trimestres', () {
    // Uma unidade do curso junta as três unidades do programa que tratam
    // do mesmo tipo de texto — uma por trimestre. Se uma ficar com dois
    // níveis, perdeu-se um trimestre pelo caminho.
    for (final u in por7().units) {
      expect(u.niveis, hasLength(3), reason: u.titulo);
    }
  });

  test('a fonte diz que é um programa, e diz que foi reagrupado', () {
    final f = por7().fonte;
    expect(f, contains('INDE'));
    expect(f, contains('quinze unidades'),
        reason: 'quem lê tem de saber que o programa tem quinze e o curso '
            'tem cinco');
    expect(f, contains('não traz exercícios'));
    expect(por7().provisorio, isFalse);
  });

  test('a gramática do programa está mesmo lá', () {
    // O "Funcionamento da Língua" é a espinha do programa: é o que se
    // avalia num exame e o que a app consegue mesmo exercitar. Isto não
    // prova que está bem ensinado — prova que não ficou de fora.
    // As opções contam tanto como o enunciado. Metade da gramática desta
    // disciplina está do lado da resposta — «formou-se por: Prefixação» —
    // e uma varredura que só olhasse para a pergunta dava a matéria por
    // ausente quando ela está mesmo à frente da criança.
    final tudo = [
      for (final u in por7().units)
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
      'sujeito',
      'preposição',
      'prefixação',
      'advérbio',
      'tratamento',
      'indicativo',
      'particípio',
      'passiva',
      'irregulares',
      'circunstancial',
      'conjunção',
      'acentuada',
      'pronome',
      'imperativo',
      'conjuntivo',
      'grau',
      'homónimas',
      'parónimas',
      'composição',
      'discurso',
    ]) {
      expect(tudo, contains(assunto),
          reason: '"$assunto" é conteúdo do programa e não aparece no curso');
    }
  });

  test('a 7ª classe tem as duas disciplinas de exame', () {
    final da7 = c.cursos.where((x) => x.classe == '7ª classe');
    expect(da7.map((x) => x.disciplina).toSet(),
        containsAll({'Matemática', 'Português'}));
  });
}
