/// Sequência de dias seguidos de estudo.
///
/// Está separada do resto do estado e não conhece relógio nenhum: recebe
/// sempre o "hoje" de fora. É o que permite testar meses de calendário num
/// segundo, em vez de esperar dias para descobrir que a contagem falha na
/// viragem do mês ou quando a criança falta um dia.
class Sequencia {
  /// Dia da última actividade que contou (ISO local, ex.: 2026-08-07).
  final String? ultimoDia;

  /// Dias seguidos acumulados até [ultimoDia], inclusive.
  final int dias;

  const Sequencia({this.ultimoDia, this.dias = 0});

  static DateTime soODia(DateTime t) => DateTime(t.year, t.month, t.day);

  static String iso(DateTime t) {
    final d = soODia(t);
    return '${d.year.toString().padLeft(4, '0')}-'
        '${d.month.toString().padLeft(2, '0')}-'
        '${d.day.toString().padLeft(2, '0')}';
  }

  /// Dias de calendário entre [de] e [ate].
  ///
  /// Conta em horas e arredonda em vez de usar `inDays`: dois dias à
  /// meia-noite podem distar 23h ou 25h se houver mudança de hora, e o
  /// truncamento do `inDays` daria o dia errado justamente nessa noite.
  static int diasEntre(String de, DateTime ate) {
    final horas = soODia(ate).difference(soODia(DateTime.parse(de))).inHours;
    return (horas / 24).round();
  }

  /// O número a mostrar no ecrã em [hoje].
  ///
  /// Se a última actividade não foi hoje nem ontem, a sequência partiu-se e
  /// vale zero — mostrar o número antigo seria mentir à criança.
  int visivelEm(DateTime hoje) {
    if (ultimoDia == null) return 0;
    final d = diasEntre(ultimoDia!, hoje);
    return (d == 0 || d == 1) ? dias : 0;
  }

  /// Devolve a sequência depois de uma actividade que conta, feita em [hoje].
  /// Repetir no mesmo dia não soma: conta dias, não lições.
  Sequencia comActividadeEm(DateTime hoje) {
    final hojeIso = iso(hoje);
    if (ultimoDia == hojeIso) return this;
    final d = ultimoDia == null ? -1 : diasEntre(ultimoDia!, hoje);
    return Sequencia(
      ultimoDia: hojeIso,
      dias: d == 1 ? dias + 1 : 1,
    );
  }

  /// Junta duas sequências da mesma criança, vindas de aparelhos
  /// diferentes.
  ///
  /// Fica a que chegou mais longe no tempo; empatando no dia, a que tem
  /// mais dias. Não se somam: a criança não estudou o dobro dos dias por
  /// ter dois telemóveis, e inventar-lhe uma sequência maior do que a que
  /// cumpriu seria mentir-lhe — que é o mesmo que [visivelEm] já recusa
  /// fazer quando a sequência se parte.
  Sequencia fundirCom(Sequencia outra) {
    if (ultimoDia == null) return outra;
    if (outra.ultimoDia == null) return this;
    final c = ultimoDia!.compareTo(outra.ultimoDia!);
    if (c > 0) return this;
    if (c < 0) return outra;
    return dias >= outra.dias ? this : outra;
  }

  Map<String, dynamic> paraJson() => {'ultimoDia': ultimoDia, 'dias': dias};

  factory Sequencia.deJson(Map<String, dynamic>? j) {
    if (j == null) return const Sequencia();
    return Sequencia(
      ultimoDia: j['ultimoDia'] as String?,
      dias: (j['dias'] ?? 0) as int,
    );
  }
}
