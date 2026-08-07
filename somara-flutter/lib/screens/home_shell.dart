import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../state/app_state.dart';
import '../theme.dart';
import 'map_screen.dart';

/// Casca da app: barra de estado (vidas, XP, streak) + a amarelinha.
class HomeShell extends StatelessWidget {
  const HomeShell({super.key});

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    return Scaffold(
      backgroundColor: S.gm950,
      body: SafeArea(
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.fromLTRB(20, 12, 20, 2),
              child: Row(
                children: [
                  _pastilha(Icons.favorite_rounded, '${st.lives}', S.life),
                  const SizedBox(width: 18),
                  _pastilha(Icons.bolt_rounded, '${st.xp}', S.chart),
                  const SizedBox(width: 18),
                  _pastilha(Icons.local_fire_department_rounded, '${st.streak}',
                      S.gold),
                  const Spacer(),
                  if (st.nome.isNotEmpty)
                    CircleAvatar(
                      radius: 18,
                      backgroundColor: S.green500,
                      child: Text(
                        st.nome.characters.first.toUpperCase(),
                        style: const TextStyle(
                            color: Colors.white,
                            fontWeight: FontWeight.w700,
                            fontSize: 16),
                      ),
                    ),
                ],
              ),
            ),
            const Expanded(child: MapScreen()),
          ],
        ),
      ),
    );
  }

  Widget _pastilha(IconData icone, String valor, Color cor) => Row(
        children: [
          Icon(icone, color: cor, size: 21),
          const SizedBox(width: 5),
          Text(valor,
              style: TextStyle(
                  color: cor, fontWeight: FontWeight.w700, fontSize: 16)),
        ],
      );
}
