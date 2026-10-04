/// Quem ensina o quê, e como se chama.
///
/// A matilha do Roby atravessa o país de classe em classe, e da 4ª em diante
/// há um animal-professor por disciplina. As fichas completas de cada um —
/// história, carácter, roupa, cores, o que diz quando a criança acerta e
/// quando erra — estão em `docs/personagens/`. Aqui fica só o que o código
/// precisa de saber: o nome, a espécie, as disciplinas e o nome dos
/// ficheiros de desenho.
///
/// **Nada disto aparece no ecrã ainda.** Os desenhos não existem, e mostrar
/// o Mestre Escamas com a cara do Roby ensinaria a criança a ligar o nome à
/// cara errada — o que depois não se desfaz. Isto está escrito antes porque
/// é o que torna o trabalho de quem desenha possível, e porque o teste que o
/// acompanha não deixa entrar uma disciplina nova sem personagem.
class Personagem {
  /// Como se chama, por extenso, como aparecerá à criança.
  final String nome;

  /// Nome curto, para os ficheiros e para a ficha em `docs/personagens/`.
  final String slug;

  final String especie;

  /// As disciplinas que ensina, com o nome exacto do currículo — o mesmo que
  /// está no `content.json`.
  ///
  /// Vazio em quem não ensina: o Roby, que está em toda a app, e a Hiena
  /// Ri-Ri, que só existe nas histórias.
  final List<String> disciplinas;

  const Personagem({
    required this.nome,
    required this.slug,
    required this.especie,
    this.disciplinas = const [],
  });

  /// O desenho desta personagem numa pose.
  ///
  /// As quatro poses que fazem falta a todas são `neutro`, `a-explicar`,
  /// `a-animar` e `a-pensar` — ver `docs/personagens/README.md`.
  ///
  /// O Roby é a excepção: os trinta e oito desenhos dele já existem com
  /// outro nome (`roby-feliz.png` e não `personagem-roby-a-animar.png`), e
  /// mudar-lhes o nome obrigava a mexer em meia app para não ganhar nada.
  String desenho(String pose) =>
      slug == 'roby' ? 'assets/img/roby-$pose.png'
                     : 'assets/img/personagem-$slug-$pose.png';
}

/// O elenco inteiro. A ordem é a do documento.
const elenco = <Personagem>[
  Personagem(nome: 'Roby', slug: 'roby', especie: 'mabeco'),
  Personagem(
    nome: 'Mestre Escamas',
    slug: 'escamas',
    especie: 'pangolim',
    disciplinas: ['Matemática'],
  ),
  Personagem(
    nome: 'Avó Coruja',
    slug: 'coruja',
    especie: 'coruja',
    disciplinas: ['Português'],
  ),
  // A mesma matéria a crescer: as Ciências Naturais do primário são a
  // Biologia do secundário, e por isso é o mesmo professor.
  Personagem(
    nome: 'Lolo',
    slug: 'lolo',
    especie: 'camaleão',
    disciplinas: ['Ciências Naturais', 'Biologia'],
  ),
  Personagem(
    nome: 'Avô Nzou',
    slug: 'nzou',
    especie: 'elefante',
    disciplinas: ['Ciências Sociais', 'História'],
  ),
  Personagem(
    nome: 'Dona Águia',
    slug: 'aguia',
    especie: 'águia-pesqueira',
    disciplinas: ['Geografia'],
  ),
  // As línguas não se partilham: na 8ª e na 9ª o aluno tem as duas no mesmo
  // ano, e a mesma ave nas duas lê-se como descuido.
  Personagem(
    nome: 'Andorinha',
    slug: 'andorinha',
    especie: 'andorinha',
    disciplinas: ['Inglês'],
  ),
  Personagem(
    nome: 'Garça Nyanja',
    slug: 'garca',
    especie: 'garça-branca',
    disciplinas: ['Francês'],
  ),
  Personagem(
    nome: 'Eco',
    slug: 'eco',
    especie: 'morcego',
    disciplinas: ['Física'],
  ),
  Personagem(
    nome: 'Tia Formiga',
    slug: 'formiga',
    especie: 'formiga',
    disciplinas: ['Química'],
  ),
  // O mesmo nome em duas fases do currículo.
  Personagem(
    nome: 'Pintinha',
    slug: 'pintinha',
    especie: 'borboleta',
    disciplinas: ['Educação Visual e Ofícios', 'Educação Visual'],
  ),
  Personagem(
    nome: 'Impala Veloz',
    slug: 'impala',
    especie: 'impala',
    disciplinas: ['Educação Física'],
  ),
  Personagem(
    nome: 'Mãe Galinha-do-mato',
    slug: 'galinha',
    especie: 'galinha-do-mato',
    disciplinas: ['Agropecuária'],
  ),
  Personagem(
    nome: 'Tecelã',
    slug: 'tecela',
    especie: 'aranha',
    disciplinas: ['TIC'],
  ),
  // Não ensina nada: é a que estava de fora e passa a ser da matilha. Nunca
  // entra num exercício — ver `docs/personagens/riri.md`.
  Personagem(nome: 'Hiena Ri-Ri', slug: 'riri', especie: 'hiena'),
];

/// Quem ensina esta disciplina. Nulo quando não há ninguém — e aí o teste
/// `personagens_test` dá erro, que é o que se quer.
Personagem? personagemDe(String disciplina) {
  for (final p in elenco) {
    if (p.disciplinas.contains(disciplina)) return p;
  }
  return null;
}
