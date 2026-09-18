# -*- coding: utf-8 -*-
"""O curso de Geografia da 9a classe -- a Geografia de Mocambique.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Geografia -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, 9a classe,
     pp. 37-47. Guardado em Documents\\planos da 5a classe\\Livros\\
     Programas INDE 1o Ciclo\\geografia.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As quatro unidades, pela ordem do programa
------------------------------------------
    I    Geografia Fisica de Mocambique   situacao e limites; geologia e
                                          minerais; relevo; clima;
                                          biogeografia e hidrografia
    II   Populacao                        indicadores; movimentos;
                                          estrutura e distribuicao
    III  Actividades Economicas           agricultura e pecuaria; pesca e
                                          silvicultura; industria;
                                          transportes e comercio; turismo
                                          e educacao financeira
    IV   Mocambique e a SADC              a Africa Austral e a SADC;
                                          integracao regional, direitos
                                          humanos e democracia

Quatro unidades, quinze aulas. A 7a foi a Geografia geral e a 8a a
humana e economica; a 9a e Mocambique inteiro, do Rovuma ao Maputo.

Correr a partir de somara-flutter/:
    python tools/conteudo_geo9c.py            # so mostra
    python tools/conteudo_geo9c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Geografia — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, 9ª classe, pp. 37-47. "
    "As quatro unidades e os conteúdos são do programa; os exercícios foram "
    "escritos a partir deles, porque um programa de ensino não traz "
    "exercícios e não há livro do aluno da 9ª classe publicado."
)

CURSO = {
    "id": "geo-9c",
    "disciplina": "Geografia",
    "classe": "9ª classe",
    "tag": "GEO",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # I  Geografia Fisica de Mocambique
        # ================================================================
        {
            "id": "u1",
            "titulo": "Geografia física de Moçambique",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Situação geográfica e limites",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Moçambique fica:",
                            "options": [
                                "Na costa oriental da África Austral, "
                                "banhado pelo Oceano Índico",
                                "Na costa ocidental de África",
                                "No norte de África",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Com quantos países faz fronteira "
                                 "Moçambique?",
                            "a": "6",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada país vizinho ao lado em que "
                                 "fica.",
                            "pairs": [
                                ["Tanzânia", "Norte, do outro lado do Rovuma"],
                                ["Malawi e Zâmbia", "Noroeste"],
                                ["Zimbabué", "Oeste"],
                                ["África do Sul e Essuatíni", "Sul e sudoeste"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O rio que marca a fronteira norte com a "
                                 "Tanzânia é o:",
                            "options": ["Rovuma", "Zambeze", "Limpopo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A costa moçambicana tem cerca de:",
                            "options": [
                                "2700 quilómetros",
                                "300 quilómetros",
                                "10 000 quilómetros",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Geologia, minerais e solos",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada unidade geológica ao que ela "
                                 "é.",
                            "pairs": [
                                ["Pré-câmbrico", "As rochas mais antigas, no interior e no norte"],
                                ["Fanerozóico", "As rochas mais recentes: Karroo, Cretácico, Quaternário"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada recurso mineral ao lugar onde "
                                 "se explora.",
                            "pairs": [
                                ["Carvão", "Moatize, em Tete"],
                                ["Gás natural", "Pande e Temane, em Inhambane"],
                                ["Areias pesadas", "Moma, em Nampula"],
                                ["Rubis", "Montepuez, em Cabo Delgado"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada mineral ao seu grupo.",
                            "pairs": [
                                ["Carvão e gás", "Energéticos"],
                                ["Ouro e ferro", "Metálicos"],
                                ["Calcário e areia", "Não metálicos"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Os recursos minerais são importantes "
                                 "porque:",
                            "options": [
                                "Dão emprego, exportações e receitas ao "
                                "Estado",
                                "Não se acabam nunca",
                                "Só servem para enfeitar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os solos das planícies dos grandes rios "
                                 "são:",
                            "options": [
                                "Aluviais e férteis, bons para a "
                                "agricultura",
                                "Rochosos e estéreis",
                                "Sempre salgados",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O relevo",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada processo de formação do relevo "
                                 "ao seu tipo.",
                            "pairs": [
                                ["Vulcões e sismos, vindos de dentro da Terra", "Endógeno"],
                                ["Erosão pela chuva, pelo vento e pelos rios", "Exógeno"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada forma de relevo ao lugar onde "
                                 "domina em Moçambique.",
                            "pairs": [
                                ["Planícies", "O litoral, sobretudo no sul"],
                                ["Planaltos", "O interior do centro e do norte"],
                                ["Montanhas", "As fronteiras oeste: Manica, Niassa, Tete"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O ponto mais alto de Moçambique é o "
                                 "monte:",
                            "options": ["Binga, em Manica", "Namuli", "Gorongosa"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "O monte Binga tem cerca de 2436 metros. "
                                 "Quantos metros lhe faltam para os 3000?",
                            "a": "564",
                        },
                        {
                            "t": "choice",
                            "q": "Lichinga fica:",
                            "options": [
                                "No planalto do Niassa, a mais de 1300 "
                                "metros de altitude",
                                "Na planície do litoral",
                                "Ao nível do mar",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "O clima",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O clima de Moçambique é, no geral:",
                            "options": [
                                "Tropical, com uma estação quente e "
                                "chuvosa e outra fresca e seca",
                                "Polar",
                                "Desértico em todo o país",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de clima à zona onde "
                                 "ocorre.",
                            "pairs": [
                                ["Tropical húmido", "Litoral norte e centro"],
                                ["Tropical seco", "Interior sul, como Gaza"],
                                ["Tropical de altitude", "Planaltos e montanhas, como Lichinga"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada factor do clima ao seu efeito.",
                            "pairs": [
                                ["Latitude", "Mais perto do equador, mais calor"],
                                ["Altitude", "Mais alto, mais fresco"],
                                ["Proximidade do mar", "Mais humidade e chuva"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Num gráfico termopluviométrico, as "
                                 "barras mostram:",
                            "options": [
                                "A chuva de cada mês",
                                "A temperatura de cada mês",
                                "A altitude",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A estação das chuvas em Moçambique vai, "
                                 "em geral:",
                            "options": [
                                "De Outubro ou Novembro a Março ou Abril",
                                "De Maio a Setembro",
                                "O ano inteiro",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n5",
                    "titulo": "Vegetação, fauna, rios e lagos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A vegetação mais espalhada em "
                                 "Moçambique é:",
                            "options": [
                                "A savana e a floresta aberta de miombo",
                                "A floresta equatorial densa",
                                "O deserto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada área protegida à província "
                                 "onde fica.",
                            "pairs": [
                                ["Parque Nacional da Gorongosa", "Sofala"],
                                ["Reserva Especial do Niassa", "Niassa e Cabo Delgado"],
                                ["Parque Nacional do Bazaruto", "Inhambane"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O maior rio de Moçambique, onde está a "
                                 "barragem de Cahora Bassa, é o:",
                            "options": ["Zambeze", "Limpopo", "Lúrio"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada rio à zona do país por onde "
                                 "corre.",
                            "pairs": [
                                ["Rovuma e Lúrio", "Norte"],
                                ["Zambeze e Save", "Centro"],
                                ["Limpopo e Incomáti", "Sul"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O lago Niassa é:",
                            "options": [
                                "O terceiro maior lago de África, "
                                "partilhado com o Malawi e a Tanzânia",
                                "Um lago artificial",
                                "O maior lago do mundo",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # II  Populacao
        # ================================================================
        {
            "id": "u2",
            "titulo": "População",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Indicadores demográficos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "No censo de 2017, a população de "
                                 "Moçambique era de cerca de:",
                            "options": [
                                "28 milhões de habitantes",
                                "5 milhões de habitantes",
                                "100 milhões de habitantes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Numa vila nasceram 40 crianças por cada "
                                 "1000 habitantes e morreram 12. Qual é a "
                                 "taxa de crescimento natural, por mil?",
                            "a": "28",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada indicador ao que ele mede.",
                            "pairs": [
                                ["Taxa de natalidade", "Nascimentos por mil habitantes num ano"],
                                ["Taxa de mortalidade", "Mortes por mil habitantes num ano"],
                                ["Crescimento natural", "Natalidade menos mortalidade"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O planeamento familiar permite:",
                            "options": [
                                "Decidir quando e quantos filhos ter, com "
                                "saúde para a mãe e os filhos",
                                "Ter o máximo de filhos possível",
                                "Proibir os filhos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A mortalidade infantil baixa quando há:",
                            "options": [
                                "Vacinas, água limpa e postos de saúde",
                                "Mais festas",
                                "Menos escolas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Movimentos populacionais",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada movimento da população ao que "
                                 "ele é.",
                            "pairs": [
                                ["Movimento natural", "Nascimentos e mortes"],
                                ["Movimento migratório", "Entradas e saídas de pessoas"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um jovem do Niassa que vai trabalhar "
                                 "para as minas da África do Sul faz uma:",
                            "options": [
                                "Emigração",
                                "Imigração",
                                "Migração interna",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A saída do campo para as cidades "
                                 "chama-se:",
                            "options": ["Êxodo rural", "Emigração", "Crescimento natural"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma consequência das migrações para a "
                                 "saúde é:",
                            "options": [
                                "Maior risco de infecções de transmissão "
                                "sexual, como o HIV, longe da família",
                                "Menos doenças",
                                "Nenhuma",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As migrações têm como causa principal:",
                            "options": [
                                "A procura de trabalho e de melhores "
                                "condições de vida",
                                "O gosto por viajar",
                                "O clima",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Estrutura e distribuição da população",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A pirâmide etária de Moçambique tem a "
                                 "base larga porque:",
                            "options": [
                                "A população é muito jovem: quase metade "
                                "tem menos de 15 anos",
                                "Há muitos idosos",
                                "Não há crianças",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada sector de actividade ao seu "
                                 "exemplo.",
                            "pairs": [
                                ["Primário", "Agricultura e pesca"],
                                ["Secundário", "Indústria"],
                                ["Terciário", "Comércio, transportes e serviços"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada província à sua densidade de "
                                 "população.",
                            "pairs": [
                                ["Nampula e Zambézia", "As mais povoadas"],
                                ["Niassa", "A menos densa, com muita terra por habitante"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A população concentra-se no litoral e "
                                 "nos vales dos rios porque:",
                            "options": [
                                "Há água, solos férteis, portos e "
                                "estradas",
                                "Há mais frio",
                                "Não há terra",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A violência baseada no género:",
                            "options": [
                                "É crime, e denuncia-se à polícia ou ao "
                                "gabinete de atendimento",
                                "É um assunto privado da família",
                                "Só acontece nas cidades",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # III  Actividades Economicas em Mocambique
        # ================================================================
        {
            "id": "u3",
            "titulo": "Actividades económicas em Moçambique",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Agricultura e pecuária",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada tipo de agricultura ao que ela "
                                 "é.",
                            "pairs": [
                                ["De subsistência", "A família cultiva para comer, com enxada"],
                                ["De plantação", "Grandes áreas de uma cultura para vender"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "No tempo colonial, as plantações de "
                                 "chá, sisal e açúcar:",
                            "options": [
                                "Eram dos colonos e usavam trabalho "
                                "forçado dos moçambicanos",
                                "Eram dos camponeses",
                                "Não existiam",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada cultura à região onde mais se "
                                 "produz.",
                            "pairs": [
                                ["Castanha de caju", "Nampula"],
                                ["Chá", "Gurué, na Zambézia"],
                                ["Cana-de-açúcar", "Vales do Incomáti e do Búzi"],
                                ["Milho e feijão", "Planaltos do centro e do norte"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Os principais factores da produção "
                                 "agrícola são:",
                            "options": [
                                "O clima, o solo, a água, a terra e o "
                                "trabalho",
                                "Só a chuva",
                                "Só o dinheiro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de gado à zona onde mais "
                                 "se cria.",
                            "pairs": [
                                ["Bovino", "Sul: Gaza, Inhambane e Maputo"],
                                ["Caprino", "Todo o país, na criação familiar"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Pesca e silvicultura",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada tipo de pesca ao que ela é.",
                            "pairs": [
                                ["Artesanal", "Canoas e redes, perto da costa, para comer e vender"],
                                ["Industrial", "Barcos grandes, ao largo, para exportar"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O principal produto pesqueiro de "
                                 "exportação de Moçambique é:",
                            "options": ["O camarão", "A sardinha", "O bacalhau"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No lago Niassa pesca-se sobretudo:",
                            "options": [
                                "Peixe de água doce, como o chambo e a "
                                "usipa",
                                "Camarão",
                                "Atum",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Silvicultura é:",
                            "options": [
                                "O cultivo e a exploração das florestas",
                                "A criação de gado",
                                "A pesca no rio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para conservar as florestas de miombo "
                                 "do Niassa deve-se:",
                            "options": [
                                "Evitar as queimadas e cortar só com "
                                "licença, replantando",
                                "Queimar para limpar",
                                "Cortar tudo para vender",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A indústria",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada indústria ao seu tipo.",
                            "pairs": [
                                ["Mina de carvão", "Extractiva"],
                                ["Fábrica de cimento", "Transformadora pesada"],
                                ["Fábrica de refrescos", "Transformadora ligeira"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada indústria ao lugar onde está.",
                            "pairs": [
                                ["Alumínio da Mozal", "Maputo"],
                                ["Carvão", "Moatize"],
                                ["Gás natural", "Inhambane e Cabo Delgado"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A indústria transformadora:",
                            "options": [
                                "Transforma matérias-primas em produtos: "
                                "cimento, açúcar, cerveja",
                                "Tira minerais da terra",
                                "Planta árvores",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A indústria moçambicana concentra-se:",
                            "options": [
                                "Em Maputo, na Beira e em Nampula",
                                "Nas aldeias do interior",
                                "Só no Niassa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma fábrica que despeja resíduos no rio:",
                            "options": [
                                "Polui a água e mata os peixes: é impacto "
                                "ambiental",
                                "Ajuda os peixes",
                                "Não tem efeito",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Transportes, comunicações e comércio",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada corredor de transportes ao "
                                 "porto onde chega.",
                            "pairs": [
                                ["Corredor de Nacala", "Porto de Nacala, em Nampula"],
                                ["Corredor da Beira", "Porto da Beira, em Sofala"],
                                ["Corredor de Maputo", "Porto de Maputo"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A estrada que atravessa o país de sul a "
                                 "norte é a:",
                            "options": [
                                "Estrada Nacional número 1",
                                "Linha de Sena",
                                "Estrada do Rovuma",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para prevenir acidentes rodoviários:",
                            "options": [
                                "Cinto posto, sem álcool ao volante e "
                                "velocidade dentro do limite",
                                "Andar mais depressa",
                                "Buzinar muito",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada noção de comércio ao que ela "
                                 "é.",
                            "pairs": [
                                ["Oferta", "O que há para vender"],
                                ["Procura", "O que as pessoas querem comprar"],
                                ["Inflação", "A subida geral dos preços"],
                                ["Exportação", "Vender para fora do país"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Os principais produtos que Moçambique "
                                 "exporta são:",
                            "options": [
                                "Alumínio, carvão, gás, camarão e castanha "
                                "de caju",
                                "Automóveis e computadores",
                                "Petróleo refinado",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n5",
                    "titulo": "Turismo e educação financeira",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada espaço turístico ao seu tipo "
                                 "de turismo.",
                            "pairs": [
                                ["Bazaruto e Tofo", "De praia"],
                                ["Gorongosa e Reserva do Niassa", "De natureza"],
                                ["Ilha de Moçambique", "Cultural e histórico"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O turismo cria:",
                            "options": [
                                "Empregos, divisas e mercado para os "
                                "produtos locais",
                                "Só poluição",
                                "Nada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As danças, as línguas e as cerimónias "
                                 "de Moçambique são:",
                            "options": [
                                "Identidade cultural, que também atrai "
                                "turistas",
                                "Coisas do passado sem valor",
                                "Só para as cidades",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada noção de educação financeira "
                                 "ao que ela é.",
                            "pairs": [
                                ["Poupança", "Guardar parte do que se ganha"],
                                ["Investimento", "Pôr dinheiro num negócio para render"],
                                ["Crédito", "Dinheiro emprestado que se paga com juros"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Uma jovem poupa 150 meticais por mês. "
                                 "Quantos meticais tem ao fim de 12 meses?",
                            "a": "1800",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # IV  Mocambique e a SADC
        # ================================================================
        {
            "id": "u4",
            "titulo": "Moçambique e a SADC",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A África Austral e a SADC",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A África Austral é:",
                            "options": [
                                "A parte sul do continente africano",
                                "O norte de África",
                                "Uma ilha",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada país da África Austral à sua "
                                 "língua oficial.",
                            "pairs": [
                                ["Moçambique e Angola", "Português"],
                                ["Zâmbia e Zimbabué", "Inglês"],
                                ["Madagáscar", "Malgaxe e francês"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A SADC é:",
                            "options": [
                                "A Comunidade de Desenvolvimento da África "
                                "Austral",
                                "Um banco",
                                "Um partido político",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "A SADC foi criada em 1992, em Windhoek, "
                                 "a partir da organização de cooperação "
                                 "fundada em 1980. Quantos anos passaram "
                                 "entre uma e outra?",
                            "a": "12",
                        },
                        {
                            "t": "choice",
                            "q": "A sede da SADC fica em:",
                            "options": ["Gaborone, no Botsuana", "Maputo", "Pretória"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Integração regional, direitos humanos e democracia",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada área de cooperação da SADC ao "
                                 "seu exemplo.",
                            "pairs": [
                                ["Transportes", "Os corredores que ligam os portos ao interior"],
                                ["Comércio", "Livre circulação de mercadorias"],
                                ["Paz e segurança", "Mediação de conflitos"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Moçambique é importante na SADC "
                                 "porque:",
                            "options": [
                                "Os seus portos servem os países do "
                                "interior, como o Malawi, a Zâmbia e o "
                                "Zimbabué",
                                "É o país mais rico",
                                "Não tem costa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A xenofobia é:",
                            "options": [
                                "O ódio aos estrangeiros, contrário aos "
                                "direitos humanos",
                                "O amor à pátria",
                                "Uma doença",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa democracia:",
                            "options": [
                                "O povo escolhe os governantes em eleições "
                                "livres",
                                "Manda quem tem mais força",
                                "Não há leis",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A cultura de paz constrói-se:",
                            "options": [
                                "Com diálogo, tolerância e respeito pelas "
                                "diferenças",
                                "Com armas",
                                "Ignorando os conflitos",
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
