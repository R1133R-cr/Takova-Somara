# Somara

App didáctica da Takova para o ensino primário moçambicano — 1ª à 6ª classe,
Matemática, Português, Ciências Naturais e Ciências Sociais, tirado dos
manuais oficiais.

A app funciona **inteira sem internet**. Isso não é um modo de emergência:
é o modo normal de quem a usa em Lichinga. Tudo o que precisa de rede —
conteúdo novo, contas, cópia do progresso — é opcional e degrada em
silêncio quando não há.

## Compilar

```bash
./compilar.sh release      # ou: ./compilar.sh debug
```

Corre a análise e os testes antes de compilar, e recusa-se a gerar um APK
com uma versão que já exista. O ficheiro fica em `../APKs/`, com as
versões anteriores ao lado.

**Não usar `./gradlew` directamente.** O Gradle lê a versão de
`android/local.properties`, que só o `flutter build` regenera a partir do
`pubspec.yaml` — pelo atalho saem APKs todos marcados como 1.0.0.

## Testes

```bash
flutter test
```

Os que interessam guardam coisas que não dão erro quando partem: a
sequência de dias ao longo de meses de calendário, a fusão do progresso
com o da nuvem, a escada de espera das vidas, e se cada nível tem matéria
e áudio em disco.

## Progresso na nuvem (opcional)

Serve uma coisa só: uma criança que muda de telemóvel — ou a quem
reinstalam a app — perdia meses de trabalho.

Enquanto não estiver configurado, **nada disto aparece na app** e tudo
funciona como sempre. A promessa "o teu progresso fica guardado" é a que
não se pode falhar, por isso não se faz até ser verdade.

Para activar, ver as instruções passo a passo no topo de
[`lib/services/firebase_config.dart`](lib/services/firebase_config.dart).
São cinco minutos na consola do Firebase e um ficheiro a editar. As regras
de segurança a colar estão em [`firestore.rules`](firestore.rules) — sem
esse passo, os dados de crianças ficam abertos a toda a gente durante 30
dias e depois a app pára.

A medição (quantos abriram, quantos terminaram uma lição, quantos
voltaram) são três contadores no documento do próprio aluno. Não há SDK
de analítica de propósito: pesaria mais no APK e recolheria
identificadores de publicidade e sinais do aparelho sobre crianças do
primário, para responder a três perguntas que três inteiros respondem.

## Ferramentas (`tools/`)

Scripts em Python que geram o que vai dentro da app. Correr a partir
desta pasta.

| Script | O que faz |
|---|---|
| `materia.py --gravar` | Mete a matéria de cada nível no `content.json` e grava a aula em voz alta. |
| `sons.py` | Sintetiza os sons da interface e a trilha de fundo. Sem dependências. |
| `desambiguar_enunciados.py` | Torna cada enunciado único dentro da classe e regrava o áudio afectado. |

A voz é sempre a mesma — `pt-PT-RaquelNeural`, tom `+25Hz`, ritmo `-5%`.
Mudar isto faz a app soar a duas pessoas diferentes.

## Notas de manutenção

- O nome do ficheiro de áudio é o SHA-1 do próprio texto, 12 hex. Mudar
  um enunciado obriga a regravar — os scripts tratam disso e apagam o que
  ficou órfão.
- Não editar `pubspec.yaml` com `Get-Content`/`Set-Content` do PowerShell
  sem `-Encoding utf8`: lê em ANSI e grava em UTF-8, e estraga os acentos.
  Já aconteceu e ficou commitado.
- O `git push` não funciona a partir do ambiente do agente; é feito pelo
  GitHub Desktop, e as etiquetas têm de ir à parte.
