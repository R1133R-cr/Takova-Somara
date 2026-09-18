# -*- coding: utf-8 -*-
"""O curso de Quimica da 8a classe -- a primeira Quimica da app.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Quimica -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, pp. 8-12 (visao
     geral dos conteudos) e pp. 17-26 (plano tematico da 8a classe).
     Guardado em Documents\\planos da 5a classe\\Livros\\Programas INDE 1o
     Ciclo\\quimica.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

A unidade que o PDF perdeu
--------------------------
O indice do programa lista quatro unidades para a 8a, mas a terceira,
"Estrutura da materia e reaccoes quimicas", aparece la com um "Error!
Bookmark not defined" e o plano tematico salta da unidade II (p. 20) para
a IV (p. 22). A unidade existe -- esta inteira na visao geral dos
conteudos, p. 10-11, com os seus quatro temas (estrutura da materia,
massa atomica e molecular, reaccoes quimicas, calculos quimicos). E dai
que se tirou. E o que ha; e o que se usou.

As quatro unidades, pela ordem do programa
------------------------------------------
    I    Introducao ao estudo da Quimica  objecto, alquimia, laboratorio
    II   Materia e suas propriedades      materia; substancia; misturas
    III  Estrutura da materia e reaccoes  atomo; moleculas e formulas;
         quimicas                         massas; reaccoes; calculos
    IV   Agua                             agua; solucoes; hidrogenio e
                                          oxigenio; ar, ozono e oxidacao

Quatro unidades, catorze aulas.

As formulas ficam nas opcoes
----------------------------
"H2O" a voz le "agá dois ó", e "CO2" pior. Nos enunciados escreve-se
"agua" e "dioxido de carbono"; a formula, quando faz falta, fica nas
opcoes, que sao para ler e nao para ouvir. As contas (massa molecular,
concentracao, moles) foram escolhidas para dar numeros inteiros.

Correr a partir de somara-flutter/:
    python tools/conteudo_qui8c.py            # so mostra
    python tools/conteudo_qui8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Química — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, pp. 8-12 e 17-26. "
    "As quatro unidades e os conteúdos são do programa (a unidade III, que "
    "o plano temático do PDF perdeu, vem da visão geral dos conteúdos); os "
    "exercícios foram escritos a partir deles, porque um programa de ensino "
    "não traz exercícios e não há livro do aluno da 8ª classe publicado."
)

CURSO = {
    "id": "qui-8c",
    "disciplina": "Química",
    "classe": "8ª classe",
    "tag": "QUI",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # I  Introducao ao estudo da Quimica
        # ================================================================
        {
            "id": "u1",
            "titulo": "Introdução ao estudo da Química",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A Química e a sua história",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Química é a ciência que estuda:",
                            "options": [
                                "As substâncias e as suas transformações",
                                "Os astros e o céu",
                                "As rochas e os rios",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes da Química moderna, os que "
                                 "procuravam transformar metais em ouro "
                                 "praticavam a:",
                            "options": ["Alquimia", "Biologia", "Geometria"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada uso da Química ao seu campo.",
                            "pairs": [
                                ["Adubos e pesticidas", "Agricultura"],
                                ["Medicamentos", "Medicina"],
                                ["Sabões e detergentes", "Indústria"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "No ensino primário, a Química vinha "
                                 "misturada com a Biologia, a Física e a "
                                 "Geografia numa disciplina chamada:",
                            "options": [
                                "Ciências Naturais",
                                "Ciências Sociais",
                                "Educação Visual",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ferver água para a tornar potável e "
                                 "conservar alimentos com sal são "
                                 "exemplos da Química:",
                            "options": ["Em casa", "No espaço", "No desporto"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Segurança no laboratório e o relatório",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "No laboratório, uma substância "
                                 "desconhecida:",
                            "options": [
                                "Nunca se prova nem se cheira de perto",
                                "Prova-se para saber o que é",
                                "Cheira-se com o nariz encostado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Durante uma experiência, o cabelo "
                                 "comprido deve estar:",
                            "options": ["Preso", "Solto", "Molhado"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Se um ácido cai na pele, a primeira "
                                 "coisa a fazer é:",
                            "options": [
                                "Lavar com muita água",
                                "Esfregar com um pano seco",
                                "Deitar outro ácido por cima",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada parte do relatório de uma "
                                 "experiência ao que ela diz.",
                            "pairs": [
                                ["Objectivo", "O que se queria saber"],
                                ["Procedimento", "O que se fez, passo a passo"],
                                ["Conclusão", "O que se ficou a saber"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Mudança de cor, libertação de um gás e "
                                 "efervescência são sinais de:",
                            "options": [
                                "Uma reacção química",
                                "Uma mudança de estado",
                                "Uma mistura",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # II  Materia e suas propriedades
        # ================================================================
        {
            "id": "u2",
            "titulo": "Matéria e suas propriedades",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A matéria e os estados",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Matéria é tudo o que:",
                            "options": [
                                "Tem massa e ocupa um lugar no espaço",
                                "Se pode ver",
                                "É duro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada propriedade geral da matéria "
                                 "ao seu exemplo.",
                            "pairs": [
                                ["Divisibilidade", "Partir um pão em fatias"],
                                ["Compressibilidade", "Apertar o ar numa bomba"],
                                ["Elasticidade", "Esticar um elástico"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada mudança de estado ao seu "
                                 "nome.",
                            "pairs": [
                                ["Sólido a líquido", "Fusão"],
                                ["Líquido a gás", "Vaporização"],
                                ["Gás a líquido", "Condensação"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A matéria classifica-se em:",
                            "options": [
                                "Substâncias e misturas",
                                "Sólidos e líquidos",
                                "Metais e plásticos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Dois corpos não podem ocupar o mesmo "
                                 "lugar ao mesmo tempo. Essa propriedade "
                                 "chama-se:",
                            "options": [
                                "Impenetrabilidade",
                                "Elasticidade",
                                "Divisibilidade",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Substâncias e propriedades específicas",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada propriedade específica ao que "
                                 "ela diz.",
                            "pairs": [
                                ["Ponto de fusão", "A temperatura a que derrete"],
                                ["Ponto de ebulição", "A temperatura a que ferve"],
                                ["Densidade", "A massa de cada volume"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Ao nível do mar, a que temperatura, em "
                                 "graus Celsius, ferve a água pura?",
                            "a": "100",
                        },
                        {
                            "t": "choice",
                            "q": "Uma substância elementar é feita de:",
                            "options": [
                                "Um só elemento químico",
                                "Dois ou mais elementos",
                                "Água e sal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada substância à sua classe.",
                            "pairs": [
                                ["Oxigénio", "Elementar"],
                                ["Ferro", "Elementar"],
                                ["Água", "Composta"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Um pedaço de ferro tem 40 gramas e "
                                 "ocupa 5 centímetros cúbicos. Qual é a "
                                 "densidade, em gramas por centímetro "
                                 "cúbico?",
                            "a": "8",
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Misturas e a sua separação",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada mistura ao seu tipo.",
                            "pairs": [
                                ["Água com açúcar dissolvido", "Homogénea"],
                                ["Água com areia", "Heterogénea"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O sal de cozinha obtém-se da água do "
                                 "mar por:",
                            "options": [
                                "Evaporação e cristalização",
                                "Filtração",
                                "Separação magnética",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada mistura ao método que a "
                                 "separa.",
                            "pairs": [
                                ["Areia e limalha de ferro", "Separação magnética"],
                                ["Água e areia", "Filtração"],
                                ["Feijão e pedrinhas", "Catação"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A destilação simples separa a água do "
                                 "álcool porque eles têm:",
                            "options": [
                                "Pontos de ebulição diferentes",
                                "Cores diferentes",
                                "O mesmo tamanho",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Deixar a água barrenta em repouso até a "
                                 "terra assentar e depois vazar a água "
                                 "limpa chama-se:",
                            "options": ["Decantação", "Peneiração", "Cromatografia"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # III  Estrutura da materia e reaccoes quimicas
        # ================================================================
        {
            "id": "u3",
            "titulo": "Estrutura da matéria e reacções químicas",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O átomo e os elementos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O número atómico de um elemento é o "
                                 "número de:",
                            "options": [
                                "Protões no núcleo",
                                "Átomos numa molécula",
                                "Letras no símbolo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um átomo tem 6 protões e 6 neutrões. "
                                 "Qual é o seu número de massa?",
                            "a": "12",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada elemento ao seu símbolo.",
                            "pairs": [
                                ["Hidrogénio", "H"],
                                ["Oxigénio", "O"],
                                ["Carbono", "C"],
                                ["Ferro", "Fe"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada elemento à sua classe.",
                            "pairs": [
                                ["Cobre", "Metal"],
                                ["Enxofre", "Não metal"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Os metais, em geral:",
                            "options": [
                                "Têm brilho e conduzem a corrente e o calor",
                                "São gases à temperatura ambiente",
                                "Não conduzem nada",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Moléculas, fórmulas e valência",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Uma molécula de água tem 2 átomos de "
                                 "hidrogénio e 1 de oxigénio. Quantos "
                                 "átomos tem ao todo?",
                            "a": "3",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada substância à sua fórmula.",
                            "pairs": [
                                ["Água", "H₂O"],
                                ["Dióxido de carbono", "CO₂"],
                                ["Oxigénio", "O₂"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A valência de um elemento diz:",
                            "options": [
                                "Quantas ligações o átomo faz",
                                "Quanto pesa o átomo",
                                "Que cor tem a substância",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O hidrogénio tem valência 1 e o oxigénio "
                                 "valência 2. Por isso a água leva:",
                            "options": [
                                "2 hidrogénios para 1 oxigénio",
                                "1 hidrogénio para 2 oxigénios",
                                "3 hidrogénios para 1 oxigénio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada molécula ao seu tipo.",
                            "pairs": [
                                ["Oxigénio, dois átomos iguais", "Substância elementar"],
                                ["Água, átomos diferentes", "Substância composta"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Massa atómica e molecular",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A massa atómica relativa de um elemento "
                                 "compara a massa do seu átomo com:",
                            "options": [
                                "Uma unidade de massa atómica",
                                "Um grama",
                                "Um quilograma",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "A massa atómica do hidrogénio é 1 e a do "
                                 "oxigénio é 16. Qual é a massa molecular "
                                 "da água?",
                            "a": "18",
                        },
                        {
                            "t": "input",
                            "q": "A massa atómica do carbono é 12 e a do "
                                 "oxigénio é 16. Qual é a massa molecular "
                                 "do dióxido de carbono?",
                            "a": "44",
                        },
                        {
                            "t": "input",
                            "q": "A massa atómica do oxigénio é 16. Qual é "
                                 "a massa molecular do oxigénio, que tem "
                                 "dois átomos?",
                            "a": "32",
                        },
                        {
                            "t": "input",
                            "q": "O sal de cozinha tem um átomo de sódio, "
                                 "de massa 23, e um de cloro, de massa "
                                 "35. Qual é a sua massa molecular?",
                            "a": "58",
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Reacções e equações químicas",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada fenómeno ao seu tipo: físico ou químico.",
                            "pairs": [
                                ["Água a ferver", "Fenómeno físico"],
                                ["Ferro a enferrujar", "Fenómeno químico"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A lei de Lavoisier diz que, numa reacção "
                                 "química, a massa:",
                            "options": [
                                "Dos produtos é igual à dos reagentes",
                                "Dos produtos é sempre maior",
                                "Desaparece",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Numa reacção, 4 gramas de hidrogénio "
                                 "juntam-se a 32 gramas de oxigénio. "
                                 "Quantos gramas de água se formam?",
                            "a": "36",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada reacção ao seu tipo.",
                            "pairs": [
                                ["Duas substâncias dão uma", "Combinação"],
                                ["Uma substância dá duas", "Decomposição"],
                                ["Liberta calor", "Exotérmica"],
                                ["Absorve calor", "Endotérmica"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Para acertar a equação do hidrogénio "
                                 "com o oxigénio a dar água, precisam-se "
                                 "2 moléculas de hidrogénio e 1 de "
                                 "oxigénio. Quantas moléculas de água se "
                                 "formam?",
                            "a": "2",
                        },
                    ],
                },
                {
                    "id": "n5",
                    "titulo": "Cálculos químicos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma mole de qualquer substância tem "
                                 "sempre:",
                            "options": [
                                "O mesmo número de partículas: o número "
                                "de Avogadro",
                                "A mesma massa em gramas",
                                "Um litro de volume",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "A massa molar da água é 18 gramas por "
                                 "mole. Quantos gramas pesam 2 moles de "
                                 "água?",
                            "a": "36",
                        },
                        {
                            "t": "input",
                            "q": "A massa molar do dióxido de carbono é 44 "
                                 "gramas por mole. Quantas moles há em 88 "
                                 "gramas?",
                            "a": "2",
                        },
                        {
                            "t": "input",
                            "q": "O metano tem 12 gramas de carbono em "
                                 "cada 16 gramas. Qual é a percentagem de "
                                 "carbono?",
                            "a": "75",
                        },
                        {
                            "t": "input",
                            "q": "Se 2 gramas de hidrogénio dão 18 gramas "
                                 "de água, quantos gramas de água dão 6 "
                                 "gramas de hidrogénio?",
                            "a": "54",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # IV  Agua
        # ================================================================
        {
            "id": "u4",
            "titulo": "Água",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A água e a sua qualidade",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A água potável é a que:",
                            "options": [
                                "É própria para beber: sem cor, sem cheiro "
                                "e sem micróbios",
                                "Tem muito sal",
                                "Vem de qualquer rio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de água ao que ela é.",
                            "pairs": [
                                ["Salobra", "Sais a mais, não se bebe"],
                                ["Mineral", "Poucos sais, brota de nascente"],
                                ["Termal", "Brota quente da nascente"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A cólera e a febre tifóide apanham-se "
                                 "por:",
                            "options": [
                                "Água contaminada com micróbios",
                                "Ar frio",
                                "Sol a mais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada método de tratamento da água "
                                 "ao que ele faz.",
                            "pairs": [
                                ["Fervura", "Mata os micróbios com calor"],
                                ["Cloragem", "Mata os micróbios com cloro"],
                                ["Filtração", "Tira a sujidade sólida"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Fechar a torneira enquanto se lava os "
                                 "dentes e reparar fugas são formas de:",
                            "options": [
                                "Conservar a água",
                                "Poluir a água",
                                "Tratar a água",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Soluções e concentração",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Na água com açúcar, liga cada coisa ao "
                                 "seu nome.",
                            "pairs": [
                                ["A água", "Solvente"],
                                ["O açúcar", "Soluto"],
                                ["A água com açúcar", "Solução"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Diluir uma solução é:",
                            "options": [
                                "Juntar-lhe mais solvente",
                                "Juntar-lhe mais soluto",
                                "Aquecê-la",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma solução em que já não se dissolve "
                                 "mais soluto chama-se:",
                            "options": ["Saturada", "Diluída", "Homogénea"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Dissolvem-se 20 gramas de sal em 80 "
                                 "gramas de água. Qual é a concentração "
                                 "percentual da solução?",
                            "a": "20",
                        },
                        {
                            "t": "input",
                            "q": "Dissolvem-se 3 moles de soluto em 1 "
                                 "litro de solução. Qual é a concentração "
                                 "molar, em moles por litro?",
                            "a": "3",
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Hidrogénio e oxigénio",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O hidrogénio é:",
                            "options": [
                                "O gás mais leve que existe",
                                "O gás mais pesado que existe",
                                "Um metal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada cientista à sua descoberta.",
                            "pairs": [
                                ["Cavendish", "Hidrogénio"],
                                ["Priestley", "Oxigénio"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "No laboratório, o oxigénio obtém-se "
                                 "decompondo o peróxido de hidrogénio com "
                                 "um catalisador. Um catalisador é uma "
                                 "substância que:",
                            "options": [
                                "Altera a rapidez de uma reacção",
                                "Se gasta toda na reacção",
                                "Apaga a reacção",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O hidrogénio a arder no oxigénio dá:",
                            "options": ["Água", "Sal", "Ferro"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada gás a uma aplicação.",
                            "pairs": [
                                ["Oxigénio", "Balões de hospital para respirar"],
                                ["Hidrogénio", "Combustível de foguetões"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Ar, ozono e oxidação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O gás que há em maior quantidade no ar "
                                 "é o:",
                            "options": ["Azoto", "Oxigénio", "Dióxido de carbono"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A camada de ozono protege a Terra:",
                            "options": [
                                "Dos raios ultravioleta do Sol",
                                "Da chuva",
                                "Do vento",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada oxidação ao seu tipo.",
                            "pairs": [
                                ["Ferro a enferrujar", "Oxidação lenta"],
                                ["Lenha a arder", "Oxidação rápida"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Pintar o portão de ferro serve para:",
                            "options": [
                                "Evitar a corrosão, tirando-lhe o ar e a "
                                "humidade",
                                "O tornar mais pesado",
                                "O fazer arder melhor",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para haver combustão precisa-se de "
                                 "combustível, calor e:",
                            "options": [
                                "Comburente, que é o oxigénio",
                                "Água",
                                "Sal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Numa reacção, os reagentes têm 80 "
                                 "unidades de energia e os produtos 30. "
                                 "Quantas unidades de energia se "
                                 "libertaram?",
                            "a": "50",
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
