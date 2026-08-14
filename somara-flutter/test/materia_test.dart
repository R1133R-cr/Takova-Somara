import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A matéria de cada nível.
///
/// Na fase C as crianças acharam as perguntas secas: chegavam ao exercício
/// sem ninguém lhes ter relembrado nada. Um enunciado da 4ª classe sem
/// contexto é um teste, não uma aula — a app avaliava sem nunca ter
/// ensinado. Estes testes seguram a aula que passou a vir antes.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;

  setUpAll(() async {
    c = await Conteudo.carregar();
  });

  Iterable<({String onde, Nivel nivel})> todosOsNiveis() sync* {
    for (final curso in c.cursos) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          yield (onde: '${curso.id}:${u.id}:${n.id}', nivel: n);
        }
      }
    }
  }

  test('todos os níveis têm matéria', () {
    final sem = [
      for (final x in todosOsNiveis())
        if (x.nivel.materia == null) '${x.onde} (${x.nivel.titulo})',
    ];
    expect(sem, isEmpty, reason: 'níveis que entram a seco no exercício');
  });

  test('a matéria tem as três partes preenchidas', () {
    final vazias = <String>[];
    for (final x in todosOsNiveis()) {
      final m = x.nivel.materia;
      if (m == null) continue;
      if (m.explica.trim().isEmpty) vazias.add('${x.onde}: explica');
      if (m.exemplo.trim().isEmpty) vazias.add('${x.onde}: exemplo');
      if (m.lembra.trim().isEmpty) vazias.add('${x.onde}: lembra');
    }
    expect(vazias, isEmpty);
  });

  test('a aula cabe no ecrã e na cabeça de uma criança', () {
    // Um limite generoso, mas um limite: a partir daqui deixa de ser um
    // lembrete antes do exercício e passa a ser um texto que ninguém lê.
    final compridas = <String>[];
    for (final x in todosOsNiveis()) {
      final m = x.nivel.materia;
      if (m == null) continue;
      if (m.explica.length > 240) {
        compridas.add('${x.onde}: explica tem ${m.explica.length}');
      }
      if (m.exemplo.length > 200) {
        compridas.add('${x.onde}: exemplo tem ${m.exemplo.length}');
      }
      if (m.lembra.length > 110) {
        compridas.add('${x.onde}: lembra tem ${m.lembra.length}');
      }
    }
    expect(compridas, isEmpty);
  });

  test('a aula é lida em voz alta e o ficheiro existe', () {
    // É a parte que serve as crianças da 1ª e da 2ª classe, que ainda não
    // lêem. Sem o ficheiro, a aula fica muda justamente para quem mais
    // precisa de a ouvir — e ninguém daria por isso a olhar para o ecrã.
    final semAudio = <String>[];
    final emFalta = <String>[];
    for (final x in todosOsNiveis()) {
      final m = x.nivel.materia;
      if (m == null) continue;
      final f = m.audio;
      if (f == null) {
        semAudio.add(x.onde);
      } else if (!File('assets/audio/$f').existsSync()) {
        emFalta.add('${x.onde} -> $f');
      }
    }
    expect(semAudio, isEmpty, reason: 'aulas sem áudio atribuído');
    expect(emFalta, isEmpty, reason: 'áudio atribuído mas ficheiro inexistente');
  });
}
