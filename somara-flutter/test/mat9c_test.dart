import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Matemática da 9ª classe — o primeiro curso da 9ª, que fecha o 1º
/// ciclo do secundário.
///
/// Oito unidades pela ordem do programa do INDE. O que este teste guarda,
/// além da forma, é o que a 9ª trouxe de novo à voz: a raiz cúbica «∛»,
/// que se diz «raiz cúbica de», e a regra de que as potências de expoente
/// fraccionário se escrevem por palavras no enunciado.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso mat9() => c.cursos.firstWhere((x) => x.id == 'mat-9c');

  Iterable<Questao> perguntas() sync* {
    for (final u in mat9().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as oito unidades do programa, pela ordem dele', () {
    expect(
      mat9().units.map((u) => u.titulo).toList(),
      [
        'Números e operações (1)',
        'Álgebra (1)',
        'Geometria (1)',
        'Álgebra (2)',
        'Funções',
        'Álgebra (3)',
        'Organização e tratamento de dados',
        'Geometria (2)',
      ],
    );
  });

  test('é o primeiro curso da 9ª, e vem logo a seguir aos da 8ª', () {
    expect(mat9().classe, '9ª classe');
    final ids = c.cursos.map((x) => x.id).toList();
    final ultimo8 = ids.lastIndexWhere((id) => id.endsWith('-8c'));
    expect(ids.indexOf('mat-9c'), ultimo8 + 1);
  });

  test('a fonte diz o programa e as páginas', () {
    expect(mat9().fonte, contains('INDE'));
    expect(mat9().fonte, contains('pp. 82-110'));
    expect(mat9().provisorio, isFalse);
  });

  test('a raiz cúbica está nos enunciados, e o expoente fraccionário não', () {
    final texto = perguntas().map((q) => q.q).join('\n');
    expect(texto, contains('∛27'));
    expect(texto, contains('elevado a um terço'));
    // "8^(1/3)" a voz lia "8 acento um terço". Não entra.
    expect(texto, isNot(contains('^')));
  });

  test('a maior Matemática da app: mais perguntas que a da 8ª', () {
    final mat8 = c.cursos.firstWhere((x) => x.id == 'mat-8c');
    int conta(Curso curso) => curso.units
        .expand((u) => u.niveis)
        .fold(0, (n, nivel) => n + nivel.questoes.length);
    expect(conta(mat9()), greaterThan(conta(mat8)));
  });

  test('as respostas numéricas dão inteiros, e o π toma-se igual a 3', () {
    for (final q in perguntas().whereType<QInput>()) {
      expect(RegExp(r'^-?\d+$').hasMatch(q.a), isTrue,
          reason: 'resposta não inteira: "${q.q}" → ${q.a}');
      if (q.q.contains('π')) {
        expect(q.q, contains('Tomando π igual a 3'), reason: q.q);
      }
    }
  });

  test('Pitágoras, Thales e Euler estão os três', () {
    final texto = perguntas().map((q) => q.q).join('\n');
    expect(texto, contains('Thales'));
    expect(texto, contains('hipotenusa'));
    expect(texto, contains('Euler'));
  });
}
