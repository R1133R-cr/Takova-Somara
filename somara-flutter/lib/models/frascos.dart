/// «Water R Sort»: arrumar líquidos até cada frasco ter uma cor só.
///
/// O jogo é conhecido e a regra é curta: despeja-se do topo de um frasco
/// para o topo de outro, e só se o outro estiver vazio ou tiver a mesma cor
/// à cabeça. Ganha-se quando todos os frascos estão vazios ou cheios de uma
/// cor só.
///
/// Porque é que o tabuleiro nasce ao contrário
/// -------------------------------------------
/// A maneira óbvia de montar um destes é atirar as cores para os frascos ao
/// acaso. É também a maneira de produzir níveis impossíveis, e um nível
/// impossível não se distingue de um nível difícil: a criança tenta, falha,
/// e culpa-se. Já aconteceu nesta app — o Pomar pedia 140 peças em doze
/// jogadas e ninguém tinha reparado.
///
/// Por isso aqui parte-se do tabuleiro ARRUMADO e dão-se jogadas ao
/// contrário. Cada jogada ao contrário é o inverso exacto de uma jogada
/// legal; jogar a lista ao contrário, do fim para o princípio, resolve o
/// nível. A solução não é procurada, é construída — e por isso não há
/// procura nenhuma a correr no telemóvel da criança.
///
/// O [test/frascos_test.dart] confirma isto por fora, com um solucionador
/// que não sabe nada de como o tabuleiro foi feito.
library;

import 'dart:math' as math;

import 'escadaria.dart';

/// As cores dos líquidos.
///
/// Nove, e não é número redondo por acaso: é quantas se distinguem mesmo
/// umas das outras no fundo escuro da app, e é exactamente quantas o último
/// degrau da escadaria pede. Cada uma tem nome porque a criança que não
/// distingue duas delas ainda as pode ouvir nomeadas.
enum CorDoLiquido {
  vermelho('Vermelho', 0xFFFF5D5D),
  laranja('Laranja', 0xFFFF9A3C),
  amarelo('Amarelo', 0xFFF5D33C),
  verde('Verde', 0xFF5FD68B),
  azul('Azul', 0xFF4FA8FF),
  roxo('Roxo', 0xFFB77BE8),
  rosa('Rosa', 0xFFFF7EC4),
  castanho('Castanho', 0xFFC08552),
  creme('Creme', 0xFFEDE6D6);

  final String nome;

  /// O valor ARGB. O modelo não importa `dart:ui` de propósito: assim
  /// corre num teste sem Flutter por baixo.
  final int valor;

  const CorDoLiquido(this.nome, this.valor);
}

/// Um frasco e o que tem dentro.
class Frasco {
  /// Do FUNDO para o TOPO. O último da lista é o que se despeja.
  final List<CorDoLiquido> blocos;

  /// Quantos blocos leva. Igual em todos os frascos da mesa — ver
  /// [ParamsFrascos.altura].
  final int altura;

  Frasco(List<CorDoLiquido> blocos, this.altura)
      : blocos = List.unmodifiable(blocos);

  Frasco.vazio(this.altura) : blocos = const [];

  bool get vazio => blocos.isEmpty;
  bool get cheio => blocos.length == altura;
  int get livre => altura - blocos.length;

  /// A cor que se despeja. Nula se o frasco está vazio.
  CorDoLiquido? get topo => vazio ? null : blocos.last;

  /// Quantos blocos iguais estão juntos no topo. É quanto sai de uma vez.
  int get corridaNoTopo {
    if (vazio) return 0;
    final c = blocos.last;
    var n = 0;
    for (var i = blocos.length - 1; i >= 0 && blocos[i] == c; i--) {
      n++;
    }
    return n;
  }

  /// Uma cor só, do fundo ao topo. Um frasco vazio não conta.
  bool get deUmaCor => !vazio && blocos.every((b) => b == blocos.first);

  /// Frasco no sítio: ou vazio, ou cheio de uma cor só.
  ///
  /// Cheio é preciso. Um frasco com dois vermelhos e mais nada está a meio
  /// caminho, não está arrumado — os outros dois vermelhos andam por aí.
  bool get arrumado => vazio || (cheio && deUmaCor);

  Frasco comBlocos(List<CorDoLiquido> novos) => Frasco(novos, altura);
}

/// Uma jogada: quantos blocos passam de um frasco para outro.
typedef Despejo = ({int de, int para, int quantos, CorDoLiquido cor});

/// A mesa de um nível.
class Frascos {
  final List<Frasco> frascos;
  final int nivel;
  final ParamsFrascos params;

  Frascos({
    required List<Frasco> frascos,
    required this.nivel,
    required this.params,
  }) : frascos = List.unmodifiable(frascos);

  /// Tudo arrumado.
  bool get ganho => frascos.every((f) => f.arrumado);

  /// Quantas cores já estão fechadas. Serve o rodapé do ecrã.
  int get coresFeitas =>
      frascos.where((f) => f.cheio && f.deUmaCor).length;

  /// Quantos blocos passariam de [de] para [para]. Zero quando a jogada
  /// não é permitida — que é a mesma coisa que dizer que não é jogada.
  ///
  /// A regra apertada, e é apertada de propósito: só se despeja para um
  /// frasco vazio, ou para um que tenha a MESMA cor à cabeça. E nunca mais
  /// do que lá cabe.
  int quantosDespeja(int de, int para) {
    if (de == para) return 0;
    if (de < 0 || para < 0) return 0;
    if (de >= frascos.length || para >= frascos.length) return 0;

    final a = frascos[de], b = frascos[para];
    if (a.vazio || b.cheio) return 0;
    if (!b.vazio && b.topo != a.topo) return 0;
    return math.min(a.corridaNoTopo, b.livre);
  }

  bool podeDespejar(int de, int para) => quantosDespeja(de, para) > 0;

  /// A mesa depois da jogada. Devolve a própria mesa se a jogada não vale,
  /// para quem chamar sem verificar não ficar com um tabuleiro partido.
  Frascos despejar(int de, int para) {
    final n = quantosDespeja(de, para);
    if (n == 0) return this;

    final a = frascos[de], b = frascos[para];
    final cor = a.topo!;
    final novos = [...frascos];
    novos[de] = a.comBlocos(a.blocos.sublist(0, a.blocos.length - n));
    novos[para] = b.comBlocos([...b.blocos, ...List.filled(n, cor)]);
    return Frascos(frascos: novos, nivel: nivel, params: params);
  }

  /// Há alguma jogada por fazer? Sem isto, um tabuleiro empancado ficava a
  /// olhar para a criança sem lhe dizer que já não há nada a fazer.
  bool get temJogada {
    for (var i = 0; i < frascos.length; i++) {
      for (var j = 0; j < frascos.length; j++) {
        if (podeDespejar(i, j)) return true;
      }
    }
    return false;
  }

  /// O tabuleiro de um degrau da escadaria.
  ///
  /// Sem [rnd] é DETERMINISTA: o nível 37 é o mesmo puzzle em todos os
  /// telemóveis — duas crianças lado a lado vêem o mesmo — e «Recomeçar»
  /// devolve exactamente o tabuleiro com que ela começou, que é o que
  /// recomeçar quer dizer.
  factory Frascos.doNivel(int nivel, {math.Random? rnd}) {
    final n = nivel.clamp(1, nivelMaximo);
    final p = frascosNo(n);
    final r = rnd ?? math.Random(n * 7919);

    // Com `nadaArrumado` nenhum frasco pode começar de uma cor só: um
    // frasco já feito é meio nível oferecido. Tenta-se algumas vezes e
    // fica-se pela melhor — nunca se devolve nível nenhum por não se
    // conseguir, porque não abrir o jogo é pior do que abri-lo mais fácil.
    final exigente = p.mecanicas.contains(Mecanica.nadaArrumado);
    List<Frasco>? melhor;
    for (var tentativa = 0; tentativa < 12; tentativa++) {
      final mesa = _baralhar(p, r);
      final serve = mesa.every((f) => f.vazio || !f.deUmaCor);
      melhor ??= mesa;
      if (!exigente || serve) {
        melhor = mesa;
        break;
      }
    }

    return Frascos(frascos: melhor!, nivel: n, params: p);
  }

  /// Do arrumado para trás, uma jogada legal de cada vez.
  static List<Frasco> _baralhar(ParamsFrascos p, math.Random r) {
    final tubos = <List<CorDoLiquido>>[
      for (var i = 0; i < p.cores; i++)
        List.filled(p.altura, CorDoLiquido.values[i], growable: true),
      for (var i = 0; i < p.vazios; i++) <CorDoLiquido>[],
    ];

    for (var passo = 0; passo < p.baralhadelas; passo++) {
      final possiveis = _aoContrario(tubos, p.altura);
      if (possiveis.isEmpty) break;
      final j = possiveis[r.nextInt(possiveis.length)];
      final cor = tubos[j.de].last;
      tubos[j.de].removeRange(tubos[j.de].length - j.quantos, tubos[j.de].length);
      tubos[j.para].addAll(List.filled(j.quantos, cor));
    }

    return [for (final t in tubos) Frasco(t, p.altura)];
  }

  /// As jogadas ao contrário que se podem dar neste estado.
  ///
  /// Uma jogada ao contrário tira [quantos] blocos do topo de `de` e
  /// põe-nos no topo de `para`. Para que a jogada DIREITA (`para` → `de`)
  /// seja legal, três coisas têm de bater certo, e é aqui que o jogo se
  /// mantém sempre resolúvel:
  ///
  /// 1. `quantos` não pode partir a corrida ao meio e deixar por baixo uma
  ///    cor diferente — ou se leva menos do que a corrida toda (e fica cor
  ///    igual à cabeça), ou se leva tudo e o frasco fica vazio. Nos outros
  ///    casos a jogada direita despejava para cima de uma cor diferente,
  ///    que é precisamente o que a regra proíbe.
  /// 2. `para` não pode já ter essa cor à cabeça. Se tivesse, a corrida no
  ///    destino ficava maior do que [quantos] e a jogada direita levava
  ///    mais blocos do que estes — deixava de ser o inverso exacto.
  /// 3. Tem de haver espaço.
  static List<({int de, int para, int quantos})> _aoContrario(
    List<List<CorDoLiquido>> tubos,
    int altura,
  ) {
    final saida = <({int de, int para, int quantos})>[];

    for (var de = 0; de < tubos.length; de++) {
      final origem = tubos[de];
      if (origem.isEmpty) continue;

      final cor = origem.last;
      var corrida = 0;
      for (var i = origem.length - 1; i >= 0 && origem[i] == cor; i--) {
        corrida++;
      }

      for (var quantos = 1; quantos <= corrida; quantos++) {
        // (1)
        if (quantos == corrida && origem.length != corrida) continue;

        for (var para = 0; para < tubos.length; para++) {
          if (para == de) continue;
          final destino = tubos[para];
          // (2)
          if (destino.isNotEmpty && destino.last == cor) continue;
          // (3)
          if (altura - destino.length < quantos) continue;
          saida.add((de: de, para: para, quantos: quantos));
        }
      }
    }
    return saida;
  }
}
