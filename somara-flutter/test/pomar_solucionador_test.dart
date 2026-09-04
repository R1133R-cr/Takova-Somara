import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/escadaria.dart';
import 'package:somara/models/pomar.dart';
import 'package:somara/models/pomar_solucionador.dart';
import 'package:somara/screens/pomar_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';

/// O Pomar com solução garantida.
///
/// A promessa é uma frase: **a criança nunca perde por azar, e nunca ganha
/// por pena.** A segunda metade é fácil de cumprir — basta não fazer nada. A
/// primeira precisa deste ficheiro, porque um nível impossível não dá erro
/// nenhum: dá uma criança que perde vezes sem conta sem perceber porquê, e
/// que conclui que o problema é ela.
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

  /// Degraus espalhados por toda a escadaria.
  const degraus = [1, 5, 25, 50, 100, 175, 250, 400, 500, 750, 900, 1000];

  group('a escadaria do Pomar é ganhável', () {
    test('em 240 tabuleiros, o jogador guloso fecha sempre o objectivo', () {
      // Este teste já apanhou o defeito para que existe: o objectivo ia a
      // 140 peças em 12 jogadas, ou seja quase doze peças por jogada. Uma
      // jogada boa apanha cinco a sete. Do nível 250 para cima o Pomar era
      // impossível, e nada na app dava por isso.
      final r = Random(11);
      for (final n in degraus) {
        final p = pomarNo(n);
        for (var i = 0; i < 20; i++) {
          final t = Pomar.novo(
            linhas: p.linhas,
            colunas: p.colunas,
            produtos: p.produtos,
            rnd: r,
          );
          final res = Solucionador.jogar(t, p, rnd: r);
          expect(res.ganhou, isTrue, reason: 'nível $n: $res');
        }
      }
    });

    test('e a maioria dos tabuleiros deixa folga a quem não é máquina', () {
      // O solucionador escolhe sempre a melhor troca visível; uma criança de
      // nove anos não. Um tabuleiro que a máquina fecha à justa é um
      // tabuleiro que ela perde — e é esse que o [pomarDoNivel] deita fora.
      //
      // Aqui não se exige que TODOS deixem folga: exige-se que a maioria
      // deixe, senão as oito tentativas do gerador esgotavam-se e ele
      // acabava a entregar o menos mau.
      final r = Random(12);
      for (final n in degraus) {
        final p = pomarNo(n);
        var comFolga = 0;
        for (var i = 0; i < 10; i++) {
          final t = Pomar.novo(
            linhas: p.linhas,
            colunas: p.colunas,
            produtos: p.produtos,
            rnd: r,
          );
          final res = Solucionador.jogar(t, p, rnd: r);
          if (res.ganhou && res.folga <= folgaMaxima) comFolga++;
        }
        expect(comFolga, greaterThanOrEqualTo(6),
            reason: 'nível $n: só $comFolga em 10 deixaram folga');
      }
    });

    test('o objectivo nunca pede mais do que uma jogada consegue dar', () {
      // A leitura directa do defeito, sem simular nada: quantas peças é que
      // cada jogada teria de colher. Acima de cinco, nem o guloso chega.
      for (var n = 1; n <= nivelMaximo; n++) {
        final p = pomarNo(n);
        expect(p.objectivo / p.jogadas, lessThan(5.0),
            reason: 'nível $n pede ${p.objectivo} peças em ${p.jogadas} jogadas');
      }
    });

    test('os produtos que a escadaria pede existem mesmo', () {
      // Pedia sete e há seis. Nenhum teste dava por isso porque nada lia
      // este número — no dia em que o tabuleiro passasse a lê-lo, ia buscar
      // um produto que não existe.
      for (var n = 1; n <= nivelMaximo; n++) {
        expect(pomarNo(n).produtos,
            inInclusiveRange(3, quantosProdutos),
            reason: 'nível $n');
      }
    });
  });

  group('o tabuleiro que se entrega', () {
    test('tem sempre jogada possível', () {
      final r = Random(13);
      for (final n in degraus) {
        final (tabuleiro: t, prova: _) = pomarDoNivel(n, rnd: r);
        expect(t.haJogada(), isTrue, reason: 'nível $n saiu bloqueado');
        expect(t.linhas, pomarNo(n).linhas);
        expect(t.colunas, pomarNo(n).colunas);
      }
    });

    test('não começa com trios já feitos', () {
      // Um trio feito à entrada dava pontos que a criança não ganhou.
      final r = Random(14);
      for (final n in degraus) {
        final (tabuleiro: t, prova: _) = pomarDoNivel(n, rnd: r);
        expect(t.analisar().vazia, isTrue, reason: 'nível $n');
      }
    });

    test('vem com a prova de que se ganha', () {
      final r = Random(15);
      for (final n in degraus) {
        final (tabuleiro: _, prova: prova) = pomarDoNivel(n, rnd: r);
        expect(prova.ganhou, isTrue, reason: 'nível $n: $prova');
        expect(prova.folga, lessThanOrEqualTo(folgaMaxima), reason: 'nível $n');
      }
    });

    test('só usa os produtos do degrau', () {
      final r = Random(16);
      for (final n in [1, 500, 1000]) {
        final p = pomarNo(n);
        final (tabuleiro: t, prova: _) = pomarDoNivel(n, rnd: r);
        final usados = t.casas.map((c) => c!.produto.index).toSet();
        expect(usados.every((i) => i < p.produtos), isTrue,
            reason: 'nível $n usou um produto a mais');
      }
    });

    test('gerar um tabuleiro é rápido de mais para precisar de isolate', () {
      // O §7 pedia menos de 300 ms no pior nível, num telemóvel barato, e
      // um isolate se não desse. Mede-se: dá muito abaixo, e um isolate
      // custava serializar o tabuleiro nos dois sentidos por uma latência
      // que não existe.
      final r = Random(17);
      final relogio = Stopwatch()..start();
      for (final n in degraus) {
        pomarDoNivel(n, rnd: r);
      }
      relogio.stop();
      final porNivel = relogio.elapsedMilliseconds / degraus.length;
      expect(porNivel, lessThan(300),
          reason: 'gerar um tabuleiro levou ${porNivel}ms');
    });
  });

  group('o solucionador', () {
    test('num tabuleiro sem saída, baralha em vez de desistir', () {
      // É o que a partida a sério faz. Sem isto, o solucionador dizia
      // "impossível" onde a criança teria simplesmente continuado.
      final r = Random(18);
      final p = pomarNo(1);

      // Um tabuleiro em diagonais de três cores: não tem trio nenhum e
      // nenhuma troca faz um. Procura-se entre alguns padrões em vez de se
      // fixar um, para o teste não se partir se as cores mudarem.
      Pomar? preso;
      for (final passo in [1, 2, 3, 4]) {
        final tentativa = Pomar(
          linhas: p.linhas,
          colunas: p.colunas,
          produtos: 3,
          casas: List.generate(
            p.linhas * p.colunas,
            (i) => Peca(
              Produto.values[(i ~/ p.colunas + passo * (i % p.colunas)) % 3],
            ),
          ),
        );
        if (!tentativa.haJogada()) {
          preso = tentativa;
          break;
        }
      }
      expect(preso, isNotNull, reason: 'não achei um tabuleiro sem saída');
      expect(preso!.haJogada(), isFalse);

      final res = Solucionador.jogar(preso, p, rnd: r);
      expect(res.ganhou, isTrue, reason: 'desistiu de um tabuleiro jogável');
    });

    test('um objectivo impossível é reprovado, não perdoado', () {
      // O contraprova do primeiro teste: com um objectivo absurdo, o
      // solucionador tem de dizer que não. Se dissesse sempre que sim, os
      // outros testes não provavam nada.
      final r = Random(19);
      const p = ParamsPomar(
        linhas: 8,
        colunas: 7,
        produtos: 6,
        jogadas: 3,
        objectivo: 500,
        mecanicas: {},
      );
      final t = Pomar.novo(produtos: 6, rnd: r);
      final res = Solucionador.jogar(t, p, rnd: r);
      expect(res.ganhou, isFalse);
      expect(res.jogadasUsadas, 3, reason: 'devia ter gasto as jogadas todas');
    });
  });

  group('o ecrã', () {
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

    for (final t in const <String, Size>{
      'telemóvel barato': Size(320, 640),
      'telemóvel comum': Size(411, 914),
      'tablet': Size(600, 1024),
    }.entries) {
      testWidgets('o Pomar com objectivo cabe num ${t.key}', (tester) async {
        // O placar passou de dois números para três: peças, pontos e
        // jogadas. É a 320 que isso se parte.
        for (final n in [1, 500, 1000]) {
          expect(await montar(tester, PomarScreen(nivel: n), estado(), t.value),
              isNull, reason: 'nível $n em ${t.value}');
        }
      });
    }

    testWidgets('mostra o degrau e o objectivo desse degrau', (tester) async {
      await montar(tester, const PomarScreen(nivel: 300), estado(),
          const Size(411, 914));
      expect(find.text('Pomar · Nível 300'), findsOneWidget);
      expect(find.text('0/${pomarNo(300).objectivo}'), findsOneWidget);
      expect(find.text('${pomarNo(300).jogadas}'), findsOneWidget);
    });

    testWidgets('entra pelo degrau guardado quando não se diz nenhum',
        (tester) async {
      final st = estado();
      for (var i = 0; i < 6; i++) {
        st.subirNivelDe(Jogo.pomar);
      }
      await montar(tester, const PomarScreen(), st, const Size(411, 914));
      expect(find.text('Pomar · Nível 7'), findsOneWidget);
    });
  });
}
