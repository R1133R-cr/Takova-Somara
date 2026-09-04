import 'dart:math';
import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/escadaria.dart';
import 'package:somara/models/sopa.dart';

/// A sopa de letras.
///
/// O defeito que estes testes existem para impedir é sempre o mesmo: uma
/// palavra que está na lista mas não está na grelha. A criança procura, não
/// encontra, e conclui que o erro é dela — não há como ela saber que não é.
///
/// Agora que a sopa tem mil degraus, isso deixou de se poder ver a olho: é
/// preciso varrer a escadaria, e é o que estes testes fazem.
void main() {
  /// Lê a grelha ao longo das casas indicadas.
  String lerEm(Sopa s, List<int> casas) =>
      casas.map((i) => s.letras[i]).join();

  /// Degraus escolhidos: o primeiro, os marcos das mecânicas, dois do meio
  /// e o último. É onde as coisas mudam.
  const degraus = [1, 9, 10, 24, 25, 50, 75, 100, 300, 600, nivelMaximo];

  test('todas as palavras da lista estão mesmo lá dentro', () {
    for (final tema in Tema.values) {
      for (final nivel in degraus) {
        for (var semente = 0; semente < 4; semente++) {
          final s = Sopa.doNivel(nivel, rnd: Random(semente), tema: tema);
          expect(s.escondidas.length, sopaNo(nivel).palavras,
              reason: '${tema.rotulo}/nível $nivel: faltam palavras');
          for (final p in s.escondidas) {
            expect(lerEm(s, p.casas), p.palavra,
                reason: '${tema.rotulo}/nível $nivel: ${p.palavra} '
                    'não está onde diz estar');
          }
        }
      }
    }
  });

  test('a grelha fica cheia, sem buracos', () {
    for (final nivel in degraus) {
      final s = Sopa.doNivel(nivel, rnd: Random(1));
      expect(s.letras.length, s.lado * s.lado, reason: 'nível $nivel');
      expect(s.letras.any((x) => x.isEmpty), isFalse, reason: 'nível $nivel');
    }
  });

  test('nenhuma palavra sai da grelha', () {
    for (final nivel in degraus) {
      final s = Sopa.doNivel(nivel, rnd: Random(4));
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
    final s = Sopa.doNivel(300, rnd: Random(8), tema: Tema.escola);
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

  group('a escadaria', () {
    test('a sopa sai com o tamanho e as palavras do degrau', () {
      for (final nivel in degraus) {
        final p = sopaNo(nivel);
        final s = Sopa.doNivel(nivel, rnd: Random(3));
        expect(s.lado, p.lado, reason: 'nível $nivel');
        expect(s.escondidas, hasLength(p.palavras), reason: 'nível $nivel');
        expect(s.nivel, nivel);
      }
    });

    test('a categoria de um nível é sempre a mesma', () {
      // Dois telemóveis com a mesma criança têm de mostrar a mesma sopa, e
      // voltar a um nível já feito não pode dar outra coisa. Por isso a
      // categoria vem do número e não do sorteio.
      for (final nivel in degraus) {
        final a = Sopa.doNivel(nivel, rnd: Random(1)).tema;
        final b = Sopa.doNivel(nivel, rnd: Random(999)).tema;
        expect(a, b, reason: 'nível $nivel mudou de categoria');
        expect(a, Tema.doNivel(nivel));
      }
    });

    test('níveis seguidos não repetem a categoria', () {
      // Nove categorias, uma de cada vez: quem joga cinco níveis de seguida
      // vê cinco assuntos diferentes, e não cinco sopas de animais.
      for (var n = 1; n < 40; n++) {
        expect(Tema.doNivel(n), isNot(Tema.doNivel(n + 1)), reason: 'nível $n');
      }
    });

    test('o nível 500 é mesmo mais difícil do que o 5', () {
      final a = Sopa.doNivel(5, rnd: Random(7));
      final b = Sopa.doNivel(500, rnd: Random(7));
      expect(b.lado, greaterThan(a.lado));
      expect(b.escondidas.length, greaterThan(a.escondidas.length));
    });
  });

  group('as direcções por nível', () {
    test('o nível 1 não tem diagonais nem palavras ao contrário', () {
      // Uma criança da 1ª classe segue a linha com o dedo, da esquerda para
      // a direita. Pôr-lhe diagonais invertidas não é desafio, é um muro.
      final dirs = Sopa.direccoesDe(sopaNo(1));
      expect(dirs, hasLength(2));
      expect(dirs, containsAll([(0, 1), (1, 0)]));
    });

    test('as diagonais entram no 10, ainda sem inverter', () {
      expect(Sopa.direccoesDe(sopaNo(9)), hasLength(2));
      final dirs = Sopa.direccoesDe(sopaNo(10));
      expect(dirs, contains((1, 1)));
      expect(dirs.every((d) => d.$1 >= 0), isTrue,
          reason: 'nada deve subir nem recuar antes do 25');
    });

    test('o marco 25 abre as oito', () {
      expect(
          Sopa.direccoesDe(sopaNo(Mecanica.aoContrario.desde)), hasLength(8));
      expect(Sopa.direccoesDe(sopaNo(nivelMaximo)), hasLength(8));
    });

    test('as palavras respeitam as direcções do nível', () {
      for (final nivel in degraus) {
        final permitidas = Sopa.direccoesDe(sopaNo(nivel)).toSet();
        final s = Sopa.doNivel(nivel, rnd: Random(6), tema: Tema.corpo);
        for (final p in s.escondidas) {
          if (p.casas.length < 2) continue;
          final a = p.casas[0], b = p.casas[1];
          final d = (
            s.linhaDe(b) - s.linhaDe(a),
            s.colunaDe(b) - s.colunaDe(a),
          );
          expect(permitidas.contains(d), isTrue,
              reason: 'nível $nivel: ${p.palavra} vai em $d');
        }
      }
    });
  });

  group('o arrasto', () {
    late Sopa s;
    setUp(() {
      s = Sopa.doNivel(60, rnd: Random(2), tema: Tema.animais);
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

  group('as categorias', () {
    test('trazem palavras que cabem e sem acentos', () {
      // Numa grelha não há acentos. Mostrar "LEÃO" na lista para se procurar
      // "LEAO" nas letras ensinaria a escrever mal.
      final acentos = RegExp('[ÁÀÂÃÉÊÍÓÔÕÚÇáàâãéêíóôõúç]');
      final maiorGrelha = sopaNo(nivelMaximo).lado;
      for (final tema in Tema.values) {
        expect(tema.palavras.length, greaterThanOrEqualTo(10),
            reason: '${tema.rotulo}: poucas palavras para variar');
        for (final p in tema.palavras) {
          expect(acentos.hasMatch(p), isFalse, reason: '$p tem acento');
          expect(p, p.toUpperCase(), reason: '$p devia estar em maiúsculas');
          expect(p.length, lessThanOrEqualTo(maiorGrelha),
              reason: '$p não cabe nem na maior grelha');
        }
      }
    });

    test('não se repetem palavras dentro da mesma categoria', () {
      // Duas iguais na lista dariam à criança uma palavra que ela já riscou.
      for (final tema in Tema.values) {
        expect(tema.palavras.toSet(), hasLength(tema.palavras.length),
            reason: '${tema.rotulo} tem palavras repetidas');
      }
    });

    test('há palavras curtas que chegam para a grelha mais pequena', () {
      // O degrau 1 tem a grelha de 7 e pede 4 palavras. Uma categoria com
      // menos de 4 palavras de 7 letras ou menos daria uma sopa mais curta
      // do que o prometido — e ninguém dava por isso.
      final p = sopaNo(1);
      for (final tema in Tema.values) {
        final cabem = tema.palavras.where((w) => w.length <= p.lado);
        expect(cabem.length, greaterThanOrEqualTo(p.palavras),
            reason: '${tema.rotulo}: não há palavras curtas que cheguem');
      }
    });
  });

  test('o que falta respeita o singular, verbo incluido', () {
    // Nao chega mudar o nome: "faltam 1" esta tao errado como "falta 3".
    expect(quantasFaltam(3), 'faltam 3');
    expect(quantasFaltam(2), 'faltam 2');
    expect(quantasFaltam(1), 'falta 1');
    expect(quantasFaltam(0), 'faltam 0');
  });
}
