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

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402
from materia_texto import MATERIA  # noqa: E402

CONTENT = audio.CONTENT
AUDIO = audio.AUDIO


def bruto_da_materia(m: dict) -> str:
    """O que a Raquel le: a explicacao e o exemplo, sem o "lembra".

    O "lembra" fica de fora de proposito -- e uma nota para os olhos, e dita
    em voz alta logo a seguir ao exemplo soa a repeticao.
    """
    return f"{m['explica']} {m['exemplo']}"


def nome_da_materia(m: dict) -> str:
    """O nome do mp3 de uma aula.

    E o SHA-1 do texto JA LIMPO, e nao do bruto -- foi assim que os 179
    ficheiros existentes foram nomeados, e mudar a conta agora renomeava-os
    a todos sem que o som mudasse.
    """
    return audio.sha(audio.limpar(bruto_da_materia(m))) + ".mp3"


def main() -> int:
    gravar = "--gravar" in sys.argv
    dados = audio.carregar_content()

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

    manifesto = audio.ler_manifesto()
    novos = 0
    for curso in dados["cursos"]:
        for u in curso["units"]:
            for n in u["niveis"]:
                m = MATERIA.get(f"{curso['id']}:{u['id']}:{n['id']}")
                if not m:
                    continue
                bruto = bruto_da_materia(m)
                ficheiro = nome_da_materia(m)
                destino = AUDIO / ficheiro

                # Grava-se quando o ficheiro falta OU quando o que la esta
                # dentro ja nao e o que as regras mandam dizer. A condicao
                # antiga era so "nao existe", e por isso uma regra de
                # pronuncia nova nunca chegava as aulas ja gravadas.
                actual = manifesto.get(ficheiro)
                devia = audio.sha(audio.dito(bruto))
                if not destino.exists() or actual != devia:
                    # O texto do ECRA e que vai para o gravador: e ele que
                    # aplica as regras. Antes daqui passava o texto cru, e
                    # foi assim que a aula do perimetro ficou a ler
                    # "cinco mais cinco mais cinco mais cinco vinte ce eme".
                    if not audio.gravar(bruto, ficheiro, manifesto):
                        print(f"FALHOU o audio de {n['id']}", file=sys.stderr)
                        audio.escrever_manifesto(manifesto)
                        return 1
                    novos += 1
                    print(f"   {destino.stat().st_size:>6} bytes  {ficheiro}")
                n["materia"] = {**m, "audio": ficheiro}

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- content.json gravado, {novos} audios gravados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
