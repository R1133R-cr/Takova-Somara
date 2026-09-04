import 'dart:math' as math;

/// Quanto tempo de joguinhos há hoje.
///
/// A app tem duas travagens e elas não são a mesma coisa. **Os corações
/// limitam os exercícios** — errar custa. **A bolsa limita os jogos** — e o
/// estudo nunca é bloqueado por ela. Uma criança sem tempo de jogo continua
/// a poder abrir a amarelinha, sempre.
///
/// A bolsa é pequena de manhã e enche-se a estudar. É a única maneira que
/// encontrámos de a parte divertida puxar pela parte da escola em vez de
/// competir com ela: o Pomar não é o prémio de acabar a lição, é o que a
/// lição paga.
///
/// ## Porquê um tecto
///
/// Sessenta minutos por dia e acabou, por mais que se estude. Sem tecto,
/// uma criança que descobrisse que refazer o nível 1 dá cinco minutos ficava
/// a refazer o nível 1 toda a tarde — e a app passava a substituir a escola
/// em vez de a acompanhar. O tecto é o que torna seguro deixar *qualquer*
/// nível concluído dar tempo, incluindo os repetidos.
///
/// ## O que se guarda
///
/// Não se guarda "quanto falta". Guarda-se o dia, o que se ganhou e o que se
/// gastou — três números que se somam sempre da mesma maneira. Guardar o
/// saldo dava um número que já não se sabia explicar quando o dia virasse a
/// meio de um jogo.
class BolsaDeTempo {
  /// O dia a que esta bolsa pertence, em ISO (`aaaa-mm-dd`).
  final String dia;

  /// Segundos ganhos a estudar, hoje.
  final int ganho;

  /// Segundos já gastos a jogar, hoje.
  final int gasto;

  const BolsaDeTempo({required this.dia, this.ganho = 0, this.gasto = 0});

  /// Uma bolsa nova, com só o que se dá de graça.
  const BolsaDeTempo.doDia(String dia) : this(dia: dia);

  /// O que se dá todos os dias sem estudar nada.
  ///
  /// Não é zero de propósito: uma criança que abre a app pela primeira vez
  /// tem de poder ver o que são os joguinhos antes de se lhe pedir seja o
  /// que for. Uma sala fechada à chave no primeiro dia não convida ninguém.
  static const gratis = Duration(minutes: 10);

  /// O que rende um nível de lição concluído.
  static const porNivel = Duration(minutes: 5);

  /// O que rende um nível sem um único erro. Substitui o [porNivel] — não
  /// se somam: acertar tudo vale oito, não treze.
  static const porNivelPerfeito = Duration(minutes: 8);

  /// O máximo que um dia pode dar, por mais que se estude.
  static const tecto = Duration(minutes: 60);

  /// Tudo o que hoje dá: o que é de graça mais o que se ganhou, até ao tecto.
  Duration get concedido => Duration(
    seconds: math.min(gratis.inSeconds + ganho, tecto.inSeconds),
  );

  /// O que ainda resta. Nunca negativo.
  Duration get restante =>
      Duration(seconds: math.max(0, concedido.inSeconds - gasto));

  bool get vazia => restante <= Duration.zero;

  /// Já se chegou ao tecto do dia — estudar mais não acrescenta tempo.
  bool get noTecto => concedido >= tecto;

  BolsaDeTempo comGanho(Duration d) =>
      BolsaDeTempo(dia: dia, ganho: ganho + math.max(0, d.inSeconds), gasto: gasto);

  BolsaDeTempo comGasto(Duration d) =>
      BolsaDeTempo(dia: dia, ganho: ganho, gasto: gasto + math.max(0, d.inSeconds));

  /// A bolsa deste dia. Se o dia virou, é uma bolsa nova.
  ///
  /// Chamada a olhar para o relógio e não por um temporizador à meia-noite:
  /// a app está fechada a essa hora, e o que conta é a data de quando se
  /// abre, não o tempo que esteve aberta. É a mesma regra das vidas.
  BolsaDeTempo noDia(String hoje) =>
      dia == hoje ? this : BolsaDeTempo.doDia(hoje);

  /// Junta com o que veio da nuvem.
  ///
  /// **O que se ganhou fica pelo maior e o que se gastou também.** Estudar
  /// no telemóvel da escola tem de contar no telemóvel de casa — e jogar
  /// também. Ficar pelo maior *saldo* seria o contrário: bastava entrar na
  /// conta noutro aparelho para os minutos gastos desaparecerem, e o tecto
  /// diário passava a ser uma sugestão.
  ///
  /// Dias diferentes não se juntam: o mais recente ganha inteiro, porque os
  /// números de ontem não dizem nada sobre hoje.
  BolsaDeTempo fundirCom(BolsaDeTempo outra) {
    if (outra.dia != dia) return outra.dia.compareTo(dia) > 0 ? outra : this;
    return BolsaDeTempo(
      dia: dia,
      ganho: math.max(ganho, outra.ganho),
      gasto: math.max(gasto, outra.gasto),
    );
  }

  Map<String, dynamic> paraJson() => {'dia': dia, 'ganho': ganho, 'gasto': gasto};

  static BolsaDeTempo? deJson(Map<String, dynamic>? j) {
    if (j == null) return null;
    final dia = j['dia'];
    if (dia is! String || dia.isEmpty) return null;
    return BolsaDeTempo(
      dia: dia,
      ganho: math.max(0, (j['ganho'] as num?)?.toInt() ?? 0),
      gasto: math.max(0, (j['gasto'] as num?)?.toInt() ?? 0),
    );
  }

  @override
  String toString() => 'BolsaDeTempo($dia, ganho $ganho s, gasto $gasto s)';
}

/// O tempo como se diz a uma criança de sete anos.
///
/// Debaixo do minuto conta-se aos segundos: mostrar "0 min" com quarenta
/// segundos ainda por gastar seria mentira, e é justamente aí que a criança
/// está a olhar para o número.
String tempoEmPalavras(Duration d) {
  final s = d.inSeconds;
  if (s < 60) return '$s s';
  return '${s ~/ 60} min';
}

/// "Faltam 40 s", mas "Falta 1 s" — o verbo também muda, não só o número.
///
/// É a mesma correcção que a sopa de letras levou. Aparece à criança nos
/// últimos segundos de um jogo, que é justamente quando ela está a ler.
String quantoFalta(Duration d) {
  final s = d.inSeconds;
  final texto = tempoEmPalavras(d);
  final um = s == 1 || (s >= 60 && s < 120);
  return um ? 'Falta $texto' : 'Faltam $texto';
}
