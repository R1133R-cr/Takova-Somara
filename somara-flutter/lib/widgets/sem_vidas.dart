import 'dart:async';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../state/app_state.dart';
import '../theme.dart';
import 'roby.dart';

/// Mostrado quando a criança tenta entrar num nível sem vidas.
///
/// A espera cresce a cada vez que as vidas acabam no mesmo dia, e reinicia
/// no dia seguinte. Mas o ecrã nunca é só uma porta fechada: quem fica sem
/// vidas é quem está com mais dificuldade, e mandá-la embora seria castigar
/// exactamente a criança que mais precisa de praticar. Por isso a revisão
/// dos erros fica sempre aberta — e é para lá que este ecrã aponta.
class SemVidas extends StatefulWidget {
  /// Chamado quando a criança escolhe ir rever os erros.
  final VoidCallback? aoRever;

  const SemVidas({super.key, this.aoRever});

  /// Abre a folha e devolve `true` se a espera terminou entretanto.
  static Future<void> mostrar(BuildContext context, {VoidCallback? aoRever}) {
    return showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (_) => SemVidas(aoRever: aoRever),
    );
  }

  @override
  State<SemVidas> createState() => _SemVidasState();
}

class _SemVidasState extends State<SemVidas> {
  Timer? _relogio;

  @override
  void initState() {
    super.initState();
    // Um tique por segundo só para redesenhar a contagem. A hora do fim está
    // guardada — se a app fechar, a espera continua a correr na mesma.
    _relogio = Timer.periodic(const Duration(seconds: 1), (_) {
      if (!mounted) {
        _relogio?.cancel();
        return;
      }
      final st = context.read<AppState>();
      st.verificarFimDoBloqueio();
      if (!st.bloqueado) {
        _relogio?.cancel();
        // `isCurrent` porque esta folha demora uns 250 ms a fechar-se: se a
        // espera acabasse exactamente nessa janela, sem esta guarda o pop
        // fechava a revisão que a criança acabara de abrir.
        if (ModalRoute.of(context)?.isCurrent ?? false) {
          Navigator.of(context).pop();
        }
      } else {
        setState(() {});
      }
    });
  }

  @override
  void dispose() {
    _relogio?.cancel();
    super.dispose();
  }

  static String _emPortugues(Duration d) {
    if (d.inHours >= 1) {
      final m = d.inMinutes.remainder(60);
      return m == 0 ? '${d.inHours}h' : '${d.inHours}h ${m}min';
    }
    if (d.inMinutes >= 1) {
      return '${d.inMinutes}min ${d.inSeconds.remainder(60)}s';
    }
    return '${d.inSeconds}s';
  }

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final falta = st.esperaRestante;
    final porRever = st.paraRever.length;

    return Container(
      width: double.infinity,
      padding: EdgeInsets.fromLTRB(
          24, 26, 24, 26 + MediaQuery.of(context).padding.bottom),
      decoration: const BoxDecoration(
        color: S.gm800,
        borderRadius: BorderRadius.vertical(top: Radius.circular(26)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Image.asset(RobyPose.triste.path, width: 108),
          const SizedBox(height: 14),
          const Text('Ficaste sem corações',
              style: TextStyle(
                  fontSize: 22, fontWeight: FontWeight.w700, color: S.tx)),
          const SizedBox(height: 8),
          Text(
            'Descansa um bocado. Os corações voltam daqui a pouco.',
            textAlign: TextAlign.center,
            style: const TextStyle(color: S.txSoft, fontSize: 15, height: 1.4),
          ),
          const SizedBox(height: 20),

          Container(
            padding: const EdgeInsets.symmetric(horizontal: 26, vertical: 14),
            decoration: BoxDecoration(
              color: S.gm900,
              border: Border.all(color: S.life, width: 2),
              borderRadius: BorderRadius.circular(S.rPill),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                const Icon(Icons.hourglass_bottom_rounded,
                    color: S.life, size: 22),
                const SizedBox(width: 10),
                Text(_emPortugues(falta),
                    style: const TextStyle(
                        color: S.life,
                        fontSize: 24,
                        fontWeight: FontWeight.w700,
                        fontFeatures: [FontFeature.tabularFigures()])),
              ],
            ),
          ),
          const SizedBox(height: 22),

          // A saída. Praticar os erros não gasta corações — quem está a
          // falhar precisa de mais treino, não de menos.
          if (porRever > 0) ...[
            SizedBox(
              width: double.infinity,
              child: GestureDetector(
                onTap: () {
                  _relogio?.cancel();
                  Navigator.of(context).pop();
                  widget.aoRever?.call();
                },
                child: Container(
                  padding: const EdgeInsets.symmetric(vertical: 17),
                  decoration: BoxDecoration(
                    color: S.chart,
                    borderRadius: BorderRadius.circular(S.rPill),
                    boxShadow: const [
                      BoxShadow(color: S.chart600, offset: Offset(0, 4)),
                    ],
                  ),
                  alignment: Alignment.center,
                  child: Text('Rever os meus erros ($porRever)',
                      style: const TextStyle(
                          fontSize: 17,
                          fontWeight: FontWeight.w700,
                          color: S.onChart)),
                ),
              ),
            ),
            const SizedBox(height: 10),
            const Text('A revisão não gasta corações.',
                style: TextStyle(color: S.txMut, fontSize: 12.5)),
          ] else
            const Text(
              'Enquanto esperas, podes ver o teu progresso no Perfil.',
              textAlign: TextAlign.center,
              style: TextStyle(color: S.txMut, fontSize: 13),
            ),
        ],
      ),
    );
  }
}
