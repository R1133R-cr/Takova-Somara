import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/screens/lesson_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';

/// O teclado das respostas escritas.
///
/// Cento e dezassete das cento e cinquenta e uma respostas escritas do
/// curriculo sao numeros. O teclado do sistema abre com letras, tapa meia
/// pergunta, e numa crianca da 1a classe que quer escrever "8" isso e um
/// obstaculo antes da conta.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo conteudo;

  setUpAll(() async {
    conteudo = await Conteudo.carregar();
    SharedPreferences.setMockInitialValues({});
  });

  /// Monta uma licao com uma pergunta escolhida a mao.
  Future<AppState> montar(WidgetTester tester, Questao q) async {
    final st = AppState()
      ..conteudo = conteudo
      ..pronto = true
      ..classe = '1ª classe'
      ..cursoId = conteudo.cursos.first.id;

    tester.view.physicalSize = const Size(411, 914);
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
    return st;
  }

  /// Uma pergunta de escrever com resposta numerica, tirada do curriculo.
  Questao perguntaNumerica() {
    for (final c in conteudo.cursos) {
      for (final u in c.units) {
        for (final n in u.niveis) {
          for (final q in n.questoes) {
            if (q is QInput && RegExp(r'^\d+$').hasMatch(q.a.trim())) return q;
          }
        }
      }
    }
    throw StateError('nenhuma pergunta numerica no curriculo');
  }

  /// Uma de escrever com resposta de letras.
  Questao perguntaDeTexto() {
    for (final c in conteudo.cursos) {
      for (final u in c.units) {
        for (final n in u.niveis) {
          for (final q in n.questoes) {
            if (q is QInput && !RegExp(r'^\d+$').hasMatch(q.a.trim())) return q;
          }
        }
      }
    }
    throw StateError('nenhuma pergunta de texto no curriculo');
  }

  testWidgets('resposta numerica traz o teclado proprio, sem TextField',
      (tester) async {
    await montar(tester, perguntaNumerica());

    for (final d in ['1', '5', '9', '0']) {
      expect(find.widgetWithText(GestureDetector, d), findsWidgets,
          reason: 'falta a tecla $d');
    }
    expect(find.textContaining('Apagar'), findsOneWidget);
    expect(find.byType(TextField), findsNothing,
        reason: 'o teclado do sistema nao deve aparecer nas respostas de numero');
  });

  testWidgets('escrever com o teclado enche o mostrador', (tester) async {
    await montar(tester, perguntaNumerica());

    // O mostrador comeca com a interrogacao e nao com um campo vazio: uma
    // caixa em branco nao diz a crianca que e ali que a resposta vai.
    expect(find.text('?'), findsOneWidget);

    await tester.tap(find.widgetWithText(GestureDetector, '4').first);
    await tester.pump();
    await tester.tap(find.widgetWithText(GestureDetector, '2').first);
    await tester.pump();
    expect(find.text('42'), findsOneWidget);

    await tester.tap(find.textContaining('Apagar'));
    await tester.pump();
    expect(find.text('4'), findsWidgets);
  });

  testWidgets('resposta de letras continua com o teclado do sistema',
      (tester) async {
    // Nem tudo o que se escreve e numero: ha palavras a completar no
    // Portugues da 1a classe, e para essas o teclado de numeros nao serve.
    await montar(tester, perguntaDeTexto());
    expect(find.byType(TextField), findsOneWidget);
  });
}
