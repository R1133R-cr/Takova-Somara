import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import 'services/nuvem.dart';
import 'services/sons.dart';
import 'state/app_state.dart';
import 'theme.dart';
import 'widgets/carregando.dart';
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

class _ArranqueState extends State<_Arranque> with WidgetsBindingObserver {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState estado) {
    switch (estado) {
      case AppLifecycleState.resumed:
        Sons.i.emPrimeiroPlano();

      // `inactive` é transitório e a app continua à vista: a sombra do
      // multitarefas, a barra de notificações a descer meio dedo, um
      // aviso de chamada. Calar a música aqui foi o que a matou — ficava
      // em pausa e o `resumed` que a devolvia nem sempre chegava.
      case AppLifecycleState.inactive:
        break;

      case AppLifecycleState.paused:
      case AppLifecycleState.hidden:
      case AppLifecycleState.detached:
        Sons.i.emSegundoPlano();
    }
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
