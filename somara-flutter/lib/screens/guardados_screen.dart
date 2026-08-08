import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';
import 'lesson_screen.dart';

/// As perguntas que a criança errou, guardadas para voltar a elas.
///
/// Guardam-se sozinhas ao errar, em vez de exigir que a criança se lembre de
/// carregar numa estrela — aos sete anos ninguém marca os próprios erros. Sai
/// da lista quando acerta, e é essa saída que dá a sensação de progresso.
class GuardadosScreen extends StatelessWidget {
  const GuardadosScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final lista = st.paraRever;

    if (lista.isEmpty) {
      return Center(
        child: Padding(
          padding: const EdgeInsets.all(34),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Image.asset(RobyPose.orgulhoso.path, width: 130),
              const SizedBox(height: 18),
              const Text('Nada guardado',
                  style: TextStyle(
                      fontSize: 21, fontWeight: FontWeight.w700, color: S.tx)),
              const SizedBox(height: 8),
              const Text(
                'As perguntas que errares ficam aqui, para as praticares '
                'até as acertares.',
                textAlign: TextAlign.center,
                style: TextStyle(color: S.txSoft, fontSize: 14.5, height: 1.45),
              ),
            ],
          ),
        ),
      );
    }

    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.fromLTRB(20, 12, 20, 0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text('Guardados',
                  style: TextStyle(
                      fontSize: 27, fontWeight: FontWeight.w700, color: S.tx)),
              const SizedBox(height: 6),
              Text(
                '${lista.length} ${lista.length == 1 ? "pergunta" : "perguntas"} '
                'para praticar. Acerta e sai da lista.',
                style: const TextStyle(color: S.txSoft, fontSize: 15),
              ),
              const SizedBox(height: 16),
              SizedBox(
                width: double.infinity,
                child: GestureDetector(
                  onTap: () => Navigator.of(context).push(MaterialPageRoute(
                    builder: (_) => LessonScreen(
                      indice: -1,
                      avulsas: lista.take(10).toList(),
                      titulo: 'Revisão',
                    ),
                  )),
                  child: Container(
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    decoration: BoxDecoration(
                      color: S.chart,
                      borderRadius: BorderRadius.circular(S.rPill),
                      boxShadow: const [
                        BoxShadow(color: S.chart600, offset: Offset(0, 4)),
                      ],
                    ),
                    alignment: Alignment.center,
                    child: const Text('Praticar agora',
                        style: TextStyle(
                            fontSize: 17,
                            fontWeight: FontWeight.w700,
                            color: S.onChart)),
                  ),
                ),
              ),
              const SizedBox(height: 18),
            ],
          ),
        ),
        Expanded(
          child: ListView.separated(
            padding: const EdgeInsets.fromLTRB(20, 0, 20, 24),
            itemCount: lista.length,
            separatorBuilder: (_, _) => const SizedBox(height: 9),
            itemBuilder: (_, i) => Container(
              padding: const EdgeInsets.symmetric(horizontal: 15, vertical: 14),
              decoration: BoxDecoration(
                color: S.surface,
                border: Border.all(color: S.line),
                borderRadius: BorderRadius.circular(S.rMd),
              ),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    width: 26,
                    height: 26,
                    alignment: Alignment.center,
                    decoration: BoxDecoration(
                      color: S.lifeDim,
                      borderRadius: BorderRadius.circular(7),
                    ),
                    child: Text('${i + 1}',
                        style: const TextStyle(
                            color: S.life,
                            fontSize: 13,
                            fontWeight: FontWeight.w700)),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Text(lista[i].q,
                        style: const TextStyle(
                            color: S.tx, fontSize: 14.5, height: 1.35)),
                  ),
                ],
              ),
            ),
          ),
        ),
      ],
    );
  }
}
