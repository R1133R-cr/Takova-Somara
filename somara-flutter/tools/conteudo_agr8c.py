# -*- coding: utf-8 -*-
"""O curso de Agropecuaria da 8a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Agropecuaria -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024,
     8a classe, pp. 37-49. Guardado em Documents\\planos da 5a classe\\
     Livros\\Programas INDE 1o Ciclo\\agropecuaria.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As seis unidades da 8a, pela ordem do programa
----------------------------------------------
    1  Culturas alimentares     as horticolas: alface, alho, cebola,
                                cenoura, pepino, pimento, tomate, couve,
                                repolho; alfobre; praticas culturais
    2  Leguminosas de grao      nhemba, vulgar, boer, feijao-verde,
                                amendoim
    3  Raizes e tuberculos      mandioca, batata-reno, batata-doce, inhame
    4  Cultivo dos cereais      milho, arroz, trigo, mapira, mexoeira
    5  Criacao de coelhos       instalacoes, alimentacao, doencas,
                                reproducao
    6  Criacao de suinos        instalacoes, alimentacao, doencas

Seis unidades, onze aulas. As quatro unidades de culturas seguem todas
o mesmo esquema do programa -- origem e distribuicao, importancia,
descricao botanica, variedades, exigencias de clima e solo, propagacao,
epoca, praticas culturais, colheita -- e as perguntas seguem-no tambem.

Correr a partir de somara-flutter/:
    python tools/conteudo_agr8c.py            # so mostra
    python tools/conteudo_agr8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Agropecuária — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, 8ª classe, pp. 37-49. "
    "As seis unidades temáticas e os conteúdos são do programa; os "
    "exercícios foram escritos a partir deles, porque um programa de ensino "
    "não traz exercícios e não há livro do aluno da 8ª classe publicado."
)

CURSO = {
    "id": "agr-8c",
    "disciplina": "Agropecuária",
    "classe": "8ª classe",
    "tag": "AGR",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # 1  Culturas alimentares (horticolas)
        # ================================================================
        {
            "id": "u1",
            "titulo": "Culturas alimentares: as hortícolas",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "As hortícolas de Moçambique",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Alface, cebola, cenoura, tomate e couve "
                                 "são:",
                            "options": ["Hortícolas", "Cereais", "Leguminosas"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada hortícola à parte que se come.",
                            "pairs": [
                                ["Cenoura", "A raiz"],
                                ["Alface", "As folhas"],
                                ["Tomate", "O fruto"],
                                ["Cebola", "O bolbo"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "As hortícolas são importantes para a "
                                 "família porque:",
                            "options": [
                                "Dão vitaminas à mesa e renda no mercado",
                                "Só servem para vender",
                                "Não precisam de água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A maior parte das hortícolas semeia-se "
                                 "primeiro:",
                            "options": [
                                "No alfobre, e depois transplanta-se para "
                                "o campo",
                                "Directamente no campo, sempre",
                                "Dentro de casa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A época mais fresca e seca, com rega, "
                                 "é a melhor para:",
                            "options": [
                                "A alface, a couve e a cenoura",
                                "O arroz",
                                "O coco",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Do alfobre à colheita",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada prática cultural ao que ela é.",
                            "pairs": [
                                ["Sacha", "Tirar as ervas daninhas"],
                                ["Desbaste", "Arrancar plantas a mais para as outras crescerem"],
                                ["Tutoragem", "Pôr uma estaca a segurar a planta"],
                                ["Adubação", "Dar alimento ao solo"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Um camponês transplanta tomateiros em "
                                 "linhas com 5 plantas cada. Quantas "
                                 "plantas tem em 12 linhas?",
                            "a": "60",
                        },
                        {
                            "t": "choice",
                            "q": "O compasso de sementeira é:",
                            "options": [
                                "A distância entre as plantas e entre as "
                                "linhas",
                                "O instrumento de desenhar círculos",
                                "A hora de semear",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O tomateiro precisa de tutor porque:",
                            "options": [
                                "O caule não aguenta o peso dos frutos",
                                "Cresce debaixo da terra",
                                "Não gosta de sol",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A couve e a alface colhem-se:",
                            "options": [
                                "De manhã cedo, antes do calor, para não "
                                "murcharem",
                                "Ao meio-dia",
                                "Só depois de secarem",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 2  Leguminosas de grao
        # ================================================================
        {
            "id": "u2",
            "titulo": "Leguminosas de grão",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Os feijões e o amendoim",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Feijão-nhemba, feijão-vulgar, feijão-bóer "
                                 "e amendoim são:",
                            "options": [
                                "Leguminosas de grão",
                                "Cereais",
                                "Raízes e tubérculos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As leguminosas são ricas em:",
                            "options": ["Proteínas", "Água", "Sal"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As leguminosas fazem bem ao solo "
                                 "porque:",
                            "options": [
                                "Fixam o azoto do ar nas raízes e "
                                "enriquecem a terra",
                                "Secam a terra",
                                "Atraem pragas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada leguminosa à sua "
                                 "característica.",
                            "pairs": [
                                ["Feijão-nhemba", "Aguenta bem a seca"],
                                ["Feijão-bóer", "Arbusto que dura mais de um ano"],
                                ["Amendoim", "A vagem cresce debaixo da terra"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Semear as leguminosas na época certa "
                                 "importa porque:",
                            "options": [
                                "Precisam de chuva para nascer e de tempo "
                                "seco para a colheita",
                                "Nascem em qualquer altura",
                                "Não gostam de chuva",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Semear, cuidar e colher",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "O feijão semeia-se com 2 grãos por cova. "
                                 "Quantos grãos vão em 40 covas?",
                            "a": "80",
                        },
                        {
                            "t": "choice",
                            "q": "Plantar milho com feijão-nhemba na "
                                 "mesma machamba chama-se:",
                            "options": ["Consociação", "Monocultura", "Estacaria"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O feijão colhe-se quando:",
                            "options": [
                                "As vagens estão secas e amarelas",
                                "As flores abrem",
                                "As folhas estão verdes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para guardar o feijão sem gorgulho "
                                 "deve-se:",
                            "options": [
                                "Secá-lo bem e fechá-lo em recipiente "
                                "limpo e seco",
                                "Guardá-lo húmido",
                                "Deixá-lo ao ar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O amendoim colhe-se:",
                            "options": [
                                "Arrancando a planta e secando as vagens",
                                "Apanhando os frutos da árvore",
                                "Cortando as folhas",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 3  Raizes e tuberculos
        # ================================================================
        {
            "id": "u3",
            "titulo": "Raízes e tubérculos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Mandioca, batata e inhame",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada cultura ao que se colhe dela.",
                            "pairs": [
                                ["Mandioca", "Raiz"],
                                ["Batata-reno", "Tubérculo"],
                                ["Batata-doce", "Raiz"],
                                ["Inhame", "Tubérculo"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A mandioca é importante em Moçambique "
                                 "porque:",
                            "options": [
                                "Aguenta a seca e os solos pobres, e dá "
                                "comida todo o ano",
                                "Precisa de muita água",
                                "Só cresce nas cidades",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A mandioca e a batata-doce propagam-se "
                                 "por:",
                            "options": [
                                "Estacas de caule ou de rama",
                                "Sementes",
                                "Enxertia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A batata-reno propaga-se por:",
                            "options": [
                                "Tubérculos com olhos, os rebentos",
                                "Folhas",
                                "Flores",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Estas culturas são sobretudo fonte de:",
                            "options": [
                                "Energia: hidratos de carbono",
                                "Proteínas",
                                "Gordura",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Plantar, amontoar e colher",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Amontoa é:",
                            "options": [
                                "Chegar terra ao pé da planta para os "
                                "tubérculos não ficarem à vista",
                                "Regar de manhã",
                                "Cortar as folhas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "As estacas de mandioca plantam-se a 1 "
                                 "metro umas das outras. Numa linha de 25 "
                                 "metros, quantas estacas cabem, contando "
                                 "as duas pontas?",
                            "a": "26",
                        },
                        {
                            "t": "choice",
                            "q": "A mandioca amarga tem de se:",
                            "options": [
                                "Descascar, demolhar ou secar bem antes "
                                "de comer",
                                "Comer crua",
                                "Comer com casca",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para a batata-doce durar, guarda-se:",
                            "options": [
                                "Em lugar fresco, seco e arejado",
                                "Ao sol",
                                "Dentro de água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A mandioca demora a colher:",
                            "options": [
                                "Cerca de um ano",
                                "Uma semana",
                                "Um mês",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 4  Cultivo dos cereais
        # ================================================================
        {
            "id": "u4",
            "titulo": "Cultivo dos cereais",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Milho, arroz, mapira e mexoeira",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Milho, arroz, trigo, mapira e mexoeira "
                                 "são:",
                            "options": ["Cereais", "Hortícolas", "Tubérculos"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada cereal ao lugar onde se dá "
                                 "melhor.",
                            "pairs": [
                                ["Arroz", "Baixas alagadas"],
                                ["Mapira e mexoeira", "Zonas secas"],
                                ["Milho", "Terras com chuva regular"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O cereal mais cultivado em Moçambique, "
                                 "de que se faz a xima, é:",
                            "options": ["O milho", "O trigo", "O arroz"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A mapira e a mexoeira são importantes "
                                 "porque:",
                            "options": [
                                "Dão colheita mesmo com pouca chuva",
                                "Precisam de água alagada",
                                "Só crescem no frio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Preparar o solo antes de semear serve "
                                 "para:",
                            "options": [
                                "Soltar a terra, tirar ervas e deixar a "
                                "raiz respirar",
                                "Endurecer a terra",
                                "Secar a terra",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Semear, cuidar e guardar o grão",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "O milho semeia-se em linhas afastadas "
                                 "80 centímetros. Quantas linhas cabem "
                                 "numa machamba com 16 metros de largura?",
                            "a": "20",
                        },
                        {
                            "t": "choice",
                            "q": "A amontoa no milho serve para:",
                            "options": [
                                "Segurar a planta e proteger as raízes",
                                "Cortar as folhas",
                                "Colher o grão",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada praga ou doença ao cereal que "
                                 "ataca.",
                            "pairs": [
                                ["Lagarta do funil", "Milho"],
                                ["Pássaros na espiga", "Mapira e mexoeira"],
                                ["Gorgulho no celeiro", "Grão guardado"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O milho colhe-se quando:",
                            "options": [
                                "A planta seca e o grão está duro",
                                "A planta ainda está verde",
                                "Aparecem as flores",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para guardar o grão sem perdas deve "
                                 "estar:",
                            "options": [
                                "Bem seco, num celeiro limpo e fechado",
                                "Húmido",
                                "Ao ar livre",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 5  Criacao de coelhos
        # ================================================================
        {
            "id": "u5",
            "titulo": "Criação de coelhos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Instalações e alimentação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Criar coelhos é bom para a família "
                                 "porque:",
                            "options": [
                                "Reproduzem-se depressa e dão carne com "
                                "pouco espaço",
                                "Comem carne",
                                "Vivem sem comer",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada forma de criação ao que ela é.",
                            "pairs": [
                                ["Familiar", "Poucos animais, para a casa e o mercado local"],
                                ["Industrial", "Muitos animais, para vender em grande"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada equipamento da coelheira ao "
                                 "que ele é.",
                            "pairs": [
                                ["Comedouro", "Onde se põe a comida"],
                                ["Bebedouro", "Onde se põe a água"],
                                ["Ninho", "Onde a fêmea tem as crias"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A coelheira deve ficar:",
                            "options": [
                                "Em terreno seco, à sombra e sem vento "
                                "forte",
                                "Num charco",
                                "Ao sol todo o dia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os coelhos comem:",
                            "options": [
                                "Pastos e forragens, e ração quando há",
                                "Carne",
                                "Só água",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Saúde e reprodução",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada doença dos coelhos ao seu "
                                 "sinal.",
                            "pairs": [
                                ["Coccidiose", "Diarreia e barriga inchada"],
                                ["Sarna", "Crostas nas orelhas e na pele"],
                                ["Coriza", "Espirros e nariz a pingar"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Para prevenir doenças, a coelheira:",
                            "options": [
                                "Limpa-se todos os dias e desinfecta-se",
                                "Nunca se limpa",
                                "Enche-se de água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "A gestação da coelha dura cerca de 31 "
                                 "dias. Se foi coberta a 1 de Março, em "
                                 "que dia de Abril pare, aproximadamente?",
                            "a": "1",
                        },
                        {
                            "t": "choice",
                            "q": "O cio é:",
                            "options": [
                                "O período em que a fêmea aceita o macho",
                                "Uma doença",
                                "O nome do ninho",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os coelhos recém-nascidos:",
                            "options": [
                                "Nascem sem pêlo e de olhos fechados, e "
                                "precisam do ninho quente",
                                "Nascem a correr",
                                "Comem capim no primeiro dia",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 6  Criacao de suinos
        # ================================================================
        {
            "id": "u6",
            "titulo": "Criação de suínos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Pocilga, alimentação e saúde",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Os suínos são:",
                            "options": ["Os porcos", "As cabras", "As galinhas"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A pocilga deve ter:",
                            "options": [
                                "Chão que se lave, sombra, comedouro e "
                                "bebedouro",
                                "Chão de lama e sem tecto",
                                "Só uma corda",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada alimento dos porcos à sua "
                                 "origem.",
                            "pairs": [
                                ["Restos da machamba", "Ramas, folhas, mandioca"],
                                ["Restos da cozinha", "Cascas e sobras"],
                                ["Ração industrial", "Comprada, já equilibrada"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada doença dos porcos ao que ela é.",
                            "pairs": [
                                ["Peste suína africana", "Vírus mortal, sem cura: mata a vara toda"],
                                ["Sarna", "Comichão e crostas na pele"],
                                ["Mal-rubro", "Manchas vermelhas na pele e febre"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Para evitar a peste suína africana:",
                            "options": [
                                "Não se metem porcos novos sem quarentena "
                                "e não se dão restos de carne de porco",
                                "Dão-se restos de carne crua",
                                "Deixam-se os porcos soltos na vila",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma porca pare 8 leitões numa ninhada e "
                                 "tem 2 ninhadas por ano. Quantos leitões "
                                 "dá num ano?",
                            "a": "16",
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
