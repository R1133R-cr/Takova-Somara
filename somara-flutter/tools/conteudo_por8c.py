# -*- coding: utf-8 -*-
"""O curso de Portugues da 8a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Lingua Portuguesa -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024,
     pp. 34-53 ("Plano Tematico da 8a Classe"). Guardado em Documents\\
     planos da 5a classe\\Livros\\Programas INDE 1o Ciclo\\portugues.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

Quinze unidades do INDE, cinco no curso -- como na 7a
-----------------------------------------------------
O programa organiza a 8a em QUINZE unidades: os mesmos cinco tipos de
texto a repetirem-se nos tres trimestres, e o terceiro trimestre e em boa
parte revisao (as unidades XII, XIII e XIV dizem-no por escrito). Corta-se
por tipo de texto, pela razao da 7a: quem abre a app para estudar "a
acta" quer a acta toda.

    u1 Normativos      I + VI + XI     Regulamento de Avaliacao;
                                       concordancia nominal; imperativo e
                                       infinitivo; voz activa e passiva;
                                       coordenadas disjuntivas
    u2 Administrativos II + VII + XII  convocatoria; concordancia verbal;
                                       conjuntivo; acta; tempos compostos;
                                       formas de tratamento
    u3 Jornalisticos   III + VIII      noticia; adverbios; numerais;
                       + XIII          anuncios classificados; complementos
                                       circunstanciais; preposicoes;
                                       acentuacao
    u4 Multiuso        IV + IX + XIV   texto expositivo; transitivos e
                                       intransitivos; sujeito e
                                       complementos; condicional; relato;
                                       dizer, pedir, ouvir; subordinadas
                                       temporais e condicionais
    u5 Literarios      V + X + XV      lenda e mito; tempo cronologico e
                                       psicologico; retrato; ir, vir,
                                       medir; poema; verso e estrofe;
                                       comparacao, metafora, hiperbole;
                                       Rui de Noronha e Marcelino dos
                                       Santos; drama; discurso directo e
                                       indirecto

Correr a partir de somara-flutter/:
    python tools/conteudo_por8c.py            # so mostra
    python tools/conteudo_por8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Língua Portuguesa — Ensino "
    "Secundário, 1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, "
    "pp. 34-53. As quinze unidades do programa juntam-se por tipo de texto "
    "em cinco; os conteúdos são os do programa e os exercícios foram "
    "escritos a partir deles, porque um programa de ensino não traz "
    "exercícios e não há livro do aluno da 8ª classe publicado."
)

CURSO = {
    "id": "por-8c",
    "disciplina": "Português",
    "classe": "8ª classe",
    "tag": "POR",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # u1  Textos normativos  (INDE: unidades I, VI e XI)
        # ================================================================
        {
            "id": "u1",
            "titulo": "Textos normativos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O regulamento de avaliação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um regulamento de avaliação é um texto:",
                            "options": [
                                "Normativo: diz o que se deve fazer",
                                "Literário: conta uma história",
                                "Jornalístico: dá uma notícia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A linguagem de um regulamento é:",
                            "options": [
                                "Clara, objectiva e impessoal",
                                "Poética e cheia de imagens",
                                "Familiar, como entre amigos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na mancha gráfica de um regulamento "
                                 "aparecem:",
                            "options": [
                                "Artigos numerados, uns a seguir aos outros",
                                "Versos e estrofes",
                                "Um título e falas de personagens",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O aluno deve apresentar-se à prova com o "
                                 "cartão de estudante.» Esta frase:",
                            "options": [
                                "Impõe um dever",
                                "Conta um acontecimento",
                                "Faz um pedido",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "«Os alunos devem entregar o trabalho até "
                                 "sexta-feira.» Escreve o verbo que indica "
                                 "obrigação.",
                            "a": "devem",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Concordância nominal, imperativo e infinitivo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Qual frase está certa quanto à "
                                 "concordância em género e número?",
                            "options": [
                                "As provas escritas são obrigatórias.",
                                "As provas escrito são obrigatórias.",
                                "As provas escritas é obrigatória.",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Entrega o teste ao professor.» O verbo "
                                 "«entrega» está no modo:",
                            "options": ["Imperativo", "Indicativo", "Conjuntivo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«É proibido copiar durante a prova.» O "
                                 "verbo «copiar» está no:",
                            "options": ["Infinitivo", "Imperativo", "Gerúndio"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Completa com o adjectivo a concordar: «Os "
                                 "resultados ___ saem em Dezembro.» (final)",
                            "a": "finais",
                        },
                        {
                            "t": "choice",
                            "q": "Qual frase usa o imperativo para dar uma "
                                 "ordem a várias pessoas?",
                            "options": [
                                "Sentem-se e leiam as instruções.",
                                "Vocês sentaram-se.",
                                "Eles vão sentar-se.",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Voz passiva e orações coordenadas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«O director aprovou o regulamento.» Na "
                                 "voz passiva fica:",
                            "options": [
                                "O regulamento foi aprovado pelo director.",
                                "O regulamento aprovou o director.",
                                "O director foi aprovado pelo regulamento.",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «O regulamento foi aprovado pelo "
                                 "director», o agente da passiva é:",
                            "options": [
                                "pelo director",
                                "o regulamento",
                                "foi aprovado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Estudas ou reprovas.» A oração ligada por "
                                 "«ou» é coordenada:",
                            "options": ["Disjuntiva", "Copulativa", "Adversativa"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas conjunções é coordenativa "
                                 "disjuntiva?",
                            "options": ["ou", "e", "mas"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A prova foi corrigida pela professora.» "
                                 "Na voz activa:",
                            "options": [
                                "A professora corrigiu a prova.",
                                "A prova corrigiu a professora.",
                                "A professora foi corrigida pela prova.",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # u2  Textos administrativos  (INDE: unidades II, VII e XII)
        # ================================================================
        {
            "id": "u2",
            "titulo": "Textos administrativos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A convocatória e a concordância verbal",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma convocatória serve para:",
                            "options": [
                                "Chamar pessoas a uma reunião, com data, "
                                "hora e local",
                                "Contar uma história",
                                "Anunciar uma venda",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O que não pode faltar numa convocatória?",
                            "options": [
                                "O dia, a hora e o local da reunião",
                                "Uma rima",
                                "O nome do herói",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em qual frase o verbo concorda com o "
                                 "sujeito?",
                            "options": [
                                "Os pais foram convocados para a reunião.",
                                "Os pais foi convocados para a reunião.",
                                "Os pais fomos convocados para a reunião.",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Tu e o teu irmão ___ à reunião.» A forma "
                                 "certa é:",
                            "options": ["vão", "vai", "vou"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Completa com o verbo estar: «Ontem, nós "
                                 "___ na reunião.»",
                            "a": "estivemos",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A acta",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A acta é o texto que:",
                            "options": [
                                "Regista o que se passou numa reunião",
                                "Convoca para uma reunião",
                                "Anuncia um produto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A acta escreve-se:",
                            "options": [
                                "Depois da reunião, com o que foi decidido",
                                "Antes da reunião, com o que se vai decidir",
                                "Durante a aula de Português",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na estrutura de uma acta aparecem:",
                            "options": [
                                "A data, os presentes, os assuntos e as "
                                "decisões",
                                "Versos e estrofes",
                                "Um pedido de desculpa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa acta, a linguagem deve ser:",
                            "options": ["Formal e objectiva", "Familiar", "Poética"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quem assina a acta no fim?",
                            "options": [
                                "O secretário e o presidente da reunião",
                                "Só os alunos",
                                "Ninguém",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O modo conjuntivo e os tempos compostos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Espero que os pais venham à reunião.» O "
                                 "verbo «venham» está no modo:",
                            "options": ["Conjuntivo", "Indicativo", "Imperativo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual forma está no presente do conjuntivo?",
                            "options": ["que eu fale", "eu falo", "eu falei"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Quando cheguei, a reunião já tinha "
                                 "começado.» «Tinha começado» é o:",
                            "options": [
                                "Pretérito mais-que-perfeito composto",
                                "Presente do indicativo",
                                "Futuro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um tempo composto forma-se com:",
                            "options": [
                                "O auxiliar ter ou haver e um particípio",
                                "Dois verbos no infinitivo",
                                "Um verbo e um adjectivo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa convocatória dirigida ao director, a "
                                 "forma de tratamento adequada é:",
                            "options": [
                                "Excelentíssimo Senhor Director",
                                "Olá, chefe",
                                "Tu, director",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # u3  Textos jornalisticos  (INDE: unidades III, VIII e XIII)
        # ================================================================
        {
            "id": "u3",
            "titulo": "Textos jornalísticos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A notícia e as suas perguntas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma notícia responde às perguntas:",
                            "options": [
                                "Quem? O quê? Quando? Onde? Como? Porquê?",
                                "Rima? Verso? Estrofe?",
                                "Herói? Vilão? Final feliz?",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O primeiro parágrafo de uma notícia:",
                            "options": [
                                "Resume o essencial do acontecimento",
                                "Dá a opinião do jornalista",
                                "É sempre um poema",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Chuvas fortes fecharam a estrada de "
                                 "Lichinga a Cuamba na terça-feira.» O "
                                 "«quando» é:",
                            "options": [
                                "na terça-feira",
                                "chuvas fortes",
                                "a estrada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na mesma notícia das chuvas, o «onde» é:",
                            "options": [
                                "a estrada de Lichinga a Cuamba",
                                "na terça-feira",
                                "chuvas fortes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A linguagem de uma notícia deve ser:",
                            "options": [
                                "Clara, objectiva e sem opiniões",
                                "Cheia de rimas",
                                "Em primeira pessoa, com sentimentos",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Advérbios, numerais e complementos "
                              "circunstanciais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Em «A escola abriu ontem», «ontem» é "
                                 "advérbio de:",
                            "options": ["Tempo", "Lugar", "Modo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «Os alunos entraram devagar», «devagar» "
                                 "é advérbio de:",
                            "options": ["Modo", "Tempo", "Lugar"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Vinte» é um numeral cardinal. «Vigésimo» "
                                 "é um numeral:",
                            "options": ["Ordinal", "Cardinal", "Colectivo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «O jogo começou às quinze horas no "
                                 "campo da escola», o complemento "
                                 "circunstancial de lugar é:",
                            "options": [
                                "no campo da escola",
                                "às quinze horas",
                                "o jogo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Escreve por extenso o numeral ordinal que "
                                 "corresponde a 3.",
                            "a": "terceiro",
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Classificados, preposições e acentuação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um anúncio classificado é:",
                            "options": [
                                "Um texto curto que oferece ou procura "
                                "alguma coisa",
                                "Uma notícia longa",
                                "Um poema",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Vende-se bicicleta em bom estado. "
                                 "Contactar a Amina.» A linguagem é:",
                            "options": [
                                "Curta e directa, para poupar espaço",
                                "Longa e descritiva",
                                "Poética",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «Vou de Lichinga para Cuamba», as "
                                 "preposições são:",
                            "options": [
                                "de e para",
                                "vou e Cuamba",
                                "Lichinga e Cuamba",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual palavra está bem acentuada?",
                            "options": ["lâmpada", "lampada", "lampáda"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As palavras esdrúxulas, com a sílaba "
                                 "tónica na antepenúltima:",
                            "options": [
                                "Acentuam-se sempre",
                                "Nunca se acentuam",
                                "Só se acentuam no plural",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # u4  Textos multiuso  (INDE: unidades IV, IX e XIV)
        # ================================================================
        {
            "id": "u4",
            "titulo": "Textos multiuso",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O texto expositivo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um texto expositivo serve para:",
                            "options": [
                                "Explicar um assunto de forma clara e "
                                "organizada",
                                "Contar uma aventura",
                                "Convencer alguém a comprar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um texto de um manual de Ciências é um "
                                 "texto:",
                            "options": [
                                "Didáctico e expositivo",
                                "Literário",
                                "Administrativo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Num texto expositivo, as ideias "
                                 "organizam-se:",
                            "options": [
                                "Do geral para o particular, com exemplos",
                                "Ao acaso",
                                "Em versos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A linguagem de um texto científico é:",
                            "options": [
                                "Objectiva e com termos precisos",
                                "Cheia de sentimentos",
                                "Familiar",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Verbos transitivos, sujeito e complementos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Em «A Amina leu o livro», o verbo «leu» é:",
                            "options": [
                                "Transitivo: precisa de complemento directo",
                                "Intransitivo",
                                "Impessoal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «O bebé dormiu», o verbo «dormiu» é:",
                            "options": [
                                "Intransitivo",
                                "Transitivo directo",
                                "Transitivo indirecto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «A Amina leu o livro», o complemento "
                                 "directo é:",
                            "options": ["o livro", "a Amina", "leu"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «O professor deu um prémio ao aluno», "
                                 "o complemento indirecto é:",
                            "options": ["ao aluno", "um prémio", "o professor"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «Os alunos escreveram um relato», o "
                                 "sujeito é:",
                            "options": ["os alunos", "um relato", "escreveram"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Relato, condicional e orações subordinadas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um relato de acontecimentos conta:",
                            "options": [
                                "Factos reais, pela ordem em que "
                                "aconteceram",
                                "Uma lenda",
                                "Um sonho em versos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Eu iria à festa se pudesse.» O verbo "
                                 "«iria» está no:",
                            "options": [
                                "Condicional",
                                "Presente",
                                "Pretérito perfeito",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Quando a chuva parou, saímos.» A oração "
                                 "«quando a chuva parou» é subordinada:",
                            "options": ["Temporal", "Condicional", "Causal"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Se estudares, passas.» A oração «se "
                                 "estudares» é subordinada:",
                            "options": ["Condicional", "Temporal", "Final"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Completa com o verbo dizer: «Ontem ele ___ "
                                 "a verdade.»",
                            "a": "disse",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # u5  Textos literarios  (INDE: unidades V, X e XV)
        # ================================================================
        {
            "id": "u5",
            "titulo": "Textos literários",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Lenda e mito: o tempo e as personagens",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma lenda é:",
                            "options": [
                                "Uma narrativa tradicional que mistura "
                                "factos reais e imaginação",
                                "Um texto de leis",
                                "Uma notícia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um mito serve, sobretudo, para:",
                            "options": [
                                "Explicar a origem do mundo ou de um "
                                "fenómeno",
                                "Vender um produto",
                                "Convocar uma reunião",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O tempo psicológico de uma narrativa é:",
                            "options": [
                                "O tempo como a personagem o sente",
                                "O tempo do relógio e do calendário",
                                "O tempo que se leva a ler",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O Ali era alto e tinha os olhos "
                                 "escuros.» Este retrato é:",
                            "options": [
                                "Físico, por caracterização directa",
                                "Psicológico",
                                "Do espaço",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quando o narrador pára a acção para "
                                 "descrever um lugar, há um momento de:",
                            "options": ["Pausa", "Avanço", "Diálogo"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Completa com o verbo vir: «Ontem eu ___ "
                                 "cedo para casa.»",
                            "a": "vim",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O poema: verso, estrofe e recursos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Cada linha de um poema chama-se:",
                            "options": ["Verso", "Estrofe", "Parágrafo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um grupo de versos separado dos outros "
                                 "por um espaço em branco é:",
                            "options": ["Uma estrofe", "Um capítulo", "Uma rima"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Os teus olhos são duas estrelas.» O "
                                 "recurso estilístico é:",
                            "options": ["Metáfora", "Comparação", "Hipérbole"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Chorei um rio de lágrimas.» O recurso "
                                 "estilístico é:",
                            "options": ["Hipérbole", "Comparação", "Metáfora"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Rui de Noronha e Marcelino dos Santos "
                                 "foram:",
                            "options": [
                                "Poetas moçambicanos",
                                "Jogadores de futebol",
                                "Presidentes de Portugal",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O drama e o discurso directo e indirecto",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um texto dramático é escrito para:",
                            "options": [
                                "Ser representado num palco",
                                "Ser cantado",
                                "Ser publicado num jornal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Num texto dramático, as indicações sobre "
                                 "gestos e cenário chamam-se:",
                            "options": ["Didascálias", "Estrofes", "Rimas"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A Amina disse: — Vou à escola.» Este é "
                                 "discurso:",
                            "options": ["Directo", "Indirecto", "Livre"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No discurso indirecto, «A Amina disse: — "
                                 "Vou à escola.» fica:",
                            "options": [
                                "A Amina disse que ia à escola.",
                                "A Amina disse: vou à escola.",
                                "A Amina vai à escola.",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao falar com um professor numa peça, a "
                                 "personagem usa a forma de tratamento:",
                            "options": ["Senhor professor", "Tu, pá", "Ó tipo"],
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
            print(f"       {n['id']}  {n['titulo']:<46}"
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

    # A seguir a Matematica da 8a, para a 8a ficar com a mesma ordem de
    # disciplinas da 7a.
    onde = ids.index("mat-8c") + 1
    dados["cursos"].insert(onde, CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta as entradas ao tools/materia_texto.py "
          "e corre python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
