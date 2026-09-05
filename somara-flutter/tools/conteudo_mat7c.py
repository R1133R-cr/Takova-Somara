# -*- coding: utf-8 -*-
"""O curso de Matematica da 7a classe.

De onde vem, e porque e diferente de todos os outros
----------------------------------------------------
Dos vinte e um cursos que a app tem, vinte saem de um LIVRO ESCOLAR. Este
sai de um PROGRAMA DE ENSINO:

    "Programa de Ensino da Disciplina de Matematica -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, 115 paginas.
     Descarregado do educador.mozestuda.com.

A diferenca conta e fica dita. Um programa traz os objectivos, os
conteudos numerados, os resultados de aprendizagem e a carga horaria; NAO
traz exercicios nem exemplos resolvidos. As sete unidades e os conteudos
de cada uma sao do INDE, palavra por palavra. As perguntas foram escritas
a partir dessa lista -- nao foram adaptadas de um livro, porque nao ha
livro do aluno da 7a classe publicado que se tenha encontrado.

Isso fica marcado no proprio content.json, no campo `fonte`, como ja
acontece com a Educacao Visual da 4a classe. Quem for a procura sabe o que
esta a ler.

Porque e que a 7a classe nao e primario
---------------------------------------
Pela Lei no 18/2018 o Ensino Primario sao seis classes. A 7a passou para o
1o ciclo do Ensino Secundario Geral. Continua dentro dos NOVE anos de
escolaridade obrigatoria, e e por isso que a app a cobre -- mas e outro
curriculo, de outro instituto, e para outra idade.

As sete unidades tematicas, tal como o INDE as ordena
-----------------------------------------------------
    1o trimestre   I   Numeros e operacoes (1)   conjuntos, inteiros
                   II  Geometria (1)             poligonos, circunferencia
                   III Numeros e operacoes (2)   racionais
    2o trimestre   IV  Geometria (2)             grandezas e medidas
                   V   Algebra                   equacoes
                   VI  Numeros e operacoes (3)   percentagens
    3o trimestre   VII Relacoes Proporcionais    razoes, escala, proporc.

Duas coisas que este curso obrigou a mexer na app
-------------------------------------------------
1. Os simbolos de conjuntos. A voz comia-os em silencio -- "5 ∈ A" saia
   "cinco a", uma frase que ate parece uma frase e esta errada. Ver o
   CONJUNTOS no tools/pronuncia.py.
2. As respostas negativas. O teclado so tinha algarismos, e a app decidia
   mostrar o teclado proprio com `^\\d+$`: um "-5" caia no teclado de
   letras do sistema. Ganhou uma tecla de sinal, que so aparece onde a
   resposta certa e negativa.

Correr a partir de somara-flutter/:
    python tools/conteudo_mat7c.py            # so mostra
    python tools/conteudo_mat7c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Matemática — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024. As unidades e os "
    "conteúdos são do programa; os exercícios foram escritos a partir "
    "deles, porque um programa de ensino não traz exercícios e não há "
    "livro do aluno da 7ª classe publicado."
)

CURSO = {
    "id": "mat-7c",
    "disciplina": "Matemática",
    "classe": "7ª classe",
    "tag": "MAT",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # Unidade Tematica I: Numeros e operacoes (1)
        # INDE: 1. Introducao a teoria de conjuntos (1.1-1.8)
        #       2. Conjunto dos numeros inteiros relativos (2.1-2.3)
        # ================================================================
        {
            "id": "u1",
            "titulo": "Números e operações (1)",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Conjuntos e elementos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um conjunto é:",
                            "options": [
                                "Uma colecção de objectos bem definidos",
                                "Um número muito grande",
                                "Uma conta por resolver",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "O conjunto A = {2, 4, 6, 8, 10}. "
                                 "Quantos elementos tem? Esse número chama-se "
                                 "cardinal de A.",
                            "a": "5",
                        },
                        {
                            "t": "choice",
                            "q": "Sendo B = {a, e, i, o, u}, o símbolo ∈ em "
                                 "«e ∈ B» quer dizer:",
                            "options": [
                                "e pertence a B",
                                "e não pertence a B",
                                "e está contido em B",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Escrever C = {1, 3, 5, 7, 9} é definir o "
                                 "conjunto:",
                            "options": [
                                "Por extensão, nomeando os elementos",
                                "Em compreensão, dizendo a regra",
                                "Por cardinal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada símbolo ao que ele diz.",
                            "pairs": [
                                ["∈", "Pertence a"],
                                ["∉", "Não pertence a"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Reunião e intersecção",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«A ⊂ B» lê-se:",
                            "options": [
                                "A está contido em B",
                                "A pertence a B",
                                "A é igual a B",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "A = {1, 2, 3} e B = {3, 4}. "
                                 "Quantos elementos tem A ∪ B?",
                            "a": "4",
                        },
                        {
                            "t": "input",
                            "q": "A = {1, 2, 3} e B = {3, 4}. "
                                 "Quantos elementos tem A ∩ B?",
                            "a": "1",
                        },
                        {
                            "t": "choice",
                            "q": "Dois conjuntos que não têm nenhum elemento "
                                 "em comum dizem-se:",
                            "options": [
                                "Disjuntos",
                                "Iguais",
                                "Singulares",
                            ],
                            "a": 0,
                        },
                        {
                            # Sem o símbolo no enunciado de propósito: a voz
                            # diz "∅" como "conjunto vazio", e a pergunta
                            # saía a dizer o mesmo duas vezes seguidas. O
                            # símbolo aparece nas opções, que são para ler.
                            "t": "input",
                            "q": "Quantos elementos tem o conjunto vazio?",
                            "a": "0",
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes símbolos representa o conjunto "
                                 "vazio?",
                            "options": ["∅", "∩", "∪"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Números inteiros relativos",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Qual é o simétrico de 7?",
                            "a": "-7",
                        },
                        {
                            "t": "input",
                            "q": "Qual é o módulo, ou valor absoluto, de −9?",
                            "a": "9",
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes números é menor?",
                            "options": ["−8", "−5", "−1"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Em Lichinga, a temperatura era de 3 graus e "
                                 "desceu 8 graus durante a noite. "
                                 "Que temperatura ficou?",
                            "a": "-5",
                        },
                        {
                            "t": "choice",
                            "q": "Na recta numérica, os números negativos "
                                 "ficam:",
                            "options": [
                                "À esquerda do zero",
                                "À direita do zero",
                                "Em cima do zero",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Operações com números inteiros",
                    "questoes": [
                        {"t": "input", "q": "Calcula: −12 + 7", "a": "-5"},
                        {"t": "input", "q": "Calcula: −8 − 5", "a": "-13"},
                        {"t": "input", "q": "Calcula: (−4) × 3", "a": "-12"},
                        {"t": "input", "q": "Calcula: (−20) : 4", "a": "-5"},
                        {
                            "t": "choice",
                            "q": "O produto de dois números negativos é:",
                            "options": [
                                "Positivo",
                                "Negativo",
                                "Sempre zero",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica II: Geometria (1)
        # INDE: 3. Introducao a geometria plana e espacial (3.2-3.5)
        # ================================================================
        {
            "id": "u2",
            "titulo": "Geometria (1)",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Polígonos e triângulos",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Quanto vale a soma das medidas dos ângulos "
                                 "internos de um triângulo, em graus?",
                            "a": "180",
                        },
                        {
                            "t": "choice",
                            "q": "Um triângulo com um ângulo recto chama-se:",
                            "options": [
                                "Rectângulo",
                                "Acutângulo",
                                "Obtusângulo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Quantos lados tem um hexágono?",
                            "a": "6",
                        },
                        {
                            "t": "choice",
                            "q": "O apótema de um polígono regular é a "
                                 "distância do centro:",
                            "options": [
                                "Ao meio de um lado",
                                "A um vértice",
                                "A outro polígono",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada polígono ao número de lados.",
                            "pairs": [
                                ["Pentágono", "5"],
                                ["Octógono", "8"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Circunferência, círculo e sólidos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A circunferência é a linha; o círculo é:",
                            "options": [
                                "A parte de dentro, com a linha",
                                "A mesma coisa",
                                "Só o centro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma circunferência tem 7 cm de raio. "
                                 "Quantos centímetros mede o diâmetro?",
                            "a": "14",
                            "figura": {"forma": "circulo", "a": 7},
                        },
                        {
                            "t": "choice",
                            "q": "A corda de uma circunferência é o segmento "
                                 "que une:",
                            "options": [
                                "Dois pontos da circunferência",
                                "O centro a um ponto",
                                "Dois centros",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes sólidos não tem nenhuma face "
                                 "plana?",
                            "options": ["A esfera", "O cubo", "O prisma"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada elemento à sua descrição.",
                            "pairs": [
                                ["Raio", "Do centro à circunferência"],
                                ["Diâmetro", "Passa pelo centro, de lado a lado"],
                            ],
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica III: Numeros e operacoes (2)
        # INDE: 4. Introducao de Numeros Racionais (4.1-4.14)
        # ================================================================
        {
            "id": "u3",
            "titulo": "Números racionais",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Fracções e fracções equivalentes",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Na fracção 3/5, o número 5 chama-se:",
                            "options": ["Denominador", "Numerador", "Cardinal"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas fracções é equivalente a 1/2?",
                            "options": ["4/8", "2/5", "3/7"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A fracção 6/8, simplificada, fica:",
                            "options": ["3/4", "2/3", "6/4"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma fracção diz-se irredutível quando:",
                            "options": [
                                "Já não se pode simplificar mais",
                                "O numerador é maior",
                                "É maior do que 1",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Três amigos repartem 12 mangas em partes "
                                 "iguais. Quantas mangas leva cada um?",
                            "a": "4",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Comparar, somar e subtrair fracções",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Para somar 1/4 com 2/4, o que se faz?",
                            "options": [
                                "Somam-se os numeradores e mantém-se o "
                                "denominador",
                                "Somam-se os dois de cima e os dois de baixo",
                                "Multiplicam-se as fracções",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quanto é 1/4 + 2/4?",
                            "options": ["3/4", "3/8", "2/8"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual é maior: 2/3 ou 1/3?",
                            "options": ["2/3", "1/3", "São iguais"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para somar 1/2 com 1/3 é preciso primeiro:",
                            "options": [
                                "Reduzir as fracções ao mesmo denominador",
                                "Simplificar as duas",
                                "Trocar os numeradores",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Decimais e arredondamentos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A fracção 1/4, na forma decimal, é:",
                            "options": ["0,25", "0,14", "1,4"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O número 3,7 arredondado às unidades fica:",
                            "options": ["4", "3", "3,5"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma dízima periódica é um número decimal "
                                 "em que:",
                            "options": [
                                "Um grupo de algarismos se repete sem fim",
                                "Não há vírgula",
                                "Só há um algarismo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um caderno custa 25 meticais. "
                                 "Quanto custam 4 cadernos, em meticais?",
                            "a": "100",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica IV: Geometria (2)
        # INDE: 5. Grandezas e medidas (5.1 perimetro, 5.2 areas, 5.3 volume)
        # ================================================================
        {
            "id": "u4",
            "titulo": "Grandezas e medidas",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Perímetros",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Um rectângulo tem 8 cm de comprimento e "
                                 "5 cm de largura. Quantos centímetros mede o "
                                 "perímetro?",
                            "a": "26",
                            "figura": {"forma": "rectangulo", "a": 8, "b": 5},
                        },
                        {
                            "t": "input",
                            "q": "Um quadrado tem 9 cm de lado. "
                                 "Quantos centímetros mede o perímetro?",
                            "a": "36",
                            "figura": {"forma": "quadrado", "a": 9},
                        },
                        {
                            "t": "choice",
                            "q": "O perímetro de uma figura é:",
                            "options": [
                                "A medida do contorno",
                                "A medida da superfície",
                                "O espaço que ocupa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma machamba tem a forma de um triângulo "
                                 "com lados de 12 m, 15 m e 20 m. "
                                 "Quantos metros de cerca são precisos para a "
                                 "rodear?",
                            "a": "47",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Áreas e volumes",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Um trapézio tem base maior de 10 cm, base "
                                 "menor de 6 cm e altura de 4 cm. "
                                 "Quantos centímetros quadrados mede a área?",
                            "a": "32",
                            "figura": {"forma": "trapezio", "a": 10, "b": 6},
                        },
                        {
                            "t": "input",
                            "q": "Um losango tem diagonais de 12 cm e 5 cm. "
                                 "Quantos centímetros quadrados mede a área?",
                            "a": "30",
                            "figura": {"forma": "losango", "a": 12, "b": 5},
                        },
                        {
                            "t": "choice",
                            "q": "A área do círculo calcula-se com:",
                            "options": [
                                "π × r × r",
                                "2 × π × r",
                                "π × d × d",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Um prisma recto tem 20 centímetros "
                                 "quadrados de área da base e 6 cm de altura. "
                                 "Quantos centímetros cúbicos mede o volume?",
                            "a": "120",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica V: Algebra
        # INDE: 6. Equacoes (6.1-6.9)
        # ================================================================
        {
            "id": "u5",
            "titulo": "Álgebra",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O que é uma equação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma equação é uma igualdade que tem:",
                            "options": [
                                "Pelo menos uma incógnita",
                                "Só números",
                                "Sempre duas soluções",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na equação 2x + 3 = 11, o x chama-se:",
                            "options": ["Incógnita", "Solução", "Termo certo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O valor x = 4 é solução de x + 5 = 9?",
                            "options": [
                                "Sim, porque 4 + 5 = 9",
                                "Não, porque 4 é menor que 9",
                                "Só se x for negativo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Duas equações dizem-se equivalentes quando:",
                            "options": [
                                "Têm a mesma solução",
                                "Têm os mesmos números",
                                "São escritas da mesma maneira",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Resolver equações",
                    "questoes": [
                        {"t": "input", "q": "Resolve: x + 7 = 12", "a": "5"},
                        {"t": "input", "q": "Resolve: 3x = 21", "a": "7"},
                        {"t": "input", "q": "Resolve: 2x − 6 = 10", "a": "8"},
                        {"t": "input", "q": "Resolve: x : 4 = 5", "a": "20"},
                        {
                            "t": "input",
                            "q": "A Amina tem x meticais. Gastou 30 e ficou "
                                 "com 45. Quantos meticais tinha?",
                            "a": "75",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica VI: Numeros e operacoes (3)
        # INDE: 7. Percentagens (7.1-7.2)  8. Literacia financeira (8.1-8.2)
        # ================================================================
        {
            "id": "u6",
            "titulo": "Percentagens e dinheiro",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Percentagens",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Quanto é 25% de 80?",
                            "a": "20",
                        },
                        {
                            "t": "input",
                            "q": "Quanto é 10% de 350?",
                            "a": "35",
                        },
                        {
                            "t": "choice",
                            "q": "50% é o mesmo que a fracção:",
                            "options": ["1/2", "1/5", "5/10 de 10"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma camisola custa 400 meticais e tem 20% "
                                 "de desconto. Quantos meticais se poupam?",
                            "a": "80",
                        },
                        {
                            "t": "choice",
                            "q": "Num gráfico circular, o círculo inteiro "
                                 "representa:",
                            "options": ["100%", "50%", "10%"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # Unidade Tematica VII: Relacoes Proporcionais
        # INDE: 9. Razoes e proporcoes  10. Orientacao e localizacao no plano
        #       11. Proporcionalidade
        # ================================================================
        {
            "id": "u7",
            "titulo": "Relações proporcionais",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Razões e proporções",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A razão entre 6 e 3 é:",
                            "options": ["2", "9", "3"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Na proporção 3/4 = x/8, quanto vale x?",
                            "a": "6",
                        },
                        {
                            "t": "input",
                            "q": "Se 4 cadernos custam 100 meticais, quantos "
                                 "meticais custam 6 cadernos?",
                            "a": "150",
                        },
                        {
                            "t": "choice",
                            "q": "Numa proporção, os extremos são:",
                            "options": [
                                "O primeiro e o último termo",
                                "Os dois do meio",
                                "Os dois de cima",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Escala, coordenadas e proporcionalidade",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Num mapa à escala 1:100, 1 cm no papel "
                                 "corresponde a:",
                            "options": [
                                "100 cm na realidade",
                                "1 cm na realidade",
                                "10 cm na realidade",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No plano cartesiano, o ponto onde os dois "
                                 "eixos se cruzam chama-se:",
                            "options": ["Origem", "Vértice", "Extremo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Se ao dobrar uma grandeza a outra também "
                                 "dobra, elas são:",
                            "options": [
                                "Directamente proporcionais",
                                "Inversamente proporcionais",
                                "Independentes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quanto mais trabalhadores, menos tempo leva "
                                 "a obra. Estas grandezas são:",
                            "options": [
                                "Inversamente proporcionais",
                                "Directamente proporcionais",
                                "Iguais",
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

    # No fim de todos: a 7a classe vem depois da 6a, e e a primeira do
    # secundario. A barra de disciplinas do mapa filtra por classe, por isso
    # a ordem dentro da lista so tem de respeitar a classe.
    dados["cursos"].append(CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta as entradas ao tools/materia_texto.py "
          "e corre python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
