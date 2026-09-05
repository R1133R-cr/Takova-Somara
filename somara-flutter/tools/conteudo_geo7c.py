# -*- coding: utf-8 -*-
"""O curso de Geografia da 7a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Geografia -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024.
     Descarregado do educador.mozestuda.com.

Programa e nao livro do aluno, como as outras tres disciplinas da 7a
classe. Fica dito no campo `fonte`.

Com esta, a Geografia separa-se das Ciencias Sociais
-----------------------------------------------------
Da 4a a 6a classe a Geografia vem dentro das CIENCIAS SOCIAIS, num curso
so com a Historia. No secundario sao duas disciplinas com dois programas.
A Historia entrou na 0.39.0; esta fecha o par.

Quatro unidades no INDE, cinco no curso
----------------------------------------
    1o trimestre    I  Introducao ao estudo da Geografia
                   II  Representacao da Terra
                  III  A Terra no Universo
    2o trimestre   IV  A Terra e suas esferas
    3o trimestre   IV  A Terra e suas esferas (continuacao)

A Unidade IV atravessa dois trimestres e cobre as quatro esferas. E o
proprio programa que as numera a parte -- 4.2 Atmosfera, 4.3 Hidrosfera,
4.4 Litosfera, 4.5 Biosfera --, e por isso o curso corta-a onde ela ja
esta cortada: a atmosfera fica numa unidade, e as outras tres esferas na
seguinte. Uma unidade com sete niveis ao lado de outra com dois nao e
ordem nenhuma.

    u1  I           conceito, ramos, ciencias vizinhas
    u2  II          coordenadas, globo, mapas, escala, paisagens
    u3  III         universo, sistema solar, movimentos da Terra
    u4  IV (4.2)    atmosfera, tempo e clima, zonas bioclimaticas
    u5  IV (4.3-5)  hidrosfera, litosfera, biosfera

O que ficou de fora, e porque
------------------------------
O programa manda usar o Atlas e "ler globos, mapas e plantas". A app nao
desenha mapas -- nao ha contornos de Mocambique nem do mundo, e desenha-
los de memoria seria inventar geografia. As perguntas foram escritas para
se responderem SEM mapa a frente: a escala calcula-se com numeros, as
coordenadas explicam-se por palavras, e o que precisaria mesmo de uma
carta geografica ficou de fora em vez de ficar meio feito.

Correr a partir de somara-flutter/:
    python tools/conteudo_geo7c.py            # so mostra
    python tools/conteudo_geo7c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Geografia — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024. As quatro unidades "
    "temáticas são do programa; a Unidade IV, que o próprio programa "
    "divide por esferas e espalha por dois trimestres, está aqui em duas "
    "unidades. Os exercícios foram escritos a partir dos conteúdos, "
    "porque um programa de ensino não traz exercícios e não há livro do "
    "aluno da 7ª classe publicado."
)

CURSO = {
    "id": "geo-7c",
    "disciplina": "Geografia",
    "classe": "7ª classe",
    "tag": "GEO",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # u1 <- INDE I: Introducao ao estudo da Geografia
        # ================================================================
        {
            "id": "u1",
            "titulo": "Introdução ao estudo da Geografia",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O que é a Geografia",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Geografia estuda:",
                            "options": [
                                "A Terra e a relação entre o Homem e o espaço",
                                "Apenas o passado dos povos",
                                "Apenas os animais e as plantas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Estudar Geografia é útil sobretudo para:",
                            "options": [
                                "Compreender e organizar o espaço onde "
                                "vivemos",
                                "Decorar nomes de países",
                                "Aprender a desenhar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Geografia Física estuda:",
                            "options": [
                                "O relevo, o clima, os rios e os solos",
                                "A população e as cidades",
                                "As leis dos Estados",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Geografia Humana estuda:",
                            "options": [
                                "A população e as suas actividades",
                                "As rochas e os vulcões",
                                "As estrelas e os planetas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A Geografia e as ciências vizinhas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Qual destas ciências ajuda a Geografia a "
                                 "estudar o passado dos lugares?",
                            "options": ["A História", "A Química", "A Física"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Geologia ajuda a Geografia a estudar:",
                            "options": [
                                "As rochas e a formação do relevo",
                                "As línguas dos povos",
                                "O comércio entre países",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Cartografia é a ciência que trata:",
                            "options": [
                                "Da elaboração dos mapas",
                                "Do estudo dos climas",
                                "Do estudo das populações",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            # A História da 7a tem uma pergunta de ligar
                            # com o mesmo enunciado, e as duas disciplinas
                            # estao na mesma classe. As perguntas erradas
                            # sao guardadas pelo texto do enunciado: dois
                            # iguais na mesma classe colidiam.
                            "q": "Liga cada ciência ao seu objecto de "
                                 "estudo.",
                            "pairs": [
                                ["Climatologia", "Os climas"],
                                ["Demografia", "As populações"],
                            ],
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # u2 <- INDE II: Representacao da Terra
        # ================================================================
        {
            "id": "u2",
            "titulo": "A representação da Terra",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Coordenadas geográficas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Os paralelos são círculos:",
                            "options": [
                                "Paralelos ao Equador",
                                "Que vão de polo a polo",
                                "Que passam todos por Greenwich",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os meridianos vão:",
                            "options": [
                                "De um polo ao outro",
                                "À volta do Equador",
                                "Só pelo hemisfério norte",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O paralelo de 0 graus chama-se:",
                            "options": [
                                "Equador",
                                "Meridiano de Greenwich",
                                "Trópico de Câncer",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A latitude mede a distância de um lugar:",
                            "options": [
                                "Ao Equador",
                                "Ao meridiano de Greenwich",
                                "Ao polo Norte apenas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A longitude mede a distância de um lugar:",
                            "options": [
                                "Ao meridiano de Greenwich",
                                "Ao Equador",
                                "Ao trópico de Capricórnio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Moçambique é atravessado pelo:",
                            "options": [
                                "Trópico de Capricórnio",
                                "Trópico de Câncer",
                                "Círculo polar árctico",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Globos, mapas e plantas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A grande vantagem do globo terrestre é:",
                            "options": [
                                "Representar a forma da Terra sem deformar",
                                "Caber num bolso",
                                "Mostrar muito pormenor",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A grande desvantagem do globo terrestre é:",
                            "options": [
                                "Mostrar pouco pormenor e ser difícil de "
                                "transportar",
                                "Deformar a forma dos continentes",
                                "Não ter cores",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes NÃO é um elemento de um mapa?",
                            "options": [
                                "O preço",
                                "A legenda",
                                "A escala",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A legenda de um mapa serve para:",
                            "options": [
                                "Explicar o que significam os símbolos e as "
                                "cores",
                                "Dizer quem desenhou o mapa",
                                "Indicar o preço do mapa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma planta representa:",
                            "options": [
                                "Uma área pequena com muito pormenor",
                                "O mundo inteiro",
                                "Um continente",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A escala e as paisagens",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Numa escala 1:100 000, um centímetro no "
                                 "mapa corresponde na realidade a:",
                            "options": [
                                "1 quilómetro",
                                "100 quilómetros",
                                "100 metros",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Numa escala 1:100 000, três centímetros no "
                                 "mapa correspondem a quantos quilómetros na "
                                 "realidade?",
                            "a": "3",
                        },
                        {
                            "t": "choice",
                            "q": "Entre uma escala 1:25 000 e uma escala "
                                 "1:500 000, qual mostra mais pormenor?",
                            "options": [
                                "A de 1:25 000",
                                "A de 1:500 000",
                                "Mostram o mesmo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma paisagem natural é aquela:",
                            "options": [
                                "Onde o Homem quase não interveio",
                                "Onde há muitas casas",
                                "Que só existe nas cidades",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma machamba é um exemplo de paisagem:",
                            "options": [
                                "Humanizada rural",
                                "Natural",
                                "Humanizada urbana",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # u3 <- INDE III: A Terra no Universo
        # ================================================================
        {
            "id": "u3",
            "titulo": "A Terra no Universo",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O Universo e os seus elementos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A teoria mais aceite sobre a origem do "
                                 "Universo chama-se:",
                            "options": [
                                "Teoria do Big Bang",
                                "Teoria da hominização",
                                "Teoria das placas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma galáxia é:",
                            "options": [
                                "Um enorme conjunto de estrelas, gás e poeira",
                                "Um planeta muito grande",
                                "Um satélite natural",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes corpos tem luz própria?",
                            "options": ["A estrela", "O planeta", "O satélite"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A galáxia onde fica o nosso Sistema Solar "
                                 "chama-se:",
                            "options": ["Via Láctea", "Andrómeda", "Órion"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O Sistema Solar",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Quantos planetas tem o Sistema Solar?",
                            "a": "8",
                        },
                        {
                            "t": "choice",
                            "q": "No centro do Sistema Solar está:",
                            "options": ["O Sol", "A Terra", "A Lua"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Contando a partir do Sol, em que posição "
                                 "está a Terra?",
                            "a": "3",
                        },
                        {
                            "t": "choice",
                            "q": "A Lua é:",
                            "options": [
                                "O satélite natural da Terra",
                                "Um planeta",
                                "Uma estrela",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual é o maior planeta do Sistema Solar?",
                            "options": ["Júpiter", "Terra", "Marte"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Os movimentos da Terra",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O movimento de rotação da Terra dá origem:",
                            "options": [
                                "Ao dia e à noite",
                                "Às estações do ano",
                                "Às marés",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Quantas horas demora a Terra a dar uma "
                                 "volta completa sobre si mesma?",
                            "a": "24",
                        },
                        {
                            "t": "choice",
                            "q": "O movimento de translação é o que a Terra "
                                 "faz:",
                            "options": [
                                "À volta do Sol",
                                "Sobre o seu próprio eixo",
                                "À volta da Lua",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A translação, com a inclinação do eixo "
                                 "terrestre, dá origem:",
                            "options": [
                                "Às estações do ano",
                                "Ao dia e à noite",
                                "Aos eclipses",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Aproximadamente quantos dias demora a "
                                 "Terra a dar uma volta ao Sol?",
                            "a": "365",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # u4 <- INDE IV, 4.2: A Atmosfera
        # ================================================================
        {
            "id": "u4",
            "titulo": "A atmosfera e o clima",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A atmosfera e as suas camadas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A atmosfera é:",
                            "options": [
                                "A camada de ar que envolve a Terra",
                                "A camada de água da Terra",
                                "A parte sólida da Terra",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual é o gás mais abundante na atmosfera?",
                            "options": [
                                "O azoto",
                                "O oxigénio",
                                "O dióxido de carbono",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A camada da atmosfera mais próxima da "
                                 "superfície, onde ocorrem os fenómenos do "
                                 "tempo, é:",
                            "options": [
                                "A troposfera",
                                "A mesosfera",
                                "A exosfera",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A camada de ozono protege os seres vivos:",
                            "options": [
                                "Dos raios ultravioleta do Sol",
                                "Da chuva forte",
                                "Dos ventos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A destruição da camada de ozono aumenta o "
                                 "risco de:",
                            "options": [
                                "Cancro da pele",
                                "Fractura dos ossos",
                                "Perda de audição",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Tempo e clima",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A diferença entre tempo e clima é que o "
                                 "tempo:",
                            "options": [
                                "É o estado da atmosfera num momento; o clima "
                                "é o que se repete ao longo de muitos anos",
                                "Dura mais do que o clima",
                                "Só existe no Verão",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um elemento do clima?",
                            "options": [
                                "A temperatura",
                                "A latitude",
                                "A altitude",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um factor do clima?",
                            "options": [
                                "A altitude",
                                "A precipitação",
                                "A temperatura",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O instrumento que mede a quantidade de "
                                 "chuva chama-se:",
                            "options": [
                                "Pluviómetro",
                                "Termómetro",
                                "Anemómetro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quanto maior a altitude de um lugar:",
                            "options": [
                                "Menor tende a ser a temperatura",
                                "Maior tende a ser a temperatura",
                                "A temperatura não muda",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada instrumento ao que ele mede.",
                            "pairs": [
                                ["Termómetro", "A temperatura"],
                                ["Anemómetro", "A velocidade do vento"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Zonas bioclimáticas e a protecção do ar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A zona bioclimática que fica entre os dois "
                                 "trópicos chama-se:",
                            "options": [
                                "Zona intertropical",
                                "Zona temperada",
                                "Zona fria",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Moçambique fica na zona:",
                            "options": [
                                "Intertropical",
                                "Temperada do norte",
                                "Fria do sul",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As zonas frias ficam:",
                            "options": [
                                "Entre os círculos polares e os polos",
                                "Entre os dois trópicos",
                                "Junto ao Equador",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um risco natural de origem "
                                 "atmosférica?",
                            "options": [
                                "O ciclone",
                                "O sismo",
                                "A erupção vulcânica",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma forma de reduzir a poluição "
                                 "atmosférica é:",
                            "options": [
                                "Usar mais transportes públicos e menos "
                                "queimadas",
                                "Queimar mais lixo ao ar livre",
                                "Cortar mais árvores",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # u5 <- INDE IV, 4.3 a 4.5: Hidrosfera, Litosfera e Biosfera
        # ================================================================
        {
            "id": "u5",
            "titulo": "Hidrosfera, litosfera e biosfera",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Oceanos e mares",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A hidrosfera é:",
                            "options": [
                                "O conjunto das águas do planeta",
                                "A camada de ar da Terra",
                                "A parte rochosa da Terra",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Aproximadamente que parte da superfície da "
                                 "Terra é ocupada por água?",
                            "options": [
                                "Cerca de 71 por cento",
                                "Cerca de 30 por cento",
                                "Cerca de 10 por cento",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Moçambique é banhado pelo oceano:",
                            "options": ["Índico", "Atlântico", "Pacífico"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As marés resultam sobretudo da atracção:",
                            "options": [
                                "Da Lua e do Sol",
                                "Do vento",
                                "Das correntes marítimas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As ondas do mar são provocadas sobretudo:",
                            "options": [
                                "Pelo vento",
                                "Pela chuva",
                                "Pelos rios",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Rios, lagos e o ciclo da água",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O lugar onde um rio nasce chama-se:",
                            "options": ["Nascente", "Foz", "Afluente"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O lugar onde um rio desagua chama-se:",
                            "options": ["Foz", "Nascente", "Leito"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um rio que desagua noutro rio chama-se:",
                            "options": ["Afluente", "Foz", "Bacia"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O maior lago de Moçambique é o:",
                            "options": ["Niassa", "Vitória", "Tanganica"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No ciclo da água, a passagem da água "
                                 "líquida a vapor chama-se:",
                            "options": [
                                "Evaporação",
                                "Condensação",
                                "Precipitação",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No ciclo da água, a formação das nuvens "
                                 "acontece por:",
                            "options": [
                                "Condensação",
                                "Evaporação",
                                "Infiltração",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A litosfera: estrutura, rochas e solos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As três camadas da estrutura interna da "
                                 "Terra são:",
                            "options": [
                                "Crusta, manto e núcleo",
                                "Troposfera, manto e núcleo",
                                "Crusta, solo e rocha",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As rochas que se formam quando o magma "
                                 "arrefece chamam-se:",
                            "options": [
                                "Magmáticas",
                                "Sedimentares",
                                "Metamórficas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As rochas que se formam pela acumulação de "
                                 "sedimentos chamam-se:",
                            "options": [
                                "Sedimentares",
                                "Magmáticas",
                                "Metamórficas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O mármore é uma rocha:",
                            "options": [
                                "Metamórfica",
                                "Magmática",
                                "Sedimentar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O solo forma-se sobretudo a partir:",
                            "options": [
                                "Da alteração das rochas e da matéria "
                                "orgânica",
                                "Da água da chuva apenas",
                                "Do vento apenas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "O relevo e a biosfera",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Os sismos e os vulcões são agentes:",
                            "options": [
                                "Internos, que constroem o relevo",
                                "Externos, que desgastam o relevo",
                                "Sem efeito no relevo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A erosão provocada pela água e pelo vento é "
                                 "um agente:",
                            "options": [
                                "Externo, que modela o relevo",
                                "Interno, que constrói o relevo",
                                "Sem efeito no relevo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A biosfera é:",
                            "options": [
                                "O conjunto de todos os seres vivos do planeta",
                                "O conjunto das rochas",
                                "A camada de ar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As quatro esferas da Terra estão "
                                 "interligadas. Isso quer dizer que:",
                            "options": [
                                "O que acontece numa afecta as outras",
                                "Cada uma funciona sozinha",
                                "Só a atmosfera tem importância",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas acções protege a biosfera?",
                            "options": [
                                "Reflorestar e proteger as espécies",
                                "Fazer queimadas descontroladas",
                                "Deitar lixo nos rios",
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
            print(f"       {n['id']}  {n['titulo']:<44}"
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

    dados["cursos"].append(CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta as entradas ao tools/materia_texto.py "
          "e corre python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
