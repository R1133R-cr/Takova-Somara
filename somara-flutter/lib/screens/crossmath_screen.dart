import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../models/crossmath.dart';
import '../models/escadaria.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';

/// Crossmath: uma grelha onde as contas têm de fechar nas linhas e nas
/// colunas ao mesmo tempo.
///
/// Não gasta corações, de propósito. É um jogo, não um nível — e a criança
/// que vem para aqui ou já fez o que tinha a fazer, ou está a passar o
/// tempo de uma espera. Em nenhum dos casos faz sentido castigá-la por
/// tentar.
class CrossmathScreen extends StatefulWidget {
  /// Por onde começar. Nulo entra pelo degrau guardado no estado.
  final int? nivel;
  const CrossmathScreen({super.key, this.nivel});

  @override
  State<CrossmathScreen> createState() => _CrossmathScreenState();
}

class _CrossmathScreenState extends State<CrossmathScreen>
    with SingleTickerProviderStateMixin {
  static const _lado = 74.0;
  static const _vaoSinal = 34.0;

  late final AnimationController _abanao;
  late Crossmath _puzzle;
  late int _nivel;

  /// Verdadeiro entre resolver e o degrau seguinte entrar.
  bool _aPassar = false;
  late List<int?> _tentativa;

  int? _seleccionada;
  List<int> _erradas = const [];
  bool _resolvido = false;
  int _resolvidos = 0;

  @override
  void initState() {
    super.initState();
    // A trilha muda ao COMECAR o jogo, nao ao espreitar a sala. Percorrer
    // os separadores e navegar; abrir um jogo e outra coisa, e e so ai que
    // o ambiente tem de mudar.
    Sons.i.definirAmbiente(Trilha.relaxar);
    _abanao = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 420),
    );
    _nivel = widget.nivel ?? context.read<AppState>().nivelDe(Jogo.crossmath);
    _novo();
  }

  @override
  void dispose() {
    Sons.i.definirAmbiente(Trilha.principal);
    _abanao.dispose();
    super.dispose();
  }

  void _novo() {
    _puzzle = GeradorCrossmath().doNivel(_nivel);
    _aPassar = false;
    _tentativa = [
      for (var i = 0; i < 9; i++)
        _puzzle.dadas[i] ? _puzzle.valores[i] : null,
    ];
    // A primeira casa por preencher fica escolhida logo: sem isto, a
    // criança olha para o teclado e não sabe onde é que o número vai cair.
    _seleccionada = _puzzle.dadas.indexOf(false);
    _erradas = const [];
    _resolvido = false;
    setState(() {});
  }

  void _escrever(int digito) {
    final i = _seleccionada;
    if (i == null || _resolvido) return;
    Sons.i.toque();
    final novo = (_tentativa[i] ?? 0) * 10 + digito;
    if (novo > 999) return;
    setState(() {
      _tentativa[i] = novo;
      _erradas = _erradas.where((e) => e != i).toList();
    });
  }

  /// Resolvido: festeja um instante e o degrau seguinte entra sozinho.
  ///
  /// O mesmo que a Sopa e o Pomar fazem. Quem acabou de resolver um puzzle
  /// já respondeu que quer o seguinte.
  Future<void> _passarAoSeguinte() async {
    setState(() => _aPassar = true);
    await Future<void>.delayed(const Duration(milliseconds: 1600));
    if (!mounted) return;
    _nivel = context.read<AppState>().subirNivelDe(Jogo.crossmath);
    setState(_novo);
  }

  void _apagar() {
    final i = _seleccionada;
    if (i == null || _resolvido || _aPassar) return;
    Sons.i.toque();
    setState(() => _tentativa[i] = null);
  }

  void _verificar() {
    if (_aPassar) return;
    final erradas = _puzzle.conferir(_tentativa);
    if (erradas.isEmpty) {
      Sons.i.nivel();
      HapticFeedback.mediumImpact();
      // Vale como três respostas certas. Um puzzle destes dá bastante mais
      // trabalho do que uma pergunta de escolha múltipla.
      context.read<AppState>().concluirTreino(3);
      setState(() {
        _resolvido = true;
        _resolvidos++;
        _erradas = const [];
      });
      unawaited(_passarAoSeguinte());
      return;
    }
    Sons.i.errado();
    HapticFeedback.heavyImpact();
    _abanao.forward(from: 0);
    setState(() => _erradas = erradas);
  }

  bool get _completo => _tentativa.every((v) => v != null);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: S.gm950,
      appBar: AppBar(
        backgroundColor: S.gm950,
        foregroundColor: S.tx,
        elevation: 0,
        title: Text(
          'Crossmath · Nível $_nivel',
          style: const TextStyle(fontSize: 16.5),
        ),
        actions: [
          if (_resolvidos > 0)
            Padding(
              padding: const EdgeInsets.only(right: 18),
              child: Center(
                child: Text(
                  _resolvidos == 1
                      ? '1 resolvido'
                      : '$_resolvidos resolvidos',
                  style: const TextStyle(
                    color: S.green300,
                    fontSize: 13.5,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ),
            ),
        ],
      ),
      body: SafeArea(
        child: Column(
          children: [
            Text(
              _resolvido
                  ? 'Boa! Fecha nas linhas e nas colunas.'
                  : 'Descobre os números que faltam.',
              textAlign: TextAlign.center,
              style: TextStyle(
                color: _resolvido ? S.chart : S.txSoft,
                fontSize: 14.5,
                fontWeight: _resolvido ? FontWeight.w700 : FontWeight.w400,
              ),
            ),
            Expanded(
              child: Center(
                child: SingleChildScrollView(
                  padding: const EdgeInsets.symmetric(horizontal: 12),
                  child: AnimatedBuilder(
                    animation: _abanao,
                    builder: (_, filho) {
                      // Abana ao errar — o mesmo gesto da lição, para a
                      // criança reconhecer o sinal sem ter de o aprender
                      // outra vez.
                      final t = _abanao.value;
                      final dx = t == 0
                          ? 0.0
                          : (1 - t) * 11 * (t * 26 % 2 < 1 ? 1 : -1);
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
            if (_resolvido) _depoisDeResolver() else _teclado(),
          ],
        ),
      ),
    );
  }

  /// A grelha com os sinais entre as casas, como no papel.
  Widget _grelha() => Column(
    mainAxisSize: MainAxisSize.min,
    children: [
      _linhaDeCasas(0),
      _linhaDeSinais('+'),
      _linhaDeCasas(3),
      _linhaDeSinais('='),
      _linhaDeCasas(6),
    ],
  );

  Widget _linhaDeCasas(int base) => Row(
    mainAxisAlignment: MainAxisAlignment.center,
    children: [
      _casa(base),
      _sinal('+'),
      _casa(base + 1),
      _sinal('='),
      _casa(base + 2),
    ],
  );

  /// Os sinais verticais, alinhados com o centro de cada coluna.
  Widget _linhaDeSinais(String s) => Padding(
    padding: const EdgeInsets.symmetric(vertical: 3),
    child: Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        SizedBox(width: _lado, child: _sinalTexto(s)),
        const SizedBox(width: _vaoSinal),
        SizedBox(width: _lado, child: _sinalTexto(s)),
        const SizedBox(width: _vaoSinal),
        SizedBox(width: _lado, child: _sinalTexto(s)),
      ],
    ),
  );

  Widget _sinal(String s) => SizedBox(width: _vaoSinal, child: _sinalTexto(s));

  Widget _sinalTexto(String s) => Text(
    s,
    textAlign: TextAlign.center,
    style: const TextStyle(
      color: S.txSoft,
      fontSize: 23,
      fontWeight: FontWeight.w400,
    ),
  );

  Widget _casa(int i) {
    final dada = _puzzle.dadas[i];
    final errada = _erradas.contains(i);
    final escolhida = _seleccionada == i && !_resolvido;
    final valor = _tentativa[i];

    return GestureDetector(
      onTap: dada || _resolvido
          ? null
          : () {
              Sons.i.toque();
              setState(() => _seleccionada = i);
            },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 180),
        width: _lado,
        height: _lado,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          // As casas dadas ficam cheias, as de descobrir ocas. A diferença
          // tem de se ver de relance, senão a criança não sabe onde pode
          // escrever.
          color: dada
              ? S.surface
              : escolhida
              ? S.chart.withValues(alpha: 0.14)
              : Colors.transparent,
          border: Border.all(
            color: errada
                ? S.life
                : escolhida
                ? S.chart
                : S.line,
            width: escolhida ? 3 : 2,
          ),
        ),
        alignment: Alignment.center,
        child: Text(
          valor?.toString() ?? '',
          style: TextStyle(
            fontSize: (valor ?? 0) > 99 ? 21 : 26,
            fontWeight: FontWeight.w700,
            color: errada
                ? S.life
                : dada
                ? S.tx
                : S.chart,
          ),
        ),
      ),
    );
  }

  Widget _teclado() => Padding(
    padding: const EdgeInsets.fromLTRB(16, 4, 16, 12),
    child: Column(
      children: [
        for (final fila in const [
          [1, 2, 3, 4, 5],
          [6, 7, 8, 9, 0],
        ])
          Padding(
            padding: const EdgeInsets.only(bottom: 8),
            child: Row(
              children: [
                for (final d in fila) ...[
                  Expanded(child: _tecla('$d', () => _escrever(d))),
                  if (d != fila.last) const SizedBox(width: 8),
                ],
              ],
            ),
          ),
        Row(
          children: [
            Expanded(
              child: _tecla(
                'Apagar',
                _apagar,
                cor: S.surface,
                corTexto: S.txSoft,
              ),
            ),
            const SizedBox(width: 8),
            Expanded(
              flex: 2,
              child: Opacity(
                opacity: _completo ? 1 : 0.45,
                child: _tecla(
                  'Verificar',
                  _completo ? _verificar : null,
                  cor: S.chart,
                  corTexto: S.onChart,
                ),
              ),
            ),
          ],
        ),
      ],
    ),
  );

  Widget _tecla(
    String texto,
    VoidCallback? aoTocar, {
    Color cor = S.gm800,
    Color corTexto = S.tx,
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
          fontSize: 18,
          fontWeight: FontWeight.w700,
          color: corTexto,
        ),
      ),
    ),
  );

  Widget _depoisDeResolver() => Padding(
    padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
    child: Column(
      children: [
        Image.asset(RobyPose.orgulhoso.path, width: 92),
        const SizedBox(height: 8),
        Text(
          'Nível $_nivel feito!',
          style: const TextStyle(
            fontSize: 18,
            fontWeight: FontWeight.w700,
            color: S.chart,
          ),
        ),
        const SizedBox(height: 4),
        Text(
          _nivel >= nivelMaximo
              ? 'Chegaste ao fim da escadaria.'
              : 'Vem aí o ${_nivel + 1}…',
          style: const TextStyle(color: S.txSoft, fontSize: 13.5),
        ),
        const SizedBox(height: 12),
        Row(
          children: [
            Expanded(
              child: _tecla(
                'Sair',
                () => Navigator.of(context).pop(),
                cor: S.surface,
                corTexto: S.txSoft,
              ),
            ),
            const SizedBox(width: 10),
            Expanded(
              flex: 2,
              child: _tecla(
                'Outro puzzle',
                () {
                  Sons.i.toque();
                  _novo();
                },
                cor: S.chart,
                corTexto: S.onChart,
              ),
            ),
          ],
        ),
      ],
    ),
  );
}
