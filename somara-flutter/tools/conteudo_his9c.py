# -*- coding: utf-8 -*-
"""O curso de Historia da 9a classe -- o seculo XX, e Mocambique nele.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Historia -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, 9a classe,
     pp. 35-45. Guardado em Documents\\planos da 5a classe\\Livros\\
     Programas INDE 1o Ciclo\\historia.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As quatro unidades tematicas, pela ordem do programa
----------------------------------------------------
    1  As contradicoes imperialistas ate ao fim da I Guerra Mundial
       (as potencias e os blocos; a guerra e as suas fases; Africa na
       guerra; Versalhes e a Sociedade das Nacoes; a ocupacao efectiva e
       o sistema colonial em Mocambique; a resistencia)
    2  O mundo entre a I e o fim da II Guerra Mundial, 1918-1945
       (a URSS; a crise de 1929; fascismo, nazismo e o Estado Novo; a
       II Guerra; a ONU)
    3  O Movimento de Libertacao e a Independencia Nacional de Mocambique
       (o Estado Novo nas colonias; UDENAMO, MANU e UNAMI; a FRELIMO e a
       luta armada; as zonas libertadas; Lusaka e a Independencia)
    4  Mocambique e o Mundo entre a confrontacao e o desanuviamento
       (a Guerra Fria; os Nao-Alinhados; o apartheid; a paz em
       Mocambique: Roma, a Constituicao de 1990, as eleicoes)

Quatro unidades, catorze aulas.

Correr a partir de somara-flutter/:
    python tools/conteudo_his9c.py            # so mostra
    python tools/conteudo_his9c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de História — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, 9ª classe, pp. 35-45. "
    "As quatro unidades temáticas e os conteúdos são do programa; os "
    "exercícios foram escritos a partir deles, porque um programa de ensino "
    "não traz exercícios e não há livro do aluno da 9ª classe publicado."
)

CURSO = {
    "id": "his-9c",
    "disciplina": "História",
    "classe": "9ª classe",
    "tag": "HIS",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # 1  As contradicoes imperialistas ate ao fim da I Guerra Mundial
        # ================================================================
        {
            "id": "u1",
            "titulo": "As contradições imperialistas e a I Guerra Mundial",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "As potências e os blocos militares",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "No fim do século XIX, as potências "
                                 "europeias disputavam:",
                            "options": [
                                "Colónias, mercados e matérias-primas",
                                "Os melhores poetas",
                                "O direito de votar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada bloco militar aos seus países.",
                            "pairs": [
                                ["Tríplice Entente", "Inglaterra, França e Rússia"],
                                ["Tríplice Aliança", "Alemanha, Áustria-Hungria e Itália"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A corrida aos armamentos foi:",
                            "options": [
                                "As potências a fabricar cada vez mais "
                                "armas e navios, à espera da guerra",
                                "Uma competição desportiva",
                                "Uma feira de comércio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "O atentado de Sarajevo, que acendeu a I "
                                 "Guerra Mundial, foi a 28 de Junho de que "
                                 "ano?",
                            "a": "1914",
                        },
                        {
                            "t": "choice",
                            "q": "Imperialismo é:",
                            "options": [
                                "A política de um país dominar outros "
                                "territórios e povos",
                                "O governo de um imperador chinês",
                                "Uma religião",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A guerra e as suas fases",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada fase da I Guerra Mundial à sua "
                                 "característica.",
                            "pairs": [
                                ["Primeira fase", "Guerra de movimentos: avanços rápidos"],
                                ["Segunda fase", "Guerra de trincheiras: frentes paradas"],
                                ["Terceira fase", "Regresso aos movimentos, até ao fim"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Em que ano entraram os Estados Unidos na "
                                 "I Guerra Mundial?",
                            "a": "1917",
                        },
                        {
                            "t": "choice",
                            "q": "A Rússia saiu da guerra em 1917 porque:",
                            "options": [
                                "A Revolução Socialista de Outubro tomou o "
                                "poder e fez a paz",
                                "Tinha ganho a guerra",
                                "Não tinha exército",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os africanos participaram na I Guerra "
                                 "Mundial:",
                            "options": [
                                "Como soldados e carregadores das potências "
                                "coloniais, muitas vezes à força",
                                "Como generais das potências",
                                "Não participaram",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em Moçambique, a I Guerra Mundial "
                                 "trouxe:",
                            "options": [
                                "Combates no norte, com a invasão alemã "
                                "vinda da Tanzânia",
                                "Paz e prosperidade",
                                "Nada: ficou de fora",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O fim da guerra e a Sociedade das Nações",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "O armistício que acabou com a I Guerra "
                                 "Mundial foi assinado a 11 de Novembro de "
                                 "que ano?",
                            "a": "1918",
                        },
                        {
                            "t": "choice",
                            "q": "O Tratado de Versalhes:",
                            "options": [
                                "Impôs à Alemanha a culpa da guerra, "
                                "perdas de território e pesadas reparações",
                                "Deu a vitória à Alemanha",
                                "Criou a União Europeia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Sociedade das Nações foi criada para:",
                            "options": [
                                "Resolver os conflitos entre países pela "
                                "via pacífica",
                                "Preparar a guerra seguinte",
                                "Organizar os Jogos Olímpicos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada consequência da I Guerra "
                                 "Mundial ao seu tipo.",
                            "pairs": [
                                ["Milhões de mortos e feridos", "Demográfica"],
                                ["Cidades e fábricas destruídas", "Económica"],
                                ["Impérios desfeitos e novos países", "Política"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Para África, a I Guerra Mundial "
                                 "significou:",
                            "options": [
                                "As colónias alemãs repartidas pelos "
                                "vencedores",
                                "A independência de todos os países",
                                "O fim do colonialismo",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "A ocupação efectiva e o sistema colonial",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada forma de administração "
                                 "colonial ao que ela era.",
                            "pairs": [
                                ["Directa", "Funcionários europeus a mandar em tudo"],
                                ["Indirecta", "Chefes africanos a governar sob controlo europeu"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "As companhias monopolistas, como a "
                                 "Companhia de Moçambique e a do Niassa:",
                            "options": [
                                "Exploravam grandes territórios e o seu "
                                "trabalho em vez do Estado português",
                                "Eram escolas",
                                "Defendiam os camponeses",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada forma de exploração colonial "
                                 "em Moçambique ao que ela era.",
                            "pairs": [
                                ["Chibalo", "Trabalho forçado"],
                                ["Imposto de palhota", "Imposto pago por cada casa"],
                                ["Culturas obrigatórias", "Algodão e arroz impostos aos camponeses"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Uma particularidade do colonialismo "
                                 "português foi:",
                            "options": [
                                "Ser um país pobre a explorar as colónias "
                                "com trabalho forçado e a exportar "
                                "trabalhadores para as minas",
                                "Dar a independência cedo",
                                "Não ter colónias em África",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada resistência à ocupação ao seu "
                                 "líder ou lugar.",
                            "pairs": [
                                ["Gaza, 1895", "Ngungunhane"],
                                ["Barué, 1917", "Makombe"],
                                ["Etiópia, 1896", "Menelik vence os italianos em Adua"],
                            ],
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 2  O mundo entre a I e o fim da II Guerra Mundial
        # ================================================================
        {
            "id": "u2",
            "titulo": "O mundo entre as duas guerras e a II Guerra Mundial",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A URSS e a crise de 1929",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Em que ano foi a Revolução Socialista de "
                                 "Outubro, na Rússia?",
                            "a": "1917",
                        },
                        {
                            "t": "choice",
                            "q": "A União das Repúblicas Socialistas "
                                 "Soviéticas foi:",
                            "options": [
                                "O Estado socialista nascido da revolução "
                                "russa, com a economia nas mãos do Estado",
                                "Uma colónia inglesa",
                                "Um reino",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Em que ano rebentou a crise económica "
                                 "mundial, com a queda da bolsa de Nova "
                                 "Iorque?",
                            "a": "1929",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada consequência da crise de 1929 "
                                 "ao lugar.",
                            "pairs": [
                                ["Fábricas fechadas e milhões de desempregados", "Estados Unidos e Europa"],
                                ["Preços do algodão e do açúcar a cair", "Moçambique e África"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Roosevelt combateu a crise com:",
                            "options": [
                                "O Estado a criar obras públicas e "
                                "empregos: o New Deal",
                                "Uma nova guerra",
                                "O fim dos impostos",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Fascismo, nazismo e o Estado Novo",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada regime ditatorial ao seu país "
                                 "e chefe.",
                            "pairs": [
                                ["Fascismo", "Itália, Mussolini"],
                                ["Nazismo", "Alemanha, Hitler"],
                                ["Estado Novo", "Portugal, Salazar"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Os regimes ditatoriais dos anos 30:",
                            "options": [
                                "Acabaram com as liberdades e "
                                "perseguiram quem discordava",
                                "Fizeram eleições livres",
                                "Deram a independência às colónias",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O nazismo alemão defendia:",
                            "options": [
                                "A superioridade de uma raça e o ódio aos "
                                "judeus, que levou ao Holocausto",
                                "A igualdade de todos os povos",
                                "A paz com os vizinhos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em Moçambique, a política fascista de "
                                 "Portugal:",
                            "options": [
                                "Apertou o trabalho forçado, as culturas "
                                "obrigatórias e a censura",
                                "Trouxe liberdade",
                                "Acabou com o colonialismo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Corporativismo foi o nome dado ao "
                                 "sistema económico e social:",
                            "options": [
                                "Do Estado Novo português",
                                "Da União Soviética",
                                "Dos Estados Unidos",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A II Guerra Mundial e a ONU",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "A II Guerra Mundial começou com a "
                                 "invasão da Polónia pela Alemanha, em que "
                                 "ano?",
                            "a": "1939",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada causa da II Guerra Mundial ao "
                                 "seu tipo.",
                            "pairs": [
                                ["A humilhação de Versalhes e a crise", "Económica e política"],
                                ["O expansionismo de Hitler", "Político-militar"],
                                ["O nazismo e o fascismo", "Ideológica"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "África participou na II Guerra Mundial:",
                            "options": [
                                "Com soldados africanos nos exércitos "
                                "coloniais e com as suas matérias-primas",
                                "Como país independente",
                                "Só a assistir",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "A II Guerra Mundial acabou em que ano, "
                                 "com a rendição da Alemanha e do Japão?",
                            "a": "1945",
                        },
                        {
                            "t": "choice",
                            "q": "A Organização das Nações Unidas, criada "
                                 "em 1945, tem como fim:",
                            "options": [
                                "Manter a paz e a cooperação entre os "
                                "povos",
                                "Governar todos os países",
                                "Fabricar armas",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 3  O Movimento de Libertacao e a Independencia Nacional
        # ================================================================
        {
            "id": "u3",
            "titulo": "A luta de libertação e a Independência de Moçambique",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O Estado Novo e o nascimento do nacionalismo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "No Estado Novo de Salazar, Moçambique "
                                 "era:",
                            "options": [
                                "Uma colónia chamada «província "
                                "ultramarina», sem direitos para os "
                                "moçambicanos",
                                "Um país independente",
                                "Uma república",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O estatuto do indigenato dividia a "
                                 "população em:",
                            "options": [
                                "Indígenas, sem direitos de cidadão, e "
                                "assimilados e colonos",
                                "Ricos e pobres",
                                "Norte e sul",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "O massacre de Mueda, em que o exército "
                                 "colonial disparou sobre uma manifestação "
                                 "pacífica, foi a 16 de Junho de que ano?",
                            "a": "1960",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada movimento nacionalista que "
                                 "antecedeu a FRELIMO ao lugar onde nasceu.",
                            "pairs": [
                                ["UDENAMO", "Salisbúria, na Rodésia do Sul"],
                                ["MANU", "Tanganhica, entre os macondes"],
                                ["UNAMI", "Malawi"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "As primeiras manifestações nacionalistas "
                                 "em Moçambique foram:",
                            "options": [
                                "Greves de estivadores, associações de "
                                "trabalhadores e jornais como O Brado "
                                "Africano",
                                "Eleições",
                                "Partidos legais",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A FRELIMO e a luta armada",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "A FRELIMO foi fundada em Dar es Salaam, "
                                 "a 25 de Junho de que ano?",
                            "a": "1962",
                        },
                        {
                            "t": "choice",
                            "q": "O primeiro presidente da FRELIMO foi:",
                            "options": [
                                "Eduardo Mondlane",
                                "Samora Machel",
                                "Joaquim Chissano",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "A luta armada de libertação nacional "
                                 "começou a 25 de Setembro de que ano, em "
                                 "Chai, Cabo Delgado?",
                            "a": "1964",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada figura da luta de libertação ao "
                                 "seu papel.",
                            "pairs": [
                                ["Eduardo Mondlane", "Fundador e primeiro presidente da FRELIMO"],
                                ["Samora Machel", "Comandante da luta armada e primeiro Presidente"],
                                ["Josina Machel", "Combatente e responsável pelos assuntos sociais"],
                                ["Filipe Samuel Magaia", "Primeiro comandante militar"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Onde foram os primeiros centros de "
                                 "preparação político-militar da FRELIMO?",
                            "options": [
                                "Na Tanzânia, em Kongwa e Nachingwea",
                                "Em Lisboa",
                                "Em Maputo",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "As zonas libertadas, Lusaka e a Independência",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As zonas libertadas eram:",
                            "options": [
                                "Áreas de Cabo Delgado, Niassa e Tete onde "
                                "a FRELIMO governava, com escolas e postos "
                                "de saúde",
                                "Cidades portuguesas",
                                "Ilhas do Índico",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Nas zonas libertadas nasceram novas "
                                 "relações sociais:",
                            "options": [
                                "Produção colectiva, escolas para todos e "
                                "a mulher na luta",
                                "O trabalho forçado",
                                "O imposto de palhota",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Os Acordos de Lusaka, que reconheceram o "
                                 "direito de Moçambique à independência, "
                                 "foram assinados a 7 de Setembro de que "
                                 "ano?",
                            "a": "1974",
                        },
                        {
                            "t": "input",
                            "q": "Em que ano foi proclamada a "
                                 "Independência Nacional, a 25 de Junho?",
                            "a": "1975",
                        },
                        {
                            "t": "choice",
                            "q": "A Constituição da República Popular de "
                                 "Moçambique, de 1975:",
                            "options": [
                                "Fez de Moçambique um Estado independente "
                                "e acabou com a discriminação colonial",
                                "Manteve o indigenato",
                                "Entregou o país a Portugal",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 4  Mocambique e o Mundo entre a confrontacao e o desanuviamento
        # ================================================================
        {
            "id": "u4",
            "titulo": "Da Guerra Fria à paz em Moçambique",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A Guerra Fria",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Guerra Fria foi:",
                            "options": [
                                "O confronto entre os Estados Unidos e a "
                                "URSS sem guerra directa entre eles",
                                "Uma guerra no Pólo Norte",
                                "Uma guerra entre Portugal e Espanha",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada bloco militar da Guerra Fria ao "
                                 "seu líder.",
                            "pairs": [
                                ["NATO", "Estados Unidos"],
                                ["Pacto de Varsóvia", "União Soviética"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O Movimento dos Não-Alinhados juntou:",
                            "options": [
                                "Países do Terceiro Mundo que não queriam "
                                "pertencer a nenhum dos blocos",
                                "Os aliados dos Estados Unidos",
                                "Os aliados da URSS",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O regime do apartheid, na África do Sul, "
                                 "desestabilizou Moçambique:",
                            "options": [
                                "Apoiando a guerra contra o Governo, no "
                                "contexto da Guerra Fria",
                                "Enviando professores",
                                "Comprando o caju",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "A queda do muro de Berlim, que marcou o "
                                 "fim da Guerra Fria, foi em que ano?",
                            "a": "1989",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Os caminhos da paz em Moçambique",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A guerra que Moçambique viveu depois da "
                                 "Independência foi entre:",
                            "options": [
                                "O Governo da FRELIMO e a RENAMO",
                                "Moçambique e a Tanzânia",
                                "Portugal e a FRELIMO",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "O Acordo Geral de Paz de Roma foi "
                                 "assinado a 4 de Outubro de que ano?",
                            "a": "1992",
                        },
                        {
                            "t": "choice",
                            "q": "As negociações de Roma foram:",
                            "options": [
                                "Conversas entre o Governo e a RENAMO, com "
                                "mediação, até ao acordo de paz",
                                "Uma batalha",
                                "Um campeonato",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Constituição de 1990 trouxe:",
                            "options": [
                                "O multipartidarismo e as liberdades: "
                                "vários partidos e eleições",
                                "O partido único",
                                "O regresso do colonialismo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "As primeiras eleições gerais "
                                 "multipartidárias de Moçambique foram em "
                                 "que ano?",
                            "a": "1994",
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "As eleições e a cultura de paz",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada eleição ao que ela escolhe.",
                            "pairs": [
                                ["Eleições gerais", "O Presidente da República e a Assembleia"],
                                ["Eleições autárquicas", "Os presidentes e assembleias dos municípios"],
                                ["Eleições provinciais", "As assembleias e os governadores das províncias"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "De quantos em quantos anos se fazem as "
                                 "eleições gerais em Moçambique?",
                            "a": "5",
                        },
                        {
                            "t": "choice",
                            "q": "Numa eleição livre, o voto é:",
                            "options": [
                                "Secreto e de cada cidadão, sem ameaças",
                                "Público e obrigatório num partido",
                                "Só dos homens",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A cultura de paz aprende-se:",
                            "options": [
                                "A resolver os conflitos pelo diálogo, na "
                                "escola e na comunidade",
                                "Com armas",
                                "Ignorando os outros",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Coexistência pacífica quer dizer:",
                            "options": [
                                "Países com sistemas diferentes a viverem "
                                "lado a lado sem guerra",
                                "Todos terem o mesmo governo",
                                "Não haver fronteiras",
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
