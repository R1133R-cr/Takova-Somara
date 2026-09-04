import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';

/// Ecrã de nível concluído. A festa é curta de propósito — o objectivo é
/// recompensar e devolver a criança ao mapa, não prender-lhe a atenção.
class CompleteScreen extends StatefulWidget {
  /// Índice do nível concluído, ou -1 numa sessão de treino/revisão.
  final int indice;
  final int acertos;
  final int total;

  /// Legenda a mostrar quando não há nível nenhum (sessão avulsa).
  final String? titulo;

  const CompleteScreen({
    super.key,
    required this.indice,
    required this.acertos,
    required this.total,
    this.titulo,
  });

  @override
  State<CompleteScreen> createState() => _CompleteScreenState();
}

class _CompleteScreenState extends State<CompleteScreen>
    with TickerProviderStateMixin {
  late final AnimationController _festa;
  late final AnimationController _entrada;
  late final List<_Particula> _particulas;

  @override
  void initState() {
    super.initState();
    Sons.i.nivel();
    final rnd = math.Random();
    _particulas = List.generate(46, (i) => _Particula.aleatoria(rnd, i));
    _festa = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 2600),
    )..forward();
    _entrada = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 620),
    )..forward();
  }

  @override
  void dispose() {
    _festa.dispose();
    _entrada.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final st = context.read<AppState>();
    final pct = widget.total == 0
        ? 0
        : (widget.acertos * 100 / widget.total).round();
    final avulsa = widget.indice < 0;
    final xpGanho = widget.acertos * AppState.xpPorAcerto +
        (avulsa ? 0 : AppState.xpPorNivel);
    // Numa sessão avulsa não há nível nenhum para nomear — procurar um pelo
    // índice -1 rebentaria o ecrã logo a seguir a a criança acertar tudo.
    final legenda = avulsa
        ? (widget.titulo ?? 'Treino')
        : '${st.niveis[widget.indice].unit.titulo} · '
            '${st.niveis[widget.indice].nivel.titulo}';

    return Scaffold(
      backgroundColor: S.gm950,
      body: Stack(
        children: [
          Positioned.fill(
            child: AnimatedBuilder(
              animation: _festa,
              builder: (_, _) => CustomPaint(
                painter: _ConfettiPainter(_particulas, _festa.value),
              ),
            ),
          ),
          SafeArea(
            child: AnimatedBuilder(
              animation: _entrada,
              builder: (_, child) {
                final e = SCurves.spring.transform(_entrada.value.clamp(0.0, 1.0));
                return Opacity(
                  opacity: _entrada.value.clamp(0.0, 1.0),
                  child: Transform.scale(scale: 0.85 + 0.15 * e, child: child),
                );
              },
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: 24),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Container(
                      width: 168,
                      height: 168,
                      decoration: BoxDecoration(
                        color: const Color(0xFFF3EFE3),
                        borderRadius: BorderRadius.circular(28),
                        boxShadow: const [
                          BoxShadow(color: Color(0x33E1FF51), blurRadius: 0, spreadRadius: 4),
                          BoxShadow(color: Color(0x80000000), blurRadius: 40, offset: Offset(0, 18)),
                        ],
                      ),
                      clipBehavior: Clip.antiAlias,
                      // A cara que a criança comprou aparece aqui, no melhor
                      // momento que a app tem para lha mostrar. As poses de
                      // corpo inteiro entram inteiras (`contain`); os bustos
                      // quadrados enchem a caixa como sempre encheram.
                      child: RobyImagem(
                        st.robyEscolhido == RobyPose.token
                            ? RobyPose.graduate
                            : st.robyEscolhido,
                        largura: 168,
                        fit: st.robyEscolhido.retrato
                            ? BoxFit.contain
                            : BoxFit.cover,
                        alinhamento: Alignment.topCenter,
                      ),
                    ),
                    const SizedBox(height: 26),
                    Text(avulsa ? 'Treino terminado!' : 'Nível concluído!',
                        style: const TextStyle(
                            fontSize: 30, fontWeight: FontWeight.w700, color: S.tx)),
                    const SizedBox(height: 8),
                    Text(legenda,
                        textAlign: TextAlign.center,
                        style: const TextStyle(color: S.txSoft, fontSize: 15)),
                    const SizedBox(height: 30),
                    Row(
                      children: [
                        Expanded(child: _cartao('+$xpGanho', 'XP ganho', S.chart)),
                        const SizedBox(width: 14),
                        Expanded(child: _cartao('$pct%', 'Acertos', S.green300)),
                      ],
                    ),
                    const SizedBox(height: 34),
                    SizedBox(
                      width: double.infinity,
                      child: GestureDetector(
                        onTap: () => Navigator.of(context).pop(),
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
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _cartao(String valor, String rotulo, Color cor) => Container(
        padding: const EdgeInsets.symmetric(vertical: 18),
        decoration: BoxDecoration(
          color: S.surface,
          borderRadius: BorderRadius.circular(S.rLg),
          border: Border.all(color: S.line, width: 2),
        ),
        child: Column(
          children: [
            Text(valor,
                style: TextStyle(
                    fontSize: 26, fontWeight: FontWeight.w700, color: cor)),
            const SizedBox(height: 4),
            Text(rotulo, style: const TextStyle(color: S.txSoft, fontSize: 12)),
          ],
        ),
      );
}

class _Particula {
  final double x, largura, altura, atraso, rodaVel, deriva;
  final Color cor;
  const _Particula(this.x, this.largura, this.altura, this.atraso, this.rodaVel,
      this.deriva, this.cor);

  factory _Particula.aleatoria(math.Random r, int i) {
    const cores = [S.chart, S.green400, S.gold, Colors.white, S.green300];
    return _Particula(
      r.nextDouble(),
      5 + r.nextDouble() * 7,
      9 + r.nextDouble() * 12,
      r.nextDouble() * 0.35,
      (r.nextDouble() - 0.5) * 9,
      (r.nextDouble() - 0.5) * 0.22,
      cores[i % cores.length],
    );
  }
}

class _ConfettiPainter extends CustomPainter {
  final List<_Particula> ps;
  final double t;
  _ConfettiPainter(this.ps, this.t);

  @override
  void paint(Canvas canvas, Size size) {
    for (final p in ps) {
      final tp = ((t - p.atraso) / (1 - p.atraso)).clamp(0.0, 1.0);
      if (tp <= 0) continue;
      // Cai a acelerar e desvanece no último terço.
      final y = -40 + tp * tp * (size.height + 80);
      final x = (p.x + p.deriva * tp) * size.width;
      final op = tp > 0.7 ? (1 - (tp - 0.7) / 0.3) : 1.0;

      canvas.save();
      canvas.translate(x, y);
      canvas.rotate(tp * p.rodaVel);
      canvas.drawRRect(
        RRect.fromRectAndRadius(
          Rect.fromCenter(center: Offset.zero, width: p.largura, height: p.altura),
          const Radius.circular(2),
        ),
        Paint()..color = p.cor.withValues(alpha: op.clamp(0.0, 1.0)),
      );
      canvas.restore();
    }
  }

  @override
  bool shouldRepaint(_ConfettiPainter old) => old.t != t;
}
