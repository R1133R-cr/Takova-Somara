import 'dart:async';
import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import '../models/conquista.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import 'roby.dart';

/// A faixa que anuncia uma conquista.
///
/// Desliza de cima, fica uns segundos e sai sozinha. **Nunca pede «OK»** e
/// nunca pára o que está a acontecer por baixo: a criança pode continuar a
/// responder à pergunta enquanto a faixa passa. É a diferença entre uma
/// festa e uma interrupção — e um `AlertDialog` a meio de uma lição é, sem
/// excepção, uma interrupção.
///
/// Vive **por cima do Navigator**, envolvida no `builder` do `MaterialApp`.
/// Metida dentro de um ecrã, não apareceria nas lições nem nos joguinhos,
/// que é justamente onde as conquistas se ganham.
class FaixaDeConquistas extends StatefulWidget {
  final Widget child;
  const FaixaDeConquistas({super.key, required this.child});

  /// Quanto tempo fica à vista depois de entrar.
  static const paragem = Duration(milliseconds: 2600);

  /// Uma letra de cada vez, na palavra CONQUISTA.
  static const porLetra = Duration(milliseconds: 40);

  @override
  State<FaixaDeConquistas> createState() => _FaixaDeConquistasState();
}

class _FaixaDeConquistasState extends State<FaixaDeConquistas>
    with SingleTickerProviderStateMixin {
  static const _palavra = 'CONQUISTA';

  late final AnimationController _entrada;
  AppState? _st;

  Conquista? _aMostrar;
  int _letras = 0;
  Timer? _maquina;

  @override
  void initState() {
    super.initState();
    _entrada = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 520),
      reverseDuration: const Duration(milliseconds: 380),
    );
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final novo = context.read<AppState>();
    if (identical(novo, _st)) return;
    _st?.removeListener(_verFila);
    _st = novo..addListener(_verFila);
    _verFila();
  }

  @override
  void dispose() {
    _maquina?.cancel();
    _st?.removeListener(_verFila);
    _entrada.dispose();
    super.dispose();
  }

  void _verFila() {
    if (!mounted || _aMostrar != null) return;
    if (_st?.proximaConquista == null) return;
    unawaited(_mostrar());
  }

  Future<void> _mostrar() async {
    final c = _st?.tirarConquista();
    if (c == null) return;

    setState(() {
      _aMostrar = c;
      _letras = 0;
    });

    Sons.i.conquista();
    HapticFeedback.mediumImpact();

    await _entrada.forward(from: 0);
    if (!mounted) return;

    // A palavra escreve-se letra a letra. É o pormenor que faz isto ler-se
    // como um anúncio e não como um aviso do sistema.
    _maquina = Timer.periodic(FaixaDeConquistas.porLetra, (t) {
      if (!mounted) return t.cancel();
      if (_letras >= _palavra.length) return t.cancel();
      setState(() => _letras++);
    });

    await Future<void>.delayed(FaixaDeConquistas.paragem);
    if (!mounted) return;
    _maquina?.cancel();

    await _entrada.reverse();
    if (!mounted) return;
    setState(() => _aMostrar = null);

    // A seguinte, se a houver: fechar uma unidade pode fechar a disciplina
    // e a classe no mesmo toque.
    _verFila();
  }

  @override
  Widget build(BuildContext context) {
    final c = _aMostrar;
    return Stack(
      children: [
        widget.child,
        if (c != null)
          // `IgnorePointer` é o que cumpre a promessa: a lição não pára, e
          // um toque atrás da faixa continua a chegar ao botão que lá está.
          Positioned(
            top: 0,
            left: 0,
            right: 0,
            child: IgnorePointer(
              child: AnimatedBuilder(
                animation: _entrada,
                builder: (_, filho) {
                  final t = Curves.easeOutBack.transform(
                    _entrada.value.clamp(0.0, 1.0),
                  );
                  return Transform.translate(
                    offset: Offset(0, (t - 1) * 240),
                    child: Opacity(
                      opacity: _entrada.value.clamp(0.0, 1.0),
                      child: filho,
                    ),
                  );
                },
                child: _faixa(context, c),
              ),
            ),
          ),
      ],
    );
  }

  Widget _faixa(BuildContext context, Conquista c) {
    // Um terço do ecrã, com tecto: num tablet um terço de mil pixéis seria
    // um cartaz.
    final altura = math.min(MediaQuery.sizeOf(context).height / 3, 200.0);

    return Material(
      type: MaterialType.transparency,
      child: Container(
        constraints: BoxConstraints(minHeight: altura),
        decoration: BoxDecoration(
          color: S.gm900,
          border: const Border(
            bottom: BorderSide(color: S.gold, width: 3),
          ),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withValues(alpha: 0.55),
              blurRadius: 26,
              offset: const Offset(0, 10),
            ),
          ],
        ),
        child: SafeArea(
          bottom: false,
          child: Padding(
            padding: const EdgeInsets.fromLTRB(16, 12, 16, 16),
            child: Row(
              children: [
                SizedBox(
                  width: 84,
                  height: 84,
                  child: RobyImagem(
                    RobyPose.conquista,
                    largura: 84,
                    alinhamento: Alignment.topCenter,
                  ),
                ),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        _palavra.substring(0, _letras),
                        style: const TextStyle(
                          color: S.gold,
                          fontSize: 15,
                          fontWeight: FontWeight.w800,
                          letterSpacing: 4.5,
                        ),
                      ),
                      const SizedBox(height: 6),
                      Text(
                        c.titulo,
                        style: const TextStyle(
                          color: S.tx,
                          fontSize: 19,
                          fontWeight: FontWeight.w700,
                          height: 1.2,
                        ),
                      ),
                      if (c.cristais > 0) ...[
                        const SizedBox(height: 8),
                        Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            const Icon(
                              Icons.diamond_rounded,
                              color: S.chart,
                              size: 17,
                            ),
                            const SizedBox(width: 5),
                            Text(
                              '+${c.cristais} CC',
                              style: const TextStyle(
                                color: S.chart,
                                fontSize: 15,
                                fontWeight: FontWeight.w700,
                              ),
                            ),
                          ],
                        ),
                      ],
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
