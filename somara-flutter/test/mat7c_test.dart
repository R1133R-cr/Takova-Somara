import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/screens/lesson_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';
import 'package:somara/widgets/desenho_geometrico.dart';

/// A Matemática da 7ª classe, e as duas coisas que ela obrigou a mexer.
///
/// O curso em si está preso pelo `content_test.dart`, como todos os outros.
/// O que aqui se guarda é o que a 7ª classe trouxe de novo à app e que
/// nenhuma classe anterior tinha pedido: respostas negativas e duas formas
/// geométricas que o desenhador não sabia desenhar.
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

  Curso mat7() => conteudo.cursos.firstWhere((c) => c.id == 'mat-7c');

  Iterable<Questao> perguntasDa7() sync* {
    for (final u in mat7().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  Future<AppState> montar(WidgetTester tester, Questao q, [Size? t]) async {
    final st = AppState()
      ..conteudo = conteudo
      ..pronto = true
      ..nome = 'Amina'
      ..classe = '7ª classe'
      ..cursoId = 'mat-7c';

    tester.view.physicalSize = t ?? const Size(411, 914);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.reset);

    await tester.pumpWidget(
      ChangeNotifierProvider<AppState>.value(
        value: st,
        child: MaterialApp(
          theme: somaraTheme(),
          home: LessonScreen(indice: -1, avulsas: [q], titulo: 'Matemática'),
        ),
      ),
    );
    await tester.pump(const Duration(milliseconds: 500));
    return st;
  }

  group('o curso', () {
    test('segue as sete unidades temáticas do INDE', () {
      expect(mat7().units, hasLength(7));
      expect(
        mat7().units.map((u) => u.titulo).toList(),
        [
          'Números e operações (1)',
          'Geometria (1)',
          'Números racionais',
          'Grandezas e medidas',
          'Álgebra',
          'Percentagens e dinheiro',
          'Relações proporcionais',
        ],
      );
    });

    test('a fonte diz que é um programa e não um livro', () {
      // É a diferença que separa este curso dos outros vinte e um, e não
      // pode ficar só na mensagem de um commit.
      expect(mat7().fonte, contains('INDE'));
      expect(mat7().fonte, contains('não traz exercícios'));
      expect(mat7().provisorio, isFalse);
    });

    test('há perguntas de resposta negativa, e é isso que é novo', () {
      final negativas = perguntasDa7()
          .whereType<QInput>()
          .where((q) => q.a.trim().startsWith('-'))
          .toList();
      expect(negativas, isNotEmpty,
          reason: 'os números inteiros relativos são conteúdo da unidade I');
    });
  });

  group('a resposta negativa', () {
    QInput negativa() => perguntasDa7()
        .whereType<QInput>()
        .firstWhere((q) => q.a.trim().startsWith('-'));

    QInput positiva() => perguntasDa7()
        .whereType<QInput>()
        .firstWhere((q) => RegExp(r'^\d+$').hasMatch(q.a.trim()));

    testWidgets('abre o teclado próprio, e não o de letras do sistema',
        (tester) async {
      // Era isto que estava partido: a app decidia mostrar o teclado
      // próprio com `^\d+$`, e um "-5" não casa. A criança da 7ª classe
      // ficava com o teclado do telemóvel, que abre com letras e tapa
      // meia pergunta, para escrever um número.
      await montar(tester, negativa());
      expect(find.byType(TextField), findsNothing,
          reason: 'abriu o teclado do sistema para escrever um número');
      expect(find.text('+/−'), findsOneWidget);
    });

    testWidgets('a tecla do sinal não aparece onde não serve', (tester) async {
      // Dar uma tecla de menos a quem responde 26 é oferecer-lhe uma
      // maneira de errar que não existia.
      await montar(tester, positiva());
      expect(find.text('+/−'), findsNothing);
    });

    testWidgets('escrever o número e trocar o sinal dá a resposta certa',
        (tester) async {
      final q = negativa();
      await montar(tester, q);

      for (final d in q.a.replaceAll('-', '').split('')) {
        await tester.tap(find.text(d).last);
        await tester.pump();
      }
      await tester.tap(find.text('+/−'));
      await tester.pump();

      await tester.tap(find.text('Verificar'));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 700));
      expect(find.text('Continuar'), findsOneWidget,
          reason: 'a resposta negativa certa não foi aceite');
    });

    testWidgets('o sinal troca nos dois sentidos', (tester) async {
      await montar(tester, negativa());
      await tester.tap(find.text('5').last);
      await tester.pump();
      await tester.tap(find.text('+/−'));
      await tester.pump();
      expect(find.text('-5'), findsOneWidget);
      await tester.tap(find.text('+/−'));
      await tester.pump();
      expect(find.text('5'), findsWidgets);
    });
  });

  group('as formas novas', () {
    test('o trapézio e o losango estão mesmo no currículo', () {
      final formas = perguntasDa7()
          .map((q) => q.figura?.forma)
          .whereType<FormaGeo>()
          .toSet();
      expect(formas, contains(FormaGeo.trapezio));
      expect(formas, contains(FormaGeo.losango));
    });

    for (final t in const <String, Size>{
      'telemóvel barato': Size(320, 640),
      'telemóvel comum': Size(411, 914),
      'tablet': Size(600, 1024),
    }.entries) {
      testWidgets('todas as figuras da 7ª desenham-se num ${t.key}',
          (tester) async {
        for (final q in perguntasDa7().where((q) => q.figura != null)) {
          await montar(tester, q, t.value);
          expect(tester.takeException(), isNull,
              reason: '"${q.q}" rebentou em ${t.value}');
          expect(find.byType(DesenhoGeometrico), findsOneWidget,
              reason: '"${q.q}" não mostrou a figura');
        }
      });
    }
  });
}
