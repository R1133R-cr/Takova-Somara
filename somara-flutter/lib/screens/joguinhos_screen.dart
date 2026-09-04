import 'package:flutter/material.dart';
import '../models/crossmath.dart';
import '../services/sons.dart';
import '../theme.dart';
import '../widgets/roby.dart';
import '../models/memoria.dart';
import '../models/sopa.dart';
import 'crossmath_screen.dart';
import 'memoria_screen.dart';
import 'pomar_screen.dart';
import 'sopa_screen.dart';

/// A sala dos joguinhos.
///
/// A amarelinha é o currículo e tem de ser cumprida por ordem. Isto é o
/// contrário: entra-se quando se quer, joga-se o que apetece, e nada disto
/// gasta corações nem faz avançar o mapa. Serve dois momentos concretos —
/// a criança que já acabou a lição do dia e quer continuar, e a que ficou
/// à espera dos corações e não tem nada para fazer.
///
/// Está feita para crescer: cada jogo é um cartão nesta lista, e acrescentar
/// outro é acrescentar uma entrada em [_jogos].
class JoguinhosScreen extends StatelessWidget {
  const JoguinhosScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(20, 12, 20, 28),
      children: [
        const Text(
          'Joguinhos',
          style: TextStyle(
            fontSize: 27,
            fontWeight: FontWeight.w700,
            color: S.tx,
          ),
        ),
        const SizedBox(height: 6),
        const Text(
          'Para brincar. Não gastam corações.',
          style: TextStyle(color: S.txSoft, fontSize: 15),
        ),
        const SizedBox(height: 22),

        _CartaoDoJogo(
          titulo: 'Crossmath',
          descricao:
              'As contas têm de fechar nas linhas e nas colunas ao mesmo '
              'tempo. Descobre os números que faltam.',
          pose: RobyPose.curioso,
          botoes: [
            for (final d in Dificuldade.values)
              (
                rotulo: d.rotulo,
                detalhe: 'até ${d.tecto}',
                abrir: (BuildContext ctx) => CrossmathScreen(dificuldade: d),
              ),
          ],
        ),
        const SizedBox(height: 14),

        _CartaoDoJogo(
          titulo: 'Pomar',
          descricao:
              'Junta três ou mais do mesmo produto. Manga, banana, coco, '
              'milho, tomate e amendoim.',
          pose: RobyPose.empolgado,
          botoes: [
            (
              rotulo: 'Jogar',
              detalhe: '20 jogadas',
              abrir: (BuildContext ctx) => const PomarScreen(),
            ),
          ],
        ),

        const SizedBox(height: 14),

        _CartaoDoJogo(
          titulo: 'Sopa de letras',
          descricao:
              'Arrasta por cima das letras para descobrir as palavras '
              'escondidas. Animais, frutas, a escola, o corpo e Moçambique.',
          pose: RobyPose.graduate,
          botoes: [
            for (final n in NivelSopa.values)
              (
                rotulo: n.rotulo,
                detalhe: '${n.quantasPalavras} palavras',
                abrir: (BuildContext ctx) => SopaScreen(nivel: n),
              ),
          ],
        ),

        const SizedBox(height: 14),

        _CartaoDoJogo(
          titulo: 'Memória',
          descricao:
              'Vira as cartas e junta os pares. O par nunca é igual a si '
              'mesmo: o 7 casa com sete maçãs, o 3 + 4 casa com o 7.',
          pose: RobyPose.dica,
          botoes: [
            for (final b in Baralho.values)
              (
                rotulo: b.rotulo,
                detalhe: b.classes,
                abrir: (BuildContext ctx) => MemoriaScreen(baralho: b),
              ),
          ],
        ),

        const SizedBox(height: 26),
        Center(
          child: Column(
            children: [
              Opacity(
                opacity: 0.35,
                child: Image.asset(RobyPose.confiante.path, width: 84),
              ),
              const SizedBox(height: 10),
              const Text(
                'Vêm mais joguinhos a caminho.',
                style: TextStyle(color: S.txMut, fontSize: 13.5),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

/// Um botão de entrada num jogo: o que diz e o ecrã que abre.
typedef BotaoDeJogo = ({
  String rotulo,
  String detalhe,
  Widget Function(BuildContext) abrir,
});

class _CartaoDoJogo extends StatelessWidget {
  final String titulo;
  final String descricao;
  final RobyPose pose;

  /// Um ou vários — o Crossmath tem três dificuldades, o Pomar tem um só
  /// modo. O cartão serve os dois sem saber a diferença.
  final List<BotaoDeJogo> botoes;

  const _CartaoDoJogo({
    required this.titulo,
    required this.descricao,
    required this.pose,
    required this.botoes,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: S.surface,
        border: Border.all(color: S.chart.withValues(alpha: 0.45), width: 2),
        borderRadius: BorderRadius.circular(S.rLg),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              SizedBox(
                width: 54,
                height: 54,
                child: ClipOval(
                  child: Container(
                    color: const Color(0xFFF3EFE3),
                    child: Image.asset(
                      pose.path,
                      fit: BoxFit.cover,
                      alignment: Alignment.topCenter,
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 14),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      titulo,
                      style: const TextStyle(
                        fontSize: 19,
                        fontWeight: FontWeight.w700,
                        color: S.tx,
                      ),
                    ),
                    const SizedBox(height: 3),
                    Text(
                      descricao,
                      style: const TextStyle(
                        color: S.txSoft,
                        fontSize: 13.5,
                        height: 1.35,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 16),
          ..._linhasDeBotoes(context),
        ],
      ),
    );
  }

  /// Os botões, em linhas de três no máximo.
  ///
  /// A Memória tem quatro baralhos, e os quatro numa só linha davam a cada
  /// botão pouco mais de sessenta pixels num telemóvel comum: o rótulo
  /// partia-se ao meio, a pílula fechava-se num oval e o texto saía pela
  /// borda fora. A partir de quatro, passam a linhas de dois.
  List<Widget> _linhasDeBotoes(BuildContext context) {
    final porLinha = botoes.length <= 3 ? botoes.length : 2;
    final linhas = <Widget>[];

    for (var i = 0; i < botoes.length; i += porLinha) {
      final fim = (i + porLinha).clamp(0, botoes.length);
      final fatia = botoes.sublist(i, fim);
      if (i > 0) linhas.add(const SizedBox(height: 8));
      linhas.add(
        // IntrinsicHeight para que um rótulo que se parta em duas linhas não
        // deixe o botão do lado mais baixo do que o seu.
        IntrinsicHeight(
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              for (var j = 0; j < fatia.length; j++) ...[
                if (j > 0) const SizedBox(width: 8),
                Expanded(child: _botao(context, fatia[j])),
              ],
              // A última linha pode vir incompleta — cinco botões, por
              // exemplo. Os lugares que sobram ficam reservados, para os
              // botões de baixo não engordarem em relação aos de cima.
              for (var j = fatia.length; j < porLinha; j++) ...[
                const SizedBox(width: 8),
                const Expanded(child: SizedBox()),
              ],
            ],
          ),
        ),
      );
    }
    return linhas;
  }

  Widget _botao(BuildContext context, BotaoDeJogo b) => GestureDetector(
    onTap: () {
      Sons.i.toque();
      Navigator.of(context).push(MaterialPageRoute(builder: b.abrir));
    },
    child: Container(
      // A folga dos lados não é enfeite: sem ela o texto encosta à borda
      // curva da pílula e fica a sair por fora dela.
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 11),
      decoration: BoxDecoration(
        color: S.gm900,
        border: Border.all(color: S.line, width: 2),
        borderRadius: BorderRadius.circular(S.rPill),
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            b.rotulo,
            textAlign: TextAlign.center,
            style: const TextStyle(
              color: S.chart,
              fontSize: 14,
              fontWeight: FontWeight.w700,
            ),
          ),
          const SizedBox(height: 1),
          // O detalhe dito por extenso: é a informação que diz a um pai se
          // aquilo serve para o filho, sem ter de o pôr a experimentar.
          Text(
            b.detalhe,
            textAlign: TextAlign.center,
            style: const TextStyle(color: S.txMut, fontSize: 11),
          ),
        ],
      ),
    ),
  );
}
