import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../state/app_state.dart';
import '../theme.dart';
import 'map_screen.dart';

/// Casca da app: barra de estado (vidas, XP, sequência) + a amarelinha.
class HomeShell extends StatelessWidget {
  const HomeShell({super.key});

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    return PopScope(
      // O botão de voltar fechava a app de repente. Numa demonstração — ou
      // na mão de uma criança — isso lê-se como a app ter ido abaixo.
      canPop: false,
      onPopInvokedWithResult: (jaSaiu, _) async {
        if (jaSaiu) return;
        final sair = await _confirmarSaida(context);
        if (sair) await SystemNavigator.pop();
      },
      child: Scaffold(
        backgroundColor: S.gm950,
        body: SafeArea(
          child: Column(
            children: [
              Padding(
                padding: const EdgeInsets.fromLTRB(20, 12, 14, 2),
                child: Row(
                  children: [
                    _pastilha(Icons.favorite_rounded, '${st.lives}', S.life),
                    const SizedBox(width: 18),
                    _pastilha(Icons.bolt_rounded, '${st.xp}', S.chart),
                    const SizedBox(width: 18),
                    _pastilha(Icons.local_fire_department_rounded,
                        '${st.streak}', S.gold),
                    const Spacer(),
                    // Toca no avatar para mudar de classe. Antes só se podia
                    // mudar reinstalando a app — um irmão mais novo não podia
                    // sequer experimentar.
                    _avatar(context, st),
                  ],
                ),
              ),
              const Expanded(child: MapScreen()),
            ],
          ),
        ),
      ),
    );
  }

  Widget _avatar(BuildContext context, AppState st) => InkWell(
        onTap: () => _abrirPerfil(context, st),
        borderRadius: BorderRadius.circular(28),
        child: Padding(
          padding: const EdgeInsets.all(6),
          child: Row(
            children: [
              CircleAvatar(
                radius: 18,
                backgroundColor: S.green500,
                child: Text(
                  st.nome.isEmpty ? '?' : st.nome.characters.first.toUpperCase(),
                  style: const TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.w700,
                      fontSize: 16),
                ),
              ),
              const Icon(Icons.expand_more_rounded, color: S.txSoft, size: 20),
            ],
          ),
        ),
      );

  Future<void> _abrirPerfil(BuildContext context, AppState st) async {
    final classes =
        st.conteudo.cursos.map((c) => c.classe).toSet().toList()..sort();

    await showModalBottomSheet<void>(
      context: context,
      backgroundColor: S.gm800,
      isScrollControlled: true,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(26)),
      ),
      builder: (ctx) => SafeArea(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(22, 14, 22, 22),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Center(
                child: Container(
                  width: 44,
                  height: 4,
                  decoration: BoxDecoration(
                    color: S.line,
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
              ),
              const SizedBox(height: 18),
              Text(
                st.nome.isEmpty ? 'Olá!' : 'Olá, ${st.nome}!',
                style: const TextStyle(
                    fontSize: 22, fontWeight: FontWeight.w700, color: S.tx),
              ),
              const SizedBox(height: 4),
              Text('${st.xp} XP · ${st.streak} dias seguidos',
                  style: const TextStyle(color: S.txSoft, fontSize: 14)),
              const SizedBox(height: 22),
              const Text('Em que classe estás?',
                  style: TextStyle(
                      fontSize: 15, fontWeight: FontWeight.w600, color: S.txSoft)),
              const SizedBox(height: 10),
              Flexible(
                child: SingleChildScrollView(
                  child: Column(
                    children: [
                      for (final c in classes)
                        Padding(
                          padding: const EdgeInsets.only(bottom: 8),
                          child: GestureDetector(
                            onTap: () {
                              st.mudarClasse(c);
                              Navigator.pop(ctx);
                            },
                            child: Container(
                              padding: const EdgeInsets.symmetric(
                                  horizontal: 16, vertical: 15),
                              decoration: BoxDecoration(
                                color: c == st.classe ? S.surface2 : S.surface,
                                border: Border.all(
                                    color: c == st.classe ? S.chart : S.line,
                                    width: 2),
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
                                    const Icon(Icons.check_rounded,
                                        color: S.chart, size: 22),
                                ],
                              ),
                            ),
                          ),
                        ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Future<bool> _confirmarSaida(BuildContext context) async {
    final sair = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        backgroundColor: S.gm800,
        title: const Text('Sair da Somara?', style: TextStyle(color: S.tx)),
        content: const Text('O teu progresso fica guardado.',
            style: TextStyle(color: S.txSoft)),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx, false),
            child: const Text('Ficar'),
          ),
          TextButton(
            onPressed: () => Navigator.pop(ctx, true),
            child: const Text('Sair', style: TextStyle(color: S.life)),
          ),
        ],
      ),
    );
    return sair ?? false;
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
