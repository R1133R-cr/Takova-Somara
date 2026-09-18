import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Educação Visual da 8ª classe.
///
/// Sete unidades do programa do INDE, pela ordem dele. O que este teste
/// guarda, além da forma, é o critério da 7ª: uma app de perguntas não
/// desenha, por isso pergunta-se o saber que o desenho precisa — que arco
/// é qual, que vista se vê de cima, que cor sai da mistura.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso ev8() => c.cursos.firstWhere((x) => x.id == 'ev-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in ev8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as sete unidades do programa, pela ordem dele', () {
    expect(
      ev8().units.map((u) => u.titulo).toList(),
      [
        'Arte universal',
        'Comunicação visual',
        'Estudo da forma',
        'Desenho geométrico',
        'Projecções ortogonais',
        'Formas em axonometria',
        'Cotagem das formas',
      ],
    );
  });

  test('a fonte diz o programa e as páginas', () {
    expect(ev8().fonte, contains('INDE'));
    expect(ev8().fonte, contains('pp. 23-32'));
    expect(ev8().provisorio, isFalse);
  });

  test('os três artistas do programa estão os três', () {
    final texto = perguntas()
        .map((q) => q is QChoice ? '${q.q} ${q.options.join(' ')}' : q.q)
        .join('\n');
    expect(texto, contains('Leonardo da Vinci'));
    expect(texto, contains('Miguel Ângelo'));
    expect(texto, contains('Pablo Picasso'));
  });

  test('a teoria da cor: as três secundárias saem das primárias', () {
    final pares = perguntas()
        .whereType<QMatch>()
        .expand((q) => q.pairs.map((p) => p.$2))
        .toList();
    expect(pares, containsAll(['Verde', 'Laranja', 'Roxo']));
  });

  test('há contas de desenho, e dão inteiros', () {
    // A malha, o raio do arco, os graus da isometria, a cota: o desenho
    // geométrico também se conta.
    final numericas = perguntas()
        .whereType<QInput>()
        .where((q) => RegExp(r'^\d+$').hasMatch(q.a))
        .toList();
    expect(numericas.length, greaterThanOrEqualTo(5));
    expect(numericas.map((q) => q.a), contains('120'));
  });
}
