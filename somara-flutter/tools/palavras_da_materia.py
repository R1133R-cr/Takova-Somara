"""O vocabulario de cada unidade, para a sopa de letras da materia.

A regra, e a que estava invertida
--------------------------------
As palavras escrevem-se BEM, com acento e cedilha. A grelha e que leva as
letras simples -- e assim em qualquer sopa de letras impressa, e e a ordem
certa das duas coisas: a lista mostra "lampada" com o circunflexo, as letras
mostram LAMPADA.

A regra anterior era "so entram palavras que dispensam acento", e falhava
por dois lados ao mesmo tempo: doze palavras do banco antigo estavam
escritas SEM o acento que tem (oleo, fogao, regua, camiao, arvore, poco) --
ou seja, a app ensinava a escreve-las mal, que era exactamente o que a regra
dizia querer evitar -- e o vocabulario das Ciencias, que e quase todo
acentuado, ficava de fora.

De onde vem
-----------
Escritas a mao, unidade a unidade, a partir dos titulos e do conteudo que a
unidade ja tem. Nao se extraem do texto automaticamente: extrair
substantivos de prosa da lixo -- artigos, verbos, palavras da pergunta e nao
da materia -- e a sopa passava a treinar vocabulario que nao e da unidade.

Correr a partir de somara-flutter/:
    python tools/palavras_da_materia.py            # so mostra
    python tools/palavras_da_materia.py --aplicar  # escreve no content.json
"""

import io
import json
import sys
import unicodedata
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

RAIZ = Path(__file__).resolve().parent.parent
CONTENT = RAIZ / "assets" / "content.json"

# Minimo para valer a pena uma sopa. Abaixo disto a grelha fica vazia e a
# crianca acha as palavras todas em dez segundos.
MINIMO = 6

# A maior grelha da sopa tem catorze letras de lado.
MAIOR_GRELHA = 14

BANCOS = {
    # ---------------------- Ciencias Naturais ----------------------
    ("cn-4c", "u2"): [
        "RAIZ", "CAULE", "FOLHA", "FLOR", "FRUTO", "SEMENTE",
        "CABRITO", "GALINHA", "PEIXE", "COBRA", "FORMIGA", "MINHOCA",
    ],
    ("cn-4c", "u3"): [
        "CHUVA", "RIO", "POÇO", "BALDE", "LIXO", "VIDRO",
        "PLÁSTICO", "PAPEL", "LATA", "FERVER", "COAR", "TAPAR",
    ],
    ("cn-4c", "u4"): [
        "VISTA", "OUVIDO", "TACTO", "OLFACTO", "PALADAR", "SAÚDE",
        "DENTE", "BANHO", "SABÃO", "FEBRE", "MICRÓBIO", "VACINA",
    ],
    ("cn-4c", "u8"): [
        "PILHA", "FIO", "LÂMPADA", "CIRCUITO", "CORRENTE", "TOMADA",
        "SÓLIDO", "LÍQUIDO", "GASOSO", "MASSA", "VOLUME",
    ],
    ("cn-4c", "u9"): [
        "MACHAMBA", "ENXADA", "SEMENTE", "MILHO", "MANDIOCA",
        "ARROZ", "REGAR", "COLHEITA", "ADUBO", "HORTA", "GADO",
    ],
    ("cn-5c", "u1"): [
        "RAIZ", "CAULE", "FOLHA", "FLOR", "PÓLEN", "FRUTO",
        "MAMÍFERO", "AVE", "RÉPTIL", "INSECTO", "PEIXE", "ANFÍBIO",
    ],
    ("cn-5c", "u2"): [
        "CHUVA", "NUVEM", "VAPOR", "RIO", "LAGO", "POÇO",
        "SOLO", "AREIA", "ARGILA", "HÚMUS", "EROSÃO", "ADUBO",
    ],
    ("cn-5c", "u5"): [
        "SOL", "VENTO", "CALOR", "LUZ", "SOM", "SOMBRA",
        "ECO", "ESPELHO", "PILHA", "CARVÃO", "LENHA", "ENERGIA",
    ],
    ("cn-6c", "u2"): [
        "CORAÇÃO", "PULMÃO", "ESTÔMAGO", "INTESTINO", "SANGUE",
        "OSSO", "MÚSCULO", "PELE", "NERVO", "RIM", "VACINA",
    ],
    ("cn-6c", "u4"): [
        "ALAVANCA", "ROLDANA", "RAMPA", "RODA", "EIXO", "MÁQUINA",
        "LUZ", "SOM", "ECO", "SOMBRA", "ESPELHO", "LENTE",
    ],
    ("cn-6c", "u5"): [
        "PILHA", "FIO", "LÂMPADA", "CIRCUITO", "CORRENTE", "TOMADA",
        "CHOQUE", "ISOLANTE", "CONDUTOR", "INTERRUPTOR", "ENERGIA",
    ],
    # ----------------------- Ciencias Sociais -----------------------
    ("cs-4c", "u1"): [
        "PAI", "MÃE", "IRMÃO", "AVÓ", "TIO", "PRIMO",
        "NOME", "RESPEITO", "ESCOLA", "AJUDA", "VERDADE", "FAMÍLIA",
    ],
    ("cs-4c", "u2"): [
        "ALDEIA", "BAIRRO", "VIZINHO", "MERCADO", "IGREJA",
        "LENDA", "CONTO", "LÍNGUA", "COSTUME", "FESTA", "RESPEITO",
    ],
    ("cs-4c", "u4"): [
        "NIASSA", "TETE", "SOFALA", "MANICA", "GAZA", "LICHINGA",
        "RIO", "MONTE", "PLANALTO", "CHUVA", "ESTRADA", "PROVÍNCIA",
    ],
    ("cs-5c", "u1"): [
        "NORTE", "SUL", "ESTE", "OESTE", "MAPA", "BÚSSOLA",
        "ZAMBEZE", "LIMPOPO", "ROVUMA", "SAVE", "ÍNDICO", "PLANALTO",
    ],
    ("cs-5c", "u4"): [
        "FRELIMO", "LUTA", "ARMADA", "LUSAKA", "BANDEIRA",
        "MONDLANE", "MACHEL", "LIBERDADE", "COLONO", "VITÓRIA", "PAZ",
    ],
    ("cs-5c", "u5"): [
        "BANDEIRA", "HINO", "EMBLEMA", "ESCUDO", "ENXADA",
        "ESTRELA", "LIVRO", "CATANA", "PAZ", "UNIDADE", "NAÇÃO",
    ],
    ("cs-6c", "u2"): [
        "ÁFRICA", "SAARA", "NILO", "CONGO", "SADC",
        "DESERTO", "SAVANA", "FLORESTA", "ILHA", "COSTA", "EQUADOR",
    ],
    ("cs-6c", "u5"): [
        "CIDADE", "CAMPO", "MACHAMBA", "FÁBRICA", "MERCADO",
        "PESCA", "MINA", "TURISMO", "COMÉRCIO", "TRANSPORTE", "PORTO",
    ],
}


def sem_acento(palavra):
    """A forma que vai para a grelha."""
    sem = unicodedata.normalize("NFD", palavra)
    return "".join(c for c in sem if not unicodedata.combining(c))


def main():
    aplicar = "--aplicar" in sys.argv
    dados = json.loads(CONTENT.read_text(encoding="utf-8"))
    por_curso = {c["id"]: c for c in dados["cursos"]}

    postos, recusadas = [], []

    for (curso_id, unidade_id), palavras in BANCOS.items():
        curso = por_curso.get(curso_id)
        unidade = None
        if curso is not None:
            unidade = next(
                (u for u in curso["units"] if u["id"] == unidade_id), None
            )
        if unidade is None:
            recusadas.append((f"{curso_id}/{unidade_id}", "nao existe"))
            continue

        boas, mas = [], []
        vistas = set()
        for p in palavras:
            simples = sem_acento(p)
            if p != p.upper():
                mas.append((p, "nao esta em maiusculas"))
            elif len(simples) > MAIOR_GRELHA:
                mas.append((p, "nao cabe nem na maior grelha"))
            elif simples in vistas:
                # Duas palavras que ficam iguais sem acento sao a mesma na
                # grelha, e a crianca so pode achar uma delas.
                mas.append((p, "fica igual a outra na grelha"))
            else:
                vistas.add(simples)
                boas.append(p)

        for p, porque in mas:
            recusadas.append((f"{curso_id}/{unidade_id}: {p}", porque))

        if len(boas) < MINIMO:
            recusadas.append(
                (f"{curso_id}/{unidade_id}", f"so {len(boas)} palavras boas")
            )
            continue

        postos.append((f"{curso_id}/{unidade_id}", unidade["titulo"], boas))
        if aplicar:
            unidade["palavras"] = boas

    print(f"-- {len(postos)} unidades com vocabulario")
    for onde, titulo, boas in postos:
        print(f"   {onde:12} {titulo:34} {len(boas):2}  {' '.join(boas)}")
    if recusadas:
        print(f"\n-- {len(recusadas)} recusadas")
        for onde, porque in recusadas:
            print(f"   {onde}  ({porque})")

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
