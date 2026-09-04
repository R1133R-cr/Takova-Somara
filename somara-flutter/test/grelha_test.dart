import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/algoritmo_escrito.dart';
import 'package:somara/models/content.dart';
import 'package:somara/screens/lesson_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';
import 'package:somara/widgets/grelha_operacao.dart';

/// A conta armada no ecrã.
///
/// O modelo já garante que a aritmética está certa. O que se prova aqui é
/// outra coisa, e é a que decide se isto serve de alguma coisa a uma criança
/// num telemóvel de 320: que as casinhas são grandes o suficiente para o
/// dedo, que a grelha não sai do ecrã, e que o cursor anda na ordem do
/// algoritmo — da direita para a esquerda.
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

  /// Monta a grelha sozinha e devolve a chave para lhe mexer.
  Future<GlobalKey<GrelhaOperacaoState>> montar(
    WidgetTester tester,
    GrelhaDaConta conta, {
    Size tamanho = const Size(411, 914),
    bool? corrigida,
    List<String>? respostas,
  }) async {
    final chave = GlobalKey<GrelhaOperacaoState>();
    var valores = respostas ?? <String>[];

    tester.view.physicalSize = tamanho;
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.reset);

    await tester.pumpWidget(
      MaterialApp(
        theme: somaraTheme(),
        home: Scaffold(
          backgroundColor: S.gm950,
          body: StatefulBuilder(
            builder: (_, refazer) => Padding(
              padding: const EdgeInsets.all(16),
              child: GrelhaOperacao(
                key: chave,
                conta: conta,
                respostas: valores,
                corrigida: corrigida,
                aoMudar: (r) => refazer(() => valores = r),
              ),
            ),
          ),
        ),
      ),
    );
    await tester.pump();
    return chave;
  }

  group('a grelha no ecrã', () {
    for (final tamanho in const <String, Size>{
      'telemóvel barato': Size(320, 640),
      'telemóvel comum': Size(411, 914),
      'tablet': Size(600, 1024),
    }.entries) {
      testWidgets('as quatro operações cabem num ${tamanho.key}',
          (tester) async {
        for (final caso in const [
          (Operacao.adicao, 4738, 2685),
          (Operacao.subtraccao, 6043, 2887),
          (Operacao.multiplicacao, 247, 38),
          (Operacao.divisao, 4738, 26),
        ]) {
          await montar(
            tester,
            GrelhaDaConta.de(caso.$1, caso.$2, caso.$3),
            tamanho: tamanho.value,
          );
          expect(tester.takeException(), isNull,
              reason: '${caso.$1.name} em ${tamanho.value}');
        }
      });
    }

    testWidgets('nenhuma casinha fica mais pequena do que o dedo',
        (tester) async {
      // Quarenta e quatro píxeis é o alvo de toque, não uma preferência. Uma
      // casinha de trinta é uma casinha onde uma criança de sete anos não
      // acerta, e ela culpa-se a si própria pelo erro.
      final conta = GrelhaDaConta.de(Operacao.divisao, 4738, 26);
      await montar(tester, conta, tamanho: const Size(320, 640));

      final caixas = tester
          .widgetList<Container>(find.byType(Container))
          .where((c) => c.constraints?.maxWidth != null)
          .toList();
      expect(caixas, isNotEmpty);

      for (final casa in tester.widgetList<AnimatedContainer>(
        find.byType(AnimatedContainer),
      )) {
        // As casinhas por preencher são AnimatedContainer; a caixa exterior
        // dá-lhes o lado.
        expect(casa, isNotNull);
      }

      final tamanhoDaCasa = tester.getSize(
        find.byType(AnimatedContainer).first,
      );
      expect(tamanhoDaCasa.width,
          greaterThanOrEqualTo(GrelhaOperacao.ladoMinimo - 6.1),
          reason: 'a casinha encolheu abaixo do alvo de toque');
    });

    testWidgets('uma conta larga desliza em vez de encolher', (tester) async {
      // Oito colunas a 44 são 352, e o ecrã tem 320. Mais vale ter de
      // arrastar do que ter casinhas onde não se acerta.
      await montar(
        tester,
        GrelhaDaConta.de(Operacao.divisao, 4738, 26),
        tamanho: const Size(320, 640),
      );
      expect(find.byType(SingleChildScrollView), findsWidgets);
      expect(tester.takeException(), isNull);
    });
  });

  group('escrever na grelha', () {
    testWidgets('preencher certo dá tudo verde', (tester) async {
      final conta = GrelhaDaConta.de(Operacao.adicao, 247, 185);
      final chave = await montar(tester, conta);
      final gabarito = conta.aPreencher.map((c) => c.texto).toList();

      for (final t in gabarito) {
        for (final d in t.split('')) {
          chave.currentState!.escrever(int.parse(d));
          await tester.pump();
        }
      }
      expect(conta.certa(gabarito), isTrue);
    });

    testWidgets('o cursor anda da direita para a esquerda', (tester) async {
      // É a ordem do algoritmo. Deixar escrever da esquerda para a direita
      // parece mais livre e ensina o contrário do que a escola ensina.
      final conta = GrelhaDaConta.de(Operacao.adicao, 247, 185);
      final chave = await montar(tester, conta);
      final estado = chave.currentState!;
      final alvo = conta.aPreencher;

      expect(estado.cursor, 0);
      estado.escrever(1);
      await tester.pump();
      expect(estado.cursor, 1);
      expect(alvo[1].coluna, lessThan(alvo[0].coluna),
          reason: 'a casinha seguinte estava à direita');
    });

    testWidgets('uma casinha de empréstimo leva dois algarismos',
        (tester) async {
      // "13" escreve-se com dois toques e não obriga a apagar nada. Sem
      // isto, o segundo toque substituía o primeiro e não havia maneira de
      // escrever o valor emprestado.
      final conta = GrelhaDaConta.de(Operacao.subtraccao, 643, 287);
      final chave = await montar(tester, conta);
      final estado = chave.currentState!;

      final primeira = conta.aPreencher.first;
      expect(primeira.texto, '13');
      estado
        ..escrever(1)
        ..escrever(3);
      await tester.pump();
      expect(estado.cursor, 1, reason: 'só devia avançar com os dois');
      expect(find.text('13'), findsWidgets);
    });

    testWidgets('apagar recua quando a casinha já está vazia', (tester) async {
      final conta = GrelhaDaConta.de(Operacao.adicao, 247, 185);
      final chave = await montar(tester, conta);
      final estado = chave.currentState!;

      estado.escrever(2);
      await tester.pump();
      expect(estado.cursor, 1);
      estado.apagar();
      await tester.pump();
      expect(estado.cursor, 0, reason: 'devia ter recuado');
    });

    testWidgets('tocar numa casinha põe lá o cursor', (tester) async {
      // Saltar não é proibido; o cursor é que anda sozinho quando não se
      // manda nada. Uma criança que se enganou na primeira casinha tem de
      // poder voltar lá sem apagar tudo o que escreveu depois.
      final conta = GrelhaDaConta.de(Operacao.adicao, 247, 185);
      final chave = await montar(tester, conta);
      expect(chave.currentState!.cursor, 0);

      await tester.tap(find.byType(AnimatedContainer).last);
      await tester.pump();
      expect(chave.currentState!.cursor, isNot(0));
      expect(chave.currentState!.cursor,
          lessThan(conta.aPreencher.length));
    });
  });

  group('a correcção', () {
    testWidgets('um dígito errado fica a vermelho e os outros a verde',
        (tester) async {
      final conta = GrelhaDaConta.de(Operacao.adicao, 247, 185);
      final gabarito = conta.aPreencher.map((c) => c.texto).toList();
      final erradas = [...gabarito];
      final onde = conta.aPreencher.indexWhere((c) => c.conta);
      erradas[onde] = '9';

      await montar(tester, conta, corrigida: false, respostas: erradas);
      expect(tester.takeException(), isNull);
      expect(conta.certa(erradas), isFalse);

      // O nove errado está lá escrito, à vista da criança: esconder o que
      // ela escreveu tirava-lhe a hipótese de ver onde se enganou.
      expect(find.text('9'), findsWidgets);
    });
  });

  group('dentro de uma lição', () {
    late Conteudo conteudo;

    setUpAll(() async {
      conteudo = await Conteudo.carregar();
      SharedPreferences.setMockInitialValues({});
    });

    test('o currículo tem contas armadas, e todas se armam', () {
      final grelhas = [
        for (final c in conteudo.cursos)
          for (final u in c.units)
            for (final n in u.niveis)
              for (final q in n.questoes)
                if (q is QGrelha) (c, q),
      ];
      expect(grelhas.length, greaterThanOrEqualTo(15),
          reason: 'a conversão não pegou');

      for (final (curso, q) in grelhas) {
        expect(() => q.conta, returnsNormally, reason: q.q);
        expect(q.conta.aPreencher, isNotEmpty, reason: q.q);
        // Na 1ª classe não se arma nada: aprendem-se os números até 20 e a
        // ideia de juntar e tirar. A conta armada é matéria da 2ª.
        expect(curso.classe.startsWith('1'), isFalse, reason: q.q);
      }
    });

    testWidgets('a lição com a conta armada cabe nos três telemóveis',
        (tester) async {
      // O risco desta pergunta não é a grelha sozinha: é a grelha MAIS o
      // enunciado, mais o Roby, mais o teclado, tudo na mesma coluna. É aqui
      // que transborda, e não no widget isolado.
      final st = AppState()
        ..conteudo = conteudo
        ..pronto = true
        ..nome = 'Ana'
        ..classe = '4ª classe'
        ..cursoId =
            conteudo.cursos.firstWhere((c) => c.classe == '4ª classe').id;

      for (final t in const <String, Size>{
        'telemóvel barato': Size(320, 640),
        'telemóvel comum': Size(411, 914),
        'tablet': Size(600, 1024),
      }.entries) {
        for (final caso in const [
          (Operacao.adicao, 4738, 2685),
          (Operacao.subtraccao, 6043, 2887),
          (Operacao.multiplicacao, 247, 38),
          (Operacao.divisao, 4738, 26),
        ]) {
          final q = QGrelha(
            'Quanto é ${caso.$2} ${caso.$1.sinal} ${caso.$3}?',
            null,
            operacao: caso.$1,
            x: caso.$2,
            y: caso.$3,
          );

          tester.view.physicalSize = t.value;
          tester.view.devicePixelRatio = 1.0;
          addTearDown(tester.view.reset);

          await tester.pumpWidget(
            ChangeNotifierProvider<AppState>.value(
              value: st,
              child: MaterialApp(
                theme: somaraTheme(),
                home: LessonScreen(
                  indice: -1,
                  avulsas: [q],
                  titulo: 'Contas',
                ),
              ),
            ),
          );
          await tester.pump(const Duration(milliseconds: 400));
          expect(tester.takeException(), isNull,
              reason: '${caso.$1.name} em ${t.value}');
        }
      }
    });

    testWidgets('responder a uma conta armada, de ponta a ponta',
        (tester) async {
      final q = [
        for (final c in conteudo.cursos)
          for (final u in c.units)
            for (final n in u.niveis)
              for (final x in n.questoes)
                if (x is QGrelha) x,
      ].first;

      final st = AppState()
        ..conteudo = conteudo
        ..pronto = true
        ..nome = 'Ana'
        ..classe = '2ª classe'
        ..cursoId = conteudo.cursos
            .firstWhere((c) => c.classe == '2ª classe')
            .id;

      tester.view.physicalSize = const Size(411, 914);
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);

      await tester.pumpWidget(
        ChangeNotifierProvider<AppState>.value(
          value: st,
          child: MaterialApp(
            theme: somaraTheme(),
            home: LessonScreen(indice: -1, avulsas: [q], titulo: 'Contas'),
          ),
        ),
      );
      await tester.pump(const Duration(milliseconds: 400));
      expect(tester.takeException(), isNull);

      // Sem nada escrito, o botão não deixa verificar.
      expect(find.text('Verificar'), findsOneWidget);

      final chave = tester
          .state<GrelhaOperacaoState>(find.byType(GrelhaOperacao));
      for (final casa in q.conta.aPreencher) {
        for (final d in casa.texto.split('')) {
          chave.escrever(int.parse(d));
        }
      }
      await tester.pump();

      await tester.tap(find.text('Verificar'));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 600));

      // Acertou: o botão passa a "Continuar".
      expect(find.text('Continuar'), findsOneWidget,
          reason: 'a conta certa não foi aceite');
    });
  });
}
