import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/escadaria.dart';
import 'package:somara/models/frascos.dart';

import 'apoio/solucionador_frascos.dart';

/// O Water R Sort, pelo modelo.
///
/// A parte que interessa é a última secção, e o solucionador que ela usa
/// (em `apoio/solucionador_frascos.dart`). Ele não sabe nada de como o
/// tabuleiro foi montado: recebe frascos e procura uma saída às cegas. É a
/// única maneira honesta de afirmar que o gerador não produz níveis
/// impossíveis — se a prova usasse o caminho que o gerador guardou, estava
/// a provar-se a si mesma.
void main() {
  /// Os degraus escolhidos: os primeiros, e um de cada lado de cada marco
  /// de mecânica (25, 50, 75, 100).
  const degraus = [1, 2, 5, 10, 24, 25, 49, 50, 74, 75, 99, 100, 250, 500,
      750, nivelMaximo];

  group('as regras do despejo', () {
    Frascos mesa(List<List<CorDoLiquido>> tubos, {int altura = 4}) => Frascos(
      frascos: [for (final t in tubos) Frasco(t, altura)],
      nivel: 1,
      params: frascosNo(1),
    );

    const v = CorDoLiquido.vermelho;
    const a = CorDoLiquido.azul;

    test('para um frasco vazio vai', () {
      final m = mesa([[v, a], []]);
      expect(m.quantosDespeja(0, 1), 1);
    });

    test('para a mesma cor vai', () {
      final m = mesa([[v, a], [a]]);
      expect(m.quantosDespeja(0, 1), 1);
    });

    test('para cor diferente não vai', () {
      final m = mesa([[v, a], [v]]);
      expect(m.quantosDespeja(0, 1), 0,
          reason: 'azul não pode assentar em cima de vermelho');
    });

    test('para um frasco cheio não vai', () {
      final m = mesa([[a], [a, a, a, a]]);
      expect(m.quantosDespeja(0, 1), 0);
    });

    test('de um frasco vazio não sai nada', () {
      expect(mesa([[], [a]]).quantosDespeja(0, 1), 0);
    });

    test('para si mesmo não vai', () {
      expect(mesa([[v, a]]).quantosDespeja(0, 0), 0);
    });

    test('sai a corrida toda de uma vez', () {
      final m = mesa([[v, a, a, a], []]);
      expect(m.quantosDespeja(0, 1), 3, reason: 'os três azuis vão juntos');
      expect(m.despejar(0, 1).frascos[0].blocos, [v]);
      expect(m.despejar(0, 1).frascos[1].blocos, [a, a, a]);
    });

    test('mas só o que couber', () {
      // Três azuis à espera e só dois lugares livres: vão dois, fica um.
      final m = mesa([[v, a, a, a], [a, a]]);
      expect(m.quantosDespeja(0, 1), 2);
      final depois = m.despejar(0, 1);
      expect(depois.frascos[0].blocos, [v, a]);
      expect(depois.frascos[1].blocos, [a, a, a, a]);
    });

    test('uma jogada que não vale devolve a mesa como estava', () {
      final m = mesa([[v], [a]]);
      expect(m.despejar(0, 1).frascos[0].blocos, [v]);
      expect(m.despejar(0, 1).frascos[1].blocos, [a]);
    });

    test('índices fora da mesa não rebentam', () {
      final m = mesa([[v], [a]]);
      expect(m.quantosDespeja(0, 9), 0);
      expect(m.quantosDespeja(-1, 0), 0);
    });
  });

  group('o frasco arrumado', () {
    const v = CorDoLiquido.vermelho;

    test('vazio conta como arrumado', () {
      expect(Frasco.vazio(4).arrumado, isTrue);
    });

    test('cheio de uma cor conta', () {
      expect(Frasco([v, v, v, v], 4).arrumado, isTrue);
    });

    test('dois vermelhos e mais nada NÃO conta', () {
      // Está a meio caminho: os outros dois vermelhos andam por aí, e dar
      // isto por arrumado fechava o nível com o puzzle por resolver.
      expect(Frasco([v, v], 4).arrumado, isFalse);
      expect(Frasco([v, v], 4).deUmaCor, isTrue, reason: 'de uma cor, sim');
    });

    test('a corrida no topo conta só os iguais seguidos', () {
      const a = CorDoLiquido.azul;
      expect(Frasco([a, v, v, v], 4).corridaNoTopo, 3);
      expect(Frasco([v, a, v], 4).corridaNoTopo, 1);
      expect(Frasco.vazio(4).corridaNoTopo, 0);
    });
  });

  group('o tabuleiro de cada degrau', () {
    test('tem as cores e a altura que a escadaria promete', () {
      for (final n in degraus) {
        final p = frascosNo(n);
        final j = Frascos.doNivel(n);
        expect(j.frascos, hasLength(p.quantos), reason: 'nível $n');
        for (final f in j.frascos) {
          expect(f.altura, p.altura, reason: 'nível $n');
        }
      }
    });

    test('cada cor tem exactamente os blocos de uma altura', () {
      // Se uma cor tivesse blocos a mais ou a menos, não havia arrumação
      // possível e o nível era impossível por aritmética.
      for (final n in degraus) {
        final p = frascosNo(n);
        final contagem = <CorDoLiquido, int>{};
        for (final f in Frascos.doNivel(n).frascos) {
          for (final b in f.blocos) {
            contagem[b] = (contagem[b] ?? 0) + 1;
          }
        }
        expect(contagem, hasLength(p.cores), reason: 'nível $n');
        for (final e in contagem.entries) {
          expect(e.value, p.altura,
              reason: 'nível $n: ${e.key.nome} tem ${e.value}');
        }
      }
    });

    test('nunca pede mais cores do que as que existem', () {
      expect(frascosNo(nivelMaximo).cores,
          lessThanOrEqualTo(CorDoLiquido.values.length));
    });

    test('não abre já ganho, e tem sempre jogada', () {
      for (final n in degraus) {
        final j = Frascos.doNivel(n);
        expect(j.ganho, isFalse, reason: 'nível $n abria resolvido');
        expect(j.temJogada, isTrue, reason: 'nível $n abria empancado');
      }
    });

    test('o mesmo degrau dá o mesmo puzzle', () {
      // Duas crianças lado a lado têm de ver a mesma coisa, e "Recomeçar"
      // tem de devolver o tabuleiro com que ela começou.
      for (final n in degraus) {
        final a = Frascos.doNivel(n), b = Frascos.doNivel(n);
        for (var i = 0; i < a.frascos.length; i++) {
          expect(b.frascos[i].blocos, a.frascos[i].blocos, reason: 'nível $n');
        }
      }
    });

    test('degraus diferentes dão puzzles diferentes', () {
      final vistos = <String>{};
      for (final n in degraus) {
        final j = Frascos.doNivel(n);
        vistos.add([
          for (final f in j.frascos) f.blocos.map((c) => c.index).join(','),
        ].join('|'));
      }
      expect(vistos, hasLength(degraus.length));
    });
  });

  group('as mecânicas da escadaria', () {
    test('antes do 25 há dois frascos vazios; depois há um', () {
      expect(frascosNo(24).vazios, 2);
      expect(frascosNo(25).vazios, 1);
    });

    test('a partir do 50 nenhum frasco começa de uma cor só', () {
      // Um frasco já feito à partida é meio nível oferecido.
      for (final n in [50, 100, 500, nivelMaximo]) {
        for (final f in Frascos.doNivel(n).frascos) {
          expect(f.vazio || !f.deUmaCor, isTrue,
              reason: 'nível $n abria com um frasco feito');
        }
      }
    });

    test('a partir do 75 os frascos são de cinco', () {
      expect(frascosNo(74).altura, 4);
      expect(frascosNo(75).altura, 5);
    });

    test('a partir do 100 entra uma cor a mais', () {
      expect(frascosNo(100).cores, frascosNo(99).cores + 1);
    });

    test('o nível 1000 é mesmo diferente do nível 5', () {
      final a = frascosNo(5), b = frascosNo(nivelMaximo);
      expect(b.cores, greaterThan(a.cores));
      expect(b.vazios, lessThan(a.vazios));
      expect(b.altura, greaterThan(a.altura));
      expect(b.baralhadelas, greaterThan(a.baralhadelas));
    });
  });

  group('todos os degraus têm solução', () {
    test('e o solucionador encontra-a sem saber como foram feitos', () {
      for (final n in degraus) {
        final r = resolver(Frascos.doNivel(n));
        expect(r.resolvido, isTrue,
            reason: 'nível $n ficou por resolver ao fim de ${r.estados} '
                'estados — ou é impossível, ou o gerador partiu-se');
      }
    });

    test('e também com sementes que não são a do nível', () {
      // A prova acima corre sobre o puzzle determinista de cada degrau.
      // Esta corre sobre outros, para o caso de a semente fixa ser a única
      // que por sorte dá certo.
      for (final n in [1, 25, 50, 75, 100, 500, nivelMaximo]) {
        for (var s = 0; s < 3; s++) {
          final j = Frascos.doNivel(n, rnd: Random(s + 1));
          expect(resolver(j).resolvido, isTrue,
              reason: 'nível $n, semente $s');
        }
      }
    });

    test('e um tabuleiro sabidamente impossível é recusado', () {
      // Sem isto, um solucionador que respondesse "sim" a tudo passava os
      // dois testes de cima sem provar nada.
      const v = CorDoLiquido.vermelho;
      const a = CorDoLiquido.azul;
      final preso = Frascos(
        frascos: [
          Frasco([v, a, v, a], 4),
          Frasco([a, v, a, v], 4),
        ],
        nivel: 1,
        params: frascosNo(1),
      );
      expect(preso.temJogada, isFalse, reason: 'não há jogada nenhuma');
      expect(resolver(preso).resolvido, isFalse);
    });
  });
}
