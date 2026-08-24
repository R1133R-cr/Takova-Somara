import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/crossmath.dart';
import 'package:somara/models/sopa.dart';
import 'package:somara/screens/crossmath_screen.dart';
import 'package:somara/screens/guardados_screen.dart';
import 'package:somara/screens/joguinhos_screen.dart';
import 'package:somara/screens/materia_screen.dart';
import 'package:somara/screens/perfil_screen.dart';
import 'package:somara/screens/pomar_screen.dart';
import 'package:somara/screens/sopa_screen.dart';
import 'package:somara/screens/praticar_screen.dart';
import 'package:somara/screens/ranking_screen.dart';
import 'package:somara/state/app_state.dart';
import 'package:somara/theme.dart';

/// Os ecrãs, em vários tamanhos de telemóvel.
///
/// O que estes testes apanham é a família de defeitos que passou por cima de
/// toda a gente até agora: texto a transbordar da caixa, linhas cortadas,
/// botões fora do ecrã. Nenhum deles dá erro no `flutter analyze` e nenhum
/// aparece nos testes de lógica — só se vêem a olhar, e só no tamanho
/// errado. Três das últimas quatro versões tiveram um destes.
///
/// Os tamanhos não são inventados: 320×640 é o Android barato que ainda se
/// vende em Moçambique, 411×914 é o telemóvel comum, e 600×1024 é um
/// tablet de escola.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

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

  /// Monta um ecrã num tamanho dado e devolve o erro, se houver.
  Future<Object?> montar(
    WidgetTester tester,
    Widget ecra,
    Size tamanho, {
    AppState? st,
  }) async {
    tester.view.physicalSize = tamanho;
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.reset);

    await tester.pumpWidget(
      ChangeNotifierProvider<AppState>.value(
        value: st ?? estado(),
        child: MaterialApp(
          theme: somaraTheme(),
          home: Scaffold(backgroundColor: S.gm950, body: ecra),
        ),
      ),
    );
    await tester.pump(const Duration(milliseconds: 600));
    return tester.takeException();
  }

  /// Cada ecrã, em cada tamanho.
  void verificar(String nome, Widget Function() construir) {
    for (final entrada in tamanhos.entries) {
      testWidgets('$nome cabe num ${entrada.key}', (tester) async {
        final erro = await montar(tester, construir(), entrada.value);
        expect(erro, isNull, reason: '$nome em ${entrada.value}');
      });
    }
  }

  verificar('Joguinhos', () => const JoguinhosScreen());
  verificar('Praticar', () => const PraticarScreen());
  verificar('Ranking', () => const RankingScreen());
  verificar('Guardados', () => const GuardadosScreen());
  verificar('Perfil', () => const PerfilScreen());
  verificar('Pomar', () => const PomarScreen());

  for (final d in Dificuldade.values) {
    verificar('Crossmath ${d.rotulo}', () => CrossmathScreen(dificuldade: d));
  }

  // A sopa é a que mais arrisca transbordar: a grelha do difícil tem doze
  // letras de lado e a lista de palavras é comprida.
  for (final n in NivelSopa.values) {
    verificar('Sopa ${n.rotulo}', () => SopaScreen(nivel: n));
  }

  group('a aula, com a matéria mais comprida que existe', () {
    // Se alguma aula transborda, é a maior — e é essa que interessa testar.
    late String titulo;
    late Materia maior;

    setUpAll(() {
      var recorde = -1;
      for (final c in conteudo.cursos) {
        for (final u in c.units) {
          for (final n in u.niveis) {
            final m = n.materia;
            if (m == null) continue;
            final tamanho =
                m.explica.length + m.exemplo.length + m.lembra.length;
            if (tamanho > recorde) {
              recorde = tamanho;
              maior = m;
              titulo = n.titulo;
            }
          }
        }
      }
      expect(recorde, greaterThan(0), reason: 'nenhuma aula encontrada');
    });

    for (final entrada in tamanhos.entries) {
      testWidgets('cabe num ${entrada.key}', (tester) async {
        final erro = await montar(
          tester,
          MateriaScreen(titulo: titulo, materia: maior),
          entrada.value,
        );
        expect(erro, isNull);
      });
    }
  });

  group('nomes longos não partem a interface', () {
    // O nome é escrito pela criança e ninguém o limita. Um nome comprido
    // já partiu o cabeçalho de outras apps.
    for (final entrada in tamanhos.entries) {
      testWidgets('Perfil com nome longo num ${entrada.key}', (tester) async {
        final st = estado()
          ..nome = 'Maria Fernanda Nhamitambo da Conceição Chissano';
        final erro = await montar(
          tester,
          const PerfilScreen(),
          entrada.value,
          st: st,
        );
        expect(erro, isNull);
      });
    }
  });
}
