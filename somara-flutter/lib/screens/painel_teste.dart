import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../models/bolsa_de_tempo.dart';
import '../models/content.dart';
import '../models/escadaria.dart';
import '../modo_teste.dart';
import '../services/sons.dart';
import '../state/app_state.dart';
import '../theme.dart';
import 'crossmath_screen.dart';
import 'frascos_screen.dart';
import 'lesson_screen.dart';
import 'materia_screen.dart';
import 'memoria_screen.dart';
import 'pomar_screen.dart';
import 'sopa_screen.dart';

/// O painel da versão de testes.
///
/// Só existe no APK de testes — o ecrã inteiro está atrás de
/// [ModoTeste.activo], que é uma constante de compilação. Na app da criança
/// este código não vai dentro do ficheiro.
///
/// Não está escondido atrás de nenhum gesto secreto de propósito. Numa
/// versão que já se chama «Somara TESTE» e tem o nome vermelho debaixo do
/// ícone, esconder o painel não protegeria nada e só daria trabalho a quem
/// o usa trinta vezes por dia.
class PainelTeste extends StatelessWidget {
  const PainelTeste({super.key});

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final sw = st.interruptores;

    return Scaffold(
      backgroundColor: S.gm900,
      appBar: AppBar(
        backgroundColor: S.life,
        foregroundColor: Colors.white,
        title: const Text(
          'PAINEL DE TESTES',
          style: TextStyle(fontWeight: FontWeight.w800, letterSpacing: 1.2),
        ),
      ),
      body: ListView(
        padding: const EdgeInsets.fromLTRB(16, 14, 16, 36),
        children: [
          _Secao('Saltar para um nível'),
          const _Saltador(),
          const SizedBox(height: 22),

          _Secao('Joguinhos'),
          const _NiveisDosJogos(),
          const SizedBox(height: 22),

          _Secao('Como se comporta'),
          _Interruptor(
            titulo: 'Pôr à venda',
            detalhe: sw.aVenda
                ? 'A app está a correr como a criança a recebe: níveis por '
                      'ordem, bolsa de 60 minutos, treino só depois de um '
                      'nível feito.'
                : 'Liga para repor todos os bloqueios de uma vez e ver a '
                      'app como ela vai sair.',
            valor: sw.aVenda,
            cor: S.gold,
            aoMudar: (v) => st.definirInterruptores(sw.com(aVenda: v)),
          ),
          _Interruptor(
            titulo: 'Corações infinitos',
            detalhe: 'Errar não custa. Para varrer muitos níveis seguidos '
                'sem ficar à espera.',
            valor: sw.coracoesInfinitos,
            activo: !sw.aVenda,
            aoMudar: (v) =>
                st.definirInterruptores(sw.com(coracoesInfinitos: v)),
          ),
          _Interruptor(
            titulo: 'Nada custa',
            detalhe: 'As compras da loja e as ajudas dos jogos não gastam '
                'ouro nem cristais.',
            valor: sw.nadaCusta,
            activo: !sw.aVenda,
            aoMudar: (v) => st.definirInterruptores(sw.com(nadaCusta: v)),
          ),
          const SizedBox(height: 22),

          _Secao('Calendário'),
          _LinhaDeAcao(
            titulo: sw.desvioDeDias == 0
                ? 'Hoje'
                : '${sw.desvioDeDias} dia${sw.desvioDeDias == 1 ? '' : 's'} '
                      'à frente',
            detalhe: 'Empurra o dia para a frente para ver a sequência, a '
                'reposição dos corações, a bolsa diária e a campanha da '
                'semana a virar sem esperar pela meia-noite.',
            botoes: [
              (
                rotulo: '+1 dia',
                cor: S.chart,
                acao: () => st.definirInterruptores(
                  sw.com(desvioDeDias: sw.desvioDeDias + 1),
                ),
              ),
              (
                rotulo: '+7 dias',
                cor: S.chart,
                acao: () => st.definirInterruptores(
                  sw.com(desvioDeDias: sw.desvioDeDias + 7),
                ),
              ),
              if (sw.desvioDeDias != 0)
                (
                  rotulo: 'Voltar a hoje',
                  cor: S.txSoft,
                  acao: () => st.definirInterruptores(sw.com(desvioDeDias: 0)),
                ),
            ],
          ),
          const SizedBox(height: 22),

          _Secao('Carteira'),
          _LinhaDeAcao(
            titulo: 'Ouro ${st.carteira.gc} · cristais ${st.carteira.cc}',
            detalhe: 'Enche a carteira a sério, para se ver a loja e as '
                'ajudas a funcionar com saldo verdadeiro.',
            botoes: [
              (
                rotulo: '+1000 ouro',
                cor: S.gold,
                acao: () => st.darMoedas(ouro: 1000),
              ),
              (
                rotulo: '+100 cristais',
                cor: S.green300,
                acao: () => st.darMoedas(cristais: 100),
              ),
            ],
          ),
          const SizedBox(height: 22),

          _Secao('Recomeçar'),
          _LinhaDeAcao(
            titulo: '${st.niveisConcluidosTotal} níveis feitos, ${st.xp} XP',
            detalhe: 'Apaga o progresso, a carteira, a colecção e as '
                'conquistas. Guarda o nome, a classe e estes '
                'interruptores.',
            botoes: [
              (
                rotulo: 'Apagar o progresso',
                cor: S.life,
                acao: () => _confirmarApagar(context, st),
              ),
            ],
          ),
          const SizedBox(height: 26),
          const _Rodape(),
        ],
      ),
    );
  }

  static Future<void> _confirmarApagar(
    BuildContext context,
    AppState st,
  ) async {
    final sim = await showDialog<bool>(
      context: context,
      builder: (_) => AlertDialog(
        backgroundColor: S.gm800,
        title: const Text('Apagar tudo?', style: TextStyle(color: S.tx)),
        content: const Text(
          'O progresso, o XP, a carteira, a colecção e as conquistas '
          'desaparecem. Não há como voltar atrás.',
          style: TextStyle(color: S.txSoft),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: const Text('Deixar como está'),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            child: const Text('Apagar', style: TextStyle(color: S.life)),
          ),
        ],
      ),
    );
    if (sim == true) await st.apagarProgresso();
  }
}

/* ---------------------------------------------------------------- saltador */

/// Classe → disciplina → unidade → nível, e entra.
///
/// Três listas e não uma árvore: são 668 níveis em 55 disciplinas, e uma
/// árvore inteira num telemóvel é mais rolo do que caminho.
class _Saltador extends StatefulWidget {
  const _Saltador();

  @override
  State<_Saltador> createState() => _SaltadorState();
}

class _SaltadorState extends State<_Saltador> {
  String? _classe;
  String? _cursoId;
  String? _unidadeId;

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final cursos = st.conteudo.cursos;

    // As classes pela ordem do currículo, que é a ordem em que aparecem no
    // content.json — e não por ordem alfabética, onde a 10ª vinha antes da
    // 2ª no dia em que houver 10ª.
    final classes = <String>[];
    for (final c in cursos) {
      if (!classes.contains(c.classe)) classes.add(c.classe);
    }
    final classe = _classe ?? st.classe;

    final daClasse = cursos.where((c) => c.classe == classe).toList();
    if (daClasse.isEmpty) return const SizedBox.shrink();
    final curso = daClasse.firstWhere(
      (c) => c.id == _cursoId,
      orElse: () => daClasse.first,
    );

    final unidade = curso.units.firstWhere(
      (u) => u.id == _unidadeId,
      orElse: () => curso.units.first,
    );

    return _Cartao(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          _escolha<String>(
            rotulo: 'Classe',
            valor: classe,
            itens: [for (final c in classes) (valor: c, texto: c)],
            aoMudar: (v) => setState(() {
              _classe = v;
              _cursoId = null;
              _unidadeId = null;
            }),
          ),
          const SizedBox(height: 10),
          _escolha<String>(
            rotulo: 'Disciplina',
            valor: curso.id,
            itens: [
              for (final c in daClasse) (valor: c.id, texto: c.disciplina),
            ],
            aoMudar: (v) => setState(() {
              _cursoId = v;
              _unidadeId = null;
            }),
          ),
          const SizedBox(height: 10),
          _escolha<String>(
            rotulo: 'Unidade',
            valor: unidade.id,
            itens: [
              for (var i = 0; i < curso.units.length; i++)
                (
                  valor: curso.units[i].id,
                  texto: '${i + 1}. ${curso.units[i].titulo}',
                ),
            ],
            aoMudar: (v) => setState(() => _unidadeId = v),
          ),
          const Divider(color: S.line, height: 26),
          for (final n in unidade.niveis) _nivel(st, curso, unidade, n),
        ],
      ),
    );
  }

  Widget _nivel(AppState st, Curso curso, Unidade u, Nivel n) {
    final feito = st.progresso.containsKey('${curso.id}:${u.id}:${n.id}');
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(
        children: [
          Icon(
            feito ? Icons.check_circle_rounded : Icons.circle_outlined,
            size: 16,
            color: feito ? S.green400 : S.txMut,
          ),
          const SizedBox(width: 8),
          Expanded(
            child: Text(
              n.titulo,
              style: const TextStyle(color: S.tx, fontSize: 14),
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
            ),
          ),
          // A matéria à parte da lição de propósito: a aula em voz alta é
          // outro ecrã e tem outros defeitos, e no mapa só se chega a ela
          // pelo nível onde o Roby está.
          IconButton(
            tooltip: 'Matéria',
            visualDensity: VisualDensity.compact,
            icon: Icon(
              Icons.menu_book_rounded,
              size: 20,
              color: n.materia == null ? S.txMut : S.chart,
            ),
            onPressed: n.materia == null
                ? null
                : () {
                    Sons.i.toque();
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (_) => MateriaScreen(
                          titulo: n.titulo,
                          materia: n.materia!,
                        ),
                      ),
                    );
                  },
          ),
          IconButton(
            tooltip: 'Entrar no nível',
            visualDensity: VisualDensity.compact,
            icon: const Icon(
              Icons.play_circle_fill_rounded,
              size: 24,
              color: S.chart,
            ),
            onPressed: n.questoes.isEmpty
                ? null
                : () => _entrar(st, curso, u, n),
          ),
        ],
      ),
    );
  }

  void _entrar(AppState st, Curso curso, Unidade u, Nivel n) {
    Sons.i.toque();
    final i = st.saltarPara(curso, u, n);
    if (i < 0) return;
    // Fecha o painel e abre a lição. Ao sair da lição, a criança — neste
    // caso o professor — cai na amarelinha da disciplina nova, que é onde o
    // salto o deixou.
    Navigator.of(context).pop();
    Navigator.of(context).push(
      MaterialPageRoute(builder: (_) => LessonScreen(indice: i)),
    );
  }

  Widget _escolha<T>({
    required String rotulo,
    required T valor,
    required List<({T valor, String texto})> itens,
    required ValueChanged<T?> aoMudar,
  }) => InputDecorator(
    decoration: InputDecoration(
      labelText: rotulo,
      labelStyle: const TextStyle(color: S.txSoft),
      isDense: true,
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(S.rSm),
        borderSide: const BorderSide(color: S.line),
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(S.rSm),
        borderSide: const BorderSide(color: S.line),
      ),
    ),
    child: DropdownButtonHideUnderline(
      child: DropdownButton<T>(
        value: valor,
        isExpanded: true,
        dropdownColor: S.gm800,
        style: const TextStyle(color: S.tx, fontSize: 15),
        items: [
          for (final i in itens)
            DropdownMenuItem(
              value: i.valor,
              child: Text(i.texto, overflow: TextOverflow.ellipsis),
            ),
        ],
        onChanged: aoMudar,
      ),
    ),
  );
}

/* ------------------------------------------------------- níveis dos jogos */

/// Escolher o degrau de cada joguinho à mão.
///
/// A escada vai até [nivelMaximo] e só se sobe a jogar. Sem isto não há
/// maneira de saber se o Water R Sort no nível 300 é jogável ou impossível —
/// e isso só se descobre a olhar para ele.
class _NiveisDosJogos extends StatefulWidget {
  const _NiveisDosJogos();

  @override
  State<_NiveisDosJogos> createState() => _NiveisDosJogosState();
}

class _NiveisDosJogosState extends State<_NiveisDosJogos> {
  final _nivel = TextEditingController(text: '1');

  @override
  void dispose() {
    _nivel.dispose();
    super.dispose();
  }

  int get _n {
    final v = int.tryParse(_nivel.text.trim()) ?? 1;
    return v.clamp(1, nivelMaximo);
  }

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final jogos = <({String nome, Jogo jogo, Widget Function(int) abrir})>[
      (
        nome: 'Crossmath',
        jogo: Jogo.crossmath,
        abrir: (n) => CrossmathScreen(nivel: n),
      ),
      (nome: 'Pomar', jogo: Jogo.pomar, abrir: (n) => PomarScreen(nivel: n)),
      (
        nome: 'Sopa de letras',
        jogo: Jogo.sopa,
        abrir: (n) => SopaScreen(nivel: n),
      ),
      (
        nome: 'Memória',
        jogo: Jogo.memoria,
        abrir: (n) => MemoriaScreen(nivel: n),
      ),
      (
        nome: 'Water R Sort',
        jogo: Jogo.frascos,
        abrir: (n) => FrascosScreen(nivel: n),
      ),
    ];

    return _Cartao(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            children: [
              const Expanded(
                child: Text(
                  'Abrir no nível',
                  style: TextStyle(color: S.txSoft, fontSize: 14),
                ),
              ),
              SizedBox(
                width: 92,
                child: TextField(
                  controller: _nivel,
                  keyboardType: TextInputType.number,
                  textAlign: TextAlign.center,
                  style: const TextStyle(color: S.tx, fontSize: 16),
                  decoration: InputDecoration(
                    isDense: true,
                    hintText: '1 a $nivelMaximo',
                    hintStyle: const TextStyle(color: S.txMut, fontSize: 12),
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(S.rSm),
                      borderSide: const BorderSide(color: S.line),
                    ),
                  ),
                  onChanged: (_) => setState(() {}),
                ),
              ),
            ],
          ),
          const Divider(color: S.line, height: 24),
          for (final j in jogos)
            Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: Row(
                children: [
                  Expanded(
                    child: Text(
                      '${j.nome}  ·  está no ${st.nivelDe(j.jogo)}',
                      style: const TextStyle(color: S.tx, fontSize: 14),
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                  TextButton(
                    onPressed: () {
                      Sons.i.toque();
                      final n = _n;
                      Navigator.of(context).push(
                        MaterialPageRoute(builder: (_) => j.abrir(n)),
                      );
                    },
                    child: Text(
                      'Abrir no $_n',
                      style: const TextStyle(color: S.chart),
                    ),
                  ),
                ],
              ),
            ),
          Text(
            'A bolsa de tempo está sem limite: '
            '${tempoEmPalavras(st.tempoDeJogo)} à disposição.',
            style: const TextStyle(color: S.txMut, fontSize: 12.5),
          ),
        ],
      ),
    );
  }
}

/* ------------------------------------------------------------------ peças */

class _Secao extends StatelessWidget {
  final String texto;
  const _Secao(this.texto);

  @override
  Widget build(BuildContext context) => Padding(
    padding: const EdgeInsets.only(bottom: 8),
    child: Text(
      texto.toUpperCase(),
      style: const TextStyle(
        color: S.txMut,
        fontSize: 12,
        fontWeight: FontWeight.w800,
        letterSpacing: 1.1,
      ),
    ),
  );
}

class _Cartao extends StatelessWidget {
  final Widget child;
  const _Cartao({required this.child});

  @override
  Widget build(BuildContext context) => Container(
    padding: const EdgeInsets.all(14),
    decoration: BoxDecoration(
      color: S.surface,
      borderRadius: BorderRadius.circular(S.rMd),
      border: Border.all(color: S.line),
    ),
    child: child,
  );
}

class _Interruptor extends StatelessWidget {
  final String titulo;
  final String detalhe;
  final bool valor;
  final bool activo;
  final Color? cor;
  final ValueChanged<bool> aoMudar;

  const _Interruptor({
    required this.titulo,
    required this.detalhe,
    required this.valor,
    required this.aoMudar,
    this.activo = true,
    this.cor,
  });

  @override
  Widget build(BuildContext context) => Opacity(
    opacity: activo ? 1 : 0.45,
    child: Padding(
      padding: const EdgeInsets.only(bottom: 10),
      child: _Cartao(
        child: Row(
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    titulo,
                    style: const TextStyle(
                      color: S.tx,
                      fontSize: 15.5,
                      fontWeight: FontWeight.w700,
                    ),
                  ),
                  const SizedBox(height: 3),
                  Text(
                    detalhe,
                    style: const TextStyle(color: S.txSoft, fontSize: 12.5),
                  ),
                ],
              ),
            ),
            const SizedBox(width: 10),
            Switch(
              value: valor,
              activeThumbColor: cor ?? S.chart,
              onChanged: activo
                  ? (v) {
                      Sons.i.toque();
                      aoMudar(v);
                    }
                  : null,
            ),
          ],
        ),
      ),
    ),
  );
}

class _LinhaDeAcao extends StatelessWidget {
  final String titulo;
  final String detalhe;
  final List<({String rotulo, Color cor, VoidCallback acao})> botoes;

  const _LinhaDeAcao({
    required this.titulo,
    required this.detalhe,
    required this.botoes,
  });

  @override
  Widget build(BuildContext context) => _Cartao(
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          titulo,
          style: const TextStyle(
            color: S.tx,
            fontSize: 15.5,
            fontWeight: FontWeight.w700,
          ),
        ),
        const SizedBox(height: 3),
        Text(detalhe, style: const TextStyle(color: S.txSoft, fontSize: 12.5)),
        const SizedBox(height: 6),
        Wrap(
          spacing: 8,
          children: [
            for (final b in botoes)
              TextButton(
                onPressed: () {
                  Sons.i.toque();
                  b.acao();
                },
                child: Text(b.rotulo, style: TextStyle(color: b.cor)),
              ),
          ],
        ),
      ],
    ),
  );
}

class _Rodape extends StatelessWidget {
  const _Rodape();

  @override
  Widget build(BuildContext context) {
    final st = context.watch<AppState>();
    final faltam = ModoTeste.diasQueFaltam();
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Somara ${ModoTeste.versao.isEmpty ? '(versão não declarada)' : ModoTeste.versao} · TESTE',
          style: const TextStyle(color: S.txSoft, fontSize: 13),
        ),
        const SizedBox(height: 3),
        Text(
          'conteúdo ${st.conteudo.versao}'
          '${ModoTeste.compiladaEm.isEmpty ? '' : ' · compilada em ${ModoTeste.compiladaEm}'}',
          style: const TextStyle(color: S.txMut, fontSize: 12.5),
        ),
        const SizedBox(height: 3),
        Text(
          faltam == null
              ? 'Esta versão não caduca (sem data de compilação).'
              : 'Caduca dentro de $faltam dia${faltam == 1 ? '' : 's'}.',
          style: const TextStyle(color: S.txMut, fontSize: 12.5),
        ),
        const SizedBox(height: 10),
        const Text(
          'Nada do que se faz nesta versão vai para a nuvem nem entra no '
          'ranking. A conta está desligada de propósito: centenas de níveis '
          'feitos a saltar não podem misturar-se com o trabalho das '
          'crianças.',
          style: TextStyle(color: S.txMut, fontSize: 12.5, height: 1.45),
        ),
      ],
    );
  }
}
