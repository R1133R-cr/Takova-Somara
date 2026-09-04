import 'dart:math';

import 'sequencia.dart';

/// A campanha da semana.
///
/// É revisão espaçada disfarçada de desafio, e é **o único sítio da app com
/// prazo**. Tudo o resto espera pela criança; isto não. Nasce à segunda,
/// vale até domingo, e o que ficar por fazer perde-se.
///
/// O prazo não é para pressionar: é para dar à semana uma forma. Sem ele,
/// rever o que se estudou há cinco dias é uma coisa que se pode sempre fazer
/// amanhã, e por isso nunca se faz.
///
/// ## De onde vêm as perguntas
///
/// De duas fontes, e as duas contam:
///
/// - **o que se errou** (a lista dos Guardados) — o material com mais valor
///   que existe, porque exercitar o que já se sabe não ensina nada;
/// - **o que se estudou na semana passada** — a revisão que faz o
///   conhecimento assentar em vez de evaporar.
///
/// Nenhuma das duas pode comer a outra: uma criança com trinta erros por
/// rever teria uma campanha só de erros, e nunca reveria a matéria nova.
/// Por isso os erros ficam por metade — ver [metadeDosErros].
class Campanha {
  /// A segunda-feira a que esta campanha pertence, em ISO.
  final String semana;

  /// As perguntas, pelo enunciado — que é o que as identifica mesmo quando
  /// mudam de nível numa actualização de conteúdo.
  final List<String> enunciados;

  final bool feita;
  final int acertos;
  final int total;

  const Campanha({
    required this.semana,
    required this.enunciados,
    this.feita = false,
    this.acertos = 0,
    this.total = 0,
  });

  /// Abaixo disto não vale a pena: cinco perguntas não são uma campanha, e
  /// prometer um desafio semanal para depois dar dois minutos de trabalho
  /// gasta a palavra "campanha" por nada.
  static const minimo = 10;

  /// Acima disto é trabalho de casa, não um desafio.
  static const maximo = 20;

  /// Quantos dos [maximo] podem vir dos erros. Metade, para a matéria nova
  /// da semana ter sempre lugar.
  static const metadeDosErros = maximo ~/ 2;

  /// A margem de erro que ainda dá prémio.
  static const margemDeErro = 0.30;

  /// A margem que dá o prémio a dobrar.
  static const margemDeOuro = 0.10;

  int get quantas => enunciados.length;

  /// Percentagem de erro, de 0 a 1. Uma campanha por fazer conta como 1.
  double get erro => total == 0 ? 1 : (total - acertos) / total;

  /// Quantas sortes é que o resultado paga.
  ///
  /// Duas para quem acertou quase tudo, uma para quem passou a margem,
  /// nenhuma abaixo disso. O degrau do meio existe para o esforço de
  /// acertar tudo valer mais do que o de passar à tangente.
  int get sortesGanhas {
    if (!feita || total == 0) return 0;
    if (erro <= margemDeOuro) return 2;
    if (erro < margemDeErro) return 1;
    return 0;
  }

  Campanha comResultado(int acertos, int total) => Campanha(
    semana: semana,
    enunciados: enunciados,
    feita: true,
    acertos: acertos,
    total: total,
  );

  Map<String, dynamic> paraJson() => {
    'semana': semana,
    'enunciados': enunciados,
    'feita': feita,
    'acertos': acertos,
    'total': total,
  };

  static Campanha? deJson(Map<String, dynamic>? j) {
    if (j == null) return null;
    final semana = j['semana'];
    final lista = j['enunciados'];
    if (semana is! String || semana.isEmpty || lista is! List) return null;
    return Campanha(
      semana: semana,
      enunciados: lista.map((e) => '$e').toList(),
      feita: (j['feita'] ?? false) as bool,
      acertos: (j['acertos'] as num?)?.toInt() ?? 0,
      total: (j['total'] as num?)?.toInt() ?? 0,
    );
  }

  /// Junta com o que veio da nuvem.
  ///
  /// Da mesma semana fica o melhor resultado, e **feita é para sempre**:
  /// tê-la feito noutro telemóvel conta, e voltar a fazê-la aqui não pode
  /// pagar duas vezes. De semanas diferentes fica a mais recente — a de
  /// ontem já não serve para nada.
  Campanha fundirCom(Campanha? outra) {
    if (outra == null) return this;
    if (outra.semana != semana) {
      return outra.semana.compareTo(semana) > 0 ? outra : this;
    }
    final melhor = outra.acertos > acertos ? outra : this;
    return Campanha(
      semana: semana,
      enunciados: enunciados.isEmpty ? outra.enunciados : enunciados,
      feita: feita || outra.feita,
      acertos: melhor.acertos,
      total: melhor.total,
    );
  }

  @override
  String toString() =>
      'Campanha($semana, $quantas perguntas, ${feita ? "feita" : "por fazer"})';
}

/// A segunda-feira da semana a que uma data pertence.
String segundaDe(DateTime t) =>
    Sequencia.iso(Sequencia.soODia(t).subtract(Duration(days: t.weekday - 1)));

/// Uma semente estável a partir do texto da semana.
///
/// O `hashCode` das strings do Dart não é garantido entre execuções, e a
/// campanha tem de sair igual em dois telemóveis. Esta soma é feia e é
/// exactamente por isso que serve: faz sempre o mesmo.
int sementeDaSemana(String semana) {
  var h = 17;
  for (final u in semana.codeUnits) {
    h = (h * 31 + u) & 0x7fffffff;
  }
  return h;
}

/// Escolhe as perguntas de uma campanha.
///
/// [dosErros] e [doEstudo] entram pela ordem em que vierem; a mistura é
/// sorteada com a semente da semana, para dar sempre o mesmo conjunto no
/// mesmo telemóvel e em qualquer outro.
///
/// Devolve lista vazia quando não há material que chegue — nesse caso não há
/// campanha nenhuma, e é melhor não haver do que haver uma fraca.
List<String> escolherPerguntas({
  required List<String> dosErros,
  required List<String> doEstudo,
  required int semente,
}) {
  final r = Random(semente);
  final erros = [...dosErros]..shuffle(r);
  final estudo = [...doEstudo]..shuffle(r);

  final escolhidas = <String>{};
  for (final e in erros.take(Campanha.metadeDosErros)) {
    escolhidas.add(e);
  }
  for (final e in estudo) {
    if (escolhidas.length >= Campanha.maximo) break;
    escolhidas.add(e);
  }
  // Se uma das fontes não chegou, a outra enche o resto. O limite de metade
  // é para os erros não taparem a matéria nova, não para deixar a campanha
  // curta quando não há matéria nova nenhuma.
  for (final e in erros) {
    if (escolhidas.length >= Campanha.maximo) break;
    escolhidas.add(e);
  }

  if (escolhidas.length < Campanha.minimo) return const [];
  return escolhidas.toList()..shuffle(r);
}
