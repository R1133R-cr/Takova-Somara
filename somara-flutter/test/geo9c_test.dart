import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A Geografia da 9ª classe — a Geografia de Moçambique.
///
/// A 7ª foi a Geografia geral e a 8ª a humana e económica; a 9ª é o país
/// inteiro, do Rovuma ao Maputo, em quatro unidades do programa do INDE.
/// O que este teste guarda é que o país está lá com os nomes certos —
/// os vizinhos, os rios, os minerais, os corredores — e o Niassa com eles.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;
  setUpAll(() async => c = await Conteudo.carregar());

  Curso geo9() => c.cursos.firstWhere((x) => x.id == 'geo-9c');

  Iterable<Questao> perguntas() sync* {
    for (final u in geo9().units) {
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

  test('as quatro unidades do programa, pela ordem dele', () {
    expect(
      geo9().units.map((u) => u.titulo).toList(),
      [
        'Geografia física de Moçambique',
        'População',
        'Actividades económicas em Moçambique',
        'Moçambique e a SADC',
      ],
    );
    expect(geo9().fonte, contains('pp. 37-47'));
    expect(geo9().provisorio, isFalse);
  });

  test('os seis vizinhos estão os seis', () {
    final texto = tudo();
    for (final pais in const [
      'Tanzânia',
      'Malawi',
      'Zâmbia',
      'Zimbabué',
      'África do Sul',
      'Essuatíni',
    ]) {
      expect(texto, contains(pais), reason: 'falta "$pais"');
    }
    final seis = perguntas().whereType<QInput>().firstWhere(
        (q) => q.q.contains('quantos países faz fronteira'));
    expect(seis.a, '6');
  });

  test('os rios, os minerais e os corredores têm o lugar certo', () {
    final pares = perguntas()
        .whereType<QMatch>()
        .expand((q) => q.pairs.map((p) => '${p.$1} → ${p.$2}'))
        .toList();
    expect(pares, contains('Carvão → Moatize, em Tete'));
    expect(pares, contains('Rovuma e Lúrio → Norte'));
    expect(pares, contains('Corredor de Nacala → Porto de Nacala, em Nampula'));
    expect(pares, contains('Castanha de caju → Nampula'));
  });

  test('o Niassa está na Geografia do país', () {
    final texto = tudo();
    expect(texto, contains('Lichinga'));
    expect(texto, contains('lago Niassa'));
    expect(texto, contains('Reserva'));
    expect(texto, contains('miombo'));
  });

  test('a SADC soletra-se e as contas dão inteiros', () {
    // "SADC" está na lista de siglas que se dizem letra a letra desde a
    // 7ª; aqui só se guarda que a sigla aparece nos enunciados e que as
    // contas (crescimento natural, poupança, anos) dão números inteiros.
    expect(perguntas().map((q) => q.q).join('\n'), contains('SADC'));
    for (final q in perguntas().whereType<QInput>()) {
      expect(RegExp(r'^\d+$').hasMatch(q.a), isTrue, reason: q.q);
    }
  });
}
