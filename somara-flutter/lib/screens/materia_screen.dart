import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/material.dart';
import '../models/content.dart';
import '../services/sons.dart';
import '../theme.dart';
import '../widgets/roby.dart';

/// A aula antes do exercício.
///
/// Na fase C as crianças acharam as perguntas secas — chegavam ao exercício
/// sem ninguém lhes ter relembrado nada, e "escreve o ano em que foi criada
/// a SADC" sem contexto nenhum é um teste, não uma aula. Sem isto, a app
/// avaliava sem nunca ter ensinado.
///
/// As três partes entram uma de cada vez, com um intervalo curto entre elas.
/// Não é enfeite: uma criança de sete anos que recebe o ecrã todo de uma vez
/// não sabe por onde começar a ler. A entrada faseada dá a ordem da leitura.
class MateriaScreen extends StatefulWidget {
  final String titulo;
  final Materia materia;

  /// O que fazer quando a criança diz que percebeu. Se for nulo, o ecrã
  /// limita-se a fechar-se — é o que acontece quando se vem da casa lateral
  /// só para reler a matéria.
  final VoidCallback? aoComecar;

  const MateriaScreen({
    super.key,
    required this.titulo,
    required this.materia,
    this.aoComecar,
  });

  @override
  State<MateriaScreen> createState() => _MateriaScreenState();
}

class _MateriaScreenState extends State<MateriaScreen>
    with SingleTickerProviderStateMixin {
  late final AnimationController _entrada;
  final _voz = AudioPlayer();

  @override
  void initState() {
    super.initState();
    _entrada = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1500),
    )..forward();
    // A aula e lida em voz alta pela Raquel: musica por cima tornava-a
    // dificil de perceber a quem ainda nao le e depende do audio.
    Sons.i.pedirSilencio();
    _ler();
  }

  Future<void> _ler() async {
    final f = widget.materia.audio;
    if (f == null) return;
    try {
      await _voz.stop();
      await _voz.play(AssetSource('audio/$f'));
    } catch (_) {
      // Sem áudio a aula lê-se na mesma. Nunca vale a pena rebentar por isto.
    }
  }

  @override
  void dispose() {
    Sons.i.largarSilencio();
    _entrada.dispose();
    _voz.dispose();
    super.dispose();
  }

  /// Fatia da animação de entrada reservada a cada bloco.
  Animation<double> _passo(int i) => CurvedAnimation(
    parent: _entrada,
    curve: Interval(i * 0.24, i * 0.24 + 0.5, curve: SCurves.easeOutBack),
  );

  Widget _aparece(int i, Widget filho) => AnimatedBuilder(
    animation: _passo(i),
    builder: (_, child) {
      final v = _passo(i).value.clamp(0.0, 1.0);
      return Opacity(
        opacity: v,
        child: Transform.translate(offset: Offset(0, (1 - v) * 22), child: child),
      );
    },
    child: filho,
  );

  @override
  Widget build(BuildContext context) {
    final m = widget.materia;

    return Scaffold(
      backgroundColor: S.gm950,
      body: SafeArea(
        child: Column(
          children: [
            // Barra de topo — o ✕ fecha, como em qualquer lição.
            Padding(
              padding: const EdgeInsets.fromLTRB(12, 8, 20, 0),
              child: Row(
                children: [
                  IconButton(
                    onPressed: () => Navigator.of(context).pop(),
                    icon: const Icon(Icons.close_rounded, color: S.txSoft),
                  ),
                  Expanded(
                    child: Text(
                      widget.titulo,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: const TextStyle(
                        color: S.txSoft,
                        fontSize: 14.5,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
                  if (m.audio != null)
                    IconButton(
                      onPressed: _ler,
                      tooltip: 'Ouvir outra vez',
                      icon: const Icon(Icons.volume_up_rounded, color: S.chart),
                    ),
                ],
              ),
            ),

            Expanded(
              child: SingleChildScrollView(
                padding: const EdgeInsets.fromLTRB(22, 4, 22, 24),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    _aparece(
                      0,
                      Column(
                        children: [
                          Image.asset(RobyPose.dica.path, width: 130),
                          const SizedBox(height: 10),
                          const Text(
                            'Antes de começar',
                            style: TextStyle(
                              color: S.chart,
                              fontSize: 13,
                              fontWeight: FontWeight.w700,
                              letterSpacing: 1.4,
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 18),

                    // 1. A explicação.
                    _aparece(
                      0,
                      Container(
                        padding: const EdgeInsets.all(18),
                        decoration: BoxDecoration(
                          color: S.surface,
                          border: Border.all(color: S.line, width: 2),
                          borderRadius: BorderRadius.circular(S.rLg),
                        ),
                        child: Text(
                          m.explica,
                          style: const TextStyle(
                            color: S.tx,
                            fontSize: 16.5,
                            height: 1.5,
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(height: 14),

                    // 2. O caso feito. Fica em destaque porque é o que uma
                    // criança copia quando não percebeu a explicação.
                    _aparece(
                      1,
                      Container(
                        padding: const EdgeInsets.fromLTRB(18, 16, 18, 18),
                        decoration: BoxDecoration(
                          color: S.chart.withValues(alpha: 0.09),
                          border: Border.all(
                            color: S.chart.withValues(alpha: 0.55),
                            width: 2,
                          ),
                          borderRadius: BorderRadius.circular(S.rLg),
                        ),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              children: [
                                const Icon(
                                  Icons.lightbulb_rounded,
                                  color: S.chart,
                                  size: 18,
                                ),
                                const SizedBox(width: 7),
                                Text(
                                  'EXEMPLO',
                                  style: TextStyle(
                                    color: S.chart.withValues(alpha: 0.9),
                                    fontSize: 11.5,
                                    fontWeight: FontWeight.w800,
                                    letterSpacing: 1.3,
                                  ),
                                ),
                              ],
                            ),
                            const SizedBox(height: 9),
                            Text(
                              m.exemplo,
                              style: const TextStyle(
                                color: S.tx,
                                fontSize: 17,
                                height: 1.5,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                    const SizedBox(height: 14),

                    // 3. A frase que se leva para o exercício.
                    _aparece(
                      2,
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const Padding(
                            padding: EdgeInsets.only(top: 2),
                            child: Icon(
                              Icons.push_pin_rounded,
                              color: S.gold,
                              size: 18,
                            ),
                          ),
                          const SizedBox(width: 9),
                          Expanded(
                            child: Text(
                              m.lembra,
                              style: const TextStyle(
                                color: S.gold,
                                fontSize: 15,
                                height: 1.45,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),

            Padding(
              padding: const EdgeInsets.fromLTRB(22, 0, 22, 18),
              child: _aparece(
                2,
                GestureDetector(
                  onTap: () {
                    final seguir = widget.aoComecar;
                    if (seguir == null) {
                      Navigator.of(context).pop();
                    } else {
                      seguir();
                    }
                  },
                  child: Container(
                    width: double.infinity,
                    padding: const EdgeInsets.symmetric(vertical: 17),
                    decoration: BoxDecoration(
                      color: S.chart,
                      borderRadius: BorderRadius.circular(S.rPill),
                      boxShadow: const [
                        BoxShadow(color: S.chart600, offset: Offset(0, 4)),
                      ],
                    ),
                    alignment: Alignment.center,
                    child: Text(
                      widget.aoComecar == null ? 'Percebi' : 'Vamos lá!',
                      style: const TextStyle(
                        fontSize: 17.5,
                        fontWeight: FontWeight.w700,
                        color: S.onChart,
                      ),
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
