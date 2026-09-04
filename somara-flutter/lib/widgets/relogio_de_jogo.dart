import 'dart:async';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../models/bolsa_de_tempo.dart';
import '../state/app_state.dart';
import '../theme.dart';

/// Envolve um joguinho e conta o tempo que ele gasta da bolsa.
///
/// Está aqui e não dentro de cada jogo por uma razão estrutural: os quatro
/// jogos abrem todos pelo mesmo botão do ecrã dos Joguinhos, e envolvê-los
/// nesse único sítio torna impossível acrescentar um quinto jogo que não
/// conte tempo. Espalhado por quatro `initState`, o quinto ficaria de fora
/// e ninguém dava por isso.
///
/// O aviso só aparece no último minuto. Antes disso não há relógio nenhum à
/// vista: uma criança a olhar para uma contagem decrescente não está a
/// jogar, está a ver o tempo acabar.
class RelogioDeJogo extends StatefulWidget {
  final Widget child;
  const RelogioDeJogo({super.key, required this.child});

  /// A partir de quando é que o aviso aparece.
  static const avisarAos = Duration(minutes: 1);

  @override
  State<RelogioDeJogo> createState() => _RelogioDeJogoState();
}

class _RelogioDeJogoState extends State<RelogioDeJogo> {
  late AppState _st;
  Timer? _tique;

  Duration _falta = Duration.zero;
  bool _acabou = false;

  @override
  void initState() {
    super.initState();
    _st = context.read<AppState>();
    _st.entrarNoJogo();
    _falta = _st.tempoDeJogo;
    _tique = Timer.periodic(const Duration(seconds: 1), _bater);
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    _st = context.read<AppState>();
  }

  @override
  void dispose() {
    _tique?.cancel();
    // Num microtask e não já: o `dispose` corre dentro da construção da
    // árvore, e avisar os ouvintes aí dá o erro de "markNeedsBuild durante
    // build". O microtask corre logo a seguir, ainda antes do fotograma
    // seguinte, e a conta do tempo fecha na mesma.
    final st = _st;
    scheduleMicrotask(st.sairDoJogo);
    super.dispose();
  }

  void _bater(Timer _) {
    if (!mounted || _acabou) return;
    final falta = _st.tempoDeJogo;
    if (falta <= Duration.zero) {
      unawaited(_fechar());
      return;
    }
    final mostrava = _falta <= RelogioDeJogo.avisarAos;
    final mostra = falta <= RelogioDeJogo.avisarAos;
    _falta = falta;
    // Só se reconstrói quando o aviso está (ou passa a estar) à vista. Fora
    // disso, um `setState` por segundo era trabalho para não mudar nada.
    if (mostra || mostrava) setState(() {});
  }

  /// O tempo acabou. Diz-se porquê antes de fechar.
  ///
  /// Um jogo que desaparece sem explicação lê-se como avaria. Um segundo e
  /// meio com a razão escrita é a diferença entre "acabou o meu tempo" e "a
  /// app estragou-se".
  Future<void> _fechar() async {
    _tique?.cancel();
    setState(() {
      _acabou = true;
      _falta = Duration.zero;
    });
    await Future<void>.delayed(const Duration(milliseconds: 1500));
    if (!mounted) return;
    await Navigator.of(context).maybePop();
  }

  @override
  Widget build(BuildContext context) {
    final mostrar = _acabou || _falta <= RelogioDeJogo.avisarAos;
    return Stack(
      children: [
        widget.child,
        if (mostrar)
          Positioned(
            top: 0,
            left: 0,
            right: 0,
            child: SafeArea(
              child: Center(
                child: Padding(
                  padding: const EdgeInsets.only(top: 8),
                  child: _aviso(),
                ),
              ),
            ),
          ),
      ],
    );
  }

  Widget _aviso() => Container(
    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 7),
    decoration: BoxDecoration(
      color: _acabou ? S.life : S.gold,
      borderRadius: BorderRadius.circular(S.rPill),
      border: Border.all(color: S.line, width: 1.5),
    ),
    child: Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Icon(
          _acabou ? Icons.hourglass_bottom_rounded : Icons.timer_rounded,
          size: 17,
          color: _acabou ? Colors.white : S.gm950,
        ),
        const SizedBox(width: 6),
        Text(
          _acabou ? 'Acabou o tempo de jogo' : quantoFalta(_falta),
          style: TextStyle(
            fontSize: 13.5,
            fontWeight: FontWeight.w700,
            color: _acabou ? Colors.white : S.gm950,
          ),
        ),
      ],
    ),
  );
}
