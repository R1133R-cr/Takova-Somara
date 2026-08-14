import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/foundation.dart';

/// O som da app.
///
/// Na fase C a app estava muda: nenhum toque respondia, acertar não soava a
/// nada e por trás havia silêncio. Faltava-lhe a metade que se ouve.
///
/// Os ficheiros são sintetizados em `tools/sons.py` — licença nossa, uns
/// kilobytes cada, e afináveis numa linha. O de erro é grave e macio de
/// propósito: uma criança que erra já se sente mal, e um som estridente
/// ensina-lhe a ter medo de tentar.
class Sons {
  Sons._();
  static final Sons i = Sons._();

  /// Um leitor por efeito. Com um só, tocar o "certo" cortava o "toque" a
  /// meio — e numa lição esses dois acontecem quase ao mesmo tempo.
  final _efeitos = <String, AudioPlayer>{};
  final _fundo = AudioPlayer();

  bool _ligado = true;
  bool _fundoAPedido = false;

  bool get ligado => _ligado;

  /// Baixo de propósito. A trilha é para não haver um buraco de silêncio,
  /// não para se dar por ela — se a criança a trautear, está alta demais.
  static const _volumeFundo = 0.22;
  static const _volumeEfeito = 0.9;

  Future<void> definirLigado(bool valor) async {
    if (_ligado == valor) return;
    _ligado = valor;
    if (valor) {
      if (_fundoAPedido) await _arrancarFundo();
    } else {
      await _fundo.stop();
      for (final p in _efeitos.values) {
        await p.stop();
      }
    }
  }

  Future<void> _tocar(String ficheiro) async {
    if (!_ligado) return;
    try {
      final p = _efeitos.putIfAbsent(
        ficheiro,
        () => AudioPlayer()..setPlayerMode(PlayerMode.lowLatency),
      );
      await p.stop();
      await p.setVolume(_volumeEfeito);
      await p.play(AssetSource('som/$ficheiro'));
    } catch (e) {
      // Um som que falha nunca pode parar uma lição.
      debugPrint('som $ficheiro: $e');
    }
  }

  Future<void> toque() => _tocar('toque.wav');
  Future<void> certo() => _tocar('certo.wav');
  Future<void> errado() => _tocar('errado.wav');
  Future<void> nivel() => _tocar('nivel.wav');
  Future<void> salto() => _tocar('salto.wav');

  Future<void> _arrancarFundo() async {
    try {
      await _fundo.setReleaseMode(ReleaseMode.loop);
      await _fundo.setVolume(_volumeFundo);
      await _fundo.play(AssetSource('som/fundo.wav'));
    } catch (e) {
      debugPrint('trilha de fundo: $e');
    }
  }

  /// Liga a trilha. Guarda que foi pedida, para voltar sozinha quando se
  /// reactivar o som ou quando a app regressar ao primeiro plano.
  Future<void> comecarFundo() async {
    _fundoAPedido = true;
    if (_ligado) await _arrancarFundo();
  }

  /// Cala tudo enquanto a app está em segundo plano.
  ///
  /// Sem isto, a música continuava a tocar depois de a criança sair da app —
  /// e num telemóvel partilhado com a família isso é um problema a sério,
  /// não um pormenor.
  Future<void> pausarPorSegundoPlano() async {
    try {
      await _fundo.pause();
    } catch (_) {}
  }

  Future<void> retomarDoSegundoPlano() async {
    if (!_ligado || !_fundoAPedido) return;
    try {
      await _fundo.resume();
    } catch (_) {}
  }
}
