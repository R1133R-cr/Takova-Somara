"""Como se faz o audio da Somara. Um sitio so, e este.

Porque e que isto existe
------------------------
Ate aqui, cada ferramenta que produzia audio tinha a sua copia da voz, do
`limpar` e do calculo do nome -- e **so uma delas conhecia as regras de
pronuncia**. O `materia.py` gravava o texto cru, sem sequer importar o
`pronuncia`. O resultado foi audio a dizer "dois dois tres" onde estava
escrito "2² × 2³", em sessenta ficheiros, durante versoes inteiras.

A pronuncia estava aplicada por uma ferramenta de REPARACAO
(`regravar_siglas.py`) e nao pela de GERACAO. Por isso o audio voltava
sempre a derivar: cada conteudo novo nascia errado e so era consertado se
alguem se lembrasse de correr o reparador.

A regra que este modulo impoe
-----------------------------
`gravar()` recebe o texto do ECRA e aplica as regras ele proprio. Nao ha
maneira de um chamador passar por cima delas -- nem por esquecimento, que
foi como aconteceu das duas vezes. Quem quiser gravar audio nesta app
passa por aqui.

Os dois nomes que nao se podem trocar
-------------------------------------
    nome do FICHEIRO  = SHA-1 do texto do ECRA      (nunca muda)
    entrada no MANIFESTO = SHA-1 do texto DITO      (muda com as regras)

E dessa diferenca que nasce o problema todo: mudar uma regra de pronuncia
muda o que se deve dizer, mas nao muda o nome do ficheiro. O ficheiro fica
com o nome certo e o som errado, e nao ha maneira de dar por isso a olhar
para o disco. O manifesto e o que torna isso visivel.
"""

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pronuncia import para_dizer  # noqa: E402

# A consola do Windows e cp1252 e nao sabe escrever o sinal de menos nem o
# de multiplicar. Sem isto o programa rebenta a MOSTRAR o que ia fazer, e
# rebenta a meio -- foi assim que sessenta ficheiros ficaram por gravar.
for _fluxo in (sys.stdout, sys.stderr):
    try:
        _fluxo.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:  # pragma: no cover
        pass

RAIZ = Path(__file__).resolve().parent.parent
CONTENT = RAIZ / "assets" / "content.json"
AUDIO = RAIZ / "assets" / "audio"
MANIFESTO = Path(__file__).resolve().parent / "audio_dito.json"

# A mesma voz do resto do corpus. Mudar qualquer um destes tres faz a app
# inteira soar a outra pessoa, e obriga a regravar os 1023 ficheiros.
VOZ = "pt-PT-RaquelNeural"
TOM = "+25Hz"
RITMO = "-5%"

# Emoji e as linhas de preencher. Os emoji sao para os olhos e nao teem
# leitura util; os underscores o motor de voz ignora-os de qualquer forma.
_LIXO = re.compile("[\U0001F000-\U0001FAFF☀-➿️‍]|_{2,}", flags=re.UNICODE)


def limpar(texto: str) -> str:
    """Tira o que nao se le em voz alta."""
    return re.sub(r"\s+", " ", _LIXO.sub(" ", texto)).strip()


def dito(ecra: str) -> str:
    """O que a Raquel diz, a partir do que esta no ecra.

    A ordem conta: primeiro as regras de pronuncia, depois a limpeza. Ao
    contrario, os emoji podiam partir um numero ao meio antes de a regra
    das unidades o ver.
    """
    return limpar(para_dizer(ecra))


def sha(texto: str) -> str:
    return hashlib.sha1(texto.encode("utf-8")).hexdigest()[:12]


def nome_do_ficheiro(ecra: str) -> str:
    """O nome do mp3: SHA-1 do texto do ECRA.

    E o texto do ecra e nao o dito, de proposito: assim o ficheiro nao muda
    de nome quando uma regra de pronuncia muda, e o content.json nao tem de
    ser reescrito de cada vez.
    """
    return sha(ecra) + ".mp3"


def ler_manifesto() -> dict:
    if not MANIFESTO.exists():
        return {}
    return json.loads(MANIFESTO.read_text(encoding="utf-8"))


def escrever_manifesto(m: dict) -> None:
    MANIFESTO.write_text(
        json.dumps(dict(sorted(m.items())), ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )


def gravar(ecra: str, ficheiro: str, manifesto: dict | None = None) -> bool:
    """Grava o audio de um texto de ecra, ja com as regras aplicadas.

    Devolve False se a gravacao falhou. O chamador nao escolhe o que se diz
    -- passa o que esta no ecra e este modulo trata do resto.
    """
    destino = AUDIO / ficheiro
    destino.parent.mkdir(parents=True, exist_ok=True)
    fala = dito(ecra)
    destino.unlink(missing_ok=True)
    r = subprocess.run(
        ["edge-tts", "--voice", VOZ, f"--pitch={TOM}", f"--rate={RITMO}",
         "--text", fala, "--write-media", str(destino)],
        capture_output=True,
    )
    ok = (r.returncode == 0 and destino.exists()
          and destino.stat().st_size > 1024)
    if ok and manifesto is not None:
        manifesto[ficheiro] = sha(fala)
    return ok


def falas_do_curriculo(dados: dict) -> dict:
    """ficheiro -> texto do ecra, para tudo o que tem audio.

    Um sitio so a decidir o que conta como "audio do curriculo": as
    perguntas e a materia. Antes estava copiado em duas ferramentas e uma
    delas esquecia-se da materia.
    """
    falas = {}
    for curso in dados["cursos"]:
        for u in curso["units"]:
            for n in u["niveis"]:
                m = n.get("materia")
                if m and m.get("audio"):
                    falas[m["audio"]] = f"{m['explica']} {m['exemplo']}"
                for q in n["questoes"]:
                    if q.get("audio"):
                        falas[q["audio"]] = q["q"]
    return falas


def carregar_content() -> dict:
    return json.loads(CONTENT.read_text(encoding="utf-8"))


def gravar_content(dados: dict) -> None:
    # indent=1 e a formatacao que o ficheiro ja tem; mudar isso poria o
    # diff inteiro a mexer e escondia a alteracao verdadeira.
    CONTENT.write_text(
        json.dumps(dados, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
