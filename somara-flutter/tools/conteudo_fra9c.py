# -*- coding: utf-8 -*-
"""O curso de Frances da 9a classe.

De onde vem
-----------
    "Programme d'Enseignement de la Discipline de Langue Francaise --
     Enseignement Secondaire -- 1er Cycle", INDE/MINEDH, Maputo,
     Setembro de 2024, 9eme classe, pp. 8 (apercu) e 22-31 (plans
     thematiques). Guardado em Documents\\planos da 5a classe\\Livros\\
     Programas INDE 1o Ciclo\\frances.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As duas unidades tematicas da 9eme, pela ordem do programa
----------------------------------------------------------
    1  Ma famille                   1 Famille
                                    2 Que fete-t-on ?
                                    3 Lettre et email d'invitation
                                    4 Invitation par telephone
                                    5 Alimentation
                                    6 Maison
                                    7 Petites annonces location
    2  L'ecole et les activites     1 Reglement scolaire
       quotidiennes (suite)         2 Presentation d'une ecole

Duas unidades, nove aulas: uma por tema do programa.

O frances fica nas opcoes, como na 8a
-------------------------------------
Os enunciados sao em portugues e o frances aparece so nas opcoes e nos
pares.

Correr a partir de somara-flutter/:
    python tools/conteudo_fra9c.py            # so mostra
    python tools/conteudo_fra9c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programme d'Enseignement de la Discipline de Langue Française — "
    "Enseignement Secondaire, 1er Cycle. INDE/MINEDH, Maputo, Setembro de "
    "2024, 9ème classe, pp. 8 e 22-31. As duas unidades, os nove temas, o "
    "vocabulário e a gramática são do programa; os exercícios foram "
    "escritos a partir deles, porque um programa de ensino não traz "
    "exercícios e não há livro do aluno da 9ª classe publicado. Os "
    "enunciados são em português e o francês fica nas opções, porque a voz "
    "da app é portuguesa."
)

CURSO = {
    "id": "fra-9c",
    "disciplina": "Francês",
    "classe": "9ª classe",
    "tag": "FRA",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # 1  Ma famille
        # ================================================================
        {
            "id": "u1",
            "titulo": "A minha família",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A família e os possessivos",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada membro da família ao francês.",
                            "pairs": [
                                ["O avô", "Le grand-père"],
                                ["A tia", "La tante"],
                                ["O primo", "Le cousin"],
                                ["Os pais", "Les parents"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«A minha mãe e o meu pai» escreve-se:",
                            "options": [
                                "Ma mère et mon père",
                                "Mon mère et ma père",
                                "Mes mère et mes père",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Este livro é o meu» escreve-se, com o "
                                 "pronome possessivo:",
                            "options": [
                                "Ce livre est le mien",
                                "Ce livre est mon",
                                "Ce livre est la mienne",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de família ao francês.",
                            "pairs": [
                                ["Família tradicional", "Famille traditionnelle"],
                                ["Família monoparental", "Famille monoparentale"],
                                ["Família recomposta", "Famille recomposée"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Eu prefiro a minha irmã mais nova» "
                                 "escreve-se:",
                            "options": [
                                "Je préfère ma petite sœur",
                                "Je préfére mon petite sœur",
                                "Je préfère ma petit sœur",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "As festas e as cerimónias",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada festa ou cerimónia ao francês.",
                            "pairs": [
                                ["Aniversário", "L'anniversaire"],
                                ["Noivado", "Les fiançailles"],
                                ["Casamento", "Le mariage"],
                                ["Funeral", "Les funérailles"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um cartão que anuncia um casamento ou um "
                                 "nascimento chama-se, em francês:",
                            "options": ["Un faire-part", "Une recette", "Un règlement"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de casamento ao francês.",
                            "pairs": [
                                ["Tradicional", "Traditionnel"],
                                ["Religioso", "Religieux"],
                                ["Civil", "Officiel"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Nós decoramos a sala e dançamos» "
                                 "escreve-se:",
                            "options": [
                                "Nous décorons la salle et nous dansons",
                                "Nous décorez la salle et nous dansez",
                                "Nous décore la salle et nous danse",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Num cartão de boas festas escreve-se:",
                            "options": [
                                "Meilleurs vœux",
                                "Bon appétit",
                                "Au secours",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A carta e o email de convite",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada parte da carta ao francês.",
                            "pairs": [
                                ["Local e data", "Lieu et date"],
                                ["Destinatário", "Destinataire"],
                                ["Assinatura", "Signature"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Queres vir à minha festa?» escreve-se:",
                            "options": [
                                "Tu veux venir à ma fête",
                                "Tu voulez venir à ma fête",
                                "Tu veux viens à ma fête",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para aceitar um convite diz-se:",
                            "options": [
                                "Avec plaisir, je viens",
                                "Désolé, je ne peux pas",
                                "Non, merci",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Não posso ir, tenho um exame» "
                                 "escreve-se:",
                            "options": [
                                "Je ne peux pas venir, j'ai un examen",
                                "Je peux ne pas venir, j'ai un examen",
                                "Je ne pas peux venir, j'ai un examen",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma carta a um amigo começa com a "
                                 "fórmula:",
                            "options": ["Cher ami", "Monsieur le Directeur", "Au revoir"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "O convite pelo telefone",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada palavra do telefone ao francês.",
                            "pairs": [
                                ["Telemóvel", "Le portable"],
                                ["Chamada", "L'appel"],
                                ["Rede", "Le réseau"],
                                ["Bateria", "La batterie"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada acção ao verbo francês.",
                            "pairs": [
                                ["Atender", "Décrocher"],
                                ["Desligar", "Raccrocher"],
                                ["Voltar a ligar", "Rappeler"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Ao atender o telefone em França, diz-se:",
                            "options": ["Allô", "Salut, merci", "Bon appétit"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Queres ir ao cinema no sábado?» "
                                 "escreve-se, com «est-ce que»:",
                            "options": [
                                "Est-ce que tu veux aller au cinéma samedi",
                                "Est-ce tu veux aller au cinéma samedi",
                                "Est-ce que veux tu aller au cinéma samedi",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para recusar com educação diz-se:",
                            "options": [
                                "C'est gentil, mais je ne suis pas libre",
                                "Non, je ne veux pas, au revoir",
                                "Laisse-moi tranquille",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n5",
                    "titulo": "A alimentação",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada refeição do dia ao francês.",
                            "pairs": [
                                ["Pequeno-almoço", "Le petit-déjeuner"],
                                ["Almoço", "Le déjeuner"],
                                ["Lanche", "Le goûter"],
                                ["Jantar", "Le dîner"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Eu como pão e bebo leite» escreve-se, "
                                 "com os partitivos:",
                            "options": [
                                "Je mange du pain et je bois du lait",
                                "Je mange le pain et je bois le lait",
                                "Je mange de pain et je bois de lait",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Quanto custa o peixe?» escreve-se:",
                            "options": [
                                "Combien coûte le poisson",
                                "Comment coûte le poisson",
                                "Combien de coûte le poisson",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Queres arroz? Sim, quero um pouco» "
                                 "escreve-se, com o pronome «en»:",
                            "options": [
                                "Tu veux du riz ? Oui, j'en veux un peu",
                                "Tu veux du riz ? Oui, je le veux un peu",
                                "Tu veux du riz ? Oui, je veux en un peu",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«É preciso comer fruta» escreve-se:",
                            "options": [
                                "Il faut manger des fruits",
                                "Il faut mange des fruits",
                                "Il faut de manger des fruits",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n6",
                    "titulo": "A casa e as tarefas",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada divisão da casa ao francês.",
                            "pairs": [
                                ["Quarto", "La chambre"],
                                ["Cozinha", "La cuisine"],
                                ["Sala de jantar", "La salle à manger"],
                                ["Casa de banho", "La salle de bains"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada móvel ou aparelho ao francês.",
                            "pairs": [
                                ["Cama", "Le lit"],
                                ["Armário", "L'armoire"],
                                ["Frigorífico", "Le frigo"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Não há ninguém na cozinha» escreve-se:",
                            "options": [
                                "Il n'y a personne dans la cuisine",
                                "Il n'y a pas personne dans la cuisine",
                                "Il y a personne ne dans la cuisine",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Não comprei nada» escreve-se:",
                            "options": [
                                "Je n'ai rien acheté",
                                "Je n'ai pas rien acheté",
                                "Je rien ai acheté",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em casa, as tarefas domésticas:",
                            "options": [
                                "Dividem-se entre rapazes e raparigas",
                                "São só das raparigas",
                                "São só dos adultos",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n7",
                    "titulo": "Os anúncios de arrendamento",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada verbo ao francês.",
                            "pairs": [
                                ["Arrendar", "Louer"],
                                ["Vender", "Vendre"],
                                ["Procurar", "Chercher"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Num anúncio, «T3» ou «trois pièces» "
                                 "quer dizer:",
                            "options": [
                                "Uma casa com três divisões",
                                "Três casas",
                                "O terceiro andar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O apartamento fica no segundo andar» "
                                 "escreve-se, com o ordinal:",
                            "options": [
                                "L'appartement est au deuxième étage",
                                "L'appartement est au deux étage",
                                "L'appartement est au second étages",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Esta casa é a mais barata» escreve-se:",
                            "options": [
                                "Cette maison est la moins chère",
                                "Cette maison est la plus chère",
                                "Cette maison est moins chère que",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A casa é tão grande como o "
                                 "apartamento» escreve-se:",
                            "options": [
                                "La maison est aussi grande que "
                                "l'appartement",
                                "La maison est plus grande "
                                "l'appartement",
                                "La maison est aussi grande comme "
                                "l'appartement",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 2  L'ecole et les activites quotidiennes (suite)
        # ================================================================
        {
            "id": "u2",
            "titulo": "A escola, outra vez",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O regulamento escolar",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada frase do regulamento ao que "
                                 "ela exprime.",
                            "pairs": [
                                ["On peut sortir à la récréation", "Permissão"],
                                ["Il est interdit de fumer", "Proibição"],
                                ["Il faut arriver à l'heure", "Obrigação"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Os alunos devem fazer os trabalhos» "
                                 "escreve-se:",
                            "options": [
                                "Les élèves doivent faire les devoirs",
                                "Les élèves doit faire les devoirs",
                                "Les élèves devons faire les devoirs",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Proibido correr nos corredores» "
                                 "escreve-se:",
                            "options": [
                                "Défense de courir dans les couloirs",
                                "Il faut courir dans les couloirs",
                                "On peut courir dans les couloirs",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada palavra da escola ao francês.",
                            "pairs": [
                                ["Atraso", "Le retard"],
                                ["Faltas", "Les absences"],
                                ["Recreio", "La récréation"],
                                ["Giz", "La craie"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Não é preciso gritar» escreve-se:",
                            "options": [
                                "Il ne faut pas crier",
                                "Il faut ne pas crier",
                                "Il ne pas faut crier",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Apresentar uma escola",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada pessoa da escola ao francês.",
                            "pairs": [
                                ["O director", "Le directeur"],
                                ["O director adjunto", "Le directeur adjoint"],
                                ["A secretária", "La secrétaire"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada pergunta ao que ela pede.",
                            "pairs": [
                                ["Qui ?", "Uma pessoa"],
                                ["Quand ?", "Um tempo"],
                                ["Pourquoi ?", "Uma razão"],
                                ["Combien ?", "Uma quantidade"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "«Quantos alunos há na escola?» "
                                 "escreve-se:",
                            "options": [
                                "Combien d'élèves il y a dans l'école",
                                "Comment d'élèves il y a dans l'école",
                                "Combien élèves il y a dans l'école",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«A secretaria fica ao lado da "
                                 "biblioteca» escreve-se:",
                            "options": [
                                "Le secrétariat est à côté de la "
                                "bibliothèque",
                                "Le secrétariat est à côté la "
                                "bibliothèque",
                                "Le secrétariat est côté de la "
                                "bibliothèque",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Respeitar o guarda, a senhora da limpeza "
                                 "e o professor é:",
                            "options": [
                                "Respeitar todas as profissões da escola",
                                "Só obrigação dos pais",
                                "Desnecessário",
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
