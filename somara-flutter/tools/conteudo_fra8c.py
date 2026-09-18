# -*- coding: utf-8 -*-
"""O curso de Frances da 8a classe -- o primeiro Frances da app.

De onde vem
-----------
    "Programme d'Enseignement de la Discipline de Langue Francaise --
     Enseignement Secondaire -- 1er Cycle", INDE/MINEDH, Maputo,
     Setembro de 2024, 8eme classe, pp. 8 (apercu) e 11-19 (plans
     thematiques). Guardado em Documents\\planos da 5a classe\\Livros\\
     Programas INDE 1o Ciclo\\frances.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

O Frances comeca na 8a
----------------------
O programa e do 1o ciclo do secundario, e o 1o ciclo do secundario, para
o Frances, sao a 8a e a 9a: o apercu dos conteudos tem duas colunas,
"8eme Classe" e "9eme Classe", e mais nenhuma. A 7a nao tem Frances.

As duas unidades tematicas da 8eme, pela ordem do programa
----------------------------------------------------------
    1  Mes amis et moi              1 Ma presentation
                                    2 Presentation de quelqu'un
                                    3 Description physique et psychologique
    2  L'ecole et les activites     1 Localisation dans la salle de classe
       quotidiennes                 2 Attitudes et comportements
                                    3 Vie quotidienne d'un(e) eleve
                                    4 Calendrier scolaire
                                    5 Salle de classe
                                    6 Objets de l'ecole et de la classe

Duas unidades, dez aulas: os nove temas do programa, com o primeiro
dividido em dois porque tem a gramatica de base (etre, avoir, verbos em
-er) que os outros oito usam.

O frances fica nas opcoes
-------------------------
A voz da app e portuguesa e nao sabe dizer frances. Como no Ingles, os
enunciados sao todos em portugues e o frances aparece so nas opcoes e
nos pares, que se leem e nao se ouvem.

Correr a partir de somara-flutter/:
    python tools/conteudo_fra8c.py            # so mostra
    python tools/conteudo_fra8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programme d'Enseignement de la Discipline de Langue Française — "
    "Enseignement Secondaire, 1er Cycle. INDE/MINEDH, Maputo, Setembro de "
    "2024, 8ème classe, pp. 8 e 11-19. As duas unidades, os nove temas, o "
    "vocabulário e a gramática são do programa; os exercícios foram "
    "escritos a partir deles, porque um programa de ensino não traz "
    "exercícios e não há livro do aluno da 8ª classe publicado. Os "
    "enunciados são em português e o francês fica nas opções, porque a voz "
    "da app é portuguesa."
)

CURSO = {
    "id": "fra-8c",
    "disciplina": "Francês",
    "classe": "8ª classe",
    "tag": "FRA",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # 1  Mes amis et moi
        # ================================================================
        {
            "id": "u1",
            "titulo": "Os meus amigos e eu",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Cumprimentar e apresentar-me",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada cumprimento ao francês.",
                            "pairs": [
                                ["Bom dia", "Bonjour"],
                                ["Boa noite", "Bonsoir"],
                                ["Adeus", "Au revoir"],
                                ["Olá", "Salut"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em francês, «chamo-me "
                                 "Amina»?",
                            "options": [
                                "Je m'appelle Amina",
                                "Je t'appelle Amina",
                                "Je suis appelle Amina",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se diz «obrigado» em francês?",
                            "options": ["Merci", "Pardon", "Bonjour"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A um professor ou a um desconhecido "
                                 "trata-se por:",
                            "options": ["Vous", "Tu", "Il"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada número ao francês.",
                            "pairs": [
                                ["Dez", "Dix"],
                                ["Vinte", "Vingt"],
                                ["Cem", "Cent"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada dia da semana ao francês.",
                            "pairs": [
                                ["Segunda-feira", "Lundi"],
                                ["Sábado", "Samedi"],
                                ["Domingo", "Dimanche"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Ser, ter e os verbos em -er",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se escreve, em francês, «eu sou "
                                 "moçambicano»?",
                            "options": [
                                "Je suis mozambicain",
                                "Je es mozambicain",
                                "Je suis mozambicaine",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Tu tens catorze anos» escreve-se:",
                            "options": [
                                "Tu as quatorze ans",
                                "Tu es quatorze ans",
                                "Tu a quatorze ans",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Nós moramos em Lichinga» escreve-se:",
                            "options": [
                                "Nous habitons à Lichinga",
                                "Nous habitent à Lichinga",
                                "Nous habite à Lichinga",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ela fala português» escreve-se:",
                            "options": [
                                "Elle parle portugais",
                                "Elle parles portugais",
                                "Elle parlez portugais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada profissão ao feminino, em "
                                 "francês.",
                            "pairs": [
                                ["Étudiant", "Étudiante"],
                                ["Infirmier", "Infirmière"],
                                ["Professeur", "Professeure"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Apresentar alguém",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Este é o meu amigo Paulo» escreve-se:",
                            "options": [
                                "C'est mon ami Paulo",
                                "Il est mon ami Paulo",
                                "Ce mon ami Paulo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ela é professora» escreve-se:",
                            "options": [
                                "Elle est professeure",
                                "C'est professeure",
                                "Elle est une professeure",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em francês, «qual é a "
                                 "tua nacionalidade»?",
                            "options": [
                                "Quelle est ta nationalité",
                                "Quel est ta nationalité",
                                "Quels est ta nationalité",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ele não é francês» escreve-se:",
                            "options": [
                                "Il n'est pas français",
                                "Il ne est pas français",
                                "Il est ne pas français",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada frase ao verbo que ela usa.",
                            "pairs": [
                                ["Je vais à l'école", "Aller"],
                                ["Tu viens de Maputo", "Venir"],
                                ["Nous faisons du sport", "Faire"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada artigo ao seu tipo.",
                            "pairs": [
                                ["Le, la, les", "Definidos"],
                                ["Un, une, des", "Indefinidos"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Descrever alguém",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada parte do corpo ao francês.",
                            "pairs": [
                                ["Os olhos", "Les yeux"],
                                ["O cabelo", "Les cheveux"],
                                ["A boca", "La bouche"],
                                ["O nariz", "Le nez"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada cor ao francês.",
                            "pairs": [
                                ["Vermelho", "Rouge"],
                                ["Azul", "Bleu"],
                                ["Verde", "Vert"],
                                ["Preto", "Noir"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Eu adoro música, mas detesto "
                                 "matemática» escreve-se:",
                            "options": [
                                "J'adore la musique, mais je déteste les "
                                "mathématiques",
                                "Je adore la musique, mais je déteste les "
                                "mathématiques",
                                "J'adore la musique, mais je détester les "
                                "mathématiques",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O Paulo é mais alto do que o João» "
                                 "escreve-se:",
                            "options": [
                                "Paulo est plus grand que João",
                                "Paulo est aussi grand que João",
                                "Paulo est moins grand que João",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Esta camisa é bonita» escreve-se, com o "
                                 "demonstrativo:",
                            "options": [
                                "Cette chemise est jolie",
                                "Ce chemise est jolie",
                                "Cet chemise est jolie",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada qualidade ao seu contrário, em "
                                 "francês.",
                            "pairs": [
                                ["Gentil", "Méchant"],
                                ["Grand", "Petit"],
                                ["Calme", "Nerveux"],
                            ],
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 2  L'ecole et les activites quotidiennes
        # ================================================================
        {
            "id": "u2",
            "titulo": "A escola e o dia-a-dia",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Onde está o colega",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se escreve, em francês, «onde está "
                                 "a Maria»?",
                            "options": [
                                "Où est Maria",
                                "Quand est Maria",
                                "Qui est Maria",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada expressão de lugar ao francês.",
                            "pairs": [
                                ["Ao lado de", "À côté de"],
                                ["À frente de", "Devant"],
                                ["Atrás de", "Derrière"],
                                ["Entre", "Entre"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«O Pedro está sentado à esquerda da "
                                 "janela» escreve-se:",
                            "options": [
                                "Pedro est assis à gauche de la fenêtre",
                                "Pedro est debout à gauche de la fenêtre",
                                "Pedro est assis à droite de la fenêtre",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada coisa da sala ao francês.",
                            "pairs": [
                                ["O quadro", "Le tableau"],
                                ["A janela", "La fenêtre"],
                                ["A cadeira", "La chaise"],
                                ["A mochila", "Le sac à dos"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Ela está de pé perto da porta» "
                                 "escreve-se:",
                            "options": [
                                "Elle est debout près de la porte",
                                "Elle est assise près de la porte",
                                "Elle est debout loin de la porte",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Comportar-se na aula",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Abram o livro!» escreve-se, no "
                                 "imperativo:",
                            "options": [
                                "Ouvrez le livre",
                                "Vous ouvrez le livre",
                                "Ouvrir le livre",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ouve o professor!» escreve-se:",
                            "options": [
                                "Écoute le professeur",
                                "Tu écoutes le professeur",
                                "Écouter le professeur",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em francês, «posso "
                                 "sair, por favor»?",
                            "options": [
                                "Est-ce que je peux sortir, s'il vous plaît",
                                "Est-ce que je peut sortir, s'il vous plaît",
                                "Je peux est-ce que sortir, s'il vous plaît",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Eu não percebo» escreve-se:",
                            "options": [
                                "Je ne comprends pas",
                                "Je comprends ne pas",
                                "Je pas comprends",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada comportamento ao francês.",
                            "pairs": [
                                ["Barulhento", "Bruyant"],
                                ["Preguiçoso", "Paresseux"],
                                ["Solidário", "Solidaire"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "As horas e o dia de um aluno",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Como se escreve, em francês, «que horas "
                                 "são»?",
                            "options": [
                                "Quelle heure est-il",
                                "Quel heure est-il",
                                "Quelle heure il est",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«São oito e meia» escreve-se:",
                            "options": [
                                "Il est huit heures et demie",
                                "Il est huit heures et quart",
                                "Il est huit heures moins le quart",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Eu levanto-me às seis horas» "
                                 "escreve-se:",
                            "options": [
                                "Je me lève à six heures",
                                "Je lève à six heures",
                                "Je me lever à six heures",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ela está a estudar» escreve-se, com a "
                                 "acção em curso:",
                            "options": [
                                "Elle est en train d'étudier",
                                "Elle est étudier",
                                "Elle en train étudie",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada marcador de ordem ao francês.",
                            "pairs": [
                                ["Primeiro", "D'abord"],
                                ["Depois", "Ensuite"],
                                ["Por fim", "Enfin"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada momento do dia ao francês.",
                            "pairs": [
                                ["A manhã", "Le matin"],
                                ["A tarde", "L'après-midi"],
                                ["A noite", "Le soir"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "O calendário escolar",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada mês ao francês.",
                            "pairs": [
                                ["Janeiro", "Janvier"],
                                ["Junho", "Juin"],
                                ["Setembro", "Septembre"],
                                ["Dezembro", "Décembre"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em francês, «quando "
                                 "começam as férias»?",
                            "options": [
                                "Quand commencent les vacances",
                                "Où commencent les vacances",
                                "Pourquoi commencent les vacances",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«As aulas vão de Fevereiro a Novembro» "
                                 "escreve-se:",
                            "options": [
                                "Les cours vont de février à novembre",
                                "Les cours vont à février de novembre",
                                "Les cours vont février jusqu'à novembre",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O 25 de Junho é o dia mais importante "
                                 "de Moçambique» escreve-se, com o "
                                 "superlativo:",
                            "options": [
                                "Le 25 juin est le jour le plus important "
                                "du Mozambique",
                                "Le 25 juin est le jour plus important du "
                                "Mozambique",
                                "Le 25 juin est le jour le moins important "
                                "du Mozambique",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada símbolo nacional ao francês.",
                            "pairs": [
                                ["A bandeira", "Le drapeau"],
                                ["O hino nacional", "L'hymne national"],
                                ["O emblema", "L'emblème"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n5",
                    "titulo": "A sala de aula",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Há um quadro na sala» escreve-se:",
                            "options": [
                                "Il y a un tableau dans la salle",
                                "Il a un tableau dans la salle",
                                "Il est un tableau dans la salle",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Não há computador» escreve-se:",
                            "options": [
                                "Il n'y a pas d'ordinateur",
                                "Il n'y a pas un ordinateur",
                                "Il y a ne pas ordinateur",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se escreve, em francês, «o que há "
                                 "em cima da mesa»?",
                            "options": [
                                "Qu'est-ce qu'il y a sur la table",
                                "Où est-ce qu'il y a sur la table",
                                "Qu'est-ce qu'il y a sous la table",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada preposição de lugar ao "
                                 "francês.",
                            "pairs": [
                                ["Em cima de", "Sur"],
                                ["Debaixo de", "Sous"],
                                ["Dentro de", "Dans"],
                                ["No chão", "Par terre"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "À pergunta «tu não tens caneta?» "
                                 "responde-se que sim com:",
                            "options": ["Si", "Oui", "Non"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n6",
                    "titulo": "Os objectos da escola",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada objecto da escola ao francês.",
                            "pairs": [
                                ["O caderno", "Le cahier"],
                                ["A caneta", "Le stylo"],
                                ["A régua", "La règle"],
                                ["A borracha", "La gomme"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«O meu caderno e a minha caneta» "
                                 "escreve-se:",
                            "options": [
                                "Mon cahier et mon stylo",
                                "Ma cahier et ma stylo",
                                "Mon cahier et ma stylo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A mochila dele é grande e verde» "
                                 "escreve-se:",
                            "options": [
                                "Son sac à dos est grand et vert",
                                "Sa sac à dos est grande et verte",
                                "Son sac à dos est grande et verte",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada característica de um objecto "
                                 "ao francês.",
                            "pairs": [
                                ["A forma", "La forme"],
                                ["O tamanho", "La taille"],
                                ["O peso", "Le poids"],
                                ["O material", "La matière"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Cuidar das carteiras e dos livros da "
                                 "escola é preservar o:",
                            "options": [
                                "Património escolar",
                                "Calendário escolar",
                                "Horário escolar",
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
