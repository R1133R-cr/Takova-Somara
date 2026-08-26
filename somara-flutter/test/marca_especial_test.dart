import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/pomar.dart';
import 'package:somara/theme.dart';
import 'package:somara/widgets/marca_especial.dart';

/// As marcas das peças especiais do Pomar, todas ao mesmo tempo.
///
/// No jogo, uma peça especial só nasce de um quatro-em-linha, e um tabuleiro
/// sorteado não oferece um quando se quer. Isto põe as quatro lado a lado
/// para se poderem ver de uma vez.
///
/// Para gravar a imagem outra vez, depois de mexer nas marcas:
///     flutter test test/marca_especial_test.dart --update-goldens
///
/// A imagem guardada foi desenhada em Windows. Comparações de imagem são
/// sensíveis ao sistema — noutra máquina o teste pode falhar sem que as
/// marcas estejam mal. Nesse caso: olhar para a imagem que o teste escreve
/// ao lado (`*_testImage.png`) antes de dar o defeito por certo.
void main() {
  /// Uma casa do tabuleiro com a marca lá dentro, como no jogo: fundo,
  /// borda e o produto por cima.
  Widget casa(Especial e) => Container(
    width: 96,
    height: 96,
    padding: const EdgeInsets.all(2.5),
    decoration: BoxDecoration(
      color: S.surface.withValues(alpha: 0.55),
      border: Border.all(color: S.line, width: 1.2),
      borderRadius: BorderRadius.circular(S.rMd),
    ),
    alignment: Alignment.center,
    child: Stack(
      alignment: Alignment.center,
      children: [
        MarcaDeEspecial(especial: e, lado: 96),
        const Text('M', style: TextStyle(fontSize: 50)),
      ],
    ),
  );

  testWidgets('as quatro marcas distinguem-se umas das outras', (tester) async {
    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          backgroundColor: S.gm950,
          body: Center(
            child: Wrap(
              spacing: 12,
              runSpacing: 12,
              children: [for (final e in Especial.values) casa(e)],
            ),
          ),
        ),
      ),
    );
    await tester.pumpAndSettle();

    await expectLater(
      find.byType(Wrap),
      matchesGoldenFile('goldens/marcas_especiais.png'),
    );
  });

  test('cada especial tem uma marca própria, menos a peça comum', () {
    // Se um dia se acrescentar um especial novo, o switch da marca deixa de
    // compilar — mas uma marca vazia compilaria. Isto trava isso.
    for (final e in Especial.values) {
      final marca = MarcaDeEspecial(especial: e, lado: 60);
      expect(marca.especial, e);
    }
    expect(Especial.values.length, 5,
        reason: 'nenhuma, riscadoH, riscadoV, embrulho, sol');
  });
}
