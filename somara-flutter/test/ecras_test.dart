import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/crossmath.dart';
import 'package:somara/models/escadaria.dart';
import 'package:somara/models/memoria.dart';
import 'package:somara/screens/crossmath_screen.dart';
import 'package:somara/screens/guardados_screen.dart';
import 'package:somara/screens/joguinhos_screen.dart';
import 'package:somara/screens/lesson_screen.dart';
import 'package:somara/screens/map_screen.dart';
import 'package:somara/screens/materia_screen.dart';
import 'package:somara/screens/perfil_screen.dart';
import 'package:somara/screens/memoria_screen.dart';
import 'package:somara/screens/pomar_screen.dart';
import 'package:somara/screens/sopa_screen.dart';
import 'package:somara/screens/praticar_screen.dart';
import 'package:somara/screens/ranking_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';

/// Os ecrãs, em vários tamanhos de telemóvel.
///
/// O que estes testes apanham é a família de defeitos que passou por cima de
/// toda a gente até agora: texto a transbordar da caixa, linhas cortadas,
/// botões fora do ecrã. Nenhum deles dá erro no `flutter analyze` e nenhum
/// aparece nos testes de lógica — só se vêem a olhar, e só no tamanho
/// errado. Três das últimas quatro versões tiveram um destes.
///
/// Os tamanhos não são inventados: 320×640 é o Android barato que ainda se
/// vende em Moçambique, 411×914 é o telemóvel comum, e 600×1024 é um
/// tablet de escola.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo conteudo;

  setUpAll(() async {
    conteudo = await Conteudo.carregar();
    SharedPreferences.setMockInitialValues({});
  });

  AppState estado() => AppState()
    ..conteudo = conteudo
    ..pronto = true
    ..nome = 'Ana'
    ..classe = '1ª classe'
    ..cursoId = conteudo.cursos.first.id;

  const tamanhos = <String, Size>{
    'telemóvel barato': Size(320, 640),
    'telemóvel comum': Size(411, 914),
    'tablet': Size(600, 1024),
  };

  /// Monta um ecrã num tamanho dado e devolve o erro, se houver.
  Future<Object?> montar(
    WidgetTester tester,
    Widget ecra,
    Size tamanho, {
    AppState? st,
  }) async {
    tester.view.physicalSize = tamanho;
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.reset);

    await tester.pumpWidget(
      ChangeNotifierProvider<AppState>.value(
        value: st ?? estado(),
        child: MaterialApp(
          theme: somaraTheme(),
          home: Scaffold(backgroundColor: S.gm950, body: ecra),
        ),
      ),
    );
    await tester.pump(const Duration(milliseconds: 600));
    return tester.takeException();
  }

  /// Cada ecrã, em cada tamanho.
  void verificar(String nome, Widget Function() construir) {
    for (final entrada in tamanhos.entries) {
      testWidgets('$nome cabe num ${entrada.key}', (tester) async {
        final erro = await montar(tester, construir(), entrada.value);
        expect(erro, isNull, reason: '$nome em ${entrada.value}');
      });
    }
  }

  verificar('Joguinhos', () => const JoguinhosScreen());
  verificar('Praticar', () => const PraticarScreen());
  verificar('Ranking', () => const RankingScreen());
  verificar('Guardados', () => const GuardadosScreen());
  verificar('Perfil', () => const PerfilScreen());
  verificar('Pomar', () => const PomarScreen());

  for (final d in Dificuldade.values) {
    verificar('Crossmath ${d.rotulo}', () => CrossmathScreen(dificuldade: d));
  }

  // A sopa é a que mais arrisca transbordar: no último degrau a grelha tem
  // catorze letras de lado e a lista de palavras é comprida. Vão o primeiro,
  // um do meio e o último — os extremos do tamanho da grelha.
  for (final n in [1, 300, nivelMaximo]) {
    verificar('Sopa nível $n', () => SopaScreen(nivel: n));
  }

  // Quatro baralhos, e o de "Contar" chega a ter nove desenhos numa carta.
  for (final b in Baralho.values) {
    verificar('Memória ${b.rotulo}', () => MemoriaScreen(baralho: b));
  }

  group('a aula, com a matéria mais comprida que existe', () {
    // Se alguma aula transborda, é a maior — e é essa que interessa testar.
    late String titulo;
    late Materia maior;

    setUpAll(() {
      var recorde = -1;
      for (final c in conteudo.cursos) {
        for (final u in c.units) {
          for (final n in u.niveis) {
            final m = n.materia;
            if (m == null) continue;
            final tamanho =
                m.explica.length + m.exemplo.length + m.lembra.length;
            if (tamanho > recorde) {
              recorde = tamanho;
              maior = m;
              titulo = n.titulo;
            }
          }
        }
      }
      expect(recorde, greaterThan(0), reason: 'nenhuma aula encontrada');
    });

    for (final entrada in tamanhos.entries) {
      testWidgets('cabe num ${entrada.key}', (tester) async {
        final erro = await montar(
          tester,
          MateriaScreen(titulo: titulo, materia: maior),
          entrada.value,
        );
        expect(erro, isNull);
      });
    }
  });

  group('nomes longos não partem a interface', () {
    // O nome é escrito pela criança e ninguém o limita. Um nome comprido
    // já partiu o cabeçalho de outras apps.
    for (final entrada in tamanhos.entries) {
      testWidgets('Perfil com nome longo num ${entrada.key}', (tester) async {
        final st = estado()
          ..nome = 'Maria Fernanda Nhamitambo da Conceição Chissano';
        final erro = await montar(
          tester,
          const PerfilScreen(),
          entrada.value,
          st: st,
        );
        expect(erro, isNull);
      });
    }
  });

  group('a cor da Educação Visual aparece mesmo no ecrã', () {
    // O modelo estar certo não garante que se veja. Esta é a peça nova da
    // app — a pergunta que mostra tinta em vez de a nomear — e sem isto
    // um erro no ecrã da lição deixava-a invisível sem nada falhar.
    late Questao mistura;
    late Questao semCor;

    setUpAll(() {
      mistura = conteudo.cursos
          .expand((c) => c.units)
          .expand((u) => u.niveis)
          .expand((n) => n.questoes)
          .firstWhere((q) => q.cores?.temMistura ?? false);
      semCor = conteudo.cursos
          .expand((c) => c.units)
          .expand((u) => u.niveis)
          .expand((n) => n.questoes)
          .firstWhere((q) => q.cores == null && q is QChoice);
    });

    for (final entrada in tamanhos.entries) {
      testWidgets('a mistura desenha-se num ${entrada.key}', (tester) async {
        final erro = await montar(
          tester,
          LessonScreen(indice: -1, avulsas: [mistura], titulo: 'cor'),
          entrada.value,
        );
        expect(erro, isNull);

        // As manchas: uma por tinta, mais a incógnita do resultado.
        final gotas = tester.widgetList<Container>(find.byType(Container)).where(
            (x) => (x.decoration as BoxDecoration?)?.shape == BoxShape.circle);
        expect(gotas.length, greaterThanOrEqualTo(3),
            reason: 'as tintas não apareceram no ecrã');
      });
    }

    testWidgets('e uma pergunta sem cor não desenha tintas', (tester) async {
      // Sem este contra-exemplo, o teste de cima passaria a contar
      // quaisquer círculos que houvesse no ecrã.
      await montar(
        tester,
        LessonScreen(indice: -1, avulsas: [semCor], titulo: 'sem cor'),
        const Size(411, 914),
      );
      final gotas = tester.widgetList<Container>(find.byType(Container)).where(
          (x) => (x.decoration as BoxDecoration?)?.shape == BoxShape.circle);
      expect(gotas.length, lessThan(3));
    });
  });

  group('a barra de disciplinas do mapa', () {
    // O mapa nunca esteve nestes testes, e é o ecrã que a criança vê
    // primeiro. A barra de disciplinas cresce com o currículo: a 1ª classe
    // tem duas, a 4ª passou a ter três com a chegada do Português, e a 5ª
    // e a 6ª têm quatro. Num telemóvel de 320 é onde isso parte.
    for (final entrada in tamanhos.entries) {
      for (final classe in ['1ª classe', '4ª classe', '6ª classe']) {
        testWidgets('$classe cabe num ${entrada.key}', (tester) async {
          final st = estado()
            ..classe = classe
            ..cursoId = conteudo.cursos.firstWhere((c) => c.classe == classe).id;
          final erro = await montar(
            tester,
            const MapScreen(),
            entrada.value,
            st: st,
          );
          expect(erro, isNull, reason: '$classe em ${entrada.value}');
        });
      }
    }

    testWidgets('cada disciplina da classe tem a sua pastilha', (tester) async {
      final st = estado()
        ..classe = '4ª classe'
        ..cursoId = 'mat-4c';
      await montar(tester, const MapScreen(), const Size(320, 640), st: st);

      // As quatro da 4ª classe. Se uma disciplina nova não aparecer aqui,
      // é porque a barra a deixou de fora — e a criança nunca lhe chega.
      //
      // As Ciências vêm abreviadas, senão o nome não cabe na pastilha. Foi
      // a esquecer-me da abreviatura que quase entreguei as Ciências
      // Sociais da 4ª com o nome inteiro.
      for (final nome in [
        'Matemática',
        'Português',
        'C. Naturais',
        'C. Sociais',
      ]) {
        expect(find.text(nome), findsWidgets, reason: 'sem pastilha: $nome');
      }
    });
  });

  group('os botões dos joguinhos', () {
    // O cartão da Memória tem quatro baralhos. Os quatro numa só linha
    // davam a cada botão pouco mais de sessenta pixels: o rótulo partia-se
    // ao meio, a pílula fechava-se num oval e o texto saía pela borda fora.
    //
    // Nada disto lança excepção — não havia RenderFlex a transbordar — e por
    // isso passou por todos os outros testes deste ficheiro. Só se via a
    // olhar para o ecrã, e foi assim que apareceu.
    Size medir(WidgetTester tester, String rotulo) => tester.getSize(
      find
          .ancestor(
            of: find.text(rotulo),
            matching: find.byType(GestureDetector),
          )
          .first,
    );

    Future<void> abrir(WidgetTester tester, Size tamanho) async {
      final erro = await montar(tester, const JoguinhosScreen(), tamanho);
      expect(erro, isNull);
      // A Memória é o último cartão da lista e num telemóvel pequeno nem
      // chega a ser construída sem se descer até lá.
      await tester.scrollUntilVisible(
        find.text(Baralho.palavras.rotulo),
        180,
        scrollable: find.byType(Scrollable).first,
      );
      await tester.pumpAndSettle();
    }

    for (final entrada in tamanhos.entries) {
      testWidgets('têm largura para o rótulo num ${entrada.key}', (
        tester,
      ) async {
        await abrir(tester, entrada.value);

        for (final b in Baralho.values) {
          final tamanho = medir(tester, b.rotulo);
          expect(
            tamanho.width,
            greaterThanOrEqualTo(110),
            reason:
                '"${b.rotulo}" ficou com ${tamanho.width.round()} px de '
                'largura — não cabe lá o rótulo',
          );
        }
      });

      testWidgets('ficam do mesmo tamanho lado a lado num ${entrada.key}', (
        tester,
      ) async {
        await abrir(tester, entrada.value);

        // Contar e Somas partilham uma linha; Dobros e Palavras a outra.
        // Um rótulo que se parte em duas linhas não pode deixar o botão do
        // lado mais baixo do que o seu.
        expect(
          medir(tester, Baralho.quantidade.rotulo).height,
          medir(tester, Baralho.somas.rotulo).height,
        );
        expect(
          medir(tester, Baralho.dobros.rotulo).height,
          medir(tester, Baralho.palavras.rotulo).height,
        );
      });
    }
  });
}
