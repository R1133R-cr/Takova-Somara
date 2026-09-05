# -*- coding: utf-8 -*-
"""O curso de Historia da 7a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Historia -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024.
     Descarregado do educador.mozestuda.com.

Programa e nao livro do aluno, como os outros dois da 7a classe. Fica dito
no campo `fonte`.

A primeira disciplina de Historia da app
----------------------------------------
As classes 4a a 6a tem CIENCIAS SOCIAIS, que junta Historia e Geografia
num curso so, como o primario as ensina. No secundario separam-se, e sao
duas disciplinas com dois programas. Esta e a de Historia.

As quatro unidades tematicas, tal como o INDE as ordena
--------------------------------------------------------
    1o trimestre   1  A Historia como Ciencia
                   2  Origem e Evolucao do Homem
    2o trimestre   3  O surgimento da agricultura e a formacao dos
                      primeiros Estados no Mundo e em Africa
    3o trimestre   4  Reinos e imperios africanos do seculo IX ao XVII

Quatro unidades, tres niveis cada. Ao contrario do Portugues, aqui a
ordem do programa e a ordem do curso: e cronologica, e a Historia so faz
sentido pela ordem em que aconteceu.

O que este curso obrigou a mexer na app
----------------------------------------
Os seculos em numeracao romana. A lista de siglas so conhecia tres --
XV, XIX e XX -- e alarga-la seria perigoso, porque MIL e CIVIL tambem se
leem como numeros romanos. A regra nova esta ancorada na palavra
"seculo", e por isso apanha todos sem esse risco. Ver [dizer_seculos] no
tools/pronuncia.py.

Correr a partir de somara-flutter/:
    python tools/conteudo_his7c.py            # so mostra
    python tools/conteudo_his7c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de História — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024. As quatro unidades "
    "temáticas e os conteúdos são do programa; os exercícios foram "
    "escritos a partir deles, porque um programa de ensino não traz "
    "exercícios e não há livro do aluno da 7ª classe publicado."
)

CURSO = {
    "id": "his-7c",
    "disciplina": "História",
    "classe": "7ª classe",
    "tag": "HIS",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # Unidade Tematica 1: A Historia como Ciencia
        # INDE: 1.1 Definicao; 1.2 Importancia; 1.3 Fontes; 1.4 Relacao com
        #       outras ciencias; 1.5 O tempo em Historia
        # ================================================================
        {
            "id": "u1",
            "titulo": "A História como ciência",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O que é a História",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A História é a ciência que estuda:",
                            "options": [
                                "O passado das sociedades humanas",
                                "Os animais e as plantas",
                                "As rochas e os minerais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Estudar História serve sobretudo para:",
                            "options": [
                                "Compreender o presente a partir do passado",
                                "Decorar datas",
                                "Prever o futuro com exactidão",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas ciências ajuda a História "
                                 "escavando e estudando os vestígios "
                                 "materiais?",
                            "options": [
                                "A Arqueologia",
                                "A Economia",
                                "A Matemática",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Antropologia ajuda a História a estudar:",
                            "options": [
                                "Os costumes e a cultura dos povos",
                                "O relevo e o clima",
                                "As contas do Estado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada ciência ao que ela estuda.",
                            "pairs": [
                                ["Geografia", "O espaço e o território"],
                                ["Arqueologia", "Os vestígios materiais"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "As fontes da História",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma fonte histórica é:",
                            "options": [
                                "Tudo o que nos dá informação sobre o passado",
                                "Só um livro de História",
                                "Só um documento do Estado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma machadinha de pedra encontrada numa "
                                 "escavação é uma fonte:",
                            "options": ["Material", "Escrita", "Oral"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Porque é que as fontes orais são tão "
                                 "importantes na História de África?",
                            "options": [
                                "Porque muito do passado africano foi "
                                "transmitido de boca em boca, de geração em "
                                "geração",
                                "Porque são mais fáceis de recolher",
                                "Porque nunca se enganam",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            # Dizia "uma carta ESCRITA há cem anos é uma
                            # fonte:" e a resposta certa era "Escrita". A
                            # palavra estava no enunciado: respondia-se sem
                            # saber nada.
                            "q": "Uma carta de um comerciante do século XIX "
                                 "é uma fonte:",
                            "options": ["Escrita", "Oral", "Material"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Ilha de Moçambique é:",
                            "options": [
                                "Um local de interesse histórico",
                                "Uma fonte oral",
                                "Uma ciência auxiliar",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O tempo em História",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Quantos anos tem um século?",
                            "a": "100",
                        },
                        {
                            "t": "input",
                            "q": "Quantos anos tem uma década?",
                            "a": "10",
                        },
                        {
                            "t": "input",
                            "q": "Quantos anos tem um milénio?",
                            "a": "1000",
                        },
                        {
                            "t": "choice",
                            "q": "O ano de 1975 pertence ao século:",
                            "options": ["XX", "XIX", "XXI"],
                            "a": 0,
                        },
                        {
                            # A pergunta ao contrário de propósito: se o
                            # enunciado dissesse «o que querem dizer as
                            # siglas a.C. e d.C.», a voz podia lê-las por
                            # extenso e dar a resposta a quem está a ouvir.
                            # Assim as siglas ficam só nas opções, que são
                            # para ler.
                            "t": "choice",
                            "q": "Que letras se escrevem a seguir a uma data "
                                 "para dizer que ela é anterior ao "
                                 "nascimento de Cristo?",
                            "options": ["a.C.", "d.C.", "s.C."],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica 2: Origem e Evolucao do Homem
        # INDE: 2.1 A origem do Homem; 2.2 Africa: o berco da Humanidade
        # ================================================================
        {
            "id": "u2",
            "titulo": "A origem e a evolução do Homem",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "As teorias sobre a origem do Homem",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A teoria da criação explica a origem do "
                                 "Homem:",
                            "options": [
                                "Por acção divina",
                                "Por transformação lenta ao longo do tempo",
                                "Por acaso",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A teoria da evolução defende que o Homem:",
                            "options": [
                                "Resultou de transformações lentas ao longo "
                                "de milhões de anos",
                                "Apareceu de uma só vez, como é hoje",
                                "Veio de outro planeta",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Chama-se hominização ao processo de:",
                            "options": [
                                "Transformação que levou aos seres humanos "
                                "actuais",
                                "Construção das primeiras cidades",
                                "Descoberta da escrita",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes NÃO é um factor da hominização?",
                            "options": [
                                "A invenção da escrita",
                                "A posição erecta e a libertação das mãos",
                                "O aumento do volume do cérebro",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "África, o berço da Humanidade",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Diz-se que África é o berço da Humanidade "
                                 "porque:",
                            "options": [
                                "É aí que se encontraram os vestígios mais "
                                "antigos dos hominídeos",
                                "É o continente maior",
                                "Foi aí que se inventou a escrita",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em que região de África se encontraram "
                                 "muitos dos restos ósseos mais antigos?",
                            "options": [
                                "No Vale do Rift, na África Oriental",
                                "No deserto do Saara",
                                "Na ilha de Madagáscar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O trabalho teve importância na evolução "
                                 "humana porque:",
                            "options": [
                                "Desenvolveu as mãos e a inteligência",
                                "Cansava os primeiros homens",
                                "Não teve importância nenhuma",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os primeiros instrumentos do Homem eram "
                                 "feitos sobretudo de:",
                            "options": ["Pedra lascada", "Ferro", "Plástico"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O fogo, os nómadas e os sedentários",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Qual destas NÃO foi uma consequência da "
                                 "conquista do fogo?",
                            "options": [
                                "A invenção da roda",
                                "Poder cozinhar os alimentos",
                                "Afastar os animais perigosos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma sociedade nómada é aquela que:",
                            "options": [
                                "Se desloca à procura de alimento",
                                "Vive sempre no mesmo lugar",
                                "Já conhece a escrita",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O que permitiu ao Homem tornar-se "
                                 "sedentário?",
                            "options": [
                                "A agricultura e a criação de animais",
                                "A caça de animais grandes",
                                "A descoberta do ferro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As pinturas rupestres mostram que os "
                                 "primeiros homens:",
                            "options": [
                                "Já tinham manifestações artísticas e "
                                "religiosas",
                                "Sabiam ler e escrever",
                                "Viviam em cidades",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica 3: O surgimento da agricultura e a formacao dos
        # primeiros Estados no Mundo e em Africa
        # ================================================================
        {
            "id": "u3",
            "titulo": "A agricultura e os primeiros Estados",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O surgimento da agricultura",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A agricultura mudou a vida do Homem "
                                 "porque:",
                            "options": [
                                "Permitiu produzir alimento e fixar-se num "
                                "lugar",
                                "Tornou a caça mais fácil",
                                "Acabou com o trabalho",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Chama-se domesticação ao processo de:",
                            "options": [
                                "Criar e aproveitar animais selvagens junto "
                                "do Homem",
                                "Construir casas de pedra",
                                "Fabricar instrumentos de metal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quando um grupo passou a produzir mais do "
                                 "que consumia, apareceu:",
                            "options": [
                                "O excedente, e com ele a diferenciação "
                                "social",
                                "A escrita",
                                "O nomadismo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A pastorícia é a actividade de:",
                            "options": [
                                "Criar gado",
                                "Cultivar cereais",
                                "Pescar no rio",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O Egipto Antigo e a Mesopotâmia",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O Egipto Antigo desenvolveu-se no vale do "
                                 "rio:",
                            "options": ["Nilo", "Zambeze", "Congo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No Egipto Antigo, o chefe do Estado era:",
                            "options": ["O faraó", "O imperador", "O rei-sol"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Mesopotâmia ficava entre os rios:",
                            "options": [
                                "Tigre e Eufrates",
                                "Nilo e Níger",
                                "Limpopo e Save",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O Código de Hamurábi é importante porque "
                                 "foi:",
                            "options": [
                                "Um dos primeiros conjuntos de leis escritas",
                                "O primeiro livro de História",
                                "Um mapa do mundo antigo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A escrita da Mesopotâmia chamava-se:",
                            "options": [
                                "Cuneiforme",
                                "Hieroglífica",
                                "Alfabética",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A Grécia e Roma",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As cidades-Estado da Grécia Antiga "
                                 "chamavam-se:",
                            "options": ["Pólis", "Províncias", "Reinos"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na democracia ateniense participavam:",
                            "options": [
                                "Apenas os cidadãos homens livres",
                                "Todos os habitantes da cidade",
                                "Apenas os escravos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quem estava excluído da democracia "
                                 "ateniense?",
                            "options": [
                                "As mulheres, os escravos e os estrangeiros",
                                "Só os estrangeiros",
                                "Ninguém",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na Roma Antiga, os escravos eram sobretudo:",
                            "options": [
                                "Prisioneiros de guerra",
                                "Cidadãos que escolhiam sê-lo",
                                "Estrangeiros pagos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma sociedade esclavagista é aquela em que:",
                            "options": [
                                "O trabalho assenta em pessoas escravizadas",
                                "Todos trabalham a mesma coisa",
                                "Não há Estado",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica 4: Reinos e imperios africanos do seculo IX ao
        # XVII
        # ================================================================
        {
            "id": "u4",
            "titulo": "Reinos e impérios africanos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Os Khoisan e os povos de língua bantu",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Os Khoisan viviam sobretudo da:",
                            "options": [
                                "Caça e da recolecção",
                                "Agricultura em grande escala",
                                "Metalurgia do ferro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os povos de língua bantu distinguiram-se "
                                 "por conhecerem:",
                            "options": [
                                "A agricultura e a metalurgia do ferro",
                                "A escrita alfabética",
                                "A navegação oceânica",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A expansão bantu trouxe a Moçambique:",
                            "options": [
                                "Novas técnicas agrícolas e o uso do ferro",
                                "O fim da agricultura",
                                "A escrita cuneiforme",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os Khoisan organizavam-se em:",
                            "options": [
                                "Pequenos grupos ou bandos",
                                "Grandes impérios",
                                "Cidades muradas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O Reino do Zimbabwe e o Império de Mutapa",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O Grande Zimbabwe ficou conhecido "
                                 "sobretudo pelas suas:",
                            "options": [
                                "Construções de pedra sem argamassa",
                                "Pirâmides",
                                "Estradas de pedra",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A riqueza do Reino do Zimbabwe vinha "
                                 "sobretudo do comércio de:",
                            "options": [
                                "Ouro e marfim",
                                "Sal e trigo",
                                "Livros e papel",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O Império de Mutapa formou-se no vale do "
                                 "rio:",
                            "options": ["Zambeze", "Nilo", "Níger"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Com quem comerciava o Império de Mutapa na "
                                 "costa?",
                            "options": [
                                "Com os mercadores swahili, e mais tarde com "
                                "os portugueses",
                                "Com os gregos",
                                "Com os egípcios",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O território do Império de Mutapa fica hoje "
                                 "sobretudo em:",
                            "options": [
                                "Moçambique e Zimbabwe",
                                "Angola e Namíbia",
                                "Quénia e Tanzânia",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Ghana, Mali e Songhai",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A riqueza do Império do Ghana assentava no "
                                 "comércio de:",
                            "options": [
                                "Ouro e sal, através do Saara",
                                "Ouro e marfim, pelo Índico",
                                "Trigo e vinho",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Que cidade do Império do Mali ficou "
                                 "célebre como centro de comércio e de "
                                 "estudo?",
                            "options": ["Timbuctu", "Cairo", "Gao"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Mansa Musa ficou conhecido por ter sido:",
                            "options": [
                                "Um imperador do Mali de enorme riqueza",
                                "Um faraó do Egipto",
                                "Um rei do Zimbabwe",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O Império Songhai teve como capital:",
                            "options": ["Gao", "Timbuctu", "Cairo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O comércio transaariano fazia-se "
                                 "atravessando o deserto com:",
                            "options": [
                                "Caravanas de camelos",
                                "Barcos a remos",
                                "Comboios",
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
