import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// As figuras das perguntas de geometria.
///
/// "Um quadrado tem 5 cm de lado. Qual é o perímetro?" sem quadrado nenhum
/// obriga a criança a imaginá-lo antes de poder pensar nele — e a de 4ª
/// classe que está a aprender o que é um perímetro não tem essa imagem na
/// cabeça para invocar.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Iterable<Questao> todas() sync* {
    for (final curso in c.cursos) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          yield* n.questoes;
        }
      }
    }
  }

  test('as perguntas que dão medidas de uma figura mostram a figura', () {
    // Se a pergunta diz "tem 5 cm de lado", ha uma figura para desenhar.
    final semFigura = <String>[];
    final padrao = RegExp(
      r'(tem \d+\s*cm de lado|cm de comprimento|cm por \d+\s*cm|'
      r'base \d+\s*cm|raio de \d+\s*cm|aresta \d+\s*cm)',
      caseSensitive: false,
    );
    for (final q in todas()) {
      if (padrao.hasMatch(q.q) && q.figura == null) semFigura.add(q.q);
    }
    expect(semFigura, isEmpty);
  });

  test('as medidas da figura batem com as do enunciado', () {
    var vistas = 0;
    for (final q in todas()) {
      final f = q.figura;
      if (f == null) continue;
      vistas++;
      // Todos os numeros da figura tem de aparecer no proprio enunciado.
      for (final valor in [f.a, if (f.b != null) f.b!]) {
        if (f.unidade.isEmpty) continue;
        expect(q.q, contains('${valor.round()}'),
            reason: '${f.forma.name} diz $valor mas "${q.q}" não o menciona');
      }
    }
    expect(vistas, greaterThanOrEqualTo(7), reason: 'poucas figuras');
  });

  test('o rectângulo guarda as duas medidas, o quadrado só uma', () {
    for (final q in todas()) {
      final f = q.figura;
      if (f == null) continue;
      if (f.forma == FormaGeo.rectangulo || f.forma == FormaGeo.triangulo) {
        expect(f.b, isNotNull,
            reason: '${f.forma.name} precisa das duas medidas');
      }
      if (f.forma == FormaGeo.quadrado || f.forma == FormaGeo.circulo) {
        expect(f.b, isNull, reason: '${f.forma.name} só tem uma medida');
      }
      expect(f.a, greaterThan(0));
    }
  });

  test('nenhuma pergunta fala de "esta figura" sem trazer uma', () {
    // Era o caso da 3ª classe: mostrava quatro réguas e perguntava quantos
    // lados tem a figura. Sem figura, a pergunta não tinha resposta.
    for (final q in todas()) {
      if (q.q.toLowerCase().contains('esta figura')) {
        expect(q.figura, isNotNull, reason: q.q);
      }
    }
  });

  test('a medida escrita traz a unidade, ou nada quando não há', () {
    const comUnidade = Figura(forma: FormaGeo.quadrado, a: 5);
    expect(comUnidade.medidaDe(5), '5 cm');
    const semUnidade = Figura(forma: FormaGeo.quadrado, a: 4, unidade: '');
    expect(semUnidade.medidaDe(4), isEmpty);
  });
}
