import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../models/conquista.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';

/// A parede de medalhas.
///
/// As ganhas a cores, as que faltam em silhueta **com a pista à vista**. Um
/// buraco na parede sem dizer o que lá deve estar não é mistério, é ruído:
/// ninguém persegue o que não sabe o que é.
class ConquistasScreen extends StatelessWidget {
  const ConquistasScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final ganhas = st.conquistas;

    return Scaffold(
      backgroundColor: S.gm950,
      appBar: AppBar(
        backgroundColor: S.gm950,
        foregroundColor: S.tx,
        elevation: 0,
        title: const Text('Medalhas', style: TextStyle(fontSize: 17)),
      ),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.fromLTRB(16, 4, 16, 28),
          children: [
            _contagem(ganhas.length, Conquista.values.length),
            const SizedBox(height: 20),
            for (final f in FamiliaDeConquista.values) ...[
              _seccao(f, ganhas),
              const SizedBox(height: 22),
            ],
          ],
        ),
      ),
    );
  }

  Widget _contagem(int ganhas, int total) => Container(
    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
    decoration: BoxDecoration(
      color: S.gm900,
      border: Border.all(color: S.gold.withValues(alpha: 0.5), width: 1.5),
      borderRadius: BorderRadius.circular(S.rMd),
    ),
    child: Row(
      children: [
        const Icon(Icons.military_tech_rounded, color: S.gold, size: 22),
        const SizedBox(width: 10),
        Expanded(
          child: Text(
            ganhas == 1 ? '1 medalha de $total' : '$ganhas medalhas de $total',
            style: const TextStyle(
              color: S.gold,
              fontSize: 16,
              fontWeight: FontWeight.w700,
            ),
          ),
        ),
      ],
    ),
  );

  Widget _seccao(FamiliaDeConquista f, Set<Conquista> ganhas) {
    final dela = Conquista.values.where((c) => c.familia == f).toList();
    final quantas = dela.where(ganhas.contains).length;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            Expanded(
              child: Text(
                f.rotulo,
                style: const TextStyle(
                  fontSize: 19,
                  fontWeight: FontWeight.w700,
                  color: S.tx,
                ),
              ),
            ),
            Text(
              '$quantas/${dela.length}',
              style: const TextStyle(color: S.txMut, fontSize: 13.5),
            ),
          ],
        ),
        const SizedBox(height: 2),
        Text(
          f.descricao,
          style: const TextStyle(color: S.txSoft, fontSize: 13.5),
        ),
        const SizedBox(height: 12),
        for (final c in dela) ...[
          _Medalha(conquista: c, ganha: ganhas.contains(c)),
          const SizedBox(height: 8),
        ],
      ],
    );
  }
}

class _Medalha extends StatelessWidget {
  final Conquista conquista;
  final bool ganha;

  const _Medalha({required this.conquista, required this.ganha});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.fromLTRB(12, 10, 14, 10),
      decoration: BoxDecoration(
        color: ganha ? S.surface : S.gm900,
        border: Border.all(
          color: ganha ? S.gold.withValues(alpha: 0.6) : S.line,
          width: ganha ? 2 : 1.5,
        ),
        borderRadius: BorderRadius.circular(S.rMd),
      ),
      child: Row(
        children: [
          SizedBox(
            width: 44,
            height: 44,
            child: Opacity(
              opacity: ganha ? 1 : 0.28,
              child: ColorFiltered(
                colorFilter: ganha
                    ? const ColorFilter.mode(Colors.transparent, BlendMode.dst)
                    : const ColorFilter.matrix(<double>[
                        0.2126, 0.7152, 0.0722, 0, 0, //
                        0.2126, 0.7152, 0.0722, 0, 0, //
                        0.2126, 0.7152, 0.0722, 0, 0, //
                        0, 0, 0, 1, 0, //
                      ]),
                child: RobyImagem(
                  ganha ? RobyPose.conquista : RobyPose.primeiro,
                  largura: 44,
                  alinhamento: Alignment.topCenter,
                ),
              ),
            ),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  conquista.titulo,
                  style: TextStyle(
                    color: ganha ? S.tx : S.txSoft,
                    fontSize: 15,
                    fontWeight: FontWeight.w700,
                  ),
                ),
                const SizedBox(height: 2),
                // A pista fica sempre, ganha ou não: depois de ganha explica
                // o que se fez, e antes diz o que falta fazer.
                Text(
                  conquista.pistaDita,
                  style: const TextStyle(
                    color: S.txMut,
                    fontSize: 12.5,
                    height: 1.3,
                  ),
                ),
              ],
            ),
          ),
          if (conquista.cristais > 0) ...[
            const SizedBox(width: 8),
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(
                  Icons.diamond_rounded,
                  size: 15,
                  color: ganha ? S.chart : S.txMut,
                ),
                const SizedBox(width: 3),
                Text(
                  '${conquista.cristais}',
                  style: TextStyle(
                    color: ganha ? S.chart : S.txMut,
                    fontSize: 13,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ],
            ),
          ],
        ],
      ),
    );
  }
}
