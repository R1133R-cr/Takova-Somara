import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/models/sequencia.dart';
import 'package:somara/state/app_state.dart';

/// A fusão do progresso local com o da nuvem.
///
/// É a parte do sistema onde um erro não dá erro nenhum: apaga meses de
/// trabalho de uma criança em silêncio, e ninguém dá por isso até ela
/// abrir a app e ver a amarelinha vazia. Daí a densidade de testes aqui.
///
/// A regra que todos verificam é a mesma: **fica sempre o melhor dos dois,
/// nunca o mais recente**.
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

  group('o progresso nunca encolhe', () {
    test('o XP fica com o maior dos dois', () {
      final st = estado()..xp = 300;
      st.fundirDaNuvem({'xp': 120});
      expect(st.xp, 300, reason: 'a nuvem estava atrasada e não pode mandar');

      final outro = estado()..xp = 50;
      outro.fundirDaNuvem({'xp': 900});
      expect(outro.xp, 900);
    });

    test('cada nível fica com a melhor nota', () {
      final st = estado();
      st.progresso['mat-1c:u1:n1'] = 100;
      st.progresso['mat-1c:u1:n2'] = 40;

      st.fundirDaNuvem({
        'progresso': {
          'mat-1c:u1:n1': 60, // pior na nuvem
          'mat-1c:u1:n2': 90, // melhor na nuvem
          'mat-1c:u2:n1': 70, // só existe na nuvem
        },
      });

      expect(st.progresso['mat-1c:u1:n1'], 100);
      expect(st.progresso['mat-1c:u1:n2'], 90);
      expect(st.progresso['mat-1c:u2:n1'], 70);
    });

    test('uma tarde a jogar sem rede sobrevive a entrar na conta', () {
      // O caso que motivou tudo isto: a criança jogou offline, e o que
      // está na nuvem é de ontem. Entrar não pode desfazer a tarde.
      final st = estado()..xp = 400;
      st.progresso['mat-1c:u1:n1'] = 100;
      st.progresso['mat-1c:u1:n2'] = 100;
      st.progresso['mat-1c:u2:n1'] = 80;

      st.fundirDaNuvem({
        'xp': 150,
        'progresso': {'mat-1c:u1:n1': 100},
      });

      expect(st.xp, 400);
      expect(st.progresso.length, 3);
    });

    test('as perguntas erradas dos dois lados juntam-se', () {
      final st = estado();
      st.erradas.addAll({'daqui', 'de ambos'});
      st.fundirDaNuvem({
        'erradas': ['de ambos', 'do outro telemóvel'],
      });
      expect(st.erradas, {'daqui', 'de ambos', 'do outro telemóvel'});
    });
  });

  group('quem é a criança', () {
    test('o nome da conta ganha ao que está no telemóvel', () {
      // Entrar numa conta é dizer "sou eu, este telemóvel é novo".
      final st = estado()..nome = 'Telemóvel emprestado';
      st.fundirDaNuvem({'nome': 'Amina'});
      expect(st.nome, 'Amina');
    });

    test('nome vazio na nuvem não apaga o que está escrito aqui', () {
      final st = estado()..nome = 'Amina';
      st.fundirDaNuvem({'nome': '   '});
      expect(st.nome, 'Amina');
    });

    test('uma classe que não existe é ignorada', () {
      // Conteúdo desactualizado no servidor não pode pôr a criança numa
      // classe sem currículo — ficaria com a amarelinha vazia.
      final st = estado();
      st.fundirDaNuvem({'classe': '12ª classe'});
      expect(st.classe, '1ª classe');
    });

    test('uma classe que existe é aceite', () {
      final st = estado();
      st.fundirDaNuvem({'classe': '5ª classe'});
      expect(st.classe, '5ª classe');
    });
  });

  group('a sequência de dias', () {
    test('fica a que chegou mais longe', () {
      const aqui = Sequencia(ultimoDia: '2026-08-10', dias: 3);
      const nuvem = Sequencia(ultimoDia: '2026-08-14', dias: 2);
      expect(aqui.fundirCom(nuvem).ultimoDia, '2026-08-14');
      expect(aqui.fundirCom(nuvem).dias, 2);
    });

    test('no mesmo dia, fica a maior', () {
      const a = Sequencia(ultimoDia: '2026-08-14', dias: 3);
      const b = Sequencia(ultimoDia: '2026-08-14', dias: 9);
      expect(a.fundirCom(b).dias, 9);
      expect(b.fundirCom(a).dias, 9);
    });

    test('não se somam os dois telemóveis', () {
      // Ter dois aparelhos não faz a criança ter estudado o dobro dos
      // dias. Inventar-lhe uma sequência maior seria mentir-lhe.
      const a = Sequencia(ultimoDia: '2026-08-14', dias: 4);
      const b = Sequencia(ultimoDia: '2026-08-14', dias: 5);
      expect(a.fundirCom(b).dias, 5);
    });

    test('quem nunca estudou não apaga quem estudou', () {
      const vazia = Sequencia();
      const cheia = Sequencia(ultimoDia: '2026-08-14', dias: 7);
      expect(vazia.fundirCom(cheia).dias, 7);
      expect(cheia.fundirCom(vazia).dias, 7);
    });
  });

  group('o que não deve viajar', () {
    test('as vidas e o bloqueio não vão para a nuvem', () {
      // São do aparelho e do momento. Sincronizar um castigo de três horas
      // para o telemóvel da escola seria absurdo.
      final st = estado();
      final payload = st.paraNuvem();
      expect(payload.containsKey('lives'), isFalse);
      expect(payload.containsKey('bloqueadoAte'), isFalse);
      expect(payload.containsKey('vezesSemVidas'), isFalse);
      expect(payload.containsKey('som'), isFalse);
    });

    test('vai o que é da criança', () {
      final payload = estado().paraNuvem();
      expect(
        payload.keys,
        containsAll(['nome', 'classe', 'xp', 'sequencia', 'progresso', 'erradas']),
      );
    });
  });

  test('uma conta nova e vazia não estraga nada do que está aqui', () {
    final st = estado()..xp = 250;
    st.progresso['mat-1c:u1:n1'] = 100;
    st.fundirDaNuvem({});
    expect(st.xp, 250);
    expect(st.progresso['mat-1c:u1:n1'], 100);
    expect(st.classe, '1ª classe');
  });
}
