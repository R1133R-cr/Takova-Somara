import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Educação Física da 9ª classe.
///
/// Cinco unidades, as do plano temático da 9ª. O Voleibol entra aqui; o
/// Basquetebol, que foi da 8ª, sai. E os números que o programa fixa —
/// os 12 minutos de Cooper, as três barreiras, os seis do voleibol —
/// estão certos.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso edf9() => c.cursos.firstWhere((x) => x.id == 'edf-9c');

  Iterable<Questao> perguntas() sync* {
    for (final u in edf9().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as cinco unidades da 9ª, pela ordem do plano temático', () {
    expect(
      edf9().units.map((u) => u.titulo).toList(),
      [
        'Danças e jogos educativos',
        'Ginástica',
        'Atletismo',
        'Futebol',
        'Voleibol',
      ],
    );
    expect(edf9().fonte, contains('pp. 33-40'));
    expect(edf9().provisorio, isFalse);
  });

  test('o Voleibol entra na 9ª e o Basquetebol fica na 8ª', () {
    final na8 = c.cursos
        .firstWhere((x) => x.id == 'edf-8c')
        .units
        .map((u) => u.titulo);
    expect(na8, contains('Basquetebol'));
    expect(na8, isNot(contains('Voleibol')));
    expect(edf9().units.map((u) => u.titulo), isNot(contains('Basquetebol')));
  });

  test('os números do programa estão certos', () {
    final respostas = {
      for (final q in perguntas().whereType<QInput>()) q.q: q.a,
    };
    String resposta(String pedaco) =>
        respostas.entries.firstWhere((e) => e.key.contains(pedaco)).value;
    expect(resposta('Cooper'), '12');
    expect(resposta('barreiras à altura do joelho'), '3');
    expect(resposta('quantos jogadores tem cada equipa'), '6');
    expect(resposta('toques pode dar'), '3');
  });

  test('as danças africanas têm o país certo', () {
    final pares = perguntas()
        .whereType<QMatch>()
        .expand((q) => q.pairs.map((p) => '${p.$1} → ${p.$2}'))
        .toList();
    expect(pares, contains('Marrabenta → Moçambique'));
    expect(pares, contains('Semba → Angola'));
    expect(pares, contains('Funaná → Cabo Verde'));
  });
}
