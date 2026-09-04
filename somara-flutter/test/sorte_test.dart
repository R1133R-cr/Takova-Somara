import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/pomar.dart';
import 'package:somara/models/rastreio.dart';
import 'package:somara/models/sopa.dart';
import 'package:somara/models/sorte.dart';
import 'package:somara/screens/pomar_screen.dart';
import 'package:somara/screens/sopa_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';

/// A Sorte.
///
/// É a única ponte que existe entre estudar e ter ajuda dentro do jogo, e
/// vale por duas coisas que se partem em silêncio: **só se ganha a acertar
/// tudo** — se um nível com erros começar a dar sortes, a ponte deixa de
/// ligar a nada — e **aponta para onde a criança não olhou**. Uma ajuda que
/// mostra o sítio onde ela já estava a trabalhar diz-lhe o que ela já sabia.
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

  group('o saldo', () {
    test('começa a zero e uma lição perfeita dá exactamente uma', () {
      const s = Sortes();
      expect(s.quantas, 0);
      expect(s.temAlguma, isFalse);
      expect(s.comGanho().quantas, 1);
    });

    test('o tecto trava às cinco', () {
      var s = const Sortes();
      for (var i = 0; i < 20; i++) {
        s = s.comGanho();
      }
      expect(s.quantas, Sortes.tecto);
      expect(s.cheio, isTrue);
    });

    test('gastar no tecto não faz reaparecer as que se perderam', () {
      // O tecto morde na hora de ganhar. Se mordesse só na de mostrar,
      // vinte lições perfeitas davam cinco sortes agora e quinze mais tarde.
      var s = const Sortes();
      for (var i = 0; i < 20; i++) {
        s = s.comGanho();
      }
      for (var i = 0; i < 5; i++) {
        s = s.aGastar()!;
      }
      expect(s.quantas, 0);
      expect(s.aGastar(), isNull);
    });

    test('não se gasta o que não se tem', () {
      expect(const Sortes().aGastar(), isNull);
      expect(const Sortes().comGanho().aGastar()!.quantas, 0);
    });

    test('vai e volta pelo JSON', () {
      final s = const Sortes().comGanho().comGanho().aGastar()!;
      final volta = Sortes.deJson(s.paraJson());
      expect(volta.quantas, 1);
      expect(volta.gastas, 1);
    });

    test('JSON estragado não dá sortes do ar', () {
      // Um ficheiro adulterado a dizer "tenho mil" fica pelo tecto.
      final v = Sortes.deJson({'ganhas': 1000, 'gastas': 0});
      expect(v.quantas, Sortes.tecto);
    });

    test('a nuvem não fabrica nem apaga sortes', () {
      final aqui = const Sortes().comGanho().comGanho().aGastar()!;
      final naNuvem = const Sortes().comGanho().comGanho();
      // Lá gastou-se menos, mas o gasto de cá conta.
      expect(aqui.fundirCom(naNuvem).quantas, 1);

      // E o que se ganhou lá conta cá.
      final estudouLa = const Sortes().comGanho().comGanho().comGanho();
      expect(aqui.fundirCom(estudouLa).quantas, 2);
    });

    test('o plural também muda', () {
      expect(sortesEmPalavras(1), '1 sorte');
      expect(sortesEmPalavras(3), '3 sortes');
      expect(sortesEmPalavras(0), '0 sortes');
    });
  });

  group('o rastreio', () {
    test('conta os toques por casa', () {
      final r = Rastreio();
      expect(r.vazio, isTrue);
      r.tocar([1, 2, 3]);
      r.tocar([2]);
      expect(r.quantoEm(2), 2);
      expect(r.quantoEm(1), 1);
      expect(r.quantoEm(9), 0);
      expect(r.intocado([8, 9]), isTrue);
      expect(r.intocado([1, 9]), isFalse);
    });

    test('escolhe o menos tocado', () {
      final r = Rastreio()..tocar([1, 2]);
      final escolhido = r.menosTocado<List<int>>(
        [
          [1, 2],
          [5, 6],
        ],
        (c) => c,
      );
      expect(escolhido, [5, 6]);
    });

    test('em empate, o desempate manda — e é sempre o mesmo', () {
      // Sem um desempate fixo, dois telemóveis com o mesmo tabuleiro davam
      // ajudas diferentes, e uma ajuda arbitrária não se percebe.
      final r = Rastreio();
      List<int>? escolher() => r.menosTocado<List<int>>(
        [
          [1, 2],
          [5, 6, 7],
        ],
        (c) => c,
        desempate: (c) => c.length,
      );
      expect(escolher(), [5, 6, 7]);
      expect(escolher(), [5, 6, 7]);
    });

    test('limpar esquece tudo', () {
      final r = Rastreio()..tocar([1]);
      r.limpar();
      expect(r.vazio, isTrue);
    });
  });

  group('a Sorte na Sopa', () {
    test('revela a palavra em que o dedo não passou', () {
      final s = Sopa.doNivel(1, rnd: Random(3));
      final r = Rastreio();

      // A criança andou em cima da primeira palavra e não achou nada.
      final procurada = s.escondidas.first;
      r.tocar(procurada.casas);
      r.tocar(procurada.casas);

      final alvo = s.menosTocada(r, {});
      expect(alvo, isNotNull);
      expect(alvo!.palavra, isNot(procurada.palavra),
          reason: 'apontou para onde ela já tinha procurado');
    });

    test('nunca revela uma que já foi encontrada', () {
      final s = Sopa.doNivel(1, rnd: Random(5));
      final achadas = s.escondidas.map((p) => p.palavra).toSet();
      expect(s.menosTocada(Rastreio(), achadas), isNull);

      final menosUma = {...achadas}..remove(s.escondidas.last.palavra);
      expect(s.menosTocada(Rastreio(), menosUma)!.palavra,
          s.escondidas.last.palavra);
    });

    test('num tabuleiro por tocar, escolhe a mais comprida', () {
      // Se ela não olhou para nenhuma, a comprida é a que lhe custa mais.
      final s = Sopa.doNivel(300, rnd: Random(9));
      final alvo = s.menosTocada(Rastreio(), {})!;
      final maior = s.escondidas
          .map((p) => p.palavra.length)
          .reduce((a, b) => a > b ? a : b);
      expect(alvo.palavra.length, maior);
    });
  });

  group('a Sorte no Pomar', () {
    test('as jogadas possíveis existem mesmo no tabuleiro', () {
      for (var semente = 0; semente < 8; semente++) {
        final p = Pomar.novo(rnd: Random(semente));
        final jogadas = p.jogadasPossiveis();
        expect(jogadas, isNotEmpty, reason: 'semente $semente');
        for (final j in jogadas) {
          expect(p.podeTrocar(j.de, j.para), isTrue,
              reason: 'a Sorte ia apontar uma jogada que não vale');
          expect(j.composicao, isNotEmpty);
        }
      }
    });

    test('e não sobra nenhuma por listar', () {
      // O `haJogada` diz SE há; o `jogadasPossiveis` diz QUAIS. Se os dois
      // discordassem, a Sorte diria "não há nada" num tabuleiro jogável.
      for (var semente = 0; semente < 8; semente++) {
        final p = Pomar.novo(rnd: Random(semente));
        expect(p.jogadasPossiveis().isNotEmpty, p.haJogada(),
            reason: 'semente $semente');
      }
    });

    test('escolhe a composição em que ela não mexeu', () {
      final p = Pomar.novo(rnd: Random(11));
      final todas = p.jogadasPossiveis();
      expect(todas.length, greaterThan(1),
          reason: 'preciso de duas para haver escolha');

      // Ela mexeu em cima da primeira, sem lá chegar.
      final mexida = todas.first;
      final r = Rastreio()..tocar(mexida.envolvidas);

      final escolhida = p.jogadaPorTocar(r)!;
      expect(escolhida.envolvidas.intersection(mexida.envolvidas), isEmpty,
          reason: 'apontou para onde ela já tinha mexido');
    });

    test('a mesma escolha, sempre', () {
      // Duas sortes seguidas no mesmo tabuleiro têm de apontar o mesmo sítio.
      final p = Pomar.novo(rnd: Random(4));
      final r = Rastreio();
      final a = p.jogadaPorTocar(r)!;
      final b = p.jogadaPorTocar(r)!;
      expect(a.de, b.de);
      expect(a.para, b.para);
    });

    test('a peça especial nasce onde a Sorte apontou', () {
      final p = Pomar.novo(rnd: Random(7));
      final j = p.jogadaPorTocar(Rastreio())!;
      final com = p.comEspecialEm(j.de, Especial.embrulho);

      expect(com.casas[j.de]!.especial, Especial.embrulho);
      expect(com.casas[j.de]!.produto, p.casas[j.de]!.produto,
          reason: 'trocou-lhe a fruta debaixo do dedo');
      // E a jogada continua a valer: uma peça especial que estragasse a
      // jogada que ela ia fazer era pior do que não dar ajuda nenhuma.
      expect(com.podeTrocar(j.de, j.para), isTrue);
    });

    test('numa casa vazia não nasce nada', () {
      final p = Pomar.novo(rnd: Random(2));
      final comBuraco = p.comCasas([...p.casas]..[0] = null);
      expect(comBuraco.comEspecialEm(0, Especial.sol).casas[0], isNull);
    });
  });

  group('ganhar sortes, no estado', () {
    late Conteudo conteudo;

    setUpAll(() async {
      conteudo = await Conteudo.carregar();
      SharedPreferences.setMockInitialValues({});
    });

    AppState estado() => AppState()
      ..conteudo = conteudo
      ..pronto = true
      ..classe = '1ª classe'
      ..cursoId = conteudo.cursos.first.id;

    test('uma lição sem erros dá exactamente uma', () {
      final st = estado();
      st.concluirNivel(0, 5, 5);
      expect(st.sortes.quantas, 1);
    });

    test('uma lição com um erro não dá nenhuma', () {
      // A regra que faz a ponte existir. Se um nível com erros começasse a
      // dar sortes, "acertar tudo" deixava de querer dizer alguma coisa.
      final st = estado();
      st.concluirNivel(0, 4, 5);
      expect(st.sortes.quantas, 0);
    });

    test('praticar não dá sortes', () {
      final st = estado();
      st.concluirTreino(20);
      expect(st.sortes.quantas, 0);
    });

    test('o tecto trava às cinco, por muito que se estude', () {
      final st = estado();
      for (var i = 0; i < 12; i++) {
        st.concluirNivel(i, 5, 5);
      }
      expect(st.sortes.quantas, Sortes.tecto);
    });

    test('gastar tira uma, e no zero recusa', () {
      final st = estado();
      st.concluirNivel(0, 5, 5);
      expect(st.gastarSorte(), isTrue);
      expect(st.sortes.quantas, 0);
      expect(st.gastarSorte(), isFalse);
    });

    test('vai e volta pela nuvem sem se perder nem duplicar', () {
      final st = estado();
      st.concluirNivel(0, 5, 5);
      st.concluirNivel(1, 5, 5);
      st.gastarSorte();

      final outro = estado()..fundirDaNuvem(st.paraNuvem());
      expect(outro.sortes.quantas, 1);
      expect(outro.sortes.gastas, 1);
    });
  });

  group('o botão, nos dois jogos', () {
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

    Future<Object?> montar(WidgetTester tester, Widget ecra, AppState st,
        Size tamanho) async {
      tester.view.physicalSize = tamanho;
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);
      await tester.pumpWidget(
        ChangeNotifierProvider<AppState>.value(
          value: st,
          child: MaterialApp(theme: somaraTheme(), home: ecra),
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

    for (final t in tamanhos.entries) {
      testWidgets('a Sopa com o botão cabe num ${t.key}', (tester) async {
        final st = estado();
        st.concluirNivel(0, 5, 5);
        final erro =
            await montar(tester, const SopaScreen(nivel: 1), st, t.value);
        expect(erro, isNull, reason: 'sopa em ${t.value}');
        expect(find.text('Sorte 1'), findsOneWidget);
      });

      testWidgets('o Pomar com o botão cabe num ${t.key}', (tester) async {
        final erro =
            await montar(tester, const PomarScreen(), estado(), t.value);
        expect(erro, isNull, reason: 'pomar em ${t.value}');
        // Sem sortes o botão fica na mesma, a dizer zero: escondê-lo tirava
        // a quem nunca teve nenhuma a hipótese de saber que existem.
        expect(find.text('Sorte 0'), findsOneWidget);
      });
    }

    testWidgets('o contador desce quando se gasta uma', (tester) async {
      final st = estado();
      st.concluirNivel(0, 5, 5);
      st.concluirNivel(1, 5, 5);
      await montar(tester, const PomarScreen(), st, const Size(411, 914));
      expect(find.text('Sorte 2'), findsOneWidget);

      await tester.tap(find.text('Sorte 2'));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 300));

      expect(st.sortes.quantas, 1, reason: 'a sorte não foi cobrada');
      expect(find.text('Sorte 1'), findsOneWidget);

      await tester.pump(const Duration(seconds: 3));
    });

    testWidgets('sem sortes, tocar não cobra nada e explica como se ganham',
        (tester) async {
      final st = estado();
      await montar(tester, const PomarScreen(), st, const Size(411, 914));

      await tester.tap(find.text('Sorte 0'));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 300));

      expect(st.sortes.quantas, 0);
      expect(
        find.textContaining('lição que acertares toda'),
        findsOneWidget,
        reason: 'quem nunca teve uma sorte tem de saber como se ganha',
      );
      await tester.pump(const Duration(seconds: 3));
    });
  });
}
