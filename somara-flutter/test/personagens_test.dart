import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/personagens.dart';

/// O elenco contra o currículo.
///
/// Serve uma coisa concreta: no dia em que entrar uma disciplina nova —
/// Desenho na 10ª, Filosofia, o que for —, este teste diz que ela ficou sem
/// professor, em vez de a app o descobrir no ecrã de uma criança. Guarda
/// também as partilhas que foram decididas em conversa, porque são o tipo de
/// decisão que alguém desfaz sem saber que foi decidida.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;

  setUpAll(() async {
    c = await Conteudo.carregar();
  });

  test('todas as disciplinas do currículo têm quem as ensine', () {
    final semProfessor = <String>{};
    for (final curso in c.cursos) {
      if (personagemDe(curso.disciplina) == null) {
        semProfessor.add(curso.disciplina);
      }
    }
    expect(
      semProfessor,
      isEmpty,
      reason: 'disciplinas sem personagem: ${semProfessor.join(', ')} — '
          'acrescenta a ficha em docs/personagens/ e a entrada no elenco',
    );
  });

  test('nenhuma personagem ensina uma disciplina que não existe', () {
    final doCurriculo = {for (final x in c.cursos) x.disciplina};
    for (final p in elenco) {
      for (final d in p.disciplinas) {
        expect(
          doCurriculo,
          contains(d),
          reason: '${p.nome} ensina "$d", que não está no content.json',
        );
      }
    }
  });

  test('cada disciplina tem um professor só', () {
    for (final curso in c.cursos) {
      final quantos = elenco
          .where((p) => p.disciplinas.contains(curso.disciplina))
          .length;
      expect(quantos, 1, reason: '${curso.disciplina} tem $quantos');
    }
  });

  test('as partilhas são as três combinadas, e só essas', () {
    // Ciências Naturais com Biologia e Ciências Sociais com História, por
    // ser a mesma matéria a crescer; Educação Visual com Educação Visual e
    // Ofícios, por ser o mesmo nome em duas fases do currículo.
    final partilham = {
      for (final p in elenco)
        if (p.disciplinas.length > 1) p.slug: p.disciplinas.toSet(),
    };
    expect(partilham, {
      'lolo': {'Ciências Naturais', 'Biologia'},
      'nzou': {'Ciências Sociais', 'História'},
      'pintinha': {'Educação Visual e Ofícios', 'Educação Visual'},
    });
  });

  test('o Inglês e o Francês não partilham personagem', () {
    // Na 8ª e na 9ª classe o aluno tem as duas disciplinas no mesmo ano.
    final ing = personagemDe('Inglês');
    final fra = personagemDe('Francês');
    expect(ing, isNotNull);
    expect(fra, isNotNull);
    expect(ing!.slug, isNot(fra!.slug));
  });

  test('os nomes e os slugs não se repetem', () {
    expect(
      elenco.map((p) => p.slug).toSet().length,
      elenco.length,
      reason: 'dois slugs iguais dariam o mesmo nome de ficheiro de desenho',
    );
    expect(elenco.map((p) => p.nome).toSet().length, elenco.length);
  });

  test('o Roby e a Hiena não ensinam disciplina nenhuma', () {
    // O Roby está em toda a app e a Ri-Ri só existe nas histórias — nunca
    // dentro de um exercício.
    expect(personagemDe('Matemática')!.slug, isNot('roby'));
    for (final slug in ['roby', 'riri']) {
      final p = elenco.firstWhere((x) => x.slug == slug);
      expect(p.disciplinas, isEmpty);
    }
  });

  test('cada personagem tem a sua ficha escrita', () {
    for (final p in elenco) {
      final f = File('docs/personagens/${p.slug}.md');
      expect(
        f.existsSync(),
        isTrue,
        reason: '${p.nome} está no elenco mas não tem ficha em '
            'docs/personagens/${p.slug}.md',
      );
      // Uma ficha vazia é pior do que nenhuma: dá a entender que o trabalho
      // está feito. As que existem andam nas 2 000 letras.
      expect(f.readAsStringSync().length, greaterThan(800),
          reason: 'a ficha de ${p.nome} está por escrever');
    }
  });

  test('o caminho do desenho do Roby é o que já existe', () {
    // Os trinta e oito desenhos dele são anteriores a esta convenção.
    final roby = elenco.firstWhere((p) => p.slug == 'roby');
    expect(roby.desenho('feliz'), 'assets/img/roby-feliz.png');
    expect(File('assets/img/roby-feliz.png').existsSync(), isTrue);
  });

  test('os outros seguem a convenção nova', () {
    final escamas = elenco.firstWhere((p) => p.slug == 'escamas');
    expect(
      escamas.desenho('a-explicar'),
      'assets/img/personagem-escamas-a-explicar.png',
    );
  });
}
