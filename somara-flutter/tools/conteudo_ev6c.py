# -*- coding: utf-8 -*-
"""O curso de Educacao Visual e Oficios da 6a classe.

De onde vem
-----------
Do livro "Educacao Visual da 6a classe", MEC 2024, guardado em

    Documents\\planos da 5a classe\\Livros\\6a Classe\\
    EV 6ª classe 2024 (www.MozEstuda.com).pdf

AVISO SOBRE A FONTE: o MozEstuda e um portal privado, nao e o MINEDH. Ver
o cabecalho do conteudo_por4c.py.

PORQUE E QUE ESTA DISCIPLINA E DIFERENTE DAS OUTRAS
====================================================
A Educacao Visual ensina-se a FAZER: desenhar, pintar, misturar tintas,
recortar, dobrar. Uma app de escolha multipla nao poe ninguem a pintar, e
fingir que poe seria enganar a crianca e quem a comprou.

Entao esta disciplina foi adaptada, e a adaptacao tem duas partes.

1. As perguntas sao sobre DECIDIR, nao sobre executar
-----------------------------------------------------
O que se pode mesmo avaliar por escrito e o que um artesao decide antes de
por as maos na obra: que material serve para que trabalho, por que ordem
se fazem as coisas, que regra de seguranca se cumpre, o que acontece
quando se juntam duas tintas.

  "Um lapis de carvao duro serve para desenho rigoroso ou livre?"
  "Antes de comecar, o que se faz primeiro?"

Isto e conhecimento verdadeiro de oficio e nao decorar nomes.

2. A COR mostra-se, nao se nomeia
----------------------------------
Perguntar "que cor da o amarelo com o azul?" com tres palavras por baixo
nao ensina cor nenhuma -- ensina vocabulario, e a crianca que nunca viu as
tintas juntar-se acerta de cor e continua sem saber.

Por isso foi acrescentado ao modelo um campo `cores`, que faz duas coisas:

    "cores": {
      "mistura": ["#F2C200", "#1E5AA8"],
      "opcoes":  ["#2E8B57", "#E8791C", "#7B3F9D"]
    }

A `mistura` aparece no ecra como duas manchas de tinta com um "+" entre
elas e um "?" no fim. As `opcoes` poem uma mancha ao lado de cada resposta.
A crianca escolhe a COR e le o nome dela ao mesmo tempo, que e a ordem
certa: primeiro ve-se verde, depois aprende-se que aquilo se chama verde.

O enunciado NOMEIA as cores, mesmo mostrando-as. Escrevi-o primeiro sem
nomes -- "Que cor sai desta mistura?" -- e estava errado por duas razoes: a
frase repetia-se em perguntas diferentes, e a crianca que depende do audio
ouvia sempre a mesma coisa sem saber de que mistura se tratava. Nomear as
cores torna cada pergunta unica, e a mancha continua la a mostrar o que a
palavra quer dizer. E nos dois sentidos que se aprende.

As misturas sao as do livro, palavra por palavra:
    Amarelo + Vermelho = Laranja
    Amarelo + Azul     = Verde
    Vermelho + Azul    = Violeta
    preto + branco     = tons de cinzento

Correr a partir de somara-flutter/:
    python tools/conteudo_ev6c.py            # so mostra
    python tools/conteudo_ev6c.py --gravar
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

# As tintas. Escolhidas para se distinguirem bem no fundo escuro da app e
# para o verde nao se confundir com o verde da propria interface.
AMARELO = "#F2C200"
AZUL = "#1E5AA8"
VERMELHO = "#D8352A"
LARANJA = "#E8791C"
VERDE = "#2E8B57"
VIOLETA = "#7B3F9D"
BRANCO = "#F5F5F0"
PRETO = "#1A1A1A"
CINZENTO = "#8A8A8A"

CURSO = {
    "id": "ev-6c",
    "disciplina": "Educação Visual e Ofícios",
    # Nome comprido: sem isto a pastilha da barra mostra tudo e nao cabe.
    "abrev": "Ed. Visual",
    "classe": "6ª classe",
    "tag": "EV",
    "units": [
        # ---------------------------------------------------------------
        # 1: Desenho  (livro, pp. 9-15)
        # ---------------------------------------------------------------
        {
            "id": "u1",
            "titulo": "Desenho",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Antes de começar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Antes de começar um trabalho, o que se faz primeiro?",
                            "options": [
                                "Juntar todos os materiais que vou precisar",
                                "Começar e ir buscando o que falta",
                                "Pedir ao colega do lado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No fim da aula, o espaço de trabalho deve ficar:",
                            "options": [
                                "Limpo, para a aula seguinte",
                                "Como está, alguém limpa",
                                "Só arrumado no fim da semana",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para desenhar e escrever, o lápis deve estar:",
                            "options": ["Bem afiado", "Rombo", "Partido"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um material riscador?",
                            "options": ["O carvão vegetal", "A cola", "A tesoura"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Escolher o material",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Para um desenho rigoroso escolhe-se um lápis:",
                            "options": [
                                "De mina mais dura",
                                "De mina mais macia",
                                "De cera",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O desenho feito sem régua nem compasso chama-se:",
                            "options": ["À mão livre", "Rigoroso", "De observação"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Desenhar aquilo que se tem à frente é desenho:",
                            "options": ["De observação", "Livre", "De tema dado"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quando o professor diz o assunto, o desenho é:",
                            "options": [
                                "Com tema dado",
                                "Livre",
                                "De observação",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # 2: A cor  (livro, pp. 16-26) -- as perguntas que MOSTRAM a cor
        # ---------------------------------------------------------------
        {
            "id": "u2",
            "titulo": "A cor",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "As cores primárias",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As cores primárias são aquelas que:",
                            "options": [
                                "Não resultam de nenhuma mistura",
                                "Se fazem com branco",
                                "São as mais bonitas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas é uma cor primária?",
                            "options": ["Azul", "Verde", "Laranja"],
                            "cores": {"opcoes": [AZUL, VERDE, LARANJA]},
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas NÃO é uma cor primária?",
                            "options": ["Violeta", "Amarelo", "Vermelho"],
                            "cores": {"opcoes": [VIOLETA, AMARELO, VERMELHO]},
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Quantas são as cores primárias?",
                            "a": "3",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Misturar tintas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Que cor sai de misturar amarelo com azul?",
                            "cores": {
                                "mistura": [AMARELO, AZUL],
                                "opcoes": [VERDE, LARANJA, VIOLETA],
                            },
                            "options": ["Verde", "Laranja", "Violeta"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Que cor sai de misturar amarelo com vermelho?",
                            "cores": {
                                "mistura": [AMARELO, VERMELHO],
                                "opcoes": [LARANJA, VERDE, VIOLETA],
                            },
                            "options": ["Laranja", "Verde", "Violeta"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Que cor sai de misturar vermelho com azul?",
                            "cores": {
                                "mistura": [VERMELHO, AZUL],
                                "opcoes": [VIOLETA, VERDE, LARANJA],
                            },
                            "options": ["Violeta", "Verde", "Laranja"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As cores que saem da mistura de duas primárias chamam-se:",
                            "options": ["Secundárias", "Primárias", "Neutras"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada mistura à cor que dela sai.",
                            "pairs": [
                                ["Amarelo e azul", "Verde"],
                                ["Vermelho e azul", "Violeta"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Tons e cores neutras",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Para clarear o tom de uma cor juntamos:",
                            "options": ["Branco", "Preto", "Água"],
                            "cores": {"opcoes": [BRANCO, PRETO, AZUL]},
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para escurecer uma cor juntamos:",
                            "options": ["Preto", "Branco", "Amarelo"],
                            "cores": {"opcoes": [PRETO, BRANCO, AMARELO]},
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Que cor sai de misturar preto com branco?",
                            "cores": {
                                "mistura": [PRETO, BRANCO],
                                "opcoes": [CINZENTO, VERDE, LARANJA],
                            },
                            "options": ["Cinzento", "Verde", "Laranja"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O preto e o branco chamam-se cores:",
                            "options": ["Neutras", "Primárias", "Secundárias"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # 3: Pintura  (livro, pp. 15-25)
        # ---------------------------------------------------------------
        {
            "id": "u3",
            "titulo": "Pintura",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Técnicas de pintar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A aguarela pinta-se com tinta misturada com:",
                            "options": ["Água", "Cera", "Cola"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas técnicas usa lápis?",
                            "options": [
                                "Lápis de cera",
                                "Guache",
                                "Aguarela",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Depois de pintar com pincel, o pincel deve ser:",
                            "options": [
                                "Lavado e guardado a secar",
                                "Guardado com tinta",
                                "Deitado fora",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As tintas artesanais fazem-se:",
                            "options": [
                                "Com materiais que há na comunidade",
                                "Só na fábrica",
                                "Só com água",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # 4: Impressao e estampagem  (livro, pp. 29-35)
        # ---------------------------------------------------------------
        {
            "id": "u4",
            "titulo": "Impressão e estampagem",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Imprimir e estampar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Na impressão digital, a marca é feita com:",
                            "options": ["O dedo", "A tesoura", "A régua"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um carimbo serve para:",
                            "options": [
                                "Repetir o mesmo desenho muitas vezes",
                                "Cortar o papel",
                                "Colar duas folhas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Estampar é passar um desenho:",
                            "options": [
                                "De uma superfície para outra",
                                "Do papel para a cabeça",
                                "De uma cor para outra",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de estampar, o que se põe por baixo do papel?",
                            "options": [
                                "Uma protecção, para não sujar a mesa",
                                "Mais papel branco",
                                "Nada",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # 5: Recorte, colagem e dobragem  (livro, pp. 35-45)
        # ---------------------------------------------------------------
        {
            "id": "u5",
            "titulo": "Recorte, colagem e dobragem",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Trabalhar o papel",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Ao passar a tesoura a um colega, entrega-se:",
                            "options": [
                                "Com as pontas viradas para mim",
                                "Com as pontas viradas para ele",
                                "Atirando-a",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na dobragem, o papel é:",
                            "options": [
                                "Dobrado, sem se cortar",
                                "Cortado em tiras",
                                "Molhado primeiro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Picotar é fazer no papel:",
                            "options": [
                                "Muitos furos pequenos seguidos",
                                "Um corte só",
                                "Uma dobra",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa colagem, a cola põe-se:",
                            "options": [
                                "Pouca e bem espalhada",
                                "Muita, no meio",
                                "Só nos cantos, aos montes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada técnica ao que se faz com o papel.",
                            "pairs": [
                                ["Recorte", "Cortar"],
                                ["Dobragem", "Dobrar"],
                            ],
                        },
                    ],
                },
            ],
        },
    ],
}


def main() -> int:
    gravar = "--gravar" in sys.argv
    dados = audio.carregar_content()
    ids = [c["id"] for c in dados["cursos"]]

    if CURSO["id"] in ids:
        print(f"o curso {CURSO['id']} ja esta no content.json", file=sys.stderr)
        return 1

    niveis = sum(len(u["niveis"]) for u in CURSO["units"])
    perguntas = sum(len(n["questoes"])
                    for u in CURSO["units"] for n in u["niveis"])
    com_cor = sum(1 for u in CURSO["units"] for n in u["niveis"]
                  for q in n["questoes"] if "cores" in q)
    print(f"{CURSO['disciplina']} da {CURSO['classe']}")
    print(f"  {len(CURSO['units'])} unidades, {niveis} niveis, "
          f"{perguntas} perguntas ({com_cor} mostram cor)")
    for u in CURSO["units"]:
        print(f"   {u['id']}  {u['titulo']}")
        for n in u["niveis"]:
            marcas = "".join("c" if "cores" in q else "." for q in n["questoes"])
            print(f"       {n['id']}  {n['titulo']:<26}"
                  f"{len(n['questoes'])}q  [{marcas}]")

    if not gravar:
        print("\n(so leitura -- corre com --gravar)")
        return 0

    manifesto = audio.ler_manifesto()
    feitos = 0
    for u in CURSO["units"]:
        for n in u["niveis"]:
            for q in n["questoes"]:
                ficheiro = audio.nome_do_ficheiro(q["q"])
                q["audio"] = ficheiro
                if (audio.AUDIO / ficheiro).exists() and \
                        manifesto.get(ficheiro) == audio.sha(audio.dito(q["q"])):
                    continue
                if not audio.gravar(q["q"], ficheiro, manifesto):
                    print(f"FALHOU o audio de {q['q'][:50]}", file=sys.stderr)
                    audio.escrever_manifesto(manifesto)
                    return 1
                feitos += 1
                print(f"   {(audio.AUDIO / ficheiro).stat().st_size:>6} bytes"
                      f"  {ficheiro}")

    # A seguir ao cs-6c: a Educacao Visual e a quinta disciplina e vem no
    # fim, como no plano de estudos.
    onde = ids.index("cs-6c") + 1
    dados["cursos"].insert(onde, CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta ao tools/materia_texto.py e corre "
          "python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
