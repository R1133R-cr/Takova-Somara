# -*- coding: utf-8 -*-
"""O curso de Matematica da 8a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Matematica -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, pp. 46-81.
     Guardado em Documents\\planos da 5a classe\\Livros\\Programas INDE 1o
     Ciclo\\matematica.pdf (texto em matematica.txt, via pdftotext).

Programa e nao livro do aluno. Fica dito no campo `fonte`, como na 7a.

As nove unidades tematicas, tal como o INDE as ordena
-----------------------------------------------------
    1o trimestre   I    Numeros e operacoes (1)   conjuntos, racionais
                   II   Funcoes (1)               coordenadas, funcao linear
                   III  Numeros e operacoes (2)   numeros reais
    2o trimestre   IV   Algebra (1)               inequacoes lineares
                   V    Geometria (1)             circunferencia e circulo
                   VI   Algebra (2)               monomios, sistemas
    3o trimestre   VII  Geometria (2)             congruencia, Pitagoras,
                                                  quadrilateros
                   VIII Organizacao e tratamento  estatistica
                        de dados
                   IX   Geometria (3)             movimentos no plano

Nove unidades, vinte aulas. A 8a e mais pesada do que a 7a -- doze
capitulos contra onze -- e a Algebra entra a serio: monomios, sistemas de
equacoes, inequacoes. E a classe em que a Matematica deixa de ser contas
e passa a ser letras.

O que esta classe obrigou a mexer na app
----------------------------------------
Simbolos que a 7a nao tinha e que a voz comia ou lia mal: o expoente
(x², 2³), a raiz quadrada (√), o pi (π), o conjunto dos reais (ℝ) e a
notacao de funcao (f(x)). Ver o tools/pronuncia.py.

Correr a partir de somara-flutter/:
    python tools/conteudo_mat8c.py            # so mostra
    python tools/conteudo_mat8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Matemática — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, pp. 46-81. As nove "
    "unidades temáticas e os conteúdos são do programa; os exercícios "
    "foram escritos a partir deles, porque um programa de ensino não traz "
    "exercícios e não há livro do aluno da 8ª classe publicado."
)

CURSO = {
    "id": "mat-8c",
    "disciplina": "Matemática",
    "classe": "8ª classe",
    "tag": "MAT",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # Unidade Tematica I: Numeros e operacoes (1)
        # INDE: 1. Introducao a teoria de conjuntos (1.1-1.2)
        #       2. Numeros racionais (2.1-2.2)
        # ================================================================
        {
            "id": "u1",
            "titulo": "Números e operações (1)",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Subconjuntos e inclusão",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A = {1, 2} e B = {1, 2, 3, 4}. Qual é a "
                                 "afirmação certa?",
                            "options": ["A ⊂ B", "B ⊂ A", "A = B"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«B contém A» escreve-se:",
                            "options": ["B ⊃ A", "B ∈ A", "B ⊂ A"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Dois conjuntos são iguais quando:",
                            "options": [
                                "Têm exactamente os mesmos elementos",
                                "Têm o mesmo número de elementos",
                                "Um está contido no outro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Quantos subconjuntos com dois elementos tem "
                                 "o conjunto {a, b, c}?",
                            "a": "3",
                        },
                        {
                            "t": "choice",
                            "q": "O conjunto universal é:",
                            "options": [
                                "O conjunto de todos os elementos em estudo",
                                "O conjunto sem elementos",
                                "O maior subconjunto de A",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Operações com conjuntos",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "A = {2, 4, 6} e B = {4, 6, 8}. "
                                 "Quantos elementos tem A ∪ B?",
                            "a": "4",
                        },
                        {
                            "t": "input",
                            "q": "A = {2, 4, 6} e B = {4, 6, 8}. "
                                 "Quantos elementos tem A ∩ B?",
                            "a": "2",
                        },
                        {
                            "t": "choice",
                            "q": "Um conjunto finito é um conjunto:",
                            "options": [
                                "Cujos elementos se podem contar até ao fim",
                                "Que tem menos de dez elementos",
                                "Que não tem elementos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Se A ∩ B = ∅, os conjuntos A e B dizem-se:",
                            "options": ["Disjuntos", "Iguais", "Universais"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Os números racionais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um número racional é um número que se pode "
                                 "escrever como:",
                            "options": [
                                "Uma fracção de dois inteiros, com "
                                "denominador diferente de zero",
                                "Um número natural",
                                "Uma dízima infinita não periódica",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas relações entre conjuntos "
                                 "numéricos está certa?",
                            "options": ["ℕ ⊂ ℤ ⊂ ℚ", "ℚ ⊂ ℤ ⊂ ℕ", "ℤ ⊂ ℕ ⊂ ℚ"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes números é menor?",
                            "options": ["−3/4", "−1/4", "1/2"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na recta numérica, −1/2 fica:",
                            "options": [
                                "Entre −1 e 0",
                                "Entre 0 e 1",
                                "À direita do 1",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Qual é o módulo de −7/7?",
                            "a": "1",
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Operar com racionais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Quanto é −1/2 + 3/4?",
                            "options": ["1/4", "−1/4", "2/6"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quanto é (−2/3) × (3/4)?",
                            "options": ["−1/2", "1/2", "−6/7"],
                            "a": 0,
                        },
                        {"t": "input", "q": "Calcula: (−3)²", "a": "9"},
                        {"t": "input", "q": "Calcula: √49", "a": "7"},
                        {
                            "t": "choice",
                            "q": "Quanto é (1/2)²?",
                            "options": ["1/4", "1/2", "2/4"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica II: Funcoes (1)
        # INDE: 3. Funcoes lineares (3.1-3.2)
        # ================================================================
        {
            "id": "u2",
            "titulo": "Funções (1)",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Coordenadas e proporcionalidade",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "No ponto (3, −2), o número 3 é:",
                            "options": [
                                "A abcissa, no eixo horizontal",
                                "A ordenada, no eixo vertical",
                                "A origem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em que quadrante fica o ponto (−2, 5)?",
                            "options": ["No segundo", "No primeiro", "No quarto"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Se y é directamente proporcional a x e "
                                 "y = 12 quando x = 4, qual é a constante de "
                                 "proporcionalidade?",
                            "a": "3",
                        },
                        {
                            "t": "input",
                            "q": "Duas grandezas são inversamente "
                                 "proporcionais e x × y = 24. "
                                 "Se x = 6, quanto vale y?",
                            "a": "4",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O que é uma função",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma correspondência é uma função quando:",
                            "options": [
                                "A cada objecto corresponde uma só imagem",
                                "Cada imagem tem vários objectos",
                                "Os dois conjuntos são iguais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Sendo f(x) = 2x + 1, quanto vale f(3)?",
                            "a": "7",
                        },
                        {
                            "t": "input",
                            "q": "Sendo f(x) = 5 − x, quanto vale f(8)?",
                            "a": "-3",
                        },
                        {
                            "t": "choice",
                            "q": "Em y = 3x, a variável independente é:",
                            "options": ["x", "y", "3"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma aplicação em que objectos diferentes "
                                 "têm sempre imagens diferentes diz-se:",
                            "options": ["Injectiva", "Sobrejectiva", "Constante"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "A função linear e o seu gráfico",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O gráfico de uma função do tipo "
                                 "y = ax + b é:",
                            "options": ["Uma recta", "Uma parábola", "Um círculo"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Qual é o zero da função f(x) = 2x − 8?",
                            "a": "4",
                        },
                        {
                            "t": "choice",
                            "q": "Em y = −2x + 5, o gráfico corta o eixo "
                                 "das ordenadas em:",
                            "options": ["5", "−2", "0"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Em y = ax + b, se a é negativo a recta:",
                            "options": [
                                "Desce da esquerda para a direita",
                                "Sobe da esquerda para a direita",
                                "É horizontal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma recta passa pela origem e pelo ponto "
                                 "(2, 6). Qual é o declive?",
                            "a": "3",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica III: Numeros e operacoes (2)
        # INDE: 4. Introducao de numeros reais (4.1-4.4)
        # ================================================================
        {
            "id": "u3",
            "titulo": "Números reais",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Irracionais e reais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Qual destes números é irracional?",
                            "options": ["√2", "√9", "0,5"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um número irracional é uma dízima:",
                            "options": [
                                "Infinita e não periódica",
                                "Infinita e periódica",
                                "Finita",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O conjunto ℝ dos números reais junta:",
                            "options": [
                                "Os racionais e os irracionais",
                                "Só os inteiros e os naturais",
                                "Só os números positivos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual é a relação certa?",
                            "options": ["ℚ ⊂ ℝ", "ℝ ⊂ ℚ", "ℝ ⊂ ℤ"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O número π é:",
                            "options": [
                                "Irracional, aproximadamente 3,14",
                                "Racional, igual a 22/7",
                                "Inteiro",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica IV: Algebra (1)
        # INDE: 5. Inequacoes lineares (5.1-5.10)
        # ================================================================
        {
            "id": "u4",
            "titulo": "Inequações lineares",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Intervalos de números reais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Os números reais x tais que 2 ≤ x ≤ 5 "
                                 "formam o intervalo:",
                            "options": ["[2, 5]", "]2, 5[", "[2, 5["],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No intervalo ]0, 3], o número 0:",
                            "options": [
                                "Não pertence ao intervalo",
                                "Pertence ao intervalo",
                                "É o maior elemento",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A intersecção de [1, 6] com [4, 9] é:",
                            "options": ["[4, 6]", "[1, 9]", "[6, 9]"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A reunião de [1, 3] com [3, 7] é:",
                            "options": ["[1, 7]", "[3, 3]", "[1, 3]"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Resolver inequações",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A solução de x + 3 > 7 é:",
                            "options": ["x > 4", "x > 10", "x < 4"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A solução de 2x ≤ 10 é:",
                            "options": ["x ≤ 5", "x ≥ 5", "x ≤ 20"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao multiplicar os dois membros de uma "
                                 "inequação por um número negativo:",
                            "options": [
                                "O sentido da desigualdade inverte-se",
                                "O sentido mantém-se",
                                "A inequação fica sem solução",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A solução de −x < 3 é:",
                            "options": ["x > −3", "x < −3", "x < 3"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Qual é o menor número inteiro que verifica "
                                 "3x − 4 > 5?",
                            "a": "4",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica V: Geometria (1)
        # INDE: 6. Circunferencias e circulos (6.1-6.4)
        # ================================================================
        {
            "id": "u5",
            "titulo": "Circunferência e círculo",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Elementos e posições da recta",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma recta que toca a circunferência num só "
                                 "ponto chama-se:",
                            "options": ["Tangente", "Secante", "Exterior"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma recta que corta a circunferência em "
                                 "dois pontos chama-se:",
                            "options": ["Secante", "Tangente", "Diâmetro"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A maior corda de uma circunferência é:",
                            "options": ["O diâmetro", "O raio", "O arco"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A recta tangente e o raio no ponto de "
                                 "tangência formam um ângulo de:",
                            "options": ["90 graus", "45 graus", "180 graus"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Ângulos, perímetro e arcos",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Um ângulo ao centro mede 80 graus. "
                                 "Quantos graus mede o ângulo inscrito que "
                                 "abrange o mesmo arco?",
                            "a": "40",
                        },
                        {
                            "t": "input",
                            "q": "Uma circunferência completa tem quantos "
                                 "graus?",
                            "a": "360",
                        },
                        {
                            "t": "choice",
                            "q": "O perímetro de uma circunferência de raio r "
                                 "calcula-se com:",
                            "options": ["2 × π × r", "π × r²", "π × r"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma circunferência tem raio de 7 cm. "
                                 "Usando π = 22/7, quantos centímetros mede o "
                                 "perímetro?",
                            "a": "44",
                            "figura": {"forma": "circulo", "a": 7},
                        },
                        {
                            "t": "input",
                            "q": "Um arco corresponde a um ângulo ao centro "
                                 "de 90 graus numa circunferência de "
                                 "perímetro 40 cm. Quantos centímetros mede "
                                 "o arco?",
                            "a": "10",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica VI: Algebra (2)
        # INDE: 7. Monomios (7.1-7.7)
        #       8. Sistema de duas equacoes lineares a duas incognitas
        # ================================================================
        {
            "id": "u6",
            "titulo": "Álgebra (2)",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Monómios",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "No monómio 5x³, o coeficiente é:",
                            "options": ["5", "x", "3"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Qual é o grau do monómio 4x²y³?",
                            "a": "5",
                        },
                        {
                            "t": "choice",
                            "q": "Dois monómios são semelhantes quando:",
                            "options": [
                                "Têm a mesma parte literal",
                                "Têm o mesmo coeficiente",
                                "Têm o mesmo grau",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quanto é 3x + 5x?",
                            "options": ["8x", "8x²", "15x"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quanto é 2x × 3x?",
                            "options": ["6x²", "6x", "5x²"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Sistemas de duas equações",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um sistema de duas equações lineares a duas "
                                 "incógnitas tem por solução:",
                            "options": [
                                "Um par de valores que verifica as duas",
                                "Um valor só",
                                "Duas equações novas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Se x + y = 10 e x − y = 2, quanto vale x?",
                            "a": "6",
                        },
                        {
                            "t": "input",
                            "q": "Se x + y = 10 e x − y = 2, quanto vale y?",
                            "a": "4",
                        },
                        {
                            "t": "choice",
                            "q": "Um sistema em que as duas rectas são "
                                 "paralelas é:",
                            "options": [
                                "Impossível: não tem solução",
                                "Possível e determinado",
                                "Possível e indeterminado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Dois cadernos e uma caneta custam 70 "
                                 "meticais; um caderno e uma caneta custam 45. "
                                 "Quantos meticais custa um caderno?",
                            "a": "25",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica VII: Geometria (2)
        # INDE: 9. Congruencia de triangulos e teorema de Pitagoras
        #       10. Quadrilateros
        # ================================================================
        {
            "id": "u7",
            "titulo": "Geometria (2)",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Congruência de triângulos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Dois triângulos são congruentes quando:",
                            "options": [
                                "Têm os lados e os ângulos iguais, cada um "
                                "ao seu",
                                "Têm a mesma área",
                                "Têm um ângulo igual",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O critério lado-ângulo-lado exige:",
                            "options": [
                                "Dois lados iguais e o ângulo entre eles igual",
                                "Três ângulos iguais",
                                "Um lado e um ângulo iguais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada critério de congruência à sua "
                                 "sigla.",
                            "pairs": [
                                ["Lado-lado-lado", "LLL"],
                                ["Ângulo-lado-ângulo", "ALA"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Uma isometria é uma transformação que:",
                            "options": [
                                "Mantém as distâncias",
                                "Duplica as figuras",
                                "Muda os ângulos",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O teorema de Pitágoras",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O teorema de Pitágoras aplica-se a:",
                            "options": [
                                "Triângulos rectângulos",
                                "Todos os triângulos",
                                "Só a triângulos equiláteros",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Num triângulo rectângulo, o lado oposto ao "
                                 "ângulo recto chama-se:",
                            "options": ["Hipotenusa", "Cateto", "Altura"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Num triângulo rectângulo os catetos medem "
                                 "3 e 4. Quanto mede a hipotenusa?",
                            "a": "5",
                        },
                        {
                            "t": "input",
                            "q": "Num triângulo rectângulo a hipotenusa mede "
                                 "13 e um cateto mede 5. Quanto mede o outro "
                                 "cateto?",
                            "a": "12",
                        },
                        {
                            "t": "input",
                            "q": "Uma escada de 10 metros está encostada a "
                                 "uma parede, com o pé a 6 metros dela. "
                                 "A que altura, em metros, toca na parede?",
                            "a": "8",
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Quadriláteros",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Quanto vale a soma dos ângulos internos de "
                                 "um quadrilátero, em graus?",
                            "a": "360",
                        },
                        {
                            "t": "choice",
                            "q": "Um quadrilátero com os quatro lados iguais "
                                 "e os ângulos não todos rectos é um:",
                            "options": ["Losango", "Rectângulo", "Trapézio"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um paralelogramo tem:",
                            "options": [
                                "Os lados opostos paralelos e iguais",
                                "Só um par de lados paralelos",
                                "Os quatro ângulos rectos, sempre",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Três ângulos de um quadrilátero medem 90, "
                                 "90 e 110 graus. Quantos graus mede o "
                                 "quarto?",
                            "a": "70",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica VIII: Organizacao e tratamento de dados
        # INDE: 11. Estatistica (11.1-11.7)
        # ================================================================
        {
            "id": "u8",
            "titulo": "Estatística",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "População, tabelas e médias",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Numa sondagem a 50 alunos de uma escola com "
                                 "800, os 50 são:",
                            "options": ["A amostra", "A população", "A moda"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "As notas de um aluno foram 12, 14, 16 e 18. "
                                 "Qual é a média?",
                            "a": "15",
                        },
                        {
                            "t": "input",
                            "q": "Numa turma, 5 alunos têm 12 anos, 15 têm "
                                 "13 e 8 têm 14. Qual é a moda das idades?",
                            "a": "13",
                        },
                        {
                            "t": "input",
                            "q": "Qual é a mediana de 3, 9, 4, 7 e 5?",
                            "a": "5",
                        },
                        {
                            "t": "choice",
                            "q": "A frequência absoluta de um valor é:",
                            "options": [
                                "O número de vezes que ele aparece",
                                "A sua percentagem no total",
                                "O maior valor observado",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica IX: Geometria (3)
        # INDE: 12. Movimentos no plano (12.1-12.11)
        # ================================================================
        {
            "id": "u9",
            "titulo": "Movimentos no plano",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Translação, reflexão e rotação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Deslocar uma figura sem a rodar nem a "
                                 "virar é uma:",
                            "options": ["Translação", "Rotação", "Reflexão"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma translação fica definida por:",
                            "options": ["Um vector", "Um ângulo", "Um eixo"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Quantos eixos de simetria tem um quadrado?",
                            "a": "4",
                        },
                        {
                            "t": "choice",
                            "q": "A reflexão de um ponto num eixo dá um ponto:",
                            "options": [
                                "À mesma distância do eixo, do outro lado",
                                "Mais afastado do eixo",
                                "Em cima do eixo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma rotação de 90 graus repetida quantas "
                                 "vezes dá uma volta completa?",
                            "a": "4",
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
            print(f"       {n['id']}  {n['titulo']:<38}"
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

    # No fim de todos: a 8a vem depois da 7a.
    dados["cursos"].append(CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta as entradas ao tools/materia_texto.py "
          "e corre python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
