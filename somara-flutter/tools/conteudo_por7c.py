# -*- coding: utf-8 -*-
"""O curso de Portugues da 7a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Lingua Portuguesa -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024.
     Descarregado do educador.mozestuda.com.

Como o de Matematica da 7a, e um PROGRAMA e nao um livro do aluno: traz os
objectivos, os conteudos e a carga horaria, e nao traz exercicios. Fica
dito no campo `fonte`.

Quinze unidades do INDE, cinco no curso
---------------------------------------
O programa organiza a 7a classe em QUINZE unidades tematicas, que sao
cinco tipos de texto a repetirem-se nos tres trimestres:

    1o trimestre    I  Normativos   II Administrativos  III Jornalisticos
                   IV  Multiuso      V Literarios
    2o trimestre   VI  Normativos  VII Administrativos VIII Jornalisticos
                   IX  Multiuso      X Literarios
    3o trimestre   XI  Normativos  XII Administrativos XIII Jornalisticos
                  XIV  Multiuso     XV Literarios

Aqui juntam-se por TIPO DE TEXTO, e nao por trimestre: cinco unidades de
tres niveis cada. A taxonomia continua a ser a do INDE -- o que muda e o
eixo por que se corta.

A razao e pratica. Uma crianca que abre a app para estudar "a noticia"
quer a noticia toda, e nao um terco dela em Marco, outro em Julho e o
resto em Outubro. E o terceiro trimestre do programa e em boa parte
revisao dos dois primeiros (as unidades XII e XIII dizem-no por escrito),
o que daria niveis quase repetidos se se seguisse o calendario.

O que cada unidade do curso junta:

    u1 Normativos      I + VI + XI    regulamento escolar; sujeito;
                                      preposicoes; formacao de palavras;
                                      adverbios; formas de tratamento
    u2 Administrativos II + VII + XII aviso; tempos do indicativo;
                                      participio passado; voz passiva;
                                      verbos irregulares
    u3 Jornalisticos   III + VIII     noticia; fait divers; formas de
                       + XIII         frase; complementos
                                      circunstanciais; conjuncoes
                                      coordenativas; acentuacao
    u4 Multiuso        IV + IX + XIV  manuais escolares; texto
                                      didactico; pronomes; modos verbais
    u5 Literarios      V + X + XV     conto e fabula; grau do adjectivo;
                                      homonimas e paronimas; composicao;
                                      texto dramatico; discurso directo
                                      e indirecto

Correr a partir de somara-flutter/:
    python tools/conteudo_por7c.py            # so mostra
    python tools/conteudo_por7c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Língua Portuguesa — Ensino "
    "Secundário, 1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024. As "
    "quinze unidades temáticas do programa estão agrupadas por tipo de "
    "texto, que é a taxonomia do próprio programa; os exercícios foram "
    "escritos a partir dos conteúdos, porque um programa de ensino não "
    "traz exercícios e não há livro do aluno da 7ª classe publicado."
)

CURSO = {
    "id": "por-7c",
    "disciplina": "Português",
    "classe": "7ª classe",
    "tag": "POR",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # u1 <- INDE I, VI, XI: Textos Normativos
        # ================================================================
        {
            "id": "u1",
            "titulo": "Textos normativos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O regulamento escolar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um texto normativo serve para:",
                            "options": [
                                "Estabelecer regras e deveres",
                                "Contar uma história",
                                "Dar notícias do dia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O Regulamento Escolar é um texto:",
                            "options": [
                                "Normativo",
                                "Literário",
                                "Jornalístico",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A linguagem de um regulamento é:",
                            "options": [
                                "Clara, formal e sem opiniões",
                                "Poética e cheia de imagens",
                                "Informal, como entre amigos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os regulamentos organizam-se normalmente em:",
                            "options": [
                                "Artigos e números",
                                "Estrofes e versos",
                                "Parágrafos sem ordem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada texto ao que ele faz.",
                            "pairs": [
                                ["Regulamento", "Estabelece regras"],
                                ["Conto", "Narra uma história"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Tipos de sujeito e preposições",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Em «Os alunos chegaram cedo», o sujeito é:",
                            "options": [
                                "Simples, porque tem um só núcleo",
                                "Composto, porque «alunos» está no plural",
                                "Não há sujeito",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «A Amina e o Jorge estudam juntos», o "
                                 "sujeito é:",
                            "options": [
                                "Composto",
                                "Simples",
                                "Subentendido",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Completa com a preposição certa: "
                                 "«Vou ___ pé para a escola.» Escreve só a "
                                 "palavra que falta.",
                            "a": "a",
                        },
                        {
                            "t": "choice",
                            "q": "Em «Fui à escola com o meu irmão», a "
                                 "palavra «com» é:",
                            "options": [
                                "Uma preposição",
                                "Um advérbio",
                                "Um pronome",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Completa com a preposição certa: "
                                 "«Escrevi o trabalho ___ caneta azul.» "
                                 "Escreve só a palavra que falta.",
                            "a": "com",
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Formar palavras e tratar as pessoas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A palavra «infeliz» formou-se por:",
                            "options": [
                                "Prefixação",
                                "Sufixação",
                                "Composição",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A palavra «felizmente» formou-se por:",
                            "options": [
                                "Sufixação",
                                "Prefixação",
                                "Aglutinação",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «Ela escreve bem», a palavra «bem» é:",
                            "options": [
                                "Um advérbio de modo",
                                "Um adjectivo",
                                "Uma preposição",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao dirigir-se ao director da escola, "
                                 "escreves:",
                            "options": [
                                "«O senhor director pode autorizar…»",
                                "«Tu podes autorizar…»",
                                "«Vocês podem autorizar…»",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Vossa Excelência» é uma forma de "
                                 "tratamento da:",
                            "options": [
                                "3ª pessoa gramatical",
                                "1ª pessoa gramatical",
                                "2ª pessoa do singular",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # u2 <- INDE II, VII, XII: Textos Administrativos
        # ================================================================
        {
            "id": "u2",
            "titulo": "Textos administrativos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O aviso",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um aviso serve para:",
                            "options": [
                                "Comunicar uma informação a muitas pessoas",
                                "Contar uma história inventada",
                                "Descrever uma paisagem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um aviso deve ser:",
                            "options": [
                                "Curto, claro e com data",
                                "Longo e cheio de pormenores",
                                "Escrito em verso",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes elementos NÃO pode faltar num "
                                 "aviso?",
                            "options": [
                                "A data",
                                "Uma rima",
                                "Um desenho",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Avisa-se toda a comunidade escolar» está "
                                 "na:",
                            "options": [
                                "Passiva de se",
                                "Voz activa",
                                "Forma interrogativa",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Os tempos do modo indicativo",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Escreve o verbo «informar» no presente do "
                                 "indicativo, na 1ª pessoa do singular: "
                                 "eu ___",
                            "a": "informo",
                        },
                        {
                            "t": "choice",
                            "q": "«A escola comunicou a decisão» está no:",
                            "options": [
                                "Pretérito perfeito do indicativo",
                                "Presente do indicativo",
                                "Futuro do indicativo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Qual é o particípio passado do verbo "
                                 "«avisar»?",
                            "a": "avisado",
                        },
                        {
                            "t": "choice",
                            "q": "«Amanhã avisaremos os encarregados» está "
                                 "no:",
                            "options": [
                                "Futuro do indicativo",
                                "Pretérito imperfeito",
                                "Presente",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Qual é o particípio passado do verbo "
                                 "«informar»?",
                            "a": "informado",
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Voz passiva e verbos irregulares",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«O aviso foi lido pelo director» está na:",
                            "options": [
                                "Voz passiva",
                                "Voz activa",
                                "Forma negativa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A frase activa «O secretário emitiu a "
                                 "declaração» na voz passiva fica:",
                            "options": [
                                "A declaração foi emitida pelo secretário",
                                "A declaração emitiu o secretário",
                                "O secretário foi emitido pela declaração",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Escreve o verbo «ir» no presente do "
                                 "indicativo, na 1ª pessoa do singular: "
                                 "eu ___",
                            "a": "vou",
                        },
                        {
                            "t": "input",
                            "q": "Escreve o verbo «pôr» no presente do "
                                 "indicativo, na 1ª pessoa do singular: "
                                 "eu ___",
                            "a": "ponho",
                        },
                        {
                            "t": "choice",
                            "q": "Os verbos «ir», «ser» e «pôr» são:",
                            "options": [
                                "Irregulares",
                                "Regulares",
                                "Defectivos",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # u3 <- INDE III, VIII, XIII: Textos Jornalisticos
        # ================================================================
        {
            "id": "u3",
            "titulo": "Textos jornalísticos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A notícia",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma notícia deve responder a:",
                            "options": [
                                "O quê, quem, quando, onde e porquê",
                                "Só ao que aconteceu",
                                "Ao que o jornalista sente",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O título de uma notícia serve para:",
                            "options": [
                                "Dizer, em poucas palavras, do que trata",
                                "Contar o fim da história",
                                "Dar a opinião do jornal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A linguagem de uma notícia deve ser:",
                            "options": [
                                "Objectiva, sem opiniões do autor",
                                "Cheia de adjectivos e emoção",
                                "Difícil, para parecer séria",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O «fait divers» é uma notícia:",
                            "options": [
                                "Breve, sobre um caso do dia-a-dia",
                                "De primeira página, muito longa",
                                "Sobre desporto apenas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Complementos circunstanciais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Em «A chuva caiu ontem», «ontem» é "
                                 "complemento circunstancial de:",
                            "options": ["Tempo", "Lugar", "Causa"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «O comboio parou em Nampula», «em "
                                 "Nampula» é complemento circunstancial de:",
                            "options": ["Lugar", "Tempo", "Fim"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «A aula foi adiada por causa da chuva», "
                                 "a expressão «por causa da chuva» indica:",
                            "options": ["Causa", "Lugar", "Tempo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «Estuda para passar de classe», «para "
                                 "passar de classe» é complemento "
                                 "circunstancial de:",
                            "options": ["Fim", "Causa", "Modo"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Conjunções, acentuação e pontuação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Em «Choveu muito, mas fomos à escola», a "
                                 "conjunção «mas» é:",
                            "options": [
                                "Adversativa",
                                "Copulativa",
                                "Conclusiva",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «Estudou bastante, logo passou», a "
                                 "conjunção «logo» é:",
                            "options": [
                                "Conclusiva",
                                "Adversativa",
                                "Copulativa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «O Jorge e a Amina chegaram», a "
                                 "conjunção «e» é:",
                            "options": [
                                "Copulativa",
                                "Adversativa",
                                "Conclusiva",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas palavras está bem acentuada?",
                            "options": ["Notícia", "Noticía", "Noticia"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Que sinal se usa para introduzir a fala de "
                                 "alguém num diálogo?",
                            "options": [
                                "O travessão",
                                "O ponto e vírgula",
                                "Os parênteses",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # u4 <- INDE IV, IX, XIV: Textos Multiuso
        # ================================================================
        {
            "id": "u4",
            "titulo": "Textos multiuso",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Manuais e textos didácticos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um manual escolar serve sobretudo para:",
                            "options": [
                                "Ensinar e explicar matéria",
                                "Divertir com histórias",
                                "Dar notícias do país",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O índice de um manual serve para:",
                            "options": [
                                "Encontrar depressa o que se procura",
                                "Decorar a capa",
                                "Contar quantas páginas há",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O vocabulário de um texto científico é:",
                            "options": [
                                "Rigoroso e próprio da matéria",
                                "Cheio de gíria",
                                "Igual ao das conversas de rua",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Num texto didáctico, os esquemas e as "
                                 "tabelas servem para:",
                            "options": [
                                "Organizar a informação e ajudar a perceber",
                                "Ocupar espaço",
                                "Substituir o texto todo",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Os pronomes",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Em «Este livro é meu», a palavra «este» é "
                                 "um pronome:",
                            "options": [
                                "Demonstrativo",
                                "Possessivo",
                                "Indefinido",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «Este livro é meu», a palavra «meu» é "
                                 "um pronome:",
                            "options": [
                                "Possessivo",
                                "Demonstrativo",
                                "Interrogativo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «Quem chegou primeiro?», a palavra "
                                 "«quem» é um pronome:",
                            "options": [
                                "Interrogativo",
                                "Possessivo",
                                "Demonstrativo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «Alguém deixou a porta aberta», a "
                                 "palavra «alguém» é um pronome:",
                            "options": [
                                "Indefinido",
                                "Definido",
                                "Possessivo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada pronome à sua classe.",
                            "pairs": [
                                ["Aquele", "Demonstrativo"],
                                ["Nosso", "Possessivo"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Os modos verbais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Estuda a lição!» está no modo:",
                            "options": [
                                "Imperativo",
                                "Indicativo",
                                "Conjuntivo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Não faças barulho» é um imperativo:",
                            "options": ["Negativo", "Afirmativo", "Neutro"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Espero que ele venha cedo» — o verbo "
                                 "«venha» está no modo:",
                            "options": [
                                "Conjuntivo",
                                "Indicativo",
                                "Imperativo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O modo indicativo exprime:",
                            "options": [
                                "Factos tidos como certos",
                                "Ordens e pedidos",
                                "Dúvida e desejo",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # u5 <- INDE V, X, XV: Textos Literarios
        # ================================================================
        {
            "id": "u5",
            "titulo": "Textos literários",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Conto, fábula e o grau do adjectivo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma fábula distingue-se de um conto porque:",
                            "options": [
                                "Tem uma moral e as personagens costumam ser "
                                "animais",
                                "É sempre mais comprida",
                                "Não tem princípio nem fim",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «A Amina é mais alta do que o Jorge», o "
                                 "adjectivo está no grau:",
                            "options": [
                                "Comparativo de superioridade",
                                "Comparativo de igualdade",
                                "Superlativo absoluto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «O rio é tão largo como o outro», o grau "
                                 "é comparativo de:",
                            "options": [
                                "Igualdade",
                                "Superioridade",
                                "Inferioridade",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Altíssimo» é um superlativo absoluto:",
                            "options": [
                                "Sintético",
                                "Analítico",
                                "Comparativo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Muito alto» é um superlativo absoluto:",
                            "options": [
                                "Analítico",
                                "Sintético",
                                "Relativo",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Homónimas, parónimas e palavras compostas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Canto» (de cantar) e «canto» (de uma sala) "
                                 "são palavras:",
                            "options": [
                                "Homónimas",
                                "Parónimas",
                                "Sinónimas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Comprimento» e «cumprimento» são palavras:",
                            "options": [
                                "Parónimas, porque só se parecem",
                                "Homónimas, porque são iguais",
                                "Sinónimas, porque querem dizer o mesmo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Passatempo» formou-se por composição:",
                            "options": [
                                "Por aglutinação",
                                "Por justaposição",
                                "Por prefixação",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Guarda-chuva» formou-se por composição:",
                            "options": [
                                "Por justaposição",
                                "Por aglutinação",
                                "Por sufixação",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Texto dramático e discurso directo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um texto dramático distingue-se do "
                                 "narrativo porque:",
                            "options": [
                                "É escrito para ser representado",
                                "É sempre mais curto",
                                "Não tem personagens",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As indicações entre parênteses num texto "
                                 "dramático chamam-se:",
                            "options": [
                                "Didascálias",
                                "Estrofes",
                                "Rubricas do jornal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O Jorge disse: — Vou à escola.» está em "
                                 "discurso:",
                            "options": ["Directo", "Indirecto", "Misto"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em discurso indirecto, «— Estou cansada, "
                                 "disse a Amina» fica:",
                            "options": [
                                "A Amina disse que estava cansada",
                                "A Amina disse: estou cansada",
                                "A Amina está cansada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A comédia é um texto dramático que procura:",
                            "options": [
                                "Fazer rir e criticar costumes",
                                "Ensinar contas",
                                "Dar notícias",
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

    # A seguir a Matematica da 7a, para a 7a classe ficar com a mesma ordem
    # de disciplinas das outras: Matematica, Portugues, e depois as outras.
    dados["cursos"].append(CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta as entradas ao tools/materia_texto.py "
          "e corre python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
