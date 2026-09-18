import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Biologia da 8ª classe.
///
/// Seis unidades do INDE, da célula ao auto-descobrimento. O que aqui se
/// guarda é o que só se vê olhando para o curso todo: a ordem das
/// unidades, a fonte, e que a saúde — a alimentação, as parasitoses, as
/// infecções de transmissão sexual — está lá com a prevenção escrita, e
/// não só com o nome da doença.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso bio8() => c.cursos.firstWhere((x) => x.id == 'bio-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in bio8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  String tudo() => [
        for (final q in perguntas()) ...[
          q.q,
          if (q is QChoice) ...q.options,
          if (q is QMatch) ...q.pairs.expand((p) => [p.$1, p.$2]),
        ],
      ].join('\n').toLowerCase();

  test('as seis unidades do programa, pela ordem dele', () {
    expect(
      bio8().units.map((u) => u.titulo).toList(),
      [
        'Seres vivos e ambiente',
        'Recursos naturais',
        'Sistemas do corpo humano',
        'Alimentação, nutrição e saúde',
        'Reprodução nos seres vivos',
        'Auto-descobrimento',
      ],
    );
  });

  test('a fonte diz o programa e as páginas', () {
    expect(bio8().fonte, contains('INDE'));
    expect(bio8().fonte, contains('pp. 30-43'));
    expect(bio8().provisorio, isFalse);
  });

  test('a prevenção está escrita, não só a doença', () {
    // Uma aula de saúde que só nomeia a doença não serve a ninguém. Cada
    // uma destas tem de vir com o que se faz para não a apanhar.
    final t = tudo();
    for (final par in const [
      ['parasitose', 'lavar as mãos'],
      ['infecção urinária', 'beber água'],
      ['transmissão sexual', 'preservativo'],
    ]) {
      expect(t, contains(par[0]), reason: 'falta ${par[0]}');
      expect(t, contains(par[1]), reason: 'falta a prevenção: ${par[1]}');
    }
  });

  test('os processos da planta estão os três', () {
    final t = tudo();
    for (final p in const ['fotossíntese', 'respiração', 'transpiração']) {
      expect(t, contains(p), reason: 'falta $p');
    }
  });

  test('fala de Moçambique: os recursos e a lei', () {
    final t = tudo();
    expect(t, contains('tete'));
    expect(t, contains('lei moçambicana'));
  });

  test('há pares para ligar, que é como a Biologia se decora', () {
    expect(perguntas().whereType<QMatch>().length, greaterThanOrEqualTo(8));
  });
}
