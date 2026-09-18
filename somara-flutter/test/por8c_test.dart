import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// O Português da 8ª classe.
///
/// Como na 7ª, o programa do INDE organiza a classe em quinze unidades — os
/// mesmos cinco tipos de texto três vezes, uma por trimestre — e o curso
/// corta-as por tipo de texto, em cinco. Este teste guarda esse corte, a
/// fonte, e o facto de a 8ª ficar, com este curso, com as duas disciplinas
/// de exame.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso por8() => c.cursos.firstWhere((x) => x.id == 'por-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in por8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('cinco unidades, uma por tipo de texto, na ordem do programa', () {
    expect(
      por8().units.map((u) => u.titulo).toList(),
      [
        'Textos normativos',
        'Textos administrativos',
        'Textos jornalísticos',
        'Textos multiuso',
        'Textos literários',
      ],
    );
    for (final u in por8().units) {
      expect(u.niveis, hasLength(3), reason: u.titulo);
    }
  });

  test('a fonte diz o programa, as páginas e o corte por tipo de texto', () {
    expect(por8().fonte, contains('INDE'));
    expect(por8().fonte, contains('pp. 34-53'));
    expect(por8().fonte, contains('por tipo de texto'));
    expect(por8().fonte, contains('não traz exercícios'));
    expect(por8().provisorio, isFalse);
  });

  test('a 8ª classe tem as duas disciplinas de exame', () {
    final da8 = c.cursos.where((x) => x.classe == '8ª classe');
    expect(
      da8.map((x) => x.disciplina).toSet(),
      containsAll(['Matemática', 'Português']),
    );
  });

  test('os textos do programa estão todos: do regulamento ao drama', () {
    // Os quinze blocos do INDE reduzem-se a cinco tipos de texto, e cada
    // tipo tem um texto específico que dá o nome à coisa. Se algum destes
    // deixar de aparecer num enunciado, perdeu-se um bloco do programa.
    final texto = perguntas().map((q) => q.q).join('\n').toLowerCase();
    for (final especifico in const [
      'regulamento',
      'convocatória',
      'acta',
      'notícia',
      'anúncio classificado',
      'texto expositivo',
      'relato',
      'lenda',
      'mito',
      'poema',
      'dramático',
    ]) {
      expect(texto, contains(especifico), reason: 'falta "$especifico"');
    }
  });

  test('as respostas escritas são palavras, não números', () {
    // O Português pede formas verbais e adjectivos por extenso: "devem",
    // "finais", "estivemos". A app abre o teclado de letras para elas, e
    // é assim que deve ser — um Português sem escrever não é Português.
    final escritas = perguntas().whereType<QInput>().toList();
    expect(escritas.length, greaterThanOrEqualTo(5));
    for (final q in escritas) {
      expect(RegExp(r'^[a-zçãõáéíóúâêô]+$').hasMatch(q.a), isTrue,
          reason: '"${q.a}" devia ser uma palavra só, em minúsculas');
    }
  });

  test('dentro do curso, nenhum enunciado se repete', () {
    final vistos = <String>{};
    for (final q in perguntas()) {
      expect(vistos.add(q.q), isTrue, reason: 'repetido: ${q.q}');
    }
  });
}
