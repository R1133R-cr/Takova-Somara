import 'dart:math';

/// Um puzzle de Crossmath: uma grelha 3×3 em que as contas têm de fechar
/// nas linhas **e** nas colunas ao mesmo tempo.
///
/// ```
///   0  +  1  =  2
///   +     +     +
///   3  +  4  =  5
///   =     =     =
///   6  +  7  =  8
/// ```
///
/// Porque é que isto entra numa app de escola: ao contrário das lições, que
/// tiveram de ser escritas uma a uma, estes puzzles **geram-se**. É conteúdo
/// sem fim para uma criança que já acabou a matéria do dia e quer continuar,
/// e treina a soma com dedução em vez de repetição.
///
/// A propriedade que faz o gerador ser simples: escolhidos os quatro valores
/// livres (0, 1, 3, 4), todo o resto fica determinado —
/// `2=0+1`, `5=3+4`, `6=0+3`, `7=1+4` — e a última linha e a última coluna
/// fecham sozinhas, porque `6+7 = (0+3)+(1+4) = (0+1)+(3+4) = 2+5`. Ou seja,
/// nenhuma grelha gerada assim pode sair inconsistente.
class Crossmath {
  /// Os nove valores, lidos da esquerda para a direita e de cima para baixo.
  final List<int> valores;

  /// Quais é que já vêm preenchidos. Os outros são para a criança descobrir.
  final List<bool> dadas;

  final Dificuldade dificuldade;

  const Crossmath({
    required this.valores,
    required this.dadas,
    required this.dificuldade,
  });

  /// As seis contas da grelha, como trios de índices (esquerda, direita,
  /// resultado). Três linhas e três colunas.
  static const equacoes = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), // linhas
    (0, 3, 6), (1, 4, 7), (2, 5, 8), // colunas
  ];

  /// Quantas casas a criança tem de descobrir.
  int get porDescobrir => dadas.where((d) => !d).length;

  /// Confere uma tentativa. Devolve os índices que estão errados — vazio
  /// quer dizer resolvido.
  ///
  /// Compara com a solução em vez de verificar as equações porque o puzzle
  /// é de solução única (garantido em [gerar]): havendo só uma resposta
  /// certa, dizer "esta casa está errada" é honesto e é o que ajuda.
  List<int> conferir(List<int?> tentativa) => [
    for (var i = 0; i < 9; i++)
      if (!dadas[i] && tentativa[i] != valores[i]) i,
  ];
}

enum Dificuldade {
  facil('Fácil', 20, 6),
  medio('Médio', 60, 5),
  dificil('Difícil', 150, 4);

  /// Nome a mostrar.
  final String rotulo;

  /// Valor máximo que a casa do canto (a maior de todas) pode ter. É o que
  /// separa a 1ª classe da 6ª: somar até 20 é outra coisa que somar até 150.
  final int tecto;

  /// Quantas casas ficam à vista. Menos pistas, mais dedução.
  ///
  /// Nunca menos de quatro, e não por gosto: cada casa é uma combinação
  /// linear dos quatro valores livres, portanto três pistas nunca chegam
  /// para os fixar. Um puzzle de três pistas tem sempre uma família de
  /// soluções — parece mais difícil e é apenas impossível.
  final int pistas;

  const Dificuldade(this.rotulo, this.tecto, this.pistas);
}

/// Gera puzzles com solução única.
///
/// A unicidade não é um pormenor: um puzzle com duas respostas certas dá
/// errado a uma criança que acertou. Numa app que ensina, isso é o pior
/// defeito possível — por isso cada puzzle é verificado por força bruta
/// antes de ser mostrado, e há um teste que percorre centenas deles.
class GeradorCrossmath {
  final Random _rnd;
  GeradorCrossmath([Random? rnd]) : _rnd = rnd ?? Random();

  /// Preenche a grelha a partir dos quatro valores livres.
  static List<int> grelhaDe(int a, int b, int d, int e) {
    final c = a + b;
    final f = d + e;
    final g = a + d;
    final h = b + e;
    return [a, b, c, d, e, f, g, h, c + f];
  }

  Crossmath gerar(Dificuldade dif) {
    // O canto de baixo à direita é a soma dos quatro livres, e é sempre o
    // maior número da grelha. Limitá-lo limita a grelha toda.
    final maxLivre = (dif.tecto / 4).floor().clamp(2, 99);

    for (var tentativa = 0; tentativa < 400; tentativa++) {
      final a = 1 + _rnd.nextInt(maxLivre);
      final b = 1 + _rnd.nextInt(maxLivre);
      final d = 1 + _rnd.nextInt(maxLivre);
      final e = 1 + _rnd.nextInt(maxLivre);
      final valores = grelhaDe(a, b, d, e);
      if (valores[8] > dif.tecto) continue;

      // Puzzles com valores todos iguais saem sem graça e sem dedução.
      if (valores.toSet().length < 5) continue;

      final dadas = _escolherPistas(valores, dif);
      if (dadas == null) continue;

      return Crossmath(valores: valores, dadas: dadas, dificuldade: dif);
    }

    // Rede de segurança: uma grelha conhecida, com os quatro cantos à vista.
    // Nunca deve chegar aqui, mas um ecrã em branco seria pior do que um
    // puzzle repetido.
    return Crossmath(
      valores: grelhaDe(8, 7, 1, 8),
      dadas: const [true, false, true, false, false, false, true, false, true],
      dificuldade: dif,
    );
  }

  /// Escolhe que casas ficam à vista, exigindo solução única.
  List<bool>? _escolherPistas(List<int> valores, Dificuldade dif) {
    for (var tentativa = 0; tentativa < 40; tentativa++) {
      final indices = List.generate(9, (i) => i)..shuffle(_rnd);
      final dadas = List.filled(9, false);
      for (final i in indices.take(dif.pistas)) {
        dadas[i] = true;
      }
      if (determinaSolucaoUnica(dadas)) return dadas;
    }
    return null;
  }

  /// Coeficientes de cada casa nos quatro valores livres (a, b, d, e).
  ///
  /// A grelha inteira é linear neles: `c = a+b`, `g = a+d`, e por aí fora.
  /// É isto que permite responder à unicidade com álgebra em vez de
  /// procura — e a diferença não é de estilo. Por procura, verificar um
  /// puzzle difícil eram vinte milhões de tentativas; assim são quatro
  /// linhas de eliminação de Gauss.
  static const _coeficientes = [
    [1, 0, 0, 0], // a
    [0, 1, 0, 0], // b
    [1, 1, 0, 0], // a+b
    [0, 0, 1, 0], // d
    [0, 0, 0, 1], // e
    [0, 0, 1, 1], // d+e
    [1, 0, 1, 0], // a+d
    [0, 1, 0, 1], // b+e
    [1, 1, 1, 1], // a+b+d+e
  ];

  /// Verdadeiro quando estas pistas fixam uma solução e uma só.
  ///
  /// As pistas dão um sistema linear nos quatro livres; a solução é única
  /// exactamente quando essas equações têm característica 4. Daí a regra
  /// de nunca haver menos de quatro pistas — e de não bastarem quatro
  /// quaisquer: os quatro cantos servem, mas uma linha inteira mais uma
  /// casa, por exemplo, não serve.
  static bool determinaSolucaoUnica(List<bool> dadas) {
    final linhas = <List<int>>[
      for (var i = 0; i < 9; i++)
        if (dadas[i]) List<int>.from(_coeficientes[i]),
    ];
    if (linhas.length < 4) return false;

    // Eliminação de Gauss sem divisões: os coeficientes são inteiros
    // pequenos e assim não há erro de vírgula flutuante a decidir se um
    // puzzle é válido.
    var posto = 0;
    for (var col = 0; col < 4 && posto < linhas.length; col++) {
      var pivo = -1;
      for (var r = posto; r < linhas.length; r++) {
        if (linhas[r][col] != 0) {
          pivo = r;
          break;
        }
      }
      if (pivo < 0) continue;
      final tmp = linhas[posto];
      linhas[posto] = linhas[pivo];
      linhas[pivo] = tmp;
      for (var r = posto + 1; r < linhas.length; r++) {
        if (linhas[r][col] == 0) continue;
        final k = linhas[r][col];
        final p = linhas[posto][col];
        for (var c = col; c < 4; c++) {
          linhas[r][c] = linhas[r][c] * p - linhas[posto][c] * k;
        }
      }
      posto++;
    }
    return posto == 4;
  }

  /// Conta grelhas válidas por força bruta. **Só para testes.**
  ///
  /// É a implementação obviamente correcta: percorre todas as grelhas
  /// possíveis e conta as que encaixam. Serve para confirmar que o teste
  /// de característica acima — o que a app usa, rápido mas menos óbvio —
  /// diz o mesmo. É lenta de propósito e não deve ir para o ecrã: com
  /// tecto 150 são milhões de tentativas por puzzle.
  static int contarSolucoes(List<int?> pistas, int tecto) {
    var encontradas = 0;
    for (var a = 1; a <= tecto; a++) {
      if (pistas[0] != null && pistas[0] != a) continue;
      for (var b = 1; a + b <= tecto; b++) {
        if (pistas[1] != null && pistas[1] != b) continue;
        if (pistas[2] != null && pistas[2] != a + b) continue;
        for (var d = 1; a + b + d <= tecto; d++) {
          if (pistas[3] != null && pistas[3] != d) continue;
          if (pistas[6] != null && pistas[6] != a + d) continue;
          for (var e = 1; a + b + d + e <= tecto; e++) {
            if (pistas[4] != null && pistas[4] != e) continue;
            if (pistas[5] != null && pistas[5] != d + e) continue;
            if (pistas[7] != null && pistas[7] != b + e) continue;
            if (pistas[8] != null && pistas[8] != a + b + d + e) continue;
            if (++encontradas >= 2) return encontradas;
          }
        }
      }
    }
    return encontradas;
  }
}
