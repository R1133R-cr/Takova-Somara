# -*- coding: utf-8 -*-
"""O curso de Educacao Visual da 9a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Educacao Visual -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024,
     9a classe, pp. 34-42. Guardado em Documents\\planos da 5a classe\\
     Livros\\Programas INDE 1o Ciclo\\educacao-visual.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As sete unidades tematicas, pela ordem do programa
--------------------------------------------------
    1  Arte Mocambicana e Universal   escultura, pintura, arquitectura
                                      mocambicanas; arte medieval e
                                      contemporanea
    2  Comunicacao Visual             cartaz, banda desenhada e paineis;
                                      programas graficos
    3  Desenho Geometrico             as curvas conicas
    4  Projeccoes Ortogonais          formas planas e tridimensionais
    5  Formas em Axonometria          isometrica, dimetrica, cavaleira
    6  Perspectiva Visual             linha do horizonte e pontos de fuga
    7  Formas em Perspectiva          elementos; um e dois pontos de fuga
       Rigorosa

Sete unidades, dez aulas.

As siglas do desenho
--------------------
"PF", "LH", "PV" e as outras siglas da perspectiva a voz leria como
palavras. Nos enunciados escreve-se "ponto de fuga", "linha do
horizonte", "ponto de vista"; as siglas ficam nos pares.

Correr a partir de somara-flutter/:
    python tools/conteudo_ev9c.py            # so mostra
    python tools/conteudo_ev9c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Educação Visual — Ensino "
    "Secundário, 1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, 9ª "
    "classe, pp. 34-42. As sete unidades temáticas e os conteúdos são do "
    "programa; os exercícios foram escritos a partir deles, porque um "
    "programa de ensino não traz exercícios e não há livro do aluno da 9ª "
    "classe publicado."
)

CURSO = {
    "id": "ev-9c",
    "disciplina": "Educação Visual",
    "classe": "9ª classe",
    "tag": "EV",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # 1  Arte Mocambicana e Universal
        # ================================================================
        {
            "id": "u1",
            "titulo": "Arte moçambicana e universal",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A arte moçambicana",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada artista ou obra moçambicana à "
                                 "sua forma de expressão.",
                            "pairs": [
                                ["Malangatana", "Pintura"],
                                ["Alberto Chissano", "Escultura"],
                                ["Fortaleza da Ilha de Moçambique", "Arquitectura"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A escultura maconde, de Cabo Delgado, "
                                 "faz-se sobretudo em:",
                            "options": [
                                "Madeira de pau-preto",
                                "Barro cozido",
                                "Ferro fundido",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O grande painel pintado por Malangatana "
                                 "num muro de Maputo é:",
                            "options": ["Um mural", "Uma escultura", "Um cartaz"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Casa de Ferro, em Maputo, é famosa "
                                 "por:",
                            "options": [
                                "Ser toda feita de placas de ferro, vindas "
                                "da Europa",
                                "Ser de madeira",
                                "Estar debaixo de água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As manifestações artísticas da comunidade, "
                                 "como as máscaras e as esteiras, são:",
                            "options": [
                                "Arte, e parte da identidade cultural",
                                "Só objectos sem valor",
                                "Coisas importadas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A arte medieval e a contemporânea",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada período da arte à sua "
                                 "característica.",
                            "pairs": [
                                ["Medieval", "Temas religiosos, catedrais e vitrais"],
                                ["Contemporânea", "Novos materiais, abstracção e arte digital"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Os vitrais coloridos das catedrais "
                                 "góticas são da arte:",
                            "options": ["Medieval", "Contemporânea", "Pré-histórica"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma pintura que não representa nada de "
                                 "reconhecível, só formas e cores, é:",
                            "options": ["Abstracta", "Figurativa", "Um retrato"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na Idade Média, os livros eram "
                                 "decorados à mão com:",
                            "options": [
                                "Iluminuras",
                                "Fotografias",
                                "Pictogramas digitais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um artista contemporâneo pode fazer uma "
                                 "obra com:",
                            "options": [
                                "Latas, garrafas e outros materiais "
                                "reaproveitados",
                                "Só tinta a óleo",
                                "Só mármore",
                            ],
                            "a": 0,
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
                    "titulo": "Cartaz, banda desenhada e painel",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada etapa da banda desenhada à sua "
                                 "ordem.",
                            "pairs": [
                                ["Escrever a história e dividi-la em cenas", "Primeiro"],
                                ["Esboçar as vinhetas", "Depois"],
                                ["Passar a tinta, pintar e pôr os balões", "Por fim"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um painel colectivo é:",
                            "options": [
                                "Uma obra grande feita por vários alunos "
                                "juntos",
                                "Um desenho de um aluno só",
                                "Um livro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Num cartaz sobre os direitos das "
                                 "crianças, o texto deve ser:",
                            "options": [
                                "Curto, grande e legível de longe",
                                "Longo e em letra pequena",
                                "Escondido na imagem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um balão de pensamento, na banda "
                                 "desenhada, desenha-se:",
                            "options": [
                                "Como uma nuvem ligada por bolinhas",
                                "Com uma seta recta",
                                "Sem contorno",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um cartaz sobre segurança no trabalho "
                                 "numa oficina deve mostrar:",
                            "options": [
                                "Luvas, óculos e botas de protecção",
                                "Só o logótipo da empresa",
                                "Um poema",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Os programas gráficos",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada programa ao que se faz melhor "
                                 "com ele.",
                            "pairs": [
                                ["Photoshop", "Editar fotografias"],
                                ["CorelDraw e Illustrator", "Desenho vectorial e logótipos"],
                                ["Paint", "Desenhos simples no computador"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um programa como o Canva serve para:",
                            "options": [
                                "Fazer cartazes e convites com modelos "
                                "prontos",
                                "Escrever programas de computador",
                                "Calcular contas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma imagem vectorial, ao ser ampliada:",
                            "options": [
                                "Não perde qualidade",
                                "Fica aos quadradinhos",
                                "Muda de cor",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma fotografia ampliada demais fica aos "
                                 "quadradinhos porque é feita de:",
                            "options": ["Píxeis", "Vectores", "Linhas de cota"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de fazer um cartaz no computador "
                                 "convém:",
                            "options": [
                                "Fazer um esboço no papel",
                                "Imprimir logo",
                                "Escolher só as cores",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 3  Desenho Geometrico
        # ================================================================
        {
            "id": "u3",
            "titulo": "Desenho geométrico",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "As curvas cónicas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As curvas cónicas chamam-se assim "
                                 "porque:",
                            "options": [
                                "Obtêm-se cortando um cone por um plano",
                                "Têm a forma de um cone",
                                "Desenham-se com um cone",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada curva cónica a um objecto de "
                                 "uso comum.",
                            "pairs": [
                                ["Elipse", "A mesa oval e a órbita da Terra"],
                                ["Parábola", "A antena parabólica e o jacto de água"],
                                ["Hipérbole", "As torres de arrefecimento das centrais"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um círculo visto de lado, inclinado, "
                                 "parece:",
                            "options": ["Uma elipse", "Uma parábola", "Um triângulo"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma elipse tem dois focos. Quantos eixos "
                                 "de simetria tem?",
                            "a": "2",
                        },
                        {
                            "t": "choice",
                            "q": "Uma composição decorativa não "
                                 "figurativa:",
                            "options": [
                                "Usa só formas geométricas, sem "
                                "representar pessoas nem objectos",
                                "Representa uma pessoa",
                                "É uma fotografia",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 4  Projeccoes Ortogonais
        # ================================================================
        {
            "id": "u4",
            "titulo": "Projecções ortogonais",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Formas planas e tridimensionais",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Na 9ª classe, as projecções fazem-se "
                                 "sobre quantos planos de projecção?",
                            "a": "4",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada plano de projecção à vista que "
                                 "dá.",
                            "pairs": [
                                ["Plano horizontal", "Planta, a vista de cima"],
                                ["Plano frontal", "Alçado, a vista de frente"],
                                ["Plano lateral", "Vista de lado"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Uma forma tridimensional pode "
                                 "construir-se com:",
                            "options": [
                                "Cartão, esferovite, madeira ou barro",
                                "Só papel de desenho",
                                "Só lápis",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um cone deitado, visto de cima, é:",
                            "options": ["Um triângulo", "Um círculo", "Um quadrado"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para construir uma caixa a partir das "
                                 "suas projecções, primeiro desenha-se:",
                            "options": [
                                "A planificação: as faces abertas num "
                                "plano",
                                "A sombra",
                                "A perspectiva a dois pontos de fuga",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 5  Formas em Axonometria
        # ================================================================
        {
            "id": "u5",
            "titulo": "Formas em axonometria",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Da projecção à axonometria",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Para desenhar em isometria com mais "
                                 "facilidade usa-se:",
                            "options": [
                                "A malha reticulada de triângulos",
                                "Uma folha lisa",
                                "O transferidor só",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na perspectiva cavaleira, a face da "
                                 "frente desenha-se:",
                            "options": [
                                "Em verdadeira grandeza, sem deformar",
                                "Reduzida a metade",
                                "Inclinada a 120 graus",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Na cavaleira, a profundidade reduz-se a "
                                 "metade. Uma caixa com 10 centímetros de "
                                 "fundo desenha-se com quantos centímetros?",
                            "a": "5",
                        },
                        {
                            "t": "choice",
                            "q": "A partir das três vistas de um sólido "
                                 "em projecção ortogonal, pode-se:",
                            "options": [
                                "Desenhá-lo em axonometria, e vice-versa",
                                "Saber o seu peso",
                                "Saber a sua cor",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Nas perspectivas axonométricas "
                                 "desenhadas a rigor, as cotas:",
                            "options": [
                                "Inscrevem-se com as medidas reais",
                                "Nunca se põem",
                                "Escrevem-se reduzidas",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 6  Perspectiva Visual
        # ================================================================
        {
            "id": "u6",
            "titulo": "Perspectiva visual",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A linha do horizonte e os pontos de fuga",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Numa estrada comprida, as bermas "
                                 "parecem juntar-se ao longe. Esse ponto "
                                 "chama-se:",
                            "options": ["Ponto de fuga", "Ponto de vista", "Linha de terra"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A linha do horizonte fica sempre:",
                            "options": [
                                "À altura dos olhos de quem observa",
                                "No fundo da folha",
                                "No cimo da folha",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na perspectiva visual, um objecto mais "
                                 "longe parece:",
                            "options": ["Mais pequeno", "Maior", "Igual"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada posição do objecto à "
                                 "perspectiva que se usa.",
                            "pairs": [
                                ["Uma face virada de frente para nós", "Um ponto de fuga"],
                                ["Uma aresta virada para nós, de canto", "Dois pontos de fuga"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um objecto desenhado acima da linha do "
                                 "horizonte vê-se:",
                            "options": [
                                "Por baixo",
                                "Por cima",
                                "Só de frente",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 7  Formas em Perspectiva Rigorosa
        # ================================================================
        {
            "id": "u7",
            "titulo": "Perspectiva rigorosa",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Os elementos da perspectiva rigorosa",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada elemento da perspectiva "
                                 "rigorosa à sua sigla.",
                            "pairs": [
                                ["Ponto de vista", "PV"],
                                ["Linha do horizonte", "LH"],
                                ["Ponto de fuga", "PF"],
                                ["Linha de terra", "LT"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O ponto de vista é:",
                            "options": [
                                "O lugar do olho de quem observa",
                                "O centro do objecto",
                                "O canto da folha",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O plano do quadro é:",
                            "options": [
                                "O plano transparente onde a imagem se "
                                "desenha, entre o olho e o objecto",
                                "O chão",
                                "O céu",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A linha de terra é onde se encontram:",
                            "options": [
                                "O plano de terra e o plano do quadro",
                                "Dois pontos de fuga",
                                "O céu e o mar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A perspectiva rigorosa usa-se:",
                            "options": [
                                "Na arquitectura, no desenho de casas e "
                                "cidades",
                                "Só na música",
                                "Só no desporto",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A um e a dois pontos de fuga",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A perspectiva central, ou cónica, tem:",
                            "options": [
                                "Um ponto de fuga",
                                "Dois pontos de fuga",
                                "Nenhum ponto de fuga",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um cubo desenhado de canto, com uma "
                                 "aresta virada para nós, precisa de "
                                 "quantos pontos de fuga?",
                            "a": "2",
                        },
                        {
                            "t": "choice",
                            "q": "Na perspectiva a um ponto de fuga, as "
                                 "linhas de profundidade:",
                            "options": [
                                "Convergem todas no ponto de fuga",
                                "Ficam paralelas",
                                "São verticais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um círculo em perspectiva rigorosa, "
                                 "deitado no chão, desenha-se como:",
                            "options": ["Uma elipse", "Um quadrado", "Uma recta"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Se se muda a posição do ponto de vista, "
                                 "o desenho do objecto:",
                            "options": [
                                "Muda: vê-se de outro ângulo",
                                "Fica igual",
                                "Desaparece",
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

    # A seguir ao ultimo curso da 9a que ja la esteja.
    onde = max(i for i, c in enumerate(dados["cursos"])
               if c["classe"] == "9ª classe") + 1
    dados["cursos"].insert(onde, CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta as entradas ao tools/materia_texto.py "
          "e corre python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
