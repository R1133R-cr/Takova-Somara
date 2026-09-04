import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/escadaria.dart';
import 'package:somara/models/sopa.dart';
import 'package:somara/screens/praticar_screen.dart';
import 'package:somara/screens/sopa_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';

/// A sopa de letras feita com o vocabulário da matéria.
///
/// O jogo é o mesmo; o que muda é de onde vêm as palavras. E é essa a razão
/// de isto ter custado pouco: a sopa não sabe a diferença entre "as coisas
/// da cozinha" e "os rios de Moçambique".
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

  group('a palavra bem escrita e a grelha simples', () {
    test('o acento sai para a grelha e fica na lista', () {
      const banco = Banco('Prova', [
        'LÂMPADA',
        'CORAÇÃO',
        'ÁRVORE',
        'PILHA',
        'FIO',
        'SOL',
      ]);
      final s = Sopa.daMateria(banco, rnd: Random(3));

      final acentos = RegExp('[ÁÀÂÃÉÊÍÓÔÕÚÇ]');
      for (final letra in s.letras) {
        expect(acentos.hasMatch(letra), isFalse,
            reason: 'a grelha levou "$letra"');
      }
      for (final p in s.escondidas) {
        // A lista mostra a palavra como se escreve...
        expect(banco.palavras, contains(p.palavra));
        // ...e as letras onde ela está são a forma simples.
        expect(p.casas.map((i) => s.letras[i]).join(), semAcento(p.palavra));
      }
    });

    test('semAcento não estraga o que não tem acento', () {
      expect(semAcento('PILHA'), 'PILHA');
      expect(semAcento('LÂMPADA'), 'LAMPADA');
      expect(semAcento('CORAÇÃO'), 'CORACAO');
      expect(semAcento('ÍNDICO'), 'INDICO');
    });
  });

  group('a sopa da matéria', () {
    test('a grelha cresce com a palavra mais comprida', () {
      const curto = Banco('Curto', ['SOL', 'LUZ', 'ECO', 'SOM', 'RIO', 'AR']);
      const comprido = Banco('Comprido', [
        'INTERRUPTOR',
        'CIRCUITO',
        'CORRENTE',
        'ISOLANTE',
        'CONDUTOR',
        'TOMADA',
      ]);
      expect(
        Sopa.daMateria(comprido, rnd: Random(1)).lado,
        greaterThan(Sopa.daMateria(curto, rnd: Random(1)).lado),
      );
    });

    test('as palavras estão mesmo lá dentro', () {
      const banco = Banco('Prova', [
        'MACHAMBA',
        'ENXADA',
        'MILHO',
        'MANDIOCA',
        'ARROZ',
        'ADUBO',
        'HORTA',
      ]);
      for (var semente = 0; semente < 8; semente++) {
        final s = Sopa.daMateria(banco, rnd: Random(semente));
        expect(s.escondidas, isNotEmpty);
        for (final p in s.escondidas) {
          expect(p.casas.map((i) => s.letras[i]).join(), semAcento(p.palavra),
              reason: '${p.palavra} não está onde diz estar');
        }
      }
    });

    test('não vai ao contrário', () {
      // Aqui treina-se reconhecer o vocabulário da matéria; procurar ao
      // espelho não treina isso.
      const banco = Banco('Prova', [
        'CHUVA', 'NUVEM', 'VAPOR', 'LAGO', 'SOLO', 'AREIA', 'ARGILA',
      ]);
      final s = Sopa.daMateria(banco, rnd: Random(5));
      for (final p in s.escondidas) {
        if (p.casas.length < 2) continue;
        final d = (
          s.linhaDe(p.casas[1]) - s.linhaDe(p.casas[0]),
          s.colunaDe(p.casas[1]) - s.colunaDe(p.casas[0]),
        );
        expect(d.$1 >= 0 && d.$2 >= 0, isTrue,
            reason: '${p.palavra} vai em $d');
      }
    });

    test('está fora da escadaria', () {
      const banco = Banco('Prova', [
        'PILHA', 'FIO', 'TOMADA', 'CHOQUE', 'ENERGIA', 'CORRENTE',
      ]);
      expect(Sopa.daMateria(banco, rnd: Random(2)).nivel, 0,
          reason: 'saber os rios não é ser melhor a sopas de letras');
    });
  });

  group('o vocabulário no currículo', () {
    late Conteudo conteudo;

    setUpAll(() async {
      conteudo = await Conteudo.carregar();
      SharedPreferences.setMockInitialValues({});
    });

    List<({Curso curso, Unidade unidade})> comPalavras() => [
      for (final c in conteudo.cursos)
        for (final u in c.units)
          if (u.palavras.isNotEmpty) (curso: c, unidade: u),
    ];

    test('há unidades com vocabulário, e só de Ciências', () {
      final unidades = comPalavras();
      expect(unidades.length, greaterThanOrEqualTo(15));
      for (final u in unidades) {
        expect(u.curso.id.startsWith('cn') || u.curso.id.startsWith('cs'),
            isTrue,
            reason: '${u.curso.id} não é de Ciências');
      }
    });

    test('cada banco dá uma sopa que se joga', () {
      for (final u in comPalavras()) {
        final banco = Banco(u.unidade.titulo, u.unidade.palavras);
        expect(banco.serve(), isTrue, reason: u.unidade.titulo);

        final s = Sopa.daMateria(banco, rnd: Random(7));
        expect(s.escondidas.length, greaterThanOrEqualTo(4),
            reason: '${u.unidade.titulo}: sopa curta de mais');
        for (final p in s.escondidas) {
          expect(p.casas.map((i) => s.letras[i]).join(), semAcento(p.palavra),
              reason: '${u.unidade.titulo}: ${p.palavra}');
        }
      }
    });

    test('nenhum banco tem duas palavras iguais na grelha', () {
      // "AVÓ" e "AVO" ficariam a mesma coisa nas letras, e a criança só
      // podia achar uma das duas.
      for (final u in comPalavras()) {
        final simples = u.unidade.palavras.map(semAcento).toList();
        expect(simples.toSet(), hasLength(simples.length),
            reason: u.unidade.titulo);
      }
    });

    test('todas as palavras cabem na maior grelha', () {
      for (final u in comPalavras()) {
        for (final p in u.unidade.palavras) {
          expect(semAcento(p).length, lessThanOrEqualTo(14),
              reason: '${u.unidade.titulo}: $p');
        }
      }
    });
  });

  group('no ecrã', () {
    late Conteudo conteudo;

    setUpAll(() async {
      conteudo = await Conteudo.carregar();
      SharedPreferences.setMockInitialValues({});
    });

    AppState estado() => AppState()
      ..conteudo = conteudo
      ..pronto = true
      ..nome = 'Ana'
      ..classe = '5ª classe'
      ..cursoId = 'cn-5c';

    Future<Object?> montar(WidgetTester tester, Widget ecra, AppState st,
        Size t) async {
      tester.view.physicalSize = t;
      tester.view.devicePixelRatio = 1.0;
      addTearDown(tester.view.reset);
      await tester.pumpWidget(
        ChangeNotifierProvider<AppState>.value(
          value: st,
          child: MaterialApp(
            theme: somaraTheme(),
            home: Scaffold(backgroundColor: S.gm950, body: ecra),
          ),
        ),
      );
      await tester.pump(const Duration(milliseconds: 400));
      return tester.takeException();
    }

    testWidgets('sem matéria estudada, o cartão não aparece', (tester) async {
      // Um cartão que promete vocabulário de unidades que ela não abriu era
      // uma porta para um sítio vazio.
      expect(
        await montar(
          tester,
          const PraticarScreen(),
          estado(),
          const Size(411, 914),
        ),
        isNull,
      );
      expect(find.text('Sopa da matéria'), findsNothing);
    });

    testWidgets('depois de estudar uma unidade de Ciências, aparece',
        (tester) async {
      final st = estado();
      final curso = conteudo.cursos.firstWhere((c) => c.id == 'cn-5c');
      final unidade = curso.units.firstWhere((u) => u.palavras.isNotEmpty);
      st.progresso['${curso.id}:${unidade.id}:${unidade.niveis.first.id}'] = 80;

      expect(
        await montar(
          tester,
          const PraticarScreen(),
          st,
          const Size(411, 914),
        ),
        isNull,
      );
      expect(find.text('Sopa da matéria'), findsOneWidget);
      expect(st.unidadesComPalavras, hasLength(1));
    });

    for (final t in const <String, Size>{
      'telemóvel barato': Size(320, 640),
      'telemóvel comum': Size(411, 914),
      'tablet': Size(600, 1024),
    }.entries) {
      testWidgets('a sopa da matéria cabe num ${t.key}', (tester) async {
        final unidade = conteudo.cursos
            .expand((c) => c.units)
            .firstWhere((u) => u.palavras.length >= 11);
        expect(
          await montar(
            tester,
            SopaScreen(banco: Banco(unidade.titulo, unidade.palavras)),
            estado(),
            t.value,
          ),
          isNull,
          reason: '${unidade.titulo} em ${t.value}',
        );
        expect(find.text('Sopa da matéria'), findsOneWidget);
      });
    }

    testWidgets('a da matéria não mostra degrau nenhum', (tester) async {
      final unidade = conteudo.cursos
          .expand((c) => c.units)
          .firstWhere((u) => u.palavras.isNotEmpty);
      final st = estado();
      await montar(
        tester,
        SopaScreen(banco: Banco(unidade.titulo, unidade.palavras)),
        st,
        const Size(411, 914),
      );
      expect(find.textContaining('Nível'), findsNothing);
      expect(st.nivelDe(Jogo.sopa), 1, reason: 'não pode mexer na escadaria');
    });
  });
}
