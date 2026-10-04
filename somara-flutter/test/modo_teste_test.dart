import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/modo_teste.dart';
import 'package:somara/models/carteira.dart';
import 'package:somara/models/content.dart';
import 'package:somara/state/app_state.dart';

/// A versão de testes não pode escapar para a app da criança.
///
/// Estes testes correm sempre com `SOMARA_TESTE` *desligado* — é como o
/// `flutter test` compila. Isso é o que os torna úteis: o que eles provam é
/// que, na app normal, nada do modo de testes está ligado. Um `if` que se
/// esqueça de olhar para [ModoTeste.activo] dá aqui erro, e dá-o antes de
/// chegar a um telemóvel.
///
/// A conta dos dias de validade testa-se à parte, com datas passadas de
/// fora: é a única conta desta app que, errada, dá um APK que ninguém
/// consegue abrir.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;

  setUpAll(() async {
    c = await Conteudo.carregar();
    SharedPreferences.setMockInitialValues({});
  });

  AppState estado() => AppState()
    ..conteudo = c
    ..classe = '1ª classe'
    ..cursoId = c.cursos.first.id;

  group('a app normal não tem nada do modo de testes', skip: ModoTeste.activo
      ? 'esta compilação é a de testes'
      : null, () {
    test('o modo de testes está desligado nesta compilação', () {
      expect(ModoTeste.activo, isFalse);
    });

    test('nenhuma das liberdades está ligada', () {
      final st = estado();
      expect(st.modoTeste, isFalse);
      expect(st.saltoLivre, isFalse, reason: 'os níveis têm de abrir por ordem');
      expect(st.jogosLivres, isFalse);
      expect(st.treinoLivre, isFalse);
      expect(st.coracoesInfinitos, isFalse);
      expect(st.nadaCusta, isFalse);
      expect(st.desvioDeDias, 0);
    });

    test('os interruptores não se ligam', () async {
      final st = estado();
      await st.definirInterruptores(
        const InterruptoresDeTeste(coracoesInfinitos: true, desvioDeDias: 9),
      );
      expect(st.coracoesInfinitos, isFalse);
      expect(st.desvioDeDias, 0);
    });

    test('errar continua a custar um coração', () {
      final st = estado();
      final antes = st.lives;
      st.perderVida();
      expect(st.lives, antes - 1);
    });

    test('gastar sem saldo continua a ser recusado', () {
      final st = estado();
      expect(st.carteira.gc, 0);
      expect(st.gastar(Moeda.gc, 50), isFalse);
    });

    test('apagar o progresso não faz nada', () async {
      final st = estado();
      st.progresso['x:y:z'] = 100;
      st.xp = 120;
      await st.apagarProgresso();
      expect(st.progresso.length, 1);
      expect(st.xp, 120);
    });

    test('dar moedas não faz nada', () async {
      final st = estado();
      await st.darMoedas(ouro: 1000);
      expect(st.carteira.gc, 0);
    });

    test('o salto para outra classe não faz nada', () {
      final st = estado();
      final outro = c.cursos.firstWhere((x) => x.classe == '6ª classe');
      final nivel = outro.units.first.niveis.first;
      expect(st.saltarPara(outro, outro.units.first, nivel), -1);
      expect(st.classe, '1ª classe', reason: 'a classe do aluno não se mexe');
    });

    test('a bolsa de tempo mantém o tecto do dia', () {
      final st = estado();
      // Sem estudar nada, o que há é o que se dá de graça — e não o tecto.
      expect(st.tempoDeJogo, lessThan(const Duration(minutes: 60)));
    });

    test('o treino continua fechado sem níveis feitos', () {
      final st = estado();
      expect(st.perguntasDeTreino(), isEmpty);
    });

    test('a app normal nunca caduca', () {
      expect(ModoTeste.caducou(), isFalse);
      expect(
        ModoTeste.caducou(DateTime(2099, 1, 1)),
        isFalse,
        reason: 'uma data no futuro não pode fechar a app da criança',
      );
    });
  });

  // O que se segue só se pode provar com a bandeira ligada, porque ela é
  // uma constante de compilação. Corre-se assim:
  //
  //   flutter test test/modo_teste_test.dart --dart-define=SOMARA_TESTE=true
  //
  // O `compilar.sh` não corre isto — correria a suite com a app noutro modo.
  // É uma verificação de quem mexe no modo de testes, e está aqui para essa
  // pessoa não ter de a inventar.
  group('a versão de testes faz o que promete', skip: ModoTeste.activo
      ? null
      : 'corre com --dart-define=SOMARA_TESTE=true', () {
    test('não há fila: tudo aberto por omissão', () {
      final st = estado();
      expect(st.modoTeste, isTrue);
      expect(st.saltoLivre, isTrue);
      expect(st.jogosLivres, isTrue);
      expect(st.treinoLivre, isTrue);
    });

    test('os corações e o ouro continuam a contar por omissão', () {
      // É a decisão que mais importa aqui: quem anda a testar precisa de
      // ver o que a criança vê, e um coração que nunca desce esconde
      // justamente a parte que mais parte.
      final st = estado();
      expect(st.coracoesInfinitos, isFalse);
      expect(st.nadaCusta, isFalse);
      final antes = st.lives;
      st.perderVida();
      expect(st.lives, antes - 1);
      expect(st.gastar(Moeda.gc, 50), isFalse);
    });

    test('a bolsa de tempo não acaba', () {
      expect(estado().tempoDeJogo, const Duration(minutes: 60));
    });

    test('o treino abre sem níveis feitos', () {
      final st = estado();
      expect(st.niveisConcluidos, 0);
      expect(st.perguntasDeTreino(), isNotEmpty);
    });

    test('os corações infinitos desligam o custo', () async {
      final st = estado();
      await st.definirInterruptores(
        const InterruptoresDeTeste(coracoesInfinitos: true),
      );
      st.perderVida();
      st.perderVida();
      expect(st.lives, AppState.maxLives);
    });

    test('«nada custa» paga com a carteira vazia', () async {
      final st = estado();
      await st.definirInterruptores(const InterruptoresDeTeste(nadaCusta: true));
      expect(st.carteira.gc, 0);
      expect(st.gastar(Moeda.gc, 500), isTrue);
      expect(st.carteira.gc, 0, reason: 'a carteira não mexe');
    });

    test('dar moedas enche a carteira a sério', () async {
      final st = estado();
      await st.darMoedas(ouro: 1000, cristais: 100);
      expect(st.carteira.gc, 1000);
      expect(st.carteira.cc, 100);
    });

    test('saltar leva a classe e a disciplina com ele', () {
      final st = estado();
      final destino = c.cursos.firstWhere((x) => x.classe == '9ª classe');
      final ultimaUnidade = destino.units.last;
      final ultimoNivel = ultimaUnidade.niveis.last;
      final i = st.saltarPara(destino, ultimaUnidade, ultimoNivel);
      expect(i, destino.niveisEmSequencia.length - 1);
      expect(st.classe, '9ª classe');
      expect(st.cursoId, destino.id);
    });

    test('empurrar o dia repõe os corações', () async {
      final st = estado();
      st.perderVida();
      expect(st.lives, lessThan(AppState.maxLives));
      await st.definirInterruptores(
        const InterruptoresDeTeste(desvioDeDias: 1),
      );
      expect(st.lives, AppState.maxLives);
      expect(st.desvioDeDias, 1);
    });

    test('apagar o progresso limpa tudo menos o nome e a classe', () async {
      final st = estado()..nome = 'Ana';
      st.progresso['x:y:z'] = 100;
      st.xp = 250;
      await st.darMoedas(ouro: 400);
      await st.apagarProgresso();
      expect(st.progresso, isEmpty);
      expect(st.xp, 0);
      expect(st.carteira.gc, 0);
      expect(st.lives, AppState.maxLives);
      expect(st.nome, 'Ana');
      expect(st.classe, '1ª classe');
    });

    test('«pôr à venda» devolve a app que a criança recebe', () async {
      final st = estado();
      await st.definirInterruptores(
        const InterruptoresDeTeste(
          aVenda: true,
          coracoesInfinitos: true,
          nadaCusta: true,
        ),
      );
      expect(st.modoTeste, isFalse);
      expect(st.saltoLivre, isFalse, reason: 'a fila dos níveis volta');
      expect(st.jogosLivres, isFalse);
      expect(st.treinoLivre, isFalse);
      // Os outros interruptores ficam guardados, mas deixam de valer: é o
      // que faz do «pôr à venda» um só gesto para ver o outro lado.
      expect(st.coracoesInfinitos, isFalse);
      expect(st.nadaCusta, isFalse);
      expect(st.tempoDeJogo, lessThan(const Duration(minutes: 60)));
    });

    test('o desvio do calendário sobrevive à venda', () async {
      // Ver a app *real* no dia seguinte é um teste que faz sentido, e por
      // isso este não é um bloqueio que a venda reponha.
      final st = estado();
      await st.definirInterruptores(
        const InterruptoresDeTeste(aVenda: true, desvioDeDias: 3),
      );
      expect(st.desvioDeDias, 3);
    });

    test('esta compilação tem data e caduca', () {
      expect(ModoTeste.compiladaEm, isNotEmpty,
          reason: 'o compilar.sh passa sempre o SOMARA_DATA');
      expect(ModoTeste.diasQueFaltam(), isNotNull);
    });
  });

  group('a validade da versão de testes', () {
    test('sem data não caduca', () {
      expect(ModoTeste.diasQueFaltamDe('', DateTime(2026, 10, 4)), isNull);
    });

    test('data estragada não caduca', () {
      expect(
        ModoTeste.diasQueFaltamDe('ontem', DateTime(2026, 10, 4)),
        isNull,
        reason: 'uma data que não se entende não pode fechar a app',
      );
    });

    test('no dia da compilação faltam os 60 dias inteiros', () {
      expect(
        ModoTeste.diasQueFaltamDe('2026-10-04', DateTime(2026, 10, 4, 23, 59)),
        ModoTeste.validade.inDays,
      );
    });

    test('a hora do dia não muda a conta', () {
      final manha = ModoTeste.diasQueFaltamDe(
        '2026-10-04',
        DateTime(2026, 11, 1, 6),
      );
      final noite = ModoTeste.diasQueFaltamDe(
        '2026-10-04',
        DateTime(2026, 11, 1, 23, 50),
      );
      expect(manha, noite);
    });

    test('no último dia ainda falta um', () {
      final fim = DateTime(2026, 10, 4).add(ModoTeste.validade);
      expect(
        ModoTeste.diasQueFaltamDe(
          '2026-10-04',
          fim.subtract(const Duration(days: 1)),
        ),
        1,
      );
    });

    test('no dia de caducar não falta nenhum', () {
      final fim = DateTime(2026, 10, 4).add(ModoTeste.validade);
      expect(ModoTeste.diasQueFaltamDe('2026-10-04', fim), 0);
    });

    test('depois disso fica negativo', () {
      final fim = DateTime(2026, 10, 4).add(ModoTeste.validade);
      expect(
        ModoTeste.diasQueFaltamDe('2026-10-04', fim.add(const Duration(days: 5))),
        -5,
      );
    });

    test('sessenta dias é o combinado', () {
      expect(ModoTeste.validade, const Duration(days: 60));
    });
  });

  group('os interruptores guardam-se e leem-se', () {
    test('ida e volta pelo JSON', () {
      const antes = InterruptoresDeTeste(
        aVenda: true,
        coracoesInfinitos: true,
        nadaCusta: true,
        desvioDeDias: 3,
      );
      final depois = InterruptoresDeTeste.deJson(antes.paraJson());
      expect(depois.aVenda, isTrue);
      expect(depois.coracoesInfinitos, isTrue);
      expect(depois.nadaCusta, isTrue);
      expect(depois.desvioDeDias, 3);
    });

    test('tudo desligado por omissão', () {
      final v = InterruptoresDeTeste.deJson(null);
      expect(v.aVenda, isFalse);
      expect(v.coracoesInfinitos, isFalse);
      expect(v.nadaCusta, isFalse);
      expect(v.desvioDeDias, 0);
    });

    test('um desvio negativo não entra', () {
      // Empurrar o calendário para trás punha a sequência de dias a ver
      // actividade no futuro — um estado que a app nunca pode ter.
      final v = InterruptoresDeTeste.deJson({'dias': -4});
      expect(v.desvioDeDias, 0);
    });

    test('lixo no ficheiro não rebenta nada', () {
      final v = InterruptoresDeTeste.deJson({
        'aVenda': 'talvez',
        'dias': 'muitos',
      });
      expect(v.aVenda, isFalse);
      expect(v.desvioDeDias, 0);
    });

    test('«pôr à venda» manda em todos os outros', () {
      // Com a venda ligada, a app de testes tem de ser indistinguível da
      // normal — é para isso que esse interruptor existe. Aqui prova-se a
      // regra na própria estrutura: ligada a venda, o que a app lê é o
      // caminho normal, qualquer que seja o resto.
      const tudoLigado = InterruptoresDeTeste(
        aVenda: true,
        coracoesInfinitos: true,
        nadaCusta: true,
      );
      expect(tudoLigado.aVenda, isTrue);
      // O estado deriva de `ModoTeste.activo && !aVenda`, e nesta
      // compilação o primeiro já é falso: o que se garante aqui é que a
      // estrutura guarda a venda, e o teste de cima garante o resto.
      expect(tudoLigado.com(aVenda: false).aVenda, isFalse);
    });
  });
}
