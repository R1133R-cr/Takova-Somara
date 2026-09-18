# -*- coding: utf-8 -*-
"""O curso de Quimica da 9a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Quimica -- Ensino Secundario --
     1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024, 9a classe,
     pp. 29-51. Guardado em Documents\\planos da 5a classe\\Livros\\
     Programas INDE 1o Ciclo\\quimica.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As sete unidades tematicas, pela ordem do programa
--------------------------------------------------
    I    Classes dos compostos inorganicos   oxidos; acidos e bases;
                                             indicadores e sais
    II   Estrutura atomica e Tabela          o atomo; a tabela e as suas
         Periodica                           regularidades
    III  Ligacao quimica                     ionica e covalente; metalica
                                             e os metais
    IV   Cloro e o grupo VIIA                halogeneos; redox e volume
                                             molar
    V    Enxofre e o grupo VIA               enxofre e compostos; cinetica
    VI   Nitrogenio e o grupo VA             azoto e amoniaco; fosforo,
                                             adubos e equilibrio quimico
    VII  Carbono e o grupo IVA               carbono e carvoes; dioxido de
                                             carbono, silicio e cimento

Sete unidades, quinze aulas.

As formulas ficam nas opcoes, como na 8a
----------------------------------------
Nos enunciados escreve-se o nome ("acido cloridrico", "amoniaco"); a
formula, quando faz falta, fica nas opcoes e nos pares. Os grupos da
tabela escrevem-se por extenso ("grupo dezassete") para a voz nao ler
"vê, i, i, a". As contas dao inteiros.

Correr a partir de somara-flutter/:
    python tools/conteudo_qui9c.py            # so mostra
    python tools/conteudo_qui9c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Química — Ensino Secundário, "
    "1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, 9ª classe, pp. 29-51. "
    "As sete unidades e os conteúdos são do programa; os exercícios foram "
    "escritos a partir deles, porque um programa de ensino não traz "
    "exercícios e não há livro do aluno da 9ª classe publicado."
)

CURSO = {
    "id": "qui-9c",
    "disciplina": "Química",
    "classe": "9ª classe",
    "tag": "QUI",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # I  Classes dos compostos inorganicos
        # ================================================================
        {
            "id": "u1",
            "titulo": "Classes dos compostos inorgânicos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Os óxidos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um óxido é um composto de:",
                            "options": [
                                "Oxigénio com outro elemento",
                                "Hidrogénio com um metal",
                                "Só oxigénio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada óxido à sua fórmula.",
                            "pairs": [
                                ["Óxido de cálcio", "CaO"],
                                ["Dióxido de enxofre", "SO₂"],
                                ["Óxido de magnésio", "MgO"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de óxido ao que dá com a "
                                 "água.",
                            "pairs": [
                                ["Óxido metálico, ou básico", "Uma base"],
                                ["Óxido ametálico, ou ácido", "Um ácido"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O óxido de cálcio, a cal viva, com água "
                                 "dá:",
                            "options": [
                                "Hidróxido de cálcio, uma base",
                                "Ácido sulfúrico",
                                "Sal de cozinha",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O dióxido de carbono é um óxido:",
                            "options": ["Ácido", "Básico", "Metálico"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Ácidos e bases",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Segundo Arrhenius, liga cada substância "
                                 "ao ião que liberta na água.",
                            "pairs": [
                                ["Ácido", "Ião hidrogénio"],
                                ["Base", "Ião hidroxilo"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada ácido ao seu tipo.",
                            "pairs": [
                                ["Ácido sulfúrico, com oxigénio", "Oxiácido"],
                                ["Ácido clorídrico, sem oxigénio", "Hidrácido"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada ácido ou base à sua fórmula.",
                            "pairs": [
                                ["Ácido clorídrico", "HCl"],
                                ["Ácido sulfúrico", "H₂SO₄"],
                                ["Hidróxido de sódio", "NaOH"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um ácido com uma base dá sal e água. "
                                 "Essa reacção chama-se:",
                            "options": ["Neutralização", "Combustão", "Decomposição"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os ácidos e as bases fortes:",
                            "options": [
                                "São corrosivos: nunca se provam nem se "
                                "tocam sem protecção",
                                "Podem provar-se para os distinguir",
                                "São inofensivos",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Indicadores e sais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um indicador ácido-base é uma substância "
                                 "que:",
                            "options": [
                                "Muda de cor conforme o meio é ácido ou "
                                "básico",
                                "Neutraliza os ácidos",
                                "Mede a temperatura",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada substância de casa ao seu "
                                 "carácter.",
                            "pairs": [
                                ["Sumo de limão e vinagre", "Ácido"],
                                ["Água de sabão e água de cinza", "Básico"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um indicador natural?",
                            "options": [
                                "O sumo de beterraba ou de flores de "
                                "buganvília",
                                "O sal",
                                "A água destilada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada sal à sua aplicação.",
                            "pairs": [
                                ["Cloreto de sódio", "Tempero e conservação dos alimentos"],
                                ["Carbonato de cálcio", "Cimento, cal e vidro"],
                                ["Nitrato de amónio", "Adubo"],
                                ["Sulfato de cálcio", "Giz e gesso"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Por lei, em Moçambique, junta-se iodo ao "
                                 "sal de cozinha para prevenir:",
                            "options": ["O bócio", "A malária", "A cárie"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # II  Estrutura atomica e Tabela Periodica
        # ================================================================
        {
            "id": "u2",
            "titulo": "Estrutura atómica e Tabela Periódica",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O átomo",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada partícula do átomo à sua "
                                 "carga.",
                            "pairs": [
                                ["Protão", "Positiva"],
                                ["Electrão", "Negativa"],
                                ["Neutrão", "Sem carga"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Um átomo tem número atómico 11 e número "
                                 "de massa 23. Quantos neutrões tem?",
                            "a": "12",
                        },
                        {
                            "t": "input",
                            "q": "Um átomo neutro de cloro tem 17 protões. "
                                 "Quantos electrões tem?",
                            "a": "17",
                        },
                        {
                            "t": "choice",
                            "q": "Isótopos são átomos do mesmo elemento "
                                 "com:",
                            "options": [
                                "O mesmo número de protões e diferente "
                                "número de neutrões",
                                "Diferente número de protões",
                                "Cargas diferentes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No modelo de Bohr, os electrões estão:",
                            "options": [
                                "Em níveis de energia à volta do núcleo",
                                "Dentro do núcleo",
                                "Parados ao acaso",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A Tabela Periódica",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Tabela Periódica ordena os elementos "
                                 "pelo número atómico, segundo a lei "
                                 "periódica de:",
                            "options": ["Mendeleev", "Lavoisier", "Newton"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada parte da Tabela ao que ela é.",
                            "pairs": [
                                ["Período", "Uma linha horizontal"],
                                ["Grupo", "Uma coluna vertical"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "O sódio tem 11 electrões, distribuídos "
                                 "por níveis: 2, 8 e 1. Quantos electrões "
                                 "tem no último nível?",
                            "a": "1",
                        },
                        {
                            "t": "input",
                            "q": "O cloro tem os electrões em três níveis: "
                                 "2, 8 e 7. Em que período da Tabela está?",
                            "a": "3",
                        },
                        {
                            "t": "choice",
                            "q": "Ao descer num grupo da Tabela, o raio "
                                 "atómico:",
                            "options": [
                                "Aumenta, porque há mais níveis",
                                "Diminui",
                                "Fica igual",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # III  Ligacao quimica
        # ================================================================
        {
            "id": "u3",
            "titulo": "Ligação química",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Ligação iónica e covalente",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A regra do octeto diz que os átomos "
                                 "tendem a ficar com:",
                            "options": [
                                "Oito electrões no último nível",
                                "Oito protões",
                                "Oito neutrões",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada ião ao seu tipo.",
                            "pairs": [
                                ["Átomo que perdeu electrões", "Catião, positivo"],
                                ["Átomo que ganhou electrões", "Anião, negativo"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada substância à sua ligação.",
                            "pairs": [
                                ["Cloreto de sódio", "Iónica"],
                                ["Água", "Covalente"],
                                ["Cobre", "Metálica"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Na ligação covalente, os átomos:",
                            "options": [
                                "Partilham pares de electrões",
                                "Trocam protões",
                                "Perdem todos os electrões",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O sal dissolvido em água conduz a "
                                 "corrente porque:",
                            "options": [
                                "Liberta iões que se movem",
                                "A água é um metal",
                                "O sal é covalente",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Ligação metálica e os metais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Na ligação metálica, os electrões:",
                            "options": [
                                "Movem-se livres entre os iões do metal",
                                "Ficam presos a cada átomo",
                                "Desaparecem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os metais conduzem bem o calor e a "
                                 "corrente porque:",
                            "options": [
                                "Têm electrões livres",
                                "São pesados",
                                "São brilhantes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada liga metálica aos metais que a "
                                 "formam.",
                            "pairs": [
                                ["Aço", "Ferro e carbono"],
                                ["Bronze", "Cobre e estanho"],
                                ["Latão", "Cobre e zinco"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O ferro bruto obtém-se no alto-forno:",
                            "options": [
                                "Reduzindo o minério de ferro com carvão",
                                "Dissolvendo o ferro em água",
                                "Juntando sal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O metal que Moçambique produz em grande "
                                 "quantidade na Mozal, em Maputo, é:",
                            "options": ["O alumínio", "O ouro", "O cobre"],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # IV  Cloro e o grupo VIIA
        # ================================================================
        {
            "id": "u4",
            "titulo": "O cloro e os halogéneos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Os halogéneos e o cloro",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Flúor, cloro, bromo e iodo são os "
                                 "halogéneos, e têm todos no último nível:",
                            "options": ["Sete electrões", "Um electrão", "Oito electrões"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O cloro usa-se no tratamento da água "
                                 "porque:",
                            "options": [
                                "Mata os micróbios",
                                "Dá-lhe sabor",
                                "Tira-lhe o sal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O sal de cozinha em Moçambique obtém-se "
                                 "sobretudo:",
                            "options": [
                                "Nas salinas do litoral, evaporando a água "
                                "do mar",
                                "Das minas de carvão",
                                "Dos rios",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada halogéneo à sua aplicação.",
                            "pairs": [
                                ["Flúor", "Pastas de dentes contra a cárie"],
                                ["Iodo", "Desinfectar feridas e o sal iodado"],
                                ["Cloro", "Tratar a água e a lixívia"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O ácido clorídrico existe no nosso "
                                 "corpo:",
                            "options": [
                                "No suco gástrico do estômago",
                                "No sangue dos ossos",
                                "Nos olhos",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Reacções redox e volume molar",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada processo ao que acontece ao "
                                 "número de oxidação.",
                            "pairs": [
                                ["Oxidação", "Aumenta: o átomo perde electrões"],
                                ["Redução", "Diminui: o átomo ganha electrões"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "No cloreto de sódio, o número de "
                                 "oxidação do cloro é menos 1. Qual é o do "
                                 "sódio?",
                            "a": "1",
                        },
                        {
                            "t": "choice",
                            "q": "O agente oxidante numa reacção é a "
                                 "substância que:",
                            "options": [
                                "Se reduz e faz o outro oxidar",
                                "Se oxida",
                                "Não reage",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Em condições normais, uma mole de "
                                 "qualquer gás ocupa 22,4 litros. Quantas "
                                 "moles há em 44,8 litros?",
                            "a": "2",
                        },
                        {
                            "t": "choice",
                            "q": "A lei de Avogadro diz que volumes iguais "
                                 "de gases, nas mesmas condições, têm:",
                            "options": [
                                "O mesmo número de moléculas",
                                "A mesma massa",
                                "A mesma cor",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # V  Enxofre e o grupo VIA
        # ================================================================
        {
            "id": "u5",
            "titulo": "O enxofre e a velocidade das reacções",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O enxofre e os seus compostos",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada variedade do enxofre à forma "
                                 "dos seus cristais.",
                            "pairs": [
                                ["Rômbico", "Cristais em losango, estável à temperatura ambiente"],
                                ["Monoclínico", "Cristais em agulha, acima dos 96 graus"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um elemento com várias formas, como o "
                                 "enxofre, tem:",
                            "options": [
                                "Variedades alotrópicas",
                                "Isótopos radioactivos",
                                "Iões diferentes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O ácido sulfúrico produz-se na indústria "
                                 "pelo método:",
                            "options": ["De contacto", "De Haber", "De Ostwald"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O ácido sulfúrico é o ácido mais usado "
                                 "na indústria, por exemplo:",
                            "options": [
                                "Nas baterias dos carros e no fabrico de "
                                "adubos",
                                "Para temperar a comida",
                                "Nas pastas de dentes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O sulfureto de hidrogénio reconhece-se:",
                            "options": [
                                "Pelo cheiro a ovo podre",
                                "Pela cor azul",
                                "Por não ter cheiro",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A velocidade das reacções",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A teoria das colisões diz que há "
                                 "reacção quando as partículas:",
                            "options": [
                                "Chocam com energia suficiente e na "
                                "posição certa",
                                "Estão paradas",
                                "Se afastam",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada exemplo ao factor que acelera "
                                 "a reacção.",
                            "pairs": [
                                ["O açúcar dissolve-se melhor em água quente", "Temperatura"],
                                ["A lenha rachada arde mais depressa que o tronco", "Superfície de contacto"],
                                ["A cinza faz amadurecer a banana mais depressa", "Catalisador"],
                                ["Vinagre mais forte ataca mais depressa o calcário", "Concentração"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A energia de activação é:",
                            "options": [
                                "A energia mínima para a reacção começar",
                                "A energia que sobra no fim",
                                "A energia do Sol",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um catalisador acelera a reacção "
                                 "porque:",
                            "options": [
                                "Baixa a energia de activação",
                                "Gasta-se todo",
                                "Aumenta a temperatura",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao mastigar pão, a saliva começa a "
                                 "digerir o amido graças à amilase, que é:",
                            "options": [
                                "Um catalisador do corpo, uma enzima",
                                "Um ácido forte",
                                "Um sal",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # VI  Nitrogenio e o grupo VA
        # ================================================================
        {
            "id": "u6",
            "titulo": "O nitrogénio, os adubos e o equilíbrio",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Nitrogénio, amoníaco e ácido nítrico",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "O nitrogénio, ou azoto, é o gás que há "
                                 "em maior quantidade no ar. Que "
                                 "percentagem do ar é azoto, "
                                 "aproximadamente?",
                            "a": "78",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada processo industrial ao que "
                                 "produz.",
                            "pairs": [
                                ["Processo de Haber-Bosch", "Amoníaco"],
                                ["Processo de Ostwald", "Ácido nítrico"],
                                ["Método de contacto", "Ácido sulfúrico"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada substância do azoto à sua fórmula.",
                            "pairs": [
                                ["Amoníaco", "NH₃"],
                                ["Ácido nítrico", "HNO₃"],
                                ["Nitrogénio", "N₂"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O amoníaco usa-se sobretudo:",
                            "options": [
                                "No fabrico de adubos",
                                "Para beber",
                                "Como combustível de cozinha",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os nitratos, sais do ácido nítrico, "
                                 "usam-se:",
                            "options": [
                                "Como adubos e no fabrico de explosivos",
                                "Como tempero",
                                "Para tratar a água",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Fósforo, adubos e equilíbrio químico",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada variedade do fósforo à sua "
                                 "característica.",
                            "pairs": [
                                ["Fósforo branco", "Muito reactivo e venenoso, arde no ar"],
                                ["Fósforo vermelho", "Mais estável, usado nos fósforos de riscar"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada adubo mineral ao nutriente "
                                 "que dá.",
                            "pairs": [
                                ["Azotado", "Azoto, para as folhas"],
                                ["Fosfatado", "Fósforo, para as raízes e flores"],
                                ["Potássico", "Potássio, para os frutos"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Adubo químico a mais:",
                            "options": [
                                "Polui o solo e a água e queima as "
                                "plantas",
                                "Faz sempre bem",
                                "Não tem efeito",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma reacção reversível é a que:",
                            "options": [
                                "Pode dar-se nos dois sentidos",
                                "Só se dá uma vez",
                                "Não produz nada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O princípio de Le Chatelier diz que, se "
                                 "se perturba um equilíbrio, ele:",
                            "options": [
                                "Desloca-se para contrariar a perturbação",
                                "Pára para sempre",
                                "Explode",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # VII  Carbono e o grupo IVA
        # ================================================================
        {
            "id": "u7",
            "titulo": "O carbono e o silício",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O carbono e os carvões",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada variedade do carbono à sua "
                                 "característica.",
                            "pairs": [
                                ["Diamante", "O material natural mais duro"],
                                ["Grafite", "Macia e boa condutora: a ponta do lápis"],
                            ],
                        },
                        {
                            "t": "match",
                            "q": "Liga cada carvão ao seu tipo.",
                            "pairs": [
                                ["Hulha e antracite", "Carvão mineral"],
                                ["Carvão de lenha e coque", "Carvão artificial"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O carvão mineral de Moatize, em Tete, é "
                                 "importante porque:",
                            "options": [
                                "É exportado e dá emprego e receitas ao "
                                "país",
                                "Serve para fazer diamantes",
                                "Não tem uso",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Fazer carvão de lenha sem replantar "
                                 "árvores:",
                            "options": [
                                "Destrói as florestas",
                                "Aumenta as florestas",
                                "Não tem efeito",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O monóxido de carbono, que sai do carvão "
                                 "a arder numa casa fechada:",
                            "options": [
                                "É um gás venenoso, sem cor nem cheiro, "
                                "que pode matar",
                                "É inofensivo",
                                "Cheira a ovo podre",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Dióxido de carbono, silício e cimento",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O dióxido de carbono identifica-se "
                                 "porque:",
                            "options": [
                                "Turva a água de cal",
                                "Acende uma vela",
                                "Cheira mal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O excesso de dióxido de carbono no ar "
                                 "causa:",
                            "options": [
                                "O efeito de estufa e o aquecimento global",
                                "O buraco no chão",
                                "A chuva de granizo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A areia da praia é sobretudo:",
                            "options": ["Dióxido de silício", "Carbonato de cálcio", "Cloreto de sódio"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada produto à sua matéria-prima "
                                 "principal.",
                            "pairs": [
                                ["Vidro", "Areia"],
                                ["Cimento", "Calcário e argila"],
                                ["Cerâmica", "Argila"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O calcário para o cimento extrai-se em "
                                 "Moçambique, por exemplo:",
                            "options": [
                                "Em Salamanga, no Dondo e em Nacala",
                                "No lago Niassa",
                                "Na ilha de Moçambique",
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
