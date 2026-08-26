import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../models/memoria.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';

/// Jogo da memória com pares que ensinam.
///
/// Virar duas cartas iguais treina memória e mais nada. Aqui o par nunca é
/// igual a si mesmo: `7` casa com sete maçãs, `3 + 4` casa com `7`, `MANGA`
/// casa com 🥭. É associação, não decoração — e é o que a amarelinha treina
/// mal.
class MemoriaScreen extends StatefulWidget {
  final Baralho baralho;
  const MemoriaScreen({super.key, required this.baralho});

  @override
  State<MemoriaScreen> createState() => _MemoriaScreenState();
}

class _MemoriaScreenState extends State<MemoriaScreen> {
  final _rnd = Random();

  late JogoDaMemoria _jogo;

  /// Índices virados neste momento (no máximo dois).
  final _viradas = <int>[];

  /// Índices já ganhos, que ficam à vista.
  final _ganhas = <int>{};

  int _tentativas = 0;
  bool _ocupado = false;

  @override
  void initState() {
    super.initState();
    Sons.i.definirAmbiente(Trilha.relaxar);
    _novo();
  }

  @override
  void dispose() {
    Sons.i.definirAmbiente(Trilha.principal);
    super.dispose();
  }

  void _novo() {
    _jogo = JogoDaMemoria.novo(baralho: widget.baralho, pares: 6, rnd: _rnd);
    _viradas.clear();
    _ganhas.clear();
    _tentativas = 0;
    _ocupado = false;
    setState(() {});
  }

  bool get _acabou => _ganhas.length == _jogo.cartas.length;

  Future<void> _virar(int i) async {
    if (_ocupado || _acabou) return;
    if (_ganhas.contains(i) || _viradas.contains(i)) return;

    Sons.i.toque();
    setState(() => _viradas.add(i));
    if (_viradas.length < 2) return;

    _ocupado = true;
    _tentativas++;
    final a = _viradas[0], b = _viradas[1];

    if (_jogo.cartas[a].par == _jogo.cartas[b].par) {
      Sons.i.certo();
      HapticFeedback.lightImpact();
      setState(() {
        _ganhas.addAll([a, b]);
        _viradas.clear();
        _ocupado = false;
      });
      if (_acabou) {
        Sons.i.nivel();
        // Um par vale como uma resposta certa de lição.
        context.read<AppState>().concluirTreino(_jogo.pares);
      }
      return;
    }

    // Não casaram: ficam à vista um instante antes de voltarem. Sem essa
    // pausa a criança não chega a ver o que virou, e o jogo passa a ser
    // sorte em vez de memória.
    Sons.i.errado();
    await Future.delayed(const Duration(milliseconds: 850));
    if (!mounted) return;
    setState(() {
      _viradas.clear();
      _ocupado = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: S.gm950,
      appBar: AppBar(
        backgroundColor: S.gm950,
        foregroundColor: S.tx,
        elevation: 0,
        title: Text(
          'Memória · ${widget.baralho.rotulo}',
          style: const TextStyle(fontSize: 16),
        ),
      ),
      body: SafeArea(
        child: Column(
          children: [
            Text(
              _acabou
                  ? 'Todos os pares! $_tentativas tentativas.'
                  : widget.baralho.explica,
              textAlign: TextAlign.center,
              style: TextStyle(
                color: _acabou ? S.chart : S.txSoft,
                fontSize: 14.5,
                fontWeight: _acabou ? FontWeight.w700 : FontWeight.w400,
              ),
            ),
            const SizedBox(height: 10),
            Expanded(
              child: Center(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 14),
                  child: _tabuleiro(),
                ),
              ),
            ),
            if (_acabou) _fim() else _rodape(),
          ],
        ),
      ),
    );
  }

  Widget _tabuleiro() => LayoutBuilder(
    builder: (context, box) {
      final colunas = _jogo.colunas;
      final linhas = (_jogo.cartas.length / colunas).ceil();
      final lado = min(box.maxWidth / colunas, box.maxHeight / linhas);
      return SizedBox(
        width: lado * colunas,
        height: lado * linhas,
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            for (var l = 0; l < linhas; l++)
              Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  for (var c = 0; c < colunas; c++)
                    if (l * colunas + c < _jogo.cartas.length)
                      _carta(l * colunas + c, lado),
                ],
              ),
          ],
        ),
      );
    },
  );

  Widget _carta(int i, double lado) {
    final carta = _jogo.cartas[i];
    final ganha = _ganhas.contains(i);
    final aberta = ganha || _viradas.contains(i);

    return GestureDetector(
      onTap: () => _virar(i),
      child: Container(
        width: lado,
        height: lado,
        padding: const EdgeInsets.all(4),
        // Roda meia volta ao virar: sem isso a face aparecia de repente e
        // não se percebia que era a mesma carta.
        child: TweenAnimationBuilder<double>(
          tween: Tween(begin: 0, end: aberta ? 1 : 0),
          duration: const Duration(milliseconds: 260),
          curve: Curves.easeOut,
          builder: (_, t, _) => Transform(
            alignment: Alignment.center,
            transform: Matrix4.identity()..rotateY(t * pi),
            child: t < 0.5 ? _costas(lado) : _face(carta, ganha, lado),
          ),
        ),
      ),
    );
  }

  Widget _costas(double lado) => Container(
    decoration: BoxDecoration(
      color: S.surface,
      border: Border.all(color: S.line, width: 2),
      borderRadius: BorderRadius.circular(S.rMd),
    ),
    alignment: Alignment.center,
    child: Icon(
      Icons.question_mark_rounded,
      color: S.txMut,
      size: lado * 0.3,
    ),
  );

  Widget _face(Carta carta, bool ganha, double lado) => Transform(
    // A carta rodou meia volta; sem esta contra-rotação o texto ficava
    // ao espelho.
    alignment: Alignment.center,
    transform: Matrix4.identity()..rotateY(pi),
    child: Container(
      decoration: BoxDecoration(
        color: ganha
            ? S.green500.withValues(alpha: 0.35)
            : S.chart.withValues(alpha: 0.16),
        border: Border.all(color: ganha ? S.green300 : S.chart, width: 2),
        borderRadius: BorderRadius.circular(S.rMd),
      ),
      alignment: Alignment.center,
      padding: const EdgeInsets.all(4),
      child: FittedBox(
        child: Text(
          // Os desenhos repetidos quebram em linhas, senão sete maçãs não
          // cabiam na largura de uma carta.
          carta.eDesenho ? _emLinhas(carta.face) : carta.face,
          textAlign: TextAlign.center,
          style: TextStyle(
            fontSize: carta.eDesenho ? 18 : 22,
            fontWeight: FontWeight.w800,
            color: ganha ? Colors.white : S.tx,
            height: 1.1,
          ),
        ),
      ),
    ),
  );

  /// Parte uma fila de emoji em linhas de três.
  static String _emLinhas(String face) {
    final partes = face.runes.map(String.fromCharCode).toList();
    final linhas = <String>[];
    for (var i = 0; i < partes.length; i += 3) {
      linhas.add(partes.skip(i).take(3).join());
    }
    return linhas.join('\n');
  }

  Widget _rodape() => Padding(
    padding: const EdgeInsets.fromLTRB(20, 6, 20, 14),
    child: Text(
      'Pares certos: ${_ganhas.length ~/ 2} de ${_jogo.pares}'
      '${_tentativas > 0 ? "  ·  $_tentativas tentativas" : ""}',
      textAlign: TextAlign.center,
      style: const TextStyle(color: S.txSoft, fontSize: 13.5),
    ),
  );

  Widget _fim() => Padding(
    padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
    child: Column(
      children: [
        Image.asset(RobyPose.orgulhoso.path, width: 76),
        const SizedBox(height: 10),
        Row(
          children: [
            Expanded(
              child: _botao('Sair', () => Navigator.of(context).pop(),
                  cor: S.surface, corTexto: S.txSoft),
            ),
            const SizedBox(width: 10),
            Expanded(
              flex: 2,
              child: _botao('Outra vez', () {
                Sons.i.toque();
                _novo();
              }, cor: S.chart, corTexto: S.onChart),
            ),
          ],
        ),
      ],
    ),
  );

  Widget _botao(
    String texto,
    VoidCallback aoTocar, {
    required Color cor,
    required Color corTexto,
  }) => GestureDetector(
    onTap: aoTocar,
    child: Container(
      height: 48,
      decoration: BoxDecoration(
        color: cor,
        border: Border.all(color: S.line, width: 1.5),
        borderRadius: BorderRadius.circular(S.rMd),
      ),
      alignment: Alignment.center,
      child: Text(
        texto,
        style: TextStyle(
          fontSize: 16.5,
          fontWeight: FontWeight.w700,
          color: corTexto,
        ),
      ),
    ),
  );
}
