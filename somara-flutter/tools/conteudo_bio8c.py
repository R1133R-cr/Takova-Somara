# -*- coding: utf-8 -*-
"""O curso de Biologia da 8a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Biologia -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, pp. 30-43.
     Guardado em Documents\\planos da 5a classe\\Livros\\Programas INDE 1o
     Ciclo\\biologia.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As seis unidades tematicas, tal como o INDE as ordena
-----------------------------------------------------
    1  Seres vivos e ambiente          celula e organelos; fotossintese,
                                       respiracao e transpiracao
    2  Recursos naturais               os de Mocambique, e a conservacao
    3  Sistemas do corpo humano        circulatorio e grupos sanguineos;
                                       excrecao e sistema urinario;
                                       endocrino
    4  Alimentacao, nutricao e saude   roda dos alimentos, vitaminas e
                                       minerais; doencas da ma
                                       alimentacao; parasitoses
    5  Reproducao nos seres vivos      assexuada e sexuada; a flor, a
                                       polinizacao, a semente
    6  Auto-descobrimento              adolescencia; ITS; HIV

Seis unidades, treze aulas.

Correr a partir de somara-flutter/:
    python tools/conteudo_bio8c.py            # so mostra
    python tools/conteudo_bio8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Biologia — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, pp. 30-43. As seis "
    "unidades e os conteúdos são do programa; os exercícios foram escritos "
    "a partir deles, porque um programa de ensino não traz exercícios e não "
    "há livro do aluno da 8ª classe publicado."
)

CURSO = {
    "id": "bio-8c",
    "disciplina": "Biologia",
    "classe": "8ª classe",
    "tag": "BIO",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # 1  Seres vivos e ambiente
        # ================================================================
        {
            "id": "u1",
            "titulo": "Seres vivos e ambiente",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A célula e os seus organelos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A substância mais abundante na célula é:",
                            "options": ["A água", "O ferro", "O açúcar"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada organelo à sua função.",
                            "pairs": [
                                ["Núcleo", "Guarda o material genético"],
                                ["Mitocôndria", "Produz energia"],
                                ["Cloroplasto", "Faz a fotossíntese"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A parede celular existe:",
                            "options": [
                                "Só nas células das plantas",
                                "Só nas células dos animais",
                                "Em todas as células",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A membrana celular serve para:",
                            "options": [
                                "Controlar o que entra e sai da célula",
                                "Fazer a fotossíntese",
                                "Guardar os genes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O vacúolo, grande nas células vegetais, "
                                 "serve para:",
                            "options": [
                                "Armazenar água e substâncias",
                                "Produzir energia",
                                "Dividir a célula",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Fotossíntese, respiração e transpiração",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Na fotossíntese, a planta usa água, "
                                 "dióxido de carbono e luz para produzir:",
                            "options": [
                                "Glicose e oxigénio",
                                "Sal e ferro",
                                "Só água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A fotossíntese acontece:",
                            "options": [
                                "Nos cloroplastos, com luz",
                                "Nas raízes, à noite",
                                "Nas mitocôndrias",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na respiração aeróbica, a célula gasta "
                                 "glicose e oxigénio e liberta:",
                            "options": [
                                "Energia, dióxido de carbono e água",
                                "Luz e clorofila",
                                "Só oxigénio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa experiência, uma vela acesa dentro "
                                 "de um frasco fechado apaga-se porque:",
                            "options": [
                                "Gastou o oxigénio que havia",
                                "Faltou dióxido de carbono",
                                "O vidro é frio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A transpiração das plantas é a perda de "
                                 "água em vapor, sobretudo:",
                            "options": [
                                "Pelas folhas, através dos estomas",
                                "Pelas raízes",
                                "Pelas sementes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A fotossíntese é importante para todos os "
                                 "seres vivos porque:",
                            "options": [
                                "Produz o alimento e o oxigénio de que "
                                "vivemos",
                                "Aquece o planeta",
                                "Faz chover",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 2  Recursos naturais
        # ================================================================
        {
            "id": "u2",
            "titulo": "Recursos naturais",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Os recursos naturais de Moçambique",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada recurso ao seu tipo.",
                            "pairs": [
                                ["Floresta e água", "Renovável"],
                                ["Carvão e gás", "Não renovável"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um recurso não renovável é aquele que:",
                            "options": [
                                "Não se refaz depois de gasto",
                                "Volta a crescer todos os anos",
                                "Não tem valor",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um recurso natural "
                                 "importante de Moçambique?",
                            "options": [
                                "O carvão de Tete e o gás de Cabo Delgado",
                                "A neve das montanhas",
                                "O petróleo do deserto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma forma de conservar as florestas é:",
                            "options": [
                                "Cortar só o necessário e plantar árvores "
                                "novas",
                                "Fazer queimadas todos os anos",
                                "Cortar tudo de uma vez",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Conservar os recursos naturais é "
                                 "importante porque:",
                            "options": [
                                "Deles dependem a nossa vida e a das "
                                "gerações seguintes",
                                "Não há mais nada para fazer",
                                "Os recursos são infinitos",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 3  Sistemas do corpo humano
        # ================================================================
        {
            "id": "u3",
            "titulo": "Sistemas do corpo humano",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O sangue e os grupos sanguíneos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Os grupos sanguíneos do sistema ABO são:",
                            "options": ["A, B, AB e O", "1, 2, 3 e 4", "X, Y e Z"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O grupo O é chamado dador universal "
                                 "porque:",
                            "options": [
                                "O seu sangue pode ser dado a todos os "
                                "grupos",
                                "Só pode receber do grupo AB",
                                "É o grupo mais raro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa transfusão, o sangue do dador tem "
                                 "de ser:",
                            "options": [
                                "Compatível com o do doente",
                                "Sempre do grupo A",
                                "De um familiar, obrigatoriamente",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Doar sangue é importante porque:",
                            "options": [
                                "Salva vidas em partos, acidentes e "
                                "operações",
                                "Faz emagrecer",
                                "Dá dinheiro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para cuidar do sistema circulatório "
                                 "deve-se:",
                            "options": [
                                "Fazer exercício, comer bem e não fumar",
                                "Comer muita gordura",
                                "Ficar sempre sentado",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A excreção e o sistema urinário",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada órgão ao que excreta.",
                            "pairs": [
                                ["Rins", "Urina"],
                                ["Pulmões", "Dióxido de carbono"],
                                ["Pele", "Suor"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A urina forma-se:",
                            "options": [
                                "Nos rins, ao filtrarem o sangue",
                                "Na bexiga",
                                "No estômago",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O caminho da urina é:",
                            "options": [
                                "Rins, ureteres, bexiga, uretra",
                                "Bexiga, rins, uretra, ureteres",
                                "Uretra, bexiga, rins",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um sinal de infecção urinária é:",
                            "options": [
                                "Dor ou ardor ao urinar",
                                "Tosse",
                                "Dor de dentes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para prevenir doenças do sistema urinário "
                                 "deve-se:",
                            "options": [
                                "Beber água e manter a higiene",
                                "Segurar a urina o mais possível",
                                "Comer muito sal",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O sistema endócrino",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As glândulas do sistema endócrino "
                                 "produzem:",
                            "options": ["Hormonas", "Urina", "Sangue"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada glândula à sua hormona ou "
                                 "função.",
                            "pairs": [
                                ["Pâncreas", "Insulina, o açúcar no sangue"],
                                ["Tiróide", "Regula o metabolismo"],
                                ["Supra-renais", "Adrenalina"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O bócio, o inchaço da tiróide, deve-se "
                                 "muitas vezes à falta de:",
                            "options": ["Iodo", "Açúcar", "Água"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O gigantismo e o nanismo são anomalias "
                                 "ligadas à hormona:",
                            "options": [
                                "Do crescimento",
                                "Da digestão",
                                "Do sono",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As glândulas sexuais produzem as hormonas "
                                 "que:",
                            "options": [
                                "Fazem aparecer as mudanças da puberdade",
                                "Fazem crescer as unhas",
                                "Controlam a urina",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 4  Alimentacao, nutricao e saude
        # ================================================================
        {
            "id": "u4",
            "titulo": "Alimentação, nutrição e saúde",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Alimentação equilibrada e nutrientes",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma alimentação equilibrada é a que:",
                            "options": [
                                "Tem de todos os grupos de alimentos, na "
                                "medida certa",
                                "Tem só carne",
                                "Tem só fruta",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada nutriente à sua função "
                                 "principal.",
                            "pairs": [
                                ["Proteínas", "Construir o corpo"],
                                ["Hidratos de carbono", "Dar energia"],
                                ["Lípidos", "Reserva de energia"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada vitamina ao que faz.",
                            "pairs": [
                                ["Vitamina A", "Ajuda a visão"],
                                ["Vitamina D", "Fortalece os ossos"],
                                ["Vitamina C", "Protege das infecções"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O ferro é um mineral importante porque:",
                            "options": [
                                "Entra no sangue e transporta o oxigénio",
                                "Faz crescer o cabelo",
                                "Dá sabor aos alimentos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O cálcio encontra-se sobretudo:",
                            "options": [
                                "No leite, no peixe e nas folhas verdes",
                                "No açúcar",
                                "No óleo",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Doenças da má alimentação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O kwashiorkor é causado pela falta de:",
                            "options": ["Proteínas", "Água", "Sal"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O marasmo é a magreza extrema causada "
                                 "por:",
                            "options": [
                                "Falta geral de alimento",
                                "Excesso de doces",
                                "Falta de sono",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada doença ao que falta.",
                            "pairs": [
                                ["Cegueira nocturna", "Vitamina A"],
                                ["Raquitismo", "Vitamina D e cálcio"],
                                ["Escorbuto", "Vitamina C"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A anemia deve-se muitas vezes à falta de:",
                            "options": ["Ferro", "Açúcar", "Gordura"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A obesidade resulta de:",
                            "options": [
                                "Comer mais do que o corpo gasta, sem "
                                "exercício",
                                "Beber muita água",
                                "Comer fruta",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Infecções e parasitoses intestinais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A febre tifóide apanha-se sobretudo:",
                            "options": [
                                "Por água e alimentos contaminados com "
                                "fezes",
                                "Pelo ar",
                                "Por picada de mosquito",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada parasitose ao seu parasita.",
                            "pairs": [
                                ["Ascaridíase", "Lombriga"],
                                ["Teníase", "Ténia"],
                                ["Oxiuríase", "Oxiúros"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A ténia apanha-se ao comer:",
                            "options": [
                                "Carne mal cozida, sobretudo de porco",
                                "Fruta lavada",
                                "Arroz cozido",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A melhor prevenção das parasitoses "
                                 "intestinais é:",
                            "options": [
                                "Lavar as mãos, ferver a água e usar "
                                "latrina",
                                "Comer depressa",
                                "Beber água do rio",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 5  Reproducao nos seres vivos
        # ================================================================
        {
            "id": "u5",
            "titulo": "Reprodução nos seres vivos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Reprodução assexuada e multiplicação "
                              "vegetativa",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Na reprodução assexuada:",
                            "options": [
                                "Um só progenitor dá origem a seres iguais "
                                "a ele",
                                "São precisos dois progenitores",
                                "Nascem sempre sementes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Plantar um pedaço de caule de mandioca "
                                 "para dar uma planta nova é:",
                            "options": ["Estacaria", "Enxertia", "Polinização"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada técnica ao que se faz.",
                            "pairs": [
                                ["Mergulhia", "Enterra-se um ramo ainda preso à planta"],
                                ["Enxertia", "Junta-se um ramo de uma planta a outra"],
                                ["Alporquia", "Fazem-se nascer raízes num ramo no ar"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A multiplicação vegetativa é útil ao "
                                 "camponês porque:",
                            "options": [
                                "Dá plantas iguais à mãe, mais depressa",
                                "Não precisa de água",
                                "Só funciona com flores",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A flor, a polinização e a semente",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada parte da flor ao seu papel.",
                            "pairs": [
                                ["Estames", "Parte masculina, com o pólen"],
                                ["Pistilo", "Parte feminina, com os óvulos"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A polinização é:",
                            "options": [
                                "A passagem do pólen para a parte feminina "
                                "da flor",
                                "O nascimento da raiz",
                                "A queda das folhas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quais são agentes polinizadores?",
                            "options": [
                                "O vento, os insectos e as aves",
                                "As pedras",
                                "O sal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Depois da fecundação, o ovário da flor "
                                 "transforma-se:",
                            "options": ["No fruto", "Na raiz", "Na folha"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma semente de coco viaja sobretudo:",
                            "options": [
                                "Pela água do mar",
                                "Pelo vento",
                                "Colada ao pêlo dos animais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Dentro de uma semente de feijão há:",
                            "options": [
                                "Um embrião e reservas de alimento",
                                "Uma flor pequena",
                                "Só água",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 6  Auto-descobrimento
        # ================================================================
        {
            "id": "u6",
            "titulo": "Auto-descobrimento",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Relacionamentos na adolescência",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A melhor forma de resolver um conflito "
                                 "com os pais ou com um amigo é:",
                            "options": [
                                "Conversar com calma e ouvir o outro",
                                "Gritar mais alto",
                                "Deixar de falar para sempre",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Igualdade de género na família quer "
                                 "dizer:",
                            "options": [
                                "Rapazes e raparigas partilham tarefas e "
                                "têm os mesmos direitos",
                                "As raparigas fazem todo o trabalho de casa",
                                "Só os rapazes estudam",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma união prematura é um casamento:",
                            "options": [
                                "Antes dos dezoito anos, e a lei "
                                "moçambicana proíbe-o",
                                "Entre pessoas de cidades diferentes",
                                "Depois dos trinta anos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma consequência das uniões prematuras "
                                 "para uma rapariga é:",
                            "options": [
                                "Deixar a escola e ter uma gravidez de "
                                "risco",
                                "Acabar os estudos mais depressa",
                                "Nenhuma",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "As infecções de transmissão sexual e o HIV",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As infecções de transmissão sexual "
                                 "apanham-se sobretudo:",
                            "options": [
                                "Em relações sexuais sem protecção",
                                "A apertar a mão",
                                "A partilhar a comida",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas é uma infecção de "
                                 "transmissão sexual?",
                            "options": ["A sífilis", "A malária", "A gripe"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um sinal frequente de infecção de "
                                 "transmissão sexual é:",
                            "options": [
                                "Corrimento ou feridas nos órgãos genitais",
                                "Dor de cabeça só",
                                "Comichão nos olhos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As duas formas seguras de prevenir as "
                                 "infecções de transmissão sexual são:",
                            "options": [
                                "A abstinência e o preservativo",
                                "Lavar as mãos e beber água",
                                "Dormir cedo e comer fruta",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O HIV ataca:",
                            "options": [
                                "As defesas do corpo, deixando entrar "
                                "outras doenças",
                                "Só os ossos",
                                "Só os olhos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma infecção oportunista comum em quem "
                                 "tem SIDA é:",
                            "options": ["A tuberculose", "A cárie", "O soluço"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quem vive com HIV e toma o tratamento "
                                 "anti-retroviral:",
                            "options": [
                                "Pode viver muitos anos com saúde",
                                "Não pode ir à escola",
                                "Não precisa de mais nada",
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
