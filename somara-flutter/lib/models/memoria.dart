import 'dart:math';

/// Que tipo de par se está a treinar.
///
/// O par nunca é igual a si mesmo, e é aí que está o valor. Virar duas
/// cartas com o mesmo desenho treina memória e mais nada; virar `7` e
/// sete maçãs obriga a **associar duas representações da mesma coisa** —
/// que é exactamente onde as crianças da 1ª e da 2ª classe tropeçam, e o
/// que a amarelinha treina mal.
enum Baralho {
  quantidade(
    'Contar',
    'Junta o número à quantidade certa',
    '1ª e 2ª classe',
  ),
  somas('Somas', 'Junta a conta ao resultado', '2ª e 3ª classe'),
  dobros('Dobros e metades', 'Junta cada conta ao seu número', '3ª e 4ª classe'),
  palavras('Palavras', 'Junta a palavra à coisa', '1ª e 2ª classe');

  final String rotulo;
  final String explica;

  /// Para quem serve. É a informação que diz a um pai se aquilo é para o
  /// filho, sem ter de o pôr a experimentar.
  final String classes;

  const Baralho(this.rotulo, this.explica, this.classes);
}

/// "1 tentativa", "2 tentativas".
///
/// Esteve "1 tentativas" no rodapé do jogo desde o primeiro dia. Numa app
/// que ensina a ler e a escrever, um plural mal feito é uma lição ao
/// contrário — e é para ali que a criança está a olhar.
String contagemDeTentativas(int n) =>
    n == 1 ? '1 tentativa' : '$n tentativas';

/// Uma carta: o que se vê, e a que par pertence.
class Carta {
  /// O texto ou os emoji na face.
  final String face;

  /// Cartas com o mesmo par casam entre si.
  final int par;

  /// Se a face é emoji repetido, convém desenhá-la mais pequena e em várias
  /// linhas — sete maçãs numa linha só não cabem numa carta.
  final bool eDesenho;

  const Carta({required this.face, required this.par, this.eDesenho = false});
}

/// O baralho de um jogo, já embaralhado.
class JogoDaMemoria {
  final Baralho baralho;
  final List<Carta> cartas;

  const JogoDaMemoria({required this.baralho, required this.cartas});

  int get pares => cartas.length ~/ 2;

  /// Quantas cartas por linha ficam bem para este número de cartas.
  int get colunas => cartas.length <= 12 ? 3 : 4;

  static const _frutas = ['🍎', '🍌', '🥭', '🥥', '🍅', '🌽'];

  /// Monta um jogo com [pares] pares.
  ///
  /// Nenhuma face se repete no tabuleiro, e a razão é mais subtil do que
  /// parece. Não basta recusar a mesma conta duas vezes: `3 + 4` e `2 + 5`
  /// são contas diferentes que dão **dois sete**. A criança juntava o `3 +
  /// 4` ao sete errado — um par que casa de facto — e o jogo recusava-lhe
  /// uma jogada certa, sem ela ter como perceber porquê.
  ///
  /// Por isso o que se guarda são as faces, não as contas.
  factory JogoDaMemoria.novo({
    required Baralho baralho,
    int pares = 6,
    Random? rnd,
  }) {
    final r = rnd ?? Random();
    final faces = <String>{};
    final cartas = <Carta>[];

    var tentativas = 0;
    while (cartas.length < pares * 2 && tentativas < 600) {
      tentativas++;
      final (esquerda, direita, _) = _fazerPar(baralho, r);
      if (faces.contains(esquerda.$1) || faces.contains(direita.$1)) continue;
      faces
        ..add(esquerda.$1)
        ..add(direita.$1);
      final n = cartas.length ~/ 2;
      cartas.add(Carta(face: esquerda.$1, par: n, eDesenho: esquerda.$2));
      cartas.add(Carta(face: direita.$1, par: n, eDesenho: direita.$2));
    }

    cartas.shuffle(r);
    return JogoDaMemoria(baralho: baralho, cartas: cartas);
  }

  /// Devolve (face esquerda, face direita, chave para não repetir).
  static ((String, bool), (String, bool), String) _fazerPar(
    Baralho b,
    Random r,
  ) {
    switch (b) {
      case Baralho.quantidade:
        final n = 1 + r.nextInt(9);
        final fruta = _frutas[r.nextInt(_frutas.length)];
        return (('$n', false), (fruta * n, true), 'q$n');

      case Baralho.somas:
        final a = 1 + r.nextInt(9);
        final c = 1 + r.nextInt(9);
        return (('$a + $c', false), ('${a + c}', false), 's$a+$c');

      case Baralho.dobros:
        final n = 1 + r.nextInt(10);
        // Metade só de números pares, senão a resposta não é inteira e a
        // criança desta idade ainda não viu fracções.
        final metade = r.nextBool() && n.isEven;
        return metade
            ? (('metade de $n', false), ('${n ~/ 2}', false), 'm$n')
            : (('dobro de $n', false), ('${n * 2}', false), 'd$n');

      case Baralho.palavras:
        const mapa = {
          'MANGA': '🥭', 'BANANA': '🍌', 'COCO': '🥥', 'MILHO': '🌽',
          'TOMATE': '🍅', 'PEIXE': '🐟', 'GATO': '🐈', 'CASA': '🏠',
          'SOL': '☀️', 'LIVRO': '📕', 'BOLA': '⚽', 'GALINHA': '🐔',
        };
        final chaves = mapa.keys.toList();
        final k = chaves[r.nextInt(chaves.length)];
        return ((k, false), (mapa[k]!, true), 'p$k');
    }
  }
}
