import '../widgets/roby.dart';
import 'carteira.dart';

/// O que está à venda na loja do Roby.
///
/// Duas famílias, e a diferença não é de preço mas de trabalho: as **caras**
/// são bustos quadrados que entram em qualquer sítio onde já esteja um Roby;
/// as **poses de corpo inteiro** são desenhos verticais que só ficam bem com
/// espaço. E há os **minutos**, que se gastam em vez de se guardarem.
/// A ordem é a ordem em que aparecem na loja, e os minutos vêm primeiro de
/// propósito: são a compra barata e do dia-a-dia, e enterrá-los debaixo de
/// vinte e três desenhos era escondê-los de quem vem cá justamente por eles.
enum Familia {
  tempo('Minutos', 'Mais tempo de joguinhos, hoje.'),
  cara('Caras', 'Como o Roby fica quando te vê a estudar.'),
  pose('Poses', 'O Roby de corpo inteiro, a fazer alguma coisa.');

  final String rotulo;
  final String descricao;
  const Familia(this.rotulo, this.descricao);
}

/// Uma coisa que se pode comprar.
class ItemDaLoja {
  /// Estável e nunca reutilizado: é isto que fica guardado no telemóvel e na
  /// nuvem. Mudar um `id` faria uma criança perder o que comprou.
  final String id;

  final Familia familia;
  final Moeda moeda;
  final int preco;

  /// O que se desbloqueia. Nulo nos minutos, que não se guardam.
  final RobyPose? pose;

  /// Quanto tempo de jogo dá. Nulo em tudo o resto.
  final Duration? tempo;

  const ItemDaLoja({
    required this.id,
    required this.familia,
    required this.moeda,
    required this.preco,
    this.pose,
    this.tempo,
  });

  /// Gasta-se em vez de se guardar: comprar duas vezes faz sentido.
  bool get consumivel => tempo != null;

  String get nome => pose?.rotulo ?? _nomeDoTempo;

  String get _nomeDoTempo {
    final m = tempo!.inMinutes;
    return m == 1 ? '+1 minuto' : '+$m minutos';
  }
}

/// Uma cara custa dois cristais; uma pose de corpo inteiro, quatro.
///
/// A diferença não é arbitrária: as poses são desenhos maiores e há menos
/// delas. Aos preços do §6 e com cerca de um cristal por semana de trabalho
/// a sério, uma cara é uma quinzena e uma pose é quase um mês — é para ser
/// uma coisa que se poupa, não uma que se apanha.
const _precoDaCara = 2;
const _precoDaPose = 4;

/// Tudo o que está à venda.
///
/// As poses de fábrica (as treze que a interface usa) **não entram**: já são
/// da criança desde o primeiro dia, e pô-las à venda seria vender-lhe o que
/// ela já tem.
final List<ItemDaLoja> catalogo = [
  const ItemDaLoja(
    id: 'tempo-5',
    familia: Familia.tempo,
    moeda: Moeda.gc,
    preco: 20,
    tempo: Duration(minutes: 5),
  ),
  const ItemDaLoja(
    id: 'tempo-30',
    familia: Familia.tempo,
    moeda: Moeda.cc,
    preco: 3,
    tempo: Duration(minutes: 30),
  ),
  for (final p in posesAVenda)
    ItemDaLoja(
      id: p.name,
      familia: p.retrato ? Familia.pose : Familia.cara,
      moeda: Moeda.cc,
      preco: p.retrato ? _precoDaPose : _precoDaCara,
      pose: p,
    ),
];

/// As poses que a interface usa e que por isso nunca se compram.
const posesDeFabrica = {
  RobyPose.token,
  RobyPose.salto,
  RobyPose.hero,
  RobyPose.dica,
  RobyPose.feliz,
  RobyPose.rindo,
  RobyPose.empolgado,
  RobyPose.orgulhoso,
  RobyPose.triste,
  RobyPose.confuso,
  RobyPose.confiante,
  RobyPose.curioso,
  RobyPose.graduate,
};

/// As restantes — as que a loja vende.
final List<RobyPose> posesAVenda = [
  for (final p in RobyPose.values)
    if (!posesDeFabrica.contains(p)) p,
];

ItemDaLoja? itemPorId(String id) {
  for (final i in catalogo) {
    if (i.id == id) return i;
  }
  return null;
}

/// O que a criança já tem, e o que escolheu usar.
class Coleccao {
  /// Os `id` do que se comprou. Só coisas que se guardam — os minutos não
  /// entram aqui, gastam-se no momento.
  final Set<String> compradas;

  /// A pose que o Roby usa no mapa. Nula quer dizer a de fábrica.
  final RobyPose? escolhida;

  const Coleccao({this.compradas = const {}, this.escolhida});

  bool tem(RobyPose p) =>
      posesDeFabrica.contains(p) || compradas.contains(p.name);

  Coleccao com(String id) =>
      Coleccao(compradas: {...compradas, id}, escolhida: escolhida);

  /// Veste uma pose. Recusa uma que não seja dela — sem isto, um estado
  /// estragado punha o Roby com uma cara por pagar.
  Coleccao aUsar(RobyPose? p) => (p == null || tem(p))
      ? Coleccao(compradas: compradas, escolhida: p)
      : this;

  /// A pose a mostrar. É onde se decide o que acontece se a escolhida
  /// desaparecer numa actualização: volta-se à de fábrica em silêncio, em
  /// vez de rebentar com um ficheiro que já não existe.
  RobyPose get roby {
    final e = escolhida;
    if (e == null || !tem(e)) return RobyPose.token;
    return e;
  }

  Map<String, dynamic> paraJson() => {
    'compradas': compradas.toList()..sort(),
    'escolhida': escolhida?.name,
  };

  static Coleccao deJson(Map<String, dynamic>? j) {
    if (j == null) return const Coleccao();
    final ids = ((j['compradas'] as List?) ?? const [])
        .map((e) => '$e')
        // Um `id` que já não exista no catálogo é deitado fora aqui e não
        // mais tarde: assim nunca chega a haver uma pose sem ficheiro.
        .where((id) => itemPorId(id) != null)
        .toSet();
    final nome = j['escolhida'] as String?;
    RobyPose? escolhida;
    for (final p in RobyPose.values) {
      if (p.name == nome) escolhida = p;
    }
    return Coleccao(compradas: ids, escolhida: escolhida).aUsar(escolhida);
  }

  /// Junta duas colecções: **união**, sempre.
  ///
  /// Comprar uma cara no telemóvel da escola e outra no de casa tem de dar
  /// as duas. Não há aqui nenhum caso em que se perca o que se comprou.
  Coleccao fundirCom(Coleccao outra) => Coleccao(
    compradas: {...compradas, ...outra.compradas},
    // A escolhida local ganha: é a que a criança está a ver neste momento,
    // e trocar-lhe a cara do Roby por causa de uma sincronização seria
    // desconcertante.
    escolhida: escolhida ?? outra.escolhida,
  ).aUsar(escolhida ?? outra.escolhida);
}

/// O que aconteceu a uma tentativa de compra.
///
/// Um enum e não um booleano: as três recusas pedem frases diferentes, e
/// "não deu" à frente de uma criança que juntou cristais durante duas
/// semanas não é resposta nenhuma.
enum ResultadoDaCompra {
  feito,

  /// Não tem moedas que cheguem.
  semSaldo,

  /// Já é dela — só acontece se dois toques passarem ao mesmo tempo.
  jaTem,

  /// Minutos com a bolsa já no tecto do dia. O dinheiro fica onde estava:
  /// vender tempo que o tecto ia deitar fora seria vender nada.
  noTecto;

  String get explicacao => switch (this) {
    ResultadoDaCompra.feito => 'Já é teu!',
    ResultadoDaCompra.semSaldo => 'Ainda não chega. Estuda mais um nível.',
    ResultadoDaCompra.jaTem => 'Já tens isso.',
    ResultadoDaCompra.noTecto =>
      'Já tens o tempo todo de hoje. Guarda para amanhã.',
  };
}
