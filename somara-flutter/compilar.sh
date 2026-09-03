#!/bin/bash
# Compila a Somara e guarda uma cópia numerada em APKs/.
#
# Usa `flutter build` e não `gradlew` de propósito: só o comando do Flutter
# reescreve o android/local.properties a partir do pubspec.yaml, e é dali
# que o Gradle tira a versão. Com o atalho do gradlew o APK sai sempre com
# a versão antiga — o que mais tarde faz a Play Store recusar a entrega,
# porque exige um versionCode maior que o anterior.
#
#   ./compilar.sh              APK de depuração (rápido, pesado, para testar)
#   ./compilar.sh release      APK de entrega, um ficheiro para todos os
#                              telemóveis — é o que se manda por WhatsApp
#   ./compilar.sh release abi  um APK por arquitectura, cada um ~1/3 do
#                              tamanho
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
SPLIT="${2:-}"
[[ "$MODO" == "debug" || "$MODO" == "release" ]] || { echo "modo inválido: $MODO"; exit 1; }
[[ -z "$SPLIT" || "$SPLIT" == "abi" ]] || { echo "segundo argumento: 'abi' ou nada"; exit 1; }

export JAVA_HOME="/c/Users/R1133R/AppData/Local/Android/jdk"
export ANDROID_SDK_ROOT="/c/Users/R1133R/AppData/Local/Android/Sdk"
export ANDROID_HOME="$ANDROID_SDK_ROOT"
export PATH="/c/Users/R1133R/AppData/Local/flutter/bin:$JAVA_HOME/bin:$PATH"

VERSAO=$(grep -E "^version:" pubspec.yaml | sed 's/version:[[:space:]]*//')
NOME="${VERSAO%%+*}"
CODIGO="${VERSAO##*+}"
ARQUIVO="../APKs"
ALVO="$ARQUIVO/somara-${NOME}+${CODIGO}-${MODO}.apk"

echo "── Somara ${NOME} (código ${CODIGO}) · ${MODO}"

# Recusar sobrepor uma versão já arquivada: a cópia antiga é justamente o
# que permite voltar atrás quando uma versão nova sai com defeito.
#
# Em modo ABI os ficheiros têm outro nome, e o guarda tem de olhar para
# esses — senão recusava-se a gerar a divisão de uma versão cujo APK
# único já existisse, que é precisamente o caso normal.
if [[ "$SPLIT" == "abi" ]]; then
  ALVO="$ARQUIVO/somara-${NOME}+${CODIGO}-arm64-v8a-${MODO}.apk"
fi

if [[ -e "$ALVO" ]]; then
  echo
  echo "ERRO: já existe $ALVO"
  echo "Sobe a versão no pubspec.yaml antes de compilar outra vez,"
  echo "ou apaga a cópia à mão se souberes o que estás a fazer."
  exit 1
fi

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

echo "── a compilar"
mkdir -p "$ARQUIVO"

if [[ "$SPLIT" == "abi" ]]; then
  flutter build apk --"$MODO" --split-per-abi >/dev/null
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
else
  flutter build apk --"$MODO" >/dev/null
  ORIGEM="build/app/outputs/flutter-apk/app-${MODO}.apk"
  cp "$ORIGEM" "$ALVO"
  TAM=$(du -m "$ALVO" | cut -f1)
  echo
  echo "  APK:     $(cd "$ARQUIVO" && pwd)/$(basename "$ALVO")"
  echo "  tamanho: ${TAM} MB"
fi
echo
echo "  cópias guardadas:"
ls -1t "$ARQUIVO"/*.apk 2>/dev/null | head -6 | sed 's|.*/|    |'
