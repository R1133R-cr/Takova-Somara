import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Biologia da 9ª classe.
///
/// Cinco unidades do programa do INDE, pela ordem dele. O que este teste
/// guarda, além da forma, é a regra das siglas: «SNC», «DIU», «HPV» e
/// «ITS» a voz leria como palavras, por isso ficam nas opções e nos
/// enunciados escreve-se por extenso. Só «HIV» entra, porque se soletra.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso bio9() => c.cursos.firstWhere((x) => x.id == 'bio-9c');

  Iterable<Questao> perguntas() sync* {
    for (final u in bio9().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as cinco unidades do programa, pela ordem dele', () {
    expect(
      bio9().units.map((u) => u.titulo).toList(),
      [
        'Seres vivos e ambiente',
        'Sistemas do corpo humano',
        'Reprodução nos seres vivos',
        'Agricultura',
        'Auto-descobrimento',
      ],
    );
    expect(bio9().fonte, contains('pp. 44-57'));
    expect(bio9().provisorio, isFalse);
  });

  test('nos enunciados, a única sigla é HIV', () {
    final siglas = <String>{};
    for (final q in perguntas()) {
      siglas.addAll(RegExp(r'\b[A-Z]{2,}\b').allMatches(q.q).map((m) => m[0]!));
    }
    expect(siglas, {'HIV'});
    final texto = perguntas().map((q) => q.q).join('\n');
    expect(texto, contains('infecções de transmissão sexual'));
    // O vírus do papiloma humano entra por extenso numa opção: é lá que a
    // sigla «HPV» teria de estar, e não está.
    final opcoes =
        perguntas().whereType<QChoice>().expand((q) => q.options).join('\n');
    expect(opcoes, contains('vírus do papiloma humano'));
    expect(opcoes, isNot(contains('HPV')));
  });

  test('os números do corpo estão certos', () {
    final respostas = {
      for (final q in perguntas().whereType<QInput>()) q.q: q.a,
    };
    String resposta(String pedaco) =>
        respostas.entries.firstWhere((e) => e.key.contains(pedaco)).value;
    expect(resposta('ossos'), '206');
    expect(resposta('ciclo menstrual'), '28');
    expect(resposta('semanas'), '40');
    expect(resposta('10 por cento'), '100');
  });

  test('o preservativo é o único que protege das infecções', () {
    final q = perguntas()
        .whereType<QChoice>()
        .firstWhere((q) => q.q.contains('infecções de transmissão sexual'));
    expect(q.options[q.a], 'O preservativo');
  });

  test('as práticas do programa estão lá: Pavlov, o joelho, a luz, o solo', () {
    final texto = perguntas().map((q) => q.q).join('\n');
    expect(texto, contains('Pavlov'));
    expect(texto, contains('joelho'));
    expect(texto, contains('sem luz'));
    expect(texto, contains('permeabilidade'));
  });
}
