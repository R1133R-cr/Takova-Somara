import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import '../widgets/roby.dart';

/// Guardar o progresso fora do telemóvel.
///
/// Escrito para o adulto, não para a criança: é o pai ou o professor que
/// preenche isto, uma vez, e depois nunca mais. Por isso o texto diz o que
/// se ganha em vez de falar de contas e sincronização — e por isso o botão
/// se chama "Guardar o meu progresso" e não "Iniciar sessão".
class ContaScreen extends StatefulWidget {
  const ContaScreen({super.key});

  @override
  State<ContaScreen> createState() => _ContaScreenState();
}

class _ContaScreenState extends State<ContaScreen> {
  final _email = TextEditingController();
  final _palavra = TextEditingController();

  bool _contaNova = true;
  bool _aTrabalhar = false;
  bool _mostrarPalavra = false;
  String? _erro;

  @override
  void dispose() {
    _email.dispose();
    _palavra.dispose();
    super.dispose();
  }

  bool get _podeAvancar =>
      _email.text.contains('@') && _palavra.text.length >= 6 && !_aTrabalhar;

  Future<void> _avancar() async {
    setState(() {
      _aTrabalhar = true;
      _erro = null;
    });
    final st = context.read<AppState>();
    final erro = await st.entrarNaConta(
      _email.text,
      _palavra.text,
      contaNova: _contaNova,
    );
    if (!mounted) return;
    setState(() {
      _aTrabalhar = false;
      _erro = erro;
    });
    if (erro == null) {
      Sons.i.nivel();
      Navigator.of(context).pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: S.gm950,
      appBar: AppBar(
        backgroundColor: S.gm950,
        foregroundColor: S.tx,
        elevation: 0,
        title: const Text('Guardar o progresso', style: TextStyle(fontSize: 17)),
      ),
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.fromLTRB(22, 8, 22, 24),
          children: [
            Center(child: Image.asset(RobyPose.hero.path, width: 118)),
            const SizedBox(height: 16),

            const Text(
              'Se este telemóvel se estragar ou for formatado, o trabalho '
              'da criança fica guardado e volta ao entrar aqui outra vez.',
              style: TextStyle(color: S.txSoft, fontSize: 15.5, height: 1.45),
            ),
            const SizedBox(height: 6),
            const Text(
              'A app continua a funcionar sem internet. Isto é só a cópia '
              'de segurança.',
              style: TextStyle(color: S.txMut, fontSize: 13.5, height: 1.4),
            ),
            const SizedBox(height: 22),

            // Criar / entrar. Duas pastilhas em vez de um link pequeno: quem
            // preenche isto fá-lo uma vez na vida e não deve ter de adivinhar
            // em que modo está.
            Row(
              children: [
                Expanded(child: _modo('Criar conta', true)),
                const SizedBox(width: 10),
                Expanded(child: _modo('Já tenho conta', false)),
              ],
            ),
            const SizedBox(height: 20),

            _campo(
              controlador: _email,
              rotulo: 'Email do encarregado',
              icone: Icons.alternate_email_rounded,
              teclado: TextInputType.emailAddress,
            ),
            const SizedBox(height: 12),
            _campo(
              controlador: _palavra,
              rotulo: 'Palavra-passe (mínimo 6)',
              icone: Icons.lock_outline_rounded,
              esconder: !_mostrarPalavra,
              sufixo: IconButton(
                icon: Icon(
                  _mostrarPalavra
                      ? Icons.visibility_off_rounded
                      : Icons.visibility_rounded,
                  color: S.txMut,
                  size: 20,
                ),
                onPressed: () =>
                    setState(() => _mostrarPalavra = !_mostrarPalavra),
              ),
            ),

            if (_erro != null) ...[
              const SizedBox(height: 14),
              Container(
                padding: const EdgeInsets.all(13),
                decoration: BoxDecoration(
                  color: S.life.withValues(alpha: 0.12),
                  border: Border.all(color: S.life.withValues(alpha: 0.5)),
                  borderRadius: BorderRadius.circular(S.rMd),
                ),
                child: Row(
                  children: [
                    const Icon(Icons.error_outline_rounded,
                        color: S.life, size: 19),
                    const SizedBox(width: 9),
                    Expanded(
                      child: Text(
                        _erro!,
                        style: const TextStyle(color: S.tx, fontSize: 14),
                      ),
                    ),
                  ],
                ),
              ),
            ],
            const SizedBox(height: 22),

            GestureDetector(
              onTap: _podeAvancar ? _avancar : null,
              child: Opacity(
                opacity: _podeAvancar ? 1 : 0.45,
                child: Container(
                  padding: const EdgeInsets.symmetric(vertical: 17),
                  decoration: BoxDecoration(
                    color: S.chart,
                    borderRadius: BorderRadius.circular(S.rPill),
                    boxShadow: const [
                      BoxShadow(color: S.chart600, offset: Offset(0, 4)),
                    ],
                  ),
                  alignment: Alignment.center,
                  child: _aTrabalhar
                      ? const SizedBox(
                          width: 21,
                          height: 21,
                          child: CircularProgressIndicator(
                            color: S.onChart,
                            strokeWidth: 2.5,
                          ),
                        )
                      : Text(
                          _contaNova ? 'Criar e guardar' : 'Entrar',
                          style: const TextStyle(
                            fontSize: 17.5,
                            fontWeight: FontWeight.w700,
                            color: S.onChart,
                          ),
                        ),
                ),
              ),
            ),
            const SizedBox(height: 14),
            const Text(
              'Nada disto é partilhado com ninguém. Só serve para a criança '
              'reencontrar o que já fez.',
              textAlign: TextAlign.center,
              style: TextStyle(color: S.txMut, fontSize: 12.5, height: 1.4),
            ),
          ],
        ),
      ),
    );
  }

  Widget _modo(String texto, bool nova) {
    final activo = _contaNova == nova;
    return GestureDetector(
      onTap: () => setState(() {
        _contaNova = nova;
        _erro = null;
      }),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        curve: SCurves.ease,
        padding: const EdgeInsets.symmetric(vertical: 12),
        decoration: BoxDecoration(
          color: activo ? S.chart : S.surface,
          border: Border.all(color: activo ? S.chart : S.line, width: 2),
          borderRadius: BorderRadius.circular(S.rPill),
        ),
        alignment: Alignment.center,
        child: Text(
          texto,
          style: TextStyle(
            color: activo ? S.onChart : S.txSoft,
            fontWeight: FontWeight.w700,
            fontSize: 14.5,
          ),
        ),
      ),
    );
  }

  Widget _campo({
    required TextEditingController controlador,
    required String rotulo,
    required IconData icone,
    TextInputType? teclado,
    bool esconder = false,
    Widget? sufixo,
  }) => TextField(
    controller: controlador,
    keyboardType: teclado,
    obscureText: esconder,
    autocorrect: false,
    enableSuggestions: false,
    onChanged: (_) => setState(() {}),
    style: const TextStyle(color: S.tx, fontSize: 16),
    decoration: InputDecoration(
      labelText: rotulo,
      labelStyle: const TextStyle(color: S.txMut),
      prefixIcon: Icon(icone, color: S.txMut, size: 20),
      suffixIcon: sufixo,
      filled: true,
      fillColor: S.surface,
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(S.rMd),
        borderSide: const BorderSide(color: S.line, width: 2),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(S.rMd),
        borderSide: const BorderSide(color: S.chart, width: 2),
      ),
    ),
  );
}
