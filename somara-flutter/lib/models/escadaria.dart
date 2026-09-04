/// A escadaria de cada joguinho: do nível 1 ao 1000.
///
/// Cada jogo tem a SUA escadaria — não há nível global do aluno. O XP e a
/// amarelinha do currículo continuam a ser outra coisa, e não se misturam
/// com isto: uma criança pode estar no nível 300 do Pomar e na segunda
/// unidade de Matemática, e as duas coisas são verdade ao mesmo tempo.
///
/// A dificuldade tem duas camadas
/// ------------------------------
/// A **base** cresce continuamente com [curva]. As **mecânicas** entram em
/// marcos e nunca mais saem — é isso que impede que o nível 500 seja apenas
/// o nível 5 mais apertado.
library;

import 'dart:math' as math;

/// Os joguinhos que têm escadaria.
enum Jogo {
  crossmath('Crossmath'),
  pomar('Pomar'),
  sopa('Sopa de letras'),
  memoria('Memória'),
  frascos('Water R Sort');

  final String rotulo;
  const Jogo(this.rotulo);
}

/// O último degrau. Não é um número mágico: é a promessa feita à criança.
const int nivelMaximo = 1000;

/// Quanto da dificuldade máxima já foi percorrida, de 0 a 1.
///
/// Uma exponencial que cresce depressa no início e abranda no fim:
///
///     nível    1 → 0,004
///     nível  100 → 0,32
///     nível  500 → 0,86
///     nível 1000 → 1,00
///
/// A forma importa. Uma recta faria os primeiros cinquenta níveis parecerem
/// todos iguais — e são esses que decidem se a criança volta. Uma curva mais
/// agressiva punha o nível 200 já no tecto, e sobrariam oitocentos degraus
/// sem nada para dar.
double curva(int nivel) {
  final n = nivel.clamp(1, nivelMaximo);
  const k = 260.0;
  final bruto = 1 - math.exp(-n / k);
  final tecto = 1 - math.exp(-nivelMaximo / k);
  return bruto / tecto;
}

/// Interpola entre dois inteiros. Aceita [de] > [ate] — há parâmetros que
/// APERTAM ao subir de nível, como as jogadas do Pomar.
int _entre(int de, int ate, double t) => (de + (ate - de) * t).round();

/// As mecânicas que entram em marcos.
///
/// Cada uma tem o jogo a que pertence e o nível a partir do qual aparece.
/// Depois do nível 100 o gerador deixa de introduzir mecânicas novas e passa
/// a COMBINAR as que já existem — é o que dá variedade sem trabalho infinito.
enum Mecanica {
  // Pomar
  gelo(Jogo.pomar, 25, 'Peças presas em gelo'),
  objectivo(Jogo.pomar, 50, 'Objectivo em vez de pontos'),
  pedras(Jogo.pomar, 75, 'Pedras que caem e tapam'),
  relogio(Jogo.pomar, 100, 'Tempo limitado'),

  // Sopa
  aoContrario(Jogo.sopa, 25, 'Palavras ao contrário'),
  buracos(Jogo.sopa, 50, 'Grelha com buracos'),
  porPista(Jogo.sopa, 75, 'Palavra escondida por pista'),
  duasCategorias(Jogo.sopa, 100, 'Duas categorias misturadas'),

  // Crossmath
  duplaEquacao(Jogo.crossmath, 25, 'Uma célula em duas equações'),
  negativos(Jogo.crossmath, 50, 'Resultado negativo'),
  intruso(Jogo.crossmath, 75, 'Uma equação errada de propósito'),
  grelhaGrande(Jogo.crossmath, 100, 'Grelha 4×4'),

  // Memória
  umaVista(Jogo.memoria, 25, 'Cartas que só viram uma vez'),
  trio(Jogo.memoria, 50, 'Um par a três'),
  baralhar(Jogo.memoria, 75, 'Cartas que trocam de sítio'),
  falsoPar(Jogo.memoria, 100, 'Duas iguais que não são par'),

  // Water R Sort
  //
  // Nenhuma destas esconde informação à criança, e é de propósito. Tapar
  // as cores de baixo é a mecânica que este género costuma trazer, e
  // transformava um jogo de planear num jogo de adivinhar — o mesmo erro
  // que a Memória evita ao deixar as cartas à vista antes de as virar.
  semFolga(Jogo.frascos, 25, 'Um frasco vazio em vez de dois'),
  nadaArrumado(Jogo.frascos, 50, 'Nenhum frasco começa arrumado'),
  maisFundo(Jogo.frascos, 75, 'Frascos de cinco'),
  maisCores(Jogo.frascos, 100, 'Uma cor a mais do que a conta');

  final Jogo jogo;
  final int desde;
  final String rotulo;
  const Mecanica(this.jogo, this.desde, this.rotulo);
}

/// As mecânicas activas de um jogo, num dado nível.
Set<Mecanica> mecanicasDe(Jogo jogo, int nivel) => Mecanica.values
    .where((m) => m.jogo == jogo && nivel >= m.desde)
    .toSet();

/// O que muda no Pomar de nível para nível.
class ParamsPomar {
  final int linhas;
  final int colunas;

  /// Quantos produtos distintos entram no tabuleiro. Menos produtos, mais
  /// fácil é encontrar três iguais.
  ///
  /// Vai de 4 a **6**, que é quantos há. Chegou a dizer 7 aqui, e nenhum
  /// teste dava por isso porque nada lia este número — no dia em que o
  /// tabuleiro passasse a lê-lo, ia buscar um produto que não existe.
  final int produtos;

  /// Jogadas dadas. Este APERTA: começa em 25 e acaba em 12.
  final int jogadas;

  /// Peças a colher para fechar o nível.
  ///
  /// De 20 a 42, e o tecto não é arbitrário: é o que o solucionador do §7
  /// consegue mesmo colher. Uma jogada boa apanha cinco a sete peças, e no
  /// último degrau há doze jogadas — pedir 140, como este número já pediu,
  /// era pedir doze peças por jogada a uma criança de nove anos.
  final int objectivo;

  final Set<Mecanica> mecanicas;

  const ParamsPomar({
    required this.linhas,
    required this.colunas,
    required this.produtos,
    required this.jogadas,
    required this.objectivo,
    required this.mecanicas,
  });
}

/// O que muda na Sopa de letras.
class ParamsSopa {
  final int lado;
  final int palavras;
  final bool diagonais;
  final bool invertidas;
  final Set<Mecanica> mecanicas;

  const ParamsSopa({
    required this.lado,
    required this.palavras,
    required this.diagonais,
    required this.invertidas,
    required this.mecanicas,
  });
}

/// O que muda no Crossmath.
class ParamsCrossmath {
  /// Valor máximo da casa maior. É o que separa a 1ª classe da 6ª.
  final int tecto;

  /// Casas à vista. NUNCA menos de quatro.
  ///
  /// Não é preferência: a grelha tem quatro valores livres, e cada casa é
  /// uma combinação linear deles. Três pistas nunca os fixam — o puzzle
  /// tem sempre uma família de soluções e é apenas impossível, não difícil.
  /// A [minimoDePistas] existe para isto não se perder ao mexer na curva.
  final int pistas;

  final Set<Mecanica> mecanicas;

  static const minimoDePistas = 4;

  const ParamsCrossmath({
    required this.tecto,
    required this.pistas,
    required this.mecanicas,
  });
}

/// O que muda na Memória.
class ParamsMemoria {
  final int pares;

  /// Quanto tempo as cartas ficam à vista antes de voltarem. Aperta.
  final Duration espera;

  final Set<Mecanica> mecanicas;

  const ParamsMemoria({
    required this.pares,
    required this.espera,
    required this.mecanicas,
  });
}

/// Os parâmetros do Pomar no nível dado.
ParamsPomar pomarNo(int nivel) {
  final t = curva(nivel);
  return ParamsPomar(
    // O tabuleiro não cresce: num telemóvel de 320 já está no limite do que
    // se vê. O que cresce é o que lá está dentro.
    linhas: 8,
    colunas: 7,
    produtos: _entre(4, 6, t),
    jogadas: _entre(25, 12, t),
    objectivo: _entre(20, 42, t),
    mecanicas: mecanicasDe(Jogo.pomar, nivel),
  );
}

/// Os parâmetros da Sopa no nível dado.
ParamsSopa sopaNo(int nivel) {
  final t = curva(nivel);
  return ParamsSopa(
    lado: _entre(7, 14, t),
    palavras: _entre(4, 10, t),
    // As diagonais entram cedo; as invertidas são a mecânica do nível 25.
    diagonais: nivel >= 10,
    invertidas: nivel >= Mecanica.aoContrario.desde,
    mecanicas: mecanicasDe(Jogo.sopa, nivel),
  );
}

/// Os parâmetros do Crossmath no nível dado.
ParamsCrossmath crossmathNo(int nivel) {
  final t = curva(nivel);
  return ParamsCrossmath(
    tecto: _entre(20, 999, t),
    // De 6 pistas a 4, e nunca abaixo — ver [ParamsCrossmath.pistas].
    pistas: _entre(6, ParamsCrossmath.minimoDePistas, t)
        .clamp(ParamsCrossmath.minimoDePistas, 9),
    mecanicas: mecanicasDe(Jogo.crossmath, nivel),
  );
}

/// O que muda no Water R Sort.
class ParamsFrascos {
  /// Cores distintas a arrumar. Cada cor tem exactamente [altura] blocos —
  /// é essa igualdade que faz o puzzle poder fechar.
  final int cores;

  /// Frascos vazios a mais das cores, para haver por onde mexer. Sem pelo
  /// menos um, não há jogada nenhuma possível de início.
  final int vazios;

  /// Blocos que cada frasco leva.
  ///
  /// TODOS têm a mesma altura, e isso não é falta de imaginação. Uma cor
  /// tem [altura] blocos e tem de caber inteira num frasco: um frasco mais
  /// curto do que os outros tornaria impossível arrumar a cor que lá fosse
  /// parar, e o nível ficava por fechar sem a criança perceber porquê.
  final int altura;

  /// Quantas jogadas ao contrário se dão a partir do tabuleiro arrumado.
  /// Quanto mais, mais longe do fim começa.
  final int baralhadelas;

  final Set<Mecanica> mecanicas;

  /// Frascos em cima da mesa.
  int get quantos => cores + vazios;

  const ParamsFrascos({
    required this.cores,
    required this.vazios,
    required this.altura,
    required this.baralhadelas,
    required this.mecanicas,
  });
}

/// Os parâmetros do Water R Sort no nível dado.
ParamsFrascos frascosNo(int nivel) {
  final t = curva(nivel);
  final m = mecanicasDe(Jogo.frascos, nivel);
  return ParamsFrascos(
    // De 3 a 8 pela curva, e a nona no nível 100 pela mecânica. São nove
    // ao todo porque nove são as cores que se distinguem mesmo umas das
    // outras no ecrã escuro — ver CorDoLiquido.
    cores: _entre(3, 8, t) + (m.contains(Mecanica.maisCores) ? 1 : 0),
    vazios: m.contains(Mecanica.semFolga) ? 1 : 2,
    altura: m.contains(Mecanica.maisFundo) ? 5 : 4,
    baralhadelas: _entre(6, 60, t),
    mecanicas: m,
  );
}

/// Os parâmetros da Memória no nível dado.
ParamsMemoria memoriaNo(int nivel) {
  final t = curva(nivel);
  return ParamsMemoria(
    pares: _entre(4, 12, t),
    espera: Duration(milliseconds: _entre(1200, 500, t)),
    mecanicas: mecanicasDe(Jogo.memoria, nivel),
  );
}
