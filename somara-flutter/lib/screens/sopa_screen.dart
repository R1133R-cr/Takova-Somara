import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
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
  final NivelSopa nivel;
  const SopaScreen({super.key, required this.nivel});

  @override
  State<SopaScreen> createState() => _SopaScreenState();
}

class _SopaScreenState extends State<SopaScreen>
    with SingleTickerProviderStateMixin {
  final _rnd = Random();
  late final AnimationController _abanao;

  late Sopa _sopa;
  final _encontradas = <String>{};

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
    _novaSopa();
  }

  @override
  void dispose() {
    Sons.i.definirAmbiente(Trilha.principal);
    _abanao.dispose();
    super.dispose();
  }

  void _novaSopa() {
    final tema = Tema.values[_rnd.nextInt(Tema.values.length)];
    _sopa = Sopa.nova(tema: tema, nivel: widget.nivel, rnd: _rnd);
    _encontradas.clear();
    _pintadas.clear();
    _de = null;
    _seleccao = const [];
    setState(() {});
  }

  bool get _acabou => _encontradas.length == _sopa.escondidas.length;

  double _lado = 34;

  int? _casaEm(Offset p) {
    final c = (p.dx / _lado).floor();
    final l = (p.dy / _lado).floor();
    if (!_sopa.dentro(l, c)) return null;
    return _sopa.indice(l, c);
  }

  void _comecar(Offset p) {
    if (_acabou) return;
    final i = _casaEm(p);
    if (i == null) return;
    setState(() {
      _de = i;
      _seleccao = [i];
    });
  }

  void _arrastar(Offset p) {
    final de = _de;
    if (de == null || _acabou) return;
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
          'Sopa de letras · ${widget.nivel.rotulo}',
          style: const TextStyle(fontSize: 16),
        ),
      ),
      body: SafeArea(
        child: Column(
          children: [
            Text(
              _acabou
                  ? 'Encontraste todas!'
                  : '${_sopa.tema.rotulo} · faltam '
                        '${_sopa.escondidas.length - _encontradas.length}',
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
              child: _botao('Outra sopa', () {
                Sons.i.toque();
                _novaSopa();
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
