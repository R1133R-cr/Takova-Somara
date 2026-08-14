import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';

/// Ranking.
///
/// Sem contas não há com quem comparar: qualquer tabela de colegas seria
/// inventada, e mostrar números falsos a uma criança é pior do que não
/// mostrar nada. Até haver contas, isto mostra os registos dela própria —
/// que é competir contra ontem, e para esta idade funciona melhor.
class RankingScreen extends StatelessWidget {
  const RankingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final total = st.niveisDaClasse;
    final feitos = st.niveisConcluidos;
    final pct = total == 0 ? 0.0 : feitos / total;

    return ListView(
      padding: const EdgeInsets.fromLTRB(20, 12, 20, 28),
      children: [
        const Text('Ranking',
            style: TextStyle(
                fontSize: 27, fontWeight: FontWeight.w700, color: S.tx)),
        const SizedBox(height: 6),
        const Text('Por agora, competes contigo mesmo.',
            style: TextStyle(color: S.txSoft, fontSize: 15)),
        const SizedBox(height: 24),

        Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            color: S.surface,
            border: Border.all(color: S.line, width: 2),
            borderRadius: BorderRadius.circular(S.rLg),
          ),
          child: Column(
            children: [
              Row(
                children: [
                  Expanded(child: _numero('${st.xp}', 'XP', S.chart)),
                  Expanded(child: _numero('${st.streak}', 'dias seguidos', S.gold)),
                  Expanded(child: _numero('$feitos', 'níveis', S.green300)),
                ],
              ),
              const SizedBox(height: 22),
              Align(
                alignment: Alignment.centerLeft,
                child: Text('${st.classe} · ${(pct * 100).round()}% concluída',
                    style: const TextStyle(color: S.txSoft, fontSize: 13.5)),
              ),
              const SizedBox(height: 8),
              ClipRRect(
                borderRadius: BorderRadius.circular(S.rPill),
                child: TweenAnimationBuilder<double>(
                  tween: Tween(begin: 0, end: pct),
                  duration: const Duration(milliseconds: 600),
                  curve: SCurves.ease,
                  builder: (_, v, _) => LinearProgressIndicator(
                    value: v,
                    minHeight: 12,
                    backgroundColor: S.gm900,
                    valueColor: const AlwaysStoppedAnimation(S.chart),
                  ),
                ),
              ),
            ],
          ),
        ),
        const SizedBox(height: 26),

        Container(
          padding: const EdgeInsets.all(18),
          decoration: BoxDecoration(
            color: S.surface,
            border: Border.all(color: S.line),
            borderRadius: BorderRadius.circular(S.rLg),
          ),
          child: Row(
            children: [
              Opacity(
                opacity: 0.85,
                child: Image.asset(RobyPose.curioso.path, width: 66),
              ),
              const SizedBox(width: 14),
              const Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('Comparar com os colegas',
                        style: TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.w700,
                            color: S.tx)),
                    SizedBox(height: 5),
                    Text(
                      'Para veres quem está à frente é preciso criar conta, '
                      'para o teu progresso viajar contigo. Ainda estamos a '
                      'preparar isso.',
                      style: TextStyle(color: S.txSoft, fontSize: 13.5, height: 1.4),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _numero(String v, String rotulo, Color cor) => Column(
        children: [
          Text(v,
              style: TextStyle(
                  fontSize: 26, fontWeight: FontWeight.w700, color: cor)),
          const SizedBox(height: 3),
          Text(rotulo,
              textAlign: TextAlign.center,
              style: const TextStyle(color: S.txSoft, fontSize: 12)),
        ],
      );
}
