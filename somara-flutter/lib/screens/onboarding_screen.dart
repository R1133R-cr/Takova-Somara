import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';
import 'home_shell.dart';

/// Duas perguntas apenas: quem és e que classe. Quanto menos fricção
/// antes do primeiro exercício, melhor — a app tem de provar o seu valor
/// nos primeiros trinta segundos.
class OnboardingScreen extends StatefulWidget {
  const OnboardingScreen({super.key});
  @override
  State<OnboardingScreen> createState() => _OnboardingScreenState();
}

class _OnboardingScreenState extends State<OnboardingScreen>
    with SingleTickerProviderStateMixin {
  final _nome = TextEditingController();
  String _classe = '1ª classe';
  int _passo = 0;
  late final AnimationController _ac;

  static const _classes = ['1ª classe', '2ª classe', '3ª classe'];

  @override
  void initState() {
    super.initState();
    _ac = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 380),
    )..forward();
  }

  @override
  void dispose() {
    _ac.dispose();
    _nome.dispose();
    super.dispose();
  }

  void _avancar() {
    if (_passo == 0) {
      setState(() => _passo = 1);
      _ac.forward(from: 0);
    } else {
      context.read<AppState>().concluirOnboarding(_nome.text.trim(), _classe);
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(builder: (_) => const HomeShell()),
      );
    }
  }

  bool get _podeAvancar => _passo == 0 ? _nome.text.trim().isNotEmpty : true;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: S.gm950,
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 10),
              ClipRRect(
                borderRadius: BorderRadius.circular(S.rPill),
                child: TweenAnimationBuilder<double>(
                  tween: Tween(begin: 0, end: (_passo + 1) / 2),
                  duration: const Duration(milliseconds: 420),
                  curve: SCurves.ease,
                  builder: (_, v, _) => LinearProgressIndicator(
                    value: v,
                    minHeight: 10,
                    backgroundColor: S.surface,
                    valueColor: const AlwaysStoppedAnimation(S.chart),
                  ),
                ),
              ),
              Expanded(
                child: AnimatedBuilder(
                  animation: _ac,
                  builder: (_, child) {
                    final e = SCurves.ease.transform(_ac.value);
                    return Transform.translate(
                      offset: Offset((1 - e) * 34, 0),
                      child: Opacity(opacity: e, child: child),
                    );
                  },
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const SizedBox(height: 26),
                      Image.asset(RobyPose.dica.path, width: 110),
                      const SizedBox(height: 18),
                      Text(
                        _passo == 0 ? 'Quem vai aprender?' : 'Em que classe estás?',
                        style: const TextStyle(
                            fontSize: 27, fontWeight: FontWeight.w700, color: S.tx),
                      ),
                      const SizedBox(height: 8),
                      Text(
                        _passo == 0
                            ? 'Diz o teu nome (ou o do teu educando).'
                            : 'Assim escolho os exercícios certos para ti.',
                        style: const TextStyle(color: S.txSoft, fontSize: 15),
                      ),
                      const SizedBox(height: 26),
                      if (_passo == 0)
                        TextField(
                          controller: _nome,
                          autofocus: true,
                          onChanged: (_) => setState(() {}),
                          style: const TextStyle(fontSize: 20, color: S.tx),
                          decoration: InputDecoration(
                            hintText: 'O teu nome',
                            hintStyle: const TextStyle(color: S.txMut),
                            filled: true,
                            fillColor: S.surface,
                            contentPadding: const EdgeInsets.symmetric(
                                horizontal: 18, vertical: 18),
                            enabledBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(S.rMd),
                              borderSide: const BorderSide(color: S.line, width: 2),
                            ),
                            focusedBorder: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(S.rMd),
                              borderSide: const BorderSide(color: S.chart, width: 2),
                            ),
                          ),
                        )
                      else
                        for (final c in _classes)
                          Padding(
                            padding: const EdgeInsets.only(bottom: 12),
                            child: GestureDetector(
                              onTap: () => setState(() => _classe = c),
                              child: AnimatedContainer(
                                duration: const Duration(milliseconds: 180),
                                padding: const EdgeInsets.symmetric(
                                    horizontal: 18, vertical: 18),
                                decoration: BoxDecoration(
                                  color: _classe == c ? S.surface2 : S.surface,
                                  border: Border.all(
                                      color: _classe == c ? S.chart : S.line,
                                      width: 2),
                                  borderRadius: BorderRadius.circular(S.rMd),
                                ),
                                child: Text(c,
                                    style: const TextStyle(
                                        fontSize: 17,
                                        fontWeight: FontWeight.w600,
                                        color: S.tx)),
                              ),
                            ),
                          ),
                    ],
                  ),
                ),
              ),
              GestureDetector(
                onTap: _podeAvancar ? _avancar : null,
                child: AnimatedOpacity(
                  opacity: _podeAvancar ? 1 : 0.45,
                  duration: const Duration(milliseconds: 180),
                  child: Container(
                    padding: const EdgeInsets.symmetric(vertical: 18),
                    decoration: BoxDecoration(
                      color: S.chart,
                      borderRadius: BorderRadius.circular(S.rPill),
                      boxShadow: const [
                        BoxShadow(color: S.chart600, offset: Offset(0, 5)),
                      ],
                    ),
                    alignment: Alignment.center,
                    child: const Text('Continuar',
                        style: TextStyle(
                            fontSize: 18,
                            fontWeight: FontWeight.w700,
                            color: S.onChart)),
                  ),
                ),
              ),
              const SizedBox(height: 26),
            ],
          ),
        ),
      ),
    );
  }
}
