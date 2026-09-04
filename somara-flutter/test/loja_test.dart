import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/carteira.dart';
import 'package:somara/models/coleccao.dart';
import 'package:somara/models/content.dart';
import 'package:somara/screens/loja_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';
import 'package:somara/widgets/roby.dart';

/// As moedas e a loja do Roby.
///
/// O que aqui se vende não ensina nada a ninguém — vale por ter custado. É
/// isso que estes testes protegem: que o preço seja verdade, que o que se
/// comprou não desapareça, e que não haja maneira de fabricar cristais sem
/// os ter ganho. Uma criança que junta cristais duas semanas e os vê sumir
/// numa sincronização não volta a juntar.
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
    test('cada pose à venda tem mesmo um ficheiro no disco', () {
      // O teste que impede o pior defeito possível desta loja: vender à
      // criança uma cara que não existe. Ela paga os cristais que juntou
      // durante duas semanas e recebe um quadrado cinzento.
      for (final i in catalogo) {
        final p = i.pose;
        if (p == null) continue;
        expect(File(p.path).existsSync(), isTrue,
            reason: '${i.nome}: falta ${p.path}');
      }
    });

    test('todas as poses do enum têm ficheiro, à venda ou não', () {
      for (final p in RobyPose.values) {
        expect(File(p.path).existsSync(), isTrue, reason: 'falta ${p.path}');
      }
    });

    test('os identificadores não se repetem', () {
      // Dois itens com o mesmo `id` davam uma compra que desbloqueava o
      // outro — e não há maneira de a criança perceber o que aconteceu.
      final ids = catalogo.map((i) => i.id).toList();
      expect(ids.toSet(), hasLength(ids.length));
    });

    test('não se vende o que já é da criança', () {
      for (final i in catalogo) {
        final p = i.pose;
        if (p == null) continue;
        expect(posesDeFabrica.contains(p), isFalse,
            reason: '${i.nome} já vem com a app');
      }
    });

    test('todo o preço é positivo e tem moeda', () {
      for (final i in catalogo) {
        expect(i.preco, greaterThan(0), reason: i.id);
      }
      // Os minutos baratos pagam-se em ouro; o que se guarda, em cristal.
      // Sem isto o ouro não teria onde ser gasto.
      expect(catalogo.where((i) => i.moeda == Moeda.gc), isNotEmpty);
      expect(catalogo.where((i) => i.moeda == Moeda.cc), isNotEmpty);
    });

    test('há caras e poses que cheguem para valer a pena', () {
      final caras = catalogo.where((i) => i.familia == Familia.cara);
      final poses = catalogo.where((i) => i.familia == Familia.pose);
      expect(caras.length, greaterThanOrEqualTo(10));
      expect(poses.length, greaterThanOrEqualTo(5));
    });

    test('as poses de corpo inteiro estão marcadas como tal', () {
      // Uma pose vertical metida num recorte redondo dá uma cabeça minúscula
      // no meio de um círculo vazio. A marca é o que permite ao ecrã evitá-lo.
      for (final i in catalogo.where((i) => i.familia == Familia.pose)) {
        expect(i.pose!.retrato, isTrue, reason: i.id);
      }
      for (final i in catalogo.where((i) => i.familia == Familia.cara)) {
        expect(i.pose!.retrato, isFalse, reason: i.id);
      }
    });
  });

  group('a carteira', () {
    test('um nível a 100% dá o máximo de ouro, e nunca se sai sem nada', () {
      expect(Carteira.ouroPorNivel(100), 15);
      expect(Carteira.ouroPorNivel(50), 10);
      // Quem tropeçou num nível difícil já teve o castigo de o ter
      // tropeçado; sair de lá sem nada era dizer-lhe que não valeu de nada.
      expect(Carteira.ouroPorNivel(0), 5);
      expect(Carteira.ouroPorNivel(-30), 5);
      expect(Carteira.ouroPorNivel(500), 15);
    });

    test('gasta o que tem e recusa o que não tem', () {
      final c = const Carteira().comGanho(Moeda.gc, 25);
      expect(c.gc, 25);
      expect(c.comGasto(Moeda.gc, 20)!.gc, 5);
      expect(c.comGasto(Moeda.gc, 26), isNull);
      expect(c.comGasto(Moeda.cc, 1), isNull, reason: 'não tem cristais');
    });

    test('as duas moedas não se misturam', () {
      final c = const Carteira().comGanho(Moeda.gc, 40).comGanho(Moeda.cc, 2);
      final paga = c.comGasto(Moeda.cc, 2)!;
      expect(paga.cc, 0);
      expect(paga.gc, 40);
    });

    test('vai e volta pelo JSON', () {
      final c = const Carteira()
          .comGanho(Moeda.gc, 30)
          .comGanho(Moeda.cc, 4)
          .comGasto(Moeda.gc, 20)!;
      final volta = Carteira.deJson(c.paraJson());
      expect(volta.gc, c.gc);
      expect(volta.cc, c.cc);
      expect(volta.gastoGc, 20);
    });

    test('a nuvem não fabrica nem apaga dinheiro', () {
      // Ficar pelo maior SALDO dava a quem tivesse dois telemóveis uma
      // máquina de cristais: gastava-os num, entrava na conta no outro, e
      // voltavam. Fica pelo maior de cada total.
      final aqui = const Carteira().comGanho(Moeda.cc, 4).comGasto(Moeda.cc, 4)!;
      final naNuvem = const Carteira().comGanho(Moeda.cc, 4);
      expect(aqui.cc, 0);
      expect(aqui.fundirCom(naNuvem).cc, 0, reason: 'os gastos voltaram');

      // Mas o que se ganhou noutro telemóvel conta.
      final estudouLa = const Carteira().comGanho(Moeda.cc, 7);
      expect(aqui.fundirCom(estudouLa).cc, 3);
    });
  });

  group('a colecção', () {
    test('as de fábrica são dela desde o primeiro dia', () {
      const c = Coleccao();
      expect(c.tem(RobyPose.feliz), isTrue);
      expect(c.tem(RobyPose.pensativo), isFalse);
      expect(c.roby, RobyPose.token);
    });

    test('não se veste o que não é dela', () {
      const c = Coleccao();
      expect(c.aUsar(RobyPose.sereno).escolhida, isNull,
          reason: 'vestiu uma pose por pagar');
      expect(c.com('sereno').aUsar(RobyPose.sereno).roby, RobyPose.sereno);
    });

    test('a fusão junta as duas, sem perder nenhuma', () {
      final aqui = const Coleccao().com('sereno');
      final la = const Coleccao().com('aCorrer');
      final junta = aqui.fundirCom(la);
      expect(junta.tem(RobyPose.sereno), isTrue);
      expect(junta.tem(RobyPose.aCorrer), isTrue);
    });

    test('a cara que se está a ver não muda com uma sincronização', () {
      final aqui = const Coleccao().com('sereno').aUsar(RobyPose.sereno);
      final la = const Coleccao().com('aCorrer').aUsar(RobyPose.aCorrer);
      expect(aqui.fundirCom(la).roby, RobyPose.sereno);
    });

    test('um item que desapareça do catálogo não deixa o Roby sem ficheiro', () {
      final c = Coleccao.deJson({
        'compradas': ['pose-que-ja-nao-existe', 'sereno'],
        'escolhida': 'pose-que-ja-nao-existe',
      });
      expect(c.compradas, {'sereno'});
      expect(c.roby, RobyPose.token, reason: 'devia ter voltado à de fábrica');
    });
  });

  group('ganhar e gastar, no estado', () {
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

    /// Os índices dos níveis de uma unidade, na ordem do mapa.
    List<int> daUnidade(AppState st, int qual) {
      final u = st.curso.units[qual];
      return [
        for (var i = 0; i < st.niveis.length; i++)
          if (st.niveis[i].unit.id == u.id) i,
      ];
    }

    test('cada nível concluído rende ouro', () {
      final (st, _) = comRelogio();
      expect(st.carteira.gc, 0);
      st.concluirNivel(0, 5, 5);
      expect(st.carteira.gc, 15);
      st.concluirNivel(1, 3, 5);
      expect(st.carteira.gc, 15 + 11);
    });

    test('uma unidade inteira sem erros vale um cristal', () {
      final (st, _) = comRelogio();
      final indices = daUnidade(st, 0);
      expect(indices, isNotEmpty);
      for (final i in indices) {
        st.concluirNivel(i, 5, 5);
      }
      expect(st.carteira.cc, Carteira.cristalPorUnidadePerfeita);
    });

    test('a mesma unidade não paga duas vezes', () {
      // Sem isto, refazer a última lição de uma unidade era uma máquina de
      // cristais — e a criança que descobrisse isso nunca mais estudava.
      final (st, _) = comRelogio();
      final indices = daUnidade(st, 0);
      for (final i in indices) {
        st.concluirNivel(i, 5, 5);
      }
      final antes = st.carteira.cc;
      for (var v = 0; v < 5; v++) {
        st.concluirNivel(indices.last, 5, 5);
      }
      expect(st.carteira.cc, antes);
    });

    test('uma unidade com um erro não paga cristal', () {
      final (st, _) = comRelogio();
      final indices = daUnidade(st, 0);
      for (final i in indices) {
        st.concluirNivel(i, i == indices.first ? 4 : 5, 5);
      }
      expect(st.carteira.cc, 0);
      expect(st.carteira.gc, greaterThan(0), reason: 'o ouro entra na mesma');
    });

    test('sete dias seguidos de estudo valem um cristal', () {
      final (st, passar) = comRelogio();
      for (var dia = 0; dia < 7; dia++) {
        st.concluirNivel(0, 3, 5);
        passar(const Duration(days: 1));
      }
      expect(st.streak, greaterThanOrEqualTo(7));
      expect(st.carteira.cc, greaterThanOrEqualTo(1));

      // E a segunda semana vale outro, mas a primeira não volta a pagar.
      final aoFimDaPrimeira = st.carteira.cc;
      for (var dia = 0; dia < 7; dia++) {
        st.concluirNivel(0, 3, 5);
        passar(const Duration(days: 1));
      }
      expect(st.carteira.cc, aoFimDaPrimeira + 1);
    });

    test('comprar minutos tira ouro e acrescenta tempo', () {
      final (st, passar) = comRelogio();
      final item = itemPorId('tempo-5')!;

      // Sem ouro, não há compra.
      expect(st.comprar(item), ResultadoDaCompra.semSaldo);

      for (var v = 0; v < 2; v++) {
        st.concluirNivel(v, 5, 5);
      }
      expect(st.carteira.gc, 30);

      // Gasta a bolsa primeiro, senão a compra bate no tecto do dia.
      st.entrarNoJogo();
      passar(const Duration(minutes: 9));
      st.sairDoJogo();
      final antes = st.tempoDeJogo;

      expect(st.comprar(item), ResultadoDaCompra.feito);
      expect(st.carteira.gc, 10);
      expect(st.tempoDeJogo, antes + const Duration(minutes: 5));
    });

    test('não se vendem minutos que o tecto do dia ia deitar fora', () {
      final (st, _) = comRelogio();
      // Estudar muito enche a bolsa até ao tecto.
      for (var v = 0; v < 12; v++) {
        st.concluirNivel(v, 5, 5);
      }
      expect(st.bolsa.noTecto, isTrue);
      final ouro = st.carteira.gc;

      expect(st.comprar(itemPorId('tempo-5')!), ResultadoDaCompra.noTecto);
      expect(st.carteira.gc, ouro, reason: 'cobrou por nada');
    });

    test('comprar uma cara veste-a logo', () {
      final (st, _) = comRelogio();
      final item = catalogo.firstWhere((i) => i.familia == Familia.cara);

      expect(st.comprar(item), ResultadoDaCompra.semSaldo);

      // Uma unidade perfeita por cada cristal de que precisa.
      for (var u = 0; u < item.preco; u++) {
        for (final i in daUnidade(st, u)) {
          st.concluirNivel(i, 5, 5);
        }
      }
      expect(st.carteira.cc, greaterThanOrEqualTo(item.preco));

      expect(st.comprar(item), ResultadoDaCompra.feito);
      expect(st.robyEscolhido, item.pose,
          reason: 'comprar e não ver era o pior momento para pedir outro toque');
      expect(st.comprar(item), ResultadoDaCompra.jaTem);
    });

    test('despir volta à cara de fábrica, sem perder a comprada', () {
      final (st, _) = comRelogio();
      final item = catalogo.firstWhere((i) => i.familia == Familia.cara);
      for (var u = 0; u < item.preco; u++) {
        for (final i in daUnidade(st, u)) {
          st.concluirNivel(i, 5, 5);
        }
      }
      st.comprar(item);

      st.escolherRoby(null);
      expect(st.robyEscolhido, RobyPose.token);
      expect(st.coleccao.tem(item.pose!), isTrue);

      st.escolherRoby(item.pose);
      expect(st.robyEscolhido, item.pose);
    });

    test('tudo isto vai e volta pela nuvem', () {
      final (st, _) = comRelogio();
      for (final i in daUnidade(st, 0)) {
        st.concluirNivel(i, 5, 5);
      }
      final outro = AppState()
        ..conteudo = conteudo
        ..classe = '1ª classe'
        ..cursoId = conteudo.cursos.first.id
        ..fundirDaNuvem(st.paraNuvem());

      expect(outro.carteira.gc, st.carteira.gc);
      expect(outro.carteira.cc, st.carteira.cc);

      // E o marco já pago não volta a pagar no telemóvel novo.
      for (final i in daUnidade(outro, 0)) {
        outro.concluirNivel(i, 5, 5);
      }
      expect(outro.carteira.cc, st.carteira.cc);
    });
  });

  group('o ecrã da loja', () {
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

    const tamanhos = <String, Size>{
      'telemóvel barato': Size(320, 640),
      'telemóvel comum': Size(411, 914),
      'tablet': Size(600, 1024),
    };

    Future<Object?> montar(WidgetTester tester, AppState st, Size tamanho) async {
      tester.view.physicalSize = tamanho;
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);
      await tester.pumpWidget(
        ChangeNotifierProvider<AppState>.value(
          value: st,
          child: MaterialApp(theme: somaraTheme(), home: const LojaScreen()),
        ),
      );
      await tester.pump(const Duration(milliseconds: 400));
      return tester.takeException();
    }

    for (final t in tamanhos.entries) {
      testWidgets('cabe num ${t.key}', (tester) async {
        final erro = await montar(tester, estado(), t.value);
        expect(erro, isNull, reason: 'loja em ${t.value}');
      });
    }

    testWidgets('mostra as duas moedas e o preço', (tester) async {
      final st = estado();
      st.concluirNivel(0, 5, 5);
      await montar(tester, st, const Size(411, 914));

      expect(find.text('15'), findsWidgets, reason: 'o ouro do nível');
      expect(find.text('GC'), findsOneWidget);
      expect(find.text('CC'), findsOneWidget);
      expect(find.text('+5 minutos'), findsOneWidget);
      expect(find.text('+30 minutos'), findsOneWidget);
    });

    testWidgets('comprar sem saldo diz porquê e não tira nada',
        (tester) async {
      final st = estado();
      await montar(tester, st, const Size(411, 914));

      await tester.tap(find.text('+5 minutos'));
      await tester.pump();
      await tester.pump(const Duration(milliseconds: 300));

      expect(find.text(ResultadoDaCompra.semSaldo.explicacao), findsOneWidget);
      expect(st.carteira.gc, 0);
    });
  });
}
