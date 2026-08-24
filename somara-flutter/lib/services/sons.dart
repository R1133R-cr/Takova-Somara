import 'dart:async';

import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/foundation.dart';

/// O som da app.
///
/// Não é enfeite: para uma criança de seis anos o som é metade da razão
/// para voltar. Uma app muda parece avariada.
///
/// Os ficheiros são sintetizados em `tools/sons.py` — licença nossa, uns
/// kilobytes cada. O de erro é grave e macio de propósito: uma criança que
/// erra já se sente mal, e um som estridente ensina-lhe a ter medo de
/// tentar.
///
/// ## Porque é que isto é escrito assim
///
/// A primeira versão tinha três sinalizadores — ligado, pedido, pausado
/// pelo ciclo de vida — e a música tocava só quando os três estavam de
/// acordo. Bastava um ficar presa para o resultado ser silêncio absoluto,
/// sem erro nenhum no log e sem nada no ecrã a dizê-lo. Foi o que
/// aconteceu.
///
/// Agora há um só estado desejado ([_deveTocar]) e uma operação idempotente
/// que o vai impor ([garantirFundo]). Chamar duas vezes não faz mal, e
/// qualquer sítio da app pode chamá-la sem saber o que aconteceu antes.
class Sons {
  Sons._();
  static final Sons i = Sons._();

  /// Um leitor por efeito. Com um só, tocar o "certo" cortava o "toque" a
  /// meio — e numa lição esses dois acontecem quase ao mesmo tempo.
  final _efeitos = <String, AudioPlayer>{};
  final _fundo = AudioPlayer();

  bool _ligado = true;

  /// A app quer música (está aberta, em primeiro plano, com som ligado).
  bool _deveTocar = false;

  /// O que já se mandou tocar, para não mandar duas vezes.
  bool _aTocar = false;

  bool get ligado => _ligado;

  /// Presente sem ser intrusiva. Mais baixo do que isto perde-se debaixo do
  /// barulho de uma sala de aula, que é onde a app vai ser usada.
  static const _volumeFundo = 0.34;
  static const _volumeEfeito = 1.0;

  Future<void> definirLigado(bool valor) async {
    _ligado = valor;
    if (!valor) {
      for (final p in _efeitos.values) {
        await p.stop();
      }
    }
    await garantirFundo();
  }

  /// Liga ou desliga a música consoante o estado desejado.
  ///
  /// Idempotente e sem excepções para fora: é chamada do arranque, da troca
  /// do interruptor, e de cada vez que a app volta ao primeiro plano.
  Future<void> garantirFundo() async {
    final devia = _deveTocar && _ligado;
    if (devia == _aTocar) return;
    try {
      if (devia) {
        await _fundo.setReleaseMode(ReleaseMode.loop);
        await _fundo.setVolume(_volumeFundo);
        await _fundo.play(AssetSource('som/fundo.wav'));
      } else {
        await _fundo.stop();
      }
      _aTocar = devia;
    } catch (e) {
      // Fica por tocar e tenta na próxima. Nunca rebenta uma lição por isto.
      debugPrint('trilha de fundo: $e');
    }
  }

  /// A app está à vista e a música deve andar.
  Future<void> emPrimeiroPlano() async {
    _deveTocar = true;
    await garantirFundo();
  }

  /// A app saiu de vista.
  ///
  /// Cala tudo — num telemóvel partilhado com a família, música a sair de
  /// uma app fechada é o tipo de coisa que faz um pai desinstalá-la.
  Future<void> emSegundoPlano() async {
    _deveTocar = false;
    await garantirFundo();
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

  Future<void> toque() => _tocar('toque.wav');
  Future<void> certo() => _tocar('certo.wav');
  Future<void> errado() => _tocar('errado.wav');
  Future<void> nivel() => _tocar('nivel.wav');
  Future<void> salto() => _tocar('salto.wav');
}
