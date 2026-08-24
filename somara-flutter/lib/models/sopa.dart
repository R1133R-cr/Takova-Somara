import 'dart:math';

/// Os conjuntos de palavras.
///
/// Todas sem acento nem cedilha, de propósito. Numa sopa de letras a grelha
/// não leva acentos, e mostrar "LEÃO" na lista para se procurar "LEAO" nas
/// letras ensinaria a escrever mal — numa app de escola isso não se faz.
/// Escolheram-se palavras que dispensam o problema.
enum Tema {
  animais('Animais', [
    'GATO', 'VACA', 'CABRA', 'GALINHA', 'PATO', 'PEIXE', 'ELEFANTE',
    'ZEBRA', 'MACACO', 'RATO', 'BURRO', 'COBRA', 'PORCO', 'CAVALO',
  ]),
  frutas('Frutas e legumes', [
    'MANGA', 'BANANA', 'COCO', 'MILHO', 'TOMATE', 'LARANJA', 'PAPAIA',
    'CAJU', 'AMENDOIM', 'ABACATE', 'MELANCIA', 'CEBOLA', 'BATATA', 'ARROZ',
  ]),
  escola('A escola', [
    'LIVRO', 'CADERNO', 'MESA', 'QUADRO', 'MOCHILA', 'ALUNO', 'ESCOLA',
    'LETRA', 'PALAVRA', 'PROFESSOR', 'TURMA', 'CANETA', 'BORRACHA', 'REGUA',
  ]),
  corpo('O corpo', [
    'PERNA', 'OLHO', 'NARIZ', 'BOCA', 'DEDO', 'COSTAS', 'OMBRO', 'JOELHO',
    'CABELO', 'DENTE', 'ORELHA', 'BARRIGA', 'TESTA', 'LINGUA',
  ]),
  mocambique('Moçambique', [
    'MAPUTO', 'BEIRA', 'NAMPULA', 'NIASSA', 'TETE', 'LICHINGA', 'PEMBA',
    'QUELIMANE', 'INHAMBANE', 'ZAMBEZE', 'GAZA', 'SOFALA', 'MANICA',
    'CHIMOIO',
  ]);

  final String rotulo;
  final List<String> palavras;
  const Tema(this.rotulo, this.palavras);
}

/// A dificuldade muda três coisas ao mesmo tempo: o tamanho da grelha,
/// quantas palavras se escondem, e em que direcções.
///
/// As diagonais e as palavras ao contrário ficam para os níveis de cima por
/// uma razão concreta: uma criança da 1ª classe que ainda lê letra a letra
/// da esquerda para a direita não procura ao contrário — vê-se-lhe o dedo a
/// seguir a linha. Pôr isso no primeiro nível não é desafio, é um muro.
enum NivelSopa {
  facil('Fácil', 8, 5, false, false),
  medio('Médio', 10, 7, true, false),
  dificil('Difícil', 12, 8, true, true);

  final String rotulo;
  final int lado;
  final int quantasPalavras;
  final bool comDiagonais;
  final bool comInvertidas;

  const NivelSopa(
    this.rotulo,
    this.lado,
    this.quantasPalavras,
    this.comDiagonais,
    this.comInvertidas,
  );
}

/// Uma palavra escondida na grelha, e onde ficou.
class PalavraColocada {
  final String palavra;

  /// Os índices das casas, na ordem em que se lê a palavra.
  final List<int> casas;

  const PalavraColocada(this.palavra, this.casas);

  /// A mesma palavra lida ao contrário serve — a criança pode arrastar de
  /// qualquer uma das pontas, e obrigá-la a adivinhar em que ponta começar
  /// seria um castigo por nada.
  bool correspondeA(List<int> seleccao) {
    if (seleccao.length != casas.length) return false;
    final igual = List.generate(casas.length, (i) => casas[i] == seleccao[i]);
    if (!igual.contains(false)) return true;
    final aoContrario = seleccao.reversed.toList();
    for (var i = 0; i < casas.length; i++) {
      if (casas[i] != aoContrario[i]) return false;
    }
    return true;
  }
}

/// Uma sopa de letras.
class Sopa {
  final int lado;

  /// As letras, lidas da esquerda para a direita e de cima para baixo.
  final List<String> letras;

  final List<PalavraColocada> escondidas;
  final Tema tema;
  final NivelSopa nivel;

  const Sopa({
    required this.lado,
    required this.letras,
    required this.escondidas,
    required this.tema,
    required this.nivel,
  });

  int indice(int l, int c) => l * lado + c;
  int linhaDe(int i) => i ~/ lado;
  int colunaDe(int i) => i % lado;
  bool dentro(int l, int c) => l >= 0 && c >= 0 && l < lado && c < lado;

  /// A palavra que esta selecção acerta, se acertar alguma.
  PalavraColocada? acertaEm(List<int> seleccao) {
    for (final p in escondidas) {
      if (p.correspondeA(seleccao)) return p;
    }
    return null;
  }

  /// As oito direcções possíveis, como (deltaLinha, deltaColuna).
  static const _direccoes = [
    (0, 1), (1, 0), (1, 1), (1, -1),
    (0, -1), (-1, 0), (-1, -1), (-1, 1),
  ];

  static List<(int, int)> direccoesDe(NivelSopa n) => [
    for (var i = 0; i < _direccoes.length; i++)
      if (_permitida(i, n)) _direccoes[i],
  ];

  static bool _permitida(int i, NivelSopa n) {
    final diagonal = i == 2 || i == 3 || i == 6 || i == 7;
    final invertida = i >= 4;
    if (diagonal && !n.comDiagonais) return false;
    if (invertida && !n.comInvertidas) return false;
    return true;
  }

  static const _alfabeto = 'ABCDEFGHIJLMNOPQRSTUVXZ';

  /// Monta uma sopa com todas as palavras mesmo lá dentro.
  ///
  /// Nunca devolve uma grelha com uma palavra por colocar: uma criança que
  /// procura uma palavra que não existe procura para sempre, e conclui que
  /// o erro é dela. Se não couberem todas, tenta outra vez do princípio.
  factory Sopa.nova({
    required Tema tema,
    required NivelSopa nivel,
    Random? rnd,
  }) {
    final r = rnd ?? Random();
    final direccoes = direccoesDe(nivel);

    for (var tentativa = 0; tentativa < 60; tentativa++) {
      final escolhidas = [...tema.palavras]
        ..shuffle(r)
        ..removeWhere((p) => p.length > nivel.lado);
      final alvo = escolhidas.take(nivel.quantasPalavras).toList()
        // As compridas primeiro: são as difíceis de encaixar, e deixá-las
        // para o fim é a maneira certa de não caberem.
        ..sort((a, b) => b.length.compareTo(a.length));

      final letras = List.filled(nivel.lado * nivel.lado, '');
      final colocadas = <PalavraColocada>[];
      var falhou = false;

      for (final palavra in alvo) {
        final onde = _tentarColocar(palavra, letras, nivel.lado, direccoes, r);
        if (onde == null) {
          falhou = true;
          break;
        }
        for (var k = 0; k < palavra.length; k++) {
          letras[onde[k]] = palavra[k];
        }
        colocadas.add(PalavraColocada(palavra, onde));
      }
      if (falhou) continue;

      for (var i = 0; i < letras.length; i++) {
        if (letras[i].isEmpty) {
          letras[i] = _alfabeto[r.nextInt(_alfabeto.length)];
        }
      }

      return Sopa(
        lado: nivel.lado,
        letras: letras,
        escondidas: colocadas,
        tema: tema,
        nivel: nivel,
      );
    }

    // Rede de segurança: uma grelha só com a palavra mais curta. Nunca deve
    // chegar aqui, mas um ecrã vazio seria pior.
    final curta = tema.palavras.reduce((a, b) => a.length <= b.length ? a : b);
    final letras = List.generate(
      nivel.lado * nivel.lado,
      (i) => i < curta.length ? curta[i] : _alfabeto[i % _alfabeto.length],
    );
    return Sopa(
      lado: nivel.lado,
      letras: letras,
      escondidas: [
        PalavraColocada(curta, List.generate(curta.length, (i) => i)),
      ],
      tema: tema,
      nivel: nivel,
    );
  }

  /// Procura um sítio onde a palavra caiba, cruzando-se com as que já lá
  /// estão sempre que as letras coincidirem.
  static List<int>? _tentarColocar(
    String palavra,
    List<String> letras,
    int lado,
    List<(int, int)> direccoes,
    Random r,
  ) {
    final ordem = [
      for (var i = 0; i < lado * lado; i++) i,
    ]..shuffle(r);

    for (final inicio in ordem) {
      final dirs = [...direccoes]..shuffle(r);
      for (final (dl, dc) in dirs) {
        final l0 = inicio ~/ lado, c0 = inicio % lado;
        final casas = <int>[];
        var cabe = true;

        for (var k = 0; k < palavra.length; k++) {
          final l = l0 + dl * k, c = c0 + dc * k;
          if (l < 0 || c < 0 || l >= lado || c >= lado) {
            cabe = false;
            break;
          }
          final i = l * lado + c;
          // Cruzar com outra palavra é bom — é o que torna a sopa densa.
          // Mas só onde a letra for exactamente a mesma.
          if (letras[i].isNotEmpty && letras[i] != palavra[k]) {
            cabe = false;
            break;
          }
          casas.add(i);
        }
        if (cabe) return casas;
      }
    }
    return null;
  }

  /// A linha recta entre duas casas, ou nulo se não estiverem alinhadas.
  ///
  /// É o que valida o arrasto: numa sopa de letras só valem linhas — a
  /// horizontal, a vertical e as duas diagonais. Um dedo que vá aos saltos
  /// não deve seleccionar nada.
  List<int>? linhaEntre(int de, int ate) {
    final l0 = linhaDe(de), c0 = colunaDe(de);
    final l1 = linhaDe(ate), c1 = colunaDe(ate);
    final dl = l1 - l0, dc = c1 - c0;

    if (dl == 0 && dc == 0) return [de];
    final alinhada = dl == 0 || dc == 0 || dl.abs() == dc.abs();
    if (!alinhada) return null;

    final passos = max(dl.abs(), dc.abs());
    final pl = dl.sign, pc = dc.sign;
    return [
      for (var k = 0; k <= passos; k++) indice(l0 + pl * k, c0 + pc * k),
    ];
  }
}
