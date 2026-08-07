import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import 'state/app_state.dart';
import 'theme.dart';
import 'screens/welcome_screen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
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

/// Segura o ecrã enquanto o conteúdo e o progresso carregam. É rápido,
/// mas sem isto a primeira frame apanharia o estado ainda vazio.
class _Arranque extends StatelessWidget {
  const _Arranque();

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    if (!st.pronto) {
      return const Scaffold(
        backgroundColor: S.gm950,
        body: Center(
          child: SizedBox(
            width: 34,
            height: 34,
            child: CircularProgressIndicator(color: S.chart, strokeWidth: 3),
          ),
        ),
      );
    }
    return const WelcomeScreen();
  }
}
