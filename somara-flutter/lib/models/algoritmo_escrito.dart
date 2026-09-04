/// As contas armadas, como se escrevem no caderno.
///
/// Este ficheiro não desenha nada e não sabe o que é um ecrã. O que faz é
/// dizer, para uma conta qualquer, **que casinhas existem, onde ficam, e o
/// que devia estar escrita em cada uma** — incluindo os transportes e os
/// empréstimos. O widget lê essa descrição e desenha-a.
///
/// ## Porque é que isto existe
///
/// Uma pergunta de escolha múltipla sobre 247 + 185 avalia se a criança
/// **sabe a resposta**. Não avalia nada do que a escola lhe está a ensinar,
/// que é o **método**: alinhar as ordens, somar coluna a coluna, e levar o
/// que passa de dez para a coluna seguinte. Uma criança pode acertar por
/// contagem nos dedos e continuar sem saber armar uma conta.
///
/// É por isso que o transporte é escrito pela criança e não desenhado pela
/// app. O "vai um" é o algoritmo; escondê-lo era ensinar metade.
library;

/// As quatro.
enum Operacao {
  adicao('+', 'mais'),
  subtraccao('−', 'menos'),
  multiplicacao('×', 'vezes'),
  divisao('÷', 'a dividir por');

  /// O sinal como aparece na grelha.
  final String sinal;

  /// Como se lê em voz alta.
  final String dito;

  const Operacao(this.sinal, this.dito);
}

/// Para que serve uma casinha.
enum Papel {
  /// Já vem escrita: um dígito de um operando, um sinal.
  fixa,

  /// O "vai um" da adição, ou o valor emprestado da subtracção.
  transporte,

  /// Um algarismo do resultado.
  resultado,

  /// Um algarismo de um produto parcial (multiplicação) ou do produto de um
  /// passo da divisão.
  produto,

  /// Um algarismo de um resto, na divisão.
  resto,

  /// Um algarismo do quociente.
  quociente,
}

/// Uma casinha da grelha.
class Casa {
  final int linha;
  final int coluna;
  final Papel papel;

  /// O que devia lá estar. Nas [Papel.fixa] é o que se mostra; nas outras é
  /// a resposta certa, que a criança não vê.
  final String texto;

  /// Dígito riscado, na subtracção: emprestou uma dezena à coluna da direita
  /// e já não vale o que lá está escrito. É assim que se faz no caderno, e
  /// riscar é o que torna visível que o número mudou.
  final bool riscado;

  const Casa({
    required this.linha,
    required this.coluna,
    required this.papel,
    required this.texto,
    this.riscado = false,
  });

  /// A criança tem de a preencher.
  bool get porPreencher => papel != Papel.fixa;

  /// Falhar esta casinha faz a resposta ficar errada.
  ///
  /// Os transportes ficam de fora de propósito: quem chega ao resultado
  /// certo fez a conta certa, mesmo que tenha somado o "vai um" de cabeça.
  /// Assinalam-se, para ela ver, mas não reprovam.
  bool get conta => porPreencher && papel != Papel.transporte;

  @override
  String toString() => 'Casa($linha,$coluna ${papel.name} "$texto")';
}

/// Uma conta armada, pronta a desenhar.
class GrelhaDaConta {
  final Operacao operacao;
  final int a;
  final int b;
  final int resultado;

  /// Resto da divisão. Zero nas outras.
  final int resto;

  final int linhas;
  final int colunas;
  final List<Casa> casas;

  /// As linhas por baixo das quais se desenha um traço, e até que coluna.
  final List<({int linha, int de, int ate})> tracos;

  /// A coluna da barra vertical da divisão. Nula nas outras operações.
  final int? barra;

  const GrelhaDaConta({
    required this.operacao,
    required this.a,
    required this.b,
    required this.resultado,
    required this.linhas,
    required this.colunas,
    required this.casas,
    required this.tracos,
    this.resto = 0,
    this.barra,
  });

  /// As casinhas que a criança tem de preencher, pela ordem em que se
  /// preenchem: **da direita para a esquerda e de cima para baixo**, que é a
  /// ordem do algoritmo.
  List<Casa> get aPreencher {
    final lista = casas.where((c) => c.porPreencher).toList()
      ..sort((x, y) {
        final l = x.linha.compareTo(y.linha);
        return l != 0 ? l : y.coluna.compareTo(x.coluna);
      });
    return lista;
  }

  Casa? em(int linha, int coluna) {
    for (final c in casas) {
      if (c.linha == linha && c.coluna == coluna) return c;
    }
    return null;
  }

  /// A conta ficou certa?
  ///
  /// [respostas] é indexada pela posição da casinha em [aPreencher].
  bool certa(List<String> respostas) {
    final alvo = aPreencher;
    for (var i = 0; i < alvo.length; i++) {
      if (!alvo[i].conta) continue;
      final dada = i < respostas.length ? respostas[i].trim() : '';
      if (dada != alvo[i].texto) return false;
    }
    return true;
  }

  /// O enunciado por extenso, para a voz e para o cabeçalho.
  String get dito => '$a ${operacao.dito} $b';

  /// Monta a grelha de uma conta.
  ///
  /// Lança se os números não servirem — uma subtracção que dá negativo ou
  /// uma divisão por zero não se armam, e é melhor rebentar aqui, num teste,
  /// do que desenhar uma conta impossível a uma criança.
  factory GrelhaDaConta.de(Operacao operacao, int a, int b) => switch (operacao) {
    Operacao.adicao => _adicao(a, b),
    Operacao.subtraccao => _subtraccao(a, b),
    Operacao.multiplicacao => _multiplicacao(a, b),
    Operacao.divisao => _divisao(a, b),
  };
}

List<int> _digitos(int n) =>
    n.abs().toString().split('').map(int.parse).toList();

/// Espalha um número por casinhas, alinhado à direita numa coluna final.
List<Casa> _numeroEm({
  required int valor,
  required int linha,
  required int fim,
  required Papel papel,
}) {
  final ds = _digitos(valor);
  return [
    for (var i = 0; i < ds.length; i++)
      Casa(
        linha: linha,
        coluna: fim - (ds.length - 1 - i),
        papel: papel,
        texto: '${ds[i]}',
      ),
  ];
}

// ---------------------------------------------------------------- adição

/// ```
///       ¹  ¹
///       2  4  7
///   +   1  8  5
///   ─────────────
///       4  3  2
/// ```
GrelhaDaConta _adicao(int a, int b) {
  if (a < 0 || b < 0) throw ArgumentError('a adição arma-se com positivos');
  final soma = a + b;
  final largura = [
    a.toString().length,
    b.toString().length,
    soma.toString().length,
  ].reduce((x, y) => x > y ? x : y);

  // Coluna 0 é a do sinal; as ordens ocupam 1..largura.
  final colunas = largura + 1;
  final fim = colunas - 1;

  // O transporte que entra em cada ordem, contado da direita para a
  // esquerda. É o "vai um": nasce numa coluna e escreve-se por cima da
  // seguinte, que é onde vai ser somado.
  final da = _digitos(a).reversed.toList();
  final db = _digitos(b).reversed.toList();
  final entra = List<int>.filled(largura + 1, 0);
  for (var o = 0; o < largura; o++) {
    final x = o < da.length ? da[o] : 0;
    final y = o < db.length ? db[o] : 0;
    entra[o + 1] = (x + y + entra[o]) >= 10 ? 1 : 0;
  }

  final casas = <Casa>[
    // Linha 0: os transportes, só onde existem.
    for (var o = 1; o <= largura; o++)
      if (entra[o] == 1)
        Casa(
          linha: 0,
          coluna: fim - o,
          papel: Papel.transporte,
          texto: '1',
        ),
    ..._numeroEm(valor: a, linha: 1, fim: fim, papel: Papel.fixa),
    const Casa(
      linha: 2,
      coluna: 0,
      papel: Papel.fixa,
      texto: '+',
    ),
    ..._numeroEm(valor: b, linha: 2, fim: fim, papel: Papel.fixa),
    ..._numeroEm(valor: soma, linha: 3, fim: fim, papel: Papel.resultado),
  ];

  return GrelhaDaConta(
    operacao: Operacao.adicao,
    a: a,
    b: b,
    resultado: soma,
    linhas: 4,
    colunas: colunas,
    casas: casas,
    tracos: [(linha: 2, de: 0, ate: fim)],
  );
}

// ------------------------------------------------------------ subtracção

/// ```
///       5  ¹4  ¹3
///       6   4   3
///   −   2   8   7
///   ──────────────
///       3   5   6
/// ```
///
/// A casinha de cima leva o valor que a ordem passa a ter: `13` numa que
/// pediu emprestado, `5` numa que emprestou. É o que se escreve no caderno,
/// e a criança escreve o mesmo.
GrelhaDaConta _subtraccao(int a, int b) {
  if (b > a) {
    throw ArgumentError('$a − $b dá negativo: não se arma no 1º ciclo');
  }
  final dif = a - b;
  final largura = a.toString().length;
  final colunas = largura + 1;
  final fim = colunas - 1;

  final da = _digitos(a).reversed.toList();
  final db = _digitos(b).reversed.toList();

  // Percorre as ordens da direita para a esquerda a marcar quem pediu e quem
  // emprestou. Uma ordem pode fazer as duas coisas — em 600 − 1, a das
  // dezenas pede à das centenas e empresta à das unidades.
  final pediu = List<bool>.filled(largura, false);
  final emprestou = List<bool>.filled(largura, false);
  var levar = 0;
  for (var o = 0; o < largura; o++) {
    final x = da[o] - levar;
    final y = o < db.length ? db[o] : 0;
    if (o > 0 && levar > 0) emprestou[o] = true;
    if (x < y) {
      pediu[o] = true;
      levar = 1;
    } else {
      levar = 0;
    }
  }
  final casas = <Casa>[
    for (var o = 0; o < largura; o++)
      if (pediu[o] || emprestou[o])
        Casa(
          linha: 0,
          coluna: fim - o,
          papel: Papel.transporte,
          texto: '${da[o] - (emprestou[o] ? 1 : 0) + (pediu[o] ? 10 : 0)}',
        ),
    // Os dígitos que mudaram ficam riscados, como no caderno.
    for (var o = 0; o < largura; o++)
      Casa(
        linha: 1,
        coluna: fim - o,
        papel: Papel.fixa,
        texto: '${da[o]}',
        riscado: pediu[o] || emprestou[o],
      ),
    const Casa(linha: 2, coluna: 0, papel: Papel.fixa, texto: '−'),
    ..._numeroEm(valor: b, linha: 2, fim: fim, papel: Papel.fixa),
    ..._numeroEm(valor: dif, linha: 3, fim: fim, papel: Papel.resultado),
  ];

  return GrelhaDaConta(
    operacao: Operacao.subtraccao,
    a: a,
    b: b,
    resultado: dif,
    linhas: 4,
    colunas: colunas,
    casas: casas,
    tracos: [(linha: 2, de: 0, ate: fim)],
  );
}

// --------------------------------------------------------- multiplicação

/// ```
///          2  4
///   ×      1  3
///   ──────────────
///          7  2     ← 24 × 3
///       2  4  ·     ← 24 × 1, deslocado
///   ──────────────
///       3  1  2
/// ```
///
/// Os produtos parciais são o que a multiplicação tem de próprio: sem eles,
/// a criança escreve um número e ninguém sabe como lá chegou.
GrelhaDaConta _multiplicacao(int a, int b) {
  if (a < 0 || b < 0) {
    throw ArgumentError('a multiplicação arma-se com positivos');
  }
  final produto = a * b;
  final db = _digitos(b).reversed.toList();
  final parciais = [for (var k = 0; k < db.length; k++) a * db[k]];

  final largura = [
    a.toString().length,
    b.toString().length,
    produto.toString().length,
    for (var k = 0; k < parciais.length; k++)
      parciais[k].toString().length + k,
  ].reduce((x, y) => x > y ? x : y);

  final colunas = largura + 1;
  final fim = colunas - 1;

  final casas = <Casa>[
    ..._numeroEm(valor: a, linha: 0, fim: fim, papel: Papel.fixa),
    const Casa(linha: 1, coluna: 0, papel: Papel.fixa, texto: '×'),
    ..._numeroEm(valor: b, linha: 1, fim: fim, papel: Papel.fixa),
  ];
  final tracos = <({int linha, int de, int ate})>[
    (linha: 1, de: 0, ate: fim),
  ];

  // Com um só algarismo no multiplicador não há produtos parciais: o
  // primeiro produto JÁ é o resultado, e escrevê-lo duas vezes ensinava um
  // passo que não existe.
  if (parciais.length == 1) {
    casas.addAll(
      _numeroEm(valor: produto, linha: 2, fim: fim, papel: Papel.resultado),
    );
    return GrelhaDaConta(
      operacao: Operacao.multiplicacao,
      a: a,
      b: b,
      resultado: produto,
      linhas: 3,
      colunas: colunas,
      casas: casas,
      tracos: tracos,
    );
  }

  var linha = 2;
  for (var k = 0; k < parciais.length; k++) {
    casas.addAll(
      _numeroEm(
        valor: parciais[k],
        linha: linha,
        fim: fim - k,
        papel: Papel.produto,
      ),
    );
    // O ponto que marca o deslocamento. Sem ele a criança não vê porque é
    // que o segundo produto começa mais à esquerda.
    for (var p = 0; p < k; p++) {
      casas.add(
        Casa(
          linha: linha,
          coluna: fim - p,
          papel: Papel.fixa,
          texto: '·',
        ),
      );
    }
    linha++;
  }

  tracos.add((linha: linha - 1, de: 0, ate: fim));
  casas.addAll(
    _numeroEm(valor: produto, linha: linha, fim: fim, papel: Papel.resultado),
  );

  return GrelhaDaConta(
    operacao: Operacao.multiplicacao,
    a: a,
    b: b,
    resultado: produto,
    linhas: linha + 1,
    colunas: colunas,
    casas: casas,
    tracos: tracos,
  );
}

// ---------------------------------------------------------------- divisão

/// ```
///      1  4  4  │  1  2
///   −  1  2     │ ─────
///   ─────────   │  1  2
///         2  4  │
///      −  2  4  │
///      ─────────│
///            0  │
/// ```
///
/// A mais difícil das quatro, e a única em que a criança escreve três coisas
/// diferentes: o quociente, cada produto e cada resto.
GrelhaDaConta _divisao(int a, int b) {
  if (b <= 0) throw ArgumentError('não se divide por $b');
  if (a < 0) throw ArgumentError('a divisão arma-se com positivos');

  final da = _digitos(a);
  final larguraEsq = da.length;

  // A barra fica logo a seguir ao dividendo; à direita ficam o divisor e o
  // quociente, um por cima do outro.
  final barra = larguraEsq + 1;
  final larguraDir =
      b.toString().length > (a ~/ b).toString().length
      ? b.toString().length
      : (a ~/ b).toString().length;
  final colunas = barra + 1 + larguraDir;
  final fimEsq = larguraEsq; // coluna 0 é a do sinal −
  final fimDir = colunas - 1;

  final quociente = a ~/ b;
  final casas = <Casa>[
    ..._numeroEm(valor: a, linha: 0, fim: fimEsq, papel: Papel.fixa),
    ..._numeroEm(valor: b, linha: 0, fim: fimDir, papel: Papel.fixa),
    ..._numeroEm(valor: quociente, linha: 2, fim: fimDir, papel: Papel.quociente),
  ];
  final tracos = <({int linha, int de, int ate})>[
    (linha: 0, de: barra + 1, ate: fimDir),
  ];

  // Os passos: baixa-se um algarismo de cada vez, e só há passo quando o
  // valor corrente já chega para o divisor. Os zeros à esquerda do
  // quociente não geram linha nenhuma — no caderno também não geram.
  var corrente = 0;
  var linha = 1;
  for (var i = 0; i < da.length; i++) {
    corrente = corrente * 10 + da[i];
    if (corrente < b) continue;

    final qd = corrente ~/ b;
    final produto = qd * b;
    final resto = corrente - produto;

    casas
      ..add(Casa(linha: linha, coluna: 0, papel: Papel.fixa, texto: '−'))
      ..addAll(
        _numeroEm(
          valor: produto,
          linha: linha,
          fim: 1 + i,
          papel: Papel.produto,
        ),
      );
    tracos.add((linha: linha, de: 0, ate: 1 + i));
    linha++;

    // O resto, e ao lado o algarismo que se baixa a seguir.
    final ultimo = i == da.length - 1;
    casas.addAll(
      _numeroEm(valor: resto, linha: linha, fim: 1 + i, papel: Papel.resto),
    );
    if (!ultimo) {
      casas.add(
        Casa(
          linha: linha,
          coluna: 2 + i,
          papel: Papel.fixa,
          texto: '${da[i + 1]}',
        ),
      );
    }
    linha++;
    corrente = resto;
  }

  return GrelhaDaConta(
    operacao: Operacao.divisao,
    a: a,
    b: b,
    resultado: quociente,
    resto: a % b,
    // O quociente vive na linha 2. Numa divisão sem passo nenhum — 3 a
    // dividir por 5 — a grelha tinha só uma linha e ele ficava de fora.
    linhas: linha < 3 ? 3 : linha,
    colunas: colunas,
    casas: casas,
    tracos: tracos,
    barra: barra,
  );
}
