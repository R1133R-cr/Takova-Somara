import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme.dart';

/// As poses disponíveis do Roby (ficheiros em assets/img/).
enum RobyPose {
  token('roby-token'),
  hero('roby-hero'),
  dica('roby-dica'),
  feliz('roby-feliz'),
  rindo('roby-rindo'),
  empolgado('roby-empolgado'),
  orgulhoso('roby-orgulhoso'),
  triste('roby-triste'),
  confuso('roby-confuso'),
  confiante('roby-confiante'),
  curioso('roby-curioso'),
  graduate('roby-graduate');

  final String file;
  const RobyPose(this.file);
  String get path => 'assets/img/$file.png';
}

/// O Roby como peça viva do tabuleiro.
///
/// Anima entre posições com física de salto real, em vez do keyframe CSS
/// que a versão web usava. Um salto de verdade tem quatro momentos, e é a
/// presença deles que faz o boneco parecer vivo em vez de deslizar:
///
///   1. antecipação — agacha-se antes de saltar (squash)
///   2. impulso     — estica-se ao descolar (stretch)
///   3. arco        — trajectória parabólica, não linha recta
///   4. aterragem   — esmaga ao bater no chão e recupera com mola
///
/// Parado, respira devagar — nunca fica completamente estático.
class RobyToken extends StatefulWidget {
  /// Centro do quadrado onde o Roby está pousado, em coordenadas do stack pai.
  final Offset position;
  final double size;
  final RobyPose pose;

  /// Disparado quando a aterragem acontece — para sincronizar som/háptica.
  final VoidCallback? onLand;

  const RobyToken({
    super.key,
    required this.position,
    this.size = 58,
    this.pose = RobyPose.token,
    this.onLand,
  });

  @override
  State<RobyToken> createState() => _RobyTokenState();
}

class _RobyTokenState extends State<RobyToken> with TickerProviderStateMixin {
  late final AnimationController _hop;
  late final AnimationController _breathe;

  late Offset _from;
  late Offset _to;
  bool _landed = false;

  /// Altura do arco do salto, em píxeis.
  static const _arcHeight = 64.0;

  @override
  void initState() {
    super.initState();
    _from = widget.position;
    _to = widget.position;

    _hop = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 620),
    )..addListener(_checkLanding);

    _breathe = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 3200),
    )..repeat(reverse: true);
  }

  void _checkLanding() {
    // A aterragem dá-se aos 78% — quando os pés tocam o chão, não no fim
    // da animação (o resto é a mola a assentar).
    if (!_landed && _hop.value >= 0.78) {
      _landed = true;
      widget.onLand?.call();
    }
  }

  @override
  void didUpdateWidget(RobyToken old) {
    super.didUpdateWidget(old);
    if (widget.position != old.position) {
      _from = _currentPos();
      _to = widget.position;
      _landed = false;
      _hop.forward(from: 0);
    }
  }

  Offset _currentPos() {
    if (!_hop.isAnimating) return _to;
    return _lerpArc(_hop.value).$1;
  }

  /// Devolve (posição, alturaDoArco) para um dado t.
  (Offset, double) _lerpArc(double t) {
    // O deslocamento horizontal usa uma curva suave; o vertical é a
    // parábola 4h·t·(1−t), que pica exactamente a meio do percurso.
    final ht = SCurves.ease.transform(t.clamp(0.0, 1.0));
    final base = Offset.lerp(_from, _to, ht)!;
    final arc = 4 * _arcHeight * t * (1 - t);
    return (base, arc);
  }

  /// Squash & stretch ao longo do salto. Os valores estão em pares
  /// (escalaX, escalaY) e conservam grosso modo o volume — esticar em
  /// altura afina a largura, que é o que o olho espera ver.
  (double, double) _squash(double t) {
    if (t < 0.14) {
      // antecipação: agacha
      final k = t / 0.14;
      return (_lerp(1.0, 1.18, k), _lerp(1.0, 0.78, k));
    } else if (t < 0.30) {
      // impulso: estica ao descolar
      final k = (t - 0.14) / 0.16;
      return (_lerp(1.18, 0.86, k), _lerp(0.78, 1.24, k));
    } else if (t < 0.68) {
      // no ar: volta ao normal
      final k = (t - 0.30) / 0.38;
      return (_lerp(0.86, 1.0, k), _lerp(1.24, 1.0, k));
    } else if (t < 0.78) {
      // queda: estica para baixo
      final k = (t - 0.68) / 0.10;
      return (_lerp(1.0, 0.90, k), _lerp(1.0, 1.16, k));
    } else if (t < 0.88) {
      // impacto: esmaga
      final k = (t - 0.78) / 0.10;
      return (_lerp(0.90, 1.28, k), _lerp(1.16, 0.72, k));
    } else {
      // mola de recuperação
      final k = (t - 0.88) / 0.12;
      final e = SCurves.spring.transform(k.clamp(0.0, 1.0));
      return (_lerp(1.28, 1.0, e), _lerp(0.72, 1.0, e));
    }
  }

  static double _lerp(double a, double b, double t) => a + (b - a) * t;

  @override
  void dispose() {
    _hop.removeListener(_checkLanding);
    _hop.dispose();
    _breathe.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: Listenable.merge([_hop, _breathe]),
      builder: (context, _) {
        final t = _hop.isAnimating ? _hop.value : 1.0;
        final (pos, arc) = _hop.isAnimating ? _lerpArc(t) : (_to, 0.0);
        final (sx, sy) = _hop.isAnimating ? _squash(t) : (1.0, 1.0);

        // Respiração: sobe e desce 3px, e incha 1.5% — subtil de propósito,
        // se for muito visível distrai da lição.
        final breath = math.sin(_breathe.value * math.pi);
        final idleY = _hop.isAnimating ? 0.0 : -breath * 3.0;
        final idleScale = _hop.isAnimating ? 1.0 : 1.0 + breath * 0.015;

        // Inclina-se ligeiramente na direcção do salto.
        final dx = _to.dx - _from.dx;
        final tilt = _hop.isAnimating
            ? (dx.sign * 0.14 * math.sin(t * math.pi))
            : 0.0;

        final h = widget.size * 1.45;

        return Positioned(
          left: pos.dx - widget.size / 2,
          top: pos.dy - h + 14 - arc + idleY,
          width: widget.size,
          height: h,
          child: IgnorePointer(
            child: Transform(
              alignment: Alignment.bottomCenter,
              transform: Matrix4.identity()
                ..rotateZ(tilt)
                ..scaleByDouble(sx * idleScale, sy * idleScale, 1.0, 1.0),
              child: Stack(
                alignment: Alignment.bottomCenter,
                children: [
                  // Sombra no chão — encolhe e desvanece quando ele sobe,
                  // que é o que dá a leitura de altura.
                  Positioned(
                    bottom: 0,
                    child: Opacity(
                      opacity: (1 - arc / _arcHeight * 0.75).clamp(0.25, 1.0),
                      child: Container(
                        width: widget.size * (0.55 - arc / _arcHeight * 0.2),
                        height: 8,
                        decoration: const BoxDecoration(
                          shape: BoxShape.circle,
                          color: Color(0x66000000),
                        ),
                      ),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(bottom: 4),
                    child: Image.asset(
                      widget.pose.path,
                      fit: BoxFit.contain,
                    ),
                  ),
                ],
              ),
            ),
          ),
        );
      },
    );
  }
}
