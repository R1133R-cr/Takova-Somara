import 'dart:math' as math;

/// As duas moedas da Somara.
///
/// Duas e não uma porque fazem trabalhos diferentes. O **Ouro** entra todos
/// os dias e sai depressa — é troco, serve para comprar minutos de jogo. O
/// **Cristal** é raro e guarda-se: é com ele que se compra uma cara nova do
/// Roby, e uma cara nova só tem valor se tiver custado alguma coisa.
///
/// Se houvesse uma moeda só, uma das duas coisas ficava estragada: ou os
/// minutos custavam tanto que ninguém os comprava, ou as caras custavam tão
/// pouco que se tinham todas na primeira semana.
enum Moeda {
  gc('GC', 'Ouro', 'moedas de ouro'),
  cc('CC', 'Cristal', 'cristais');

  /// A sigla, como aparece ao lado do número.
  final String sigla;

  /// O nome no singular.
  final String nome;

  /// Como se diz no plural, dentro de uma frase.
  final String plural;

  const Moeda(this.sigla, this.nome, this.plural);
}

/// O que a criança tem, e o que já ganhou e gastou.
///
/// Guardam-se os **quatro totais** e não os dois saldos, pela mesma razão da
/// [BolsaDeTempo]: é o que permite juntar dois telemóveis sem inventar nem
/// apagar dinheiro. Ficar pelo maior saldo dava a quem tivesse dois
/// aparelhos uma máquina de fabricar cristais — gastava-os num, entrava na
/// conta no outro, e voltavam.
class Carteira {
  final int ganhoGc;
  final int gastoGc;
  final int ganhoCc;
  final int gastoCc;

  const Carteira({
    this.ganhoGc = 0,
    this.gastoGc = 0,
    this.ganhoCc = 0,
    this.gastoCc = 0,
  });

  int get gc => ganhoGc - gastoGc;
  int get cc => ganhoCc - gastoCc;

  int quanto(Moeda m) => m == Moeda.gc ? gc : cc;

  bool chegaPara(Moeda m, int preco) => quanto(m) >= preco;

  Carteira comGanho(Moeda m, int quanto) {
    final q = math.max(0, quanto);
    return m == Moeda.gc
        ? Carteira(
            ganhoGc: ganhoGc + q,
            gastoGc: gastoGc,
            ganhoCc: ganhoCc,
            gastoCc: gastoCc,
          )
        : Carteira(
            ganhoGc: ganhoGc,
            gastoGc: gastoGc,
            ganhoCc: ganhoCc + q,
            gastoCc: gastoCc,
          );
  }

  /// Paga, se chegar. Devolve nulo quando não chega — quem chama tem de
  /// decidir o que dizer, e não há compra a meio.
  Carteira? comGasto(Moeda m, int preco) {
    if (preco <= 0 || !chegaPara(m, preco)) return null;
    return m == Moeda.gc
        ? Carteira(
            ganhoGc: ganhoGc,
            gastoGc: gastoGc + preco,
            ganhoCc: ganhoCc,
            gastoCc: gastoCc,
          )
        : Carteira(
            ganhoGc: ganhoGc,
            gastoGc: gastoGc,
            ganhoCc: ganhoCc,
            gastoCc: gastoCc + preco,
          );
  }

  /// O ouro que um nível de lição rende: 5 se se acertou pouco, 15 se se
  /// acertou tudo.
  ///
  /// Nunca zero, nem no pior resultado. Uma criança que tropeçou num nível
  /// difícil já teve o castigo de o ter tropeçado; sair de lá sem nada era
  /// dizer-lhe que a meia hora não valeu de nada.
  static int ouroPorNivel(int percentagem) =>
      5 + (percentagem.clamp(0, 100) / 10).round();

  /// Um cristal por unidade fechada sem um único erro.
  static const cristalPorUnidadePerfeita = 1;

  /// Um cristal por cada sete dias seguidos de estudo.
  static const cristalPorSemanaSeguida = 1;

  Map<String, dynamic> paraJson() => {
    'ganhoGc': ganhoGc,
    'gastoGc': gastoGc,
    'ganhoCc': ganhoCc,
    'gastoCc': gastoCc,
  };

  static Carteira deJson(Map<String, dynamic>? j) {
    if (j == null) return const Carteira();
    int ler(String k) => math.max(0, (j[k] as num?)?.toInt() ?? 0);
    return Carteira(
      ganhoGc: ler('ganhoGc'),
      gastoGc: ler('gastoGc'),
      ganhoCc: ler('ganhoCc'),
      gastoCc: ler('gastoCc'),
    );
  }

  /// Fica pelo maior de cada um dos quatro totais.
  ///
  /// O que se ganhou noutro telemóvel conta, e o que lá se gastou também.
  Carteira fundirCom(Carteira outra) => Carteira(
    ganhoGc: math.max(ganhoGc, outra.ganhoGc),
    gastoGc: math.max(gastoGc, outra.gastoGc),
    ganhoCc: math.max(ganhoCc, outra.ganhoCc),
    gastoCc: math.max(gastoCc, outra.gastoCc),
  );

  @override
  String toString() => 'Carteira($gc GC, $cc CC)';
}
