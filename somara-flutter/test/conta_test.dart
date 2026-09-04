import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/screens/conta_screen.dart';
import 'package:somara/screens/perfil_screen.dart';
import 'package:somara/services/nuvem.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';

/// O ecrã de entrar na conta, e o cartão do perfil que lá leva.
///
/// Nenhum dos dois tinha teste nenhum, e a razão é a mesma para os dois: o
/// cartão só se monta quando o Firebase está configurado, e até à 0.36.0 a
/// consola estava por preencher. Ou seja — a porta de entrada para toda a
/// parte da nuvem ia aparecer no telemóvel de alguém sem nunca ter sido
/// desenhada aqui.
///
/// Nada disto fala com o Firebase. O que se prova é o que se parte sem
/// rede: a montagem nos três tamanhos, o botão que não deixa avançar com
/// dados incompletos, e a falha explicada em português em vez de um erro.
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

  tearDown(() => Nuvem.i.fingirDisponivel = false);

  AppState estado() => AppState()
    ..conteudo = conteudo
    ..pronto = true
    ..nome = 'Ana'
    ..classe = '3ª classe'
    ..cursoId = conteudo.cursos.first.id;

  Future<Object?> montar(WidgetTester tester, Widget ecra, Size t) async {
    tester.view.physicalSize = t;
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.reset);
    await tester.pumpWidget(
      ChangeNotifierProvider<AppState>.value(
        value: estado(),
        // O Scaffold à volta é o mesmo do `ecras_test.dart`: o interruptor
        // do som, no perfil, é um widget do Material e exige-o por cima.
        // Na app quem o dá é o HomeShell.
        child: MaterialApp(
          theme: somaraTheme(),
          home: Scaffold(backgroundColor: S.gm950, body: ecra),
        ),
      ),
    );
    await tester.pump(const Duration(milliseconds: 400));
    return tester.takeException();
  }

  const tamanhos = <String, Size>{
    'telemóvel barato': Size(320, 640),
    'telemóvel comum': Size(411, 914),
    'tablet': Size(600, 1024),
  };

  group('o ecrã de guardar o progresso', () {
    for (final t in tamanhos.entries) {
      testWidgets('cabe num ${t.key}', (tester) async {
        expect(await montar(tester, const ContaScreen(), t.value), isNull);
        expect(find.text('Criar conta'), findsOneWidget);
        expect(find.text('Já tenho conta'), findsOneWidget);
      });
    }

    /// A opacidade do botão grande diz se ele está vivo: o ecrã apaga-o
    /// enquanto os dados não servirem.
    double opacidadeDoBotao(WidgetTester tester, String rotulo) =>
        tester
            .widget<Opacity>(
              find
                  .ancestor(
                    of: find.text(rotulo),
                    matching: find.byType(Opacity),
                  )
                  .first,
            )
            .opacity;

    testWidgets('não deixa avançar sem email e sem palavra-passe',
        (tester) async {
      await montar(tester, const ContaScreen(), const Size(411, 914));
      expect(opacidadeDoBotao(tester, 'Criar e guardar'), lessThan(1));

      // Email sem arroba não serve.
      await tester.enterText(find.byType(TextField).at(0), 'pai.exemplo.mz');
      await tester.enterText(find.byType(TextField).at(1), 'abcdef');
      await tester.pump();
      expect(opacidadeDoBotao(tester, 'Criar e guardar'), lessThan(1),
          reason: 'um email sem @ passou');

      // Palavra-passe curta também não.
      await tester.enterText(find.byType(TextField).at(0), 'pai@exemplo.mz');
      await tester.enterText(find.byType(TextField).at(1), 'abc');
      await tester.pump();
      expect(opacidadeDoBotao(tester, 'Criar e guardar'), lessThan(1),
          reason: 'uma palavra-passe de três letras passou');

      // Os dois bem, e o botão acende.
      await tester.enterText(find.byType(TextField).at(1), 'abcdef');
      await tester.pump();
      expect(opacidadeDoBotao(tester, 'Criar e guardar'), 1.0);
    });

    testWidgets('o botão muda de nome consoante o modo', (tester) async {
      await montar(tester, const ContaScreen(), const Size(411, 914));
      expect(find.text('Criar e guardar'), findsOneWidget);

      await tester.tap(find.text('Já tenho conta'));
      await tester.pump(const Duration(milliseconds: 300));
      expect(find.text('Entrar'), findsOneWidget);
      expect(find.text('Criar e guardar'), findsNothing,
          reason: 'quem já tem conta não pode ver "Criar"');
    });

    testWidgets('a palavra-passe começa escondida e mostra-se ao pedir',
        (tester) async {
      await montar(tester, const ContaScreen(), const Size(411, 914));
      expect(tester.widget<TextField>(find.byType(TextField).at(1)).obscureText,
          isTrue);

      await tester.tap(find.byIcon(Icons.visibility_rounded));
      await tester.pump();
      expect(tester.widget<TextField>(find.byType(TextField).at(1)).obscureText,
          isFalse);
    });

    testWidgets('sem rede, explica-se em português e não rebenta',
        (tester) async {
      // Sem Firebase a chamada falha. O que não pode acontecer é a app
      // deitar um erro em inglês para cima de quem está a tentar guardar o
      // trabalho do filho.
      await montar(tester, const ContaScreen(), const Size(411, 914));
      await tester.enterText(find.byType(TextField).at(0), 'pai@exemplo.mz');
      await tester.enterText(find.byType(TextField).at(1), 'abcdef');
      await tester.pump();

      await tester.tap(find.text('Criar e guardar'));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 400));

      expect(tester.takeException(), isNull);
      expect(find.textContaining('Não foi possível ligar'), findsOneWidget);
      // E continua a dar para tentar outra vez.
      expect(find.text('Criar e guardar'), findsOneWidget);
    });
  });

  group('o cartão da conta, no perfil', () {
    testWidgets('não aparece enquanto a nuvem não estiver configurada',
        (tester) async {
      // Prometer "o teu progresso fica guardado" sem nuvem seria mentir.
      expect(await montar(tester, const PerfilScreen(), const Size(411, 914)),
          isNull);
      expect(find.text('Guardar o progresso'), findsNothing);
    });

    for (final t in tamanhos.entries) {
      testWidgets('com a nuvem configurada, cabe num ${t.key}',
          (tester) async {
        Nuvem.i.fingirDisponivel = true;
        expect(await montar(tester, const PerfilScreen(), t.value), isNull);
        expect(find.text('Guardar o progresso'), findsOneWidget);
      });
    }
  });
}
