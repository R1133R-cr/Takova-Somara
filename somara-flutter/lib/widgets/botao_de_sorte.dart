import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../models/sorte.dart';
import '../state/app_state.dart';
import '../theme.dart';

/// O botão «Sorte», igual nos dois jogos.
///
/// Está num sítio só para não divergir: um botão de ajuda que num jogo se
/// chama de uma maneira e noutro de outra obriga a criança a aprender duas
/// vezes a mesma coisa.
///
/// **Mostra sempre quantas há**, mesmo quando são zero. Um botão que
/// desaparece quando o saldo acaba esconde a existência da ajuda a quem
/// nunca a teve — e é justamente essa criança que precisa de saber que ela
/// existe e como se ganha.
class BotaoDeSorte extends StatelessWidget {
  /// Chamado quando há sortes e o jogo está pronto a receber uma. Nulo
  /// enquanto o tabuleiro estiver ocupado.
  final VoidCallback? aoPedir;

  const BotaoDeSorte({super.key, required this.aoPedir});

  @override
  Widget build(BuildContext context) {
    final quantas = context.watch<AppState>().sortes.quantas;
    final activo = quantas > 0 && aoPedir != null;

    return Padding(
      padding: const EdgeInsets.only(right: 8),
      child: GestureDetector(
        onTap: activo
            ? aoPedir
            : () => ScaffoldMessenger.of(context)
                ..hideCurrentSnackBar()
                ..showSnackBar(
                  const SnackBar(
                    content: Text(
                      'Ganhas uma sorte por cada lição que acertares toda.',
                    ),
                    backgroundColor: S.gm800,
                    duration: Duration(milliseconds: 2200),
                  ),
                ),
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 11, vertical: 7),
          decoration: BoxDecoration(
            color: activo ? S.gold.withValues(alpha: 0.18) : S.gm900,
            border: Border.all(
              color: activo ? S.gold : S.line,
              width: 1.5,
            ),
            borderRadius: BorderRadius.circular(S.rPill),
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(
                Icons.auto_awesome_rounded,
                size: 16,
                color: activo ? S.gold : S.txMut,
              ),
              const SizedBox(width: 5),
              Text(
                'Sorte $quantas',
                style: TextStyle(
                  color: activo ? S.gold : S.txMut,
                  fontSize: 13.5,
                  fontWeight: FontWeight.w700,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

/// O que dizer quando a Sorte não encontra nada para mostrar.
///
/// Acontece pouco, mas acontece: uma sopa em que só falta uma palavra e o
/// dedo já passou por cima dela, um Pomar sem jogada nenhuma. Nesse caso a
/// sorte **não se gasta** — cobrar por uma ajuda que não ajudou seria roubo.
const semNadaParaMostrar = 'Não há nada escondido que tu ainda não tenhas '
    'olhado. A sorte fica contigo.';

/// Diz quantas ficaram, depois de se gastar uma.
String sobramSortes(Sortes s) => s.quantas == 0
    ? 'Era a tua última sorte.'
    : 'Ficas com ${sortesEmPalavras(s.quantas)}.';
