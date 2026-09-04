import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/escadaria.dart';
import 'package:somara/models/sopa.dart';
import 'package:somara/screens/joguinhos_screen.dart';
import 'package:somara/screens/sopa_screen.dart';
import 'package:somara/theme.dart';
import 'package:somara/state/app_state.dart';

/// A sopa jogada até ao fim, com o dedo.
///
/// Os testes do modelo provam que a grelha está bem montada. Este prova a
/// promessa que se fez à criança: encontrar a última palavra faz subir um
/// degrau, sem lhe perguntar nada. Se a progressão automática se partir —
/// um `mounted` a mais, um `setState` a menos — não há teste de modelo que
/// dê por isso, e ninguém repara até um miúdo ficar preso no nível 1.
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

  Future<void> montar(WidgetTester tester, Widget ecra, AppState st) async {
    tester.view.physicalSize = const Size(411, 914);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.reset);

    await tester.pumpWidget(
      ChangeNotifierProvider<AppState>.value(
        value: st,
        child: MaterialApp(
          theme: somaraTheme(),
          home: Scaffold(backgroundColor: S.gm950, body: ecra),
        ),
      ),
    );
    await tester.pump(const Duration(milliseconds: 300));
  }

  /// Arrasta da primeira à última letra de uma palavra colocada.
  Future<void> arrastar(WidgetTester tester, Sopa sopa,
      PalavraColocada p) async {
    final caixa = find.byKey(const ValueKey('sopa-grelha'));
    final canto = tester.getTopLeft(caixa);
    final lado = tester.getSize(caixa).width / sopa.lado;

    Offset centro(int i) => canto +
        Offset(
          (sopa.colunaDe(i) + 0.5) * lado,
          (sopa.linhaDe(i) + 0.5) * lado,
        );

    final g = await tester.startGesture(centro(p.casas.first));
    await tester.pump();
    await g.moveTo(centro(p.casas.last));
    await tester.pump();
    await g.up();
    await tester.pump(const Duration(milliseconds: 100));
  }

  testWidgets('a sopa acabada leva ao degrau seguinte sem perguntar',
      (tester) async {
    const semente = 11;
    final sopa = Sopa.doNivel(1, rnd: Random(semente));
    final st = estado();

    await montar(
      tester,
      SopaScreen(nivel: 1, aleatorio: Random(semente)),
      st,
    );

    // A lista mostra as palavras deste nível.
    for (final p in sopa.escondidas) {
      expect(find.text(p.palavra), findsWidgets,
          reason: '${p.palavra} devia estar na lista');
    }
    expect(find.textContaining('Nível 1'), findsOneWidget);

    for (final p in sopa.escondidas) {
      await arrastar(tester, sopa, p);
    }

    // Festeja primeiro...
    expect(find.text('Encontraste todas!'), findsOneWidget);
    expect(find.text('Nível 1 feito!'), findsOneWidget);
    expect(find.textContaining('Vem aí o 2'), findsOneWidget);
    // ...e não há botão nenhum a perguntar se se quer continuar.
    expect(find.text('Outra sopa'), findsNothing);
    expect(find.text('Sair'), findsNothing);

    // ...e o degrau seguinte entra sozinho.
    await tester.pump(const Duration(milliseconds: 1700));
    expect(st.nivelDe(Jogo.sopa), 2, reason: 'a escadaria não subiu');
    expect(find.textContaining('Nível 2'), findsOneWidget);
    expect(find.text('Encontraste todas!'), findsNothing,
        reason: 'a sopa nova devia estar por fazer');
  });

  testWidgets('quem sobe de nível vê-o no cartão dos joguinhos',
      (tester) async {
    final st = estado();
    for (var i = 0; i < 6; i++) {
      st.subirNivelDe(Jogo.sopa);
    }

    await montar(tester, const JoguinhosScreen(), st);
    // Quatro "Continuar": os quatro joguinhos estão todos na escadaria. O
    // que os distingue é o degrau por baixo.
    expect(find.text('Continuar'), findsNWidgets(4));
    expect(find.text('nível 7 de $nivelMaximo'), findsOneWidget);
    expect(find.text('nível 1 de $nivelMaximo'), findsNWidgets(3),
        reason: 'os outros três deviam estar no primeiro degrau');
    // As três dificuldades antigas desapareceram. Vinham rotuladas com o
    // número de palavras — se alguma dessas sobrar, voltou-se a perguntar à
    // criança uma coisa que ela não tem de escolher.
    for (var n = 4; n <= 10; n++) {
      expect(find.text('$n palavras'), findsNothing,
          reason: 'sobrou a escolha de dificuldade');
    }
  });
}
