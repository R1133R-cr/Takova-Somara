/// A mesa do Water R Sort: os frascos desenhados e o toque em cada um.
///
/// O jogo em si não está aqui — está em [Frascos], que é uma classe sem
/// ecrã nenhum e por isso se pode provar num teste. Este ficheiro só sabe
/// pintar o que lhe dão e dizer em que frasco a criança tocou.
library;

import 'dart:math' as math;

import 'package:flutter/foundation.dart' show listEquals;
import 'package:flutter/material.dart';

import '../models/frascos.dart';
import '../theme.dart';

/// Um despejo a meio caminho, para a mesa saber o que animar.
///
/// [t] anda de 0 a 1: o líquido desce no frasco de origem e sobe no de
/// destino ao mesmo tempo, e é por isso que os dois precisam do mesmo
/// número — se cada um contasse o seu, via-se líquido a desaparecer de um
/// lado antes de aparecer do outro.
typedef DespejoEmCurso = ({
  int de,
  int para,
  int quantos,
  CorDoLiquido cor,
  double t,
});

/// Onde fica cada frasco, dado o espaço que há.
///
/// Função pura e à parte para se poder medir num teste: um frasco que sai
/// pela borda fora num telemóvel de 320 é o defeito mais provável desta
/// mesa, e não se vê a olho num emulador grande.
///
/// Até cinco frascos vão numa linha. A partir daí vão em duas, porque dez
/// frascos lado a lado num ecrã estreito ficam com menos de trinta pixels
/// cada um — mais finos do que o dedo que lhes vai tocar.
List<Rect> disporFrascos(Size tamanho, int quantos, int altura) {
  if (quantos <= 0) return const [];

  final porLinha = quantos <= 5 ? quantos : (quantos / 2).ceil();
  final linhas = (quantos / porLinha).ceil();

  final vaoW = tamanho.width / porLinha;
  final vaoH = tamanho.height / linhas;

  // Um frasco é bastante mais alto do que largo, e a altura depende de
  // quantos blocos leva: os de cinco são mais compridos do que os de quatro.
  final razao = altura * 1.05 + 0.75;
  final larg = math.min(vaoW * 0.74, (vaoH * 0.84) / razao);
  final alt = larg * razao;

  return [
    for (var i = 0; i < quantos; i++) ...[
      () {
        final linha = i ~/ porLinha;
        final coluna = i % porLinha;
        // A última linha pode vir incompleta — nove frascos dão cinco e
        // quatro. Centra-se, senão ficava encostada à esquerda e a mesa
        // parecia torta.
        final nesta = math.min(porLinha, quantos - linha * porLinha);
        final sobra = (porLinha - nesta) * vaoW / 2;
        return Rect.fromCenter(
          center: Offset(
            sobra + coluna * vaoW + vaoW / 2,
            linha * vaoH + vaoH / 2,
          ),
          width: larg,
          height: alt,
        );
      }(),
    ],
  ];
}

/// Os frascos todos, dispostos e a responder ao toque.
class MesaDeFrascos extends StatelessWidget {
  final Frascos jogo;

  /// O frasco levantado à espera de destino.
  final int? seleccionado;

  final DespejoEmCurso? despejo;

  final void Function(int frasco) aoTocar;

  const MesaDeFrascos({
    super.key,
    required this.jogo,
    required this.seleccionado,
    required this.despejo,
    required this.aoTocar,
  });

  @override
  Widget build(BuildContext context) => LayoutBuilder(
    builder: (context, caixa) {
      final sitios = disporFrascos(
        Size(caixa.maxWidth, caixa.maxHeight),
        jogo.frascos.length,
        jogo.params.altura,
      );

      return Stack(
        children: [
          for (var i = 0; i < jogo.frascos.length; i++)
            _posto(i, sitios),
        ],
      );
    },
  );

  Widget _posto(int i, List<Rect> sitios) {
    final d = despejo;
    final origem = d != null && d.de == i;
    final destino = d != null && d.para == i;

    // Quantos blocos mostrar, com casas decimais: é o que faz o líquido
    // descer e subir sem saltos.
    var nivel = jogo.frascos[i].blocos.length.toDouble();
    var blocos = jogo.frascos[i].blocos;
    if (origem) {
      nivel -= d.quantos * d.t;
    } else if (destino) {
      // O destino já leva a cor nova na lista, mas só a mostra à medida
      // que ela chega.
      blocos = [...blocos, ...List.filled(d.quantos, d.cor)];
      nivel += d.quantos * d.t;
    }

    // Levantado quando está escolhido, e também quando está a despejar.
    final levantado = seleccionado == i || origem;

    // O frasco de origem inclina-se para o lado do destino. É o gesto que
    // diz à criança para onde é que aquilo foi.
    var angulo = 0.0;
    if (origem) {
      final paraDireita = sitios[d.para].center.dx >= sitios[d.de].center.dx;
      // Sobe e desce: no meio do despejo é onde está mais inclinado.
      final forca = math.sin(d.t * math.pi);
      angulo = (paraDireita ? 1 : -1) * 0.30 * forca;
    }

    return Positioned.fromRect(
      rect: sitios[i].translate(0, levantado ? -12 : 0),
      child: GestureDetector(
        key: ValueKey('frasco-$i'),
        behavior: HitTestBehavior.opaque,
        onTap: () => aoTocar(i),
        child: Transform.rotate(
          angle: angulo,
          alignment: Alignment.topCenter,
          child: CustomPaint(
            painter: _PintorDoFrasco(
              blocos: blocos,
              nivel: nivel,
              altura: jogo.params.altura,
              escolhido: seleccionado == i,
              aReceber: destino ? d.cor : null,
            ),
          ),
        ),
      ),
    );
  }
}

class _PintorDoFrasco extends CustomPainter {
  final List<CorDoLiquido> blocos;

  /// Quantos blocos mostrar, com casas decimais.
  final double nivel;

  final int altura;
  final bool escolhido;

  /// A cor que está a cair lá para dentro neste momento, se alguma.
  final CorDoLiquido? aReceber;

  _PintorDoFrasco({
    required this.blocos,
    required this.nivel,
    required this.altura,
    required this.escolhido,
    required this.aReceber,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final fora = Offset.zero & size;
    final parede = size.width * 0.085;
    final vidro = _corpo(fora);

    // O buraco por onde se despeja. Dá-lhe a volta redonda que faz o frasco
    // parecer um cilindro e não um rectângulo.
    final boca = Rect.fromCenter(
      center: Offset(size.width / 2, parede * 0.9),
      width: size.width - parede * 1.2,
      height: size.width * 0.30,
    );

    canvas.drawPath(vidro, Paint()..color = S.gm900.withValues(alpha: 0.55));

    final dentro = _corpo(fora.deflate(parede));
    final coluna = Rect.fromLTRB(
      fora.left + parede,
      boca.center.dy,
      fora.right - parede,
      fora.bottom - parede,
    );

    canvas.save();
    canvas.clipPath(dentro);
    _liquido(canvas, coluna);
    canvas.restore();

    // O jacto a cair, desenhado por cima do líquido e por baixo do vidro.
    final cor = aReceber;
    if (cor != null) {
      final fita = Rect.fromCenter(
        center: Offset(size.width / 2, coluna.top),
        width: size.width * 0.16,
        height: coluna.height * 0.5,
      );
      canvas.save();
      canvas.clipPath(dentro);
      canvas.drawRRect(
        RRect.fromRectAndRadius(fita, Radius.circular(fita.width / 2)),
        Paint()..color = Color(cor.valor).withValues(alpha: 0.75),
      );
      canvas.restore();
    }

    // O vidro por cima de tudo, para o líquido parecer estar lá dentro.
    canvas.drawPath(
      vidro,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = escolhido ? 3.2 : 2.0
        ..color = escolhido ? S.chart : S.line,
    );

    canvas.drawOval(
      boca,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = escolhido ? 2.6 : 1.8
        ..color = escolhido ? S.chart : S.line,
    );

    // Um brilho ao alto, do lado esquerdo. É o que dá a volta ao cilindro.
    canvas.drawRRect(
      RRect.fromRectAndRadius(
        Rect.fromLTWH(
          fora.left + parede * 1.5,
          coluna.top + coluna.height * 0.10,
          size.width * 0.09,
          coluna.height * 0.55,
        ),
        Radius.circular(size.width * 0.05),
      ),
      Paint()..color = Colors.white.withValues(alpha: 0.16),
    );
  }

  /// O contorno do frasco: quase direito em cima, redondo no fundo.
  Path _corpo(Rect r) => Path()
    ..addRRect(
      RRect.fromRectAndCorners(
        r,
        topLeft: Radius.circular(r.width * 0.16),
        topRight: Radius.circular(r.width * 0.16),
        bottomLeft: Radius.circular(r.width * 0.46),
        bottomRight: Radius.circular(r.width * 0.46),
      ),
    );

  /// As bandas de cor, de baixo para cima.
  void _liquido(Canvas canvas, Rect coluna) {
    final passo = coluna.height / altura;

    for (var i = 0; i < blocos.length; i++) {
      // Que fatia desta banda está preenchida: 1 nas de baixo, um valor
      // entre 0 e 1 na que está a encher ou a esvaziar.
      final fatia = (nivel - i).clamp(0.0, 1.0);
      if (fatia <= 0) break;

      final base = coluna.bottom - i * passo;
      final banda = Rect.fromLTRB(
        coluna.left,
        base - passo * fatia,
        coluna.right,
        base,
      );
      canvas.drawRect(banda, Paint()..color = Color(blocos[i].valor));

      // Um risco mais escuro no fundo de cada banda. Sem ele, quatro
      // vermelhos seguidos são uma mancha só e a criança não os consegue
      // contar — que é metade do que o jogo lhe pede para fazer.
      if (i > 0) {
        canvas.drawRect(
          Rect.fromLTRB(banda.left, banda.bottom - 1.5, banda.right,
              banda.bottom),
          Paint()..color = Colors.black.withValues(alpha: 0.22),
        );
      }
    }

    // A superfície do líquido, mais clara, a fazer de elipse vista de cima.
    if (nivel > 0 && blocos.isNotEmpty) {
      final topo = coluna.bottom - nivel.clamp(0, altura) * passo;
      final qual = math.min(nivel.ceil() - 1, blocos.length - 1);
      canvas.drawOval(
        Rect.fromCenter(
          center: Offset(coluna.center.dx, topo),
          width: coluna.width,
          height: coluna.width * 0.26,
        ),
        Paint()..color = Color(blocos[qual].valor).withValues(alpha: 0.55),
      );
    }
  }

  @override
  bool shouldRepaint(_PintorDoFrasco antigo) =>
      antigo.nivel != nivel ||
      antigo.escolhido != escolhido ||
      antigo.aReceber != aReceber ||
      !listEquals(antigo.blocos, blocos);
}
