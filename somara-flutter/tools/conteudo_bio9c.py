# -*- coding: utf-8 -*-
"""O curso de Biologia da 9a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Biologia -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, 9a classe,
     pp. 44-57. Guardado em Documents\\planos da 5a classe\\Livros\\
     Programas INDE 1o Ciclo\\biologia.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As cinco unidades tematicas, pela ordem do programa
---------------------------------------------------
    1  Seres vivos e ambiente      ecossistema; cadeias, teias e energia;
                                   a accao do Homem (desmatamento, caca,
                                   agua, residuos)
    2  Sistemas do corpo humano    esqueleto; musculos e articulacoes;
                                   sistema nervoso
    3  Reproducao nos seres vivos  reproducao no Homem; metodos
                                   anti-conceptivos; hormonas vegetais e
                                   tropismos
    4  Agricultura                 o solo; organismos, fertilidade e
                                   conservacao; culturas e adubos
    5  Auto-descobrimento          inclusao e diversidade; as doencas;
                                   sistema reprodutor e medicamentos

Cinco unidades, quinze aulas.

As siglas
---------
"SNC", "SNP", "DIU", "HPV" e "ITS" a voz leria como palavras. Ficam nas
opcoes; nos enunciados escreve-se "sistema nervoso central", "dispositivo
intra-uterino", "virus do papiloma humano", "infeccoes de transmissao
sexual". "HIV" soletra-se, como desde a 7a.

Correr a partir de somara-flutter/:
    python tools/conteudo_bio9c.py            # so mostra
    python tools/conteudo_bio9c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Biologia — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, 9ª classe, pp. 44-57. "
    "As cinco unidades temáticas e os conteúdos são do programa; os "
    "exercícios foram escritos a partir deles, porque um programa de ensino "
    "não traz exercícios e não há livro do aluno da 9ª classe publicado."
)

CURSO = {
    "id": "bio-9c",
    "disciplina": "Biologia",
    "classe": "9ª classe",
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
                    "titulo": "O ecossistema",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um ecossistema é:",
                            "options": [
                                "Os seres vivos de um lugar e o ambiente "
                                "em que vivem, a trocar matéria e energia",
                                "Só as plantas de um lugar",
                                "Só o clima",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada ecossistema ao seu tipo.",
                            "pairs": [
                                ["O lago Niassa", "Natural"],
                                ["Uma machamba", "Artificial"],
                                ["Um aquário", "Artificial"],
                                ["A floresta de miombo", "Natural"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada factor do ecossistema ao seu "
                                 "tipo.",
                            "pairs": [
                                ["Plantas, animais e micróbios", "Bióticos"],
                                ["Luz, água, temperatura e solo", "Abióticos"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Se a água de um lago seca, o factor que "
                                 "mudou é:",
                            "options": ["Abiótico", "Biótico", "Nenhum"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa machamba de milho, o homem que a "
                                 "sacha é:",
                            "options": [
                                "Um factor biótico que altera o ecossistema",
                                "Um factor abiótico",
                                "Parte do solo",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Cadeias, teias e energia",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Na cadeia capim, cabra, leão, liga cada "
                                 "ser ao seu nível trófico.",
                            "pairs": [
                                ["Capim", "Produtor"],
                                ["Cabra", "Consumidor primário"],
                                ["Leão", "Consumidor secundário"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Uma teia alimentar é:",
                            "options": [
                                "Várias cadeias alimentares cruzadas",
                                "Uma só cadeia",
                                "A teia de uma aranha",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A energia numa cadeia alimentar:",
                            "options": [
                                "Flui num só sentido e diminui de um nível "
                                "para o seguinte",
                                "Aumenta de nível para nível",
                                "Anda em círculo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "De onde vem a energia que entra na "
                                 "cadeia alimentar?",
                            "options": ["Do Sol, pela fotossíntese", "Do solo", "Dos animais"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "De cada nível trófico só passa cerca de "
                                 "10 por cento da energia ao seguinte. Se o "
                                 "capim tem 1000 unidades, quantas chegam "
                                 "à cabra?",
                            "a": "100",
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A acção do Homem",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada acção do Homem à sua "
                                 "consequência.",
                            "pairs": [
                                ["Desmatamento", "Erosão e perda de habitat"],
                                ["Caça furtiva", "Espécies em perigo de extinção"],
                                ["Lixo no rio", "Água poluída e doenças"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de água ao que ela é.",
                            "pairs": [
                                ["Potável", "Própria para beber"],
                                ["Poluída", "Com substâncias químicas ou lixo"],
                                ["Contaminada", "Com micróbios que causam doenças"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada resíduo sólido ao seu tipo.",
                            "pairs": [
                                ["Cascas e restos de comida", "Doméstico"],
                                ["Seringas e ligaduras usadas", "Hospitalar"],
                                ["Sobras de metal e químicos", "Das fábricas"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Os resíduos hospitalares tratam-se:",
                            "options": [
                                "Queimando-os em incineradoras, longe das "
                                "pessoas",
                                "Deitando-os no rio",
                                "Misturando-os com o lixo de casa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Separar em casa o papel, o plástico e o "
                                 "vidro serve para:",
                            "options": [
                                "Reciclar: fazer coisas novas com o que "
                                "se deitava fora",
                                "Ocupar mais espaço",
                                "Atrair moscas",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 2  Sistemas do corpo humano
        # ================================================================
        {
            "id": "u2",
            "titulo": "Sistemas do corpo humano",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O esqueleto",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O esqueleto serve para:",
                            "options": [
                                "Dar forma e suporte ao corpo, proteger os "
                                "órgãos e permitir o movimento",
                                "Só para andar",
                                "Digerir os alimentos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada osso à sua forma.",
                            "pairs": [
                                ["Fémur", "Longo"],
                                ["Ossos do pulso", "Curtos"],
                                ["Omoplata", "Plano"],
                                ["Vértebra", "Irregular"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada osso à parte do esqueleto onde "
                                 "está.",
                            "pairs": [
                                ["Crânio", "Cabeça"],
                                ["Costelas e coluna", "Tronco"],
                                ["Úmero", "Membro superior"],
                                ["Tíbia", "Membro inferior"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Os ossos são feitos de:",
                            "options": [
                                "Osteína, que dá flexibilidade, e sais de "
                                "cálcio, que dão dureza, mais água",
                                "Só de cálcio",
                                "Só de água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Quantos ossos tem o esqueleto de um "
                                 "adulto?",
                            "a": "206",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Músculos, articulações e saúde",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada tipo de músculo ao seu exemplo.",
                            "pairs": [
                                ["Estriado", "Os músculos dos braços, que se comandam"],
                                ["Liso", "Os do estômago e do intestino"],
                                ["Cardíaco", "O coração"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada articulação ao seu tipo.",
                            "pairs": [
                                ["Joelho e ombro", "Móvel"],
                                ["Entre as vértebras", "Semimóvel"],
                                ["Ossos do crânio", "Imóvel"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada lesão ao que ela é.",
                            "pairs": [
                                ["Entorse", "Torcer uma articulação, sem sair do lugar"],
                                ["Luxação", "O osso sai da articulação"],
                                ["Escoliose", "A coluna curvada para o lado"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Cifose e lordose são:",
                            "options": [
                                "Curvaturas anormais da coluna, para trás "
                                "e para a frente",
                                "Doenças dos músculos",
                                "Tipos de articulação",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para cuidar dos ossos e músculos "
                                 "deve-se:",
                            "options": [
                                "Fazer exercício, sentar direito, comer "
                                "cálcio e não carregar pesos a mais",
                                "Ficar sempre sentado",
                                "Carregar tudo às costas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "O sistema nervoso",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada órgão à parte do sistema "
                                 "nervoso a que pertence.",
                            "pairs": [
                                ["Cérebro, cerebelo e medula espinal", "Sistema nervoso central"],
                                ["Nervos e gânglios", "Sistema nervoso periférico"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada acto ao seu tipo.",
                            "pairs": [
                                ["Levantar o braço para responder", "Voluntário"],
                                ["Tirar a mão do fogo sem pensar", "Reflexo"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O arco reflexo é:",
                            "options": [
                                "O caminho do estímulo: receptor, nervo, "
                                "medula, nervo, músculo",
                                "Um osso do braço",
                                "Um tipo de articulação",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na experiência de Pavlov, o cão "
                                 "salivava ao ouvir a campainha porque:",
                            "options": [
                                "Aprendeu a associar o som à comida: um "
                                "reflexo condicionado",
                                "Tinha fome de campainhas",
                                "Estava doente",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quando o médico bate no joelho e a perna "
                                 "salta, é:",
                            "options": [
                                "Um acto reflexo, comandado pela medula",
                                "Um acto voluntário",
                                "Uma luxação",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 3  Reproducao nos seres vivos
        # ================================================================
        {
            "id": "u3",
            "titulo": "Reprodução nos seres vivos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A reprodução no Homem",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "O ciclo menstrual dura, em média, "
                                 "quantos dias?",
                            "a": "28",
                        },
                        {
                            "t": "choice",
                            "q": "A ovulação, o dia mais fértil, dá-se:",
                            "options": [
                                "A meio do ciclo, por volta do dia 14",
                                "No primeiro dia da menstruação",
                                "No último dia do ciclo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A fecundação é:",
                            "options": [
                                "A união do espermatozóide com o óvulo, "
                                "na trompa",
                                "O nascimento do bebé",
                                "A menstruação",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma gravidez na adolescência traz:",
                            "options": [
                                "Riscos para a saúde da rapariga, abandono "
                                "da escola e um bebé sem condições",
                                "Só alegria",
                                "Nenhuma consequência",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma gravidez dura cerca de quantas "
                                 "semanas?",
                            "a": "40",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Os métodos anti-conceptivos",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada método anti-conceptivo ao seu "
                                 "tipo.",
                            "pairs": [
                                ["Preservativo", "Artificial"],
                                ["Calendário", "Natural"],
                                ["Pílula", "Artificial"],
                                ["Temperatura basal", "Natural"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O único método que evita a gravidez e "
                                 "também as infecções de transmissão sexual "
                                 "é:",
                            "options": ["O preservativo", "A pílula", "O calendário"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os métodos naturais têm a desvantagem "
                                 "de:",
                            "options": [
                                "Falharem muito, porque o ciclo nem sempre "
                                "é regular",
                                "Custarem caro",
                                "Precisarem de médico",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada método ao que ele é.",
                            "pairs": [
                                ["Dispositivo intra-uterino", "Colocado no útero por um profissional, dura anos"],
                                ["Injecção", "Hormona dada de três em três meses"],
                                ["Pílula", "Comprimido tomado todos os dias"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Os adolescentes têm direito a:",
                            "options": [
                                "Informação e serviços de saúde sexual e "
                                "reprodutiva, sem serem julgados",
                                "Nada, até casarem",
                                "Só a conselhos dos amigos",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "As plantas: hormonas e tropismos",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada hormona vegetal à sua acção.",
                            "pairs": [
                                ["Auxinas", "Fazem crescer o caule e as raízes"],
                                ["Giberelinas", "Fazem germinar e alongar"],
                                ["Etileno", "Amadurece os frutos"],
                                ["Ácido abscísico", "Faz cair as folhas e dormir as sementes"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Para amadurecer bananas mais depressa, "
                                 "tapam-se num saco porque:",
                            "options": [
                                "O etileno que elas libertam fica junto "
                                "delas",
                                "Ficam mais quentes",
                                "Não apanham luz",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada movimento da planta ao seu "
                                 "nome.",
                            "pairs": [
                                ["O caule cresce para a luz", "Fototropismo"],
                                ["A raiz cresce para baixo", "Geotropismo"],
                                ["A mimosa fecha as folhas ao toque", "Nastismo"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A diferença entre tropismo e nastismo é "
                                 "que:",
                            "options": [
                                "O tropismo segue a direcção do estímulo; "
                                "o nastismo não",
                                "O nastismo é mais lento",
                                "Não há diferença",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa experiência, feijões com luz, com "
                                 "pouca luz e sem luz. Ao fim de duas "
                                 "semanas, os sem luz:",
                            "options": [
                                "Ficam amarelos, fracos e compridos",
                                "Crescem melhor",
                                "Ficam iguais aos outros",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 4  Agricultura
        # ================================================================
        {
            "id": "u4",
            "titulo": "Agricultura",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O solo",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada componente do solo à sua parte.",
                            "pairs": [
                                ["Areia, argila, limo e cascalho", "Parte mineral"],
                                ["Húmus", "Parte orgânica"],
                                ["Ar e água", "Os espaços entre as partículas"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de solo ao que ele faz "
                                 "com a água.",
                            "pairs": [
                                ["Arenoso", "Deixa-a passar depressa e seca"],
                                ["Argiloso", "Retém-na e encharca"],
                                ["Misto", "Retém o suficiente: o melhor para cultivar"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O húmus é:",
                            "options": [
                                "Matéria orgânica decomposta, que dá "
                                "fertilidade ao solo",
                                "Uma pedra",
                                "Um tipo de areia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na experiência da permeabilidade, "
                                 "deita-se água em frascos com solos "
                                 "diferentes para ver:",
                            "options": [
                                "Qual retém mais e qual deixa passar mais "
                                "água",
                                "Qual é mais bonito",
                                "Qual pesa mais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um solo escuro e fofo, com minhocas, é:",
                            "options": ["Fértil", "Estéril", "Arenoso"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Organismos, fertilidade e conservação",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada organismo do solo ao seu papel.",
                            "pairs": [
                                ["Plantas", "Produtores"],
                                ["Insectos e ratos", "Consumidores"],
                                ["Bactérias, fungos e minhocas", "Decompositores"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Os decompositores são importantes "
                                 "porque:",
                            "options": [
                                "Transformam os restos em húmus e "
                                "devolvem os nutrientes ao solo",
                                "Comem as colheitas",
                                "Secam o solo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A irrigação permite:",
                            "options": [
                                "Cultivar na época seca, com água levada "
                                "ao campo",
                                "Cultivar sem solo",
                                "Evitar as pragas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada prática de conservação do solo "
                                 "ao que ela evita.",
                            "pairs": [
                                ["Curvas de nível nas encostas", "A erosão pela chuva"],
                                ["Rotação de culturas", "O esgotamento dos nutrientes"],
                                ["Cobertura com palha", "A secura e as ervas"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "As queimadas antes de cultivar:",
                            "options": [
                                "Matam os organismos do solo e empobrecem-no",
                                "Fertilizam para sempre",
                                "Não têm efeito",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Culturas alimentares e adubos",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada cultura alimentar ao seu grupo.",
                            "pairs": [
                                ["Milho e arroz", "Cereais"],
                                ["Feijão e amendoim", "Leguminosas"],
                                ["Mandioca e batata-doce", "Raízes e tubérculos"],
                                ["Couve e tomate", "Hortícolas"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O adubo orgânico faz-se de:",
                            "options": [
                                "Estrume, restos de plantas e de cozinha, "
                                "deixados a decompor",
                                "Produtos químicos da fábrica",
                                "Areia e pedras",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma vantagem do adubo orgânico é:",
                            "options": [
                                "Ser barato, feito em casa, e melhorar o "
                                "solo sem o envenenar",
                                "Agir só num dia",
                                "Vir em saco",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Com os adubos artificiais deve-se:",
                            "options": [
                                "Usar a dose certa, com luvas, e longe da "
                                "água e das crianças",
                                "Deitar o mais possível",
                                "Guardá-los na cozinha",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um composto orgânico leva cerca de 3 "
                                 "meses a ficar pronto. Se se começou em "
                                 "Março, em que mês do ano está pronto? "
                                 "Responde com o número do mês.",
                            "a": "6",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 5  Auto-descobrimento
        # ================================================================
        {
            "id": "u5",
            "titulo": "Auto-descobrimento",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Inclusão e diversidade",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada conceito ao que ele é.",
                            "pairs": [
                                ["Preconceito", "Julgar alguém antes de o conhecer"],
                                ["Discriminação", "Tratar pior por ser diferente"],
                                ["Estigma", "Marca de vergonha posta num grupo"],
                                ["Exclusão", "Deixar de fora"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O estigma sobre quem tem HIV faz com "
                                 "que:",
                            "options": [
                                "As pessoas escondam a doença e não "
                                "procurem tratamento",
                                "A doença desapareça",
                                "Todos fiquem mais saudáveis",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Inclusão é:",
                            "options": [
                                "Respeitar as diferenças e dar lugar a "
                                "todos",
                                "Fazer todos iguais",
                                "Separar os diferentes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um colega com deficiência na turma:",
                            "options": [
                                "Tem os mesmos direitos e a turma ganha "
                                "com a diversidade",
                                "Deve ficar em casa",
                                "Atrasa os outros",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Discriminar alguém é:",
                            "options": [
                                "Uma violação dos direitos humanos",
                                "Uma opinião como outra qualquer",
                                "Permitido se for por brincadeira",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "As doenças",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada doença ao seu tipo.",
                            "pairs": [
                                ["Malária e cólera", "Transmissível"],
                                ["Diabetes e hipertensão", "Não transmissível"],
                                ["Tuberculose", "Transmissível"],
                                ["Asma", "Não transmissível"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada vector à doença que transmite.",
                            "pairs": [
                                ["Mosquito anófeles", "Malária"],
                                ["Mosca", "Diarreias"],
                                ["Água contaminada", "Cólera"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um factor de risco para a hipertensão é:",
                            "options": [
                                "Comer muito sal e não fazer exercício",
                                "Beber água",
                                "Dormir bem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A tinha e a sarna passam de pessoa para "
                                 "pessoa:",
                            "options": [
                                "Pelo contacto e pela roupa partilhada",
                                "Pelo ar",
                                "Não passam",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A obesidade previne-se com:",
                            "options": [
                                "Alimentação equilibrada e exercício",
                                "Refrescos e fritos",
                                "Jejum total",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Sistema reprodutor e medicamentos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O cancro mais frequente na mulher em "
                                 "Moçambique é:",
                            "options": [
                                "O do colo do útero, ligado ao vírus do "
                                "papiloma humano",
                                "O da pele",
                                "O do osso",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada cancro ao exame que o "
                                 "detecta cedo.",
                            "pairs": [
                                ["Da mama", "Auto-exame e mamografia"],
                                ["Do colo do útero", "Rastreio no centro de saúde"],
                                ["Da próstata", "Análise ao sangue e exame médico"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um caroço na mama ou uma hemorragia fora "
                                 "do período:",
                            "options": [
                                "São sinais para ir ao centro de saúde sem "
                                "demora",
                                "Passam sozinhos",
                                "Não têm importância",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Com os medicamentos deve-se:",
                            "options": [
                                "Tomar só com receita, na dose e no tempo "
                                "certos, e ver o prazo",
                                "Tomar os do vizinho",
                                "Parar assim que se sente melhor",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Comichão, manchas na pele e inchaço "
                                 "depois de um medicamento são:",
                            "options": [
                                "Uma reacção alérgica: pára-se e vai-se ao "
                                "centro de saúde",
                                "Sinal de que está a fazer efeito",
                                "Normal em todos",
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
