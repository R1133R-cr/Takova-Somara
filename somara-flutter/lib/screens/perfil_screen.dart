import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';

/// Quem sou eu, o que já fiz, e em que classe estou.
class PerfilScreen extends StatelessWidget {
  /// Chamado depois de mudar de classe, para levar logo à amarelinha nova.
  ///
  /// Sem isto, tocar numa classe só mudava a marca de visto e a criança
  /// ficava no mesmo ecrã sem saber se tinha acontecido alguma coisa —
  /// parecia que faltava um botão de confirmar. A consequência visível vale
  /// mais do que um botão.
  final VoidCallback? aoMudarClasse;

  const PerfilScreen({super.key, this.aoMudarClasse});

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final classes = st.conteudo.cursos.map((c) => c.classe).toSet().toList()
      ..sort();

    return ListView(
      padding: const EdgeInsets.fromLTRB(20, 12, 20, 28),
      children: [
        Row(
          children: [
            CircleAvatar(
              radius: 30,
              backgroundColor: S.green500,
              child: Text(
                st.nome.isEmpty ? '?' : st.nome.characters.first.toUpperCase(),
                style: const TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.w700,
                    fontSize: 26),
              ),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(st.nome.isEmpty ? 'Olá!' : st.nome,
                      style: const TextStyle(
                          fontSize: 23,
                          fontWeight: FontWeight.w700,
                          color: S.tx)),
                  Text(st.classe,
                      style: const TextStyle(color: S.txSoft, fontSize: 15)),
                ],
              ),
            ),
          ],
        ),
        const SizedBox(height: 24),

        Row(
          children: [
            Expanded(child: _stat('${st.xp}', 'XP', S.chart)),
            const SizedBox(width: 10),
            Expanded(child: _stat('${st.streak}', 'dias', S.gold)),
            const SizedBox(width: 10),
            // O total de todas as classes: aqui é a folha de serviço da
            // criança, não o progresso da classe onde está agora.
            Expanded(
                child: _stat(
                    '${st.niveisConcluidosTotal}', 'níveis', S.green300)),
          ],
        ),
        const SizedBox(height: 28),

        const Text('Mudar de classe',
            style: TextStyle(
                fontSize: 16, fontWeight: FontWeight.w700, color: S.tx)),
        const SizedBox(height: 4),
        const Text(
          'O progresso de cada classe fica guardado à parte — podes voltar '
          'atrás sem perder nada.',
          style: TextStyle(color: S.txSoft, fontSize: 13.5, height: 1.4),
        ),
        const SizedBox(height: 12),
        for (final c in classes)
          Padding(
            padding: const EdgeInsets.only(bottom: 9),
            child: GestureDetector(
              onTap: () {
                if (c == st.classe) return;
                st.mudarClasse(c);
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text('Agora estás na $c'),
                    duration: const Duration(seconds: 2),
                    backgroundColor: S.green700,
                  ),
                );
                aoMudarClasse?.call();
              },
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 180),
                padding:
                    const EdgeInsets.symmetric(horizontal: 16, vertical: 15),
                decoration: BoxDecoration(
                  color: c == st.classe ? S.surface2 : S.surface,
                  border: Border.all(
                      color: c == st.classe ? S.chart : S.line, width: 2),
                  borderRadius: BorderRadius.circular(S.rMd),
                ),
                child: Row(
                  children: [
                    Text(c,
                        style: const TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.w600,
                            color: S.tx)),
                    const Spacer(),
                    if (c == st.classe)
                      const Icon(Icons.check_rounded, color: S.chart, size: 22),
                  ],
                ),
              ),
            ),
          ),
        const SizedBox(height: 26),

        Center(
          child: Column(
            children: [
              Opacity(
                opacity: 0.75,
                child: Image.asset(RobyPose.dica.path, width: 92),
              ),
              const SizedBox(height: 10),
              Text('Somara · conteúdo ${st.conteudo.versao}',
                  style: const TextStyle(color: S.txMut, fontSize: 12)),
              const Text('Takova · Lichinga, Niassa',
                  style: TextStyle(color: S.txMut, fontSize: 12)),
            ],
          ),
        ),
      ],
    );
  }

  Widget _stat(String v, String rotulo, Color cor) => Container(
        padding: const EdgeInsets.symmetric(vertical: 16),
        decoration: BoxDecoration(
          color: S.surface,
          border: Border.all(color: S.line),
          borderRadius: BorderRadius.circular(S.rLg),
        ),
        child: Column(
          children: [
            Text(v,
                style: TextStyle(
                    fontSize: 22, fontWeight: FontWeight.w700, color: cor)),
            const SizedBox(height: 2),
            Text(rotulo,
                style: const TextStyle(color: S.txSoft, fontSize: 12)),
          ],
        ),
      );
}
