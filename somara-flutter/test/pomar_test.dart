import 'dart:math';
import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/pomar.dart';

/// O tabuleiro do Pomar.
///
/// As regras de um match-3 são fáceis de escrever mal e difíceis de ver a
/// olho: um tabuleiro que nasce bloqueado, uma peça que fica a flutuar
/// depois da colheita, um trio que não é apanhado porque estava na coluna
/// em vez de na linha. Nada disto dá erro — dá um jogo que parece avariado.
void main() {
  /// Monta um tabuleiro a partir de um desenho, para os casos serem
  /// legíveis. Cada letra é a inicial do produto; o ponto é um buraco.
  Pomar desenhar(List<String> filas) {
    const letras = {
      'm': Produto.manga,
      'b': Produto.banana,
      'c': Produto.coco,
      'i': Produto.milho,
      't': Produto.tomate,
      'a': Produto.amendoim,
    };
    return Pomar(
      linhas: filas.length,
      colunas: filas.first.length,
      casas: [
        for (final f in filas)
          for (final ch in f.split(''))
            ch == '.' ? null : Peca(letras[ch]!),
      ],
    );
  }

  String desenhoDe(Pomar p) => [
    for (var l = 0; l < p.linhas; l++)
      [
        for (var c = 0; c < p.colunas; c++)
          p.em(l, c)?.produto.nome.substring(0, 1) ?? '.',
      ].join(),
  ].join('/');

  group('encontrar os trios', () {
    test('apanha um trio na horizontal', () {
      final p = desenhar(['mmmb', 'tcta', 'batc']);
      expect(p.grupos(), {0, 1, 2});
    });

    test('apanha um trio na vertical', () {
      final p = desenhar(['mbc', 'mta', 'mct', 'bta']);
      expect(p.grupos(), {0, 3, 6});
    });

    test('apanha quatro e cinco seguidos, não só três', () {
      expect(desenhar(['mmmmb']).grupos(), {0, 1, 2, 3});
      expect(desenhar(['mmmmm']).grupos(), {0, 1, 2, 3, 4});
    });

    test('em cruz, apanha os dois braços de uma vez', () {
      // A coluna do meio e a linha do meio partilham o centro.
      final p = desenhar(['btbc', 'mmmc', 'btbc', 'ctac']);
      expect(p.grupos(), containsAll([4, 5, 6]));
      expect(p.grupos(), containsAll([3, 7, 11, 15]));
    });

    test('dois a seguir não são trio', () {
      expect(desenhar(['mmbc', 'tcta', 'batc']).grupos(), isEmpty);
    });

    test('buracos não formam trios', () {
      // Sem isto, três buracos em fila contavam como um grupo e o jogo
      // dava pontos por nada.
      expect(desenhar(['...b', 'tcta', 'batc']).grupos(), isEmpty);
    });
  });

  group('a troca', () {
    test('só entre vizinhas', () {
      final p = desenhar(['mbm', 'bmb', 'mbm']);
      expect(p.saoVizinhas(0, 1), isTrue);
      expect(p.saoVizinhas(0, 3), isTrue);
      expect(p.saoVizinhas(0, 4), isFalse, reason: 'diagonal não é vizinha');
      expect(p.saoVizinhas(0, 2), isFalse, reason: 'saltar uma não é vizinha');
    });

    test('recusa a troca que não forma nada', () {
      final p = desenhar(['mbtc', 'tcmb', 'bmct']);
      expect(p.podeTrocar(0, 1), isFalse);
    });

    test('aceita a troca que forma um trio', () {
      // Trocar as duas do meio da primeira linha põe três mangas em fila.
      final p = desenhar(['mmbm', 'tctc', 'batc']);
      expect(p.podeTrocar(2, 3), isTrue);
      expect(p.trocaCrua(2, 3).grupos(), {0, 1, 2});
    });

    test('recusa uma troca entre casas distantes mesmo que formasse trio', () {
      final p = desenhar(['mmbm', 'tctc', 'batc']);
      expect(p.podeTrocar(0, 3), isFalse, reason: 'não são vizinhas');
    });
  });

  group('assentar', () {
    test('faz cair o que fica por cima do buraco', () {
      final p = desenhar(['mmm', 'bbb', '...']).assentar();
      expect(desenhoDe(p), '.../mmm/bbb');
    });

    test('cada coluna cai por si', () {
      final p = desenhar(['mbc', '.b.', 'tbc']).assentar();
      expect(desenhoDe(p), '.b./mbc/tbc');
    });

    test('não inventa nem perde peças', () {
      final antes = desenhar(['mbc', '.b.', 'tbc']);
      final depois = antes.assentar();
      expect(depois.casas.whereType<Peca>().length,
          antes.casas.whereType<Peca>().length);
    });

    test('assentar duas vezes não muda nada', () {
      final uma = desenhar(['mbc', '.b.', 'tbc']).assentar();
      expect(desenhoDe(uma.assentar()), desenhoDe(uma));
    });
  });

  test('encher não deixa buracos', () {
    final p = desenhar(['...', '.b.', 'tbc']).encher(Random(1));
    expect(p.casas.any((x) => x == null), isFalse);
  });

  group('o tabuleiro que se entrega à criança', () {
    test('nasce sem trios já feitos e com jogada possível', () {
      // Trios feitos davam pontos que ela não ganhou; sem jogada possível,
      // ficava a arrastar peças à espera de algo que nunca aconteceria.
      for (var semente = 0; semente < 40; semente++) {
        final p = Pomar.novo(rnd: Random(semente));
        expect(p.grupos(), isEmpty, reason: 'semente $semente');
        expect(p.haJogada(), isTrue, reason: 'semente $semente');
        expect(p.casas.any((x) => x == null), isFalse);
      }
    });

    test('baralhar devolve um tabuleiro jogável com as mesmas peças', () {
      final r = Random(9);
      final antes = Pomar.novo(rnd: r);
      final depois = antes.baralhar(r);
      expect(depois.haJogada(), isTrue);
      expect(depois.grupos(), isEmpty);
      expect(depois.casas.length, antes.casas.length);
    });
  });

  test('a cascata acaba sempre', () {
    // Colher, assentar e encher pode voltar a formar trios. Se o ciclo não
    // convergisse, a app ficava presa a animar para sempre.
    final r = Random(4);
    var p = Pomar.novo(rnd: r);
    var voltas = 0;
    // Força uma colheita inicial com uma troca válida qualquer.
    for (var i = 0; i < p.casas.length && voltas == 0; i++) {
      for (final j in [i + 1, i + p.colunas]) {
        if (j < p.casas.length && p.podeTrocar(i, j)) {
          p = p.trocaCrua(i, j);
          voltas = 1;
          break;
        }
      }
    }
    expect(voltas, 1, reason: 'devia existir pelo menos uma troca válida');

    while (p.grupos().isNotEmpty) {
      p = p.colher(p.analisar()).assentar().encher(r);
      voltas++;
      expect(voltas, lessThan(200), reason: 'a cascata não convergiu');
    }
    expect(p.grupos(), isEmpty);
  });

  group('o prémio', () {
    test('cada peça a mais vale bastante mais', () {
      // Se a diferença fosse pequena, não compensava procurar e o jogo
      // virava sorte.
      expect(Pomar.pontosDe(4), Pomar.pontosDe(3) * 2);
      expect(Pomar.pontosDe(5), greaterThan(Pomar.pontosDe(4) * 1.5));
      for (var n = 4; n <= 12; n++) {
        expect(Pomar.pontosDe(n), greaterThan(Pomar.pontosDe(n - 1)),
            reason: '$n peças devia valer mais do que ${n - 1}');
      }
    });

    test('as cascatas premeiam em degraus, não por multiplicação', () {
      expect(Pomar.premioDeCascata(1), 0, reason: 'a primeira não é cascata');
      expect(Pomar.premioDeCascata(2), greaterThan(0));
      // Em degraus fixos: a diferença entre níveis é sempre a mesma, e é
      // isso que impede uma jogada feliz de valer mais do que a partida.
      final d1 = Pomar.premioDeCascata(3) - Pomar.premioDeCascata(2);
      final d2 = Pomar.premioDeCascata(4) - Pomar.premioDeCascata(3);
      expect(d1, d2);
    });
  });

  group('a voz de festejo', () {
    test('cala-se num trio simples', () {
      // Uma voz a cada trio seria ruído em vez de prémio.
      expect(Pomar.vozPara(3, 1), isNull);
    });

    test('escala com o tamanho do feito', () {
      final ordem = [
        Pomar.vozPara(5, 1),
        Pomar.vozPara(6, 1),
        Pomar.vozPara(8, 1),
      ];
      expect(ordem, everyElement(isNotNull));
      expect(ordem.toSet().length, 3, reason: 'cada patamar tem a sua voz');
    });

    test('uma cascata longa ganha a tudo o resto', () {
      expect(Pomar.vozPara(3, 4), 'voz-sequencia.mp3');
      expect(Pomar.vozPara(9, 5), 'voz-sequencia.mp3');
    });

    test('as estrelinhas crescem com o grupo e não saem num trio', () {
      expect(Pomar.estrelasPara(3), 0);
      expect(Pomar.estrelasPara(5), greaterThan(Pomar.estrelasPara(4)));
    });
  });

  testesDasEspeciais();

  test('seis produtos, todos do dia-a-dia', () {
    expect(Produto.values.length, 6);
    expect(Produto.values.map((p) => p.nome),
        containsAll(['manga', 'banana', 'milho', 'amendoim']));
    for (final p in Produto.values) {
      expect(p.emoji.isNotEmpty, isTrue);
    }
  });
}

/// As peças especiais.
///
/// É a camada que transforma o jogo: sem ela, juntar quatro ou cinco dá mais
/// pontos mas joga-se da mesma maneira. Com ela, a criança começa a planear
/// — a trocar de propósito para fabricar a peça e a guardá-la para o momento
/// certo. Também é a parte com mais maneiras de estar subtilmente errada,
/// daí a densidade daqui para baixo.
void testesDasEspeciais() {
  Pomar montar(List<String> filas, [Map<int, Especial> especiais = const {}]) {
    const letras = {
      'm': Produto.manga, 'b': Produto.banana, 'c': Produto.coco,
      'i': Produto.milho, 't': Produto.tomate, 'a': Produto.amendoim,
    };
    final casas = <Peca?>[];
    for (final f in filas) {
      for (final ch in f.split('')) {
        casas.add(ch == '.' ? null : Peca(letras[ch]!));
      }
    }
    especiais.forEach((i, e) {
      casas[i] = casas[i]!.comEspecial(e);
    });
    return Pomar(
      linhas: filas.length,
      colunas: filas.first.length,
      casas: casas,
    );
  }

  group('que peça nasce', () {
    test('um trio simples não deixa nada', () {
      expect(montar(['mmmbc', 'tctct', 'batcb']).analisar().criar, isEmpty);
    });

    test('quatro em linha dá um riscado que limpa a coluna', () {
      // Perpendicular de propósito: assim a peça abre terreno novo em vez
      // de repetir a fila que acabou de ser limpa.
      final c = montar(['mmmmc', 'tctct', 'batcb']).analisar();
      expect(c.criar.single.tipo, Especial.riscadoV);
    });

    test('quatro em coluna dá um riscado que limpa a linha', () {
      final c = montar(['mbc', 'mtc', 'mct', 'mtb', 'btc']).analisar();
      expect(c.criar.single.tipo, Especial.riscadoH);
    });

    test('cinco em linha dá um sol', () {
      final c = montar(['mmmmm', 'tctct', 'batcb']).analisar();
      expect(c.criar.single.tipo, Especial.sol);
    });

    test('um L ou um T dá um embrulho', () {
      // Uma fila horizontal e uma vertical que se cruzam são o mesmo
      // encaixe — é isso que as distingue de duas filas soltas.
      final p = montar(['mmm', 'mtc', 'mct']);
      final c = p.analisar();
      expect(c.criar.single.tipo, Especial.embrulho);
      expect(c.limpar, containsAll([0, 1, 2, 3, 6]));
    });

    test('duas filas separadas dão duas peças, não uma', () {
      final c = montar(['mmmm.', '.....', 'bbbb.']).analisar();
      expect(c.criar.length, 2);
    });

    test('a peça nasce onde a criança mexeu', () {
      // Se nascesse no meio da fila, aparecia longe de onde ela está a
      // olhar e parecia que o jogo tinha feito outra coisa.
      final c = montar(['mmmmc', 'tctct', 'batcb']).analisar(origem: 3);
      expect(c.criar.single.onde, 3);
    });
  });

  group('o que cada peça rebenta', () {
    test('o riscado horizontal limpa a linha inteira', () {
      final p = montar(['mbcit', 'bcitm', 'citmb'],
          {6: Especial.riscadoH});
      expect(p.detonar({6}), {5, 6, 7, 8, 9});
    });

    test('o riscado vertical limpa a coluna inteira', () {
      final p = montar(['mbcit', 'bcitm', 'citmb'],
          {6: Especial.riscadoV});
      expect(p.detonar({6}), {1, 6, 11});
    });

    test('o embrulho rebenta o quadrado de três por três', () {
      final p = montar(['mbcit', 'bcitm', 'citmb'],
          {6: Especial.embrulho});
      expect(p.detonar({6}), {0, 1, 2, 5, 6, 7, 10, 11, 12});
    });

    test('o embrulho no canto não sai do tabuleiro', () {
      final p = montar(['mbc', 'bci', 'cit'], {0: Especial.embrulho});
      expect(p.detonar({0}), {0, 1, 3, 4});
    });

    test('rebentar uma apanha as outras, em cadeia', () {
      // É daqui que vêm as jogadas grandes, e é o que faz valer a pena
      // guardar uma peça especial em vez de a gastar logo.
      final p = montar(['mbcit', 'bcitm', 'citmb'],
          {6: Especial.riscadoH, 8: Especial.riscadoV});
      final apanhadas = p.detonar({6});
      expect(apanhadas, containsAll([5, 6, 7, 8, 9]),
          reason: 'a linha do primeiro riscado');
      expect(apanhadas, containsAll([3, 13]),
          reason: 'a coluna do riscado que ele apanhou');
    });

    test('a cadeia não entra em ciclo', () {
      // Dois riscados que se apanham um ao outro parariam a app para sempre
      // se cada um voltasse a disparar o outro.
      final p = montar(['mbcit', 'bcitm', 'citmb'],
          {5: Especial.riscadoH, 9: Especial.riscadoH});
      expect(p.detonar({5}).length, lessThanOrEqualTo(15));
    });
  });

  group('o sol', () {
    test('trocado com uma peça, limpa todos os produtos iguais', () {
      final p = montar(['mbmbm', 'bmbmb', 'mbmbm'], {0: Especial.sol});
      final apanhadas = p.colheitaDoSol(0, 1);
      expect(apanhadas, isNotNull);
      // Todas as bananas, mais o próprio sol.
      expect(apanhadas!.contains(0), isTrue);
      for (var i = 0; i < 15; i++) {
        if (p.casas[i]!.produto == Produto.banana) {
          expect(apanhadas.contains(i), isTrue, reason: 'banana em $i');
        }
      }
    });

    test('vale como jogada mesmo sem formar fila nenhuma', () {
      // É a razão de ser da peça: guarda-se e usa-se quando se quiser.
      final p = montar(['mbcit', 'bcitm', 'citmb'], {0: Especial.sol});
      expect(p.trocaCrua(0, 1).grupos(), isEmpty);
      expect(p.podeTrocar(0, 1), isTrue);
    });

    test('sol com sol limpa o tabuleiro', () {
      final p = montar(['mbcit', 'bcitm', 'citmb'],
          {0: Especial.sol, 1: Especial.sol});
      expect(p.colheitaDoSol(0, 1)!.length, 15);
    });

    test('sozinho não rebenta nada', () {
      // Só age quando é trocado — senão bastava apanhá-lo por acaso numa
      // fila para limpar meio tabuleiro sem querer.
      final p = montar(['mbcit', 'bcitm', 'citmb'], {6: Especial.sol});
      expect(p.detonar({6}), {6});
    });

    test('não se activa entre casas distantes', () {
      final p = montar(['mbcit', 'bcitm', 'citmb'], {0: Especial.sol});
      expect(p.colheitaDoSol(0, 4), isNull);
    });
  });

  test('colher põe a peça nova no sítio e tira as colhidas', () {
    final p = montar(['mmmmc', 'tctct', 'batcb']);
    final c = p.analisar(origem: 1);
    final depois = p.colher(c);
    expect(depois.casas[1]!.especial, Especial.riscadoV);
    for (final i in [0, 2, 3]) {
      expect(depois.casas[i], isNull, reason: 'casa $i devia estar vazia');
    }
  });
}
