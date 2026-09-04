import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/escadaria.dart';
import 'package:somara/state/app_state.dart';

/// A escadaria tem mil degraus e ninguém os vai percorrer a olho.
///
/// Estes testes são o que impede que um deles esteja partido: um parâmetro
/// que desce quando devia subir, uma grelha que não cabe no ecrã, um
/// Crossmath impossível. São mil níveis vezes quatro jogos — só uma máquina
/// os pode conferir todos.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  final todos = List.generate(nivelMaximo, (i) => i + 1);

  group('a curva', () {
    test('vai de perto de zero a exactamente um', () {
      expect(curva(1), lessThan(0.01));
      expect(curva(nivelMaximo), closeTo(1.0, 1e-9));
    });

    test('nunca desce', () {
      var anterior = -1.0;
      for (final n in todos) {
        final c = curva(n);
        expect(c, greaterThanOrEqualTo(anterior), reason: 'nível $n');
        anterior = c;
      }
    });

    test('cresce depressa no início e abranda no fim', () {
      // É esta forma que faz os primeiros níveis parecerem diferentes uns
      // dos outros. Uma recta daria 0,1 aos 100 e a criança não sentia nada.
      expect(curva(100), greaterThan(0.25));
      expect(curva(500), greaterThan(0.80));
      // E a última metade tem de dar pouco, senão sobram degraus vazios.
      expect(curva(1000) - curva(500), lessThan(0.20));
    });

    test('aguenta níveis fora do intervalo sem rebentar', () {
      expect(curva(0), curva(1));
      expect(curva(-5), curva(1));
      expect(curva(99999), curva(nivelMaximo));
    });
  });

  group('os parâmetros nunca andam para trás', () {
    // Um parâmetro que oscila faz o nível 301 mais fácil do que o 300, e a
    // criança sente-o mesmo sem saber explicar.
    void monotono(String nome, int Function(int) ler, {required bool sobe}) {
      test('$nome ${sobe ? "sobe" : "aperta"} sempre', () {
        var anterior = ler(1);
        for (final n in todos) {
          final v = ler(n);
          if (sobe) {
            expect(v, greaterThanOrEqualTo(anterior), reason: 'nível $n');
          } else {
            expect(v, lessThanOrEqualTo(anterior), reason: 'nível $n');
          }
          anterior = v;
        }
      });
    }

    monotono('produtos do Pomar', (n) => pomarNo(n).produtos, sobe: true);
    monotono('jogadas do Pomar', (n) => pomarNo(n).jogadas, sobe: false);
    monotono('objectivo do Pomar', (n) => pomarNo(n).objectivo, sobe: true);
    monotono('lado da Sopa', (n) => sopaNo(n).lado, sobe: true);
    monotono('palavras da Sopa', (n) => sopaNo(n).palavras, sobe: true);
    monotono('tecto do Crossmath', (n) => crossmathNo(n).tecto, sobe: true);
    monotono('pistas do Crossmath', (n) => crossmathNo(n).pistas, sobe: false);
    monotono('pares da Memória', (n) => memoriaNo(n).pares, sobe: true);
    monotono('espera da Memória',
        (n) => memoriaNo(n).espera.inMilliseconds, sobe: false);
  });

  group('os limites de cada jogo', () {
    test('Pomar', () {
      final p1 = pomarNo(1), pM = pomarNo(nivelMaximo);
      expect(p1.produtos, 4);
      expect(pM.produtos, 7);
      expect(p1.jogadas, 25);
      expect(pM.jogadas, 12);
      // O tabuleiro não cresce: num telemóvel de 320 já está no limite.
      for (final n in todos) {
        expect(pomarNo(n).linhas, 8);
        expect(pomarNo(n).colunas, 7);
      }
    });

    test('Sopa: a grelha cabe e as palavras cabem na grelha', () {
      for (final n in todos) {
        final s = sopaNo(n);
        expect(s.lado, inInclusiveRange(7, 14));
        expect(s.palavras, inInclusiveRange(4, 10));
        // Mais palavras do que metade do lado é sopa impossível de encher.
        expect(s.palavras, lessThanOrEqualTo(s.lado));
      }
    });

    test('Crossmath: NUNCA menos de quatro pistas', () {
      // Não é preferência. A grelha tem quatro valores livres e cada casa é
      // uma combinação linear deles: três pistas nunca os fixam, e o puzzle
      // fica com uma família de soluções — impossível, não difícil.
      for (final n in todos) {
        expect(crossmathNo(n).pistas,
            greaterThanOrEqualTo(ParamsCrossmath.minimoDePistas),
            reason: 'nível $n geraria um puzzle sem solução única');
      }
      expect(crossmathNo(1).pistas, 6);
      expect(crossmathNo(nivelMaximo).pistas, 4);
    });

    test('Memória: os pares cabem na grelha de cartas', () {
      for (final n in todos) {
        final m = memoriaNo(n);
        expect(m.pares, inInclusiveRange(4, 12));
        expect(m.espera.inMilliseconds, inInclusiveRange(500, 1200));
      }
    });
  });

  group('as mecânicas', () {
    test('entram no marco e nunca mais saem', () {
      for (final m in Mecanica.values) {
        expect(mecanicasDe(m.jogo, m.desde - 1), isNot(contains(m)));
        expect(mecanicasDe(m.jogo, m.desde), contains(m));
        expect(mecanicasDe(m.jogo, nivelMaximo), contains(m));
      }
    });

    test('cada jogo tem as suas, e não as dos outros', () {
      for (final jogo in Jogo.values) {
        final suas = mecanicasDe(jogo, nivelMaximo);
        expect(suas, isNotEmpty, reason: '${jogo.rotulo} sem mecânicas');
        for (final m in suas) {
          expect(m.jogo, jogo);
        }
      }
    });

    test('o nível 1 não tem mecânica nenhuma', () {
      // A primeira vez que uma criança abre um jogo, o jogo é o jogo. As
      // complicações vêm depois de ela perceber o básico.
      for (final jogo in Jogo.values) {
        expect(mecanicasDe(jogo, 1), isEmpty, reason: jogo.rotulo);
      }
    });

    test('depois do 100 não entram mecânicas novas', () {
      // A partir daí a variedade vem de COMBINAR as que já existem. Uma
      // mecânica nova no nível 400 seria conteúdo que quase ninguém veria.
      for (final m in Mecanica.values) {
        expect(m.desde, lessThanOrEqualTo(100), reason: m.rotulo);
      }
    });
  });

  test('o nível 500 é mesmo diferente do nível 5', () {
    // O teste que resume a razão de tudo isto existir.
    final a = pomarNo(5), b = pomarNo(500);
    expect(b.produtos, greaterThan(a.produtos));
    expect(b.jogadas, lessThan(a.jogadas));
    expect(b.objectivo, greaterThan(a.objectivo));
    expect(mecanicasDe(Jogo.pomar, 500).length,
        greaterThan(mecanicasDe(Jogo.pomar, 5).length));
  });
  group('o degrau guardado no estado', () {
    late Conteudo c;

    setUpAll(() async {
      c = await Conteudo.carregar();
      SharedPreferences.setMockInitialValues({});
    });

    AppState estado() => AppState()
      ..conteudo = c
      ..classe = '1ª classe';

    test('toda a gente começa no degrau 1', () {
      final st = estado();
      for (final jogo in Jogo.values) {
        expect(st.nivelDe(jogo), 1, reason: jogo.rotulo);
      }
    });

    test('subir um jogo não mexe nos outros', () {
      final st = estado();
      st.subirNivelDe(Jogo.pomar);
      st.subirNivelDe(Jogo.pomar);
      expect(st.nivelDe(Jogo.pomar), 3);
      expect(st.nivelDe(Jogo.sopa), 1);
      expect(st.nivelDe(Jogo.crossmath), 1);
    });

    test('não passa do tecto', () {
      final st = estado();
      for (var i = 0; i < nivelMaximo + 50; i++) {
        st.subirNivelDe(Jogo.sopa);
      }
      expect(st.nivelDe(Jogo.sopa), nivelMaximo);
    });

    test('a nuvem nunca faz a escadaria descer', () {
      // A mesma regra do XP e do progresso: fica sempre o melhor dos dois.
      // Jogar a tarde toda sem rede e depois entrar na conta não pode
      // apagar esse trabalho.
      final st = estado();
      for (var i = 0; i < 40; i++) {
        st.subirNivelDe(Jogo.pomar);
      }
      expect(st.nivelDe(Jogo.pomar), 41);

      st.fundirDaNuvem({
        'jogos': {'pomar': 12, 'sopa': 77},
      });
      expect(st.nivelDe(Jogo.pomar), 41, reason: 'a nuvem tinha menos');
      expect(st.nivelDe(Jogo.sopa), 77, reason: 'a nuvem tinha mais');
    });

    test('vai e volta pelo JSON sem se perder', () {
      final st = estado();
      st.subirNivelDe(Jogo.memoria);
      st.subirNivelDe(Jogo.memoria);
      final n = st.paraNuvem();

      final outro = estado()..fundirDaNuvem(n);
      expect(outro.nivelDe(Jogo.memoria), 3);
    });

    test('guarda pelo nome do jogo, não pelo índice', () {
      // Se amanhã entrar um quinto joguinho no meio da lista, ninguém pode
      // acordar com o nível do Pomar no Crossmath.
      final st = estado()..subirNivelDe(Jogo.pomar);
      expect(st.paraNuvem()['jogos'], containsPair('pomar', 2));
    });
  });
}
