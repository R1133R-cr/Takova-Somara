import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/campanha.dart';
import '../models/content.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';
import 'lesson_screen.dart';

/// Treinar o que já se aprendeu, sem avançar no mapa.
///
/// A separação importa: a amarelinha é para descobrir matéria nova, e treinar
/// não deve dar avanço nenhum lá — senão a criança sobe de nível sem ter
/// aprendido nada de novo.
class PraticarScreen extends StatelessWidget {
  const PraticarScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final rever = st.paraRever;
    final temFeitos = st.niveisConcluidos > 0;

    return ListView(
      padding: const EdgeInsets.fromLTRB(20, 12, 20, 28),
      children: [
        const Text('Praticar',
            style: TextStyle(
                fontSize: 27, fontWeight: FontWeight.w700, color: S.tx)),
        const SizedBox(height: 6),
        const Text('Treina sem perder o teu lugar na amarelinha.',
            style: TextStyle(color: S.txSoft, fontSize: 15)),
        const SizedBox(height: 24),

        // A campanha vem primeiro porque é a única coisa da app com prazo.
        // Enterrada debaixo do treino, passava a semana sem se ver.
        if (st.campanha != null) ...[
          _CartaoDaCampanha(campanha: st.campanha!),
          const SizedBox(height: 14),
        ],

        _Cartao(
          icone: Icons.refresh_rounded,
          cor: S.life,
          titulo: 'Rever os meus erros',
          detalhe: rever.isEmpty
              ? 'Ainda não erraste nada. Quando errares, a pergunta aparece aqui.'
              : '${rever.length} ${rever.length == 1 ? "pergunta" : "perguntas"} '
                  'à espera de revisão.',
          activo: rever.isNotEmpty,
          onTap: () => _abrir(context, rever.take(10).toList(), 'Revisão'),
        ),
        const SizedBox(height: 14),

        _Cartao(
          icone: Icons.shuffle_rounded,
          cor: S.chart,
          titulo: 'Treino baralhado',
          detalhe: temFeitos
              ? '10 perguntas ao acaso dos níveis que já fizeste.'
              : 'Termina um nível na amarelinha para desbloquear o treino.',
          activo: temFeitos,
          onTap: () => _abrir(context, st.perguntasDeTreino(), 'Treino baralhado'),
        ),
        const SizedBox(height: 28),

        if (rever.isNotEmpty) ...[
          const Text('À espera de revisão',
              style: TextStyle(
                  fontSize: 15, fontWeight: FontWeight.w600, color: S.txSoft)),
          const SizedBox(height: 10),
          for (final q in rever.take(8))
            Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 13),
                decoration: BoxDecoration(
                  color: S.surface,
                  border: Border.all(color: S.line),
                  borderRadius: BorderRadius.circular(S.rMd),
                ),
                child: Row(
                  children: [
                    const Icon(Icons.error_outline_rounded,
                        color: S.life, size: 19),
                    const SizedBox(width: 10),
                    Expanded(
                      child: Text(q.q,
                          maxLines: 2,
                          overflow: TextOverflow.ellipsis,
                          style: const TextStyle(color: S.tx, fontSize: 14)),
                    ),
                  ],
                ),
              ),
            ),
        ] else
          Center(
            child: Column(
              children: [
                const SizedBox(height: 20),
                Opacity(
                  opacity: 0.5,
                  child: Image.asset(RobyPose.confiante.path, width: 110),
                ),
                const SizedBox(height: 14),
                const Text('Sem erros por rever. Bom trabalho!',
                    style: TextStyle(color: S.txSoft, fontSize: 15)),
              ],
            ),
          ),
      ],
    );
  }

  void _abrir(BuildContext context, List<Questao> qs, String titulo) {
    if (qs.isEmpty) return;
    Navigator.of(context).push(MaterialPageRoute(
      builder: (_) => LessonScreen(indice: -1, avulsas: qs, titulo: titulo),
    ));
  }
}

/// A campanha da semana: o desafio que expira ao domingo.
class _CartaoDaCampanha extends StatelessWidget {
  final Campanha campanha;
  const _CartaoDaCampanha({required this.campanha});

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final feita = campanha.feita;

    return GestureDetector(
      onTap: feita
          ? null
          : () {
              final qs = st.perguntasDaCampanha;
              if (qs.isEmpty) return;
              Navigator.of(context).push(
                MaterialPageRoute<void>(
                  builder: (_) => LessonScreen(
                    indice: -1,
                    avulsas: qs,
                    titulo: 'Campanha da semana',
                    campanha: true,
                  ),
                ),
              );
            },
      child: Container(
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: S.surface,
          border: Border.all(
            color: feita ? S.green300 : S.gold,
            width: 2,
          ),
          borderRadius: BorderRadius.circular(S.rLg),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Icon(
                  feita
                      ? Icons.verified_rounded
                      : Icons.local_fire_department_rounded,
                  color: feita ? S.green300 : S.gold,
                  size: 24,
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        'Campanha da semana',
                        style: TextStyle(
                          fontSize: 17,
                          fontWeight: FontWeight.w700,
                          color: S.tx,
                        ),
                      ),
                      const SizedBox(height: 3),
                      Text(
                        feita
                            ? _comoCorreu(campanha)
                            : '${campanha.quantas} perguntas do que estudaste e '
                                'do que erraste. Acaba antes de domingo.',
                        style: const TextStyle(
                          color: S.txSoft,
                          fontSize: 13.5,
                          height: 1.35,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            if (!feita) ...[
              const SizedBox(height: 12),
              Row(
                children: [
                  const Icon(Icons.auto_awesome_rounded,
                      color: S.gold, size: 16),
                  const SizedBox(width: 5),
                  Expanded(
                    child: Text(
                      'Menos de ${(Campanha.margemDeErro * 100).round()}% de '
                      'erro dá uma sorte. Quase tudo certo dá duas.',
                      style: const TextStyle(color: S.txMut, fontSize: 12.5),
                    ),
                  ),
                ],
              ),
            ],
          ],
        ),
      ),
    );
  }

  String _comoCorreu(Campanha c) {
    final ganhas = c.sortesGanhas;
    final certas = '${c.acertos} de ${c.total}';
    if (ganhas == 0) {
      return 'Feita: $certas. Para a semana há outra.';
    }
    return 'Feita: $certas. '
        'Ganhaste ${ganhas == 1 ? "uma sorte" : "duas sortes"}.';
  }
}

class _Cartao extends StatelessWidget {
  final IconData icone;
  final Color cor;
  final String titulo;
  final String detalhe;
  final bool activo;
  final VoidCallback onTap;

  const _Cartao({
    required this.icone,
    required this.cor,
    required this.titulo,
    required this.detalhe,
    required this.activo,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) => Opacity(
        opacity: activo ? 1 : 0.5,
        child: GestureDetector(
          onTap: activo ? onTap : null,
          child: Container(
            padding: const EdgeInsets.all(18),
            decoration: BoxDecoration(
              color: S.surface,
              border: Border.all(color: activo ? cor : S.line, width: 2),
              borderRadius: BorderRadius.circular(S.rLg),
            ),
            child: Row(
              children: [
                Container(
                  width: 46,
                  height: 46,
                  decoration: BoxDecoration(
                    color: cor.withValues(alpha: 0.16),
                    shape: BoxShape.circle,
                  ),
                  child: Icon(icone, color: cor, size: 24),
                ),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(titulo,
                          style: const TextStyle(
                              fontSize: 17,
                              fontWeight: FontWeight.w700,
                              color: S.tx)),
                      const SizedBox(height: 3),
                      Text(detalhe,
                          style: const TextStyle(color: S.txSoft, fontSize: 13.5)),
                    ],
                  ),
                ),
                if (activo)
                  const Icon(Icons.chevron_right_rounded, color: S.txSoft),
              ],
            ),
          ),
        ),
      );
}
