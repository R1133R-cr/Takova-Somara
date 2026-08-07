import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../models/content.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';
import 'complete_screen.dart';

class LessonScreen extends StatefulWidget {
  final int indice;
  const LessonScreen({super.key, required this.indice});
  @override
  State<LessonScreen> createState() => _LessonScreenState();
}

enum Fase { responder, certo, errado }

class _LessonScreenState extends State<LessonScreen> with TickerProviderStateMixin {
  late List<Questao> qs;
  int idx = 0;
  int acertos = 0;
  Fase fase = Fase.responder;

  // Estado por tipo de questão
  int? escolha;                       // choice / count
  final _input = TextEditingController();
  final Map<int, int> ligacoes = {};  // match: esquerda → direita
  int? matchSelEsq;
  List<int> ordemDireita = [];        // match: coluna direita baralhada
  int? zonaLargada;                   // drag

  late final AnimationController _entrada;
  late final AnimationController _abanao;

  static const _msgsCerto = [
    'Boa! Certíssimo ⚡',
    'Isso mesmo! Continua assim.',
    'Muito bem! ⭐',
    'Acertaste em cheio!',
  ];
  static const _msgsErrado = ['Quase!', 'Não foi desta vez.', 'Vamos tentar de novo.'];
  static const _facesCerto = [
    RobyPose.feliz, RobyPose.rindo, RobyPose.empolgado, RobyPose.orgulhoso,
  ];
  static const _facesErrado = [RobyPose.triste, RobyPose.confuso];

  final _rnd = math.Random();
  late RobyPose _faceActual;
  late String _msgActual;

  @override
  void initState() {
    super.initState();
    final st = context.read<AppState>();
    qs = st.niveis[widget.indice].nivel.questoes;
    _faceActual = RobyPose.confiante;
    _msgActual = '';

    _entrada = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 340),
    )..forward();
    _abanao = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 420),
    );
    _prepararQuestao();
  }

  @override
  void dispose() {
    _entrada.dispose();
    _abanao.dispose();
    _input.dispose();
    super.dispose();
  }

  Questao get q => qs[idx];

  void _prepararQuestao() {
    escolha = null;
    zonaLargada = null;
    ligacoes.clear();
    matchSelEsq = null;
    _input.clear();
    final cur = q;
    if (cur is QMatch) {
      ordemDireita = List.generate(cur.pairs.length, (i) => i)..shuffle(_rnd);
    }
  }

  bool get _podeVerificar {
    final cur = q;
    if (cur is QChoice || cur is QCount) return escolha != null;
    if (cur is QInput) return _input.text.trim().isNotEmpty;
    if (cur is QDrag) return zonaLargada != null;
    if (cur is QMatch) return ligacoes.length == cur.pairs.length;
    return false;
  }

  /// Normaliza para comparar respostas escritas: sem maiúsculas, sem acentos,
  /// sem espaços a mais. Uma criança de 6 anos não deve falhar por escrever
  /// "aviao" em vez de "avião".
  static String _norm(String s) {
    const de = 'áàâãäéèêëíìîïóòôõöúùûüçÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ';
    const para = 'aaaaaeeeeiiiiooooouuuucAAAAAEEEEIIIIOOOOOUUUUC';
    var r = s.trim().toLowerCase();
    final b = StringBuffer();
    for (final ch in r.split('')) {
      final i = de.indexOf(ch);
      b.write(i >= 0 ? para[i] : ch);
    }
    return b.toString().replaceAll(RegExp(r'\s+'), ' ');
  }

  bool _avaliar() {
    final cur = q;
    if (cur is QCount) return escolha == cur.a;
    if (cur is QChoice) return escolha == cur.a;
    if (cur is QInput) return _norm(_input.text) == _norm(cur.a);
    if (cur is QDrag) return zonaLargada == cur.a;
    if (cur is QMatch) {
      for (var e = 0; e < cur.pairs.length; e++) {
        if (ligacoes[e] != e) return false;
      }
      return true;
    }
    return false;
  }

  void _verificar() {
    final ok = _avaliar();
    final st = context.read<AppState>();
    setState(() {
      fase = ok ? Fase.certo : Fase.errado;
      _faceActual = ok
          ? _facesCerto[_rnd.nextInt(_facesCerto.length)]
          : _facesErrado[_rnd.nextInt(_facesErrado.length)];
      _msgActual = ok
          ? _msgsCerto[_rnd.nextInt(_msgsCerto.length)]
          : _msgsErrado[_rnd.nextInt(_msgsErrado.length)];
      if (ok) acertos++;
    });
    if (ok) {
      HapticFeedback.lightImpact();
    } else {
      HapticFeedback.heavyImpact();
      _abanao.forward(from: 0);
      st.perderVida();
    }
  }

  void _seguinte() {
    if (idx + 1 >= qs.length) {
      final st = context.read<AppState>();
      st.concluirNivel(widget.indice, acertos, qs.length);
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(
          builder: (_) => CompleteScreen(
            indice: widget.indice,
            acertos: acertos,
            total: qs.length,
          ),
        ),
      );
      return;
    }
    setState(() {
      idx++;
      fase = Fase.responder;
      _prepararQuestao();
    });
    _entrada.forward(from: 0);
  }

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    return Scaffold(
      backgroundColor: S.gm950,
      body: SafeArea(
        child: Column(
          children: [
            _barraTopo(st),
            Expanded(
              child: SingleChildScrollView(
                padding: const EdgeInsets.fromLTRB(18, 8, 18, 24),
                child: AnimatedBuilder(
                  animation: Listenable.merge([_entrada, _abanao]),
                  builder: (_, child) {
                    // Entrada: desliza de baixo e aparece.
                    final e = SCurves.ease.transform(_entrada.value);
                    // Erro: abana horizontalmente, amortecido.
                    final a = _abanao.isAnimating
                        ? math.sin(_abanao.value * math.pi * 5) *
                            10 *
                            (1 - _abanao.value)
                        : 0.0;
                    return Transform.translate(
                      offset: Offset(a, (1 - e) * 26),
                      child: Opacity(opacity: e, child: child),
                    );
                  },
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      _balaoRoby(),
                      const SizedBox(height: 22),
                      _corpoQuestao(),
                    ],
                  ),
                ),
              ),
            ),
            _doca(),
          ],
        ),
      ),
    );
  }

  Widget _barraTopo(AppState st) => Padding(
        padding: const EdgeInsets.fromLTRB(14, 10, 14, 6),
        child: Row(
          children: [
            IconButton(
              icon: const Icon(Icons.close_rounded, color: S.txSoft),
              onPressed: () => _confirmarSaida(),
            ),
            Expanded(
              child: ClipRRect(
                borderRadius: BorderRadius.circular(S.rPill),
                child: TweenAnimationBuilder<double>(
                  tween: Tween(begin: 0, end: idx / qs.length),
                  duration: const Duration(milliseconds: 420),
                  curve: SCurves.ease,
                  builder: (_, v, _) => LinearProgressIndicator(
                    value: v,
                    minHeight: 12,
                    backgroundColor: S.surface,
                    valueColor: const AlwaysStoppedAnimation(S.chart),
                  ),
                ),
              ),
            ),
            const SizedBox(width: 12),
            Row(children: [
              const Icon(Icons.favorite_rounded, color: S.life, size: 20),
              const SizedBox(width: 4),
              Text('${st.lives}',
                  style: const TextStyle(
                      color: S.life, fontWeight: FontWeight.w700, fontSize: 16)),
            ]),
          ],
        ),
      );

  Future<void> _confirmarSaida() async {
    final sair = await showDialog<bool>(
      context: context,
      builder: (_) => AlertDialog(
        backgroundColor: S.gm800,
        title: const Text('Sair da lição?', style: TextStyle(color: S.tx)),
        content: const Text('Este nível não vai contar.',
            style: TextStyle(color: S.txSoft)),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: const Text('Continuar a jogar'),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            child: const Text('Sair', style: TextStyle(color: S.life)),
          ),
        ],
      ),
    );
    if (sair == true && mounted) Navigator.of(context).pop();
  }

  Widget _balaoRoby() => Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            width: 62,
            height: 62,
            child: ClipOval(
              child: Container(
                color: const Color(0xFFF3EFE3),
                child: Image.asset(RobyPose.confiante.path,
                    fit: BoxFit.cover, alignment: Alignment.topCenter),
              ),
            ),
          ),
          const SizedBox(width: 10),
          Expanded(
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
              decoration: BoxDecoration(
                color: S.surface,
                borderRadius: BorderRadius.circular(S.rLg),
                border: Border.all(color: S.line, width: 2),
              ),
              child: Text(
                q.q,
                style: const TextStyle(
                    fontSize: 19, fontWeight: FontWeight.w600, color: S.tx, height: 1.25),
              ),
            ),
          ),
        ],
      );

  Widget _corpoQuestao() {
    final cur = q;
    return switch (cur) {
      QCount() => _vistaCount(cur),
      QChoice() => _opcoes(cur.options),
      QInput() => _vistaInput(),
      QMatch() => _vistaMatch(cur),
      QDrag() => _vistaDrag(cur),
    };
  }

  Widget _vistaCount(QCount cur) => Column(
        children: [
          Container(
            padding: const EdgeInsets.all(18),
            decoration: BoxDecoration(
              color: S.surface,
              borderRadius: BorderRadius.circular(S.rLg),
              border: Border.all(color: S.line, width: 2),
            ),
            child: Wrap(
              alignment: WrapAlignment.center,
              spacing: 10,
              runSpacing: 10,
              children: [
                for (var i = 0; i < cur.n; i++)
                  // Cada objecto entra com um pequeno atraso em cadeia —
                  // ajuda a criança a contar com os olhos.
                  TweenAnimationBuilder<double>(
                    key: ValueKey('$idx-$i'),
                    tween: Tween(begin: 0, end: 1),
                    duration: Duration(milliseconds: 260 + i * 90),
                    curve: SCurves.spring,
                    builder: (_, v, child) =>
                        Transform.scale(scale: v, child: child),
                    child: Text(cur.emoji, style: const TextStyle(fontSize: 42)),
                  ),
              ],
            ),
          ),
          const SizedBox(height: 20),
          _opcoes(cur.options),
        ],
      );

  // Ocupam a largura toda de propósito: o alvo de toque de uma criança de
  // seis anos é impreciso, e um botão à medida do texto ("3") daria um alvo
  // minúsculo. A altura mínima segue a recomendação de 48dp do Android.
  Widget _opcoes(List<String> opts) => Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          for (var i = 0; i < opts.length; i++)
            Padding(
              padding: const EdgeInsets.only(bottom: 12),
              child: _botaoOpcao(i, opts[i]),
            ),
        ],
      );

  Widget _botaoOpcao(int i, String texto) {
    final sel = escolha == i;
    final revelar = fase != Fase.responder;
    final cur = q;
    final certa = cur is QChoice ? cur.a : (cur is QCount ? cur.a : -1);

    Color borda = S.line, fundo = S.surface, txt = S.tx;
    if (revelar && i == certa) {
      borda = S.chart; fundo = S.green700.withValues(alpha: 0.35); txt = S.chart;
    } else if (revelar && sel && i != certa) {
      borda = S.life; fundo = S.lifeDim.withValues(alpha: 0.5); txt = S.life;
    } else if (sel) {
      borda = S.chart; fundo = S.surface2;
    }

    return GestureDetector(
      onTap: fase == Fase.responder
          ? () {
              HapticFeedback.selectionClick();
              setState(() => escolha = i);
            }
          : null,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 180),
        curve: SCurves.ease,
        constraints: const BoxConstraints(minHeight: 62),
        alignment: Alignment.center,
        padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 17),
        decoration: BoxDecoration(
          color: fundo,
          border: Border.all(color: borda, width: 2),
          borderRadius: BorderRadius.circular(S.rMd),
        ),
        child: Text(texto,
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.w600, color: txt)),
      ),
    );
  }

  Widget _vistaInput() => Padding(
        padding: const EdgeInsets.only(top: 8),
        child: TextField(
          controller: _input,
          enabled: fase == Fase.responder,
          autofocus: true,
          textAlign: TextAlign.center,
          textCapitalization: TextCapitalization.characters,
          onChanged: (_) => setState(() {}),
          onSubmitted: (_) => _podeVerificar ? _verificar() : null,
          style: const TextStyle(fontSize: 24, color: S.tx, fontWeight: FontWeight.w600),
          decoration: InputDecoration(
            hintText: 'Escreve a resposta',
            hintStyle: const TextStyle(color: S.txMut, fontWeight: FontWeight.w400),
            filled: true,
            fillColor: S.surface,
            contentPadding: const EdgeInsets.symmetric(vertical: 20),
            enabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(S.rMd),
              borderSide: const BorderSide(color: S.line, width: 2),
            ),
            focusedBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(S.rMd),
              borderSide: const BorderSide(color: S.chart, width: 2),
            ),
            disabledBorder: OutlineInputBorder(
              borderRadius: BorderRadius.circular(S.rMd),
              borderSide: const BorderSide(color: S.line, width: 2),
            ),
          ),
        ),
      );

  Widget _vistaMatch(QMatch cur) {
    final n = cur.pairs.length;
    return Column(
      children: [
        Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Expanded(
              child: Column(
                children: [
                  for (var e = 0; e < n; e++)
                    _fichaMatch(
                      texto: cur.pairs[e].$1,
                      seleccionada: matchSelEsq == e,
                      ligada: ligacoes.containsKey(e),
                      onTap: () => setState(() => matchSelEsq = e),
                    ),
                ],
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                children: [
                  for (final d in ordemDireita)
                    _fichaMatch(
                      texto: cur.pairs[d].$2,
                      seleccionada: false,
                      ligada: ligacoes.containsValue(d),
                      onTap: () {
                        if (matchSelEsq == null) return;
                        setState(() {
                          ligacoes.removeWhere((k, v) => v == d);
                          ligacoes[matchSelEsq!] = d;
                          matchSelEsq = null;
                        });
                        HapticFeedback.selectionClick();
                      },
                    ),
                ],
              ),
            ),
          ],
        ),
        const SizedBox(height: 10),
        const Text('Toca num de cada lado para ligar.',
            style: TextStyle(color: S.txMut, fontSize: 13)),
      ],
    );
  }

  Widget _fichaMatch({
    required String texto,
    required bool seleccionada,
    required bool ligada,
    required VoidCallback onTap,
  }) =>
      Padding(
        padding: const EdgeInsets.only(bottom: 10),
        child: GestureDetector(
          onTap: fase == Fase.responder ? onTap : null,
          child: AnimatedContainer(
            duration: const Duration(milliseconds: 180),
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 16),
            decoration: BoxDecoration(
              color: ligada ? S.green700.withValues(alpha: 0.4) : S.surface,
              border: Border.all(
                color: seleccionada ? S.chart : (ligada ? S.green500 : S.line),
                width: 2,
              ),
              borderRadius: BorderRadius.circular(S.rMd),
            ),
            child: Text(texto,
                textAlign: TextAlign.center,
                style: const TextStyle(
                    fontSize: 16, fontWeight: FontWeight.w600, color: S.tx)),
          ),
        ),
      );

  Widget _vistaDrag(QDrag cur) => Column(
        children: [
          // A peça a arrastar — desaparece do sítio quando já foi largada.
          SizedBox(
            height: 88,
            child: zonaLargada == null
                ? Draggable<int>(
                    data: 0,
                    feedback: _chip(cur.chip, arrastando: true),
                    childWhenDragging: Opacity(opacity: 0.25, child: _chip(cur.chip)),
                    child: _chip(cur.chip),
                  )
                : Center(
                    child: Text('Largaste em: ${cur.zones[zonaLargada!]}',
                        style: const TextStyle(color: S.txSoft, fontSize: 14)),
                  ),
          ),
          const SizedBox(height: 18),
          Row(
            children: [
              for (var z = 0; z < cur.zones.length; z++)
                Expanded(
                  child: Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 5),
                    child: DragTarget<int>(
                      onAcceptWithDetails: (_) {
                        setState(() => zonaLargada = z);
                        HapticFeedback.mediumImpact();
                      },
                      builder: (_, candidatos, _) {
                        final activa = candidatos.isNotEmpty;
                        final escolhida = zonaLargada == z;
                        return AnimatedContainer(
                          duration: const Duration(milliseconds: 160),
                          height: 96,
                          decoration: BoxDecoration(
                            color: activa
                                ? S.chart.withValues(alpha: 0.16)
                                : (escolhida ? S.surface2 : S.surface),
                            border: Border.all(
                              color: activa || escolhida ? S.chart : S.line,
                              width: 2.5,
                            ),
                            borderRadius: BorderRadius.circular(S.rMd),
                          ),
                          alignment: Alignment.center,
                          child: Text(
                            cur.zones[z],
                            textAlign: TextAlign.center,
                            style: const TextStyle(
                                fontSize: 15, fontWeight: FontWeight.w600, color: S.tx),
                          ),
                        );
                      },
                    ),
                  ),
                ),
            ],
          ),
        ],
      );

  Widget _chip(String emoji, {bool arrastando = false}) => Material(
        color: Colors.transparent,
        child: Center(
          child: AnimatedScale(
            scale: arrastando ? 1.22 : 1.0,
            duration: const Duration(milliseconds: 140),
            child: Container(
              width: 84,
              height: 84,
              decoration: BoxDecoration(
                color: S.surface2,
                shape: BoxShape.circle,
                border: Border.all(color: S.chart, width: 2.5),
                boxShadow: arrastando
                    ? const [BoxShadow(color: Color(0x88000000), blurRadius: 18, offset: Offset(0, 8))]
                    : null,
              ),
              alignment: Alignment.center,
              child: Text(emoji, style: const TextStyle(fontSize: 42)),
            ),
          ),
        ),
      );

  Widget _doca() {
    final respondeu = fase != Fase.responder;
    final certo = fase == Fase.certo;
    return AnimatedContainer(
      duration: const Duration(milliseconds: 260),
      curve: SCurves.ease,
      padding: const EdgeInsets.fromLTRB(18, 16, 18, 20),
      decoration: BoxDecoration(
        color: respondeu
            ? (certo ? S.green700.withValues(alpha: 0.30) : S.lifeDim.withValues(alpha: 0.45))
            : Colors.transparent,
        borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          if (respondeu) ...[
            Row(
              children: [
                // O Roby reage — cara diferente a cada resposta, para não
                // ficar previsível ao fim de três exercícios.
                TweenAnimationBuilder<double>(
                  key: ValueKey('$idx-$fase'),
                  tween: Tween(begin: 0, end: 1),
                  duration: const Duration(milliseconds: 420),
                  curve: SCurves.spring,
                  builder: (_, v, child) => Transform.scale(scale: v, child: child),
                  child: SizedBox(
                    width: 52,
                    height: 52,
                    child: ClipOval(
                      child: Container(
                        color: const Color(0xFFF3EFE3),
                        child: Image.asset(_faceActual.path,
                            fit: BoxFit.cover, alignment: Alignment.topCenter),
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(_msgActual,
                          style: TextStyle(
                              fontSize: 17,
                              fontWeight: FontWeight.w700,
                              color: certo ? S.chart : S.life)),
                      if (!certo) Text(_respostaCerta(),
                          style: const TextStyle(color: S.txSoft, fontSize: 13)),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 14),
          ],
          SizedBox(
            width: double.infinity,
            child: _botaoGrande(
              texto: respondeu ? 'Continuar' : 'Verificar',
              activo: respondeu || _podeVerificar,
              cor: certo || !respondeu ? S.chart : S.life,
              corTexto: certo || !respondeu ? S.onChart : Colors.white,
              onTap: respondeu ? _seguinte : _verificar,
            ),
          ),
        ],
      ),
    );
  }

  String _respostaCerta() {
    final cur = q;
    final r = switch (cur) {
      QCount() => cur.options[cur.a],
      QChoice() => cur.options[cur.a],
      QInput() => cur.a,
      QDrag() => cur.zones[cur.a],
      QMatch() => '',
    };
    return r.isEmpty ? 'Vê as ligações certas.' : 'Resposta certa: $r';
  }

  Widget _botaoGrande({
    required String texto,
    required bool activo,
    required Color cor,
    required Color corTexto,
    required VoidCallback onTap,
  }) =>
      GestureDetector(
        onTap: activo ? onTap : null,
        child: AnimatedOpacity(
          opacity: activo ? 1 : 0.45,
          duration: const Duration(milliseconds: 180),
          child: Container(
            padding: const EdgeInsets.symmetric(vertical: 18),
            decoration: BoxDecoration(
              color: cor,
              borderRadius: BorderRadius.circular(S.rPill),
              boxShadow: [
                BoxShadow(
                    color: cor == S.chart ? S.chart600 : S.life.withValues(alpha: 0.5),
                    offset: const Offset(0, 5)),
              ],
            ),
            alignment: Alignment.center,
            child: Text(texto,
                style: TextStyle(
                    fontSize: 18, fontWeight: FontWeight.w700, color: corTexto)),
          ),
        ),
      );
}
