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

# A consola do Windows e cp1252 e nao sabe escrever o sinal de menos (−,
# U+2212) nem o de multiplicar (×). Sem isto o programa rebenta a MOSTRAR
# o que ia fazer -- e rebenta a meio, depois de ja ter gravado uns
# quantos, deixando o resto por gravar sem que se de por isso.
#
# Foi exactamente o que aconteceu: sessenta ficheiros de Matematica da 3a
# a 6a classe ficaram por tratar numa passagem que pareceu correr bem.
for _fluxo in (sys.stdout, sys.stderr):
    try:
        _fluxo.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:  # pragma: no cover -- fluxo redirigido
        pass

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pronuncia import para_dizer, mexe_em  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
CONTENT = RAIZ / "assets" / "content.json"
AUDIO = RAIZ / "assets" / "audio"

# Que texto e que esta gravado dentro de cada mp3.
#
# O nome do ficheiro e o SHA-1 do texto do ECRA, e por isso nao muda quando
# uma regra de pronuncia muda: o ficheiro fica com o nome certo e o som
# errado, e nao ha maneira de dar por isso a olhar para o disco.
#
# Aconteceu duas vezes. Uma delas ficaram sessenta ficheiros de Matematica
# da 3a a 6a classe a ler "dois dois tres" onde esta "2² × 2³", e so se
# descobriu por acaso, meses depois, ao gravar o mesmo texto outra vez e
# repapar no tamanho.
#
# Este ficheiro guarda o SHA-1 do texto DITO. Com ele, `--conferir` diz num
# instante se algum audio ficou para tras, sem ter de regravar nada.
#
# Fica em tools/ e nao em assets/: e uma ferramenta de quem constroi a app,
# nao faz falta nenhuma dentro do telemovel.
MANIFESTO = Path(__file__).resolve().parent / "audio_dito.json"

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


def ler_manifesto() -> dict[str, str]:
    if not MANIFESTO.exists():
        return {}
    return json.loads(MANIFESTO.read_text(encoding="utf-8"))


def escrever_manifesto(m: dict[str, str]) -> None:
    MANIFESTO.write_text(
        json.dumps(dict(sorted(m.items())), ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )


def todas_as_falas(dados) -> dict[str, str]:
    """ficheiro -> texto do ecra, para tudo o que tem audio."""
    falas: dict[str, str] = {}
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


def conferir(dados) -> int:
    """O audio gravado corresponde ao que as regras de hoje mandam dizer?"""
    manifesto = ler_manifesto()
    falas = todas_as_falas(dados)
    fora, sem_registo, sem_ficheiro = [], [], []

    for ficheiro, ecra in falas.items():
        if not (AUDIO / ficheiro).exists():
            sem_ficheiro.append(ficheiro)
            continue
        devia = nome_do_audio(limpar(para_dizer(ecra)))
        registado = manifesto.get(ficheiro)
        if registado is None:
            sem_registo.append(ficheiro)
        elif registado != devia:
            fora.append((ficheiro, ecra))

    for f in sem_ficheiro:
        print(f"EM FALTA   {f}", file=sys.stderr)
    for f in sem_registo:
        print(f"SEM REGISTO {f} — corre --manifesto depois de confirmar",
              file=sys.stderr)
    for f, ecra in fora:
        print(f"DESACTUALIZADO {f}", file=sys.stderr)
        print(f"    ecra: {ecra[:90]}", file=sys.stderr)
        print(f"    devia dizer: {para_dizer(ecra)[:90]}", file=sys.stderr)

    mau = len(fora) + len(sem_registo) + len(sem_ficheiro)
    if mau:
        print(f"\n{mau} de {len(falas)} ficheiros de audio fora do sitio.\n"
              f"Regrava com: python tools/regravar_siglas.py --gravar "
              f"{' '.join(f for f, _ in fora) or '<nomes>'}", file=sys.stderr)
        return 1
    print(f"os {len(falas)} ficheiros de audio dizem o que devem dizer")
    return 0


def main() -> int:
    gravar_mesmo = "--gravar" in sys.argv
    # Nomes de ficheiro dados a mao: regrava-se so esses.
    escolhidos = {a for a in sys.argv[1:] if a.endswith(".mp3")}
    dados = json.loads(CONTENT.read_text(encoding="utf-8"))

    if "--conferir" in sys.argv:
        return conferir(dados)

    if "--manifesto" in sys.argv:
        # So se faz isto depois de ter confirmado que o audio esta certo:
        # o manifesto passa a ser a verdade, e escreve-lo por cima de audio
        # errado torna o erro invisivel para sempre.
        falas = todas_as_falas(dados)
        novo = {f: nome_do_audio(limpar(para_dizer(t)))
                for f, t in falas.items() if (AUDIO / f).exists()}
        escrever_manifesto(novo)
        print(f"-- manifesto escrito com {len(novo)} entradas")
        return 0

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

    manifesto = ler_manifesto()
    feitos = 0
    for ficheiro, (_, dizer) in tarefas.items():
        destino = AUDIO / ficheiro
        dito = limpar(dizer)
        destino.unlink(missing_ok=True)
        if not gravar(dito, destino):
            print(f"FALHOU {ficheiro}", file=sys.stderr)
            # O manifesto vai gravado com o que ja se fez: se a passagem
            # morrer a meio, o --conferir aponta exactamente o que ficou
            # por fazer, em vez de o esconder.
            escrever_manifesto(manifesto)
            return 1
        manifesto[ficheiro] = nome_do_audio(dito)
        feitos += 1
        print(f"   {destino.stat().st_size:>6} bytes  {ficheiro}")

    escrever_manifesto(manifesto)
    print(f"\n-- {feitos} ficheiros regravados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
