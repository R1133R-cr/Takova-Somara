import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Química da 8ª classe — a primeira Química da app.
///
/// Duas coisas ficam guardadas aqui. Uma é a unidade III, «Estrutura da
/// matéria e reacções químicas», que o PDF do programa perdeu (o índice
/// diz «Error! Bookmark not defined» e o plano temático salta da II para
/// a IV): está no curso porque a visão geral dos conteúdos a tem inteira.
/// A outra é a regra da voz: fórmulas como «H₂O» só nas opções, nunca no
/// enunciado.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso qui8() => c.cursos.firstWhere((x) => x.id == 'qui-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in qui8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as quatro unidades do programa, pela ordem dele', () {
    expect(
      qui8().units.map((u) => u.titulo).toList(),
      [
        'Introdução ao estudo da Química',
        'Matéria e suas propriedades',
        'Estrutura da matéria e reacções químicas',
        'Água',
      ],
    );
  });

  test('a unidade III que o PDF perdeu está cá, com os quatro temas', () {
    final u3 = qui8().units[2];
    expect(u3.niveis.length, 5);
    final titulos = u3.niveis.map((n) => n.titulo).join(' | ');
    expect(titulos, contains('átomo'));
    expect(titulos, contains('Massa atómica'));
    expect(titulos, contains('Reacções'));
    expect(titulos, contains('Cálculos'));
    expect(qui8().fonte, contains('unidade III'));
  });

  test('a Química começa na 8ª: a 7ª não a tem', () {
    expect(
      c.cursos.where((x) => x.classe == '7ª classe').map((x) => x.disciplina),
      isNot(contains('Química')),
    );
    expect(qui8().classe, '8ª classe');
    expect(qui8().provisorio, isFalse);
  });

  test('fórmulas químicas só nas opções, nunca no enunciado', () {
    // Um índice em subscrito (H₂O, CO₂) ou uma fórmula de duas letras
    // coladas a um algarismo (H2O) não se dizem. Ficam nas opções.
    final formula = RegExp(r'[A-Z][a-z]?[₀-₉0-9]');
    for (final q in perguntas()) {
      expect(formula.hasMatch(q.q), isFalse,
          reason: 'fórmula num enunciado: "${q.q}"');
    }
    final opcoes = perguntas()
        .whereType<QMatch>()
        .expand((q) => q.pairs.expand((p) => [p.$1, p.$2]))
        .join('\n');
    expect(opcoes, contains('H₂O'));
    expect(opcoes, contains('CO₂'));
  });

  test('as contas dão inteiros: massas, moles, concentrações', () {
    final numericas = perguntas()
        .whereType<QInput>()
        .where((q) => RegExp(r'^\d+$').hasMatch(q.a))
        .toList();
    expect(numericas.length, greaterThanOrEqualTo(14));
    final respostas = numericas.map((q) => q.a).toList();
    expect(respostas, contains('18')); // a água
    expect(respostas, contains('44')); // o dióxido de carbono
  });

  test('Lavoisier está no curso', () {
    final texto = perguntas().map((q) => q.q).join('\n');
    expect(texto, contains('Lavoisier'));
  });
}
