"""Torna cada enunciado unico dentro da sua classe.

Porque e que isto e preciso
---------------------------
As perguntas erradas sao guardadas pelo texto do enunciado (ver `erradas`
em app_state.dart). Enunciados genericos como "Qual e o maior?" apareciam
em varios niveis: a lista de Guardados mostrava a mesma linha duas vezes,
o contador dizia 7 quando so havia 6 erros, e acertar numa marcava as
outras como aprendidas.

Ha um segundo problema, pior: o audio le o enunciado em voz alta para as
criancas que ainda nao leem. "Qual e o maior?" dito em voz alta, com tres
botoes que a crianca nao consegue ler, nao ensina nada. Nomear as opcoes
no enunciado resolve as duas coisas de uma vez.

O que faz
---------
1. Reescreve os enunciados repetidos (tabela `TROCAS` abaixo).
2. Recalcula o nome do ficheiro de audio -- SHA-1 do texto, 12 hex.
3. Grava os audios novos com a mesma voz do resto do corpus.
4. Apaga os audios que deixaram de ser referenciados.

Correr a partir de somara-flutter/:
    python tools/desambiguar_enunciados.py
"""

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CONTENT = RAIZ / "assets" / "content.json"
AUDIO = RAIZ / "assets" / "audio"
CONTENT_WEB = RAIZ.parent / "somara-app" / "assets" / "js" / "content.js"

# A voz do resto do corpus. Confirmada byte a byte contra os ficheiros ja
# gravados: com -5% o mp3 sai exactamente do mesmo tamanho.
VOZ = "pt-PT-RaquelNeural"
TOM = "+25Hz"
RITMO = "-5%"

# texto antigo -> [(opcoes que identificam a pergunta, texto novo)]
# As opcoes distinguem as varias perguntas que partilhavam o mesmo texto.
TROCAS = {
    "Qual é o maior?": [
        (["6", "8", "10"], "Qual é o maior: 6, 8 ou 10?"),
        (["11", "18", "14"], "Qual é o maior: 11, 18 ou 14?"),
        (["99 999", "100 000", "90 999"],
         "Qual é o maior: 99 999, 100 000 ou 90 999?"),
    ],
    "Qual está bem escrito?": [
        (["excepção", "excessão", "esceção"],
         "Qual está bem escrito: excepção, excessão ou esceção?"),
        (["houve", "ouve (do verbo haver)", "ove"],
         "Do verbo haver, qual está bem escrito: houve, ouve ou ove?"),
        (["porquê (no fim da frase)", "por que (no fim da frase)", "porque?"],
         "No fim da frase, qual está bem escrito: porquê, por que ou porque?"),
    ],
    # Esta e uma pergunta de escrita, nao de escolha: pedir para escrever o
    # ano diz a crianca o que se espera dela e separa-a da irma de escolha
    # multipla, que fica como estava.
    "Em que ano foi criada a SADC?": [
        (None, "Escreve o ano em que foi criada a SADC."),
    ],
}

# Emoji e simbolos sao retirados antes de ler em voz alta: "45 __ 54"
# le-se como pausa, nao como "underscore underscore".
_LIXO = re.compile(
    "[\U0001F000-\U0001FAFF☀-➿️‍]|_{2,}", flags=re.UNICODE
)


def nome_do_audio(texto: str) -> str:
    return hashlib.sha1(texto.encode("utf-8")).hexdigest()[:12]


def texto_para_ler(texto: str) -> str:
    return re.sub(r"\s+", " ", _LIXO.sub(" ", texto)).strip()


def gravar(texto: str, destino: Path) -> bool:
    r = subprocess.run(
        ["edge-tts", "--voice", VOZ, f"--pitch={TOM}", f"--rate={RITMO}",
         "--text", texto_para_ler(texto), "--write-media", str(destino)],
        capture_output=True,
    )
    return r.returncode == 0 and destino.exists() and destino.stat().st_size > 0


def main() -> int:
    dados = json.loads(CONTENT.read_text(encoding="utf-8"))

    trocados = []   # (texto_antigo, texto_novo, ficheiro_novo)
    for curso in dados["cursos"]:
        for unidade in curso["units"]:
            for nivel in unidade["niveis"]:
                for q in nivel["questoes"]:
                    regras = TROCAS.get(q["q"])
                    if not regras:
                        continue
                    for opcoes, novo in regras:
                        casa = (
                            (opcoes is None and q.get("t") == "input")
                            or (opcoes is not None and q.get("options") == opcoes)
                        )
                        if not casa:
                            continue
                        antigo = q["q"]
                        q["q"] = novo
                        q["audio"] = nome_do_audio(novo) + ".mp3"
                        trocados.append((antigo, novo, q["audio"]))
                        break

    if not trocados:
        print("nada a trocar — o conteudo ja esta desambiguado")
        return 0

    print(f"-- {len(trocados)} enunciados a trocar")
    for antigo, novo, _ in trocados:
        print(f"   {antigo}\n   -> {novo}")

    print("-- a gravar audio")
    for _, novo, ficheiro in trocados:
        destino = AUDIO / ficheiro
        if destino.exists():
            print(f"   ja existia  {ficheiro}")
            continue
        if gravar(novo, destino):
            print(f"   {destino.stat().st_size:>6} bytes  {ficheiro}")
        else:
            print(f"   FALHOU  {ficheiro}  ({novo})", file=sys.stderr)
            return 1

    # indent=1 e a formatacao que o ficheiro ja tem: com outro valor o diff
    # passava de seis linhas para dez mil.
    CONTENT.write_text(
        json.dumps(dados, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    print(f"-- {CONTENT.name} gravado")

    # A versao web partilha os mesmos enunciados; sem isto ficavam a divergir.
    if CONTENT_WEB.exists():
        web = CONTENT_WEB.read_text(encoding="utf-8")
        antes = web
        for antigo, novo, _ in trocados:
            # So troca onde o texto aparece como valor de `q`, para nao
            # apanhar a palavra solta noutro sitio qualquer do ficheiro.
            web = web.replace(f'q: "{antigo}"', f'q: "{novo}"', 1)
            web = web.replace(f"q: '{antigo}'", f"q: '{novo}'", 1)
        if web != antes:
            CONTENT_WEB.write_text(web, encoding="utf-8")
            print(f"-- {CONTENT_WEB.name} actualizado")

    # Audios que deixaram de ser referenciados por alguem.
    usados = {
        q["audio"]
        for curso in dados["cursos"]
        for unidade in curso["units"]
        for nivel in unidade["niveis"]
        for q in nivel["questoes"]
        if q.get("audio")
    }
    orfaos = [f for f in AUDIO.glob("*.mp3") if f.name not in usados]
    for f in orfaos:
        f.unlink()
        print(f"-- apagado (ja ninguem o usa)  {f.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
