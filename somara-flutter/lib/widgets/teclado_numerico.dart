import 'package:flutter/material.dart';
import '../services/sons.dart';
import '../theme.dart';

/// Teclado de números para as respostas escritas.
///
/// Porque não o teclado do telemóvel: o do sistema abre com letras, tapa
/// meio ecrã, e num aparelho barato demora a aparecer. Uma criança da 1ª
/// classe que quer escrever "8" não devia ter de encontrar a tecla dos
/// números primeiro — e com a pergunta tapada, perde de vista o que lhe
/// foi perguntado.
///
/// Teclas grandes de propósito. O alvo de toque de um dedo de seis anos é
/// maior e menos certeiro do que o de um adulto.
class TecladoNumerico extends StatelessWidget {
  final ValueChanged<int> aoDigito;
  final VoidCallback aoApagar;

  /// Fora deste estado o teclado fica visível mas inerte — desaparecer
  /// depois de responder faria o ecrã saltar por baixo do dedo.
  final bool activo;

  const TecladoNumerico({
    super.key,
    required this.aoDigito,
    required this.aoApagar,
    this.activo = true,
  });

  @override
  Widget build(BuildContext context) {
    return Opacity(
      opacity: activo ? 1 : 0.4,
      child: Column(
        mainAxisSize: MainAxisSize.min,
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
                    Expanded(child: _tecla('$d', () => aoDigito(d))),
                    if (d != fila.last) const SizedBox(width: 8),
                  ],
                ],
              ),
            ),
          SizedBox(
            width: double.infinity,
            child: _tecla(
              '⌫  Apagar',
              aoApagar,
              cor: S.surface,
              corTexto: S.txSoft,
            ),
          ),
        ],
      ),
    );
  }

  Widget _tecla(
    String texto,
    VoidCallback accao, {
    Color cor = S.gm800,
    Color corTexto = S.tx,
  }) => GestureDetector(
    onTap: activo
        ? () {
            Sons.i.toque();
            accao();
          }
        : null,
    child: Container(
      height: 52,
      decoration: BoxDecoration(
        color: cor,
        border: Border.all(color: S.line, width: 1.5),
        borderRadius: BorderRadius.circular(S.rMd),
      ),
      alignment: Alignment.center,
      child: Text(
        texto,
        style: TextStyle(
          fontSize: 19,
          fontWeight: FontWeight.w700,
          color: corTexto,
        ),
      ),
    ),
  );
}

/// A caixa onde o número escrito aparece.
///
/// Não é um TextField: com o teclado próprio não há cursor nem selecção a
/// gerir, e uma caixa simples não abre o teclado do sistema por engano
/// quando a criança lhe toca.
class MostradorDoNumero extends StatelessWidget {
  final String valor;
  final bool erro;

  const MostradorDoNumero({super.key, required this.valor, this.erro = false});

  @override
  Widget build(BuildContext context) => Container(
    width: double.infinity,
    padding: const EdgeInsets.symmetric(vertical: 18),
    decoration: BoxDecoration(
      color: S.surface,
      border: Border.all(
        color: erro ? S.life : (valor.isEmpty ? S.line : S.chart),
        width: 2,
      ),
      borderRadius: BorderRadius.circular(S.rMd),
    ),
    alignment: Alignment.center,
    child: Text(
      valor.isEmpty ? '?' : valor,
      style: TextStyle(
        fontSize: 30,
        fontWeight: FontWeight.w800,
        color: valor.isEmpty ? S.txMut : (erro ? S.life : S.tx),
      ),
    ),
  );
}
