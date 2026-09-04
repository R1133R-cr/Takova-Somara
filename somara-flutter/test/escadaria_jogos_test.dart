import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/escadaria.dart';
import 'package:somara/models/memoria.dart';
import 'package:somara/screens/crossmath_screen.dart';
import 'package:somara/screens/joguinhos_screen.dart';
import 'package:somara/screens/memoria_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';

/// O Crossmath e a Memória na escadaria.
///
/// Eram os dois últimos joguinhos que ainda pediam à criança que escolhesse
/// uma dificuldade antes de ver o jogo. Agora continuam de onde ela ficou,
/// como os outros dois — e é isso que estes testes prendem, além do que a
/// mudança podia partir sem dar erro: um baralho que não chega para os pares
/// que a escadaria promete, ou um puzzle que deixa de crescer a meio.
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

  const degraus = [1, 2, 3, 4, 25, 100, 250, 500, 750, nivelMaximo];

  group('a Memória', () {
    test('cada degrau dá os pares que a escadaria promete', () {
      // O baralho de "Contar" ia de 1 a 9 e a escadaria pede doze pares no
      // último degrau: o jogo entregava nove e ninguém dava por isso, porque
      // uma mesa com menos cartas do que devia continua a jogar-se.
      final r = Random(3);
      for (final n in degraus) {
        final j = JogoDaMemoria.doNivel(n, rnd: r);
        expect(j.pares, memoriaNo(n).pares, reason: 'nível $n');
        expect(j.cartas, hasLength(memoriaNo(n).pares * 2), reason: 'nível $n');
      }
    });

    test('e nenhum baralho fica a dever no tecto', () {
      final r = Random(4);
      final pedidos = memoriaNo(nivelMaximo).pares;
      for (final b in Baralho.values) {
        final j = JogoDaMemoria.novo(baralho: b, pares: pedidos, rnd: r);
        expect(j.pares, pedidos, reason: '${b.rotulo} não chega aos $pedidos');
      }
    });

    test('cada carta tem par, e um só', () {
      final r = Random(5);
      for (final n in degraus) {
        final j = JogoDaMemoria.doNivel(n, rnd: r);
        final contagem = <int, int>{};
        for (final c in j.cartas) {
          contagem[c.par] = (contagem[c.par] ?? 0) + 1;
        }
        for (final e in contagem.entries) {
          expect(e.value, 2, reason: 'nível $n: o par ${e.key} tem ${e.value}');
        }
      }
    });

    test('nenhuma face se repete na mesa', () {
      // "3 + 4" e "2 + 5" são contas diferentes que dão dois setes. A criança
      // juntava o "3 + 4" ao sete errado — um par que casa de facto — e o
      // jogo recusava-lhe uma jogada certa.
      final r = Random(6);
      for (final n in degraus) {
        final j = JogoDaMemoria.doNivel(n, rnd: r);
        final faces = j.cartas.map((c) => c.face).toList();
        expect(faces.toSet(), hasLength(faces.length), reason: 'nível $n');
      }
    });

    test('o baralho de um degrau é sempre o mesmo', () {
      for (final n in degraus) {
        expect(
          JogoDaMemoria.doNivel(n, rnd: Random(1)).baralho,
          JogoDaMemoria.doNivel(n, rnd: Random(99)).baralho,
          reason: 'nível $n mudou de baralho',
        );
      }
      // E os quatro primeiros degraus dão os quatro baralhos, para ela os
      // conhecer todos antes de a escadaria começar a apertar.
      expect(
        {for (var n = 1; n <= 4; n++) Baralho.doNivel(n)},
        hasLength(Baralho.values.length),
      );
    });

    test('a espera aperta com o degrau', () {
      // A curva já anda um bocadinho no primeiro degrau — 1197 e não 1200 —
      // e é por isso que estes limites são intervalos e não igualdades.
      expect(memoriaNo(1).espera.inMilliseconds, inInclusiveRange(1150, 1200));
      expect(memoriaNo(nivelMaximo).espera.inMilliseconds, 500);
      var anterior = memoriaNo(1).espera;
      for (final n in degraus) {
        expect(memoriaNo(n).espera, lessThanOrEqualTo(anterior),
            reason: 'nível $n');
        anterior = memoriaNo(n).espera;
      }
    });
  });

  group('o Crossmath', () {
    test('o degrau manda no tecto e nas pistas', () {
      expect(crossmathNo(1).pistas, 6);
      expect(crossmathNo(nivelMaximo).pistas, 4);
      expect(crossmathNo(nivelMaximo).tecto,
          greaterThan(crossmathNo(1).tecto * 10));
    });
  });

  group('os ecrãs', () {
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
        Size t) async {
      tester.view.physicalSize = t;
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

    testWidgets('o Crossmath entra pelo degrau guardado', (tester) async {
      final st = estado();
      for (var i = 0; i < 9; i++) {
        st.subirNivelDe(Jogo.crossmath);
      }
      await montar(tester, const CrossmathScreen(), st, const Size(411, 914));
      expect(find.text('Crossmath · Nível 10'), findsOneWidget);
    });

    testWidgets('a Memória entra pelo degrau guardado', (tester) async {
      final st = estado();
      for (var i = 0; i < 4; i++) {
        st.subirNivelDe(Jogo.memoria);
      }
      await montar(tester, const MemoriaScreen(), st, const Size(411, 914));
      expect(find.text('Memória · Nível 5'), findsOneWidget);
    });

    testWidgets('e nenhum deles mexe na escadaria dos outros',
        (tester) async {
      final st = estado();
      for (var i = 0; i < 4; i++) {
        st.subirNivelDe(Jogo.crossmath);
      }
      expect(st.nivelDe(Jogo.crossmath), 5);
      expect(st.nivelDe(Jogo.memoria), 1);
      expect(st.nivelDe(Jogo.sopa), 1);
      expect(st.nivelDe(Jogo.pomar), 1);
    });

    testWidgets('os quatro joguinhos continuam, nenhum pergunta a dificuldade',
        (tester) async {
      // Era isto que faltava: os quatro cartões diziam coisas diferentes uns
      // dos outros, e dois deles pediam à criança que decidisse quão difícil
      // queria o jogo antes de o ver.
      await montar(
        tester,
        const JoguinhosScreen(),
        estado(),
        const Size(411, 914),
      );
      expect(find.text('Continuar'), findsNWidgets(Jogo.values.length));
      for (final antigo in const [
        'Fácil', 'Médio', 'Difícil', 'Contar', 'Somas',
        'Dobros e metades', 'Palavras',
      ]) {
        expect(find.text(antigo), findsNothing,
            reason: 'sobrou a escolha "$antigo"');
      }
    });

    for (final t in const <String, Size>{
      'telemóvel barato': Size(320, 640),
      'telemóvel comum': Size(411, 914),
      'tablet': Size(600, 1024),
    }.entries) {
      testWidgets('a mesa cheia da Memória cabe num ${t.key}',
          (tester) async {
        // Doze pares são vinte e quatro cartas, e o baralho de "Contar"
        // chega a ter doze desenhos numa carta.
        expect(
          await montar(
            tester,
            const MemoriaScreen(nivel: nivelMaximo),
            estado(),
            t.value,
          ),
          isNull,
        );
      });

      testWidgets('o Crossmath de três algarismos cabe num ${t.key}',
          (tester) async {
        expect(
          await montar(
            tester,
            const CrossmathScreen(nivel: nivelMaximo),
            estado(),
            t.value,
          ),
          isNull,
        );
      });
    }
  });
}
