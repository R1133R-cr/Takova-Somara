import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import 'guardados_screen.dart';
import 'map_screen.dart';
import 'perfil_screen.dart';
import 'praticar_screen.dart';
import 'ranking_screen.dart';

/// Casca da app: barra de estado em cima, cinco separadores em baixo.
class HomeShell extends StatefulWidget {
  const HomeShell({super.key});
  @override
  State<HomeShell> createState() => _HomeShellState();
}

class _HomeShellState extends State<HomeShell> {
  int _aba = 0;

  static const _abas = [
    (icone: Icons.map_rounded, rotulo: 'Aprender'),
    (icone: Icons.fitness_center_rounded, rotulo: 'Praticar'),
    (icone: Icons.emoji_events_rounded, rotulo: 'Ranking'),
    (icone: Icons.bookmark_rounded, rotulo: 'Guardados'),
    (icone: Icons.person_rounded, rotulo: 'Perfil'),
  ];

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();

    return PopScope(
      // Estando fora do primeiro separador, voltar traz de volta a Aprender
      // em vez de fechar a app. Só no primeiro é que perguntamos se quer sair.
      canPop: false,
      onPopInvokedWithResult: (jaSaiu, _) async {
        if (jaSaiu) return;
        if (_aba != 0) {
          setState(() => _aba = 0);
          return;
        }
        if (await _confirmarSaida(context)) await SystemNavigator.pop();
      },
      child: Scaffold(
        backgroundColor: S.gm950,
        body: SafeArea(
          bottom: false,
          child: Column(
            children: [
              _barraEstado(st),
              Expanded(
                // IndexedStack e não troca de widget: assim a amarelinha
                // guarda a posição do scroll quando se vai a outro separador
                // e se volta. Reconstruir levaria a criança de volta ao fundo
                // do mapa de cada vez.
                child: IndexedStack(
                  index: _aba,
                  children: [
                    const MapScreen(),
                    const PraticarScreen(),
                    const RankingScreen(),
                    const GuardadosScreen(),
                    // Mudar de classe leva logo à amarelinha nova: é a
                    // consequência visível que faltava.
                    PerfilScreen(aoMudarClasse: () => setState(() => _aba = 0)),
                  ],
                ),
              ),
            ],
          ),
        ),
        bottomNavigationBar: _barraInferior(st),
      ),
    );
  }

  Widget _barraEstado(AppState st) => Padding(
        padding: const EdgeInsets.fromLTRB(20, 10, 20, 2),
        child: Row(
          children: [
            _pastilha(Icons.favorite_rounded, '${st.lives}', S.life),
            const SizedBox(width: 18),
            _pastilha(Icons.bolt_rounded, '${st.xp}', S.chart),
            const SizedBox(width: 18),
            _pastilha(
                Icons.local_fire_department_rounded, '${st.streak}', S.gold),
            const Spacer(),
            Text(st.classe,
                style: const TextStyle(color: S.txMut, fontSize: 13)),
          ],
        ),
      );

  Widget _barraInferior(AppState st) {
    final porRever = st.paraRever.length;
    return Container(
      decoration: const BoxDecoration(
        color: S.gm900,
        border: Border(top: BorderSide(color: S.line, width: 1.5)),
      ),
      child: SafeArea(
        top: false,
        child: SizedBox(
          height: 62,
          child: Row(
            children: [
              for (var i = 0; i < _abas.length; i++)
                Expanded(
                  child: InkWell(
                    onTap: () {
                      Sons.i.toque();
                      setState(() => _aba = i);
                    },
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        // O número de perguntas por rever fica à vista: sem
                        // isto, o separador Guardados nunca chamaria ninguém.
                        // O ícone escolhido dá um salto pequeno. Sem isto a
                        // troca de separador era um corte seco, e num ecrã
                        // que uma criança toca dezenas de vezes por sessão
                        // é o movimento que confirma que o toque valeu.
                        TweenAnimationBuilder<double>(
                          tween: Tween(begin: 1, end: i == _aba ? 1.16 : 1.0),
                          duration: const Duration(milliseconds: 260),
                          curve: SCurves.spring,
                          builder: (_, escala, filho) =>
                              Transform.scale(scale: escala, child: filho),
                          child: Badge(
                            isLabelVisible: i == 3 && porRever > 0,
                            label: Text('$porRever'),
                            backgroundColor: S.life,
                            child: Icon(
                              _abas[i].icone,
                              size: 23,
                              color: i == _aba ? S.chart : S.txMut,
                            ),
                          ),
                        ),
                        const SizedBox(height: 3),
                        Text(
                          _abas[i].rotulo,
                          style: TextStyle(
                            fontSize: 10.5,
                            fontWeight:
                                i == _aba ? FontWeight.w700 : FontWeight.w500,
                            color: i == _aba ? S.chart : S.txMut,
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
