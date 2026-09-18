/// A mesa do Water R Sort: os frascos desenhados, animados e a responder ao
/// toque e ao arrasto.
///
/// O jogo em si não está aqui — está em [Frascos], que é uma classe sem
/// ecrã nenhum e por isso se pode provar num teste. Este ficheiro só sabe
/// pintar o que lhe dão, animar um despejo, e dizer em que frasco a criança
/// tocou ou largou.
///
/// O «3D» é pintado, não calculado
/// -------------------------------
/// Um motor de 3D a sério era uma dependência nova e pesada, ainda mal
/// suportada nos telemóveis baratos que esta app tem de servir. O que dá a
/// volta ao cilindro é o que a dá em qualquer desenho: uma elipse na boca,
/// um degradé de lado a lado no vidro e no líquido, a superfície do líquido
/// em elipse mais clara, e a fronteira entre duas cores em elipse mais
/// escura. Vê-se um frasco redondo e não há um único vértice.
///
/// O líquido obedece à gravidade
/// -----------------------------
/// Quando o frasco se inclina para despejar, o líquido NÃO roda com ele: a
/// superfície fica horizontal e o líquido escorre para a boca, como num
/// copo de verdade. É a diferença entre uma animação que se acredita e uma
/// que se vê que é desenho. Está feito com contas simples — cada camada de
/// cor é o rectângulo do interior cortado por dois planos horizontais, e a
/// altura de cada plano acha-se por bissecção para a área bater com o
/// volume da camada.
library;

import 'dart:math' as math;

import 'package:flutter/foundation.dart' show listEquals;
import 'package:flutter/material.dart';

import '../models/frascos.dart';
import '../theme.dart';

/// Um despejo a meio caminho.
///
/// [t] anda de 0 a 1 e tem três fases, e é a mesa que as conhece, não o
/// ecrã: primeiro o frasco VIAJA até ficar por cima do destino, depois
/// VIRA-SE e o líquido passa, e por fim VOLTA ao seu lugar. É o gesto que
/// uma pessoa faz com um copo, e é isso que a criança reconhece.
///
/// [desde] é de onde o frasco parte quando foi arrastado até lá: sem isso
/// ele saltava do dedo para o seu lugar antes de começar a viagem.
typedef DespejoEmCurso = ({
  int de,
  int para,
  int quantos,
  CorDoLiquido cor,
  double t,
  Offset? desde,
});

/// Um frasco preso ao dedo.
typedef Arrasto = ({int frasco, Offset centro});

/// O brilho de um frasco que acabou de ficar arrumado.
typedef Brilho = ({int frasco, double t});

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
  final razao = altura * 1.05 + 0.85;
  final larg = math.min(vaoW * 0.72, (vaoH * 0.84) / razao);
  final alt = larg * razao;

  return [
    for (var i = 0; i < quantos; i++)
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
  ];
}

/// As medidas de um frasco desenhado num rectângulo.
///
/// Partilhadas entre quem pinta o frasco e quem pinta o jacto por cima: o
/// jacto tem de cair exactamente na superfície do líquido, e a superfície
/// é esta conta.
class _Geometria {
  final double w, h, parede, boca, topo, fundo;

  _Geometria(Size s)
      : w = s.width,
        h = s.height,
        parede = s.width * 0.085,
        boca = s.width * 0.36,
        topo = s.width * 0.36 / 2 + s.width * 0.085 * 0.35,
        fundo = s.height - s.width * 0.085 * 1.15;

  /// O y da superfície com o frasco direito, para [altura] blocos de
  /// capacidade e [nivel] blocos de líquido — com casas decimais.
  double superficie(int altura, double nivel) =>
      fundo - nivel.clamp(0, altura) * ((fundo - topo) / altura);

  /// O interior onde o líquido cabe, como quatro cantos.
  List<Offset> get cantos => [
        Offset(parede, topo),
        Offset(w - parede, topo),
        Offset(w - parede, fundo),
        Offset(parede, fundo),
      ];
}

/// Onde fica a superfície do líquido de um frasco direito, em coordenadas
/// da mesa.
Offset superficieDe(Rect r, int altura, double nivel) => Offset(
      r.center.dx,
      r.top + _Geometria(r.size).superficie(altura, nivel),
    );

// As três fases do despejo, em fracções do tempo total.
const _fimDaViagem = 0.26;
const _fimDoVerter = 0.80;

/// Quanto o frasco vira ao despejar: mais de um ângulo recto, para a boca
/// ficar mais baixa do que o fundo — sem isso o líquido, que obedece à
/// gravidade, não sairia.
const _viragem = 1.95;

/// De 0 a 1 dentro da fase de verter.
double _faseDeVerter(double t) =>
    ((t - _fimDaViagem) / (_fimDoVerter - _fimDaViagem)).clamp(0.0, 1.0);

/// O ângulo do frasco de origem ao longo do despejo, sem sinal.
///
/// Começa a virar ainda em viagem e acaba de endireitar já a voltar: assim
/// nunca está direito em cima do destino, onde ficaria a tapá-lo.
double _anguloEm(double t) {
  if (t < _fimDaViagem) {
    final f = ((t - 0.08) / (_fimDaViagem - 0.08)).clamp(0.0, 1.0);
    return 0.35 * _viragem * Curves.easeIn.transform(f);
  }
  if (t < _fimDoVerter) {
    return _viragem * (0.35 + 0.65 * math.sin(_faseDeVerter(t) * math.pi));
  }
  final f = ((t - _fimDoVerter) / (1 - _fimDoVerter)).clamp(0.0, 1.0);
  return 0.35 * _viragem * (1 - Curves.easeOut.transform(f));
}

/// Quanto do líquido já passou, de 0 a 1. Só corre com a boca em baixo —
/// não antes de virar nem depois de se endireitar.
double _liquidoPassado(double t) {
  final f = _faseDeVerter(t);
  return Curves.easeInOut.transform(((f - 0.28) / 0.46).clamp(0.0, 1.0));
}

/// Os frascos todos, dispostos, animados e a responder ao toque.
class MesaDeFrascos extends StatefulWidget {
  final Frascos jogo;

  /// O frasco levantado à espera de destino.
  final int? seleccionado;

  final DespejoEmCurso? despejo;
  final Arrasto? arrasto;

  /// O frasco por baixo do dedo durante um arrasto, e se o despejo para lá
  /// vale — é o que pinta o realce verde ou vermelho.
  final int? alvo;
  final bool alvoServe;

  final Brilho? brilho;

  final void Function(int frasco) aoTocar;

  /// Chamado a cada movimento do dedo com o frasco preso. Nulo desliga o
  /// arrasto e fica só o toque.
  final void Function(int frasco, Offset centro, int? alvo)? aoArrastar;
  final void Function(int frasco, int? alvo)? aoLargar;

  const MesaDeFrascos({
    super.key,
    required this.jogo,
    required this.seleccionado,
    required this.despejo,
    required this.aoTocar,
    this.arrasto,
    this.alvo,
    this.alvoServe = false,
    this.brilho,
    this.aoArrastar,
    this.aoLargar,
  });

  @override
  State<MesaDeFrascos> createState() => _MesaDeFrascosState();
}

class _MesaDeFrascosState extends State<MesaDeFrascos> {
  final _caixa = GlobalKey();

  /// Levantado quando escolhido. Catorze pixels: chega para se ver, não
  /// chega para tapar o frasco de cima na segunda linha.
  static const _levantar = 14.0;

  Offset _local(Offset global) {
    final caixa = _caixa.currentContext?.findRenderObject() as RenderBox?;
    return caixa == null ? global : caixa.globalToLocal(global);
  }

  int? _frascoEm(Offset p, List<Rect> sitios, {int? excepto}) {
    for (var i = 0; i < sitios.length; i++) {
      if (i == excepto) continue;
      if (sitios[i].inflate(6).contains(p)) return i;
    }
    return null;
  }

  @override
  Widget build(BuildContext context) => LayoutBuilder(
        builder: (context, caixa) {
          final tamanho = Size(caixa.maxWidth, caixa.maxHeight);
          final sitios = disporFrascos(
            tamanho,
            widget.jogo.frascos.length,
            widget.jogo.params.altura,
          );
          final actuais = [
            for (var i = 0; i < sitios.length; i++)
              _rectActual(i, sitios, tamanho),
          ];

          // O frasco activo — arrastado ou a despejar — fica por cima de
          // todos: é o único que atravessa os outros.
          final ordem = [for (var i = 0; i < sitios.length; i++) i];
          final activo = widget.arrasto?.frasco ?? widget.despejo?.de;
          if (activo != null) {
            ordem
              ..remove(activo)
              ..add(activo);
          }

          return SizedBox.expand(
            key: _caixa,
            child: Stack(
              clipBehavior: Clip.none,
              children: [
                for (final i in ordem) _posto(i, sitios, actuais, tamanho),
                Positioned.fill(
                  child: IgnorePointer(
                    child: CustomPaint(
                      painter: _PintorDosEfeitos(
                        jogo: widget.jogo,
                        rects: actuais,
                        despejo: widget.despejo,
                        brilho: widget.brilho,
                        verteParaADireita: widget.despejo == null
                            ? true
                            : _verteParaADireita(
                                sitios[widget.despejo!.para], tamanho),
                      ),
                    ),
                  ),
                ),
              ],
            ),
          );
        },
      );

  /// Despeja-se para o lado onde há mesa. O frasco de origem, virado, fica
  /// com o corpo para o lado contrário à boca: se o destino está na metade
  /// direita, o corpo vai para a esquerda, onde cabe.
  static bool _verteParaADireita(Rect destino, Size mesa) =>
      destino.center.dx >= mesa.width / 2;

  /// O sítio de um frasco NESTE instante: no lugar, levantado, preso ao
  /// dedo, ou a meio da viagem de um despejo.
  Rect _rectActual(int i, List<Rect> sitios, Size mesa) {
    final lugar = sitios[i];
    final d = widget.despejo;
    if (d != null && d.de == i) return _rectDaOrigem(d, sitios, mesa);

    final a = widget.arrasto;
    if (a != null && a.frasco == i) {
      return Rect.fromCenter(
        center: a.centro,
        width: lugar.width * 1.06,
        height: lugar.height * 1.06,
      );
    }
    if (widget.seleccionado == i) return lugar.translate(0, -_levantar);
    return lugar;
  }

  /// A viagem do frasco de origem: do seu lugar (ou do dedo) até pousar
  /// com a boca por cima do destino, e de volta.
  Rect _rectDaOrigem(DespejoEmCurso d, List<Rect> sitios, Size mesa) {
    final lugar = sitios[d.de];
    final destino = sitios[d.para];
    final inicio = d.desde == null
        ? lugar.translate(0, -_levantar)
        : Rect.fromCenter(
            center: d.desde!,
            width: lugar.width * 1.06,
            height: lugar.height * 1.06,
          );
    final poiso = _poiso(lugar, destino, mesa);

    if (d.t < _fimDaViagem) {
      final f = Curves.easeOutCubic.transform(d.t / _fimDaViagem);
      return Rect.lerp(inicio, poiso, f)!;
    }
    if (d.t < _fimDoVerter) return poiso;
    final f = Curves.easeInOutCubic
        .transform((d.t - _fimDoVerter) / (1 - _fimDoVerter));
    return Rect.lerp(poiso, lugar, f)!;
  }

  /// Onde o frasco pousa para despejar. O que se fixa é o EIXO da viragem —
  /// o canto da boca por onde o líquido sai —, um bocado acima da boca do
  /// destino. O rectângulo é o que resulta de pendurar o frasco nesse
  /// canto; quando ele vira, o corpo sobe para o lado e sai da frente.
  Rect _poiso(Rect lugar, Rect destino, Size mesa) {
    final w = lugar.width, h = lugar.height;
    final direita = _verteParaADireita(destino, mesa);
    final eixo = Offset(
      destino.center.dx + (direita ? -0.10 : 0.10) * w,
      destino.top - h * 0.30,
    );
    return direita
        ? Rect.fromLTWH(eixo.dx - w, eixo.dy, w, h)
        : Rect.fromLTWH(eixo.dx, eixo.dy, w, h);
  }

  Widget _posto(int i, List<Rect> sitios, List<Rect> actuais, Size mesa) {
    final d = widget.despejo;
    final origem = d != null && d.de == i;
    final destino = d != null && d.para == i;

    // Quantos blocos mostrar, com casas decimais: é o que faz o líquido
    // descer num frasco e subir no outro sem saltos.
    var nivel = widget.jogo.frascos[i].blocos.length.toDouble();
    var blocos = widget.jogo.frascos[i].blocos;
    final passou = d == null ? 0.0 : _liquidoPassado(d.t);
    if (origem) {
      nivel -= d.quantos * passou;
    } else if (destino) {
      // O destino já leva a cor nova na lista, mas só a mostra à medida
      // que ela chega.
      blocos = [...blocos, ...List.filled(d.quantos, d.cor)];
      nivel += d.quantos * passou;
    }

    // O frasco de origem vira com o canto da boca a fazer de eixo — como
    // quem despeja um copo. É o gesto que diz à criança para onde é que
    // aquilo foi.
    var angulo = 0.0;
    var eixo = Alignment.topCenter;
    if (origem) {
      final direita = _verteParaADireita(sitios[d.para], mesa);
      angulo = (direita ? 1 : -1) * _anguloEm(d.t);
      eixo = direita ? Alignment.topRight : Alignment.topLeft;
    }

    final realce = widget.alvo == i && widget.arrasto != null
        ? (widget.alvoServe ? _Realce.bom : _Realce.mau)
        : _Realce.nenhum;

    final ondulacao = destino ? _faseDeVerter(d.t) : -1.0;

    return Positioned.fromRect(
      rect: actuais[i],
      child: GestureDetector(
        key: ValueKey('frasco-$i'),
        behavior: HitTestBehavior.opaque,
        onTap: () => widget.aoTocar(i),
        onPanStart: widget.aoArrastar == null
            ? null
            : (g) => _arrastar(i, g.globalPosition, sitios),
        onPanUpdate: widget.aoArrastar == null
            ? null
            : (g) => _arrastar(i, g.globalPosition, sitios),
        onPanEnd: widget.aoLargar == null ? null : (_) => _largar(i, sitios),
        onPanCancel: widget.aoLargar == null ? null : () => _largar(i, sitios),
        child: Transform.rotate(
          angle: angulo,
          alignment: eixo,
          child: CustomPaint(
            painter: _PintorDoFrasco(
              blocos: blocos,
              nivel: nivel,
              altura: widget.jogo.params.altura,
              inclinacao: angulo,
              escolhido: widget.seleccionado == i,
              arrumado: widget.jogo.frascos[i].cheio &&
                  widget.jogo.frascos[i].deUmaCor &&
                  !origem,
              realce: realce,
              ondulacao: ondulacao,
              preso: widget.arrasto?.frasco == i,
            ),
          ),
        ),
      ),
    );
  }

  Offset? _ultimoDedo;

  void _arrastar(int i, Offset global, List<Rect> sitios) {
    final dedo = _local(global);
    _ultimoDedo = dedo;
    // O frasco fica um bocado acima do dedo, senão o dedo tapa-o e a
    // criança não vê o que está a arrastar.
    final centro = dedo + Offset(0, -sitios[i].height * 0.35);
    widget.aoArrastar!(i, centro, _frascoEm(dedo, sitios, excepto: i));
  }

  void _largar(int i, List<Rect> sitios) {
    final dedo = _ultimoDedo;
    _ultimoDedo = null;
    widget.aoLargar!(
        i, dedo == null ? null : _frascoEm(dedo, sitios, excepto: i));
  }
}

enum _Realce { nenhum, bom, mau }

Color _tom(Color c, double delta) {
  final h = HSLColor.fromColor(c);
  return h.withLightness((h.lightness + delta).clamp(0.0, 1.0)).toColor();
}

// ------------------------------------------------------------- geometria

double _produto(Offset a, Offset b) => a.dx * b.dx + a.dy * b.dy;

/// Corta um polígono convexo por um plano: fica o lado onde `p·n − c` tem
/// o sinal pedido.
List<Offset> _cortar(List<Offset> poligono, Offset n, double c,
    {required bool manterMaior}) {
  final fora = <Offset>[];
  for (var i = 0; i < poligono.length; i++) {
    final a = poligono[i], b = poligono[(i + 1) % poligono.length];
    final da = _produto(a, n) - c, db = _produto(b, n) - c;
    final dentroA = manterMaior ? da >= 0 : da <= 0;
    final dentroB = manterMaior ? db >= 0 : db <= 0;
    if (dentroA) fora.add(a);
    if (dentroA != dentroB) {
      final t = da / (da - db);
      fora.add(Offset(a.dx + (b.dx - a.dx) * t, a.dy + (b.dy - a.dy) * t));
    }
  }
  return fora;
}

double _areaDe(List<Offset> p) {
  var soma = 0.0;
  for (var i = 0; i < p.length; i++) {
    final a = p[i], b = p[(i + 1) % p.length];
    soma += a.dx * b.dy - b.dx * a.dy;
  }
  return soma.abs() / 2;
}

/// A cota `c` (ao longo de [baixo]) abaixo da qual está a [fraccao] do
/// interior. Por bissecção: a área que fica de um lado do plano é uma
/// função monótona de onde o plano está.
double _cota(List<Offset> interior, Offset baixo, double fraccao) {
  var lo = double.infinity, hi = double.negativeInfinity;
  for (final p in interior) {
    final v = _produto(p, baixo);
    lo = math.min(lo, v);
    hi = math.max(hi, v);
  }
  if (fraccao <= 0) return hi;
  if (fraccao >= 1) return lo;
  final alvo = fraccao * _areaDe(interior);
  for (var i = 0; i < 20; i++) {
    final meio = (lo + hi) / 2;
    final area = _areaDe(_cortar(interior, baixo, meio, manterMaior: true));
    if (area > alvo) {
      lo = meio;
    } else {
      hi = meio;
    }
  }
  return (lo + hi) / 2;
}

/// Os dois pontos onde o plano `p·n = c` atravessa o polígono.
List<Offset> _travessia(List<Offset> poligono, Offset n, double c) {
  final pontos = <Offset>[];
  for (var i = 0; i < poligono.length; i++) {
    final a = poligono[i], b = poligono[(i + 1) % poligono.length];
    final da = _produto(a, n) - c, db = _produto(b, n) - c;
    if ((da >= 0) != (db >= 0)) {
      final t = da / (da - db);
      pontos.add(Offset(a.dx + (b.dx - a.dx) * t, a.dy + (b.dy - a.dy) * t));
    }
  }
  return pontos;
}

class _PintorDoFrasco extends CustomPainter {
  final List<CorDoLiquido> blocos;
  final double nivel;
  final int altura;

  /// O ângulo a que o frasco está virado, o mesmo do `Transform.rotate`
  /// que o roda. É com ele que o líquido sabe para onde é «para baixo».
  final double inclinacao;

  final bool escolhido;
  final bool arrumado;
  final _Realce realce;

  /// Fase da ondulação na superfície enquanto recebe líquido; negativa
  /// quando não está a receber.
  final double ondulacao;

  final bool preso;

  _PintorDoFrasco({
    required this.blocos,
    required this.nivel,
    required this.altura,
    required this.inclinacao,
    required this.escolhido,
    required this.arrumado,
    required this.realce,
    required this.ondulacao,
    required this.preso,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final g = _Geometria(size);
    final w = g.w;
    final boca = Rect.fromLTWH(0, 0, w, g.boca);
    final corpo = _corpo(g, 0);
    final dentro = _corpo(g, g.parede);

    // Sombra no chão. Mais funda quando o frasco está levantado ou preso ao
    // dedo — é o que diz que ele saiu da mesa.
    final alturaDaSombra = preso ? 14.0 : (escolhido ? 9.0 : 5.0);
    canvas.drawPath(
      corpo.shift(Offset(0, alturaDaSombra)),
      Paint()
        ..color = Colors.black.withValues(alpha: preso ? 0.45 : 0.32)
        ..maskFilter = MaskFilter.blur(BlurStyle.normal, preso ? 10 : 6),
    );

    // A parede de trás da boca: vê-se por dentro, e é mais escura.
    canvas.drawOval(boca, Paint()..color = const Color(0xFF001A1F));

    // O vidro. O degradé de lado a lado é o que faz o cilindro: claro
    // perto da esquerda, onde bate a luz, escuro nas bordas.
    canvas.drawPath(
      corpo,
      Paint()
        ..shader = LinearGradient(
          colors: [
            Colors.white.withValues(alpha: 0.05),
            Colors.white.withValues(alpha: 0.16),
            Colors.white.withValues(alpha: 0.06),
            Colors.white.withValues(alpha: 0.03),
            Colors.white.withValues(alpha: 0.10),
          ],
          stops: const [0, 0.22, 0.5, 0.85, 1],
        ).createShader(Offset.zero & size),
    );

    canvas.save();
    canvas.clipPath(dentro);
    _liquido(canvas, g);
    canvas.restore();

    // Reflexo ao alto, do lado esquerdo. É o brilho do vidro por cima do
    // líquido, e é o que dá a volta.
    canvas.drawRRect(
      RRect.fromRectAndRadius(
        Rect.fromLTWH(g.parede * 1.6, g.topo + (g.fundo - g.topo) * 0.06,
            w * 0.09, (g.fundo - g.topo) * 0.62),
        Radius.circular(w * 0.05),
      ),
      Paint()..color = Colors.white.withValues(alpha: 0.20),
    );

    // O contorno e a boca por cima de tudo, para o líquido parecer estar
    // lá dentro e não pintado por cima.
    final corDoContorno = switch (realce) {
      _Realce.bom => S.green300,
      _Realce.mau => S.life,
      _Realce.nenhum => escolhido
          ? S.chart
          : (arrumado ? S.green300 : Colors.white.withValues(alpha: 0.42)),
    };
    final grossura = escolhido || realce != _Realce.nenhum ? 2.8 : 1.7;

    if (escolhido || realce != _Realce.nenhum) {
      canvas.drawPath(
        corpo,
        Paint()
          ..style = PaintingStyle.stroke
          ..strokeWidth = 7
          ..color = corDoContorno.withValues(alpha: 0.35)
          ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 6),
      );
    }
    canvas.drawPath(
      corpo,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = grossura
        ..color = corDoContorno,
    );
    canvas.drawOval(
      boca,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = grossura
        ..color = corDoContorno,
    );
    // A metade da frente da boca, mais grossa: é a que está mais perto.
    canvas.drawArc(
      boca,
      0,
      math.pi,
      false,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = grossura + 1.2
        ..color = corDoContorno,
    );

    if (arrumado) _tampa(canvas, g);
  }

  /// O contorno do frasco: direito dos lados, redondo no fundo, e a começar
  /// a meio da boca — a metade de cima da elipse fica à vista por trás.
  Path _corpo(_Geometria g, double recuo) {
    final r = g.w / 2 - recuo;
    return Path()
      ..moveTo(recuo, g.boca / 2)
      ..lineTo(recuo, g.h - g.w / 2)
      ..arcToPoint(
        Offset(g.w - recuo, g.h - g.w / 2),
        radius: Radius.circular(r),
        clockwise: false,
      )
      ..lineTo(g.w - recuo, g.boca / 2)
      ..close();
  }

  /// As camadas de cor, de baixo para cima, niveladas com a gravidade.
  ///
  /// «Para baixo» em coordenadas do frasco é o mundo a rodar ao contrário
  /// da inclinação: com o frasco direito é (0, 1); virado de lado é quase
  /// (1, 0), e o líquido encosta-se à parede que ficou por baixo.
  void _liquido(Canvas canvas, _Geometria g) {
    final baixo = Offset(math.sin(inclinacao), math.cos(inclinacao));
    final interior = g.cantos;
    final elipse = g.boca * 0.92;

    var cotaDeBaixo = _cota(interior, baixo, 0);
    var cotaDoTopo = cotaDeBaixo;
    CorDoLiquido? corDoTopo;

    for (var i = 0; i < blocos.length; i++) {
      // Que fatia desta camada está preenchida: 1 nas de baixo, um valor
      // entre 0 e 1 na que está a encher ou a esvaziar.
      final fatia = (nivel - i).clamp(0.0, 1.0);
      if (fatia <= 0) break;

      final cor = Color(blocos[i].valor);
      cotaDoTopo = _cota(interior, baixo, (i + fatia) / altura);
      corDoTopo = blocos[i];

      final camada = _cortar(
        _cortar(interior, baixo, cotaDoTopo, manterMaior: true),
        baixo,
        cotaDeBaixo,
        manterMaior: false,
      );
      if (camada.length >= 3) {
        final caminho = Path()..addPolygon(camada, true);
        final caixa = caminho.getBounds();
        canvas.drawPath(
          caminho,
          Paint()
            ..shader = LinearGradient(
              colors: [
                _tom(cor, -0.16),
                _tom(cor, 0.09),
                cor,
                _tom(cor, -0.22),
              ],
              stops: const [0, 0.28, 0.6, 1],
            ).createShader(caixa),
        );
      }

      // A elipse no cimo de cada camada, mais escura. A camada seguinte
      // tapa a metade de cima e sobra o arco da frente — é a fronteira
      // curva entre duas cores, e é também o que permite contar os blocos.
      _elipseNaCota(canvas, interior, baixo, cotaDoTopo, elipse,
          Paint()..color = _tom(cor, -0.13));

      cotaDeBaixo = cotaDoTopo;
    }

    // A superfície: a elipse mais clara, com uma orla, por cima da última
    // elipse escura.
    if (nivel > 0 && corDoTopo != null) {
      final cor = Color(corDoTopo.valor);
      _elipseNaCota(canvas, interior, baixo, cotaDoTopo, elipse,
          Paint()..color = _tom(cor, 0.17));
      _elipseNaCota(
        canvas,
        interior,
        baixo,
        cotaDoTopo,
        elipse,
        Paint()
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1.2
          ..color = _tom(cor, -0.08),
      );
      // Um reflexo pequeno na superfície, e as ondas de quem está a
      // receber líquido: anéis que nascem no meio e crescem até à borda.
      _elipseNaCota(canvas, interior, baixo, cotaDoTopo, elipse * 0.28,
          Paint()..color = Colors.white.withValues(alpha: 0.32),
          escala: 0.32, desvio: -0.10);
      if (ondulacao >= 0) {
        for (var k = 0; k < 2; k++) {
          final f = (ondulacao * 2.2 + k * 0.5) % 1.0;
          _elipseNaCota(
            canvas,
            interior,
            baixo,
            cotaDoTopo,
            elipse * (0.15 + 0.85 * f),
            Paint()
              ..style = PaintingStyle.stroke
              ..strokeWidth = 1.6
              ..color = Colors.white.withValues(alpha: 0.55 * (1 - f)),
            escala: 0.15 + 0.85 * f,
          );
        }
      }
    }
  }

  /// Uma elipse deitada sobre o plano `p·baixo = cota`, tão larga quanto o
  /// interior nesse sítio. Com o frasco direito é a elipse de sempre; com o
  /// frasco virado inclina-se para ficar horizontal no mundo.
  void _elipseNaCota(
    Canvas canvas,
    List<Offset> interior,
    Offset baixo,
    double cota,
    double alturaDaElipse,
    Paint tinta, {
    double escala = 1,
    double desvio = 0,
  }) {
    final pontos = _travessia(interior, baixo, cota);
    if (pontos.length < 2) return;
    final a = pontos[0], b = pontos[1];
    final meio = Offset((a.dx + b.dx) / 2, (a.dy + b.dy) / 2);
    final comprimento = (b - a).distance;
    final direccao = math.atan2(b.dy - a.dy, b.dx - a.dx);

    canvas.save();
    canvas.translate(meio.dx, meio.dy);
    canvas.rotate(direccao);
    canvas.drawOval(
      Rect.fromCenter(
        center: Offset(comprimento * desvio, 0),
        width: comprimento * escala,
        height: alturaDaElipse,
      ),
      tinta,
    );
    canvas.restore();
  }

  /// A tampa de um frasco arrumado. É a maneira de dizer «este está feito»
  /// sem escrever nada: fecha-se.
  void _tampa(Canvas canvas, _Geometria g) {
    final tampa = RRect.fromRectAndRadius(
      Rect.fromLTWH(g.w * 0.16, 0, g.w * 0.68, g.boca * 0.78),
      Radius.circular(g.w * 0.12),
    );
    canvas.drawRRect(tampa, Paint()..color = S.green500);
    canvas.drawRRect(
      RRect.fromRectAndRadius(
        Rect.fromLTWH(g.w * 0.16, 0, g.w * 0.68, g.boca * 0.30),
        Radius.circular(g.w * 0.12),
      ),
      Paint()..color = S.green300.withValues(alpha: 0.75),
    );
  }

  @override
  bool shouldRepaint(_PintorDoFrasco antigo) =>
      antigo.nivel != nivel ||
      antigo.inclinacao != inclinacao ||
      antigo.escolhido != escolhido ||
      antigo.arrumado != arrumado ||
      antigo.realce != realce ||
      antigo.ondulacao != ondulacao ||
      antigo.preso != preso ||
      !listEquals(antigo.blocos, blocos);
}

/// O que se pinta por cima de todos os frascos: o jacto de um despejo e o
/// brilho de um frasco que acabou de fechar.
class _PintorDosEfeitos extends CustomPainter {
  final Frascos jogo;
  final List<Rect> rects;
  final DespejoEmCurso? despejo;
  final Brilho? brilho;
  final bool verteParaADireita;

  _PintorDosEfeitos({
    required this.jogo,
    required this.rects,
    required this.despejo,
    required this.brilho,
    required this.verteParaADireita,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final d = despejo;
    if (d != null) _jacto(canvas, d);
    final b = brilho;
    if (b != null && b.frasco < rects.length) _brilhar(canvas, b);
  }

  /// O líquido no ar: uma curva do canto da boca do frasco virado até à
  /// superfície do destino, com o miolo mais claro.
  void _jacto(Canvas canvas, DespejoEmCurso d) {
    final fase = _faseDeVerter(d.t);
    // Só enquanto o líquido passa, e a aparecer e a desaparecer com
    // suavidade nas pontas.
    final visivel = math
        .min(1.0, math.min(fase - 0.24, 0.78 - fase) / 0.06)
        .clamp(0.0, 1.0);
    if (visivel <= 0) return;

    final origem = rects[d.de], destino = rects[d.para];
    final g = _Geometria(origem.size);

    // O eixo da viragem é um canto de cima do rectângulo e não se mexe. A
    // boca de verdade está uns pixels para dentro; roda-se esse desvio
    // pelo mesmo ângulo do frasco.
    final angulo = (verteParaADireita ? 1 : -1) * _anguloEm(d.t);
    final eixo = verteParaADireita ? origem.topRight : origem.topLeft;
    final desvio = Offset(
      verteParaADireita ? -g.parede : g.parede,
      g.boca * 0.5,
    );
    final rodado = Offset(
      desvio.dx * math.cos(angulo) - desvio.dy * math.sin(angulo),
      desvio.dx * math.sin(angulo) + desvio.dy * math.cos(angulo),
    );
    final boca = eixo + rodado;

    final nivelDoDestino =
        jogo.frascos[d.para].blocos.length + d.quantos * _liquidoPassado(d.t);
    final alvo = superficieDe(destino, jogo.params.altura, nivelDoDestino);

    final controlo = Offset(
      boca.dx + (alvo.dx - boca.dx) * 0.15,
      boca.dy + (alvo.dy - boca.dy) * 0.40,
    );
    final caminho = Path()
      ..moveTo(boca.dx, boca.dy)
      ..quadraticBezierTo(controlo.dx, controlo.dy, alvo.dx, alvo.dy);

    final cor = Color(d.cor.valor);
    canvas.drawPath(
      caminho,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeCap = StrokeCap.round
        ..strokeWidth = g.w * 0.20
        ..color = cor.withValues(alpha: 0.92 * visivel),
    );
    canvas.drawPath(
      caminho,
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeCap = StrokeCap.round
        ..strokeWidth = g.w * 0.07
        ..color = _tom(cor, 0.22).withValues(alpha: 0.8 * visivel),
    );

    // Uns pingos à volta do sítio onde cai.
    final r = math.Random(d.de * 31 + d.para);
    for (var k = 0; k < 5; k++) {
      final a = r.nextDouble() * math.pi * 2;
      final dist = g.w * (0.18 + 0.30 * r.nextDouble()) * (0.5 + 0.5 * fase);
      canvas.drawCircle(
        alvo + Offset(math.cos(a) * dist, -math.sin(a).abs() * dist * 0.7),
        g.w * 0.035,
        Paint()..color = _tom(cor, 0.15).withValues(alpha: 0.7 * visivel),
      );
    }
  }

  /// Estrelinhas a sair da boca do frasco que acabou de ficar arrumado.
  void _brilhar(Canvas canvas, Brilho b) {
    final r = rects[b.frasco];
    final centro = Offset(r.center.dx, r.top);
    final t = b.t;
    if (t >= 1) return;
    final w = r.width;

    // Um anel que se abre e desvanece.
    canvas.drawCircle(
      centro,
      w * (0.3 + 0.9 * t),
      Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.5 * (1 - t)
        ..color = S.chart.withValues(alpha: 0.7 * (1 - t)),
    );

    for (var k = 0; k < 9; k++) {
      final a = -math.pi / 2 + (k - 4) * 0.42;
      final dist = w * (0.25 + 1.15 * Curves.easeOut.transform(t));
      final p = centro + Offset(math.cos(a) * dist, math.sin(a) * dist);
      final tamanho = w * 0.09 * (1 - t) + 1;
      final cor = k.isEven ? S.chart : Colors.white;
      _estrela(canvas, p, tamanho, cor.withValues(alpha: 1 - t));
    }
  }

  void _estrela(Canvas canvas, Offset c, double r, Color cor) {
    final p = Path();
    for (var i = 0; i < 8; i++) {
      final a = i * math.pi / 4;
      final raio = i.isEven ? r : r * 0.42;
      final v = c + Offset(math.cos(a) * raio, math.sin(a) * raio);
      if (i == 0) {
        p.moveTo(v.dx, v.dy);
      } else {
        p.lineTo(v.dx, v.dy);
      }
    }
    p.close();
    canvas.drawPath(p, Paint()..color = cor);
  }

  @override
  bool shouldRepaint(_PintorDosEfeitos antigo) =>
      antigo.despejo != despejo ||
      antigo.brilho != brilho ||
      antigo.verteParaADireita != verteParaADireita ||
      !listEquals(antigo.rects, rects);
}
