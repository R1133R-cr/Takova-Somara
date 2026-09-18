import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// As TIC da 8ª classe — as últimas do 1º ciclo.
///
/// O programa do INDE é «de 7ª e 8ª Classe»: diz-o no título, e a 9ª não
/// tem TIC. Três unidades pela ordem dele. E uma decisão de voz: «OSI» e
/// «ATM» a voz leria como palavras, por isso ficam nas opções; nos
/// enunciados escreve-se «o modelo de sete camadas» e «a caixa
/// automática».
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso tic8() => c.cursos.firstWhere((x) => x.id == 'tic-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in tic8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as três unidades do programa, pela ordem dele', () {
    expect(
      tic8().units.map((u) => u.titulo).toList(),
      [
        'Componentes básicos de sistemas computacionais',
        'Comunicação, cidadania digital e cibersegurança',
        'Transacções electrónicas e aplicações das TIC',
      ],
    );
  });

  test('a fonte diz o programa de 7ª e 8ª e as páginas', () {
    expect(tic8().fonte, contains('7ª e 8ª'));
    expect(tic8().fonte, contains('pp. 26-33'));
    expect(tic8().provisorio, isFalse);
  });

  test('«OSI» e «ATM» só nas opções, nunca no enunciado', () {
    for (final q in perguntas()) {
      expect(q.q, isNot(matches(RegExp(r'\b(OSI|ATM)\b'))),
          reason: 'sigla que a voz não sabe dizer: "${q.q}"');
    }
    final opcoes = perguntas().whereType<QChoice>().expand((q) => q.options);
    expect(opcoes, contains('Modelo OSI'));
  });

  test('a única sigla dos enunciados é TIC, que se soletra', () {
    final siglas = <String>{};
    for (final q in perguntas()) {
      siglas.addAll(RegExp(r'\b[A-Z]{2,}\b').allMatches(q.q).map((m) => m[0]!));
    }
    expect(siglas, {'TIC'});
  });

  test('a lei das transacções electrónicas escreve-se por extenso', () {
    // «Lei n.º 3/2017» a voz lia como uma fracção. Escreve-se «Lei número
    // 3 de 2017».
    final texto = perguntas().map((q) => q.q).join('\n');
    expect(texto, contains('Lei número 3 de 2017'));
    expect(texto, isNot(contains('3/2017')));
  });

  test('o custo dos dados em Lichinga está dito', () {
    final opcoes = perguntas().whereType<QChoice>().expand((q) => q.options);
    expect(opcoes, contains('Precisa de Internet, e os dados pagam-se'));
  });
}
