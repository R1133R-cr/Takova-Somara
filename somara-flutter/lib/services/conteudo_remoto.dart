import 'dart:convert';
import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:path_provider/path_provider.dart';
import '../models/content.dart';

/// Mantém o currículo actualizado sem obrigar a instalar a app de novo.
///
/// Corrigir uma resposta errada ou acrescentar um nível passa a ser publicar
/// um ficheiro; as apps instaladas apanham-no sozinhas. Isto importa porque
/// um erro numa pergunta, hoje, só se corrige com um APK novo em cada
/// telemóvel — o que na prática significa que não se corrige.
///
/// Duas regras que moldam tudo o resto:
///
///  1. **Nunca esperar pela rede.** A app abre com o que já tem e vai buscar
///     a versão nova por trás. Uma criança em Lichinga com rede fraca não
///     pode ficar a olhar para um ecrã de espera.
///
///  2. **Nunca confiar no que chega.** Um ficheiro truncado ou mal editado
///     publicado por engano tem de ser recusado, não guardado. Se passasse,
///     estragava todas as apps instaladas de uma vez — e sem forma de
///     desfazer, porque a app já não abriria para se actualizar.
class ConteudoRemoto {
  /// O ramo `main` no GitHub Pages é o que está publicado. Trabalhar noutro
  /// ramo não mexe no que as crianças têm — só a junção a `main` é que
  /// publica.
  ///
  /// Pode apontar-se para outro sítio ao compilar, o que serve para
  /// experimentar uma actualização antes de a publicar a sério:
  ///   flutter build apk --dart-define=SOMARA_CONTENT_URL=http://…
  static const url = String.fromEnvironment(
    'SOMARA_CONTENT_URL',
    defaultValue:
        'https://r1133r-cr.github.io/Takova-Somara/somara-flutter/assets/content.json',
  );

  static const _nomeFicheiro = 'content-descarregado.json';

  /// Tempo máximo à espera da rede. Curto de propósito: isto corre por trás
  /// e não há pressa nenhuma — se falhar, tenta-se da próxima vez que a app
  /// abrir.
  static const _limite = Duration(seconds: 20);

  static Future<File> _ficheiro() async {
    final dir = await getApplicationDocumentsDirectory();
    return File('${dir.path}/$_nomeFicheiro');
  }

  /// O conteúdo a usar agora: o descarregado, se existir e servir; senão o
  /// que veio dentro da app.
  ///
  /// O que estiver gravado já foi validado antes de ser gravado, mas
  /// verifica-se à mesma — um ficheiro em disco pode corromper-se, e cair
  /// para o conteúdo de origem é sempre melhor do que não abrir.
  static Future<Conteudo> carregar() async {
    try {
      final f = await _ficheiro();
      if (await f.exists()) {
        final guardado = Conteudo.deTexto(await f.readAsString());
        final origem = await Conteudo.carregar();
        // Se a app for reinstalada com conteúdo mais recente do que o
        // descarregado, é o de origem que vale.
        if (guardado.versao > origem.versao) return guardado;
        await f.delete();
        return origem;
      }
    } catch (e) {
      debugPrint('conteúdo descarregado ilegível, a usar o de origem: $e');
      try {
        await (await _ficheiro()).delete();
      } catch (_) {}
    }
    return Conteudo.carregar();
  }

  /// Procura uma versão mais recente e guarda-a para a próxima abertura.
  ///
  /// Devolve `true` se guardou alguma coisa. Não aplica a mudança à sessão
  /// a decorrer de propósito: ver os níveis mudarem de sítio a meio de uma
  /// lição seria desconcertante para a criança.
  ///
  /// Nunca lança — falhar em silêncio é o comportamento certo aqui.
  static Future<bool> procurarActualizacao(int versaoActual) async {
    HttpClient? cliente;
    try {
      cliente = HttpClient()..connectionTimeout = _limite;
      final pedido = await cliente.getUrl(Uri.parse(url)).timeout(_limite);
      final resposta = await pedido.close().timeout(_limite);
      if (resposta.statusCode != 200) {
        debugPrint('conteúdo remoto: HTTP ${resposta.statusCode}');
        return false;
      }

      final texto = await resposta.transform(utf8.decoder).join().timeout(_limite);

      // Validar antes de gravar. É aqui que se trava um ficheiro estragado.
      final novo = Conteudo.deTexto(texto);
      final problema = validar(novo, versaoActual);
      if (problema != null) {
        debugPrint('conteúdo remoto recusado: $problema');
        return false;
      }

      await (await _ficheiro()).writeAsString(texto, flush: true);
      debugPrint('conteúdo actualizado para a versão ${novo.versao}');
      return true;
    } catch (e) {
      debugPrint('conteúdo remoto indisponível: $e');
      return false;
    } finally {
      cliente?.close(force: true);
    }
  }

  /// Diz porque é que este conteúdo não serve, ou `null` se servir.
  ///
  /// Separado da rede de propósito, para poder ser testado com ficheiros
  /// estragados à mão — que é a única maneira de ter a certeza de que a
  /// recusa funciona antes de precisarmos dela a sério.
  static String? validar(Conteudo c, int versaoActual) {
    if (c.versao <= versaoActual) {
      return 'versão ${c.versao} não é mais recente que $versaoActual';
    }
    if (c.cursos.isEmpty) return 'sem cursos';

    for (final curso in c.cursos) {
      if (curso.id.trim().isEmpty) return 'curso sem identificador';
      if (curso.disciplina.trim().isEmpty) return '${curso.id}: sem disciplina';
      if (curso.classe.trim().isEmpty) return '${curso.id}: sem classe';

      final niveis = curso.niveisEmSequencia;
      // Um curso com um punhado de níveis daria uma amarelinha vazia. Mais
      // vale ficar com o conteúdo anterior do que mostrar um mapa deserto.
      if (niveis.length < 4) {
        return '${curso.id}: só ${niveis.length} níveis';
      }

      for (final lv in niveis) {
        final onde = '${curso.id}/${lv.nivel.id}';
        if (lv.nivel.titulo.trim().isEmpty) return '$onde: nível sem título';
        if (lv.nivel.questoes.isEmpty) return '$onde: nível sem perguntas';

        for (final q in lv.nivel.questoes) {
          if (q.q.trim().isEmpty) return '$onde: pergunta sem enunciado';
          final mal = _questaoInvalida(q);
          if (mal != null) return '$onde: $mal';
        }
      }
    }
    return null;
  }

  /// Uma resposta fora do intervalo das opções faria a lição rebentar a meio.
  static String? _questaoInvalida(Questao q) {
    switch (q) {
      case QCount():
        if (q.options.isEmpty) return 'pergunta de contar sem opções';
        if (q.a < 0 || q.a >= q.options.length) return 'resposta fora das opções';
        if (q.n <= 0) return 'quantidade inválida';
      case QChoice():
        if (q.options.length < 2) return 'escolha com menos de duas opções';
        if (q.a < 0 || q.a >= q.options.length) return 'resposta fora das opções';
      case QInput():
        if (q.a.trim().isEmpty) return 'pergunta escrita sem resposta';
      case QMatch():
        if (q.pairs.length < 2) return 'ligação com menos de dois pares';
      case QDrag():
        if (q.zones.length < 2) return 'arrastar com menos de duas zonas';
        if (q.a < 0 || q.a >= q.zones.length) return 'zona certa fora do intervalo';
    }
    return null;
  }
}
