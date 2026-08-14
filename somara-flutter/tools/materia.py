"""Mete a materia dentro do content.json e grava o audio de cada aula.

Porque e que isto existe
------------------------
Na fase C as criancas acharam as perguntas secas: chegavam ao exercicio sem
ninguem lhes ter relembrado a materia. Um enunciado da 4a classe sem
contexto e um teste, nao uma aula -- a app avaliava sem nunca ter ensinado.

Cada nivel passa a ter tres campos curtos: explica, exemplo e lembra. O
audio le a explicacao e o exemplo em voz alta, para as criancas da 1a e da
2a classe que ainda nao leem.

Correr a partir de somara-flutter/:
    python tools/materia.py            # so mostra o que falta
    python tools/materia.py --gravar   # escreve o content.json e o audio
"""

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from materia_texto import MATERIA

RAIZ = Path(__file__).resolve().parent.parent
CONTENT = RAIZ / "assets" / "content.json"
AUDIO = RAIZ / "assets" / "audio"

# A mesma voz do resto do corpus, confirmada byte a byte contra os ficheiros
# ja gravados. Mudar isto faria a aula soar a outra pessoa.
VOZ = "pt-PT-RaquelNeural"
TOM = "+25Hz"
RITMO = "-5%"

_LIXO = re.compile("[\U0001F000-\U0001FAFF☀-➿️‍]|_{2,}", flags=re.UNICODE)


def nome_do_audio(texto: str) -> str:
    return hashlib.sha1(texto.encode("utf-8")).hexdigest()[:12]


def para_ler(m: dict) -> str:
    """O que a Raquel le: a explicacao e o exemplo, sem o "lembra".

    O "lembra" fica de fora de proposito -- e uma nota para os olhos, e dita
    em voz alta logo a seguir ao exemplo soa a repeticao.
    """
    bruto = f"{m['explica']} {m['exemplo']}"
    return re.sub(r"\s+", " ", _LIXO.sub(" ", bruto)).strip()


def gravar_audio(texto: str, destino: Path) -> bool:
    r = subprocess.run(
        ["edge-tts", "--voice", VOZ, f"--pitch={TOM}", f"--rate={RITMO}",
         "--text", texto, "--write-media", str(destino)],
        capture_output=True,
    )
    return r.returncode == 0 and destino.exists() and destino.stat().st_size > 0


def main() -> int:
    gravar = "--gravar" in sys.argv
    dados = json.loads(CONTENT.read_text(encoding="utf-8"))

    chaves_no_curriculo = []
    for curso in dados["cursos"]:
        for u in curso["units"]:
            for n in u["niveis"]:
                chaves_no_curriculo.append(f"{curso['id']}:{u['id']}:{n['id']}")

    faltam = [k for k in chaves_no_curriculo if k not in MATERIA]
    sobram = [k for k in MATERIA if k not in chaves_no_curriculo]

    print(f"niveis no curriculo: {len(chaves_no_curriculo)}")
    print(f"materia escrita:     {len(MATERIA)}")
    if faltam:
        print(f"-- sem materia ({len(faltam)}):")
        for k in faltam:
            print(f"     {k}")
    if sobram:
        # Chave que ja nao corresponde a nivel nenhum: quase sempre um erro
        # de escrita, e passaria despercebida sem este aviso.
        print(f"-- materia orfa ({len(sobram)}):", file=sys.stderr)
        for k in sobram:
            print(f"     {k}", file=sys.stderr)
        return 1

    if not gravar:
        print("\n(so leitura -- corre com --gravar para escrever)")
        return 0

    novos = 0
    for curso in dados["cursos"]:
        for u in curso["units"]:
            for n in u["niveis"]:
                m = MATERIA.get(f"{curso['id']}:{u['id']}:{n['id']}")
                if not m:
                    continue
                texto = para_ler(m)
                ficheiro = nome_do_audio(texto) + ".mp3"
                destino = AUDIO / ficheiro
                if not destino.exists():
                    if not gravar_audio(texto, destino):
                        print(f"FALHOU o audio de {n['id']}", file=sys.stderr)
                        return 1
                    novos += 1
                    print(f"   {destino.stat().st_size:>6} bytes  {ficheiro}")
                n["materia"] = {**m, "audio": ficheiro}

    # indent=1 e a formatacao que o ficheiro ja tem.
    CONTENT.write_text(
        json.dumps(dados, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    print(f"\n-- content.json gravado, {novos} audios novos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
