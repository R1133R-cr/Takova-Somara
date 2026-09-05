import 'dart:math' as math;
import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import '../models/content.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/desenho_geometrico.dart';
import '../widgets/mostra_cores.dart';
import '../widgets/roby.dart';
import '../widgets/grelha_operacao.dart';
import '../widgets/interactivos.dart';
import '../widgets/teclado_numerico.dart';
import 'complete_screen.dart';

class LessonScreen extends StatefulWidget {
  /// Índice do nível na amarelinha. Vale -1 numa sessão avulsa (treino ou
  /// revisão), em que não há nível nenhum a concluir.
  final int indice;

  /// Perguntas escolhidas de fora, para treinar ou rever. Quando vem
  /// preenchido, terminar não marca nenhum nível como feito nem faz o Roby
  /// avançar — treinar não é progredir, e confundir as duas coisas daria
  /// ao mapa um avanço que a criança não ganhou.
  final List<Questao>? avulsas;

  /// O que se mostra no fim, quando a sessão é avulsa.
  final String? titulo;

  /// Esta sessão é a campanha da semana. Ao acabar, fecha-a e paga as
  /// sortes que o resultado valer.
  final bool campanha;

  const LessonScreen({
    super.key,
    required this.indice,
    this.avulsas,
    this.titulo,
    this.campanha = false,
  });

  bool get eAvulsa => avulsas != null;
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
  final _voz = AudioPlayer();

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
    qs = widget.avulsas ?? st.niveis[widget.indice].nivel.questoes;
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
    // Musica fora enquanto se resolve. Uma pergunta de Matematica exige
    // concentracao, e som por cima de quem esta a contar nos dedos
    // atrapalha em vez de animar. E o enunciado lido em voz alta tem de se
    // ouvir por cima de nada.
    Sons.i.pedirSilencio();
    _lerEnunciado();
  }

  /// Lê o enunciado em voz alta.
  ///
  /// Uma criança da 1ª ou 2ª classe ainda está a aprender a ler; sem isto a
  /// app só serve a quem já lê corrido, e passa a precisar de um adulto ao
  /// lado. Toca sozinho ao abrir cada pergunta e repete-se no altifalante.
  ///
  /// Falhar aqui nunca pode parar a lição: se o ficheiro faltar, segue-se
  /// em silêncio com o enunciado escrito, que continua no ecrã.
  Future<void> _lerEnunciado() async {
    final ficheiro = q.audio;
    if (ficheiro == null) return;
    try {
      await _voz.stop();
      await _voz.play(AssetSource('audio/$ficheiro'));
    } catch (_) {}
  }

  @override
  void dispose() {
    Sons.i.largarSilencio();
    _entrada.dispose();
    _abanao.dispose();
    _input.dispose();
    _voz.dispose();
    super.dispose();
  }

  Questao get q => qs[idx];

  void _prepararQuestao() {
    escolha = null;
    zonaLargada = null;
    ligacoes.clear();
    matchSelEsq = null;
    _input.clear();
    _casinhas = const [];
    _ordem = const [];
    _porGrupo = const [];
    _noCenario = const [];
    final cur = q;
    if (cur is QMatch) {
      ordemDireita = List.generate(cur.pairs.length, (i) => i)..shuffle(_rnd);
    }
    if (cur is QSequencia) _ordem = cur.baralhados();
    if (cur is QGrupos) {
      _porGrupo = List<int?>.filled(cur.itens.length, null);
    }
    if (cur is QCenario) {
      _noCenario = List<String?>.filled(cur.alvos.length, null);
    }
  }

  /// A chave da grelha aberta, para o widget se refazer entre perguntas.
  final _grelha = GlobalKey<GrelhaOperacaoState>();

  /// O que a criança escreveu nas casinhas da conta armada.
  List<String> _casinhas = const [];

  /// A ordem em que os passos estão, numa pergunta de sequência.
  List<int> _ordem = const [];

  /// Em que grupo está cada coisa, numa de classificar.
  List<int?> _porGrupo = const [];

  /// A peça largada em cada sítio do cenário.
  List<String?> _noCenario = const [];

  bool get _podeVerificar {
    final cur = q;
    if (cur is QChoice || cur is QCount) return escolha != null;
    if (cur is QInput) return _input.text.trim().isNotEmpty;
    if (cur is QDrag) return zonaLargada != null;
    if (cur is QMatch) return ligacoes.length == cur.pairs.length;
    // A sequência está sempre respondida: os passos já estão numa ordem,
    // mesmo antes de ela mexer em algum. Obrigá-la a mexer para poder
    // verificar era inventar uma regra que ninguém lhe explicou.
    if (cur is QSequencia) return _ordem.length == cur.passos.length;
    if (cur is QGrupos) return !_porGrupo.contains(null);
    if (cur is QCenario) return !_noCenario.contains(null);
    if (cur is QGrelha) {
      // Só se verifica com tudo o que conta preenchido. Os transportes
      // podem ficar em branco: quem soma o "vai um" de cabeça não está a
      // fazer nada de errado.
      final alvo = cur.conta.aPreencher;
      for (var i = 0; i < alvo.length; i++) {
        if (!alvo[i].conta) continue;
        if (i >= _casinhas.length || _casinhas[i].trim().isEmpty) return false;
      }
      return true;
    }
    return false;
  }

  /// Normaliza para comparar respostas escritas: sem maiúsculas, sem acentos,
  /// sem espaços a mais. Uma criança de 6 anos não deve falhar por escrever
  /// "aviao" em vez de "avião".
  static String _norm(String s) {
    const de = 'áàâãäéèêëíìîïóòôõöúùûüçÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ';
    const para = 'aaaaaeeeeiiiiooooouuuucAAAAAEEEEIIIIOOOOOUUUUC';
    // O sinal de menos tem três formas que se parecem todas: o hífen do
    // teclado, o menos tipográfico (−) e o travessão. Quem escreve o
    // currículo usa o do meio; quem responde carrega no do teclado.
    var r = s.trim().toLowerCase().replaceAll('−', '-').replaceAll('–', '-');
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
    if (cur is QSequencia) return cur.certa(_ordem);
    if (cur is QGrupos) return cur.certa(_porGrupo);
    if (cur is QCenario) return cur.certa(_noCenario);
    if (cur is QGrelha) return cur.conta.certa(_casinhas);
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
      Sons.i.certo();
      // Acertou: sai da lista de revisão, se lá estava.
      st.marcarAprendida(q.q);
    } else {
      HapticFeedback.heavyImpact();
      Sons.i.errado();
      _abanao.forward(from: 0);
      // Errar a praticar não custa coração: quem está a falhar precisa de
      // mais treino, e tirar-lho seria fechar a porta a quem mais precisa.
      if (!widget.eAvulsa) st.perderVida();
      // Fica guardada para rever mais tarde no separador Guardados.
      st.marcarErrada(q.q);
    }
  }

  void _seguinte() {
    if (idx + 1 >= qs.length) {
      final st = context.read<AppState>();
      if (widget.eAvulsa) {
        // Treino e revisão também dão XP e contam para a sequência: o ecrã de
        // fim mostra "+XP ganho" e esse número tem de ser verdadeiro.
        st.concluirTreino(acertos);
        // A campanha fecha-se à parte: é ela que paga as sortes, e paga-as
        // uma vez só por semana.
        if (widget.campanha) st.concluirCampanha(acertos, qs.length);
      } else {
        st.concluirNivel(widget.indice, acertos, qs.length);
      }
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(
          builder: (_) => CompleteScreen(
            indice: widget.eAvulsa ? -1 : widget.indice,
            acertos: acertos,
            total: qs.length,
            titulo: widget.titulo,
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
    _lerEnunciado();
  }

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    return PopScope(
      // Sem isto, o botão de voltar fecha a app a meio da lição em vez de
      // fazer o que o ✕ faz. Perder a lição já é mau; perder a app é pior.
      canPop: false,
      onPopInvokedWithResult: (jaSaiu, _) {
        if (!jaSaiu) _confirmarSaida();
      },
      child: Scaffold(
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
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Expanded(
                    child: Text(
                      q.q,
                      style: const TextStyle(
                          fontSize: 19,
                          fontWeight: FontWeight.w600,
                          color: S.tx,
                          height: 1.25),
                    ),
                  ),
                  if (q.audio != null) ...[
                    const SizedBox(width: 8),
                    // Alvo generoso de propósito: dedos pequenos falham
                    // botões pequenos, e este é o que salva quem ainda não lê.
                    Semantics(
                      button: true,
                      label: 'Ouvir a pergunta outra vez',
                      child: InkWell(
                        onTap: _lerEnunciado,
                        borderRadius: BorderRadius.circular(24),
                        child: Container(
                          width: 46,
                          height: 46,
                          decoration: BoxDecoration(
                            color: S.surface2,
                            shape: BoxShape.circle,
                            border: Border.all(color: S.chart, width: 2),
                          ),
                          child: const Icon(Icons.volume_up_rounded,
                              color: S.chart, size: 24),
                        ),
                      ),
                    ),
                  ],
                ],
              ),
            ),
          ),
        ],
      );

  Widget _corpoQuestao() {
    final cur = q;
    final resposta = switch (cur) {
      QCount() => _vistaCount(cur),
      QChoice() => _opcoes(cur.options),
      QInput() => _vistaInput(),
      QMatch() => _vistaMatch(cur),
      QDrag() => _vistaDrag(cur),
      QGrelha() => _vistaGrelha(cur),
      QSequencia() => Padding(
        padding: const EdgeInsets.only(top: 4),
        child: OrdenarPassos(
          questao: cur,
          ordem: _ordem,
          corrigida: fase == Fase.responder ? null : fase == Fase.certo,
          aoMudar: (o) => setState(() => _ordem = o),
        ),
      ),
      QGrupos() => Padding(
        padding: const EdgeInsets.only(top: 4),
        child: ClassificarGrupos(
          questao: cur,
          posto: _porGrupo,
          corrigida: fase == Fase.responder ? null : fase == Fase.certo,
          aoMudar: (p) => setState(() => _porGrupo = p),
        ),
      ),
      QCenario() => Padding(
        padding: const EdgeInsets.only(top: 4),
        child: CenarioInteractivo(
          questao: cur,
          posto: _noCenario,
          corrigida: fase == Fase.responder ? null : fase == Fase.certo,
          aoMudar: (p) => setState(() => _noCenario = p),
        ),
      ),
    };

    final fig = cur.figura;
    final cor = cur.cores;
    if (fig == null && (cor == null || !cor.temMistura)) return resposta;

    // A figura e as tintas entram entre o enunciado e a resposta, que e onde
    // a crianca olha a seguir a ler a pergunta. "Um quadrado tem 5 cm de
    // lado" sem quadrado nenhum obriga-a a imagina-lo antes de poder pensar
    // nele; "amarelo mais azul" sem as tintas a vista ensina tres palavras
    // e nao uma cor.
    return Column(
      children: [
        if (fig != null) DesenhoGeometrico(figura: fig),
        if (cor != null && cor.temMistura) MostraCores(cores: cor),
        const SizedBox(height: 8),
        resposta,
      ],
    );
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

    final paleta = cur.cores?.opcoes ?? const <int>[];
    final gota = i < paleta.length ? Color(paleta[i]) : null;

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
              Sons.i.toque();
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
        child: Row(
          mainAxisSize: MainAxisSize.min,
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // A cor da resposta, quando a pergunta e de Educacao Visual. Vai
            // AO LADO do nome e nao em vez dele: assim a crianca escolhe
            // pela cor e fica a saber como ela se chama.
            if (gota != null) GotaDaOpcao(cor: gota),
            Flexible(
              child: Text(texto,
                  textAlign: TextAlign.center,
                  style: TextStyle(
                      fontSize: 18, fontWeight: FontWeight.w600, color: txt)),
            ),
          ],
        ),
      ),
    );
  }

  /// A resposta desta pergunta e um numero?
  ///
  /// Olha-se para a resposta certa e nao para o enunciado: e ela que diz o
  /// que se espera. Cento e dezassete das cento e cinquenta e uma respostas
  /// escritas do curriculo sao numeros.
  bool get _respostaENumero {
    final cur = q;
    return cur is QInput && RegExp(r'^-?\d+$').hasMatch(cur.a.trim());
  }

  /// A resposta certa é negativa. Só então aparece a tecla do sinal.
  bool get _respostaPodeSerNegativa {
    final cur = q;
    return cur is QInput && cur.a.trim().startsWith('-');
  }

  /// A conta armada, com o teclado por baixo.
  ///
  /// A grelha ocupa o lugar que noutras perguntas é das opções, e o teclado
  /// é o mesmo das respostas numéricas — uma criança que já sabe escrever
  /// um número aqui não tem nada de novo a aprender.
  Widget _vistaGrelha(QGrelha cur) => Padding(
    padding: const EdgeInsets.only(top: 8),
    child: Column(
      children: [
        GrelhaOperacao(
          key: _grelha,
          conta: cur.conta,
          respostas: _casinhas,
          corrigida: fase == Fase.responder ? null : fase == Fase.certo,
          aoMudar: (r) => setState(() => _casinhas = r),
        ),
        const SizedBox(height: 16),
        TecladoNumerico(
          activo: fase == Fase.responder,
          aoDigito: (d) => _grelha.currentState?.escrever(d),
          aoApagar: () => _grelha.currentState?.apagar(),
        ),
      ],
    ),
  );

  Widget _vistaInput() =>
      _respostaENumero ? _vistaNumero() : _vistaTexto();

  /// Resposta numerica: mostrador e teclado proprio, sem o teclado do
  /// sistema a tapar a pergunta.
  Widget _vistaNumero() => Padding(
    padding: const EdgeInsets.only(top: 8),
    child: Column(
      children: [
        MostradorDoNumero(
          valor: _input.text,
          erro: fase == Fase.errado,
        ),
        const SizedBox(height: 14),
        TecladoNumerico(
          activo: fase == Fase.responder,
          aoDigito: (d) {
            // Cinco algarismos chegam: a maior resposta do curriculo tem
            // quatro, e sem travao a crianca podia encher a caixa a brincar.
            // O sinal nao conta para o travao — senao um numero negativo
            // ficava com menos um algarismo do que um positivo.
            final algarismos = _input.text.replaceAll('-', '').length;
            if (algarismos >= 5) return;
            setState(() => _input.text = '${_input.text}$d');
          },
          aoApagar: () {
            if (_input.text.isEmpty) return;
            setState(() => _input.text =
                _input.text.substring(0, _input.text.length - 1));
          },
          aoSinal: _respostaPodeSerNegativa
              ? () => setState(() {
                    _input.text = _input.text.startsWith('-')
                        ? _input.text.substring(1)
                        : '-${_input.text}';
                  })
              : null,
        ),
      ],
    ),
  );

  Widget _vistaTexto() => Padding(
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
                      Row(
                        children: [
                          Flexible(
                            child: Text(_msgActual,
                                style: TextStyle(
                                    fontSize: 17,
                                    fontWeight: FontWeight.w700,
                                    color: certo ? S.chart : S.life)),
                          ),
                          // O XP só aparecia no fim da lição, longe do acerto
                          // que o mereceu. Na fase C as crianças acharam o
                          // jogo pouco recompensador, e esta é a recompensa
                          // mais barata que havia por dar: dizer, na hora,
                          // que aquela resposta valeu alguma coisa.
                          if (certo) ...[
                            const SizedBox(width: 8),
                            _MaisXp(
                              key: ValueKey(idx),
                              quanto: AppState.xpPorAcerto,
                            ),
                          ],
                        ],
                      ),
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
      QGrelha() => '${cur.conta.resultado}',
      QSequencia() => cur.passos.first,
      QGrupos() => '',
      QCenario() => '',
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

/// A pastilha "+10 XP" que salta ao lado do "Boa!".
///
/// Entra com mola e sobe um pouco: é curta de propósito, porque a seguir vem
/// o botão de continuar e o que se quer é impulso, não um espectáculo.
class _MaisXp extends StatelessWidget {
  final int quanto;
  const _MaisXp({super.key, required this.quanto});

  @override
  Widget build(BuildContext context) => TweenAnimationBuilder<double>(
    tween: Tween(begin: 0, end: 1),
    duration: const Duration(milliseconds: 520),
    curve: SCurves.spring,
    builder: (_, v, filho) => Opacity(
      opacity: v.clamp(0.0, 1.0),
      child: Transform.translate(
        offset: Offset(0, (1 - v) * 14),
        child: Transform.scale(scale: 0.6 + 0.4 * v, child: filho),
      ),
    ),
    child: Container(
      padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 3),
      decoration: BoxDecoration(
        color: S.chart.withValues(alpha: 0.16),
        borderRadius: BorderRadius.circular(S.rPill),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          const Icon(Icons.bolt_rounded, color: S.chart, size: 14),
          const SizedBox(width: 2),
          Text(
            '+$quanto',
            style: const TextStyle(
              color: S.chart,
              fontSize: 13.5,
              fontWeight: FontWeight.w800,
            ),
          ),
        ],
      ),
    ),
  );
}
