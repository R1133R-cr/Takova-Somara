# -*- coding: utf-8 -*-
"""O curso de Historia da 8a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Historia -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, pp. 24-34.
     Guardado em Documents\\planos da 5a classe\\Livros\\Programas INDE 1o
     Ciclo\\historia.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

Do Antigo Regime ao Imperialismo, e Mocambique dentro de cada unidade
---------------------------------------------------------------------
A 7a foi das origens ate aos reinos africanos. A 8a e a formacao do mundo
capitalista, do seculo XV ao XIX, e o programa mete Mocambique em todas as
unidades: a expansao portuguesa e o trafico, a presenca europeia na epoca
das revolucoes, a partilha imperialista e a resistencia.

    1o e 2o trim.  I    A formacao do sistema capitalista mundial
                        (secs. XV-XVIII): Antigo Regime, Africa,
                        expansao europeia, Renascimento, Reforma,
                        Mercantilismo, Absolutismo, Revolucoes Burguesas
    2o trimestre   II   Africa e Mocambique na epoca das revolucoes
    3o trimestre   III  A Revolucao Industrial e o movimento operario
                   IV   Do capitalismo industrial ao imperialismo:
                        monopolios, partilha de Africa, resistencia

Quatro unidades, doze aulas: cinco na primeira, porque e ela que ocupa
dois trimestres.

Correr a partir de somara-flutter/:
    python tools/conteudo_his8c.py            # so mostra
    python tools/conteudo_his8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de História — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, pp. 24-34. As quatro "
    "unidades e os conteúdos são do programa; os exercícios foram escritos "
    "a partir deles, porque um programa de ensino não traz exercícios e não "
    "há livro do aluno da 8ª classe publicado."
)

CURSO = {
    "id": "his-8c",
    "disciplina": "História",
    "classe": "8ª classe",
    "tag": "HIS",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # Unidade I: A formacao do sistema capitalista mundial, XV-XVIII
        # ================================================================
        {
            "id": "u1",
            "titulo": "A formação do sistema capitalista",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A Europa e a África no século XV",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "No Antigo Regime, a sociedade europeia "
                                 "dividia-se em:",
                            "options": [
                                "Clero, nobreza e povo",
                                "Operários e patrões",
                                "Cidadãos todos iguais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A economia europeia do Antigo Regime era, "
                                 "sobretudo:",
                            "options": [
                                "Agrária, com a terra nas mãos dos senhores",
                                "Industrial, com fábricas",
                                "Baseada em bancos e bolsas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada reino ou império africano à sua "
                                 "região.",
                            "pairs": [
                                ["Monomotapa", "Vale do Zambeze"],
                                ["Mali e Songai", "África Ocidental"],
                                ["Congo", "África Central"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Entre os séculos XV e XVII, a África "
                                 "comerciava com o exterior sobretudo:",
                            "options": [
                                "Ouro, marfim e escravos",
                                "Automóveis e máquinas",
                                "Petróleo e gás",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes da chegada dos europeus, o comércio "
                                 "da costa de Moçambique fazia-se com:",
                            "options": [
                                "Os árabes e os suaílis do Índico",
                                "Os ingleses",
                                "Os americanos",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A expansão europeia e o comércio colonial",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um dos objectivos da expansão europeia do "
                                 "século XV foi:",
                            "options": [
                                "Chegar às especiarias e ao ouro por mar",
                                "Fugir da peste",
                                "Estudar as estrelas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Em que ano Vasco da Gama chegou à costa de "
                                 "Moçambique, a caminho da Índia?",
                            "a": "1498",
                        },
                        {
                            "t": "choice",
                            "q": "Os portugueses instalaram-se primeiro em "
                                 "Moçambique:",
                            "options": [
                                "Na costa: Sofala e a Ilha de Moçambique",
                                "No interior: em Lichinga",
                                "Nas montanhas: em Gorongosa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Trocas desiguais» quer dizer que:",
                            "options": [
                                "Os europeus davam pouco valor pelo muito "
                                "que levavam",
                                "As trocas eram justas para todos",
                                "Só os africanos ganhavam",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O tráfico de escravos levou milhões de "
                                 "africanos, à força, sobretudo para:",
                            "options": [
                                "As plantações da América e as ilhas do "
                                "Índico",
                                "As universidades europeias",
                                "A China",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma consequência da expansão europeia para "
                                 "a África foi:",
                            "options": [
                                "A perda de gente e de riquezas, e reinos "
                                "enfraquecidos",
                                "O fim da escravatura",
                                "A independência imediata",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Renascimento, Humanismo e Reforma",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O Renascimento foi um movimento cultural "
                                 "que nasceu:",
                            "options": [
                                "Em Itália, nos séculos XIV a XVI",
                                "Em Moçambique, no século XX",
                                "Na Rússia, no século XIX",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O Humanismo pôs no centro das "
                                 "preocupações:",
                            "options": ["O ser humano", "Só Deus", "O rei"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada nome ao que fez.",
                            "pairs": [
                                ["Gutenberg", "A imprensa"],
                                ["Copérnico", "A Terra gira à volta do Sol"],
                                ["Leonardo da Vinci", "Pintura e invenções"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A Reforma Protestante começou em 1517 "
                                 "com:",
                            "options": ["Martinho Lutero", "Calvino", "O Papa"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada corrente protestante ao seu "
                                 "país de origem.",
                            "pairs": [
                                ["Luteranismo", "Alemanha"],
                                ["Calvinismo", "Suíça"],
                                ["Anglicanismo", "Inglaterra"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A resposta da Igreja Católica à Reforma "
                                 "chamou-se:",
                            "options": [
                                "Contra-Reforma",
                                "Renascimento",
                                "Mercantilismo",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Mercantilismo e Absolutismo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Para o mercantilismo, a riqueza de um país "
                                 "media-se:",
                            "options": [
                                "Pelo ouro e prata que acumulava",
                                "Pelo número de escolas",
                                "Pela extensão das florestas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No mercantilismo, as colónias serviam "
                                 "para:",
                            "options": [
                                "Fornecer matérias-primas e comprar os "
                                "produtos da metrópole",
                                "Governar a metrópole",
                                "Nada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No absolutismo, o poder estava:",
                            "options": [
                                "Todo nas mãos do rei",
                                "Dividido por um parlamento eleito",
                                "Nas mãos do povo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os reis absolutos diziam que o seu poder "
                                 "vinha:",
                            "options": ["De Deus", "Das eleições", "Dos operários"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«O Estado sou eu» é a frase atribuída a:",
                            "options": [
                                "Luís XIV, rei de França",
                                "Lutero",
                                "Vasco da Gama",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n5",
                    "titulo": "As revoluções burguesas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Revolução Inglesa do século XVII acabou "
                                 "por:",
                            "options": [
                                "Limitar o poder do rei e reforçar o "
                                "Parlamento",
                                "Dar ao rei todo o poder",
                                "Abolir o Parlamento para sempre",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As treze colónias inglesas da América do "
                                 "Norte revoltaram-se, entre outras razões, "
                                 "porque:",
                            "options": [
                                "Pagavam impostos sem ter representantes",
                                "Queriam mais reis",
                                "Não tinham terra",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Em que ano foi aprovada a Constituição dos "
                                 "Estados Unidos da América?",
                            "a": "1787",
                        },
                        {
                            "t": "input",
                            "q": "Em que ano começou a Revolução Francesa, "
                                 "com a tomada da Bastilha?",
                            "a": "1789",
                        },
                        {
                            "t": "choice",
                            "q": "Uma causa da Revolução Francesa foi:",
                            "options": [
                                "Os privilégios do clero e da nobreza e a "
                                "fome do povo",
                                "A falta de reis",
                                "A descoberta da América",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O lema da Revolução Francesa era:",
                            "options": [
                                "Liberdade, igualdade, fraternidade",
                                "Ordem e progresso",
                                "Deus, pátria e rei",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade II: Africa e Mocambique na epoca das revolucoes
        # ================================================================
        {
            "id": "u2",
            "titulo": "África e Moçambique na época das revoluções",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O mapa de África e a presença europeia",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "No fim do século XVIII, a presença "
                                 "portuguesa em Moçambique limitava-se, "
                                 "sobretudo:",
                            "options": [
                                "À costa e ao vale do Zambeze",
                                "A todo o território",
                                "Ao Niassa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os prazos da Zambézia eram:",
                            "options": [
                                "Grandes terras concedidas pela Coroa a "
                                "colonos, no vale do Zambeze",
                                "Datas de exames",
                                "Barcos de pesca",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No início do século XIX, a economia de "
                                 "Moçambique assentava sobretudo:",
                            "options": [
                                "No comércio de marfim e de escravos",
                                "Na indústria automóvel",
                                "No turismo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No início do século XIX, a maior parte da "
                                 "África:",
                            "options": [
                                "Era governada por reinos e estados "
                                "africanos",
                                "Já estava toda ocupada pelos europeus",
                                "Estava vazia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Revolução Industrial na Europa fez "
                                 "aumentar em África a procura de:",
                            "options": [
                                "Matérias-primas e mercados",
                                "Escolas",
                                "Reis",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade III: A Revolucao Industrial e o movimento operario
        # ================================================================
        {
            "id": "u3",
            "titulo": "A Revolução Industrial e o movimento operário",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A Revolução Industrial",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Revolução Industrial começou em "
                                 "Inglaterra porque lá havia:",
                            "options": [
                                "Carvão, ferro, capitais e mercados "
                                "coloniais",
                                "Muitas montanhas",
                                "Pouca gente",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada invenção ao que mudou.",
                            "pairs": [
                                ["Máquina a vapor", "Energia para as fábricas"],
                                ["Locomotiva", "Transporte por caminho-de-ferro"],
                                ["Tear mecânico", "Tecidos em grande quantidade"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A fonte de energia da primeira fase da "
                                 "Revolução Industrial foi:",
                            "options": ["O carvão", "O petróleo", "O sol"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na segunda fase da Revolução Industrial "
                                 "entraram:",
                            "options": [
                                "A electricidade, o petróleo e o aço",
                                "A enxada e o arado",
                                "O carvão pela primeira vez",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "James Watt aperfeiçoou a máquina a vapor "
                                 "no século dezoito. Escreve esse século em "
                                 "algarismos.",
                            "a": "18",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Consequências da Revolução Industrial",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Com a Revolução Industrial, a produção "
                                 "passou:",
                            "options": [
                                "Das oficinas artesanais para as fábricas",
                                "Das fábricas para as oficinas",
                                "Do campo para o mar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As duas classes sociais que a "
                                 "industrialização fez crescer foram:",
                            "options": [
                                "A burguesia e o proletariado",
                                "O clero e a nobreza",
                                "Os reis e os escravos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma consequência social da Revolução "
                                 "Industrial foi:",
                            "options": [
                                "O crescimento rápido das cidades",
                                "O regresso ao campo",
                                "O fim das cidades",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma consequência ambiental das fábricas "
                                 "foi:",
                            "options": [
                                "A poluição do ar e dos rios",
                                "O ar mais limpo",
                                "Mais florestas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O movimento operário",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Nas primeiras fábricas, os operários "
                                 "trabalhavam:",
                            "options": [
                                "Catorze horas ou mais, por salários baixos",
                                "Seis horas, com férias",
                                "Só quando queriam",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As mulheres e as crianças eram "
                                 "contratadas nas fábricas porque:",
                            "options": [
                                "Recebiam ainda menos do que os homens",
                                "Trabalhavam menos horas",
                                "Eram as donas das fábricas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um sindicato é:",
                            "options": [
                                "Uma organização de trabalhadores para "
                                "defender os seus direitos",
                                "Uma fábrica",
                                "Um partido do rei",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os primeiros sindicatos, os trade-unions, "
                                 "nasceram:",
                            "options": ["Em Inglaterra", "Em Moçambique", "No Brasil"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os partidos operários europeus lutavam "
                                 "por:",
                            "options": [
                                "Melhores salários, menos horas e direito "
                                "de voto",
                                "Mais horas de trabalho",
                                "O regresso do absolutismo",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade IV: Do capitalismo industrial ao imperialismo
        # ================================================================
        {
            "id": "u4",
            "titulo": "Do capitalismo industrial ao imperialismo",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Do capitalismo de concorrência aos monopólios",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um monopólio existe quando:",
                            "options": [
                                "Uma empresa, ou poucas, domina todo um "
                                "mercado",
                                "Há muitas empresas pequenas a competir",
                                "O Estado proíbe o comércio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada forma de concentração ao seu "
                                 "exemplo.",
                            "pairs": [
                                ["Horizontal", "Várias fábricas do mesmo produto juntam-se"],
                                ["Vertical", "A mina, a fundição e a fábrica no mesmo dono"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Na passagem ao capitalismo monopolista, os "
                                 "bancos:",
                            "options": [
                                "Ganharam poder sobre a indústria",
                                "Desapareceram",
                                "Passaram a ser do Estado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O imperialismo é a fase em que os países "
                                 "industrializados:",
                            "options": [
                                "Disputam colónias por matérias-primas, "
                                "mercados e prestígio",
                                "Fecham as fronteiras",
                                "Devolvem as colónias",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A partilha de África e Moçambique",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Conferência de Berlim, de 1884 a 1885, "
                                 "serviu para:",
                            "options": [
                                "As potências europeias repartirem a África "
                                "entre si",
                                "Dar a independência à África",
                                "Acabar com o comércio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Pelo princípio da ocupação efectiva, uma "
                                 "potência só tinha direito a um "
                                 "território se:",
                            "options": [
                                "O ocupasse e administrasse de facto",
                                "O desenhasse num mapa",
                                "O visitasse uma vez",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada potência às suas colónias em "
                                 "África.",
                            "pairs": [
                                ["Portugal", "Moçambique e Angola"],
                                ["Inglaterra", "Nigéria e África do Sul"],
                                ["França", "Argélia e Senegal"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O Ultimato inglês de 1890 obrigou Portugal "
                                 "a:",
                            "options": [
                                "Desistir das terras entre Angola e "
                                "Moçambique",
                                "Deixar Moçambique",
                                "Comprar a África do Sul",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Companhia de Moçambique e a Companhia do "
                                 "Niassa eram:",
                            "options": [
                                "Companhias majestáticas que exploravam e "
                                "administravam regiões inteiras",
                                "Equipas de futebol",
                                "Escolas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A resistência dos povos africanos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Os zulus, na África do Sul, resistiram:",
                            "options": [
                                "Aos ingleses, e venceram-nos em "
                                "Isandlwana, em 1879",
                                "Aos portugueses, no Niassa",
                                "Aos franceses, no Senegal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na Namíbia, os hereros e os namas "
                                 "revoltaram-se contra:",
                            "options": ["Os alemães", "Os portugueses", "Os belgas"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ngungunhane, imperador de Gaza, foi preso "
                                 "pelos portugueses em:",
                            "options": ["Chaimite, em 1895", "Lichinga, em 1975", "Berlim, em 1884"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Em que ano os portugueses prenderam "
                                 "Ngungunhane em Chaimite?",
                            "a": "1895",
                        },
                        {
                            "t": "choice",
                            "q": "A revolta do Barué, em 1917, foi:",
                            "options": [
                                "Uma grande resistência armada contra a "
                                "ocupação portuguesa no centro de Moçambique",
                                "Uma festa tradicional",
                                "Uma eleição",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A resistência dos povos africanos mostra "
                                 "que a ocupação colonial:",
                            "options": [
                                "Foi imposta pela força e contra a vontade "
                                "dos povos",
                                "Foi aceite sem luta",
                                "Nunca aconteceu",
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
            print(f"       {n['id']}  {n['titulo']:<48}"
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
