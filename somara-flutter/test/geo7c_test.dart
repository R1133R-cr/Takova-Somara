import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Geografia da 7ª classe — a outra metade das Ciências Sociais.
///
/// Da 4ª à 6ª classe a Geografia e a História vêm juntas num curso só, que
/// é como o primário as dá. No secundário separam-se. A História entrou na
/// 0.39.0; esta fecha o par, e a partir daqui a 7ª classe tem as duas.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso geo7() => c.cursos.firstWhere((x) => x.id == 'geo-7c');

  test('as cinco unidades, e a razão de não serem quatro', () {
    // O INDE tem quatro. A Unidade IV atravessa dois trimestres e cobre as
    // quatro esferas — e é o próprio programa que as numera à parte
    // (4.2 Atmosfera, 4.3 Hidrosfera, 4.4 Litosfera, 4.5 Biosfera). O
    // curso corta-a onde ela já está cortada; uma unidade com sete níveis
    // ao lado de outra com dois não é ordem nenhuma.
    expect(
      geo7().units.map((u) => u.titulo).toList(),
      [
        'Introdução ao estudo da Geografia',
        'A representação da Terra',
        'A Terra no Universo',
        'A atmosfera e o clima',
        'Hidrosfera, litosfera e biosfera',
      ],
    );
    expect(geo7().fonte, contains('Unidade IV'),
        reason: 'a divisão da Unidade IV tem de estar dita nos dados');
  });

  test('a fonte é o programa do INDE, e diz que não é um livro', () {
    expect(geo7().fonte, contains('INDE'));
    expect(geo7().fonte, contains('não traz exercícios'));
    expect(geo7().provisorio, isFalse);
  });

  test('a 7ª classe tem as duas metades das Ciências Sociais', () {
    final na7 = c.cursos
        .where((x) => x.classe == '7ª classe')
        .map((x) => x.disciplina)
        .toSet();
    expect(na7, containsAll({'História', 'Geografia'}));
    expect(na7, isNot(contains('Ciências Sociais')),
        reason: 'no secundário são duas disciplinas, não uma');

    // E no primário continuam juntas, que é como lá se dão.
    final noPrimario = c.cursos
        .where((x) => x.classe != '7ª classe')
        .map((x) => x.disciplina)
        .toSet();
    expect(noPrimario, contains('Ciências Sociais'));
    expect(noPrimario, isNot(contains('Geografia')));
  });

  test('o programa do INDE está mesmo coberto', () {
    final tudo = [
      for (final u in geo7().units)
        for (final n in u.niveis) ...[
          n.titulo,
          for (final q in n.questoes) ...[
            q.q,
            if (q is QChoice) ...q.options,
            if (q is QMatch)
              for (final par in q.pairs) ...[par.$1, par.$2],
          ],
        ],
    ].join(' ').toLowerCase();

    for (final assunto in const [
      'geografia física', 'geografia humana', 'cartografia',
      'paralelos', 'meridianos', 'latitude', 'longitude', 'equador',
      'capricórnio', 'globo', 'legenda', 'escala', 'planta', 'paisagem',
      'big bang', 'galáxia', 'sistema solar', 'satélite',
      'rotação', 'translação', 'atmosfera', 'troposfera', 'ozono',
      'clima', 'pluviómetro', 'altitude', 'intertropical',
      'hidrosfera', 'marés', 'índico', 'nascente', 'foz', 'afluente',
      'evaporação', 'condensação', 'litosfera', 'crusta', 'manto',
      'núcleo', 'magmáticas', 'sedimentares', 'metamórfica', 'solo',
      'erosão', 'biosfera',
    ]) {
      expect(tudo, contains(assunto),
          reason: '"$assunto" é conteúdo do programa e não aparece no curso');
    }
  });

  test('nenhuma pergunta manda ler um mapa que a app não desenha', () {
    // O programa manda usar o Atlas. A app não tem contornos de Moçambique
    // nem do mundo, e desenhá-los de memória seria inventar geografia. As
    // perguntas foram escritas para se responderem sem mapa à frente — e
    // este teste impede que entre uma que dependa de um.
    final padrao = RegExp(
      r'\b(no mapa (?:acima|ao lado|seguinte)|observa o mapa|'
      r'na figura|neste mapa|no atlas)\b',
      caseSensitive: false,
    );
    for (final u in geo7().units) {
      for (final n in u.niveis) {
        for (final q in n.questoes) {
          expect(padrao.hasMatch(q.q), isFalse,
              reason: '"${q.q}" pede um mapa que não existe');
        }
      }
    }
  });
}
