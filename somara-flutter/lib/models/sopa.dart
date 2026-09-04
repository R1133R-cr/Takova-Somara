import 'dart:math';

import 'escadaria.dart';
import 'rastreio.dart';

/// De onde vêm as palavras de uma sopa.
///
/// Ou de uma das categorias do dia-a-dia ([Tema]), ou do vocabulário de uma
/// unidade que a criança acabou de estudar. A sopa não sabe a diferença — e
/// é por isso que a segunda custou quase nada a fazer.
class Banco {
  final String rotulo;
  final List<String> palavras;
  const Banco(this.rotulo, this.palavras);

  /// Serve para uma sopa? Precisa de palavras que cheguem e que caibam.
  bool serve({int minimo = 4, int lado = 12}) =>
      palavras.where((p) => p.length <= lado).length >= minimo;
}

/// Tira os acentos e a cedilha, para a grelha.
///
/// A grelha é de maiúsculas simples — é assim em qualquer sopa de letras
/// impressa. A **lista** é que mostra a palavra bem escrita: "leão" na
/// lista, LEAO nas letras. É a ordem certa das duas coisas, e foi a que
/// aqui esteve trocada durante versões.
///
/// A regra anterior era "só entram palavras que dispensam acento", e ela
/// falhava por dois lados ao mesmo tempo: doze palavras do banco estavam
/// **escritas sem o acento que têm** — óleo, fogão, régua, camião, árvore,
/// poço — ou seja, a app ensinava a escrevê-las mal, que era exactamente o
/// que a regra dizia querer evitar; e o vocabulário das Ciências, que é
/// quase todo acentuado, ficava de fora da sopa da matéria.
String semAcento(String texto) {
  const de = 'ÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇáàâãäéèêëíìîïóòôõöúùûüç';
  const para = 'AAAAAEEEEIIIIOOOOOUUUUCaaaaaeeeeiiiiooooouuuuc';
  final b = StringBuffer();
  for (final ch in texto.split('')) {
    final i = de.indexOf(ch);
    b.write(i >= 0 ? para[i] : ch);
  }
  return b.toString();
}

/// Os conjuntos de palavras.
///
/// Escrevem-se **bem**, com acento e cedilha. O [semAcento] é que as prepara
/// para a grelha; a lista mostra-as como se escrevem.
enum Tema {
  casa('Em casa', [
    'LATA', 'MESA', 'CAMA', 'PORTA', 'BALDE', 'ESTEIRA', 'CADEIRA',
    'JANELA', 'TELHADO', 'CHAVE', 'PANO', 'VASSOURA', 'CANDEEIRO',
  ]),
  cozinha('Na cozinha', [
    'PANELA', 'PRATO', 'COLHER', 'SAL', 'ARROZ', 'ÓLEO', 'FARINHA',
    'COPO', 'FACA', 'GARFO', 'CHÁVENA', 'FOGÃO', 'PEIXE', 'CALDEIRÃO',
  ]),
  escola('A escola', [
    'LIVRO', 'CADERNO', 'MESA', 'QUADRO', 'MOCHILA', 'ALUNO', 'ESCOLA',
    'LETRA', 'PALAVRA', 'PROFESSOR', 'TURMA', 'CANETA', 'BORRACHA', 'RÉGUA',
  ]),
  mercado('No mercado', [
    'BANANA', 'TOMATE', 'CARVÃO', 'CAPULANA', 'METICAL', 'MANGA', 'COCO',
    'CEBOLA', 'BATATA', 'LARANJA', 'AMENDOIM', 'PAPAIA', 'CAJU', 'SACO',
  ]),
  transporte('Como se anda', [
    'CHAPA', 'BICICLETA', 'CAMIÃO', 'BARCO', 'COMBOIO', 'ESTRADA',
    'CARRO', 'AVIÃO', 'PONTE', 'RODA', 'MOTA', 'CARROÇA',
  ]),
  animais('Animais', [
    'GATO', 'VACA', 'CABRA', 'GALINHA', 'PATO', 'PEIXE', 'ELEFANTE',
    'ZEBRA', 'MACACO', 'RATO', 'BURRO', 'COBRA', 'PORCO', 'CAVALO',
  ]),
  corpo('O corpo', [
    'PERNA', 'OLHO', 'NARIZ', 'BOCA', 'DEDO', 'COSTAS', 'OMBRO', 'JOELHO',
    'CABELO', 'DENTE', 'ORELHA', 'BARRIGA', 'TESTA', 'LÍNGUA',
  ]),
  campo('No campo', [
    'MACHAMBA', 'ENXADA', 'MILHO', 'MANDIOCA', 'CHUVA', 'SOL', 'ÁRVORE',
    'CAPIM', 'SEMENTE', 'HORTA', 'GADO', 'POÇO', 'PALHA', 'BAMBU',
  ]),
  mocambique('Moçambique', [
    'MAPUTO', 'BEIRA', 'NAMPULA', 'NIASSA', 'TETE', 'LICHINGA', 'PEMBA',
    'QUELIMANE', 'INHAMBANE', 'ZAMBEZE', 'GAZA', 'SOFALA', 'MANICA',
    'CHIMOIO',
  ]);

  final String rotulo;
  final List<String> palavras;
  const Tema(this.rotulo, this.palavras);

  Banco get banco => Banco(rotulo, palavras);

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

  /// De onde saíram as palavras. Uma categoria do dia-a-dia ou o vocabulário
  /// de uma unidade — a sopa é a mesma.
  final Banco banco;

  /// O degrau da escadaria — de 1 a 1000.
  final int nivel;

  const Sopa({
    required this.lado,
    required this.letras,
    required this.escondidas,
    required this.banco,
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

  /// A sopa de um degrau da escadaria.
  ///
  /// O nível manda em tudo: a categoria (fixa, para o mesmo nível dar sempre
  /// a mesma), o tamanho da grelha, quantas palavras se escondem e em que
  /// direcções.
  factory Sopa.doNivel(int nivel, {Random? rnd, Tema? tema, Banco? banco}) {
    final p = sopaNo(nivel);
    return Sopa._montar(
      banco: banco ?? (tema ?? Tema.doNivel(nivel)).banco,
      lado: p.lado,
      quantas: p.palavras,
      direccoes: direccoesDe(p),
      nivel: nivel,
      r: rnd ?? Random(),
    );
  }

  /// A sopa do vocabulário de uma unidade.
  ///
  /// Não anda na escadaria: é sobre o que a criança acabou de estudar, e
  /// isso não tem degraus. A grelha nasce do banco — larga o suficiente para
  /// a palavra mais comprida caber — e as palavras nunca vão ao contrário:
  /// aqui o que se treina é reconhecer o vocabulário da matéria, e procurar
  /// ao espelho não treina isso.
  factory Sopa.daMateria(Banco banco, {Random? rnd}) {
    final maior = banco.palavras
        .map((w) => w.length)
        .reduce((a, b) => a > b ? a : b);
    final lado = (maior + 2).clamp(7, 14);
    final quantas = banco.palavras
        .where((w) => w.length <= lado)
        .length
        .clamp(1, 6);

    return Sopa._montar(
      banco: banco,
      lado: lado,
      quantas: quantas,
      direccoes: const [(0, 1), (1, 0), (1, 1)],
      // Zero quer dizer "fora da escadaria". É o que o ecrã lê para saber
      // que não há degrau seguinte a carregar.
      nivel: 0,
      r: rnd ?? Random(),
    );
  }

  /// Monta uma sopa com todas as palavras mesmo lá dentro.
  ///
  /// Nunca devolve uma grelha com uma palavra por colocar: uma criança que
  /// procura uma palavra que não existe procura para sempre, e conclui que o
  /// erro é dela. Se não couberem todas, tenta outra vez do princípio.
  static Sopa _montar({
    required Banco banco,
    required int lado,
    required int quantas,
    required List<(int, int)> direccoes,
    required int nivel,
    required Random r,
  }) {
    for (var tentativa = 0; tentativa < 60; tentativa++) {
      final escolhidas = [...banco.palavras]
        ..shuffle(r)
        ..removeWhere((w) => w.length > lado);
      final alvo = escolhidas.take(quantas).toList()
        // As compridas primeiro: são as difíceis de encaixar, e deixá-las
        // para o fim é a maneira certa de não caberem.
        ..sort((a, b) => b.length.compareTo(a.length));

      final letras = List.filled(lado * lado, '');
      final colocadas = <PalavraColocada>[];
      var falhou = false;

      for (final palavra in alvo) {
        // Na grelha entram as letras simples; a lista guarda a palavra como
        // ela se escreve.
        final nasLetras = semAcento(palavra);
        final casas = _tentarColocar(nasLetras, letras, lado, direccoes, r);
        if (casas == null) {
          falhou = true;
          break;
        }
        for (var k = 0; k < nasLetras.length; k++) {
          letras[casas[k]] = nasLetras[k];
        }
        colocadas.add(PalavraColocada(palavra, casas));
      }
      if (falhou) continue;

      for (var i = 0; i < letras.length; i++) {
        if (letras[i].isEmpty) {
          letras[i] = _alfabeto[r.nextInt(_alfabeto.length)];
        }
      }

      return Sopa(
        lado: lado,
        letras: letras,
        escondidas: colocadas,
        banco: banco,
        nivel: nivel,
      );
    }

    // Rede de segurança: uma grelha só com a palavra mais curta. Nunca deve
    // chegar aqui, mas um ecrã vazio seria pior.
    final curta =
        banco.palavras.reduce((a, b) => a.length <= b.length ? a : b);
    final simples = semAcento(curta);
    final letras = List.generate(
      lado * lado,
      (i) => i < simples.length ? simples[i] : _alfabeto[i % _alfabeto.length],
    );
    return Sopa(
      lado: lado,
      letras: letras,
      escondidas: [
        PalavraColocada(curta, List.generate(simples.length, (i) => i)),
      ],
      banco: banco,
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

  /// A palavra por encontrar em que o dedo menos passou.
  ///
  /// É o que a Sorte revela. Entre duas igualmente intocadas fica a mais
  /// comprida: se a criança não olhou para nenhuma das duas, a comprida é a
  /// que lhe custa mais a achar sozinha.
  PalavraColocada? menosTocada(Rastreio rastreio, Set<String> jaEncontradas) {
    final porAchar = [
      for (final p in escondidas)
        if (!jaEncontradas.contains(p.palavra)) p,
    ];
    if (porAchar.isEmpty) return null;
    return rastreio.menosTocado(
      porAchar,
      (p) => p.casas,
      desempate: (p) => p.palavra.length,
    );
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
