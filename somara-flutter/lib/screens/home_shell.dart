import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';
import 'guardados_screen.dart';
import 'joguinhos_screen.dart';
import 'map_screen.dart';
import 'perfil_screen.dart';
import 'praticar_screen.dart';
import 'ranking_screen.dart';

/// Casca da app: barra de estado em cima, seis separadores em baixo.
class HomeShell extends StatefulWidget {
  const HomeShell({super.key});
  @override
  State<HomeShell> createState() => _HomeShellState();
}

class _HomeShellState extends State<HomeShell> {
  int _aba = 0;

  /// Os separadores. O `roby` substitui o ícone quando existe: a sala dos
  /// joguinhos é a única parte da app que não é escola, e um rosto no meio
  /// de cinco ícones de traço diz isso sem precisar de o escrever.
  static const _abas = [
    (icone: Icons.map_rounded, rotulo: 'Aprender', roby: null),
    (icone: Icons.fitness_center_rounded, rotulo: 'Praticar', roby: null),
    (icone: Icons.videogame_asset_rounded, rotulo: 'Joguinhos',
        roby: RobyPose.rindo),
    (icone: Icons.emoji_events_rounded, rotulo: 'Ranking', roby: null),
    (icone: Icons.bookmark_rounded, rotulo: 'Guardados', roby: null),
    (icone: Icons.person_rounded, rotulo: 'Perfil', roby: null),
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
                    const JoguinhosScreen(),
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
            // O altifalante cortado só aparece quando o som está desligado,
            // e é o que faltava: a app calada não dava sinal nenhum de que
            // estava calada de propósito. Toca-se aqui para o devolver, sem
            // ter de ir ao Perfil procurá-lo.
            if (!st.som)
              GestureDetector(
                onTap: () => st.definirSom(true),
                child: const Padding(
                  padding: EdgeInsets.only(right: 12),
                  child: Icon(Icons.volume_off_rounded,
                      color: S.gold, size: 19),
                ),
              ),
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
          height: 64,
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
                            isLabelVisible:
                                _abas[i].rotulo == 'Guardados' && porRever > 0,
                            label: Text('$porRever'),
                            backgroundColor: S.life,
                            child: _simbolo(i),
                          ),
                        ),
                        const SizedBox(height: 3),
                        Text(
                          _abas[i].rotulo,
                          style: TextStyle(
                            fontSize: 9.8,
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

  /// O símbolo do separador: o rosto do Roby onde há um, o ícone de traço
  /// nos outros.
  ///
  /// Fora do separador escolhido o rosto fica esbatido e sem cor, para não
  /// gritar mais alto que os ícones ao lado — a barra tem de se ler como um
  /// conjunto, não como cinco ícones e um autocolante.
  Widget _simbolo(int i) {
    final pose = _abas[i].roby;
    final escolhido = i == _aba;
    if (pose == null) {
      return Icon(
        _abas[i].icone,
        size: 23,
        color: escolhido ? S.chart : S.txMut,
      );
    }
    return Opacity(
      opacity: escolhido ? 1 : 0.5,
      child: Container(
        width: 25,
        height: 25,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          border: Border.all(
            color: escolhido ? S.chart : S.txMut,
            width: 1.6,
          ),
        ),
        child: ClipOval(
          child: ColorFiltered(
            colorFilter: escolhido
                ? const ColorFilter.mode(Colors.transparent, BlendMode.dst)
                : const ColorFilter.matrix(<double>[
                    0.2126, 0.7152, 0.0722, 0, 0,
                    0.2126, 0.7152, 0.0722, 0, 0,
                    0.2126, 0.7152, 0.0722, 0, 0,
                    0, 0, 0, 1, 0,
                  ]),
            child: Image.asset(
              pose.path,
              fit: BoxFit.cover,
              alignment: Alignment.topCenter,
            ),
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
