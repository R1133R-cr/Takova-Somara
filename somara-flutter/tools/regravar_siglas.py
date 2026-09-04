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

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402
from audio import AUDIO, escrever_manifesto, ler_manifesto, limpar  # noqa: E402
from pronuncia import mexe_em, para_dizer  # noqa: E402

# A voz, o `limpar`, o calculo do nome e o manifesto vivem todos no
# tools/audio.py. Tinham copias aqui, e foi ter copias -- uma delas sem as
# regras de pronuncia -- que poe audio errado no telemovel.
nome_do_audio = audio.sha
todas_as_falas = audio.falas_do_curriculo


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
    dados = audio.carregar_content()

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
    #
    # Ha duas contas validas porque ha duas convencoes: as perguntas foram
    # nomeadas sobre o texto cru, as aulas sobre o texto ja limpo.
    for ficheiro, (ecra, _) in tarefas.items():
        if ficheiro not in (nome_do_audio(ecra) + ".mp3",
                            nome_do_audio(limpar(ecra)) + ".mp3"):
            print(f"AVISO: {ficheiro} nao corresponde ao texto do ecra",
                  file=sys.stderr)

    manifesto = ler_manifesto()
    feitos = 0
    for ficheiro, (ecra, _) in tarefas.items():
        # Passa-se o texto do ECRA: e o audio.py que aplica as regras e
        # escreve o registo. Aqui nao se decide o que se diz -- foi isso
        # que correu mal quando cada ferramenta decidia por si.
        if not audio.gravar(ecra, ficheiro, manifesto):
            print(f"FALHOU {ficheiro}", file=sys.stderr)
            # O manifesto vai gravado com o que ja se fez: se a passagem
            # morrer a meio, o --conferir aponta exactamente o que ficou
            # por fazer, em vez de o esconder.
            escrever_manifesto(manifesto)
            return 1
        feitos += 1
        print(f"   {(AUDIO / ficheiro).stat().st_size:>6} bytes  {ficheiro}")

    escrever_manifesto(manifesto)
    print(f"\n-- {feitos} ficheiros regravados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
