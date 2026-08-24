import 'dart:math';

/// O que se apanha no tabuleiro.
///
/// Seis produtos do dia-a-dia moçambicano, não os rebuçados coloridos do
/// costume. Uma criança de Lichinga reconhece um maçaroca de milho e um
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

/// O tabuleiro do Pomar: um match-3 clássico.
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
  final List<Produto?> casas;

  const Pomar({
    required this.linhas,
    required this.colunas,
    required this.casas,
  });

  int indice(int l, int c) => l * colunas + c;
  int linhaDe(int i) => i ~/ colunas;
  int colunaDe(int i) => i % colunas;

  Produto? em(int l, int c) =>
      (l < 0 || c < 0 || l >= linhas || c >= colunas) ? null : casas[indice(l, c)];

  Pomar comCasas(List<Produto?> novas) =>
      Pomar(linhas: linhas, colunas: colunas, casas: novas);

  /// Um tabuleiro pronto a jogar: sem trios já feitos e com pelo menos uma
  /// jogada possível.
  ///
  /// As duas condições contam. Começar com trios feitos dava pontos que a
  /// criança não ganhou; começar sem jogada possível dava um tabuleiro
  /// bloqueado logo à entrada, e ela não teria como saber que a culpa não
  /// era dela.
  factory Pomar.novo({
    int linhas = 8,
    int colunas = 7,
    Random? rnd,
  }) {
    final r = rnd ?? Random();
    for (var tentativa = 0; tentativa < 200; tentativa++) {
      var p = Pomar(
        linhas: linhas,
        colunas: colunas,
        casas: List.generate(
          linhas * colunas,
          (_) => Produto.values[r.nextInt(Produto.values.length)],
        ),
      );
      p = p._desfazerTriosIniciais(r);
      if (p.haJogada()) return p;
    }
    // Nunca deve chegar aqui com seis produtos num tabuleiro deste tamanho.
    return Pomar(
      linhas: linhas,
      colunas: colunas,
      casas: List.generate(
        linhas * colunas,
        (i) => Produto.values[(i + i ~/ colunas) % Produto.values.length],
      ),
    );
  }

  /// Troca produtos até não sobrar nenhum trio feito.
  Pomar _desfazerTriosIniciais(Random r) {
    var casas = List<Produto?>.from(this.casas);
    for (var volta = 0; volta < 60; volta++) {
      final grupos = comCasas(casas).grupos();
      if (grupos.isEmpty) break;
      for (final i in grupos) {
        casas[i] = Produto.values[r.nextInt(Produto.values.length)];
      }
    }
    return comCasas(casas);
  }

  /// Todas as casas que fazem parte de um trio ou mais, em linha ou coluna.
  Set<int> grupos() {
    final marcadas = <int>{};

    void varrer(bool horizontal) {
      final externo = horizontal ? linhas : colunas;
      final interno = horizontal ? colunas : linhas;
      for (var a = 0; a < externo; a++) {
        var inicio = 0;
        while (inicio < interno) {
          final actual = horizontal ? em(a, inicio) : em(inicio, a);
          var fim = inicio + 1;
          if (actual != null) {
            while (fim < interno &&
                (horizontal ? em(a, fim) : em(fim, a)) == actual) {
              fim++;
            }
          }
          if (actual != null && fim - inicio >= 3) {
            for (var k = inicio; k < fim; k++) {
              marcadas.add(horizontal ? indice(a, k) : indice(k, a));
            }
          }
          inicio = fim;
        }
      }
    }

    varrer(true);
    varrer(false);
    return marcadas;
  }

  bool saoVizinhas(int a, int b) {
    final dl = (linhaDe(a) - linhaDe(b)).abs();
    final dc = (colunaDe(a) - colunaDe(b)).abs();
    return dl + dc == 1;
  }

  /// O tabuleiro com duas casas trocadas, sem verificar nada.
  Pomar trocaCrua(int a, int b) {
    final novas = List<Produto?>.from(casas);
    final t = novas[a];
    novas[a] = novas[b];
    novas[b] = t;
    return comCasas(novas);
  }

  /// Uma troca só vale se for entre vizinhas e se formar um trio.
  ///
  /// Trocar sem formar nada é a regra que faz o jogo ser um jogo. Sem ela
  /// bastava arrastar tudo ao acaso até acontecer alguma coisa.
  bool podeTrocar(int a, int b) =>
      saoVizinhas(a, b) && trocaCrua(a, b).grupos().isNotEmpty;

  /// Há alguma troca que forme um trio?
  ///
  /// Sem esta pergunta, o tabuleiro podia ficar bloqueado sem ninguém dar
  /// por isso — e a criança ficava a arrastar peças à espera de algo que
  /// nunca ia acontecer.
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

  /// Tira do tabuleiro as casas colhidas, deixando buracos.
  Pomar colher(Set<int> quais) {
    final novas = List<Produto?>.from(casas);
    for (final i in quais) {
      novas[i] = null;
    }
    return comCasas(novas);
  }

  /// Faz cair o que está por cima dos buracos.
  Pomar assentar() {
    final novas = List<Produto?>.from(casas);
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
    final novas = List<Produto?>.from(casas);
    for (var i = 0; i < novas.length; i++) {
      novas[i] ??= Produto.values[r.nextInt(Produto.values.length)];
    }
    return comCasas(novas);
  }

  /// Baralha o tabuleiro mantendo os mesmos produtos.
  ///
  /// Usa-se quando não há jogada possível: em vez de acabar a partida por
  /// azar do tabuleiro, remexem-se as mesmas peças até haver saída.
  Pomar baralhar(Random r) {
    final produtos = casas.whereType<Produto>().toList();
    for (var tentativa = 0; tentativa < 80; tentativa++) {
      produtos.shuffle(r);
      final p = comCasas(List<Produto?>.from(produtos))
          ._desfazerTriosIniciais(r);
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
  /// É a mecânica que os jogos do género usam para premiar quem viu longe:
  /// a peça que cai e forma outro trio sozinha vale mais do que a que foi
  /// trocada à mão. Cresce em degraus fixos e não por multiplicação —
  /// multiplicar dava mil pontos numa jogada feliz e tornava as outras
  /// dezanove irrelevantes.
  static int premioDeCascata(int nivel) => nivel <= 1 ? 0 : (nivel - 1) * 50;

  /// O que a criança ouve, conforme o tamanho do feito.
  ///
  /// A escada existe porque é ela que faz querer jogar outra vez: chegar ao
  /// topo tem de ser raro e tem de se ouvir. Silêncio abaixo de cinco peças
  /// — uma voz a cada trio seria ruído em vez de prémio.
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
