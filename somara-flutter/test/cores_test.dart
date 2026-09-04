import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';
import 'package:somara/theme.dart';
import 'package:somara/widgets/mostra_cores.dart';

/// A cor da Educação Visual, desenhada para se poder ver.
///
/// A pergunta de mistura só aparece no quarto nível de uma disciplina que
/// está no fim da barra da 6ª classe — chegar lá no emulador são vinte
/// toques, e vinte toques que falham a meio não provam nada. Isto desenha a
/// peça e guarda a imagem.
///
/// Para gravar a imagem outra vez, depois de mexer nas cores:
///     flutter test test/cores_test.dart --update-goldens
///
/// A imagem foi desenhada em Windows. Comparações de imagem são sensíveis
/// ao sistema — noutra máquina pode falhar sem que nada esteja mal.
void main() {
  const amarelo = 0xFFF2C200;
  const azul = 0xFF1E5AA8;
  const verde = 0xFF2E8B57;
  const laranja = 0xFFE8791C;
  const violeta = 0xFF7B3F9D;

  testWidgets('a mistura e as manchas das respostas', (tester) async {
    await tester.pumpWidget(
      MaterialApp(
        theme: somaraTheme(),
        home: Scaffold(
          backgroundColor: S.gm950,
          body: Center(
            child: Padding(
              padding: const EdgeInsets.all(20),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Text(
                    'Que cor sai de misturar amarelo com azul?',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                        fontSize: 19,
                        fontWeight: FontWeight.w700,
                        color: S.tx),
                  ),
                  const MostraCores(
                    cores: Cores(mistura: [amarelo, azul]),
                  ),
                  const SizedBox(height: 8),
                  // As respostas, como aparecem no ecrã da lição: a mancha
                  // ao lado do nome, para se escolher a cor e aprender o
                  // nome dela ao mesmo tempo.
                  for (final (cor, nome) in [
                    (verde, 'Verde'),
                    (laranja, 'Laranja'),
                    (violeta, 'Violeta'),
                  ])
                    Padding(
                      padding: const EdgeInsets.only(bottom: 12),
                      child: Container(
                        constraints: const BoxConstraints(minHeight: 62),
                        alignment: Alignment.center,
                        padding: const EdgeInsets.symmetric(
                            horizontal: 18, vertical: 17),
                        decoration: BoxDecoration(
                          color: S.surface,
                          border: Border.all(color: S.line, width: 2),
                          borderRadius: BorderRadius.circular(S.rMd),
                        ),
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            GotaDaOpcao(cor: Color(cor)),
                            Text(nome,
                                style: const TextStyle(
                                    fontSize: 18,
                                    fontWeight: FontWeight.w600,
                                    color: S.tx)),
                          ],
                        ),
                      ),
                    ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
    await tester.pumpAndSettle();

    await expectLater(
      find.byType(Column).first,
      matchesGoldenFile('goldens/cores_educacao_visual.png'),
    );
  });

  test('o hexadecimal do content.json vira a cor certa', () {
    final c = Cores.fromJson(const {
      'mistura': ['#F2C200', '#1E5AA8'],
      'opcoes': ['#2E8B57'],
    });
    expect(c.mistura, [amarelo, azul]);
    expect(c.opcoes, [verde]);
    expect(c.temMistura, isTrue);

    // Uma cor só não é mistura nenhuma.
    expect(
      Cores.fromJson(const {'mistura': ['#F2C200']}).temMistura,
      isFalse,
    );
  });
}
