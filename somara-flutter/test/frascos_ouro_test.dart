import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/escadaria.dart';
import 'package:somara/models/frascos.dart';
import 'package:somara/screens/frascos_screen.dart';
import 'package:somara/screens/lesson_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';
import 'package:somara/widgets/teclado_numerico.dart';

/// O que se compra com ouro no Water R Sort, o arrasto, e o mostrador dos
/// números que deixou de travar aos cinco algarismos.
///
/// Tudo o que aqui se prende tem um preço ou um travão, e é por isso que
/// precisa de teste: uma compra que cobra sem dar, ou que dá sem cobrar, é
/// dinheiro de criança a desaparecer sem ninguém reparar.
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

  late Conteudo conteudo;

  setUpAll(() async {
    conteudo = await Conteudo.carregar();
    SharedPreferences.setMockInitialValues({});
  });

  /// Um estado com [ouro] moedas de ouro. Entra pela fusão da nuvem, que é
  /// a única porta pública para pôr dinheiro numa carteira sem estudar.
  AppState comOuro(int ouro) => AppState()
    ..conteudo = conteudo
    ..pronto = true
    ..nome = 'Ana'
    ..classe = '1ª classe'
    ..cursoId = conteudo.cursos.first.id
    ..fundirDaNuvem({
      'carteira': {'ganhoGc': ouro, 'gastoGc': 0, 'ganhoCc': 0, 'gastoCc': 0},
    });

  Future<void> montar(WidgetTester tester, Widget ecra, AppState st) async {
    tester.view.physicalSize = const Size(411, 914);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(
      ChangeNotifierProvider<AppState>.value(
        value: st,
        child: MaterialApp(theme: somaraTheme(), home: ecra),
      ),
    );
    await tester.pump(const Duration(milliseconds: 400));
  }

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

  /// Uma jogada completa, com a animação inteira a passar.
  Future<void> jogar(WidgetTester tester, ({int de, int para}) j) async {
    await tocarNoFrasco(tester, j.de);
    await tocarNoFrasco(tester, j.para);
    await tester.pump(const Duration(milliseconds: 1100));
  }

  /// Abre a folha de compra tocando no botão, e espera que ela suba.
  Future<void> abrirFolha(WidgetTester tester, String botao) async {
    await tester.tap(find.text(botao));
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 500));
  }

  Future<void> responder(WidgetTester tester, String botao) async {
    await tester.tap(find.text(botao));
    await tester.pump();
    await tester.pump(const Duration(milliseconds: 500));
  }

  group('o frasco extra', () {
    testWidgets('acrescenta um frasco vazio e cobra o preço', (tester) async {
      final st = comOuro(30);
      await montar(tester, const FrascosScreen(nivel: 1), st);
      final antes = Frascos.doNivel(1).frascos.length;
      expect(find.byKey(ValueKey('frasco-$antes')), findsNothing);

      await abrirFolha(tester, 'Frasco extra');
      expect(find.text('Confirmar'), findsOneWidget);
      await responder(tester, 'Confirmar');

      expect(find.byKey(ValueKey('frasco-$antes')), findsOneWidget,
          reason: 'pagou e o frasco não apareceu');
      expect(st.carteira.gc, 30 - PrecoNosFrascos.frascoExtra);
    });

    testWidgets('sem ouro que chegue, explica quanto falta e não cobra',
        (tester) async {
      final st = comOuro(3);
      await montar(tester, const FrascosScreen(nivel: 1), st);
      final antes = Frascos.doNivel(1).frascos.length;

      await abrirFolha(tester, 'Frasco extra');
      expect(find.textContaining('faltam-te 7'), findsOneWidget);
      expect(find.text('Confirmar'), findsNothing,
          reason: 'não pode haver botão de confirmar sem dinheiro');
      await responder(tester, 'Está bem');

      expect(find.byKey(ValueKey('frasco-$antes')), findsNothing);
      expect(st.carteira.gc, 3, reason: 'cobrou sem dar');
    });

    testWidgets('«Agora não» fecha sem cobrar', (tester) async {
      final st = comOuro(30);
      await montar(tester, const FrascosScreen(nivel: 1), st);
      await abrirFolha(tester, 'Frasco extra');
      await responder(tester, 'Agora não');
      expect(st.carteira.gc, 30);
    });

    testWidgets('sobrevive ao Recomeçar — foi pago', (tester) async {
      final st = comOuro(30);
      await montar(tester, const FrascosScreen(nivel: 1), st);
      final antes = Frascos.doNivel(1).frascos.length;
      await abrirFolha(tester, 'Frasco extra');
      await responder(tester, 'Confirmar');

      await jogar(tester, primeiraJogada());
      await tester.tap(find.text('Recomeçar'));
      await tester.pump();
      expect(find.byKey(ValueKey('frasco-$antes')), findsOneWidget,
          reason: 'recomeçar tirou da mesa um frasco pago');
    });

    testWidgets('e o Desfazer também não o tira', (tester) async {
      final st = comOuro(30);
      await montar(tester, const FrascosScreen(nivel: 1), st);
      final antes = Frascos.doNivel(1).frascos.length;

      await jogar(tester, primeiraJogada());
      await abrirFolha(tester, 'Frasco extra');
      await responder(tester, 'Confirmar');
      await tester.tap(find.text('Desfazer'));
      await tester.pump();
      expect(find.byKey(ValueKey('frasco-$antes')), findsOneWidget,
          reason: 'desfazer a jogada anterior à compra tirou o frasco');
    });
  });

  group('o Desfazer', () {
    testWidgets('três de graça, e o quarto custa uma moeda', (tester) async {
      final st = comOuro(10);
      await montar(tester, const FrascosScreen(nivel: 1), st);
      final j = primeiraJogada();

      for (var vez = 1; vez <= 3; vez++) {
        await jogar(tester, j);
        await tester.tap(find.text('Desfazer'));
        await tester.pump();
        expect(find.textContaining('1 jogada'), findsNothing,
            reason: 'o Desfazer nº $vez não desfez');
        expect(st.carteira.gc, 10, reason: 'o Desfazer nº $vez cobrou');
      }
      expect(find.text('${PrecoNosFrascos.desfazer} GC'), findsOneWidget,
          reason: 'o botão devia passar a mostrar o preço');

      await jogar(tester, j);
      await abrirFolha(tester, 'Desfazer');
      expect(find.text('Confirmar'), findsOneWidget);
      await responder(tester, 'Confirmar');
      expect(find.textContaining('1 jogada'), findsNothing,
          reason: 'pagou e não desfez');
      expect(st.carteira.gc, 10 - PrecoNosFrascos.desfazer);
    });
  });

  group('saltar o nível', () {
    testWidgets('cobra, sobe a escadaria e não conta como treino',
        (tester) async {
      final st = comOuro(50);
      await montar(tester, const FrascosScreen(nivel: 1), st);
      final xpAntes = st.xp;

      await abrirFolha(tester, 'Saltar');
      await responder(tester, 'Confirmar');

      expect(find.text('Water R Sort · Nível 2'), findsOneWidget);
      expect(st.nivelDe(Jogo.frascos), 2);
      expect(st.carteira.gc, 50 - PrecoNosFrascos.saltar);
      expect(st.xp, xpAntes, reason: 'saltar não pode dar XP');
    });

    testWidgets('no último degrau não há para onde saltar', (tester) async {
      await montar(
          tester, const FrascosScreen(nivel: nivelMaximo), comOuro(100));
      expect(find.text('último'), findsOneWidget);
    });
  });

  group('o arrasto', () {
    testWidgets('arrastar um frasco até outro despeja', (tester) async {
      await montar(tester, const FrascosScreen(nivel: 1), comOuro(0));
      final j = primeiraJogada();
      final de = tester.getCenter(find.byKey(ValueKey('frasco-${j.de}')));
      final para = tester.getCenter(find.byKey(ValueKey('frasco-${j.para}')));

      await tester.drag(find.byKey(ValueKey('frasco-${j.de}')), para - de);
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 1100));
      expect(find.textContaining('1 jogada'), findsOneWidget,
          reason: 'largar em cima do destino devia despejar');
    });

    testWidgets('largar onde não dá deixa o frasco levantado, à espera',
        (tester) async {
      await montar(tester, const FrascosScreen(nivel: 1), comOuro(0));
      final mesa = Frascos.doNivel(1);
      ({int de, int para})? par;
      for (var i = 0; i < mesa.frascos.length && par == null; i++) {
        for (var k = 0; k < mesa.frascos.length; k++) {
          if (i != k &&
              !mesa.frascos[i].vazio &&
              !mesa.frascos[k].vazio &&
              !mesa.podeDespejar(i, k)) {
            par = (de: i, para: k);
            break;
          }
        }
      }
      expect(par, isNotNull, reason: 'o nível 1 devia ter um par que não dá');

      final de = tester.getCenter(find.byKey(ValueKey('frasco-${par!.de}')));
      final para =
          tester.getCenter(find.byKey(ValueKey('frasco-${par.para}')));
      await tester.drag(find.byKey(ValueKey('frasco-${par.de}')), para - de);
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 1100));

      expect(find.textContaining('1 jogada'), findsNothing);
      expect(find.textContaining('para onde queres despejar'), findsOneWidget,
          reason: 'o frasco devia ficar escolhido, à espera de destino');
    });
  });

  group('o mostrador dos números', () {
    test('agrupa os milhares com um espaço fino', () {
      expect(MostradorDoNumero.agrupar('100000'), '100 000');
      expect(MostradorDoNumero.agrupar('1234567'), '1 234 567');
      expect(MostradorDoNumero.agrupar('12'), '12');
      expect(MostradorDoNumero.agrupar('-5'), '−5');
      expect(MostradorDoNumero.agrupar('-1000'), '−1 000');
    });

    testWidgets('uma resposta de seis algarismos aceita-se — antes não',
        (tester) async {
      // Três perguntas da 4ª classe respondem 100000, e com o travão nos
      // cinco algarismos nenhuma delas se conseguia responder.
      final q = conteudo.cursos
          .expand((c) => c.units)
          .expand((u) => u.niveis)
          .expand((n) => n.questoes)
          .whereType<QInput>()
          .firstWhere((q) => q.a.trim() == '100000');

      final st = AppState()
        ..conteudo = conteudo
        ..pronto = true
        ..nome = 'Ana'
        ..classe = '4ª classe'
        ..cursoId = 'mat-4c';
      tester.view.physicalSize = const Size(320, 640);
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);
      await tester.pumpWidget(
        ChangeNotifierProvider<AppState>.value(
          value: st,
          child: MaterialApp(
            theme: somaraTheme(),
            home: LessonScreen(indice: -1, avulsas: [q], titulo: 'Teste'),
          ),
        ),
      );
      await tester.pump(const Duration(milliseconds: 500));

      for (final d in '100000'.split('')) {
        await tester.tap(find.text(d).last);
        await tester.pump();
      }
      expect(find.text('100 000'), findsOneWidget,
          reason: 'o sexto algarismo não entrou, ou não se agrupou');
      expect(tester.takeException(), isNull,
          reason: 'transbordou num telemóvel de 320');

      await tester.tap(find.text('Verificar'));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 700));
      expect(find.text('Continuar'), findsOneWidget,
          reason: 'a resposta certa de seis algarismos não foi aceite');
    });
  });
}
