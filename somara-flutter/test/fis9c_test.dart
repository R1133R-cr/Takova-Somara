import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Física da 9ª classe.
///
/// Cinco unidades do programa do INDE, pela ordem dele. As regras da 8ª
/// valem aqui e o teste guarda-as: as unidades escrevem-se por extenso nos
/// enunciados («ohms», «volts», «amperes», «watts», «pascal»), os símbolos
/// ficam nas opções, e as contas dão inteiros com a gravidade igual a 10.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso fis9() => c.cursos.firstWhere((x) => x.id == 'fis-9c');

  Iterable<Questao> perguntas() sync* {
    for (final u in fis9().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  test('as cinco unidades do programa, pela ordem dele', () {
    expect(
      fis9().units.map((u) => u.titulo).toList(),
      [
        'Óptica geométrica',
        'Estática dos sólidos e dos fluidos',
        'Electricidade',
        'Electromagnetismo',
        'Oscilações e ondas mecânicas',
      ],
    );
    expect(fis9().fonte, contains('pp. 32-44'));
    expect(fis9().provisorio, isFalse);
  });

  test('nos enunciados, as unidades vêm por extenso', () {
    final proibidos = RegExp(r'\d\s*(V\b|A\b|W\b|Ω|Pa\b|Hz\b|N\b|kWh)');
    for (final q in perguntas()) {
      expect(proibidos.hasMatch(q.q), isFalse,
          reason: 'símbolo de unidade num enunciado: "${q.q}"');
    }
    final texto = perguntas().map((q) => q.q).join('\n');
    for (final palavra in const [
      'ohms',
      'volts',
      'amperes',
      'watts',
      'pascal',
      'hertz',
      'newtons',
      'quilowatt-hora',
    ]) {
      expect(texto, contains(palavra), reason: 'falta "$palavra"');
    }
  });

  test('as contas de electricidade dão certo', () {
    final respostas = {
      for (final q in perguntas().whereType<QInput>()) q.q: q.a,
    };
    String resposta(String pedaco) =>
        respostas.entries.firstWhere((e) => e.key.contains(pedaco)).value;
    expect(resposta('4 ohms'), '3'); // 12 V / 4 Ω
    expect(resposta('2 amperes quando'), '110'); // 220 V / 2 A
    expect(resposta('em série dão'), '10');
    expect(resposta('em paralelo dão'), '3');
    expect(resposta('Qual é a potência, em watts'), '440');
    expect(resposta('quilowatt-hora'), '1');
  });

  test('Pascal, Arquimedes, Ohm, Oersted e Torricelli estão os cinco', () {
    final texto = perguntas().map((q) => q.q).join('\n');
    for (final nome in const ['Pascal', 'Arquimedes', 'Ohm', 'Oersted', 'Torricelli']) {
      expect(texto, contains(nome), reason: 'falta "$nome"');
    }
  });

  test('as respostas numéricas são inteiras', () {
    for (final q in perguntas().whereType<QInput>()) {
      expect(RegExp(r'^\d+$').hasMatch(q.a), isTrue, reason: q.q);
    }
  });
}
