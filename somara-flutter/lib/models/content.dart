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

  /// Ficheiro do enunciado lido em voz alta (assets/audio/…), gerado à parte
  /// e gravado no content.json. Vem pronto para a app não ter de calcular
  /// nada — e não existe para enunciados que sejam só emoji.
  final String? audio;

  const Questao(this.q, this.audio);

  static Questao fromJson(Map<String, dynamic> j) {
    final q = (j['q'] ?? '') as String;
    final a = j['audio'] as String?;
    switch (j['t']) {
      case 'count':
        return QCount(
          q,
          a,
          emoji: j['emoji'] as String,
          n: j['n'] as int,
          options: (j['options'] as List).cast<String>(),
          a: j['a'] as int,
        );
      case 'choice':
        return QChoice(
          q,
          a,
          options: (j['options'] as List).cast<String>(),
          a: j['a'] as int,
        );
      case 'input':
        return QInput(q, a, resposta: '${j['a']}');
      case 'match':
        return QMatch(
          q,
          a,
          pairs: (j['pairs'] as List)
              .map((p) => ((p as List).cast<String>()))
              .map((p) => (p[0], p[1]))
              .toList(),
        );
      case 'drag':
        return QDrag(
          q,
          a,
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
  const QCount(super.q, super.audio, {required this.emoji, required this.n, required this.options, required this.a});
}

/// Escolha múltipla.
class QChoice extends Questao {
  final List<String> options;
  final int a;
  const QChoice(super.q, super.audio, {required this.options, required this.a});
}

/// Resposta escrita — comparada sem distinguir maiúsculas nem acentos.
class QInput extends Questao {
  final String a;
  const QInput(super.q, super.audio, {required String resposta}) : a = resposta;
}

/// Ligar pares (esquerda ↔ direita).
class QMatch extends Questao {
  final List<(String, String)> pairs;
  const QMatch(super.q, super.audio, {required this.pairs});
}

/// Arrastar uma peça para a zona certa.
class QDrag extends Questao {
  final String chip;
  final List<String> zones;
  final int a;
  const QDrag(super.q, super.audio, {required this.chip, required this.zones, required this.a});
}

class Nivel {
  final String id;
  final String titulo;
  final List<Questao> questoes;
  const Nivel({required this.id, required this.titulo, required this.questoes});

  factory Nivel.fromJson(Map<String, dynamic> j) => Nivel(
        id: j['id'] as String,
        titulo: j['titulo'] as String,
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
  final String disciplina;
  final String classe;
  final String tag;
  final List<Unidade> units;
  const Curso({
    required this.id,
    required this.disciplina,
    required this.classe,
    required this.tag,
    required this.units,
  });

  factory Curso.fromJson(Map<String, dynamic> j) => Curso(
        id: j['id'] as String,
        disciplina: j['disciplina'] as String,
        classe: j['classe'] as String,
        tag: (j['tag'] ?? '') as String,
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
  const Conteudo(this.cursos);

  static Future<Conteudo> carregar() async {
    final raw = await rootBundle.loadString('assets/content.json');
    final j = json.decode(raw) as Map<String, dynamic>;
    return Conteudo(
      (j['cursos'] as List)
          .map((c) => Curso.fromJson(c as Map<String, dynamic>))
          .toList(),
    );
  }
}
