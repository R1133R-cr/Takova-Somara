import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/carteira.dart';
import 'package:somara/models/conquista.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/escadaria.dart';
import 'package:somara/screens/conquistas_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';
import 'package:somara/widgets/faixa_conquista.dart';

/// As conquistas.
///
/// Uma medalha só vale por duas coisas: chegar **uma vez** — repetida deixa
/// de ser um acontecimento — e **nunca desaparecer**. Uma criança que abre a
/// app e vê menos medalhas do que ontem não volta a acreditar no ecrã, e
/// nenhuma das duas falhas dá erro em lado nenhum.
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

  group('o catálogo', () {
    test('cada medalha tem título e pista', () {
      // Uma silhueta sem pista é um buraco na parede que não diz o que lá
      // deve estar, e ninguém persegue o que não sabe o que é.
      for (final c in Conquista.values) {
        expect(c.titulo.trim(), isNotEmpty, reason: c.name);
        expect(c.pistaDita.trim(), isNotEmpty, reason: c.name);
        expect(c.cristais, greaterThanOrEqualTo(0), reason: c.name);
      }
    });

    test('não há dois títulos iguais', () {
      final titulos = Conquista.values.map((c) => c.titulo).toList();
      expect(titulos.toSet(), hasLength(titulos.length));
    });

    test('cada jogo tem os seus seis degraus', () {
      for (final j in Jogo.values) {
        final suas = Conquista.values.where((c) => c.jogo == j).toList();
        expect(suas, hasLength(6), reason: j.rotulo);
        expect(
          suas.map((c) => c.degrau).toList(),
          [10, 50, 100, 250, 500, 1000],
          reason: j.rotulo,
        );
      }
    });

    test('a maior parte não paga nada', () {
      // Uma medalha que paga sempre deixa de ser medalha e passa a salário.
      final pagas = Conquista.values.where((c) => c.cristais > 0).length;
      expect(pagas, lessThan(Conquista.values.length / 2));
    });

    test('um aluno sem nada não tem medalha nenhuma', () {
      expect(conquistasDe(const RetratoDoAluno()), isEmpty);
    });

    test('um aluno que fez tudo tem-nas todas', () {
      // O teste que apanha uma condição esquecida: uma conquista nova sem
      // ramo no `switch` fica para sempre por ganhar, em silêncio.
      final tudo = RetratoDoAluno(
        niveis: 1000,
        unidades: 100,
        disciplinas: 20,
        classes: 6,
        perfeitos: 500,
        recuperadas: 50,
        diasSeguidos: 365,
        diasAEstudarPrimeiro: 60,
        especiaisNoPomar: 40,
        sopasPerfeitas: 9,
        degraus: {for (final j in Jogo.values) j: nivelMaximo},
      );
      expect(conquistasDe(tudo), hasLength(Conquista.values.length));
    });

    test('cada condição precisa mesmo do seu número', () {
      // Um a menos em cada eixo tem de deixar a medalha por ganhar.
      expect(alcancada(Conquista.tresDias, const RetratoDoAluno(diasSeguidos: 2)),
          isFalse);
      expect(alcancada(Conquista.tresDias, const RetratoDoAluno(diasSeguidos: 3)),
          isTrue);
      expect(alcancada(Conquista.cemNiveis, const RetratoDoAluno(niveis: 99)),
          isFalse);
      expect(
        alcancada(Conquista.pomar500, const RetratoDoAluno(degraus: {Jogo.pomar: 499})),
        isFalse,
      );
      expect(
        alcancada(Conquista.pomar500, const RetratoDoAluno(degraus: {Jogo.pomar: 500})),
        isTrue,
      );
      // E o degrau de um jogo não conta para outro.
      expect(
        alcancada(Conquista.sopa10, const RetratoDoAluno(degraus: {Jogo.pomar: 900})),
        isFalse,
      );
    });
  });

  group('no estado', () {
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
        ..classe = '1ª classe'
        ..cursoId = conteudo.cursos.first.id
        ..relogio = () => agora;
      return (st, (Duration d) => agora = agora.add(d));
    }

    List<int> daUnidade(AppState st, int qual) {
      final u = st.curso.units[qual];
      return [
        for (var i = 0; i < st.niveis.length; i++)
          if (st.niveis[i].unit.id == u.id) i,
      ];
    }

    test('o primeiro nível dá a primeira medalha, e uma faixa', () {
      final (st, _) = comRelogio();
      expect(st.conquistas, isEmpty);
      expect(st.proximaConquista, isNull);

      st.concluirNivel(0, 5, 5);
      expect(st.ganhou(Conquista.primeiroNivel), isTrue);
      expect(st.ganhou(Conquista.nivelPerfeito), isTrue);
      expect(st.proximaConquista, isNotNull);
    });

    test('cada medalha chega uma vez e só uma', () {
      final (st, _) = comRelogio();
      st.concluirNivel(0, 5, 5);
      while (st.tirarConquista() != null) {}

      for (var v = 0; v < 5; v++) {
        st.concluirNivel(0, 5, 5);
      }
      expect(st.proximaConquista, isNull,
          reason: 'a mesma medalha voltou a disparar');
    });

    test('a fila entrega-as por ordem e esvazia-se', () {
      final (st, _) = comRelogio();
      for (final i in daUnidade(st, 0)) {
        st.concluirNivel(i, 5, 5);
      }
      final vistas = <Conquista>[];
      for (var c = st.tirarConquista(); c != null; c = st.tirarConquista()) {
        vistas.add(c);
      }
      expect(vistas, contains(Conquista.primeiroNivel));
      expect(vistas, contains(Conquista.primeiraUnidade));
      expect(vistas.toSet(), hasLength(vistas.length), reason: 'repetiu');
      expect(st.proximaConquista, isNull);
    });

    test('a medalha paga os cristais que promete, uma vez', () {
      final (st, _) = comRelogio();
      for (final i in daUnidade(st, 0)) {
        st.concluirNivel(i, 5, 5);
      }
      // A unidade perfeita paga por dois caminhos, e são dois de propósito:
      // o marco do §6 (a unidade sem erros) e a medalha da primeira unidade.
      expect(st.ganhou(Conquista.primeiraUnidade), isTrue);
      expect(st.carteira.cc,
          Carteira.cristalPorUnidadePerfeita + Conquista.primeiraUnidade.cristais);

      final antes = st.carteira.cc;
      for (var v = 0; v < 3; v++) {
        st.concluirNivel(daUnidade(st, 0).last, 5, 5);
      }
      expect(st.carteira.cc, antes, reason: 'a medalha pagou outra vez');
    });

    test('subir no joguinho dá as medalhas do jogo', () {
      final (st, _) = comRelogio();
      for (var v = 0; v < 10; v++) {
        st.subirNivelDe(Jogo.sopa);
      }
      expect(st.ganhou(Conquista.sopa10), isTrue);
      expect(st.ganhou(Conquista.pomar10), isFalse,
          reason: 'a Sopa deu medalha ao Pomar');
    });

    test('as medalhas que só se vêem de dentro de um jogo', () {
      // Não são degraus da escadaria: acontecem a meio de um nível, e por
      // isso foi preciso o jogo avisar. Ficaram de fora quando as medalhas
      // nasceram, e entram agora que a Sorte instrumentou os dois jogos.
      final (st, _) = comRelogio();
      expect(st.ganhou(Conquista.primeiraEspecial), isFalse);
      st.registarPecaEspecial();
      expect(st.ganhou(Conquista.primeiraEspecial), isTrue);

      expect(st.ganhou(Conquista.sopaSemFalhar), isFalse);
      st.registarSopaPerfeita();
      expect(st.ganhou(Conquista.sopaSemFalhar), isTrue);
    });

    test('acertar o que se tinha errado conta', () {
      final (st, _) = comRelogio();
      final q = st.conteudo.cursos.first.units.first.niveis.first.questoes.first;
      st.marcarErrada(q.q);
      st.marcarAprendida(q.q);
      expect(st.ganhou(Conquista.recuperada), isTrue);
    });

    test('sete dias seguidos', () {
      final (st, passar) = comRelogio();
      for (var dia = 0; dia < 3; dia++) {
        st.concluirNivel(0, 3, 5);
        passar(const Duration(days: 1));
      }
      expect(st.ganhou(Conquista.tresDias), isTrue);
      expect(st.ganhou(Conquista.umaSemana), isFalse);

      for (var dia = 0; dia < 4; dia++) {
        st.concluirNivel(0, 3, 5);
        passar(const Duration(days: 1));
      }
      expect(st.ganhou(Conquista.umaSemana), isTrue);
    });

    group('primeiro a escola', () {
      test('cinco dias a estudar antes de jogar', () {
        final (st, passar) = comRelogio();
        for (var dia = 0; dia < 5; dia++) {
          st.concluirNivel(0, 3, 5);
          st.entrarNoJogo();
          st.sairDoJogo();
          passar(const Duration(days: 1));
        }
        expect(st.ganhou(Conquista.estudarPrimeiro), isTrue);
      });

      test('jogar primeiro parte a corrente', () {
        final (st, passar) = comRelogio();
        for (var dia = 0; dia < 4; dia++) {
          st.concluirNivel(0, 3, 5);
          passar(const Duration(days: 1));
        }
        // No quinto dia abre os joguinhos primeiro.
        st.entrarNoJogo();
        st.sairDoJogo();
        st.concluirNivel(0, 3, 5);
        passar(const Duration(days: 1));
        st.concluirNivel(0, 3, 5);

        expect(st.ganhou(Conquista.estudarPrimeiro), isFalse,
            reason: 'a corrente devia ter partido no dia em que jogou antes');
      });

      test('um dia falhado recomeça a contagem', () {
        final (st, passar) = comRelogio();
        for (var dia = 0; dia < 4; dia++) {
          st.concluirNivel(0, 3, 5);
          passar(const Duration(days: 1));
        }
        passar(const Duration(days: 2)); // dois dias sem abrir a app
        st.concluirNivel(0, 3, 5);
        expect(st.ganhou(Conquista.estudarPrimeiro), isFalse);
      });
    });

    test('as medalhas nunca desaparecem numa sincronização', () {
      // Um telemóvel com A e B, outro com B e C → ficam os dois com A, B e C.
      final (aqui, _) = comRelogio();
      for (var v = 0; v < 10; v++) {
        aqui.subirNivelDe(Jogo.sopa);
      }
      expect(aqui.ganhou(Conquista.sopa10), isTrue);
      expect(aqui.ganhou(Conquista.pomar10), isFalse);

      final (la, _) = comRelogio();
      for (var v = 0; v < 10; v++) {
        la.subirNivelDe(Jogo.pomar);
      }

      aqui.fundirDaNuvem(la.paraNuvem());
      expect(aqui.ganhou(Conquista.sopa10), isTrue, reason: 'perdeu a sua');
      expect(aqui.ganhou(Conquista.pomar10), isTrue, reason: 'não trouxe a outra');
    });

    test('o que se recuperou fica pelo maior dos dois', () {
      final (aqui, _) = comRelogio();
      final (la, _) = comRelogio();
      final qs = la.conteudo.cursos.first.units.first.niveis.first.questoes;
      for (final q in qs.take(3)) {
        la.marcarErrada(q.q);
        la.marcarAprendida(q.q);
      }
      aqui.fundirDaNuvem(la.paraNuvem());
      expect(aqui.retrato.recuperadas, 3);
    });
  });

  group('a faixa', () {
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

    testWidgets('desliza, diz o que se ganhou e sai sozinha', (tester) async {
      final st = estado();
      tester.view.physicalSize = const Size(411, 914);
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);

      await tester.pumpWidget(
        ChangeNotifierProvider<AppState>.value(
          value: st,
          child: MaterialApp(
            theme: somaraTheme(),
            builder: (_, filho) => FaixaDeConquistas(child: filho!),
            home: const Scaffold(body: Center(child: Text('a lição'))),
          ),
        ),
      );
      await tester.pump();
      expect(find.text('CONQUISTA'), findsNothing);

      st.concluirNivel(0, 5, 5);
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 600));

      // A palavra escreve-se letra a letra; ao fim de meio segundo já lá está.
      await tester.pump(const Duration(milliseconds: 500));
      expect(find.text('CONQUISTA'), findsOneWidget);
      expect(find.text(Conquista.primeiroNivel.titulo), findsOneWidget);

      // E a lição por baixo nunca desapareceu.
      expect(find.text('a lição'), findsOneWidget);

      // Sai sozinha, sem se tocar em nada.
      await tester.pump(FaixaDeConquistas.paragem);
      await tester.pump(const Duration(milliseconds: 600));
      await tester.pump();
      expect(find.text('CONQUISTA'), findsNothing);
    });

    // A faixa com o título mais comprido que existe, nos três tamanhos. É a
    // comprida que transborda, e ela nunca aparece nos testes de cima
    // porque só se ganha depois de uma disciplina inteira.
    final comprida = Conquista.values.reduce(
      (a, b) => a.titulo.length >= b.titulo.length ? a : b,
    );
    for (final t in const <String, Size>{
      'telemóvel barato': Size(320, 640),
      'telemóvel comum': Size(411, 914),
      'tablet': Size(600, 1024),
    }.entries) {
      testWidgets('cabe num ${t.key}, com o título mais comprido',
          (tester) async {
        final st = estado();
        tester.view.physicalSize = t.value;
        tester.view.devicePixelRatio = 1.0;
        addTearDown(tester.view.reset);

        await tester.pumpWidget(
          ChangeNotifierProvider<AppState>.value(
            value: st,
            child: MaterialApp(
              theme: somaraTheme(),
              builder: (_, filho) => FaixaDeConquistas(child: filho!),
              home: const Scaffold(body: SizedBox()),
            ),
          ),
        );
        st.encomendarFaixa(comprida);
        await tester.pump();
        await tester.pump(const Duration(milliseconds: 600));

        expect(tester.takeException(), isNull, reason: 'faixa em ${t.value}');
        expect(find.text(comprida.titulo), findsOneWidget);

        await tester.pump(FaixaDeConquistas.paragem);
        await tester.pump(const Duration(milliseconds: 600));
        await tester.pump();
      });
    }

    testWidgets('não trava o toque no que está por baixo', (tester) async {
      // A promessa do §2: «a lição não pára, a faixa passa por cima e a
      // criança continua».
      final st = estado();
      var tocou = false;

      await tester.pumpWidget(
        ChangeNotifierProvider<AppState>.value(
          value: st,
          child: MaterialApp(
            theme: somaraTheme(),
            builder: (_, filho) => FaixaDeConquistas(child: filho!),
            home: Scaffold(
              body: Align(
                alignment: Alignment.topCenter,
                child: GestureDetector(
                  onTap: () => tocou = true,
                  child: const SizedBox(
                    width: 300,
                    height: 120,
                    child: Text('responder'),
                  ),
                ),
              ),
            ),
          ),
        ),
      );
      st.concluirNivel(0, 5, 5);
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 600));
      // A palavra ainda se está a escrever letra a letra; o que interessa
      // aqui é a faixa estar à vista, e o título já lá está desde o início.
      expect(find.text(Conquista.primeiroNivel.titulo), findsOneWidget);

      await tester.tap(find.text('responder'), warnIfMissed: false);
      await tester.pump();
      expect(tocou, isTrue, reason: 'a faixa comeu o toque da lição');

      // Deixa a faixa acabar de sair: o teste não pode terminar com o
      // temporizador dela ainda a correr.
      await tester.pump(FaixaDeConquistas.paragem);
      await tester.pump(const Duration(milliseconds: 600));
      await tester.pump();
    });
  });

  group('o histórico', () {
    late Conteudo conteudo;

    setUpAll(() async {
      conteudo = await Conteudo.carregar();
      SharedPreferences.setMockInitialValues({});
    });

    const tamanhos = <String, Size>{
      'telemóvel barato': Size(320, 640),
      'telemóvel comum': Size(411, 914),
      'tablet': Size(600, 1024),
    };

    for (final t in tamanhos.entries) {
      testWidgets('cabe num ${t.key}', (tester) async {
        final st = AppState()
          ..conteudo = conteudo
          ..pronto = true
          ..classe = '1ª classe'
          ..cursoId = conteudo.cursos.first.id;
        st.concluirNivel(0, 5, 5);

        tester.view.physicalSize = t.value;
        tester.view.devicePixelRatio = 1.0;
        addTearDown(tester.view.reset);
        await tester.pumpWidget(
          ChangeNotifierProvider<AppState>.value(
            value: st,
            child: MaterialApp(
              theme: somaraTheme(),
              home: const ConquistasScreen(),
            ),
          ),
        );
        await tester.pump(const Duration(milliseconds: 400));
        expect(tester.takeException(), isNull, reason: 'medalhas em ${t.value}');
      });
    }
  });
}
