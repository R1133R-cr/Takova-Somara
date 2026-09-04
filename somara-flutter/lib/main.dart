import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import 'services/ciclo_de_vida.dart';
import 'services/nuvem.dart';
import 'services/sons.dart';
import 'state/app_state.dart';
import 'theme.dart';
import 'widgets/carregando.dart';
import 'widgets/faixa_conquista.dart';
import 'screens/welcome_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  // Antes do runApp para a app já saber, na primeira frame, se há sessão
  // aberta. Não vai à rede: só arranca o SDK, e devolve logo se a consola
  // ainda não estiver configurada.
  await Nuvem.i.arrancar();
  // Antes de qualquer som: define o foco de áudio para os nossos efeitos
  // não calarem a nossa própria música.
  await Sons.i.arrancar();
  // App para crianças: só retrato, para o tabuleiro nunca ficar deitado.
  SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
  ]);
  SystemChrome.setSystemUIOverlayStyle(const SystemUiOverlayStyle(
    statusBarColor: Colors.transparent,
    statusBarIconBrightness: Brightness.light,
  ));
  runApp(const SomaraApp());
}

class SomaraApp extends StatelessWidget {
  const SomaraApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => AppState()..carregar(),
      child: MaterialApp(
        title: 'Somara',
        debugShowCheckedModeBanner: false,
        theme: somaraTheme(),
        // A faixa das conquistas vive AQUI, por cima do Navigator, e não
        // dentro de um ecrã: metida num ecrã não aparecia nas lições nem nos
        // joguinhos, que é justamente onde as conquistas se ganham.
        builder: (_, filho) => FaixaDeConquistas(child: filho!),
        home: const _Arranque(),
      ),
    );
  }
}

/// Segura o ecrã enquanto o conteúdo e o progresso carregam, e cala a
/// trilha quando a app vai para segundo plano.
///
/// O silêncio em segundo plano não é um pormenor: o telemóvel é da família,
/// e música a sair de uma app fechada é o tipo de coisa que faz um pai
/// desinstalá-la.
class _Arranque extends StatefulWidget {
  const _Arranque();

  @override
  State<_Arranque> createState() => _ArranqueState();
}

class _ArranqueState extends State<_Arranque> {
  late final CicloDeVida _ciclo;

  @override
  void initState() {
    super.initState();
    _ciclo = CicloDeVida(context.read<AppState>());
    WidgetsBinding.instance.addObserver(_ciclo);
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(_ciclo);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    if (!st.pronto) {
      return const Carregando(mensagem: 'A preparar as tuas lições...');
    }
    return const WelcomeScreen();
  }
}
