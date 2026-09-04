import 'dart:async';
import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import '../models/escadaria.dart';
import '../models/frascos.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/mesa_de_frascos.dart';
import '../widgets/roby.dart';

/// «Water R Sort»: arrumar os líquidos até cada frasco ter uma cor só.
///
/// É o único joguinho que não ensina matéria nenhuma, e isso é deliberado.
/// O que treina é planear com antecedência: uma jogada que resolve agora
/// pode fechar a única saída daqui a três, e a criança tem de ver isso
/// antes de tocar. É a mesma cabeça que a conta de dividir pede, sem ser
/// uma conta de dividir.
class FrascosScreen extends StatefulWidget {
  /// Por onde começar. Nulo entra pelo degrau guardado no estado.
  final int? nivel;

  const FrascosScreen({super.key, this.nivel});

  @override
  State<FrascosScreen> createState() => _FrascosScreenState();
}

class _FrascosScreenState extends State<FrascosScreen>
    with SingleTickerProviderStateMixin {
  late Frascos _jogo;
  late int _nivel;

  /// O frasco levantado à espera de destino.
  int? _seleccionado;

  /// As mesas anteriores, para o Desfazer. Guarda-se a mesa inteira e não a
  /// jogada: são meia dúzia de listas curtas, e desfazer passa a ser voltar
  /// atrás em vez de calcular o contrário de um despejo.
  final _historico = <Frascos>[];

  int _jogadas = 0;

  /// Verdadeiro entre ganhar e o degrau seguinte entrar.
  bool _aPassar = false;

  late final AnimationController _anim;

  /// O despejo a decorrer, sem o tempo — o tempo vem de [_anim].
  ({int de, int para, int quantos, CorDoLiquido cor})? _emCurso;

  @override
  void initState() {
    super.initState();
    _anim = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 460),
    );
    Sons.i.definirAmbiente(Trilha.relaxar);
    _nivel = widget.nivel ?? context.read<AppState>().nivelDe(Jogo.frascos);
    _montarNivel();
  }

  @override
  void dispose() {
    _anim.dispose();
    Sons.i.definirAmbiente(Trilha.principal);
    super.dispose();
  }

  void _montarNivel() {
    _jogo = Frascos.doNivel(_nivel);
    _historico.clear();
    _seleccionado = null;
    _emCurso = null;
    _jogadas = 0;
    _aPassar = false;
  }

  /// Empancado: ainda não ganhou e já não há jogada nenhuma.
  bool get _preso => !_jogo.ganho && !_jogo.temJogada;

  bool get _ocupado => _emCurso != null || _aPassar;

  void _tocar(int i) {
    if (_ocupado || _jogo.ganho) return;

    final escolhido = _seleccionado;
    if (escolhido == null) {
      // Levantar um frasco vazio não leva a lado nenhum.
      if (_jogo.frascos[i].vazio) return;
      Sons.i.toque();
      setState(() => _seleccionado = i);
      return;
    }

    if (escolhido == i) {
      Sons.i.toque();
      setState(() => _seleccionado = null);
      return;
    }

    if (_jogo.podeDespejar(escolhido, i)) {
      unawaited(_despejar(escolhido, i));
      return;
    }

    // Não dava. Em vez de não fazer nada — que a criança lê como o jogo
    // estar avariado — passa-se a escolha para o frasco em que ela tocou.
    Sons.i.errado();
    setState(() => _seleccionado = _jogo.frascos[i].vazio ? null : i);
  }

  Future<void> _despejar(int de, int para) async {
    final quantos = _jogo.quantosDespeja(de, para);
    final cor = _jogo.frascos[de].topo!;

    _historico.add(_jogo);
    setState(() {
      _emCurso = (de: de, para: para, quantos: quantos, cor: cor);
      _seleccionado = null;
    });

    Sons.i.toque();
    await _anim.forward(from: 0);
    if (!mounted) return;

    final depois = _jogo.despejar(de, para);
    setState(() {
      _jogo = depois;
      _emCurso = null;
      _jogadas++;
    });

    final destino = depois.frascos[para];
    if (destino.cheio && destino.deUmaCor) {
      Sons.i.certo();
      HapticFeedback.lightImpact();
    }

    if (depois.ganho) {
      Sons.i.nivel();
      // Arrumar uma cor vale como uma resposta certa de lição.
      context.read<AppState>().concluirTreino(depois.params.cores);
      unawaited(_passarAoSeguinte());
    }
  }

  Future<void> _passarAoSeguinte() async {
    setState(() => _aPassar = true);
    await Future<void>.delayed(const Duration(milliseconds: 1600));
    if (!mounted) return;
    _nivel = context.read<AppState>().subirNivelDe(Jogo.frascos);
    setState(_montarNivel);
  }

  void _desfazer() {
    if (_ocupado || _historico.isEmpty) return;
    Sons.i.toque();
    setState(() {
      _jogo = _historico.removeLast();
      _seleccionado = null;
      _jogadas = math.max(0, _jogadas - 1);
    });
  }

  /// Volta ao tabuleiro com que ela começou. É o mesmo porque o nível é
  /// determinista — ver [Frascos.doNivel].
  void _recomecar() {
    if (_ocupado) return;
    Sons.i.toque();
    setState(_montarNivel);
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
          'Water R Sort · Nível $_nivel',
          style: const TextStyle(fontSize: 16),
        ),
      ),
      body: SafeArea(
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16),
              child: Text(
                _dizer(),
                textAlign: TextAlign.center,
                style: TextStyle(
                  color: _jogo.ganho
                      ? S.chart
                      : (_preso ? S.gold : S.txSoft),
                  fontSize: 14.5,
                  fontWeight:
                      _jogo.ganho || _preso ? FontWeight.w700 : FontWeight.w400,
                  height: 1.3,
                ),
              ),
            ),
            const SizedBox(height: 6),
            Expanded(
              child: Padding(
                padding: const EdgeInsets.fromLTRB(10, 4, 10, 4),
                child: AnimatedBuilder(
                  animation: _anim,
                  builder: (context, _) {
                    final c = _emCurso;
                    return MesaDeFrascos(
                      jogo: _jogo,
                      seleccionado: _seleccionado,
                      despejo: c == null
                          ? null
                          : (
                              de: c.de,
                              para: c.para,
                              quantos: c.quantos,
                              cor: c.cor,
                              t: _anim.value,
                            ),
                      aoTocar: _tocar,
                    );
                  },
                ),
              ),
            ),
            if (_jogo.ganho) _fim() else _rodape(),
          ],
        ),
      ),
    );
  }

  String _dizer() {
    if (_jogo.ganho) {
      return 'Arrumado! ${contagemDeJogadas(_jogadas)}.';
    }
    if (_preso) {
      return 'Já não há jogada possível. Desfaz a última, ou recomeça o '
          'nível.';
    }
    if (_seleccionado != null) {
      return 'Agora toca no frasco para onde queres despejar.';
    }
    return 'Deixa cada frasco com uma cor só. Só se despeja para um frasco '
        'vazio ou para a mesma cor.';
  }

  Widget _rodape() => Padding(
    padding: const EdgeInsets.fromLTRB(14, 4, 14, 12),
    child: Column(
      children: [
        Text(
          'Cores arrumadas: ${_jogo.coresFeitas} de ${_jogo.params.cores}'
          '${_jogadas > 0 ? "  ·  ${contagemDeJogadas(_jogadas)}" : ""}',
          textAlign: TextAlign.center,
          style: const TextStyle(color: S.txSoft, fontSize: 13),
        ),
        const SizedBox(height: 8),
        Row(
          children: [
            Expanded(
              child: _botao(
                'Desfazer',
                Icons.undo_rounded,
                _historico.isEmpty ? null : _desfazer,
              ),
            ),
            const SizedBox(width: 10),
            Expanded(
              child: _botao(
                'Recomeçar',
                Icons.refresh_rounded,
                _jogadas == 0 && _historico.isEmpty ? null : _recomecar,
              ),
            ),
          ],
        ),
      ],
    ),
  );

  /// Um botão do rodapé. Apagado quando não há nada a fazer com ele — um
  /// Desfazer que não desfaz nada mente à criança sobre o que aconteceu.
  Widget _botao(String texto, IconData icone, VoidCallback? aoTocar) {
    final vivo = aoTocar != null;
    return GestureDetector(
      onTap: aoTocar,
      child: Opacity(
        opacity: vivo ? 1 : 0.35,
        child: Container(
          height: 46,
          decoration: BoxDecoration(
            color: S.gm900,
            border: Border.all(color: S.line, width: 2),
            borderRadius: BorderRadius.circular(S.rPill),
          ),
          alignment: Alignment.center,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(icone, color: S.chart, size: 18),
              const SizedBox(width: 7),
              // Flexível porque com o texto do sistema aumentado "Recomeçar"
              // cresce e sairia pela borda curva da pílula fora.
              Flexible(
                child: Text(
                  texto,
                  overflow: TextOverflow.ellipsis,
                  style: const TextStyle(
                    color: S.chart,
                    fontSize: 14.5,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _fim() => Padding(
    padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
    child: Column(
      children: [
        Image.asset(RobyPose.orgulhoso.path, width: 72),
        const SizedBox(height: 6),
        Text(
          'Nível $_nivel feito!',
          style: const TextStyle(
            fontSize: 18,
            fontWeight: FontWeight.w700,
            color: S.chart,
          ),
        ),
        const SizedBox(height: 3),
        Text(
          _nivel >= nivelMaximo
              ? 'Chegaste ao fim da escadaria.'
              : 'Vem aí o ${_nivel + 1}…',
          style: const TextStyle(color: S.txSoft, fontSize: 13.5),
        ),
      ],
    ),
  );
}

/// «1 jogada» e «7 jogadas». O singular importa: a app fala português a
/// crianças que estão a aprender a escrevê-lo.
String contagemDeJogadas(int n) => n == 1 ? '1 jogada' : '$n jogadas';
