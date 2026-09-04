import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/escadaria.dart';
import 'package:somara/models/frascos.dart';
import 'package:somara/screens/frascos_screen.dart';
import 'package:somara/screens/joguinhos_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';
import 'package:somara/widgets/mesa_de_frascos.dart';

import 'apoio/solucionador_frascos.dart';

/// O Water R Sort no ecrã.
///
/// O modelo já está provado noutro ficheiro. O que aqui se guarda é o que
/// só se parte na montagem: a mesa que não cabe no telemóvel barato, o
/// Desfazer que não desfaz, e o nível que se acaba mas não faz subir a
/// escadaria.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  setUpAll(() {
    for (final canal in const [
      MethodChannel('xyz.luan/audioplayers.global'),
      MethodChannel('xyz.luan/audioplayers'),
    ]) {
      TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
          .setMockMethodCallHandler(canal, (_) async => null);
    }
  });

  group('a disposição dos frascos', () {
    // Uma função pura, e por isso mede-se sem montar nada. É aqui que se
    // apanha o frasco que sai pela borda fora.
    const caixa = Size(300, 420);

    test('nenhum frasco sai da caixa, de três a dez', () {
      for (var quantos = 3; quantos <= 10; quantos++) {
        for (final altura in [4, 5]) {
          final sitios = disporFrascos(caixa, quantos, altura);
          expect(sitios, hasLength(quantos));
          for (final r in sitios) {
            expect(r.left, greaterThanOrEqualTo(-0.01),
                reason: '$quantos frascos de $altura: sai pela esquerda');
            expect(r.right, lessThanOrEqualTo(caixa.width + 0.01),
                reason: '$quantos frascos de $altura: sai pela direita');
            expect(r.top, greaterThanOrEqualTo(-0.01),
                reason: '$quantos frascos de $altura: sai por cima');
            expect(r.bottom, lessThanOrEqualTo(caixa.height + 0.01),
                reason: '$quantos frascos de $altura: sai por baixo');
          }
        }
      }
    });

    test('os frascos não se sobrepõem', () {
      for (var quantos = 3; quantos <= 10; quantos++) {
        final sitios = disporFrascos(caixa, quantos, 4);
        for (var i = 0; i < sitios.length; i++) {
          for (var j = i + 1; j < sitios.length; j++) {
            expect(sitios[i].overlaps(sitios[j]), isFalse,
                reason: '$quantos frascos: o $i e o $j estão em cima um do '
                    'outro');
          }
        }
      }
    });

    test('o dedo apanha-os: nunca mais estreitos do que 28 px', () {
      // Dez frascos numa linha só dariam menos de trinta pixels a cada um.
      // É por isso que a partir de cinco vão em duas linhas.
      for (var quantos = 3; quantos <= 10; quantos++) {
        final largura = disporFrascos(const Size(300, 420), quantos, 5).first
            .width;
        expect(largura, greaterThanOrEqualTo(28),
            reason: '$quantos frascos ficaram com ${largura.round()} px');
      }
    });
  });

  group('no ecrã', () {
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

    Future<Object?> montar(
      WidgetTester tester,
      Widget ecra,
      AppState st,
      Size t,
    ) async {
      tester.view.physicalSize = t;
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);
      await tester.pumpWidget(
        ChangeNotifierProvider<AppState>.value(
          value: st,
          child: MaterialApp(theme: somaraTheme(), home: ecra),
        ),
      );
      await tester.pump(const Duration(milliseconds: 400));
      return tester.takeException();
    }

    for (final t in const <String, Size>{
      'telemóvel barato': Size(320, 640),
      'telemóvel comum': Size(411, 914),
      'tablet': Size(600, 1024),
    }.entries) {
      testWidgets('o primeiro nível cabe num ${t.key}', (tester) async {
        expect(
          await montar(tester, const FrascosScreen(nivel: 1), estado(), t.value),
          isNull,
        );
      });

      testWidgets('e a mesa cheia do último também cabe num ${t.key}',
          (tester) async {
        // Dez frascos de cinco blocos: é o pior caso que a escadaria produz.
        expect(
          await montar(
            tester,
            const FrascosScreen(nivel: nivelMaximo),
            estado(),
            t.value,
          ),
          isNull,
        );
      });
    }

    testWidgets('entra pelo degrau guardado', (tester) async {
      final st = estado();
      for (var i = 0; i < 6; i++) {
        st.subirNivelDe(Jogo.frascos);
      }
      await montar(tester, const FrascosScreen(), st, const Size(411, 914));
      expect(find.text('Water R Sort · Nível 7'), findsOneWidget);
    });

    /// A primeira jogada legal do tabuleiro do nível 1 — que é sempre o
    /// mesmo, porque o nível é determinista.
    ({int de, int para}) primeiraJogada() {
      final tabuleiro = Frascos.doNivel(1);
      for (var i = 0; i < tabuleiro.frascos.length; i++) {
        for (var j = 0; j < tabuleiro.frascos.length; j++) {
          if (tabuleiro.podeDespejar(i, j)) return (de: i, para: j);
        }
      }
      throw StateError('o nível 1 abriu sem jogada nenhuma');
    }

    Future<void> tocarNoFrasco(WidgetTester tester, int i) async {
      await tester.tap(find.byKey(ValueKey('frasco-$i')));
      await tester.pump();
    }

    testWidgets('tocar em dois frascos despeja de um para o outro',
        (tester) async {
      await montar(
          tester, const FrascosScreen(nivel: 1), estado(), const Size(411, 914));
      final j = primeiraJogada();

      await tocarNoFrasco(tester, j.de);
      expect(find.textContaining('para onde queres despejar'), findsOneWidget,
          reason: 'o frasco escolhido devia dizer o que fazer a seguir');

      await tocarNoFrasco(tester, j.para);
      await tester.pump(const Duration(milliseconds: 700));
      expect(find.textContaining('1 jogada'), findsOneWidget);
    });

    testWidgets('o Desfazer volta atrás, e o Recomeçar limpa tudo',
        (tester) async {
      await montar(
          tester, const FrascosScreen(nivel: 1), estado(), const Size(411, 914));
      final j = primeiraJogada();

      // Antes de jogar, os dois botões estão apagados e não fazem nada.
      await tester.tap(find.text('Desfazer'));
      await tester.pump();
      expect(find.textContaining('jogada'), findsNothing);

      await tocarNoFrasco(tester, j.de);
      await tocarNoFrasco(tester, j.para);
      await tester.pump(const Duration(milliseconds: 700));
      expect(find.textContaining('1 jogada'), findsOneWidget);

      await tester.tap(find.text('Desfazer'));
      await tester.pump();
      expect(find.textContaining('1 jogada'), findsNothing,
          reason: 'o Desfazer não voltou atrás');

      // E outra vez, para o Recomeçar.
      await tocarNoFrasco(tester, j.de);
      await tocarNoFrasco(tester, j.para);
      await tester.pump(const Duration(milliseconds: 700));
      await tester.tap(find.text('Recomeçar'));
      await tester.pump();
      expect(find.textContaining('1 jogada'), findsNothing,
          reason: 'o Recomeçar não limpou as jogadas');
    });

    testWidgets('acabar o nível faz subir a escadaria', (tester) async {
      // Joga-se o nível 1 até ao fim, aos toques, pelo caminho que o
      // solucionador encontrou. É o teste que prova que uma criança
      // consegue mesmo chegar ao fim de um nível por este ecrã — e não só
      // que o modelo sabe somar.
      final st = estado();
      await montar(
          tester, const FrascosScreen(nivel: 1), st, const Size(411, 914));

      final jogadas = caminho(Frascos.doNivel(1));
      expect(jogadas, isNotNull, reason: 'o nível 1 não tinha solução');

      for (final j in jogadas!) {
        await tocarNoFrasco(tester, j.de);
        await tocarNoFrasco(tester, j.para);
        await tester.pump(const Duration(milliseconds: 600));
      }

      expect(find.textContaining('Arrumado!'), findsOneWidget);
      expect(find.text('Nível 1 feito!'), findsOneWidget);

      // A passagem ao degrau seguinte demora 1,6 s de propósito, para dar
      // tempo de ver o que se fez.
      await tester.pump(const Duration(milliseconds: 1800));
      expect(st.nivelDe(Jogo.frascos), 2, reason: 'a escadaria não subiu');
      expect(find.text('Water R Sort · Nível 2'), findsOneWidget);
    });

    testWidgets('e nenhum dos outros joguinhos se mexeu', (tester) async {
      final st = estado();
      st.subirNivelDe(Jogo.frascos);
      expect(st.nivelDe(Jogo.frascos), 2);
      for (final outro in Jogo.values.where((j) => j != Jogo.frascos)) {
        expect(st.nivelDe(outro), 1, reason: outro.rotulo);
      }
    });

    testWidgets('o cartão está na sala dos joguinhos, e abre o jogo',
        (tester) async {
      await montar(
        tester,
        const JoguinhosScreen(),
        estado(),
        const Size(411, 914),
      );
      expect(find.text('Water R Sort'), findsOneWidget);
      expect(find.byIcon(Icons.science_rounded), findsOneWidget,
          reason: 'o cartão devia ter o frasco por ícone');

      // O cartão novo é o último da lista, e por isso é o último
      // "Continuar". Vem de fora do ecrã num telemóvel — daí o
      // ensureVisible antes do toque.
      final botao = find.text('Continuar').at(Jogo.values.length - 1);
      await tester.ensureVisible(botao);
      await tester.pump();
      await tester.tap(botao);
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 700));
      expect(find.text('Water R Sort · Nível 1'), findsOneWidget,
          reason: 'o botão do cartão não abriu o jogo');
    });
  });
}
