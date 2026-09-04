import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../models/carteira.dart';
import '../models/coleccao.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';

/// A loja do Roby.
///
/// O que aqui se vende não vale nada por si: uma cara nova do Roby não
/// ensina Matemática a ninguém. Vale por ter custado — é a prova, à vista de
/// toda a gente, de que a criança fez o trabalho. Por isso não há como
/// comprar moedas: só se ganham a estudar, e é essa a única regra que faz
/// esta loja significar alguma coisa.
class LojaScreen extends StatelessWidget {
  const LojaScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();

    return Scaffold(
      backgroundColor: S.gm950,
      appBar: AppBar(
        backgroundColor: S.gm950,
        foregroundColor: S.tx,
        elevation: 0,
        title: const Text('Loja do Roby', style: TextStyle(fontSize: 17)),
      ),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.fromLTRB(16, 4, 16, 28),
          children: [
            _CarteiraAVista(carteira: st.carteira),
            const SizedBox(height: 6),
            const Text(
              'As moedas ganham-se a estudar. Não há outra maneira.',
              style: TextStyle(color: S.txMut, fontSize: 13, height: 1.35),
            ),
            const SizedBox(height: 20),
            for (final f in Familia.values) ...[
              _seccao(context, st, f),
              const SizedBox(height: 22),
            ],
          ],
        ),
      ),
    );
  }

  Widget _seccao(BuildContext context, AppState st, Familia familia) {
    final itens = catalogo.where((i) => i.familia == familia).toList();
    if (itens.isEmpty) return const SizedBox.shrink();

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          familia.rotulo,
          style: const TextStyle(
            fontSize: 19,
            fontWeight: FontWeight.w700,
            color: S.tx,
          ),
        ),
        const SizedBox(height: 2),
        Text(
          familia.descricao,
          style: const TextStyle(color: S.txSoft, fontSize: 13.5),
        ),
        const SizedBox(height: 12),
        if (familia == Familia.tempo)
          for (final i in itens) ...[
            _LinhaDeTempo(item: i),
            const SizedBox(height: 8),
          ]
        else
          // Duas colunas e não uma grelha automática: a 320 dp três cartões
          // por linha dariam noventa píxeis a cada um, e o Roby lá dentro
          // ficava do tamanho de um selo.
          Wrap(
            spacing: 10,
            runSpacing: 10,
            children: [
              for (final i in itens)
                SizedBox(
                  width: (MediaQuery.sizeOf(context).width - 32 - 10) / 2,
                  child: _CartaoDaPose(item: i),
                ),
            ],
          ),
      ],
    );
  }
}

/// Quanto se tem, das duas moedas.
class _CarteiraAVista extends StatelessWidget {
  final Carteira carteira;
  const _CarteiraAVista({required this.carteira});

  @override
  Widget build(BuildContext context) => Row(
    children: [
      Expanded(child: _moeda(Moeda.gc, carteira.gc, S.gold)),
      const SizedBox(width: 10),
      Expanded(child: _moeda(Moeda.cc, carteira.cc, S.chart)),
    ],
  );

  Widget _moeda(Moeda m, int quanto, Color cor) => Container(
    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
    decoration: BoxDecoration(
      color: S.gm900,
      border: Border.all(color: cor.withValues(alpha: 0.55), width: 1.5),
      borderRadius: BorderRadius.circular(S.rMd),
    ),
    child: Row(
      children: [
        Icon(
          m == Moeda.gc ? Icons.monetization_on_rounded : Icons.diamond_rounded,
          color: cor,
          size: 20,
        ),
        const SizedBox(width: 7),
        Text(
          '$quanto',
          style: TextStyle(
            color: cor,
            fontSize: 18,
            fontWeight: FontWeight.w700,
          ),
        ),
        const SizedBox(width: 5),
        Flexible(
          child: Text(
            m.sigla,
            style: const TextStyle(color: S.txMut, fontSize: 12.5),
          ),
        ),
      ],
    ),
  );
}

/// O preço, com a moeda ao lado.
class _Preco extends StatelessWidget {
  final ItemDaLoja item;
  final bool chega;
  const _Preco({required this.item, required this.chega});

  @override
  Widget build(BuildContext context) {
    final cor = !chega
        ? S.txMut
        : item.moeda == Moeda.gc
        ? S.gold
        : S.chart;
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Icon(
          item.moeda == Moeda.gc
              ? Icons.monetization_on_rounded
              : Icons.diamond_rounded,
          size: 15,
          color: cor,
        ),
        const SizedBox(width: 4),
        Text(
          '${item.preco}',
          style: TextStyle(
            color: cor,
            fontSize: 14,
            fontWeight: FontWeight.w700,
          ),
        ),
      ],
    );
  }
}

/// Diz o que aconteceu à compra, com todas as letras.
void _dizer(BuildContext context, ResultadoDaCompra r) {
  ScaffoldMessenger.of(context)
    ..hideCurrentSnackBar()
    ..showSnackBar(
      SnackBar(
        content: Text(r.explicacao),
        backgroundColor: r == ResultadoDaCompra.feito ? S.green500 : S.gm800,
        duration: const Duration(milliseconds: 1800),
      ),
    );
}

/// Uma compra de minutos.
class _LinhaDeTempo extends StatelessWidget {
  final ItemDaLoja item;
  const _LinhaDeTempo({required this.item});

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final chega = st.carteira.chegaPara(item.moeda, item.preco);

    return GestureDetector(
      onTap: () {
        Sons.i.toque();
        final r = context.read<AppState>().comprar(item);
        if (r == ResultadoDaCompra.feito) Sons.i.certo();
        _dizer(context, r);
      },
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
        decoration: BoxDecoration(
          color: S.surface,
          border: Border.all(color: S.line, width: 1.5),
          borderRadius: BorderRadius.circular(S.rMd),
        ),
        child: Row(
          children: [
            const Icon(Icons.timer_rounded, color: S.gold, size: 20),
            const SizedBox(width: 10),
            Expanded(
              child: Text(
                item.nome,
                style: const TextStyle(
                  color: S.tx,
                  fontSize: 15,
                  fontWeight: FontWeight.w700,
                ),
              ),
            ),
            _Preco(item: item, chega: chega),
          ],
        ),
      ),
    );
  }
}

/// Uma cara ou uma pose: o desenho, o nome e o preço — ou o botão de vestir.
class _CartaoDaPose extends StatelessWidget {
  final ItemDaLoja item;
  const _CartaoDaPose({required this.item});

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final pose = item.pose!;
    final minha = st.coleccao.tem(pose);
    final vestida = st.robyEscolhido == pose;
    final chega = st.carteira.chegaPara(item.moeda, item.preco);

    return GestureDetector(
      onTap: () {
        Sons.i.toque();
        if (minha) {
          // Já é dela: um toque veste, outro despe.
          context.read<AppState>().escolherRoby(vestida ? null : pose);
          return;
        }
        final r = context.read<AppState>().comprar(item);
        if (r == ResultadoDaCompra.feito) Sons.i.nivel();
        _dizer(context, r);
      },
      child: Container(
        padding: const EdgeInsets.fromLTRB(10, 10, 10, 12),
        decoration: BoxDecoration(
          color: S.surface,
          border: Border.all(
            color: vestida ? S.chart : S.line,
            width: vestida ? 2.5 : 1.5,
          ),
          borderRadius: BorderRadius.circular(S.rLg),
        ),
        child: Column(
          children: [
            SizedBox(
              height: 104,
              // Por comprar, a pose aparece em silhueta. Mostrá-la a cores é
              // que a torna desejável — e escondê-la por trás de um ponto de
              // interrogação era pedir à criança que poupasse às cegas.
              child: Opacity(
                opacity: minha ? 1 : 0.30,
                child: ColorFiltered(
                  colorFilter: minha
                      ? const ColorFilter.mode(
                          Colors.transparent,
                          BlendMode.dst,
                        )
                      : const ColorFilter.matrix(<double>[
                          0.2126, 0.7152, 0.0722, 0, 0, //
                          0.2126, 0.7152, 0.0722, 0, 0, //
                          0.2126, 0.7152, 0.0722, 0, 0, //
                          0, 0, 0, 1, 0, //
                        ]),
                  child: RobyImagem(
                    pose,
                    largura: 104,
                    alinhamento: Alignment.topCenter,
                  ),
                ),
              ),
            ),
            const SizedBox(height: 8),
            Text(
              item.nome,
              textAlign: TextAlign.center,
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
              style: TextStyle(
                color: minha ? S.tx : S.txSoft,
                fontSize: 13.5,
                fontWeight: FontWeight.w700,
              ),
            ),
            const SizedBox(height: 6),
            if (!minha)
              _Preco(item: item, chega: chega)
            else
              Text(
                vestida ? 'A usar' : 'Vestir',
                style: TextStyle(
                  color: vestida ? S.chart : S.txMut,
                  fontSize: 12.5,
                  fontWeight: FontWeight.w700,
                ),
              ),
          ],
        ),
      ),
    );
  }
}
