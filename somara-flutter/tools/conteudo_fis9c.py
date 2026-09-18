# -*- coding: utf-8 -*-
"""O curso de Fisica da 9a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Fisica -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, 9a classe,
     pp. 32-44. Guardado em Documents\\planos da 5a classe\\Livros\\
     Programas INDE 1o Ciclo\\fisica.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As cinco unidades tematicas, pela ordem do programa
---------------------------------------------------
    I    Optica geometrica            espelhos esfericos; refraccao;
                                      lentes e o olho
    II   Estatica dos solidos e       equilibrio e momento; maquinas
         fluidos                      simples; densidade e pressao;
                                      Pascal, Arquimedes e flutuacao
    III  Electricidade                carga e electrizacao; corrente,
                                      tensao e circuito; lei de Ohm;
                                      associacoes e potencia
    IV   Electromagnetismo            imanes e campo magnetico; Oersted e
                                      o electroiman
    V    Oscilacoes e ondas mecanicas oscilacoes; ondas

Cinco unidades, quinze aulas.

As unidades por extenso, como na 8a
-----------------------------------
"ohms", "volts", "amperes", "watts", "pascal" e "newtons" escrevem-se
por palavras nos enunciados; os simbolos ficam nas opcoes. As contas
foram escolhidas para dar inteiros, e a gravidade toma-se igual a 10.

Correr a partir de somara-flutter/:
    python tools/conteudo_fis9c.py            # so mostra
    python tools/conteudo_fis9c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Física — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, 9ª classe, pp. 32-44. "
    "As cinco unidades e os conteúdos são do programa; os exercícios foram "
    "escritos a partir deles, porque um programa de ensino não traz "
    "exercícios e não há livro do aluno da 9ª classe publicado."
)

CURSO = {
    "id": "fis-9c",
    "disciplina": "Física",
    "classe": "9ª classe",
    "tag": "FIS",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # I  Optica geometrica
        # ================================================================
        {
            "id": "u1",
            "titulo": "Óptica geométrica",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Espelhos esféricos",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada espelho esférico ao seu "
                                 "exemplo.",
                            "pairs": [
                                ["Côncavo", "O espelho do dentista, que amplia"],
                                ["Convexo", "O retrovisor do carro, que mostra mais campo"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Num espelho esférico, o foco fica a "
                                 "meio caminho entre o espelho e o centro "
                                 "de curvatura. Se o raio de curvatura é 40 "
                                 "centímetros, a quantos centímetros está o "
                                 "foco?",
                            "a": "20",
                        },
                        {
                            "t": "choice",
                            "q": "Num espelho côncavo, um raio que chega "
                                 "paralelo ao eixo reflecte-se:",
                            "options": [
                                "Passando pelo foco",
                                "Paralelo ao eixo",
                                "De volta pelo mesmo caminho",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um objecto entre o foco e um espelho "
                                 "côncavo dá uma imagem:",
                            "options": [
                                "Direita, maior e virtual",
                                "Invertida e mais pequena",
                                "Nenhuma",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A imagem num espelho convexo é sempre:",
                            "options": [
                                "Direita, mais pequena e virtual",
                                "Invertida e maior",
                                "Real e do mesmo tamanho",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A refracção da luz",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A refracção é:",
                            "options": [
                                "O desvio da luz ao passar de um meio para "
                                "outro, como do ar para a água",
                                "A luz a voltar para trás",
                                "A luz a apagar-se",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um lápis dentro de um copo com água "
                                 "parece partido porque:",
                            "options": [
                                "A luz muda de direcção ao sair da água "
                                "para o ar",
                                "A água parte o lápis",
                                "O copo é curvo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao passar do ar para a água, a luz:",
                            "options": [
                                "Abranda e aproxima-se da normal",
                                "Acelera e afasta-se da normal",
                                "Não muda",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O índice de refracção de um meio diz:",
                            "options": [
                                "Quantas vezes a luz é mais lenta nesse "
                                "meio do que no vazio",
                                "A cor da luz",
                                "O peso do meio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "No vazio a luz anda a 300 mil "
                                 "quilómetros por segundo. Num vidro de "
                                 "índice de refracção 1,5, anda a quantos "
                                 "mil quilómetros por segundo?",
                            "a": "200",
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Lentes e o olho humano",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada lente ao que ela faz aos raios "
                                 "paralelos.",
                            "pairs": [
                                ["Convergente, mais grossa no meio", "Junta-os no foco"],
                                ["Divergente, mais fina no meio", "Afasta-os"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Uma lupa é uma lente:",
                            "options": ["Convergente", "Divergente", "Plana"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma lente dá uma imagem 3 vezes maior "
                                 "que o objecto. Se o objecto tem 2 "
                                 "centímetros, quantos centímetros tem a "
                                 "imagem?",
                            "a": "6",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada defeito do olho à lente que o "
                                 "corrige.",
                            "pairs": [
                                ["Miopia: vê mal ao longe", "Divergente"],
                                ["Hipermetropia: vê mal ao perto", "Convergente"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Para cuidar dos olhos deve-se:",
                            "options": [
                                "Não olhar para o Sol, ler com luz "
                                "suficiente e lavar as mãos antes de os "
                                "tocar",
                                "Esfregá-los com força",
                                "Ler no escuro",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # II  Estatica dos solidos e fluidos
        # ================================================================
        {
            "id": "u2",
            "titulo": "Estática dos sólidos e dos fluidos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Equilíbrio e momento de uma força",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada tipo de equilíbrio ao seu "
                                 "exemplo.",
                            "pairs": [
                                ["Estável", "Uma bola no fundo de uma taça"],
                                ["Instável", "Uma bola no cimo de uma bola maior"],
                                ["Indiferente", "Uma bola numa mesa plana"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O centro de gravidade de um corpo é:",
                            "options": [
                                "O ponto onde se pode considerar aplicado "
                                "o seu peso",
                                "O ponto mais alto",
                                "O ponto mais pesado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma força de 20 newtons aplicada a 2 "
                                 "metros do eixo tem que momento, em "
                                 "newtons-metro?",
                            "a": "40",
                        },
                        {
                            "t": "choice",
                            "q": "Para abrir uma porta com menos esforço, "
                                 "empurra-se:",
                            "options": [
                                "Longe das dobradiças, porque o braço é "
                                "maior",
                                "Junto às dobradiças",
                                "No meio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um camião carregado no alto vira mais "
                                 "facilmente porque:",
                            "options": [
                                "O centro de gravidade subiu",
                                "O centro de gravidade desceu",
                                "Tem mais rodas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "As máquinas simples",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada alavanca ao seu tipo.",
                            "pairs": [
                                ["Tesoura: o apoio no meio", "Interfixa"],
                                ["Carrinho de mão: a carga no meio", "Inter-resistente"],
                                ["Pinça: a força no meio", "Interpotente"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Numa alavanca, uma pedra de 80 newtons "
                                 "está a 1 metro do apoio. Que força, em "
                                 "newtons, a equilibra a 4 metros do "
                                 "apoio?",
                            "a": "20",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada roldana ao que ela faz.",
                            "pairs": [
                                ["Fixa", "Só muda a direcção da força"],
                                ["Móvel", "Divide a força por dois"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Com uma roldana móvel, para levantar 100 "
                                 "newtons bastam quantos newtons?",
                            "a": "50",
                        },
                        {
                            "t": "choice",
                            "q": "A regra de ouro da mecânica diz que as "
                                 "máquinas simples:",
                            "options": [
                                "Poupam força mas não poupam trabalho: o "
                                "que se ganha em força perde-se em "
                                "distância",
                                "Poupam trabalho",
                                "Criam energia",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Densidade e pressão",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Um corpo de 200 gramas ocupa 100 "
                                 "centímetros cúbicos. Qual é a densidade, "
                                 "em gramas por centímetro cúbico?",
                            "a": "2",
                        },
                        {
                            "t": "input",
                            "q": "Uma força de 200 newtons apoia-se numa "
                                 "superfície de 4 metros quadrados. Qual é "
                                 "a pressão, em pascal?",
                            "a": "50",
                        },
                        {
                            "t": "choice",
                            "q": "Uma faca afiada corta melhor porque:",
                            "options": [
                                "A mesma força fica numa área menor e a "
                                "pressão é maior",
                                "Pesa mais",
                                "É mais comprida",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "A pressão da água a uma profundidade é "
                                 "densidade vezes gravidade vezes altura. "
                                 "Com densidade 1000, gravidade 10 e 2 "
                                 "metros de profundidade, qual é a pressão, "
                                 "em pascal?",
                            "a": "20000",
                        },
                        {
                            "t": "choice",
                            "q": "A experiência de Torricelli mediu:",
                            "options": [
                                "A pressão atmosférica, com uma coluna de "
                                "mercúrio de 76 centímetros",
                                "A pressão de um sólido",
                                "A densidade do ar",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Pascal, Arquimedes e a flutuação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O princípio de Pascal diz que a pressão "
                                 "feita num líquido fechado:",
                            "options": [
                                "Transmite-se igual a todos os pontos do "
                                "líquido",
                                "Só se sente no fundo",
                                "Desaparece",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Numa prensa hidráulica, o êmbolo grande "
                                 "tem 10 vezes a área do pequeno. Com 50 "
                                 "newtons no pequeno, quantos newtons faz o "
                                 "grande?",
                            "a": "500",
                        },
                        {
                            "t": "choice",
                            "q": "O princípio de Arquimedes diz que um "
                                 "corpo num líquido recebe:",
                            "options": [
                                "Um empuxo para cima igual ao peso do "
                                "líquido que desloca",
                                "Uma força para baixo",
                                "Nada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um corpo flutua quando:",
                            "options": [
                                "É menos denso que o líquido",
                                "É mais denso que o líquido",
                                "É muito pequeno",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Nos vasos comunicantes, o mesmo líquido "
                                 "em repouso fica:",
                            "options": [
                                "À mesma altura em todos os ramos",
                                "Mais alto no ramo mais largo",
                                "Mais alto no ramo mais estreito",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para prevenir afogamentos na praia ou no "
                                 "rio:",
                            "options": [
                                "Não nadar sozinho nem onde não se sabe a "
                                "profundidade, e respeitar as bandeiras",
                                "Nadar depois de beber",
                                "Ir para longe da margem",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # III  Electricidade
        # ================================================================
        {
            "id": "u3",
            "titulo": "Electricidade",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Carga eléctrica e electrização",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Esfregar uma régua de plástico no cabelo "
                                 "e ela atrair papelinhos é electrização "
                                 "por:",
                            "options": ["Atrito", "Contacto", "Indução"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada par de cargas ao que acontece "
                                 "entre elas.",
                            "pairs": [
                                ["Duas cargas iguais", "Repelem-se"],
                                ["Duas cargas contrárias", "Atraem-se"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O electroscópio de folhas serve para:",
                            "options": [
                                "Detectar se um corpo está electrizado",
                                "Medir a temperatura",
                                "Pesar cargas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um corpo fica com carga negativa quando:",
                            "options": [
                                "Ganha electrões",
                                "Perde electrões",
                                "Ganha protões",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O campo eléctrico é:",
                            "options": [
                                "A região à volta de uma carga onde se "
                                "sentem forças eléctricas",
                                "Um campo de futebol",
                                "Um fio de cobre",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Corrente, tensão e circuito",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada grandeza à sua unidade.",
                            "pairs": [
                                ["Intensidade da corrente", "Ampere"],
                                ["Tensão eléctrica", "Volt"],
                                ["Resistência", "Ohm"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada corrente ao seu exemplo.",
                            "pairs": [
                                ["Contínua", "A de uma pilha"],
                                ["Alternada", "A da rede eléctrica em casa"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A corrente eléctrica só existe num "
                                 "circuito:",
                            "options": [
                                "Fechado, com uma fonte de tensão",
                                "Aberto",
                                "Sem fonte",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada aparelho de medida à forma de "
                                 "o ligar no circuito.",
                            "pairs": [
                                ["Amperímetro", "Em série"],
                                ["Voltímetro", "Em paralelo"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A tensão da rede em Moçambique é de 220 "
                                 "volts. Tocar num fio descarnado:",
                            "options": [
                                "Pode matar: nunca se mexe em fios com a "
                                "corrente ligada",
                                "Não faz nada",
                                "Só dá cócegas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A lei de Ohm e a resistência",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A primeira lei de Ohm diz que a tensão é "
                                 "igual a:",
                            "options": [
                                "Resistência vezes intensidade",
                                "Resistência a dividir pela intensidade",
                                "Intensidade ao quadrado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma resistência de 4 ohms está ligada a "
                                 "12 volts. Que intensidade a atravessa, em "
                                 "amperes?",
                            "a": "3",
                        },
                        {
                            "t": "input",
                            "q": "Por uma lâmpada passam 2 amperes quando "
                                 "está a 220 volts. Qual é a sua "
                                 "resistência, em ohms?",
                            "a": "110",
                        },
                        {
                            "t": "match",
                            "q": "Pela segunda lei de Ohm, liga cada "
                                 "mudança no fio ao efeito na resistência.",
                            "pairs": [
                                ["Fio mais comprido", "Resistência maior"],
                                ["Fio mais grosso", "Resistência menor"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "No gráfico da intensidade em função da "
                                 "tensão, um condutor que segue a lei de "
                                 "Ohm dá:",
                            "options": [
                                "Uma recta que passa pela origem",
                                "Uma curva",
                                "Uma recta horizontal",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Associações, potência e a lei de Joule",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Três resistências de 2, 3 e 5 ohms em "
                                 "série dão uma resistência total de "
                                 "quantos ohms?",
                            "a": "10",
                        },
                        {
                            "t": "input",
                            "q": "Duas resistências de 6 ohms em paralelo "
                                 "dão uma resistência total de quantos "
                                 "ohms?",
                            "a": "3",
                        },
                        {
                            "t": "input",
                            "q": "Um ferro de engomar a 220 volts é "
                                 "atravessado por 2 amperes. Qual é a "
                                 "potência, em watts?",
                            "a": "440",
                        },
                        {
                            "t": "input",
                            "q": "Uma lâmpada de 100 watts ligada 10 horas "
                                 "consome quantos quilowatt-hora?",
                            "a": "1",
                        },
                        {
                            "t": "choice",
                            "q": "A lei de Joule-Lenz explica que a "
                                 "corrente numa resistência:",
                            "options": [
                                "Produz calor, como no ferro de engomar e "
                                "no fogão eléctrico",
                                "Produz frio",
                                "Não produz nada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um curto-circuito:",
                            "options": [
                                "Deixa passar uma corrente enorme, aquece "
                                "os fios e pode causar incêndio",
                                "Poupa energia",
                                "Faz a luz mais forte sem perigo",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # IV  Electromagnetismo
        # ================================================================
        {
            "id": "u4",
            "titulo": "Electromagnetismo",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Ímanes e campo magnético",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada par de pólos ao que acontece "
                                 "entre eles.",
                            "pairs": [
                                ["Norte com norte", "Repelem-se"],
                                ["Norte com sul", "Atraem-se"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Se se parte um íman ao meio:",
                            "options": [
                                "Ficam dois ímanes, cada um com norte e "
                                "sul",
                                "Fica um pólo norte e um pólo sul "
                                "separados",
                                "Deixa de ser íman",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O campo magnético é:",
                            "options": [
                                "A região à volta do íman onde se sentem "
                                "forças magnéticas",
                                "O peso do íman",
                                "A cor do íman",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A bússola aponta para o norte porque:",
                            "options": [
                                "A Terra tem um campo magnético e a agulha "
                                "é um íman",
                                "O norte é mais frio",
                                "O Sol a puxa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um íman atrai:",
                            "options": [
                                "O ferro e o aço",
                                "A madeira e o plástico",
                                "Tudo",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Oersted e o electroíman",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A experiência de Oersted mostrou que:",
                            "options": [
                                "Uma corrente eléctrica cria um campo "
                                "magnético: a bússola desvia-se ao pé do "
                                "fio",
                                "Os ímanes produzem corrente",
                                "A luz é magnética",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um electroíman faz-se com:",
                            "options": [
                                "Um fio enrolado à volta de um núcleo de "
                                "ferro, com corrente a passar",
                                "Um íman de pedra",
                                "Um fio de plástico",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A vantagem do electroíman sobre o íman "
                                 "permanente é:",
                            "options": [
                                "Liga-se e desliga-se com a corrente",
                                "Ser mais bonito",
                                "Não precisar de ferro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada aparelho ao que o electroíman "
                                 "faz nele.",
                            "pairs": [
                                ["Campainha eléctrica", "Puxa o martelo que bate na campânula"],
                                ["Grua de sucata", "Levanta e larga o ferro"],
                                ["Motor eléctrico", "Faz girar o eixo"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Para o electroíman ficar mais forte:",
                            "options": [
                                "Mais voltas de fio ou mais corrente",
                                "Menos voltas",
                                "Tirar o núcleo de ferro",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # V  Oscilacoes e ondas mecanicas
        # ================================================================
        {
            "id": "u5",
            "titulo": "Oscilações e ondas mecânicas",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "As oscilações",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada grandeza da oscilação ao que "
                                 "ela é.",
                            "pairs": [
                                ["Amplitude", "O afastamento máximo da posição de equilíbrio"],
                                ["Período", "O tempo de uma oscilação completa"],
                                ["Frequência", "O número de oscilações por segundo"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Um pêndulo faz uma oscilação completa em "
                                 "meio segundo. Qual é a frequência, em "
                                 "hertz?",
                            "a": "2",
                        },
                        {
                            "t": "input",
                            "q": "Uma oscilação tem frequência de 5 hertz. "
                                 "Quantas oscilações faz em 4 segundos?",
                            "a": "20",
                        },
                        {
                            "t": "choice",
                            "q": "O período de um pêndulo simples "
                                 "depende:",
                            "options": [
                                "Do comprimento do fio, e não da massa",
                                "Da massa, e não do comprimento",
                                "Da cor do peso",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No gráfico da elongação em função do "
                                 "tempo, o movimento harmónico simples "
                                 "dá:",
                            "options": ["Uma curva em onda", "Uma recta", "Um círculo"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "As ondas mecânicas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma onda mecânica é:",
                            "options": [
                                "A propagação de uma oscilação num meio, "
                                "sem transportar matéria",
                                "Uma pedra a cair",
                                "O vento",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O comprimento de onda é:",
                            "options": [
                                "A distância entre duas cristas seguidas",
                                "A altura da crista",
                                "O tempo de uma oscilação",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma onda tem 2 metros de comprimento de "
                                 "onda e frequência de 5 hertz. A que "
                                 "velocidade se propaga, em metros por "
                                 "segundo?",
                            "a": "10",
                        },
                        {
                            "t": "choice",
                            "q": "O som é uma onda mecânica porque:",
                            "options": [
                                "Precisa de um meio, como o ar, para se "
                                "propagar",
                                "Anda no vazio",
                                "É luz",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A poluição sonora, como música muito "
                                 "alta durante horas:",
                            "options": [
                                "Danifica o ouvido e tira o sono: "
                                "baixa-se o volume",
                                "Faz bem aos ouvidos",
                                "Não tem efeito",
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
