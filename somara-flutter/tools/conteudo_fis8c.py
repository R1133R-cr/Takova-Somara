# -*- coding: utf-8 -*-
"""O curso de Fisica da 8a classe -- a primeira Fisica da app.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Fisica -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, pp. 19-31.
     Guardado em Documents\\planos da 5a classe\\Livros\\Programas INDE 1o
     Ciclo\\fisica.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

A Fisica comeca na 8a
---------------------
O programa nao menciona a 7a classe uma unica vez: a visao geral dos
conteudos tem colunas para a 8a e a 9a e mais nada. E por isso que a 7a
nao tem Fisica e esta e a primeira.

As seis unidades tematicas, tal como o INDE as ordena
-----------------------------------------------------
    I    Introducao ao estudo da Fisica   materia e propriedades;
                                          grandezas e unidades
    II   Cinematica                       repouso, movimento, velocidade;
                                          MRU; MUV e queda livre
    III  Dinamica -- Leis de Newton       forca; as tres leis
    IV   Trabalho e Energia               trabalho, energia, potencia
    V    Fenomenos termicos               temperatura e escalas; calor
    VI   Optica geometrica                luz e propagacao; reflexao e
                                          espelhos planos

Seis unidades, treze aulas.

As unidades escrevem-se por extenso nos enunciados
--------------------------------------------------
"5 m/s" e "20 J" sao coisas que a voz nao sabe dizer: a barra virava
virgula e a letra ficava solta. Nos enunciados escreve-se "metros por
segundo" e "joules"; os simbolos ficam nas opcoes, que sao para ler.

Correr a partir de somara-flutter/:
    python tools/conteudo_fis8c.py            # so mostra
    python tools/conteudo_fis8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Física — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, pp. 19-31. As seis "
    "unidades e os conteúdos são do programa; os exercícios foram escritos "
    "a partir deles, porque um programa de ensino não traz exercícios e não "
    "há livro do aluno da 8ª classe publicado."
)

CURSO = {
    "id": "fis-8c",
    "disciplina": "Física",
    "classe": "8ª classe",
    "tag": "FIS",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # I  Introducao ao estudo da Fisica
        # ================================================================
        {
            "id": "u1",
            "titulo": "Introdução ao estudo da Física",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A Física e a matéria",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Física é a ciência que estuda:",
                            "options": [
                                "Os fenómenos da natureza em que a matéria "
                                "não muda de substância",
                                "Só os seres vivos",
                                "A história dos povos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada fenómeno ao seu tipo.",
                            "pairs": [
                                ["O gelo a derreter", "Fenómeno físico"],
                                ["A lenha a arder", "Fenómeno químico"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Matéria é:",
                            "options": [
                                "Tudo o que tem massa e ocupa espaço",
                                "Só o que se vê",
                                "Só o que é sólido",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A inércia, a divisibilidade e a "
                                 "impenetrabilidade são:",
                            "options": [
                                "Propriedades gerais da matéria",
                                "Propriedades só dos líquidos",
                                "Ramos da Física",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A água sobe por um pedaço de papel ou por "
                                 "um pavio. Esse fenómeno chama-se:",
                            "options": ["Capilaridade", "Inércia", "Reflexão"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Grandezas e unidades",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada grandeza fundamental à sua "
                                 "unidade no Sistema Internacional.",
                            "pairs": [
                                ["Comprimento", "metro"],
                                ["Massa", "quilograma"],
                                ["Tempo", "segundo"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas é uma grandeza derivada?",
                            "options": ["A velocidade", "A massa", "O tempo"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada grandeza ao instrumento que a "
                                 "mede.",
                            "pairs": [
                                ["Comprimento", "Fita métrica"],
                                ["Massa", "Balança"],
                                ["Tempo", "Cronómetro"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Quantos centímetros tem 1 metro e meio?",
                            "a": "150",
                        },
                        {
                            "t": "input",
                            "q": "Quantos gramas tem 2 quilogramas?",
                            "a": "2000",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # II  Cinematica
        # ================================================================
        {
            "id": "u2",
            "titulo": "Cinemática",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Repouso, movimento e velocidade",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um corpo está em movimento quando:",
                            "options": [
                                "Muda de posição em relação a um ponto de "
                                "referência",
                                "Faz barulho",
                                "Tem muita massa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um passageiro sentado num autocarro em "
                                 "andamento está:",
                            "options": [
                                "Em repouso em relação ao autocarro e em "
                                "movimento em relação à estrada",
                                "Sempre em repouso",
                                "Sempre em movimento",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A velocidade calcula-se dividindo:",
                            "options": [
                                "A distância pelo tempo",
                                "O tempo pela distância",
                                "A massa pelo tempo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um carro percorre 100 metros em 20 "
                                 "segundos. Qual é a velocidade, em metros "
                                 "por segundo?",
                            "a": "5",
                        },
                        {
                            "t": "choice",
                            "q": "No Sistema Internacional, a velocidade "
                                 "mede-se em:",
                            "options": ["m/s", "km", "kg"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O movimento rectilíneo uniforme",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "No movimento rectilíneo uniforme, a "
                                 "velocidade:",
                            "options": [
                                "É constante e a trajectória é uma recta",
                                "Aumenta sempre",
                                "É sempre zero",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um autocarro anda a 60 quilómetros por "
                                 "hora, sempre à mesma velocidade. Quantos "
                                 "quilómetros percorre em 2 horas?",
                            "a": "120",
                        },
                        {
                            "t": "input",
                            "q": "Um ciclista a 5 metros por segundo, em "
                                 "movimento uniforme, leva quantos segundos "
                                 "a percorrer 200 metros?",
                            "a": "40",
                        },
                        {
                            "t": "choice",
                            "q": "No gráfico da distância em função do "
                                 "tempo, o movimento uniforme é:",
                            "options": [
                                "Uma recta inclinada",
                                "Uma curva",
                                "Uma recta vertical",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No gráfico da velocidade em função do "
                                 "tempo, o movimento uniforme é:",
                            "options": [
                                "Uma recta horizontal",
                                "Uma recta que sobe",
                                "Uma curva",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Movimento variado e queda livre",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A aceleração mede:",
                            "options": [
                                "Quanto a velocidade muda em cada segundo",
                                "A distância percorrida",
                                "O peso do corpo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um carro parte do repouso e ganha 2 "
                                 "metros por segundo em cada segundo. "
                                 "Que velocidade tem ao fim de 5 segundos, "
                                 "em metros por segundo?",
                            "a": "10",
                        },
                        {
                            "t": "choice",
                            "q": "Um movimento em que a velocidade diminui "
                                 "de forma regular chama-se:",
                            "options": [
                                "Uniformemente retardado",
                                "Uniformemente acelerado",
                                "Uniforme",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na queda livre, todos os corpos caem:",
                            "options": [
                                "Com a mesma aceleração, se não houver ar "
                                "a travar",
                                "Mais depressa quanto mais pesados",
                                "À mesma velocidade constante",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um corpo cai em queda livre. Tomando a "
                                 "aceleração da gravidade como 10 metros por "
                                 "segundo em cada segundo, que velocidade "
                                 "tem ao fim de 3 segundos, em metros por "
                                 "segundo?",
                            "a": "30",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # III  Dinamica -- Leis de Newton
        # ================================================================
        {
            "id": "u3",
            "titulo": "Dinâmica: as leis de Newton",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A força",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma força pode:",
                            "options": [
                                "Pôr um corpo em movimento, pará-lo ou "
                                "deformá-lo",
                                "Só deformar",
                                "Só aquecer",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os elementos de uma força são:",
                            "options": [
                                "Ponto de aplicação, direcção, sentido e "
                                "intensidade",
                                "Massa, volume e tempo",
                                "Cor, forma e tamanho",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Duas pessoas empurram um carro no mesmo "
                                 "sentido, uma com 200 newtons e outra com "
                                 "300. Qual é a força resultante, em "
                                 "newtons?",
                            "a": "500",
                        },
                        {
                            "t": "input",
                            "q": "Dois rapazes puxam uma corda em sentidos "
                                 "contrários, um com 400 newtons e outro com "
                                 "150. Qual é a força resultante, em "
                                 "newtons?",
                            "a": "250",
                        },
                        {
                            "t": "choice",
                            "q": "No Sistema Internacional, a força mede-se "
                                 "em:",
                            "options": ["Newton", "Quilograma", "Metro"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "As três leis de Newton",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Pela primeira lei de Newton, um corpo sem "
                                 "forças a actuar:",
                            "options": [
                                "Fica em repouso ou em movimento uniforme",
                                "Pára sempre",
                                "Acelera",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quando o autocarro trava de repente, os "
                                 "passageiros vão para a frente por causa "
                                 "da:",
                            "options": ["Inércia", "Gravidade", "Reflexão"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A segunda lei de Newton diz que a força é "
                                 "igual a:",
                            "options": [
                                "Massa vezes aceleração",
                                "Massa vezes velocidade",
                                "Distância a dividir pelo tempo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Que força, em newtons, é preciso para dar "
                                 "a um corpo de 2 quilogramas uma aceleração "
                                 "de 3 metros por segundo em cada segundo?",
                            "a": "6",
                        },
                        {
                            "t": "choice",
                            "q": "Pela terceira lei de Newton, quando "
                                 "empurras uma parede:",
                            "options": [
                                "A parede empurra-te com uma força igual e "
                                "de sentido contrário",
                                "A parede não faz nada",
                                "A parede empurra-te com o dobro da força",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # IV  Trabalho e Energia
        # ================================================================
        {
            "id": "u4",
            "titulo": "Trabalho e energia",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O trabalho e a energia",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Em Física, uma força realiza trabalho "
                                 "quando:",
                            "options": [
                                "Desloca o corpo em que actua",
                                "Está a suar",
                                "O corpo fica parado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma força de 10 newtons empurra uma caixa "
                                 "ao longo de 2 metros. Qual é o trabalho "
                                 "realizado, em joules?",
                            "a": "20",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada situação ao tipo de energia.",
                            "pairs": [
                                ["Uma pedra no alto de um monte", "Energia potencial"],
                                ["Uma bola a rolar", "Energia cinética"],
                                ["Uma pilha", "Energia química"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O princípio da conservação da energia "
                                 "diz que a energia:",
                            "options": [
                                "Não se cria nem se destrói, só se "
                                "transforma",
                                "Desaparece quando se gasta",
                                "Aparece do nada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa lâmpada, a energia eléctrica "
                                 "transforma-se em:",
                            "options": [
                                "Luz e calor",
                                "Energia química",
                                "Massa",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Potência e energia eléctrica",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A potência mede:",
                            "options": [
                                "O trabalho realizado em cada segundo",
                                "A força total",
                                "A distância percorrida",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma máquina realiza 100 joules de trabalho "
                                 "em 5 segundos. Qual é a potência, em "
                                 "watts?",
                            "a": "20",
                        },
                        {
                            "t": "choice",
                            "q": "A barragem de Cahora Bassa produz "
                                 "electricidade a partir de:",
                            "options": [
                                "Água em movimento: energia hidroeléctrica",
                                "Carvão",
                                "Vento",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada fonte de energia ao seu tipo.",
                            "pairs": [
                                ["Sol e vento", "Renovável"],
                                ["Carvão e petróleo", "Não renovável"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Poupar energia eléctrica em casa é:",
                            "options": [
                                "Apagar as luzes e desligar o que não se "
                                "usa",
                                "Deixar tudo ligado",
                                "Usar lâmpadas mais fracas na rua",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # V  Fenomenos termicos
        # ================================================================
        {
            "id": "u5",
            "titulo": "Fenómenos térmicos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Temperatura e escalas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A temperatura mede:",
                            "options": [
                                "Quão quente ou frio está um corpo",
                                "O peso de um corpo",
                                "A quantidade de água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O instrumento que mede a temperatura é:",
                            "options": ["O termómetro", "A balança", "O cronómetro"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada escala ao ponto em que a água "
                                 "ferve.",
                            "pairs": [
                                ["Celsius", "100 graus"],
                                ["Kelvin", "373 kelvin"],
                                ["Fahrenheit", "212 graus"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Para passar de graus Celsius a kelvin "
                                 "soma-se 273. Quantos kelvin são 25 graus "
                                 "Celsius?",
                            "a": "298",
                        },
                        {
                            "t": "choice",
                            "q": "Quando dois corpos a temperaturas "
                                 "diferentes ficam em contacto:",
                            "options": [
                                "O calor passa do mais quente para o mais "
                                "frio até ficarem iguais",
                                "O frio passa para o quente",
                                "Nada acontece",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Calor: dilatação e transmissão",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Quando se aquece um corpo, em geral ele:",
                            "options": ["Dilata: aumenta de volume", "Encolhe", "Fica igual"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os carris do comboio têm folgas entre "
                                 "eles para:",
                            "options": [
                                "Não empenarem quando dilatam com o calor",
                                "Fazerem barulho",
                                "Poupar ferro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada forma de transmissão de calor ao "
                                 "exemplo.",
                            "pairs": [
                                ["Condução", "A colher aquece na panela"],
                                ["Convecção", "O ar quente sobe na sala"],
                                ["Radiação", "O sol aquece a pele"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Os metais são bons:",
                            "options": [
                                "Condutores de calor",
                                "Isoladores de calor",
                                "Reflectores de som",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As mudanças climáticas estão ligadas ao "
                                 "aumento:",
                            "options": [
                                "Dos gases que prendem o calor na "
                                "atmosfera",
                                "Do número de rios",
                                "Da altura das montanhas",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # VI  Optica geometrica
        # ================================================================
        {
            "id": "u6",
            "titulo": "Óptica geométrica",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A luz e a sua propagação",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada corpo ao seu tipo.",
                            "pairs": [
                                ["O Sol", "Corpo luminoso"],
                                ["A Lua", "Corpo iluminado"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Num meio homogéneo, a luz propaga-se:",
                            "options": ["Em linha recta", "Em curva", "Em ziguezague"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A sombra forma-se porque:",
                            "options": [
                                "A luz não contorna os corpos opacos",
                                "A luz é fria",
                                "O corpo absorve o ar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Num eclipse do Sol:",
                            "options": [
                                "A Lua fica entre o Sol e a Terra",
                                "A Terra fica entre o Sol e a Lua",
                                "O Sol se apaga",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A zona de sombra parcial à volta da sombra "
                                 "chama-se:",
                            "options": ["Penumbra", "Reflexo", "Eclipse"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Reflexão e espelhos planos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A reflexão da luz é:",
                            "options": [
                                "A luz a voltar para trás ao bater numa "
                                "superfície",
                                "A luz a atravessar o vidro",
                                "A luz a apagar-se",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um raio de luz bate num espelho plano com "
                                 "um ângulo de incidência de 40 graus. "
                                 "Quantos graus tem o ângulo de reflexão?",
                            "a": "40",
                        },
                        {
                            "t": "choice",
                            "q": "A imagem num espelho plano é:",
                            "options": [
                                "Do mesmo tamanho, direita e invertida da "
                                "esquerda para a direita",
                                "Mais pequena e de pernas para o ar",
                                "Maior e de cor diferente",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Se estás a 1 metro de um espelho plano, a "
                                 "tua imagem parece estar:",
                            "options": [
                                "A 1 metro atrás do espelho",
                                "Em cima do espelho",
                                "A 2 metros atrás do espelho",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um periscópio serve para ver por cima de "
                                 "um obstáculo e usa:",
                            "options": [
                                "Dois espelhos planos inclinados",
                                "Uma lâmpada",
                                "Um íman",
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
