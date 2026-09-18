# -*- coding: utf-8 -*-
"""O curso de Matematica da 9a classe -- o primeiro curso da 9a.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Matematica -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, 9a classe,
     pp. 82-110. Guardado em Documents\\planos da 5a classe\\Livros\\
     Programas INDE 1o Ciclo\\matematica.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As oito unidades tematicas, pela ordem do programa
--------------------------------------------------
    I     Numeros e operacoes (1)   teoria de conjuntos; numeros reais;
                                    radiciacao; operacoes com radicais
    II    Algebra (1)               inequacoes e sistemas de inequacoes
    III   Geometria (1)             homotetia e proporcoes; semelhanca de
                                    triangulos; Thales e Pitagoras
    IV    Algebra (2)               polinomios; produtos notaveis;
                                    equacoes quadraticas
    V     Funcoes                   funcao quadratica
    VI    Algebra (3)               inequacoes quadraticas
    VII   Organizacao e tratamento  estatistica: frequencias; media,
          de dados                  moda e mediana
    VIII  Geometria (2)             poliedros e Euler; prismas;
                                    piramides; cilindro, cone e esfera

Oito unidades, vinte e uma aulas. E a Matematica maior da app, porque o
programa da 9a e o maior do ciclo (vinte e cinco horas so para os numeros
reais).

O que a voz sabe dizer
----------------------
A raiz quadrada, o quadrado, o cubo, os conjuntos e os sinais ja se
diziam desde a 8a. A raiz cubica entra com esta classe: o simbolo ∛ passa
a ler-se "raiz cubica de" (tools/pronuncia.py). Potencias de expoente
fraccionario e expoente negativo nao tem simbolo que a voz diga, por isso
escrevem-se por palavras no enunciado ("elevado a um terco") e em simbolo
so nas opcoes. Nas contas com π toma-se π igual a 3, dito no enunciado,
para a resposta ser inteira.

Correr a partir de somara-flutter/:
    python tools/conteudo_mat9c.py            # so mostra
    python tools/conteudo_mat9c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Matemática — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, 9ª classe, pp. 82-110. "
    "As oito unidades temáticas e os conteúdos são do programa; os "
    "exercícios foram escritos a partir deles, porque um programa de ensino "
    "não traz exercícios e não há livro do aluno da 9ª classe publicado."
)

CURSO = {
    "id": "mat-9c",
    "disciplina": "Matemática",
    "classe": "9ª classe",
    "tag": "MAT",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # I  Numeros e operacoes (1)
        # ================================================================
        {
            "id": "u1",
            "titulo": "Números e operações (1)",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Teoria de conjuntos",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "A = {1, 2, 3} e B = {3, 4}. Quantos "
                                 "elementos tem A ∪ B?",
                            "a": "4",
                        },
                        {
                            "t": "input",
                            "q": "A = {1, 2, 3, 4} e B = {2, 4, 6}. "
                                 "Quantos elementos tem A ∩ B?",
                            "a": "2",
                        },
                        {
                            "t": "input",
                            "q": "A = {1, 2, 3, 4, 5} e B = {2, 4}. "
                                 "Quantos elementos tem a diferença A "
                                 "menos B?",
                            "a": "3",
                        },
                        {
                            "t": "input",
                            "q": "O universo U é {1, 2, 3, 4, 5, 6} e "
                                 "A = {1, 3, 5}. Quantos elementos tem o "
                                 "complementar de A?",
                            "a": "3",
                        },
                        {
                            "t": "choice",
                            "q": "Dois conjuntos sem nenhum elemento em "
                                 "comum dizem-se:",
                            "options": ["Disjuntos", "Iguais", "Infinitos"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O conjunto dos números naturais é:",
                            "options": [
                                "Infinito: nunca acaba",
                                "Finito: acaba no 100",
                                "Vazio",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Os números reais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um número irracional é o que:",
                            "options": [
                                "Não se escreve como fracção: a dízima é "
                                "infinita e não periódica",
                                "É negativo",
                                "É muito grande",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada número ao conjunto mais "
                                 "pequeno a que pertence.",
                            "pairs": [
                                ["7", "Naturais"],
                                ["−3", "Inteiros"],
                                ["1/2", "Racionais"],
                                ["√2", "Irracionais"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O conjunto dos números reais é:",
                            "options": [
                                "Os racionais juntos com os irracionais",
                                "Só os inteiros",
                                "Só os positivos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um número irracional?",
                            "options": ["π", "0,5", "−4"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "√50 está entre dois números naturais "
                                 "seguidos. Qual é o menor deles?",
                            "a": "7",
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Radiciação",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Quanto é ∛27?",
                            "a": "3",
                        },
                        {
                            "t": "input",
                            "q": "Quanto é ∛(−8)?",
                            "a": "-2",
                        },
                        {
                            "t": "input",
                            "q": "Um cubo tem 125 centímetros cúbicos de "
                                 "volume. Quanto mede a aresta, em "
                                 "centímetros?",
                            "a": "5",
                        },
                        {
                            "t": "choice",
                            "q": "A potência 8 elevado a um terço é o "
                                 "mesmo que:",
                            "options": ["∛8, que dá 2", "8 a dividir por 3", "8³"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Passando o factor para fora do radical, "
                                 "√12 fica:",
                            "options": ["2√3", "3√2", "6√2"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Operações com radicais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Quanto é 2√3 + 5√3?",
                            "options": ["7√3", "7√6", "10√3"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Quanto é √4 × √9?",
                            "a": "6",
                        },
                        {
                            "t": "input",
                            "q": "Quanto é √50 a dividir por √2?",
                            "a": "5",
                        },
                        {
                            "t": "input",
                            "q": "Quanto é (√7)²?",
                            "a": "7",
                        },
                        {
                            "t": "choice",
                            "q": "Racionalizar o denominador de 1 sobre "
                                 "√2 dá:",
                            "options": ["√2 sobre 2", "2 sobre √2", "√2"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # II  Algebra (1)
        # ================================================================
        {
            "id": "u2",
            "titulo": "Álgebra (1)",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Inequações lineares",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Qual é o maior número natural que "
                                 "satisfaz 2x + 1 < 9?",
                            "a": "3",
                        },
                        {
                            "t": "input",
                            "q": "Qual é o menor número natural que "
                                 "satisfaz 3x − 5 > 7?",
                            "a": "5",
                        },
                        {
                            "t": "choice",
                            "q": "Ao multiplicar os dois membros de uma "
                                 "inequação por um número negativo:",
                            "options": [
                                "O sinal da desigualdade inverte-se",
                                "O sinal fica igual",
                                "A inequação deixa de ter solução",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A solução de x − 2 ≥ 1, em intervalo, é:",
                            "options": ["[3, +∞[", "]−∞, 3]", "[1, 3]"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na recta graduada, a solução de x < 4 "
                                 "marca-se com:",
                            "options": [
                                "Bola aberta no 4 e traço para a esquerda",
                                "Bola fechada no 4 e traço para a direita",
                                "Só um ponto no 4",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Sistemas de inequações",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Quantos números inteiros satisfazem ao "
                                 "mesmo tempo x > 1 e x < 5?",
                            "a": "3",
                        },
                        {
                            "t": "choice",
                            "q": "A solução de um sistema de duas "
                                 "inequações é:",
                            "options": [
                                "A intersecção das soluções das duas",
                                "A reunião das soluções das duas",
                                "A solução da primeira",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O sistema x > 3 e x < 1 tem solução:",
                            "options": [
                                "Nenhuma: é impossível",
                                "Todos os números",
                                "x = 2",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um quarto rectangular tem o comprimento "
                                 "1 metro maior que a largura e o "
                                 "perímetro inferior a 22 metros. Qual é a "
                                 "maior largura inteira possível, em "
                                 "metros?",
                            "a": "4",
                        },
                        {
                            "t": "choice",
                            "q": "A solução de x ≥ −1 e x ≤ 2, em "
                                 "intervalo, é:",
                            "options": ["[−1, 2]", "]−1, 2[", "[2, +∞["],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # III  Geometria (1)
        # ================================================================
        {
            "id": "u3",
            "titulo": "Geometria (1)",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Razões, proporções e homotetia",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Na proporção 3 está para 4 assim como 9 "
                                 "está para x, quanto vale x?",
                            "a": "12",
                        },
                        {
                            "t": "input",
                            "q": "Uma homotetia de razão 3 transforma um "
                                 "segmento de 4 centímetros num segmento "
                                 "de quantos centímetros?",
                            "a": "12",
                        },
                        {
                            "t": "choice",
                            "q": "Uma homotetia de razão entre 0 e 1:",
                            "options": ["Reduz a figura", "Amplia a figura", "Roda a figura"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um quadrado de lado 2 é ampliado com "
                                 "razão 3. Qual é a área do quadrado "
                                 "ampliado?",
                            "a": "36",
                        },
                        {
                            "t": "choice",
                            "q": "Numa ampliação, os ângulos da figura:",
                            "options": [
                                "Ficam iguais",
                                "Ficam maiores",
                                "Ficam menores",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Semelhança de triângulos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Dois triângulos são semelhantes quando:",
                            "options": [
                                "Têm os ângulos iguais e os lados "
                                "proporcionais",
                                "Têm a mesma área",
                                "Têm o mesmo perímetro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada critério de semelhança ao que "
                                 "ele exige.",
                            "pairs": [
                                ["Lado-lado-lado", "Os três lados proporcionais"],
                                ["Ângulo-ângulo", "Dois ângulos iguais"],
                                ["Lado-ângulo-lado", "Dois lados proporcionais e o ângulo entre eles igual"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Dois triângulos são semelhantes com "
                                 "razão 2. Um lado do primeiro mede 5. "
                                 "Quanto mede o lado correspondente do "
                                 "segundo?",
                            "a": "10",
                        },
                        {
                            "t": "input",
                            "q": "Dois triângulos semelhantes têm razão "
                                 "3. Se o perímetro do primeiro é 10, qual "
                                 "é o perímetro do segundo?",
                            "a": "30",
                        },
                        {
                            "t": "input",
                            "q": "Dois triângulos semelhantes têm razão "
                                 "2. Se a área do primeiro é 6, qual é a "
                                 "área do segundo?",
                            "a": "24",
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Thales e Pitágoras",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O teorema de Thales diz que rectas "
                                 "paralelas cortadas por duas secantes:",
                            "options": [
                                "Determinam segmentos proporcionais",
                                "Determinam segmentos iguais",
                                "Nunca se cortam",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um poste de 2 metros faz uma sombra de "
                                 "3 metros. À mesma hora, uma árvore faz "
                                 "uma sombra de 12 metros. Quantos metros "
                                 "tem a árvore?",
                            "a": "8",
                        },
                        {
                            "t": "input",
                            "q": "Num triângulo rectângulo os catetos "
                                 "medem 6 e 8. Quanto mede a hipotenusa?",
                            "a": "10",
                        },
                        {
                            "t": "input",
                            "q": "Num triângulo rectângulo a hipotenusa "
                                 "mede 13 e um cateto mede 5. Quanto mede "
                                 "o outro cateto?",
                            "a": "12",
                        },
                        {
                            "t": "choice",
                            "q": "Um triângulo de lados 3, 4 e 5 é:",
                            "options": [
                                "Rectângulo, porque 9 mais 16 é 25",
                                "Equilátero",
                                "Impossível",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # IV  Algebra (2)
        # ================================================================
        {
            "id": "u4",
            "titulo": "Álgebra (2)",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Polinómios",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Qual é o grau do polinómio 2x³ + x² − "
                                 "5?",
                            "a": "3",
                        },
                        {
                            "t": "choice",
                            "q": "Quanto é (3x + 2) + (2x − 5)?",
                            "options": ["5x − 3", "5x + 7", "x − 3"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quanto é 2x × (x + 3)?",
                            "options": ["2x² + 6x", "2x² + 3", "2x + 6x"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quanto é (x + 2) × (x + 3)?",
                            "options": ["x² + 5x + 6", "x² + 6", "x² + 5x"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Qual é o valor numérico de x² + 3x − 1 "
                                 "para x = 2?",
                            "a": "9",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Produtos notáveis e factorização",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Quanto é (x + 3)²?",
                            "options": ["x² + 6x + 9", "x² + 9", "x² + 3x + 9"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quanto é (x − 2)²?",
                            "options": ["x² − 4x + 4", "x² − 4", "x² + 4x + 4"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quanto é (x + 5) × (x − 5)?",
                            "options": ["x² − 25", "x² + 25", "x² − 10x + 25"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Pondo o factor comum em evidência, "
                                 "3x² + 6x fica:",
                            "options": ["3x(x + 2)", "3(x + 2)", "x(3x + 6x)"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Factorizando, x² − 9 fica:",
                            "options": [
                                "(x + 3)(x − 3)",
                                "(x − 3)²",
                                "(x + 9)(x − 1)",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Equações quadráticas incompletas",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Resolve x² − 16 = 0. Qual é a raiz "
                                 "positiva?",
                            "a": "4",
                        },
                        {
                            "t": "input",
                            "q": "Resolve x² − 5x = 0. Qual é a raiz "
                                 "diferente de zero?",
                            "a": "5",
                        },
                        {
                            "t": "choice",
                            "q": "A lei do anulamento do produto diz que "
                                 "se a × b = 0, então:",
                            "options": [
                                "a = 0 ou b = 0",
                                "a = 0 e b = 0",
                                "a = b",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A equação x² + 4 = 0:",
                            "options": [
                                "Não tem solução real: nenhum quadrado é "
                                "negativo",
                                "Tem solução x = 2",
                                "Tem solução x = −2",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Quantas soluções tem a equação x² = 0?",
                            "a": "1",
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Equações quadráticas completas",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Na equação x² − 5x + 6 = 0, quanto vale "
                                 "o discriminante, b² − 4ac?",
                            "a": "1",
                        },
                        {
                            "t": "input",
                            "q": "Resolve x² − 5x + 6 = 0. Qual é a maior "
                                 "raiz?",
                            "a": "3",
                        },
                        {
                            "t": "input",
                            "q": "As raízes de x² − 7x + 10 = 0 são 2 e "
                                 "5. Quanto vale a soma das raízes?",
                            "a": "7",
                        },
                        {
                            "t": "choice",
                            "q": "Se o discriminante é negativo, a equação "
                                 "quadrática:",
                            "options": [
                                "Não tem raízes reais",
                                "Tem duas raízes iguais",
                                "Tem duas raízes diferentes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "A área de um quadrado mais o triplo do "
                                 "seu lado é 28. Quanto mede o lado?",
                            "a": "4",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # V  Funcoes
        # ================================================================
        {
            "id": "u5",
            "titulo": "Funções",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A função quadrática",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O gráfico de uma função quadrática é:",
                            "options": ["Uma parábola", "Uma recta", "Uma circunferência"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Sendo f(x) = 2x², quanto vale f(3)?",
                            "a": "18",
                        },
                        {
                            "t": "choice",
                            "q": "Em y = ax², se a é negativo a parábola "
                                 "tem a concavidade:",
                            "options": [
                                "Voltada para baixo",
                                "Voltada para cima",
                                "Para a direita",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O vértice da parábola y = x² é:",
                            "options": ["A origem, (0, 0)", "O ponto (1, 1)", "O ponto (0, 1)"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O eixo de simetria de y = 3x² é:",
                            "options": [
                                "O eixo das ordenadas, x = 0",
                                "O eixo das abcissas, y = 0",
                                "A recta y = x",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Vértice, zeros e translações",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "A parábola y = x² − 9 corta o eixo das "
                                 "abcissas em dois pontos. Qual é a "
                                 "abcissa positiva?",
                            "a": "3",
                        },
                        {
                            "t": "choice",
                            "q": "O gráfico de y = x² + 2 é o de y = x²:",
                            "options": [
                                "Subido 2 unidades",
                                "Descido 2 unidades",
                                "Deslocado 2 para a direita",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O vértice da parábola y = (x − 4)² + 1 "
                                 "é:",
                            "options": ["(4, 1)", "(−4, 1)", "(1, 4)"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "A função y = x² − 4x tem dois zeros. "
                                 "Qual é o zero diferente de 0?",
                            "a": "4",
                        },
                        {
                            "t": "choice",
                            "q": "Se a parábola tem a concavidade para "
                                 "cima, o vértice é:",
                            "options": [
                                "O mínimo da função",
                                "O máximo da função",
                                "Um zero da função",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # VI  Algebra (3)
        # ================================================================
        {
            "id": "u6",
            "titulo": "Álgebra (3)",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Inequações quadráticas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Para resolver x² − 4 < 0 começa-se por:",
                            "options": [
                                "Achar as raízes de x² − 4 = 0",
                                "Dividir tudo por x",
                                "Passar o 4 para o outro lado e esquecer "
                                "o quadrado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A solução de x² − 4 < 0 é:",
                            "options": ["]−2, 2[", "]2, +∞[", "]−∞, −2["],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A solução de x² − 4 > 0 é:",
                            "options": [
                                "x < −2 ou x > 2",
                                "−2 < x < 2",
                                "Só x > 2",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Quantos números inteiros satisfazem "
                                 "x² − 9 ≤ 0?",
                            "a": "7",
                        },
                        {
                            "t": "choice",
                            "q": "Na resolução gráfica de uma inequação "
                                 "quadrática, olha-se para onde a "
                                 "parábola está:",
                            "options": [
                                "Acima ou abaixo do eixo das abcissas",
                                "À esquerda do eixo das ordenadas",
                                "Mais perto da origem",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # VII  Organizacao e tratamento de dados
        # ================================================================
        {
            "id": "u7",
            "titulo": "Organização e tratamento de dados",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "População, amostra e frequências",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Para saber a altura média dos alunos da "
                                 "escola mediram-se 40 alunos. Liga cada "
                                 "coisa ao seu nome.",
                            "pairs": [
                                ["Todos os alunos da escola", "População"],
                                ["Os 40 alunos medidos", "Amostra"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Numa turma de 40 alunos, 10 têm 14 "
                                 "anos. Qual é a frequência relativa "
                                 "percentual dos que têm 14 anos?",
                            "a": "25",
                        },
                        {
                            "t": "input",
                            "q": "As frequências absolutas são 5, 8 e 7. "
                                 "Qual é a frequência acumulada até à "
                                 "segunda classe?",
                            "a": "13",
                        },
                        {
                            "t": "input",
                            "q": "Num gráfico circular, uma fatia de 25 "
                                 "por cento tem quantos graus?",
                            "a": "90",
                        },
                        {
                            "t": "choice",
                            "q": "A idade é uma variável:",
                            "options": ["Quantitativa", "Qualitativa", "Sem valor"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Média, moda e mediana",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Qual é a média de 12, 14 e 16?",
                            "a": "14",
                        },
                        {
                            "t": "input",
                            "q": "Qual é a moda de 3, 5, 5, 7, 9?",
                            "a": "5",
                        },
                        {
                            "t": "input",
                            "q": "Qual é a mediana de 4, 9, 2, 7, 5?",
                            "a": "5",
                        },
                        {
                            "t": "input",
                            "q": "Qual é a mediana de 2, 4, 6, 8?",
                            "a": "5",
                        },
                        {
                            "t": "input",
                            "q": "Um aluno teve 10 em três testes e 14 "
                                 "num quarto. Qual é a média dos quatro?",
                            "a": "11",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # VIII  Geometria (2)
        # ================================================================
        {
            "id": "u8",
            "titulo": "Geometria (2)",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Poliedros e prismas",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Um cubo tem 8 vértices e 6 faces. Pela "
                                 "relação de Euler, quantas arestas tem?",
                            "a": "12",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada poliedro ao seu número de "
                                 "faces.",
                            "pairs": [
                                ["Tetraedro", "4"],
                                ["Hexaedro", "6"],
                                ["Octaedro", "8"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Um prisma recto tem base rectangular de "
                                 "3 por 4 e altura 5. Qual é o volume?",
                            "a": "60",
                        },
                        {
                            "t": "input",
                            "q": "Um prisma recto tem base triangular de "
                                 "área 6 e altura 10. Qual é o volume?",
                            "a": "60",
                        },
                        {
                            "t": "input",
                            "q": "Um cubo tem aresta 3. Qual é a área "
                                 "total das suas faces?",
                            "a": "54",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Pirâmides",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Uma pirâmide quadrangular tem quantas "
                                 "faces, contando a base?",
                            "a": "5",
                        },
                        {
                            "t": "input",
                            "q": "Uma pirâmide tem base quadrada de lado 6 "
                                 "e altura 5. Qual é o volume?",
                            "a": "60",
                        },
                        {
                            "t": "choice",
                            "q": "O volume da pirâmide é:",
                            "options": [
                                "Um terço do volume do prisma com a mesma "
                                "base e altura",
                                "O dobro do volume do prisma",
                                "Igual ao volume do prisma",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma pirâmide triangular tem quantos "
                                 "vértices?",
                            "a": "4",
                        },
                        {
                            "t": "input",
                            "q": "Um prisma e uma pirâmide têm a mesma "
                                 "base e a mesma altura. O prisma tem "
                                 "volume 90. Qual é o volume da pirâmide?",
                            "a": "30",
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Cilindro, cone e esfera",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada sólido de revolução à figura "
                                 "que o gera ao rodar.",
                            "pairs": [
                                ["Cilindro", "Rectângulo"],
                                ["Cone", "Triângulo rectângulo"],
                                ["Esfera", "Semicírculo"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Um cilindro tem raio 2 e altura 5. "
                                 "Tomando π igual a 3, qual é o volume?",
                            "a": "60",
                        },
                        {
                            "t": "input",
                            "q": "Um cone tem raio 3 e altura 4. Tomando "
                                 "π igual a 3, qual é o volume?",
                            "a": "36",
                        },
                        {
                            "t": "input",
                            "q": "Uma esfera tem raio 3. Tomando π igual "
                                 "a 3, qual é o volume?",
                            "a": "108",
                        },
                        {
                            "t": "input",
                            "q": "Um cilindro tem raio 1 e altura 10. "
                                 "Tomando π igual a 3, qual é a área "
                                 "lateral?",
                            "a": "60",
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

    # A seguir ao ultimo curso do secundario que ja la esteja: e o primeiro
    # da 9a, por isso entra depois do ultimo da 8a.
    onde = max(i for i, c in enumerate(dados["cursos"])
               if c["classe"] in ("8ª classe", "9ª classe")) + 1
    dados["cursos"].insert(onde, CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta as entradas ao tools/materia_texto.py "
          "e corre python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
