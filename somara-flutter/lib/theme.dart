import 'package:flutter/material.dart';

/// Paleta da Somara — Gun Metal (tela escura) + Verde Niassa (percurso)
/// + Chartreuse (néon de energia). Transposta da versão web para manter
/// a marca idêntica entre as duas.
class S {
  // Gun Metal — tela escura
  static const gm950 = Color(0xFF00181C);
  static const gm900 = Color(0xFF00272C); // fundo principal
  static const gm800 = Color(0xFF05323A);
  static const surface = Color(0xFF06343B);
  static const surface2 = Color(0xFF0A4048);
  static const line = Color(0xFF14535D);

  // Verde Niassa — percurso / primário
  static const green700 = Color(0xFF1A6B45);
  static const green600 = Color(0xFF237A4E);
  static const green500 = Color(0xFF2E8B57);
  static const green400 = Color(0xFF4DA378);
  static const green300 = Color(0xFF86C4A2);

  // Chartreuse — néon de energia
  static const chart = Color(0xFFE1FF51);
  static const chart600 = Color(0xFFB6D92F); // aresta 3D
  static const chartDim = Color(0xFFC7E64A);
  static const onChart = Color(0xFF00272C);

  // Estados
  static const life = Color(0xFFFF5D5D);
  static const lifeDim = Color(0xFF7A2F33);
  static const wrong = Color(0xFFFF5D5D);
  static const gold = Color(0xFFECC658);

  // Texto sobre escuro
  static const tx = Color(0xFFEAF5EF);
  static const txSoft = Color(0xFFA9C4BB);
  static const txMut = Color(0xFF6F8F86);

  // Raios
  static const rSm = 10.0;
  static const rMd = 16.0;
  static const rLg = 22.0;
  static const rPill = 999.0;
}

/// Curvas de animação da casa. `spring` reproduz o
/// cubic-bezier(.34,1.56,.64,1) da versão web — passa do alvo e volta,
/// que é o que dá a sensação de "vivo" em vez de mecânico.
class SCurves {
  static const spring = Cubic(0.34, 1.56, 0.64, 1.0);
  static const ease = Cubic(0.4, 0.0, 0.2, 1.0);
  static const easeOutBack = Cubic(0.175, 0.885, 0.32, 1.275);
  /// Queda acelerada — usada na aterragem do Roby.
  static const gravity = Cubic(0.55, 0.055, 0.675, 0.19);
}

ThemeData somaraTheme() {
  final base = ThemeData.dark(useMaterial3: true);
  return base.copyWith(
    scaffoldBackgroundColor: S.gm950,
    colorScheme: base.colorScheme.copyWith(
      primary: S.chart,
      onPrimary: S.onChart,
      secondary: S.green500,
      surface: S.surface,
      error: S.life,
    ),
    textTheme: base.textTheme.apply(
      bodyColor: S.tx,
      displayColor: S.tx,
      fontFamily: 'Roboto',
    ),
    splashFactory: InkRipple.splashFactory,
  );
}
