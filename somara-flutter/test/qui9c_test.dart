import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Química da 9ª classe.
///
/// Sete unidades do programa do INDE, pela ordem dele: as classes de
/// compostos, o átomo e a tabela, as ligações, e os quatro grupos
/// principais — halogéneos, enxofre, azoto, carbono. A regra da voz é a
/// da 8ª e o teste guarda-a: fórmulas só nas opções e nos pares.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso qui9() => c.cursos.firstWhere((x) => x.id == 'qui-9c');

  Iterable<Questao> perguntas() sync* {
    for (final u in qui9().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as sete unidades do programa, pela ordem dele', () {
    expect(
      qui9().units.map((u) => u.titulo).toList(),
      [
        'Classes dos compostos inorgânicos',
        'Estrutura atómica e Tabela Periódica',
        'Ligação química',
        'O cloro e os halogéneos',
        'O enxofre e a velocidade das reacções',
        'O nitrogénio, os adubos e o equilíbrio',
        'O carbono e o silício',
      ],
    );
    expect(qui9().fonte, contains('pp. 29-51'));
    expect(qui9().provisorio, isFalse);
  });

  test('fórmulas químicas só nas opções e nos pares', () {
    final formula = RegExp(r'[A-Z][a-z]?[₀-₉0-9]');
    for (final q in perguntas()) {
      expect(formula.hasMatch(q.q), isFalse,
          reason: 'fórmula num enunciado: "${q.q}"');
    }
    final pares = perguntas()
        .whereType<QMatch>()
        .expand((q) => q.pairs.map((p) => p.$2))
        .toList();
    expect(pares, containsAll(['H₂SO₄', 'NH₃', 'NaOH', 'SO₂']));
  });

  test('os cientistas e os processos do programa estão lá', () {
    final texto = perguntas()
        .map((q) => switch (q) {
              QMatch() => '${q.q} ${q.pairs.expand((p) => [p.$1, p.$2]).join(' ')}',
              QChoice() => '${q.q} ${q.options.join(' ')}',
              _ => q.q,
            })
        .join('\n');
    for (final nome in const [
      'Arrhenius',
      'Mendeleev',
      'Avogadro',
      'Le Chatelier',
      'Haber-Bosch',
      'Ostwald',
    ]) {
      expect(texto, contains(nome), reason: 'falta "$nome"');
    }
  });

  test('as contas dão inteiros', () {
    final respostas = {
      for (final q in perguntas().whereType<QInput>()) q.q: q.a,
    };
    String resposta(String pedaco) =>
        respostas.entries.firstWhere((e) => e.key.contains(pedaco)).value;
    expect(resposta('número de massa 23'), '12');
    expect(resposta('44,8 litros'), '2');
    expect(resposta('azoto'), '78');
  });
}
