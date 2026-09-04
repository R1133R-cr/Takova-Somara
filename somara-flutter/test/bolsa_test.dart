import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/bolsa_de_tempo.dart';
import 'package:somara/models/content.dart';
import 'package:somara/screens/joguinhos_screen.dart';
import 'package:somara/services/ciclo_de_vida.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';
import 'package:somara/widgets/relogio_de_jogo.dart';

/// A bolsa de tempo de jogo.
///
/// Isto é uma promessa a duas pessoas ao mesmo tempo, e as duas têm de a ver
/// cumprida: à criança, que o tempo que ela ganhou a estudar não desaparece;
/// ao pai, que a app não vira televisão. Um erro de contas aqui quebra uma
/// das duas — e nenhum deles daria erro em lado nenhum.
///
/// O relógio é falso de propósito: sem isso não há maneira de provar que a
/// bolsa se repõe à meia-noite sem esperar pela meia-noite.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  // O audioplayers não tem implementação nativa num teste, e criar o
  // primeiro leitor atira um MissingPluginException por um future que
  // ninguém está a ouvir — que o test framework atribui, ao calhas, ao teste
  // que estiver a correr nesse instante. Os testes de ecrã escondem-no com
  // `takeException`; aqui responde-se-lhe, que é mais honesto.
  setUpAll(() {
    for (final canal in const [
      MethodChannel('xyz.luan/audioplayers.global'),
      MethodChannel('xyz.luan/audioplayers'),
    ]) {
      TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger
          .setMockMethodCallHandler(canal, (_) async => null);
    }
  });

  group('o modelo', () {
    const hoje = '2026-09-04';
    const ontem = '2026-09-03';

    test('um dia começa com dez minutos de graça', () {
      const b = BolsaDeTempo.doDia(hoje);
      expect(b.restante, const Duration(minutes: 10));
      expect(b.vazia, isFalse);
    });

    test('gasta quatro dos dez e restam seis', () {
      final b = const BolsaDeTempo.doDia(hoje)
          .comGasto(const Duration(minutes: 4));
      expect(b.restante, const Duration(minutes: 6));
    });

    test('um nível concluído dá mais cinco; sem erros dá oito', () {
      final normal = const BolsaDeTempo.doDia(hoje)
          .comGanho(BolsaDeTempo.porNivel);
      final perfeito = const BolsaDeTempo.doDia(hoje)
          .comGanho(BolsaDeTempo.porNivelPerfeito);
      expect(normal.restante, const Duration(minutes: 15));
      expect(perfeito.restante, const Duration(minutes: 18));
    });

    test('o tecto trava aos sessenta, por mais que se estude', () {
      var b = const BolsaDeTempo.doDia(hoje);
      for (var i = 0; i < 40; i++) {
        b = b.comGanho(BolsaDeTempo.porNivel);
      }
      expect(b.concedido, BolsaDeTempo.tecto);
      expect(b.restante, BolsaDeTempo.tecto);
      expect(b.noTecto, isTrue);
    });

    test('gastar a mais não deixa o saldo negativo', () {
      // Um número negativo à frente de uma criança de sete anos não quer
      // dizer nada, e um `Duration` negativo lá dentro estragava as contas.
      final b = const BolsaDeTempo.doDia(hoje)
          .comGasto(const Duration(hours: 3));
      expect(b.restante, Duration.zero);
      expect(b.vazia, isTrue);
    });

    test('à meia-noite a bolsa é outra', () {
      // Ontem estudou-se muito e jogou-se tudo: quarenta ganhos, quarenta
      // gastos, saldo zero.
      final gasta = const BolsaDeTempo.doDia(ontem)
          .comGanho(const Duration(minutes: 30))
          .comGasto(const Duration(minutes: 40));
      expect(gasta.restante, Duration.zero);

      final nova = gasta.noDia(hoje);
      expect(nova.dia, hoje);
      expect(nova.restante, BolsaDeTempo.gratis,
          reason: 'o dia novo devia começar do princípio');
      // E o que se ganhou ontem não transita: senão bastava um sábado de
      // estudo para se ter o tecto todos os dias da semana seguinte.
      expect(nova.ganho, 0);
    });

    test('o mesmo dia não é reposto', () {
      final b = const BolsaDeTempo.doDia(hoje)
          .comGasto(const Duration(minutes: 3));
      expect(b.noDia(hoje).gasto, const Duration(minutes: 3).inSeconds);
    });

    test('vai e volta pelo JSON sem se perder', () {
      final b = const BolsaDeTempo.doDia(hoje)
          .comGanho(const Duration(minutes: 5))
          .comGasto(const Duration(minutes: 2));
      final volta = BolsaDeTempo.deJson(b.paraJson())!;
      expect(volta.dia, b.dia);
      expect(volta.ganho, b.ganho);
      expect(volta.gasto, b.gasto);
    });

    test('JSON estragado não rebenta nada', () {
      expect(BolsaDeTempo.deJson(null), isNull);
      expect(BolsaDeTempo.deJson({'dia': ''}), isNull);
      expect(BolsaDeTempo.deJson({'ganho': 5}), isNull);
    });

    group('a fusão com a nuvem', () {
      test('o que se estudou noutro telemóvel conta', () {
        final aqui = const BolsaDeTempo.doDia(hoje);
        final la = const BolsaDeTempo.doDia(hoje)
            .comGanho(const Duration(minutes: 20));
        expect(aqui.fundirCom(la).restante, const Duration(minutes: 30));
      });

      test('o que se jogou noutro telemóvel também', () {
        // É o ponto que decide se o tecto diário quer dizer alguma coisa.
        // Ficar pelo maior SALDO em vez do maior gasto dava isto: jogar dez
        // minutos, entrar na conta noutro aparelho, e os dez voltarem.
        final aqui = const BolsaDeTempo.doDia(hoje);
        final la = const BolsaDeTempo.doDia(hoje)
            .comGasto(const Duration(minutes: 7));
        expect(aqui.fundirCom(la).restante, const Duration(minutes: 3));
      });

      test('a bolsa de ontem não mexe na de hoje', () {
        final hojeB = const BolsaDeTempo.doDia(hoje)
            .comGasto(const Duration(minutes: 8));
        final ontemB = const BolsaDeTempo.doDia(ontem)
            .comGanho(const Duration(minutes: 50));
        expect(hojeB.fundirCom(ontemB).dia, hoje);
        expect(hojeB.fundirCom(ontemB).restante, const Duration(minutes: 2));
      });
    });

    test('o tempo diz-se como se diz a uma criança', () {
      expect(tempoEmPalavras(const Duration(minutes: 10)), '10 min');
      expect(tempoEmPalavras(const Duration(seconds: 40)), '40 s');
      expect(tempoEmPalavras(Duration.zero), '0 s');
      // "0 min" com quarenta segundos por gastar seria mentira, e é aí que
      // a criança está a olhar para o número.
      expect(tempoEmPalavras(const Duration(seconds: 59)), '59 s');

      expect(quantoFalta(const Duration(seconds: 40)), 'Faltam 40 s');
      expect(quantoFalta(const Duration(seconds: 1)), 'Falta 1 s');
      expect(quantoFalta(const Duration(seconds: 90)), 'Falta 1 min');
      expect(quantoFalta(const Duration(minutes: 2)), 'Faltam 2 min');
    });
  });

  group('o relógio do estado', () {
    late Conteudo conteudo;

    setUpAll(() async {
      conteudo = await Conteudo.carregar();
      SharedPreferences.setMockInitialValues({});
    });

    /// Um estado com um relógio que só anda quando o teste mandar.
    (AppState, void Function(Duration)) comRelogio() {
      var agora = DateTime(2026, 9, 4, 15, 0);
      final st = AppState()
        ..conteudo = conteudo
        ..classe = '1ª classe'
        ..relogio = () => agora;
      return (st, (Duration d) => agora = agora.add(d));
    }

    test('sem jogar, nada se gasta', () {
      final (st, passar) = comRelogio();
      passar(const Duration(hours: 2));
      expect(st.tempoDeJogo, BolsaDeTempo.gratis);
      expect(st.podeJogar, isTrue);
    });

    test('o tempo dentro de um jogo desconta-se', () {
      final (st, passar) = comRelogio();
      st.entrarNoJogo();
      passar(const Duration(minutes: 4));
      expect(st.tempoDeJogo, const Duration(minutes: 6));
      st.sairDoJogo();
      expect(st.tempoDeJogo, const Duration(minutes: 6),
          reason: 'sair não pode mudar a conta');
    });

    test('fora do jogo o relógio está parado', () {
      final (st, passar) = comRelogio();
      st.entrarNoJogo();
      passar(const Duration(minutes: 3));
      st.sairDoJogo();
      passar(const Duration(hours: 5));
      expect(st.tempoDeJogo, const Duration(minutes: 7));
    });

    test('com a app minimizada o relógio pára', () {
      // Quem atende uma chamada a meio do Pomar não paga por essa chamada,
      // e um telemóvel esquecido em cima da mesa não gasta a tarde toda.
      final (st, passar) = comRelogio();
      st.entrarNoJogo();
      passar(const Duration(minutes: 2));

      st.pausarTempoDeJogo();
      passar(const Duration(hours: 3));
      expect(st.tempoDeJogo, const Duration(minutes: 8),
          reason: 'contou tempo com a app fechada');

      st.retomarTempoDeJogo();
      passar(const Duration(minutes: 1));
      expect(st.tempoDeJogo, const Duration(minutes: 7));
    });

    test('a app em segundo plano pára mesmo o relógio', () {
      // O teste anterior chama o pausar à mão. Este passa pelo caminho real:
      // é o sistema operativo que avisa, e é essa ligação que se parte sem
      // ninguém dar por ela.
      final (st, passar) = comRelogio();
      final ciclo = CicloDeVida(st);
      st.entrarNoJogo();
      passar(const Duration(minutes: 2));

      ciclo.didChangeAppLifecycleState(AppLifecycleState.paused);
      passar(const Duration(hours: 3));
      expect(st.tempoDeJogo, const Duration(minutes: 8));

      ciclo.didChangeAppLifecycleState(AppLifecycleState.resumed);
      passar(const Duration(minutes: 1));
      expect(st.tempoDeJogo, const Duration(minutes: 7));
    });

    test('a barra de notificações meio aberta não pára o jogo', () {
      // `inactive` é transitório e a app continua à vista. Parar aqui daria
      // um relógio aos saltos e, pior, um `resumed` que nem sempre chega.
      final (st, passar) = comRelogio();
      final ciclo = CicloDeVida(st);
      st.entrarNoJogo();
      ciclo.didChangeAppLifecycleState(AppLifecycleState.inactive);
      passar(const Duration(minutes: 3));
      expect(st.tempoDeJogo, const Duration(minutes: 7));
    });

    test('retomar sem jogo aberto não arranca nada', () {
      final (st, passar) = comRelogio();
      st.retomarTempoDeJogo();
      passar(const Duration(minutes: 30));
      expect(st.tempoDeJogo, BolsaDeTempo.gratis);
    });

    test('a bolsa esgota-se e o jogo fecha-se', () {
      final (st, passar) = comRelogio();
      st.entrarNoJogo();
      passar(const Duration(minutes: 25));
      expect(st.tempoDeJogo, Duration.zero);
      expect(st.podeJogar, isFalse);
    });

    test('concluir um nível enche a bolsa', () {
      final (st, passar) = comRelogio();
      st.entrarNoJogo();
      passar(const Duration(minutes: 10));
      st.sairDoJogo();
      expect(st.podeJogar, isFalse);

      // Um nível com um erro: mais cinco minutos.
      st.concluirNivel(0, 4, 5);
      expect(st.tempoDeJogo, BolsaDeTempo.porNivel);

      // Um nível sem erros: mais oito.
      st.concluirNivel(0, 5, 5);
      expect(st.tempoDeJogo,
          BolsaDeTempo.porNivel + BolsaDeTempo.porNivelPerfeito);
    });

    test('jogar não enche a bolsa', () {
      // Seria um círculo: jogar para ganhar tempo de jogo. O treino dá XP e
      // conta para a sequência, mas não paga tempo.
      final (st, passar) = comRelogio();
      st.entrarNoJogo();
      passar(const Duration(minutes: 6));
      st.concluirTreino(10);
      st.sairDoJogo();
      expect(st.tempoDeJogo, const Duration(minutes: 4));
    });

    test('à meia-noite a bolsa enche-se outra vez', () {
      final (st, passar) = comRelogio();
      st.entrarNoJogo();
      passar(const Duration(minutes: 10));
      st.sairDoJogo();
      expect(st.podeJogar, isFalse);

      passar(const Duration(hours: 10)); // passa da meia-noite
      expect(st.tempoDeJogo, BolsaDeTempo.gratis);
      expect(st.podeJogar, isTrue);
    });

    test('a nuvem nunca devolve minutos já jogados', () {
      final (st, passar) = comRelogio();
      st.entrarNoJogo();
      passar(const Duration(minutes: 6));
      st.sairDoJogo();
      expect(st.tempoDeJogo, const Duration(minutes: 4));

      // A nuvem tinha uma cópia de antes de se jogar.
      st.fundirDaNuvem({
        'bolsa': const BolsaDeTempo.doDia('2026-09-04').paraJson(),
      });
      expect(st.tempoDeJogo, const Duration(minutes: 4),
          reason: 'entrar na conta não pode devolver tempo gasto');

      // Mas o que se estudou noutro telemóvel conta.
      st.fundirDaNuvem({
        'bolsa': const BolsaDeTempo.doDia('2026-09-04')
            .comGanho(const Duration(minutes: 20))
            .paraJson(),
      });
      expect(st.tempoDeJogo, const Duration(minutes: 24));
    });

    test('o saldo vai e volta pelo JSON da nuvem', () {
      final (st, passar) = comRelogio();
      st.entrarNoJogo();
      passar(const Duration(minutes: 3));
      st.sairDoJogo();

      final outro = AppState()
        ..conteudo = conteudo
        ..classe = '1ª classe'
        ..relogio = st.relogio
        ..fundirDaNuvem(st.paraNuvem());
      expect(outro.tempoDeJogo, const Duration(minutes: 7));
    });

    test('o estudo nunca é travado pela bolsa', () {
      // A regra que separa as duas travagens: os corações limitam os
      // exercícios, a bolsa limita os jogos. Uma criança sem tempo de jogo
      // continua a poder estudar — e é justamente aí que se quer que ela vá.
      final (st, passar) = comRelogio();
      st.entrarNoJogo();
      passar(const Duration(minutes: 30));
      st.sairDoJogo();

      expect(st.podeJogar, isFalse);
      expect(st.lives, greaterThan(0));
      expect(st.bloqueado, isFalse);
    });
  });

  group('o ecrã dos joguinhos', () {
    late Conteudo conteudo;

    setUpAll(() async {
      conteudo = await Conteudo.carregar();
      SharedPreferences.setMockInitialValues({});
    });

    (AppState, void Function(Duration)) comRelogio() {
      var agora = DateTime(2026, 9, 4, 15, 0);
      final st = AppState()
        ..conteudo = conteudo
        ..pronto = true
        ..nome = 'Ana'
        ..classe = '1ª classe'
        ..cursoId = conteudo.cursos.first.id
        // Por último: numa cascata, o corpo de `=> agora` engolia a linha
        // seguinte e o `..cursoId` ia parar ao DateTime.
        ..relogio = () => agora;
      return (st, (Duration d) => agora = agora.add(d));
    }

    Future<void> montar(WidgetTester tester, AppState st,
        {VoidCallback? aoIrEstudar}) async {
      tester.view.physicalSize = const Size(411, 914);
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);
      await tester.pumpWidget(
        ChangeNotifierProvider<AppState>.value(
          value: st,
          child: MaterialApp(
            theme: somaraTheme(),
            home: Scaffold(
              backgroundColor: S.gm950,
              body: JoguinhosScreen(aoIrEstudar: aoIrEstudar),
            ),
          ),
        ),
      );
      await tester.pump(const Duration(milliseconds: 300));
    }

    testWidgets('mostra sempre os minutos que restam', (tester) async {
      final (st, passar) = comRelogio();
      await montar(tester, st);
      expect(find.text('10 min de jogo'), findsOneWidget);

      st.entrarNoJogo();
      passar(const Duration(minutes: 6));
      st.sairDoJogo();
      await tester.pump();
      expect(find.text('4 min de jogo'), findsOneWidget);
    });

    testWidgets('com a bolsa vazia, os cartões fecham e há por onde ir',
        (tester) async {
      final (st, passar) = comRelogio();
      st.entrarNoJogo();
      passar(const Duration(minutes: 10));
      st.sairDoJogo();
      expect(st.podeJogar, isFalse);

      var foiEstudar = false;
      await montar(tester, st, aoIrEstudar: () => foiEstudar = true);

      expect(find.text('Acabou o tempo de jogo de hoje'), findsOneWidget);
      expect(find.text('Estuda um nível e ganhas mais cinco minutos.'),
          findsOneWidget);

      // Os cartões continuam à vista — esconder os jogos deixaria a criança
      // sem perceber que eles existem — mas não respondem ao toque.
      expect(find.text('Crossmath'), findsOneWidget);
      final barreira = tester.widget<IgnorePointer>(
        find.ancestor(
          of: find.text('Crossmath'),
          matching: find.byType(IgnorePointer),
        ).first,
      );
      expect(barreira.ignoring, isTrue);

      await tester.tap(find.text('Ir estudar'));
      await tester.pump();
      expect(foiEstudar, isTrue, reason: 'o botão tem de levar à amarelinha');
    });

    testWidgets('com tempo, os cartões respondem', (tester) async {
      final (st, _) = comRelogio();
      await montar(tester, st);
      final barreira = tester.widget<IgnorePointer>(
        find.ancestor(
          of: find.text('Crossmath'),
          matching: find.byType(IgnorePointer),
        ).first,
      );
      expect(barreira.ignoring, isFalse);
      expect(find.text('Ir estudar'), findsNothing);
    });
  });

  group('o relógio dentro do jogo', () {
    late Conteudo conteudo;

    setUpAll(() async {
      conteudo = await Conteudo.carregar();
      SharedPreferences.setMockInitialValues({});
    });

    testWidgets('avisa no último minuto e fecha o jogo ao acabar',
        (tester) async {
      var agora = DateTime(2026, 9, 4, 15, 0);
      final st = AppState()
        ..conteudo = conteudo
        ..pronto = true
        ..classe = '1ª classe'
        ..cursoId = conteudo.cursos.first.id
        ..relogio = () => agora;

      /// Deixa a bolsa quase vazia sem entrar em jogo nenhum.
      void gastar(Duration d) {
        st.entrarNoJogo();
        agora = agora.add(d);
        st.sairDoJogo();
      }

      gastar(const Duration(minutes: 8, seconds: 30));
      expect(st.tempoDeJogo, const Duration(minutes: 1, seconds: 30));

      await tester.pumpWidget(
        // O provider fica ACIMA do MaterialApp, como na app: um jogo é uma
        // rota empilhada, e providers metidos no `home:` não chegam lá.
        ChangeNotifierProvider<AppState>.value(
          value: st,
          child: MaterialApp(
            theme: somaraTheme(),
            home: Builder(
              builder: (ctx) => Scaffold(
                body: Center(
                  child: GestureDetector(
                    onTap: () => Navigator.of(ctx).push(
                      MaterialPageRoute<void>(
                        builder: (_) => const RelogioDeJogo(
                          child: Scaffold(body: Center(child: Text('a jogar'))),
                        ),
                      ),
                    ),
                    child: const Text('abrir'),
                  ),
                ),
              ),
            ),
          ),
        ),
      );

      await tester.tap(find.text('abrir'));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 400));
      expect(find.text('a jogar'), findsOneWidget);

      // Falta mais de um minuto: nenhum relógio à vista. Uma criança a ver
      // uma contagem decrescente não está a jogar, está a ver o tempo acabar.
      expect(find.textContaining('Falta'), findsNothing);

      agora = agora.add(const Duration(seconds: 31));
      await tester.pump(const Duration(seconds: 1));
      expect(find.textContaining('Falta'), findsOneWidget);

      // E agora acaba.
      agora = agora.add(const Duration(seconds: 60));
      await tester.pump(const Duration(seconds: 1));
      expect(find.text('Acabou o tempo de jogo'), findsOneWidget,
          reason: 'um jogo que desaparece sem explicação lê-se como avaria');
      expect(find.text('a jogar'), findsOneWidget,
          reason: 'ainda não fechou — o aviso tem de se poder ler');

      // O temporizador de segundo a segundo já foi cancelado pelo fecho, e
      // por isso o `pumpAndSettle` já assenta em vez de correr para sempre.
      await tester.pump(const Duration(milliseconds: 1600));
      await tester.pumpAndSettle();
      expect(find.text('a jogar'), findsNothing, reason: 'devia ter fechado');
      expect(find.text('abrir'), findsOneWidget);

      await tester.pump();
      expect(st.tempoDeJogo, Duration.zero);
      expect(st.podeJogar, isFalse);
    });

    testWidgets('o tempo do jogo sai mesmo da bolsa', (tester) async {
      var agora = DateTime(2026, 9, 4, 15, 0);
      final st = AppState()
        ..conteudo = conteudo
        ..pronto = true
        ..classe = '1ª classe'
        ..cursoId = conteudo.cursos.first.id
        ..relogio = () => agora;

      await tester.pumpWidget(
        ChangeNotifierProvider<AppState>.value(
          value: st,
          child: MaterialApp(
            theme: somaraTheme(),
            home: const RelogioDeJogo(
              child: Scaffold(body: Center(child: Text('a jogar'))),
            ),
          ),
        ),
      );
      await tester.pump();

      agora = agora.add(const Duration(minutes: 3));
      await tester.pump(const Duration(seconds: 1));
      expect(st.tempoDeJogo, const Duration(minutes: 7));

      // Desmontar fecha a conta.
      await tester.pumpWidget(const MaterialApp(home: SizedBox()));
      await tester.pump();
      expect(st.tempoDeJogo, const Duration(minutes: 7));
    });
  });
}
