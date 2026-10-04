/// A versão de testes da Somara — a que não tem fila.
///
/// Existem duas entregas do mesmo código:
///
///  * a **normal**, que é a app como a criança a recebe: os níveis abrem-se
///    por ordem, os corações custam, a bolsa dá sessenta minutos por dia;
///  * a **de testes**, para o professor que está a procurar defeitos. Aqui
///    qualquer nível se abre em qualquer ordem — incluindo o último de uma
///    disciplina sem se ter feito o primeiro —, qualquer nível de qualquer
///    joguinho se escolhe à mão, e o tempo de jogo não acaba.
///
/// ## O que *não* muda na versão de testes
///
/// Os corações e o dinheiro continuam a funcionar como na app real. É de
/// propósito: quem anda a testar precisa de ver o que a criança vê, e um
/// coração que nunca desce esconde justamente a parte que mais parte. Há
/// interruptores no painel para os desligar quando o objectivo for varrer
/// cinquenta níveis depressa — mas ligados é que é a posição de descanso.
///
/// ## Como se compila
///
/// ```bash
/// flutter build apk --release \
///   --dart-define=SOMARA_TESTE=true \
///   --dart-define=SOMARA_DATA=2026-10-04 \
///   -Pteste=true
/// ```
///
/// O `--dart-define` chega ao código Dart; o `-Pteste=true` chega ao Gradle,
/// que é quem põe o sufixo `.teste` no identificador da aplicação e o nome
/// «Somara TESTE» debaixo do ícone. São os dois necessários: sem o primeiro
/// a app não se abre a si mesma, sem o segundo instalar uma apagava a outra.
/// O `compilar.sh release ambas` faz as duas de uma vez e não deixa esquecer
/// nenhum dos dois.
///
/// ## Porque é que caduca
///
/// Um APK com tudo aberto que ande a circular no WhatsApp é, no dia em que
/// a 8ª e a 9ª passarem a pagas, a app inteira de graça — e não há maneira
/// de o chamar de volta. Sessenta dias depois de compilado, este recusa-se
/// a abrir. Quem o recebeu de segunda mão fica com um ficheiro morto; os
/// professores que o revêem recebem um novo a cada versão, de qualquer
/// maneira.
class ModoTeste {
  ModoTeste._();

  /// Esta compilação é a de testes.
  ///
  /// Constante de compilação: na versão normal o compilador corta todo o
  /// código que depende disto, e o painel de testes não vai dentro do APK.
  static const bool activo = bool.fromEnvironment('SOMARA_TESTE');

  /// O dia em que o APK foi compilado, em ISO (`aaaa-mm-dd`).
  static const String compiladaEm = String.fromEnvironment('SOMARA_DATA');

  /// A versão do `pubspec.yaml`, como o `compilar.sh` a passa.
  ///
  /// Vem por aqui e não de um pacote novo: `package_info_plus` seria mais
  /// uma dependência — mais uma coisa que pode partir numa actualização —
  /// para ler uma linha que o guião de compilação já tem na mão.
  static const String versao = String.fromEnvironment('SOMARA_VERSAO');

  /// Quanto tempo vive uma versão de testes.
  static const Duration validade = Duration(days: 60);

  /// Quantos dias faltam a uma versão compilada em `compilada` (ISO), vista
  /// de `agora`. Negativo depois de caducar.
  ///
  /// Devolve nulo quando não há data, ou quando a data não se entende — e
  /// nesse caso a app **não** caduca. É deliberado: um `--dart-define`
  /// esquecido não pode transformar-se numa app que não abre. O guarda
  /// contra o esquecimento está no `compilar.sh`, que passa sempre a data.
  ///
  /// Está à parte e recebe os dois valores de fora para se poder testar: é
  /// a única conta desta app que, errada, dá um APK que ninguém consegue
  /// abrir.
  static int? diasQueFaltamDe(String compilada, DateTime agora) {
    if (compilada.isEmpty) return null;
    final d = DateTime.tryParse(compilada);
    if (d == null) return null;
    final fim = DateTime(d.year, d.month, d.day).add(validade);
    return fim.difference(DateTime(agora.year, agora.month, agora.day)).inDays;
  }

  /// Quantos dias faltam a *esta* compilação. Nulo sem data.
  static int? diasQueFaltam([DateTime? agora]) =>
      diasQueFaltamDe(compiladaEm, agora ?? DateTime.now());

  /// O dia a partir do qual deixa de abrir. Nulo quando não há data.
  static DateTime? get caducaEm {
    if (compiladaEm.isEmpty) return null;
    final d = DateTime.tryParse(compiladaEm);
    return d == null ? null : DateTime(d.year, d.month, d.day).add(validade);
  }

  /// Esta versão de testes já passou da validade?
  ///
  /// Falso na versão normal, sempre — ela não caduca.
  static bool caducou([DateTime? agora]) {
    if (!activo) return false;
    final faltam = diasQueFaltam(agora);
    return faltam != null && faltam <= 0;
  }
}

/// Os interruptores do painel de testes.
///
/// Guardam-se à parte do progresso (chave própria no `shared_preferences`)
/// por duas razões: apagar o progresso não pode apagar a configuração do
/// painel, e a versão normal nunca lê esta chave — nem que o ficheiro lá
/// esteja, por exemplo num telemóvel onde se instalaram as duas.
class InterruptoresDeTeste {
  /// Repõe a app como a criança a vê: fila dos níveis, corações, bolsa,
  /// tudo. É o interruptor «pôr à venda» — serve para testar o outro lado
  /// sem trocar de APK.
  ///
  /// Quando está ligado, manda em todos os outros: a app de testes passa a
  /// ser indistinguível da normal, excepto na marca vermelha.
  final bool aVenda;

  /// Errar não custa. Desligado por omissão.
  final bool coracoesInfinitos;

  /// Comprar e pagar ajudas não gasta nada. Desligado por omissão.
  final bool nadaCusta;

  /// Quantos dias para a frente o calendário foi empurrado à mão.
  ///
  /// A sequência de dias, a reposição dos corações, a bolsa diária e a
  /// campanha da semana só se vêem a mexer quando o dia vira. Sem isto, a
  /// única maneira de os testar era esperar pela meia-noite.
  final int desvioDeDias;

  const InterruptoresDeTeste({
    this.aVenda = false,
    this.coracoesInfinitos = false,
    this.nadaCusta = false,
    this.desvioDeDias = 0,
  });

  InterruptoresDeTeste com({
    bool? aVenda,
    bool? coracoesInfinitos,
    bool? nadaCusta,
    int? desvioDeDias,
  }) => InterruptoresDeTeste(
    aVenda: aVenda ?? this.aVenda,
    coracoesInfinitos: coracoesInfinitos ?? this.coracoesInfinitos,
    nadaCusta: nadaCusta ?? this.nadaCusta,
    desvioDeDias: desvioDeDias ?? this.desvioDeDias,
  );

  Map<String, dynamic> paraJson() => {
    'aVenda': aVenda,
    'coracoes': coracoesInfinitos,
    'nadaCusta': nadaCusta,
    'dias': desvioDeDias,
  };

  static InterruptoresDeTeste deJson(Map<String, dynamic>? j) {
    if (j == null) return const InterruptoresDeTeste();
    final dias = j['dias'];
    return InterruptoresDeTeste(
      aVenda: j['aVenda'] == true,
      coracoesInfinitos: j['coracoes'] == true,
      nadaCusta: j['nadaCusta'] == true,
      // Negativo não entra: um desvio para trás punha a sequência de dias a
      // ver actividade no futuro, e isso não é um teste — é um estado que a
      // app nunca pode ter.
      desvioDeDias: dias is int && dias > 0 ? dias : 0,
    );
  }
}
