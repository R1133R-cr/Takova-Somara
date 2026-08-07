#!/bin/bash
# Compila a Somara e guarda uma cópia numerada em APKs/.
#
# Usa `flutter build` e não `gradlew` de propósito: só o comando do Flutter
# reescreve o android/local.properties a partir do pubspec.yaml, e é dali
# que o Gradle tira a versão. Com o atalho do gradlew o APK sai sempre com
# a versão antiga — o que mais tarde faz a Play Store recusar a entrega,
# porque exige um versionCode maior que o anterior.
#
#   ./compilar.sh           APK de depuração (rápido, pesado, para testar)
#   ./compilar.sh release   APK de entrega (mais lento, ~4x mais leve)

set -euo pipefail
cd "$(dirname "$0")"

MODO="${1:-debug}"
[[ "$MODO" == "debug" || "$MODO" == "release" ]] || { echo "modo inválido: $MODO"; exit 1; }

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
if [[ -e "$ALVO" ]]; then
  echo
  echo "ERRO: já existe $ALVO"
  echo "Sobe a versão no pubspec.yaml antes de compilar outra vez,"
  echo "ou apaga a cópia à mão se souberes o que estás a fazer."
  exit 1
fi

echo "── análise e testes"
flutter analyze >/dev/null
flutter test >/dev/null
echo "   sem problemas"

echo "── a compilar"
flutter build apk --"$MODO" >/dev/null

ORIGEM="build/app/outputs/flutter-apk/app-${MODO}.apk"
mkdir -p "$ARQUIVO"
cp "$ORIGEM" "$ALVO"

TAM=$(du -m "$ALVO" | cut -f1)
echo
echo "  APK:     $(cd "$ARQUIVO" && pwd)/$(basename "$ALVO")"
echo "  tamanho: ${TAM} MB"
echo
echo "  cópias guardadas:"
ls -1t "$ARQUIVO"/*.apk 2>/dev/null | head -6 | sed 's|.*/|    |'
