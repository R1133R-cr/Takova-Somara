import 'dart:math';

import 'escadaria.dart';
import 'pomar.dart';

/// Joga o Pomar sozinho, para saber se o nível se ganha.
///
/// ## O que isto prova, e o que não prova
///
/// Prova que **um jogador razoável chega ao objectivo com as jogadas que
/// tem**. Não prova que o tabuleiro é bom, nem procura a melhor jogada: é
/// uma heurística gulosa — em cada jogada escolhe a troca que colhe mais
/// peças — e é de propósito. Se um jogador que nunca planeia consegue, uma
/// criança que planeia também consegue.
///
/// O contrário é o que interessa impedir: um nível em que nem o melhor
/// jogador do mundo chegava ao objectivo. Nesse caso a criança perde sem ter
/// feito nada de errado, e não tem como saber que a culpa não foi dela.
///
/// ## Porque é que o resultado não é uma certeza
///
/// As peças que caem para encher os buracos são sorteadas. O solucionador
/// não sabe quais vão sair na partida a sério — joga com o **seu** sorteio.
/// O que ele mede, portanto, é se o nível é ganhável com uma queda de peças
/// normal, e não com aquela queda em concreto. É quanto se pode saber sem
/// mentir, e chega: o que se está a excluir são níveis impossíveis por
/// parâmetros, não por azar de uma jogada.
class Solucionador {
  /// O resultado de uma simulação.
  static ResultadoDaSimulacao jogar(
    Pomar inicial,
    ParamsPomar params, {
    Random? rnd,
  }) {
    final r = rnd ?? Random();
    var tabuleiro = inicial;
    var colhidas = 0;
    var usadas = 0;

    while (usadas < params.jogadas && colhidas < params.objectivo) {
      final jogadas = tabuleiro.jogadasPossiveis();
      if (jogadas.isEmpty) {
        // Sem saída, o jogo baralha — é o que a partida a sério faz, e o
        // solucionador tem de fazer o mesmo, senão dizia "impossível" onde
        // a criança teria simplesmente continuado.
        tabuleiro = tabuleiro.baralhar(r);
        continue;
      }

      // A gulosa: a troca que colhe mais, contando o que as peças especiais
      // rebentam em cadeia.
      JogadaPossivel? melhor;
      var maior = -1;
      for (final j in jogadas) {
        final quantas = _quantoColhe(tabuleiro, j);
        if (quantas > maior) {
          maior = quantas;
          melhor = j;
        }
      }
      if (melhor == null) break;

      final (depois, apanhadas) = _fazer(tabuleiro, melhor, r);
      tabuleiro = depois;
      colhidas += apanhadas;
      usadas++;
    }

    return ResultadoDaSimulacao(
      ganhou: colhidas >= params.objectivo,
      colhidas: colhidas,
      jogadasUsadas: usadas,
      jogadasDadas: params.jogadas,
    );
  }

  /// Quantas peças esta troca colhe, só na primeira colheita.
  ///
  /// Não conta as cascatas: contá-las obrigava a simular as quedas, e a
  /// escolha mudava pouco por muito mais trabalho. A gulosa não precisa de
  /// ser esperta, precisa de ser rápida e honesta.
  static int _quantoColhe(Pomar t, JogadaPossivel j) {
    final doSol = t.colheitaDoSol(j.de, j.para);
    if (doSol != null) return t.detonar(doSol).length;
    final trocado = t.trocaCrua(j.de, j.para);
    final base = trocado.analisar(origem: j.para);
    return trocado.detonar(base.limpar).length;
  }

  /// Faz a jogada e resolve a cascata toda, como o ecrã faz.
  static (Pomar, int) _fazer(Pomar t, JogadaPossivel j, Random r) {
    var tabuleiro = t;
    var total = 0;

    final doSol = tabuleiro.colheitaDoSol(j.de, j.para);
    Set<int>? forcado = doSol;
    if (doSol == null) tabuleiro = tabuleiro.trocaCrua(j.de, j.para);

    var origem = j.para;
    // Vinte cascatas é muito mais do que alguma vez acontece; existe para
    // um erro num destes passos não dar um ciclo infinito dentro de um
    // teste que varre mil níveis.
    for (var passo = 0; passo < 20; passo++) {
      final Colheita colheita;
      if (forcado != null) {
        colheita = Colheita(limpar: tabuleiro.detonar(forcado), criar: const []);
        forcado = null;
      } else {
        final base = tabuleiro.analisar(origem: passo == 0 ? origem : null);
        if (base.vazia) break;
        colheita = Colheita(
          limpar: tabuleiro.detonar(base.limpar),
          criar: base.criar,
        );
      }
      if (colheita.vazia) break;

      total += colheita.limpar.length;
      tabuleiro = tabuleiro.colher(colheita).assentar().encher(r);
    }

    return (tabuleiro, total);
  }
}

/// O que aconteceu na simulação.
class ResultadoDaSimulacao {
  final bool ganhou;
  final int colhidas;
  final int jogadasUsadas;
  final int jogadasDadas;

  const ResultadoDaSimulacao({
    required this.ganhou,
    required this.colhidas,
    required this.jogadasUsadas,
    required this.jogadasDadas,
  });

  /// Que fatia das jogadas foi precisa. Um nível ganho à justa é um nível
  /// difícil de mais para quem não joga como uma máquina.
  double get folga =>
      jogadasDadas == 0 ? 1 : jogadasUsadas / jogadasDadas;

  @override
  String toString() => ganhou
      ? 'ganhou com $colhidas em $jogadasUsadas/$jogadasDadas jogadas'
      : 'perdeu com $colhidas de $jogadasDadas jogadas';
}

/// Quanta das jogadas dadas o solucionador pode gastar e o nível ainda
/// contar como ganhável.
///
/// Oitenta por cento, e a folga que sobra não é generosidade: o
/// solucionador joga sempre a melhor troca visível, e uma criança de nove
/// anos não. Um nível que a máquina fecha à justa é um nível que ela perde.
const folgaMaxima = 0.8;

/// Um tabuleiro do degrau [nivel], já provado ganhável.
///
/// Sorteia e simula. Se o jogador guloso não fechar o objectivo dentro da
/// [folgaMaxima], deita fora e sorteia outro. Ao fim de [tentativas]
/// entrega o melhor que apareceu — porque um tabuleiro difícil é melhor do
/// que um ecrã em branco, e porque a alternativa seria tentar para sempre
/// num nível cujos parâmetros não dão.
///
/// Não corre num isolate. Media-se: o pior nível fica muito abaixo dos
/// 300 ms que o §7 pedia, e há um teste que o mantém assim. Um isolate
/// custava serializar o tabuleiro nos dois sentidos por uma latência que
/// não existe.
({Pomar tabuleiro, ResultadoDaSimulacao prova}) pomarDoNivel(
  int nivel, {
  Random? rnd,
  int tentativas = 8,
}) {
  final p = pomarNo(nivel);
  final r = rnd ?? Random();

  ({Pomar tabuleiro, ResultadoDaSimulacao prova})? melhor;
  for (var t = 0; t < tentativas; t++) {
    final tabuleiro = Pomar.novo(
      linhas: p.linhas,
      colunas: p.colunas,
      produtos: p.produtos,
      rnd: r,
    );
    final prova = Solucionador.jogar(tabuleiro, p, rnd: r);
    if (prova.ganhou && prova.folga <= folgaMaxima) {
      return (tabuleiro: tabuleiro, prova: prova);
    }
    // Fica o que chegou mais longe: se nenhum servir, é este que se entrega.
    if (melhor == null || prova.colhidas > melhor.prova.colhidas) {
      melhor = (tabuleiro: tabuleiro, prova: prova);
    }
  }
  return melhor!;
}
