"""Perguntas interactivas de Ciencias Naturais e Sociais.

Porque e que nao sao escolha multipla
-------------------------------------
"O ciclo da agua e: (a)... (b)... (c)..." avalia se a crianca reconhece a
frase certa. Por os quatro passos pela ordem certa avalia se ela percebeu o
ciclo. Numa disciplina em que quase tudo e sequencia, causa e classificacao,
a escolha multipla estava a medir a coisa errada.

Tres tipos, e cada um serve uma coisa que a disciplina tem:

    sequencia -> processos: o ciclo da agua, da semente a planta, a ordem
                 dos acontecimentos historicos, a divisao administrativa
    grupos    -> classificar: vertebrado ou invertebrado, direito ou dever,
                 necessidade ou desejo, campo ou cidade
    cenario   -> montar: o circuito electrico, as partes da planta, os
                 orgaos do corpo, a cadeia alimentar

Onde e que estas perguntas entram
---------------------------------
Nos niveis que JA existem, e nao em niveis novos. A amarelinha nao muda de
forma: o que muda e o que ha dentro de cada casa. Uma crianca a meio da 5a
classe nao pode ver o mapa crescer por baixo dela.

Os enunciados vao acentuados
----------------------------
Sao o que a crianca le, e portugues sem acentos numa app de escola ensina a
escrever mal. (E a mesma razao por que o banco de palavras da sopa so tem
palavras que DISPENSAM acento: la a grelha e de maiusculas simples.)

O audio
-------
Cada enunciado novo e gravado pelo `audio.py`, que aplica as regras de
pronuncia ele proprio. Nao ha caminho por fora.

Correr a partir de somara-flutter/:
    python tools/conteudo_interactivo.py            # so mostra
    python tools/conteudo_interactivo.py --aplicar  # escreve e grava audio
"""

import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402


def seq(enunciado, passos):
    """Uma sequencia. Os passos vao PELA ORDEM CERTA -- e a unica que
    interessa guardar; quem mostra e que baralha."""
    return {"t": "sequencia", "q": enunciado, "passos": passos}


def grupos(enunciado, caixas, itens):
    """itens: lista de (nome, indice da caixa)."""
    return {
        "t": "grupos",
        "q": enunciado,
        "grupos": caixas,
        "itens": [{"nome": n, "g": g} for n, g in itens],
    }


def cenario(enunciado, cena, alvos):
    """alvos: lista de (x, y, peca), com x e y de 0 a 1 sobre o desenho."""
    return {
        "t": "cenario",
        "q": enunciado,
        "cena": cena,
        "alvos": [{"x": x, "y": y, "peca": p} for x, y, p in alvos],
    }


NOVAS = {
    # ------------------------- Ciencias Naturais -------------------------
    ("cn-4c", "u2", "n1"): [
        cenario(
            "Arrasta cada nome para a parte certa da planta.",
            "planta",
            [
                (0.26, 0.90, "raiz"),
                (0.74, 0.72, "caule"),
                (0.22, 0.50, "folha"),
                (0.56, 0.14, "flor"),
            ],
        ),
        seq(
            "Põe por ordem o que acontece da semente até a planta dar flor.",
            [
                "A semente é posta na terra húmida.",
                "A semente germina e sai a raiz.",
                "O caule sobe e abrem-se as primeiras folhas.",
                "A planta cresce e dá flor.",
            ],
        ),
    ],
    ("cn-4c", "u2", "n2"): [
        grupos(
            "Arruma cada animal no seu grupo.",
            ["Vertebrado", "Invertebrado"],
            [
                ("cabrito", 0),
                ("peixe", 0),
                ("galinha", 0),
                ("cobra", 0),
                ("formiga", 1),
                ("minhoca", 1),
                ("caracol", 1),
                ("aranha", 1),
            ],
        ),
    ],
    ("cn-4c", "u3", "n1"): [
        seq(
            "Põe por ordem os passos para tornar a água boa para beber.",
            [
                "Tirar a água do poço ou do rio.",
                "Deixar assentar e coar num pano limpo.",
                "Ferver a água durante alguns minutos.",
                "Deixar arrefecer e guardar num recipiente tapado.",
            ],
        ),
    ],
    ("cn-4c", "u7", "n1"): [
        grupos(
            "Arruma cada coisa: veio da natureza ou foi feita pelo homem?",
            ["Natural", "Feito pelo homem"],
            [
                ("árvore", 0),
                ("pedra", 0),
                ("água do rio", 0),
                ("areia", 0),
                ("tijolo", 1),
                ("cadeira", 1),
                ("garrafa", 1),
                ("capulana", 1),
            ],
        ),
    ],
    ("cn-5c", "u1", "n2"): [
        cenario(
            "Monta a cadeia alimentar, de cima para baixo.",
            "cadeia",
            [
                (0.50, 0.14, "o sol"),
                (0.50, 0.38, "o capim"),
                (0.50, 0.62, "o cabrito"),
                (0.50, 0.86, "o leopardo"),
            ],
        ),
    ],
    ("cn-5c", "u2", "n1"): [
        seq(
            "Põe por ordem o que acontece no ciclo da água.",
            [
                "O sol aquece a água dos rios e do mar.",
                "A água evapora e sobe em vapor.",
                "Lá em cima o vapor arrefece e forma nuvens.",
                "As nuvens deixam cair a chuva sobre a terra.",
            ],
        ),
    ],
    ("cn-5c", "u3", "n1"): [
        grupos(
            "Arruma cada coisa pelo estado em que se encontra.",
            ["Sólido", "Líquido", "Gasoso"],
            [
                ("pedra", 0),
                ("gelo", 0),
                ("madeira", 0),
                ("água", 1),
                ("óleo", 1),
                ("leite", 1),
                ("ar", 2),
                ("vapor de água", 2),
                ("fumo", 2),
            ],
        ),
    ],
    ("cn-6c", "u1", "n1"): [
        seq(
            "Põe por ordem o que acontece desde a flor até ao fruto.",
            [
                "A flor abre-se e mostra as suas partes.",
                "O pólen chega ao pistilo da flor.",
                "As pétalas murcham e caem.",
                "O fruto cresce com a semente lá dentro.",
            ],
        ),
    ],
    ("cn-6c", "u2", "n1"): [
        cenario(
            "Põe cada órgão no seu lugar dentro do corpo.",
            "corpo",
            [
                (0.30, 0.44, "coração"),
                (0.72, 0.40, "pulmões"),
                (0.44, 0.70, "estômago"),
            ],
        ),
    ],
    ("cn-6c", "u5", "n1"): [
        cenario(
            "Fecha o circuito para a lâmpada acender.",
            "circuito",
            [
                (0.50, 0.20, "lâmpada"),
                (0.14, 0.49, "pilha"),
                (0.86, 0.49, "fio"),
            ],
        ),
    ],
    # -------------------------- Ciencias Sociais --------------------------
    ("cs-4c", "u1", "n3"): [
        grupos(
            "Arruma cada frase: é um direito teu ou um dever teu?",
            ["Direito", "Dever"],
            [
                ("ter um nome", 0),
                ("ter saúde", 0),
                ("brincar", 0),
                ("ser tratado com respeito", 0),
                ("respeitar os mais velhos", 1),
                ("ajudar em casa", 1),
                ("cuidar da escola", 1),
                ("dizer a verdade", 1),
            ],
        ),
    ],
    ("cs-4c", "u4", "n1"): [
        seq(
            "Põe por ordem, do mais pequeno ao maior.",
            [
                "Povoação",
                "Localidade",
                "Posto administrativo",
                "Distrito",
                "Província",
            ],
        ),
    ],
    ("cs-4c", "u5", "n1"): [
        grupos(
            "Arruma cada coisa: precisas mesmo dela ou só gostavas de a ter?",
            ["Necessidade", "Desejo"],
            [
                ("comida", 0),
                ("água limpa", 0),
                ("casa", 0),
                ("roupa", 0),
                ("telemóvel", 1),
                ("doces", 1),
                ("brinquedo novo", 1),
                ("bicicleta", 1),
            ],
        ),
    ],
    ("cs-5c", "u4", "n2"): [
        seq(
            "Põe estes acontecimentos por ordem, do mais antigo ao mais recente.",
            [
                "Fundação da FRELIMO, em 1962.",
                "Início da luta armada, a 25 de Setembro de 1964.",
                "Acordos de Lusaka, em Setembro de 1974.",
                "Independência de Moçambique, a 25 de Junho de 1975.",
            ],
        ),
    ],
    ("cs-6c", "u5", "n1"): [
        grupos(
            "Arruma cada coisa no sítio onde é mais comum encontrá-la.",
            ["No campo", "Na cidade"],
            [
                ("machamba", 0),
                ("gado", 0),
                ("poço", 0),
                ("palhota", 0),
                ("prédio", 1),
                ("semáforo", 1),
                ("autocarro", 1),
                ("hospital central", 1),
            ],
        ),
    ],
}


def main():
    aplicar = "--aplicar" in sys.argv
    dados = audio.carregar_content()

    por_curso = {c["id"]: c for c in dados["cursos"]}
    acrescentadas, falhadas = [], []

    for (curso_id, unidade_id, nivel_id), perguntas in NOVAS.items():
        curso = por_curso.get(curso_id)
        if curso is None:
            falhadas.append((curso_id, "curso nao existe"))
            continue
        unidade = next(
            (u for u in curso["units"] if u["id"] == unidade_id), None
        )
        if unidade is None:
            falhadas.append((f"{curso_id}/{unidade_id}", "unidade nao existe"))
            continue
        nivel = next(
            (n for n in unidade["niveis"] if n["id"] == nivel_id), None
        )
        if nivel is None:
            falhadas.append(
                (f"{curso_id}/{unidade_id}/{nivel_id}", "nivel nao existe")
            )
            continue

        ja = {q["q"] for q in nivel["questoes"]}
        for pergunta in perguntas:
            if pergunta["q"] in ja:
                continue
            acrescentadas.append(
                (f"{curso_id}/{unidade_id}/{nivel_id}", pergunta)
            )
            if aplicar:
                nivel["questoes"].append(pergunta)

    print(f"-- {len(acrescentadas)} perguntas interactivas")
    por_tipo = {}
    for _, p in acrescentadas:
        por_tipo[p["t"]] = por_tipo.get(p["t"], 0) + 1
    for t, n in sorted(por_tipo.items()):
        print(f"   {t:10} {n}")
    for onde, p in acrescentadas:
        print(f'   {onde:16} [{p["t"]:9}] {p["q"]}')
    for onde, porque in falhadas:
        print(f"   !! {onde}: {porque}")

    if not aplicar:
        print("\n-- nada foi escrito (usa --aplicar)")
        return

    # O audio por ultimo, so depois de o conteudo estar montado.
    manifesto = audio.ler_manifesto()
    gravados = 0
    for _, pergunta in acrescentadas:
        nome = audio.nome_do_ficheiro(pergunta["q"])
        pergunta["audio"] = nome
        if audio.gravar(pergunta["q"], nome, manifesto):
            gravados += 1
            print(f'   audio {nome}  {pergunta["q"][:52]}')
    audio.escrever_manifesto(manifesto)
    audio.gravar_content(dados)
    print(f"\n-- {gravados} ficheiros de audio, content.json escrito")


if __name__ == "__main__":
    main()
