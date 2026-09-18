import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/screens/lesson_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';

/// A Matemática da 8ª classe — a primeira disciplina do segundo ano do
/// secundário.
///
/// O curso em si está preso pelo `content_test.dart`. O que aqui se guarda
/// é a forma que o programa do INDE lhe dá — nove unidades, e não sete
/// como a 7ª — e o que a 8ª trouxe de novo à app: símbolos que a voz não
/// sabia dizer, e que agora ficam no enunciado à vista de quem lê.
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

  Curso mat8() => conteudo.cursos.firstWhere((c) => c.id == 'mat-8c');

  Iterable<Questao> perguntas() sync* {
    for (final u in mat8().units) {
      for (final n in u.niveis) {
        yield* n.questoes;
      }
    }
  }

  group('o curso', () {
    test('segue as nove unidades temáticas do INDE, pela ordem dele', () {
      expect(
        mat8().units.map((u) => u.titulo).toList(),
        [
          'Números e operações (1)',
          'Funções (1)',
          'Números reais',
          'Inequações lineares',
          'Circunferência e círculo',
          'Álgebra (2)',
          'Geometria (2)',
          'Estatística',
          'Movimentos no plano',
        ],
      );
    });

    test('a fonte diz o programa, as páginas, e que não é um livro', () {
      expect(mat8().fonte, contains('INDE'));
      expect(mat8().fonte, contains('pp. 46-81'));
      expect(mat8().fonte, contains('não traz exercícios'));
      expect(mat8().provisorio, isFalse);
    });

    test('é a 8ª classe, e a lista de classes passa a tê-la', () {
      expect(mat8().classe, '8ª classe');
      expect(conteudo.cursos.map((c) => c.classe).toSet(),
          contains('8ª classe'));
    });

    test('os símbolos novos estão mesmo nos enunciados', () {
      // Expoentes, raiz, pi, os reais e a notação de função: é o que a 8ª
      // pede e a 7ª não pedia. Cada um tem regra de pronúncia no
      // tools/pronuncia.py, e esta lista é o que garante que a regra tem
      // onde ser usada.
      final texto = perguntas().map((q) => q.q).join('\n');
      for (final simbolo in ['²', '³', '√', 'π', 'ℝ', 'f(x)']) {
        expect(texto, contains(simbolo), reason: 'não há "$simbolo" na 8ª');
      }
    });

    test('há uma resposta negativa, para a tecla do sinal servir', () {
      expect(
        perguntas().whereType<QInput>().where((q) => q.a.startsWith('-')),
        isNotEmpty,
      );
    });
  });

  group('no ecrã', () {
    Future<Object?> montar(WidgetTester tester, Questao q, Size t) async {
      final st = AppState()
        ..conteudo = conteudo
        ..pronto = true
        ..nome = 'Amina'
        ..classe = '8ª classe'
        ..cursoId = 'mat-8c';
      tester.view.physicalSize = t;
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
      return tester.takeException();
    }

    for (final t in const <String, Size>{
      'telemóvel barato': Size(320, 640),
      'telemóvel comum': Size(411, 914),
    }.entries) {
      testWidgets('as perguntas com opções compridas cabem num ${t.key}',
          (tester) async {
        // As opções da 8ª são frases inteiras — "Uma fracção de dois
        // inteiros, com denominador diferente de zero" — e é aí que um
        // telemóvel estreito parte primeiro.
        final compridas = perguntas()
            .whereType<QChoice>()
            .where((q) => q.options.any((o) => o.length > 45));
        expect(compridas, isNotEmpty);
        for (final q in compridas) {
          expect(await montar(tester, q, t.value), isNull,
              reason: '"${q.q}" em ${t.value}');
        }
      });
    }
  });
}
