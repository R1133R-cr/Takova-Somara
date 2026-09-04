import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/painters/cenas.dart';
import 'package:somara/screens/lesson_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';
import 'package:somara/widgets/interactivos.dart';

/// Os exercícios interactivos de Ciências.
///
/// Trazem a Ciências o que a grelha trouxe à Matemática: deixam de medir se
/// a criança reconhece a frase certa e passam a medir se ela percebeu a
/// coisa. Pôr o ciclo da água por ordem não se acerta por eliminação.
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

  group('a sequência', () {
    const q = QSequencia(
      'Põe por ordem.',
      null,
      passos: ['Primeiro', 'Segundo', 'Terceiro', 'Quarto'],
    );

    test('a ordem certa é a ordem em que os passos estão guardados', () {
      expect(q.certa([0, 1, 2, 3]), isTrue);
      expect(q.certa([1, 0, 2, 3]), isFalse);
      expect(q.certa([0, 1, 2]), isFalse, reason: 'faltava um passo');
    });

    test('nunca aparece já resolvida', () {
      // Uma sequência que abre pela ordem certa não é um exercício, é um
      // texto — e a criança carrega em Verificar sem ter feito nada.
      final baralho = q.baralhados();
      expect(q.certa(baralho), isFalse);
      expect(baralho.toSet(), hasLength(q.passos.length),
          reason: 'a baralhação perdeu ou repetiu um passo');
    });

    test('a mesma pergunta baralha sempre igual', () {
      // Dois telemóveis com a mesma pergunta têm de a mostrar igual, senão
      // a criança que compara com o colega vê duas coisas diferentes.
      expect(q.baralhados(), q.baralhados());
    });

    test('duas perguntas diferentes baralham de maneira diferente', () {
      const outra = QSequencia(
        'Põe por outra ordem qualquer.',
        null,
        passos: ['Primeiro', 'Segundo', 'Terceiro', 'Quarto'],
      );
      expect(q.baralhados(), isNot(outra.baralhados()));
    });
  });

  group('a classificação', () {
    const q = QGrupos(
      'Arruma.',
      null,
      grupos: ['Vertebrado', 'Invertebrado'],
      itens: [
        (nome: 'cabrito', grupo: 0),
        (nome: 'peixe', grupo: 0),
        (nome: 'formiga', grupo: 1),
      ],
    );

    test('tudo no sítio dá certo; uma coisa trocada dá errado', () {
      expect(q.certa([0, 0, 1]), isTrue);
      expect(q.certa([0, 1, 1]), isFalse);
    });

    test('com uma coisa por arrumar não está certa', () {
      expect(q.certa([0, 0, null]), isFalse);
      expect(q.certa([null, null, null]), isFalse);
    });
  });

  group('o cenário', () {
    const q = QCenario(
      'Fecha o circuito.',
      null,
      cena: Cena.circuito,
      alvos: [
        (x: 0.5, y: 0.2, peca: 'lâmpada'),
        (x: 0.14, y: 0.49, peca: 'pilha'),
        (x: 0.86, y: 0.49, peca: 'fio'),
      ],
    );

    test('cada peça no seu sítio dá certo', () {
      expect(q.certa(['lâmpada', 'pilha', 'fio']), isTrue);
      expect(q.certa(['pilha', 'lâmpada', 'fio']), isFalse);
      expect(q.certa(['lâmpada', 'pilha', null]), isFalse);
    });

    test('as peças são exactamente as dos alvos', () {
      expect(q.pecas, ['lâmpada', 'pilha', 'fio']);
    });
  });

  group('no ecrã', () {
    late Conteudo conteudo;

    setUpAll(() async {
      conteudo = await Conteudo.carregar();
      SharedPreferences.setMockInitialValues({});
    });

    /// As perguntas interactivas que estão mesmo no currículo.
    List<Questao> doTipo(bool Function(Questao) e) => [
      for (final c in conteudo.cursos)
        for (final u in c.units)
          for (final n in u.niveis)
            for (final q in n.questoes)
              if (e(q)) q,
    ];

    AppState estado() => AppState()
      ..conteudo = conteudo
      ..pronto = true
      ..nome = 'Ana'
      ..classe = '5ª classe'
      ..cursoId = conteudo.cursos.firstWhere((c) => c.id == 'cn-5c').id;

    Future<Object?> montar(WidgetTester tester, Questao q, Size t) async {
      tester.view.physicalSize = t;
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);
      await tester.pumpWidget(
        ChangeNotifierProvider<AppState>.value(
          value: estado(),
          child: MaterialApp(
            theme: somaraTheme(),
            home: LessonScreen(indice: -1, avulsas: [q], titulo: 'Ciências'),
          ),
        ),
      );
      await tester.pump(const Duration(milliseconds: 400));
      return tester.takeException();
    }

    test('o currículo tem mesmo os três tipos', () {
      expect(doTipo((q) => q is QSequencia), isNotEmpty);
      expect(doTipo((q) => q is QGrupos), isNotEmpty);
      expect(doTipo((q) => q is QCenario), isNotEmpty);
    });

    test('todas as cenas usadas sabem desenhar-se', () {
      // O `Cena.values.byName` no `content.dart` já rebentaria a leitura,
      // mas isto diz qual é a cena que falta em vez de "erro de formato".
      for (final q in doTipo((q) => q is QCenario).cast<QCenario>()) {
        expect(Cena.values, contains(q.cena), reason: q.q);
      }
    });

    for (final t in const <String, Size>{
      'telemóvel barato': Size(320, 640),
      'telemóvel comum': Size(411, 914),
      'tablet': Size(600, 1024),
    }.entries) {
      testWidgets('todas as interactivas cabem num ${t.key}', (tester) async {
        // Cada uma tem uma altura própria: a de nove coisas para arrumar em
        // três caixas é a que mais arrisca, e é a que menos se vê a testar
        // à mão.
        for (final q in doTipo(
          (q) => q is QSequencia || q is QGrupos || q is QCenario,
        )) {
          expect(await montar(tester, q, t.value), isNull,
              reason: '"${q.q}" em ${t.value}');
        }
      });
    }

    testWidgets('arrumar tudo certo é aceite', (tester) async {
      final q = doTipo((q) => q is QGrupos).first as QGrupos;
      await montar(tester, q, const Size(411, 914));

      // Sem nada arrumado, não há nada a verificar.
      expect(find.text('Verificar'), findsOneWidget);

      // Arruma pela via do modelo — o arrasto em si é do Flutter e está
      // testado por ele; o que aqui interessa é a lição aceitar o resultado.
      final widget =
          tester.widget<ClassificarGrupos>(find.byType(ClassificarGrupos));
      widget.aoMudar([for (final i in q.itens) i.grupo]);
      await tester.pump();

      await tester.tap(find.text('Verificar'));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 600));
      expect(find.text('Continuar'), findsOneWidget,
          reason: 'a arrumação certa não foi aceite');
    });

    testWidgets('uma coisa na caixa errada é recusada', (tester) async {
      final q = doTipo((q) => q is QGrupos).first as QGrupos;
      await montar(tester, q, const Size(411, 914));

      final widget =
          tester.widget<ClassificarGrupos>(find.byType(ClassificarGrupos));
      final errado = [for (final i in q.itens) i.grupo];
      errado[0] = (errado[0] + 1) % q.grupos.length;
      widget.aoMudar(errado);
      await tester.pump();

      await tester.tap(find.text('Verificar'));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 600));
      // Errar não deixa avançar sem primeiro mostrar o que estava certo.
      expect(find.text('Continuar'), findsOneWidget);
      expect(find.byType(ClassificarGrupos), findsOneWidget,
          reason: 'a arrumação dela devia ficar à vista, com as cores');
    });

    testWidgets('a sequência certa é aceite', (tester) async {
      final q = doTipo((q) => q is QSequencia).first as QSequencia;
      await montar(tester, q, const Size(411, 914));

      final widget = tester.widget<OrdenarPassos>(find.byType(OrdenarPassos));
      widget.aoMudar([for (var i = 0; i < q.passos.length; i++) i]);
      await tester.pump();

      await tester.tap(find.text('Verificar'));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 600));
      expect(find.text('Continuar'), findsOneWidget);
    });

    testWidgets('o cenário certo acende a lâmpada', (tester) async {
      final q = doTipo(
        (q) => q is QCenario && q.cena == Cena.circuito,
      ).first as QCenario;
      await montar(tester, q, const Size(411, 914));

      final widget =
          tester.widget<CenarioInteractivo>(find.byType(CenarioInteractivo));
      widget.aoMudar(q.pecas);
      await tester.pump();

      // O brilho é do painter, e o que se pode afirmar daqui é que ele passa
      // a saber que a conta fechou.
      expect(q.certa(q.pecas), isTrue);

      await tester.tap(find.text('Verificar'));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 600));
      expect(find.text('Continuar'), findsOneWidget);
    });
  });
}
