import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';
import 'onboarding_screen.dart';
import 'home_shell.dart';

class WelcomeScreen extends StatefulWidget {
  const WelcomeScreen({super.key});
  @override
  State<WelcomeScreen> createState() => _WelcomeScreenState();
}

class _WelcomeScreenState extends State<WelcomeScreen>
    with TickerProviderStateMixin {
  late final AnimationController _flutua;
  late final AnimationController _entrada;

  @override
  void initState() {
    super.initState();
    _flutua = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 3000),
    )..repeat(reverse: true);
    _entrada = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 700),
    )..forward();
  }

  @override
  void dispose() {
    _flutua.dispose();
    _entrada.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          gradient: RadialGradient(
            center: Alignment(0, -0.35),
            radius: 1.1,
            colors: [S.gm800, S.gm950],
          ),
        ),
        child: SafeArea(
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 28),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Spacer(),
                AnimatedBuilder(
                  animation: Listenable.merge([_flutua, _entrada]),
                  builder: (_, child) {
                    final e = SCurves.spring.transform(_entrada.value.clamp(0.0, 1.0));
                    final f = Curves.easeInOut.transform(_flutua.value);
                    return Transform.translate(
                      offset: Offset(0, -f * 12 + (1 - e) * 30),
                      child: Transform.scale(scale: 0.9 + 0.1 * e, child: child),
                    );
                  },
                  child: Image.asset(RobyPose.hero.path, width: 230),
                ),
                const SizedBox(height: 20),
                const Text('SOMARA',
                    style: TextStyle(
                      fontSize: 46,
                      fontWeight: FontWeight.w400,
                      color: S.tx,
                      letterSpacing: 3,
                      fontFamily: 'Melfira',
                    )),
                const SizedBox(height: 10),
                const Text('APRENDE · CRESCE · BRILHA',
                    style: TextStyle(
                      color: S.chart,
                      fontWeight: FontWeight.w700,
                      fontSize: 14,
                      letterSpacing: 1.6,
                    )),
                const SizedBox(height: 22),
                const Text(
                  'Sou o Roby! Vamos aprender matemática e português, '
                  'nível a nível, como uma amarelinha.',
                  textAlign: TextAlign.center,
                  style: TextStyle(color: S.txSoft, fontSize: 16, height: 1.5),
                ),
                const Spacer(),
                SizedBox(
                  width: double.infinity,
                  child: GestureDetector(
                    onTap: () => Navigator.of(context).pushReplacement(
                      MaterialPageRoute(
                        builder: (_) => st.onboarded
                            ? const HomeShell()
                            : const OnboardingScreen(),
                      ),
                    ),
                    child: Container(
                      padding: const EdgeInsets.symmetric(vertical: 19),
                      decoration: BoxDecoration(
                        color: S.chart,
                        borderRadius: BorderRadius.circular(S.rPill),
                        boxShadow: const [
                          BoxShadow(color: S.chart600, offset: Offset(0, 5)),
                        ],
                      ),
                      alignment: Alignment.center,
                      child: Text(
                        st.onboarded ? 'Continuar' : 'Começar',
                        style: const TextStyle(
                            fontSize: 19,
                            fontWeight: FontWeight.w700,
                            color: S.onChart),
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 28),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
