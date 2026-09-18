# -*- coding: utf-8 -*-
"""O curso de Ingles da 9a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Lingua Inglesa -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024,
     Grade 9, pp. 48-63. Guardado em Documents\\planos da 5a classe\\
     Livros\\Programas INDE 1o Ciclo\\ingles.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As nove unidades do Grade 9, pela ordem do programa
---------------------------------------------------
    1  English in the business world today   comercio; comparativos;
                                             can e may; futuro
    2  Importance of Education               educacao; adverbios de modo;
                                             formacao de palavras; present
                                             perfect continuous
    3  Human Rights and Gender               direitos; have to; passado;
                                             both, either, neither
    4  Growing economy through farming       campo e pesca; quantificadores;
                                             conselhos; comparativos curtos
    5  Doing business                        negocio; few e little;
                                             imperativo; passiva; in, at, on
    6  School subjects and future            disciplinas; passado e present
       professions                           perfect; relativos; oracoes de
                                             tempo
    7  Science and Technology in the 21st    aparelhos; do e make; although;
       Century                               past perfect
    8  Successful and famous people          figuras; as ... as; discurso
                                             indirecto
    9  Life after school                     trabalho; gerundio; revisao

Nove unidades, catorze aulas.

O ingles fica nas opcoes, como na 7a e na 8a
--------------------------------------------
A voz da app e portuguesa. Os enunciados sao em portugues e o ingles
aparece so nas opcoes e nos pares.

Correr a partir de somara-flutter/:
    python tools/conteudo_ing9c.py            # so mostra
    python tools/conteudo_ing9c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Língua Inglesa — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, Grade 9, pp. 48-63. "
    "As nove unidades, o vocabulário e a gramática são do programa; os "
    "exercícios foram escritos a partir deles, porque um programa de ensino "
    "não traz exercícios e não há livro do aluno da 9ª classe publicado. Os "
    "enunciados são em português e o inglês fica nas opções, porque a voz da "
    "app é portuguesa."
)

CURSO = {
    "id": "ing-9c",
    "disciplina": "Inglês",
    "classe": "9ª classe",
    "tag": "ING",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # 1  English in the business world today
        # ================================================================
        {
            "id": "u1",
            "titulo": "O inglês no mundo dos negócios",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Comércio e comparações",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada palavra do comércio ao inglês.",
                            "pairs": [
                                ["Moeda", "Currency"],
                                ["Empréstimo", "Loan"],
                                ["Cliente", "Customer"],
                                ["Comércio", "Trade"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«O inglês é tão importante como o "
                                 "português» escreve-se:",
                            "options": [
                                "English is as important as Portuguese",
                                "English is so important than Portuguese",
                                "English is as important than Portuguese",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O mercado de Lichinga é menos caro do "
                                 "que o de Maputo» escreve-se:",
                            "options": [
                                "Lichinga market is less expensive than "
                                "Maputo market",
                                "Lichinga market is least expensive than "
                                "Maputo market",
                                "Lichinga market is less expensive as "
                                "Maputo market",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «integração regional» em "
                                 "inglês?",
                            "options": [
                                "Regional integration",
                                "Regional independence",
                                "Integral region",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada país vizinho à sua língua "
                                 "oficial.",
                            "pairs": [
                                ["Malawi", "English"],
                                ["Angola", "Portuguese"],
                                ["Zimbabwe", "English"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Probabilidade e futuro",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Pode ser que os preços subam» "
                                 "escreve-se, com probabilidade:",
                            "options": [
                                "Prices may go up",
                                "Prices must go up",
                                "Prices going up",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O inglês pode abrir-te muitas portas» "
                                 "escreve-se:",
                            "options": [
                                "English can open many doors for you",
                                "English cans open many doors for you",
                                "English can opens many doors for you",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Amanhã vamos vender os tomates no "
                                 "mercado» escreve-se, com o futuro de "
                                 "intenção:",
                            "options": [
                                "We are going to sell the tomatoes at the "
                                "market tomorrow",
                                "We go to sell the tomatoes at the market "
                                "tomorrow",
                                "We sold the tomatoes at the market "
                                "tomorrow",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Um dia, o meu negócio vai crescer» "
                                 "escreve-se, como previsão:",
                            "options": [
                                "One day, my business will grow",
                                "One day, my business grows will",
                                "One day, my business will grows",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «lucro» em inglês?",
                            "options": ["Profit", "Loss", "Price"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 2  Importance of Education
        # ================================================================
        {
            "id": "u2",
            "titulo": "A importância da educação",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Educação e advérbios de modo",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada palavra da educação ao inglês.",
                            "pairs": [
                                ["Formação", "Training"],
                                ["Cidadania", "Citizenship"],
                                ["Qualidade", "Quality"],
                                ["Espírito crítico", "Critical sense"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Ela estuda com atenção» escreve-se, com "
                                 "um advérbio de modo:",
                            "options": [
                                "She studies carefully",
                                "She studies careful",
                                "She careful studies",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada adjectivo ao seu advérbio de "
                                 "modo.",
                            "pairs": [
                                ["Quick", "Quickly"],
                                ["Easy", "Easily"],
                                ["Good", "Well"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Educar as raparigas é importante para "
                                 "o país» escreve-se:",
                            "options": [
                                "Educating girls is important for the "
                                "country",
                                "Educate girls are important for the "
                                "country",
                                "Educating girls are important for the "
                                "country",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os pais ensinam em casa e os professores "
                                 "na escola. «Em casa» diz-se:",
                            "options": ["At home", "In home", "On home"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Formar palavras e o present perfect continuous",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada nome ao adjectivo que dele se "
                                 "forma.",
                            "pairs": [
                                ["Use", "Useful"],
                                ["Danger", "Dangerous"],
                                ["Care", "Careless"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Tenho estado a estudar há duas horas» "
                                 "escreve-se:",
                            "options": [
                                "I have been studying for two hours",
                                "I have studying for two hours",
                                "I am been studying for two hours",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ela tem ensinado nesta escola desde "
                                 "2020» escreve-se:",
                            "options": [
                                "She has been teaching at this school "
                                "since 2020",
                                "She has been teaching at this school for "
                                "2020",
                                "She have been teaching at this school "
                                "since 2020",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Com uma data usa-se «since»; com uma "
                                 "duração, como «três anos», usa-se:",
                            "options": ["For", "Since", "Ago"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes adjectivos quer dizer «sem "
                                 "esperança»?",
                            "options": ["Hopeless", "Hopeful", "Hoping"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 3  Human Rights and Gender
        # ================================================================
        {
            "id": "u3",
            "titulo": "Direitos humanos e género",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Direitos, deveres e o passado",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada palavra dos direitos ao inglês.",
                            "pairs": [
                                ["Lei", "Law"],
                                ["Crime", "Crime"],
                                ["Paz", "Peace"],
                                ["Violência doméstica", "Domestic violence"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«As crianças têm de ir à escola» "
                                 "escreve-se:",
                            "options": [
                                "Children have to go to school",
                                "Children has to go to school",
                                "Children have go to school",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ela tem de ajudar em casa» escreve-se:",
                            "options": [
                                "She has to help at home",
                                "She have to help at home",
                                "She has help at home",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A lei protegeu as raparigas» escreve-se:",
                            "options": [
                                "The law protected the girls",
                                "The law protects the girls yesterday",
                                "The law protecting the girls",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual é a diferença entre «sex» e "
                                 "«gender»?",
                            "options": [
                                "Sex é biológico; gender são os papéis que "
                                "a sociedade dá",
                                "São a mesma coisa",
                                "Gender é biológico; sex é social",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Ambos, um ou outro, nenhum",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Tanto os rapazes como as raparigas têm "
                                 "direitos» escreve-se:",
                            "options": [
                                "Both boys and girls have rights",
                                "Either boys and girls have rights",
                                "Neither boys and girls have rights",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Nem o pai nem a mãe podem bater nos "
                                 "filhos» escreve-se:",
                            "options": [
                                "Neither the father nor the mother can hit "
                                "the children",
                                "Either the father nor the mother can hit "
                                "the children",
                                "Neither the father or the mother can hit "
                                "the children",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Podes falar com o professor ou com o "
                                 "director» escreve-se:",
                            "options": [
                                "You can talk to either the teacher or the "
                                "headmaster",
                                "You can talk to neither the teacher or "
                                "the headmaster",
                                "You can talk to both the teacher or the "
                                "headmaster",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada direito da criança ao inglês.",
                            "pairs": [
                                ["Direito à educação", "Right to education"],
                                ["Direito à saúde", "Right to health"],
                                ["Direito a brincar", "Right to play"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «igualdade de direitos» em "
                                 "inglês?",
                            "options": ["Equal rights", "Same laws", "Right equals"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 4  Growing economy through farming
        # ================================================================
        {
            "id": "u4",
            "titulo": "A economia e a agricultura",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Campo, pesca e quantidades",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada palavra do campo ao inglês.",
                            "pairs": [
                                ["Adubo", "Fertilizer"],
                                ["Tractor", "Tractor"],
                                ["Barragem", "Dam"],
                                ["Albufeira", "Reservoir"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Os tractores são mais rápidos do que as "
                                 "enxadas» escreve-se:",
                            "options": [
                                "Tractors are faster than hoes",
                                "Tractors are more fast than hoes",
                                "Tractors are fastest than hoes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Deverias secar o peixe antes de o "
                                 "vender» escreve-se, como conselho:",
                            "options": [
                                "You should dry the fish before selling it",
                                "You should to dry the fish before selling "
                                "it",
                                "You should drying the fish before selling "
                                "it",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Há poucos peixes no rio este ano» "
                                 "escreve-se:",
                            "options": [
                                "There are few fish in the river this year",
                                "There is little fish in the river this "
                                "year",
                                "There are much fish in the river this "
                                "year",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A aldeia inteira ajudou na colheita» "
                                 "escreve-se:",
                            "options": [
                                "The whole village helped with the harvest",
                                "The all village helped with the harvest",
                                "The whole villages helped with the harvest",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 5  Doing business
        # ================================================================
        {
            "id": "u5",
            "titulo": "Fazer negócio",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O negócio, few e little",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada palavra do negócio ao inglês.",
                            "pairs": [
                                ["Fábrica", "Factory"],
                                ["Matéria-prima", "Raw material"],
                                ["Mercado informal", "Informal market"],
                                ["Rendimento", "Income"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Tenho um pouco de dinheiro» escreve-se:",
                            "options": [
                                "I have a little money",
                                "I have a few money",
                                "I have a little moneys",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Tenho alguns clientes» escreve-se:",
                            "options": [
                                "I have a few customers",
                                "I have a little customers",
                                "I have a few customer",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Abre a loja às oito!» escreve-se, no "
                                 "imperativo:",
                            "options": [
                                "Open the shop at eight",
                                "You opens the shop at eight",
                                "Opening the shop at eight",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada expressão de tempo à "
                                 "preposição certa em inglês.",
                            "pairs": [
                                ["… Monday", "On"],
                                ["… eight o'clock", "At"],
                                ["… January", "In"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A passiva e a carta de negócio",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«O caju é exportado para a Índia» "
                                 "escreve-se, na passiva:",
                            "options": [
                                "Cashew is exported to India",
                                "Cashew exports to India",
                                "Cashew is export to India",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Estes cestos são feitos à mão» "
                                 "escreve-se:",
                            "options": [
                                "These baskets are made by hand",
                                "These baskets make by hand",
                                "These baskets are make by hand",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma carta de negócio a quem não se "
                                 "conhece começa por:",
                            "options": [
                                "Dear Sir or Madam",
                                "Hi friend",
                                "Hello boss",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A loja fica no mercado» escreve-se:",
                            "options": [
                                "The shop is in the market",
                                "The shop is on the market",
                                "The shop is at the market street on",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ganhamos mais e gastamos menos» "
                                 "escreve-se:",
                            "options": [
                                "We earn more and spend less",
                                "We earn most and spend least",
                                "We earn more and spend fewer",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 6  School subjects and future professions
        # ================================================================
        {
            "id": "u6",
            "titulo": "Disciplinas e profissões futuras",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Disciplinas e relativos",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada disciplina ao inglês.",
                            "pairs": [
                                ["Matemática", "Mathematics"],
                                ["Física", "Physics"],
                                ["Química", "Chemistry"],
                                ["Geografia", "Geography"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Um médico é uma pessoa que trata os "
                                 "doentes» escreve-se:",
                            "options": [
                                "A doctor is a person who treats sick "
                                "people",
                                "A doctor is a person which treats sick "
                                "people",
                                "A doctor is a person what treats sick "
                                "people",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A disciplina de que mais gosto é a "
                                 "Biologia» escreve-se:",
                            "options": [
                                "The subject that I like most is Biology",
                                "The subject who I like most is Biology",
                                "The subject I like more is Biology most",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada disciplina à profissão que ela "
                                 "prepara.",
                            "pairs": [
                                ["Biology", "Nurse"],
                                ["Mathematics", "Engineer"],
                                ["Agriculture", "Farmer"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«A Física é mais difícil do que a "
                                 "Geografia» escreve-se:",
                            "options": [
                                "Physics is more difficult than Geography",
                                "Physics is difficulter than Geography",
                                "Physics is most difficult than Geography",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Passado, present perfect e orações de tempo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Ontem terminei os trabalhos» "
                                 "escreve-se:",
                            "options": [
                                "I finished my homework yesterday",
                                "I have finished my homework yesterday",
                                "I finish my homework yesterday",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Já escolhi a minha profissão» "
                                 "escreve-se:",
                            "options": [
                                "I have already chosen my profession",
                                "I already chose my profession yesterday",
                                "I have already choose my profession",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Logo que acabar a escola, vou "
                                 "trabalhar» escreve-se:",
                            "options": [
                                "As soon as I finish school, I will work",
                                "As soon as I will finish school, I work",
                                "As soon as I finished school, I will work",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A ponte foi construída em 2009» "
                                 "escreve-se, na passiva do passado:",
                            "options": [
                                "The bridge was built in 2009",
                                "The bridge is built in 2009",
                                "The bridge built in 2009",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Estudo enquanto a minha irmã cozinha» "
                                 "escreve-se:",
                            "options": [
                                "I study while my sister cooks",
                                "I study until my sister cooks",
                                "I study as soon my sister cooks",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 7  Science and Technology in the 21st Century
        # ================================================================
        {
            "id": "u7",
            "titulo": "Ciência e tecnologia no século XXI",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Aparelhos, do e make, e o past perfect",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada aparelho ao inglês.",
                            "pairs": [
                                ["Painel solar", "Solar panel"],
                                ["Telemóvel", "Cell phone"],
                                ["Bomba de água a pedal", "Pedal water pump"],
                                ["Sítio da Internet", "Website"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada expressão ao verbo que ela "
                                 "pede em inglês.",
                            "pairs": [
                                ["… homework", "Do"],
                                ["… a phone call", "Make"],
                                ["… a mistake", "Make"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Embora a Internet seja útil, custa "
                                 "caro» escreve-se:",
                            "options": [
                                "Although the Internet is useful, it is "
                                "expensive",
                                "Although the Internet is useful, but it "
                                "is expensive",
                                "Although the Internet useful, it "
                                "expensive",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Nunca tinha usado um computador antes "
                                 "de 2020» escreve-se:",
                            "options": [
                                "I had never used a computer before 2020",
                                "I have never used a computer before 2020",
                                "I had never use a computer before 2020",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma desvantagem das tecnologias de "
                                 "informação, em inglês, é:",
                            "options": [
                                "Data costs money",
                                "Data is free",
                                "Phones never break",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 8  Successful and famous people
        # ================================================================
        {
            "id": "u8",
            "titulo": "Pessoas famosas e de sucesso",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Heróis, comparações e discurso indirecto",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada figura moçambicana à sua área, "
                                 "em inglês.",
                            "pairs": [
                                ["Maria de Lurdes Mutola", "Sport"],
                                ["Malangatana", "Painting"],
                                ["Mia Couto", "Writing"],
                                ["Eduardo Mondlane", "Politics"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Ela corre tão depressa como um carro» "
                                 "escreve-se:",
                            "options": [
                                "She runs as fast as a car",
                                "She runs as faster as a car",
                                "She runs so fast than a car",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Eu sou professor», disse ele. Em "
                                 "discurso indirecto:",
                            "options": [
                                "He said that he was a teacher",
                                "He said that I am a teacher",
                                "He said that he is being a teacher",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Estou a pintar», disse ela. Em discurso "
                                 "indirecto:",
                            "options": [
                                "She said that she was painting",
                                "She said that she is paint",
                                "She said that I was painting",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Canta como um anjo» escreve-se:",
                            "options": [
                                "He sings like an angel",
                                "He sings as an angel like",
                                "He sing like a angel",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 9  Life after school
        # ================================================================
        {
            "id": "u9",
            "titulo": "A vida depois da escola",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Trabalho, empreendedorismo e revisão",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada palavra do trabalho ao inglês.",
                            "pairs": [
                                ["Empreendedorismo", "Entrepreneurship"],
                                ["Trabalho por conta própria", "Self-employment"],
                                ["Formação profissional", "Vocational training"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Gosto de trabalhar em equipa» "
                                 "escreve-se, com o gerúndio:",
                            "options": [
                                "I enjoy working in a team",
                                "I enjoy to working in a team",
                                "I enjoy work in a team",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Se eu tivesse dinheiro, abriria uma "
                                 "loja» escreve-se:",
                            "options": [
                                "If I had money, I would open a shop",
                                "If I have money, I would open a shop",
                                "If I had money, I will open a shop",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada qualidade pessoal ao inglês.",
                            "pairs": [
                                ["Trabalhador", "Hard-working"],
                                ["Honesto", "Honest"],
                                ["Pontual", "Punctual"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Numa sociedade, «business partnership» "
                                 "quer dizer:",
                            "options": [
                                "Duas ou mais pessoas a fazer um negócio "
                                "juntas",
                                "Um negócio de uma pessoa só",
                                "Um empréstimo do banco",
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
