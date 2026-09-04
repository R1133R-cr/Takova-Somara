/// Um solucionador do Water R Sort às cegas, só para os testes.
///
/// Não sabe nada de como o tabuleiro foi montado: recebe frascos e procura
/// uma saída. É por isso que serve de prova — se usasse o caminho que o
/// gerador guardou, estava a provar-se a si mesmo.
///
/// Não vai em `lib/` de propósito. O jogo não precisa dele para nada: os
/// níveis nascem resolúveis por construção, e uma procura destas a correr
/// no telemóvel de uma criança seria trabalho a mais para nada.
///
/// Este ficheiro não acaba em `_test.dart`, e por isso o `flutter test` não
/// o corre — é uma biblioteca de apoio, não uma bateria.
library;

import 'package:somara/models/frascos.dart';

typedef Jogada = ({int de, int para});

/// O caminho até ao tabuleiro arrumado, ou nulo se não houver.
///
/// Devolve nulo também quando desiste por [tecto]. Nos testes isso conta
/// como falha, e deve contar: um nível que precisa de trezentos mil estados
/// para se resolver não é um nível para uma criança.
List<Jogada>? caminho(Frascos inicio, {int tecto = 300000}) {
  final vistos = <String>{_chave(inicio)};
  final andamento = <Jogada>[];
  final conta = _Conta();
  return _procurar(inicio, vistos, andamento, conta, tecto);
}

/// Só diz se tem solução, e quantos estados custou dizê-lo.
({bool resolvido, int estados}) resolver(Frascos inicio, {int tecto = 300000}) {
  final vistos = <String>{_chave(inicio)};
  final andamento = <Jogada>[];
  final conta = _Conta();
  final r = _procurar(inicio, vistos, andamento, conta, tecto);
  return (resolvido: r != null, estados: conta.n);
}

class _Conta {
  int n = 0;
}

/// Dois tabuleiros que só diferem na ORDEM dos frascos são o mesmo
/// tabuleiro. Ordenar a chave é o corte que faz isto caber em memória.
String _chave(Frascos f) => ([
  for (final t in f.frascos) t.blocos.map((c) => c.index).join(','),
]..sort()).join('|');

List<Jogada>? _procurar(
  Frascos estado,
  Set<String> vistos,
  List<Jogada> andamento,
  _Conta conta,
  int tecto,
) {
  if (estado.ganho) return List.of(andamento);
  if (++conta.n > tecto) return null;

  final seguintes = <({Frascos estado, Jogada jogada, int nota})>[];
  for (var i = 0; i < estado.frascos.length; i++) {
    for (var j = 0; j < estado.frascos.length; j++) {
      if (estado.quantosDespeja(i, j) == 0) continue;
      // Mudar um frasco de uma cor só para outro vazio dá o mesmo
      // tabuleiro com os frascos trocados. Não é jogada, é arrumar a mesa.
      if (estado.frascos[i].deUmaCor && estado.frascos[j].vazio) continue;

      final novo = estado.despejar(i, j);
      seguintes.add((
        estado: novo,
        jogada: (de: i, para: j),
        nota: _promessa(novo, j),
      ));
    }
  }

  // Do mais promissor para o menos: fechar uma cor vale muito, e ter
  // frascos vazios vale alguma coisa porque é espaço para manobrar.
  seguintes.sort((a, b) => b.nota.compareTo(a.nota));

  for (final s in seguintes) {
    if (!vistos.add(_chave(s.estado))) continue;
    andamento.add(s.jogada);
    final r = _procurar(s.estado, vistos, andamento, conta, tecto);
    if (r != null) return r;
    andamento.removeLast();
  }
  return null;
}

int _promessa(Frascos e, int destino) {
  var n = e.frascos.where((f) => f.vazio).length;
  if (e.frascos[destino].cheio && e.frascos[destino].deUmaCor) n += 10;
  return n;
}
