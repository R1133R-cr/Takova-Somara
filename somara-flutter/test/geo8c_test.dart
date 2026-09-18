import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Geografia da 8ª classe — a Geografia Humana ou Económica.
///
/// A 7ª foi a Geografia física; esta é a das pessoas: população,
/// actividades económicas, cidades. O programa do INDE dá-lhe quatro
/// unidades muito desiguais, e é isso que aqui se guarda — que o curso as
/// segue como são, com a terceira a valer quase metade.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso geo8() => c.cursos.firstWhere((x) => x.id == 'geo-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in geo8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as quatro unidades do programa, pela ordem dele', () {
    expect(
      geo8().units.map((u) => u.titulo).toList(),
      [
        'A Geografia Humana',
        'População',
        'Actividades económicas',
        'Cidades',
      ],
    );
  });

  test('a terceira unidade é a maior — como no programa', () {
    // As actividades económicas ocupam dois trimestres e meio no INDE:
    // agricultura, pecuária, indústria, comércio, turismo, transportes.
    // Um curso que lhes desse o mesmo peso que às outras estaria a
    // desenhar um programa que não existe.
    final niveis = geo8().units.map((u) => u.niveis.length).toList();
    expect(niveis[2], greaterThanOrEqualTo(niveis[0] + niveis[1]));
    expect(niveis[2], greaterThan(niveis[3]));
  });

  test('a fonte diz o programa e as páginas', () {
    expect(geo8().fonte, contains('INDE'));
    expect(geo8().fonte, contains('pp. 23-35'));
    expect(geo8().fonte, contains('não traz exercícios'));
    expect(geo8().provisorio, isFalse);
  });

  test('os sectores e as actividades estão todos', () {
    final texto = perguntas().map((q) => q.q).join('\n').toLowerCase();
    for (final tema in const [
      'natalidade',
      'migração',
      'pirâmide etária',
      'agricultura',
      'pecuária',
      'indústria',
      'comércio',
      'turismo',
      'transporte',
      'urbanização',
      'planeamento urbano',
    ]) {
      expect(texto, contains(tema), reason: 'falta "$tema"');
    }
  });

  test('há contas de geografia, e são de resposta numérica', () {
    // Crescimento natural, saldo da balança comercial, taxa de
    // urbanização: a Geografia Humana também se conta.
    final numericas = perguntas()
        .whereType<QInput>()
        .where((q) => RegExp(r'^\d+$').hasMatch(q.a));
    expect(numericas.length, greaterThanOrEqualTo(3));
  });

  test('fala de Moçambique, e não só do mundo', () {
    final texto = [
      for (final q in perguntas()) ...[
        q.q,
        if (q is QChoice) ...q.options,
        if (q is QMatch) ...q.pairs.expand((p) => [p.$1, p.$2]),
      ],
    ].join('\n');
    expect(texto, contains('Maputo'));
    expect(texto, contains('Niassa'));
  });
}
