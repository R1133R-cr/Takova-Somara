import 'dart:convert';
import 'package:flutter/services.dart' show rootBundle;

import 'algoritmo_escrito.dart';
import '../painters/cenas.dart';

/// Modelos do currículo. Espelham a estrutura do content.json
/// (gerado a partir do content.js da versão web, conteúdo extraído dos
/// manuais reais da 1ª classe).

/// Os cinco tipos de exercício. `sealed` obriga o switch a cobrir todos —
/// se amanhã acrescentarmos um tipo, o compilador aponta cada sítio que
/// falta tratar, em vez de falhar silenciosamente em produção.
sealed class Questao {
  final String q;

  /// O desenho que acompanha a pergunta, quando ela fala de uma figura.
  final Figura? figura;

  /// As cores que a pergunta mostra, quando é de Educação Visual.
  final Cores? cores;

  /// Ficheiro do enunciado lido em voz alta (assets/audio/…), gerado à parte
  /// e gravado no content.json. Vem pronto para a app não ter de calcular
  /// nada — e não existe para enunciados que sejam só emoji.
  final String? audio;

  const Questao(this.q, this.audio, {this.figura, this.cores});

  static Questao fromJson(Map<String, dynamic> j) {
    final q = (j['q'] ?? '') as String;
    final a = j['audio'] as String?;
    final fig = j['figura'] == null
        ? null
        : Figura.fromJson(j['figura'] as Map<String, dynamic>);
    final cor = j['cores'] == null
        ? null
        : Cores.fromJson(j['cores'] as Map<String, dynamic>);
    switch (j['t']) {
      case 'count':
        return QCount(
          q,
          a,
          figura: fig,
          cores: cor,
          emoji: j['emoji'] as String,
          n: j['n'] as int,
          options: (j['options'] as List).cast<String>(),
          a: j['a'] as int,
        );
      case 'choice':
        return QChoice(
          q,
          a,
          figura: fig,
          cores: cor,
          options: (j['options'] as List).cast<String>(),
          a: j['a'] as int,
        );
      case 'input':
        return QInput(q, a, figura: fig, cores: cor, resposta: '${j['a']}');
      case 'match':
        return QMatch(
          q,
          a,
          figura: fig,
          cores: cor,
          pairs: (j['pairs'] as List)
              .map((p) => ((p as List).cast<String>()))
              .map((p) => (p[0], p[1]))
              .toList(),
        );
      case 'grelha':
        return QGrelha(
          q,
          a,
          figura: fig,
          cores: cor,
          operacao: Operacao.values.byName(j['op'] as String),
          x: j['x'] as int,
          y: j['y'] as int,
        );
      case 'sequencia':
        return QSequencia(
          q,
          a,
          figura: fig,
          cores: cor,
          passos: (j['passos'] as List).cast<String>(),
        );
      case 'grupos':
        return QGrupos(
          q,
          a,
          figura: fig,
          cores: cor,
          grupos: (j['grupos'] as List).cast<String>(),
          itens: [
            for (final i in (j['itens'] as List))
              (nome: (i as Map)['nome'] as String, grupo: i['g'] as int),
          ],
        );
      case 'cenario':
        return QCenario(
          q,
          a,
          figura: fig,
          cores: cor,
          cena: Cena.values.byName(j['cena'] as String),
          alvos: [
            for (final z in (j['alvos'] as List))
              (
                x: ((z as Map)['x'] as num).toDouble(),
                y: (z['y'] as num).toDouble(),
                peca: z['peca'] as String,
              ),
          ],
        );
      case 'drag':
        return QDrag(
          q,
          a,
          figura: fig,
          cores: cor,
          chip: j['chip'] as String,
          zones: (j['zones'] as List).cast<String>(),
          a: j['a'] as int,
        );
      default:
        throw FormatException('Tipo de questão desconhecido: ${j['t']}');
    }
  }
}

/// Contar objectos (emoji repetido n vezes) e escolher o número.
class QCount extends Questao {
  final String emoji;
  final int n;
  final List<String> options;
  final int a;
  const QCount(super.q, super.audio, {super.figura, super.cores, required this.emoji, required this.n, required this.options, required this.a});
}

/// Escolha múltipla.
class QChoice extends Questao {
  final List<String> options;
  final int a;
  const QChoice(super.q, super.audio, {super.figura, super.cores, required this.options, required this.a});
}

/// Resposta escrita — comparada sem distinguir maiúsculas nem acentos.
class QInput extends Questao {
  final String a;
  const QInput(super.q, super.audio, {super.figura, super.cores, required String resposta}) : a = resposta;
}

/// Ligar pares (esquerda ↔ direita).
class QMatch extends Questao {
  final List<(String, String)> pairs;
  const QMatch(super.q, super.audio, {super.figura, super.cores, required this.pairs});
}

/// Arrastar uma peça para a zona certa.
class QDrag extends Questao {
  final String chip;
  final List<String> zones;
  final int a;
  const QDrag(super.q, super.audio, {super.figura, super.cores, required this.chip, required this.zones, required this.a});
}

/// Pôr passos pela ordem certa.
///
/// Os [passos] vêm no content.json **já pela ordem certa** — é a ordem que
/// se guarda, porque é a única que interessa saber. Quem mostra é que
/// baralha, e baralha de maneira fixa: dois telemóveis com a mesma pergunta
/// têm de a mostrar igual.
class QSequencia extends Questao {
  final List<String> passos;

  const QSequencia(
    super.q,
    super.audio, {
    super.figura,
    super.cores,
    required this.passos,
  });

  /// A ordem baralhada em que se mostram, pelos índices da ordem certa.
  ///
  /// Nunca devolve a ordem já feita: uma sequência que aparece resolvida não
  /// é um exercício, é um texto.
  List<int> baralhados() {
    final n = passos.length;
    if (n < 2) return [0];
    // Um deslocamento fixo, dependente do enunciado: sempre o mesmo, nunca
    // a identidade, e sem precisar de guardar mais nada no ficheiro.
    var salto = 0;
    for (final u in q.codeUnits) {
      salto = (salto + u) % n;
    }
    if (salto == 0) salto = 1;
    final ordem = [for (var i = 0; i < n; i++) (i * salto + salto) % n];
    return ordem.toSet().length == n
        ? ordem
        : [for (var i = 0; i < n; i++) (i + 1) % n];
  }

  bool certa(List<int> ordemDada) {
    if (ordemDada.length != passos.length) return false;
    for (var i = 0; i < passos.length; i++) {
      if (ordemDada[i] != i) return false;
    }
    return true;
  }
}

/// Arrastar cada coisa para o grupo a que pertence.
class QGrupos extends Questao {
  final List<String> grupos;
  final List<({String nome, int grupo})> itens;

  const QGrupos(
    super.q,
    super.audio, {
    super.figura,
    super.cores,
    required this.grupos,
    required this.itens,
  });

  /// [posto] é o grupo onde cada item foi largado, ou nulo se ainda não foi.
  bool certa(List<int?> posto) {
    if (posto.length != itens.length) return false;
    for (var i = 0; i < itens.length; i++) {
      if (posto[i] != itens[i].grupo) return false;
    }
    return true;
  }
}

/// Largar peças nos sítios certos de um cenário desenhado.
///
/// O cenário nasce dos dados e não de um ficheiro de imagem, como as figuras
/// de geometria e as manchas de cor: um desenho em código muda com o tema,
/// não pesa nada, e não fica desfocado num ecrã grande.
class QCenario extends Questao {
  final Cena cena;

  /// Onde cada peça tem de ir parar, em coordenadas de 0 a 1 sobre o
  /// desenho — para o alvo acompanhar o cenário em qualquer tamanho de ecrã.
  final List<({double x, double y, String peca})> alvos;

  const QCenario(
    super.q,
    super.audio, {
    super.figura,
    super.cores,
    required this.cena,
    required this.alvos,
  });

  List<String> get pecas => [for (final a in alvos) a.peca];

  /// [posto] é a peça largada em cada alvo, ou nulo.
  bool certa(List<String?> posto) {
    if (posto.length != alvos.length) return false;
    for (var i = 0; i < alvos.length; i++) {
      if (posto[i] != alvos[i].peca) return false;
    }
    return true;
  }
}

/// Uma conta armada, para preencher casinha a casinha.
///
/// Não guarda a grelha: guarda a operação e os dois números, e a grelha
/// calcula-se. Guardá-la desenhada seria guardar uma resposta — e bastava
/// alguém abrir o `content.json` para a ver.
class QGrelha extends Questao {
  final Operacao operacao;
  final int x;
  final int y;

  const QGrelha(
    super.q,
    super.audio, {
    super.figura,
    super.cores,
    required this.operacao,
    required this.x,
    required this.y,
  });

  GrelhaDaConta get conta => GrelhaDaConta.de(operacao, x, y);
}

/// As formas que a app sabe desenhar.
enum FormaGeo { quadrado, rectangulo, triangulo, circulo, cubo }

/// A figura que acompanha uma pergunta de geometria.
///
/// Guardada como números e não como imagem: a figura desenha-se a partir
/// destes valores, com a proporcao certa e a medida escrita no sitio certo.
/// Um rectangulo de 8 por 3 tem de SER mais comprido do que alto, senao
/// ensina-se a crianca que as medidas escritas nao querem dizer nada.
class Figura {
  final FormaGeo forma;

  /// Lado, comprimento, base ou raio, conforme a forma.
  final double a;

  /// Largura ou altura, quando a forma precisa de duas medidas.
  final double? b;

  /// "cm" — ou vazio, quando a figura serve so para se ver a forma e as
  /// medidas nao interessam ("Quantos lados tem esta figura?").
  final String unidade;

  const Figura({
    required this.forma,
    required this.a,
    this.b,
    this.unidade = 'cm',
  });

  /// A medida escrita ao lado do desenho. Vazia quando nao ha unidade.
  String medidaDe(double valor) {
    if (unidade.isEmpty) return '';
    final inteiro = valor == valor.roundToDouble();
    return '${inteiro ? valor.round() : valor} $unidade';
  }

  static FormaGeo _formaDe(String nome) => switch (nome) {
        'quadrado' => FormaGeo.quadrado,
        'rectangulo' => FormaGeo.rectangulo,
        'triangulo' => FormaGeo.triangulo,
        'circulo' => FormaGeo.circulo,
        'cubo' => FormaGeo.cubo,
        _ => throw FormatException('Forma desconhecida: $nome'),
      };

  factory Figura.fromJson(Map<String, dynamic> j) => Figura(
        forma: _formaDe(j['forma'] as String),
        a: (j['a'] as num).toDouble(),
        b: j['b'] == null ? null : (j['b'] as num).toDouble(),
        unidade: (j['unidade'] ?? 'cm') as String,
      );

  @override
  bool operator ==(Object other) =>
      other is Figura &&
      other.forma == forma &&
      other.a == a &&
      other.b == b &&
      other.unidade == unidade;

  @override
  int get hashCode => Object.hash(forma, a, b, unidade);
}

/// As cores que uma pergunta de Educação Visual mostra.
///
/// Porque é que isto existe
/// ------------------------
/// A Educação Visual ensina-se a fazer: desenhar, pintar, misturar tintas.
/// Perguntar «que cor dá o amarelo com o azul?» com três palavras por baixo
/// não ensina cor nenhuma — ensina vocabulário. A criança que nunca viu as
/// duas tintas juntar-se acerta de cor e continua sem saber.
///
/// Por isso a pergunta mostra as cores. As duas tintas aparecem lado a lado
/// com um sinal de mais entre elas, e cada resposta traz a sua mancha de cor
/// ao lado do nome. A criança escolhe a COR e aprende o nome dela ao mesmo
/// tempo — que é a ordem certa.
///
/// Guardadas como números e não como imagens, pela mesma razão da [Figura]:
/// nascem do conteúdo, não de um ficheiro que alguém tem de desenhar.
class Cores {
  /// As tintas que se juntam, mostradas com um "+" entre elas e um "=" no
  /// fim. Vazia quando a pergunta não é de mistura.
  final List<int> mistura;

  /// Uma cor por opção de resposta, na mesma ordem das opções. Vazia
  /// quando as respostas são palavras e não cores.
  final List<int> opcoes;

  const Cores({this.mistura = const [], this.opcoes = const []});

  bool get temMistura => mistura.length >= 2;

  /// "#F2C200" → 0xFFF2C200. Escrito em hexadecimal no content.json porque
  /// é assim que uma cor se lê e se corrige à mão.
  static int _daHex(String s) =>
      int.parse('FF${s.replaceFirst('#', '')}', radix: 16);

  static List<int> _lista(Object? v) => v == null
      ? const []
      : (v as List).map((x) => _daHex(x as String)).toList();

  factory Cores.fromJson(Map<String, dynamic> j) => Cores(
        mistura: _lista(j['mistura']),
        opcoes: _lista(j['opcoes']),
      );

  @override
  bool operator ==(Object other) =>
      other is Cores &&
      other.mistura.join() == mistura.join() &&
      other.opcoes.join() == opcoes.join();

  @override
  int get hashCode => Object.hash(mistura.join(), opcoes.join());
}

/// A matéria de um nível — o que se ensina antes de se perguntar.
///
/// As crianças da fase C acharam as perguntas secas: chegavam ao exercício
/// sem ninguém lhes ter relembrado a matéria, e um enunciado da 4ª classe
/// sem contexto é um teste, não uma aula. São três partes de propósito:
/// explicar, mostrar um caso feito, e deixar uma frase curta que se leve
/// para o exercício.
class Materia {
  final String explica;
  final String exemplo;
  final String lembra;

  /// Enunciado lido em voz alta, para quem ainda não lê.
  final String? audio;

  const Materia({
    required this.explica,
    required this.exemplo,
    required this.lembra,
    this.audio,
  });

  factory Materia.fromJson(Map<String, dynamic> j) => Materia(
        explica: j['explica'] as String,
        exemplo: j['exemplo'] as String,
        lembra: j['lembra'] as String,
        audio: j['audio'] as String?,
      );
}

class Nivel {
  final String id;
  final String titulo;
  final List<Questao> questoes;

  /// Nula enquanto a matéria daquele nível não estiver escrita. A app trata
  /// disso sem se queixar: sem matéria, entra-se directamente no exercício,
  /// como era antes.
  final Materia? materia;

  const Nivel({
    required this.id,
    required this.titulo,
    required this.questoes,
    this.materia,
  });

  factory Nivel.fromJson(Map<String, dynamic> j) => Nivel(
        id: j['id'] as String,
        titulo: j['titulo'] as String,
        materia: j['materia'] == null
            ? null
            : Materia.fromJson(j['materia'] as Map<String, dynamic>),
        questoes: (j['questoes'] as List)
            .map((q) => Questao.fromJson(q as Map<String, dynamic>))
            .toList(),
      );
}

class Unidade {
  final String id;
  final String titulo;
  final List<Nivel> niveis;

  /// O vocabulário desta unidade, para a sopa de letras da matéria.
  ///
  /// Vazio na maior parte das unidades, e é assim que deve ser: só entram
  /// palavras que **dispensam acento e cedilha**, porque a grelha da sopa é
  /// de maiúsculas simples. Mostrar "SAUDE" na lista para se procurar
  /// "SAUDE" nas letras ensinaria a escrever mal, e numa app de escola isso
  /// não se faz — por isso a palavra fica de fora em vez de se lhe tirar o
  /// acento.
  final List<String> palavras;

  const Unidade({
    required this.id,
    required this.titulo,
    required this.niveis,
    this.palavras = const [],
  });

  factory Unidade.fromJson(Map<String, dynamic> j) => Unidade(
        id: j['id'] as String,
        titulo: j['titulo'] as String,
        niveis: (j['niveis'] as List)
            .map((n) => Nivel.fromJson(n as Map<String, dynamic>))
            .toList(),
        palavras: ((j['palavras'] as List?) ?? const []).cast<String>(),
      );
}

class Curso {
  final String id;

  /// Nome próprio da disciplina, como no currículo — "Ciências Naturais" e
  /// "Ciências Sociais" são disciplinas diferentes e não se abreviam uma na
  /// outra.
  final String disciplina;

  final String classe;
  final String tag;

  /// Nome curto para a barra de disciplinas, onde o espaço é pouco.
  /// Sem isto, "Ciências Naturais" ao lado de "Ciências Sociais" fica
  /// ilegível no telemóvel. Quando falta, usa-se o nome inteiro.
  final String? abrev;

  /// De onde saiu o conteúdo deste curso.
  ///
  /// Quase todos vêm de um manual escolar moçambicano, e nesses este campo
  /// não existe — a fonte está escrita na ferramenta que os gerou.
  ///
  /// Está aqui para o caso contrário: um curso montado SEM livro, a partir
  /// do que o currículo descreve e do que se sabe das classes vizinhas.
  /// Isso tem de ficar dito onde alguém tropece nele, e não só no commit.
  ///
  /// Hoje é um só: a Educação Visual da 4ª classe, que não tem manual
  /// publicado. Se aparecer um, tira-se este campo.
  final String? fonte;

  /// Este curso foi montado sem manual?
  bool get provisorio => fonte != null;

  final List<Unidade> units;

  const Curso({
    required this.id,
    required this.disciplina,
    required this.classe,
    required this.tag,
    required this.units,
    this.abrev,
    this.fonte,
  });

  /// O que se mostra na aba.
  String get rotulo => abrev ?? disciplina;

  factory Curso.fromJson(Map<String, dynamic> j) => Curso(
        id: j['id'] as String,
        disciplina: j['disciplina'] as String,
        classe: j['classe'] as String,
        tag: (j['tag'] ?? '') as String,
        abrev: j['abrev'] as String?,
        fonte: j['fonte'] as String?,
        units: (j['units'] as List)
            .map((u) => Unidade.fromJson(u as Map<String, dynamic>))
            .toList(),
      );

  /// Todos os níveis do curso em sequência — é assim que a amarelinha
  /// os apresenta (uma fila contínua, ignorando a fronteira das unidades).
  List<({Unidade unit, Nivel nivel})> get niveisEmSequencia => [
        for (final u in units)
          for (final n in u.niveis) (unit: u, nivel: n),
      ];
}

class Conteudo {
  final List<Curso> cursos;

  /// Data da última alteração ao currículo, como número (ex.: 20260807).
  /// É por este número que a app decide se o que está na internet é mais
  /// recente do que aquilo que já tem.
  final int versao;

  const Conteudo(this.cursos, {this.versao = 0});

  /// Lê o conteúdo que veio dentro da app.
  static Future<Conteudo> carregar() async {
    return deTexto(await rootBundle.loadString('assets/content.json'));
  }

  /// Lê conteúdo a partir de texto — usado tanto para o que vem dentro da
  /// app como para o que se descarrega. Rebenta com excepção se o texto
  /// estiver mal formado, e é isso que se quer: quem descarrega apanha o
  /// erro e fica com o conteúdo anterior.
  static Conteudo deTexto(String texto) {
    final j = json.decode(texto) as Map<String, dynamic>;
    final cursos = (j['cursos'] as List)
        .map((c) => Curso.fromJson(c as Map<String, dynamic>))
        .toList();
    return Conteudo(cursos, versao: (j['versao'] ?? 0) as int);
  }
}
