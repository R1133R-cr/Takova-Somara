import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A História da 9ª classe — o século XX, e Moçambique nele.
///
/// Quatro unidades do programa do INDE, das contradições imperialistas
/// à paz de Roma. O que este teste guarda são as datas que nenhum
/// moçambicano deve trocar — Mueda, a FRELIMO, Chai, Lusaka, a
/// Independência, Roma — e que a voz diz «século dezanove» e não «xis».
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso his9() => c.cursos.firstWhere((x) => x.id == 'his-9c');

  Iterable<Questao> perguntas() sync* {
    for (final u in his9().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as quatro unidades do programa, pela ordem dele', () {
    expect(
      his9().units.map((u) => u.titulo).toList(),
      [
        'As contradições imperialistas e a I Guerra Mundial',
        'O mundo entre as duas guerras e a II Guerra Mundial',
        'A luta de libertação e a Independência de Moçambique',
        'Da Guerra Fria à paz em Moçambique',
      ],
    );
    expect(his9().fonte, contains('pp. 35-45'));
    expect(his9().provisorio, isFalse);
  });

  test('as datas de Moçambique estão certas', () {
    final datas = {
      for (final q in perguntas().whereType<QInput>()) q.q: q.a,
    };
    String resposta(String pedaco) => datas.entries
        .firstWhere((e) => e.key.contains(pedaco),
            orElse: () => throw StateError('não há pergunta com "$pedaco"'))
        .value;
    expect(resposta('Mueda'), '1960');
    expect(resposta('FRELIMO foi fundada'), '1962');
    expect(resposta('Chai'), '1964');
    expect(resposta('Lusaka'), '1974');
    expect(resposta('Independência Nacional'), '1975');
    expect(resposta('Roma'), '1992');
    expect(resposta('multipartidárias'), '1994');
  });

  test('as datas do mundo estão certas', () {
    final datas = {
      for (final q in perguntas().whereType<QInput>()) q.q: q.a,
    };
    String resposta(String pedaco) =>
        datas.entries.firstWhere((e) => e.key.contains(pedaco)).value;
    expect(resposta('Sarajevo'), '1914');
    expect(resposta('armistício'), '1918');
    expect(resposta('bolsa de Nova Iorque'), '1929');
    expect(resposta('Polónia'), '1939');
    expect(resposta('rendição'), '1945');
    expect(resposta('muro de Berlim'), '1989');
  });

  test('as figuras da luta de libertação estão as quatro', () {
    final figuras = perguntas()
        .whereType<QMatch>()
        .firstWhere((q) => q.q.contains('figura da luta'))
        .pairs
        .map((p) => p.$1)
        .toList();
    expect(figuras, [
      'Eduardo Mondlane',
      'Samora Machel',
      'Josina Machel',
      'Filipe Samuel Magaia',
    ]);
  });

  test('o século escreve-se em numeração romana no ecrã', () {
    // «século XIX» fica assim no ecrã; a voz diz «século dezanove» por
    // regra do pronuncia.py, e é essa regra que o test_pronuncia guarda.
    expect(perguntas().map((q) => q.q).join('\n'), contains('século XIX'));
  });
}
