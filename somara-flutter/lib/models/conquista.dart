import 'escadaria.dart';

/// As três famílias de conquistas.
///
/// A ordem é a ordem em que aparecem no histórico, e o estudo vem primeiro
/// de propósito: são vinte e quatro medalhas de jogos contra doze de escola,
/// e sem cabeçalhos e sem ordem a parede lia-se como a de uma consola.
enum FamiliaDeConquista {
  estudo('Escola', 'O que já aprendeste.'),
  consistencia('Todos os dias', 'Voltar é a parte difícil.'),
  jogos('Joguinhos', 'As escadarias dos quatro jogos.');

  final String rotulo;
  final String descricao;
  const FamiliaDeConquista(this.rotulo, this.descricao);
}

/// Uma conquista.
///
/// O `name` do enum é o identificador guardado — mudá-lo faz uma criança
/// perder uma medalha que ganhou.
///
/// A **pista** não é enfeite: é o que uma medalha por ganhar mostra em vez
/// do nome. Uma silhueta sem pista é um buraco na parede que não diz o que
/// lá deve estar, e ninguém persegue o que não sabe o que é.
enum Conquista {
  // ---- Escola ----
  primeiroNivel(
    FamiliaDeConquista.estudo,
    'O primeiro passo',
    'Termina o teu primeiro nível.',
    cristais: 0,
  ),
  primeiraUnidade(
    FamiliaDeConquista.estudo,
    'Uma unidade inteira',
    'Termina todos os níveis de uma unidade.',
    cristais: 1,
  ),
  cincoUnidades(
    FamiliaDeConquista.estudo,
    'Cinco unidades',
    'Termina cinco unidades.',
    cristais: 1,
  ),
  cemNiveis(
    FamiliaDeConquista.estudo,
    'Cem níveis',
    'Termina cem níveis, de qualquer disciplina.',
    cristais: 2,
  ),
  disciplinaCompleta(
    FamiliaDeConquista.estudo,
    'Uma disciplina do princípio ao fim',
    'Termina todas as unidades de uma disciplina.',
    cristais: 3,
  ),
  classeCompleta(
    FamiliaDeConquista.estudo,
    'Uma classe inteira',
    'Termina todas as disciplinas da tua classe.',
    cristais: 5,
  ),
  nivelPerfeito(
    FamiliaDeConquista.estudo,
    'Sem um único erro',
    'Termina um nível sem errar nada.',
    cristais: 0,
  ),
  dezPerfeitos(
    FamiliaDeConquista.estudo,
    'Dez sem erro nenhum',
    'Termina dez níveis sem errar nada.',
    cristais: 1,
  ),
  recuperada(
    FamiliaDeConquista.estudo,
    'Aprendeste o que tinhas errado',
    'Acerta, a rever, uma pergunta que tinhas errado.',
    cristais: 0,
  ),
  dezRecuperadas(
    FamiliaDeConquista.estudo,
    'Dez erros corrigidos',
    'Acerta dez perguntas que tinhas errado.',
    cristais: 1,
  ),

  // ---- Todos os dias ----
  tresDias(
    FamiliaDeConquista.consistencia,
    'Três dias seguidos',
    'Estuda três dias seguidos.',
    cristais: 0,
  ),
  umaSemana(
    FamiliaDeConquista.consistencia,
    'Uma semana seguida',
    'Estuda sete dias seguidos.',
    cristais: 1,
  ),
  umMes(
    FamiliaDeConquista.consistencia,
    'Um mês seguido',
    'Estuda trinta dias seguidos.',
    cristais: 3,
  ),
  estudarPrimeiro(
    FamiliaDeConquista.consistencia,
    'Primeiro a escola',
    'Cinco dias a fio a estudar antes de jogar.',
    cristais: 1,
  ),

  // ---- Joguinhos ----
  // Estas duas não são degraus: são coisas que se fazem DENTRO de um nível,
  // e precisaram de instrumentar os jogos. Ficaram de fora quando as
  // medalhas nasceram, por isso mesmo.
  primeiraEspecial(
    FamiliaDeConquista.jogos,
    'A tua primeira peça especial',
    'Junta quatro ou mais frutas iguais no Pomar.',
  ),
  sopaSemFalhar(
    FamiliaDeConquista.jogos,
    'Sopa sem falhar uma letra',
    'Acaba uma sopa sem arrastar por cima de uma palavra errada.',
    cristais: 1,
  ),

  // Seis degraus por jogo. Os primeiros chegam na mesma tarde; o 250 e o 500
  // são de meses. É esse espaçamento que os faz valer alguma coisa.
  crossmath10(FamiliaDeConquista.jogos, 'Crossmath 10', '',
      jogo: Jogo.crossmath, degrau: 10),
  crossmath50(FamiliaDeConquista.jogos, 'Crossmath 50', '',
      jogo: Jogo.crossmath, degrau: 50),
  crossmath100(FamiliaDeConquista.jogos, 'Crossmath 100', '',
      jogo: Jogo.crossmath, degrau: 100),
  crossmath250(FamiliaDeConquista.jogos, 'Crossmath 250', '',
      jogo: Jogo.crossmath, degrau: 250),
  crossmath500(FamiliaDeConquista.jogos, 'Crossmath 500', '',
      jogo: Jogo.crossmath, degrau: 500, cristais: 1),
  crossmath1000(FamiliaDeConquista.jogos, 'Crossmath 1000', '',
      jogo: Jogo.crossmath, degrau: 1000, cristais: 2),

  pomar10(FamiliaDeConquista.jogos, 'Pomar 10', '',
      jogo: Jogo.pomar, degrau: 10),
  pomar50(FamiliaDeConquista.jogos, 'Pomar 50', '',
      jogo: Jogo.pomar, degrau: 50),
  pomar100(FamiliaDeConquista.jogos, 'Pomar 100', '',
      jogo: Jogo.pomar, degrau: 100),
  pomar250(FamiliaDeConquista.jogos, 'Pomar 250', '',
      jogo: Jogo.pomar, degrau: 250),
  pomar500(FamiliaDeConquista.jogos, 'Pomar 500', '',
      jogo: Jogo.pomar, degrau: 500, cristais: 1),
  pomar1000(FamiliaDeConquista.jogos, 'Pomar 1000', '',
      jogo: Jogo.pomar, degrau: 1000, cristais: 2),

  sopa10(FamiliaDeConquista.jogos, 'Sopa 10', '',
      jogo: Jogo.sopa, degrau: 10),
  sopa50(FamiliaDeConquista.jogos, 'Sopa 50', '',
      jogo: Jogo.sopa, degrau: 50),
  sopa100(FamiliaDeConquista.jogos, 'Sopa 100', '',
      jogo: Jogo.sopa, degrau: 100),
  sopa250(FamiliaDeConquista.jogos, 'Sopa 250', '',
      jogo: Jogo.sopa, degrau: 250),
  sopa500(FamiliaDeConquista.jogos, 'Sopa 500', '',
      jogo: Jogo.sopa, degrau: 500, cristais: 1),
  sopa1000(FamiliaDeConquista.jogos, 'Sopa 1000', '',
      jogo: Jogo.sopa, degrau: 1000, cristais: 2),

  memoria10(FamiliaDeConquista.jogos, 'Memória 10', '',
      jogo: Jogo.memoria, degrau: 10),
  memoria50(FamiliaDeConquista.jogos, 'Memória 50', '',
      jogo: Jogo.memoria, degrau: 50),
  memoria100(FamiliaDeConquista.jogos, 'Memória 100', '',
      jogo: Jogo.memoria, degrau: 100),
  memoria250(FamiliaDeConquista.jogos, 'Memória 250', '',
      jogo: Jogo.memoria, degrau: 250),
  memoria500(FamiliaDeConquista.jogos, 'Memória 500', '',
      jogo: Jogo.memoria, degrau: 500, cristais: 1),
  memoria1000(FamiliaDeConquista.jogos, 'Memória 1000', '',
      jogo: Jogo.memoria, degrau: 1000, cristais: 2),

  frascos10(FamiliaDeConquista.jogos, 'Water R Sort 10', '',
      jogo: Jogo.frascos, degrau: 10),
  frascos50(FamiliaDeConquista.jogos, 'Water R Sort 50', '',
      jogo: Jogo.frascos, degrau: 50),
  frascos100(FamiliaDeConquista.jogos, 'Water R Sort 100', '',
      jogo: Jogo.frascos, degrau: 100),
  frascos250(FamiliaDeConquista.jogos, 'Water R Sort 250', '',
      jogo: Jogo.frascos, degrau: 250),
  frascos500(FamiliaDeConquista.jogos, 'Water R Sort 500', '',
      jogo: Jogo.frascos, degrau: 500, cristais: 1),
  frascos1000(FamiliaDeConquista.jogos, 'Water R Sort 1000', '',
      jogo: Jogo.frascos, degrau: 1000, cristais: 2);

  final FamiliaDeConquista familia;
  final String titulo;

  /// O que fazer para a ganhar. Vazio nas dos jogos, que se explicam pelo
  /// próprio título — ver [pistaDita].
  final String _pista;

  /// Cristais que paga. Zero na maior parte: uma medalha que paga sempre
  /// deixa de ser uma medalha e passa a ser um salário.
  final int cristais;

  /// Só nas conquistas de jogo.
  final Jogo? jogo;
  final int degrau;

  const Conquista(
    this.familia,
    this.titulo,
    this._pista, {
    this.cristais = 0,
    this.jogo,
    this.degrau = 0,
  });

  String get pistaDita =>
      _pista.isNotEmpty ? _pista : 'Chega ao nível $degrau d$_doJogo.';

  String get _doJogo => switch (jogo) {
    Jogo.sopa => 'a Sopa de letras',
    Jogo.memoria => 'a Memória',
    Jogo.pomar => 'o Pomar',
    Jogo.crossmath => 'o Crossmath',
    Jogo.frascos => 'o Water R Sort',
    null => 'o jogo',
  };
}

/// Os factos de que as condições precisam, e nada mais.
///
/// Existe para as condições serem uma função pura de números, e não uma
/// consulta ao estado inteiro da app. É o que torna possível provar as
/// trinta e seis num teste sem montar um aluno de verdade para cada uma.
class RetratoDoAluno {
  /// Níveis de lição concluídos, somando todas as classes.
  final int niveis;

  /// Unidades em que todos os níveis estão feitos.
  final int unidades;

  /// Disciplinas com todas as unidades feitas.
  final int disciplinas;

  /// Classes com todas as disciplinas feitas.
  final int classes;

  /// Níveis fechados a 100%.
  final int perfeitos;

  /// Perguntas que estavam nos Guardados e passaram a certas.
  final int recuperadas;

  /// Dias seguidos de estudo.
  final int diasSeguidos;

  /// Dias a fio em que o primeiro acto do dia foi estudar, e não jogar.
  final int diasAEstudarPrimeiro;

  /// Peças especiais nascidas no Pomar, ao todo.
  final int especiaisNoPomar;

  /// Sopas fechadas sem uma única selecção errada.
  final int sopasPerfeitas;

  /// O degrau de cada joguinho.
  final Map<Jogo, int> degraus;

  const RetratoDoAluno({
    this.niveis = 0,
    this.unidades = 0,
    this.disciplinas = 0,
    this.classes = 0,
    this.perfeitos = 0,
    this.recuperadas = 0,
    this.diasSeguidos = 0,
    this.diasAEstudarPrimeiro = 0,
    this.especiaisNoPomar = 0,
    this.sopasPerfeitas = 0,
    this.degraus = const {},
  });
}

/// Já foi alcançada?
///
/// Um `switch` e não uma função guardada dentro de cada entrada do enum:
/// assim o compilador obriga a que uma conquista nova traga a sua condição,
/// em vez de ficar para sempre por ganhar sem ninguém reparar.
bool alcancada(Conquista c, RetratoDoAluno r) {
  final j = c.jogo;
  if (j != null) return (r.degraus[j] ?? 1) >= c.degrau;

  return switch (c) {
    Conquista.primeiroNivel => r.niveis >= 1,
    Conquista.primeiraUnidade => r.unidades >= 1,
    Conquista.cincoUnidades => r.unidades >= 5,
    Conquista.cemNiveis => r.niveis >= 100,
    Conquista.disciplinaCompleta => r.disciplinas >= 1,
    Conquista.classeCompleta => r.classes >= 1,
    Conquista.nivelPerfeito => r.perfeitos >= 1,
    Conquista.dezPerfeitos => r.perfeitos >= 10,
    Conquista.recuperada => r.recuperadas >= 1,
    Conquista.dezRecuperadas => r.recuperadas >= 10,
    Conquista.tresDias => r.diasSeguidos >= 3,
    Conquista.umaSemana => r.diasSeguidos >= 7,
    Conquista.umMes => r.diasSeguidos >= 30,
    Conquista.estudarPrimeiro => r.diasAEstudarPrimeiro >= 5,
    Conquista.primeiraEspecial => r.especiaisNoPomar >= 1,
    Conquista.sopaSemFalhar => r.sopasPerfeitas >= 1,
    // As dos jogos saíram acima, pelo [c.jogo].
    _ => false,
  };
}

/// Todas as que este retrato já alcançou.
Set<Conquista> conquistasDe(RetratoDoAluno r) =>
    {for (final c in Conquista.values) if (alcancada(c, r)) c};
