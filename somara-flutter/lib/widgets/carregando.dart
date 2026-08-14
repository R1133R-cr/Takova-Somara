import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme.dart';
import 'roby.dart';

/// O ecrã de espera das coisas demoradas: arrancar, descarregar conteúdo
/// novo, mudar de classe.
///
/// Antes era uma roda cinzenta a girar. Numa app para crianças isso não diz
/// nada — e o arranque, num telemóvel barato, chega a demorar uns segundos
/// bem contados. O Roby a saltar diz "está a trabalhar, não está avariado",
/// que é a única coisa que uma espera precisa de comunicar.
class Carregando extends StatefulWidget {
  /// O que se está a fazer, em linguagem de criança. Sem isto fica só o
  /// boneco a saltar e ninguém sabe ao que espera.
  final String mensagem;

  const Carregando({super.key, this.mensagem = 'Um instante...'});

  @override
  State<Carregando> createState() => _CarregandoState();
}

class _CarregandoState extends State<Carregando>
    with SingleTickerProviderStateMixin {
  late final AnimationController _salto;

  @override
  void initState() {
    super.initState();
    _salto = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 900),
    )..repeat();
  }

  @override
  void dispose() {
    _salto.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: S.gm950,
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            AnimatedBuilder(
              animation: _salto,
              builder: (_, child) {
                final t = _salto.value;
                // Parábola: sobe e volta, com o pico a meio do ciclo.
                final altura = 4 * 26 * t * (1 - t);
                // Esmaga ao tocar no chão, estica no ar — sem isto o boneco
                // parece uma imagem a deslizar para cima e para baixo.
                final k = math.sin(t * math.pi);
                return Transform.translate(
                  offset: Offset(0, -altura),
                  child: Transform.scale(
                    scaleX: 1 + 0.10 * (1 - k) - 0.05 * k,
                    scaleY: 1 - 0.10 * (1 - k) + 0.05 * k,
                    alignment: Alignment.bottomCenter,
                    child: child,
                  ),
                );
              },
              child: Image.asset(RobyPose.salto.path, width: 118),
            ),
            const SizedBox(height: 10),
            // A sombra fica no chão enquanto ele sobe — é ela que dá a
            // leitura de altura ao salto.
            AnimatedBuilder(
              animation: _salto,
              builder: (_, _) {
                final k = math.sin(_salto.value * math.pi);
                return Opacity(
                  opacity: 0.30 - 0.18 * k,
                  child: Container(
                    width: 62 - 18 * k,
                    height: 8,
                    decoration: const BoxDecoration(
                      borderRadius: BorderRadius.all(Radius.elliptical(31, 4)),
                      color: Colors.black,
                    ),
                  ),
                );
              },
            ),
            const SizedBox(height: 26),
            Text(
              widget.mensagem,
              textAlign: TextAlign.center,
              style: const TextStyle(color: S.txSoft, fontSize: 15.5),
            ),
          ],
        ),
      ),
    );
  }
}
