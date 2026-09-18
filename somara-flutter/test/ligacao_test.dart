import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';

/// A correcção das ligações.
///
/// Durante muito tempo comparou-se o índice da ficha da direita, e isso
/// só falhava quando duas fichas tinham o mesmo texto — o que nenhum curso
/// fazia até à Química da 8ª («Oxigénio → Elementar, Ferro → Elementar»).
/// Aí, ligar o Ferro à primeira «Elementar» dava errado sem a criança ter
/// errado nada: as duas fichas são iguais no ecrã.
void main() {
  const substancias = QMatch(
    'Liga cada substância à sua classe.',
    '',
    pairs: [
      ('Oxigénio', 'Elementar'),
      ('Ferro', 'Elementar'),
      ('Água', 'Composta'),
    ],
  );

  test('a ligação certa, ficha a ficha, está certa', () {
    expect(substancias.certa({0: 0, 1: 1, 2: 2}), isTrue);
  });

  test('trocar duas fichas com o mesmo texto continua certo', () {
    expect(substancias.certa({0: 1, 1: 0, 2: 2}), isTrue);
  });

  test('ligar a uma ficha de texto diferente está errado', () {
    expect(substancias.certa({0: 2, 1: 1, 2: 0}), isFalse);
  });

  test('uma ligação a meio não conta', () {
    expect(substancias.certa({0: 0, 1: 1}), isFalse);
  });

  test('sem textos repetidos, só a ligação exacta serve', () {
    const pares = QMatch('', '', pairs: [('A', 'x'), ('B', 'y')]);
    expect(pares.certa({0: 0, 1: 1}), isTrue);
    expect(pares.certa({0: 1, 1: 0}), isFalse);
  });

  test('um índice fora da coluna não rebenta: está só errado', () {
    expect(substancias.certa({0: 0, 1: 1, 2: 7}), isFalse);
  });
}
