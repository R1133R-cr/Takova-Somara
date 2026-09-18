import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// O Português da 9ª classe.
///
/// O programa do INDE tem quinze unidades: em cada trimestre os mesmos
/// cinco tipos de texto, pela mesma ordem, com um texto específico de
/// cada vez. Como na 8ª, o curso agrupa-as pelo tipo de texto. O que este
/// teste guarda é isso, e os textos específicos que o programa manda ler.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso por9() => c.cursos.firstWhere((x) => x.id == 'por-9c');

  Iterable<Questao> perguntas() sync* {
    for (final u in por9().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  String tudo() => perguntas()
      .map((q) => switch (q) {
            QChoice() => '${q.q} ${q.options.join(' ')}',
            QMatch() => '${q.q} ${q.pairs.expand((p) => [p.$1, p.$2]).join(' ')}',
            _ => q.q,
          })
      .join('\n');

  test('os cinco tipos de texto, pela ordem do programa', () {
    expect(
      por9().units.map((u) => u.titulo).toList(),
      [
        'Textos normativos',
        'Textos administrativos',
        'Textos jornalísticos',
        'Textos multiuso',
        'Textos literários',
      ],
    );
    expect(por9().fonte, contains('quinze unidades'));
    expect(por9().fonte, contains('pp. 55-74'));
    expect(por9().provisorio, isFalse);
  });

  test('os textos específicos da 9ª estão lá', () {
    final texto = tudo();
    for (final especifico in const [
      'Direitos Humanos',
      'Direitos da Criança',
      'carta de apresentação',
      'Curriculum Vitae',
      'requerimento',
      'entrevista',
      'publicitário',
      'guia turístico',
      'relato de viagem',
      'romance',
      'poema',
      'dramático',
    ]) {
      expect(texto.toLowerCase(), contains(especifico.toLowerCase()),
          reason: 'falta "$especifico"');
    }
  });

  test('os autores que o programa manda ler estão lá', () {
    final texto = tudo();
    for (final autor in const [
      'Aldino Muianga',
      'Germano Almeida',
      'Noémia de Sousa',
      'Luís Vaz de Camões',
    ]) {
      expect(texto, contains(autor), reason: 'falta "$autor"');
    }
  });

  test('a gramática da 9ª: fazer, dar e poder; atributo e aposto', () {
    final texto = tudo();
    expect(texto, contains('fizemos'));
    expect(texto, contains('darão'));
    expect(texto, contains('puderes'));
    expect(texto, contains('Aposto'));
    expect(texto, contains('Atributo'));
  });

  test('vem a seguir à Matemática da 9ª', () {
    final ids = c.cursos.map((x) => x.id).toList();
    expect(ids.indexOf('por-9c'), ids.indexOf('mat-9c') + 1);
  });
}
