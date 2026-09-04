import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/campanha.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/sorte.dart';
import 'package:somara/screens/praticar_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';

/// A campanha da semana.
///
/// É o único sítio da app com prazo, e é isso que a torna fácil de partir em
/// silêncio: uma campanha que muda a meio da semana deixa de ter prazo, uma
/// que paga duas vezes deixa de ter valor, e uma que não aparece deixa de
/// existir sem ninguém reparar. Nenhuma das três dá erro em lado nenhum.
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

  group('a semana', () {
    test('a segunda-feira de um dia qualquer', () {
      // 2026-09-04 é uma sexta; a segunda dessa semana é 31 de Agosto.
      expect(segundaDe(DateTime(2026, 9, 4)), '2026-08-31');
      expect(segundaDe(DateTime(2026, 8, 31)), '2026-08-31');
      // Domingo pertence à semana que começou na segunda anterior.
      expect(segundaDe(DateTime(2026, 9, 6)), '2026-08-31');
      // E a segunda seguinte já é outra semana.
      expect(segundaDe(DateTime(2026, 9, 7)), '2026-09-07');
    });

    test('a hora do dia não muda a semana', () {
      expect(segundaDe(DateTime(2026, 9, 4, 23, 59)), '2026-08-31');
      expect(segundaDe(DateTime(2026, 9, 4, 0, 1)), '2026-08-31');
    });

    test('a semente é a mesma em qualquer telemóvel', () {
      // O `hashCode` das strings do Dart não é garantido entre execuções, e
      // a campanha tem de sair igual nos dois aparelhos da mesma criança.
      expect(sementeDaSemana('2026-08-31'), sementeDaSemana('2026-08-31'));
      expect(sementeDaSemana('2026-08-31'),
          isNot(sementeDaSemana('2026-09-07')));
      expect(sementeDaSemana('2026-08-31'), greaterThan(0));
    });
  });

  group('a escolha das perguntas', () {
    List<String> muitas(String prefixo, int n) =>
        [for (var i = 0; i < n; i++) '$prefixo $i'];

    test('junta as duas fontes', () {
      final p = escolherPerguntas(
        dosErros: muitas('erro', 6),
        doEstudo: muitas('estudo', 30),
        semente: 1,
      );
      expect(p, hasLength(Campanha.maximo));
      expect(p.where((e) => e.startsWith('erro')), hasLength(6));
      expect(p.where((e) => e.startsWith('estudo')), hasLength(14));
    });

    test('os erros não comem a campanha toda', () {
      // Uma criança com trinta erros por rever teria uma campanha só de
      // erros, e nunca reveria a matéria nova da semana.
      final p = escolherPerguntas(
        dosErros: muitas('erro', 40),
        doEstudo: muitas('estudo', 40),
        semente: 2,
      );
      expect(p.where((e) => e.startsWith('erro')),
          hasLength(Campanha.metadeDosErros));
    });

    test('mas enchem o resto quando não há matéria nova', () {
      // O limite de metade é para não taparem o estudo, não para deixar a
      // campanha curta quando não há estudo nenhum.
      final p = escolherPerguntas(
        dosErros: muitas('erro', 40),
        doEstudo: const [],
        semente: 3,
      );
      expect(p, hasLength(Campanha.maximo));
    });

    test('sem material que chegue não há campanha', () {
      expect(
        escolherPerguntas(dosErros: const [], doEstudo: const [], semente: 4),
        isEmpty,
      );
      expect(
        escolherPerguntas(
          dosErros: muitas('erro', 3),
          doEstudo: muitas('estudo', 4),
          semente: 4,
        ),
        isEmpty,
        reason: 'sete perguntas não são uma campanha',
      );
      expect(
        escolherPerguntas(
          dosErros: const [],
          doEstudo: muitas('estudo', Campanha.minimo),
          semente: 4,
        ),
        hasLength(Campanha.minimo),
      );
    });

    test('não repete perguntas', () {
      final p = escolherPerguntas(
        dosErros: muitas('mesma', 12),
        doEstudo: muitas('mesma', 12),
        semente: 5,
      );
      expect(p.toSet(), hasLength(p.length));
    });

    test('a mesma semana dá sempre a mesma campanha', () {
      List<String> gerar() => escolherPerguntas(
        dosErros: muitas('erro', 15),
        doEstudo: muitas('estudo', 40),
        semente: sementeDaSemana('2026-08-31'),
      );
      expect(gerar(), gerar());
      // E a semana seguinte dá outra.
      final outra = escolherPerguntas(
        dosErros: muitas('erro', 15),
        doEstudo: muitas('estudo', 40),
        semente: sementeDaSemana('2026-09-07'),
      );
      expect(gerar(), isNot(outra));
    });
  });

  group('o resultado', () {
    Campanha feitaCom(int acertos, int total) => Campanha(
      semana: '2026-08-31',
      enunciados: [for (var i = 0; i < total; i++) 'q$i'],
    ).comResultado(acertos, total);

    test('29% de erro dá sorte, 31% não dá', () {
      // 20 perguntas: 6 erradas são 30% (não chega), 5 são 25% (chega).
      expect(feitaCom(15, 20).sortesGanhas, 1);
      expect(feitaCom(14, 20).sortesGanhas, 0);
    });

    test('quase tudo certo dá duas', () {
      expect(feitaCom(20, 20).sortesGanhas, 2);
      expect(feitaCom(18, 20).sortesGanhas, 2);
      expect(feitaCom(17, 20).sortesGanhas, 1);
    });

    test('por fazer não vale nada', () {
      const c = Campanha(semana: '2026-08-31', enunciados: ['a', 'b']);
      expect(c.feita, isFalse);
      expect(c.sortesGanhas, 0);
      expect(c.erro, 1);
    });

    test('vai e volta pelo JSON', () {
      final c = feitaCom(15, 20);
      final volta = Campanha.deJson(c.paraJson())!;
      expect(volta.semana, c.semana);
      expect(volta.enunciados, c.enunciados);
      expect(volta.feita, isTrue);
      expect(volta.sortesGanhas, 1);
    });

    test('JSON estragado não dá campanha nenhuma', () {
      expect(Campanha.deJson(null), isNull);
      expect(Campanha.deJson({'semana': ''}), isNull);
      expect(Campanha.deJson({'enunciados': []}), isNull);
    });

    group('a fusão com a nuvem', () {
      test('feita noutro telemóvel é feita aqui', () {
        const porFazer = Campanha(semana: '2026-08-31', enunciados: ['a']);
        final la = porFazer.comResultado(18, 20);
        expect(porFazer.fundirCom(la).feita, isTrue);
        expect(porFazer.fundirCom(la).sortesGanhas, 2);
      });

      test('fica o melhor resultado', () {
        const base = Campanha(semana: '2026-08-31', enunciados: ['a']);
        final fraca = base.comResultado(10, 20);
        final boa = base.comResultado(19, 20);
        expect(fraca.fundirCom(boa).acertos, 19);
        expect(boa.fundirCom(fraca).acertos, 19);
      });

      test('a campanha de ontem não substitui a de hoje', () {
        const velha = Campanha(semana: '2026-08-24', enunciados: ['a']);
        const nova = Campanha(semana: '2026-08-31', enunciados: ['b']);
        expect(nova.fundirCom(velha).semana, '2026-08-31');
        expect(velha.fundirCom(nova).semana, '2026-08-31');
      });
    });
  });

  group('no estado', () {
    late Conteudo conteudo;

    setUpAll(() async {
      conteudo = await Conteudo.carregar();
      SharedPreferences.setMockInitialValues({});
    });

    /// Uma segunda-feira, para o relógio falso começar em cima da viragem.
    DateTime segunda(int semanas) =>
        DateTime(2026, 8, 31, 10).add(Duration(days: 7 * semanas));

    (AppState, void Function(Duration)) comRelogio({DateTime? inicio}) {
      var agora = inicio ?? segunda(0);
      final st = AppState()
        ..conteudo = conteudo
        ..pronto = true
        ..classe = '1ª classe'
        ..cursoId = conteudo.cursos.first.id
        ..relogio = () => agora;
      return (st, (Duration d) => agora = agora.add(d));
    }

    test('sem estudo nenhum, não há campanha', () {
      final (st, _) = comRelogio();
      st.verificarCampanha();
      expect(st.campanha, isNull);
      expect(st.temCampanhaPorFazer, isFalse);
    });

    test('a campanha de segunda traz o que se estudou na semana passada', () {
      final (st, passar) = comRelogio();
      // Quatro níveis na primeira semana — cinco perguntas cada.
      for (var i = 0; i < 4; i++) {
        st.concluirNivel(i, 5, 5);
        passar(const Duration(days: 1));
      }

      // Ainda é a mesma semana: nada.
      st.verificarCampanha();
      expect(st.campanha, isNull);

      // Passa à segunda seguinte.
      passar(const Duration(days: 4));
      st.verificarCampanha();

      final c = st.campanha;
      expect(c, isNotNull, reason: 'a semana de estudo não gerou campanha');
      expect(c!.semana, segundaDe(segunda(1)));
      expect(c.quantas, inInclusiveRange(Campanha.minimo, Campanha.maximo));

      // E as perguntas são mesmo as dos níveis que ela fez.
      final feitas = {
        for (var i = 0; i < 4; i++)
          ...st.niveis[i].nivel.questoes.map((q) => q.q),
      };
      expect(c.enunciados.every(feitas.contains), isTrue,
          reason: 'entraram perguntas que ela não estudou');
      expect(st.perguntasDaCampanha, hasLength(c.quantas));
    });

    test('não muda a meio da semana', () {
      // É a única coisa que a define. Uma campanha que se refaz à
      // quarta-feira deixa de ter prazo.
      final (st, passar) = comRelogio();
      for (var i = 0; i < 4; i++) {
        st.concluirNivel(i, 5, 5);
      }
      passar(const Duration(days: 7));
      st.verificarCampanha();
      final antes = [...st.campanha!.enunciados];

      passar(const Duration(days: 2));
      st.concluirNivel(9, 5, 5);
      st.verificarCampanha();
      expect(st.campanha!.enunciados, antes);
    });

    test('à segunda seguinte é outra', () {
      final (st, passar) = comRelogio();
      for (var i = 0; i < 4; i++) {
        st.concluirNivel(i, 5, 5);
      }
      passar(const Duration(days: 7));
      st.verificarCampanha();
      final primeira = st.campanha!;

      // Estuda outros níveis nesta semana e passa à seguinte.
      for (var i = 5; i < 9; i++) {
        st.concluirNivel(i, 5, 5);
      }
      passar(const Duration(days: 7));
      st.verificarCampanha();

      expect(st.campanha!.semana, isNot(primeira.semana));
      expect(st.campanha!.feita, isFalse);
    });

    test('sem estudo na semana passada, puxa da anterior', () {
      final (st, passar) = comRelogio();
      for (var i = 0; i < 4; i++) {
        st.concluirNivel(i, 5, 5);
      }
      // Duas semanas sem estudar: férias, doença, telemóvel emprestado.
      passar(const Duration(days: 14));
      st.verificarCampanha();
      expect(st.campanha, isNotNull,
          reason: 'devia ter recuado mais uma semana');
    });

    test('três semanas depois já não puxa nada', () {
      final (st, passar) = comRelogio();
      for (var i = 0; i < 4; i++) {
        st.concluirNivel(i, 5, 5);
      }
      passar(const Duration(days: 21));
      st.verificarCampanha();
      expect(st.campanha, isNull,
          reason: 'puxar de um mês atrás já não é rever, é começar outra vez');
    });

    test('acabá-la bem paga sortes, uma vez só', () {
      final (st, passar) = comRelogio();
      for (var i = 0; i < 4; i++) {
        st.concluirNivel(i, 4, 5); // com erros: não dá sortes de lição
      }
      expect(st.sortes.quantas, 0);

      passar(const Duration(days: 7));
      st.verificarCampanha();
      final total = st.campanha!.quantas;

      st.concluirCampanha(total, total);
      expect(st.campanha!.feita, isTrue);
      expect(st.sortes.quantas, 2, reason: 'tudo certo devia dar duas');
      expect(st.temCampanhaPorFazer, isFalse);

      // Refazê-la não paga outra vez.
      st.concluirCampanha(total, total);
      expect(st.sortes.quantas, 2);
    });

    test('acabá-la mal não paga nada', () {
      final (st, passar) = comRelogio();
      for (var i = 0; i < 4; i++) {
        st.concluirNivel(i, 4, 5);
      }
      passar(const Duration(days: 7));
      st.verificarCampanha();
      final total = st.campanha!.quantas;

      // Metade errada: bem acima da margem.
      st.concluirCampanha(total ~/ 2, total);
      expect(st.sortes.quantas, 0);
      expect(st.campanha!.feita, isTrue);
    });

    test('vai e volta pela nuvem, e feita não se desfaz', () {
      final (st, passar) = comRelogio();
      for (var i = 0; i < 4; i++) {
        st.concluirNivel(i, 5, 5);
      }
      passar(const Duration(days: 7));
      st.verificarCampanha();
      final total = st.campanha!.quantas;
      st.concluirCampanha(total, total);

      final outro = AppState()
        ..conteudo = conteudo
        ..pronto = true
        ..classe = '1ª classe'
        ..cursoId = conteudo.cursos.first.id
        ..relogio = st.relogio
        ..fundirDaNuvem(st.paraNuvem());

      expect(outro.campanha, isNotNull);
      expect(outro.campanha!.feita, isTrue,
          reason: 'fazê-la noutro telemóvel tem de contar');
      expect(outro.temCampanhaPorFazer, isFalse);
    });

    test('o que se estudou noutro telemóvel entra na campanha', () {
      final (aqui, passarA) = comRelogio();
      final (la, _) = comRelogio();
      for (var i = 0; i < 4; i++) {
        la.concluirNivel(i, 5, 5);
      }

      aqui.fundirDaNuvem(la.paraNuvem());
      passarA(const Duration(days: 7));
      aqui.verificarCampanha();
      expect(aqui.campanha, isNotNull);
    });
  });

  group('o cartão', () {
    late Conteudo conteudo;

    setUpAll(() async {
      conteudo = await Conteudo.carregar();
      SharedPreferences.setMockInitialValues({});
    });

    (AppState, void Function(Duration)) comCampanha() {
      var agora = DateTime(2026, 8, 31, 10);
      final st = AppState()
        ..conteudo = conteudo
        ..pronto = true
        ..nome = 'Ana'
        ..classe = '1ª classe'
        ..cursoId = conteudo.cursos.first.id
        ..relogio = () => agora;
      for (var i = 0; i < 4; i++) {
        st.concluirNivel(i, 5, 5);
      }
      agora = agora.add(const Duration(days: 7));
      st.verificarCampanha();
      return (st, (Duration d) => agora = agora.add(d));
    }

    Future<Object?> montar(WidgetTester tester, AppState st, Size t) async {
      tester.view.physicalSize = t;
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);
      await tester.pumpWidget(
        ChangeNotifierProvider<AppState>.value(
          value: st,
          child: MaterialApp(
            theme: somaraTheme(),
            home: const Scaffold(
              backgroundColor: S.gm950,
              body: PraticarScreen(),
            ),
          ),
        ),
      );
      await tester.pump(const Duration(milliseconds: 400));
      return tester.takeException();
    }

    for (final t in const <String, Size>{
      'telemóvel barato': Size(320, 640),
      'telemóvel comum': Size(411, 914),
      'tablet': Size(600, 1024),
    }.entries) {
      testWidgets('cabe num ${t.key}', (tester) async {
        final (st, _) = comCampanha();
        expect(await montar(tester, st, t.value), isNull);
        expect(find.text('Campanha da semana'), findsOneWidget);
      });
    }

    testWidgets('sem campanha, o cartão não aparece', (tester) async {
      final st = AppState()
        ..conteudo = conteudo
        ..pronto = true
        ..classe = '1ª classe'
        ..cursoId = conteudo.cursos.first.id;
      expect(await montar(tester, st, const Size(411, 914)), isNull);
      expect(find.text('Campanha da semana'), findsNothing);
    });

    testWidgets('feita, o cartão conta como correu', (tester) async {
      final (st, _) = comCampanha();
      final total = st.campanha!.quantas;
      st.concluirCampanha(total, total);

      expect(await montar(tester, st, const Size(411, 914)), isNull);
      expect(find.textContaining('Ganhaste duas sortes'), findsOneWidget);
      expect(st.sortes.quantas, greaterThanOrEqualTo(2));
      expect(st.sortes.quantas, lessThanOrEqualTo(Sortes.tecto));
    });
  });
}
