import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import 'modo_teste.dart';
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
        title: ModoTeste.activo ? 'Somara TESTE' : 'Somara',
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
    // Antes de tudo: uma versão de testes velha não abre. Ver o porquê em
    // `lib/modo_teste.dart`.
    if (ModoTeste.caducou()) return const _Caducou();
    final st = context.watch<AppState>();
    if (!st.pronto) {
      return const Carregando(mensagem: 'A preparar as tuas lições...');
    }
    return const WelcomeScreen();
  }
}

/// O que se vê quando a versão de testes passou da validade.
///
/// Diz o que fazer, e não só que não dá. Quem tem este ficheiro recebeu-o de
/// alguém, e a frase tem de servir para essa pessoa pedir a versão nova.
class _Caducou extends StatelessWidget {
  const _Caducou();

  @override
  Widget build(BuildContext context) => Scaffold(
    backgroundColor: S.gm950,
    body: Center(
      child: Padding(
        padding: const EdgeInsets.all(32),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.hourglass_disabled_rounded,
                color: S.life, size: 64),
            const SizedBox(height: 20),
            const Text(
              'Esta versão de testes caducou',
              textAlign: TextAlign.center,
              style: TextStyle(
                color: S.tx,
                fontSize: 21,
                fontWeight: FontWeight.w700,
              ),
            ),
            const SizedBox(height: 12),
            Text(
              'Foi compilada em ${ModoTeste.compiladaEm} e só serve durante '
              '${ModoTeste.validade.inDays} dias. Peça a versão nova a quem '
              'lhe deu esta.',
              textAlign: TextAlign.center,
              style: const TextStyle(color: S.txSoft, fontSize: 15, height: 1.5),
            ),
            const SizedBox(height: 20),
            const Text(
              'A Somara a sério está na loja e não caduca.',
              textAlign: TextAlign.center,
              style: TextStyle(color: S.txMut, fontSize: 13),
            ),
          ],
        ),
      ),
    ),
  );
}
