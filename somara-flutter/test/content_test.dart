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

  test('cobre o primário inteiro, e o primeiro degrau do secundário', () {
    expect(c.cursos.length, 25);

    final classes = c.cursos.map((x) => x.classe).toSet();
    expect(classes, {
      '1ª classe', '2ª classe', '3ª classe',
      '4ª classe', '5ª classe', '6ª classe',
      // A 7ª já não é primário: pela Lei nº 18/2018 o Ensino Primário são
      // seis classes, e a 7ª abre o 1º ciclo do Ensino Secundário Geral.
      // Continua dentro dos nove anos de escolaridade obrigatória, e é
      // por isso que a app a cobre.
      '7ª classe',
    });
  });

  test('cada classe traz as disciplinas que lhe pertencem', () {
    // Da 1ª à 3ª são duas: Matemática e Português.
    for (final classe in ['1ª classe', '2ª classe', '3ª classe']) {
      final daClasse = c.cursos.where((x) => x.classe == classe);
      expect(daClasse.length, 2, reason: classe);
      expect(daClasse.map((x) => x.disciplina),
          containsAll(['Matemática', 'Português']), reason: classe);
    }

    // O II ciclo — 4ª, 5ª e 6ª — tem as quatro disciplinas académicas. A
    // 4ª esteve incompleta durante meses, com Matemática e Ciências
    // Naturais só; o Português e as Ciências Sociais chegaram com os
    // Cadernos de Actividades do MINEDH.
    for (final classe in ['4ª classe', '5ª classe', '6ª classe']) {
      final daClasse =
          c.cursos.where((x) => x.classe == classe).map((x) => x.disciplina);
      expect(
          daClasse,
          containsAll([
            'Matemática',
            'Português',
            'Ciências Naturais',
            'Ciências Sociais',
          ]),
          reason: classe);
    }

    // Educação Visual e Ofícios é a quinta disciplina do II ciclo, e o
    // ciclo fica coberto por inteiro.
    for (final classe in ['4ª classe', '5ª classe', '6ª classe']) {
      expect(
          c.cursos.where((x) => x.classe == classe).map((x) => x.disciplina),
          contains('Educação Visual e Ofícios'),
          reason: classe);
    }
  });

  test('Naturais e Sociais nunca se confundem uma com a outra', () {
    // O erro que já se cometeu uma vez: chamar "Ciências" a uma delas
    // apagava a distinção. São disciplinas separadas, com manuais próprios.
    final nomes = c.cursos.map((x) => x.disciplina).toSet();
    expect(nomes, isNot(contains('Ciências')));
    for (final curso in c.cursos.where((x) => x.disciplina.startsWith('Ciências'))) {
      expect(curso.disciplina, anyOf('Ciências Naturais', 'Ciências Sociais'));
      expect(curso.abrev, isNotNull,
          reason: '${curso.id}: nome longo precisa de abreviatura para a aba');
    }
  });

  test('o corpus de perguntas não encolhe sem se dar por isso', () {
    // O número sobe quando se acrescenta conteúdo, e isso tem de ser um
    // acto deliberado: se descer, ou subir sem ninguém ter escrito nada,
    // perdeu-se ou duplicou-se conteúdo numa migração.
    //
    //   851  até à 0.19.3
    //   908  com o Português da 4ª classe (57 perguntas)
    //   958  com as Ciências Sociais da 4ª classe (50 perguntas)
    //   992  com a Educação Visual da 6ª classe (34 perguntas)
    //  1027  com a Educação Visual da 5ª classe (35 perguntas)
    //  1060  com a Educação Visual da 4ª classe (33 perguntas)
    //  1076  com os exercícios interactivos de Ciências (16)
    //  1150  com a Matemática da 7ª classe (74)
    //  1219  com o Português da 7ª classe (69)
    //  1274  com a História da 7ª classe (55)
    //  1349  com a Geografia da 7ª classe (75)
    final total = c.cursos
        .expand((cu) => cu.units)
        .expand((u) => u.niveis)
        .expand((n) => n.questoes)
        .length;
    expect(total, 1349);
  });

  test('as cores da Educação Visual estão bem formadas', () {
    // A Educação Visual mostra a cor em vez de a nomear: a pergunta traz
    // as tintas a misturar e cada resposta traz a sua mancha. Duas coisas
    // podem correr mal em silêncio, e nenhuma daria erro na app.
    var comCor = 0;
    for (final curso in c.cursos) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          for (final q in n.questoes) {
            final cor = q.cores;
            if (cor == null) continue;
            comCor++;
            final onde = '${curso.id}/${u.id}/${n.id}: ${q.q}';

            // Uma mistura de uma cor só não é mistura nenhuma.
            if (cor.mistura.isNotEmpty) {
              expect(cor.mistura.length, greaterThanOrEqualTo(2), reason: onde);
            }

            // Se há manchas nas opções, tem de haver uma por opção. Com
            // menos, as últimas respostas ficavam sem cor e a criança não
            // percebia porquê.
            if (cor.opcoes.isNotEmpty && q is QChoice) {
              expect(cor.opcoes.length, q.options.length, reason: onde);
            }

            // Opacas. Uma cor sem alfa sai invisível no fundo escuro.
            for (final v in [...cor.mistura, ...cor.opcoes]) {
              expect(v >> 24 & 0xFF, 0xFF, reason: '$onde: cor transparente');
            }
          }
        }
      }
    }
    expect(comCor, greaterThan(0), reason: 'nenhuma pergunta mostra cor');
  });

  test('o conteúdo sem fonte nenhuma está marcado como tal', () {
    // Dos cursos da app, um só foi montado sem documento nenhum: a
    // Educação Visual da 4ª classe, porque não existe manual publicado nem
    // programa que se tenha encontrado. Isso não é um defeito — é uma
    // decisão — mas tem de estar escrito onde alguém tropece nele, e não
    // só na mensagem de um commit de há um ano.
    final provisorios =
        c.cursos.where((x) => x.provisorio).map((x) => x.id).toList();
    expect(provisorios, ['ev-4c'],
        reason: 'mudou a lista de cursos sem fonte nenhuma');

    final ev4 = c.cursos.firstWhere((x) => x.id == 'ev-4c');
    expect(ev4.fonte, contains('provisória'));
    expect(ev4.fonte, contains('sem fonte confirmada'));
  });

  test('e o que sai de uma fonte que não é um livro diz qual é', () {
    // Ter `fonte` não quer dizer «provisório» — quer dizer «não veio de um
    // manual, e aqui fica de onde veio». O campo já significou as duas
    // coisas ao mesmo tempo, e no dia em que entrou a Matemática da 7ª
    // classe ela passou a contar como provisória sem nada de provisória
    // ter. São perguntas diferentes e agora são campos diferentes.
    final mat7 = c.cursos.firstWhere((x) => x.id == 'mat-7c');
    expect(mat7.provisorio, isFalse,
        reason: 'a 7ª tem fonte oficial: o programa do INDE');
    expect(mat7.fonte, contains('INDE'));
    expect(mat7.fonte, contains('programa'),
        reason: 'tem de dizer que é um programa e não um livro do aluno');
  });

  test('nenhum enunciado manda olhar para o que não está lá', () {
    // Escrevi uma pergunta que dizia "a expressão sublinhada indica:" — e
    // a app não sublinha nada. Num livro há sublinhados, negritos e setas;
    // aqui há uma linha de texto e três opções. Uma pergunta que aponta
    // para uma marca que não existe é impossível de responder, e não há
    // maneira de a criança perceber que o erro não é dela.
    final apontam = <String>[];
    final padrao = RegExp(
      r'(sublinhad[oa]s?|a negrito|em negrito|assinalad[oa]s?|'
      r'destacad[oa]s?|na figura acima|no quadro acima)',
      caseSensitive: false,
    );
    for (final curso in c.cursos) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          for (final q in n.questoes) {
            if (padrao.hasMatch(q.q)) apontam.add('${curso.id}: ${q.q}');
          }
        }
      }
    }
    expect(apontam, isEmpty,
        reason: 'a pergunta aponta para uma marca que o ecrã não mostra');
  });

  test('dentro de uma classe, cada enunciado é único', () {
    // As perguntas erradas são guardadas pelo texto do enunciado. Dois
    // enunciados iguais na mesma classe estragam três coisas ao mesmo
    // tempo: a lista de Guardados mostra a linha a dobrar, o contador
    // conta a mais, e acertar numa marca a outra como aprendida.
    //
    // E há o pior: o áudio lê o enunciado às crianças que ainda não lêem.
    // Um "Qual é o maior?" dito em voz alta, com três botões que a criança
    // não consegue ler, não ensina nada — por isso as opções passaram a
    // vir no próprio enunciado.
    for (final classe in c.cursos.map((x) => x.classe).toSet()) {
      final vistos = <String, String>{};
      for (final curso in c.cursos.where((x) => x.classe == classe)) {
        for (final u in curso.units) {
          for (final n in u.niveis) {
            for (final q in n.questoes) {
              final onde = '${curso.disciplina} / ${n.titulo}';
              expect(vistos.containsKey(q.q), isFalse,
                  reason: '$classe: "${q.q}" está em $onde '
                      'e também em ${vistos[q.q]}');
              vistos[q.q] = onde;
            }
          }
        }
      }
    }
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
              case QSequencia():
                expect(q.passos.length, greaterThanOrEqualTo(2), reason: onde);
                // A ordem baralhada tem de mostrar mesmo tudo, e nunca a
                // ordem já feita — senão aparece resolvida.
                final baralho = q.baralhados();
                expect(baralho.toSet(), hasLength(q.passos.length),
                    reason: onde);
                expect(q.certa(baralho), isFalse, reason: '$onde já vem feita');
              case QGrupos():
                expect(q.grupos.length, greaterThanOrEqualTo(2), reason: onde);
                for (final i in q.itens) {
                  expect(i.grupo, inInclusiveRange(0, q.grupos.length - 1),
                      reason: onde);
                }
                // Um grupo vazio é uma caixa que nunca recebe nada.
                for (var g = 0; g < q.grupos.length; g++) {
                  expect(q.itens.any((i) => i.grupo == g), isTrue,
                      reason: '$onde: grupo "${q.grupos[g]}" fica vazio');
                }
              case QCenario():
                expect(q.alvos, isNotEmpty, reason: onde);
                expect(q.pecas.toSet(), hasLength(q.pecas.length),
                    reason: onde);
                for (final a in q.alvos) {
                  expect(a.x, inInclusiveRange(0.0, 1.0), reason: onde);
                  expect(a.y, inInclusiveRange(0.0, 1.0), reason: onde);
                }
              case QGrelha():
                // Uma conta que não se arma rebentaria dentro da lição, com
                // a criança lá.
                expect(() => q.conta, returnsNormally, reason: onde);
                expect(q.conta.aPreencher, isNotEmpty, reason: onde);
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

  test('nenhum ficheiro de áudio está vazio', () {
    // Existir não chega. A matéria do metical da 3ª classe passou uma
    // versão inteira com um mp3 de zero bytes: o ficheiro estava lá, o
    // teste de existência passava, e a aula era muda. Uma gravação que
    // falha a meio deixa exactamente isto para trás.
    //
    // Este teste cobre também o áudio da MATÉRIA, que o de cima não via —
    // e era ali que estava o defeito.
    var vazios = <String>[];

    void conferir(String? ficheiro, String onde) {
      if (ficheiro == null) return;
      final f = File('assets/audio/$ficheiro');
      if (!f.existsSync()) return; // já é apanhado pelo teste de cima
      final bytes = f.lengthSync();
      // Uma frase curta da Raquel não desce dos 10 kB. Abaixo de 1 kB não
      // há fala nenhuma lá dentro.
      if (bytes < 1024) vazios.add('$onde -> $ficheiro ($bytes bytes)');
    }

    for (final curso in c.cursos) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          conferir(n.materia?.audio, '${curso.id}/${n.id} (matéria)');
          for (final q in n.questoes) {
            conferir(q.audio, '${curso.id}/${n.id}: ${q.q}');
          }
        }
      }
    }

    expect(vazios, isEmpty, reason: 'áudio sem som lá dentro');
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
