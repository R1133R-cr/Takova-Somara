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
    # ---------------------------------------------------------------
    # Educacao Visual e Oficios -- 4a classe
    #
    # ESTRUTURA PROVISORIA, SEM FONTE CONFIRMADA. Nao ha manual de EV da
    # 4a classe publicado. Ver o cabecalho do conteudo_ev4c.py.
    # ---------------------------------------------------------------
    "ev-4c:u1:n1": {
        "explica": "Um trabalho manual comeca antes do trabalho: junta-se "
                   "tudo o que se vai precisar e prepara-se a mesa.",
        "exemplo": "Antes de pintar, poe-se papel ou jornal por baixo para "
                   "a mesa nao ficar suja.",
        "lembra": "Quem prepara antes nao interrompe depois.",
    },
    "ev-4c:u1:n2": {
        "explica": "As ferramentas cortam e furam, e por isso pedem regras. "
                   "Guardam-se no seu lugar depois de usadas.",
        "exemplo": "A tesoura passa-se pelo cabo: seguras nas pontas e "
                   "das-lhe o cabo a quem a recebe.",
        "lembra": "Com a tesoura na mao, ninguem corre.",
    },
    "ev-4c:u2:n1": {
        "explica": "Desenha-se com muitos materiais: lapis, giz, carvao "
                   "vegetal. Cada um risca de sua maneira.",
        "exemplo": "Um lapis bem afiado risca fino; um lapis rombo risca "
                   "grosso.",
        "lembra": "O lapis afia-se antes da aula, nao a meio dela.",
    },
    "ev-4c:u2:n2": {
        "explica": "Desenhar o que se tem a frente e desenho de "
                   "observacao. Desenhar o que apetece e desenho livre.",
        "exemplo": "Antes de desenhar uma cadeira, olha-se bem para ela: "
                   "quantas pernas tem, onde e o encosto.",
        "lembra": "Olha primeiro, desenha depois.",
    },
    "ev-4c:u3:n1": {
        "explica": "Recortar e colar sao duas tecnicas que andam juntas: "
                   "corta-se o papel e junta-se numa folha.",
        "exemplo": "Marca-se a linha a lapis, corta-se por cima dela, e "
                   "cola-se com pouca cola bem espalhada.",
        "lembra": "Muita cola enruga o papel. Pouca e melhor.",
    },
    "ev-4c:u3:n2": {
        "explica": "Na dobragem o papel dobra-se sem se cortar. No "
                   "picotado fazem-se muitos furos pequenos seguidos.",
        "exemplo": "Passa-se a unha por cima do vinco para a dobra ficar "
                   "direita.",
        "lembra": "Dobrar nao e cortar: o papel fica inteiro.",
    },
    "ev-4c:u4:n1": {
        "explica": "Na nossa comunidade ha muitos oficios feitos com as "
                   "maos: cestaria, costura, carpintaria, jardinagem.",
        "exemplo": "Quem faz cestos e esteiras com palha trabalha na "
                   "cestaria; quem trabalha a madeira e carpinteiro.",
        "lembra": "Cada oficio tem o seu material e a sua tecnica.",
    },
    "ev-4c:u4:n2": {
        "explica": "Os materiais dos trabalhos manuais vem muitas vezes da "
                   "natureza que temos a volta: argila, palha, bambu.",
        "exemplo": "Com argila fazem-se vasos e panelas; com palha e bambu, "
                   "cestos e esteiras.",
        "lembra": "Um saco velho reaproveitado tambem e material.",
    },

    # ---------------------------------------------------------------
    # Matematica -- 7a classe  (1o ciclo do Ensino Secundario)
    #
    # O tom sobe com a idade. Um aluno de doze anos nao precisa de frases
    # de cinco palavras; precisa de uma definicao que aguente ser lida
    # duas vezes, e de um exemplo que se possa copiar para o caderno.
    # ---------------------------------------------------------------
    "mat-7c:u1:n1": {
        "explica": "Um conjunto é uma colecção de objectos bem definidos, a "
                   "que chamamos elementos. Escreve-se entre chavetas. O "
                   "número de elementos chama-se cardinal.",
        "exemplo": "A = {2, 4, 6, 8, 10}. Os elementos são 2, 4, 6, 8 e 10. "
                   "O cardinal de A é 5. Dizemos 4 ∈ A e 5 ∉ A.",
        "lembra": "∈ liga um elemento a um conjunto: pertence ou não pertence.",
    },
    "mat-7c:u1:n2": {
        "explica": "A reunião de dois conjuntos junta todos os elementos dos "
                   "dois. A intersecção fica só com os que estão nos dois ao "
                   "mesmo tempo. Um conjunto está contido noutro quando "
                   "todos os seus elementos também são do outro.",
        "exemplo": "A = {1, 2, 3} e B = {3, 4}. A ∪ B = {1, 2, 3, 4}, que "
                   "tem 4 elementos. A ∩ B = {3}, que tem 1.",
        "lembra": "Reunião junta tudo; intersecção guarda só o que se repete.",
    },
    "mat-7c:u1:n3": {
        "explica": "Aos números naturais juntam-se agora os negativos. Na "
                   "recta numérica, os negativos ficam à esquerda do zero. O "
                   "simétrico de um número está do outro lado do zero, à "
                   "mesma distância. O módulo é essa distância, e nunca é "
                   "negativo.",
        "exemplo": "O simétrico de 7 é −7. O módulo de −9 é 9. Entre −8 e "
                   "−5, o menor é −8, porque está mais à esquerda.",
        "lembra": "Quanto mais à esquerda na recta, menor é o número.",
    },
    "mat-7c:u1:n4": {
        "explica": "Somar um número negativo é andar para a esquerda na "
                   "recta. Na multiplicação e na divisão, sinais iguais dão "
                   "positivo e sinais diferentes dão negativo.",
        "exemplo": "−12 + 7 = −5. (−4) × 3 = −12, porque os sinais são "
                   "diferentes. (−4) × (−3) = 12, porque são iguais.",
        "lembra": "Sinais iguais, positivo. Sinais diferentes, negativo.",
    },
    "mat-7c:u2:n1": {
        "explica": "Um polígono é uma figura fechada feita de segmentos de "
                   "recta. Classifica-se pelo número de lados. Num triângulo, "
                   "a soma dos ângulos internos é sempre 180 graus.",
        "exemplo": "Um pentágono tem 5 lados, um hexágono 6. Num triângulo "
                   "com ângulos de 90 e 60 graus, o terceiro é 30, porque "
                   "90 + 60 + 30 = 180.",
        "lembra": "Os ângulos de qualquer triângulo somam 180 graus.",
    },
    "mat-7c:u2:n2": {
        "explica": "A circunferência é a linha; o círculo é a região que ela "
                   "fecha. O raio vai do centro à linha; o diâmetro atravessa "
                   "o círculo pelo centro e vale dois raios. A corda une dois "
                   "pontos da circunferência.",
        "exemplo": "Se o raio é 7 cm, o diâmetro é 14 cm. Um sólido como a "
                   "esfera não tem nenhuma face plana; o cubo tem seis.",
        "lembra": "Diâmetro é sempre o dobro do raio.",
    },
    "mat-7c:u3:n1": {
        "explica": "Uma fracção representa partes de um todo. O denominador "
                   "diz em quantas partes se dividiu; o numerador, quantas se "
                   "tomaram. Fracções equivalentes representam a mesma "
                   "quantidade escrita de outra maneira.",
        "exemplo": "1/2 = 2/4 = 4/8, e todas valem metade. Para simplificar "
                   "6/8, divide-se o de cima e o de baixo por 2: fica 3/4.",
        "lembra": "Uma fracção é irredutível quando já não se pode simplificar.",
    },
    "mat-7c:u3:n2": {
        "explica": "Com o mesmo denominador, somam-se ou subtraem-se os "
                   "numeradores e o denominador fica na mesma. Com "
                   "denominadores diferentes, reduzem-se primeiro ao mesmo.",
        "exemplo": "1/4 + 2/4 = 3/4. Para 1/2 + 1/3, passa-se aos sextos: "
                   "3/6 + 2/6 = 5/6.",
        "lembra": "Só se somam fracções que estejam partidas do mesmo tamanho.",
    },
    "mat-7c:u3:n3": {
        "explica": "Toda a fracção se pode escrever na forma decimal, "
                   "dividindo o numerador pelo denominador. Às vezes a "
                   "divisão não acaba e um grupo de algarismos repete-se sem "
                   "fim: é uma dízima periódica.",
        "exemplo": "1/4 = 0,25. E 1/3 = 0,333... , que é periódica. "
                   "Arredondando 3,7 às unidades fica 4, porque 7 é maior "
                   "que 5.",
        "lembra": "Para arredondar, olha-se para o algarismo seguinte.",
    },
    "mat-7c:u4:n1": {
        "explica": "O perímetro é a medida do contorno de uma figura: "
                   "soma-se o comprimento de todos os lados.",
        "exemplo": "Um rectângulo de 8 cm por 5 cm tem perímetro "
                   "8 + 5 + 8 + 5 = 26 cm. Um quadrado de 9 cm de lado tem "
                   "4 × 9 = 36 cm.",
        "lembra": "Perímetro é o caminho à volta; área é o espaço lá dentro.",
    },
    "mat-7c:u4:n2": {
        "explica": "A área do trapézio é a soma das bases a dividir por 2, "
                   "vezes a altura. A do losango é o produto das diagonais a "
                   "dividir por 2. O volume de um prisma é a área da base "
                   "vezes a altura.",
        "exemplo": "Trapézio de bases 10 e 6 e altura 4: (10 + 6) : 2 = 8, e "
                   "8 × 4 = 32 centímetros quadrados. Losango de diagonais "
                   "12 e 5: 12 × 5 : 2 = 30.",
        "lembra": "Área mede-se em unidades quadradas; volume, em cúbicas.",
    },
    "mat-7c:u5:n1": {
        "explica": "Uma equação é uma igualdade com pelo menos uma letra "
                   "desconhecida, a incógnita. Resolver é descobrir o valor "
                   "que torna a igualdade verdadeira: a solução. Duas "
                   "equações com a mesma solução dizem-se equivalentes.",
        "exemplo": "Em x + 5 = 9, a incógnita é x e a solução é 4, porque "
                   "4 + 5 = 9. As equações x + 5 = 9 e x = 4 são "
                   "equivalentes.",
        "lembra": "Uma solução verifica-se substituindo e vendo se dá certo.",
    },
    "mat-7c:u5:n2": {
        "explica": "Para resolver, isola-se a incógnita fazendo a mesma coisa "
                   "aos dois lados da igualdade. O que está a somar passa a "
                   "subtrair; o que está a multiplicar passa a dividir.",
        "exemplo": "x + 7 = 12. Tira-se 7 dos dois lados: x = 5. "
                   "Em 3x = 21, divide-se tudo por 3: x = 7.",
        "lembra": "O que se faz de um lado faz-se do outro, sempre.",
    },
    "mat-7c:u6:n1": {
        "explica": "Uma percentagem é uma fracção de denominador 100. Para "
                   "calcular uma percentagem de uma quantidade, divide-se por "
                   "100 e multiplica-se pela percentagem.",
        "exemplo": "25% de 80: 80 : 100 = 0,8, e 0,8 × 25 = 20. "
                   "Num desconto de 20% sobre 400 meticais, poupam-se 80.",
        "lembra": "50% é metade, 25% é um quarto, 10% é dividir por dez.",
    },
    "mat-7c:u7:n1": {
        "explica": "Uma razão compara duas quantidades por divisão. Uma "
                   "proporção é a igualdade entre duas razões. Numa "
                   "proporção, o produto dos extremos é igual ao produto dos "
                   "meios.",
        "exemplo": "A razão entre 6 e 3 é 2. Em 3/4 = x/8, faz-se "
                   "3 × 8 = 4 × x, ou seja 24 = 4x, logo x = 6.",
        "lembra": "Multiplica em cruz: extremos com extremos, meios com meios.",
    },
    "mat-7c:u7:n2": {
        "explica": "A escala diz quantas vezes o desenho é menor do que a "
                   "realidade. Duas grandezas são directamente proporcionais "
                   "quando crescem juntas, e inversamente proporcionais "
                   "quando uma cresce e a outra diminui.",
        "exemplo": "Numa escala 1:100, 1 cm no papel são 100 cm na "
                   "realidade. Mais trabalhadores, menos tempo de obra: são "
                   "inversamente proporcionais.",
        "lembra": "Directa: dobra uma, dobra a outra. Inversa: dobra uma, a "
                  "outra fica a metade.",
    },

    # ---------------------------------------------------------------
    # Portugues -- 7a classe  (1o ciclo do Ensino Secundario)
    #
    # As quinze unidades do INDE agrupadas em cinco por tipo de texto.
    # Ver o cabecalho do tools/conteudo_por7c.py para a razao.
    # ---------------------------------------------------------------
    "por-7c:u1:n1": {
        "explica": "Um texto normativo estabelece regras: diz o que se pode e o que não se pode fazer. O Regulamento Escolar é o exemplo mais próximo de ti. Organiza-se em artigos numerados e usa linguagem clara, formal e sem opiniões.",
        "exemplo": "«Artigo 5 — O aluno deve chegar à escola cinco minutos antes do toque de entrada.» Diz o dever, e mais nada.",
        "lembra": "Um regulamento manda ou proíbe; não conta nem opina.",
    },
    "por-7c:u1:n2": {
        "explica": "O sujeito é quem pratica a acção. É simples quando tem um só núcleo e composto quando tem dois ou mais. As preposições — a, com, de — ligam palavras umas às outras.",
        "exemplo": "«Os alunos chegaram cedo»: sujeito simples, o núcleo é «alunos». «A Amina e o Jorge estudam»: sujeito composto, dois núcleos.",
        "lembra": "Conta os núcleos do sujeito: um é simples, dois ou mais é composto.",
    },
    "por-7c:u1:n3": {
        "explica": "Formam-se palavras novas juntando pedaços a uma palavra que já existe: um prefixo antes, um sufixo depois. As formas de tratamento mudam consoante a pessoa a quem se fala.",
        "exemplo": "De «feliz» faz-se «infeliz» (prefixo in-) e «felizmente» (sufixo -mente). Ao director escreve-se «o senhor director», e não «tu».",
        "lembra": "Prefixo vem antes, sufixo vem depois.",
    },
    "por-7c:u2:n1": {
        "explica": "O aviso comunica uma informação a muitas pessoas ao mesmo tempo. É curto, tem data e diz apenas o que é preciso saber. Costuma usar a passiva de se: «avisa-se», «comunica-se».",
        "exemplo": "«Avisa-se toda a comunidade escolar de que as aulas recomeçam a 8 de Fevereiro. A Direcção, 2 de Fevereiro.»",
        "lembra": "Um aviso sem data é um aviso que não serve.",
    },
    "por-7c:u2:n2": {
        "explica": "O modo indicativo apresenta os factos como certos. Tem tempos: o presente para o que é agora, o pretérito para o que já foi, o futuro para o que há-de ser. O particípio passado acaba em -ado ou -ido.",
        "exemplo": "Presente: «eu informo». Pretérito perfeito: «eu informei». Futuro: «eu informarei». Particípio passado: «informado».",
        "lembra": "O indicativo conta o que é; não pede nem duvida.",
    },
    "por-7c:u2:n3": {
        "explica": "Na voz activa o sujeito faz a acção; na voz passiva sofre-a. Para passar de uma à outra, o complemento directo passa a sujeito. Alguns verbos são irregulares e mudam de raiz ao conjugar.",
        "exemplo": "Activa: «O secretário emitiu a declaração.» Passiva: «A declaração foi emitida pelo secretário.» Irregulares: eu vou, eu sou, eu ponho.",
        "lembra": "Na passiva, quem fazia a acção fica no fim, com «por».",
    },
    "por-7c:u3:n1": {
        "explica": "A notícia informa sobre um facto real e responde a cinco perguntas: o quê, quem, quando, onde e porquê. A linguagem é objectiva — o jornalista conta, não opina. O fait divers é uma notícia breve do dia-a-dia.",
        "exemplo": "«Chuva forte cortou a estrada de Lichinga na madrugada de ontem, devido à cheia do rio.» Diz o quê, onde, quando e porquê.",
        "lembra": "Se a notícia diz o que o autor sente, deixou de ser notícia.",
    },
    "por-7c:u3:n2": {
        "explica": "Os complementos circunstanciais dizem as circunstâncias da acção: quando (tempo), onde (lugar), porquê (causa) e para quê (fim).",
        "exemplo": "«A aula foi adiada ontem, na escola, por causa da chuva, para proteger os alunos»: tempo, lugar, causa e fim, por esta ordem.",
        "lembra": "Pergunta quando, onde, porquê e para quê — a resposta é o complemento.",
    },
    "por-7c:u3:n3": {
        "explica": "As conjunções coordenativas ligam orações do mesmo nível. As copulativas somam, as adversativas opõem e as conclusivas tiram uma conclusão.",
        "exemplo": "Copulativa: «Estudou e passou.» Adversativa: «Estudou, mas faltou.» Conclusiva: «Estudou, logo passou.»",
        "lembra": "«E» soma, «mas» opõe, «logo» conclui.",
    },
    "por-7c:u4:n1": {
        "explica": "Os textos multiuso servem para aprender e consultar: manuais escolares, textos didácticos e científicos. Organizam-se com índice, títulos, esquemas e tabelas, e usam vocabulário rigoroso.",
        "exemplo": "Para achar depressa a lição sobre o ciclo da água, vais ao índice em vez de folhear o livro todo.",
        "lembra": "Num texto didáctico, o índice e os títulos são atalhos.",
    },
    "por-7c:u4:n2": {
        "explica": "Os pronomes substituem ou acompanham o nome. Os demonstrativos situam, os possessivos dizem de quem é, os interrogativos perguntam e os indefinidos falam de alguém ou de algo que não se identifica.",
        "exemplo": "Demonstrativo: «este livro». Possessivo: «o meu livro». Interrogativo: «quem chegou?». Indefinido: «alguém chegou».",
        "lembra": "O pronome evita repetir o nome a toda a hora.",
    },
    "por-7c:u4:n3": {
        "explica": "Os modos verbais dizem como se apresenta a acção. O indicativo dá o facto como certo, o imperativo dá uma ordem ou um pedido, e o conjuntivo exprime dúvida, desejo ou possibilidade.",
        "exemplo": "Indicativo: «ele estuda». Imperativo: «estuda!» e «não estudes!». Conjuntivo: «espero que ele estude».",
        "lembra": "Depois de «espero que» ou «talvez» vem o conjuntivo.",
    },
    "por-7c:u5:n1": {
        "explica": "O conto narra uma história curta. A fábula também, mas as personagens costumam ser animais e termina com uma moral. O adjectivo flexiona em grau para comparar.",
        "exemplo": "Comparativo de superioridade: «mais alta do que». De igualdade: «tão alta como». Superlativo absoluto: «altíssima» (sintético) ou «muito alta» (analítico).",
        "lembra": "A fábula acaba sempre com uma lição.",
    },
    "por-7c:u5:n2": {
        "explica": "Palavras homónimas escrevem-se e dizem-se igual, mas querem dizer coisas diferentes. Parónimas apenas se parecem. E compõem-se palavras juntando duas: por aglutinação, quando se perdem letras, ou por justaposição, quando não.",
        "exemplo": "Homónimas: «canto» de cantar e «canto» da sala. Parónimas: «comprimento» e «cumprimento». Aglutinação: «passatempo». Justaposição: «guarda-chuva».",
        "lembra": "Homónimas são iguais; parónimas só se parecem.",
    },
    "por-7c:u5:n3": {
        "explica": "O texto dramático é escrito para ser representado: só tem as falas das personagens e as indicações de cena, chamadas didascálias. No discurso directo a personagem fala; no indirecto alguém conta o que ela disse.",
        "exemplo": "Directo: «O Jorge disse: — Vou à escola.» Indirecto: «O Jorge disse que ia à escola.»",
        "lembra": "Ao passar a indirecto, o travessão desaparece e entra o «que».",
    },

    # ---------------------------------------------------------------
    # Historia -- 7a classe  (1o ciclo do Ensino Secundario)
    #
    # A primeira Historia separada da app: da 4a a 6a classe ela vem
    # dentro das Ciencias Sociais, como o primario a ensina.
    # ---------------------------------------------------------------
    "his-7c:u1:n1": {
        "explica": "A História é a ciência que estuda o passado das sociedades humanas. Não serve para decorar datas: serve para perceber como chegámos onde estamos. Apoia-se noutras ciências — a Arqueologia, a Geografia, a Antropologia e a Economia.",
        "exemplo": "A Arqueologia escava e estuda os objectos que ficaram; a Antropologia estuda os costumes; a Geografia diz onde tudo aconteceu.",
        "lembra": "A História explica o presente pelo passado.",
    },
    "his-7c:u1:n2": {
        "explica": "Fonte histórica é tudo o que nos dá informação sobre o passado. Há fontes escritas, materiais e orais. Em África as orais têm um peso especial, porque muito do passado foi transmitido de boca em boca, de geração em geração.",
        "exemplo": "Uma carta antiga é fonte escrita; uma machadinha de pedra é material; o que um ancião conta sobre a sua aldeia é oral.",
        "lembra": "Nenhuma fonte diz tudo: cruzam-se umas com as outras.",
    },
    "his-7c:u1:n3": {
        "explica": "A História mede o tempo em décadas, séculos e milénios, e conta os anos a partir do nascimento de Cristo, para trás e para a frente. O século um vai do ano 1 ao ano 100 — e é por isso que os anos 1900 são o século vinte.",
        "exemplo": "Década: 10 anos. Século: 100. Milénio: 1000. O ano de 1975 pertence ao século vinte, porque este vai de 1901 a 2000.",
        "lembra": "Anos 1900 são o século vinte, não o dezanove.",
    },
    "his-7c:u2:n1": {
        "explica": "Há duas explicações para a origem do Homem. A teoria da criação atribui-a a uma acção divina. A da evolução defende que o ser humano resultou de transformações lentas ao longo de milhões de anos: a hominização.",
        "exemplo": "São factores da hominização a posição erecta, a libertação das mãos, o trabalho, a linguagem e o aumento do cérebro.",
        "lembra": "Hominização é o caminho lento até ao ser humano de hoje.",
    },
    "his-7c:u2:n2": {
        "explica": "África é o berço da Humanidade porque foi aí que se encontraram os vestígios mais antigos dos hominídeos, sobretudo no Vale do Rift. O trabalho foi decisivo: usar as mãos desenvolveu-as, e desenvolveu a inteligência.",
        "exemplo": "Os primeiros instrumentos eram de pedra lascada, e serviam para cortar, raspar e caçar.",
        "lembra": "A Humanidade começou em África, e os ossos provam-no.",
    },
    "his-7c:u2:n3": {
        "explica": "O domínio do fogo mudou a vida: aquecia, afastava os animais e permitia cozinhar. Depois veio a agricultura, e com ela a passagem de sociedades nómadas — que se deslocavam à procura de alimento — a sociedades sedentárias, fixas num lugar.",
        "exemplo": "As pinturas rupestres, feitas nas paredes das grutas, mostram que esses homens já tinham arte e religião.",
        "lembra": "Nómada anda; sedentário fica. Foi a agricultura que fixou.",
    },
    "his-7c:u3:n1": {
        "explica": "Com a agricultura e a domesticação de animais, o Homem passou a produzir o alimento em vez de o procurar. Ao produzir mais do que consumia, apareceu o excedente — e com ele a diferenciação social.",
        "exemplo": "Quem guardava o excedente ganhava poder sobre quem não tinha. É aí que começam as diferenças entre grupos sociais.",
        "lembra": "Excedente é o que sobra — e foi ele que criou as desigualdades.",
    },
    "his-7c:u3:n2": {
        "explica": "Os primeiros Estados nasceram junto de grandes rios, onde a terra era fértil: o Egipto no vale do Nilo, governado pelo faraó, e a Mesopotâmia entre o Tigre e o Eufrates, onde nasceu a escrita cuneiforme.",
        "exemplo": "O Código de Hamurábi é um dos primeiros conjuntos de leis escritas que se conhecem: as regras deixaram de depender da memória de quem julgava.",
        "lembra": "Os primeiros Estados nasceram onde havia rio e terra boa.",
    },
    "his-7c:u3:n3": {
        "explica": "A Grécia Antiga organizava-se em cidades-Estado, as pólis. Em Atenas nasceu a democracia, mas só votavam os cidadãos homens livres: mulheres, escravos e estrangeiros ficavam de fora.",
        "exemplo": "Numa Atenas de dezenas de milhares de habitantes, só uma parte podia votar. Era democracia, e era limitada.",
        "lembra": "A democracia ateniense excluía mais gente do que incluía.",
    },
    "his-7c:u4:n1": {
        "explica": "Os Khoisan foram dos mais antigos habitantes da África Austral: viviam da caça e da recolecção, em pequenos grupos. Os povos de língua bantu chegaram depois, e traziam a agricultura e a metalurgia do ferro.",
        "exemplo": "Com o ferro fizeram-se enxadas e catanas melhores, e com elas cultivou-se mais terra e alimentou-se mais gente.",
        "lembra": "Os bantu trouxeram a enxada de ferro — e com ela, aldeias maiores.",
    },
    "his-7c:u4:n2": {
        "explica": "O Reino do Zimbabwe ergueu grandes construções de pedra sem argamassa e enriqueceu com o ouro e o marfim. O Império de Mutapa formou-se depois, no vale do Zambeze, e comerciava com os swahili da costa.",
        "exemplo": "O ouro do interior descia até à costa e trocava-se por tecidos e missangas vindos do outro lado do Índico.",
        "lembra": "O território de Mutapa fica hoje entre Moçambique e o Zimbabwe.",
    },
    "his-7c:u4:n3": {
        "explica": "Na África Ocidental, três impérios sucederam-se à custa do comércio transaariano: Ghana, Mali e Songhai. As caravanas de camelos atravessavam o deserto levando ouro do sul e trazendo sal do norte.",
        "exemplo": "No Mali, Timbuctu tornou-se centro de comércio e de estudo. Mansa Musa ficou célebre pela enorme riqueza do seu império. O Songhai teve capital em Gao.",
        "lembra": "Ouro para norte, sal para sul: era esse o negócio do Saara.",
    },

    # ---------------------------------------------------------------
    # Geografia -- 7a classe  (1o ciclo do Ensino Secundario)
    #
    # Com esta, a Geografia separa-se das Ciencias Sociais: da 4a a 6a
    # classe vem la dentro, junto com a Historia.
    # ---------------------------------------------------------------
    "geo-7c:u1:n1": {
        "explica": "A Geografia estuda a Terra e a relação entre o Homem e o espaço onde vive. Tem dois grandes ramos: a Física, que trata do relevo, do clima, dos rios e dos solos, e a Humana, que trata da população e do que ela faz.",
        "exemplo": "Estudar onde chove mais é Geografia Física. Estudar porque é que as pessoas se mudam para a cidade é Geografia Humana.",
        "lembra": "Física: a Terra. Humana: as pessoas na Terra.",
    },
    "geo-7c:u1:n2": {
        "explica": "A Geografia não trabalha sozinha. Apoia-se na História para saber o passado dos lugares, na Geologia para as rochas, na Cartografia para os mapas, na Climatologia para os climas e na Demografia para as populações.",
        "exemplo": "Para explicar porque é que uma cidade cresceu naquele sítio, é preciso saber o relevo, o rio, e também a História de quem lá chegou primeiro.",
        "lembra": "Cada ciência vizinha responde a uma parte da pergunta.",
    },
    "geo-7c:u2:n1": {
        "explica": "Para localizar um ponto da Terra usam-se linhas imaginárias. Os paralelos são círculos paralelos ao Equador; os meridianos vão de polo a polo. A latitude mede a distância ao Equador; a longitude, a Greenwich.",
        "exemplo": "O Equador é o paralelo de 0 graus. Moçambique é atravessado pelo trópico de Capricórnio, a sul do Equador.",
        "lembra": "Latitude conta a partir do Equador; longitude, de Greenwich.",
    },
    "geo-7c:u2:n2": {
        "explica": "A Terra representa-se de três maneiras. O globo não deforma as formas, mas mostra pouco e não se transporta. O mapa cabe numa folha e mostra mais, mas deforma. A planta representa uma área pequena com muito pormenor.",
        "exemplo": "Um mapa tem sempre título, legenda, escala e orientação. A legenda diz o que significam as cores e os símbolos.",
        "lembra": "Um mapa sem legenda e sem escala não se lê.",
    },
    "geo-7c:u2:n3": {
        "explica": "A escala diz quantas vezes o mapa é menor do que a realidade. Quanto menor o segundo número, maior o pormenor. E as paisagens dividem-se em naturais, onde o Homem quase não interveio, e humanizadas, que podem ser rurais ou urbanas.",
        "exemplo": "Numa escala 1:100 000, 1 cm no mapa é 100 000 cm na realidade, ou seja 1 km. Uma machamba é paisagem humanizada rural.",
        "lembra": "Escala pequena, muito terreno e pouco pormenor.",
    },
    "geo-7c:u3:n1": {
        "explica": "O Universo é tudo o que existe. A explicação mais aceite para a sua origem é a teoria do Big Bang. É feito de galáxias, que são enormes conjuntos de estrelas, gás e poeira. As estrelas têm luz própria; os planetas e os satélites não.",
        "exemplo": "A nossa galáxia chama-se Via Láctea. O Sol é uma estrela; a Terra é um planeta; a Lua é um satélite.",
        "lembra": "Estrela brilha por si; planeta só reflecte.",
    },
    "geo-7c:u3:n2": {
        "explica": "O Sistema Solar tem o Sol no centro e oito planetas a girar à volta dele. Pela ordem, a contar do Sol: Mercúrio, Vénus, Terra, Marte, Júpiter, Saturno, Úrano e Neptuno.",
        "exemplo": "A Terra é o terceiro planeta a contar do Sol. Júpiter é o maior de todos.",
        "lembra": "Oito planetas, e a Terra é o terceiro.",
    },
    "geo-7c:u3:n3": {
        "explica": "A Terra tem dois movimentos. A rotação é a volta sobre si mesma, demora cerca de 24 horas e dá o dia e a noite. A translação é a volta ao Sol, demora cerca de 365 dias e, com a inclinação do eixo, dá as estações do ano.",
        "exemplo": "É por a Terra rodar que o Sol parece nascer a este e pôr-se a oeste. Não é o Sol que anda: somos nós.",
        "lembra": "Rotação: dia e noite. Translação: as estações.",
    },
    "geo-7c:u4:n1": {
        "explica": "A atmosfera é a camada de ar que envolve a Terra. É feita sobretudo de azoto e de oxigénio, e divide-se em camadas. A mais baixa é a troposfera, onde acontecem as nuvens, a chuva e o vento.",
        "exemplo": "Na estratosfera fica a camada de ozono, que trava os raios ultravioleta do Sol. Sem ela, o risco de cancro da pele aumenta.",
        "lembra": "O tempo faz-se na troposfera, a camada de baixo.",
    },
    "geo-7c:u4:n2": {
        "explica": "Tempo é o estado da atmosfera num momento; clima é o que se repete ao longo de muitos anos. Os elementos do clima medem-se — temperatura, precipitação. Os factores explicam-no: latitude, altitude, continentalidade e correntes marítimas.",
        "exemplo": "«Hoje chove» é tempo. «Aqui chove de Novembro a Março» é clima. A chuva mede-se com o pluviómetro.",
        "lembra": "Elemento mede-se; factor explica.",
    },
    "geo-7c:u4:n3": {
        "explica": "Pela latitude, a Terra divide-se em zonas bioclimáticas: a intertropical, entre os dois trópicos; as temperadas, entre os trópicos e os círculos polares; e as frias, dos círculos polares aos polos.",
        "exemplo": "Moçambique fica na zona intertropical, e por isso tem temperaturas altas todo o ano e uma época de chuvas.",
        "lembra": "Quanto mais longe do Equador, mais frio.",
    },
    "geo-7c:u5:n1": {
        "explica": "A hidrosfera é o conjunto das águas do planeta, e ocupa cerca de 71 por cento da superfície. As águas do mar mexem-se de três maneiras: ondas, feitas pelo vento; marés, pela atracção da Lua e do Sol; e correntes marítimas.",
        "exemplo": "Moçambique é banhado pelo oceano Índico, ao longo de quase 2 700 km de costa.",
        "lembra": "Ondas, vento. Marés, Lua. São coisas diferentes.",
    },
    "geo-7c:u5:n2": {
        "explica": "Um rio nasce na nascente e desagua na foz; um rio que desagua noutro é um afluente. A água anda em ciclo: evapora, condensa em nuvens, cai em precipitação e volta ao mar pelos rios ou infiltra-se no solo.",
        "exemplo": "O maior lago de Moçambique é o Niassa. O Zambeze é o maior rio que atravessa o país.",
        "lembra": "Evaporar, condensar, precipitar: o ciclo não pára.",
    },
    "geo-7c:u5:n3": {
        "explica": "A litosfera é a parte sólida. Por dentro, a Terra tem crusta, manto e núcleo. As rochas são de três tipos: magmáticas, do magma arrefecido; sedimentares, de sedimentos acumulados; e metamórficas, transformadas pelo calor.",
        "exemplo": "O granito é magmático, o arenito é sedimentar e o mármore é metamórfico. O solo nasce da alteração das rochas mais a matéria orgânica.",
        "lembra": "Crusta, manto, núcleo — de fora para dentro.",
    },
    "geo-7c:u5:n4": {
        "explica": "O relevo é feito e desfeito ao mesmo tempo. Os agentes internos — sismos e vulcões — constroem; os externos — a água, o vento, o gelo — desgastam. A biosfera é o conjunto de todos os seres vivos, e depende das outras três esferas.",
        "exemplo": "Um vulcão levanta uma montanha em meses; a chuva demora milhares de anos a gastá-la. As duas forças trabalham sempre.",
        "lembra": "As quatro esferas estão ligadas: mexer numa mexe as outras.",
    },

    # ---------------------------------------------------------------
    # As seis disciplinas que fecham a 7a classe
    #
    # Biologia, Ingles, Educacao Visual, Educacao Fisica, Agropecuaria e
    # TIC. Com estas, o plano de estudos da 7a fica coberto por inteiro:
    # a Fisica, a Quimica e o Frances nao entram porque comecam na 8a.
    # ---------------------------------------------------------------
    "bio-7c:u1:n1": {
        "explica": "A Biologia é a ciência da vida: estuda os seres vivos, como funcionam e como se relacionam. Divide-se em ramos — a Zoologia trata dos animais, a Botânica das plantas, a Citologia da célula e a Anatomia da forma do corpo.",
        "exemplo": "A palavra vem do grego: «bios» é vida e «logos» é ciência. Ciência da vida.",
        "lembra": "Cada ramo da Biologia olha para uma parte da mesma coisa: a vida.",
    },
    "bio-7c:u1:n2": {
        "explica": "O método científico é a maneira de procurar respostas sem se enganar a si próprio: observa-se, levanta-se uma explicação possível, põe-se à prova com uma experiência e regista-se o que aconteceu — mesmo quando contraria o esperado.",
        "exemplo": "Numa experiência, lê-se sempre o rótulo antes de mexer numa substância, e nunca se faz nada que não tenha sido autorizado.",
        "lembra": "Observar, experimentar, registar. E aceitar o resultado.",
    },
    "bio-7c:u1:n3": {
        "explica": "Primeiros socorros são os cuidados imediatos até chegar ajuda médica. Não substituem o hospital: ganham tempo. Num corte, lava-se com água e sabão; numa queimadura, arrefece-se com água corrente e não se rebentam as bolhas.",
        "exemplo": "Se alguém engolir um produto tóxico, leva-se ao hospital com a embalagem: saber o que foi engolido é metade do tratamento.",
        "lembra": "Socorrer é ganhar tempo até chegar quem sabe mais.",
    },
    "bio-7c:u2:n1": {
        "explica": "A célula é a unidade básica de todos os seres vivos, e é pequena de mais para se ver a olho nu — daí o microscópio. A célula vegetal tem parede celular, que a animal não tem. O núcleo comanda o funcionamento.",
        "exemplo": "O microscópio óptico usa luz e amplia centenas de vezes; o electrónico usa electrões e amplia muito mais.",
        "lembra": "Parede celular: sinal de que a célula é vegetal.",
    },
    "bio-7c:u2:n2": {
        "explica": "Classificar é arrumar os seres vivos em grupos que partilham características. Uns são unicelulares, feitos de uma só célula, como as bactérias; outros são pluricelulares. Os fungos não fazem fotossíntese: alimentam-se de matéria já formada.",
        "exemplo": "Um cogumelo não é planta nem animal — é fungo, e por isso tem grupo próprio.",
        "lembra": "Classificar não é ordenar por importância: é agrupar por parecença.",
    },
    "bio-7c:u2:n3": {
        "explica": "As plantas fabricam o seu alimento por fotossíntese, usando luz, água e dióxido de carbono, e libertam oxigénio. Os animais dividem-se em vertebrados, que têm coluna, e invertebrados, que não têm.",
        "exemplo": "A minhoca e a formiga são invertebrados; o peixe, a cobra e o cabrito são vertebrados.",
        "lembra": "As plantas dão-nos o oxigénio que respiramos.",
    },
    "bio-7c:u3:n1": {
        "explica": "Alimento é o que se come; nutriente é a substância que o corpo aproveita. Os hidratos de carbono dão energia, as proteínas constroem e reparam o corpo, e as vitaminas e os sais minerais fazem tudo funcionar.",
        "exemplo": "A laranja e o limão são ricos em vitamina C. O feijão e o peixe dão proteínas. A mandioca e o milho dão energia.",
        "lembra": "Comer variado é mais importante do que comer muito.",
    },
    "bio-7c:u3:n2": {
        "explica": "Os alimentos estragam-se porque os micróbios crescem neles. Conservar é travar esse crescimento — secando, salgando, fumando ou arrefecendo. Todos estes métodos fazem o mesmo: tiram aos micróbios a água ou o calor de que precisam.",
        "exemplo": "O peixe salgado dura semanas porque o sal lhe retira a água. Lavar as mãos antes de cozinhar evita levar micróbios à comida.",
        "lembra": "Sem água e sem calor, o micróbio não se multiplica.",
    },
    "bio-7c:u3:n3": {
        "explica": "A intoxicação alimentar acontece ao comer alimento estragado ou contaminado. Dá vómitos e diarreia, e o maior perigo não é a doença em si: é a desidratação que vem com ela, sobretudo nas crianças.",
        "exemplo": "Quem tem diarreia deve beber muitos líquidos. Para evitar a cólera, bebe-se água fervida ou tratada.",
        "lembra": "Com diarreia, o que salva é beber, não deixar de beber.",
    },
    "bio-7c:u4:n1": {
        "explica": "A digestão começa na boca, onde os dentes cortam e trituram e a saliva começa a desfazer o alimento. A absorção dos nutrientes faz-se sobretudo no intestino delgado. Um adulto tem 32 dentes.",
        "exemplo": "Os incisivos cortam, os caninos rasgam e os molares trituram. A cárie nasce dos restos de açúcar deixados entre os dentes.",
        "lembra": "Mastigar bem é começar bem a digestão.",
    },
    "bio-7c:u4:n2": {
        "explica": "O coração bombeia o sangue para todo o corpo. As artérias levam o sangue do coração para fora; as veias trazem-no de volta. Os glóbulos vermelhos transportam oxigénio e os brancos defendem o corpo.",
        "exemplo": "Uma ferida infectada incha porque os glóbulos brancos acorreram ao local a combater os micróbios.",
        "lembra": "Artérias saem, veias voltam.",
    },
    "bio-7c:u4:n3": {
        "explica": "Ao inspirar entra ar rico em oxigénio; ao expirar sai ar com dióxido de carbono. As trocas fazem-se nos alvéolos pulmonares, sacos minúsculos onde o ar e o sangue quase se tocam. A imunidade é a defesa do corpo contra as doenças.",
        "exemplo": "O fumo do tabaco destrói os alvéolos, e por isso quem fuma cansa-se mais depressa a subir escadas.",
        "lembra": "Inspirar e expirar são os dois movimentos, e não um só.",
    },
    "bio-7c:u5:n1": {
        "explica": "A adolescência é a passagem da infância para a idade adulta. O corpo muda, e muda em ritmos diferentes de pessoa para pessoa — isso é normal e não é doença. A higiene passa a ser mais importante, porque o corpo transpira mais.",
        "exemplo": "Quem tem dúvidas sobre o próprio corpo deve falar com um adulto de confiança ou com um profissional de saúde.",
        "lembra": "Cada corpo tem o seu ritmo. Não há atraso nem pressa.",
    },
    "bio-7c:u5:n2": {
        "explica": "Um relacionamento saudável assenta em respeito mútuo: ninguém manda no outro e ninguém é pressionado. Dizer não é sempre uma resposta legítima, e procurar ajuda de um adulto não é fraqueza.",
        "exemplo": "A gravidez precoce afecta a saúde e interrompe os estudos da rapariga, e é por isso que continuar a estudar abre mais escolhas.",
        "lembra": "Quem gosta de ti respeita o teu não.",
    },
    "ing-7c:u1:n1": {
        "explica": "Em inglês cumprimenta-se conforme a hora do dia: «good morning» de manhã, «good afternoon» de tarde e «good evening» ao fim do dia. Para se apresentar diz-se «I am» seguido do nome.",
        "exemplo": "«Good morning! What is your name?» — «I am Amina.» Para se despedir: «Goodbye» ou «See you tomorrow».",
        "lembra": "«Good night» é para ir dormir, não para chegar.",
    },
    "ing-7c:u1:n2": {
        "explica": "Os números até vinte aprendem-se de cor, porque muitos não seguem regra. De países formam-se nacionalidades: Mozambique dá «Mozambican». Para perguntar a origem usa-se «Where are you from?».",
        "exemplo": "Twelve é 12 e twenty é 20. Cuidado: «thirteen» é 13 e «thirty» é 30 — a diferença está no fim da palavra.",
        "lembra": "-teen é adolescente do número: treze a dezanove.",
    },
    "ing-7c:u1:n3": {
        "explica": "Na escola há «classroom», «library» e «playground». Para as horas pergunta-se «What time is it?». Os dias da semana escrevem-se sempre com letra grande em inglês, ao contrário do português.",
        "exemplo": "O plural faz-se quase sempre com -s: book dá books. Monday é segunda-feira e Sunday é domingo.",
        "lembra": "Em inglês, os dias da semana levam maiúscula.",
    },
    "ing-7c:u2:n1": {
        "explica": "Os nomes da família em inglês: mother, father, brother, sister, son, daughter. Os avós formam-se com «grand-»: grandmother e grandfather.",
        "exemplo": "«This is my brother» — este é o meu irmão. «She is my grandmother» — ela é a minha avó.",
        "lembra": "«Grand-» à frente transforma pai em avô.",
    },
    "ing-7c:u2:n2": {
        "explica": "Os possessivos dizem de quem é a coisa e vêm antes do nome: my, your, his, her, its, our, their. Ao contrário do português, não mudam com o plural do objecto.",
        "exemplo": "«My book» e «my books» — o possessivo não muda. «His book» é dele; «her book» é dela.",
        "lembra": "His é dele, her é dela. O sexo é de quem tem, não do que se tem.",
    },
    "ing-7c:u2:n3": {
        "explica": "O verbo «to be» muda com a pessoa: I am, you are, he/she/it is, we/you/they are. A negativa faz-se juntando «not», e a pergunta trocando a ordem.",
        "exemplo": "«She is my friend.» Negativa: «She is not my friend.» Pergunta: «Is she your friend?»",
        "lembra": "Para perguntar com «to be», o verbo vai à frente.",
    },
    "ing-7c:u3:n1": {
        "explica": "As partes do corpo em inglês: head, eyes, ears, mouth, arm, hand, leg, foot. Alguns plurais são irregulares: foot dá feet, e tooth dá teeth.",
        "exemplo": "«I have two hands and two feet.» Repara: não é «foots».",
        "lembra": "Foot dá feet, tooth dá teeth. São dos poucos assim.",
    },
    "ing-7c:u3:n2": {
        "explica": "Para falar de saúde usa-se «I am sick» ou «I have a…». As dores formam-se com «-ache»: headache é dor de cabeça, toothache dor de dentes.",
        "exemplo": "«I have a headache.» Alimentos: water, milk, bread, fruit, meat, fish.",
        "lembra": "«-ache» no fim da palavra quer dizer dor.",
    },
    "ing-7c:u3:n3": {
        "explica": "Para dizer que existe alguma coisa usa-se «there is» para o singular e «there are» para o plural. As divisões da casa: kitchen, bedroom, bathroom, living room.",
        "exemplo": "«There is a table in the kitchen.» «There are three chairs.»",
        "lembra": "Um: there is. Mais do que um: there are.",
    },
    "ing-7c:u4:n1": {
        "explica": "Vocabulário da natureza: tree, grass, flower, river, lake, forest, rubbish. Para dar uma ordem negativa usa-se «Do not» seguido do verbo.",
        "exemplo": "«Do not throw rubbish on the ground.» — não deites lixo no chão.",
        "lembra": "Ordem negativa em inglês começa sempre por «Do not».",
    },
    "ing-7c:u4:n2": {
        "explica": "A vida aquática: fish, turtle, crab, shark, sea, water. Repara que «fish» tem a mesma forma no singular e no plural.",
        "exemplo": "«Fish live in water.» Um peixe é «a fish»; muitos peixes continuam «fish».",
        "lembra": "Fish não leva -s no plural.",
    },
    "ing-7c:u4:n3": {
        "explica": "O presente simples usa-se para hábitos e factos. Com «he», «she» e «it» o verbo leva -s no fim. A negativa faz-se com «do not» ou «does not», e aí o verbo volta à forma simples.",
        "exemplo": "«He studies every day.» Negativa: «He does not study every day» — sem o -s, porque já está no «does».",
        "lembra": "He, she, it: o verbo leva -s. Mas só na afirmativa.",
    },
    "ing-7c:u5:n1": {
        "explica": "Os transportes em inglês: bus, car, train, bicycle, boat, plane. Para dizer como se vai a algum lado usa-se «by» — by bus, by car — excepto a pé, que é «on foot» ou simplesmente «I walk».",
        "exemplo": "«I go to school by bus.» «I walk to school.»",
        "lembra": "A pé não leva «by»: diz-se «on foot».",
    },
    "ing-7c:u5:n2": {
        "explica": "A comunicação: letter, mobile phone, radio, television, message. Ao telefone atende-se com «Hello». A cortesia faz-se com «please», «thank you» e «sorry».",
        "exemplo": "«Hello, can I speak to Jorge, please?» — «Please» no fim transforma um pedido numa boa maneira.",
        "lembra": "«Please» e «thank you» abrem mais portas do que o resto do vocabulário.",
    },
    "ing-7c:u5:n3": {
        "explica": "Desporto e lazer: football, swim, run, dance, sing, play. Para gostos usa-se «I like» seguido do nome ou do verbo com -ing.",
        "exemplo": "«I like music.» «He plays football on Saturday» — com -s, porque é «he».",
        "lembra": "Em inglês britânico, futebol é «football».",
    },
    "ev-7c:u1:n1": {
        "explica": "A Arte é uma forma de o ser humano se exprimir e comunicar. Toma muitas formas: arquitectura, escultura, pintura, cerâmica, música, dança. Em Moçambique, muita arte vive dentro do quotidiano — nas cerimónias, nos objectos, nas casas.",
        "exemplo": "A cerâmica trabalha a argila; a escultura, a madeira ou a pedra; a arquitectura concebe os espaços onde se vive.",
        "lembra": "A Arte não copia o mundo: diz alguma coisa sobre ele.",
    },
    "ev-7c:u1:n2": {
        "explica": "Moçambique tem artistas conhecidos dentro e fora do país. Malangatana Valente Ngwenya na pintura, Alberto Chissano na escultura, Reinata Sadimba na cerâmica e José Forjaz na arquitectura.",
        "exemplo": "As telas de Malangatana são reconhecíveis pelas figuras densas e pelas cores fortes.",
        "lembra": "Cada artista trabalha um material — e o material molda a obra.",
    },
    "ev-7c:u2:n1": {
        "explica": "O suporte é aquilo sobre que se trabalha; o material é aquilo com que se trabalha. Um caderno de esboços serve para registar ideias, e um godê para preparar tintas. Muito material bom vem do que se ia deitar fora.",
        "exemplo": "Tampas de plástico iguais coladas num cartão fazem um godê. Um cartão resistente faz capa de caderno.",
        "lembra": "Antes de comprar material, olha para o que já existe.",
    },
    "ev-7c:u2:n2": {
        "explica": "Um quadro em relevo tem partes salientes que se sentem ao toque. Uma composição é realística se representa objectos reconhecíveis, e abstracta se não representa. A segurança vale sempre: local arejado e ferramentas arrumadas.",
        "exemplo": "Recortam-se formas em cartão, colam-se sobre o suporte e obtém-se relevo sem precisar de esculpir nada.",
        "lembra": "Abstracto não é mal feito: é outra intenção.",
    },
    "ev-7c:u3:n1": {
        "explica": "Nos materiais de expressão gráfica distinguem-se os suportes — papel, cartolina, parede, quadro — dos riscadores — lápis, esferográfica, carvão, giz, marcador. Escolher bem depende do resultado que se quer.",
        "exemplo": "O carvão dá traço intenso e esbate-se com o dedo; a esferográfica dá traço fino e não se apaga.",
        "lembra": "Suporte é onde se desenha; riscador é com que se desenha.",
    },
    "ev-7c:u3:n2": {
        "explica": "As técnicas gráficas mudam o resultado com o mesmo material. O desenho de observação faz-se com o objecto à frente; o pontilhismo constrói a imagem com pontos; a pintura soprada espalha a tinta com o sopro. A técnica mista combina várias.",
        "exemplo": "Num painel colectivo, cada aluno trabalha uma parte e o conjunto forma uma obra só.",
        "lembra": "Experimenta antes de escolher: é assim que se descobre a técnica certa.",
    },
    "ev-7c:u4:n1": {
        "explica": "A comunicação visual transmite mensagens por imagens, sinais e símbolos, sem precisar de palavras. Um ícone parece-se com o que representa; um símbolo representa por convenção. Um bom código visual entende-se à primeira.",
        "exemplo": "Um sinal de trânsito diz o que fazer em silêncio e a quem passa depressa. É comunicação visual a funcionar.",
        "lembra": "Se é preciso explicar o símbolo, o símbolo falhou.",
    },
    "ev-7c:u4:n2": {
        "explica": "Um cartaz tem pouco texto, imagem forte e letra legível ao longe. A banda desenhada conta uma história por vinhetas — os quadrados — e põe a fala das personagens dentro de balões.",
        "exemplo": "Um cartaz sobre igualdade de género serve para fazer pensar e mudar comportamentos, e não só para decorar a parede.",
        "lembra": "Cartaz lê-se de longe e em poucos segundos.",
    },
    "ev-7c:u5:n1": {
        "explica": "O desenho geométrico representa objectos com rigor e medidas. A normalização é o conjunto de regras que faz com que toda a gente leia o desenho da mesma maneira: esquadria a delimitar a folha e legenda a identificar o trabalho.",
        "exemplo": "A esquadria é a moldura traçada junto às margens; a legenda vai no canto inferior direito.",
        "lembra": "Normalizar é combinar regras para todos se entenderem.",
    },
    "ev-7c:u5:n2": {
        "explica": "As letras e os algarismos do desenho técnico são simples, iguais entre si e fáceis de ler. Não são decoração: são informação, e um desenho mal escrito deixa de se poder executar.",
        "exemplo": "Traça-se primeiro a esquadria, depois a legenda, e só então o desenho. A ordem evita ter de refazer.",
        "lembra": "Num desenho técnico, a letra bonita é a letra clara.",
    },
    "edf-7c:u1:n1": {
        "explica": "O aquecimento prepara músculos e articulações e reduz o risco de lesão; o retorno à calma baixa o ritmo aos poucos no fim. A água bebe-se em pequenas quantidades ao longo do esforço, e não toda de uma vez no fim.",
        "exemplo": "Cinco minutos de corrida leve mais alguns alongamentos chegam para aquecer antes de uma aula.",
        "lembra": "Nunca comeces a esforçar-te com o corpo frio.",
    },
    "edf-7c:u1:n2": {
        "explica": "Na ginástica de solo trabalham-se rolamentos, equilíbrios e flexibilidade. O equilíbrio melhora com base de apoio mais larga e centro de gravidade mais baixo. A ajuda de um colega dá segurança e corrige o movimento.",
        "exemplo": "No rolamento à frente apoiam-se as mãos e enrola-se a cabeça para dentro — nunca se apoia a cabeça no solo.",
        "lembra": "Mais baixo e mais largo: é assim que não se cai.",
    },
    "edf-7c:u2:n1": {
        "explica": "No atletismo há corridas de velocidade, de fundo, de barreiras e de estafetas. Na velocidade parte-se de blocos; no fundo gere-se o esforço; nas estafetas passa-se o testemunho dentro da zona marcada.",
        "exemplo": "Quem corre uma prova longa ao máximo desde o início chega ao fim sem nada — gerir é parte da prova.",
        "lembra": "Velocidade é explosão; fundo é gestão.",
    },
    "edf-7c:u2:n2": {
        "explica": "O salto em comprimento tem quatro fases: corrida, chamada, voo e queda, e mede-se pela marca mais próxima da tábua. No lançamento do peso, o peso é empurrado a partir do ombro e nunca atirado.",
        "exemplo": "Antes de qualquer lançamento, confirma-se que a zona de queda está livre. É a regra que evita o acidente.",
        "lembra": "O peso empurra-se; não se atira.",
    },
    "edf-7c:u3:n1": {
        "explica": "No andebol jogam sete por equipa: seis de campo e um guarda-redes. Com a bola na mão dão-se no máximo três passos, a área de baliza é só do guarda-redes, e jogar com o pé é falta.",
        "exemplo": "Três passos, drible, mais três passos — é assim que se avança legalmente com a bola.",
        "lembra": "Três passos com bola. Ao quarto, é falta.",
    },
    "edf-7c:u3:n2": {
        "explica": "Os gestos base do andebol são o passe, a recepção, o drible e o remate. O passe de ombro leva a bola ao longe com precisão; o remate em suspensão faz-se com o corpo no ar, antes de tocar o solo.",
        "exemplo": "Na defesa, o objectivo é impedir o remate e recuperar a bola — sem empurrar nem agarrar.",
        "lembra": "Remate em suspensão: sai do chão antes de atirar.",
    },
    "edf-7c:u4:n1": {
        "explica": "No futebol de onze cada equipa tem onze jogadores em campo, e só o guarda-redes toca a bola com as mãos dentro da sua área. Bola fora pela lateral recomeça com lançamento; o cartão vermelho expulsa.",
        "exemplo": "Um jogador expulso não é substituído: a equipa fica a jogar com menos um.",
        "lembra": "Amarelo avisa; vermelho manda sair.",
    },
    "edf-7c:u4:n2": {
        "explica": "Os gestos base do futebol são o passe, a recepção, a condução e o remate. O passe curto e rasteiro faz-se com a parte interna do pé, que é a zona mais larga e mais precisa. A recepção amortece a bola em vez de a repelir.",
        "exemplo": "Conduzir é levar a bola em corrida com toques curtos, e não chutá-la para a frente e correr atrás.",
        "lembra": "Parte interna do pé: mais superfície, mais pontaria.",
    },
    "edf-7c:u5:n1": {
        "explica": "As danças tradicionais moçambicanas preservam a cultura e juntam a comunidade. O Mapiko, dos Macondes, é uma das mais conhecidas. Dançar em grupo exige acompanhar o ritmo em conjunto, e não ser o mais rápido.",
        "exemplo": "A dança desenvolve coordenação, ritmo e expressão — capacidades que servem em qualquer desporto.",
        "lembra": "Numa dança de grupo, o ritmo é de todos.",
    },
    "edf-7c:u5:n2": {
        "explica": "Os jogos educativos ensinam enquanto se joga: raciocínio, estratégia, cooperação. O desportivismo é aceitar o resultado e cumprimentar o adversário, tenha-se ganho ou perdido.",
        "exemplo": "O ntxuva é um jogo tradicional moçambicano de tabuleiro, e treina o mesmo cálculo que a matemática pede.",
        "lembra": "Se alguém se magoa, o jogo pára. Sempre.",
    },
    "agr-7c:u1:n1": {
        "explica": "A agropecuária junta duas actividades: a agricultura, que cultiva plantas, e a pecuária, que cria animais. Em Moçambique é a base do sustento da maior parte das famílias, e é dela que depende a segurança alimentar do país.",
        "exemplo": "Segurança alimentar quer dizer que todos têm acesso a alimento suficiente, seguro e ao longo de todo o ano.",
        "lembra": "Agricultura cultiva; pecuária cria. Juntas, agropecuária.",
    },
    "agr-7c:u1:n2": {
        "explica": "Há três sistemas agrários. Na subsistência produz-se para comer em casa; no de rendimento produz-se para vender; no agro-industrial produz-se em grande escala, com máquinas e ligação à indústria.",
        "exemplo": "Cada cultura dá-se melhor numa região: é isso que explica o cajueiro no norte e o gado no sul.",
        "lembra": "O que se planta depende do clima e do solo do lugar.",
    },
    "agr-7c:u2:n1": {
        "explica": "Preparar o solo é deixar a terra solta, limpa e pronta a receber a semente. A lavoura revolve a terra e enterra as ervas. A queimada parece limpar depressa, mas destrói a matéria orgânica e empobrece o solo.",
        "exemplo": "Um solo com muita matéria orgânica retém melhor a água e alimenta melhor a planta.",
        "lembra": "Queimar limpa hoje e empobrece amanhã.",
    },
    "agr-7c:u2:n2": {
        "explica": "As plantas propagam-se por semente — propagação sexuada — ou por partes da própria planta, como estacas, que é propagação vegetativa. O compasso é a distância entre plantas e entre linhas.",
        "exemplo": "A mandioca planta-se por estaca do caule. Semear demasiado junto põe as plantas a competir por luz, água e nutrientes.",
        "lembra": "O viveiro cria a planta pequena antes de ir para o campo.",
    },
    "agr-7c:u3:n1": {
        "explica": "As práticas culturais são o trabalho depois da sementeira: sachar tira as ervas e areja o solo, regar dá água quando falta chuva, adubar devolve à terra o que a colheita levou.",
        "exemplo": "Rega-se de manhã cedo ou ao fim da tarde: ao meio-dia grande parte da água evapora antes de chegar à raiz.",
        "lembra": "As ervas daninhas comem o que era para a cultura.",
    },
    "agr-7c:u3:n2": {
        "explica": "Uma praga é um organismo que ataca a cultura. Combate-se de várias maneiras, e nem todas envolvem veneno: a rotação de culturas quebra o ciclo de vida das pragas, e a consociação aproveita melhor o terreno.",
        "exemplo": "Milho com feijão na mesma machamba protege o solo e aproveita o espaço melhor do que cada um sozinho.",
        "lembra": "Pesticida usa-se com protecção e conforme o rótulo.",
    },
    "agr-7c:u4:n1": {
        "explica": "Colher no ponto certo decide a qualidade e a conservação: cedo de mais, o produto não amadureceu; tarde de mais, começa a estragar-se. Depois de colhido, o grão tem de ser bem seco antes de guardado.",
        "exemplo": "Guardar milho húmido dá bolor, e o bolor não estraga só uma parte: passa a toda a pilha.",
        "lembra": "Perdas pós-colheita são colheita que se teve e se perdeu.",
    },
    "agr-7c:u4:n2": {
        "explica": "Um bom celeiro é seco, arejado, levantado do chão e protegido de roedores. A semente que se guarda para a campanha seguinte escolhe-se entre os grãos maiores, sãos e bem secos.",
        "exemplo": "O gorgulho é uma praga do grão já armazenado — ataca depois da colheita, e não no campo.",
        "lembra": "Celeiro levantado do chão: sem humidade e sem ratos.",
    },
    "agr-7c:u5:n1": {
        "explica": "A pecuária cria animais para obter carne, leite, ovos e outros produtos. Maneio é o conjunto de cuidados diários: alimentar, dar água, limpar, observar. A vacinação previne doenças, e um animal doente separa-se dos outros.",
        "exemplo": "Observar os animais todos os dias é o que permite apanhar a doença no início, quando ainda se trata.",
        "lembra": "Prevenir com vacina custa menos do que tratar depois.",
    },
    "agr-7c:u5:n2": {
        "explica": "A avicultura cria aves. O galinheiro deve ser seco, arejado e limpo. As galinhas dividem-se em poedeiras, criadas para o ovo, e frangos de corte, criados para a carne. A doença de Newcastle é a principal ameaça.",
        "exemplo": "Os patos precisam de água para nadar, e os perus são maiores e demoram mais tempo a crescer do que as galinhas.",
        "lembra": "Galinheiro húmido é galinheiro doente.",
    },
    "tic-7c:u1:n1": {
        "explica": "TIC quer dizer Tecnologias de Informação e Comunicação: o conjunto de meios que servem para tratar, guardar e transmitir informação. Computador, telemóvel, Internet e calculadora científica são todos dispositivos computacionais.",
        "exemplo": "Antes das TIC, uma carta de Lichinga a Maputo demorava dias. Hoje a mesma mensagem chega em segundos.",
        "lembra": "As TIC não criam informação: tratam-na e transmitem-na.",
    },
    "tic-7c:u1:n2": {
        "explica": "Hardware é a parte física, aquilo em que se toca. Software são os programas, que dizem ao computador o que fazer. Os dispositivos de entrada dão informação à máquina; os de saída devolvem-na.",
        "exemplo": "Teclado e rato são entrada; monitor e impressora são saída. O sistema operativo é o software que faz o resto funcionar.",
        "lembra": "Se se pode tocar, é hardware.",
    },
    "tic-7c:u1:n3": {
        "explica": "As regras ergonómicas evitam dores e lesões: ecrã à altura dos olhos, costas apoiadas, pausas regulares. O equipamento dura mais se estiver limpo e arejado, e quando morre vai para reciclagem própria.",
        "exemplo": "O lixo electrónico tem metais que contaminam o solo, e por isso não vai no lixo comum nem se queima.",
        "lembra": "Ecrã à altura dos olhos, a cerca de um braço.",
    },
    "tic-7c:u2:n1": {
        "explica": "A Internet é uma rede mundial que liga computadores entre si. Liga-se por cabo ou sem fios, com Wi-Fi ou Bluetooth. O navegador é o programa que abre as páginas.",
        "exemplo": "Nem tudo o que está na Internet é verdade. Antes de acreditar, verifica-se a fonte e compara-se com outras.",
        "lembra": "Muitas partilhas não fazem uma coisa verdadeira.",
    },
    "tic-7c:u2:n2": {
        "explica": "Dados pessoais são as informações que identificam uma pessoa, e têm dono. Publicar a fotografia de alguém sem lhe perguntar é violar a privacidade dessa pessoa, mesmo que a intenção seja boa.",
        "exemplo": "Copiar um texto da Internet e apresentá-lo como teu chama-se plágio. Citar a fonte transforma o mesmo texto em pesquisa honesta.",
        "lembra": "Se te ameaçarem em linha: guarda a prova e conta a um adulto.",
    },
    "tic-7c:u2:n3": {
        "explica": "As TIC servem para aprender quando se usam com um objectivo. Plataformas de apoio, repositórios de partilha e até jogos ajudam — desde que a procura seja dirigida e não uma deriva sem fim.",
        "exemplo": "A dama, o xadrez e o ntxuva desenvolvem raciocínio e estratégia, e são jogos que não precisam de electricidade.",
        "lembra": "Procurar com objectivo é estudar; sem objectivo é passar o tempo.",
    },
    "tic-7c:u3:n1": {
        "explica": "Uma senha protege tudo o que está na conta. Boa senha é longa, mistura letras, números e símbolos, não é uma data conhecida, e não se repete de serviço para serviço. E não se empresta.",
        "exemplo": "«123456» é a pior senha que há. Serviços sérios nunca pedem a senha por mensagem — quem pede está a tentar enganar-te.",
        "lembra": "A senha é como a chave de casa: não se empresta.",
    },
    "tic-7c:u3:n2": {
        "explica": "Um vírus informático é um programa que danifica ou rouba dados. Protege-se instalando aplicações só de lojas oficiais, desligando o Bluetooth quando não é preciso, e fazendo cópias de segurança dos ficheiros.",
        "exemplo": "Uma cópia de segurança é o que separa perder o telemóvel de perder o telemóvel e o trabalho todo.",
        "lembra": "Cópia de segurança feita antes vale mais do que arrepender-se depois.",
    },
    "tic-7c:u3:n3": {
        "explica": "As TIC aplicam-se a tudo. Na agricultura, para consultar o tempo e os preços; na saúde, para guardar registos e ligar unidades distantes; no comércio, para pagar pelo telemóvel sem ir ao banco.",
        "exemplo": "STEM junta Ciências, Tecnologia, Engenharia e Matemática, e é aí que as TIC servem de ferramenta a todas as outras.",
        "lembra": "A tecnologia não substitui quem sabe: dá-lhe alcance.",
    },

    # ---------------------------------------------------------------
    # Matematica -- 8a classe
    #
    # A classe em que a Matematica deixa de ser contas e passa a ser
    # letras. As explicacoes definem; os exemplos sao para copiar para o
    # caderno com os passos a vista.
    # ---------------------------------------------------------------
    "mat-8c:u1:n1": {
        "explica": "A está contido em B quando todos os elementos de A também "
                   "são de B: A ⊂ B, e B contém A. Dois conjuntos são iguais "
                   "quando têm exactamente os mesmos elementos. O universal é "
                   "o conjunto de tudo o que está em estudo.",
        "exemplo": "A = {1, 2} e B = {1, 2, 3, 4}. Todos os elementos de A "
                   "estão em B, logo A ⊂ B. Os subconjuntos de dois elementos "
                   "de {a, b, c} são {a, b}, {a, c} e {b, c}.",
        "lembra": "⊂ é entre conjuntos; ∈ é entre um elemento e um conjunto.",
    },
    "mat-8c:u1:n2": {
        "explica": "A reunião A ∪ B junta os elementos dos dois conjuntos, sem "
                   "repetir. A intersecção A ∩ B fica só com os que estão nos "
                   "dois. Se a intersecção é vazia, os conjuntos são "
                   "disjuntos. Um conjunto é finito quando se contam os "
                   "elementos até ao fim.",
        "exemplo": "A = {2, 4, 6} e B = {4, 6, 8}. A ∪ B = {2, 4, 6, 8}, com 4 "
                   "elementos. A ∩ B = {4, 6}, com 2.",
        "lembra": "Na reunião, o que se repete conta uma vez só.",
    },
    "mat-8c:u1:n3": {
        "explica": "Um número racional escreve-se como fracção de dois "
                   "inteiros, com denominador diferente de zero. Os naturais "
                   "cabem nos inteiros e estes nos racionais: ℕ ⊂ ℤ ⊂ ℚ. Na "
                   "recta, os negativos ficam à esquerda do zero.",
        "exemplo": "−1/2 fica entre −1 e 0. Entre −3/4 e −1/4, o menor é −3/4, "
                   "porque está mais à esquerda. O módulo de −7/7 é 1.",
        "lembra": "Quanto mais à esquerda na recta, menor é o número.",
    },
    "mat-8c:u1:n4": {
        "explica": "Com racionais opera-se como com fracções, com atenção ao "
                   "sinal. Uma potência de base negativa e expoente par dá "
                   "positivo. A raiz quadrada de um número é o que, ao "
                   "quadrado, dá esse número.",
        "exemplo": "−1/2 + 3/4 = −2/4 + 3/4 = 1/4. (−3)² = 9, porque "
                   "(−3) × (−3) = 9. √49 = 7, porque 7 × 7 = 49.",
        "lembra": "Sinais iguais na multiplicação dão positivo.",
    },
    "mat-8c:u2:n1": {
        "explica": "Um ponto do plano tem duas coordenadas: a abcissa, no eixo "
                   "horizontal, e a ordenada, no vertical. Na "
                   "proporcionalidade directa, y é x vezes uma constante; na "
                   "inversa, o produto x × y é constante.",
        "exemplo": "Em (3, −2) a abcissa é 3. Se y = 12 quando x = 4, a "
                   "constante é 12 : 4 = 3. Se x × y = 24 e x = 6, então "
                   "y = 4.",
        "lembra": "Primeiro anda-se na horizontal, depois na vertical.",
    },
    "mat-8c:u2:n2": {
        "explica": "Uma função é uma correspondência em que cada objecto tem "
                   "uma só imagem. Escreve-se f(x). Para achar a imagem, "
                   "substitui-se o x pelo valor. A variável independente é o "
                   "x; a dependente é o y.",
        "exemplo": "f(x) = 2x + 1. Então f(3) = 2 × 3 + 1 = 7. Se f(x) = "
                   "5 − x, f(8) = 5 − 8 = −3.",
        "lembra": "f(3) quer dizer: põe 3 no lugar do x e faz a conta.",
    },
    "mat-8c:u2:n3": {
        "explica": "Uma função linear é do tipo y = ax + b. O gráfico é uma "
                   "recta: a é o declive, b é onde ela corta o eixo das "
                   "ordenadas. O zero da função é o x que dá y = 0.",
        "exemplo": "f(x) = 2x − 8. Zero: 2x − 8 = 0, logo x = 4. Em "
                   "y = −2x + 5, a recta corta o eixo dos y em 5 e desce, "
                   "porque a = −2 é negativo.",
        "lembra": "Declive positivo sobe; declive negativo desce.",
    },
    "mat-8c:u3:n1": {
        "explica": "Há números que não se escrevem como fracção: são dízimas "
                   "infinitas sem período, como √2 ou π. Chamam-se "
                   "irracionais. Racionais e irracionais juntos formam os "
                   "números reais, ℝ.",
        "exemplo": "√9 = 3 é racional. √2 = 1,4142... não acaba nem repete: é "
                   "irracional. Assim, ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ.",
        "lembra": "Se a raiz não é exacta, o número é irracional.",
    },
    "mat-8c:u4:n1": {
        "explica": "Um intervalo é o conjunto dos reais entre dois números. "
                   "Parêntesis recto para dentro inclui o extremo; para fora "
                   "exclui. Intersecção é a parte comum; reunião é tudo junto.",
        "exemplo": "2 ≤ x ≤ 5 é [2, 5]. Em ]0, 3] o 0 fica de fora e o 3 "
                   "dentro. [1, 6] ∩ [4, 9] = [4, 6].",
        "lembra": "Parêntesis virado para dentro, o número entra.",
    },
    "mat-8c:u4:n2": {
        "explica": "Uma inequação resolve-se como uma equação, com uma "
                   "excepção: ao multiplicar ou dividir os dois membros por um "
                   "número negativo, o sentido da desigualdade inverte-se.",
        "exemplo": "x + 3 > 7 dá x > 4. Mas −x < 3: divide-se por −1 e vira, "
                   "x > −3. Em 3x − 4 > 5 vem x > 3, e o menor inteiro é 4.",
        "lembra": "Dividir por negativo vira o sinal da desigualdade.",
    },
    "mat-8c:u5:n1": {
        "explica": "Uma recta pode ser exterior à circunferência, tangente se "
                   "lhe toca num só ponto, ou secante se a corta em dois. A "
                   "tangente é perpendicular ao raio no ponto de tangência. A "
                   "maior corda é o diâmetro.",
        "exemplo": "Uma roda de bicicleta no chão: o chão é tangente, toca-lhe "
                   "num ponto só, e faz 90 graus com o raio até esse ponto.",
        "lembra": "Tangente toca; secante corta.",
    },
    "mat-8c:u5:n2": {
        "explica": "A circunferência completa tem 360 graus. Um ângulo "
                   "inscrito mede metade do ângulo ao centro que abrange o "
                   "mesmo arco. O perímetro é 2 × π × r, e um arco é a parte "
                   "do perímetro que o seu ângulo ocupa.",
        "exemplo": "Raio 7 cm com π = 22/7: perímetro 2 × 22/7 × 7 = 44 cm. "
                   "Um arco de 90 graus é um quarto da volta: 40 : 4 = 10 cm.",
        "lembra": "Inscrito é metade do ângulo ao centro.",
    },
    "mat-8c:u6:n1": {
        "explica": "Um monómio é um número vezes letras com expoentes: 5x³ tem "
                   "coeficiente 5 e parte literal x³. O grau é a soma dos "
                   "expoentes. Só se somam monómios semelhantes, com a mesma "
                   "parte literal.",
        "exemplo": "4x²y³ tem grau 2 + 3 = 5. 3x + 5x = 8x, porque são "
                   "semelhantes. 2x × 3x = 6x², somando os expoentes.",
        "lembra": "Soma-se o que é semelhante; multiplica-se tudo.",
    },
    "mat-8c:u6:n2": {
        "explica": "Um sistema de duas equações a duas incógnitas tem por "
                   "solução o par (x, y) que verifica as duas ao mesmo tempo. "
                   "Resolve-se por substituição ou somando as equações para "
                   "eliminar uma incógnita.",
        "exemplo": "x + y = 10 e x − y = 2. Somando: 2x = 12, x = 6. Então "
                   "y = 4. Se as rectas fossem paralelas, não havia solução.",
        "lembra": "Verifica: a solução tem de servir nas duas equações.",
    },
    "mat-8c:u7:n1": {
        "explica": "Dois triângulos são congruentes quando têm os lados e os "
                   "ângulos iguais, cada um ao seu. Basta verificar um "
                   "critério: LLL, LAL ou ALA. Uma isometria move a figura "
                   "sem lhe mudar as distâncias.",
        "exemplo": "Dois triângulos com lados 3, 4 e 5 são congruentes pelo "
                   "critério LLL. Se têm dois lados iguais e o ângulo entre "
                   "eles igual, é LAL.",
        "lembra": "L é lado, A é ângulo: LLL, LAL, ALA.",
    },
    "mat-8c:u7:n2": {
        "explica": "Num triângulo rectângulo, o lado oposto ao ângulo recto é "
                   "a hipotenusa e os outros dois são os catetos. Teorema de "
                   "Pitágoras: o quadrado da hipotenusa é a soma dos "
                   "quadrados dos catetos.",
        "exemplo": "Catetos 3 e 4: 3² + 4² = 9 + 16 = 25, e a hipotenusa é "
                   "√25 = 5. Hipotenusa 13 e cateto 5: 13² − 5² = 144, e o "
                   "outro cateto é 12.",
        "lembra": "A hipotenusa é sempre o lado maior.",
    },
    "mat-8c:u7:n3": {
        "explica": "Um quadrilátero tem quatro lados e os ângulos internos "
                   "somam 360 graus. O paralelogramo tem lados opostos "
                   "paralelos e iguais; o losango tem os quatro iguais; o "
                   "trapézio tem só um par de lados paralelos.",
        "exemplo": "Ângulos de 90, 90 e 110: o quarto é 360 − 290 = 70 graus.",
        "lembra": "Os quatro ângulos somam 360, como duas vezes 180.",
    },
    "mat-8c:u8:n1": {
        "explica": "A população é o conjunto todo; a amostra é a parte que se "
                   "observa. A frequência absoluta é quantas vezes um valor "
                   "aparece. A média soma tudo e divide; a moda é o mais "
                   "frequente; a mediana é o do meio, depois de ordenar.",
        "exemplo": "Notas 12, 14, 16, 18: média (12 + 14 + 16 + 18) : 4 = 15. "
                   "Em 3, 9, 4, 7, 5 ordena-se 3, 4, 5, 7, 9 e a mediana é 5.",
        "lembra": "Para a mediana, ordena primeiro.",
    },
    "mat-8c:u9:n1": {
        "explica": "Uma translação desloca a figura segundo um vector, sem a "
                   "rodar. Uma reflexão espelha-a num eixo: cada ponto fica "
                   "à mesma distância, do outro lado. Uma rotação roda-a à "
                   "volta de um ponto, por um ângulo.",
        "exemplo": "Um quadrado tem 4 eixos de simetria: dois pelas diagonais "
                   "e dois pelo meio dos lados. Quatro rotações de 90 graus "
                   "dão a volta completa.",
        "lembra": "Translação desliza, reflexão espelha, rotação roda.",
    },

    # ---------------------------------------------------------------
    # Portugues -- 8a classe
    # ---------------------------------------------------------------
    "por-8c:u1:n1": {
        "explica": "Um regulamento de avaliação é um texto normativo: diz o "
                   "que se deve e não se deve fazer. Organiza-se em artigos "
                   "numerados, e a linguagem é clara, objectiva e impessoal — "
                   "não fala de ninguém em particular.",
        "exemplo": "«Artigo 3. O aluno deve apresentar-se à prova com o "
                   "cartão de estudante.» O verbo «deve» impõe um dever a "
                   "todos os alunos.",
        "lembra": "Normativo é o texto que manda; dever e proibir são as suas "
                  "palavras.",
    },
    "por-8c:u1:n2": {
        "explica": "Nome e adjectivo concordam em género e número: prova "
                   "escrita, provas escritas. Para dar ordens usa-se o "
                   "imperativo — entrega, sentem-se. Nos regulamentos, a "
                   "regra vem muitas vezes no infinitivo: é proibido copiar.",
        "exemplo": "Os resultados finais saem em Dezembro. Sentem-se e leiam "
                   "as instruções. É proibido copiar durante a prova.",
        "lembra": "O adjectivo veste-se como o nome: no mesmo género e no "
                  "mesmo número.",
    },
    "por-8c:u1:n3": {
        "explica": "Na voz activa o sujeito faz a acção; na passiva recebe-a, "
                   "e quem a faz passa a agente da passiva, com «por». As "
                   "orações coordenadas disjuntivas ligam-se por «ou» e "
                   "apresentam alternativas.",
        "exemplo": "O director aprovou o regulamento. Na passiva: O "
                   "regulamento foi aprovado pelo director. Disjuntiva: "
                   "Estudas ou reprovas.",
        "lembra": "Na passiva, o «pelo» aponta para quem fez.",
    },
    "por-8c:u2:n1": {
        "explica": "A convocatória chama pessoas a uma reunião e tem de dizer "
                   "o dia, a hora, o local e o assunto. O verbo concorda com "
                   "o sujeito em pessoa e número: os pais foram, tu e o teu "
                   "irmão vão.",
        "exemplo": "«Convocam-se os encarregados de educação para a reunião "
                   "de sexta-feira, às 15 horas, na sala 4.» Ontem nós "
                   "estivemos na reunião.",
        "lembra": "Sujeito no plural, verbo no plural.",
    },
    "por-8c:u2:n2": {
        "explica": "A acta regista o que se passou numa reunião: a data, "
                   "quem esteve presente, os assuntos tratados e as decisões. "
                   "Escreve-se depois da reunião, em linguagem formal e "
                   "objectiva, e é assinada pelo secretário e pelo presidente.",
        "exemplo": "«Aos dez dias de Março reuniram-se os pais... Foi "
                   "decidido comprar livros para a biblioteca.» Assinam o "
                   "secretário e o presidente.",
        "lembra": "A convocatória vem antes da reunião; a acta vem depois.",
    },
    "por-8c:u2:n3": {
        "explica": "O modo conjuntivo exprime desejo, dúvida ou possibilidade: "
                   "espero que venham. Os tempos compostos formam-se com o "
                   "auxiliar ter e um particípio: tinha começado é o "
                   "pretérito mais-que-perfeito composto.",
        "exemplo": "Presente do conjuntivo: que eu fale. Quando cheguei, a "
                   "reunião já tinha começado. Ao director escreve-se "
                   "«Excelentíssimo Senhor Director».",
        "lembra": "Tinha + particípio: uma coisa que aconteceu antes de outra "
                  "no passado.",
    },
    "por-8c:u3:n1": {
        "explica": "A notícia conta um acontecimento real e responde a seis "
                   "perguntas: quem, o quê, quando, onde, como e porquê. O "
                   "primeiro parágrafo resume o essencial, e a linguagem é "
                   "clara e objectiva, sem opiniões.",
        "exemplo": "«Chuvas fortes fecharam a estrada de Lichinga a Cuamba na "
                   "terça-feira.» O quê: chuvas fecharam a estrada. Onde: de "
                   "Lichinga a Cuamba. Quando: na terça-feira.",
        "lembra": "Primeiro o essencial; os pormenores vêm depois.",
    },
    "por-8c:u3:n2": {
        "explica": "Os advérbios dizem quando (ontem), onde (aqui) e como "
                   "(devagar). Os numerais cardinais contam (vinte); os "
                   "ordinais ordenam (vigésimo). Os complementos "
                   "circunstanciais dizem o tempo, o lugar e o modo da acção.",
        "exemplo": "O jogo começou às quinze horas (tempo) no campo da escola "
                   "(lugar). Terceiro é o ordinal de três.",
        "lembra": "Advérbio de tempo, lugar ou modo: pergunta quando, onde, "
                  "como.",
    },
    "por-8c:u3:n3": {
        "explica": "O anúncio classificado é curto e directo, para caber num "
                   "espaço pequeno. As preposições a, de, em, para e por ligam "
                   "palavras. As esdrúxulas acentuam-se sempre: lâmpada, "
                   "médico, sílaba.",
        "exemplo": "«Vende-se bicicleta em bom estado. Contactar a Amina.» "
                   "Vou de Lichinga para Cuamba: de e para são preposições.",
        "lembra": "Sílaba tónica na antepenúltima: leva sempre acento.",
    },
    "por-8c:u4:n1": {
        "explica": "O texto expositivo explica um assunto de forma clara e "
                   "organizada: é o texto dos manuais de Ciências e de "
                   "História. Vai do geral para o particular, dá exemplos, e "
                   "usa termos precisos e uma linguagem objectiva.",
        "exemplo": "«A água existe em três estados: sólido, líquido e gasoso. "
                   "O gelo, por exemplo, é água no estado sólido.» Primeiro a "
                   "ideia geral, depois o exemplo.",
        "lembra": "Expor é explicar, não contar nem convencer.",
    },
    "por-8c:u4:n2": {
        "explica": "Um verbo transitivo precisa de um complemento: leu o "
                   "livro. Um intransitivo não precisa: dormiu. O complemento "
                   "directo responde a «o quê?»; o indirecto responde a «a "
                   "quem?». O sujeito é quem faz a acção.",
        "exemplo": "A Amina (sujeito) leu o livro (complemento directo). O "
                   "professor deu um prémio ao aluno (complemento indirecto).",
        "lembra": "Directo: o quê? Indirecto: a quem?",
    },
    "por-8c:u4:n3": {
        "explica": "O relato conta factos reais pela ordem em que aconteceram. "
                   "O condicional diz o que aconteceria: iria. As orações "
                   "subordinadas temporais dizem quando (quando chegou); as "
                   "condicionais põem uma condição (se estudares).",
        "exemplo": "Eu iria à festa se pudesse. Quando a chuva parou, saímos. "
                   "Se estudares, passas. Ontem ele disse a verdade.",
        "lembra": "«Quando» é tempo; «se» é condição.",
    },
    "por-8c:u5:n1": {
        "explica": "A lenda é uma narrativa tradicional que mistura factos e "
                   "imaginação; o mito explica a origem de alguma coisa. O "
                   "tempo pode ser cronológico, o do relógio, ou psicológico, "
                   "o que a personagem sente. O retrato é físico ou "
                   "psicológico.",
        "exemplo": "«O Ali era alto e tinha os olhos escuros» é um retrato "
                   "físico directo. Quando o narrador pára para descrever o "
                   "rio, há uma pausa na acção. Ontem eu vim cedo.",
        "lembra": "Directo é o que o narrador diz; indirecto é o que se "
                  "adivinha pelo que a personagem faz.",
    },
    "por-8c:u5:n2": {
        "explica": "Num poema cada linha é um verso e cada grupo de versos é "
                   "uma estrofe. A comparação usa «como»; a metáfora diz que "
                   "uma coisa é outra; a hipérbole exagera. Rui de Noronha e "
                   "Marcelino dos Santos são poetas moçambicanos.",
        "exemplo": "«Os teus olhos são como estrelas» é comparação. «Os teus "
                   "olhos são duas estrelas» é metáfora. «Chorei um rio de "
                   "lágrimas» é hipérbole.",
        "lembra": "Com «como» é comparação; sem «como» é metáfora.",
    },
    "por-8c:u5:n3": {
        "explica": "O texto dramático é escrito para ser representado: tem "
                   "falas de personagens e didascálias, as indicações sobre "
                   "gestos e cenário. No discurso directo a personagem fala; "
                   "no indirecto o narrador conta o que ela disse.",
        "exemplo": "Directo: A Amina disse: — Vou à escola. Indirecto: A "
                   "Amina disse que ia à escola. Numa peça, ao professor "
                   "diz-se «Senhor professor».",
        "lembra": "Directo tem travessão; indirecto tem «que».",
    },

    # ---------------------------------------------------------------
    # Geografia -- 8a classe  (Geografia Humana ou Economica)
    # ---------------------------------------------------------------
    "geo-8c:u1:n1": {
        "explica": "A Geografia Física estuda a natureza: o relevo, o clima, "
                   "os rios. A Geografia Humana ou Económica estuda as "
                   "pessoas — onde vivem, quantas são, o que fazem e como "
                   "organizam o espaço.",
        "exemplo": "Perguntar porque é que Lichinga cresce, de que vive a "
                   "sua gente e de onde vêm os que lá chegam é fazer "
                   "Geografia Humana.",
        "lembra": "Física é a natureza; Humana são as pessoas no espaço.",
    },
    "geo-8c:u2:n1": {
        "explica": "A natalidade conta os nascimentos e a mortalidade as "
                   "mortes, por cada mil habitantes num ano. A diferença é o "
                   "crescimento natural. As migrações são mudanças de "
                   "residência: quem sai emigra, quem chega imigra.",
        "exemplo": "30 nascimentos e 10 mortes por mil dão um crescimento "
                   "natural de 20 por mil. Um jovem que deixa a aldeia para "
                   "trabalhar em Nampula migrou do campo para a cidade.",
        "lembra": "Crescimento natural: nascimentos menos mortes.",
    },
    "geo-8c:u2:n2": {
        "explica": "A população mundial cresceu depressa nos últimos dois "
                   "séculos. A pirâmide etária mostra-a por idades e por "
                   "sexo: base larga é população jovem, topo largo é "
                   "população envelhecida. A estrutura sectorial divide-a "
                   "pelo trabalho que faz.",
        "exemplo": "Moçambique tem uma pirâmide de base larga: há muitas "
                   "crianças. Um país europeu tem o topo mais largo: há "
                   "muitos idosos.",
        "lembra": "Base larga, população jovem.",
    },
    "geo-8c:u2:n3": {
        "explica": "A população concentra-se onde há solos férteis, água e "
                   "clima ameno, e onde há emprego, estradas e serviços. A "
                   "Ásia é o continente mais populoso. Crescer depressa sem "
                   "recursos que cheguem cria problemas e pressiona o "
                   "ambiente.",
        "exemplo": "O vale do Zambeze é fértil e povoado; o deserto do "
                   "Saara é quase vazio. Uma cidade que cresce sem água nem "
                   "recolha de lixo polui os rios de que vive.",
        "lembra": "As pessoas vão para onde há água, terra boa e trabalho.",
    },
    "geo-8c:u3:n1": {
        "explica": "Há três sectores: primário (agricultura, pecuária, "
                   "pesca), secundário (indústria) e terciário (comércio, "
                   "transportes, serviços). A agricultura tradicional usa a "
                   "enxada e a chuva; a moderna usa máquinas e produz para "
                   "vender.",
        "exemplo": "A machamba de milho de sequeiro depende da chuva. Uma "
                   "plantação de chá em Gurué, com máquinas e trabalhadores, "
                   "é agricultura moderna de plantação.",
        "lembra": "Primário tira da natureza, secundário transforma, "
                  "terciário serve.",
    },
    "geo-8c:u3:n2": {
        "explica": "A pecuária é a criação de animais para carne, leite, "
                   "peles ou trabalho. Na criação extensiva o gado pasta "
                   "livre em grandes áreas; na intensiva vive fechado e "
                   "alimentado. Gado a mais no mesmo pasto degrada o solo.",
        "exemplo": "Bovino são os bois e as vacas; caprino são as cabras; "
                   "suíno são os porcos. Nas pastagens de Tete o gado bovino "
                   "cria-se de forma extensiva.",
        "lembra": "Extensiva: muito espaço, pouco gado por hectare.",
    },
    "geo-8c:u3:n3": {
        "explica": "A indústria transforma matérias-primas em produtos. A "
                   "Revolução Industrial começou em Inglaterra, no século "
                   "XVIII, e fez crescer as fábricas e as cidades. Uma "
                   "fábrica instala-se onde há matérias-primas, energia, "
                   "mão-de-obra e transportes.",
        "exemplo": "A Europa, a América do Norte e a Ásia Oriental são as "
                   "regiões mais industrializadas. Uma fábrica de cimento "
                   "instala-se perto do calcário e de uma estrada.",
        "lembra": "A indústria vai para onde estão as matérias-primas e os "
                  "transportes.",
    },
    "geo-8c:u3:n4": {
        "explica": "O comércio é comprar e vender. É interno dentro do país e "
                   "externo entre países. A balança comercial compara o que "
                   "se exporta com o que se importa: exporta-se mais, o "
                   "saldo é positivo. Bancos e seguros formam o sistema "
                   "financeiro.",
        "exemplo": "Exportar 80 milhões e importar 50 dá um saldo de 30 "
                   "milhões, positivo. Moçambique exporta carvão, alumínio e "
                   "gás, e importa combustível e máquinas.",
        "lembra": "Balança: exportações menos importações.",
    },
    "geo-8c:u3:n5": {
        "explica": "O turismo é a deslocação de pessoas, por lazer, cultura "
                   "ou descanso, para fora de onde vivem. Pode ser cultural, "
                   "ambiental, religioso, desportivo. Precisa de paisagens, "
                   "património e segurança — e em excesso polui e estraga o "
                   "que o atraiu.",
        "exemplo": "O Lago Niassa e o Gorongosa atraem turismo ambiental; a "
                   "Ilha de Moçambique, património da humanidade, atrai "
                   "turismo cultural.",
        "lembra": "O turismo vive do que preserva.",
    },
    "geo-8c:u3:n6": {
        "explica": "Os transportes levam pessoas e cargas: por terra, mar e "
                   "ar, cada um com vantagens. O navio leva muito a baixo "
                   "custo; o avião é rápido. Os meios de comunicação levam "
                   "informação. Desenvolvimento sustentável é usar os "
                   "recursos sem os esgotar.",
        "exemplo": "O corredor de Nacala liga o Malawi ao porto pela linha "
                   "férrea. Um peão atravessa na passadeira e olha para os "
                   "dois lados: é educação rodoviária.",
        "lembra": "Transporte leva coisas; comunicação leva informação.",
    },
    "geo-8c:u4:n1": {
        "explica": "As cidades cresceram muito depois da Revolução "
                   "Industrial, com a chegada de trabalhadores. A taxa de "
                   "urbanização é a percentagem da população que vive em "
                   "cidades. Campo e cidade dependem um do outro, e cada "
                   "cidade tem funções principais.",
        "exemplo": "4 milhões em cidades num país de 10 milhões dão 40% de "
                   "urbanização. Maputo é a capital administrativa; a Beira "
                   "é porto e comércio.",
        "lembra": "O campo alimenta a cidade; a cidade serve o campo.",
    },
    "geo-8c:u4:n2": {
        "explica": "Crescer depressa traz problemas às cidades: bairros sem "
                   "água, luz e saneamento, trânsito, lixo, drogas. O "
                   "planeamento urbano organiza ruas, bairros e serviços. "
                   "Uma cidade sustentável recolhe o lixo, planta árvores e "
                   "poupa água e energia.",
        "exemplo": "Um bairro planeado tem ruas, água canalizada, escola e "
                   "espaço verde. Os conflitos resolvem-se pelo diálogo, "
                   "numa cultura de paz.",
        "lembra": "Cidade planeada é cidade com água, escola e ruas para "
                  "todos.",
    },

    # ---------------------------------------------------------------
    # Historia -- 8a classe
    # ---------------------------------------------------------------
    "his-8c:u1:n1": {
        "explica": "No século XV a Europa vivia o Antigo Regime: uma "
                   "sociedade de ordens — clero, nobreza e povo — e uma "
                   "economia agrária. A África tinha reinos e impérios "
                   "fortes, como o Monomotapa, o Mali e o Congo, que "
                   "comerciavam ouro, marfim e escravos.",
        "exemplo": "Na costa de Moçambique, antes dos portugueses, o ouro do "
                   "Monomotapa saía por Sofala para os comerciantes árabes e "
                   "suaílis do Índico.",
        "lembra": "A África do século XV não estava vazia nem atrasada: tinha "
                  "reinos e comércio.",
    },
    "his-8c:u1:n2": {
        "explica": "Os europeus lançaram-se ao mar à procura de ouro e "
                   "especiarias. Vasco da Gama passou por Moçambique em 1498, "
                   "a caminho da Índia, e os portugueses ficaram na costa: "
                   "Sofala e a Ilha de Moçambique. Vieram as trocas desiguais "
                   "e o tráfico.",
        "exemplo": "Milhões de africanos foram levados à força para as "
                   "plantações da América e para as ilhas do Índico. A "
                   "África perdeu gente e riquezas, e os reinos "
                   "enfraqueceram.",
        "lembra": "Expansão para uns foi pilhagem para outros.",
    },
    "his-8c:u1:n3": {
        "explica": "O Renascimento, nascido em Itália, pôs o ser humano no "
                   "centro: é o Humanismo. Nasceram a imprensa e a ciência "
                   "moderna. Em 1517 Lutero abriu a Reforma Protestante, e a "
                   "Igreja Católica respondeu com a Contra-Reforma.",
        "exemplo": "Gutenberg inventou a imprensa; Copérnico disse que a "
                   "Terra gira à volta do Sol. Luteranismo na Alemanha, "
                   "Calvinismo na Suíça, Anglicanismo em Inglaterra.",
        "lembra": "Renascimento é olhar para o homem; Reforma é dividir a "
                  "Igreja.",
    },
    "his-8c:u1:n4": {
        "explica": "O mercantilismo media a riqueza pelo ouro e prata "
                   "acumulados, e usava as colónias para fornecer "
                   "matérias-primas e comprar produtos. O absolutismo pôs "
                   "todo o poder no rei, que dizia recebê-lo de Deus.",
        "exemplo": "Luís XIV, em França, é o exemplo do rei absoluto: «O "
                   "Estado sou eu». O ouro que vinha das colónias enchia os "
                   "cofres da Europa.",
        "lembra": "Mercantilismo é a economia; absolutismo é o poder.",
    },
    "his-8c:u1:n5": {
        "explica": "As revoluções burguesas derrubaram o Antigo Regime. Em "
                   "Inglaterra o Parlamento limitou o rei. A América fez-se "
                   "independente e escreveu a Constituição de 1787. Em 1789 a "
                   "Revolução Francesa proclamou liberdade, igualdade e "
                   "fraternidade.",
        "exemplo": "Em França o povo passava fome enquanto o clero e a "
                   "nobreza não pagavam impostos. A 14 de Julho de 1789 "
                   "tomou a Bastilha.",
        "lembra": "1787 é a Constituição americana; 1789 é a Bastilha.",
    },
    "his-8c:u2:n1": {
        "explica": "Enquanto a Europa fazia revoluções, quase toda a África "
                   "era governada por reinos africanos. Em Moçambique os "
                   "portugueses estavam na costa e no vale do Zambeze, nos "
                   "prazos, e a economia assentava no marfim e no tráfico de "
                   "escravos.",
        "exemplo": "Um prazo era uma grande terra concedida pela Coroa a um "
                   "colono, que a explorava e cobrava aos habitantes. A "
                   "indústria europeia passou a querer mais matérias-primas "
                   "de África.",
        "lembra": "No início do século XIX a ocupação europeia de África era "
                  "ainda pequena.",
    },
    "his-8c:u3:n1": {
        "explica": "A Revolução Industrial começou em Inglaterra, no século "
                   "XVIII, porque havia carvão, ferro, capitais e mercados. A "
                   "máquina a vapor deu energia às fábricas e à locomotiva. "
                   "A segunda fase trouxe a electricidade, o petróleo e o "
                   "aço.",
        "exemplo": "O tear mecânico fazia num dia o que um artesão fazia num "
                   "mês. O comboio levou o carvão e os tecidos por todo o "
                   "país.",
        "lembra": "Primeira fase: carvão e vapor. Segunda: electricidade e "
                  "petróleo.",
    },
    "his-8c:u3:n2": {
        "explica": "A produção saiu das oficinas para as fábricas. Cresceram "
                   "duas classes: a burguesia, dona das fábricas, e o "
                   "proletariado, que vendia o seu trabalho. As cidades "
                   "cresceram depressa, e com elas a poluição e os bairros "
                   "pobres.",
        "exemplo": "Manchester passou de vila a cidade de fábricas em poucas "
                   "décadas, com o ar negro do fumo do carvão.",
        "lembra": "Fábrica, cidade, burguesia e proletariado nascem juntos.",
    },
    "his-8c:u3:n3": {
        "explica": "Os operários trabalhavam catorze horas por salários "
                   "baixos, e mulheres e crianças recebiam ainda menos. Para "
                   "se defenderem criaram sindicatos — os trade-unions — e "
                   "partidos operários, que exigiam menos horas, mais "
                   "salário e o voto.",
        "exemplo": "Uma greve parava a fábrica até o patrão negociar. Foi "
                   "assim que se conquistou o dia de oito horas.",
        "lembra": "Sozinho o operário não podia nada; junto, podia parar a "
                  "fábrica.",
    },
    "his-8c:u4:n1": {
        "explica": "Da concorrência entre muitas empresas passou-se aos "
                   "monopólios: poucas empresas a dominar um mercado, por "
                   "concentração horizontal ou vertical, com os bancos a "
                   "mandar na indústria. É o capitalismo monopolista, que "
                   "leva ao imperialismo.",
        "exemplo": "Horizontal: várias fábricas de aço juntam-se numa. "
                   "Vertical: o mesmo dono tem a mina, a fundição e a "
                   "fábrica.",
        "lembra": "Monopólio é um mercado nas mãos de poucos.",
    },
    "his-8c:u4:n2": {
        "explica": "Na Conferência de Berlim, de 1884 a 1885, as potências "
                   "europeias repartiram a África, com a regra da ocupação "
                   "efectiva. Portugal cedeu ao Ultimato inglês de 1890 e "
                   "entregou regiões de Moçambique a companhias "
                   "majestáticas.",
        "exemplo": "A Companhia do Niassa administrou o norte de Moçambique "
                   "como se fosse dona dele, a cobrar impostos e a obrigar a "
                   "trabalhar.",
        "lembra": "Berlim repartiu; a ocupação efectiva obrigou a conquistar.",
    },
    "his-8c:u4:n3": {
        "explica": "Os povos africanos resistiram à ocupação: os zulus "
                   "venceram os ingleses em Isandlwana, os hereros e namas "
                   "lutaram contra os alemães, e em Moçambique Ngungunhane "
                   "foi preso em Chaimite, em 1895, e o Barué revoltou-se em "
                   "1917.",
        "exemplo": "Ngungunhane, imperador de Gaza, resistiu anos aos "
                   "portugueses. Depois de preso foi levado para os Açores, "
                   "onde morreu.",
        "lembra": "A ocupação colonial foi imposta pela força — e combatida.",
    },

    # ---------------------------------------------------------------
    # Biologia -- 8a classe
    # ---------------------------------------------------------------
    "bio-8c:u1:n1": {
        "explica": "A célula é feita sobretudo de água, com sais, proteínas "
                   "e lípidos. Cada organelo tem uma função: o núcleo guarda "
                   "os genes, a mitocôndria produz energia, o cloroplasto faz "
                   "a fotossíntese, a membrana controla o que entra e sai.",
        "exemplo": "Só a célula vegetal tem parede celular e cloroplastos. O "
                   "vacúolo, grande nas plantas, guarda água — é por isso que "
                   "uma folha sem água murcha.",
        "lembra": "Núcleo manda, mitocôndria dá energia, cloroplasto faz "
                  "comida.",
    },
    "bio-8c:u1:n2": {
        "explica": "Na fotossíntese, a planta junta água e dióxido de carbono "
                   "com a luz, nos cloroplastos, e produz glicose e "
                   "oxigénio. Na respiração, todas as células gastam glicose "
                   "e oxigénio para ter energia, e libertam dióxido de "
                   "carbono e água.",
        "exemplo": "Uma vela num frasco fechado apaga-se: gastou o oxigénio. "
                   "Com uma planta ao lado, à luz, aguenta mais tempo, porque "
                   "a planta repõe oxigénio.",
        "lembra": "Fotossíntese faz alimento com luz; respiração gasta-o para "
                  "dar energia.",
    },
    "bio-8c:u2:n1": {
        "explica": "Os recursos naturais são renováveis, como as florestas, "
                   "a água e os animais, que se refazem, ou não renováveis, "
                   "como o carvão, o gás e os minerais, que acabam. "
                   "Conservá-los é usá-los sem os esgotar.",
        "exemplo": "Moçambique tem carvão em Tete, gás em Inhambane e Cabo "
                   "Delgado, rubis em Montepuez e florestas no Niassa. Cortar "
                   "uma árvore e plantar duas é conservar.",
        "lembra": "O que se refaz é renovável; o que acaba não é.",
    },
    "bio-8c:u3:n1": {
        "explica": "O sangue tem quatro grupos, A, B, AB e O. Numa "
                   "transfusão, o sangue do dador tem de ser compatível com "
                   "o do doente: o grupo O pode dar a todos, e o AB pode "
                   "receber de todos. Doar sangue salva vidas.",
        "exemplo": "Uma mãe que perde muito sangue no parto precisa de uma "
                   "transfusão compatível. É por isso que os hospitais "
                   "pedem dadores de todos os grupos.",
        "lembra": "O dá a todos; AB recebe de todos.",
    },
    "bio-8c:u3:n2": {
        "explica": "Excretar é deitar fora o que o corpo não quer. Os rins "
                   "filtram o sangue e fazem a urina, que desce pelos "
                   "ureteres até à bexiga e sai pela uretra. Os pulmões "
                   "excretam dióxido de carbono e a pele excreta o suor.",
        "exemplo": "Dor ou ardor ao urinar é sinal de infecção urinária. "
                   "Beber água, manter a higiene e não segurar a urina "
                   "protegem os rins.",
        "lembra": "Rins, ureteres, bexiga, uretra: é esse o caminho.",
    },
    "bio-8c:u3:n3": {
        "explica": "As glândulas endócrinas produzem hormonas, mensageiros "
                   "químicos que viajam no sangue. O pâncreas faz a "
                   "insulina, a tiróide regula o metabolismo, as "
                   "supra-renais fazem a adrenalina e as glândulas sexuais "
                   "comandam a puberdade.",
        "exemplo": "A falta de iodo faz a tiróide inchar: é o bócio. Hormona "
                   "do crescimento a mais dá gigantismo; a menos, nanismo.",
        "lembra": "Hormona é uma mensagem que vai no sangue.",
    },
    "bio-8c:u4:n1": {
        "explica": "Uma alimentação equilibrada tem de todos os grupos da "
                   "roda dos alimentos, na medida certa. As proteínas "
                   "constroem, os hidratos de carbono dão energia, os lípidos "
                   "são reserva. As vitaminas e os minerais regulam o corpo.",
        "exemplo": "O feijão e o peixe dão proteínas; a xima e o arroz dão "
                   "energia; as folhas verdes e o leite dão cálcio; a "
                   "papaia e a manga dão vitamina A.",
        "lembra": "Comer de tudo um pouco, e de cada coisa não de mais.",
    },
    "bio-8c:u4:n2": {
        "explica": "Comer mal adoece. O kwashiorkor vem da falta de "
                   "proteínas e o marasmo da falta geral de alimento. Falta "
                   "de vitamina A dá cegueira nocturna, de vitamina D "
                   "raquitismo, de vitamina C escorbuto, de ferro anemia. "
                   "Comer a mais dá obesidade.",
        "exemplo": "Uma criança com a barriga inchada e o cabelo a "
                   "descolorar pode ter kwashiorkor: falta-lhe feijão, "
                   "peixe, ovos, carne.",
        "lembra": "Cada doença da má alimentação tem um nutriente em falta.",
    },
    "bio-8c:u4:n3": {
        "explica": "A febre tifóide, a lombriga, a ténia e os oxiúros entram "
                   "pela boca: água e comida contaminadas com fezes, carne "
                   "mal cozida, mãos sujas. A prevenção é sempre a mesma: "
                   "lavar as mãos, ferver a água, cozer bem a carne e usar "
                   "latrina.",
        "exemplo": "A ténia apanha-se em carne de porco mal passada. Os "
                   "oxiúros passam das unhas para a boca — daí lavar as "
                   "mãos antes de comer.",
        "lembra": "Mãos lavadas, água fervida, carne bem cozida.",
    },
    "bio-8c:u5:n1": {
        "explica": "Na reprodução assexuada um só progenitor dá seres "
                   "iguais a ele; na sexuada juntam-se dois. As plantas "
                   "multiplicam-se sem semente por estacaria, mergulhia, "
                   "enxertia e alporquia — e o camponês usa isso todos os "
                   "dias.",
        "exemplo": "A mandioca e a batata-doce plantam-se por estaca: um "
                   "pedaço de caule na terra dá uma planta igual à mãe, "
                   "mais depressa do que uma semente.",
        "lembra": "Estaca é um pedaço de caule que ganha raízes.",
    },
    "bio-8c:u5:n2": {
        "explica": "Os estames têm o pólen e o pistilo tem os óvulos. A "
                   "polinização leva o pólen ao pistilo, pelo vento, insectos "
                   "ou aves. Depois da fecundação, o ovário vira fruto e os "
                   "óvulos viram sementes, que o vento, a água e os animais "
                   "espalham.",
        "exemplo": "O coco viaja pelo mar; a semente do capim vai no vento; "
                   "a do feijão leva um embrião e reservas para germinar.",
        "lembra": "Pólen ao pistilo é polinização; ovário a fruto é "
                  "frutificação.",
    },
    "bio-8c:u6:n1": {
        "explica": "Na adolescência há conflitos com os pais e os amigos, e "
                   "resolvem-se a conversar e a ouvir. Rapazes e raparigas "
                   "partilham as tarefas e têm os mesmos direitos. Casar "
                   "antes dos dezoito é uma união prematura, e a lei "
                   "moçambicana proíbe-a.",
        "exemplo": "Uma rapariga casada aos catorze anos quase sempre deixa "
                   "a escola, e uma gravidez tão cedo é um risco para a "
                   "vida dela.",
        "lembra": "Dezoito anos: antes disso, escola e não casamento.",
    },
    "bio-8c:u6:n2": {
        "explica": "A gonorreia, a sífilis e o HIV apanham-se em relações "
                   "sexuais sem protecção. Sinais: corrimento, feridas, dor "
                   "ao urinar. Previnem-se com abstinência e preservativo. O "
                   "HIV destrói as defesas e deixa entrar a tuberculose e "
                   "outras infecções.",
        "exemplo": "Quem tem HIV e toma os anti-retrovirais todos os dias "
                   "vive muitos anos com saúde e não transmite o vírus. O "
                   "teste é gratuito no centro de saúde.",
        "lembra": "Abstinência ou preservativo, e fazer o teste.",
    },

    # ---------------------------------------------------------------
    # Fisica -- 8a classe  (a primeira Fisica da app)
    #
    # As unidades escrevem-se por extenso, como nos enunciados: a voz nao
    # sabe dizer "m/s" nem "J".
    # ---------------------------------------------------------------
    "fis-8c:u1:n1": {
        "explica": "A Física estuda os fenómenos em que a matéria não muda de "
                   "substância: o gelo derrete e continua a ser água. Matéria "
                   "é tudo o que tem massa e ocupa espaço, e tem propriedades "
                   "gerais como a inércia e a impenetrabilidade.",
        "exemplo": "Lenha a arder é fenómeno químico: vira cinza e fumo. Água "
                   "a subir por um pavio é capilaridade, um fenómeno físico.",
        "lembra": "Físico muda a forma; químico muda a substância.",
    },
    "fis-8c:u1:n2": {
        "explica": "As grandezas fundamentais são o comprimento, a massa e o "
                   "tempo: medem-se em metros, quilogramas e segundos, as "
                   "unidades do Sistema Internacional. A velocidade, a área e "
                   "a força são derivadas: calculam-se a partir delas.",
        "exemplo": "1 metro e meio são 150 centímetros; 2 quilogramas são "
                   "2000 gramas. A fita métrica mede o comprimento, a balança "
                   "a massa, o cronómetro o tempo.",
        "lembra": "Metro, quilograma, segundo: as três unidades de base.",
    },
    "fis-8c:u2:n1": {
        "explica": "Um corpo está em movimento quando muda de posição em "
                   "relação a um ponto de referência — e pode estar parado em "
                   "relação a um e em movimento em relação a outro. A "
                   "velocidade é a distância a dividir pelo tempo, em metros "
                   "por segundo.",
        "exemplo": "100 metros em 20 segundos: 100 a dividir por 20 dá 5 "
                   "metros por segundo. Sentado no autocarro, estás parado "
                   "em relação a ele e em movimento em relação à estrada.",
        "lembra": "Velocidade é distância a dividir pelo tempo.",
    },
    "fis-8c:u2:n2": {
        "explica": "No movimento rectilíneo uniforme a trajectória é uma "
                   "recta e a velocidade não muda. Distância é velocidade "
                   "vezes tempo. No gráfico da distância pelo tempo sai uma "
                   "recta inclinada; no da velocidade pelo tempo, uma recta "
                   "horizontal.",
        "exemplo": "A 60 quilómetros por hora, em 2 horas andam-se 120 "
                   "quilómetros. A 5 metros por segundo, 200 metros levam "
                   "200 a dividir por 5, ou seja 40 segundos.",
        "lembra": "Uniforme: a mesma velocidade do princípio ao fim.",
    },
    "fis-8c:u2:n3": {
        "explica": "A aceleração é quanto a velocidade muda por segundo. "
                   "Se cresce ao mesmo ritmo é uniformemente acelerado; se "
                   "diminui, retardado. Na queda livre todos os corpos caem "
                   "com a mesma aceleração, perto de 10 metros por segundo "
                   "em cada segundo.",
        "exemplo": "Parte do repouso e ganha 2 metros por segundo a cada "
                   "segundo: ao fim de 5 segundos vai a 10. Em queda livre, "
                   "ao fim de 3 segundos vai a 30 metros por segundo.",
        "lembra": "Velocidade final é aceleração vezes tempo, partindo do "
                  "repouso.",
    },
    "fis-8c:u3:n1": {
        "explica": "Uma força põe um corpo em movimento, pára-o ou "
                   "deforma-o. Tem ponto de aplicação, direcção, sentido e "
                   "intensidade, e mede-se em newtons. Forças na mesma "
                   "direcção somam-se se têm o mesmo sentido e subtraem-se "
                   "se têm sentidos contrários.",
        "exemplo": "Duas pessoas a empurrar no mesmo sentido, com 200 e 300 "
                   "newtons, fazem 500. A puxar uma corda em sentidos "
                   "contrários, com 400 e 150, a resultante é 250.",
        "lembra": "Mesmo sentido soma; sentidos contrários subtraem.",
    },
    "fis-8c:u3:n2": {
        "explica": "Primeira lei: sem forças, o corpo fica como está — parado "
                   "ou em movimento uniforme. É a inércia. Segunda lei: força "
                   "é massa vezes aceleração. Terceira lei: a toda a acção "
                   "corresponde uma reacção igual e de sentido contrário.",
        "exemplo": "O autocarro trava e tu vais para a frente: inércia. 2 "
                   "quilogramas com aceleração de 3 pedem 6 newtons. Empurras "
                   "a parede e a parede empurra-te.",
        "lembra": "Inércia, força igual a massa vezes aceleração, acção e "
                  "reacção.",
    },
    "fis-8c:u4:n1": {
        "explica": "Uma força realiza trabalho quando desloca o corpo: "
                   "trabalho é força vezes distância, em joules. Energia é a "
                   "capacidade de realizar trabalho — potencial, cinética, "
                   "química, eléctrica — e não se cria nem se destrói, só se "
                   "transforma.",
        "exemplo": "10 newtons ao longo de 2 metros são 20 joules. Numa "
                   "lâmpada, a energia eléctrica vira luz e calor; numa "
                   "pedra a cair, a potencial vira cinética.",
        "lembra": "Trabalho é força vezes distância; a energia só se "
                  "transforma.",
    },
    "fis-8c:u4:n2": {
        "explica": "A potência é o trabalho realizado em cada segundo, em "
                   "watts. A electricidade produz-se a partir de outras "
                   "energias: a água de Cahora Bassa, o carvão, o sol e o "
                   "vento. Sol e vento são renováveis; carvão e petróleo não.",
        "exemplo": "100 joules em 5 segundos são 20 watts. Apagar a luz ao "
                   "sair de uma sala é poupar energia e dinheiro.",
        "lembra": "Potência é trabalho a dividir pelo tempo.",
    },
    "fis-8c:u5:n1": {
        "explica": "A temperatura diz quão quente ou frio está um corpo e "
                   "mede-se com o termómetro, em graus Celsius, kelvin ou "
                   "Fahrenheit. Dois corpos em contacto trocam calor do "
                   "mais quente para o mais frio até ficarem iguais: é o "
                   "equilíbrio térmico.",
        "exemplo": "A água ferve a 100 graus Celsius, 373 kelvin ou 212 "
                   "Fahrenheit. Para passar de Celsius a kelvin soma-se 273: "
                   "25 graus são 298 kelvin.",
        "lembra": "Kelvin é Celsius mais 273.",
    },
    "fis-8c:u5:n2": {
        "explica": "Aquecido, um corpo dilata: aumenta de volume. O calor "
                   "transmite-se por condução nos sólidos, por convecção nos "
                   "líquidos e gases, e por radiação mesmo sem matéria, como "
                   "o do Sol. Os metais são bons condutores.",
        "exemplo": "Os carris têm folgas para não empenarem no calor. A "
                   "colher aquece na panela por condução; o ar quente sobe "
                   "por convecção; o sol aquece a pele por radiação.",
        "lembra": "Condução toca, convecção sobe, radiação atravessa o vazio.",
    },
    "fis-8c:u6:n1": {
        "explica": "O Sol e uma lâmpada são corpos luminosos; a Lua e uma "
                   "parede são iluminados. Num meio homogéneo a luz anda em "
                   "linha recta, e por isso há sombra atrás dos corpos "
                   "opacos, penumbra à volta, e eclipses quando um astro "
                   "tapa outro.",
        "exemplo": "No eclipse do Sol, a Lua fica entre o Sol e a Terra. No "
                   "eclipse da Lua, é a Terra que fica no meio e faz sombra "
                   "na Lua.",
        "lembra": "A luz vai a direito; o que se mete à frente faz sombra.",
    },
    "fis-8c:u6:n2": {
        "explica": "Na reflexão a luz volta ao bater numa "
                   "superfície, e o ângulo de reflexão é igual ao de "
                   "incidência. Num espelho plano a imagem tem o mesmo "
                   "tamanho, está direita, à mesma distância atrás do "
                   "espelho, e trocada da esquerda para a direita.",
        "exemplo": "Um raio que chega a 40 graus sai a 40 graus. A 1 metro do "
                   "espelho, a imagem parece estar 1 metro atrás dele. O "
                   "periscópio usa dois espelhos inclinados.",
        "lembra": "Ângulo de incidência igual ao ângulo de reflexão.",
    },

    # ---------------------------------------------------------------
    # Quimica -- 8a classe  (a primeira Quimica da app)
    #
    # Sem formulas: "H2O" a voz le "aga dois o". Escreve-se "agua".
    # ---------------------------------------------------------------
    "qui-8c:u1:n1": {
        "explica": "A Química estuda as substâncias e as suas "
                   "transformações. Nasceu da alquimia, que procurava "
                   "transformar metais em ouro, e hoje está em casa, na "
                   "medicina, na agricultura e na indústria: sabões, "
                   "adubos, medicamentos, purificação da água.",
        "exemplo": "Ferver água para a tornar potável, conservar peixe com "
                   "sal, deitar adubo na machamba, tomar um comprimido: é "
                   "Química todos os dias.",
        "lembra": "Química: substâncias e transformações.",
    },
    "qui-8c:u1:n2": {
        "explica": "No laboratório não se prova nem se cheira de perto "
                   "nada, o cabelo vai preso, e um ácido na pele lava-se "
                   "logo com muita água. Uma experiência acaba num "
                   "relatório: objectivo, material, procedimento, "
                   "observações e conclusão.",
        "exemplo": "Mudança de cor, um gás a sair, efervescência, calor: "
                   "são os sinais de que houve uma reacção química, e é "
                   "isso que se escreve nas observações.",
        "lembra": "Nunca provar, nunca cheirar de perto, e relatório no "
                  "fim.",
    },
    "qui-8c:u2:n1": {
        "explica": "Matéria é tudo o que tem massa e ocupa lugar. Tem "
                   "propriedades gerais — massa, volume, "
                   "impenetrabilidade, divisibilidade, elasticidade, "
                   "compressibilidade — e três estados: sólido, líquido e "
                   "gasoso, que mudam com o calor.",
        "exemplo": "Fusão é o gelo a virar água; vaporização é a água a "
                   "virar vapor; condensação é o vapor a virar gotas na "
                   "tampa da panela. Dois corpos não cabem no mesmo lugar: "
                   "impenetrabilidade.",
        "lembra": "Matéria: substâncias puras ou misturas.",
    },
    "qui-8c:u2:n2": {
        "explica": "Cada substância tem propriedades específicas que a "
                   "identificam: ponto de fusão, ponto de ebulição, "
                   "densidade, cor, cheiro. Uma substância elementar tem um "
                   "só elemento, como o ferro; uma composta tem vários, "
                   "como a água.",
        "exemplo": "A água pura ferve a 100 graus ao nível do mar. Um "
                   "pedaço de ferro de 40 gramas em 5 centímetros cúbicos "
                   "tem densidade 8: a massa a dividir pelo volume.",
        "lembra": "Densidade é massa a dividir por volume.",
    },
    "qui-8c:u2:n3": {
        "explica": "Uma mistura homogénea não se distingue à vista, como a "
                   "água com açúcar; uma heterogénea sim, como água com "
                   "areia. Separam-se pelas propriedades: evaporação, "
                   "cristalização, destilação; catação, peneiração, "
                   "decantação, filtração, íman.",
        "exemplo": "O sal vem da água do mar por evaporação e cristalização. "
                   "A limalha de ferro sai da areia com um íman. A água "
                   "barrenta decanta-se: espera-se que a terra assente.",
        "lembra": "O método de separação escolhe-se pela propriedade que "
                  "difere.",
    },
    "qui-8c:u3:n1": {
        "explica": "O átomo tem um núcleo com protões e neutrões. O número "
                   "atómico é o número de protões; o número de massa é "
                   "protões mais neutrões. Cada elemento tem um símbolo, e "
                   "os elementos são metais, com brilho e bons condutores, "
                   "ou não metais.",
        "exemplo": "Carbono: 6 protões e 6 neutrões, número de massa 12, "
                   "símbolo C. O cobre é metal e conduz a corrente; o "
                   "enxofre é não metal.",
        "lembra": "Número de massa é protões mais neutrões.",
    },
    "qui-8c:u3:n2": {
        "explica": "Os átomos juntam-se em moléculas. A fórmula diz quantos "
                   "átomos de cada elemento há: a água tem 2 de hidrogénio "
                   "e 1 de oxigénio. A valência diz quantas ligações cada "
                   "átomo faz, e é ela que dita a fórmula.",
        "exemplo": "Hidrogénio valência 1, oxigénio valência 2: são "
                   "precisos 2 hidrogénios para 1 oxigénio. A molécula de "
                   "oxigénio, dois átomos iguais, é elementar; a de água é "
                   "composta.",
        "lembra": "A fórmula conta os átomos; a valência explica-a.",
    },
    "qui-8c:u3:n3": {
        "explica": "A massa atómica relativa compara o átomo com a unidade "
                   "de massa atómica. A massa molecular é a soma das "
                   "massas atómicas dos átomos da molécula, contando cada "
                   "um as vezes que aparece.",
        "exemplo": "Água: 2 vezes 1 mais 16 dá 18. Dióxido de carbono: 12 "
                   "mais 2 vezes 16 dá 44. Oxigénio, dois átomos de 16: 32. "
                   "Sal: 23 mais 35 dá 58.",
        "lembra": "Massa molecular: soma-se cada átomo as vezes que "
                  "aparece.",
    },
    "qui-8c:u3:n4": {
        "explica": "Num fenómeno químico nasce uma substância nova. A "
                   "equação escreve a reacção; pela lei de Lavoisier, a "
                   "massa dos produtos é igual à dos reagentes, e por isso "
                   "se acerta. Há reacções de combinação, decomposição, "
                   "exotérmicas e endotérmicas.",
        "exemplo": "4 gramas de hidrogénio com 32 de oxigénio dão 36 gramas "
                   "de água, nem mais nem menos. 2 moléculas de hidrogénio "
                   "e 1 de oxigénio dão 2 moléculas de água.",
        "lembra": "Na natureza nada se perde, nada se cria: tudo se "
                  "transforma.",
    },
    "qui-8c:u3:n5": {
        "explica": "Uma mole é um número fixo de partículas, o número de "
                   "Avogadro. A massa molar é a massa de uma mole, em "
                   "gramas: é a massa molecular em gramas. Com ela "
                   "passa-se de gramas a moles e de moles a gramas.",
        "exemplo": "Água: 18 gramas por mole, logo 2 moles são 36 gramas. "
                   "Dióxido de carbono: 44 por mole, logo 88 gramas são 2 "
                   "moles. O metano tem 12 de carbono em 16: 75 por cento.",
        "lembra": "Massa é moles vezes massa molar.",
    },
    "qui-8c:u4:n1": {
        "explica": "A água potável é própria para beber: sem cor, sem "
                   "cheiro, sem micróbios. A salobra tem sais a mais; a "
                   "mineral brota de nascentes, fria ou termal. A água "
                   "contaminada traz cólera e febre tifóide; trata-se por "
                   "fervura, cloro e filtração.",
        "exemplo": "Ferver a água mata os micróbios; umas gotas de cloro "
                   "também. Fechar a torneira ao lavar os dentes e reparar "
                   "as fugas conserva a água.",
        "lembra": "Água que se bebe: fervida ou clorada.",
    },
    "qui-8c:u4:n2": {
        "explica": "Uma solução é o soluto dissolvido no solvente. Diluir "
                   "é juntar solvente; uma solução saturada já não "
                   "dissolve mais. A concentração percentual é os gramas "
                   "de soluto em 100 de solução; a molar é as moles de "
                   "soluto por litro.",
        "exemplo": "20 gramas de sal em 80 de água são 100 gramas de "
                   "solução: 20 por cento. 3 moles num litro: 3 moles por "
                   "litro.",
        "lembra": "Percentual em 100 gramas; molar por litro.",
    },
    "qui-8c:u4:n3": {
        "explica": "O hidrogénio, descoberto por Cavendish, é o gás mais "
                   "leve e arde no oxigénio a dar água. O oxigénio, "
                   "descoberto por Priestley, obtém-se no laboratório do "
                   "peróxido de hidrogénio com um catalisador, que acelera "
                   "a reacção sem se gastar.",
        "exemplo": "O oxigénio enche as balas dos hospitais e alimenta o "
                   "fogo; o hidrogénio é combustível de foguetões. O "
                   "fermento do pão é um catalisador da cozinha.",
        "lembra": "Catalisador: muda a rapidez, não se gasta.",
    },
    "qui-8c:u4:n4": {
        "explica": "O ar é sobretudo azoto e oxigénio, e a camada de ozono "
                   "trava os raios ultravioleta. Ganhar oxigénio é oxidar: "
                   "lenta, como o ferro a enferrujar, ou rápida, a "
                   "combustão, que precisa de combustível, comburente e "
                   "calor.",
        "exemplo": "Pintar o portão tira-lhe o ar e a humidade e evita a "
                   "ferrugem. Reagentes com 80 de energia e produtos com "
                   "30: libertaram-se 50, reacção exotérmica.",
        "lembra": "Combustível, oxigénio e calor: o triângulo do fogo.",
    },

    # ---------------------------------------------------------------
    # Ingles -- 8a classe
    #
    # Como na 7a: a explicacao e em portugues e o ingles vai entre
    # aspas, pouco de cada vez, para a voz portuguesa nao se perder.
    # ---------------------------------------------------------------
    "ing-8c:u1:n1": {
        "explica": "Moçambique está rodeado de países onde se fala inglês: "
                   "«South Africa», «Zimbabwe», «Zambia», «Tanzania», "
                   "«Malawi». Por isso o inglês serve para o comércio, o "
                   "turismo e a escola. As línguas e as nacionalidades "
                   "escrevem-se com letra grande.",
        "exemplo": "«I speak Portuguese and English.» «She is Mozambican.» "
                   "Repara: «Portuguese», «English» e «Mozambican» levam "
                   "maiúscula, ao contrário do português.",
        "lembra": "Línguas e nacionalidades, em inglês, com letra grande.",
    },
    "ing-8c:u1:n2": {
        "explica": "No presente simples, com «he», «she» e «it» o verbo "
                   "ganha «s»: «she works». No passado simples os verbos "
                   "regulares ganham «ed»: «we visited». «And», «but», "
                   "«because» e «or» ligam frases; «can» diz o que se sabe "
                   "fazer.",
        "exemplo": "«She works in a hotel.» «We visited Tanzania last "
                   "year.» «I can swim, but I can't drive.» «Always», "
                   "«sometimes» e «never» dizem quantas vezes.",
        "lembra": "Terceira pessoa no presente leva «s»; passado regular "
                  "leva «ed».",
    },
    "ing-8c:u2:n1": {
        "explica": "A saúde tem o «doctor», o «healer» e a «herbal "
                   "medicine». Para o futuro há «going to», quando já se "
                   "decidiu, e «will», para o que se prevê ou promete. O "
                   "que está a acontecer agora vai em «ing»: «she is "
                   "taking».",
        "exemplo": "«I am going to the hospital tomorrow.» «The doctor will "
                   "help you.» «She is taking the medicine now.»",
        "lembra": "«Going to» é plano; «will» é previsão ou promessa.",
    },
    "ing-8c:u2:n2": {
        "explica": "A condição de sempre usa o presente nas duas partes: "
                   "«if you have a fever, go to the hospital». A condição "
                   "provável usa «will» na segunda: «if it rains, we will "
                   "stay». «Few» e «many» são para contáveis; «should» dá "
                   "conselho.",
        "exemplo": "«If it rains, we will stay at home.» «There are few "
                   "doctors in the village.» «You should go to the doctor.» "
                   "Automedicação é «self-medication», e faz mal.",
        "lembra": "Depois de «if» não se usa «will».",
    },
    "ing-8c:u3:n1": {
        "explica": "As cerimónias da comunidade têm nome em inglês: "
                   "«wedding», «funeral», «birth», «initiation rites». Para "
                   "contar como uma decorre usam-se os marcadores de "
                   "sequência: «first», «then», «after that», «finally».",
        "exemplo": "«First, the family meets; then, the elders speak; "
                   "finally, everybody dances.» Um costume é «custom»; um "
                   "cliente é «customer».",
        "lembra": "«First», «then», «finally»: o princípio, o meio e o fim.",
    },
    "ing-8c:u3:n2": {
        "explica": "«Must» é obrigação forte e «mustn't» é proibição; "
                   "«should» é o que é boa ideia. Nunca levam «to» a seguir. "
                   "Com os mais velhos fala-se formal — «good morning, sir» "
                   "— e com os amigos informal — «hi».",
        "exemplo": "«We must respect the elders.» «You mustn't miss "
                   "classes.» «Boys and girls should share the tasks.» "
                   "«Thank you very much» é formal; «thanks» é entre "
                   "amigos.",
        "lembra": "«Must», «mustn't» e «should» nunca levam «to».",
    },
    "ing-8c:u4:n1": {
        "explica": "No campo há a «hoe», o «plough», a «harvest» e os "
                   "desastres: «drought», «flood», «cyclone». «A» e «an» "
                   "são os artigos indefinidos — «an» antes de vogal. A água "
                   "não se conta, por isso pergunta-se «how much water».",
        "exemplo": "«Maize is an important crop.» «How much water do the "
                   "plants need?» Criar animais é «animal husbandry».",
        "lembra": "«How much» para o que não se conta; «how many» para o "
                  "que se conta.",
    },
    "ing-8c:u4:n2": {
        "explica": "O passado contínuo diz o que estava a acontecer: «were "
                   "planting». O present perfect diz o que já está feito: "
                   "«have harvested». A passiva põe a coisa à frente: «the "
                   "fish is dried». As perguntas de lugar começam por "
                   "«where».",
        "exemplo": "«The farmers were planting when the rain started.» "
                   "«We have harvested the maize.» «The fish is dried in "
                   "the sun.» «Where do they keep the seeds?»",
        "lembra": "Present perfect é «have» ou «has» mais o particípio.",
    },
    "ing-8c:u5:n1": {
        "explica": "Nas compras pergunta-se o preço com «how much is», a "
                   "quantidade com «how many», e compara-se com «more "
                   "expensive than» nos adjectivos longos. A pergunta no "
                   "fim da frase, «isn't it», pede que o outro concorde.",
        "exemplo": "«How much is this shirt?» «How many oranges do you "
                   "want?» «This dress is more expensive than that one, "
                   "isn't it?» Regatear é «bargaining»; desconto é "
                   "«discount».",
        "lembra": "Adjectivo longo compara-se com «more ... than».",
    },
    "ing-8c:u6:n1": {
        "explica": "Moçambique tem o «elephant», o «lion», o «hippo» e a "
                   "«turtle», e parques como o Gorongosa. "
                   "O superlativo dos adjectivos longos faz-se com «the "
                   "most»; o caçador furtivo é «poacher» e as espécies em "
                   "perigo, «endangered species».",
        "exemplo": "«Gorongosa is the most famous park in Mozambique.» "
                   "«Poachers kill elephants for ivory.» «The turtle is an "
                   "endangered species.»",
        "lembra": "Superlativo longo: «the most» antes do adjectivo.",
    },
    "ing-8c:u6:n2": {
        "explica": "«Have to» é obrigação que vem de fora; «may not» é "
                   "não ter licença. Os reflexivos — «myself», «herself», "
                   "«themselves» — dizem que a acção volta para quem a faz. "
                   "«Have you ever» pergunta se alguma vez aconteceu.",
        "exemplo": "«Tourists have to protect nature.» «You may not feed "
                   "the animals.» «She enjoyed herself at the beach.» «Have "
                   "you ever visited Mozambique Island?»",
        "lembra": "«She» dá «herself»; «he» dá «himself».",
    },
    "ing-8c:u7:n1": {
        "explica": "Do ambiente: «erosion», «pollution», «deforestation», "
                   "«recycle». «That» e «which» ligam uma frase a uma "
                   "coisa; «who» a uma pessoa. A segunda condicional "
                   "imagina: «if I were president, I would protect the "
                   "forests».",
        "exemplo": "«The trees that we planted are growing.» «If I were "
                   "president, I would protect the forests.» «Don't throw "
                   "rubbish in the river.»",
        "lembra": "Segunda condicional: «if» com passado, e «would» na "
                  "outra parte.",
    },
    "ing-8c:u8:n1": {
        "explica": "As doenças: «malaria», «cholera», «anaemia», "
                   "«kwashiorkor»; os sintomas: «fever», «headache». Os "
                   "nutrientes: «proteins», «carbohydrates», «vitamins». "
                   "Alguns plurais são irregulares: «child» dá «children», "
                   "«foot» dá «feet».",
        "exemplo": "«One child, three children.» «You should take the test "
                   "at the hospital.» «I prefer fruit to sweets.»",
        "lembra": "«Prefer» pede «to», não «than».",
    },
    "ing-8c:u9:n1": {
        "explica": "As profissões: «nurse», «engineer», «driver», "
                   "«teacher». Diz-se o que se quer ser com «I want to be "
                   "a», e porquê com «because». A pergunta no fim "
                   "confirma: «she is a nurse, isn't she?». Para pedir que "
                   "repitam: «can you repeat, please?».",
        "exemplo": "«I want to be a doctor because I like helping people.» "
                   "«If you study, you will be an engineer.» Emprego é "
                   "«job».",
        "lembra": "«Want» leva «to»: «I want to be».",
    },

    # ---------------------------------------------------------------
    # Frances -- 8a classe  (o primeiro Frances da app)
    #
    # Como no Ingles: a explicacao e em portugues e o frances vai entre
    # aspas, pouco de cada vez.
    # ---------------------------------------------------------------
    "fra-8c:u1:n1": {
        "explica": "Em francês cumprimenta-se com «bonjour» de dia e "
                   "«bonsoir» à noite; «salut» é entre amigos. Para se "
                   "apresentar diz-se «je m'appelle» e o nome. Aos "
                   "professores e aos desconhecidos trata-se por «vous»; "
                   "aos amigos por «tu».",
        "exemplo": "«Bonjour! Je m'appelle Amina. Merci, au revoir.» "
                   "«Dix» é 10, «vingt» é 20, «cent» é 100. «Lundi» é "
                   "segunda-feira e «dimanche» é domingo.",
        "lembra": "«Tu» para os amigos, «vous» para o resto.",
    },
    "fra-8c:u1:n2": {
        "explica": "«Être» é ser: «je suis», «tu es», «il est». «Avoir» é "
                   "ter, e a idade diz-se com ele: «j'ai quatorze ans». Os "
                   "verbos em «er» — «habiter», «parler», «étudier» — "
                   "conjugam-se todos da mesma maneira: «nous habitons», "
                   "«elle parle».",
        "exemplo": "«Je suis mozambicain.» «Tu as quatorze ans.» «Nous "
                   "habitons à Lichinga.» «Elle parle portugais.» A "
                   "estudante é «étudiante», com «e» no fim.",
        "lembra": "A idade em francês tem-se: «j'ai» tantos «ans».",
    },
    "fra-8c:u1:n3": {
        "explica": "Para apresentar alguém usa-se «c'est» e o nome, e "
                   "«il est» ou «elle est» e a profissão, sem artigo. A "
                   "pergunta faz-se com «quel» ou «quelle», e a negação "
                   "com «ne ... pas» à volta do verbo. «Aller», «venir» e "
                   "«faire» são irregulares.",
        "exemplo": "«C'est mon ami Paulo.» «Elle est professeure.» «Quelle "
                   "est ta nationalité?» «Il n'est pas français.» «Je vais "
                   "à l'école, tu viens de Maputo.»",
        "lembra": "«C'est» com nome; «il est» com profissão.",
    },
    "fra-8c:u1:n4": {
        "explica": "Descreve-se alguém pelo corpo — «les yeux», «les "
                   "cheveux», «la bouche» — pela roupa e pelas cores. "
                   "Os gostos dizem-se com «aimer», «adorer», «préférer», "
                   "«détester», e compara-se com «plus», «aussi» ou «moins» "
                   "... «que».",
        "exemplo": "«J'adore la musique, mais je déteste les "
                   "mathématiques.» «Paulo est plus grand que João.» «Cette "
                   "chemise est jolie.» «Gentil» é o contrário de "
                   "«méchant».",
        "lembra": "«Plus ... que» é mais; «moins ... que» é menos.",
    },
    "fra-8c:u2:n1": {
        "explica": "Pergunta-se onde alguém está com «où», e responde-se "
                   "com as preposições de lugar: «à côté de», «devant», "
                   "«derrière», «entre», «à gauche de», «à droite de». "
                   "Sentado é «assis», de pé é «debout».",
        "exemplo": "«Où est Maria?» «Pedro est assis à gauche de la "
                   "fenêtre.» «Elle est debout près de la porte.» O "
                   "quadro é «le tableau» e a mochila é «le sac à dos».",
        "lembra": "«Où» pergunta onde; «assis» e «debout» dizem como.",
    },
    "fra-8c:u2:n2": {
        "explica": "As ordens dão-se no imperativo, sem o pronome: "
                   "«ouvrez», «écoute». A pergunta educada começa por "
                   "«est-ce que». A negação é «ne ... pas» à volta do verbo. "
                   "Os comportamentos têm adjectivo: «bruyant», "
                   "«paresseux», «solidaire».",
        "exemplo": "«Ouvrez le livre!» «Écoute le professeur!» «Est-ce que "
                   "je peux sortir, s'il vous plaît?» «Je ne comprends "
                   "pas.»",
        "lembra": "Imperativo é o verbo sem «tu» nem «vous» à frente.",
    },
    "fra-8c:u2:n3": {
        "explica": "«Quelle heure est-il?» pergunta as horas: «il est huit "
                   "heures et demie». Os verbos pronominais levam «me», "
                   "«te», «se»: «je me lève». O que decorre "
                   "diz-se com «être en train de», e o dia "
                   "conta-se com «d'abord», «ensuite», «enfin».",
        "exemplo": "«Je me lève à six heures.» «Elle est en train "
                   "d'étudier.» «D'abord je me lave, ensuite je mange, "
                   "enfin je pars.» «Le matin», «l'après-midi», «le soir».",
        "lembra": "«Et demie» é e meia; «et quart» é e um quarto.",
    },
    "fra-8c:u2:n4": {
        "explica": "Os meses — «janvier», «juin», «décembre» — "
                   "escrevem-se com minúscula. Pergunta-se quando com "
                   "«quand», e um período vai «de ... à». O superlativo é "
                   "«le plus» ou «le moins» e o adjectivo. Símbolos "
                   "nacionais: «le drapeau», «l'hymne».",
        "exemplo": "«Quand commencent les vacances?» «Les cours vont de "
                   "février à novembre.» «Le 25 juin est le jour le plus "
                   "important du Mozambique.»",
        "lembra": "Superlativo: «le plus» ou «le moins» e o adjectivo.",
    },
    "fra-8c:u2:n5": {
        "explica": "O que há na sala diz-se com «il y a», e o que não há "
                   "com «il n'y a pas de». Pergunta-se o que há com "
                   "«qu'est-ce qu'il y a». As preposições: «sur», «sous», "
                   "«dans», «par terre». A uma pergunta negativa "
                   "responde-se que sim com «si».",
        "exemplo": "«Il y a un tableau dans la salle.» «Il n'y a pas "
                   "d'ordinateur.» «Qu'est-ce qu'il y a sur la table?» "
                   "«Tu n'as pas de stylo?» «Si, j'ai un stylo.»",
        "lembra": "Depois de «il n'y a pas» vem «de», não «un».",
    },
    "fra-8c:u2:n6": {
        "explica": "Os objectos da escola: «le cahier», «le stylo», «la "
                   "règle», «la gomme». Os possessivos concordam com o "
                   "objecto: «mon cahier», «ma règle», «son sac». O "
                   "adjectivo concorda com o nome: «grand» e «vert» com "
                   "«sac», que é masculino.",
        "exemplo": "«Mon cahier et mon stylo.» «Son sac à dos est grand et "
                   "vert.» Cuidar das carteiras e dos livros é preservar o "
                   "património escolar.",
        "lembra": "«Mon», «ma», «mes» concordam com a coisa, não com quem "
                  "a tem.",
    },

    # ---------------------------------------------------------------
    # Educacao Visual -- 8a classe
    # ---------------------------------------------------------------
    "ev-8c:u1:n1": {
        "explica": "A arte universal é pintura, escultura e arquitectura. "
                   "Leonardo da Vinci pintou a Mona Lisa; Miguel Ângelo "
                   "esculpiu o David e pintou a Capela Sistina; Picasso "
                   "inventou o cubismo. Uma obra lê-se pelo tipo, pela "
                   "técnica e pelo tema.",
        "exemplo": "Diante de um quadro pergunta-se: é pintura? Foi feito "
                   "a óleo sobre tela? De que fala — uma pessoa, uma "
                   "paisagem, uma guerra? São os três elementos da "
                   "leitura.",
        "lembra": "Tipo, técnica e tema: as três perguntas a uma obra.",
    },
    "ev-8c:u2:n1": {
        "explica": "Os códigos visuais comunicam sem palavras. O indício é "
                   "um sinal natural de que algo aconteceu: fumo, pegadas. "
                   "O pictograma é um desenho simples feito de propósito "
                   "para toda a gente entender: o boneco na porta da casa "
                   "de banho.",
        "exemplo": "No aeroporto, quem não lê português percebe o "
                   "pictograma da mala e da seta. Um bom pictograma é "
                   "simples e sem pormenores a mais.",
        "lembra": "Indício acontece; pictograma desenha-se.",
    },
    "ev-8c:u2:n2": {
        "explica": "Um cartaz lê-se de longe e num relance: pouca letra, "
                   "grande, e uma imagem forte. Faz-se em etapas — tema e "
                   "mensagem, esboço, cartaz final. A banda desenhada conta "
                   "com vinhetas, balões de fala e onomatopeias.",
        "exemplo": "Um cartaz sobre os direitos das crianças: uma imagem, "
                   "uma frase, cores fortes. Na banda desenhada, o «pum» "
                   "escrito é a onomatopeia. Com o x-acto, corta-se para "
                   "fora do corpo.",
        "lembra": "Cartaz: ver de longe, perceber num relance.",
    },
    "ev-8c:u3:n1": {
        "explica": "Forma-função: a forma de um objecto depende do que ele "
                   "serve. As formas são naturais, artificiais ou mistas. "
                   "A malha, ou rede, deixa ampliar ou reduzir um desenho "
                   "sem o deformar. Ponto, linha e plano são os elementos "
                   "básicos.",
        "exemplo": "Copiar um desenho de quadrados de 1 centímetro para "
                   "quadrados de 3 amplia-o 3 vezes. Um copo tem a forma "
                   "que tem porque serve para beber.",
        "lembra": "A malha amplia e reduz sem deformar.",
    },
    "ev-8c:u3:n2": {
        "explica": "As cores primárias são o amarelo, o azul e o vermelho. "
                   "Duas primárias dão uma "
                   "secundária — verde, laranja, roxo — e uma primária com "
                   "a secundária vizinha dá uma terciária. A cor comunica: "
                   "o vermelho do trânsito manda parar.",
        "exemplo": "Amarelo com azul dá verde; amarelo com vermelho dá "
                   "laranja; azul com vermelho dá roxo. Com lápis de cor, "
                   "pinta-se uma por cima da outra.",
        "lembra": "Três primárias, três secundárias, e as terciárias entre "
                  "elas.",
    },
    "ev-8c:u3:n3": {
        "explica": "A textura é o aspecto da superfície: lisa, rugosa, "
                   "áspera, macia. É natural, como a casca da árvore, ou "
                   "artificial, como um tecido. No desenho imita-se com "
                   "pontos, traços e riscos repetidos, ou obtém-se por "
                   "decalque.",
        "exemplo": "Pôr o papel sobre uma moeda e esfregar com o lápis faz "
                   "aparecer a textura: é o decalque. O vidro é liso, a "
                   "lixa é áspera, o algodão é macio.",
        "lembra": "Textura é o que a superfície faz sentir ao tocar.",
    },
    "ev-8c:u4:n1": {
        "explica": "A espiral de dois centros desenha-se com "
                   "semicircunferências alternadas a partir de dois pontos, "
                   "e o raio cresce a cada meia volta. A oval tem dois "
                   "eixos de simetria; o óvulo, como o ovo, tem um só. "
                   "Tudo com compasso.",
        "exemplo": "Centros a 1 centímetro e primeiro raio 1: os raios "
                   "seguintes são 2, 3, 4. A concha do caracol é uma "
                   "espiral da natureza.",
        "lembra": "Dois centros, meias voltas, raio a crescer.",
    },
    "ev-8c:u4:n2": {
        "explica": "O arco romano é meia circunferência com o centro no "
                   "meio da abertura. A ogiva acaba em bico; o árabe fecha "
                   "em ferradura; o abatido é mais baixo que meia "
                   "circunferência; o contracurvado junta curvas para os "
                   "dois lados.",
        "exemplo": "Um arco romano com 60 centímetros de abertura tem 30 "
                   "de raio. Nas portas antigas da ilha de Moçambique "
                   "vêem-se arcos: o desenho geométrico está nas ruas.",
        "lembra": "Arco romano: raio é metade da abertura.",
    },
    "ev-8c:u5:n1": {
        "explica": "As projecções ortogonais mostram todas as faces de um "
                   "objecto numa só folha. O plano horizontal dá a vista de "
                   "cima, o frontal a de frente, o de perfil a de lado. As "
                   "linhas de projecção são perpendiculares ao plano.",
        "exemplo": "Um cilindro em pé visto de cima é um círculo; visto de "
                   "frente é um rectângulo. A mesma coisa, duas vistas.",
        "lembra": "De cima, de frente, de lado: três vistas.",
    },
    "ev-8c:u5:n2": {
        "explica": "Os sólidos projectam-se vista a vista: a pirâmide "
                   "quadrangular é um quadrado com as diagonais de cima e "
                   "um triângulo de frente. Com duas vistas dadas, a "
                   "terceira acha-se com o cubo envolvente e o rebatimento "
                   "dos planos.",
        "exemplo": "O cone em pé, de cima, é um círculo com um ponto no "
                   "meio. Um molde de costura e a planta de uma casa são "
                   "projecções que se usam no trabalho.",
        "lembra": "Cubo envolvente: a caixa onde o sólido cabe.",
    },
    "ev-8c:u6:n1": {
        "explica": "A axonometria desenha o objecto a três dimensões numa "
                   "folha. Na isométrica os três eixos fazem 120 graus "
                   "entre si; na dimétrica dois têm a mesma escala; na "
                   "cavaleira a face da frente fica em verdadeira grandeza "
                   "e o eixo que foge reduz-se.",
        "exemplo": "Um cubo em isometria vê-se como um hexágono com três "
                   "losangos iguais. Na cavaleira, a profundidade "
                   "desenha-se em geral a metade.",
        "lembra": "Isométrica: 120 graus, tudo à mesma escala.",
    },
    "ev-8c:u7:n1": {
        "explica": "Cotar é escrever no desenho as medidas reais do "
                   "objecto. O esboço cotado é à mão levantada; o desenho "
                   "cotado é a rigor. Com as cotas, quem constrói sabe as "
                   "medidas certas e transporta-as das projecções para a "
                   "axonometria.",
        "exemplo": "Uma carteira com 120 centímetros de comprimento e 60 "
                   "de largura: as cotas escrevem-se ao lado das linhas de "
                   "cota, com setas nas pontas.",
        "lembra": "Sem cotas não se constrói; com cotas não há dúvidas.",
    },

    # ---------------------------------------------------------------
    # Educacao Fisica -- 8a classe
    # ---------------------------------------------------------------
    "edf-8c:u1:n1": {
        "explica": "Os jogos da comunidade ensinam a jogar em grupo e a "
                   "respeitar regras. Quem conhece o jogo explica-o de "
                   "forma clara antes de começar. Há jogos para pensar na "
                   "poupança, no ambiente, na higiene, e todos jogam "
                   "juntos, rapazes e raparigas.",
        "exemplo": "Antes do jogo confere-se o campo: pedras e buracos "
                   "tiram-se. Perder também se aprende: é a tolerância.",
        "lembra": "Regras claras, campo seguro, todos a jogar.",
    },
    "edf-8c:u1:n2": {
        "explica": "As danças tradicionais guardam a cultura de cada zona: "
                   "o nhau no Niassa e em Tete, o mapiko em Cabo Delgado, o "
                   "xigubo no sul. Aprendem-se os passos básicos e montam-se "
                   "numa coreografia, ao ritmo do tambor.",
        "exemplo": "Uma coreografia simples: quatro passos para a direita, "
                   "quatro para a esquerda, uma volta, tudo ao compasso do "
                   "batuque.",
        "lembra": "Coreografia é a dança montada passo a passo.",
    },
    "edf-8c:u2:n1": {
        "explica": "A ginástica geral treina as capacidades motoras: força, "
                   "flexibilidade, equilíbrio, ritmo, coordenação. No salto "
                   "à corda, a corda mede-se até às axilas e os movimentos "
                   "aprendem-se primeiro parado. Com turmas grandes "
                   "trabalha-se em circuito.",
        "exemplo": "Estação um: saltos à corda; estação dois: equilíbrios; "
                   "estação três: saltos no solo. Os grupos rodam e todos "
                   "fazem tudo.",
        "lembra": "A corda certa chega às axilas.",
    },
    "edf-8c:u2:n2": {
        "explica": "Na ginástica artística de solo há posições de "
                   "equilíbrio — o avião, a ponte, a espargata — que se "
                   "aguentam alguns segundos, e saltos, voltas e afundos. "
                   "Faz-se sempre aquecimento antes e um colega ajuda a "
                   "segurar.",
        "exemplo": "No avião, um pé no chão, o tronco à frente e os braços "
                   "abertos: três segundos parado. A pares, um faz e o "
                   "outro segura, e depois trocam.",
        "lembra": "Aquecer primeiro; a pares, um faz e o outro segura.",
    },
    "edf-8c:u3:n1": {
        "explica": "A corrida de resistência vai até dez minutos, em grupo, "
                   "ao ritmo do mais lento, alternando com caminhada se for "
                   "preciso. Nas estafetas o testemunho passa-se por baixo, "
                   "dentro da zona marcada e sem parar de correr.",
        "exemplo": "Quatro corredores de 100 metros fazem 400. A "
                   "transmissão aprende-se a andar, depois em corrida lenta, "
                   "depois a correr.",
        "lembra": "Testemunho por baixo, na zona, a correr.",
    },
    "edf-8c:u3:n2": {
        "explica": "O salto em comprimento tem quatro fases: corrida de "
                   "balanço, chamada, voo e queda. Na técnica engrupada, "
                   "durante o voo encolhem-se os joelhos ao peito. "
                   "Aprende-se primeiro sem corrida, e a caixa de areia "
                   "tem de estar limpa.",
        "exemplo": "Correr, bater com um pé na tábua, encolher os joelhos "
                   "no ar, cair com os pés à frente na areia: é o salto "
                   "todo.",
        "lembra": "Balanço, chamada, voo, queda.",
    },
    "edf-8c:u4:n1": {
        "explica": "No basquetebol avança-se a driblar: a bola bate no "
                   "chão. Os passes são de peito, picado e de ombro. Com a "
                   "bola na mão, na tripla ameaça, pode-se passar, driblar "
                   "ou lançar. No lançamento na passada dão-se dois apoios "
                   "e salta-se.",
        "exemplo": "Adversário perto: drible de protecção, com o corpo "
                   "entre ele e a bola. Campo aberto: drible de progressão, "
                   "a correr.",
        "lembra": "Passar, driblar ou lançar: a tripla ameaça.",
    },
    "edf-8c:u4:n2": {
        "explica": "Quem tem a bola ataca: mantém a posse, leva a bola ao "
                   "cesto e lança. Quem não a tem defende: recupera a bola "
                   "e protege o cesto. Na posição defensiva os joelhos "
                   "flectem e os braços abrem, entre o adversário e o "
                   "cesto.",
        "exemplo": "Defender quem tem a bola é pressão; defender quem não "
                   "a tem é sobremarcação e ajuda. Nos jogos reduzidos há "
                   "pelo menos três por equipa.",
        "lembra": "Com bola ataca-se; sem bola defende-se.",
    },
    "edf-8c:u5:n1": {
        "explica": "No futebol, desmarcar-se é sair de perto do adversário "
                   "para receber a bola, e ocupar o espaço é a equipa "
                   "espalhar-se em vez de correr toda atrás dela. A finta "
                   "engana o adversário; proteger a bola é pôr o corpo "
                   "entre ela e ele.",
        "exemplo": "Onze por equipa no jogo formal, com o guarda-redes. "
                   "Quando o capitão decide, a equipa respeita e joga em "
                   "conjunto.",
        "lembra": "Desmarcar, ocupar o espaço, proteger a bola.",
    },

    # ---------------------------------------------------------------
    # Agropecuaria -- 8a classe
    # ---------------------------------------------------------------
    "agr-8c:u1:n1": {
        "explica": "As hortícolas — alface, alho, cebola, cenoura, pepino, "
                   "pimento, tomate, couve, repolho — dão vitaminas à mesa "
                   "e renda no mercado. Quase todas se semeiam no alfobre "
                   "e transplantam-se, e a época fresca e seca, com rega, é "
                   "a melhor.",
        "exemplo": "Da cenoura come-se a raiz, da alface as folhas, do "
                   "tomate o fruto, da cebola o bolbo. O alfobre é o "
                   "canteiro onde as plantinhas nascem protegidas.",
        "lembra": "Alfobre primeiro, campo depois.",
    },
    "agr-8c:u1:n2": {
        "explica": "As práticas culturais são os cuidados depois de "
                   "plantar: sacha para tirar ervas, desbaste para arrancar "
                   "plantas a mais, adubação, rega, tutoragem para segurar "
                   "o tomateiro. O compasso é a distância entre plantas e "
                   "entre linhas.",
        "exemplo": "Doze linhas de 5 tomateiros são 60 plantas. A couve e "
                   "a alface colhem-se de manhã cedo, antes do calor, para "
                   "não murcharem.",
        "lembra": "Sacha, desbaste, adubação, rega, tutor.",
    },
    "agr-8c:u2:n1": {
        "explica": "As leguminosas de grão — nhemba, vulgar, bóer, "
                   "feijão-verde, amendoim — são ricas em proteínas e fazem "
                   "bem ao solo, porque fixam o azoto do ar nas raízes. "
                   "Semeiam-se com a chuva e colhem-se no tempo seco.",
        "exemplo": "O nhemba aguenta a seca; o bóer é um arbusto que dura "
                   "anos; o amendoim cria a vagem debaixo da terra.",
        "lembra": "Leguminosa: proteína na mesa, azoto na terra.",
    },
    "agr-8c:u2:n2": {
        "explica": "O feijão semeia-se com dois grãos por cova e "
                   "dá-se bem com o milho na mesma machamba: é a "
                   "consociação. Colhe-se com as vagens secas e amarelas e "
                   "guarda-se bem seco, em recipiente limpo e fechado, "
                   "contra o gorgulho.",
        "exemplo": "Quarenta covas com dois grãos são 80 grãos. O amendoim "
                   "colhe-se arrancando a planta inteira e pondo as vagens "
                   "a secar.",
        "lembra": "Seco e fechado, o feijão dura o ano.",
    },
    "agr-8c:u3:n1": {
        "explica": "A mandioca e a batata-doce são raízes; a batata-reno e "
                   "o inhame são tubérculos. Dão energia, hidratos de "
                   "carbono. A mandioca aguenta a seca e os solos pobres e "
                   "propaga-se por estacas; a batata-reno propaga-se por "
                   "tubérculos com olhos.",
        "exemplo": "Um pedaço de caule de mandioca espetado na terra dá "
                   "uma planta nova. A batata-doce planta-se por ramas.",
        "lembra": "Mandioca por estaca, batata-reno por tubérculo.",
    },
    "agr-8c:u3:n2": {
        "explica": "A amontoa chega terra ao pé da planta para os "
                   "tubérculos não ficarem à vista. A mandioca leva cerca "
                   "de um ano a colher, e a amarga descasca-se, demolha-se "
                   "ou seca-se antes de comer. A batata-doce guarda-se em "
                   "lugar fresco, seco e arejado.",
        "exemplo": "Estacas a 1 metro numa linha de 25 metros: 26 estacas, "
                   "contando as duas pontas.",
        "lembra": "Mandioca amarga: nunca crua.",
    },
    "agr-8c:u4:n1": {
        "explica": "Os cereais — milho, arroz, trigo, mapira, mexoeira — "
                   "são a base da alimentação. O milho quer chuva regular e "
                   "dá a xima; o arroz quer baixas alagadas; a mapira e a "
                   "mexoeira dão colheita com pouca chuva. O solo "
                   "prepara-se antes de semear.",
        "exemplo": "Numa zona seca do Niassa, a mexoeira dá onde o milho "
                   "falha. Lavrar solta a terra, tira as ervas e deixa a "
                   "raiz respirar.",
        "lembra": "Milho com chuva, mapira e mexoeira sem ela.",
    },
    "agr-8c:u4:n2": {
        "explica": "O milho semeia-se em linhas afastadas 80 centímetros e "
                   "amontoa-se para segurar a planta. A lagarta do funil "
                   "ataca-o, os pássaros comem a mapira, o "
                   "gorgulho ataca o grão guardado. Colhe-se seco e "
                   "guarda-se num celeiro limpo e fechado.",
        "exemplo": "Dezasseis metros de largura a 80 centímetros por linha "
                   "dão 20 linhas. Grão húmido no celeiro é grão perdido.",
        "lembra": "Colher seco, guardar fechado.",
    },
    "agr-8c:u5:n1": {
        "explica": "Os coelhos reproduzem-se depressa e dão carne com "
                   "pouco espaço. Criam-se de forma familiar ou "
                   "industrial, numa coelheira em terreno seco, à sombra e "
                   "sem vento, com comedouro, bebedouro e ninho. Comem "
                   "pastos, forragens e ração.",
        "exemplo": "Uma coelheira de família: quatro fêmeas e um macho em "
                   "gaiolas com ninho, e capim fresco todos os dias.",
        "lembra": "Seco, à sombra, com água e capim.",
    },
    "agr-8c:u5:n2": {
        "explica": "A coccidiose dá diarreia, a sarna dá crostas, a coriza "
                   "dá espirros; previnem-se com limpeza e desinfecção "
                   "diárias. A fêmea aceita o macho no cio, a gestação "
                   "dura cerca de 31 dias, e as crias nascem sem pêlo e de "
                   "olhos fechados.",
        "exemplo": "Coberta a 1 de Março, a coelha pare por volta de 1 de "
                   "Abril. O ninho tem de estar quente e limpo para as "
                   "crias.",
        "lembra": "Um mês de gestação; ninho quente para as crias.",
    },
    "agr-8c:u6:n1": {
        "explica": "Os porcos criam-se numa pocilga com chão que se lave, "
                   "sombra, comedouro e bebedouro. Comem restos da "
                   "machamba e da cozinha, pastos e ração. A peste suína "
                   "africana não tem cura: porcos novos em quarentena e "
                   "nunca restos de carne de porco.",
        "exemplo": "Uma porca com 8 leitões por ninhada e duas ninhadas "
                   "por ano dá 16 leitões. A sarna dá comichão; o mal-rubro "
                   "dá manchas vermelhas e febre.",
        "lembra": "Peste suína: quarentena, e nunca carne de porco na "
                  "comida.",
    },

    # ---------------------------------------------------------------
    # TIC -- 8a classe
    # ---------------------------------------------------------------
    "tic-8c:u1:n1": {
        "explica": "Sem software o hardware não faz nada. O operacional, "
                   "como o Windows, arranca o computador e gere "
                   "tudo; o básico, como os controladores, faz os aparelhos "
                   "funcionar; o de protecção é o antivírus; o de gestão "
                   "organiza contas e alunos.",
        "exemplo": "A escola usa o sistema operativo para ligar o "
                   "computador, o controlador para a impressora imprimir, "
                   "o antivírus para se proteger e um programa de gestão "
                   "para as pautas.",
        "lembra": "Operacional, básico, de protecção, de gestão.",
    },
    "tic-8c:u1:n2": {
        "explica": "Um programa é obra de alguém e tem direitos de autor. "
                   "O software livre pode usar-se, estudar-se, alterar-se e "
                   "partilhar-se; o proprietário só como o dono autoriza; o "
                   "comercial paga-se. Copiar um programa pago sem licença "
                   "é pirataria.",
        "exemplo": "Um programa pode ser grátis e proprietário ao mesmo "
                   "tempo: não se paga, mas não se pode alterar nem "
                   "redistribuir. A licença é o acordo que diz o que se "
                   "pode.",
        "lembra": "Grátis não é o mesmo que livre.",
    },
    "tic-8c:u1:n3": {
        "explica": "Uma aplicação descarrega-se da loja ou do sítio "
                   "oficial. Um vírus é um programa malicioso que se copia "
                   "e estraga ou rouba dados; o antivírus instala-se, "
                   "configura-se e actualiza-se. Actualizar fecha falhas de "
                   "segurança.",
        "exemplo": "Uma lanterna que pede acesso aos contactos, à câmara e "
                   "às mensagens é suspeita: não se instala.",
        "lembra": "Só da loja oficial, e sempre actualizado.",
    },
    "tic-8c:u2:n1": {
        "explica": "Uma rede são dois ou mais computadores ligados para "
                   "trocar dados. A Internet nasceu da ARPANET. As "
                   "topologias são a estrela, o anel e o barramento; as "
                   "ligações são com fios, por cabo, ou sem fios, por "
                   "Wi-Fi.",
        "exemplo": "Na escola, os computadores ligam-se todos ao router, "
                   "em estrela, e o router liga a escola à Internet.",
        "lembra": "Estrela, anel, barramento: as três topologias.",
    },
    "tic-8c:u2:n2": {
        "explica": "A rede dá serviços: a web, o e-mail, a transferência "
                   "de ficheiros. No e-mail, o que vem depois da arroba é o "
                   "fornecedor. No computador da escola termina-se a "
                   "sessão no fim, e nunca se dá a palavra-passe a quem a "
                   "pede por e-mail.",
        "exemplo": "Para enviar o trabalho a três colegas, põem-se os três "
                   "endereços separados por vírgulas. Um e-mail do «banco» "
                   "a pedir o código é burla.",
        "lembra": "Sessão terminada, palavra-passe guardada.",
    },
    "tic-8c:u2:n3": {
        "explica": "A nuvem são servidores na Internet onde se guardam "
                   "ficheiros, acessíveis de qualquer aparelho. Faz-se "
                   "upload para lá pôr, download para trazer, e partilha-se "
                   "só com quem precisa. Precisa de Internet, e em Lichinga "
                   "os dados pagam-se.",
        "exemplo": "Se o telemóvel se perde, as fotografias que estavam na "
                   "nuvem continuam lá. Partilhar um trabalho é dar acesso "
                   "ao professor, não ao mundo inteiro.",
        "lembra": "Upload sobe, download desce.",
    },
    "tic-8c:u2:n4": {
        "explica": "O ciberespaço é o espaço das redes; a cibercultura são "
                   "os hábitos de quem lá vive. Ciber-higiene são os bons "
                   "hábitos: palavras-passe compridas, com letras, números "
                   "e sinais, diferentes em cada conta. Entrar na conta de "
                   "outro é crime.",
        "exemplo": "Uma palavra-passe com pelo menos oito caracteres: se "
                   "tem cinco, faltam três. O nome ou «um, dois, três, "
                   "quatro» não servem.",
        "lembra": "Comprida, misturada, e uma para cada conta.",
    },
    "tic-8c:u3:n1": {
        "explica": "Uma transacção electrónica é um pagamento ou "
                   "transferência por meios digitais: carteira móvel, caixa "
                   "automática, cartão. O código secreto nunca se diz a "
                   "ninguém, nem a quem diz ser do banco, e na caixa "
                   "leva-se o cartão e confere-se o talão.",
        "exemplo": "Uma mãe recebe 500 meticais na carteira móvel e paga "
                   "120 de electricidade: ficam-lhe 380, sem sair de casa.",
        "lembra": "O código secreto é só teu.",
    },
    "tic-8c:u3:n2": {
        "explica": "A Lei número 3 de 2017 dá valor legal aos documentos "
                   "e assinaturas electrónicos. O comércio electrónico é "
                   "comprar e vender pela Internet: só em lojas conhecidas "
                   "e sítios seguros, e nunca com pagamento adiantado para "
                   "receber prémios.",
        "exemplo": "Comprar pela Internet chega a produtos que não há na "
                   "vila. Uma mensagem a pedir dinheiro para receber um "
                   "prémio é burla.",
        "lembra": "Loja conhecida, sítio seguro, sem adiantamentos.",
    },
    "tic-8c:u3:n3": {
        "explica": "As TIC servem a agricultura, a saúde e o ambiente. A "
                   "e-Agricultura informa o camponês da chuva e dos "
                   "preços; a e-Saúde guarda o registo do doente e marca "
                   "consultas; os satélites vigiam queimadas e o aviso de "
                   "ciclone chega por mensagem.",
        "exemplo": "Um camponês do Niassa que vê o preço do feijão em "
                   "Maputo antes de vender, vende melhor.",
        "lembra": "Informação a tempo é dinheiro e é vida.",
    },

    # ---------------------------------------------------------------
    # Matematica -- 9a classe
    # ---------------------------------------------------------------
    "mat-9c:u1:n1": {
        "explica": "A reunião A ∪ B junta os dois conjuntos; a "
                   "intersecção A ∩ B fica só com os comuns; a diferença "
                   "A menos B tira a A o que está em B; o complementar de "
                   "A é o que está no universo e não em A. Sem elementos "
                   "comuns, são disjuntos.",
        "exemplo": "A = {1, 2, 3} e B = {3, 4}: A ∪ B tem 4 elementos, A ∩ "
                   "B tem 1, A menos B tem 2. Os naturais são um conjunto "
                   "infinito: nunca acabam.",
        "lembra": "Reunião junta, intersecção cruza, diferença tira.",
    },
    "mat-9c:u1:n2": {
        "explica": "Os racionais escrevem-se como fracção e a dízima é "
                   "finita ou periódica. Os irracionais, como √2 e π, têm "
                   "dízima infinita não periódica. Juntos formam os reais, "
                   "que enchem a recta: ℕ está dentro de ℤ, ℤ dentro de "
                   "ℚ, ℚ dentro de ℝ.",
        "exemplo": "7 é natural, −3 é inteiro, 1/2 é racional, √2 é "
                   "irracional. √50 está entre 7 e 8, porque 49 é menor "
                   "que 50 e 64 é maior.",
        "lembra": "Racional tem fracção; irracional não tem.",
    },
    "mat-9c:u1:n3": {
        "explica": "A raiz cúbica é o contrário do cubo: ∛27 é 3 porque 3 "
                   "ao cubo é 27, e ∛(−8) é −2. Uma potência de expoente "
                   "fraccionário é uma raiz: 8 elevado a um terço é ∛8. "
                   "Um factor sai do radical quando é um quadrado.",
        "exemplo": "Um cubo com 125 de volume tem aresta ∛125, que é 5. "
                   "√12 é √(4 × 3), e como 4 é 2 ao quadrado, sai: 2√3.",
        "lembra": "Expoente um terço é raiz cúbica.",
    },
    "mat-9c:u1:n4": {
        "explica": "Radicais semelhantes somam-se: 2√3 mais 5√3 dá 7√3. "
                   "Multiplicam-se e dividem-se por dentro: √4 × √9 é √36. "
                   "O quadrado de uma raiz quadrada é o radicando. "
                   "Racionalizar é tirar a raiz do denominador, "
                   "multiplicando em cima e em baixo.",
        "exemplo": "√50 a dividir por √2 é √25, que é 5. (√7)² é 7. 1 sobre "
                   "√2 vira √2 sobre 2.",
        "lembra": "Só se somam radicais com o mesmo radicando.",
    },
    "mat-9c:u2:n1": {
        "explica": "Uma inequação resolve-se como uma equação, com uma "
                   "excepção: ao multiplicar ou dividir por um "
                   "negativo, o sinal da desigualdade inverte-se. A solução "
                   "é um intervalo, e na recta marca-se bola aberta para < "
                   "e > e bola fechada para ≤ e ≥.",
        "exemplo": "2x + 1 < 9 dá x < 4: o maior natural é 3. 3x − 5 > 7 "
                   "dá x > 4: o menor natural é 5. x − 2 ≥ 1 é [3, +∞[.",
        "lembra": "Negativo a multiplicar vira o sinal.",
    },
    "mat-9c:u2:n2": {
        "explica": "Num sistema de inequações, as duas condições têm de "
                   "valer ao mesmo tempo: a solução é a intersecção das "
                   "duas. Se não há parte comum, o sistema é impossível. "
                   "Muitos problemas da vida têm duas condições e dão um "
                   "sistema.",
        "exemplo": "x > 1 e x < 5 dá ]1, 5[: os inteiros são 2, 3 e 4. x > "
                   "3 e x < 1 não tem solução. Um quarto com perímetro "
                   "menor que 22 e comprimento igual à largura mais 1: a "
                   "largura vai até 4.",
        "lembra": "Sistema é intersecção: o que serve às duas.",
    },
    "mat-9c:u3:n1": {
        "explica": "Numa proporção, os produtos cruzados são iguais. Uma "
                   "homotetia amplia ou reduz uma figura por uma razão: os "
                   "comprimentos multiplicam-se pela razão, os ângulos "
                   "ficam iguais, e a área multiplica-se pela razão ao "
                   "quadrado.",
        "exemplo": "3 está para 4 como 9 está para 12. Razão 3: um segmento "
                   "de 4 passa a 12, e um quadrado de lado 2 passa a lado "
                   "6, com área 36. Razão entre 0 e 1 reduz.",
        "lembra": "A área cresce com o quadrado da razão.",
    },
    "mat-9c:u3:n2": {
        "explica": "Dois triângulos são semelhantes quando têm os ângulos "
                   "iguais e os lados proporcionais. Basta um critério: "
                   "lado-lado-lado, ângulo-ângulo, ou lado-ângulo-lado. Os "
                   "perímetros estão na razão; as áreas, na razão ao "
                   "quadrado.",
        "exemplo": "Razão 2: um lado de 5 passa a 10. Razão 3: perímetro "
                   "10 passa a 30. Razão 2: área 6 passa a 24, porque 2 ao "
                   "quadrado é 4.",
        "lembra": "Dois ângulos iguais chegam para a semelhança.",
    },
    "mat-9c:u3:n3": {
        "explica": "Thales: rectas paralelas cortadas por duas secantes "
                   "determinam segmentos proporcionais: é por isso que a "
                   "sombra do poste dá a altura da árvore. "
                   "Pitágoras: no triângulo rectângulo, a hipotenusa ao "
                   "quadrado é a soma dos quadrados dos catetos.",
        "exemplo": "Poste de 2 com sombra 3, árvore com sombra 12: a "
                   "árvore tem 8. Catetos 6 e 8: hipotenusa 10. Hipotenusa "
                   "13 e cateto 5: o outro é 12.",
        "lembra": "Hipotenusa ao quadrado é cateto mais cateto, ao "
                  "quadrado.",
    },
    "mat-9c:u4:n1": {
        "explica": "Um polinómio é uma soma de monómios; o grau é o "
                   "maior expoente. Somam-se juntando os semelhantes; um "
                   "monómio multiplica um polinómio distribuindo; dois "
                   "binómios multiplicam-se termo a termo. O valor "
                   "numérico sai substituindo o x.",
        "exemplo": "(3x + 2) + (2x − 5) é 5x − 3. 2x × (x + 3) é 2x² + 6x. "
                   "(x + 2) × (x + 3) é x² + 5x + 6. Para x = 2, x² + 3x − "
                   "1 dá 9.",
        "lembra": "Cada termo de um multiplica cada termo do outro.",
    },
    "mat-9c:u4:n2": {
        "explica": "Os produtos notáveis poupam contas: (a + b)² é a² + "
                   "2ab + b², (a − b)² é a² − 2ab + b², e (a + b)(a − b) é "
                   "a² − b². Factorizar é o caminho ao contrário: pôr o "
                   "factor comum em evidência ou reconhecer um caso "
                   "notável.",
        "exemplo": "(x + 3)² é x² + 6x + 9. (x − 2)² é x² − 4x + 4. (x + "
                   "5)(x − 5) é x² − 25. 3x² + 6x é 3x(x + 2). x² − 9 é (x + "
                   "3)(x − 3).",
        "lembra": "Soma vezes diferença é diferença de quadrados.",
    },
    "mat-9c:u4:n3": {
        "explica": "Uma equação quadrática tem x ao quadrado. Sem o "
                   "termo em x, isola-se o quadrado e tira-se a raiz: duas "
                   "soluções simétricas, ou nenhuma se der negativo. "
                   "Sem termo independente, põe-se x em evidência e "
                   "usa-se a lei do anulamento do produto.",
        "exemplo": "x² − 16 = 0 dá x = 4 ou x = −4. x² − 5x = 0 é x(x − 5) "
                   "= 0, logo x = 0 ou x = 5. x² + 4 = 0 não tem solução "
                   "real. x² = 0 só tem o zero.",
        "lembra": "Produto zero: um dos factores é zero.",
    },
    "mat-9c:u4:n4": {
        "explica": "Na equação completa ax² + bx + c = 0, o discriminante "
                   "b² − 4ac diz quantas raízes há: duas se é positivo, uma "
                   "se é zero, nenhuma se é negativo. A fórmula resolvente "
                   "dá-as, e a soma das raízes é −b sobre a; o produto, c "
                   "sobre a.",
        "exemplo": "x² − 5x + 6 = 0: discriminante 25 − 24 = 1, raízes 2 e "
                   "3. Um quadrado cuja área mais o triplo do lado dá 28 "
                   "tem lado 4, porque 16 + 12 é 28.",
        "lembra": "Discriminante negativo: sem raízes reais.",
    },
    "mat-9c:u5:n1": {
        "explica": "A função quadrática y = ax² tem por gráfico uma "
                   "parábola com o vértice na origem e o eixo das "
                   "ordenadas como eixo de simetria. Se a é positivo, a "
                   "concavidade é para cima; se é negativo, para baixo.",
        "exemplo": "f(x) = 2x²: f(3) é 2 × 9, que é 18. y = −x² é a "
                   "parábola de y = x² virada para baixo.",
        "lembra": "a positivo sorri; a negativo faz beicinho.",
    },
    "mat-9c:u5:n2": {
        "explica": "Somar c a ax² sobe ou desce a parábola; escrever a(x − "
                   "h)² + k põe o vértice em (h, k). Os zeros são onde a "
                   "parábola corta o eixo das abcissas, e o vértice é o "
                   "mínimo se a concavidade é para cima, ou o máximo se é "
                   "para baixo.",
        "exemplo": "y = x² − 9 tem zeros em −3 e 3. y = x² + 2 é y = x² "
                   "subida 2. y = (x − 4)² + 1 tem vértice (4, 1). y = x² − "
                   "4x tem zeros em 0 e 4.",
        "lembra": "Em a(x − h)² + k, o vértice é (h, k).",
    },
    "mat-9c:u6:n1": {
        "explica": "Uma inequação quadrática resolve-se achando as raízes "
                   "da equação e vendo depois o sinal entre elas e fora "
                   "delas, numa tabela de sinais ou no esboço da parábola: "
                   "abaixo do eixo o valor é negativo, acima é positivo.",
        "exemplo": "x² − 4 < 0 é ]−2, 2[: entre as raízes a parábola está "
                   "em baixo. x² − 4 > 0 é fora: x < −2 ou x > 2. x² − 9 ≤ "
                   "0 tem 7 inteiros, de −3 a 3.",
        "lembra": "Raízes primeiro, sinal depois.",
    },
    "mat-9c:u7:n1": {
        "explica": "A população é o todo; a amostra é a parte que "
                   "se observa. A frequência absoluta conta; a relativa "
                   "divide pelo total, e em percentagem multiplica por 100; "
                   "a acumulada soma até à classe. No gráfico circular, 100 "
                   "por cento são 360 graus.",
        "exemplo": "10 em 40 alunos são 25 por cento. Frequências 5, 8 e 7: "
                   "a acumulada até à segunda é 13. Uma fatia de 25 por "
                   "cento tem 90 graus.",
        "lembra": "Relativa é a parte sobre o todo.",
    },
    "mat-9c:u7:n2": {
        "explica": "A média é a soma a dividir pelo número de dados. A moda "
                   "é o valor mais frequente. A mediana é o valor do meio "
                   "depois de ordenar: com um número par de dados, é a "
                   "média dos dois do meio.",
        "exemplo": "Média de 12, 14 e 16: 14. Moda de 3, 5, 5, 7, 9: 5. "
                   "Mediana de 2, 4, 5, 7, 9: 5. Mediana de 2, 4, 6, 8: "
                   "entre 4 e 6, que é 5.",
        "lembra": "Mediana: ordenar primeiro, meio depois.",
    },
    "mat-9c:u8:n1": {
        "explica": "Um poliedro é um sólido de faces planas, e a relação de "
                   "Euler diz que vértices menos arestas mais faces dá 2. O "
                   "prisma tem duas bases iguais e paralelas, e o volume é "
                   "a área da base vezes a altura.",
        "exemplo": "Cubo: 8 vértices, 6 faces, logo 12 arestas. Prisma de "
                   "base 3 por 4 e altura 5: volume 60. Cubo de aresta 3: "
                   "6 faces de 9, área total 54.",
        "lembra": "Vértices menos arestas mais faces é 2.",
    },
    "mat-9c:u8:n2": {
        "explica": "A pirâmide tem uma base e faces triangulares que se "
                   "juntam no vértice. O volume é um terço da área da base "
                   "vezes a altura: uma pirâmide com a mesma base e altura "
                   "que um prisma tem um terço do volume dele.",
        "exemplo": "Base quadrada de lado 6 e altura 5: 36 × 5 a dividir "
                   "por 3 dá 60. Prisma de volume 90: a pirâmide igual tem "
                   "30. A pirâmide quadrangular tem 5 faces.",
        "lembra": "Pirâmide é um terço do prisma.",
    },
    "mat-9c:u8:n3": {
        "explica": "Cilindro, cone e esfera nascem de rodar um rectângulo, "
                   "um triângulo rectângulo e um semicírculo. Volume do "
                   "cilindro: π r² h; do cone: um terço disso; da esfera: "
                   "quatro terços de π r³. A área lateral do cilindro é "
                   "2π r h.",
        "exemplo": "Com π igual a 3: cilindro de raio 2 e altura 5 dá 60; "
                   "cone de raio 3 e altura 4 dá 36; esfera de raio 3 dá "
                   "108; a área lateral de um cilindro de raio 1 e altura "
                   "10 dá 60.",
        "lembra": "Cone é um terço do cilindro com a mesma base e altura.",
    },

    # ---------------------------------------------------------------
    # Portugues -- 9a classe
    # ---------------------------------------------------------------
    "por-9c:u1:n1": {
        "explica": "A Declaração dos Direitos Humanos é um "
                   "texto normativo: diz, em linguagem clara, os direitos "
                   "de todas as pessoas, sem distinção. Há direitos "
                   "pessoais, como a liberdade; judiciários, como o "
                   "julgamento justo; sociais, como a educação.",
        "exemplo": "«Todos os seres humanos nascem livres e iguais em "
                   "dignidade e em direitos» é o primeiro artigo. Não "
                   "conta uma história nem vende nada: manda e garante.",
        "lembra": "Normativo: diz o que se deve e o que se pode.",
    },
    "por-9c:u1:n2": {
        "explica": "Fazer, dar e poder são verbos irregulares: mudam o "
                   "radical ao conjugar. Fiz, fizeste, fez; dei, deste, "
                   "deu; pude, pudeste, pôde. No futuro: farei, darei, "
                   "poderei. No conjuntivo: faça, dê, possa; se fizer, se "
                   "der, se puder.",
        "exemplo": "«Ontem fiz os trabalhos.» «Amanhã eles darão sangue.» "
                   "«Se tu puderes, vem.» «Nós fizemos tudo o que "
                   "podíamos.»",
        "lembra": "Fiz, dei, pude: o pretérito muda o radical.",
    },
    "por-9c:u1:n3": {
        "explica": "A vírgula separa enumerações e orações; os dois pontos "
                   "anunciam uma explicação ou uma fala; o ponto e vírgula "
                   "separa partes longas; o travessão abre a fala. "
                   "Sinónimos dizem o mesmo por outra palavra; antónimos "
                   "dizem o contrário.",
        "exemplo": "«Todos têm direitos: à vida, à liberdade e à "
                   "educação.» Liberdade e autonomia são sinónimos; justo e "
                   "injusto, igualdade e desigualdade, são antónimos.",
        "lembra": "Dois pontos anunciam; a vírgula separa.",
    },
    "por-9c:u1:n4": {
        "explica": "A Declaração dos Direitos da Criança garante a quem "
                   "tem menos de dezoito anos escola, saúde, protecção e "
                   "brincadeira, e proíbe o trabalho infantil. Os "
                   "adjectivos biformes têm duas formas, alto e alta; os "
                   "uniformes uma só, feliz.",
        "exemplo": "Português dá portuguesa, europeu dá europeia, "
                   "espanhol dá espanhola, comilão dá comilona. «Sem pés "
                   "nem cabeça» e «às direitas» são locuções adjectivas.",
        "lembra": "Biforme muda com o género; uniforme não.",
    },
    "por-9c:u2:n1": {
        "explica": "A carta de apresentação é um texto administrativo: "
                   "apresenta-se a uma empresa ou instituição e pede uma "
                   "oportunidade. Tem local e data, destinatário, corpo — "
                   "quem sou, o que sei, o que peço — despedida e "
                   "assinatura, em linguagem formal.",
        "exemplo": "«Excelentíssimo Senhor Director» para quem não se "
                   "conhece; «Com os melhores cumprimentos» a fechar. Os "
                   "impostos que se pagam são as escolas e os hospitais que "
                   "se têm.",
        "lembra": "Formal: tratamento certo, sem calão.",
    },
    "por-9c:u2:n2": {
        "explica": "O Curriculum Vitae resume a vida escolar e "
                   "profissional: dados pessoais, formação, experiência, "
                   "por ordem e sem enfeites. As palavras compostas "
                   "formam-se por "
                   "justaposição, sem perder letras, ou por aglutinação, "
                   "fundindo-se.",
        "exemplo": "Guarda-chuva e couve-flor são justaposição; aguardente "
                   "(água ardente) e fidalgo (filho de algo) são "
                   "aglutinação. Desporto no Curriculum também conta.",
        "lembra": "Justaposição junta; aglutinação funde.",
    },
    "por-9c:u2:n3": {
        "explica": "O requerimento pede algo por escrito a uma entidade: "
                   "destinatário, identificação de quem pede, o pedido e "
                   "os seus motivos, «pede deferimento», local, data e "
                   "assinatura. O verbo concorda com o sujeito em pessoa e "
                   "número.",
        "exemplo": "Um camponês pede ao Administrador do Distrito a "
                   "concessão de um terreno. «Os alunos pedem», «eu e tu "
                   "vamos»: o verbo segue o sujeito.",
        "lembra": "Sujeito no plural, verbo no plural.",
    },
    "por-9c:u3:n1": {
        "explica": "A entrevista faz-se com um guião de perguntas e "
                   "escreve-se em discurso directo, com travessão, ou "
                   "indirecto, com «que» e o verbo a recuar no tempo. A "
                   "conjugação perifrástica junta um auxiliar ao "
                   "infinitivo: estar a, começar a, acabar de.",
        "exemplo": "«A enfermeira disse: — Eu durmo com rede» vira «a "
                   "enfermeira disse que dormia com rede». «Está a "
                   "explicar» decorre; «começou a» inicia; «acabou de» "
                   "terminou.",
        "lembra": "Indirecto: «que», e o verbo recua.",
    },
    "por-9c:u3:n2": {
        "explica": "O texto publicitário tem parte verbal, o slogan e o "
                   "texto, e parte não verbal, a imagem e as cores. As "
                   "preposições até, com, contra, desde, entre e sem ligam "
                   "palavras. Acentuam-se os monossílabos tónicos, os "
                   "hiatos e o «têm» do plural.",
        "exemplo": "«Sabão Sol: brilho que dura!» é um slogan. «Vou até "
                   "Lichinga», «trabalha desde a manhã», «ficou sem casa». "
                   "Saúde leva acento no hiato; eles têm, ele tem.",
        "lembra": "Ele tem, eles têm: o acento marca o plural.",
    },
    "por-9c:u3:n3": {
        "explica": "As orações subordinadas dependem de outra. A "
                   "interrogativa indirecta faz a pergunta por dentro: "
                   "«pergunto se vens». A concessiva admite um obstáculo: "
                   "«embora chovesse». A consecutiva diz a consequência: "
                   "«tão alto que todos ouviram».",
        "exemplo": "Embora e apesar de abrem concessivas; de modo que e "
                   "tanto que abrem consecutivas; se e quando, numa "
                   "pergunta indirecta, abrem interrogativas.",
        "lembra": "Embora concede; tanto que resulta.",
    },
    "por-9c:u4:n1": {
        "explica": "O guia turístico dá a conhecer os lugares de uma "
                   "região em linguagem informativa e atraente: onde ficam, "
                   "o que têm, como se chega. A oração subordinada "
                   "integrante completa um verbo como saber, dizer ou "
                   "pensar: «sabemos que o lago é lindo».",
        "exemplo": "O Niassa tem o lago, com praias e pesca; a Reserva do "
                   "Niassa, com elefantes; o monte Massangulo. «Dizem que "
                   "a água é morna»: «que a água é morna» é integrante.",
        "lembra": "Integrante: completa o que se sabe, se diz, se pensa.",
    },
    "por-9c:u4:n2": {
        "explica": "O relato de viagem conta uma viagem, real ou "
                   "imaginada, por ordem, com o que se viu e se sentiu. Os "
                   "pronomes relativos — que, quem, onde, o qual — ligam "
                   "uma oração relativa ao nome que ela explica.",
        "exemplo": "«O guia que nos levou era de Lichinga.» «A aldeia "
                   "onde nasci fica perto do lago.» «A senhora com quem "
                   "falámos vendia peixe.» Guardar as danças e as línguas "
                   "é preservar o património.",
        "lembra": "Relativo aponta para trás: para o nome que explica.",
    },
    "por-9c:u5:n1": {
        "explica": "O romance é a narrativa longa: mais personagens, mais "
                   "acções, mais tempo que o conto ou a novela. Na narração "
                   "a acção avança; na descrição pára para mostrar. O "
                   "atributo qualifica por ser ou estar; o aposto "
                   "explica um nome ao lado dele.",
        "exemplo": "«Meledina, a rapariga da Zambézia, chegou»: «a "
                   "rapariga da Zambézia» é aposto. «A cidade era enorme»: "
                   "«enorme» é atributo. Aldino Muianga e Germano Almeida "
                   "lêem-se nesta classe.",
        "lembra": "Aposto explica; atributo qualifica.",
    },
    "por-9c:u5:n2": {
        "explica": "O poema faz-se de versos, em estrofes, muitas vezes "
                   "com rima. Os recursos estilísticos dão-lhe força: a "
                   "hipérbole exagera, a anáfora repete no início dos "
                   "versos, a ironia diz o contrário. Os advérbios "
                   "afirmam, intensificam ou excluem.",
        "exemplo": "Noémia de Sousa, «Se me queres conhecer»; Craveirinha, "
                   "«Um homem nunca chora»; Camões, «Amor é fogo que arde "
                   "sem se ver». «Certamente» afirma, «muito» intensifica, "
                   "«só» exclui.",
        "lembra": "Verso, estrofe, rima: a forma do poema.",
    },
    "por-9c:u5:n3": {
        "explica": "O texto dramático escreve-se para ser representado: "
                   "falas das personagens e didascálias, as indicações "
                   "sobre gestos e cenário. A tragédia acaba mal. As "
                   "interjeições — ai, oh — exprimem emoção; as falas "
                   "passam de directo a indirecto.",
        "exemplo": "«Ai! Que dor!» tem uma interjeição. Uma cena sobre "
                   "uma gravidez precoce mostra o que ela custa: a saúde da "
                   "rapariga e a escola que fica para trás.",
        "lembra": "Didascália: o que se faz, não o que se diz.",
    },

    # ---------------------------------------------------------------
    # Geografia -- 9a classe  (a Geografia de Mocambique)
    # ---------------------------------------------------------------
    "geo-9c:u1:n1": {
        "explica": "Moçambique fica na costa oriental da África Austral, "
                   "com uns 2700 quilómetros de Índico. Faz fronteira com "
                   "seis países: Tanzânia a norte, além do Rovuma; Malawi "
                   "e Zâmbia a noroeste; Zimbabué a oeste; África do Sul e "
                   "Essuatíni a sul.",
        "exemplo": "Do Rovuma ao Maputo são mais de 2000 quilómetros. O "
                   "canal de Moçambique separa-nos de Madagáscar.",
        "lembra": "Seis vizinhos por terra, o Índico por mar.",
    },
    "geo-9c:u1:n2": {
        "explica": "As rochas mais antigas, do Pré-câmbrico, estão no "
                   "interior e no norte; as mais recentes, do Fanerozóico "
                   "— Karroo, Cretácico, Quaternário — nas bacias e no "
                   "litoral. Daí vêm os minerais: energéticos, metálicos e "
                   "não metálicos.",
        "exemplo": "Carvão em Moatize, gás em Pande e Temane, areias "
                   "pesadas em Moma, rubis em Montepuez. Os solos aluviais "
                   "dos grandes rios são os mais férteis.",
        "lembra": "Pré-câmbrico é o velho; Fanerozóico é o novo.",
    },
    "geo-9c:u1:n3": {
        "explica": "O relevo nasce de processos endógenos, de dentro da "
                   "Terra, e exógenos, a erosão da chuva, do vento e dos "
                   "rios. O país sobe do litoral para o interior: "
                   "planícies na costa e no sul, planaltos no centro e no "
                   "norte, montanhas a oeste.",
        "exemplo": "O monte Binga, em Manica, tem 2436 metros e é o mais "
                   "alto do país. Lichinga está no planalto do Niassa, a "
                   "mais de 1300 metros.",
        "lembra": "Planície, planalto, montanha: de leste para oeste.",
    },
    "geo-9c:u1:n4": {
        "explica": "O clima é tropical, com uma estação quente e chuvosa, "
                   "de Outubro a Março, e outra fresca e seca. Varia com a "
                   "latitude, a altitude e a distância ao mar: húmido no "
                   "litoral norte e centro, seco no interior sul, de "
                   "altitude nos planaltos.",
        "exemplo": "Num gráfico termopluviométrico, as barras são a chuva "
                   "de cada mês e a linha é a temperatura. Em Lichinga a "
                   "linha é mais baixa do que em Pemba.",
        "lembra": "Chuva de Outubro a Março; seco de Maio a Setembro.",
    },
    "geo-9c:u1:n5": {
        "explica": "A savana e o miombo cobrem o país; elefantes e leões "
                   "vivem nas áreas protegidas: Gorongosa, Reserva do "
                   "Niassa, Bazaruto. O Zambeze é o maior rio; Rovuma, "
                   "Lúrio, Save e Limpopo fazem as outras bacias. O lago "
                   "Niassa é o terceiro de África.",
        "exemplo": "Cahora Bassa, no Zambeze, dá electricidade ao país e "
                   "aos vizinhos. O lago Niassa é partilhado com o Malawi "
                   "e a Tanzânia.",
        "lembra": "Rovuma e Lúrio a norte, Zambeze ao centro, Limpopo a "
                  "sul.",
    },
    "geo-9c:u2:n1": {
        "explica": "No censo de 2017, Moçambique tinha uns 28 milhões "
                   "de habitantes. A natalidade conta os nascimentos por "
                   "mil habitantes, a mortalidade as mortes, e a "
                   "diferença é o crescimento natural. O "
                   "planeamento familiar deixa escolher quando ter filhos.",
        "exemplo": "40 nascimentos e 12 mortes por mil dão um crescimento "
                   "natural de 28 por mil. Vacinas, água limpa e postos de "
                   "saúde fazem baixar a mortalidade infantil.",
        "lembra": "Crescimento natural: natalidade menos mortalidade.",
    },
    "geo-9c:u2:n2": {
        "explica": "A população muda pelo movimento natural, nascimentos "
                   "e mortes, e pelo migratório, entradas e saídas. Quem "
                   "sai do país emigra; quem entra imigra; quem deixa o "
                   "campo pela cidade faz o êxodo rural. A causa principal "
                   "é a procura de trabalho.",
        "exemplo": "Um jovem do Niassa que vai para as minas da África do "
                   "Sul emigra. Longe da família, cresce o risco de "
                   "infecções como o HIV: é a ligação entre migração e "
                   "saúde.",
        "lembra": "Emigra quem sai; imigra quem entra.",
    },
    "geo-9c:u2:n3": {
        "explica": "A população é jovem: quase metade tem menos de 15 "
                   "anos. Trabalha sobretudo no sector primário e "
                   "concentra-se no litoral e nos vales, onde há água, "
                   "solos e portos: "
                   "Nampula e Zambézia são as mais povoadas, o Niassa o "
                   "menos denso.",
        "exemplo": "Não há trabalhos só de homens nem só de mulheres. A "
                   "violência baseada no género é crime e denuncia-se.",
        "lembra": "Base larga: país jovem.",
    },
    "geo-9c:u3:n1": {
        "explica": "A agricultura de subsistência é a da família, com "
                   "enxada, para comer; a de plantação é de grandes áreas "
                   "para vender, herdada do tempo colonial e do trabalho "
                   "forçado. Depende do clima, do solo, da água, da terra "
                   "e do trabalho.",
        "exemplo": "Caju em Nampula, chá no Gurué, açúcar nos vales do "
                   "Incomáti e do Búzi, milho e feijão nos planaltos. O "
                   "gado bovino cria-se sobretudo no sul.",
        "lembra": "Subsistência alimenta; plantação exporta.",
    },
    "geo-9c:u3:n2": {
        "explica": "A pesca artesanal faz-se de canoa perto da costa e "
                   "nos lagos; a industrial, de barco grande ao largo, "
                   "exporta camarão. A silvicultura cultiva e explora as "
                   "florestas, e conservá-las é evitar queimadas e cortar "
                   "só com licença, replantando.",
        "exemplo": "No lago Niassa pesca-se o chambo e a usipa. O miombo "
                   "do Niassa dá lenha, carvão e madeira, mas só dura se "
                   "não se queimar.",
        "lembra": "Camarão para fora; chambo para a mesa.",
    },
    "geo-9c:u3:n3": {
        "explica": "A indústria extractiva tira minerais da terra: carvão "
                   "em Moatize, gás em Inhambane. A transformadora faz "
                   "produtos: a pesada, como o alumínio da Mozal e o "
                   "cimento; a ligeira, como os refrescos. Está sobretudo "
                   "em Maputo, na Beira e Nampula.",
        "exemplo": "Uma fábrica que despeja resíduos no rio mata os "
                   "peixes: é o impacto ambiental, e a lei obriga a "
                   "tratá-los.",
        "lembra": "Extractiva tira; transformadora faz.",
    },
    "geo-9c:u3:n4": {
        "explica": "Os corredores de Nacala, da Beira e de Maputo ligam os "
                   "portos ao interior, e a Estrada "
                   "Nacional número 1 atravessa o país de sul a norte. O "
                   "comércio interno é formal e informal; o externo "
                   "exporta alumínio, carvão, gás, camarão e caju.",
        "exemplo": "Oferta é o que há para vender; procura é o que se "
                   "quer comprar; inflação é os preços a subir. Cinto "
                   "posto e sem álcool ao volante previnem acidentes.",
        "lembra": "Três corredores, três portos: Nacala, Beira, Maputo.",
    },
    "geo-9c:u3:n5": {
        "explica": "O turismo é de praia, no Bazaruto; de "
                   "natureza, na Gorongosa e no Niassa; cultural, na Ilha "
                   "de Moçambique. Cria empregos e vive da "
                   "identidade cultural. Poupar é guardar, investir é pôr "
                   "a render, crédito é emprestado com juros.",
        "exemplo": "Quem poupa 150 meticais por mês tem 1800 ao fim de um "
                   "ano — o suficiente para começar um pequeno negócio.",
        "lembra": "Poupar primeiro, investir depois, crédito com cuidado.",
    },
    "geo-9c:u4:n1": {
        "explica": "A África Austral é o sul do continente. A SADC, a "
                   "Comunidade de Desenvolvimento da África Austral, "
                   "nasceu em 1992 em Windhoek, da organização de 1980, e "
                   "tem sede em Gaborone. Fala-se português, inglês, "
                   "francês e malgaxe nos seus países.",
        "exemplo": "Moçambique e Angola falam português; a Zâmbia e o "
                   "Zimbabué, inglês; Madagáscar, malgaxe e francês.",
        "lembra": "SADC: 1992, Windhoek, sede em Gaborone.",
    },
    "geo-9c:u4:n2": {
        "explica": "A SADC coopera nos transportes, no comércio e na paz. "
                   "Moçambique é a porta do mar dos países do interior: os "
                   "corredores levam-lhes as mercadorias. A integração pede "
                   "cultura de paz, direitos humanos e democracia, e "
                   "combate a xenofobia.",
        "exemplo": "O Malawi, a Zâmbia e o Zimbabué exportam pelos portos "
                   "da Beira e de Nacala. Numa democracia o povo escolhe "
                   "quem governa, em eleições livres.",
        "lembra": "Integração é ganhar com os vizinhos, não contra eles.",
    },

    # ---------------------------------------------------------------
    # Historia -- 9a classe  (o seculo XX)
    # ---------------------------------------------------------------
    "his-9c:u1:n1": {
        "explica": "No fim do século XIX as potências europeias disputavam "
                   "colónias, mercados e matérias-primas: é o "
                   "imperialismo. Formaram blocos militares e correram "
                   "aos armamentos, até que um atentado acendeu a guerra.",
        "exemplo": "Inglaterra, França e Rússia de um lado; Alemanha, "
                   "Áustria-Hungria e Itália do outro. A 28 de Junho de "
                   "1914, em Sarajevo, mataram o herdeiro austríaco.",
        "lembra": "Dois blocos, uma corrida às armas, um atentado.",
    },
    "his-9c:u1:n2": {
        "explica": "A I Guerra Mundial teve três fases: movimentos, "
                   "trincheiras, movimentos outra vez. Os Estados Unidos "
                   "entraram em 1917; a Rússia saiu nesse ano, com a "
                   "revolução. África deu soldados e carregadores à "
                   "força; Moçambique teve combates no norte.",
        "exemplo": "As tropas alemãs entraram por Cabo Delgado e o Niassa "
                   "vindas da Tanzânia; milhares de moçambicanos foram "
                   "levados como carregadores.",
        "lembra": "Movimentos, trincheiras, movimentos.",
    },
    "his-9c:u1:n3": {
        "explica": "O armistício de 1918 acabou a guerra. "
                   "O Tratado de Versalhes culpou a Alemanha e impôs-lhe "
                   "perdas, e a Sociedade das Nações nasceu "
                   "para resolver conflitos em paz. Milhões de mortos, "
                   "economias destruídas, impérios desfeitos.",
        "exemplo": "As colónias alemãs em África foram repartidas pelos "
                   "vencedores: o Tanganhica passou aos ingleses. Ninguém "
                   "ficou independente.",
        "lembra": "Versalhes humilhou a Alemanha; a Sociedade das Nações "
                  "quis a paz.",
    },
    "his-9c:u1:n4": {
        "explica": "A ocupação efectiva pôs a administração colonial: "
                   "directa, por europeus, ou indirecta, por chefes "
                   "africanos. Em Moçambique, as companhias, o chibalo, o imposto de palhota e as culturas "
                   "obrigatórias exploravam o povo, que resistiu.",
        "exemplo": "A Companhia do Niassa mandou no norte até 1929. "
                   "Ngungunhane resistiu em Gaza em 1895, Makombe no Barué "
                   "em 1917, e Menelik venceu os italianos em Adua.",
        "lembra": "Chibalo é trabalho forçado.",
    },
    "his-9c:u2:n1": {
        "explica": "Em 1917 a Revolução de Outubro fez da Rússia o primeiro "
                   "Estado socialista, a URSS, com a economia nas mãos do "
                   "Estado. Em 1929 a bolsa de Nova Iorque caiu e a crise "
                   "fechou fábricas no mundo inteiro; Roosevelt "
                   "respondeu com o New Deal.",
        "exemplo": "Em Moçambique a crise fez cair os preços do algodão e "
                   "do açúcar, e os camponeses ficaram a ganhar menos pelo "
                   "mesmo trabalho.",
        "lembra": "1917 revolução, 1929 crise.",
    },
    "his-9c:u2:n2": {
        "explica": "Nos anos 30 nasceram ditaduras: o fascismo de "
                   "Mussolini, o nazismo de Hitler, o Estado Novo de "
                   "Salazar. Acabaram com as liberdades; o nazismo pregou "
                   "o ódio racial e o Holocausto. Em Moçambique, o Estado "
                   "Novo apertou o trabalho forçado.",
        "exemplo": "O corporativismo foi o sistema do Estado Novo. Nas "
                   "colónias, mais culturas obrigatórias, mais chibalo e "
                   "censura à imprensa.",
        "lembra": "Fascismo, nazismo, Estado Novo: três ditaduras.",
    },
    "his-9c:u2:n3": {
        "explica": "A II Guerra Mundial começou em 1939 com a invasão da "
                   "Polónia e acabou em 1945. Causas: a humilhação de "
                   "Versalhes, a crise, o expansionismo de Hitler, o "
                   "nazismo. África deu soldados e matérias-primas. No "
                   "fim nasceu a ONU, para manter a paz.",
        "exemplo": "Soldados africanos lutaram nos exércitos coloniais em "
                   "África e na Europa. A bomba atómica em Hiroxima mostrou "
                   "o perigo das armas de destruição maciça.",
        "lembra": "1939 a 1945; no fim, a ONU.",
    },
    "his-9c:u3:n1": {
        "explica": "No Estado Novo, Moçambique era «província ultramarina» "
                   "e o indigenato negava direitos aos moçambicanos. O "
                   "nacionalismo nasceu em greves, associações e jornais, "
                   "e o massacre de Mueda, em 1960, mostrou que a "
                   "independência não viria em paz.",
        "exemplo": "A UDENAMO nasceu na Rodésia, a MANU no Tanganhica, a "
                   "UNAMI no Malawi: três movimentos de emigrantes "
                   "moçambicanos, que se juntariam.",
        "lembra": "Mueda, 16 de Junho de 1960.",
    },
    "his-9c:u3:n2": {
        "explica": "A 25 de Junho de 1962, em Dar es Salaam, os três "
                   "movimentos fundiram-se na FRELIMO, com Eduardo Mondlane "
                   "como presidente. Preparou combatentes em Kongwa e "
                   "Nachingwea e, a 25 de Setembro de 1964, em Chai, "
                   "começou a luta armada.",
        "exemplo": "Samora Machel comandou a luta e foi o primeiro "
                   "Presidente; Josina Machel cuidou dos assuntos sociais; "
                   "Filipe Samuel Magaia foi o primeiro comandante militar.",
        "lembra": "1962 a FRELIMO, 1964 a luta armada.",
    },
    "his-9c:u3:n3": {
        "explica": "Nas zonas libertadas, a "
                   "FRELIMO governava com escolas, postos de saúde, "
                   "produção colectiva e a mulher na luta. A 7 de Setembro "
                   "de 1974 os Acordos de Lusaka reconheceram a "
                   "independência, proclamada a 25 de Junho de 1975.",
        "exemplo": "A Constituição de 1975 fez de Moçambique a República "
                   "Popular de Moçambique, um Estado independente sem a "
                   "discriminação colonial.",
        "lembra": "Lusaka em 1974, Independência em 1975.",
    },
    "his-9c:u4:n1": {
        "explica": "A Guerra Fria opôs os Estados Unidos, com a NATO, à "
                   "URSS, com o Pacto de Varsóvia, sem guerra directa "
                   "entre eles. Os Não-Alinhados recusaram os blocos. O "
                   "apartheid sul-africano desestabilizou Moçambique, e o "
                   "muro de Berlim caiu em 1989.",
        "exemplo": "Moçambique sofreu ataques e sabotagens apoiados pelo "
                   "apartheid, que via no país independente uma ameaça.",
        "lembra": "Guerra Fria: dois blocos, nunca frente a frente.",
    },
    "his-9c:u4:n2": {
        "explica": "Depois da Independência, o Governo da FRELIMO e a "
                   "RENAMO fizeram uma guerra de dezasseis anos. As "
                   "negociações de Roma levaram ao Acordo Geral de Paz, a "
                   "4 de Outubro de 1992. A Constituição de 1990 já tinha "
                   "aberto o multipartidarismo.",
        "exemplo": "As primeiras eleições gerais multipartidárias foram em "
                   "1994: vários partidos, voto secreto, o povo a "
                   "escolher.",
        "lembra": "Roma, 4 de Outubro de 1992: a paz.",
    },
    "his-9c:u4:n3": {
        "explica": "De cinco em cinco anos há eleições gerais, para o "
                   "Presidente e a Assembleia; há também autárquicas, para "
                   "os municípios, e provinciais. O voto é secreto. "
                   "A cultura de paz é resolver os conflitos pelo diálogo, "
                   "na escola como entre países.",
        "exemplo": "Coexistência pacífica é países com sistemas diferentes "
                   "a viver lado a lado sem guerra: foi o que a Guerra Fria "
                   "acabou por aprender.",
        "lembra": "Voto secreto, diálogo primeiro.",
    },

    # ---------------------------------------------------------------
    # Biologia -- 9a classe
    # ---------------------------------------------------------------
    "bio-9c:u1:n1": {
        "explica": "Um ecossistema são os seres vivos de um lugar e o "
                   "ambiente em que vivem. É natural, como o lago ou o "
                   "miombo, ou artificial, como a machamba. Os factores "
                   "bióticos são os seres vivos; os abióticos são a luz, "
                   "a água, a temperatura.",
        "exemplo": "Num aquário, os peixes e as algas são bióticos; a água, "
                   "a luz e a temperatura são abióticos. Se o lago seca, "
                   "mudou um factor abiótico e tudo muda.",
        "lembra": "Biótico vive; abiótico não.",
    },
    "bio-9c:u1:n2": {
        "explica": "Na cadeia alimentar, o produtor faz o alimento com a "
                   "luz do Sol, o consumidor primário come-o, o secundário "
                   "come o primário. Várias cadeias cruzadas são uma teia. "
                   "A energia flui num só sentido e perde-se de nível "
                   "para nível.",
        "exemplo": "Capim, cabra, leão. Se o capim tem 1000 unidades de "
                   "energia, só uns 100 chegam à cabra e uns 10 ao leão: "
                   "por isso comer produtores rende mais.",
        "lembra": "A energia desce a cadeia e não volta.",
    },
    "bio-9c:u1:n3": {
        "explica": "O desmatamento traz "
                   "erosão, a caça furtiva extingue espécies, o lixo polui "
                   "a água. A água potável bebe-se; a poluída tem "
                   "químicos; a contaminada tem micróbios. Os resíduos "
                   "domésticos separam-se e reciclam-se; os hospitalares "
                   "queimam-se.",
        "exemplo": "Papel, plástico e vidro separados em casa voltam a ser "
                   "coisas novas. Seringas e ligaduras vão para a "
                   "incineradora, nunca para o rio.",
        "lembra": "Separar, reciclar, e o hospitalar ao fogo.",
    },
    "bio-9c:u2:n1": {
        "explica": "O esqueleto dá forma e suporte, protege os órgãos e "
                   "permite o movimento. Tem 206 ossos: "
                   "longos como o fémur, curtos como os do pulso, planos "
                   "como a omoplata, irregulares como as vértebras. São "
                   "feitos de osteína, sais de cálcio e água.",
        "exemplo": "A osteína dá flexibilidade e o cálcio dá dureza: os "
                   "ossos das crianças, com mais osteína, partem-se menos; "
                   "os dos idosos, com mais cálcio, partem-se mais.",
        "lembra": "Osteína dobra, cálcio endurece.",
    },
    "bio-9c:u2:n2": {
        "explica": "Os músculos estriados comandam-se, os lisos "
                   "trabalham sozinhos no intestino, o "
                   "cardíaco é o coração. As articulações são móveis, "
                   "semimóveis ou imóveis. Entorse torce, luxação desloca; "
                   "cifose, lordose e escoliose curvam a coluna.",
        "exemplo": "Sentar direito, fazer exercício, comer cálcio e não "
                   "carregar pesos a mais protegem os ossos e os "
                   "músculos.",
        "lembra": "Joelho é móvel, vértebra semimóvel, crânio imóvel.",
    },
    "bio-9c:u2:n3": {
        "explica": "O sistema nervoso central é o cérebro, o cerebelo "
                   "e a medula espinal; o periférico são os nervos e "
                   "os gânglios. Os actos voluntários dependem da vontade; "
                   "os reflexos não: o estímulo vai pelo arco reflexo até "
                   "à medula e volta ao músculo.",
        "exemplo": "Tirar a mão do fogo antes de sentir a dor é um "
                   "reflexo. O cão de Pavlov salivava à campainha: um "
                   "reflexo condicionado, aprendido.",
        "lembra": "Reflexo passa pela medula, não pelo cérebro.",
    },
    "bio-9c:u3:n1": {
        "explica": "O ciclo menstrual dura uns 28 dias e a ovulação, o "
                   "dia mais fértil, é a meio, no dia 14. A "
                   "fecundação junta o espermatozóide ao óvulo na trompa, "
                   "e a gravidez dura 40 semanas. Na adolescência é um "
                   "risco para a mãe e para o bebé.",
        "exemplo": "Uma rapariga de catorze anos grávida deixa a escola, "
                   "e o seu corpo ainda não está pronto: mais partos "
                   "difíceis e mais bebés com pouco peso.",
        "lembra": "Dia 14: o mais fértil.",
    },
    "bio-9c:u3:n2": {
        "explica": "Os métodos naturais — calendário, temperatura — "
                   "falham, porque o ciclo nem sempre é regular. Os "
                   "artificiais — preservativo, pílula, injecção, "
                   "dispositivo intra-uterino — são mais seguros, e só o "
                   "preservativo protege também das infecções.",
        "exemplo": "A pílula toma-se todos os dias; a injecção de três em "
                   "três meses; o dispositivo dura anos. Os adolescentes "
                   "têm direito a informação no centro de saúde.",
        "lembra": "Preservativo: dois em um, gravidez e infecções.",
    },
    "bio-9c:u3:n3": {
        "explica": "As plantas têm hormonas: as auxinas fazem crescer, as "
                   "giberelinas germinar, o etileno amadurece, o ácido "
                   "abscísico faz cair as folhas. Reagem ao ambiente: o "
                   "tropismo segue o estímulo, como o caule para a luz; o "
                   "nastismo não.",
        "exemplo": "Bananas num saco amadurecem depressa porque o etileno "
                   "fica junto delas. Feijões sem luz crescem amarelos, "
                   "fracos e compridos.",
        "lembra": "Fototropismo para a luz, geotropismo para a terra.",
    },
    "bio-9c:u4:n1": {
        "explica": "O solo tem uma parte mineral — areia, argila, limo, "
                   "cascalho — uma parte orgânica, o húmus, e ar e água "
                   "nos espaços. O arenoso deixa passar a água, o argiloso "
                   "encharca, o misto retém o suficiente e é o melhor para "
                   "cultivar.",
        "exemplo": "Água em três frascos com solos diferentes mostra qual "
                   "retém mais. Um solo escuro e fofo, com minhocas, é "
                   "fértil.",
        "lembra": "Misto é o meio-termo, e é o bom.",
    },
    "bio-9c:u4:n2": {
        "explica": "No solo há produtores, as plantas, consumidores, como "
                   "os insectos, e decompositores, as bactérias "
                   "e as minhocas, que fazem o húmus. A irrigação permite "
                   "cultivar na seca. Conserva-se o solo com curvas de "
                   "nível, rotação e cobertura.",
        "exemplo": "As queimadas matam os organismos do solo e "
                   "empobrecem-no. Curvas de nível na encosta travam a "
                   "chuva; palha por cima guarda a humidade.",
        "lembra": "Decompositor faz húmus; queimada mata-o.",
    },
    "bio-9c:u4:n3": {
        "explica": "As culturas alimentares são os cereais, as "
                   "leguminosas, as raízes e tubérculos e as hortícolas. O "
                   "adubo orgânico faz-se de estrume e restos a decompor: "
                   "barato, melhora o solo. O artificial "
                   "usa-se na dose certa, com luvas, longe da água.",
        "exemplo": "Um composto de restos de cozinha e estrume leva uns "
                   "três meses: começado em Março, está pronto em Junho.",
        "lembra": "Orgânico alimenta o solo; artificial só a planta.",
    },
    "bio-9c:u5:n1": {
        "explica": "Preconceito é julgar sem conhecer; discriminação é "
                   "tratar pior; estigma é a marca de vergonha; exclusão é "
                   "deixar de fora. Fazem mal à saúde: quem tem HIV "
                   "esconde-se e não se trata. Inclusão é respeitar as "
                   "diferenças e dar lugar a todos.",
        "exemplo": "Um colega com deficiência na turma tem os mesmos "
                   "direitos, e a turma ganha com a diversidade. "
                   "Discriminar é violar os direitos humanos.",
        "lembra": "Diferente não é menos.",
    },
    "bio-9c:u5:n2": {
        "explica": "As doenças transmissíveis passam "
                   "por vectores: malária pelo mosquito, cólera pela água, "
                   "tuberculose pelo ar, tinha e sarna pelo contacto. As "
                   "não transmissíveis — asma, diabetes, hipertensão, "
                   "obesidade — vêm de factores de risco.",
        "exemplo": "Sal a mais e falta de exercício sobem a tensão; "
                   "refrescos e fritos engordam. Rede mosquiteira e água "
                   "fervida travam a malária e a cólera.",
        "lembra": "Vector transmite; factor de risco predispõe.",
    },
    "bio-9c:u5:n3": {
        "explica": "O cancro do colo do útero é o mais frequente na mulher "
                   "em Moçambique, ligado ao vírus do papiloma humano; há "
                   "também o da mama e o da próstata. Detectam-se cedo com "
                   "exames. Os medicamentos tomam-se com receita, na dose "
                   "e no tempo certos.",
        "exemplo": "Um caroço na mama ou uma hemorragia fora do período "
                   "pedem o centro de saúde sem demora. Comichão e "
                   "inchaço depois de um remédio são alergia: pára-se.",
        "lembra": "Exame cedo salva; remédio só com receita.",
    },

    # ---------------------------------------------------------------
    # Fisica -- 9a classe
    # ---------------------------------------------------------------
    "fis-9c:u1:n1": {
        "explica": "Os espelhos esféricos são côncavos, como o do "
                   "dentista, ou convexos, como o retrovisor. O foco fica "
                   "a meio do raio de curvatura. No côncavo, o raio "
                   "paralelo reflecte-se pelo foco. O convexo dá sempre "
                   "imagem direita e menor.",
        "exemplo": "Raio de curvatura 40 centímetros: foco a 20. Um objecto "
                   "entre o foco e o espelho côncavo dá uma imagem "
                   "direita, maior e virtual: é a lupa do dentista.",
        "lembra": "Foco é metade do raio.",
    },
    "fis-9c:u1:n2": {
        "explica": "A refracção é o desvio da luz ao mudar de meio: do ar "
                   "para a água abranda e aproxima-se da normal. O índice "
                   "de refracção diz quantas vezes a luz é mais lenta "
                   "nesse meio do que no vazio.",
        "exemplo": "O lápis no copo parece partido porque a luz muda de "
                   "direcção ao sair da água. Num vidro de índice 1,5, a "
                   "luz anda a 200 mil quilómetros por segundo em vez de "
                   "300 mil.",
        "lembra": "Muda o meio, muda a direcção.",
    },
    "fis-9c:u1:n3": {
        "explica": "A lente convergente, mais grossa no meio, junta os "
                   "raios no foco; a divergente afasta-os. O olho é uma "
                   "lente convergente: a miopia, que vê mal ao longe, "
                   "corrige-se com divergente; a hipermetropia, com "
                   "convergente.",
        "exemplo": "Uma lupa é convergente: uma imagem 3 vezes maior faz "
                   "de 2 centímetros 6. Ler com luz, não olhar para o Sol "
                   "e lavar as mãos protegem os olhos.",
        "lembra": "Míope: divergente. Hipermétrope: convergente.",
    },
    "fis-9c:u2:n1": {
        "explica": "O centro de gravidade é o ponto onde se considera "
                   "aplicado o peso. O equilíbrio é estável, instável ou "
                   "indiferente. O momento de uma força é força vezes "
                   "braço: quanto maior o braço, mais fácil rodar.",
        "exemplo": "20 newtons a 2 metros do eixo dão 40 newtons-metro. "
                   "Empurra-se a porta longe das dobradiças. Um camião "
                   "carregado no alto vira mais depressa.",
        "lembra": "Momento é força vezes braço.",
    },
    "fis-9c:u2:n2": {
        "explica": "As máquinas simples poupam força: a alavanca, a "
                   "roldana fixa, que só muda a direcção, a móvel, que "
                   "divide a força por dois, o plano inclinado. Mas não "
                   "poupam trabalho: é a regra de ouro da mecânica.",
        "exemplo": "80 newtons a 1 metro do apoio equilibram-se com 20 "
                   "newtons a 4 metros. Com uma roldana móvel, 100 "
                   "newtons levantam-se com 50.",
        "lembra": "Ganha-se em força, perde-se em distância.",
    },
    "fis-9c:u2:n3": {
        "explica": "Densidade é massa a dividir por volume. Pressão é "
                   "força a dividir por área, em pascal: a faca afiada "
                   "corta porque a área é pequena. Num líquido, a pressão "
                   "cresce com a profundidade; a do ar mediu-a Torricelli.",
        "exemplo": "200 gramas em 100 centímetros cúbicos: densidade 2. "
                   "200 newtons em 4 metros quadrados: 50 pascal. A 2 "
                   "metros de água, com gravidade 10: 20 000 pascal.",
        "lembra": "Pressão é força sobre área.",
    },
    "fis-9c:u2:n4": {
        "explica": "Pascal: a pressão num líquido fechado transmite-se "
                   "igual a todos os pontos; é assim que a prensa "
                   "hidráulica multiplica a força. Arquimedes: o corpo "
                   "recebe um empuxo igual ao peso do líquido deslocado, "
                   "e flutua se for menos denso.",
        "exemplo": "Êmbolo grande com 10 vezes a área do pequeno: 50 "
                   "newtons viram 500. Nos vasos comunicantes, a água "
                   "fica à mesma altura. Na praia, nunca nadar sozinho.",
        "lembra": "Flutua o que é menos denso que a água.",
    },
    "fis-9c:u3:n1": {
        "explica": "Os corpos electrizam-se por atrito, contacto ou "
                   "indução: ganham electrões e ficam negativos, ou "
                   "perdem-nos e ficam positivos. Cargas iguais "
                   "repelem-se, contrárias atraem-se. O electroscópio "
                   "detecta a carga.",
        "exemplo": "A régua esfregada no cabelo atrai papelinhos: "
                   "electrizou-se por atrito. As folhas do electroscópio "
                   "abrem-se quando um corpo carregado lhe toca.",
        "lembra": "Iguais repelem, contrárias atraem.",
    },
    "fis-9c:u3:n2": {
        "explica": "A corrente é o movimento de cargas num circuito "
                   "fechado. Mede-se em amperes; a tensão em volts; a "
                   "resistência em ohms. A pilha dá corrente contínua, a "
                   "rede dá alternada. O amperímetro liga-se em série, o "
                   "voltímetro em paralelo.",
        "exemplo": "A rede em Moçambique tem 220 volts: um fio descarnado "
                   "pode matar, nunca se mexe com a corrente ligada.",
        "lembra": "Amperímetro em série, voltímetro em paralelo.",
    },
    "fis-9c:u3:n3": {
        "explica": "Primeira lei de Ohm: a tensão é a resistência vezes a "
                   "intensidade. Segunda lei: a resistência cresce com o "
                   "comprimento do fio e diminui com a sua grossura. No "
                   "gráfico da intensidade pela "
                   "tensão sai uma recta pela origem.",
        "exemplo": "4 ohms a 12 volts: 3 amperes. Uma lâmpada com 2 "
                   "amperes a 220 volts tem 110 ohms.",
        "lembra": "Tensão é resistência vezes intensidade.",
    },
    "fis-9c:u3:n4": {
        "explica": "Em série as resistências somam-se; em paralelo a "
                   "total é menor que a menor. A potência é tensão vezes "
                   "intensidade, em watts; a energia é potência vezes "
                   "tempo. Pela lei de Joule-Lenz, a corrente aquece a "
                   "resistência.",
        "exemplo": "2, 3 e 5 ohms em série dão 10; dois de 6 em paralelo "
                   "dão 3. Um ferro a 220 volts e 2 amperes tem 440 watts. "
                   "100 watts durante 10 horas são 1 quilowatt-hora.",
        "lembra": "Potência é tensão vezes intensidade.",
    },
    "fis-9c:u4:n1": {
        "explica": "Um íman tem pólo norte e pólo sul, e partido dá dois "
                   "ímanes. Pólos iguais repelem-se, contrários atraem-se. "
                   "O campo magnético é a região onde se sentem essas "
                   "forças; a Terra tem o seu, e é por ele que a bússola "
                   "aponta ao norte.",
        "exemplo": "O íman atrai o ferro e o aço, e não a madeira nem o "
                   "plástico. A agulha da bússola é um íman pequeno.",
        "lembra": "Um íman nunca fica só com um pólo.",
    },
    "fis-9c:u4:n2": {
        "explica": "Oersted viu a bússola desviar-se ao pé de um fio com "
                   "corrente: a corrente cria campo magnético. Daí o "
                   "electroíman, um fio enrolado num núcleo de ferro, que "
                   "se liga e desliga com a corrente e fica mais forte com "
                   "mais voltas.",
        "exemplo": "A campainha eléctrica, a grua da sucata e o motor "
                   "eléctrico usam electroímanes. Sem corrente, o "
                   "electroíman larga o ferro.",
        "lembra": "Corrente faz íman.",
    },
    "fis-9c:u5:n1": {
        "explica": "Amplitude é o afastamento máximo da posição de "
                   "equilíbrio, período é o tempo de uma oscilação, "
                   "frequência é quantas faz por segundo, em hertz: 1 "
                   "sobre o período. O período do pêndulo depende do "
                   "comprimento, não da massa.",
        "exemplo": "Meio segundo por oscilação: 2 hertz. A 5 hertz, em 4 "
                   "segundos fazem-se 20 oscilações. No gráfico da "
                   "elongação pelo tempo sai uma onda.",
        "lembra": "Frequência é 1 sobre o período.",
    },
    "fis-9c:u5:n2": {
        "explica": "A onda mecânica é a propagação de uma oscilação num "
                   "meio, sem transportar matéria. O comprimento de onda "
                   "é a distância entre duas cristas, e a velocidade é "
                   "comprimento de onda vezes frequência. O som é uma onda "
                   "mecânica: precisa do ar.",
        "exemplo": "2 metros de comprimento de onda a 5 hertz: 10 metros "
                   "por segundo. Música muito alta durante horas danifica "
                   "o ouvido: baixa-se o volume.",
        "lembra": "Velocidade é comprimento de onda vezes frequência.",
    },

    # ---------------------------------------------------------------
    # Quimica -- 9a classe
    #
    # Sem formulas, como na 8a: "H2SO4" nao se diz.
    # ---------------------------------------------------------------
    "qui-9c:u1:n1": {
        "explica": "Um óxido é o oxigénio junto com outro elemento. Com um "
                   "metal forma um óxido básico, que com a água dá uma "
                   "base; com um não metal forma um óxido ácido, que com a "
                   "água dá um ácido.",
        "exemplo": "A cal viva, óxido de cálcio, com água dá hidróxido de "
                   "cálcio: uma base. O dióxido de carbono com água dá "
                   "ácido carbónico: é por isso que os refrescos com gás "
                   "são ácidos.",
        "lembra": "Metal dá base; não metal dá ácido.",
    },
    "qui-9c:u1:n2": {
        "explica": "Para Arrhenius, um ácido liberta na água iões "
                   "hidrogénio e uma base liberta iões hidroxilo. Os "
                   "ácidos são oxiácidos, com oxigénio, ou hidrácidos, sem "
                   "ele. Ácido com base dá sal e água: é a neutralização.",
        "exemplo": "O ácido clorídrico com o hidróxido de sódio dá cloreto "
                   "de sódio e água. Ácidos e bases fortes queimam: nunca "
                   "se provam nem se tocam sem luvas.",
        "lembra": "Ácido mais base: sal mais água.",
    },
    "qui-9c:u1:n3": {
        "explica": "Um indicador muda de cor conforme o meio é ácido ou "
                   "básico; há naturais, como o sumo de beterraba ou de "
                   "buganvília. Os sais saem da neutralização e têm muitos "
                   "usos: temperar, construir, adubar.",
        "exemplo": "Limão e vinagre são ácidos; água de sabão e de cinza "
                   "são básicas. O sal de cozinha leva iodo por lei, contra "
                   "o bócio; o calcário dá cimento; o nitrato de amónio é "
                   "adubo.",
        "lembra": "O indicador mostra pela cor.",
    },
    "qui-9c:u2:n1": {
        "explica": "O átomo tem no núcleo os protões, positivos, e os "
                   "neutrões, sem carga; à volta, em níveis de energia, os "
                   "electrões, negativos. Número atómico são os protões; "
                   "número de massa, protões mais neutrões. Isótopos têm "
                   "neutrões diferentes.",
        "exemplo": "Número atómico 11 e massa 23: 23 menos 11 dá 12 "
                   "neutrões. O cloro neutro tem 17 protões e 17 "
                   "electrões.",
        "lembra": "Neutrões são massa menos número atómico.",
    },
    "qui-9c:u2:n2": {
        "explica": "A Tabela Periódica, da lei de Mendeleev, ordena os "
                   "elementos pelo número atómico. As linhas são "
                   "períodos, e o período é o número de níveis; as colunas "
                   "são grupos, e o grupo diz os electrões do último "
                   "nível.",
        "exemplo": "O sódio, 2, 8, 1: três níveis, terceiro período, um "
                   "electrão no último nível. Ao descer num grupo o raio "
                   "cresce, porque há mais níveis.",
        "lembra": "Período conta níveis; grupo conta o último.",
    },
    "qui-9c:u3:n1": {
        "explica": "Os átomos ligam-se para ficar com oito electrões no "
                   "último nível: a regra do octeto. Na ligação iónica, um "
                   "dá electrões e o outro recebe, e formam-se iões. Na "
                   "covalente, partilham pares de electrões.",
        "exemplo": "O sódio perde um electrão e fica catião; o cloro "
                   "ganha-o e fica anião: sal. Dissolvido, conduz a "
                   "corrente, porque os iões se movem. A água é covalente.",
        "lembra": "Iónica troca; covalente partilha.",
    },
    "qui-9c:u3:n2": {
        "explica": "Na ligação metálica, os electrões andam livres entre "
                   "os iões do metal: por isso os metais conduzem o calor "
                   "e a corrente. As ligas juntam metais: aço, bronze, "
                   "latão. O ferro obtém-se no alto-forno, reduzindo o "
                   "minério com carvão.",
        "exemplo": "O aço é ferro com carbono; o bronze, cobre com "
                   "estanho; o latão, cobre com zinco. A Mozal, em Maputo, "
                   "produz alumínio para exportar.",
        "lembra": "Electrões livres: bom condutor.",
    },
    "qui-9c:u4:n1": {
        "explica": "Os halogéneos — flúor, cloro, bromo, iodo — têm sete "
                   "electrões no último nível e reagem muito. O cloro "
                   "desinfecta a água, o flúor protege os dentes, o iodo "
                   "entra no sal. O sal vem das salinas.",
        "exemplo": "Umas gotas de lixívia, com cloro, tornam a água de "
                   "beber segura. O estômago faz ácido clorídrico para "
                   "digerir.",
        "lembra": "Sete electrões: sempre à procura de um.",
    },
    "qui-9c:u4:n2": {
        "explica": "Oxidar é perder electrões, e o número de oxidação "
                   "sobe; reduzir é ganhá-los, e desce. O oxidante "
                   "reduz-se e faz o outro oxidar. Uma mole de qualquer "
                   "gás, em condições normais, ocupa 22,4 litros.",
        "exemplo": "No cloreto de sódio, o cloro tem menos 1 e o sódio "
                   "mais 1: a soma dá zero. 44,8 litros de gás são 2 "
                   "moles.",
        "lembra": "Perde oxida, ganha reduz.",
    },
    "qui-9c:u5:n1": {
        "explica": "O enxofre tem variedades alotrópicas, a rômbica e a "
                   "monoclínica. Dele se faz o ácido sulfúrico, pelo "
                   "método de contacto: o ácido mais usado, das baterias "
                   "aos adubos. O sulfureto de hidrogénio cheira a ovo "
                   "podre.",
        "exemplo": "A bateria do carro leva ácido sulfúrico diluído. Um "
                   "cheiro a ovo podre perto de águas paradas é sulfureto "
                   "de hidrogénio.",
        "lembra": "Ácido sulfúrico: o mais usado na indústria.",
    },
    "qui-9c:u5:n2": {
        "explica": "Uma reacção dá-se quando as partículas chocam com "
                   "energia suficiente, a energia de activação. É mais "
                   "rápida com mais temperatura, mais superfície de "
                   "contacto, mais concentração, ou com um catalisador, "
                   "que baixa essa energia.",
        "exemplo": "Açúcar em água quente dissolve-se depressa; lenha "
                   "rachada arde mais que o tronco; a cinza acelera o "
                   "amadurecer da banana; a saliva digere o amido do pão.",
        "lembra": "Calor, pedaços, concentração, catalisador.",
    },
    "qui-9c:u6:n1": {
        "explica": "O azoto é 78 por cento do ar. Dele se faz o amoníaco, "
                   "pelo processo de Haber-Bosch, e do amoníaco o ácido "
                   "nítrico, pelo de Ostwald. Os nitratos, seus sais, são "
                   "adubos e explosivos.",
        "exemplo": "Quase todo o amoníaco do mundo vai para adubos: é o "
                   "azoto que faz crescer as folhas do milho.",
        "lembra": "Haber faz amoníaco; Ostwald faz ácido nítrico.",
    },
    "qui-9c:u6:n2": {
        "explica": "O fósforo branco é venenoso e arde no ar; o vermelho é "
                   "estável e vai nos fósforos. Os adubos dão azoto, "
                   "fósforo e potássio, mas a mais poluem. Uma reacção "
                   "reversível chega ao equilíbrio, e Le Chatelier diz "
                   "como este se desloca.",
        "exemplo": "Azoto para as folhas, fósforo para as raízes, potássio "
                   "para os frutos. O composto de restos e estrume é o "
                   "adubo natural.",
        "lembra": "Equilíbrio perturbado reage contra a perturbação.",
    },
    "qui-9c:u7:n1": {
        "explica": "O carbono tem formas cristalinas, o diamante, duríssimo, "
                   "e a grafite, macia e condutora, e formas amorfas, os "
                   "carvões: minerais, como a hulha, e artificiais, como o "
                   "carvão de lenha e o coque.",
        "exemplo": "O carvão de Moatize é exportado. Carvão a arder numa "
                   "casa fechada liberta monóxido de carbono, que mata sem "
                   "cheiro: deixa-se sempre ar entrar.",
        "lembra": "Carvão numa casa fechada mata.",
    },
    "qui-9c:u7:n2": {
        "explica": "O dióxido de carbono turva a água de cal e, a mais no "
                   "ar, aumenta o efeito de estufa. O silício está na "
                   "areia, dióxido de silício. Da areia faz-se o vidro; do "
                   "calcário e da argila, o cimento; da argila, a "
                   "cerâmica.",
        "exemplo": "O calcário do cimento extrai-se em Salamanga, no Dondo "
                   "e em Nacala. Soprar com uma palhinha para água de cal "
                   "turva-a: é o dióxido de carbono do nosso ar.",
        "lembra": "Areia faz vidro; calcário faz cimento.",
    },

    # ---------------------------------------------------------------
    # Ingles -- 9a classe
    # ---------------------------------------------------------------
    "ing-9c:u1:n1": {
        "explica": "No comércio usam-se «currency», «loan», «customer», "
                   "«trade». Compara-se com «as ... as» para igualdade, "
                   "«less ... than» para inferioridade e «more ... than» ou "
                   "«-er than» para superioridade. Os vizinhos da SADC "
                   "falam inglês ou português.",
        "exemplo": "«English is as important as Portuguese.» «Lichinga "
                   "market is less expensive than Maputo market.» O Malawi "
                   "fala inglês; Angola, português.",
        "lembra": "As ... as é igual; less ... than é menos.",
    },
    "ing-9c:u1:n2": {
        "explica": "«May» diz que algo pode acontecer; «can» diz que é "
                   "possível ou que se sabe fazer. O futuro de intenção faz-"
                   "se com «going to»; a previsão, com «will». Depois de "
                   "«can», «may» e «will» o verbo não leva «s».",
        "exemplo": "«Prices may go up.» «English can open many doors for "
                   "you.» «We are going to sell the tomatoes tomorrow.» "
                   "Lucro é «profit».",
        "lembra": "Can, may, will: o verbo a seguir fica simples.",
    },
    "ing-9c:u2:n1": {
        "explica": "A educação traz «training», «citizenship», «critical "
                   "sense». O advérbio de modo diz como se faz, e forma-se "
                   "quase sempre com «-ly»: «careful» dá «carefully». "
                   "Irregular: «good» dá «well».",
        "exemplo": "«She studies carefully.» «Educating girls is important "
                   "for the country.» Em casa diz-se «at home».",
        "lembra": "Adjectivo mais «-ly» dá advérbio; good dá well.",
    },
    "ing-9c:u2:n2": {
        "explica": "De nomes fazem-se adjectivos: «-ful» é com, «-less» é "
                   "sem, «-ous» é cheio de. O present perfect continuous, "
                   "«have been» mais «-ing», diz o que começou antes e "
                   "ainda continua: «since» com a data, «for» com a "
                   "duração.",
        "exemplo": "«Useful», «careless», «dangerous». «I have been "
                   "studying for two hours.» «She has been teaching here "
                   "since 2020.»",
        "lembra": "Since com a data; for com a duração.",
    },
    "ing-9c:u3:n1": {
        "explica": "Os direitos têm a sua língua: «law», «crime», «peace», "
                   "«domestic violence». «Have to» é obrigação, e com «he» "
                   "ou «she» fica «has to». O passado simples regular "
                   "acaba em «-ed». Sex é biológico; gender são os papéis "
                   "sociais.",
        "exemplo": "«Children have to go to school.» «She has to help at "
                   "home.» «The law protected the girls.»",
        "lembra": "He e she: has to.",
    },
    "ing-9c:u3:n2": {
        "explica": "«Both ... and» junta dois; «either ... or» escolhe um "
                   "dos dois; «neither ... nor» nega os dois. Os direitos "
                   "da criança: «right to education», «to health», «to "
                   "play». Igualdade de direitos é «equal rights».",
        "exemplo": "«Both boys and girls have rights.» «Neither the father "
                   "nor the mother can hit the children.» «Talk to either "
                   "the teacher or the headmaster.»",
        "lembra": "Neither vai com nor; either vai com or.",
    },
    "ing-9c:u4:n1": {
        "explica": "No campo: «fertilizer», «tractor», «dam», «reservoir». "
                   "Os adjectivos curtos comparam-se com «-er than». «Few» "
                   "é para o que se conta, «little» para o que não; "
                   "«whole» é inteiro. «Should» dá conselho.",
        "exemplo": "«Tractors are faster than hoes.» «You should dry the "
                   "fish before selling it.» «The whole village helped with "
                   "the harvest.»",
        "lembra": "Curto: -er than. Longo: more ... than.",
    },
    "ing-9c:u5:n1": {
        "explica": "No negócio: «factory», «raw material», «informal "
                   "market», «income». «A little» vai com o que não se "
                   "conta, «a few» com o que se conta. O imperativo é o "
                   "verbo sozinho. «On» é para dias, «at» para horas, «in» "
                   "para meses.",
        "exemplo": "«I have a little money.» «I have a few customers.» "
                   "«Open the shop at eight.» «On Monday», «in January».",
        "lembra": "On o dia, at a hora, in o mês.",
    },
    "ing-9c:u5:n2": {
        "explica": "A passiva põe a coisa à frente: «is» ou «are» mais o "
                   "particípio. A carta de negócio a quem não se conhece "
                   "começa por «Dear Sir or Madam». «More» e «less» "
                   "comparam quantidades.",
        "exemplo": "«Cashew is exported to India.» «These baskets are made "
                   "by hand.» «We earn more and spend less.»",
        "lembra": "Passiva: is ou are e o particípio.",
    },
    "ing-9c:u6:n1": {
        "explica": "As disciplinas: «Mathematics», «Physics», "
                   "«Chemistry», «Geography». O relativo «who» é para "
                   "pessoas, «which» para coisas, «that» para as duas. "
                   "Cada disciplina prepara profissões.",
        "exemplo": "«A doctor is a person who treats sick people.» «The "
                   "subject that I like most is Biology.» Biologia leva a "
                   "«nurse»; Matemática a «engineer».",
        "lembra": "Who para pessoas; which para coisas.",
    },
    "ing-9c:u6:n2": {
        "explica": "O passado simples diz quando: «yesterday», «in 2009». "
                   "O present perfect não diz quando: «already», «just». "
                   "A passiva do passado usa «was» ou «were». Depois de "
                   "«as soon as» e «when», o verbo fica no presente, mesmo "
                   "a falar do futuro.",
        "exemplo": "«I finished my homework yesterday.» «I have already "
                   "chosen my profession.» «As soon as I finish school, I "
                   "will work.»",
        "lembra": "Com yesterday, passado simples.",
    },
    "ing-9c:u7:n1": {
        "explica": "A tecnologia: «solar panel», «cell phone», «pedal water "
                   "pump», «website». «Do» vai com tarefas, «make» com o "
                   "que se fabrica ou produz. «Although» opõe sem «but». O "
                   "past perfect, «had» mais particípio, é o passado do "
                   "passado.",
        "exemplo": "«Do homework», «make a phone call», «make a mistake». "
                   "«Although the Internet is useful, it is expensive.» «I "
                   "had never used a computer before 2020.»",
        "lembra": "Although nunca leva but.",
    },
    "ing-9c:u8:n1": {
        "explica": "Moçambique tem figuras em cada área: Mutola no "
                   "desporto, Malangatana na pintura, Mia Couto na "
                   "escrita, Mondlane na política. «As ... as» e «like» "
                   "comparam. No discurso indirecto, o verbo recua: «am» "
                   "passa a «was».",
        "exemplo": "«She runs as fast as a car.» «He sings like an angel.» "
                   "«I am a teacher», he said: «he said that he was a "
                   "teacher».",
        "lembra": "Indirecto: o presente vira passado.",
    },
    "ing-9c:u9:n1": {
        "explica": "Depois da escola há «vocational training», "
                   "«self-employment», «entrepreneurship». Depois de "
                   "«enjoy» vem o gerúndio, com «-ing». A segunda "
                   "condicional imagina: «if» com o passado, «would» na "
                   "outra parte.",
        "exemplo": "«I enjoy working in a team.» «If I had money, I would "
                   "open a shop.» «Hard-working», «honest» e «punctual» "
                   "valem em qualquer emprego.",
        "lembra": "Enjoy pede -ing.",
    },

    # ---------------------------------------------------------------
    # Frances -- 9a classe
    # ---------------------------------------------------------------
    "fra-9c:u1:n1": {
        "explica": "A família: «le grand-père», «la tante», «le cousin», "
                   "«les parents». O adjectivo possessivo vai antes do "
                   "nome e concorda com ele: «ma mère», «mon père». O "
                   "pronome possessivo substitui o nome: «le mien», «la "
                   "mienne».",
        "exemplo": "«Ce livre est le mien.» «Je préfère ma petite sœur.» Há "
                   "famílias tradicionais, monoparentais e recompostas.",
        "lembra": "Ma mère, mon père; le mien, la mienne.",
    },
    "fra-9c:u1:n2": {
        "explica": "As festas e cerimónias: «l'anniversaire», «les "
                   "fiançailles», «le mariage», «les funérailles». O "
                   "casamento é tradicional, religioso ou civil. O "
                   "«faire-part» anuncia um casamento ou um nascimento; o "
                   "cartão deseja «meilleurs vœux».",
        "exemplo": "«Nous décorons la salle et nous dansons.» Verbos em "
                   "«-er» com «nous» acabam em «-ons».",
        "lembra": "Faire-part anuncia; meilleurs vœux deseja.",
    },
    "fra-9c:u1:n3": {
        "explica": "A carta e o email de convite têm lugar e data, "
                   "destinatário, fórmula de chamada, corpo, fórmula final "
                   "e assinatura. Convida-se com «tu veux venir», "
                   "aceita-se com «avec plaisir» e recusa-se com «je ne "
                   "peux pas».",
        "exemplo": "«Cher ami, tu veux venir à ma fête samedi?» — «Je ne "
                   "peux pas venir, j'ai un examen.»",
        "lembra": "Ne ... pas à volta do verbo que se nega.",
    },
    "fra-9c:u1:n4": {
        "explica": "Ao telefone atende-se com «allô». «Décrocher» é "
                   "atender, «raccrocher» desligar, «rappeler» voltar a "
                   "ligar. Pergunta-se com «est-ce que», e recusa-se com "
                   "educação: «c'est gentil, mais je ne suis pas libre».",
        "exemplo": "«Allô? Est-ce que tu veux aller au cinéma samedi?» O "
                   "telemóvel é «le portable», a rede é «le réseau».",
        "lembra": "Recusar bem: agradecer primeiro.",
    },
    "fra-9c:u1:n5": {
        "explica": "As refeições: «petit-déjeuner», «déjeuner», «goûter», "
                   "«dîner». Os partitivos dizem uma parte: «du pain», «de "
                   "la viande». «En» substitui a quantidade. «Il faut» e o "
                   "infinitivo dá conselho e obrigação.",
        "exemplo": "«Je mange du pain et je bois du lait.» «Combien coûte le "
                   "poisson?» «Tu veux du riz? Oui, j'en veux un peu.» «Il "
                   "faut manger des fruits.»",
        "lembra": "Du, de la, des: uma parte do que há.",
    },
    "fra-9c:u1:n6": {
        "explica": "A casa: «la chambre», «la cuisine», «la salle à "
                   "manger», «la salle de bains»; os móveis e aparelhos: "
                   "«le lit», «l'armoire», «le frigo». «Personne» e «rien» "
                   "negam com «ne», sem «pas».",
        "exemplo": "«Il n'y a personne dans la cuisine.» «Je n'ai rien "
                   "acheté.» As tarefas de casa dividem-se entre rapazes e "
                   "raparigas.",
        "lembra": "Ne ... personne, ne ... rien: nunca com pas.",
    },
    "fra-9c:u1:n7": {
        "explica": "Os anúncios de arrendamento abreviam: «T3» é uma casa "
                   "de três divisões. «Louer» é arrendar, «vendre» vender, "
                   "«chercher» procurar. Os ordinais contam os andares; o "
                   "superlativo e o comparativo comparam as casas.",
        "exemplo": "«L'appartement est au deuxième étage.» «Cette maison "
                   "est la moins chère.» «La maison est aussi grande que "
                   "l'appartement.»",
        "lembra": "Premier, deuxième, troisième: os ordinais.",
    },
    "fra-9c:u2:n1": {
        "explica": "O regulamento escolar diz o que se pode, o que se não "
                   "pode e o que se deve. Permissão: «on peut». Proibição: "
                   "«il est interdit de», «défense de», «il ne faut pas». "
                   "Obrigação: «il faut», «devoir».",
        "exemplo": "«On peut sortir à la récréation.» «Il est interdit de "
                   "fumer.» «Les élèves doivent faire les devoirs.» «Il ne "
                   "faut pas crier.»",
        "lembra": "On peut, il faut, il est interdit.",
    },
    "fra-9c:u2:n2": {
        "explica": "Para apresentar a escola dizem-se os seus espaços e as "
                   "suas pessoas: «le directeur», «le directeur adjoint», "
                   "«la secrétaire». As perguntas: «qui», «quand», «où», "
                   "«pourquoi», «combien».",
        "exemplo": "«Combien d'élèves il y a dans l'école?» «Le secrétariat "
                   "est à côté de la bibliothèque.» Todas as profissões da "
                   "escola merecem respeito.",
        "lembra": "Qui, quand, où, pourquoi, combien.",
    },
}
