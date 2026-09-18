import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Física da 8ª classe — a primeira Física da app.
///
/// O programa do INDE não menciona a 7ª uma única vez: a Física começa
/// aqui. O que este teste guarda, além da forma do curso, é uma decisão de
/// voz: as unidades escrevem-se por extenso nos enunciados, porque «m/s»
/// e «J» não se dizem, e os símbolos ficam nas opções, que se lêem.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso fis8() => c.cursos.firstWhere((x) => x.id == 'fis-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in fis8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as seis unidades do programa, pela ordem dele', () {
    expect(
      fis8().units.map((u) => u.titulo).toList(),
      [
        'Introdução ao estudo da Física',
        'Cinemática',
        'Dinâmica: as leis de Newton',
        'Trabalho e energia',
        'Fenómenos térmicos',
        'Óptica geométrica',
      ],
    );
  });

  test('a Física começa na 8ª: a 7ª não a tem', () {
    expect(
      c.cursos.where((x) => x.classe == '7ª classe').map((x) => x.disciplina),
      isNot(contains('Física')),
    );
    expect(fis8().classe, '8ª classe');
  });

  test('a fonte diz o programa e as páginas', () {
    expect(fis8().fonte, contains('INDE'));
    expect(fis8().fonte, contains('pp. 19-31'));
    expect(fis8().provisorio, isFalse);
  });

  test('nos enunciados, as unidades vêm por extenso', () {
    // "5 m/s" sai "cinco eme, esse" e "20 J" sai "vinte jota". Os símbolos
    // podem ficar nas opções; no que a voz lê, escreve-se a palavra.
    final proibidos = RegExp(r'\d\s*(m/s|km/h|J\b|W\b|N\b|°C)');
    for (final q in perguntas()) {
      expect(proibidos.hasMatch(q.q), isFalse,
          reason: 'símbolo de unidade num enunciado: "${q.q}"');
    }
    final texto = perguntas().map((q) => q.q).join('\n');
    for (final palavra in const [
      'metros por segundo',
      'newtons',
      'joules',
      'watts',
      'graus Celsius',
    ]) {
      expect(texto, contains(palavra), reason: 'falta "$palavra"');
    }
  });

  test('há contas de Física, e dão números inteiros', () {
    // Velocidade, força, trabalho, potência, kelvin: a Física da 8ª
    // conta-se, e as contas foram escolhidas para dar certo sem vírgula.
    final numericas = perguntas()
        .whereType<QInput>()
        .where((q) => RegExp(r'^\d+$').hasMatch(q.a))
        .toList();
    expect(numericas.length, greaterThanOrEqualTo(10));
  });

  test('as três leis de Newton estão as três', () {
    final texto = perguntas().map((q) => q.q).join('\n').toLowerCase();
    expect(texto, contains('primeira lei de newton'));
    expect(texto, contains('segunda lei de newton'));
    expect(texto, contains('terceira lei de newton'));
  });
}
