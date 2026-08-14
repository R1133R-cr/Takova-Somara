import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:somara/models/content.dart';
import 'package:somara/state/app_state.dart';

/// Contagem de progresso.
///
/// O progresso é guardado numa só tabela para todas as classes, e a chave
/// leva o curso lá dentro. Contar as chaves todas e comparar com os níveis
/// de uma classe só dava percentagens impossíveis — foi o que acontecia:
/// quem trocasse da 1ª para a 6ª via a 6ª "100% concluída" sem lá ter
/// feito nada. Estes testes seguram essa relação.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  late Conteudo c;

  setUpAll(() async {
    c = await Conteudo.carregar();
    SharedPreferences.setMockInitialValues({});
  });

  /// Um estado com o conteúdo real mas sem passar pelo disco.
  AppState comProgressoDe(String classe) {
    final st = AppState()
      ..conteudo = c
      ..classe = classe;
    return st;
  }

  /// Marca todos os níveis de uma classe como feitos.
  void concluirTudoDe(AppState st, String classe) {
    for (final curso in c.cursos.where((x) => x.classe == classe)) {
      for (final u in curso.units) {
        for (final n in u.niveis) {
          st.progresso['${curso.id}:${u.id}:${n.id}'] = 100;
        }
      }
    }
  }

  test('os níveis feitos noutra classe não contam para a classe actual', () {
    final st = comProgressoDe('6ª classe');
    concluirTudoDe(st, '1ª classe');

    expect(st.niveisConcluidos, 0,
        reason: 'a 6ª classe não tem nada feito — o trabalho foi na 1ª');
    expect(st.niveisConcluidosTotal, greaterThan(0),
        reason: 'mas o trabalho da 1ª não desaparece do Perfil');
  });

  test('nunca há mais níveis feitos do que níveis na classe', () {
    for (final classe in [
      '1ª classe', '2ª classe', '3ª classe',
      '4ª classe', '5ª classe', '6ª classe',
    ]) {
      final st = comProgressoDe(classe);
      // Progresso de toda a gente, em todas as classes.
      for (final curso in c.cursos) {
        for (final u in curso.units) {
          for (final n in u.niveis) {
            st.progresso['${curso.id}:${u.id}:${n.id}'] = 100;
          }
        }
      }
      expect(st.niveisConcluidos, lessThanOrEqualTo(st.niveisDaClasse),
          reason: classe);
      expect(st.niveisConcluidos, st.niveisDaClasse,
          reason: '$classe: com tudo feito, tem de dar 100%');
    }
  });

  test('o treino dá o XP que o ecrã de fim promete', () async {
    final st = comProgressoDe('1ª classe');
    final antes = st.xp;
    st.concluirTreino(7);
    expect(st.xp, antes + 7 * AppState.xpPorAcerto);
  });

  test('o treino conta como dia de estudo', () async {
    final st = comProgressoDe('1ª classe');
    expect(st.streak, 0);
    st.concluirTreino(3);
    expect(st.streak, 1, reason: 'rever os erros é estudar');
  });
}
