import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../models/pomar.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';

/// O Pomar: juntar três ou mais do mesmo produto.
///
/// As peças são manga, banana, coco, milho, tomate e amendoim — o que se vê
/// no mercado, não os rebuçados coloridos do costume. Sem ensinar nada de
/// propósito, o jogo nomeia as coisas do dia-a-dia da criança.
///
/// Não gasta corações e não faz avançar a amarelinha. É para brincar.
class PomarScreen extends StatefulWidget {
  const PomarScreen({super.key});

  @override
  State<PomarScreen> createState() => _PomarScreenState();
}

class _PomarScreenState extends State<PomarScreen>
    with SingleTickerProviderStateMixin {
  static const _jogadas = 20;

  final _rnd = Random();
  late final AnimationController _abanao;

  late Pomar _tabuleiro;
  int _pontos = 0;
  int _restam = _jogadas;
  int? _escolhida;

  /// As casas a desaparecer neste instante, para se ver a colheita.
  Set<int> _aColher = const {};

  /// Enquanto a cascata corre, o tabuleiro não aceita toques.
  bool _ocupado = false;

  /// Mensagem passageira: baralhámos, fim de jogo, e afins.
  String? _aviso;

  @override
  void initState() {
    super.initState();
    _abanao = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 380),
    );
    _tabuleiro = Pomar.novo(rnd: _rnd);
  }

  @override
  void dispose() {
    _abanao.dispose();
    super.dispose();
  }

  bool get _acabou => _restam <= 0;

  Future<void> _tocarEm(int i) async {
    if (_ocupado || _acabou) return;

    final anterior = _escolhida;
    if (anterior == null) {
      Sons.i.toque();
      setState(() => _escolhida = i);
      return;
    }
    if (anterior == i) {
      setState(() => _escolhida = null);
      return;
    }

    // Tocar numa casa distante muda a escolha em vez de recusar. Uma criança
    // que muda de ideias não devia ter de desmarcar primeiro.
    if (!_tabuleiro.saoVizinhas(anterior, i)) {
      Sons.i.toque();
      setState(() => _escolhida = i);
      return;
    }

    if (!_tabuleiro.podeTrocar(anterior, i)) {
      // Troca que não forma nada: abana e não gasta jogada. Gastar uma
      // jogada por uma tentativa que o jogo recusa seria injusto.
      Sons.i.errado();
      HapticFeedback.heavyImpact();
      _abanao.forward(from: 0);
      setState(() => _escolhida = null);
      return;
    }

    setState(() {
      _escolhida = null;
      _ocupado = true;
      _restam--;
      _tabuleiro = _tabuleiro.trocaCrua(anterior, i);
    });
    await _resolverCascata();
  }

  /// Colhe, deixa cair, enche — e repete enquanto for formando trios.
  Future<void> _resolverCascata() async {
    var multiplicador = 1;
    while (mounted) {
      final grupos = _tabuleiro.grupos();
      if (grupos.isEmpty) break;

      Sons.i.certo();
      HapticFeedback.lightImpact();
      setState(() => _aColher = grupos);
      await Future.delayed(const Duration(milliseconds: 220));
      if (!mounted) return;

      setState(() {
        _pontos += Pomar.pontosDe(grupos.length) * multiplicador;
        _aColher = const {};
        _tabuleiro = _tabuleiro.colher(grupos).assentar();
      });
      await Future.delayed(const Duration(milliseconds: 170));
      if (!mounted) return;

      setState(() => _tabuleiro = _tabuleiro.encher(_rnd));
      await Future.delayed(const Duration(milliseconds: 120));
      if (!mounted) return;

      // Cada cascata seguida vale mais, até um tecto. Sem tecto, uma
      // cascata feliz dava mil pontos numa jogada e as outras dezanove
      // deixavam de contar.
      if (multiplicador < 4) multiplicador++;
    }

    if (!mounted) return;

    // Tabuleiro sem saída: remexe-se em vez de acabar a partida por azar.
    if (!_tabuleiro.haJogada()) {
      setState(() {
        _tabuleiro = _tabuleiro.baralhar(_rnd);
        _aviso = 'Não havia jogadas. Baralhámos as peças.';
      });
      Timer(const Duration(seconds: 3), () {
        if (mounted) setState(() => _aviso = null);
      });
    }

    setState(() => _ocupado = false);

    if (_acabou) {
      Sons.i.nivel();
      // Os pontos valem XP, com um travão: quinhentos pontos por cada
      // acerto de lição, e nunca mais de oito. Jogar não pode render mais
      // depressa do que estudar — e o travão tem de estar longe do alcance
      // de uma jogada só, senão as outras dezanove não valem nada.
      final ganho = (_pontos / 500).floor().clamp(0, 8);
      if (ganho > 0 && mounted) {
        context.read<AppState>().concluirTreino(ganho);
      }
    }
  }

  void _recomecar() {
    Sons.i.toque();
    setState(() {
      _tabuleiro = Pomar.novo(rnd: _rnd);
      _pontos = 0;
      _restam = _jogadas;
      _escolhida = null;
      _aColher = const {};
      _ocupado = false;
      _aviso = null;
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
        title: const Text('Pomar', style: TextStyle(fontSize: 17)),
      ),
      body: SafeArea(
        child: Column(
          children: [
            _placar(),
            if (_aviso != null)
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: Text(
                  _aviso!,
                  textAlign: TextAlign.center,
                  style: const TextStyle(color: S.gold, fontSize: 13.5),
                ),
              ),
            Expanded(
              child: Center(
                child: Padding(
                  padding: const EdgeInsets.all(10),
                  child: AnimatedBuilder(
                    animation: _abanao,
                    builder: (_, filho) {
                      final t = _abanao.value;
                      final dx = t == 0
                          ? 0.0
                          : (1 - t) * 9 * (t * 24 % 2 < 1 ? 1 : -1);
                      return Transform.translate(
                        offset: Offset(dx, 0),
                        child: filho,
                      );
                    },
                    child: _grelha(),
                  ),
                ),
              ),
            ),
            if (_acabou) _fim() else _rodape(),
          ],
        ),
      ),
    );
  }

  Widget _placar() => Padding(
    padding: const EdgeInsets.fromLTRB(20, 0, 20, 10),
    child: Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        _numero('$_pontos', 'pontos', S.chart),
        _numero('$_restam', _restam == 1 ? 'jogada' : 'jogadas',
            _restam <= 3 ? S.life : S.gold),
      ],
    ),
  );

  Widget _numero(String v, String rotulo, Color cor) => Column(
    crossAxisAlignment: CrossAxisAlignment.start,
    children: [
      Text(v,
          style: TextStyle(
              color: cor, fontSize: 26, fontWeight: FontWeight.w800)),
      Text(rotulo, style: const TextStyle(color: S.txMut, fontSize: 12)),
    ],
  );

  Widget _grelha() => LayoutBuilder(
    builder: (context, box) {
      final lado = min(
        box.maxWidth / _tabuleiro.colunas,
        box.maxHeight / _tabuleiro.linhas,
      );
      return SizedBox(
        width: lado * _tabuleiro.colunas,
        height: lado * _tabuleiro.linhas,
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            for (var l = 0; l < _tabuleiro.linhas; l++)
              Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  for (var c = 0; c < _tabuleiro.colunas; c++)
                    _casa(_tabuleiro.indice(l, c), lado),
                ],
              ),
          ],
        ),
      );
    },
  );

  Widget _casa(int i, double lado) {
    final produto = _tabuleiro.casas[i];
    final escolhida = _escolhida == i;
    final aColher = _aColher.contains(i);

    return GestureDetector(
      onTap: () => _tocarEm(i),
      child: Container(
        width: lado,
        height: lado,
        padding: const EdgeInsets.all(2.5),
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 160),
          decoration: BoxDecoration(
            color: escolhida
                ? S.chart.withValues(alpha: 0.24)
                : S.surface.withValues(alpha: 0.55),
            border: Border.all(
              color: escolhida ? S.chart : S.line,
              width: escolhida ? 2.5 : 1.2,
            ),
            borderRadius: BorderRadius.circular(S.rMd),
          ),
          alignment: Alignment.center,
          child: AnimatedScale(
            // A peça colhida encolhe até desaparecer: sem isto, as peças
            // trocavam de sítio de repente e não se percebia o que tinha
            // acontecido.
            scale: aColher ? 0.1 : 1,
            duration: const Duration(milliseconds: 210),
            curve: Curves.easeInBack,
            child: Text(
              produto?.emoji ?? '',
              style: TextStyle(fontSize: lado * 0.52),
            ),
          ),
        ),
      ),
    );
  }

  Widget _rodape() => const Padding(
    padding: EdgeInsets.fromLTRB(20, 4, 20, 16),
    child: Text(
      'Toca em duas peças vizinhas para as trocar. Três iguais em linha '
      'colhem-se.',
      textAlign: TextAlign.center,
      style: TextStyle(color: S.txSoft, fontSize: 13, height: 1.35),
    ),
  );

  Widget _fim() => Padding(
    padding: const EdgeInsets.fromLTRB(20, 0, 20, 18),
    child: Column(
      children: [
        Image.asset(RobyPose.orgulhoso.path, width: 84),
        const SizedBox(height: 8),
        Text(
          'Fizeste $_pontos pontos!',
          style: const TextStyle(
            color: S.chart,
            fontSize: 18,
            fontWeight: FontWeight.w700,
          ),
        ),
        const SizedBox(height: 12),
        Row(
          children: [
            Expanded(
              child: _botao('Sair', () => Navigator.of(context).pop(),
                  cor: S.surface, corTexto: S.txSoft),
            ),
            const SizedBox(width: 10),
            Expanded(
              flex: 2,
              child: _botao('Jogar outra vez', _recomecar,
                  cor: S.chart, corTexto: S.onChart),
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
      height: 50,
      decoration: BoxDecoration(
        color: cor,
        border: Border.all(color: S.line, width: 1.5),
        borderRadius: BorderRadius.circular(S.rMd),
      ),
      alignment: Alignment.center,
      child: Text(
        texto,
        style: TextStyle(
          fontSize: 17,
          fontWeight: FontWeight.w700,
          color: corTexto,
        ),
      ),
    ),
  );
}
