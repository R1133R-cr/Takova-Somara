# -*- coding: utf-8 -*-
"""A materia de cada nivel, na lingua em que se fala a uma crianca.

Tres campos por nivel:

  explica  o conceito, em frases curtas. Quanto mais nova a classe, mais
           curtas -- na 1a classe a Raquel le isto em voz alta a quem ainda
           nao sabe ler, e uma frase comprida perde-se a meio.
  exemplo  um caso ja resolvido. E o que uma crianca copia quando nao
           percebeu a explicacao, por isso tem de estar completo.
  lembra   a frase que se leva para o exercicio. Nunca e um resumo da
           explicacao: e a regra pratica, o que fazer quando se hesita.

Ortografia anterior ao Acordo de 1990, como o resto do conteudo e como se
escreve nas escolas mocambicanas.
"""

MATERIA = {

    # ---------------------------------------------------------------
    # Matematica -- 1a classe
    # ---------------------------------------------------------------
    "mat-1c:u1:n1": {
        "explica": "Contar é dizer quantos há. Apontas para cada coisa uma "
                   "vez e vais dizendo os números: um, dois, três, quatro, "
                   "cinco.",
        "exemplo": "Três maçãs: apontas e dizes um, dois, três. São 3 maçãs.",
        "lembra": "O último número que disseres é a resposta.",
    },
    "mat-1c:u1:n2": {
        "explica": "Depois do cinco vêm o seis, o sete, o oito, o nove e o "
                   "dez. Contam-se do mesmo jeito, um de cada vez.",
        "exemplo": "6, 7, 8, 9, 10. O número antes do 10 é o 9.",
        "lembra": "Antes é o que vem primeiro. Depois é o que vem a seguir.",
    },
    "mat-1c:u2:n1": {
        "explica": "Quando contamos, os números vão ficando maiores. O que "
                   "vem depois é sempre maior do que o que vem antes.",
        "exemplo": "3 ou 7? Contando, o 7 vem depois do 3. Logo o 7 é maior.",
        "lembra": "Quem vem mais tarde na contagem é o maior.",
    },
    "mat-1c:u2:n2": {
        "explica": "Os números têm sempre a mesma ordem. Se souberes contar, "
                   "descobres qual é o que falta.",
        "exemplo": "1, 2, 3, __ . Contas: um, dois, três... quatro. Falta o 4.",
        "lembra": "Conta desde o princípio até chegares ao lugar vazio.",
    },
    "mat-1c:u3:n1": {
        "explica": "Somar é juntar. Pões tudo junto e contas outra vez desde "
                   "o princípio.",
        "exemplo": "2 + 1: tens duas coisas, juntas mais uma, ficam três. "
                   "2 + 1 = 3.",
        "lembra": "Somar dá sempre mais do que tinhas.",
    },
    "mat-1c:u3:n2": {
        "explica": "Para somar até dez, podes usar os dedos: levantas os "
                   "primeiros e depois continuas a contar os outros.",
        "exemplo": "4 + 3: levantas 4 dedos e contas mais três — cinco, seis, "
                   "sete. 4 + 3 = 7.",
        "lembra": "Começa no número maior e conta o outro por cima.",
    },
    "mat-1c:u4:n1": {
        "explica": "Subtrair é tirar. Ficas com menos do que tinhas.",
        "exemplo": "Tinhas 3 rebuçados e comeste 1. Tiras um: ficam 2.",
        "lembra": "Tirar dá sempre menos do que tinhas.",
    },
    "mat-1c:u4:n2": {
        "explica": "Para tirar, conta para trás. Começas no número grande e "
                   "andas para trás tantas vezes quantas tiras.",
        "exemplo": "8 − 3: partes do 8 e andas três para trás — sete, seis, "
                   "cinco. 8 − 3 = 5.",
        "lembra": "Somar anda para a frente, tirar anda para trás.",
    },
    "mat-1c:u5:n1": {
        "explica": "Depois do dez os números continuam: onze, doze, treze, "
                   "catorze, quinze... até ao vinte.",
        "exemplo": "12, 13, __ , 15. A seguir ao treze vem o catorze.",
        "lembra": "Depois do dez, continua a contar do mesmo modo.",
    },
    "mat-1c:u5:n2": {
        "explica": "Com números maiores faz-se o mesmo: somar é juntar, "
                   "tirar é afastar.",
        "exemplo": "10 + 5: partes do dez e contas mais cinco — 11, 12, 13, "
                   "14, 15.",
        "lembra": "Parte sempre do número maior. Dá menos trabalho.",
    },
    "mat-1c:u6:n1": {
        "explica": "As coisas têm formas. O círculo é redondo, o triângulo "
                   "tem três lados e o quadrado tem quatro lados iguais.",
        "exemplo": "Uma bola é redonda: tem a forma de um círculo.",
        "lembra": "Conta os lados: três é triângulo, quatro é quadrado.",
    },
    "mat-1c:u6:n2": {
        "explica": "O dinheiro de Moçambique é o metical. Comprar é dar "
                   "dinheiro; o troco é o que sobra e volta para a tua mão.",
        "exemplo": "O pão custa 5 MT e pagas com 10 MT. O troco é 10 − 5 = 5 MT.",
        "lembra": "O troco é uma subtracção: o que deste menos o que custou.",
    },
    "mat-1c:u7:n1": {
        "explica": "Agora aparecem contas de somar e de tirar à mistura. Olha "
                   "bem para o sinal antes de responder.",
        "exemplo": "6 + 3 = 9, mas 9 − 2 = 7. O sinal muda tudo.",
        "lembra": "Primeiro vê o sinal. Só depois faz a conta.",
    },

    # ---------------------------------------------------------------
    # Portugues -- 1a classe
    # ---------------------------------------------------------------
    "por-1c:u1:n1": {
        "explica": "As vogais são cinco letras: a, e, i, o, u. Sem elas não "
                   "há palavras — todas as palavras têm pelo menos uma.",
        "exemplo": "Na palavra casa há duas vogais: o a e o a.",
        "lembra": "a, e, i, o, u. As outras letras são consoantes.",
    },
    "por-1c:u1:n2": {
        "explica": "Muitas palavras começam por vogal. Diz a palavra devagar "
                   "e ouve bem o primeiro som.",
        "exemplo": "ASA começa por A. ELEFANTE começa por E.",
        "lembra": "Diz a palavra em voz alta e escuta o primeiro som.",
    },
    "por-1c:u2:n1": {
        "explica": "Uma consoante junta-se a uma vogal e faz uma sílaba. O "
                   "P com o A faz PA.",
        "exemplo": "P + A = PA. P + I = PI.",
        "lembra": "Consoante à frente, vogal atrás: sai uma sílaba.",
    },
    "por-1c:u2:n2": {
        "explica": "Duas sílabas juntas fazem uma palavra.",
        "exemplo": "PA + TO = PATO. Dizes as duas seguidas e ouves a palavra.",
        "lembra": "Diz as sílabas depressa uma atrás da outra.",
    },
    "por-1c:u3:n1": {
        "explica": "O M faz o mesmo que o P: junta-se às vogais e forma "
                   "sílabas.",
        "exemplo": "M + A = MA. M + I = MI.",
        "lembra": "É sempre igual: a consoante primeiro, a vogal depois.",
    },
    "por-1c:u3:n2": {
        "explica": "Com as sílabas do M fazem-se palavras que já conheces.",
        "exemplo": "MA + LA = MALA. MA + PA = MAPA.",
        "lembra": "Junta as sílabas e vê se a palavra existe.",
    },
    "por-1c:u4:n1": {
        "explica": "O L e o T também formam sílabas com todas as vogais.",
        "exemplo": "L + A = LA. T + E = TE.",
        "lembra": "Cada consoante dá cinco sílabas, uma por vogal.",
    },
    "por-1c:u4:n2": {
        "explica": "Agora juntas sílabas do L e do T para fazer palavras.",
        "exemplo": "LA + TA = LATA. TA + TU = TATU.",
        "lembra": "Lê devagar da esquerda para a direita.",
    },
    "por-1c:u5:n1": {
        "explica": "Todas as palavras se fazem juntando sílabas. Já sabes "
                   "juntar muitas.",
        "exemplo": "CA + SA = CASA. BO + LA = BOLA.",
        "lembra": "Primeira sílaba, segunda sílaba, e a palavra aparece.",
    },
    "por-1c:u6:n1": {
        "explica": "Uma frase diz alguma coisa. Começa sempre com letra "
                   "grande e acaba com um ponto final.",
        "exemplo": "O cão corre. Começa com O grande e acaba com ponto.",
        "lembra": "Letra grande no princípio, ponto no fim.",
    },
    "por-1c:u7:n1": {
        "explica": "Ler é perceber o que está escrito. Lê o texto devagar e "
                   "depois procura a resposta lá dentro.",
        "exemplo": "«O Pedro tem um cão. O cão chama-se Bobi.» Como se chama "
                   "o cão? Está escrito: Bobi.",
        "lembra": "A resposta está no texto. Volta atrás e procura.",
    },

    # ---------------------------------------------------------------
    # Matematica -- 2a classe
    # ---------------------------------------------------------------
    "mat-2c:u1:n1": {
        "explica": "Os números até cem lêem-se em duas partes: primeiro as "
                   "dezenas, depois as unidades, ligadas por «e».",
        "exemplo": "57 lê-se cinquenta e sete: cinquenta mais sete.",
        "lembra": "Primeiro o algarismo da esquerda, depois o da direita.",
    },
    "mat-2c:u1:n2": {
        "explica": "Para comparar dois números, olha primeiro para o "
                   "algarismo da esquerda. O sinal > quer dizer maior, "
                   "< quer dizer menor e = quer dizer igual.",
        "exemplo": "45 e 54: à esquerda o 4 é menor que o 5, logo 45 < 54.",
        "lembra": "O bico do sinal aponta sempre para o número menor.",
    },
    "mat-2c:u1:n3": {
        "explica": "Cada número de dois algarismos tem dezenas e unidades. "
                   "Uma dezena são dez unidades juntas.",
        "exemplo": "47 tem 4 dezenas e 7 unidades: quarenta mais sete.",
        "lembra": "O algarismo da esquerda são dezenas, o da direita unidades.",
    },
    "mat-2c:u2:n1": {
        "explica": "Para somar números grandes, soma primeiro as unidades e "
                   "depois as dezenas.",
        "exemplo": "34 + 25: unidades 4 + 5 = 9; dezenas 30 + 20 = 50. "
                   "Total 59.",
        "lembra": "Unidades com unidades, dezenas com dezenas.",
    },
    "mat-2c:u2:n2": {
        "explica": "Na subtracção faz-se o mesmo: tiram-se as unidades e "
                   "depois as dezenas.",
        "exemplo": "68 − 25: unidades 8 − 5 = 3; dezenas 60 − 20 = 40. "
                   "Resta 43.",
        "lembra": "Arruma um por baixo do outro e tira parte a parte.",
    },
    "mat-2c:u2:n3": {
        "explica": "Os números ordinais dizem a ordem de chegada: primeiro, "
                   "segundo, terceiro...",
        "exemplo": "Quem chega em 1.º lugar chega em primeiro.",
        "lembra": "O ponto e o «o» pequenino mostram que é ordem, não "
                  "quantidade.",
    },
    "mat-2c:u3:n1": {
        "explica": "O relógio marca as horas e os minutos. O ponteiro pequeno "
                   "marca as horas e o grande marca os minutos.",
        "exemplo": "Um dia tem 24 horas e cada hora tem 60 minutos.",
        "lembra": "60 minutos numa hora, 24 horas num dia.",
    },
    "mat-2c:u3:n2": {
        "explica": "O calendário organiza o tempo em dias, semanas e meses.",
        "exemplo": "Uma semana tem 7 dias e um ano tem 12 meses.",
        "lembra": "7 dias numa semana, 12 meses num ano.",
    },
    "mat-2c:u4:n1": {
        "explica": "Multiplicar é somar a mesma quantidade muitas vezes.",
        "exemplo": "4 × 3 é o mesmo que 3 + 3 + 3 + 3 = 12.",
        "lembra": "Quando não souberes de cor, soma tantas vezes quantas "
                  "manda o primeiro número.",
    },
    "mat-2c:u4:n2": {
        "explica": "Números pares podem dividir-se em dois grupos iguais. Os "
                   "ímpares deixam sempre um de fora.",
        "exemplo": "8 é par: 4 e 4. 7 é ímpar: 3 e 3 e sobra um.",
        "lembra": "Acaba em 0, 2, 4, 6 ou 8? É par.",
    },
    "mat-2c:u5:n1": {
        "explica": "Uma linha recta não faz curvas. As figuras fazem-se com "
                   "linhas, e conta-se pelos lados.",
        "exemplo": "O quadrado tem 4 lados todos iguais.",
        "lembra": "Conta os lados para saber que figura é.",
    },
    "mat-2c:u5:n2": {
        "explica": "Os sólidos ocupam espaço: podes pegar-lhes. A esfera é "
                   "redonda e o cubo tem seis faces quadradas.",
        "exemplo": "Uma bola é uma esfera. Um dado é um cubo.",
        "lembra": "Figura é plana, no papel. Sólido tem grossura.",
    },

    # ---------------------------------------------------------------
    # Portugues -- 2a classe
    # ---------------------------------------------------------------
    "por-2c:u1:n1": {
        "explica": "As sílabas são os bocados em que a palavra se parte "
                   "quando a dizemos devagar. Cada sílaba tem uma vogal.",
        "exemplo": "me-ni-no tem três sílabas. Bate as palmas uma por sílaba.",
        "lembra": "Uma palma por sílaba: é assim que se contam.",
    },
    "por-2c:u1:n2": {
        "explica": "Uma frase põe as palavras por ordem para fazer sentido. "
                   "Começa com maiúscula e acaba com ponto.",
        "exemplo": "casa / na / Tito / está / o dá: O Tito está na casa.",
        "lembra": "Se a frase não faz sentido, a ordem está trocada.",
    },
    "por-2c:u2:n1": {
        "explica": "Há frases que dão ordens ou pedidos. Costumam começar "
                   "pelo verbo.",
        "exemplo": "«Abre a porta.» dá uma ordem. O contrário é «Fecha a "
                   "porta.»",
        "lembra": "Se a frase manda fazer alguma coisa, é uma ordem.",
    },
    "por-2c:u2:n2": {
        "explica": "Os artigos vêm antes do nome: o, a, os, as. Mudam "
                   "conforme o nome é masculino ou feminino.",
        "exemplo": "O caderno é novo. A professora chegou.",
        "lembra": "O para masculino, a para feminino.",
    },
    "por-2c:u3:n1": {
        "explica": "Os possessivos dizem de quem é a coisa: meu, teu, seu, "
                   "nosso.",
        "exemplo": "De mim: esta é a minha mão. De ti: esse é o teu livro.",
        "lembra": "Pergunta «de quem é?» e escolhe o possessivo certo.",
    },
    "por-2c:u3:n2": {
        "explica": "O nome diz o que a coisa é. O adjectivo diz como ela é, e "
                   "muda com o nome.",
        "exemplo": "A menina é bonita. Os meninos são bonitos.",
        "lembra": "O adjectivo acompanha o nome no género e no número.",
    },
    "por-2c:u4:n1": {
        "explica": "Os demonstrativos mostram onde está a coisa: este é "
                   "perto de mim, esse é perto de ti, aquele está longe dos "
                   "dois.",
        "exemplo": "Este livro está na minha mão. Aquele está lá longe.",
        "lembra": "Este perto de mim, esse perto de ti, aquele longe.",
    },
    "por-2c:u4:n2": {
        "explica": "Compreender um texto é procurar dentro dele a resposta, "
                   "sem inventar.",
        "exemplo": "«A Lila escova os dentes de manhã e à noite.» São duas "
                   "vezes por dia.",
        "lembra": "Se não está no texto, não é resposta.",
    },
    "por-2c:u5:n1": {
        "explica": "O verbo ser diz o que a coisa é sempre. O verbo estar diz "
                   "como ela está agora.",
        "exemplo": "A árvore é grande, sempre foi. A água está fria, mas "
                   "depois aquece.",
        "lembra": "Ser é para sempre, estar é por agora.",
    },
    "por-2c:u5:n2": {
        "explica": "Cuidar do ambiente é cuidar do sítio onde vivemos: não "
                   "deitar lixo no chão e plantar em vez de só cortar.",
        "exemplo": "O lixo deve ser posto no caixote, não na rua.",
        "lembra": "Quem corta uma árvore deve plantar outra.",
    },
    "por-2c:u6:n1": {
        "explica": "Os indefinidos falam de quantidade sem dizer o número "
                   "certo: todos, alguns, muitos, nenhum.",
        "exemplo": "Todos os alunos chegaram. Algumas meninas cantaram.",
        "lembra": "Não dizem quantos ao certo — só se são muitos ou poucos.",
    },
    "por-2c:u6:n2": {
        "explica": "Na fábula, os animais falam e agem como pessoas. No fim "
                   "há sempre uma lição, chamada moral.",
        "exemplo": "Numa fábula, a raposa fala com o corvo e no fim aprende-se "
                   "alguma coisa.",
        "lembra": "Fábula tem animais a falar e uma moral no fim.",
    },

    # ---------------------------------------------------------------
    # Matematica -- 3a classe
    # ---------------------------------------------------------------
    "mat-3c:u1:n1": {
        "explica": "Nos números de quatro algarismos, o primeiro conta os "
                   "milhares. Lê-se por partes: milhares, centenas, dezenas "
                   "e unidades.",
        "exemplo": "3 425 lê-se três mil, quatrocentos e vinte e cinco.",
        "lembra": "Separa o milhar com um espaço e lê da esquerda para a "
                  "direita.",
    },
    "mat-3c:u1:n2": {
        "explica": "Para comparar números grandes, compara algarismo a "
                   "algarismo, a começar pela esquerda. O primeiro que for "
                   "diferente decide.",
        "exemplo": "2 340 e 2 430: os milhares são iguais, mas 3 centenas é "
                   "menos que 4. Logo 2 340 < 2 430.",
        "lembra": "Só continua a comparar enquanto os algarismos forem iguais.",
    },
    "mat-3c:u2:n1": {
        "explica": "Rectas perpendiculares cruzam-se formando um ângulo "
                   "recto, como o canto de uma folha. Rectas paralelas nunca "
                   "se encontram.",
        "exemplo": "Os dois lados de uma porta são paralelos; o lado e o "
                   "chão são perpendiculares.",
        "lembra": "Paralelas nunca se tocam; perpendiculares fazem um canto "
                  "certo.",
    },
    "mat-3c:u2:n2": {
        "explica": "O quadrado tem quatro lados iguais. O rectângulo tem "
                   "quatro lados, iguais dois a dois. O círculo não tem "
                   "lados.",
        "exemplo": "Uma janela alta e estreita é um rectângulo: dois lados "
                   "compridos e dois curtos.",
        "lembra": "Todo o quadrado é rectângulo, mas nem todo o rectângulo é "
                  "quadrado.",
    },
    "mat-3c:u3:n1": {
        "explica": "Para somar números grandes, arruma-os uns por baixo dos "
                   "outros: unidades com unidades, dezenas com dezenas.",
        "exemplo": "245 + 132: 5+2 = 7, 4+3 = 7, 2+1 = 3. Dá 377.",
        "lembra": "Se a coluna passar de nove, sobe um para a coluna "
                  "seguinte.",
    },
    "mat-3c:u3:n2": {
        "explica": "Na subtracção arruma-se do mesmo modo. Quando não dá para "
                   "tirar, pede-se emprestado à coluna da esquerda.",
        "exemplo": "587 − 243: 7−3 = 4, 8−4 = 4, 5−2 = 3. Dá 344.",
        "lembra": "Confere no fim: soma o resultado com o que tiraste e tem "
                  "de dar o número de cima.",
    },
    "mat-3c:u4:n1": {
        "explica": "Multiplicar é somar parcelas iguais. Multiplicar por 10 é "
                   "só acrescentar um zero.",
        "exemplo": "7 × 8 = 56. E 25 × 10 = 250.",
        "lembra": "Trocar a ordem não muda nada: 7 × 8 é igual a 8 × 7.",
    },
    "mat-3c:u4:n2": {
        "explica": "Dividir é repartir em partes iguais. É a operação "
                   "contrária da multiplicação.",
        "exemplo": "48 : 6 = 8, porque 6 × 8 = 48.",
        "lembra": "Para conferir uma divisão, multiplica de volta.",
    },
    "mat-3c:u5:n1": {
        "explica": "O metro mede comprimento e o quilograma mede massa. Cada "
                   "um divide-se em cem ou mil partes.",
        "exemplo": "1 metro tem 100 centímetros. 1 quilograma tem 1 000 "
                   "gramas.",
        "lembra": "Centi quer dizer cem; mili quer dizer mil.",
    },
    "mat-3c:u5:n2": {
        "explica": "O litro mede o que cabe dentro; a hora mede o tempo.",
        "exemplo": "1 litro tem 1 000 mililitros. 1 hora tem 60 minutos.",
        "lembra": "O tempo conta de 60 em 60, não de 100 em 100.",
    },
    "mat-3c:u6:n1": {
        "explica": "Uma fracção é uma parte de um todo dividido em partes "
                   "iguais. O número de baixo diz em quantas partes se "
                   "dividiu.",
        "exemplo": "Um bolo partido em duas partes iguais: cada parte é "
                   "metade, e escreve-se 1/2.",
        "lembra": "As partes têm de ser iguais, senão não é fracção.",
    },
    "mat-3c:u7:n1": {
        "explica": "O metical é a moeda de Moçambique e escreve-se MT. "
                   "Somam-se notas e moedas como quaisquer números.",
        "exemplo": "Duas notas de 50 MT são 50 + 50 = 100 MT.",
        "lembra": "Junta primeiro as notas iguais: é mais depressa.",
    },
    "mat-3c:u8:n1": {
        "explica": "Quando falta um número numa conta, faz a operação "
                   "contrária para o descobrir.",
        "exemplo": "5 + ___ = 12. Faz ao contrário: 12 − 5 = 7.",
        "lembra": "Falta numa soma? Subtrai. Falta numa subtracção? Soma.",
    },
    "mat-3c:u9:n1": {
        "explica": "Um gráfico de barras mostra quantidades com barras: "
                   "quanto mais alta, maior a quantidade.",
        "exemplo": "Se a barra da segunda-feira é a mais alta, foi o dia em "
                   "que houve mais.",
        "lembra": "Lê sempre os nomes por baixo das barras antes de "
                  "responder.",
    },

    # ---------------------------------------------------------------
    # Portugues -- 3a classe
    # ---------------------------------------------------------------
    "por-3c:u1:n1": {
        "explica": "O verbo é a palavra que diz o que se faz ou o que "
                   "acontece. É o coração da frase.",
        "exemplo": "«A Ana estuda todos os dias.» O verbo é estuda.",
        "lembra": "Pergunta «o que é que faz?» — a resposta é o verbo.",
    },
    "por-3c:u1:n2": {
        "explica": "Sinónimos são palavras diferentes com o mesmo "
                   "significado.",
        "exemplo": "Bonita e linda querem dizer o mesmo: são sinónimos.",
        "lembra": "Troca a palavra na frase. Se o sentido ficar igual, é "
                  "sinónimo.",
    },
    "por-3c:u2:n1": {
        "explica": "Antónimos são palavras com significado contrário.",
        "exemplo": "O antónimo de alta é baixa.",
        "lembra": "Sinónimo é igual, antónimo é o contrário.",
    },
    "por-3c:u2:n2": {
        "explica": "A sílaba é cada bocado da palavra que se diz de uma vez "
                   "só. Divide-se com hífen.",
        "exemplo": "es-co-la tem três sílabas; pro-fes-sor também tem três.",
        "lembra": "Cada sílaba tem uma vogal — conta as vogais que soam.",
    },
    "por-3c:u3:n1": {
        "explica": "O adjectivo diz como é a pessoa ou a coisa: a sua "
                   "qualidade.",
        "exemplo": "«A casa é bonita.» O adjectivo é bonita: diz como é a "
                   "casa.",
        "lembra": "Pergunta «como é?» — a resposta é o adjectivo.",
    },
    "por-3c:u3:n2": {
        "explica": "Escreve-se com maiúscula no princípio da frase e nos "
                   "nomes próprios: pessoas, cidades, países.",
        "exemplo": "O Tomás vive em Lichinga. Tomás e Lichinga levam "
                   "maiúscula.",
        "lembra": "Nomes de pessoas e lugares levam sempre maiúscula.",
    },
    "por-3c:u4:n1": {
        "explica": "Os sinais de pontuação dizem como se lê a frase. O ponto "
                   "acaba, a interrogação pergunta e a exclamação exclama.",
        "exemplo": "Como te chamas? leva ponto de interrogação porque "
                   "pergunta.",
        "lembra": "Pergunta leva ?, afirmação leva . e espanto leva !",
    },
    "por-3c:u4:n2": {
        "explica": "Há textos que contam histórias (narrativos) e textos que "
                   "dizem como são as coisas (descritivos).",
        "exemplo": "«Era uma vez...» conta uma história: é narrativo.",
        "lembra": "Conta o que aconteceu? Narrativo. Diz como é? Descritivo.",
    },
    "por-3c:u5:n1": {
        "explica": "Nome próprio é o nome de alguém ou de algum lugar em "
                   "particular. Nome comum serve para todos da mesma espécie.",
        "exemplo": "Maputo é nome próprio; cidade é nome comum.",
        "lembra": "Nome próprio leva maiúscula; nome comum não.",
    },
    "por-3c:u5:n2": {
        "explica": "Género é masculino ou feminino. Número é singular (um) ou "
                   "plural (muitos).",
        "exemplo": "Professor fica professora no feminino; casa fica casas no "
                   "plural.",
        "lembra": "Para o plural junta-se quase sempre um s.",
    },
    "por-3c:u5:n3": {
        "explica": "O tempo do verbo diz quando aconteceu: presente é agora, "
                   "passado é antes, futuro é depois.",
        "exemplo": "Eu estudo é presente. Eu estudei é passado. Eu estudarei "
                   "é futuro.",
        "lembra": "Pergunta «quando?» — agora, antes ou depois.",
    },
    "por-3c:u5:n4": {
        "explica": "A frase interrogativa faz uma pergunta e acaba sempre com "
                   "ponto de interrogação.",
        "exemplo": "Onde está o livro? é interrogativa.",
        "lembra": "Se esperas uma resposta, é pergunta.",
    },

    # ---------------------------------------------------------------
    # Matematica -- 4a classe
    # ---------------------------------------------------------------
    "mat-4c:u1:n1": {
        "explica": "Nos números grandes separa-se de três em três algarismos, "
                   "a começar da direita. Cada grupo lê-se de uma vez.",
        "exemplo": "45 300 lê-se quarenta e cinco mil e trezentos.",
        "lembra": "Conta os algarismos de trás para a frente, de três em "
                  "três.",
    },
    "mat-4c:u1:n2": {
        "explica": "Arredondar é trocar o número pelo mais próximo de uma "
                   "certa ordem. Olha-se para o algarismo seguinte: se for 5 "
                   "ou mais, sobe.",
        "exemplo": "4 780 à centena: a seguir às centenas está o 8, que é "
                   "mais que 5, logo sobe para 4 800.",
        "lembra": "5 ou mais, sobe. Menos de 5, fica.",
    },
    "mat-4c:u2:n1": {
        "explica": "O perímetro é o comprimento de toda a volta da figura. "
                   "Somam-se todos os lados.",
        "exemplo": "Um quadrado de 5 cm de lado: 5 + 5 + 5 + 5 = 20 cm.",
        "lembra": "Perímetro é a volta. Anda à volta e vai somando.",
    },
    "mat-4c:u2:n2": {
        "explica": "A área é o espaço que a figura ocupa por dentro. No "
                   "rectângulo multiplica-se o comprimento pela largura.",
        "exemplo": "Um rectângulo de 6 cm por 4 cm tem 6 × 4 = 24 "
                   "centímetros quadrados.",
        "lembra": "Perímetro soma-se, área multiplica-se.",
    },
    "mat-4c:u3:n1": {
        "explica": "Com números grandes o método é o mesmo: alinhar as ordens "
                   "e operar coluna a coluna.",
        "exemplo": "12 450 + 3 250 = 15 700.",
        "lembra": "Alinha pela direita, nunca pela esquerda.",
    },
    "mat-4c:u4:n1": {
        "explica": "Para multiplicar por dois algarismos, multiplica-se "
                   "primeiro pelas unidades, depois pelas dezenas, e somam-se "
                   "os dois resultados.",
        "exemplo": "24 × 12: 24 × 2 = 48 e 24 × 10 = 240. Somando, 288.",
        "lembra": "Parte o número em dezenas e unidades, é mais fácil.",
    },
    "mat-4c:u4:n2": {
        "explica": "Nem todas as divisões são exactas. O que sobra chama-se "
                   "resto, e é sempre menor que o divisor.",
        "exemplo": "144 : 12 = 12, sem resto. Mas 145 : 12 = 12 e sobra 1.",
        "lembra": "Se o resto for igual ou maior que o divisor, ainda dá para "
                  "dividir mais.",
    },
    "mat-4c:u5:n1": {
        "explica": "As unidades de comprimento andam de mil em mil ou de cem "
                   "em cem. Para passar a maior, divide-se; a menor, "
                   "multiplica-se.",
        "exemplo": "1 km = 1 000 m. Logo 2 500 m são 2,5 km.",
        "lembra": "Para unidade maior, o número fica menor.",
    },
    "mat-4c:u6:n1": {
        "explica": "Quando o número de cima é igual, ganha a fracção com o "
                   "número de baixo mais pequeno — porque as partes são "
                   "maiores.",
        "exemplo": "1/2 é maior que 1/4: partir em duas dá pedaços maiores do "
                   "que partir em quatro.",
        "lembra": "Mais partes, pedaços mais pequenos.",
    },
    "mat-4c:u7:n1": {
        "explica": "A vírgula separa a parte inteira das partes mais "
                   "pequenas. A primeira casa depois da vírgula são décimas.",
        "exemplo": "0,5 lê-se cinco décimas, e é o mesmo que meio.",
        "lembra": "Uma casa é décimas, duas casas são centésimas.",
    },
    "mat-4c:u7:n2": {
        "explica": "Para somar decimais, alinha-se a vírgula por baixo da "
                   "vírgula.",
        "exemplo": "1,2 + 2,3 = 3,5. As vírgulas ficam uma debaixo da outra.",
        "lembra": "Vírgula com vírgula. O resto é como sempre.",
    },
    "mat-4c:u8:n1": {
        "explica": "Poupar é guardar um pouco de cada vez. O troco é o que "
                   "sobra depois de pagar.",
        "exemplo": "Livro de 320 MT pago com 500 MT: o troco é 500 − 320 = "
                   "180 MT.",
        "lembra": "Troco é subtracção; poupança semana a semana é "
                  "multiplicação.",
    },
    "mat-4c:u9:n1": {
        "explica": "Para descobrir o número escondido, faz a operação "
                   "contrária da que está na conta.",
        "exemplo": "___ + 250 = 1 000. Ao contrário: 1 000 − 250 = 750.",
        "lembra": "Soma desfaz-se com subtracção; multiplicação com divisão.",
    },
    "mat-4c:u10:n1": {
        "explica": "As tabelas e os gráficos arrumam números para se poderem "
                   "comparar de relance.",
        "exemplo": "Para saber o total do mês numa tabela de despesas, "
                   "somam-se todas as linhas.",
        "lembra": "Lê primeiro os títulos: dizem o que cada número significa.",
    },

    # ---------------------------------------------------------------
    # Ciencias Naturais -- 4a classe
    # ---------------------------------------------------------------
    "cn-4c:u1:n1": {
        "explica": "Os seres vivos nascem, crescem, alimentam-se, "
                   "reproduzem-se e morrem. Os não vivos não fazem nada "
                   "disto.",
        "exemplo": "Uma árvore é um ser vivo: nasce, cresce e dá sementes. "
                   "Uma pedra não.",
        "lembra": "Se nasce e cresce, é ser vivo.",
    },
    "cn-4c:u2:n1": {
        "explica": "A planta tem raiz, caule, folhas, flor e fruto. A raiz "
                   "segura e bebe água; as folhas fabricam o alimento.",
        "exemplo": "A raiz da mandioqueira segura a planta e guarda alimento "
                   "debaixo da terra.",
        "lembra": "Cada parte da planta tem um trabalho seu.",
    },
    "cn-4c:u2:n2": {
        "explica": "Animais domésticos vivem com as pessoas e são criados por "
                   "elas. Os selvagens vivem sozinhos na natureza.",
        "exemplo": "A cabra é doméstica; o leão é selvagem.",
        "lembra": "Se alguém trata dele, é doméstico.",
    },
    "cn-4c:u3:n1": {
        "explica": "A água do mar é salgada e a dos rios é doce. Nem toda a "
                   "água doce é própria para beber.",
        "exemplo": "O poço e o furo são fontes de água na comunidade.",
        "lembra": "Água limpa à vista pode na mesma ter micróbios. Ferve-a.",
    },
    "cn-4c:u3:n2": {
        "explica": "O lixo deve ir para o caixote. Separar serve para "
                   "aproveitar outra vez o que ainda presta.",
        "exemplo": "As garrafas de plástico separadas podem ser recicladas.",
        "lembra": "Lixo no chão suja a água e traz doenças.",
    },
    "cn-4c:u4:n1": {
        "explica": "Temos cinco órgãos dos sentidos: olhos para ver, ouvidos "
                   "para ouvir, nariz para cheirar, língua para saborear e "
                   "pele para sentir.",
        "exemplo": "A língua sente o doce e o salgado: é o paladar.",
        "lembra": "Cinco órgãos, cinco sentidos, um para cada.",
    },
    "cn-4c:u4:n2": {
        "explica": "Os alimentos energéticos dão força, os construtores "
                   "ajudam a crescer e os protectores defendem das doenças.",
        "exemplo": "A mandioca dá energia; o peixe ajuda a crescer; a fruta "
                   "protege.",
        "lembra": "Comer de tudo um pouco é comer bem.",
    },
    "cn-4c:u4:n3": {
        "explica": "Os micróbios são seres tão pequenos que só se vêem ao "
                   "microscópio. Alguns causam doenças, outros são úteis.",
        "exemplo": "Há micróbios que transformam o leite em iogurte.",
        "lembra": "Lavar as mãos tira os micróbios maus.",
    },
    "cn-4c:u5:n1": {
        "explica": "Corpos luminosos têm luz própria; os iluminados só "
                   "reflectem a luz de outro. A luz anda em linha recta.",
        "exemplo": "O Sol tem luz própria; a Lua só reflecte a luz do Sol.",
        "lembra": "A sombra aparece quando alguma coisa tapa a luz.",
    },
    "cn-4c:u6:n1": {
        "explica": "Uma força pode pôr as coisas a mexer, pará-las ou mudar a "
                   "sua forma. A gravidade puxa tudo para o chão.",
        "exemplo": "A pedra cai porque a gravidade a puxa para baixo.",
        "lembra": "Onde há movimento a mudar, houve uma força.",
    },
    "cn-4c:u7:n1": {
        "explica": "Recursos naturais são as riquezas que a natureza dá: "
                   "água, solo, florestas, minerais.",
        "exemplo": "O solo é feito de areia, argila e restos de plantas e "
                   "animais.",
        "lembra": "Os recursos não são infinitos: usam-se com cuidado.",
    },
    "cn-4c:u8:n1": {
        "explica": "Matéria é tudo o que ocupa espaço e tem massa. Aparece em "
                   "três estados: sólido, líquido e gasoso.",
        "exemplo": "A água é gelo (sólido), água (líquido) e vapor (gasoso).",
        "lembra": "É a mesma matéria — muda só o estado.",
    },
    "cn-4c:u8:n2": {
        "explica": "A electricidade dá luz e faz funcionar máquinas. É útil, "
                   "mas perigosa se não se tiver cuidado.",
        "exemplo": "Um fio descarnado pode dar choque, sobretudo com as mãos "
                   "molhadas.",
        "lembra": "Nunca toques em fios eléctricos, muito menos molhados.",
    },
    "cn-4c:u9:n1": {
        "explica": "A agricultura produz os alimentos. Usa instrumentos "
                   "próprios e depende da chuva e do solo.",
        "exemplo": "A enxada serve para cavar e limpar a machamba.",
        "lembra": "Solo bem tratado dá melhor colheita.",
    },

    # ---------------------------------------------------------------
    # Matematica -- 5a classe
    # ---------------------------------------------------------------
    "mat-5c:u1:n1": {
        "explica": "Divisores de um número são os que o dividem sem deixar "
                   "resto. Múltiplos são o que se obtém multiplicando-o.",
        "exemplo": "Divisores de 12: 1, 2, 3, 4, 6 e 12. Múltiplos de 12: "
                   "12, 24, 36...",
        "lembra": "Divisores cabem dentro; múltiplos vão para além.",
    },
    "mat-5c:u1:n2": {
        "explica": "Um número primo só tem dois divisores: o 1 e ele próprio. "
                   "O 1 não é primo.",
        "exemplo": "7 é primo, porque só se divide por 1 e por 7. Já 9 "
                   "divide-se também por 3.",
        "lembra": "Se encontrares um terceiro divisor, já não é primo.",
    },
    "mat-5c:u2:n1": {
        "explica": "A potência diz quantas vezes o número se multiplica por "
                   "si próprio. O número pequeno em cima é o expoente.",
        "exemplo": "2³ = 2 × 2 × 2 = 8. E 5² = 5 × 5 = 25.",
        "lembra": "O expoente conta os factores, não é uma multiplicação por "
                  "ele.",
    },
    "mat-5c:u3:n1": {
        "explica": "Fracções equivalentes valem o mesmo, escritas de maneira "
                   "diferente. Multiplica-se ou divide-se cima e baixo pelo "
                   "mesmo número.",
        "exemplo": "1/2 = 2/4, porque 1×2 = 2 e 2×2 = 4.",
        "lembra": "O que fizeres em cima, faz igual em baixo.",
    },
    "mat-5c:u4:n1": {
        "explica": "Nos decimais, alinha-se sempre a vírgula. Podes juntar "
                   "zeros à direita para as casas ficarem iguais.",
        "exemplo": "2,5 + 1,25: escreve 2,50 + 1,25 = 3,75.",
        "lembra": "Zeros à direita da última casa decimal não mudam o valor.",
    },
    "mat-5c:u5:n1": {
        "explica": "Percentagem é uma parte em cada cem. Para calcular, "
                   "divide-se por 100 e multiplica-se pela percentagem.",
        "exemplo": "10% de 500: 500 : 100 = 5, e 5 × 10 = 50.",
        "lembra": "50% é metade, 25% é um quarto, 10% é dividir por dez.",
    },
    "mat-5c:u6:n1": {
        "explica": "Na circunferência, o raio vai do centro à linha. O "
                   "diâmetro atravessa-a toda e vale dois raios.",
        "exemplo": "Se o raio for 3 cm, o diâmetro é 6 cm.",
        "lembra": "Diâmetro é sempre o dobro do raio.",
    },
    "mat-5c:u7:n1": {
        "explica": "O tempo conta-se de 60 em 60, não de 10 em 10. Meia hora "
                   "são 30 minutos.",
        "exemplo": "Uma hora e meia são 60 + 30 = 90 minutos.",
        "lembra": "Passa tudo a minutos antes de fazer contas com horas.",
    },
    "mat-5c:u8:n1": {
        "explica": "Numa equação, o x é o número que não conhecemos. "
                   "Descobre-se fazendo a operação contrária dos dois lados.",
        "exemplo": "x + 15 = 40. Tira 15 aos dois lados: x = 25.",
        "lembra": "O que fizeres de um lado, faz do outro.",
    },
    "mat-5c:u9:n1": {
        "explica": "Receitas é o dinheiro que entra; despesas é o que sai. "
                   "Quando as despesas passam as receitas, falta dinheiro.",
        "exemplo": "Recebe 3 000 MT e gasta 3 500 MT: fica a dever 500 MT.",
        "lembra": "Gastar menos do que se recebe é o que permite poupar.",
    },
    "mat-5c:u9:n2": {
        "explica": "A conta móvel guarda dinheiro no telemóvel e permite "
                   "enviar e receber. O PIN é a chave dela.",
        "exemplo": "Podes mandar dinheiro à tua família sem sair de casa.",
        "lembra": "O PIN é só teu. Nunca se diz a ninguém.",
    },

    # ---------------------------------------------------------------
    # Portugues -- 5a classe
    # ---------------------------------------------------------------
    "por-5c:u1:n1": {
        "explica": "O plural forma-se quase sempre com s. Mas as palavras "
                   "terminadas em l trocam-no por is, e as em ão mudam de "
                   "várias maneiras.",
        "exemplo": "papel fica papéis; pão fica pães.",
        "lembra": "Termina em l? Troca por is. Termina em ão? Ouve como soa "
                  "no plural.",
    },
    "por-5c:u1:n2": {
        "explica": "O adjectivo tem graus: normal, comparativo (compara dois) "
                   "e superlativo (leva ao extremo).",
        "exemplo": "alto; mais alto do que (comparativo); altíssimo "
                   "(superlativo).",
        "lembra": "Compara dois? Comparativo. Exagera? Superlativo.",
    },
    "por-5c:u2:n1": {
        "explica": "Os pronomes pessoais substituem o nome da pessoa: eu, tu, "
                   "ele, nós, vós, eles.",
        "exemplo": "Nós estudamos na 5ª classe. Nós substitui os nossos "
                   "nomes.",
        "lembra": "O pronome evita repetir o nome a toda a hora.",
    },
    "por-5c:u2:n2": {
        "explica": "Possessivos dizem de quem é (meu, teu, nosso). "
                   "Demonstrativos dizem onde está (este, esse, aquele).",
        "exemplo": "O meu livro é possessivo. Este livro é demonstrativo.",
        "lembra": "De quem é? Possessivo. Qual deles? Demonstrativo.",
    },
    "por-5c:u3:n1": {
        "explica": "O sujeito é quem pratica a acção. O predicado é tudo o "
                   "que se diz do sujeito, e leva o verbo.",
        "exemplo": "«O Carlos estuda.» Sujeito: o Carlos. Predicado: estuda.",
        "lembra": "Pergunta «quem?» ao verbo. A resposta é o sujeito.",
    },
    "por-5c:u3:n2": {
        "explica": "O advérbio diz como, quando ou onde acontece a acção. Não "
                   "muda de forma.",
        "exemplo": "«Ontem estudei aqui.» Ontem é de tempo, aqui é de lugar.",
        "lembra": "Onde, quando ou como — é advérbio.",
    },
    "por-5c:u4:n1": {
        "explica": "O texto poético organiza-se em versos e estrofes. O texto "
                   "didáctico serve para ensinar.",
        "exemplo": "Cada linha de um poema é um verso; um grupo de versos é "
                   "uma estrofe.",
        "lembra": "Olha para a forma no papel: ela já diz que texto é.",
    },
    "por-5c:u5:n1": {
        "explica": "Os verbos dividem-se em três conjugações, pela "
                   "terminação: -ar, -er e -ir.",
        "exemplo": "cantar é da 1ª; comer é da 2ª; partir é da 3ª.",
        "lembra": "Olha para as duas últimas letras do infinitivo.",
    },
    "por-5c:u5:n2": {
        "explica": "O acento agudo abre a vogal; o circunflexo fecha-a. "
                   "Marcam a sílaba mais forte da palavra.",
        "exemplo": "café leva agudo; avô leva circunflexo.",
        "lembra": "Diz a palavra alto: o acento cai onde a voz sobe.",
    },
    "por-5c:u6:n1": {
        "explica": "Família de palavras são as que nascem da mesma raiz. O "
                   "diminutivo faz mais pequeno.",
        "exemplo": "terra, terreno, enterrar são da mesma família. Casa fica "
                   "casinha.",
        "lembra": "Procura o bocado que se repete: é a raiz.",
    },

    # ---------------------------------------------------------------
    # Ciencias Naturais -- 5a classe
    # ---------------------------------------------------------------
    "cn-5c:u1:n1": {
        "explica": "As plantas fabricam o seu alimento pela fotossíntese. "
                   "Precisam de luz do Sol, água e dióxido de carbono.",
        "exemplo": "A folha apanha a luz e transforma-a em alimento, "
                   "libertando oxigénio.",
        "lembra": "A planta não come: fabrica o alimento dela.",
    },
    "cn-5c:u1:n2": {
        "explica": "Vertebrados têm coluna vertebral; invertebrados não têm.",
        "exemplo": "O peixe é vertebrado. A minhoca é invertebrada.",
        "lembra": "Tem ossos nas costas? É vertebrado.",
    },
    "cn-5c:u2:n1": {
        "explica": "A água anda em ciclo: evapora, sobe, condensa em nuvens e "
                   "volta a cair em chuva.",
        "exemplo": "O calor do Sol evapora a água do rio; ao subir arrefece e "
                   "forma nuvens.",
        "lembra": "Evaporação sobe, condensação junta, precipitação cai.",
    },
    "cn-5c:u2:n2": {
        "explica": "A camada de cima do solo é a mais rica. A erosão leva-a "
                   "embora, sobretudo quando não há plantas a segurá-la.",
        "exemplo": "Numa encosta sem árvores, a chuva arrasta a terra boa.",
        "lembra": "Plantar segura o solo; deixar nu deixa-o fugir.",
    },
    "cn-5c:u3:n1": {
        "explica": "A massa é a quantidade de matéria e mede-se em "
                   "quilogramas. O volume é o espaço ocupado.",
        "exemplo": "Um saco de arroz de 5 kg tem 5 kg de massa.",
        "lembra": "Massa é quanto pesa; volume é quanto espaço ocupa.",
    },
    "cn-5c:u4:n1": {
        "explica": "O corpo trabalha por sistemas. O cérebro comanda o "
                   "sistema nervoso; o coração comanda o circulatório.",
        "exemplo": "O coração bombeia o sangue para todo o corpo.",
        "lembra": "Cada sistema tem um órgão principal.",
    },
    "cn-5c:u4:n2": {
        "explica": "Muitas doenças evitam-se com higiene. A malária "
                   "transmite-se pela picada do mosquito.",
        "exemplo": "Lavar as mãos antes de comer evita doenças da barriga.",
        "lembra": "Dormir debaixo da rede tratada é a melhor defesa contra a "
                  "malária.",
    },
    "cn-5c:u4:n3": {
        "explica": "Na puberdade o corpo muda. É natural e acontece a todos, "
                   "cada um no seu tempo.",
        "exemplo": "A voz muda, o corpo cresce, aparecem pêlos.",
        "lembra": "Com as mudanças, a higiene passa a ser ainda mais "
                  "importante.",
    },
    "cn-5c:u5:n1": {
        "explica": "A energia tem muitas formas. A do Sol é solar, a do vento "
                   "é eólica, a da água a correr é hídrica.",
        "exemplo": "Um painel solar transforma a luz do Sol em "
                   "electricidade.",
        "lembra": "O nome da energia vem da sua origem.",
    },
    "cn-5c:u5:n2": {
        "explica": "A luz viaja muito mais depressa do que o som. Por isso "
                   "chega primeiro.",
        "exemplo": "Numa trovoada vês o relâmpago e só depois ouves o trovão.",
        "lembra": "Vê-se primeiro, ouve-se depois — é sempre assim.",
    },

    # ---------------------------------------------------------------
    # Ciencias Sociais -- 5a classe
    # ---------------------------------------------------------------
    "cs-5c:u1:n1": {
        "explica": "Os pontos cardeais são quatro: Norte, Sul, Este e Oeste. "
                   "O Sol nasce a Este e põe-se a Oeste.",
        "exemplo": "De manhã, se olhares para o Sol, tens o Norte à tua "
                   "esquerda.",
        "lembra": "O Sol nasce a Este. Com isso descobres os outros três.",
    },
    "cs-5c:u1:n2": {
        "explica": "Moçambique tem onze províncias e a capital é Maputo. Fica "
                   "na costa oriental de África.",
        "exemplo": "Niassa é uma das onze províncias, no Norte do país.",
        "lembra": "Onze províncias, de Maputo ao Niassa.",
    },
    "cs-5c:u2:n1": {
        "explica": "Os primeiros habitantes viviam da caça e da recolha. "
                   "Depois chegaram os povos bantu, que sabiam trabalhar o "
                   "ferro e cultivar.",
        "exemplo": "Com o ferro fizeram-se enxadas melhores e a agricultura "
                   "cresceu.",
        "lembra": "O ferro e a agricultura mudaram o modo de vida.",
    },
    "cs-5c:u3:n1": {
        "explica": "Os árabes chegaram primeiro à costa, para comerciar. Os "
                   "portugueses vieram depois, no século XV.",
        "exemplo": "Nas cidades da costa trocava-se ouro e marfim por tecidos "
                   "e missangas.",
        "lembra": "Primeiro vieram comerciar; só mais tarde vieram ocupar.",
    },
    "cs-5c:u4:n1": {
        "explica": "A Luta de Libertação Nacional começou a 25 de Setembro de "
                   "1964, para libertar Moçambique do domínio colonial.",
        "exemplo": "Começou no Norte, na província de Cabo Delgado.",
        "lembra": "25 de Setembro de 1964: começa a Luta.",
    },
    "cs-5c:u4:n2": {
        "explica": "Moçambique tornou-se independente a 25 de Junho de 1975, "
                   "depois de dez anos de luta.",
        "exemplo": "Nesse dia foi hasteada pela primeira vez a Bandeira "
                   "Nacional.",
        "lembra": "25 de Junho de 1975: Independência.",
    },
    "cs-5c:u5:n1": {
        "explica": "A Bandeira tem quatro cores — verde, preto, amarelo e "
                   "vermelho — e ainda o branco a separar. Traz também "
                   "símbolos.",
        "exemplo": "Na Bandeira estão o livro, a enxada e a arma, sobre uma "
                   "estrela.",
        "lembra": "Livro é a educação, enxada é o trabalho, estrela é o "
                  "internacionalismo.",
    },
    "cs-5c:u5:n2": {
        "explica": "Depois da Independência o Estado tomou para si a terra, a "
                   "saúde e a educação, e as cidades mudaram de nome.",
        "exemplo": "Lourenço Marques passou a chamar-se Maputo.",
        "lembra": "Mudar os nomes foi também uma forma de recomeçar.",
    },
    "cs-5c:u6:n1": {
        "explica": "Direitos são o que nos é devido; deveres são o que "
                   "devemos aos outros. Andam sempre a par.",
        "exemplo": "Todas as crianças têm direito à educação e à saúde.",
        "lembra": "Não há direitos sem deveres.",
    },

    # ---------------------------------------------------------------
    # Matematica -- 6a classe
    # ---------------------------------------------------------------
    "mat-6c:u1:n1": {
        "explica": "Numa expressão resolvem-se primeiro os parênteses, depois "
                   "as potências, depois multiplicações e divisões, e só no "
                   "fim somas e subtracções.",
        "exemplo": "2 + 3 × 4: primeiro 3 × 4 = 12, depois 2 + 12 = 14.",
        "lembra": "Da esquerda para a direita só dentro do mesmo nível.",
    },
    "mat-6c:u1:n2": {
        "explica": "Os números negativos estão à esquerda do zero na recta. "
                   "Quanto maior o número depois do sinal menos, menor ele é.",
        "exemplo": "−2 é maior que −5, porque está mais perto do zero.",
        "lembra": "Nos negativos, é ao contrário: o que parece maior é menor.",
    },
    "mat-6c:u2:n1": {
        "explica": "O m.d.c. é o maior número que divide os dois. O m.m.c. é "
                   "o menor múltiplo que ambos têm em comum.",
        "exemplo": "12 e 18: o m.d.c. é 6. Já 4 e 6 têm m.m.c. 12.",
        "lembra": "Divisor comum é menor ou igual aos números; múltiplo comum "
                  "é maior ou igual.",
    },
    "mat-6c:u3:n1": {
        "explica": "Ao multiplicar potências com a mesma base, somam-se os "
                   "expoentes.",
        "exemplo": "2² × 2³ = 2⁵ = 32. E 3⁴ = 3 × 3 × 3 × 3 = 81.",
        "lembra": "Mesma base a multiplicar: soma os expoentes.",
    },
    "mat-6c:u4:n1": {
        "explica": "Para somar fracções de denominador diferente, passa-se "
                   "primeiro ao mesmo denominador.",
        "exemplo": "1/2 + 1/3: passa a 3/6 + 2/6 = 5/6.",
        "lembra": "Multiplicar fracções é directo: cima com cima, baixo com "
                  "baixo.",
    },
    "mat-6c:u4:n2": {
        "explica": "Ao multiplicar decimais, conta-se o total de casas "
                   "decimais dos dois números. Ao dividir, tira-se a vírgula "
                   "do divisor.",
        "exemplo": "2,5 × 4 = 10. E 7,5 : 2,5 = 3.",
        "lembra": "Na multiplicação, o resultado tem tantas casas quantas as "
                  "duas parcelas juntas.",
    },
    "mat-6c:u5:n1": {
        "explica": "Um desconto tira uma percentagem do preço. Calcula-se a "
                   "percentagem e subtrai-se.",
        "exemplo": "500 MT com 10% de desconto: 10% de 500 é 50, logo paga-se "
                   "450 MT.",
        "lembra": "Desconto tira; imposto acrescenta.",
    },
    "mat-6c:u6:n1": {
        "explica": "A área do triângulo é base vezes altura a dividir por "
                   "dois — é meio rectângulo.",
        "exemplo": "Base 10 cm e altura 6 cm: 10 × 6 = 60, a dividir por 2 dá "
                   "30 cm quadrados.",
        "lembra": "Não te esqueças de dividir por dois.",
    },
    "mat-6c:u7:n1": {
        "explica": "Converter é mudar de unidade sem mudar a quantidade. Para "
                   "unidade menor, multiplica-se.",
        "exemplo": "2,5 m = 250 cm. E 1 tonelada = 1 000 kg.",
        "lembra": "Unidade menor, número maior. Sempre.",
    },
    "mat-6c:u8:n1": {
        "explica": "Para resolver uma equação, isola-se o x fazendo a "
                   "operação contrária dos dois lados.",
        "exemplo": "2x + 5 = 19. Tira 5: 2x = 14. Divide por 2: x = 7.",
        "lembra": "Desfaz primeiro a soma, só depois a multiplicação.",
    },

    # ---------------------------------------------------------------
    # Portugues -- 6a classe
    # ---------------------------------------------------------------
    "por-6c:u1:n1": {
        "explica": "O sujeito é quem pratica a acção e pode ter várias "
                   "palavras. Quando não aparece na frase, diz-se "
                   "subentendido.",
        "exemplo": "«Os alunos da 6ª classe estudam muito.» O sujeito é toda "
                   "a expressão os alunos da 6ª classe.",
        "lembra": "Pergunta «quem?» ao verbo e leva tudo o que vier agarrado.",
    },
    "por-6c:u1:n2": {
        "explica": "O complemento directo completa o verbo sem preposição. Um "
                   "verbo transitivo é o que precisa de complemento.",
        "exemplo": "«A Maria comprou um livro.» Um livro é complemento "
                   "directo.",
        "lembra": "Pergunta «o quê?» ao verbo: se responde sem preposição, é "
                  "directo.",
    },
    "por-6c:u2:n1": {
        "explica": "O indicativo afirma factos, o conjuntivo exprime dúvida "
                   "ou desejo, o imperativo dá ordens.",
        "exemplo": "«Se eu estudasse» é conjuntivo; «Estuda!» é imperativo.",
        "lembra": "Facto é indicativo; hipótese é conjuntivo; ordem é "
                  "imperativo.",
    },
    "por-6c:u2:n2": {
        "explica": "Na voz activa o sujeito faz a acção. Na passiva, sofre-a.",
        "exemplo": "«O caçador viu o leão» é activa. «O leão foi visto pelo "
                   "caçador» é passiva.",
        "lembra": "Se aparece o verbo ser mais particípio, é passiva.",
    },
    "por-6c:u3:n1": {
        "explica": "O discurso directo reproduz as palavras tal como foram "
                   "ditas, com travessão ou aspas. O indirecto conta-as.",
        "exemplo": "Directo: — Estou cansado, disse ele. Indirecto: Ele disse "
                   "que estava cansado.",
        "lembra": "Travessão ou aspas? Directo.",
    },
    "por-6c:u4:n1": {
        "explica": "O determinante acompanha o nome; o pronome substitui-o.",
        "exemplo": "«O meu livro»: meu é determinante. «O meu está aqui»: meu "
                   "é pronome.",
        "lembra": "Se o nome está lá ao lado, é determinante.",
    },
    "por-6c:u4:n2": {
        "explica": "O superlativo relativo compara com todos os outros. Os "
                   "advérbios classificam-se pelo sentido que dão.",
        "exemplo": "«O mais alto de todos» é superlativo relativo. «Talvez» é "
                   "advérbio de dúvida.",
        "lembra": "De todos? Superlativo relativo.",
    },
    "por-6c:u5:n1": {
        "explica": "Algumas palavras confundem-se por soarem parecido. "
                   "Escreve-se pelo significado, não pelo som.",
        "exemplo": "houve é do verbo haver; ouve é do verbo ouvir.",
        "lembra": "Na dúvida, troca a palavra por outra da mesma família.",
    },
    "por-6c:u5:n2": {
        "explica": "Um texto organiza-se em introdução, desenvolvimento e "
                   "conclusão. O resumo guarda só o essencial.",
        "exemplo": "A introdução apresenta o assunto; a conclusão fecha-o.",
        "lembra": "Um resumo não copia frases: diz o mesmo por outras "
                  "palavras.",
    },
    "por-6c:u6:n1": {
        "explica": "A ideia principal costuma estar no início ou no fim do "
                   "parágrafo. A personagem principal é aquela à volta de "
                   "quem gira a história.",
        "exemplo": "Se tirares a personagem principal, a história deixa de "
                   "existir.",
        "lembra": "Lê o primeiro e o último período de cada parágrafo.",
    },

    # ---------------------------------------------------------------
    # Ciencias Naturais -- 6a classe
    # ---------------------------------------------------------------
    "cn-6c:u1:n1": {
        "explica": "A flor tem estames, que produzem o pólen, e o pistilo, "
                   "que o recebe. A polinização leva o pólen de uma flor a "
                   "outra.",
        "exemplo": "A abelha, ao procurar néctar, leva o pólen no corpo.",
        "lembra": "Sem polinização não há fruto nem semente.",
    },
    "cn-6c:u1:n2": {
        "explica": "Numa cadeia alimentar, as plantas são produtoras. Quem "
                   "come plantas é consumidor primário; quem come esses é "
                   "secundário.",
        "exemplo": "Capim, zebra, leão: o leão é consumidor secundário.",
        "lembra": "Conta os degraus desde a planta.",
    },
    "cn-6c:u2:n1": {
        "explica": "O coração bombeia o sangue; os pulmões trocam o oxigénio. "
                   "Cada sistema tem a sua função.",
        "exemplo": "A troca de oxigénio acontece nos alvéolos dos pulmões.",
        "lembra": "Coração empurra, pulmão troca.",
    },
    "cn-6c:u2:n2": {
        "explica": "A malária é causada por um parasita transmitido pelo "
                   "mosquito. A tuberculose ataca sobretudo os pulmões.",
        "exemplo": "A rede mosquiteira tratada corta a transmissão da "
                   "malária.",
        "lembra": "Prevenir é sempre mais barato do que tratar.",
    },
    "cn-6c:u3:n1": {
        "explica": "O ciclo da água inclui evaporação, condensação e "
                   "precipitação. A poluição estraga-a em qualquer ponto do "
                   "ciclo.",
        "exemplo": "Lixo e esgotos lançados no rio poluem a água de quem vive "
                   "a jusante.",
        "lembra": "A água que sujas aqui, alguém bebe mais abaixo.",
    },
    "cn-6c:u4:n1": {
        "explica": "A luz reflecte-se quando bate numa superfície e volta. O "
                   "eco é a reflexão do som.",
        "exemplo": "Gritas contra uma parede ao longe e ouves a tua voz "
                   "voltar.",
        "lembra": "Reflexão é bater e voltar — vale para a luz e para o som.",
    },
    "cn-6c:u4:n2": {
        "explica": "Máquinas simples facilitam o trabalho. A alavanca, a "
                   "roldana e o plano inclinado são exemplos.",
        "exemplo": "A tesoura são duas alavancas presas pelo mesmo ponto.",
        "lembra": "Não fazem menos trabalho: tornam-no mais fácil.",
    },
    "cn-6c:u5:n1": {
        "explica": "Para a corrente passar, o circuito tem de estar fechado. "
                   "Os metais conduzem; a madeira e o plástico não.",
        "exemplo": "Se o interruptor estiver aberto, a lâmpada não acende.",
        "lembra": "Circuito aberto não passa corrente.",
    },

    # ---------------------------------------------------------------
    # Ciencias Sociais -- 6a classe
    # ---------------------------------------------------------------
    "cs-6c:u1:n1": {
        "explica": "Os paralelos são as linhas horizontais e os meridianos as "
                   "verticais. Cruzam-se para dar a posição exacta.",
        "exemplo": "O Equador é o paralelo principal; Greenwich é o meridiano "
                   "principal.",
        "lembra": "Paralelos acompanham o Equador; meridianos ligam os polos.",
    },
    "cs-6c:u2:n1": {
        "explica": "África tem o maior deserto quente do mundo, o Sara, no "
                   "Norte, e o rio mais longo, o Nilo.",
        "exemplo": "O Nilo corre para norte e desagua no Mediterrâneo.",
        "lembra": "Sara e Nilo ficam ambos no Norte de África.",
    },
    "cs-6c:u2:n2": {
        "explica": "Moçambique fica na África Austral e pertence à SADC, a "
                   "Comunidade de Desenvolvimento da África Austral.",
        "exemplo": "A SADC junta países vizinhos para trabalharem em "
                   "conjunto.",
        "lembra": "SADC é dos países do Sul; UA é de África toda.",
    },
    "cs-6c:u3:n1": {
        "explica": "Na Conferência de Berlim, em 1884-85, as potências "
                   "europeias repartiram África entre si, sem ouvir os "
                   "africanos.",
        "exemplo": "As fronteiras que foram traçadas nessa altura são, em "
                   "muitos casos, as de hoje.",
        "lembra": "Berlim dividiu África numa mesa, longe de África.",
    },
    "cs-6c:u4:n1": {
        "explica": "Moçambique tornou-se independente em 1975. O Acordo Geral "
                   "de Paz, que pôs fim à guerra, foi assinado em Roma em "
                   "1992.",
        "exemplo": "Entre a Independência e a Paz passaram-se dezassete anos.",
        "lembra": "1975 Independência; 1992 Paz.",
    },
    "cs-6c:u4:n2": {
        "explica": "Votar é um direito e um dever dos cidadãos. A diversidade "
                   "cultural do país é uma riqueza.",
        "exemplo": "Em Moçambique falam-se muitas línguas além do português.",
        "lembra": "Cidadania é participar, não só receber.",
    },
    "cs-6c:u5:n1": {
        "explica": "A maior parte dos moçambicanos vive no campo, mas as "
                   "cidades crescem. A esse crescimento chama-se urbanização.",
        "exemplo": "Muita gente vai do campo para a cidade à procura de "
                   "trabalho.",
        "lembra": "Urbanização é a população a mudar-se para as cidades.",
    },
    "cs-6c:u5:n2": {
        "explica": "No campo, a principal actividade é a agricultura. Na "
                   "costa e nos lagos, a pesca.",
        "exemplo": "No lago Niassa a pesca sustenta muitas famílias.",
        "lembra": "A actividade de cada zona depende do que a terra e a água "
                  "dão.",
    },
    "cs-6c:u6:n1": {
        "explica": "Há datas que marcam a história do país e convém saber de "
                   "cor.",
        "exemplo": "1884-85 Berlim; 1964 início da Luta; 1975 Independência; "
                   "1992 Paz.",
        "lembra": "Põe as datas por ordem: cada uma explica a seguinte.",
    },

    # ---------------------------------------------------------------
    # Portugues -- 4a classe
    #
    # Do Caderno de Actividades de Lingua Portuguesa da 4a Classe,
    # MINEDH/MEC 2025. As unidades sao as tematicas do livro -- Familia,
    # Escola, Comunidade... -- e a gramatica entra dentro do tema, como
    # ali esta.
    # ---------------------------------------------------------------
    "por-4c:u1:n1": {
        "explica": "Os princípios de cortesia servem para falarmos uns com "
                   "os outros com delicadeza e respeito. Ouve-se quem fala, "
                   "espera-se pela nossa vez e respeita-se o assunto da "
                   "conversa.",
        "exemplo": "Com pessoas de respeito diz-se «Bom dia, senhora "
                   "professora!»; entre amigos diz-se «Olá, amiga!».",
        "lembra": "Por favor, com licença, obrigado, desculpe — são as "
                  "palavras da cortesia.",
    },
    "por-4c:u1:n2": {
        "explica": "Os nomes comuns designam seres de uma mesma espécie: "
                   "irmã, amigo, prato. Os nomes próprios designam um em "
                   "especial e escrevem-se sempre com letra maiúscula.",
        "exemplo": "cidade é nome comum; Tete é nome próprio.",
        "lembra": "Nome próprio começa por maiúscula. Se não começa, é comum.",
    },
    "por-4c:u1:n3": {
        "explica": "Os nomes terminados em ão não fazem todos o plural da "
                   "mesma maneira. Uns ficam em ãos, outros em ães e outros "
                   "em ões.",
        "exemplo": "mão fica mãos; pão fica pães; coração fica corações.",
        "lembra": "Diz a palavra no plural em voz alta: o ouvido acerta "
                  "antes da regra.",
    },
    "por-4c:u2:n1": {
        "explica": "Há quatro tipos de frase. A declarativa conta, a "
                   "imperativa manda, a exclamativa mostra o que se sente e "
                   "a interrogativa pergunta.",
        "exemplo": "A Lurdes gosta de aprender. Fecha a porta, Tânia! Ah! "
                   "Que presente bonito! Onde está o teu material?",
        "lembra": "Olha o sinal no fim: ponto conta, exclamação sente, "
                  "interrogação pergunta.",
    },
    "por-4c:u2:n2": {
        "explica": "O sujeito é quem faz a acção e o predicado é o que ele "
                   "faz. O texto narrativo conta uma história, com "
                   "personagens, tempo e lugar.",
        "exemplo": "Em «O Gabriel vive numa casa bonita», o sujeito é O "
                   "Gabriel e o predicado é vive numa casa bonita.",
        "lembra": "Pergunta «quem?» para achar o sujeito e «faz o quê?» "
                  "para o predicado.",
    },
    "por-4c:u3:n1": {
        "explica": "As preposições são palavras invariáveis que ligam "
                   "elementos da frase: a, com, de, em, para, por, sobre, "
                   "sem, até.",
        "exemplo": "A Célia vai à machamba com a avó. A preposição é com.",
        "lembra": "A preposição nunca muda: não tem masculino, feminino nem "
                  "plural.",
    },
    "por-4c:u4:n1": {
        "explica": "O verbo diz quando a acção acontece. O presente é "
                   "agora, o pretérito perfeito é o que já passou e o "
                   "futuro é o que ainda vem.",
        "exemplo": "Hoje estudo; ontem estudei; amanhã estudarei.",
        "lembra": "Ontem, hoje, amanhã — o verbo muda com cada um.",
    },
    "por-4c:u4:n2": {
        "explica": "Os sinais de pontuação arrumam a frase. Um nome "
                   "colectivo é um só nome para um conjunto de seres da "
                   "mesma espécie.",
        "exemplo": "Muitas árvores juntas são uma floresta; muitos bois são "
                   "uma manada.",
        "lembra": "Pergunta acaba em ponto de interrogação. O conjunto tem "
                  "nome só dele.",
    },
    "por-4c:u5:n1": {
        "explica": "A frase simples tem um só verbo principal. Começa por "
                   "letra maiúscula e acaba com um sinal de pontuação.",
        "exemplo": "A Maria lavou as mãos. É simples: só tem o verbo lavou.",
        "lembra": "Conta os verbos. Um só verbo, frase simples.",
    },
    "por-4c:u6:n1": {
        "explica": "Os pronomes possessivos dizem de quem é a coisa, e "
                   "mudam com o género e com o número.",
        "exemplo": "Esta é a minha mão; estas são as minhas mãos; esse é o "
                   "teu livro.",
        "lembra": "De mim é meu ou minha; de ti é teu ou tua.",
    },
    "por-4c:u7:n1": {
        "explica": "Os advérbios de tempo dizem quando a acção acontece: "
                   "ontem, hoje, amanhã, cedo, tarde, nunca, sempre.",
        "exemplo": "O comboio chegou cedo. Cedo diz quando ele chegou.",
        "lembra": "Pergunta «quando?» — a resposta é o advérbio de tempo.",
    },
    "por-4c:u8:n1": {
        "explica": "Os meios de comunicação levam a mensagem de uns aos "
                   "outros: a rádio, a televisão, o jornal, o telefone, a "
                   "carta e o postal. Os advérbios de modo dizem como a "
                   "acção acontece.",
        "exemplo": "A Ana escreveu depressa. Depressa diz como ela escreveu.",
        "lembra": "«Quando?» é tempo; «como?» é modo.",
    },
    "por-4c:u9:n1": {
        "explica": "Os advérbios de negação dizem que a acção não acontece: "
                   "não, nunca, jamais, nada.",
        "exemplo": "«Eu fui à escola» fica «Eu não fui à escola».",
        "lembra": "Basta um «não» antes do verbo para negar a frase toda.",
    },

    # ---------------------------------------------------------------
    # Ciencias Sociais -- 4a classe
    #
    # Do Caderno de Actividades de Ciencias Sociais da 4a Classe,
    # MINEDH/MEC 2025. As definicoes com numeros -- os 200 metros da
    # planicie, os 30 anos do clima -- foram lidas no livro e nao
    # escritas de cor.
    # ---------------------------------------------------------------
    "cs-4c:u1:n1": {
        "explica": "A família é um conjunto de pessoas unidas por laço de "
                   "sangue, pelo matrimónio ou pela adopção. Há a família "
                   "nuclear, a monoparental e a alargada.",
        "exemplo": "Pai, mãe e filhos são uma família nuclear. Se só um dos "
                   "pais cria os filhos, é monoparental.",
        "lembra": "Avós são os pais dos meus pais; tios são os irmãos deles.",
    },
    "cs-4c:u1:n2": {
        "explica": "Viver em família é repartir tarefas e resolver as "
                   "zangas a conversar. Cada membro tem os seus deveres.",
        "exemplo": "A árvore genealógica mostra, num desenho, quem são os "
                   "parentes de uma família.",
        "lembra": "Conflito resolve-se a falar, nunca à força.",
    },
    "cs-4c:u1:n3": {
        "explica": "A criança tem direitos — à vida, a um nome, à saúde, a "
                   "uma família, à educação e a brincar — e tem deveres, "
                   "como respeitar os outros e estudar.",
        "exemplo": "Ter um nome é um direito; cuidar do material escolar é "
                   "um dever.",
        "lembra": "Direito é o que recebo; dever é o que faço.",
    },
    "cs-4c:u2:n1": {
        "explica": "Comunidade é o conjunto de pessoas que vivem juntas. Há "
                   "a rural, a urbana, a religiosa e a educativa.",
        "exemplo": "Quem vive no campo forma uma comunidade rural; quem "
                   "vive na cidade, uma urbana.",
        "lembra": "Usos e costumes passam de geração para geração.",
    },
    "cs-4c:u2:n2": {
        "explica": "A lenda explica acontecimentos misteriosos e mistura "
                   "factos reais com fantasia. O conto passa dos mais "
                   "velhos para os mais novos.",
        "exemplo": "Há contos realistas, populares, de humor e infantis. Os "
                   "infantis deixam uma lição.",
        "lembra": "Lenda explica; conto conta.",
    },
    "cs-4c:u2:n3": {
        "explica": "Na comunidade fala-se português e línguas moçambicanas, "
                   "e as pessoas vivem de actividades como a agricultura, a "
                   "pesca e o comércio.",
        "exemplo": "A dança e a música tradicional são cultura da "
                   "comunidade.",
        "lembra": "Quem é diferente de mim merece o mesmo respeito.",
    },
    "cs-4c:u3:n1": {
        "explica": "A escola é a nossa segunda casa. Tem um regulamento "
                   "interno com as regras, e conservá-la é tarefa de todos.",
        "exemplo": "Limpar o pátio e as salas é ajudar a conservar a escola.",
        "lembra": "Na escola, como em casa, a zanga resolve-se a falar.",
    },
    "cs-4c:u4:n1": {
        "explica": "Moçambique divide-se em províncias, distritos, postos "
                   "administrativos, localidades e povoações.",
        "exemplo": "O Administrador dirige o distrito; o Conselho "
                   "Autárquico é o órgão executivo do município.",
        "lembra": "Do maior para o menor: província, distrito, posto, "
                  "localidade.",
    },
    "cs-4c:u4:n2": {
        "explica": "Relevo são as formas como a Terra se apresenta: "
                   "planícies, planaltos e montanhas. Clima é o tempo que "
                   "se repete durante trinta anos ou mais.",
        "exemplo": "A planície fica abaixo dos 200 metros; o planalto, "
                   "acima. Um rio pequeno que desagua num maior é um "
                   "afluente.",
        "lembra": "Tempo é hoje; clima são trinta anos.",
    },
    "cs-4c:u4:n3": {
        "explica": "Os meios de transporte levam pessoas e coisas. Na "
                   "estrada há sinais de trânsito, e cumpri-los é o que "
                   "nos mantém vivos.",
        "exemplo": "Antes de atravessar, olha para os dois lados.",
        "lembra": "Queimar a floresta degrada o ambiente; plantar repõe-o.",
    },
    "cs-4c:u5:n1": {
        "explica": "Necessidade é o que é indispensável para viver. Desejo "
                   "é o que apetece ter. Não se deve tratar um desejo como "
                   "se fosse uma necessidade.",
        "exemplo": "Comida e remédios são necessidades; um brinquedo novo "
                   "é um desejo.",
        "lembra": "Primeiro o que é preciso, depois o que apetece.",
    },
    # ---------------------------------------------------------------
    # Educacao Visual e Oficios -- 6a classe
    #
    # Do livro de Educacao Visual da 6a classe, MEC 2024. E a disciplina
    # de FAZER, e por isso a materia fala do que se decide antes de por
    # as maos na obra. A cor mostra-se no ecra; aqui a materia so lhe
    # da os nomes.
    # ---------------------------------------------------------------
    "ev-6c:u1:n1": {
        "explica": "Antes de comecar um trabalho junta-se tudo o que se "
                   "vai precisar, e no fim deixa-se o espaco limpo para "
                   "quem vem a seguir.",
        "exemplo": "Para desenhar: o lapis bem afiado, a borracha e a "
                   "folha, tudo a mao antes de a primeira linha ser feita.",
        "lembra": "Primeiro juntar, depois fazer, e sempre limpar.",
    },
    "ev-6c:u1:n2": {
        "explica": "Ha muitos materiais riscadores: lapis de carvao, giz, "
                   "carvao vegetal, lapis de cor, lapis de cera. Escolhe-se "
                   "conforme o desenho que se quer.",
        "exemplo": "A mina dura risca fino e serve o desenho rigoroso; a "
                   "macia risca grosso e serve o desenho a mao livre.",
        "lembra": "O material escolhe-se depois de saber o que se vai "
                  "desenhar, nunca antes.",
    },
    "ev-6c:u2:n1": {
        "explica": "As cores primarias nao saem de mistura nenhuma: sao "
                   "puras. Sao tres -- o azul, o amarelo e o vermelho.",
        "exemplo": "O verde nao e primaria, porque se faz juntando duas.",
        "lembra": "Azul, amarelo e vermelho: destas tres saem as outras.",
    },
    "ev-6c:u2:n2": {
        "explica": "Juntando duas cores primarias nasce uma cor "
                   "secundaria. Sao tres: o laranja, o verde e o violeta.",
        "exemplo": "Amarelo com vermelho da laranja; amarelo com azul da "
                   "verde; vermelho com azul da violeta.",
        "lembra": "Duas primarias juntas fazem sempre uma secundaria.",
    },
    "ev-6c:u2:n3": {
        "explica": "Tons sao as tonalidades dentro da mesma cor. Junta-se "
                   "branco para clarear e preto para escurecer.",
        "exemplo": "Ao preto com um pouco de branco chama-se cinzento.",
        "lembra": "O preto e o branco nao sao cores do arco-iris: sao "
                  "cores neutras.",
    },
    "ev-6c:u3:n1": {
        "explica": "Cada tinta pede a sua tecnica. A aguarela mistura-se "
                   "com agua, o guache e mais espesso, e as tintas "
                   "artesanais fazem-se com o que ha na comunidade.",
        "exemplo": "Depois de pintar, o pincel lava-se e poe-se a secar "
                   "com os pelos para cima.",
        "lembra": "Pincel sujo que seca fica perdido.",
    },
    "ev-6c:u4:n1": {
        "explica": "Imprimir e estampar e passar um desenho de uma "
                   "superficie para outra, e repeti-lo quantas vezes se "
                   "quiser.",
        "exemplo": "Com o dedo pintado faz-se impressao digital; com um "
                   "carimbo repete-se o mesmo desenho ao longo do papel.",
        "lembra": "Poe sempre uma proteccao por baixo antes de comecar.",
    },
    "ev-6c:u5:n1": {
        "explica": "O papel corta-se, dobra-se, pica-se e cola-se. Cada "
                   "uma destas e uma tecnica com a sua regra.",
        "exemplo": "Na dobragem o papel nao se corta; no recorte corta-se "
                   "pela linha marcada.",
        "lembra": "A tesoura passa-se com as pontas viradas para quem a "
                  "da, nunca para quem a recebe.",
    },
    # ---------------------------------------------------------------
    # Educacao Visual e Oficios -- 5a classe
    #
    # Do livro EVO da 5a classe, 2023. Ao contrario da 6a, esta e sobretudo
    # OFICIO: barro, fibras, cestaria. Nao tem cor porque o livro nao a
    # ensina nesta classe.
    # ---------------------------------------------------------------
    "ev-5c:u1:n1": {
        "explica": "Antes de comecar junta-se tudo o que se vai precisar, e "
                   "no fim deixa-se o espaco limpo para quem vem a seguir.",
        "exemplo": "Antes da aula: os lapis afiados. Antes de pintar: a "
                   "mesa forrada.",
        "lembra": "Preparar antes custa um minuto; limpar depois custa a "
                  "aula toda.",
    },
    "ev-5c:u1:n2": {
        "explica": "Ha varias maneiras de desenhar. De observacao e "
                   "desenhar o que se tem a frente; com tema dado e "
                   "desenhar o assunto que o professor disse.",
        "exemplo": "A ilustracao acompanha um texto e ajuda a explica-lo. "
                   "Um painel colectivo faz-se com os colegas todos.",
        "lembra": "Olha primeiro, desenha depois.",
    },
    "ev-5c:u2:n1": {
        "explica": "Imprimir e estampar e passar um desenho de uma "
                   "superficie para outra, e repeti-lo quantas vezes se "
                   "quiser.",
        "exemplo": "Uma batata cortada ao meio e mergulhada em tinta faz um "
                   "carimbo.",
        "lembra": "Poe sempre uma proteccao por baixo antes de comecar.",
    },
    "ev-5c:u2:n2": {
        "explica": "O papel corta-se, dobra-se, pica-se e cola-se. Cada uma "
                   "destas e uma tecnica com a sua regra.",
        "exemplo": "Na dobragem o papel nao se corta; no picotado fazem-se "
                   "muitos furos pequenos seguidos.",
        "lembra": "A tesoura passa-se pelo cabo, com as pontas seguras na "
                  "nossa mao.",
    },
    "ev-5c:u3:n1": {
        "explica": "Modelagem e dar forma a uma materia-prima modelavel. "
                   "Moldagem e reproduzir um objecto atraves de um molde.",
        "exemplo": "Um vaso feito a mao com barro e modelagem; dez vasos "
                   "iguais tirados do mesmo molde sao moldagem.",
        "lembra": "A vantagem da modelagem: ve-se a peca de todos os lados.",
    },
    "ev-5c:u3:n2": {
        "explica": "O barro prepara-se por passos: limpa-se, peneira-se "
                   "para tirar as pedras, mistura-se com agua e amassa-se.",
        "exemplo": "Amassa-se ate a massa ficar homogenea e deixar de se "
                   "colar as maos.",
        "lembra": "Guarda o barro num plastico, senao seca e perde-se.",
    },
    "ev-5c:u4:n1": {
        "explica": "As fibras naturais saem da natureza -- algodao, sisal, "
                   "la, linho. As artificiais fazem-se na industria, como o "
                   "nylon. As reciclaveis sao reaproveitadas.",
        "exemplo": "Os fios dos sacos de comida, guardados e reaproveitados, "
                   "sao fibras reciclaveis.",
        "lembra": "Vem da planta ou do animal? E natural. Vem da fabrica? E "
                  "artificial.",
    },
    "ev-5c:u4:n2": {
        "explica": "Tecer e entrelacar fios. A cestaria usa o mesmo "
                   "processo, com palha, bambu ou fitas de plastico.",
        "exemplo": "Da cestaria saem cestos, chapeus, peneiras e esteiras.",
        "lembra": "Tecelagem e cestaria sao a mesma ideia: entrelacar.",
    },
}
