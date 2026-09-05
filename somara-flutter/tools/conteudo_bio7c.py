# -*- coding: utf-8 -*-
"""O curso de Biologia da 7a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Biologia -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024.
     Descarregado do educador.mozestuda.com.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

A Biologia comeca na 7a; a Fisica e a Quimica nao
-------------------------------------------------
Das tres Ciencias do 1o ciclo, so a Biologia tem 7a classe. Os programas
de Fisica e de Quimica nao mencionam a 7a uma unica vez: as tabelas de
conteudos de ambos tem colunas para a 8a e a 9a e mais nada. Comecam na
8a, e por isso nao entram nesta classe.

As cinco unidades tematicas, tal como o INDE as ordena
-------------------------------------------------------
    1  Introducao a Biologia          conceito, ramos, metodo cientifico,
                                      primeiros socorros
    2  Seres vivos e ambiente         celula, microscopio, classificacao,
                                      plantas, animais
    3  Alimentacao, Nutricao e Saude  nutrientes, conservacao, intoxicacao
    4  Sistemas do corpo humano       digestivo, dentes, circulatorio,
                                      respiratorio
    5  Auto-descobrimento             adolescencia e relacionamentos

Cinco unidades, tres niveis cada. A ordem e a do programa.

Correr a partir de somara-flutter/:
    python tools/conteudo_bio7c.py            # so mostra
    python tools/conteudo_bio7c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Biologia — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024. As cinco unidades "
    "temáticas e os conteúdos são do programa; os exercícios foram "
    "escritos a partir deles, porque um programa de ensino não traz "
    "exercícios e não há livro do aluno da 7ª classe publicado."
)

CURSO = {
    "id": "bio-7c",
    "disciplina": "Biologia",
    "classe": "7ª classe",
    "tag": "BIO",
    "fonte": FONTE,
    "units": [
        {
            "id": "u1",
            "titulo": "Introdução à Biologia",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A Biologia e os seus ramos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Biologia é a ciência que estuda:",
                            "options": [
                                "Os seres vivos e a vida",
                                "As rochas e os minerais",
                                "Os astros e os planetas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A palavra «Biologia» vem do grego e quer "
                                 "dizer:",
                            "options": [
                                "Ciência da vida",
                                "Ciência da terra",
                                "Ciência do corpo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O ramo da Biologia que estuda os animais "
                                 "chama-se:",
                            "options": ["Zoologia", "Botânica", "Citologia"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O ramo que estuda as plantas chama-se:",
                            "options": ["Botânica", "Zoologia", "Anatomia"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada ramo da Biologia ao que ele "
                                 "estuda.",
                            "pairs": [
                                ["Citologia", "A célula"],
                                ["Anatomia", "A forma do corpo"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O método científico",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O método científico começa por:",
                            "options": [
                                "Observar com atenção",
                                "Tirar conclusões",
                                "Escrever o relatório",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A experimentação serve para:",
                            "options": [
                                "Pôr à prova o que se pensa que acontece",
                                "Confirmar sempre a opinião do cientista",
                                "Evitar ter de observar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de mexer numa substância numa "
                                 "experiência, deve-se:",
                            "options": [
                                "Ler o rótulo e conhecer os riscos",
                                "Provar um pouco para ver o sabor",
                                "Cheirar de perto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa aula prática, o que NUNCA se deve "
                                 "fazer?",
                            "options": [
                                "Realizar actividades não autorizadas",
                                "Lavar as mãos no fim",
                                "Registar o que se observou",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Primeiros socorros",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Perante um ferimento com corte, a primeira "
                                 "coisa a fazer é:",
                            "options": [
                                "Lavar a ferida com água e sabão",
                                "Deitar areia por cima",
                                "Esperar que pare sozinho",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa queimadura ligeira, deve-se:",
                            "options": [
                                "Arrefecer com água corrente e não rebentar "
                                "as bolhas",
                                "Pôr óleo ou pasta de dentes",
                                "Rebentar as bolhas com uma agulha",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Se alguém engolir um produto tóxico, "
                                 "deve-se:",
                            "options": [
                                "Levar ao hospital com a embalagem do produto",
                                "Dar de beber muito leite e esperar",
                                "Fazer vomitar sempre",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os primeiros socorros são:",
                            "options": [
                                "Os cuidados imediatos até chegar ajuda médica",
                                "O tratamento completo da doença",
                                "Um exame feito no hospital",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u2",
            "titulo": "Seres vivos e ambiente",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A célula e o microscópio",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A célula é:",
                            "options": [
                                "A unidade básica dos seres vivos",
                                "Um órgão do corpo humano",
                                "Um tipo de microscópio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para ver uma célula é preciso:",
                            "options": [
                                "Um microscópio",
                                "Uma lupa de bolso",
                                "Um telescópio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas partes existe na célula vegetal "
                                 "e não na animal?",
                            "options": [
                                "A parede celular",
                                "O núcleo",
                                "O citoplasma",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O microscópio electrónico distingue-se do "
                                 "óptico porque:",
                            "options": [
                                "Amplia muito mais",
                                "É mais pequeno",
                                "Usa luz do sol",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A parte da célula que comanda o seu "
                                 "funcionamento é:",
                            "options": ["O núcleo", "A membrana", "A parede"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Classificar os seres vivos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Classificar os seres vivos serve para:",
                            "options": [
                                "Os organizar em grupos com características "
                                "comuns",
                                "Decidir quais são mais úteis",
                                "Contar quantos existem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um ser vivo formado por uma só célula "
                                 "diz-se:",
                            "options": [
                                "Unicelular",
                                "Pluricelular",
                                "Vertebrado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As bactérias são seres:",
                            "options": [
                                "Unicelulares",
                                "Pluricelulares",
                                "Vertebrados",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os fungos, como os cogumelos, alimentam-se:",
                            "options": [
                                "De matéria orgânica já formada",
                                "Fazendo fotossíntese",
                                "Só de água",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Plantas e animais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As plantas produzem o seu alimento por:",
                            "options": [
                                "Fotossíntese",
                                "Respiração",
                                "Digestão",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na fotossíntese, a planta liberta:",
                            "options": [
                                "Oxigénio",
                                "Dióxido de carbono",
                                "Azoto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os animais com coluna vertebral chamam-se:",
                            "options": [
                                "Vertebrados",
                                "Invertebrados",
                                "Mamíferos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um invertebrado?",
                            "options": ["A minhoca", "O peixe", "A cobra"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As plantas são importantes para o ambiente "
                                 "porque:",
                            "options": [
                                "Produzem oxigénio e seguram o solo",
                                "Só servem de alimento",
                                "Não têm importância nenhuma",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u3",
            "titulo": "Alimentação, nutrição e saúde",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Alimentos e nutrientes",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um nutriente é:",
                            "options": [
                                "A substância do alimento que o corpo "
                                "aproveita",
                                "Qualquer coisa que se come",
                                "Uma refeição completa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os alimentos que dão sobretudo energia são "
                                 "ricos em:",
                            "options": [
                                "Hidratos de carbono",
                                "Vitaminas",
                                "Água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As proteínas servem sobretudo para:",
                            "options": [
                                "Construir e reparar o corpo",
                                "Dar energia imediata",
                                "Arrefecer o corpo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma alimentação equilibrada é aquela que:",
                            "options": [
                                "Tem alimentos variados e nas quantidades "
                                "certas",
                                "Tem sempre carne",
                                "É a mais barata",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A laranja e o limão são ricos sobretudo em:",
                            "options": [
                                "Vitamina C",
                                "Gorduras",
                                "Proteínas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Conservar os alimentos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Conservar os alimentos serve para:",
                            "options": [
                                "Travar os micróbios que os estragam",
                                "Os tornar mais saborosos",
                                "Aumentar a sua quantidade",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um método tradicional de "
                                 "conservação?",
                            "options": [
                                "Secar ao sol",
                                "Guardar num saco fechado ao calor",
                                "Deixar ao ar livre molhado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de preparar comida, deve-se sempre:",
                            "options": [
                                "Lavar bem as mãos",
                                "Provar os alimentos crus",
                                "Deixar a comida destapada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A salga conserva o peixe porque:",
                            "options": [
                                "Tira a água de que os micróbios precisam",
                                "Aquece o peixe",
                                "Adiciona vitaminas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Intoxicação alimentar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A intoxicação alimentar acontece quando se "
                                 "come:",
                            "options": [
                                "Alimento estragado ou contaminado",
                                "Alimento demasiado quente",
                                "Alimento sem sal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um sinal comum de "
                                 "intoxicação alimentar?",
                            "options": [
                                "Vómitos e diarreia",
                                "Dor de dentes",
                                "Visão turva apenas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quem tem diarreia deve sobretudo:",
                            "options": [
                                "Beber muitos líquidos para não desidratar",
                                "Deixar de beber água",
                                "Comer mais gordura",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para evitar a cólera é essencial:",
                            "options": [
                                "Beber água tratada ou fervida",
                                "Comer só à noite",
                                "Beber água do rio",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u4",
            "titulo": "Sistemas do corpo humano",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O sistema digestivo e os dentes",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A digestão começa:",
                            "options": ["Na boca", "No estômago", "No intestino"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A absorção dos nutrientes faz-se sobretudo:",
                            "options": [
                                "No intestino delgado",
                                "No esófago",
                                "Na boca",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Quantos dentes tem, normalmente, um adulto?",
                            "a": "32",
                        },
                        {
                            "t": "choice",
                            "q": "Os dentes que servem para cortar os "
                                 "alimentos são:",
                            "options": ["Os incisivos", "Os molares", "Os caninos"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A cárie dentária resulta sobretudo de:",
                            "options": [
                                "Restos de açúcar e falta de higiene",
                                "Beber água",
                                "Escovar os dentes",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O sistema circulatório",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O órgão que bombeia o sangue é:",
                            "options": ["O coração", "O pulmão", "O fígado"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os vasos que levam o sangue do coração "
                                 "para o corpo chamam-se:",
                            "options": ["Artérias", "Veias", "Nervos"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os glóbulos vermelhos servem para:",
                            "options": [
                                "Transportar o oxigénio",
                                "Defender o corpo dos micróbios",
                                "Coagular o sangue",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os glóbulos brancos servem para:",
                            "options": [
                                "Defender o corpo dos micróbios",
                                "Transportar oxigénio",
                                "Dar cor ao sangue",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O sistema respiratório",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As trocas gasosas fazem-se:",
                            "options": [
                                "Nos alvéolos pulmonares",
                                "No estômago",
                                "No coração",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao inspirar, entra no corpo sobretudo:",
                            "options": [
                                "Oxigénio",
                                "Dióxido de carbono",
                                "Azoto puro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os dois movimentos respiratórios "
                                 "chamam-se:",
                            "options": [
                                "Inspiração e expiração",
                                "Sístole e diástole",
                                "Digestão e absorção",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O tabaco prejudica sobretudo:",
                            "options": [
                                "Os pulmões",
                                "Os ossos",
                                "Os dentes de leite",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A imunidade é a capacidade do corpo de:",
                            "options": [
                                "Se defender das doenças",
                                "Digerir os alimentos",
                                "Crescer depressa",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u5",
            "titulo": "Auto-descobrimento",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A adolescência",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A adolescência é:",
                            "options": [
                                "A fase de passagem da infância para a idade "
                                "adulta",
                                "Uma doença passageira",
                                "O fim do crescimento",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As mudanças do corpo na adolescência são:",
                            "options": [
                                "Normais e acontecem a toda a gente",
                                "Um sinal de doença",
                                "Iguais em todos ao mesmo tempo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Se tiveres dúvidas sobre o teu corpo, o "
                                 "melhor é:",
                            "options": [
                                "Falar com um adulto de confiança ou um "
                                "profissional de saúde",
                                "Guardar para ti",
                                "Perguntar só a quem tem a tua idade",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A higiene pessoal na adolescência é:",
                            "options": [
                                "Mais importante, porque o corpo transpira "
                                "mais",
                                "Menos importante do que na infância",
                                "Indiferente",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Relacionamentos e respeito",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Num relacionamento saudável há sempre:",
                            "options": [
                                "Respeito mútuo",
                                "Uma pessoa a mandar",
                                "Ciúmes constantes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Se alguém te pressionar a fazer algo que "
                                 "não queres, deves:",
                            "options": [
                                "Dizer que não e procurar ajuda de um adulto",
                                "Ceder para não perder a amizade",
                                "Ficar calado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A gravidez precoce prejudica sobretudo:",
                            "options": [
                                "A saúde e os estudos da rapariga",
                                "Apenas a família",
                                "Ninguém",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Continuar a estudar durante a adolescência "
                                 "é importante porque:",
                            "options": [
                                "Abre mais escolhas para o futuro",
                                "É obrigatório e mais nada",
                                "Evita o crescimento",
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
    if CURSO["id"] in [c["id"] for c in dados["cursos"]]:
        print(f"o curso {CURSO['id']} ja esta no content.json", file=sys.stderr)
        return 1

    niveis = sum(len(u["niveis"]) for u in CURSO["units"])
    perguntas = sum(len(n["questoes"])
                    for u in CURSO["units"] for n in u["niveis"])
    print(f"{CURSO['disciplina']} da {CURSO['classe']}: "
          f"{len(CURSO['units'])} unidades, {niveis} niveis, "
          f"{perguntas} perguntas")
    for u in CURSO["units"]:
        for n in u["niveis"]:
            print(f"   {u['id']}/{n['id']}  {n['titulo']:<42}"
                  f"{len(n['questoes'])}q")

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

    dados["cursos"].append(CURSO)
    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
