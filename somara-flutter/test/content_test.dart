import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// Guarda o pipeline de conteúdo: o content.json é gerado a partir do
/// content.js da versão web, e um índice de resposta fora do intervalo
/// só daria erro com a criança já a olhar para o exercício.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;

  setUpAll(() async {
    c = await Conteudo.carregar();
  });

  test('carrega Matemática e Português da 1ª e da 2ª classe', () {
    expect(c.cursos.length, 4);
    for (final classe in ['1ª classe', '2ª classe']) {
      final daClasse = c.cursos.where((x) => x.classe == classe);
      expect(daClasse.length, 2, reason: classe);
      expect(daClasse.map((x) => x.disciplina),
          containsAll(['Matemática', 'Português']), reason: classe);
    }
  });

  test('todas as 253 questões sobreviveram à migração', () {
    final total = c.cursos
        .expand((cu) => cu.units)
        .expand((u) => u.niveis)
        .expand((n) => n.questoes)
        .length;
    expect(total, 253);
  });

  test('cada classe tem conteúdo suficiente para uma amarelinha', () {
    for (final curso in c.cursos) {
      expect(curso.niveisEmSequencia.length, greaterThanOrEqualTo(8),
          reason: '${curso.id}: poucos níveis para o mapa fazer sentido');
    }
  });

  test('os cinco tipos de exercício estão representados', () {
    final tipos = c.cursos
        .expand((cu) => cu.units)
        .expand((u) => u.niveis)
        .expand((n) => n.questoes)
        .map((q) => q.runtimeType)
        .toSet();
    expect(tipos, containsAll([QCount, QChoice, QInput, QMatch, QDrag]));
  });

  test('nenhum índice de resposta cai fora das opções', () {
    for (final curso in c.cursos) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          for (final q in n.questoes) {
            final onde = '${curso.id}/${u.id}/${n.id}';
            switch (q) {
              case QCount():
                expect(q.a, inInclusiveRange(0, q.options.length - 1), reason: onde);
                expect(q.n, greaterThan(0), reason: onde);
              case QChoice():
                expect(q.a, inInclusiveRange(0, q.options.length - 1), reason: onde);
              case QInput():
                expect(q.a.trim(), isNotEmpty, reason: onde);
              case QDrag():
                expect(q.a, inInclusiveRange(0, q.zones.length - 1), reason: onde);
              case QMatch():
                expect(q.pairs.length, greaterThanOrEqualTo(2), reason: onde);
            }
          }
        }
      }
    }
  });

  test('cada pergunta tem o seu áudio, e o ficheiro existe mesmo', () {
    // Um áudio em falta não rebenta a app — ela segue em silêncio. É
    // justamente por isso que precisa de teste: ninguém daria por ela até
    // uma criança que não lê ficar encalhada numa pergunta muda.
    var semAudio = <String>[];
    var emFalta = <String>[];

    for (final curso in c.cursos) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          for (final q in n.questoes) {
            final onde = '${curso.id}/${u.id}/${n.id}: ${q.q}';
            if (q.audio == null) {
              semAudio.add(onde);
              continue;
            }
            if (!File('assets/audio/${q.audio}').existsSync()) {
              emFalta.add('$onde -> ${q.audio}');
            }
          }
        }
      }
    }

    expect(semAudio, isEmpty, reason: 'perguntas sem áudio atribuído');
    expect(emFalta, isEmpty, reason: 'áudio atribuído mas ficheiro inexistente');
  });

  test('nenhum nível fica sem enunciado ou sem questões', () {
    for (final curso in c.cursos) {
      for (final lv in curso.niveisEmSequencia) {
        expect(lv.nivel.questoes, isNotEmpty, reason: lv.nivel.id);
        expect(lv.nivel.titulo.trim(), isNotEmpty, reason: lv.nivel.id);
        for (final q in lv.nivel.questoes) {
          expect(q.q.trim(), isNotEmpty, reason: '${lv.nivel.id}: enunciado vazio');
        }
      }
    }
  });
}
