import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/sequencia.dart';

/// Estes testes existem porque um erro na contagem de dias só se manifesta
/// dias depois, quando já é tarde para perceber onde falhou.
void main() {
  DateTime dia(int ano, int mes, int d, [int hora = 10]) =>
      DateTime(ano, mes, d, hora);

  group('o que se mostra no ecrã', () {
    test('sem nunca ter estudado, mostra zero', () {
      expect(const Sequencia().visivelEm(dia(2026, 8, 7)), 0);
    });

    test('tendo estudado hoje, mostra a contagem', () {
      const s = Sequencia(ultimoDia: '2026-08-07', dias: 4);
      expect(s.visivelEm(dia(2026, 8, 7)), 4);
    });

    test('tendo estudado ontem, ainda mostra — o dia ainda não acabou', () {
      const s = Sequencia(ultimoDia: '2026-08-06', dias: 4);
      expect(s.visivelEm(dia(2026, 8, 7)), 4);
    });

    test('faltando dois dias, a sequência partiu-se e mostra zero', () {
      const s = Sequencia(ultimoDia: '2026-08-05', dias: 40);
      expect(s.visivelEm(dia(2026, 8, 7)), 0);
    });
  });

  group('o que acontece ao concluir um nível', () {
    test('a primeira vez de sempre começa em 1', () {
      final s = const Sequencia().comActividadeEm(dia(2026, 8, 7));
      expect(s.dias, 1);
      expect(s.ultimoDia, '2026-08-07');
    });

    test('dois níveis no mesmo dia contam como um só', () {
      var s = const Sequencia().comActividadeEm(dia(2026, 8, 7, 9));
      s = s.comActividadeEm(dia(2026, 8, 7, 20));
      expect(s.dias, 1);
    });

    test('dias seguidos somam', () {
      var s = const Sequencia();
      for (var d = 1; d <= 5; d++) {
        s = s.comActividadeEm(dia(2026, 8, d));
      }
      expect(s.dias, 5);
    });

    test('um dia falhado recomeça do 1', () {
      var s = const Sequencia(ultimoDia: '2026-08-01', dias: 9);
      s = s.comActividadeEm(dia(2026, 8, 3));
      expect(s.dias, 1);
    });

    test('atravessa a viragem do mês', () {
      var s = const Sequencia(ultimoDia: '2026-08-31', dias: 12);
      s = s.comActividadeEm(dia(2026, 9, 1));
      expect(s.dias, 13);
    });

    test('atravessa a viragem do ano', () {
      var s = const Sequencia(ultimoDia: '2026-12-31', dias: 30);
      s = s.comActividadeEm(dia(2027, 1, 1));
      expect(s.dias, 31);
    });

    test('conta o 29 de Fevereiro de um ano bissexto', () {
      var s = const Sequencia(ultimoDia: '2028-02-28', dias: 3);
      s = s.comActividadeEm(dia(2028, 2, 29));
      expect(s.dias, 4);
      s = s.comActividadeEm(dia(2028, 3, 1));
      expect(s.dias, 5);
    });

    test('estudar tarde e cedo em dias seguidos conta como dois dias', () {
      // 23h de um dia e 7h do dia seguinte distam 8 horas, mas são dois
      // dias de calendário — e é o calendário que conta.
      var s = const Sequencia().comActividadeEm(dia(2026, 8, 7, 23));
      s = s.comActividadeEm(dia(2026, 8, 8, 7));
      expect(s.dias, 2);
    });
  });

  test('sobrevive a ser gravada e lida de novo', () {
    final antes = const Sequencia().comActividadeEm(dia(2026, 8, 7));
    final depois = Sequencia.deJson(antes.paraJson());
    expect(depois.dias, antes.dias);
    expect(depois.ultimoDia, antes.ultimoDia);
  });

  test('estado gravado em falta não rebenta', () {
    expect(Sequencia.deJson(null).dias, 0);
  });
}
