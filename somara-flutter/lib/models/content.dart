import 'dart:convert';
import 'package:flutter/services.dart' show rootBundle;

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
  const Unidade({required this.id, required this.titulo, required this.niveis});

  factory Unidade.fromJson(Map<String, dynamic> j) => Unidade(
        id: j['id'] as String,
        titulo: j['titulo'] as String,
        niveis: (j['niveis'] as List)
            .map((n) => Nivel.fromJson(n as Map<String, dynamic>))
            .toList(),
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

  final List<Unidade> units;

  const Curso({
    required this.id,
    required this.disciplina,
    required this.classe,
    required this.tag,
    required this.units,
    this.abrev,
  });

  /// O que se mostra na aba.
  String get rotulo => abrev ?? disciplina;

  factory Curso.fromJson(Map<String, dynamic> j) => Curso(
        id: j['id'] as String,
        disciplina: j['disciplina'] as String,
        classe: j['classe'] as String,
        tag: (j['tag'] ?? '') as String,
        abrev: j['abrev'] as String?,
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
