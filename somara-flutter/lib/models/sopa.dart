import 'dart:math';

import 'escadaria.dart';

/// Os conjuntos de palavras.
///
/// Todas sem acento nem cedilha, de propósito. Numa sopa de letras a grelha
/// não leva acentos, e mostrar "LEÃO" na lista para se procurar "LEAO" nas
/// letras ensinaria a escrever mal — numa app de escola isso não se faz.
/// Escolheram-se palavras que dispensam o problema.
enum Tema {
  casa('Em casa', [
    'LATA', 'MESA', 'CAMA', 'PORTA', 'BALDE', 'ESTEIRA', 'CADEIRA',
    'JANELA', 'TELHADO', 'CHAVE', 'PANO', 'VASSOURA', 'CANDEEIRO',
  ]),
  cozinha('Na cozinha', [
    'PANELA', 'PRATO', 'COLHER', 'SAL', 'ARROZ', 'OLEO', 'FARINHA',
    'COPO', 'FACA', 'GARFO', 'CHAVENA', 'FOGAO', 'PEIXE', 'CALDEIRAO',
  ]),
  escola('A escola', [
    'LIVRO', 'CADERNO', 'MESA', 'QUADRO', 'MOCHILA', 'ALUNO', 'ESCOLA',
    'LETRA', 'PALAVRA', 'PROFESSOR', 'TURMA', 'CANETA', 'BORRACHA', 'REGUA',
  ]),
  mercado('No mercado', [
    'BANANA', 'TOMATE', 'CARVAO', 'CAPULANA', 'METICAL', 'MANGA', 'COCO',
    'CEBOLA', 'BATATA', 'LARANJA', 'AMENDOIM', 'PAPAIA', 'CAJU', 'SACO',
  ]),
  transporte('Como se anda', [
    'CHAPA', 'BICICLETA', 'CAMIAO', 'BARCO', 'COMBOIO', 'ESTRADA',
    'CARRO', 'AVIAO', 'PONTE', 'RODA', 'MOTA', 'CARROCA',
  ]),
  animais('Animais', [
    'GATO', 'VACA', 'CABRA', 'GALINHA', 'PATO', 'PEIXE', 'ELEFANTE',
    'ZEBRA', 'MACACO', 'RATO', 'BURRO', 'COBRA', 'PORCO', 'CAVALO',
  ]),
  corpo('O corpo', [
    'PERNA', 'OLHO', 'NARIZ', 'BOCA', 'DEDO', 'COSTAS', 'OMBRO', 'JOELHO',
    'CABELO', 'DENTE', 'ORELHA', 'BARRIGA', 'TESTA', 'LINGUA',
  ]),
  campo('No campo', [
    'MACHAMBA', 'ENXADA', 'MILHO', 'MANDIOCA', 'CHUVA', 'SOL', 'ARVORE',
    'CAPIM', 'SEMENTE', 'HORTA', 'GADO', 'POCO', 'PALHA', 'BAMBU',
  ]),
  mocambique('Moçambique', [
    'MAPUTO', 'BEIRA', 'NAMPULA', 'NIASSA', 'TETE', 'LICHINGA', 'PEMBA',
    'QUELIMANE', 'INHAMBANE', 'ZAMBEZE', 'GAZA', 'SOFALA', 'MANICA',
    'CHIMOIO',
  ]);

  final String rotulo;
  final List<String> palavras;
  const Tema(this.rotulo, this.palavras);

  /// A categoria de um nível da escadaria.
  ///
  /// Determinada pelo número e não sorteada: o nível 47 tem de dar sempre a
  /// mesma categoria, senão dois telemóveis com a mesma criança mostravam
  /// sopas diferentes, e voltar a um nível já feito dava outra coisa.
  static Tema doNivel(int nivel) => values[(nivel - 1) % values.length];
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

/// "faltam 3", mas "falta 1" — o verbo também muda, não só o nome.
String quantasFaltam(int n) => n == 1 ? 'falta 1' : 'faltam $n';

/// Uma sopa de letras.
class Sopa {
  final int lado;

  /// As letras, lidas da esquerda para a direita e de cima para baixo.
  final List<String> letras;

  final List<PalavraColocada> escondidas;
  final Tema tema;

  /// O degrau da escadaria — de 1 a 1000.
  final int nivel;

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

  /// As direcções permitidas num nível.
  ///
  /// As diagonais e as palavras ao contrário ficam para mais tarde por uma
  /// razão concreta: uma criança que ainda lê letra a letra da esquerda
  /// para a direita não procura ao contrário — vê-se-lhe o dedo a seguir a
  /// linha. Pôr isso no nível 1 não é desafio, é um muro.
  static List<(int, int)> direccoesDe(ParamsSopa p) => [
    for (var i = 0; i < _direccoes.length; i++)
      if (_permitida(i, p)) _direccoes[i],
  ];

  static bool _permitida(int i, ParamsSopa p) {
    final diagonal = i == 2 || i == 3 || i == 6 || i == 7;
    final invertida = i >= 4;
    if (diagonal && !p.diagonais) return false;
    if (invertida && !p.invertidas) return false;
    return true;
  }

  static const _alfabeto = 'ABCDEFGHIJLMNOPQRSTUVXZ';

  /// Monta uma sopa com todas as palavras mesmo lá dentro.
  ///
  /// Nunca devolve uma grelha com uma palavra por colocar: uma criança que
  /// procura uma palavra que não existe procura para sempre, e conclui que
  /// o erro é dela. Se não couberem todas, tenta outra vez do princípio.
  /// A sopa de um degrau da escadaria.
  ///
  /// O nível manda em tudo: a categoria (fixa, para o mesmo nível dar sempre
  /// a mesma), o tamanho da grelha, quantas palavras se escondem e em que
  /// direcções.
  factory Sopa.doNivel(int nivel, {Random? rnd, Tema? tema}) {
    final p = sopaNo(nivel);
    final categoria = tema ?? Tema.doNivel(nivel);
    final r = rnd ?? Random();
    final direccoes = direccoesDe(p);

    for (var tentativa = 0; tentativa < 60; tentativa++) {
      final escolhidas = [...categoria.palavras]
        ..shuffle(r)
        ..removeWhere((w) => w.length > p.lado);
      final alvo = escolhidas.take(p.palavras).toList()
        // As compridas primeiro: são as difíceis de encaixar, e deixá-las
        // para o fim é a maneira certa de não caberem.
        ..sort((a, b) => b.length.compareTo(a.length));

      final letras = List.filled(p.lado * p.lado, '');
      final colocadas = <PalavraColocada>[];
      var falhou = false;

      for (final palavra in alvo) {
        final onde = _tentarColocar(palavra, letras, p.lado, direccoes, r);
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
        lado: p.lado,
        letras: letras,
        escondidas: colocadas,
        tema: categoria,
        nivel: nivel,
      );
    }

    // Rede de segurança: uma grelha só com a palavra mais curta. Nunca deve
    // chegar aqui, mas um ecrã vazio seria pior.
    final curta =
        categoria.palavras.reduce((a, b) => a.length <= b.length ? a : b);
    final letras = List.generate(
      p.lado * p.lado,
      (i) => i < curta.length ? curta[i] : _alfabeto[i % _alfabeto.length],
    );
    return Sopa(
      lado: p.lado,
      letras: letras,
      escondidas: [
        PalavraColocada(curta, List.generate(curta.length, (i) => i)),
      ],
      tema: categoria,
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
