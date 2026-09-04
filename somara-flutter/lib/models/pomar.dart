import 'dart:math';

/// O que se apanha no tabuleiro.
///
/// Seis produtos do dia-a-dia moçambicano, não os rebuçados coloridos do
/// costume. Uma criança de Lichinga reconhece uma maçaroca de milho e um
/// amendoim; e o jogo, sem ensinar nada de propósito, nomeia as coisas que
/// ela vê no mercado.
///
/// Seis e não oito: quantos mais tipos houver, menos coincidências saem por
/// acaso, e um tabuleiro onde raramente se forma um trio deixa de ser um
/// jogo e passa a ser uma busca.
enum Produto {
  manga('🥭', 'manga'),
  banana('🍌', 'banana'),
  coco('🥥', 'coco'),
  milho('🌽', 'milho'),
  tomate('🍅', 'tomate'),
  amendoim('🥜', 'amendoim');

  final String emoji;
  final String nome;
  const Produto(this.emoji, this.nome);
}

/// O que uma peça faz de especial quando é colhida.
///
/// Vem da mecânica que os jogos do género usam há uma década, e existe por
/// uma razão concreta: sem ela, juntar quatro ou cinco peças dá mais pontos
/// mas joga-se exactamente da mesma maneira. Com ela, a criança começa a
/// **planear** — a trocar de propósito para fabricar a peça, e a guardá-la
/// para o momento certo. É a diferença entre carregar em coisas e jogar.
enum Especial {
  /// Peça comum.
  nenhuma,

  /// Quatro em coluna: limpa a linha inteira onde estiver.
  riscadoH,

  /// Quatro em linha: limpa a coluna inteira onde estiver.
  ///
  /// A direcção é perpendicular à do encaixe de propósito — assim a peça
  /// abre terreno novo em vez de repetir o que já foi limpo.
  riscadoV,

  /// Cinco em L ou em T: rebenta o quadrado de três por três à volta.
  embrulho,

  /// Cinco em linha: limpa todos os produtos iguais ao da peça com que for
  /// trocada. É a peça mais forte do tabuleiro e a mais rara.
  sol;

  bool get eRiscado => this == riscadoH || this == riscadoV;
}

/// Uma casa do tabuleiro: o produto e o que ele tem de especial.
class Peca {
  final Produto produto;
  final Especial especial;

  const Peca(this.produto, [this.especial = Especial.nenhuma]);

  Peca comEspecial(Especial e) => Peca(produto, e);

  bool get eEspecial => especial != Especial.nenhuma;

  @override
  bool operator ==(Object other) =>
      other is Peca && other.produto == produto && other.especial == especial;

  @override
  int get hashCode => Object.hash(produto, especial);

  @override
  String toString() => '${produto.nome}${eEspecial ? "/${especial.name}" : ""}';
}

/// O resultado de olhar para o tabuleiro: o que se colhe e o que nasce.
class Colheita {
  /// Todas as casas a tirar.
  final Set<int> limpar;

  /// As peças especiais a criar, com o sítio e o tipo.
  final List<({int onde, Especial tipo, Produto produto})> criar;

  const Colheita({required this.limpar, required this.criar});

  bool get vazia => limpar.isEmpty;
}

/// O tabuleiro do Pomar: um match-3 com peças especiais.
///
/// Imutável de propósito. Cada passo — trocar, colher, assentar, encher —
/// devolve um tabuleiro novo, e é isso que torna a cascata fácil de seguir
/// e de testar: a partida é uma lista de estados, não uma grelha que se
/// altera por baixo dos pés de quem está a desenhá-la.
class Pomar {
  final int linhas;
  final int colunas;

  /// As casas, lidas da esquerda para a direita e de cima para baixo.
  /// Nulo é um buraco à espera de ser preenchido.
  final List<Peca?> casas;

  const Pomar({
    required this.linhas,
    required this.colunas,
    required this.casas,
  });

  int indice(int l, int c) => l * colunas + c;
  int linhaDe(int i) => i ~/ colunas;
  int colunaDe(int i) => i % colunas;

  bool dentro(int l, int c) =>
      l >= 0 && c >= 0 && l < linhas && c < colunas;

  Peca? em(int l, int c) => dentro(l, c) ? casas[indice(l, c)] : null;
  Produto? produtoEm(int l, int c) => em(l, c)?.produto;

  Pomar comCasas(List<Peca?> novas) =>
      Pomar(linhas: linhas, colunas: colunas, casas: novas);

  /// Um tabuleiro pronto a jogar: sem trios já feitos e com pelo menos uma
  /// jogada possível.
  ///
  /// As duas condições contam. Começar com trios feitos dava pontos que a
  /// criança não ganhou; começar sem jogada possível dava um tabuleiro
  /// bloqueado logo à entrada, e ela não teria como saber que a culpa não
  /// era dela.
  factory Pomar.novo({int linhas = 8, int colunas = 7, Random? rnd}) {
    final r = rnd ?? Random();
    for (var tentativa = 0; tentativa < 200; tentativa++) {
      var p = Pomar(
        linhas: linhas,
        colunas: colunas,
        casas: List.generate(
          linhas * colunas,
          (_) => Peca(Produto.values[r.nextInt(Produto.values.length)]),
        ),
      );
      p = p._desfazerTriosIniciais(r);
      if (p.haJogada()) return p;
    }
    return Pomar(
      linhas: linhas,
      colunas: colunas,
      casas: List.generate(
        linhas * colunas,
        (i) => Peca(Produto.values[(i + i ~/ colunas) % Produto.values.length]),
      ),
    );
  }

  Pomar _desfazerTriosIniciais(Random r) {
    var casas = List<Peca?>.from(this.casas);
    for (var volta = 0; volta < 60; volta++) {
      final grupos = comCasas(casas).grupos();
      if (grupos.isEmpty) break;
      for (final i in grupos) {
        casas[i] = Peca(Produto.values[r.nextInt(Produto.values.length)]);
      }
    }
    return comCasas(casas);
  }

  /// As sequências de três ou mais do mesmo produto, em linha e em coluna.
  ///
  /// Devolve cada sequência à parte — é dela que sai o tipo de peça especial
  /// a criar, e uma vez juntas num único conjunto essa informação perdia-se.
  List<({List<int> casas, bool horizontal})> _sequencias() {
    final achadas = <({List<int> casas, bool horizontal})>[];

    void varrer(bool horizontal) {
      final externo = horizontal ? linhas : colunas;
      final interno = horizontal ? colunas : linhas;
      for (var a = 0; a < externo; a++) {
        var inicio = 0;
        while (inicio < interno) {
          final actual =
              horizontal ? produtoEm(a, inicio) : produtoEm(inicio, a);
          var fim = inicio + 1;
          if (actual != null) {
            while (fim < interno &&
                (horizontal ? produtoEm(a, fim) : produtoEm(fim, a)) ==
                    actual) {
              fim++;
            }
          }
          if (actual != null && fim - inicio >= 3) {
            achadas.add((
              casas: [
                for (var k = inicio; k < fim; k++)
                  horizontal ? indice(a, k) : indice(k, a),
              ],
              horizontal: horizontal,
            ));
          }
          inicio = fim;
        }
      }
    }

    varrer(true);
    varrer(false);
    return achadas;
  }

  /// Todas as casas que fazem parte de um encaixe.
  Set<int> grupos() => {
    for (final s in _sequencias()) ...s.casas,
  };

  /// Olha para o tabuleiro e diz o que se colhe e que peças nascem.
  ///
  /// [origem] é a casa que a criança acabou de mover. Quando faz parte de um
  /// encaixe, a peça especial nasce **lá** e não no meio da fila — é onde ela
  /// está a olhar, e onde espera que apareça.
  Colheita analisar({int? origem}) {
    final sequencias = _sequencias();
    if (sequencias.isEmpty) {
      return const Colheita(limpar: {}, criar: []);
    }

    // Sequências que partilham casas são o mesmo encaixe: é assim que um L
    // ou um T se reconhecem, e é isso que os distingue de duas filas soltas.
    final grupos = <List<({List<int> casas, bool horizontal})>>[];
    for (final s in sequencias) {
      final conjunto = s.casas.toSet();
      final juntar = <int>[];
      for (var g = 0; g < grupos.length; g++) {
        if (grupos[g].any((o) => o.casas.any(conjunto.contains))) {
          juntar.add(g);
        }
      }
      if (juntar.isEmpty) {
        grupos.add([s]);
      } else {
        final fundido = <({List<int> casas, bool horizontal})>[s];
        for (final g in juntar.reversed) {
          fundido.addAll(grupos.removeAt(g));
        }
        grupos.add(fundido);
      }
    }

    final limpar = <int>{};
    final criar = <({int onde, Especial tipo, Produto produto})>[];

    for (final grupo in grupos) {
      final casasDoGrupo = <int>{for (final s in grupo) ...s.casas};
      limpar.addAll(casasDoGrupo);

      final maior = grupo
          .map((s) => s.casas.length)
          .reduce((a, b) => a > b ? a : b);
      final temHorizontal = grupo.any((s) => s.horizontal);
      final temVertical = grupo.any((s) => !s.horizontal);

      final Especial tipo;
      if (maior >= 5) {
        tipo = Especial.sol;
      } else if (temHorizontal && temVertical) {
        // Cruzamento em L ou em T.
        tipo = Especial.embrulho;
      } else if (maior == 4) {
        // Perpendicular ao encaixe: quatro em linha dá uma peça que limpa
        // a coluna, e vice-versa.
        tipo = temHorizontal ? Especial.riscadoV : Especial.riscadoH;
      } else {
        continue; // um trio simples não deixa nada.
      }

      final onde = (origem != null && casasDoGrupo.contains(origem))
          ? origem
          : casasDoGrupo.elementAt(casasDoGrupo.length ~/ 2);

      criar.add((
        onde: onde,
        tipo: tipo,
        produto: casas[casasDoGrupo.first]!.produto,
      ));
    }

    return Colheita(limpar: limpar, criar: criar);
  }

  /// Alarga um conjunto de casas com o que as peças especiais rebentam.
  ///
  /// Em cadeia: um riscado que apanha um embrulho faz o embrulho rebentar
  /// também. É daqui que vêm as jogadas grandes, e é o que faz valer a pena
  /// guardar uma peça especial em vez de a gastar logo.
  Set<int> detonar(Set<int> inicial) {
    final marcadas = <int>{...inicial};
    final porTratar = <int>[...inicial];

    while (porTratar.isNotEmpty) {
      final i = porTratar.removeLast();
      final peca = casas[i];
      if (peca == null || !peca.eEspecial) continue;

      final novas = <int>{};
      switch (peca.especial) {
        case Especial.riscadoH:
          final l = linhaDe(i);
          for (var c = 0; c < colunas; c++) {
            novas.add(indice(l, c));
          }
        case Especial.riscadoV:
          final c = colunaDe(i);
          for (var l = 0; l < linhas; l++) {
            novas.add(indice(l, c));
          }
        case Especial.embrulho:
          final l = linhaDe(i), c = colunaDe(i);
          for (var dl = -1; dl <= 1; dl++) {
            for (var dc = -1; dc <= 1; dc++) {
              if (dentro(l + dl, c + dc)) novas.add(indice(l + dl, c + dc));
            }
          }
        case Especial.sol:
          // Sozinho não faz nada: o sol só age quando é trocado, e aí é
          // [trocarComSol] que decide o que ele apanha.
          break;
        case Especial.nenhuma:
          break;
      }

      for (final n in novas) {
        if (casas[n] != null && marcadas.add(n)) porTratar.add(n);
      }
    }
    return marcadas;
  }

  bool saoVizinhas(int a, int b) {
    final dl = (linhaDe(a) - linhaDe(b)).abs();
    final dc = (colunaDe(a) - colunaDe(b)).abs();
    return dl + dc == 1;
  }

  /// O tabuleiro com duas casas trocadas, sem verificar nada.
  Pomar trocaCrua(int a, int b) {
    final novas = List<Peca?>.from(casas);
    final t = novas[a];
    novas[a] = novas[b];
    novas[b] = t;
    return comCasas(novas);
  }

  /// A troca envolve um sol? Nesse caso vale sempre, e limpa tudo o que for
  /// do produto da outra peça.
  Set<int>? colheitaDoSol(int a, int b) {
    if (!saoVizinhas(a, b)) return null;
    final pa = casas[a], pb = casas[b];
    if (pa == null || pb == null) return null;

    final sol = pa.especial == Especial.sol
        ? a
        : (pb.especial == Especial.sol ? b : null);
    if (sol == null) return null;

    final outra = sol == a ? pb : pa;

    // Sol com sol limpa o tabuleiro inteiro — a jogada mais rara que há.
    if (outra.especial == Especial.sol) {
      return {for (var i = 0; i < casas.length; i++) if (casas[i] != null) i};
    }

    return {
      sol,
      for (var i = 0; i < casas.length; i++)
        if (casas[i]?.produto == outra.produto) i,
    };
  }

  /// Uma troca só vale se for entre vizinhas e se formar alguma coisa.
  ///
  /// Trocar sem formar nada é a regra que faz o jogo ser um jogo. Sem ela
  /// bastava arrastar tudo ao acaso até acontecer alguma coisa.
  bool podeTrocar(int a, int b) {
    if (!saoVizinhas(a, b)) return false;
    if (colheitaDoSol(a, b) != null) return true;
    return trocaCrua(a, b).grupos().isNotEmpty;
  }

  /// Há alguma troca que forme alguma coisa?
  bool haJogada() {
    for (var l = 0; l < linhas; l++) {
      for (var c = 0; c < colunas; c++) {
        final i = indice(l, c);
        if (c + 1 < colunas && podeTrocar(i, indice(l, c + 1))) return true;
        if (l + 1 < linhas && podeTrocar(i, indice(l + 1, c))) return true;
      }
    }
    return false;
  }

  /// Tira do tabuleiro as casas colhidas, deixando buracos, e põe as peças
  /// especiais que nasceram.
  Pomar colher(Colheita c) {
    final novas = List<Peca?>.from(casas);
    for (final i in c.limpar) {
      novas[i] = null;
    }
    for (final n in c.criar) {
      novas[n.onde] = Peca(n.produto, n.tipo);
    }
    return comCasas(novas);
  }

  /// Faz cair o que está por cima dos buracos.
  Pomar assentar() {
    final novas = List<Peca?>.from(casas);
    for (var c = 0; c < colunas; c++) {
      var escrita = linhas - 1;
      for (var l = linhas - 1; l >= 0; l--) {
        final v = novas[indice(l, c)];
        if (v != null) {
          novas[indice(escrita, c)] = v;
          if (escrita != l) novas[indice(l, c)] = null;
          escrita--;
        }
      }
      for (var l = escrita; l >= 0; l--) {
        novas[indice(l, c)] = null;
      }
    }
    return comCasas(novas);
  }

  /// Enche os buracos que sobraram em cima.
  Pomar encher(Random r) {
    final novas = List<Peca?>.from(casas);
    for (var i = 0; i < novas.length; i++) {
      novas[i] ??= Peca(Produto.values[r.nextInt(Produto.values.length)]);
    }
    return comCasas(novas);
  }

  /// Baralha o tabuleiro mantendo as mesmas peças.
  ///
  /// Usa-se quando não há jogada possível: em vez de acabar a partida por
  /// azar do tabuleiro, remexem-se as mesmas peças até haver saída.
  Pomar baralhar(Random r) {
    final pecas = casas.whereType<Peca>().toList();
    for (var tentativa = 0; tentativa < 80; tentativa++) {
      pecas.shuffle(r);
      final p =
          comCasas(List<Peca?>.from(pecas))._desfazerTriosIniciais(r);
      if (p.haJogada()) return p;
    }
    return Pomar.novo(linhas: linhas, colunas: colunas, rnd: r);
  }

  /// Pontos de uma colheita, por número de peças.
  ///
  /// Os saltos são grandes de propósito. Num match-3, o que separa quem
  /// arrasta peças à toa de quem procura é ver que quatro vale o dobro de
  /// três e cinco vale quase o quádruplo — se a diferença for pequena, não
  /// compensa procurar e o jogo vira sorte.
  static int pontosDe(int quantas) {
    if (quantas <= 3) return 60;
    if (quantas == 4) return 120;
    if (quantas == 5) return 220;
    return 220 + (quantas - 5) * 90;
  }

  /// Prémio por cada cascata seguida, a partir da segunda.
  ///
  /// Cresce em degraus fixos e não por multiplicação — multiplicar dava mil
  /// pontos numa jogada feliz e tornava as outras dezanove irrelevantes.
  static int premioDeCascata(int nivel) => nivel <= 1 ? 0 : (nivel - 1) * 50;

  /// O que a criança ouve, conforme o tamanho do feito.
  ///
  /// Silêncio abaixo de cinco peças — uma voz a cada trio seria ruído em vez
  /// de prémio.
  static String? vozPara(int quantas, int nivelDeCascata) {
    if (nivelDeCascata >= 4) return 'voz-sequencia.mp3';
    if (quantas >= 8) return 'voz-fantastico.mp3';
    if (quantas >= 6) return 'voz-excelente.mp3';
    if (quantas >= 5) return 'voz-muito-bem.mp3';
    if (nivelDeCascata >= 2) return 'voz-boa.mp3';
    return null;
  }

  /// Quantas estrelinhas saltam de uma colheita.
  static int estrelasPara(int quantas) =>
      quantas <= 3 ? 0 : (quantas - 2) * 3;
}
