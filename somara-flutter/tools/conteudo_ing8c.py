# -*- coding: utf-8 -*-
"""O curso de Ingles da 8a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Lingua Inglesa -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024,
     Grade 8, pp. 31-46. Guardado em Documents\\planos da 5a classe\\
     Livros\\Programas INDE 1o Ciclo\\ingles.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As nove unidades do Grade 8, pela ordem do programa
---------------------------------------------------
    1  English in Mozambique             linguas, paises vizinhos;
                                         presente e passado simples
    2  Modern and traditional medicine   saude; futuro; condicionais
    3  Customs and traditions            tradicoes; sequencia; should/must
    4  Farming                           campo; artigos; passiva
    5  Shopping                          compras; how much/many; comparativo
    6  Tourism and wildlife              parques; superlativo; reflexivos
    7  Managing our planet               ambiente; relativos; 2a condicional
    8  Health and Fitness                doencas e nutricao; plurais
    9  Occupations and professions       profissoes; question tags

Nove unidades, catorze aulas. Cada unidade e uma unidade da app, com a
gramatica que o programa lhe da.

O ingles fica nas opcoes
------------------------
A voz da app e portuguesa e nao sabe dizer ingles. Como na 7a, os
enunciados sao todos em portugues -- "Como se diz «...» em ingles?",
"«...» escreve-se:" -- e o ingles aparece so nas opcoes e nos pares,
que se leem e nao se ouvem.

Correr a partir de somara-flutter/:
    python tools/conteudo_ing8c.py            # so mostra
    python tools/conteudo_ing8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Língua Inglesa — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, Grade 8, pp. 31-46. "
    "As nove unidades, o vocabulário e a gramática são do programa; os "
    "exercícios foram escritos a partir deles, porque um programa de ensino "
    "não traz exercícios e não há livro do aluno da 8ª classe publicado. Os "
    "enunciados são em português e o inglês fica nas opções, porque a voz da "
    "app é portuguesa."
)

CURSO = {
    "id": "ing-8c",
    "disciplina": "Inglês",
    "classe": "8ª classe",
    "tag": "ING",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # 1  English in Mozambique
        # ================================================================
        {
            "id": "u1",
            "titulo": "O inglês em Moçambique",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Línguas e países vizinhos",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada país vizinho de Moçambique ao "
                                 "seu nome em inglês.",
                            "pairs": [
                                ["África do Sul", "South Africa"],
                                ["Zimbabué", "Zimbabwe"],
                                ["Zâmbia", "Zambia"],
                                ["Tanzânia", "Tanzania"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «eu falo "
                                 "português e inglês»?",
                            "options": [
                                "I speak Portuguese and English",
                                "I speaks Portuguese and English",
                                "I am speak Portuguese and English",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada língua ao seu nome em inglês.",
                            "pairs": [
                                ["Francês", "French"],
                                ["Espanhol", "Spanish"],
                                ["Mandarim", "Mandarin"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «nacionalidade» em inglês?",
                            "options": ["Nationality", "Nation", "National"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O inglês é importante para o turismo» "
                                 "escreve-se:",
                            "options": [
                                "English is important for tourism",
                                "English are important for tourism",
                                "English important is for tourism",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Presente e passado simples",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «ela "
                                 "trabalha num hotel»?",
                            "options": [
                                "She works in a hotel",
                                "She work in a hotel",
                                "She working in a hotel",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Nós visitámos a Tanzânia no ano "
                                 "passado» escreve-se:",
                            "options": [
                                "We visited Tanzania last year",
                                "We visit Tanzania last year",
                                "We visiting Tanzania last year",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Eu sei nadar, mas não sei conduzir» "
                                 "escreve-se:",
                            "options": [
                                "I can swim, but I can't drive",
                                "I can swim, and I can't drive",
                                "I can swim, or I can't drive",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ela fica em casa porque está a chover» "
                                 "escreve-se:",
                            "options": [
                                "She stays at home because it is raining",
                                "She stays at home but it is raining",
                                "She stays at home or it is raining",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada advérbio de frequência ao seu "
                                 "significado.",
                            "pairs": [
                                ["Sempre", "Always"],
                                ["Às vezes", "Sometimes"],
                                ["Nunca", "Never"],
                            ],
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 2  Modern and traditional medicine
        # ================================================================
        {
            "id": "u2",
            "titulo": "Medicina moderna e tradicional",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A saúde e o futuro",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada palavra da saúde ao inglês.",
                            "pairs": [
                                ["Médico", "Doctor"],
                                ["Curandeiro", "Healer"],
                                ["Vacina", "Vaccine"],
                                ["Seringa", "Syringe"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «remédio de ervas» em "
                                 "inglês?",
                            "options": [
                                "Herbal medicine",
                                "Modern medicine",
                                "Hospital",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Amanhã vou ao hospital» escreve-se, com "
                                 "o futuro de intenção:",
                            "options": [
                                "I am going to the hospital tomorrow",
                                "I go to the hospital tomorrow",
                                "I went to the hospital tomorrow",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O médico vai ajudar-te» escreve-se:",
                            "options": [
                                "The doctor will help you",
                                "The doctor helped you",
                                "The doctor helping you",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «ela está a "
                                 "tomar o remédio agora»?",
                            "options": [
                                "She is taking the medicine now",
                                "She takes the medicine now",
                                "She took the medicine now",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Conselhos, condições e quantidades",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Se tiveres febre, vai ao hospital» "
                                 "escreve-se:",
                            "options": [
                                "If you have a fever, go to the hospital",
                                "If you has a fever, go to the hospital",
                                "If you have a fever, went to the hospital",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Se chover, ficaremos em casa» "
                                 "escreve-se:",
                            "options": [
                                "If it rains, we will stay at home",
                                "If it rains, we stayed at home",
                                "If it rain, we will stay at home",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «automedicação» em inglês?",
                            "options": [
                                "Self-medication",
                                "Self-service",
                                "Medical care",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Há poucos médicos na aldeia» "
                                 "escreve-se:",
                            "options": [
                                "There are few doctors in the village",
                                "There are many doctors in the village",
                                "There are much doctors in the village",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «tu devias "
                                 "ir ao médico»?",
                            "options": [
                                "You should go to the doctor",
                                "You should to go to the doctor",
                                "You should going to the doctor",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 3  Customs and traditions
        # ================================================================
        {
            "id": "u3",
            "titulo": "Costumes e tradições",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Cerimónias e a ordem das coisas",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada cerimónia ao inglês.",
                            "pairs": [
                                ["Casamento", "Wedding"],
                                ["Funeral", "Funeral"],
                                ["Nascimento", "Birth"],
                                ["Ritos de iniciação", "Initiation rites"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «tambor» em inglês?",
                            "options": ["Drum", "Dance", "Song"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada marcador de sequência ao "
                                 "inglês.",
                            "pairs": [
                                ["Primeiro", "First"],
                                ["Depois", "Then"],
                                ["Finalmente", "Finally"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Primeiro, a família reúne-se; depois, "
                                 "os anciãos falam» escreve-se:",
                            "options": [
                                "First, the family meets; then, the elders "
                                "speak",
                                "Finally, the family meets; first, the "
                                "elders speak",
                                "Then, the family meets; then, the elders "
                                "speak",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «costume» em inglês?",
                            "options": ["Custom", "Customer", "Cost"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Dever e proibição",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Devemos respeitar os mais velhos» "
                                 "escreve-se:",
                            "options": [
                                "We must respect the elders",
                                "We mustn't respect the elders",
                                "We must respecting the elders",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Não deves faltar às aulas» escreve-se:",
                            "options": [
                                "You mustn't miss classes",
                                "You must miss classes",
                                "You mustn't to miss classes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «os rapazes e "
                                 "as raparigas deviam partilhar as "
                                 "tarefas»?",
                            "options": [
                                "Boys and girls should share the tasks",
                                "Boys and girls should shares the tasks",
                                "Boys and girls should to share the tasks",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ela nunca chega atrasada, mas ele "
                                 "chega sempre» escreve-se:",
                            "options": [
                                "She is never late, but he always is",
                                "She is always late, but he never is",
                                "She is late never, but he is always",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada expressão formal à informal.",
                            "pairs": [
                                ["Good morning, Sir", "Hi"],
                                ["Thank you very much", "Thanks"],
                                ["Goodbye", "Bye"],
                            ],
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 4  Farming
        # ================================================================
        {
            "id": "u4",
            "titulo": "A agricultura",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O campo e as suas palavras",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada palavra do campo ao inglês.",
                            "pairs": [
                                ["Enxada", "Hoe"],
                                ["Charrua", "Plough"],
                                ["Colheita", "Harvest"],
                                ["Seca", "Drought"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «cheia» em inglês?",
                            "options": ["Flood", "Cyclone", "Earthquake"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O milho é uma cultura importante» "
                                 "escreve-se:",
                            "options": [
                                "Maize is an important crop",
                                "Maize is a important crop",
                                "The maize is an important crops",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «quanta água "
                                 "precisam as plantas»?",
                            "options": [
                                "How much water do the plants need",
                                "How many water do the plants need",
                                "How much waters do the plants need",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «criação de animais» em "
                                 "inglês?",
                            "options": [
                                "Animal husbandry",
                                "Animal hospital",
                                "Animal house",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O que estava a acontecer e o que já foi feito",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Os camponeses estavam a plantar quando "
                                 "a chuva começou» escreve-se:",
                            "options": [
                                "The farmers were planting when the rain "
                                "started",
                                "The farmers planting when the rain "
                                "started",
                                "The farmers are planting when the rain "
                                "started",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Nós já colhemos o milho» escreve-se, "
                                 "com o present perfect:",
                            "options": [
                                "We have harvested the maize",
                                "We has harvested the maize",
                                "We have harvest the maize",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O peixe é seco ao sol» escreve-se, na "
                                 "passiva:",
                            "options": [
                                "The fish is dried in the sun",
                                "The fish dries in the sun",
                                "The fish is dry in the sun",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «onde é que "
                                 "guardam as sementes»?",
                            "options": [
                                "Where do they keep the seeds",
                                "What do they keep the seeds",
                                "Where they keep the seeds",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Devíamos plantar árvores para travar a "
                                 "erosão» escreve-se:",
                            "options": [
                                "We should plant trees to stop erosion",
                                "We should planting trees to stop erosion",
                                "We should to plant trees to stop erosion",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 5  Shopping
        # ================================================================
        {
            "id": "u5",
            "titulo": "As compras",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Lojas, preços e regatear",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada lugar de compras ao inglês.",
                            "pairs": [
                                ["Mercado", "Market"],
                                ["Supermercado", "Supermarket"],
                                ["Padaria", "Bakery"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «quanto "
                                 "custa esta camisa»?",
                            "options": [
                                "How much is this shirt",
                                "How many is this shirt",
                                "How much are this shirt",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Quantas laranjas quer?» escreve-se:",
                            "options": [
                                "How many oranges do you want",
                                "How much oranges do you want",
                                "How many orange do you want",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «desconto» em inglês?",
                            "options": ["Discount", "Receipt", "Invoice"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Este vestido é mais caro do que "
                                 "aquele» escreve-se:",
                            "options": [
                                "This dress is more expensive than that one",
                                "This dress is expensiver than that one",
                                "This dress is more expensive that that one",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«É caro, não é?» escreve-se, com a "
                                 "pergunta no fim:",
                            "options": [
                                "It is expensive, isn't it",
                                "It is expensive, is it",
                                "It is expensive, doesn't it",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 6  Tourism and wildlife
        # ================================================================
        {
            "id": "u6",
            "titulo": "Turismo e vida selvagem",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Parques, praias e animais",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada animal ao inglês.",
                            "pairs": [
                                ["Elefante", "Elephant"],
                                ["Leão", "Lion"],
                                ["Hipopótamo", "Hippo"],
                                ["Tartaruga", "Turtle"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «caçador furtivo» em "
                                 "inglês?",
                            "options": ["Poacher", "Tourist", "Ranger"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «parque nacional» em inglês?",
                            "options": [
                                "National park",
                                "Natural place",
                                "Game reserve",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O Gorongosa é o parque mais famoso de "
                                 "Moçambique» escreve-se:",
                            "options": [
                                "Gorongosa is the most famous park in "
                                "Mozambique",
                                "Gorongosa is the more famous park in "
                                "Mozambique",
                                "Gorongosa is the famousest park in "
                                "Mozambique",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «espécies em perigo» em "
                                 "inglês?",
                            "options": [
                                "Endangered species",
                                "Dangerous species",
                                "Wild species",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Obrigações e reflexivos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Os turistas têm de proteger a "
                                 "natureza» escreve-se:",
                            "options": [
                                "Tourists have to protect nature",
                                "Tourists has to protect nature",
                                "Tourists have protect nature",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Não podes dar de comer aos animais» "
                                 "escreve-se:",
                            "options": [
                                "You may not feed the animals",
                                "You may not feeding the animals",
                                "You not may feed the animals",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «ela "
                                 "divertiu-se na praia»?",
                            "options": [
                                "She enjoyed herself at the beach",
                                "She enjoyed himself at the beach",
                                "She enjoyed her at the beach",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Já visitaste a ilha de Moçambique?» "
                                 "escreve-se:",
                            "options": [
                                "Have you ever visited Mozambique Island",
                                "Did you ever visited Mozambique Island",
                                "Have you ever visit Mozambique Island",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «mergulho com tubo» em "
                                 "inglês?",
                            "options": ["Snorkelling", "Yachting", "Hiking"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 7  Managing our planet
        # ================================================================
        {
            "id": "u7",
            "titulo": "Cuidar do planeta",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O ambiente e o que faríamos por ele",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada palavra do ambiente ao inglês.",
                            "pairs": [
                                ["Erosão", "Erosion"],
                                ["Poluição", "Pollution"],
                                ["Desflorestação", "Deforestation"],
                                ["Reciclar", "Recycle"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«As árvores que plantámos estão a "
                                 "crescer» escreve-se, com o pronome "
                                 "relativo:",
                            "options": [
                                "The trees that we planted are growing",
                                "The trees who we planted are growing",
                                "The trees what we planted are growing",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Se eu fosse presidente, protegeria as "
                                 "florestas» escreve-se:",
                            "options": [
                                "If I were president, I would protect the "
                                "forests",
                                "If I am president, I will protect the "
                                "forests",
                                "If I was president, I protect the forests",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «não deites "
                                 "lixo no rio»?",
                            "options": [
                                "Don't throw rubbish in the river",
                                "Doesn't throw rubbish in the river",
                                "Not throw rubbish in the river",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Devíamos reciclar as garrafas de "
                                 "plástico» escreve-se:",
                            "options": [
                                "We should recycle the plastic bottles",
                                "We should recycled the plastic bottles",
                                "We should recycles the plastic bottles",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 8  Health and Fitness
        # ================================================================
        {
            "id": "u8",
            "titulo": "Saúde e forma física",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Doenças, comida e plurais",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada doença ou sintoma ao inglês.",
                            "pairs": [
                                ["Malária", "Malaria"],
                                ["Cólera", "Cholera"],
                                ["Febre", "Fever"],
                                ["Dor de cabeça", "Headache"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada grupo de nutrientes ao inglês.",
                            "pairs": [
                                ["Proteínas", "Proteins"],
                                ["Hidratos de carbono", "Carbohydrates"],
                                ["Vitaminas", "Vitamins"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «anemia» em inglês?",
                            "options": ["Anaemia", "Blindness", "Kwashiorkor"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Uma criança, três crianças» escreve-se, "
                                 "com o plural certo:",
                            "options": [
                                "One child, three children",
                                "One child, three childs",
                                "One children, three childrens",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Deves fazer o teste no hospital» "
                                 "escreve-se:",
                            "options": [
                                "You should take the test at the hospital",
                                "You should takes the test at the hospital",
                                "You should to take the test at the hospital",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «eu prefiro "
                                 "fruta a doces»?",
                            "options": [
                                "I prefer fruit to sweets",
                                "I prefer fruit than sweets",
                                "I prefers fruit to sweets",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 9  Occupations and professions
        # ================================================================
        {
            "id": "u9",
            "titulo": "Ofícios e profissões",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Profissões e o que queremos ser",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada profissão ao inglês.",
                            "pairs": [
                                ["Enfermeira", "Nurse"],
                                ["Engenheiro", "Engineer"],
                                ["Motorista", "Driver"],
                                ["Professor", "Teacher"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «eu quero "
                                 "ser médica porque gosto de ajudar as "
                                 "pessoas»?",
                            "options": [
                                "I want to be a doctor because I like "
                                "helping people",
                                "I want be a doctor because I like helping "
                                "people",
                                "I want to be a doctor because I like help "
                                "people",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ela é enfermeira, não é?» escreve-se:",
                            "options": [
                                "She is a nurse, isn't she",
                                "She is a nurse, is she",
                                "She is a nurse, isn't it",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Se estudares, serás engenheiro» "
                                 "escreve-se:",
                            "options": [
                                "If you study, you will be an engineer",
                                "If you study, you would be an engineer",
                                "If you will study, you are an engineer",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Pode repetir, por favor?» escreve-se:",
                            "options": [
                                "Can you repeat that, please",
                                "Can you repeating that, please",
                                "You can repeat that, please",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «emprego» em inglês?",
                            "options": ["Job", "Jab", "Joy"],
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
