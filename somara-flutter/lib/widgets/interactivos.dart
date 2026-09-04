/// Os três exercícios interactivos de Ciências.
///
/// Estão num ficheiro só porque partilham a mesma ideia e as mesmas peças:
/// uma pastilha que se arrasta, uma caixa que a recebe, e um sinal de certo
/// ou errado no fim. Separá-los em três ficheiros dava três cópias do mesmo
/// chip com três feitios ligeiramente diferentes — que é como uma interface
/// deixa de se parecer consigo própria.
///
/// ## Porque é que isto não é escolha múltipla
///
/// «O ciclo da água é: (a)… (b)… (c)…» avalia se a criança reconhece a
/// frase certa. Pôr os quatro passos pela ordem certa avalia se ela percebeu
/// o ciclo. Numa disciplina em que quase tudo é sequência, causa e
/// classificação, a escolha múltipla estava a medir a coisa errada.
library;

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../models/content.dart';
import '../painters/cenas.dart';
import '../services/sons.dart';
import '../theme.dart';

/// A pastilha comum aos três.
class Pastilha extends StatelessWidget {
  final String texto;
  final bool aArrastar;
  final bool colocada;
  final Color? cor;

  const Pastilha(
    this.texto, {
    super.key,
    this.aArrastar = false,
    this.colocada = false,
    this.cor,
  });

  @override
  Widget build(BuildContext context) => Material(
    color: Colors.transparent,
    child: Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
      decoration: BoxDecoration(
        color: cor ?? (colocada ? S.surface2 : S.surface),
        border: Border.all(
          color: cor != null ? cor! : (aArrastar ? S.chart : S.line),
          width: aArrastar ? 2.5 : 1.8,
        ),
        borderRadius: BorderRadius.circular(S.rPill),
        boxShadow: aArrastar
            ? [
                BoxShadow(
                  color: Colors.black.withValues(alpha: 0.35),
                  blurRadius: 12,
                  offset: const Offset(0, 5),
                ),
              ]
            : null,
      ),
      child: Text(
        texto,
        style: TextStyle(
          color: cor != null ? S.gm950 : S.tx,
          fontSize: 14.5,
          fontWeight: FontWeight.w700,
        ),
      ),
    ),
  );
}

/// Pôr os passos pela ordem certa.
///
/// Arrasta-se pela pega, e não pela pastilha inteira: numa lista curta, um
/// arrasto que começa em qualquer sítio confunde-se com o gesto de rolar a
/// página, e a criança fica sem perceber porque é que às vezes pega e às
/// vezes não.
class OrdenarPassos extends StatelessWidget {
  final QSequencia questao;

  /// A ordem actual, por índices da ordem certa.
  final List<int> ordem;
  final ValueChanged<List<int>> aoMudar;

  /// Nulo enquanto ela responde; depois, se acertou.
  final bool? corrigida;

  const OrdenarPassos({
    super.key,
    required this.questao,
    required this.ordem,
    required this.aoMudar,
    this.corrigida,
  });

  @override
  Widget build(BuildContext context) {
    return ReorderableListView.builder(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      buildDefaultDragHandles: false,
      itemCount: ordem.length,
      // `onReorderItem` e não `onReorder`: o índice novo já vem corrigido
      // para o item ter saído do sítio antigo, e é justamente essa correcção
      // que se fazia à mão e se enganava por um em metade dos casos.
      onReorderItem: (de, para) {
        if (corrigida != null) return;
        Sons.i.toque();
        HapticFeedback.selectionClick();
        final nova = [...ordem];
        nova.insert(para, nova.removeAt(de));
        aoMudar(nova);
      },
      itemBuilder: (context, i) {
        final passo = ordem[i];
        // Depois de corrigir, cada passo diz se está no seu lugar. Um
        // "erraste" sem dizer onde não ensina nada.
        final noLugar = corrigida != null && passo == i;
        return Padding(
          key: ValueKey(passo),
          padding: const EdgeInsets.only(bottom: 8),
          child: Container(
            padding: const EdgeInsets.fromLTRB(10, 10, 6, 10),
            decoration: BoxDecoration(
              color: corrigida == null
                  ? S.surface
                  : (noLugar
                        ? S.green500.withValues(alpha: 0.18)
                        : S.life.withValues(alpha: 0.16)),
              border: Border.all(
                color: corrigida == null
                    ? S.line
                    : (noLugar ? S.green300 : S.life),
                width: 1.8,
              ),
              borderRadius: BorderRadius.circular(S.rMd),
            ),
            child: Row(
              children: [
                Container(
                  width: 26,
                  height: 26,
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                    color: S.chart.withValues(alpha: 0.18),
                    shape: BoxShape.circle,
                  ),
                  child: Text(
                    '${i + 1}',
                    style: const TextStyle(
                      color: S.chart,
                      fontSize: 13,
                      fontWeight: FontWeight.w800,
                    ),
                  ),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: Text(
                    questao.passos[passo],
                    style: const TextStyle(
                      color: S.tx,
                      fontSize: 14.5,
                      height: 1.3,
                    ),
                  ),
                ),
                if (corrigida == null)
                  ReorderableDragStartListener(
                    index: i,
                    child: const Padding(
                      padding: EdgeInsets.all(6),
                      child: Icon(
                        Icons.drag_indicator_rounded,
                        color: S.txMut,
                        size: 22,
                      ),
                    ),
                  ),
              ],
            ),
          ),
        );
      },
    );
  }
}

/// Arrastar cada coisa para o grupo a que pertence.
class ClassificarGrupos extends StatelessWidget {
  final QGrupos questao;

  /// Em que grupo está cada item, ou nulo se ainda está por colocar.
  final List<int?> posto;
  final ValueChanged<List<int?>> aoMudar;
  final bool? corrigida;

  const ClassificarGrupos({
    super.key,
    required this.questao,
    required this.posto,
    required this.aoMudar,
    this.corrigida,
  });

  @override
  Widget build(BuildContext context) {
    final porColocar = [
      for (var i = 0; i < questao.itens.length; i++)
        if (posto[i] == null) i,
    ];

    return Column(
      children: [
        // O que falta colocar fica em cima, sempre no mesmo sítio. Uma
        // reserva que muda de lugar obriga a criança a procurá-la a cada
        // peça largada.
        Container(
          width: double.infinity,
          constraints: const BoxConstraints(minHeight: 62),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: S.gm900,
            border: Border.all(color: S.line),
            borderRadius: BorderRadius.circular(S.rMd),
          ),
          child: porColocar.isEmpty
              ? const Center(
                  child: Text(
                    'Está tudo arrumado.',
                    style: TextStyle(color: S.txMut, fontSize: 13.5),
                  ),
                )
              : Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  alignment: WrapAlignment.center,
                  children: [
                    for (final i in porColocar) _arrastavel(i),
                  ],
                ),
        ),
        const SizedBox(height: 12),
        Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            for (var g = 0; g < questao.grupos.length; g++) ...[
              if (g > 0) const SizedBox(width: 8),
              Expanded(child: _caixa(g)),
            ],
          ],
        ),
      ],
    );
  }

  Widget _arrastavel(int i) {
    final nome = questao.itens[i].nome;
    if (corrigida != null) return Pastilha(nome);
    return Draggable<int>(
      data: i,
      feedback: Pastilha(nome, aArrastar: true),
      childWhenDragging: Opacity(opacity: 0.25, child: Pastilha(nome)),
      child: Pastilha(nome),
    );
  }

  Widget _caixa(int g) => DragTarget<int>(
    onAcceptWithDetails: (d) {
      Sons.i.toque();
      HapticFeedback.mediumImpact();
      final nova = [...posto];
      nova[d.data] = g;
      aoMudar(nova);
    },
    builder: (_, candidatos, _) {
      final activa = candidatos.isNotEmpty;
      final dentro = [
        for (var i = 0; i < posto.length; i++)
          if (posto[i] == g) i,
      ];
      return AnimatedContainer(
        duration: const Duration(milliseconds: 160),
        constraints: const BoxConstraints(minHeight: 108),
        padding: const EdgeInsets.all(9),
        decoration: BoxDecoration(
          color: activa ? S.chart.withValues(alpha: 0.14) : S.surface,
          border: Border.all(
            color: activa ? S.chart : S.line,
            width: activa ? 2.5 : 1.8,
          ),
          borderRadius: BorderRadius.circular(S.rMd),
        ),
        child: Column(
          children: [
            Text(
              questao.grupos[g],
              textAlign: TextAlign.center,
              style: const TextStyle(
                color: S.chart,
                fontSize: 14,
                fontWeight: FontWeight.w700,
              ),
            ),
            const SizedBox(height: 8),
            Wrap(
              spacing: 6,
              runSpacing: 6,
              alignment: WrapAlignment.center,
              children: [
                for (final i in dentro)
                  GestureDetector(
                    // Um toque devolve a peça à reserva. Sem isto, uma peça
                    // largada na caixa errada ficava lá para sempre.
                    onTap: corrigida != null
                        ? null
                        : () {
                            Sons.i.toque();
                            final nova = [...posto];
                            nova[i] = null;
                            aoMudar(nova);
                          },
                    child: Pastilha(
                      questao.itens[i].nome,
                      colocada: true,
                      cor: corrigida == null
                          ? null
                          : (posto[i] == questao.itens[i].grupo
                                ? S.green300
                                : S.life),
                    ),
                  ),
              ],
            ),
          ],
        ),
      );
    },
  );
}

/// Largar peças nos sítios certos de um cenário desenhado.
class CenarioInteractivo extends StatelessWidget {
  final QCenario questao;

  /// A peça largada em cada alvo, ou nulo.
  final List<String?> posto;
  final ValueChanged<List<String?>> aoMudar;
  final bool? corrigida;

  const CenarioInteractivo({
    super.key,
    required this.questao,
    required this.posto,
    required this.aoMudar,
    this.corrigida,
  });

  /// A altura do cenário. Fixa e não proporcional: as posições dos alvos são
  /// relativas ao desenho, e um desenho que mudasse de proporção com o ecrã
  /// punha o coração fora do peito num telemóvel comprido.
  static const altura = 210.0;

  @override
  Widget build(BuildContext context) {
    final colocadas = posto.whereType<String>().toSet();
    final porColocar = [
      for (final p in questao.pecas)
        if (!colocadas.contains(p)) p,
    ];
    final completa = questao.certa(posto);

    return Column(
      children: [
        SizedBox(
          height: 56,
          child: porColocar.isEmpty
              ? const Center(
                  child: Text(
                    'Já não falta nada.',
                    style: TextStyle(color: S.txMut, fontSize: 13.5),
                  ),
                )
              : Center(
                  child: Wrap(
                    spacing: 8,
                    runSpacing: 6,
                    alignment: WrapAlignment.center,
                    children: [
                      for (final p in porColocar)
                        if (corrigida != null)
                          Pastilha(p)
                        else
                          Draggable<String>(
                            data: p,
                            feedback: Pastilha(p, aArrastar: true),
                            childWhenDragging:
                                Opacity(opacity: 0.25, child: Pastilha(p)),
                            child: Pastilha(p),
                          ),
                    ],
                  ),
                ),
        ),
        const SizedBox(height: 10),
        SizedBox(
          height: altura,
          child: LayoutBuilder(
            builder: (context, box) => Stack(
              children: [
                Positioned.fill(
                  child: CustomPaint(
                    painter: FundoDaCena(
                      cena: questao.cena,
                      completa: completa,
                    ),
                  ),
                ),
                for (var i = 0; i < questao.alvos.length; i++)
                  _alvo(i, box.maxWidth, box.maxHeight),
              ],
            ),
          ),
        ),
      ],
    );
  }

  Widget _alvo(int i, double largura, double alturaCaixa) {
    final alvo = questao.alvos[i];
    final aqui = posto[i];
    const w = 96.0, h = 38.0;

    return Positioned(
      left: (alvo.x * largura - w / 2).clamp(0.0, largura - w),
      top: (alvo.y * alturaCaixa - h / 2).clamp(0.0, alturaCaixa - h),
      width: w,
      height: h,
      child: DragTarget<String>(
        onAcceptWithDetails: (d) {
          Sons.i.toque();
          HapticFeedback.mediumImpact();
          final nova = [...posto];
          // A mesma peça não pode estar em dois sítios.
          for (var k = 0; k < nova.length; k++) {
            if (nova[k] == d.data) nova[k] = null;
          }
          nova[i] = d.data;
          aoMudar(nova);
        },
        builder: (_, candidatos, _) {
          final activa = candidatos.isNotEmpty;
          final certa = corrigida != null && aqui == alvo.peca;
          return GestureDetector(
            onTap: (aqui == null || corrigida != null)
                ? null
                : () {
                    Sons.i.toque();
                    final nova = [...posto];
                    nova[i] = null;
                    aoMudar(nova);
                  },
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 160),
              decoration: BoxDecoration(
                color: corrigida != null
                    ? (certa
                          ? S.green500.withValues(alpha: 0.25)
                          : S.life.withValues(alpha: 0.20))
                    : (activa
                          ? S.chart.withValues(alpha: 0.22)
                          : S.surface.withValues(alpha: 0.85)),
                border: Border.all(
                  color: corrigida != null
                      ? (certa ? S.green300 : S.life)
                      : (activa ? S.chart : S.line),
                  width: activa ? 2.5 : 1.8,
                ),
                borderRadius: BorderRadius.circular(S.rSm),
              ),
              alignment: Alignment.center,
              child: Text(
                aqui ?? '?',
                textAlign: TextAlign.center,
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
                style: TextStyle(
                  color: aqui == null ? S.txMut : S.tx,
                  fontSize: aqui == null ? 16 : 12.5,
                  fontWeight: FontWeight.w700,
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}
