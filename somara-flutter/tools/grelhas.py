"""Converte perguntas de Matematica em contas armadas.

Porque e que so algumas
-----------------------
A grelha ensina o METODO: alinhar as ordens, somar coluna a coluna, levar o
que passa de dez. Numa conta de uma so ordem -- 2 + 1, 4 - 2 -- nao ha
metodo nenhum para ensinar: ha uma coisa que se sabe de cor. Armar 2 + 1
numa grelha de duas casinhas nao ensina nada e faz perder tempo a uma
crianca da 1a classe, que e justamente quem tem essas perguntas.

Por isso o criterio e o do valor pedagogico e nao o do numero de perguntas
convertidas:

  1a classe           -> nunca. Nao se arma nada na 1a classe: aprendem-se
                         os numeros ate 20 e a ideia de juntar e tirar. A
                         conta armada e materia da 2a. Uma grelha aqui
                         ensina um metodo que a turma ainda nao tem.
  adicao e subtraccao -> pelo menos um dos numeros com duas ordens
  multiplicacao       -> o multiplicando com duas ordens, e nenhum zero no
                         multiplicador. "25 x 10" arma-se com duas linhas
                         de zeros, e nao e assim que se ensina -- x10
                         ensina-se como regra ("acrescenta um zero"), nao
                         como algoritmo.
  divisao             -> o dividendo com duas ordens

Como se sabe que a leitura do enunciado esta certa
--------------------------------------------------
Nao se acredita no texto. Le-se "Quanto e 247 + 185?", calcula-se, e
COMPARA-SE com a resposta que ja la estava no content.json. Se nao bater,
nao se converte -- foi mal lido. Isto apanhou de proposito coisas como
"Conta de 5 em 5: 5, 10, 15, ?", que tem digitos e dois pontos e nao e
divisao nenhuma.

O enunciado nao muda, e por isso o audio ja gravado continua bom. E a
unica razao por que esta conversao nao obriga a regravar nada.

Correr a partir de somara-flutter/:
    python tools/grelhas.py            # so mostra o que ia mudar
    python tools/grelhas.py --aplicar  # escreve no content.json
"""

import io
import json
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

RAIZ = Path(__file__).resolve().parent.parent
CONTENT = RAIZ / "assets" / "content.json"

# Os sinais como aparecem nos enunciados, e o nome do enum Operacao.
SINAIS = {
    "+": "adicao",
    "-": "subtraccao",
    "−": "subtraccao",   # menos tipografico
    "–": "subtraccao",   # travessao, que aparece nalguns enunciados
    "x": "multiplicacao",
    "×": "multiplicacao",
    ":": "divisao",
    "÷": "divisao",
}

# O enunciado tem de ser SO a conta, com um destes moldes. Um texto a volta
# da conta e quase sempre um problema com historia, e esse continua a ser
# melhor em escolha multipla.
MOLDES = [
    re.compile(r"^quanto\s+é\s+(\d+)\s*(.)\s*(\d+)\s*\?$", re.I),
    re.compile(r"^(\d+)\s*(.)\s*(\d+)\s*=\s*\??$", re.I),
    re.compile(r"^calcula:?\s*(\d+)\s*(.)\s*(\d+)\s*=?\s*\??$", re.I),
]


def ler_conta(enunciado):
    """(operacao, x, y) ou None."""
    texto = enunciado.strip()
    for molde in MOLDES:
        m = molde.match(texto)
        if not m:
            continue
        sinal = m.group(2)
        op = SINAIS.get(sinal)
        if op is None:
            return None
        return op, int(m.group(1)), int(m.group(3))
    return None


def resultado(op, x, y):
    if op == "adicao":
        return x + y
    if op == "subtraccao":
        return x - y
    if op == "multiplicacao":
        return x * y
    if op == "divisao":
        return None if y == 0 or x % y else x // y
    return None


def vale_a_pena(op, x, y):
    """A grelha ensina alguma coisa nesta conta?"""
    if op in ("adicao", "subtraccao"):
        return x >= 10 or y >= 10
    if op == "multiplicacao":
        return x >= 10 and "0" not in str(y)
    if op == "divisao":
        return x >= 10
    return False


def resposta_dita(q):
    """O que o content.json diz ser a resposta certa, como texto."""
    if q["t"] == "input":
        return str(q["a"]).strip()
    if q["t"] == "choice":
        return str(q["options"][q["a"]]).strip()
    return None


def converter(dados, aplicar):
    mudadas, recusadas = [], []

    for curso in dados["cursos"]:
        if not curso["id"].startswith("mat"):
            continue
        if curso["classe"].startswith("1"):
            recusadas.append((curso["id"], "(curso inteiro)", "1a classe"))
            continue
        for unidade in curso["units"]:
            for nivel in unidade["niveis"]:
                for q in nivel["questoes"]:
                    if q["t"] not in ("input", "choice"):
                        continue
                    lida = ler_conta(q["q"])
                    if lida is None:
                        continue
                    op, x, y = lida
                    onde = f'{curso["id"]}/{unidade["id"]}/{nivel["id"]}'

                    r = resultado(op, x, y)
                    if r is None:
                        recusadas.append((onde, q["q"], "nao se arma"))
                        continue

                    dita = resposta_dita(q)
                    if dita is None or dita != str(r):
                        # Le-se mal ou a resposta guardada e outra coisa.
                        recusadas.append(
                            (onde, q["q"], f"resposta {dita!r} != {r}")
                        )
                        continue

                    if not vale_a_pena(op, x, y):
                        recusadas.append((onde, q["q"], "uma ordem so"))
                        continue

                    mudadas.append((onde, q["q"], op, x, y, r))
                    if aplicar:
                        # O enunciado e o audio ficam como estao. So muda a
                        # maneira de responder.
                        for chave in ("options", "a", "chip", "zones"):
                            q.pop(chave, None)
                        q["t"] = "grelha"
                        q["op"] = op
                        q["x"] = x
                        q["y"] = y

    return mudadas, recusadas


def main():
    aplicar = "--aplicar" in sys.argv
    dados = json.loads(CONTENT.read_text(encoding="utf-8"))
    mudadas, recusadas = converter(dados, aplicar)

    por_op = {}
    for _, _, op, *_ in mudadas:
        por_op[op] = por_op.get(op, 0) + 1

    print(f"-- {len(mudadas)} perguntas viram conta armada")
    for op, n in sorted(por_op.items()):
        print(f"   {op:16} {n}")
    for onde, texto, op, x, y, r in mudadas:
        print(f"   {onde:22} {texto}  ->  {op} {x} {y} = {r}")

    print(f"\n-- {len(recusadas)} deixadas como estavam")
    for onde, texto, porque in recusadas:
        print(f"   {onde:22} {texto}  ({porque})")

    if aplicar:
        CONTENT.write_text(
            json.dumps(dados, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
        print("\n-- content.json escrito")
    else:
        print("\n-- nada foi escrito (usa --aplicar)")


if __name__ == "__main__":
    main()
