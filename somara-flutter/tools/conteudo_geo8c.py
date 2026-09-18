# -*- coding: utf-8 -*-
"""O curso de Geografia da 8a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Geografia -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, pp. 23-35
     ("Programa da 8a classe"). Guardado em Documents\\planos da 5a classe\\
     Livros\\Programas INDE 1o Ciclo\\geografia.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

A 7a foi a Geografia fisica; a 8a e a Geografia humana
-------------------------------------------------------
O programa chama-lhe "Geografia Humana ou Economica" e organiza-a em
QUATRO unidades, muito desiguais: a terceira, as actividades economicas,
ocupa dois trimestres e meio e vale mais de metade da classe.

    1o trimestre   I    Introducao ao estudo da Geografia Humana
                   II   Populacao          natalidade, mortalidade,
                                           migracoes, piramides etarias,
                                           distribuicao, problemas
    2o trimestre   III  Actividades        agricultura, pecuaria,
                        economicas         industria, comercio
    3o trimestre   III  (continuacao)      turismo, transportes,
                                           desenvolvimento sustentavel
                   IV   Cidades            evolucao, urbanizacao,
                                           funcoes, problemas, planeamento

Quatro unidades, treze aulas -- seis delas na terceira, porque e o
programa que a faz assim.

Correr a partir de somara-flutter/:
    python tools/conteudo_geo8c.py            # so mostra
    python tools/conteudo_geo8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Geografia — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, pp. 23-35. As quatro "
    "unidades e os conteúdos são do programa; os exercícios foram escritos "
    "a partir deles, porque um programa de ensino não traz exercícios e não "
    "há livro do aluno da 8ª classe publicado."
)

CURSO = {
    "id": "geo-8c",
    "disciplina": "Geografia",
    "classe": "8ª classe",
    "tag": "GEO",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # Unidade I: Introducao ao estudo da Geografia Humana ou Economica
        # ================================================================
        {
            "id": "u1",
            "titulo": "A Geografia Humana",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O que estuda a Geografia Humana",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Geografia Humana ou Económica estuda:",
                            "options": [
                                "As pessoas e as suas actividades no espaço",
                                "Só o clima e o relevo",
                                "As estrelas e os planetas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes assuntos é de Geografia "
                                 "Humana?",
                            "options": [
                                "A distribuição da população pelo mundo",
                                "A formação das rochas",
                                "O ciclo da água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada ramo da Geografia ao que estuda.",
                            "pairs": [
                                ["Geografia Física", "Relevo, clima, rios"],
                                ["Geografia Humana", "População, cidades, economia"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Estudar a Geografia Humana serve para:",
                            "options": [
                                "Perceber como as pessoas usam e organizam o "
                                "espaço onde vivem",
                                "Decorar os nomes dos rios",
                                "Prever o tempo de amanhã",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade II: Populacao
        # ================================================================
        {
            "id": "u2",
            "titulo": "População",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Natalidade, mortalidade e migrações",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A taxa de natalidade indica:",
                            "options": [
                                "Quantos nascem por cada mil habitantes num "
                                "ano",
                                "Quantos morrem por cada mil habitantes",
                                "Quantas pessoas mudam de país",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Num ano, uma região teve 30 nascimentos e "
                                 "10 mortes por cada mil habitantes. Qual foi "
                                 "o crescimento natural, por mil?",
                            "a": "20",
                        },
                        {
                            "t": "choice",
                            "q": "Uma migração é:",
                            "options": [
                                "A mudança de residência de pessoas de um "
                                "lugar para outro",
                                "O aumento dos nascimentos",
                                "A construção de estradas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada palavra ao seu significado.",
                            "pairs": [
                                ["Emigrante", "Quem sai do seu país"],
                                ["Imigrante", "Quem chega a outro país"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Uma causa frequente das migrações do campo "
                                 "para a cidade é:",
                            "options": [
                                "A procura de emprego e de serviços",
                                "O gosto pelo barulho",
                                "A falta de rios na cidade",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O crescimento efectivo de uma população "
                                 "junta o crescimento natural com:",
                            "options": [
                                "O saldo migratório",
                                "A taxa de natalidade só",
                                "O número de cidades",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Evolução e estrutura da população",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A população mundial, nos últimos duzentos "
                                 "anos:",
                            "options": [
                                "Cresceu muito depressa",
                                "Ficou na mesma",
                                "Diminuiu para metade",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma pirâmide etária mostra:",
                            "options": [
                                "A população por idades e por sexo",
                                "A altura das montanhas",
                                "O número de escolas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma pirâmide etária de base larga e topo "
                                 "estreito indica uma população:",
                            "options": ["Jovem", "Envelhecida", "Sem crianças"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A estrutura sectorial da população "
                                 "divide-a por:",
                            "options": [
                                "Sectores de actividade: primário, "
                                "secundário e terciário",
                                "Cor dos olhos",
                                "Continentes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Equidade de género quer dizer:",
                            "options": [
                                "Igualdade de oportunidades para raparigas e "
                                "rapazes",
                                "Só os rapazes vão à escola",
                                "As raparigas ficam em casa",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Distribuição e problemas demográficos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Qual é um factor natural que atrai "
                                 "população?",
                            "options": [
                                "Solos férteis e água",
                                "Deserto sem água",
                                "Montanhas geladas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual é um factor humano da distribuição da "
                                 "população?",
                            "options": [
                                "A existência de emprego e de indústrias",
                                "O clima",
                                "O relevo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O continente mais populoso do mundo é:",
                            "options": ["A Ásia", "A Europa", "A Oceânia"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um problema demográfico dos países menos "
                                 "desenvolvidos é:",
                            "options": [
                                "O crescimento rápido da população sem "
                                "serviços que cheguem",
                                "Haver demasiadas escolas",
                                "A falta de crianças",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma população que cresce muito num lugar "
                                 "com poucos recursos:",
                            "options": [
                                "Pressiona o ambiente: desmata, polui, "
                                "esgota a água",
                                "Não tem efeito no ambiente",
                                "Faz chover mais",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade III: Actividades Economicas
        # ================================================================
        {
            "id": "u3",
            "titulo": "Actividades económicas",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Os sectores e a agricultura",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada actividade ao seu sector.",
                            "pairs": [
                                ["Agricultura e pesca", "Sector primário"],
                                ["Indústria", "Sector secundário"],
                                ["Comércio e transportes", "Sector terciário"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A agricultura itinerante é aquela em que:",
                            "options": [
                                "O agricultor muda de terreno quando o solo "
                                "se cansa",
                                "Se usam máquinas e adubos químicos",
                                "Só se cultiva para vender",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A agricultura de sequeiro depende:",
                            "options": [
                                "Da chuva, sem rega",
                                "De rega artificial",
                                "De estufas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas é uma característica da "
                                 "agricultura moderna?",
                            "options": [
                                "Máquinas, adubos e produção para o mercado",
                                "Enxada e produção só para a família",
                                "Mudar de machamba todos os anos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um problema ambiental causado pela "
                                 "agricultura é:",
                            "options": [
                                "O desgaste e a erosão dos solos",
                                "O aumento das florestas",
                                "A chuva ácida das fábricas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A pecuária",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A pecuária é:",
                            "options": [
                                "A criação de animais para carne, leite, "
                                "peles e trabalho",
                                "O cultivo de cereais",
                                "A pesca no mar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na criação extensiva, o gado:",
                            "options": [
                                "Pasta livremente em grandes áreas",
                                "Vive fechado e alimentado com rações",
                                "Não existe",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de gado ao seu nome.",
                            "pairs": [
                                ["Bois e vacas", "Gado bovino"],
                                ["Cabras", "Gado caprino"],
                                ["Porcos", "Gado suíno"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um problema ambiental da pecuária em "
                                 "excesso é:",
                            "options": [
                                "O pisoteio e o sobrepastoreio, que "
                                "degradam o solo",
                                "O aumento da água nos rios",
                                "O crescimento das florestas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A indústria e a Revolução Industrial",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A indústria transforma:",
                            "options": [
                                "Matérias-primas em produtos",
                                "Produtos em matérias-primas",
                                "Água em chuva",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Revolução Industrial começou:",
                            "options": [
                                "Em Inglaterra, no século XVIII",
                                "Em Moçambique, no século XX",
                                "Na China, no século V",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma consequência da Revolução Industrial "
                                 "foi:",
                            "options": [
                                "O crescimento das cidades e das fábricas",
                                "O fim do comércio",
                                "O regresso de toda a gente ao campo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um factor que atrai a localização de uma "
                                 "indústria é:",
                            "options": [
                                "Matérias-primas, energia e mão-de-obra por "
                                "perto",
                                "Estar longe de tudo",
                                "Não ter estradas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quais são regiões muito industrializadas do "
                                 "mundo?",
                            "options": [
                                "Europa, América do Norte e Ásia Oriental",
                                "Só a África",
                                "Só a Oceânia",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "O comércio",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O comércio é a actividade de:",
                            "options": [
                                "Comprar e vender produtos",
                                "Fabricar produtos",
                                "Cultivar a terra",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de comércio à sua "
                                 "descrição.",
                            "pairs": [
                                ["Comércio interno", "Dentro do mesmo país"],
                                ["Comércio externo", "Entre países"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A balança comercial compara:",
                            "options": [
                                "O valor das exportações com o das "
                                "importações",
                                "O peso dos produtos",
                                "O número de lojas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um país exportou 80 milhões e importou 50 "
                                 "milhões. Qual é o saldo da balança "
                                 "comercial, em milhões?",
                            "a": "30",
                        },
                        {
                            "t": "choice",
                            "q": "Os bancos e os seguros fazem parte do:",
                            "options": [
                                "Sistema financeiro",
                                "Sector primário",
                                "Relevo",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n5",
                    "titulo": "O turismo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O turismo é:",
                            "options": [
                                "A deslocação de pessoas para lazer, cultura "
                                "ou descanso fora de onde vivem",
                                "A mudança definitiva de país",
                                "O transporte de mercadorias",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de turismo ao seu exemplo.",
                            "pairs": [
                                ["Turismo ambiental", "Visitar o Lago Niassa"],
                                ["Turismo cultural", "Visitar a Ilha de Moçambique"],
                                ["Turismo religioso", "Uma peregrinação"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um factor que favorece o turismo numa "
                                 "região é:",
                            "options": [
                                "Paisagens, património e segurança",
                                "A falta de estradas",
                                "A poluição",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O turismo em excesso pode:",
                            "options": [
                                "Poluir e estragar o património",
                                "Aumentar as florestas",
                                "Baixar os preços para os habitantes",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n6",
                    "titulo": "Transportes, comunicações e sustentabilidade",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada meio de transporte à sua via.",
                            "pairs": [
                                ["Comboio", "Via férrea"],
                                ["Navio", "Via marítima"],
                                ["Avião", "Via aérea"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Uma vantagem do transporte marítimo é:",
                            "options": [
                                "Levar muita carga a baixo custo",
                                "Ser o mais rápido",
                                "Chegar a todas as aldeias",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O telemóvel e a internet são:",
                            "options": [
                                "Meios de comunicação",
                                "Meios de transporte",
                                "Vias de comunicação",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na via pública, um peão deve:",
                            "options": [
                                "Atravessar na passadeira e olhar para os "
                                "dois lados",
                                "Correr pela estrada",
                                "Atravessar a falar ao telemóvel",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Desenvolvimento sustentável é:",
                            "options": [
                                "Usar os recursos sem os esgotar para quem "
                                "vem depois",
                                "Gastar tudo agora",
                                "Não usar recurso nenhum",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade IV: Cidades
        # ================================================================
        {
            "id": "u4",
            "titulo": "Cidades",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "As cidades e a urbanização",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Depois da Revolução Industrial, as "
                                 "cidades:",
                            "options": [
                                "Cresceram muito, com a chegada de "
                                "trabalhadores para as fábricas",
                                "Desapareceram",
                                "Ficaram do mesmo tamanho",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A taxa de urbanização indica:",
                            "options": [
                                "A percentagem da população que vive nas "
                                "cidades",
                                "O número de estradas",
                                "A altura dos prédios",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Num país com 10 milhões de habitantes, 4 "
                                 "milhões vivem em cidades. Qual é a taxa de "
                                 "urbanização, em percentagem?",
                            "a": "40",
                        },
                        {
                            "t": "choice",
                            "q": "O campo e a cidade:",
                            "options": [
                                "Dependem um do outro: o campo dá alimentos, "
                                "a cidade dá serviços e produtos",
                                "Não têm nada a ver um com o outro",
                                "São a mesma coisa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada cidade à sua função principal.",
                            "pairs": [
                                ["Maputo", "Capital, administrativa"],
                                ["Beira", "Porto e comércio"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Problemas das cidades e planeamento",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um problema comum nas grandes cidades é:",
                            "options": [
                                "Bairros sem água, luz e saneamento",
                                "Haver campos a mais",
                                "A falta de pessoas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O planeamento urbano serve para:",
                            "options": [
                                "Organizar a cidade: ruas, bairros, água, "
                                "escolas, espaços verdes",
                                "Aumentar o trânsito",
                                "Fechar as escolas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O consumo de álcool, tabaco e outras "
                                 "drogas nas cidades:",
                            "options": [
                                "É um problema de saúde que se previne com "
                                "informação e apoio",
                                "Não tem consequências",
                                "Faz bem ao estudo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Viver numa cultura de paz e de democracia "
                                 "é:",
                            "options": [
                                "Resolver os conflitos pelo diálogo e "
                                "respeitar os direitos de todos",
                                "Obedecer sem discutir",
                                "Resolver tudo à força",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma cidade sustentável:",
                            "options": [
                                "Recolhe o lixo, planta árvores e poupa "
                                "água e energia",
                                "Deita o lixo nos rios",
                                "Corta todas as árvores",
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
