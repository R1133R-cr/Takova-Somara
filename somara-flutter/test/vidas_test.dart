import 'package:flutter_test/flutter_test.dart';
import 'package:somara/state/app_state.dart';

/// A escada de esperas é uma lista de constantes — o tipo de coisa que
/// alguém reordena por engano e que só se nota meses depois, quando uma
/// criança leva três horas de castigo à primeira falha.
void main() {
  test('as esperas crescem sempre, nunca encolhem', () {
    for (var i = 1; i < AppState.esperas.length; i++) {
      expect(AppState.esperas[i], greaterThan(AppState.esperas[i - 1]),
          reason: 'espera ${i + 1} não é maior que a anterior');
    }
  });

  test('a primeira espera é curta o suficiente para não afastar', () {
    // Uma criança que apanha o telemóvel meia hora por dia não pode levar
    // com um castigo longo logo à primeira.
    expect(AppState.esperas.first, lessThanOrEqualTo(const Duration(minutes: 5)));
  });

  test('a espera mais longa não passa de três horas', () {
    expect(AppState.esperas.last, lessThanOrEqualTo(const Duration(hours: 3)));
  });

  test('a escada é a combinada: 5, 15, 30 minutos, 1 e 3 horas', () {
    expect(AppState.esperas, const [
      Duration(minutes: 5),
      Duration(minutes: 15),
      Duration(minutes: 30),
      Duration(hours: 1),
      Duration(hours: 3),
    ]);
  });
}
