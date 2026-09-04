import 'package:flutter/material.dart';

import '../models/algoritmo_escrito.dart';
import '../services/sons.dart';
import '../theme.dart';

/// A conta armada, para a criança preencher.
///
/// Desenha o que o [GrelhaDaConta] descreve e não decide nada de
/// aritmética: se a conta estiver mal, o erro está no modelo e é lá que se
/// corrige. Aqui só se trata de dedos e de píxeis.
///
/// ## Duas regras de dedo que valem mais do que parecem
///
/// **Uma casinha de cada vez, e o cursor anda sozinho para a esquerda.** É a
/// ordem do algoritmo, e é ela que a escola ensina. Deixar escrever em
/// qualquer sítio parece mais livre e é pior: a criança escreve o resultado
/// da esquerda para a direita, como leria um número, e nunca aprende que a
/// conta se faz ao contrário.
///
/// **Quarenta e quatro píxeis de lado, no mínimo.** É o alvo de toque de um
/// dedo, e num telemóvel de 320 uma grelha de cinco ordens já não cabe a
/// encolher. A partir daí a grelha desliza na horizontal — mais vale ter de
/// arrastar do que ter casinhas onde não se acerta.
class GrelhaOperacao extends StatefulWidget {
  final GrelhaDaConta conta;

  /// O que a criança escreveu, por casinha (pela ordem de [aPreencher]).
  final List<String> respostas;

  /// Chamado sempre que uma casinha muda.
  final ValueChanged<List<String>> aoMudar;

  /// Depois de verificar, cada casinha ganha cor. Nulo enquanto ela ainda
  /// está a responder.
  final bool? corrigida;

  const GrelhaOperacao({
    super.key,
    required this.conta,
    required this.respostas,
    required this.aoMudar,
    this.corrigida,
  });

  /// Lado mínimo de uma casinha. É o alvo de toque, não uma preferência.
  static const ladoMinimo = 44.0;

  @override
  State<GrelhaOperacao> createState() => GrelhaOperacaoState();
}

class GrelhaOperacaoState extends State<GrelhaOperacao> {
  /// A casinha onde está o cursor, no índice de [GrelhaDaConta.aPreencher].
  int cursor = 0;

  /// O que está escrito, guardado AQUI e não lido da propriedade.
  ///
  /// Parece um pormenor e não é: a propriedade só se actualiza no fotograma
  /// seguinte, e dois toques dentro do mesmo fotograma liam os dois o valor
  /// velho — o segundo algarismo apagava o primeiro. Numa casinha de
  /// empréstimo, onde se escreve "13", isso tornava-a impossível de
  /// preencher.
  late List<String> _valores;

  List<Casa> get _alvo => widget.conta.aPreencher;

  @override
  void initState() {
    super.initState();
    _valores = _seed();
  }

  List<String> _seed() => [
    for (var i = 0; i < widget.conta.aPreencher.length; i++)
      i < widget.respostas.length ? widget.respostas[i] : '',
  ];

  @override
  void didUpdateWidget(GrelhaOperacao oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.conta != widget.conta) {
      cursor = 0;
      _valores = _seed();
    }
  }

  /// Escreve um algarismo na casinha do cursor.
  ///
  /// As casinhas de empréstimo levam dois algarismos (13, 10) e por isso
  /// aceitam um segundo toque; as outras avançam logo. É a diferença entre
  /// escrever "13" e ter de apagar para corrigir.
  void escrever(int digito) {
    if (cursor >= _alvo.length) return;
    final casa = _alvo[cursor];
    final cabe = casa.texto.length;
    final agora = _valor(cursor);

    final novo = agora.length < cabe ? '$agora$digito' : '$digito';
    _guardar(cursor, novo);
    if (novo.length >= cabe) avancar();
  }

  void apagar() {
    if (cursor >= _alvo.length) return;
    final agora = _valor(cursor);
    if (agora.isEmpty) {
      recuar();
      return;
    }
    _guardar(cursor, agora.substring(0, agora.length - 1));
  }

  void avancar() {
    if (cursor + 1 >= _alvo.length) return;
    setState(() => cursor++);
  }

  void recuar() {
    if (cursor == 0) return;
    setState(() => cursor--);
  }

  String _valor(int i) => i < _valores.length ? _valores[i] : '';

  void _guardar(int i, String v) {
    setState(() => _valores[i] = v);
    widget.aoMudar(List<String>.from(_valores));
  }

  @override
  Widget build(BuildContext context) {
    final g = widget.conta;
    final indices = <String, int>{
      for (var i = 0; i < _alvo.length; i++)
        '${_alvo[i].linha}:${_alvo[i].coluna}': i,
    };

    return LayoutBuilder(
      builder: (context, box) {
        // Encolhe até ao mínimo e não mais; daí para a frente desliza.
        final cabe = box.maxWidth / g.colunas;
        final lado = cabe < GrelhaOperacao.ladoMinimo
            ? GrelhaOperacao.ladoMinimo
            : (cabe > 62 ? 62.0 : cabe);
        final largura = lado * g.colunas;

        final tabela = SizedBox(
          width: largura,
          child: Stack(
            children: [
              Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  for (var l = 0; l < g.linhas; l++)
                    SizedBox(
                      height: lado,
                      child: Row(
                        children: [
                          for (var c = 0; c < g.colunas; c++)
                            _casa(g, l, c, lado, indices),
                        ],
                      ),
                    ),
                ],
              ),
              // Os traços por baixo das linhas certas, e a barra da divisão.
              Positioned.fill(
                child: IgnorePointer(
                  child: CustomPaint(
                    painter: _Riscos(conta: g, lado: lado),
                  ),
                ),
              ),
            ],
          ),
        );

        return SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          child: tabela,
        );
      },
    );
  }

  Widget _casa(
    GrelhaDaConta g,
    int linha,
    int coluna,
    double lado,
    Map<String, int> indices,
  ) {
    final casa = g.em(linha, coluna);
    if (casa == null) return SizedBox(width: lado, height: lado);

    if (!casa.porPreencher) {
      return SizedBox(
        width: lado,
        height: lado,
        child: Center(
          child: Text(
            casa.texto,
            style: TextStyle(
              fontSize: lado * 0.46,
              fontWeight: FontWeight.w700,
              color: casa.riscado ? S.txMut : S.tx,
              // O riscado é o que torna visível que aquele algarismo já não
              // vale o que lá está escrito. Sem ele, a criança lê o número
              // antigo e a conta deixa de fazer sentido.
              decoration: casa.riscado ? TextDecoration.lineThrough : null,
              decorationColor: S.life,
              decorationThickness: 2.5,
            ),
          ),
        ),
      );
    }

    final i = indices['$linha:$coluna']!;
    final texto = _valor(i);
    final noCursor = i == cursor && widget.corrigida == null;
    final corrigida = widget.corrigida != null && texto.isNotEmpty;
    final certa = corrigida && texto == casa.texto;
    final transporte = casa.papel == Papel.transporte;

    final cor = widget.corrigida == null
        ? (noCursor ? S.chart : S.line)
        : (texto.isEmpty ? S.life : (certa ? S.green300 : S.life));

    return GestureDetector(
      onTap: () {
        Sons.i.toque();
        setState(() => cursor = i);
      },
      child: Container(
        width: lado,
        height: lado,
        padding: const EdgeInsets.all(3),
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 140),
          decoration: BoxDecoration(
            color: widget.corrigida == null
                ? (noCursor ? S.chart.withValues(alpha: 0.16) : S.surface)
                : (certa
                      ? S.green500.withValues(alpha: 0.20)
                      : S.life.withValues(alpha: 0.18)),
            border: Border.all(color: cor, width: noCursor ? 2.5 : 1.5),
            borderRadius: BorderRadius.circular(S.rSm),
          ),
          alignment: Alignment.center,
          child: Text(
            texto,
            style: TextStyle(
              // O transporte escreve-se mais pequeno, como no caderno: é uma
              // nota de trabalho e não parte da resposta.
              fontSize: transporte ? lado * 0.34 : lado * 0.46,
              fontWeight: FontWeight.w700,
              color: widget.corrigida == null
                  ? (transporte ? S.gold : S.tx)
                  : (certa ? S.green300 : S.life),
            ),
          ),
        ),
      ),
    );
  }
}

/// Os traços da conta: os horizontais e a barra da divisão.
class _Riscos extends CustomPainter {
  final GrelhaDaConta conta;
  final double lado;

  const _Riscos({required this.conta, required this.lado});

  @override
  void paint(Canvas canvas, Size size) {
    final tinta = Paint()
      ..color = S.tx
      ..strokeWidth = 2.2
      ..strokeCap = StrokeCap.round;

    for (final t in conta.tracos) {
      final y = (t.linha + 1) * lado;
      canvas.drawLine(
        Offset(t.de * lado + 3, y),
        Offset((t.ate + 1) * lado - 3, y),
        tinta,
      );
    }

    final barra = conta.barra;
    if (barra != null) {
      final x = barra * lado + lado / 2;
      canvas.drawLine(Offset(x, 3), Offset(x, size.height - 3), tinta);
    }
  }

  @override
  bool shouldRepaint(_Riscos velho) =>
      velho.conta != conta || velho.lado != lado;
}
