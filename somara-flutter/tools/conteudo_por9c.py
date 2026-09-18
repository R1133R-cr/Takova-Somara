# -*- coding: utf-8 -*-
"""O curso de Portugues da 9a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Portugues -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, 9a classe,
     pp. 55-74. Guardado em Documents\\planos da 5a classe\\Livros\\
     Programas INDE 1o Ciclo\\portugues.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

Quinze unidades, cinco tipos de texto
-------------------------------------
O programa da 9a tem quinze unidades: em cada trimestre, os mesmos cinco
tipos de texto pela mesma ordem -- normativos, administrativos,
jornalisticos, multiuso, literarios -- com um texto especifico de cada
vez. Como na 8a, o curso agrupa-as pelo tipo de texto, que e o que o
aluno aprende a ler e a escrever:

    1  Textos normativos       Declaracao dos Direitos Humanos; Direitos
                               da Crianca; fazer, dar e poder; pontuacao;
                               sinonimos e antonimos; adjectivos
    2  Textos administrativos  carta de apresentacao; Curriculum Vitae;
                               requerimento; formas de tratamento;
                               palavras compostas; concordancia verbal
    3  Textos jornalisticos    entrevista; texto publicitario; discurso
                               directo e indirecto; conjugacao
                               perifrastica; preposicoes; acentuacao;
                               oracoes subordinadas
    4  Textos multiuso         guia turistico; relato de viagem; oracoes
                               integrantes; pronomes relativos
    5  Textos literarios       romance; poema; texto dramatico; atributo
                               e aposto; recursos estilisticos;
                               interjeicoes

Cinco unidades, quinze aulas.

Correr a partir de somara-flutter/:
    python tools/conteudo_por9c.py            # so mostra
    python tools/conteudo_por9c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Português — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, 9ª classe, pp. 55-74. "
    "As quinze unidades do programa estão agrupadas nos cinco tipos de texto "
    "que ele repete em cada trimestre; os conteúdos são os dele e os "
    "exercícios foram escritos a partir deles, porque um programa de ensino "
    "não traz exercícios e não há livro do aluno da 9ª classe publicado."
)

CURSO = {
    "id": "por-9c",
    "disciplina": "Português",
    "classe": "9ª classe",
    "tag": "POR",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # 1  Textos normativos
        # ================================================================
        {
            "id": "u1",
            "titulo": "Textos normativos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A Declaração dos Direitos Humanos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Declaração Universal dos Direitos "
                                 "Humanos é um texto:",
                            "options": [
                                "Normativo: diz o que se deve e o que não "
                                "se pode fazer",
                                "Publicitário",
                                "Poético",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada direito ao seu tipo.",
                            "pairs": [
                                ["Direito à vida e à liberdade", "Pessoal"],
                                ["Direito a um julgamento justo", "Judiciário"],
                                ["Direito à educação e ao trabalho", "Social"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O objectivo principal da Declaração é:",
                            "options": [
                                "Garantir a todas as pessoas os mesmos "
                                "direitos, sem distinção",
                                "Dar mais direitos a quem tem dinheiro",
                                "Organizar o trânsito",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A linguagem de um texto normativo é:",
                            "options": [
                                "Clara, objectiva e sem ambiguidades",
                                "Cheia de rimas",
                                "Familiar e brincalhona",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "A Declaração Universal dos Direitos "
                                 "Humanos foi adoptada pelas Nações Unidas "
                                 "em que ano?",
                            "a": "1948",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Os verbos fazer, dar e poder",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Ontem eu … os trabalhos de casa.» O "
                                 "verbo fazer fica:",
                            "options": ["fiz", "fazi", "fazia"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Amanhã eles … o sangue no hospital.» O "
                                 "verbo dar fica:",
                            "options": ["darão", "dão", "deram"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Se tu …, vem à reunião.» O verbo poder "
                                 "fica:",
                            "options": ["puderes", "poderes", "podes"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Nós … tudo o que podíamos.» O verbo "
                                 "fazer, no pretérito perfeito, fica:",
                            "options": ["fizemos", "fazemos", "fizémos"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Fazer, dar e poder são verbos:",
                            "options": [
                                "Irregulares: mudam o radical ao conjugar",
                                "Regulares da primeira conjugação",
                                "Defectivos",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Pontuação, sinónimos e antónimos",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada sinal de pontuação ao seu uso.",
                            "pairs": [
                                ["Vírgula", "Separa elementos de uma enumeração"],
                                ["Dois pontos", "Anuncia uma explicação ou uma fala"],
                                ["Ponto e vírgula", "Separa partes longas de uma frase"],
                                ["Travessão", "Introduz a fala de uma personagem"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas frases está bem pontuada?",
                            "options": [
                                "Todos têm direitos: à vida, à liberdade e "
                                "à educação.",
                                "Todos têm direitos à vida: à liberdade, e "
                                "à educação.",
                                "Todos, têm direitos à vida à liberdade e "
                                "à educação.",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um sinónimo de «liberdade» é:",
                            "options": ["Autonomia", "Prisão", "Dever"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O antónimo de «justo» é:",
                            "options": ["Injusto", "Correcto", "Legal"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada palavra ao seu antónimo.",
                            "pairs": [
                                ["Igualdade", "Desigualdade"],
                                ["Respeito", "Desprezo"],
                                ["Paz", "Guerra"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Os Direitos da Criança e os adjectivos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Segundo a Declaração dos Direitos da "
                                 "Criança, uma criança de dez anos:",
                            "options": [
                                "Tem direito a estudar e a brincar, e não "
                                "a trabalhar",
                                "Deve trabalhar para ajudar em casa",
                                "Só tem direitos depois dos dezoito",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada adjectivo ao seu tipo.",
                            "pairs": [
                                ["Alto, alta", "Biforme: tem duas formas"],
                                ["Feliz", "Uniforme: uma forma só"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O feminino de «português» é:",
                            "options": ["portuguesa", "portuguêsa", "portugueza"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O feminino de «europeu» é:",
                            "options": ["europeia", "europea", "europeua"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em «uma história sem pés nem cabeça», "
                                 "«sem pés nem cabeça» é:",
                            "options": [
                                "Uma locução adjectiva",
                                "Um advérbio",
                                "Um verbo",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 2  Textos administrativos
        # ================================================================
        {
            "id": "u2",
            "titulo": "Textos administrativos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A carta de apresentação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma carta de apresentação serve para:",
                            "options": [
                                "Apresentar-se a uma empresa ou instituição "
                                "e pedir uma oportunidade",
                                "Contar as férias a um amigo",
                                "Vender um produto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada parte da carta de apresentação "
                                 "à sua ordem.",
                            "pairs": [
                                ["Local, data e destinatário", "Primeiro"],
                                ["Quem sou e o que peço", "Depois"],
                                ["Despedida e assinatura", "Por fim"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A um director que não se conhece "
                                 "escreve-se:",
                            "options": [
                                "Excelentíssimo Senhor Director",
                                "Olá, chefe",
                                "Querido amigo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A linguagem de uma carta de apresentação "
                                 "é:",
                            "options": [
                                "Formal e cuidada",
                                "Familiar, com calão",
                                "Poética",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Pagar impostos é importante porque:",
                            "options": [
                                "É com eles que o Estado paga escolas, "
                                "hospitais e estradas",
                                "Faz as pessoas mais ricas",
                                "É só um costume antigo",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O Curriculum Vitae e as palavras compostas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um Curriculum Vitae é:",
                            "options": [
                                "O resumo da vida escolar e profissional "
                                "de uma pessoa",
                                "Uma carta de amor",
                                "Um relato de viagem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada dado ao campo do Curriculum "
                                 "Vitae onde entra.",
                            "pairs": [
                                ["Nome, data de nascimento, contacto", "Dados pessoais"],
                                ["9ª classe na Escola Secundária de Lichinga", "Formação"],
                                ["Ajudante numa oficina, dois anos", "Experiência"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada palavra composta ao processo "
                                 "que a formou.",
                            "pairs": [
                                ["Guarda-chuva", "Justaposição"],
                                ["Aguardente", "Aglutinação"],
                                ["Fidalgo", "Aglutinação"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Na justaposição, as palavras juntam-se:",
                            "options": [
                                "Sem perder letras, em geral com hífen",
                                "Perdendo letras e fundindo-se",
                                "Trocando a ordem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Praticar actividade física regularmente:",
                            "options": [
                                "Fortalece o corpo e previne doenças",
                                "Só serve para atletas",
                                "Faz mal ao coração",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O requerimento e a concordância verbal",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um requerimento é um texto em que:",
                            "options": [
                                "Se pede algo a uma entidade, por escrito e "
                                "com formalidade",
                                "Se conta uma história",
                                "Se anuncia um produto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um camponês que quer um terreno para "
                                 "cultivar escreve um requerimento:",
                            "options": [
                                "Ao Administrador do Distrito, a pedir a "
                                "concessão da terra",
                                "Ao vizinho",
                                "Ao jornal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas frases tem a concordância "
                                 "certa?",
                            "options": [
                                "Os alunos pedem um terreno para a horta.",
                                "Os alunos pede um terreno para a horta.",
                                "Os alunos pedes um terreno para a horta.",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Eu e tu … ao campo amanhã.» O verbo ir "
                                 "fica:",
                            "options": ["vamos", "vão", "vais"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O requerimento termina com:",
                            "options": [
                                "«Pede deferimento», o local, a data e a "
                                "assinatura",
                                "«Beijinhos»",
                                "Um poema",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 3  Textos jornalisticos
        # ================================================================
        {
            "id": "u3",
            "titulo": "Textos jornalísticos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A entrevista",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Antes de uma entrevista, o entrevistador "
                                 "prepara:",
                            "options": [
                                "Um guião com as perguntas",
                                "As respostas do entrevistado",
                                "Um poema",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A enfermeira disse: — A malária "
                                 "previne-se com rede.» Este discurso é:",
                            "options": ["Directo", "Indirecto", "Poético"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em discurso indirecto, «A enfermeira "
                                 "disse: — Eu durmo com rede» fica:",
                            "options": [
                                "A enfermeira disse que dormia com rede.",
                                "A enfermeira disse: eu durmo com rede.",
                                "A enfermeira dorme com rede, disse.",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O médico está a explicar os sintomas.» "
                                 "A forma «está a explicar» é:",
                            "options": [
                                "Uma conjugação perifrástica: verbo "
                                "auxiliar mais infinitivo",
                                "Um tempo simples",
                                "Um adjectivo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada perifrástica ao que ela "
                                 "exprime.",
                            "pairs": [
                                ["Está a estudar", "Acção a decorrer"],
                                ["Começou a estudar", "Início da acção"],
                                ["Acabou de estudar", "Fim da acção"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O texto publicitário",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Num anúncio, a imagem e as cores são a "
                                 "parte:",
                            "options": ["Não verbal", "Verbal", "Gramatical"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Sabão Sol: brilho que dura!» é um:",
                            "options": ["Slogan", "Requerimento", "Relato"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada frase à preposição que lhe "
                                 "falta.",
                            "pairs": [
                                ["Vou … Lichinga de autocarro.", "até"],
                                ["Trabalha … a manhã.", "desde"],
                                ["Ficou … casa.", "sem"],
                                ["Lutamos … a malária.", "contra"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas palavras está bem "
                                 "acentuada?",
                            "options": ["Saúde", "Saude", "Sáude"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Eles … razão.» A forma do verbo ter, "
                                 "na terceira pessoa do plural, é:",
                            "options": ["têm", "tem", "tèm"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Orações subordinadas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Pergunto se vens à entrevista.» A "
                                 "oração «se vens à entrevista» é:",
                            "options": [
                                "Subordinada interrogativa indirecta",
                                "Subordinada concessiva",
                                "Coordenada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Embora chovesse, fomos à entrevista.» "
                                 "A oração «embora chovesse» é:",
                            "options": ["Concessiva", "Consecutiva", "Relativa"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Falou tão alto que todos ouviram.» A "
                                 "oração «que todos ouviram» é:",
                            "options": ["Consecutiva", "Concessiva", "Integrante"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada conjunção ao tipo de oração "
                                 "que introduz.",
                            "pairs": [
                                ["Embora, apesar de", "Concessiva"],
                                ["De modo que, tanto que", "Consecutiva"],
                                ["Se, quando (numa pergunta)", "Interrogativa indirecta"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Dormir com rede mosquiteira e tirar as "
                                 "águas paradas previnem:",
                            "options": ["A malária", "A diabetes", "A gripe"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 4  Textos multiuso
        # ================================================================
        {
            "id": "u4",
            "titulo": "Textos multiuso",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O guia turístico e as orações integrantes",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um guia turístico serve para:",
                            "options": [
                                "Dar a conhecer os lugares de interesse de "
                                "uma região",
                                "Pedir um terreno",
                                "Contar um romance",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada lugar de interesse do Niassa ao "
                                 "que ele é.",
                            "pairs": [
                                ["Lago Niassa", "Praias de água doce e pesca"],
                                ["Reserva do Niassa", "Elefantes e leões"],
                                ["Monte Massangulo", "Montanha e paisagem"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Sabemos que o lago é lindo.» A oração "
                                 "«que o lago é lindo» é:",
                            "options": [
                                "Subordinada integrante",
                                "Subordinada relativa",
                                "Coordenada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A oração integrante completa o sentido "
                                 "de:",
                            "options": [
                                "Um verbo como saber, dizer, pensar",
                                "Um nome",
                                "Um adjectivo apenas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A linguagem de um guia turístico é:",
                            "options": [
                                "Informativa e atraente",
                                "Só de ordens",
                                "Cheia de calão",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O relato de viagem e os pronomes relativos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um relato de viagem conta:",
                            "options": [
                                "Uma viagem real ou imaginada, por ordem, "
                                "com o que se viu e sentiu",
                                "As regras de um jogo",
                                "Um anúncio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A aldeia onde nasci fica perto do "
                                 "lago.» O pronome relativo é:",
                            "options": ["onde", "aldeia", "perto"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O guia que nos levou era de Lichinga.» "
                                 "A oração «que nos levou» é:",
                            "options": [
                                "Subordinada relativa",
                                "Subordinada integrante",
                                "Coordenada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada frase ao pronome relativo que "
                                 "lhe falta.",
                            "pairs": [
                                ["O barco … apanhámos era pequeno.", "que"],
                                ["A senhora … falámos vendia peixe.", "com quem"],
                                ["A ilha … chegámos chama-se Likoma.", "aonde"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Preservar o património cultural é:",
                            "options": [
                                "Guardar as danças, as línguas e os "
                                "monumentos para quem vem depois",
                                "Vender os objectos antigos",
                                "Esquecer as tradições",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 5  Textos literarios
        # ================================================================
        {
            "id": "u5",
            "titulo": "Textos literários",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O romance",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O romance distingue-se do conto por ser:",
                            "options": [
                                "Mais longo, com mais personagens e mais "
                                "acções",
                                "Sempre em verso",
                                "Sempre verdadeiro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada momento do texto narrativo ao "
                                 "que ele é.",
                            "pairs": [
                                ["Narração", "A acção avança"],
                                ["Descrição", "A acção pára para mostrar"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Meledina, a rapariga da Zambézia, "
                                 "chegou a Lourenço Marques.» «A rapariga "
                                 "da Zambézia» é:",
                            "options": ["Aposto", "Atributo", "Sujeito"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A cidade era enorme.» «Enorme» é:",
                            "options": ["Atributo", "Aposto", "Complemento directo"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada obra ao seu autor.",
                            "pairs": [
                                ["Da Chegada de Meledina a Lourenço Marques", "Aldino Muianga"],
                                ["A Personalidade de Pedro Trago", "Germano Almeida"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O poema",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada elemento do poema ao que ele é.",
                            "pairs": [
                                ["Verso", "Cada linha"],
                                ["Estrofe", "Um grupo de versos"],
                                ["Rima", "Sons iguais no fim dos versos"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada recurso estilístico ao seu "
                                 "exemplo.",
                            "pairs": [
                                ["Hipérbole", "Chorei um rio de lágrimas"],
                                ["Anáfora", "Terra minha, terra livre, terra mãe"],
                                ["Ironia", "Que bela chuva, no dia da festa"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Quem escreveu o poema «Se me queres "
                                 "conhecer»?",
                            "options": ["Noémia de Sousa", "Luís de Camões", "Rui Knopfli"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Amor é fogo que arde sem se ver» é um "
                                 "verso de:",
                            "options": ["Luís Vaz de Camões", "José Craveirinha", "Orlando Mendes"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada advérbio ao seu tipo.",
                            "pairs": [
                                ["Sim, certamente", "Afirmação"],
                                ["Muito, bastante", "Intensidade"],
                                ["Só, apenas", "Exclusão"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O texto dramático",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um texto dramático é escrito para:",
                            "options": [
                                "Ser representado em palco",
                                "Ser cantado",
                                "Ser lido em silêncio apenas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A tragédia é o texto dramático que:",
                            "options": [
                                "Acaba mal, com a desgraça da personagem",
                                "Faz rir do princípio ao fim",
                                "Não tem personagens",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ai! Que dor!» A palavra «ai» é:",
                            "options": ["Uma interjeição", "Um verbo", "Um pronome"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No texto dramático, as indicações entre "
                                 "parêntesis sobre gestos e cenário "
                                 "chamam-se:",
                            "options": ["Didascálias", "Estrofes", "Apostos"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma gravidez precoce, na adolescência:",
                            "options": [
                                "Põe em risco a saúde da rapariga e "
                                "afasta-a da escola",
                                "Não tem consequências",
                                "É obrigatória",
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
