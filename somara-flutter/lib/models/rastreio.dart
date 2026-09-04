/// O que a criança tocou no nível que está a jogar.
///
/// Serve uma pergunta só, e é a que faz a Sorte valer alguma coisa: **onde
/// é que ela não olhou?** Uma ajuda que aponta para o sítio onde ela já
/// estava a trabalhar não ajuda — diz-lhe o que ela já sabia. A ajuda útil é
/// a que mostra o canto do tabuleiro em que o dedo dela nunca passou.
///
/// Vive só enquanto o nível durar e não se guarda em lado nenhum. Por isso é
/// mutável, ao contrário de quase tudo o resto: é um bloco de rascunho, não
/// um facto sobre a criança.
class Rastreio {
  final Map<int, int> _toques = {};

  /// Quantas vezes cada casa foi tocada. Só para ler.
  Map<int, int> get toques => Map.unmodifiable(_toques);

  /// Regista que o dedo passou por estas casas.
  void tocar(Iterable<int> casas) {
    for (final c in casas) {
      _toques[c] = (_toques[c] ?? 0) + 1;
    }
  }

  void limpar() => _toques.clear();

  int quantoEm(int casa) => _toques[casa] ?? 0;

  /// Quanto é que este conjunto de casas foi mexido, ao todo.
  int somaEm(Iterable<int> casas) {
    var t = 0;
    for (final c in casas) {
      t += _toques[c] ?? 0;
    }
    return t;
  }

  bool intocado(Iterable<int> casas) => somaEm(casas) == 0;

  bool get vazio => _toques.isEmpty;

  /// Escolhe o conjunto menos mexido de uma lista de candidatos.
  ///
  /// Empate resolve-se pelo [desempate], que cada jogo dá à sua maneira — o
  /// maior número ganha. Sem um desempate fixo, dois telemóveis com o mesmo
  /// tabuleiro davam ajudas diferentes, e uma ajuda que não é sempre a mesma
  /// parece arbitrária a quem a recebe.
  T? menosTocado<T>(
    Iterable<T> candidatos,
    Iterable<int> Function(T) casasDe, {
    int Function(T)? desempate,
  }) {
    T? melhor;
    var menosToques = 0;
    var melhorDesempate = 0;

    for (final c in candidatos) {
      final t = somaEm(casasDe(c));
      final d = desempate?.call(c) ?? 0;
      if (melhor == null ||
          t < menosToques ||
          (t == menosToques && d > melhorDesempate)) {
        melhor = c;
        menosToques = t;
        melhorDesempate = d;
      }
    }
    return melhor;
  }
}
