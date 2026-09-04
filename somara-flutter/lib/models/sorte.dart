import 'dart:math' as math;

/// As sortes: a ajuda que se ganha a estudar e se gasta a jogar.
///
/// É a ponte que faltava entre as duas metades da app. As moedas pagam
/// enfeites; a Sorte paga **ajuda dentro do jogo** — e a única maneira de a
/// ter é acabar uma lição sem um único erro. Uma criança encalhada no Pomar
/// tem, à distância de uma lição, uma saída que não é desistir.
///
/// ## Porquê um tecto
///
/// Cinco, e as que se ganham a mais perdem-se. Sem tecto, quem estudasse
/// duas semanas entrava no Pomar com cinquenta sortes e o jogo deixava de
/// ser um jogo. A ajuda só vale enquanto for escassa — e ela sabe disso.
class Sortes {
  /// Quantas já se ganharam ao todo. Nunca passa de [gastas] + [tecto]: o
  /// tecto morde na hora de ganhar e não na de mostrar, senão gastar cinco
  /// fazia reaparecer as que já se tinham perdido.
  final int ganhas;

  /// Quantas já se gastaram ao todo.
  final int gastas;

  const Sortes({this.ganhas = 0, this.gastas = 0});

  /// O máximo que se pode ter guardado ao mesmo tempo.
  static const tecto = 5;

  /// O que rende uma lição fechada sem um único erro.
  static const porLicaoPerfeita = 1;

  int get quantas => ganhas - gastas;

  bool get temAlguma => quantas > 0;

  /// Já não cabe mais nenhuma. O ecrã da lição diz isto à criança em vez de
  /// lhe prometer uma sorte que ia direita ao lixo.
  bool get cheio => quantas >= tecto;

  Sortes comGanho([int n = porLicaoPerfeita]) => Sortes(
    ganhas: math.min(ganhas + math.max(0, n), gastas + tecto),
    gastas: gastas,
  );

  /// Gasta uma. Devolve nulo quando não há — quem chama decide o que dizer.
  Sortes? aGastar() =>
      temAlguma ? Sortes(ganhas: ganhas, gastas: gastas + 1) : null;

  Map<String, dynamic> paraJson() => {'ganhas': ganhas, 'gastas': gastas};

  static Sortes deJson(Map<String, dynamic>? j) {
    if (j == null) return const Sortes();
    final gastas = math.max(0, (j['gastas'] as num?)?.toInt() ?? 0);
    final ganhas = math.max(0, (j['ganhas'] as num?)?.toInt() ?? 0);
    return Sortes(ganhas: math.min(ganhas, gastas + tecto), gastas: gastas);
  }

  /// Fica pelo maior de cada total, e volta a aplicar o tecto.
  ///
  /// A mesma regra da carteira e da bolsa: o que se ganhou noutro telemóvel
  /// conta, e o que lá se gastou também. Ficar pelo maior saldo dava uma
  /// máquina de sortes a quem tivesse dois aparelhos.
  Sortes fundirCom(Sortes outra) {
    final gastas = math.max(this.gastas, outra.gastas);
    return Sortes(
      ganhas: math.min(math.max(ganhas, outra.ganhas), gastas + tecto),
      gastas: gastas,
    );
  }

  @override
  String toString() => 'Sortes($quantas de $tecto)';
}

/// "1 sorte", mas "3 sortes".
String sortesEmPalavras(int n) => n == 1 ? '1 sorte' : '$n sortes';
