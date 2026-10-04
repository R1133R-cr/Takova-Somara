#!/bin/bash
# Compila a Somara e guarda uma cópia numerada em APKs/.
#
# Usa `flutter build` e não `gradlew` de propósito: só o comando do Flutter
# reescreve o android/local.properties a partir do pubspec.yaml, e é dali
# que o Gradle tira a versão. Com o atalho do gradlew o APK sai sempre com
# a versão antiga — o que mais tarde faz a Play Store recusar a entrega,
# porque exige um versionCode maior que o anterior.
#
#   ./compilar.sh                 APK de depuração (rápido, pesado, para testar)
#   ./compilar.sh release         APK de entrega, um ficheiro para todos os
#                                 telemóveis — é o que se manda por WhatsApp
#   ./compilar.sh release abi     um APK por arquitectura, cada um ~1/3 do
#                                 tamanho
#   ./compilar.sh release teste   só a versão de testes (tudo desbloqueado)
#   ./compilar.sh release ambas   a normal e a de testes, de uma vez
#
# ## As duas versões
#
# A **normal** é a app como a criança a recebe: os níveis abrem-se por
# ordem. A **de testes** não tem fila — qualquer nível em qualquer ordem,
# qualquer nível de qualquer joguinho, bolsa de tempo sem limite — e traz um
# painel vermelho com interruptores. Ver `lib/modo_teste.dart`.
#
# Ela precisa de três coisas ao mesmo tempo, e é por isso que se compila por
# aqui e não à mão:
#
#   --dart-define=SOMARA_TESTE=true   abre a app a si mesma
#   --dart-define=SOMARA_DATA=<hoje>  marca o dia; caduca 60 dias depois
#   -Pteste=true                      sufixo .teste e nome «Somara TESTE»
#
# Faltando o primeiro sai uma app normal com nome de testes; faltando o
# terceiro, instalá-la apaga a normal do telemóvel; faltando o segundo, nunca
# caduca. Nenhum dos três se pode esquecer, logo nenhum se escreve à mão.
#
# O corte por arquitectura conta: um APK único leva o código do motor do
# Flutter compilado para ARM de 32 bits, ARM de 64 e x86_64, e cada
# telemóvel só usa um deles. Quem paga os dados ao megabyte descarrega
# três vezes o que precisa. Para a Play Store isto nem se põe — envia-se
# um AAB e a loja trata do assunto; isto é para a entrega à mão, que é
# como a app chega às escolas.

set -euo pipefail
cd "$(dirname "$0")"

MODO="${1:-debug}"
VARIANTE="${2:-}"
[[ "$MODO" == "debug" || "$MODO" == "release" ]] || { echo "modo inválido: $MODO"; exit 1; }
case "$VARIANTE" in
  ""|abi|teste|ambas) ;;
  *) echo "segundo argumento: 'abi', 'teste', 'ambas' ou nada"; exit 1 ;;
esac

export JAVA_HOME="/c/Users/R1133R/AppData/Local/Android/jdk"
export ANDROID_SDK_ROOT="/c/Users/R1133R/AppData/Local/Android/Sdk"
export ANDROID_HOME="$ANDROID_SDK_ROOT"
export PATH="/c/Users/R1133R/AppData/Local/flutter/bin:$JAVA_HOME/bin:$PATH"

VERSAO=$(grep -E "^version:" pubspec.yaml | sed 's/version:[[:space:]]*//')
NOME="${VERSAO%%+*}"
CODIGO="${VERSAO##*+}"
ARQUIVO="../APKs"
HOJE=$(date +%F)

# A versão vai dentro do APK para o painel de testes a poder mostrar. Vem
# por aqui e não de um pacote novo — ver `lib/modo_teste.dart`.
COMUNS=(--dart-define=SOMARA_VERSAO="${NOME}+${CODIGO}")

ALVO_NORMAL="$ARQUIVO/somara-${NOME}+${CODIGO}-${MODO}.apk"
ALVO_ABI="$ARQUIVO/somara-${NOME}+${CODIGO}-arm64-v8a-${MODO}.apk"
if [[ "$MODO" == "release" ]]; then
  ALVO_TESTE="$ARQUIVO/somara-${NOME}+${CODIGO}-teste.apk"
else
  ALVO_TESTE="$ARQUIVO/somara-${NOME}+${CODIGO}-teste-debug.apk"
fi

# O que esta corrida vai produzir.
A_FAZER=()
case "$VARIANTE" in
  "")      A_FAZER=(normal) ;;
  abi)     A_FAZER=(abi) ;;
  teste)   A_FAZER=(teste) ;;
  ambas)   A_FAZER=(normal teste) ;;
esac

echo "── Somara ${NOME} (código ${CODIGO}) · ${MODO} · ${A_FAZER[*]}"

# Recusar sobrepor uma versão já arquivada: a cópia antiga é justamente o
# que permite voltar atrás quando uma versão nova sai com defeito.
#
# Confere-se antes de compilar e para todos os ficheiros desta corrida. Com
# `ambas`, descobrir à segunda que o ficheiro já existe significava ter
# esperado seis minutos pela primeira para nada.
for QUAL in "${A_FAZER[@]}"; do
  case "$QUAL" in
    normal) ALVO="$ALVO_NORMAL" ;;
    abi)    ALVO="$ALVO_ABI" ;;
    teste)  ALVO="$ALVO_TESTE" ;;
  esac
  if [[ -e "$ALVO" ]]; then
    echo
    echo "ERRO: já existe $ALVO"
    echo "Sobe a versão no pubspec.yaml antes de compilar outra vez,"
    echo "ou apaga a cópia à mão se souberes o que estás a fazer."
    exit 1
  fi
done

# O áudio diz o que as regras de pronúncia mandam dizer?
#
# O nome de cada mp3 é o SHA-1 do texto do ECRÃ, e não muda quando uma
# regra de pronúncia muda. O ficheiro fica com o nome certo e o som
# errado, e não há maneira de dar por isso a olhar para o disco.
#
# Já aconteceu duas vezes. Da segunda ficaram sessenta ficheiros de
# Matemática da 3ª à 6ª classe a ler "dois dois três" onde está escrito
# "2² × 2³", e a versão saiu na mesma. Agora não sai.
if command -v python >/dev/null 2>&1; then
  echo "── a conferir o áudio"
  if ! python tools/regravar_siglas.py --conferir; then
    echo
    echo "ERRO: há áudio que não diz o que devia dizer (ver acima)."
    echo "Regrava-o antes de compilar."
    exit 1
  fi
else
  echo "AVISO: sem python — o áudio não foi conferido" >&2
fi

echo "── análise e testes"
flutter analyze >/dev/null
flutter test >/dev/null
echo "   sem problemas"

mkdir -p "$ARQUIVO"

# Guarda o APK que o Flutter acabou de deixar em build/ e diz o tamanho.
# Tem de ser logo depois de cada compilação: as duas versões saem do mesmo
# caminho em build/, e a segunda escreve por cima da primeira.
guardar() {
  local destino="$1"
  local origem="build/app/outputs/flutter-apk/app-${MODO}.apk"
  cp "$origem" "$destino"
  echo "  $(du -m "$destino" | cut -f1) MB   $(basename "$destino")"
}

for QUAL in "${A_FAZER[@]}"; do
  case "$QUAL" in
    normal)
      echo "── a compilar a normal"
      flutter build apk --"$MODO" "${COMUNS[@]}" >/dev/null
      echo
      guardar "$ALVO_NORMAL"
      ;;

    teste)
      echo "── a compilar a de testes (caduca em $(date -d "+60 days" +%F 2>/dev/null || echo '60 dias'))"
      flutter build apk --"$MODO" \
        "${COMUNS[@]}" \
        --dart-define=SOMARA_TESTE=true \
        --dart-define=SOMARA_DATA="$HOJE" \
        -Pteste=true >/dev/null
      echo
      guardar "$ALVO_TESTE"
      echo "  instala-se ao lado da normal (mz.co.takova.somara.teste)"
      ;;

    abi)
      echo "── a compilar por arquitectura"
      flutter build apk --"$MODO" "${COMUNS[@]}" --split-per-abi >/dev/null
      echo
      for ABI in armeabi-v7a arm64-v8a x86_64; do
        ORIGEM="build/app/outputs/flutter-apk/app-${ABI}-${MODO}.apk"
        [[ -e "$ORIGEM" ]] || continue
        DESTINO="$ARQUIVO/somara-${NOME}+${CODIGO}-${ABI}-${MODO}.apk"
        cp "$ORIGEM" "$DESTINO"
        echo "  $(du -m "$DESTINO" | cut -f1) MB   $(basename "$DESTINO")"
      done
      echo
      echo "  arm64-v8a serve a esmagadora maioria dos telemóveis desde 2016."
      echo "  armeabi-v7a é para os mais antigos; x86_64 só para emuladores."
      ;;
  esac
done

echo
echo "  pasta:   $(cd "$ARQUIVO" && pwd)"
echo "  cópias guardadas:"
ls -1t "$ARQUIVO"/*.apk 2>/dev/null | head -6 | sed 's|.*/|    |'
