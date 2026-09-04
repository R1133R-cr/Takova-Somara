import 'package:flutter/widgets.dart';

import '../state/app_state.dart';
import 'sons.dart';

/// O que acontece quando a app sai da frente e quando volta.
///
/// Está numa classe própria e não dentro do `State` do arranque por uma
/// razão prática: assim pode ser construída num teste e recebe os estados
/// do ciclo de vida à mão. Enterrada num `State` privado, esta ligação não
/// tinha teste nenhum — apagavam-se-lhe duas linhas e a suite continuava
/// verde enquanto o relógio dos jogos corria com a app fechada.
class CicloDeVida extends WidgetsBindingObserver {
  final AppState estado;
  CicloDeVida(this.estado);

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    switch (state) {
      case AppLifecycleState.resumed:
        Sons.i.emPrimeiroPlano();
        estado.retomarTempoDeJogo();

      // `inactive` é transitório e a app continua à vista: a sombra do
      // multitarefas, a barra de notificações a descer meio dedo, um
      // aviso de chamada. Calar a música aqui foi o que a matou — ficava
      // em pausa e o `resumed` que a devolvia nem sempre chegava. Pelo
      // mesmo motivo o relógio também não pára: quem está a jogar com a
      // barra de notificações meio aberta ainda está a jogar.
      case AppLifecycleState.inactive:
        break;

      case AppLifecycleState.paused:
      case AppLifecycleState.hidden:
      case AppLifecycleState.detached:
        Sons.i.emSegundoPlano();
        // O tempo de jogo pára com a app. Quem atende uma chamada a meio do
        // Pomar não paga por essa chamada — e um telemóvel esquecido em cima
        // da mesa não gasta a bolsa da tarde toda.
        estado.pausarTempoDeJogo();
    }
  }
}
