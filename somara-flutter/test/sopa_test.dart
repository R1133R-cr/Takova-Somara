import 'dart:math';
import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/sopa.dart';

/// A sopa de letras.
///
/// O defeito que estes testes existem para impedir é sempre o mesmo: uma
/// palavra que está na lista mas não está na grelha. A criança procura, não
/// encontra, e conclui que o erro é dela — não há como ela saber que não é.
void main() {
  /// Lê a grelha ao longo das casas indicadas.
  String lerEm(Sopa s, List<int> casas) =>
      casas.map((i) => s.letras[i]).join();

  test('todas as palavras da lista estão mesmo lá dentro', () {
    for (final tema in Tema.values) {
      for (final nivel in NivelSopa.values) {
        for (var semente = 0; semente < 6; semente++) {
          final s = Sopa.nova(
            tema: tema,
            nivel: nivel,
            rnd: Random(semente),
          );
          expect(s.escondidas.length, nivel.quantasPalavras,
              reason: '${tema.rotulo}/${nivel.rotulo}: faltam palavras');
          for (final p in s.escondidas) {
            expect(lerEm(s, p.casas), p.palavra,
                reason: '${tema.rotulo}/${nivel.rotulo}: ${p.palavra} '
                    'não está onde diz estar');
          }
        }
      }
    }
  });

  test('a grelha fica cheia, sem buracos', () {
    final s = Sopa.nova(tema: Tema.animais, nivel: NivelSopa.medio, rnd: Random(1));
    expect(s.letras.length, s.lado * s.lado);
    expect(s.letras.any((x) => x.isEmpty), isFalse);
  });

  test('nenhuma palavra sai da grelha', () {
    for (final nivel in NivelSopa.values) {
      final s = Sopa.nova(tema: Tema.frutas, nivel: nivel, rnd: Random(4));
      for (final p in s.escondidas) {
        for (final i in p.casas) {
          expect(i, inInclusiveRange(0, s.lado * s.lado - 1));
        }
      }
    }
  });

  test('as palavras cruzam-se só onde a letra é a mesma', () {
    // É o que torna a sopa densa; cruzar onde as letras diferem daria uma
    // grelha em que as palavras se apagam umas às outras.
    final s = Sopa.nova(tema: Tema.escola, nivel: NivelSopa.dificil, rnd: Random(8));
    final ocupadas = <int, String>{};
    for (final p in s.escondidas) {
      for (var k = 0; k < p.palavra.length; k++) {
        final i = p.casas[k];
        final letra = p.palavra[k];
        if (ocupadas.containsKey(i)) {
          expect(ocupadas[i], letra, reason: 'cruzamento errado em $i');
        }
        ocupadas[i] = letra;
      }
    }
  });

  group('as direcções por nível', () {
    test('o fácil não tem diagonais nem palavras ao contrário', () {
      // Uma criança da 1ª classe segue a linha com o dedo, da esquerda para
      // a direita. Pôr-lhe diagonais invertidas não é desafio, é um muro.
      final dirs = Sopa.direccoesDe(NivelSopa.facil);
      expect(dirs, hasLength(2));
      expect(dirs, containsAll([(0, 1), (1, 0)]));
    });

    test('o médio ganha diagonais, ainda sem inverter', () {
      final dirs = Sopa.direccoesDe(NivelSopa.medio);
      expect(dirs, contains((1, 1)));
      expect(dirs.every((d) => d.$1 >= 0), isTrue,
          reason: 'nada deve subir nem recuar no médio');
    });

    test('o difícil usa as oito', () {
      expect(Sopa.direccoesDe(NivelSopa.dificil), hasLength(8));
    });

    test('as palavras respeitam as direcções do nível', () {
      for (final nivel in NivelSopa.values) {
        final permitidas = Sopa.direccoesDe(nivel).toSet();
        final s = Sopa.nova(tema: Tema.corpo, nivel: nivel, rnd: Random(6));
        for (final p in s.escondidas) {
          if (p.casas.length < 2) continue;
          final a = p.casas[0], b = p.casas[1];
          final d = (s.linhaDe(b) - s.linhaDe(a), s.colunaDe(b) - s.colunaDe(a));
          expect(permitidas.contains(d), isTrue,
              reason: '${nivel.rotulo}: ${p.palavra} vai em $d');
        }
      }
    });
  });

  group('o arrasto', () {
    late Sopa s;
    setUp(() {
      s = Sopa.nova(tema: Tema.animais, nivel: NivelSopa.medio, rnd: Random(2));
    });

    test('uma linha recta dá as casas pelo caminho', () {
      final linha = s.linhaEntre(s.indice(2, 1), s.indice(2, 4));
      expect(linha, [
        s.indice(2, 1), s.indice(2, 2), s.indice(2, 3), s.indice(2, 4),
      ]);
    });

    test('uma diagonal também', () {
      final linha = s.linhaEntre(s.indice(0, 0), s.indice(3, 3));
      expect(linha, [
        s.indice(0, 0), s.indice(1, 1), s.indice(2, 2), s.indice(3, 3),
      ]);
    });

    test('um dedo aos saltos não selecciona nada', () {
      // Numa sopa de letras só valem linhas. Sem esta regra, arrastar em
      // ziguezague apanhava letras soltas e acertava por acidente.
      expect(s.linhaEntre(s.indice(0, 0), s.indice(2, 5)), isNull);
    });

    test('acerta na palavra, arrastada de qualquer das pontas', () {
      // Obrigar a começar pela ponta certa seria um castigo por nada.
      final p = s.escondidas.first;
      expect(s.acertaEm(p.casas)?.palavra, p.palavra);
      expect(s.acertaEm(p.casas.reversed.toList())?.palavra, p.palavra);
    });

    test('não acerta em letras que não formam palavra da lista', () {
      final p = s.escondidas.first;
      expect(s.acertaEm(p.casas.take(p.casas.length - 1).toList()), isNull);
    });
  });

  test('os temas trazem palavras que cabem e sem acentos', () {
    // Numa grelha não há acentos. Mostrar "LEÃO" na lista para se procurar
    // "LEAO" nas letras ensinaria a escrever mal.
    final acentos = RegExp('[ÁÀÂÃÉÊÍÓÔÕÚÇáàâãéêíóôõúç]');
    for (final tema in Tema.values) {
      expect(tema.palavras.length, greaterThanOrEqualTo(10),
          reason: '${tema.rotulo}: poucas palavras para variar');
      for (final p in tema.palavras) {
        expect(acentos.hasMatch(p), isFalse, reason: '$p tem acento');
        expect(p, p.toUpperCase(), reason: '$p devia estar em maiúsculas');
        expect(p.length, lessThanOrEqualTo(NivelSopa.facil.lado + 4),
            reason: '$p é comprida de mais para caber em qualquer grelha');
      }
    }
  });

  test('há palavras curtas que cabem no nível fácil', () {
    for (final tema in Tema.values) {
      final cabem =
          tema.palavras.where((p) => p.length <= NivelSopa.facil.lado);
      expect(cabem.length,
          greaterThanOrEqualTo(NivelSopa.facil.quantasPalavras),
          reason: '${tema.rotulo}: não há palavras curtas que cheguem');
    }
  });
  test('o que falta respeita o singular, verbo incluido', () {
    // Nao chega mudar o nome: "faltam 1" esta tao errado como "falta 3".
    expect(quantasFaltam(3), 'faltam 3');
    expect(quantasFaltam(2), 'faltam 2');
    expect(quantasFaltam(1), 'falta 1');
    expect(quantasFaltam(0), 'faltam 0');
  });
}
