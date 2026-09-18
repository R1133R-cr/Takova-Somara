# -*- coding: utf-8 -*-
"""O curso de Educacao Visual da 8a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Educacao Visual -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024,
     8a classe, pp. 23-32. Guardado em Documents\\planos da 5a classe\\
     Livros\\Programas INDE 1o Ciclo\\educacao-visual.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As sete unidades tematicas, pela ordem do programa
--------------------------------------------------
    1  Arte Universal             pintura, escultura, arquitectura; Da
                                  Vinci, Miguel Angelo, Picasso; leitura
                                  de obras
    2  Comunicacao Visual         indicios e pictogramas; cartaz; banda
                                  desenhada
    3  Estudo da Forma            forma-funcao e malha; cor; textura
    4  Desenho Geometrico         espirais, oval e ovulo; arcos
    5  Projeccoes Ortogonais      planos e vistas; solidos; 3a vista
    6  Formas em Axonometria      isometrica, dimetrica, cavaleira
    7  Cotagem das Formas         esboco cotado, desenho cotado

Sete unidades, treze aulas.

O que se pergunta
-----------------
Educacao Visual e desenhar, e uma app de perguntas nao desenha. O que
se pergunta e o saber que o desenho precisa: que arco e qual, quantos
centros tem a espiral, que vista se ve de cima, que cor sai da mistura.
E o mesmo criterio da 7a.

Correr a partir de somara-flutter/:
    python tools/conteudo_ev8c.py            # so mostra
    python tools/conteudo_ev8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Educação Visual — Ensino "
    "Secundário, 1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, 8ª "
    "classe, pp. 23-32. As sete unidades temáticas e os conteúdos são do "
    "programa; os exercícios foram escritos a partir deles, porque um "
    "programa de ensino não traz exercícios e não há livro do aluno da 8ª "
    "classe publicado."
)

CURSO = {
    "id": "ev-8c",
    "disciplina": "Educação Visual",
    "classe": "8ª classe",
    "tag": "EV",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # 1  Arte Universal
        # ================================================================
        {
            "id": "u1",
            "titulo": "Arte universal",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Pintura, escultura e arquitectura",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada obra à forma de expressão "
                                 "artística.",
                            "pairs": [
                                ["Um quadro a óleo", "Pintura"],
                                ["Uma estátua de mármore", "Escultura"],
                                ["Uma catedral", "Arquitectura"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Quem pintou a Mona Lisa?",
                            "options": [
                                "Leonardo da Vinci",
                                "Pablo Picasso",
                                "Miguel Ângelo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quem esculpiu o David e pintou o tecto "
                                 "da Capela Sistina?",
                            "options": [
                                "Miguel Ângelo",
                                "Leonardo da Vinci",
                                "Pablo Picasso",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Pablo Picasso é conhecido sobretudo pelo:",
                            "options": [
                                "Cubismo, que parte as figuras em formas "
                                "geométricas",
                                "Retrato realista",
                                "Desenho de catedrais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Para ler uma obra de arte, liga cada "
                                 "elemento à pergunta que ele responde.",
                            "pairs": [
                                ["Tipo de expressão", "É pintura, escultura ou arquitectura?"],
                                ["Técnica e materiais", "Foi feita com quê?"],
                                ["Tema", "De que fala?"],
                            ],
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 2  Comunicacao Visual
        # ================================================================
        {
            "id": "u2",
            "titulo": "Comunicação visual",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Indícios e pictogramas",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada código visual ao seu tipo.",
                            "pairs": [
                                ["Fumo ao longe: há fogo", "Indício"],
                                ["Boneco numa porta: casa de banho", "Pictograma"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um pictograma é:",
                            "options": [
                                "Um desenho simples que todos entendem sem "
                                "ler",
                                "Um texto longo",
                                "Uma fotografia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Pegadas frescas na areia são:",
                            "options": [
                                "Um indício de que alguém passou",
                                "Um pictograma",
                                "Um cartaz",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Nos aeroportos e hospitais usam-se "
                                 "pictogramas porque:",
                            "options": [
                                "Entendem-se em qualquer língua",
                                "São mais bonitos",
                                "Ocupam mais espaço",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um bom pictograma é:",
                            "options": [
                                "Simples, claro e sem pormenores a mais",
                                "Cheio de pormenores",
                                "Escrito em letras pequenas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O cartaz e a banda desenhada",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um cartaz tem de se perceber:",
                            "options": [
                                "De longe e num relance",
                                "Só de perto e com tempo",
                                "Só com uma lupa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada etapa do cartaz à sua ordem.",
                            "pairs": [
                                ["Escolher o tema e a mensagem", "Primeiro"],
                                ["Fazer o esboço", "Depois"],
                                ["Desenhar e pintar o cartaz final", "Por fim"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada elemento da banda desenhada "
                                 "ao que ele é.",
                            "pairs": [
                                ["Vinheta", "Cada quadradinho da história"],
                                ["Balão", "Onde vai a fala"],
                                ["Onomatopeia", "O som escrito: pum, zás"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um cartaz sobre igualdade de género ou "
                                 "direitos das crianças trata de um:",
                            "options": [
                                "Tema transversal",
                                "Tema geométrico",
                                "Tema secreto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao cortar cartão com um x-acto deve-se:",
                            "options": [
                                "Cortar para fora do corpo, com a mão "
                                "livre longe da lâmina",
                                "Cortar para o corpo",
                                "Segurar a lâmina com os dedos",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 3  Estudo da Forma
        # ================================================================
        {
            "id": "u3",
            "titulo": "Estudo da forma",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Forma e função, e a malha",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Forma-função quer dizer que:",
                            "options": [
                                "A forma de um objecto depende do que ele "
                                "serve",
                                "A forma não interessa",
                                "Todos os objectos são redondos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada forma ao seu tipo.",
                            "pairs": [
                                ["Uma folha de árvore", "Natural"],
                                ["Um copo", "Artificial"],
                                ["Uma cabaça transformada em recipiente", "Mista"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A rede ou malha serve para:",
                            "options": [
                                "Ampliar ou reduzir um desenho sem o "
                                "deformar",
                                "Pintar mais depressa",
                                "Medir o peso do papel",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um desenho está numa malha de quadrados "
                                 "de 1 centímetro e quer-se copiá-lo numa "
                                 "malha de quadrados de 3 centímetros. "
                                 "Quantas vezes fica maior cada lado?",
                            "a": "3",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada elemento básico da comunicação "
                                 "gráfica ao que ele é.",
                            "pairs": [
                                ["Ponto", "A marca mais pequena"],
                                ["Linha", "Um ponto em movimento"],
                                ["Plano", "Uma superfície fechada por linhas"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A cor e o círculo cromático",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As cores primárias são:",
                            "options": [
                                "Amarelo, azul e vermelho",
                                "Verde, laranja e roxo",
                                "Preto, branco e cinzento",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada mistura à cor secundária que "
                                 "dá.",
                            "pairs": [
                                ["Amarelo com azul", "Verde"],
                                ["Amarelo com vermelho", "Laranja"],
                                ["Azul com vermelho", "Roxo"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Uma cor terciária obtém-se misturando:",
                            "options": [
                                "Uma primária com a secundária vizinha",
                                "Preto com branco",
                                "Duas cores iguais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No trânsito, o vermelho quer dizer "
                                 "parar. Isso mostra que a cor:",
                            "options": [
                                "Comunica: tem significado",
                                "Só serve para enfeitar",
                                "Não se vê de longe",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Com lápis de cor, uma cor secundária "
                                 "obtém-se:",
                            "options": [
                                "Pintando uma primária por cima da outra",
                                "Molhando o papel",
                                "Apagando com borracha",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A textura",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Textura é:",
                            "options": [
                                "O aspecto da superfície: lisa, rugosa, "
                                "áspera, macia",
                                "A cor da superfície",
                                "O tamanho do objecto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada textura ao seu tipo.",
                            "pairs": [
                                ["A casca de uma árvore", "Natural"],
                                ["Um tecido tecido à máquina", "Artificial"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Pôr um papel sobre uma moeda e esfregar "
                                 "com lápis para a textura aparecer "
                                 "chama-se:",
                            "options": ["Decalque", "Colagem", "Recorte"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada textura ao que se sente ao "
                                 "tocar.",
                            "pairs": [
                                ["Vidro", "Liso"],
                                ["Lixa", "Áspero"],
                                ["Algodão", "Macio"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Pontos, traços e riscos repetidos num "
                                 "desenho para imitar uma superfície são:",
                            "options": [
                                "Elementos gráficos texturais",
                                "Cores terciárias",
                                "Pictogramas",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 4  Desenho Geometrico
        # ================================================================
        {
            "id": "u4",
            "titulo": "Desenho geométrico",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Espirais, oval e óvulo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma espiral de dois centros desenha-se "
                                 "com:",
                            "options": [
                                "Semicircunferências alternadas a partir "
                                "de dois pontos",
                                "Uma só circunferência",
                                "Linhas rectas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Na espiral de dois centros, cada meia "
                                 "volta aumenta o raio de uma distância "
                                 "igual à que vai de um centro ao outro. Se "
                                 "os centros distam 1 centímetro e o "
                                 "primeiro raio é 1, quanto mede o quarto "
                                 "raio, em centímetros?",
                            "a": "4",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada figura à sua descrição.",
                            "pairs": [
                                ["Oval", "Dois eixos de simetria, como um ovo visto de lado"],
                                ["Óvulo", "Um só eixo, mais largo num lado, como o ovo"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Onde se vê uma espiral na natureza?",
                            "options": [
                                "Na concha do caracol",
                                "Numa folha de papel",
                                "Num tijolo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para traçar arcos de circunferência com "
                                 "rigor usa-se:",
                            "options": ["O compasso", "A régua", "O esquadro"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Os arcos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O arco romano, ou de volta inteira, é:",
                            "options": [
                                "Uma semicircunferência com o centro no "
                                "meio da abertura",
                                "Um arco em bico",
                                "Uma linha recta",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada arco à sua forma.",
                            "pairs": [
                                ["Ogiva", "Acaba em bico, como nas igrejas góticas"],
                                ["Árabe", "Ferradura: fecha por baixo da largura maior"],
                                ["Abatido", "Mais baixo que meia circunferência"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Um arco romano tem uma abertura de 60 "
                                 "centímetros. Qual é o raio do arco, em "
                                 "centímetros?",
                            "a": "30",
                        },
                        {
                            "t": "choice",
                            "q": "O arco contracurvado junta:",
                            "options": [
                                "Curvas para um lado e curvas para o outro",
                                "Só linhas rectas",
                                "Uma circunferência inteira",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Nas portas e janelas dos edifícios "
                                 "antigos de Moçambique vêem-se arcos. "
                                 "Isso mostra que o desenho geométrico:",
                            "options": [
                                "Está na arquitectura à nossa volta",
                                "Só existe no papel",
                                "Não se usa há muito tempo",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 5  Projeccoes Ortogonais
        # ================================================================
        {
            "id": "u5",
            "titulo": "Projecções ortogonais",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Planos e vistas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As projecções ortogonais servem para:",
                            "options": [
                                "Mostrar todas as faces de um objecto numa "
                                "só folha",
                                "Pintar o objecto",
                                "Medir o peso do objecto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada plano de projecção à vista que "
                                 "dá.",
                            "pairs": [
                                ["Plano horizontal", "Vista de cima"],
                                ["Plano frontal", "Vista de frente"],
                                ["Plano de perfil", "Vista de lado"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um cilindro em pé, visto de cima, é:",
                            "options": ["Um círculo", "Um rectângulo", "Um triângulo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O mesmo cilindro em pé, visto de "
                                 "frente, é:",
                            "options": ["Um rectângulo", "Um círculo", "Um quadrado"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Nas projecções ortogonais, as linhas de "
                                 "projecção são:",
                            "options": [
                                "Perpendiculares ao plano",
                                "Inclinadas ao plano",
                                "Curvas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Sólidos e a terceira vista",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma pirâmide quadrangular vista de cima "
                                 "é:",
                            "options": [
                                "Um quadrado com as diagonais",
                                "Um triângulo",
                                "Um círculo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A mesma pirâmide vista de frente é:",
                            "options": ["Um triângulo", "Um quadrado", "Um círculo"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada sólido à sua vista de cima.",
                            "pairs": [
                                ["Prisma triangular deitado", "Rectângulo"],
                                ["Cubo", "Quadrado"],
                                ["Cone em pé", "Círculo com um ponto no meio"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Para achar a terceira vista a partir de "
                                 "duas vistas dadas usa-se:",
                            "options": [
                                "O cubo envolvente e o rebatimento dos "
                                "planos",
                                "Uma balança",
                                "Um lápis de cor",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um molde de costura ou a planta de uma "
                                 "casa são exemplos de:",
                            "options": [
                                "Projecções usadas no trabalho",
                                "Pictogramas",
                                "Texturas",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 6  Formas em Axonometria
        # ================================================================
        {
            "id": "u6",
            "titulo": "Formas em axonometria",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Isométrica, dimétrica e cavaleira",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A axonometria serve para desenhar:",
                            "options": [
                                "Um objecto a três dimensões numa folha "
                                "plana",
                                "Só a vista de frente",
                                "A cor do objecto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de axonometria à sua "
                                 "característica.",
                            "pairs": [
                                ["Isométrica", "Os três eixos fazem 120 graus entre si"],
                                ["Dimétrica", "Dois eixos com a mesma escala, um diferente"],
                                ["Cavaleira", "A face da frente fica em verdadeira grandeza"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Na perspectiva isométrica, os três eixos "
                                 "fazem ângulos iguais entre si. Quantos "
                                 "graus tem cada ângulo?",
                            "a": "120",
                        },
                        {
                            "t": "choice",
                            "q": "Na perspectiva cavaleira, as medidas no "
                                 "eixo que foge para trás:",
                            "options": [
                                "Reduzem-se, em geral a metade",
                                "Duplicam",
                                "Ficam iguais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um cubo em isometria vê-se como:",
                            "options": [
                                "Um hexágono com três losangos iguais",
                                "Um quadrado",
                                "Um círculo",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 7  Cotagem das Formas
        # ================================================================
        {
            "id": "u7",
            "titulo": "Cotagem das formas",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Esboço cotado e desenho cotado",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Cotar um desenho é:",
                            "options": [
                                "Escrever nele as medidas reais do objecto",
                                "Pintá-lo",
                                "Assiná-lo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo ao que ele é.",
                            "pairs": [
                                ["Esboço cotado", "À mão levantada, com as medidas"],
                                ["Desenho cotado", "A rigor, com régua e compasso, com as medidas"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A cotagem é importante porque:",
                            "options": [
                                "Quem constrói o objecto sabe as medidas "
                                "certas",
                                "Fica mais bonito",
                                "Poupa papel",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma carteira de sala tem 120 centímetros "
                                 "de comprimento e 60 de largura no "
                                 "desenho cotado. Quantos centímetros tem "
                                 "o comprimento a mais do que a largura?",
                            "a": "60",
                        },
                        {
                            "t": "choice",
                            "q": "Transportar as medidas das projecções "
                                 "ortogonais cotadas para a axonometria "
                                 "serve para:",
                            "options": [
                                "Desenhar o sólido a três dimensões com as "
                                "medidas certas",
                                "Apagar as vistas",
                                "Mudar a cor do sólido",
                            ],
                            "a": 0,
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

    unidades = len(CURSO["units"])
    niveis = sum(len(u["niveis"]) for u in CURSO["units"])
    perguntas = sum(len(n["questoes"])
                    for u in CURSO["units"] for n in u["niveis"])
    print(f"{CURSO['disciplina']} da {CURSO['classe']}")
    print(f"  {unidades} unidades, {niveis} niveis, {perguntas} perguntas")
    for u in CURSO["units"]:
        print(f"   {u['id']}  {u['titulo']}")
        for n in u["niveis"]:
            tipos = sorted({q["t"] for q in n["questoes"]})
            print(f"       {n['id']}  {n['titulo']:<40}"
                  f"{len(n['questoes'])}q  {tipos}")

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

    # A seguir ao ultimo curso da 8a que ja la esteja.
    onde = max(i for i, c in enumerate(dados["cursos"])
               if c["classe"] == "8ª classe") + 1
    dados["cursos"].insert(onde, CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta as entradas ao tools/materia_texto.py "
          "e corre python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
