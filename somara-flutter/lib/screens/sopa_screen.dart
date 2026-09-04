import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../models/escadaria.dart';
import '../models/sopa.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';

/// Sopa de letras.
///
/// Arrasta-se por cima das letras, como no Pomar — o mesmo gesto nos dois
/// jogos, para a criança não ter de aprender duas maneiras de mexer.
///
/// Não gasta corações e não faz avançar a amarelinha. Mas treina uma coisa
/// que a amarelinha treina pouco: reconhecer a palavra inteira de relance,
/// em vez de a soletrar. É disso que se faz a leitura fluente.
class SopaScreen extends StatefulWidget {
  /// Por onde começar. Nulo entra pelo degrau guardado no estado — que é o
  /// caso normal; o número serve para os testes e para reabrir um nível.
  final int? nivel;

  /// Só para os testes: fixa o sorteio, para o teste poder saber onde as
  /// palavras ficaram e arrastar por cima delas. Em uso é sempre nulo.
  @visibleForTesting
  final Random? aleatorio;

  const SopaScreen({super.key, this.nivel, this.aleatorio});

  @override
  State<SopaScreen> createState() => _SopaScreenState();
}

class _SopaScreenState extends State<SopaScreen>
    with SingleTickerProviderStateMixin {
  late final Random _rnd = widget.aleatorio ?? Random();
  late final AnimationController _abanao;

  late Sopa _sopa;
  late int _nivel;
  final _encontradas = <String>{};

  /// Verdadeiro entre acabar um nível e o seguinte entrar. Trava o arrasto
  /// para a criança não seleccionar letras de uma sopa que já saiu.
  bool _aPassar = false;

  /// As casas já ganhas, para ficarem marcadas.
  final _pintadas = <int>{};

  int? _de;
  List<int> _seleccao = const [];

  @override
  void initState() {
    super.initState();
    Sons.i.definirAmbiente(Trilha.relaxar);
    _abanao = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 380),
    );
    _nivel = widget.nivel ?? context.read<AppState>().nivelDe(Jogo.sopa);
    _novaSopa();
  }

  @override
  void dispose() {
    Sons.i.definirAmbiente(Trilha.principal);
    _abanao.dispose();
    super.dispose();
  }

  void _novaSopa() {
    _sopa = Sopa.doNivel(_nivel, rnd: _rnd);
    _encontradas.clear();
    _pintadas.clear();
    _de = null;
    _seleccao = const [];
    _aPassar = false;
    setState(() {});
  }

  /// Acabou o nível: festeja um instante e o seguinte entra sozinho.
  ///
  /// Não há botão de "outra sopa". Uma escadaria de mil degraus com um botão
  /// a perguntar se se quer continuar seria mil perguntas — e a criança que
  /// acabou de encontrar a última palavra já respondeu que sim.
  Future<void> _passarAoSeguinte() async {
    setState(() => _aPassar = true);
    await Future<void>.delayed(const Duration(milliseconds: 1500));
    if (!mounted) return;
    _nivel = context.read<AppState>().subirNivelDe(Jogo.sopa);
    _novaSopa();
  }

  bool get _acabou => _encontradas.length == _sopa.escondidas.length;

  String get _quantasFaltam =>
      quantasFaltam(_sopa.escondidas.length - _encontradas.length);

  double _lado = 34;

  int? _casaEm(Offset p) {
    final c = (p.dx / _lado).floor();
    final l = (p.dy / _lado).floor();
    if (!_sopa.dentro(l, c)) return null;
    return _sopa.indice(l, c);
  }

  void _comecar(Offset p) {
    if (_acabou || _aPassar) return;
    final i = _casaEm(p);
    if (i == null) return;
    setState(() {
      _de = i;
      _seleccao = [i];
    });
  }

  void _arrastar(Offset p) {
    final de = _de;
    if (de == null || _acabou || _aPassar) return;
    final ate = _casaEm(p);
    if (ate == null) return;
    // Só linhas rectas: um dedo aos saltos não selecciona nada, senão
    // arrastar em ziguezague apanhava letras soltas e acertava por acidente.
    final linha = _sopa.linhaEntre(de, ate);
    if (linha == null) return;
    setState(() => _seleccao = linha);
  }

  void _largar() {
    if (_seleccao.length < 2) {
      setState(() {
        _de = null;
        _seleccao = const [];
      });
      return;
    }

    final achada = _sopa.acertaEm(_seleccao);
    if (achada != null && !_encontradas.contains(achada.palavra)) {
      Sons.i.certo();
      HapticFeedback.lightImpact();
      _encontradas.add(achada.palavra);
      _pintadas.addAll(achada.casas);

      if (_acabou) {
        Sons.i.nivel();
        // Uma palavra encontrada vale como uma resposta certa de lição.
        context.read<AppState>().concluirTreino(_sopa.escondidas.length);
        _passarAoSeguinte();
      } else if (_encontradas.length >= 3) {
        Sons.i.voz('voz-boa.mp3');
      }
    } else if (achada == null) {
      Sons.i.errado();
      _abanao.forward(from: 0);
    }

    setState(() {
      _de = null;
      _seleccao = const [];
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
          'Sopa de letras · Nível $_nivel',
          style: const TextStyle(fontSize: 16),
        ),
      ),
      body: SafeArea(
        child: Column(
          children: [
            Text(
              _acabou
                  ? 'Encontraste todas!'
                  : '${_sopa.tema.rotulo} · $_quantasFaltam',
              style: TextStyle(
                color: _acabou ? S.chart : S.txSoft,
                fontSize: 15,
                fontWeight: _acabou ? FontWeight.w700 : FontWeight.w500,
              ),
            ),
            const SizedBox(height: 8),
            Expanded(
              child: Center(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 10),
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
            _lista(),
            if (_acabou) _fim(),
          ],
        ),
      ),
    );
  }

  Widget _grelha() => LayoutBuilder(
    builder: (context, box) {
      final lado = min(box.maxWidth, box.maxHeight) / _sopa.lado;
      _lado = lado;
      // O gesto é da grelha inteira: um arrasto começa numa letra e acaba
      // noutra, e com um detector por letra o dedo deixava de ser seguido
      // assim que saísse da primeira.
      return GestureDetector(
        onPanStart: (d) => _comecar(d.localPosition),
        onPanUpdate: (d) => _arrastar(d.localPosition),
        onPanEnd: (_) => _largar(),
        onPanCancel: _largar,
        child: SizedBox(
          key: const ValueKey('sopa-grelha'),
          width: lado * _sopa.lado,
          height: lado * _sopa.lado,
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              for (var l = 0; l < _sopa.lado; l++)
                Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    for (var c = 0; c < _sopa.lado; c++)
                      _letra(_sopa.indice(l, c), lado),
                  ],
                ),
            ],
          ),
        ),
      );
    },
  );

  Widget _letra(int i, double lado) {
    final ganha = _pintadas.contains(i);
    final aSeleccionar = _seleccao.contains(i);

    return Container(
      width: lado,
      height: lado,
      padding: const EdgeInsets.all(1),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 130),
        decoration: BoxDecoration(
          // A palavra ganha fica pintada e não risca: numa sopa de letras a
          // marca é o troféu, e apagá-la tirava à criança o que ela fez.
          color: ganha
              ? S.green500.withValues(alpha: 0.55)
              : aSeleccionar
              ? S.chart.withValues(alpha: 0.30)
              : Colors.transparent,
          borderRadius: BorderRadius.circular(lado * 0.28),
        ),
        alignment: Alignment.center,
        child: Text(
          _sopa.letras[i],
          style: TextStyle(
            fontSize: lado * 0.5,
            fontWeight: ganha || aSeleccionar
                ? FontWeight.w800
                : FontWeight.w600,
            color: ganha
                ? Colors.white
                : aSeleccionar
                ? S.chart
                : S.txSoft,
          ),
        ),
      ),
    );
  }

  Widget _lista() => Padding(
    padding: const EdgeInsets.fromLTRB(16, 10, 16, 12),
    child: Wrap(
      spacing: 8,
      runSpacing: 6,
      alignment: WrapAlignment.center,
      children: [
        for (final p in _sopa.escondidas)
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
            decoration: BoxDecoration(
              color: _encontradas.contains(p.palavra)
                  ? S.green500.withValues(alpha: 0.22)
                  : S.surface,
              border: Border.all(
                color: _encontradas.contains(p.palavra) ? S.green300 : S.line,
              ),
              borderRadius: BorderRadius.circular(S.rPill),
            ),
            child: Text(
              p.palavra,
              style: TextStyle(
                fontSize: 13,
                fontWeight: FontWeight.w700,
                color: _encontradas.contains(p.palavra)
                    ? S.green300
                    : S.txSoft,
                decoration: _encontradas.contains(p.palavra)
                    ? TextDecoration.lineThrough
                    : null,
                decorationColor: S.green300,
              ),
            ),
          ),
      ],
    ),
  );

  Widget _fim() => Padding(
    padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
    child: Column(
      children: [
        Image.asset(RobyPose.orgulhoso.path, width: 76),
        const SizedBox(height: 8),
        Text(
          'Nível $_nivel feito!',
          style: const TextStyle(
            fontSize: 19,
            fontWeight: FontWeight.w700,
            color: S.chart,
          ),
        ),
        const SizedBox(height: 4),
        Text(
          _nivel >= nivelMaximo
              ? 'Chegaste ao fim da escadaria.'
              : 'Vem aí o ${_nivel + 1}…',
          style: const TextStyle(color: S.txSoft, fontSize: 14),
        ),
      ],
    ),
  );
}
