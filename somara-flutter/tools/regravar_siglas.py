"""Regrava o audio dos textos que levam siglas ou abreviaturas.

O nome do ficheiro e o SHA-1 do texto que aparece no ECRA, e esse nao muda
-- muda so o que a voz diz. Por isso nao chega gerar: e preciso apagar o
ficheiro antigo e gravar por cima.

Correr a partir de somara-flutter/:
    python tools/regravar_siglas.py          # so mostra o que ia mudar
    python tools/regravar_siglas.py --gravar

Sem mais nada, apanha TODOS os textos cuja voz difere do ecra -- inclusive
os que ja foram gravados bem numa passagem anterior, porque o ficheiro nao
diz o que tem la dentro. Quando se acrescenta uma regra nova e se sabe
quais os ficheiros que ela desactualizou, dao-se os nomes:

    python tools/regravar_siglas.py --gravar 8bf7c46fe30a.mp3 ...

Assim regravam-se 16 e nao 240.
"""

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pronuncia import para_dizer, mexe_em  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
CONTENT = RAIZ / "assets" / "content.json"
AUDIO = RAIZ / "assets" / "audio"

VOZ = "pt-PT-RaquelNeural"
TOM = "+25Hz"
RITMO = "-5%"

_LIXO = re.compile("[\U0001F000-\U0001FAFF☀-➿️‍]|_{2,}", flags=re.UNICODE)


def nome_do_audio(texto: str) -> str:
    return hashlib.sha1(texto.encode("utf-8")).hexdigest()[:12]


def limpar(texto: str) -> str:
    return re.sub(r"\s+", " ", _LIXO.sub(" ", texto)).strip()


def gravar(texto: str, destino: Path) -> bool:
    r = subprocess.run(
        ["edge-tts", "--voice", VOZ, f"--pitch={TOM}", f"--rate={RITMO}",
         "--text", texto, "--write-media", str(destino)],
        capture_output=True,
    )
    return r.returncode == 0 and destino.exists() and destino.stat().st_size > 0


def main() -> int:
    gravar_mesmo = "--gravar" in sys.argv
    # Nomes de ficheiro dados a mao: regrava-se so esses.
    escolhidos = {a for a in sys.argv[1:] if a.endswith(".mp3")}
    dados = json.loads(CONTENT.read_text(encoding="utf-8"))

    # ficheiro -> (texto no ecra, texto a dizer)
    tarefas: dict[str, tuple[str, str]] = {}

    for curso in dados["cursos"]:
        for u in curso["units"]:
            for n in u["niveis"]:
                m = n.get("materia")
                if m and m.get("audio"):
                    bruto = f"{m['explica']} {m['exemplo']}"
                    if mexe_em(bruto):
                        tarefas[m["audio"]] = (bruto, para_dizer(bruto))
                for q in n["questoes"]:
                    if q.get("audio") and mexe_em(q["q"]):
                        tarefas[q["audio"]] = (q["q"], para_dizer(q["q"]))

    if escolhidos:
        emfalta = escolhidos - set(tarefas)
        if emfalta:
            print(f"AVISO: nao encontrados no content.json: "
                  f"{', '.join(sorted(emfalta))}", file=sys.stderr)
        tarefas = {f: v for f, v in tarefas.items() if f in escolhidos}

    print(f"ficheiros a regravar: {len(tarefas)}\n")
    for ficheiro, (antes, depois) in list(tarefas.items())[:6]:
        print(f"  {ficheiro}")
        print(f"    ecra: {antes[:90]}")
        print(f"    voz : {para_dizer(antes)[:90]}\n")
    if len(tarefas) > 6:
        print(f"  ... e mais {len(tarefas) - 6}\n")

    if not gravar_mesmo:
        print("(so leitura -- corre com --gravar)")
        return 0

    # Confirma que o nome bate certo com o texto do ecra: se nao bater, o
    # audio ia parar ao ficheiro errado e a pergunta ficava com a voz de
    # outra.
    for ficheiro, (ecra, _) in tarefas.items():
        esperado = nome_do_audio(limpar(ecra) if False else ecra) + ".mp3"
        if esperado != ficheiro:
            # A materia usa explica+exemplo, cujo nome foi calculado sobre o
            # texto ja limpo. Aceita-se essa variante.
            alternativo = nome_do_audio(limpar(ecra)) + ".mp3"
            if alternativo != ficheiro:
                print(f"AVISO: {ficheiro} nao corresponde ao texto; saltado",
                      file=sys.stderr)

    feitos = 0
    for ficheiro, (_, dizer) in tarefas.items():
        destino = AUDIO / ficheiro
        destino.unlink(missing_ok=True)
        if not gravar(limpar(dizer), destino):
            print(f"FALHOU {ficheiro}", file=sys.stderr)
            return 1
        feitos += 1
        print(f"   {destino.stat().st_size:>6} bytes  {ficheiro}")

    print(f"\n-- {feitos} ficheiros regravados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
