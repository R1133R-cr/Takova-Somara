import 'dart:async';

import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/foundation.dart';

/// Qual das trilhas deve estar a tocar.
enum Trilha {
  /// A app em geral: mapa, separadores, perfil, ranking.
  principal('som/principal.mp3'),

  /// A sala dos joguinhos. Outro ambiente de propósito — entrar ali é sair
  /// da escola, e a música é a primeira coisa que diz isso.
  relaxar('som/relaxar.mp3');

  final String ficheiro;
  const Trilha(this.ficheiro);
}

/// O som da app.
///
/// Não é enfeite: para uma criança de seis anos o som é metade da razão
/// para voltar. Uma app muda parece avariada.
///
/// ## As duas trilhas e o silêncio
///
/// A música de fundo acompanha a interface, mas **cala-se durante os
/// exercícios**. Uma pergunta de Matemática exige concentração, e música
/// por cima de quem está a contar nos dedos atrapalha em vez de animar. Os
/// joguinhos são o contrário: aí a música é parte do descanso.
///
/// ## Porque é que o silêncio é um contador e não um sim/não
///
/// A Matéria abre a Lição com `pushReplacement`: a Lição entra em cena
/// **antes** de a Matéria sair. Com um sinalizador simples, o `dispose` da
/// Matéria devolvia a música a meio da Lição. Com um contador, o +1 da
/// Lição e o -1 da Matéria deixam o saldo em 1 e o silêncio aguenta-se.
class Sons {
  Sons._();
  static final Sons i = Sons._();

  /// Um leitor por efeito. Com um só, tocar o "certo" cortava o "toque" a
  /// meio — e numa lição esses dois acontecem quase ao mesmo tempo.
  final _efeitos = <String, AudioPlayer>{};
  final _fundo = AudioPlayer();

  bool _ligado = true;

  /// A app está à vista.
  bool _emCena = false;

  /// A trilha que a parte da app onde se está pede.
  Trilha _ambiente = Trilha.principal;

  /// Quantos ecrãs abertos pedem silêncio. Ver a nota da classe.
  int _pedidosDeSilencio = 0;

  /// O que está mesmo a tocar, para não voltar a mandar o mesmo.
  Trilha? _aTocar;

  /// As mudanças de trilha em fila, uma de cada vez.
  ///
  /// Trocar de separador depressa disparava dois [_garantir] ao mesmo
  /// tempo, e os dois mexiam no mesmo leitor: um mandava parar enquanto o
  /// outro mandava tocar, e o resultado era silêncio permanente. Encadeadas,
  /// a segunda só começa quando a primeira acabar.
  Future<void> _fila = Future.value();

  bool get ligado => _ligado;

  /// Presente sem ser intrusiva. Mais baixo do que isto perde-se debaixo do
  /// barulho de uma sala de aula, que é onde a app vai ser usada.
  static const _volumeFundo = 0.34;
  static const _volumeEfeito = 1.0;

  /// A trilha que devia estar a tocar agora, ou nula para silêncio.
  Trilha? get _desejada {
    if (!_ligado || !_emCena || _pedidosDeSilencio > 0) return null;
    return _ambiente;
  }

  /// Põe a tocar o que se deve estar a ouvir.
  ///
  /// Idempotente e sem excepções para fora: chama-se do arranque, da troca
  /// de separador, ao entrar e sair de cada lição, e sempre que a app volta
  /// ao primeiro plano. Chamar duas vezes não faz mal.
  Future<void> _garantir() {
    _fila = _fila.then((_) => _aplicar());
    return _fila;
  }

  Future<void> _aplicar() async {
    final querida = _desejada;
    if (querida == _aTocar) return;
    try {
      // Parar sempre antes de tocar, mesmo para trocar de trilha. Mandar
      // tocar outra fonte num leitor que ainda está a tocar deixava-o num
      // estado em que não tocava mais nada — foi o que calou a app inteira
      // a partir da primeira troca de separador.
      await _fundo.stop();
      _aTocar = null;

      if (querida != null) {
        await _fundo.setReleaseMode(ReleaseMode.loop);
        await _fundo.setVolume(_volumeFundo);
        await _fundo.play(AssetSource(querida.ficheiro));
      }
      _aTocar = querida;
    } catch (e) {
      // Fica por tocar e tenta na próxima. Nunca rebenta uma lição por isto.
      debugPrint('trilha: $e');
    }
  }

  /// Prepara o áudio antes de qualquer som tocar.
  ///
  /// Sem isto, cada efeito calava a música: por omissão o audioplayers pede
  /// **foco exclusivo** de áudio a cada `play`, e o sistema pára tudo o
  /// resto para lho dar — incluindo a nossa própria trilha, que assim
  /// morria ao primeiro toque num separador e só voltava quando algo a
  /// reiniciava. Foi isto que deixou a app praticamente muda.
  ///
  /// Com `AndroidAudioFocus.none`, os nossos sons convivem uns com os
  /// outros. O efeito lateral é não interrompermos a música de outra app —
  /// e num telemóvel de família isso é melhor educação, não pior.
  Future<void> arrancar() async {
    try {
      await AudioPlayer.global.setAudioContext(
        AudioContext(
          android: AudioContextAndroid(
            isSpeakerphoneOn: false,
            stayAwake: false,
            contentType: AndroidContentType.music,
            usageType: AndroidUsageType.media,
            audioFocus: AndroidAudioFocus.none,
          ),
          iOS: AudioContextIOS(
            category: AVAudioSessionCategory.ambient,
            options: {AVAudioSessionOptions.mixWithOthers},
          ),
        ),
      );
    } catch (e) {
      debugPrint('contexto de áudio: $e');
    }
  }

  Future<void> definirLigado(bool valor) async {
    _ligado = valor;
    if (!valor) {
      for (final p in _efeitos.values) {
        await p.stop();
      }
    }
    await _garantir();
  }

  /// A app está à vista e a música deve andar.
  Future<void> emPrimeiroPlano() async {
    _emCena = true;
    await _garantir();
  }

  /// A app saiu de vista.
  ///
  /// Cala tudo — num telemóvel partilhado com a família, música a sair de
  /// uma app fechada é o tipo de coisa que faz um pai desinstalá-la.
  Future<void> emSegundoPlano() async {
    _emCena = false;
    await _garantir();
  }

  /// Qual das trilhas a parte da app onde se está quer ouvir.
  Future<void> definirAmbiente(Trilha t) async {
    if (_ambiente == t) return;
    _ambiente = t;
    await _garantir();
  }

  /// Um ecrã de exercício abriu: música fora até ele fechar.
  Future<void> pedirSilencio() async {
    _pedidosDeSilencio++;
    await _garantir();
  }

  Future<void> largarSilencio() async {
    if (_pedidosDeSilencio > 0) _pedidosDeSilencio--;
    await _garantir();
  }

  Future<void> _tocar(String ficheiro) async {
    if (!_ligado) return;
    try {
      final p = _efeitos.putIfAbsent(ficheiro, AudioPlayer.new);
      await p.stop();
      await p.setVolume(_volumeEfeito);
      await p.play(AssetSource('som/$ficheiro'));
    } catch (e) {
      debugPrint('som $ficheiro: $e');
    }
  }

  /// Uma voz de festejo dos joguinhos, pelo nome do ficheiro.
  ///
  /// Vem do modelo do jogo e não daqui: é lá que se decide o que o feito
  /// merece, e esta classe só sabe tocar.
  Future<void> voz(String ficheiro) => _tocar(ficheiro);

  Future<void> toque() => _tocar('toque.wav');
  Future<void> certo() => _tocar('certo.wav');
  Future<void> errado() => _tocar('errado.wav');
  Future<void> nivel() => _tocar('nivel.wav');
  Future<void> salto() => _tocar('salto.wav');
}
