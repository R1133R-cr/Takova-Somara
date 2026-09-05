# -*- coding: utf-8 -*-
"""O curso de Ingles da 7a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Lingua Inglesa -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024.
     Descarregado do educador.mozestuda.com.

O programa esta escrito em ingles e organiza a 7a classe (Grade 7) em NOVE
unidades. Aqui ficam agrupadas em cinco, por proximidade de assunto -- a
lista completa das nove esta no comentario de cada unidade.

A regra que mandou nas perguntas: a voz nao fala ingles
--------------------------------------------------------
A app tem UMA voz, e e portuguesa (pt-PT-RaquelNeural). Se um enunciado
fosse escrito em ingles, ela lia-o com sotaque e regras portuguesas --
"the house" sairia qualquer coisa como "te ouse". Uma app que ensina
ingles a pronunciar mal o ingles faz pior do que nao ensinar nada.

Por isso, aqui:

    O ENUNCIADO esta sempre em PORTUGUES  -- e o que a voz le
    O INGLES vive nas OPCOES              -- e o que a crianca le

Nao e uma limitacao disfarcada de escolha: e a unica forma honesta de dar
ingles com uma voz portuguesa.

A regra vale para FRASES. Uma palavra inglesa solta no enunciado -- "o
plural de «book»" -- e inevitavel numa disciplina de linguas, e uma
palavra lida com fonetica portuguesa fica perto do que devia ser. Uma
frase inteira nao fica: perde-se por completo.

O dia em que a app tiver uma segunda voz, os enunciados podem passar a
ingles e isto reescreve-se.

As nove unidades do INDE, e como ficaram
-----------------------------------------
    u1  1 Greetings and Introductions   alfabeto, saudacoes, numeros,
        2 School                        paises, escola, horas
    u2  3 The family and friends        familia, amigos, possessivos
    u3  4 The Human body, Health        corpo, saude, alimentacao
          and Nutrition
        5 The home and Community        casa, comunidade
    u4  6 The Environment               ambiente
        7 Aquatic life                  vida aquatica
    u5  8 Transport and Communication   transportes, comunicacao
        9 Entertainment and Sports      lazer e desporto

Correr a partir de somara-flutter/:
    python tools/conteudo_ing7c.py            # so mostra
    python tools/conteudo_ing7c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Língua Inglesa — Ensino "
    "Secundário, 1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024. As nove "
    "unidades do Grade 7 estão agrupadas em cinco por proximidade de "
    "assunto. Os enunciados estão em português e o inglês vive nas "
    "opções: a app tem uma só voz, portuguesa, e uma voz portuguesa a ler "
    "inglês ensinaria a pronúncia errada. Os exercícios foram escritos a "
    "partir dos conteúdos, porque um programa de ensino não traz "
    "exercícios e não há livro do aluno da 7ª classe publicado."
)

CURSO = {
    "id": "ing-7c",
    "disciplina": "Inglês",
    "classe": "7ª classe",
    "tag": "ING",
    "fonte": FONTE,
    "units": [
        # u1 <- INDE 1 (Greetings and Introductions) + 2 (School)
        {
            "id": "u1",
            "titulo": "Cumprimentos e escola",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Cumprimentar e apresentar-se",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se diz «bom dia» em inglês?",
                            "options": [
                                "Good morning",
                                "Good night",
                                "Goodbye",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «boa tarde» em inglês?",
                            "options": [
                                "Good afternoon",
                                "Good morning",
                                "Good night",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como perguntas o nome de alguém, em inglês?",
                            "options": [
                                "What is your name?",
                                "How old are you?",
                                "Where are you from?",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para dizer «eu sou o Jorge», escreve-se:",
                            "options": [
                                "I am Jorge",
                                "You are Jorge",
                                "He is Jorge",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «até amanhã» em inglês?",
                            "options": [
                                "See you tomorrow",
                                "See you never",
                                "Good luck",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Números, países e nacionalidades",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se escreve o número 12 em inglês?",
                            "options": ["Twelve", "Twenty", "Two"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve o número 15 em inglês?",
                            "options": ["Fifteen", "Fifty", "Five"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Alguém de Moçambique é, em inglês:",
                            "options": [
                                "Mozambican",
                                "Mozambique",
                                "Mozambiquese",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para perguntar de onde alguém é, dizes:",
                            "options": [
                                "Where are you from?",
                                "What are you from?",
                                "Who are you from?",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada número ao seu nome em inglês.",
                            "pairs": [
                                ["7", "Seven"],
                                ["20", "Twenty"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A escola e as horas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se diz «sala de aula» em inglês?",
                            "options": ["Classroom", "Playground", "Library"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «biblioteca» em inglês?",
                            "options": ["Library", "Bookshop", "Classroom"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para perguntar as horas, dizes:",
                            "options": [
                                "What time is it?",
                                "What day is it?",
                                "How much is it?",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O primeiro dia da semana escolar, «segunda-"
                                 "feira», é em inglês:",
                            "options": ["Monday", "Sunday", "Saturday"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O plural de «book» é:",
                            "options": ["Books", "Bookes", "Book"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # u2 <- INDE 3 (The family and friends)
        {
            "id": "u2",
            "titulo": "A família e os amigos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Os membros da família",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se diz «mãe» em inglês?",
                            "options": ["Mother", "Sister", "Aunt"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «irmão» em inglês?",
                            "options": ["Brother", "Father", "Cousin"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «avó» em inglês?",
                            "options": [
                                "Grandmother",
                                "Grandfather",
                                "Mother",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada palavra ao seu significado.",
                            "pairs": [
                                ["Father", "Pai"],
                                ["Daughter", "Filha"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Os possessivos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«A minha mãe» diz-se, em inglês:",
                            "options": ["My mother", "Your mother", "Her mother"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O irmão dela» diz-se:",
                            "options": [
                                "Her brother",
                                "His brother",
                                "Their brother",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O livro dele» diz-se:",
                            "options": ["His book", "Her book", "Its book"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A nossa casa» diz-se:",
                            "options": ["Our house", "Your house", "Their house"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Falar dos amigos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Ela é a minha amiga» escreve-se:",
                            "options": [
                                "She is my friend",
                                "He is my friend",
                                "She are my friend",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «eu não sou "
                                 "estudante»?",
                            "options": [
                                "I am not a student",
                                "I not am a student",
                                "I am no student",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para perguntar a idade de alguém, dizes:",
                            "options": [
                                "How old are you?",
                                "How are you?",
                                "How many are you?",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Eles são meus amigos» escreve-se:",
                            "options": [
                                "They are my friends",
                                "They is my friends",
                                "Them are my friends",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # u3 <- INDE 4 (Human body, Health and Nutrition) + 5 (Home and Community)
        {
            "id": "u3",
            "titulo": "O corpo, a saúde e a casa",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "As partes do corpo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se diz «cabeça» em inglês?",
                            "options": ["Head", "Hand", "Heart"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «mão» em inglês?",
                            "options": ["Hand", "Foot", "Arm"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «olhos» em inglês?",
                            "options": ["Eyes", "Ears", "Legs"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada parte do corpo ao seu nome em "
                                 "inglês.",
                            "pairs": [
                                ["Perna", "Leg"],
                                ["Boca", "Mouth"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A saúde e a alimentação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Estou doente» diz-se, em inglês:",
                            "options": ["I am sick", "I am hungry", "I am tired"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Dor de cabeça» diz-se:",
                            "options": ["Headache", "Toothache", "Stomachache"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «água» em inglês?",
                            "options": ["Water", "Milk", "Juice"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Fruta» diz-se, em inglês:",
                            "options": ["Fruit", "Bread", "Meat"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A casa e a comunidade",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se diz «cozinha» em inglês?",
                            "options": ["Kitchen", "Bedroom", "Bathroom"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Há uma mesa na sala» escreve-se:",
                            "options": [
                                "There is a table in the room",
                                "There are a table in the room",
                                "It has a table in the room",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Há três cadeiras» escreve-se:",
                            "options": [
                                "There are three chairs",
                                "There is three chairs",
                                "There have three chairs",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «mercado» em inglês?",
                            "options": ["Market", "Hospital", "School"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # u4 <- INDE 6 (The Environment) + 7 (Aquatic life)
        {
            "id": "u4",
            "titulo": "O ambiente e a vida aquática",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A natureza",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se diz «árvore» em inglês?",
                            "options": ["Tree", "Grass", "Flower"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «rio» em inglês?",
                            "options": ["River", "Sea", "Lake"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Lixo» diz-se, em inglês:",
                            "options": ["Rubbish", "Rubber", "Rock"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Não deites lixo no chão» escreve-se:",
                            "options": [
                                "Do not throw rubbish on the ground",
                                "No throw rubbish on the ground",
                                "Not throw rubbish on the ground",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A vida aquática",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se diz «peixe» em inglês?",
                            "options": ["Fish", "Bird", "Frog"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «mar» em inglês?",
                            "options": ["Sea", "Sky", "Sand"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Os peixes vivem na água» escreve-se:",
                            "options": [
                                "Fish live in water",
                                "Fish lives in water",
                                "Fish living in water",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «tartaruga» em inglês?",
                            "options": ["Turtle", "Crab", "Shark"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O presente simples",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Ele estuda todos os dias» escreve-se:",
                            "options": [
                                "He studies every day",
                                "He study every day",
                                "He studying every day",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em inglês, «ela não "
                                 "trabalha aqui»?",
                            "options": [
                                "She does not work here",
                                "She not works here",
                                "She do not works here",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A pergunta «Tu gostas de peixe?» escreve-se:",
                            "options": [
                                "Do you like fish?",
                                "Does you like fish?",
                                "You do like fish?",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No presente simples, com «he», «she» e "
                                 "«it», o verbo leva:",
                            "options": [
                                "Um -s no fim",
                                "Um -ed no fim",
                                "Nada de diferente",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # u5 <- INDE 8 (Transport and Communication) + 9 (Entertainment and Sports)
        {
            "id": "u5",
            "titulo": "Transportes, lazer e desporto",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Os transportes",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se diz «autocarro» em inglês?",
                            "options": ["Bus", "Car", "Train"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «bicicleta» em inglês?",
                            "options": ["Bicycle", "Motorbike", "Boat"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Vou à escola a pé» escreve-se:",
                            "options": [
                                "I walk to school",
                                "I go school by foot",
                                "I am walk to school",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «comboio» em inglês?",
                            "options": ["Train", "Truck", "Plane"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A comunicação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se diz «carta» em inglês?",
                            "options": ["Letter", "Number", "Paper"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «telemóvel» em inglês?",
                            "options": [
                                "Mobile phone",
                                "Television",
                                "Radio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao atender o telefone em inglês, dizes:",
                            "options": ["Hello", "Goodbye", "Please"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Por favor» diz-se, em inglês:",
                            "options": ["Please", "Sorry", "Thanks"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Lazer e desporto",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se diz «futebol» em inglês britânico?",
                            "options": ["Football", "Handball", "Baseball"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Eu gosto de música» escreve-se:",
                            "options": [
                                "I like music",
                                "I likes music",
                                "I am like music",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ele joga futebol ao sábado» escreve-se:",
                            "options": [
                                "He plays football on Saturday",
                                "He play football on Saturday",
                                "He playing football on Saturday",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «nadar» em inglês?",
                            "options": ["Swim", "Run", "Jump"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «dançar» em inglês?",
                            "options": ["Dance", "Sing", "Play"],
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
    if CURSO["id"] in [c["id"] for c in dados["cursos"]]:
        print(f"o curso {CURSO['id']} ja esta no content.json", file=sys.stderr)
        return 1

    niveis = sum(len(u["niveis"]) for u in CURSO["units"])
    perguntas = sum(len(n["questoes"])
                    for u in CURSO["units"] for n in u["niveis"])
    print(f"{CURSO['disciplina']} da {CURSO['classe']}: "
          f"{len(CURSO['units'])} unidades, {niveis} niveis, "
          f"{perguntas} perguntas")

    if not gravar:
        print("(so leitura -- corre com --gravar)")
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

    dados["cursos"].append(CURSO)
    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"-- curso inserido, {feitos} audios gravados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
