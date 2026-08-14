/* ============================================================
   SOMARA — Conteúdo (1ª e 2ª classes)
   Estrutura: curso (disciplina) → unidade → nível → questão.
   Tipos: "count" (contar emoji×n), "choice" (escolha; a = índice),
   "input" (escrever; comparação sem distinção de maiúsculas),
   "match" (ligar pares), "drag" (arrastar para a zona certa).
   Português pré-Acordo (pré-1997).

   Base: manuais oficiais do MINEDH. A 1ª classe segue os manuais dessa
   classe; a 2ª segue "Matemática 2.ª classe — O mundo da matemática" e o
   manual de Português da 2.ª classe, respeitando a ordem e o vocabulário
   com que os temas la aparecem. Os personagens Tito e Lila vêm dos
   próprios manuais e atravessam as duas classes, como no livro.
   ============================================================ */
window.SOMARA_CONTENT = {
  cursos: [
    {
      id: "mat-1c", disciplina: "Matemática", classe: "1ª classe", tag: "MAT",
      units: [
        { id: "u1", titulo: "Contar até 10", niveis: [
          { id: "n1", titulo: "Números 1 a 5", questoes: [
            { t: "count", q: "Quantas maçãs há?", emoji: "🍎", n: 3, options: ["2", "3", "4"], a: 1 },
            { t: "count", q: "Quantas estrelas há?", emoji: "⭐", n: 5, options: ["4", "5", "6"], a: 1 },
            { t: "choice", q: "Que número vem depois do 3?", options: ["2", "4", "5"], a: 1 },
            { t: "count", q: "Quantos peixes há?", emoji: "🐟", n: 2, options: ["1", "2", "3"], a: 1 },
            { t: "choice", q: "Que número vem antes do 2?", options: ["1", "3", "5"], a: 0 },
            { t: "choice", q: "Qual destes é o número quatro?", options: ["3", "4", "6"], a: 1 }
          ]},
          { id: "n2", titulo: "Números 6 a 10", questoes: [
            { t: "count", q: "Quantas flores há?", emoji: "🌼", n: 7, options: ["6", "7", "8"], a: 1 },
            { t: "choice", q: "O número antes do 10 é...", options: ["8", "9", "11"], a: 1 },
            { t: "count", q: "Quantas bolas há?", emoji: "⚽", n: 9, options: ["8", "9", "10"], a: 1 },
            { t: "input", q: "Escreve o número: seis", a: "6" },
            { t: "choice", q: "Qual é o maior: 6, 8 ou 10?", options: ["6", "8", "10"], a: 2 },
            { t: "count", q: "Quantos patos há?", emoji: "🦆", n: 6, options: ["5", "6", "7"], a: 1 },
            { t: "match", q: "Liga cada número à sua palavra.", pairs: [["6", "seis"], ["8", "oito"], ["10", "dez"]] }
          ]}
        ]},
        { id: "u2", titulo: "Comparar e ordenar", niveis: [
          { id: "n1", titulo: "Maior e menor", questoes: [
            { t: "choice", q: "Qual é maior: 3 ou 7?", options: ["3", "7"], a: 1 },
            { t: "choice", q: "Qual é menor: 5 ou 2?", options: ["5", "2"], a: 1 },
            { t: "choice", q: "🍎🍎🍎🍎 e 🍎🍎. Onde há mais maçãs?", options: ["No primeiro (4)", "No segundo (2)"], a: 0 },
            { t: "choice", q: "Qual é o maior número?", options: ["8", "4", "6"], a: 0 },
            { t: "choice", q: "10 é ___ que 6.", options: ["maior", "menor"], a: 0 }
          ]},
          { id: "n2", titulo: "Pôr em ordem", questoes: [
            { t: "choice", q: "Que número vem a seguir? 1, 2, 3, __", options: ["4", "5", "6"], a: 0 },
            { t: "input", q: "Falta o número: 4, 5, __ , 7", a: "6" },
            { t: "choice", q: "Contando para trás: 5, 4, 3, __", options: ["2", "1", "6"], a: 0 },
            { t: "choice", q: "Qual sequência está certa?", options: ["1, 2, 3, 4", "2, 1, 4, 3", "4, 3, 1, 2"], a: 0 },
            { t: "choice", q: "Do menor para o maior, qual vem primeiro?", options: ["7", "2", "5"], a: 1 }
          ]}
        ]},
        { id: "u3", titulo: "Juntar (somar)", niveis: [
          { id: "n1", titulo: "Somar até 5", questoes: [
            { t: "count", q: "1 🍎 e mais 1 🍎. Quantas maçãs?", emoji: "🍎", n: 2, options: ["1", "2", "3"], a: 1 },
            { t: "choice", q: "Quanto é 2 + 1?", options: ["2", "3", "4"], a: 1 },
            { t: "choice", q: "Quanto é 2 + 2?", options: ["3", "4", "5"], a: 1 },
            { t: "input", q: "3 + 1 = ?", a: "4" },
            { t: "input", q: "1 + 4 = ?", a: "5" },
            { t: "choice", q: "Quanto é 0 + 3?", options: ["0", "3", "6"], a: 1 }
          ]},
          { id: "n2", titulo: "Somar até 10", questoes: [
            { t: "choice", q: "Quanto é 4 + 3?", options: ["6", "7", "8"], a: 1 },
            { t: "choice", q: "Quanto é 5 + 5?", options: ["9", "10", "11"], a: 1 },
            { t: "input", q: "6 + 2 = ?", a: "8" },
            { t: "input", q: "3 + 4 = ?", a: "7" },
            { t: "choice", q: "Qual soma dá 9?", options: ["4 + 4", "5 + 4", "6 + 4"], a: 1 },
            { t: "input", q: "7 + 3 = ?", a: "10" }
          ]}
        ]},
        { id: "u4", titulo: "Tirar (subtrair)", niveis: [
          { id: "n1", titulo: "Subtrair até 5", questoes: [
            { t: "choice", q: "Tinhas 3 🍬 e comeste 1. Quantos ficam?", options: ["1", "2", "3"], a: 1 },
            { t: "choice", q: "Quanto é 4 − 2?", options: ["1", "2", "3"], a: 1 },
            { t: "input", q: "5 − 1 = ?", a: "4" },
            { t: "input", q: "3 − 3 = ?", a: "0" },
            { t: "choice", q: "Quanto é 5 − 4?", options: ["0", "1", "2"], a: 1 }
          ]},
          { id: "n2", titulo: "Subtrair até 10", questoes: [
            { t: "choice", q: "Quanto é 8 − 3?", options: ["4", "5", "6"], a: 1 },
            { t: "input", q: "10 − 4 = ?", a: "6" },
            { t: "input", q: "9 − 5 = ?", a: "4" },
            { t: "choice", q: "Qual conta dá 2?", options: ["7 − 4", "7 − 5", "7 − 6"], a: 1 },
            { t: "input", q: "10 − 10 = ?", a: "0" },
            { t: "input", q: "7 − 3 = ?", a: "4" }
          ]}
        ]},
        { id: "u5", titulo: "Números até 20", niveis: [
          { id: "n1", titulo: "Contar 11 a 20", questoes: [
            { t: "choice", q: "Que número vem depois do 10?", options: ["9", "11", "20"], a: 1 },
            { t: "choice", q: "12, 13, __ , 15", options: ["14", "16", "11"], a: 0 },
            { t: "input", q: "Escreve o número: quinze", a: "15" },
            { t: "choice", q: "Qual é o maior: 11, 18 ou 14?", options: ["11", "18", "14"], a: 1 },
            { t: "choice", q: "O número antes do 20 é...", options: ["18", "19", "21"], a: 1 },
            { t: "choice", q: "Dez mais dez é...", options: ["15", "20", "12"], a: 1 }
          ]},
          { id: "n2", titulo: "Somar e tirar até 20", questoes: [
            { t: "choice", q: "Quanto é 10 + 5?", options: ["14", "15", "16"], a: 1 },
            { t: "input", q: "12 + 3 = ?", a: "15" },
            { t: "input", q: "18 − 2 = ?", a: "16" },
            { t: "choice", q: "Quanto é 15 − 5?", options: ["5", "10", "20"], a: 1 },
            { t: "input", q: "11 + 4 = ?", a: "15" }
          ]}
        ]},
        { id: "u6", titulo: "Formas e meticais", niveis: [
          { id: "n1", titulo: "Formas geométricas", questoes: [
            { t: "choice", q: "Uma bola tem a forma de...", options: ["círculo", "quadrado", "triângulo"], a: 0 },
            { t: "choice", q: "Quantos lados tem um triângulo?", options: ["2", "3", "4"], a: 1 },
            { t: "choice", q: "Um quadrado tem __ lados iguais.", options: ["3", "4", "5"], a: 1 },
            { t: "choice", q: "Qual forma NÃO tem lados?", options: ["quadrado", "triângulo", "círculo"], a: 2 },
            { t: "choice", q: "Uma porta tem a forma de um...", options: ["rectângulo", "círculo", "triângulo"], a: 0 },
            { t: "drag", q: "Arrasta a bola para a forma certa.", chip: "⚽", zones: ["Círculo", "Quadrado", "Triângulo"], a: 0 }
          ]},
          { id: "n2", titulo: "Contar meticais", questoes: [
            { t: "choice", q: "Tens 5 MT e mais 5 MT. Quanto tens?", options: ["5 MT", "10 MT", "15 MT"], a: 1 },
            { t: "choice", q: "Um pão custa 5 MT. Pagas com 10 MT. O troco é...", options: ["2 MT", "5 MT", "10 MT"], a: 1 },
            { t: "input", q: "2 MT + 3 MT = ? (só o número)", a: "5" },
            { t: "choice", q: "Qual é mais dinheiro?", options: ["10 MT", "5 MT"], a: 0 },
            { t: "choice", q: "Tens 20 MT e gastas 10 MT. Ficas com...", options: ["5 MT", "10 MT", "20 MT"], a: 1 }
          ]}
        ]},
        { id: "u7", titulo: "Desafio final", niveis: [
          { id: "n1", titulo: "Mistura", questoes: [
            { t: "choice", q: "Quanto é 6 + 3?", options: ["8", "9", "10"], a: 1 },
            { t: "input", q: "9 − 2 = ?", a: "7" },
            { t: "count", q: "Quantos corações há?", emoji: "❤️", n: 8, options: ["7", "8", "9"], a: 1 },
            { t: "choice", q: "Qual é o maior: 14 ou 18?", options: ["14", "18"], a: 1 },
            { t: "choice", q: "Quanto é 7 + 2?", options: ["8", "9", "10"], a: 1 },
            { t: "input", q: "10 − 7 = ?", a: "3" }
          ]}
        ]}
      ]
    },
    {
      id: "por-1c", disciplina: "Português", classe: "1ª classe", tag: "POR",
      units: [
        { id: "u1", titulo: "As vogais", niveis: [
          { id: "n1", titulo: "Conhecer as vogais", questoes: [
            { t: "choice", q: "Qual destas letras é uma vogal?", options: ["b", "a", "t"], a: 1 },
            { t: "choice", q: "Qual NÃO é uma vogal?", options: ["e", "i", "m"], a: 2 },
            { t: "input", q: "Completa: A, E, __ , O, U", a: "I" },
            { t: "choice", q: "Quantas vogais existem?", options: ["3", "5", "7"], a: 1 },
            { t: "choice", q: "A palavra UVA começa por...", options: ["U", "V", "A"], a: 0 },
            { t: "choice", q: "Qual é a última vogal?", options: ["O", "U", "A"], a: 1 }
          ]},
          { id: "n2", titulo: "Vogais nas palavras", questoes: [
            { t: "choice", q: "ASA começa por...", options: ["A", "S"], a: 0 },
            { t: "choice", q: "Qual palavra começa por E?", options: ["Bola", "Escola", "Casa"], a: 1 },
            { t: "input", q: "Completa com a vogal: ov_ (ovo)", a: "O" },
            { t: "choice", q: "IGREJA começa por...", options: ["I", "G"], a: 0 },
            { t: "choice", q: "Qual palavra começa por O?", options: ["Ovo", "Pato", "Uva"], a: 0 },
            { t: "drag", q: "Arrasta a uva para a vogal com que UVA começa.", chip: "🍇", zones: ["A", "O", "U"], a: 2 }
          ]}
        ]},
        { id: "u2", titulo: "Sílabas com P", niveis: [
          { id: "n1", titulo: "pa, pe, pi, po, pu", questoes: [
            { t: "choice", q: "P + A = ?", options: ["PA", "AP", "PO"], a: 0 },
            { t: "choice", q: "P + I = ?", options: ["IP", "PI", "PU"], a: 1 },
            { t: "input", q: "Escreve: P + O", a: "PO" },
            { t: "choice", q: "PATO começa pela sílaba...", options: ["PU", "PA", "PE"], a: 1 },
            { t: "choice", q: "Que sílaba está em PÉ?", options: ["PA", "PE", "PI"], a: 1 }
          ]},
          { id: "n2", titulo: "Palavras com P", questoes: [
            { t: "choice", q: "PA + TO = ?", options: ["PATO", "TOPA", "APTO"], a: 0 },
            { t: "input", q: "Junta as sílabas: PI + PA", a: "PIPA" },
            { t: "choice", q: "PO + TE = ?", options: ["TEPO", "POTE"], a: 1 },
            { t: "choice", q: "Qual palavra começa por PA?", options: ["Pato", "Bola", "Mesa"], a: 0 },
            { t: "choice", q: "O 🐤 pequenino é o...", options: ["pato", "pinto", "pombo"], a: 1 }
          ]}
        ]},
        { id: "u3", titulo: "Sílabas com M", niveis: [
          { id: "n1", titulo: "ma, me, mi, mo, mu", questoes: [
            { t: "choice", q: "M + A = ?", options: ["MA", "AM", "MO"], a: 0 },
            { t: "choice", q: "M + I = ?", options: ["IM", "MI", "MU"], a: 1 },
            { t: "input", q: "Escreve: M + O", a: "MO" },
            { t: "choice", q: "Que sílaba está em MALA?", options: ["MA", "ME", "MU"], a: 0 },
            { t: "choice", q: "MOTA começa pela sílaba...", options: ["MU", "MO", "MI"], a: 1 }
          ]},
          { id: "n2", titulo: "Palavras com M", questoes: [
            { t: "choice", q: "MA + LA = ?", options: ["MALA", "LAMA", "MELA"], a: 0 },
            { t: "choice", q: "MA + PA = ?", options: ["PAMA", "MAPA"], a: 1 },
            { t: "input", q: "Junta as sílabas: ME + SA", a: "MESA" },
            { t: "choice", q: "Qual é uma palavra de verdade?", options: ["MAMÃ", "AMÃM", "MÃAM"], a: 0 },
            { t: "choice", q: "MI + MO forma...", options: ["MIMO", "MOMI"], a: 0 }
          ]}
        ]},
        { id: "u4", titulo: "Sílabas com L e T", niveis: [
          { id: "n1", titulo: "la, le, li... / ta, te, ti...", questoes: [
            { t: "choice", q: "L + A = ?", options: ["LA", "AL", "LO"], a: 0 },
            { t: "choice", q: "T + E = ?", options: ["ET", "TE", "TI"], a: 1 },
            { t: "input", q: "Escreve: L + I", a: "LI" },
            { t: "choice", q: "TIA começa pela sílaba...", options: ["TI", "TA", "TU"], a: 0 },
            { t: "choice", q: "Que sílaba está no fim de BOLA?", options: ["LA", "LE", "LI"], a: 0 }
          ]},
          { id: "n2", titulo: "Palavras (L e T)", questoes: [
            { t: "choice", q: "TA + TU = ?", options: ["TATU", "TUTA"], a: 0 },
            { t: "choice", q: "LA + TA = ?", options: ["TALA", "LATA"], a: 1 },
            { t: "input", q: "Junta as sílabas: TE + LA", a: "TELA" },
            { t: "choice", q: "LU + A = ?", options: ["ALU", "LUA"], a: 1 },
            { t: "choice", q: "O gato faz...", options: ["au", "miau", "mu"], a: 1 }
          ]}
        ]},
        { id: "u5", titulo: "Formar palavras", niveis: [
          { id: "n1", titulo: "Juntar sílabas", questoes: [
            { t: "choice", q: "CA + SA = ?", options: ["CASA", "SACA", "ACAS"], a: 0 },
            { t: "choice", q: "BO + LA = ?", options: ["LOBA", "BOLA"], a: 1 },
            { t: "input", q: "Junta as sílabas: SO + PA", a: "SOPA" },
            { t: "choice", q: "GA + TO = ?", options: ["TOGA", "GATO"], a: 1 },
            { t: "input", q: "Junta as sílabas: DE + DO", a: "DEDO" },
            { t: "choice", q: "Qual palavra tem 2 sílabas?", options: ["SOL", "CASA", "PÃO"], a: 1 }
          ]}
        ]},
        { id: "u6", titulo: "Primeiras frases", niveis: [
          { id: "n1", titulo: "A frase", questoes: [
            { t: "choice", q: "Uma frase começa com letra...", options: ["pequena", "grande (maiúscula)"], a: 1 },
            { t: "choice", q: "No fim de uma frase pomos...", options: ["ponto final (.)", "nada", "um número"], a: 0 },
            { t: "choice", q: "Qual frase está bem escrita?", options: ["o gato dorme", "O gato dorme.", "gato o dorme"], a: 1 },
            { t: "choice", q: "Ordena: bola / a / é / vermelha", options: ["A bola é vermelha.", "Bola vermelha a é.", "É a bola vermelha"], a: 0 },
            { t: "choice", q: "O nome das pessoas começa por letra...", options: ["pequena", "maiúscula"], a: 1 }
          ]}
        ]},
        { id: "u7", titulo: "Ler e compreender", niveis: [
          { id: "n1", titulo: "Compreensão", questoes: [
            { t: "choice", q: "O Pedro tem um cão. O cão chama-se Bobi. Como se chama o cão?", options: ["Pedro", "Bobi", "Cão"], a: 1 },
            { t: "choice", q: "A Ana come uma maçã. O que come a Ana?", options: ["uma banana", "uma maçã", "um pão"], a: 1 },
            { t: "choice", q: "Está a chover. O que levamos para a rua?", options: ["chapéu-de-chuva", "óculos de sol", "uma bola"], a: 0 },
            { t: "choice", q: "O Sol brilha de dia. Quando brilha o Sol?", options: ["de noite", "de dia"], a: 1 },
            { t: "choice", q: "A vaca dá-nos...", options: ["leite", "lã", "mel"], a: 0 },
            { t: "match", q: "Liga cada animal ao som que faz.", pairs: [["Gato", "Miau"], ["Cão", "Au-au"], ["Vaca", "Mu"]] }
          ]}
        ]}
      ]
    },

    /* ---------- 2ª CLASSE ---------- */

    {
      id: "mat-2c", disciplina: "Matemática", classe: "2ª classe", tag: "MAT",
      units: [
        { id: "u1", titulo: "Números até 100", niveis: [
          { id: "n1", titulo: "Ler e escrever até 100", questoes: [
            { t: "choice", q: "Como se escreve o número 57 por extenso?", options: ["cinquenta e sete", "setenta e cinco", "quinze e sete"], a: 0 },
            { t: "input", q: "Escreve em algarismos: oitenta e quatro.", a: "84" },
            { t: "input", q: "Escreve em algarismos: noventa e nove.", a: "99" },
            { t: "choice", q: "Qual é o número que vem depois de 69?", options: ["68", "70", "79"], a: 1 },
            { t: "choice", q: "Qual é o número que vem antes de 80?", options: ["81", "79", "70"], a: 1 }
          ]},
          { id: "n2", titulo: "Ordenar e comparar", questoes: [
            { t: "choice", q: "Qual símbolo completa? 45 __ 54", options: ["<", ">", "="], a: 0 },
            { t: "choice", q: "Qual símbolo completa? 78 __ 78", options: ["<", ">", "="], a: 2 },
            { t: "choice", q: "Qual símbolo completa? 91 __ 19", options: ["<", ">", "="], a: 1 },
            { t: "choice", q: "Qual destes é o maior número?", options: ["63", "36", "60"], a: 0 },
            { t: "choice", q: "Por ordem crescente: 40, 14, 41.", options: ["14, 40, 41", "41, 40, 14", "40, 41, 14"], a: 0 }
          ]},
          { id: "n3", titulo: "Dezena e unidade", questoes: [
            { t: "choice", q: "Quantas dezenas tem o número 47?", options: ["4", "7", "47"], a: 0 },
            { t: "choice", q: "Quantas unidades tem o número 47?", options: ["4", "7", "11"], a: 1 },
            { t: "input", q: "6 dezenas e 3 unidades formam que número?", a: "63" },
            { t: "choice", q: "80 = 8 dezenas e ...", options: ["0 unidades", "8 unidades", "80 unidades"], a: 0 },
            { t: "input", q: "Decompõe: 25 = 20 + ?", a: "5" }
          ]}
        ]},
        { id: "u2", titulo: "Somar e tirar até 100", niveis: [
          { id: "n1", titulo: "Adição até 100", questoes: [
            { t: "input", q: "Calcula: 34 + 25 =", a: "59" },
            { t: "input", q: "Calcula: 46 + 30 =", a: "76" },
            { t: "input", q: "Calcula: 58 + 7 =", a: "65" },
            { t: "choice", q: "A Lila tem 40 meticais e ganha 35. Com quanto fica?", options: ["75 meticais", "5 meticais", "70 meticais"], a: 0 },
            { t: "input", q: "Calcula: 27 + 27 =", a: "54" }
          ]},
          { id: "n2", titulo: "Subtracção até 100", questoes: [
            { t: "input", q: "Calcula: 68 − 25 =", a: "43" },
            { t: "input", q: "Calcula: 90 − 40 =", a: "50" },
            { t: "input", q: "Calcula: 73 − 8 =", a: "65" },
            { t: "choice", q: "O Tito tinha 55 mangas e vendeu 20. Quantas ficaram?", options: ["35", "75", "25"], a: 0 },
            { t: "input", q: "Calcula: 100 − 60 =", a: "40" }
          ]},
          { id: "n3", titulo: "Números ordinais", questoes: [
            { t: "choice", q: "Quem chega em 1.º lugar chega em...", options: ["primeiro", "último", "terceiro"], a: 0 },
            { t: "choice", q: "Como se lê 7.º?", options: ["sétimo", "sete", "setenta"], a: 0 },
            { t: "choice", q: "Depois de 9.º vem...", options: ["10.º", "8.º", "19.º"], a: 0 },
            { t: "match", q: "Liga o número ordinal à palavra.", pairs: [["2.º", "segundo"], ["5.º", "quinto"], ["20.º", "vigésimo"]] },
            { t: "choice", q: "A Lila ficou em 3.º lugar. Quantos chegaram à frente dela?", options: ["2", "3", "4"], a: 0 }
          ]}
        ]},
        { id: "u3", titulo: "Grandezas e Medidas", niveis: [
          { id: "n1", titulo: "O relógio", questoes: [
            { t: "choice", q: "Um dia tem quantas horas?", options: ["24 horas", "12 horas", "60 horas"], a: 0 },
            { t: "choice", q: "Uma hora tem quantos minutos?", options: ["60", "24", "100"], a: 0 },
            { t: "choice", q: "O ponteiro pequeno do relógio marca as...", options: ["horas", "minutos", "semanas"], a: 0 },
            { t: "choice", q: "Quando o ponteiro grande está no 12 e o pequeno no 3, são...", options: ["3 horas", "12 horas", "15 horas"], a: 0 },
            { t: "drag", q: "Arrasta o Sol para a altura do dia em que ele nasce.", chip: "☀️", zones: ["De manhã", "À noite"], a: 0 }
          ]},
          { id: "n2", titulo: "O calendário", questoes: [
            { t: "choice", q: "Uma semana tem quantos dias?", options: ["7", "5", "30"], a: 0 },
            { t: "choice", q: "Um ano tem quantos meses?", options: ["12", "10", "7"], a: 0 },
            { t: "choice", q: "Qual é o primeiro mês do ano?", options: ["Janeiro", "Dezembro", "Março"], a: 0 },
            { t: "choice", q: "Que dia vem depois de terça-feira?", options: ["quarta-feira", "segunda-feira", "domingo"], a: 0 },
            { t: "match", q: "Liga cada mês à sua posição no ano.", pairs: [["Janeiro", "1.º mês"], ["Junho", "6.º mês"], ["Dezembro", "12.º mês"]] }
          ]}
        ]},
        { id: "u4", titulo: "Multiplicar e contar", niveis: [
          { id: "n1", titulo: "Multiplicação até 50", questoes: [
            { t: "input", q: "Calcula: 2 × 5 =", a: "10" },
            { t: "input", q: "Calcula: 4 × 3 =", a: "12" },
            { t: "choice", q: "3 + 3 + 3 + 3 é o mesmo que...", options: ["4 × 3", "3 × 3", "4 + 3"], a: 0 },
            { t: "input", q: "Calcula: 5 × 8 =", a: "40" },
            { t: "choice", q: "Cada caixa tem 6 ovos. Quantos ovos há em 4 caixas?", options: ["24", "10", "18"], a: 0 }
          ]},
          { id: "n2", titulo: "Pares, ímpares e contagens", questoes: [
            { t: "choice", q: "Qual destes números é par?", options: ["18", "17", "15"], a: 0 },
            { t: "choice", q: "Qual destes números é ímpar?", options: ["23", "20", "16"], a: 0 },
            { t: "input", q: "Conta de 5 em 5: 5, 10, 15, ?", a: "20" },
            { t: "input", q: "Conta de 10 em 10: 40, 50, 60, ?", a: "70" },
            { t: "choice", q: "Contando de 2 em 2 a partir de 0, chegamos ao...", options: ["8", "9", "7"], a: 0 }
          ]}
        ]},
        { id: "u5", titulo: "Espaço e Forma", niveis: [
          { id: "n1", titulo: "Linhas e figuras", questoes: [
            { t: "choice", q: "Uma linha que não faz curvas chama-se linha...", options: ["recta", "curva", "redonda"], a: 0 },
            { t: "choice", q: "Quantos lados tem um quadrado?", options: ["4", "3", "6"], a: 0 },
            { t: "choice", q: "Quantos lados tem um triângulo?", options: ["3", "4", "5"], a: 0 },
            { t: "choice", q: "Qual figura não tem lados nem cantos?", options: ["o círculo", "o quadrado", "o rectângulo"], a: 0 },
            { t: "match", q: "Liga cada figura ao número de lados.", pairs: [["Triângulo", "3 lados"], ["Quadrado", "4 lados"], ["Círculo", "sem lados"]] }
          ]},
          { id: "n2", titulo: "Sólidos geométricos", questoes: [
            { t: "choice", q: "Uma bola tem a forma de...", options: ["esfera", "cubo", "cilindro"], a: 0 },
            { t: "choice", q: "Um dado tem a forma de...", options: ["cubo", "esfera", "cone"], a: 0 },
            { t: "choice", q: "Uma lata de conserva tem a forma de...", options: ["cilindro", "cubo", "esfera"], a: 0 },
            { t: "choice", q: "Qual destes sólidos rola?", options: ["a esfera", "o cubo"], a: 0 },
            { t: "drag", q: "Arrasta o dado para o sólido com que se parece.", chip: "🎲", zones: ["Cubo", "Esfera"], a: 0 }
          ]}
        ]}
      ]
    },

    {
      id: "por-2c", disciplina: "Português", classe: "2ª classe", tag: "POR",
      units: [
        { id: "u1", titulo: "Família", niveis: [
          { id: "n1", titulo: "Sílabas e palavras", questoes: [
            { t: "choice", q: "Quantas sílabas tem a palavra «fa-mí-lia»?", options: ["3", "2", "4"], a: 0 },
            { t: "choice", q: "Como se divide «menino» em sílabas?", options: ["me-ni-no", "men-ino", "meni-no"], a: 0 },
            { t: "input", q: "Junta as sílabas e escreve a palavra: MA + NA", a: "mana" },
            { t: "input", q: "Junta as sílabas e escreve a palavra: PA + PÁ + IA", a: "papaia" },
            { t: "choice", q: "Quantas sílabas tem «pai»?", options: ["1", "2", "3"], a: 0 }
          ]},
          { id: "n2", titulo: "Frases", questoes: [
            { t: "choice", q: "Ordena: casa / na / Tito / está / o", options: ["O Tito está na casa.", "Casa o Tito na está.", "Está o na Tito casa."], a: 0 },
            { t: "choice", q: "Que frase está bem escrita?", options: ["A Lila come papaia.", "a lila come papaia", "A Lila come papaia"], a: 0 },
            { t: "choice", q: "Uma pergunta acaba com que sinal?", options: ["?", ".", "!"], a: 0 },
            { t: "choice", q: "Os nomes das pessoas escrevem-se com letra...", options: ["maiúscula", "minúscula"], a: 0 },
            { t: "input", q: "Completa: A minha mãe e o meu pai são os meus ___.", a: "pais" }
          ]}
        ]},
        { id: "u2", titulo: "Escola", niveis: [
          { id: "n1", titulo: "Dar ordens", questoes: [
            { t: "choice", q: "Qual destas frases dá uma ordem?", options: ["Abre o livro.", "O livro é azul.", "O livro está na mesa."], a: 0 },
            { t: "choice", q: "O contrário de «Abre a porta.» é...", options: ["Fecha a porta.", "A porta é grande.", "Abre a janela."], a: 0 },
            { t: "choice", q: "Qual é uma frase imperativa?", options: ["Levanta a mão.", "Eu levanto a mão."], a: 0 },
            { t: "match", q: "Liga cada ordem à ordem contrária.", pairs: [["Abre o livro", "Fecha o livro"], ["Levanta a mão", "Baixa a mão"], ["Entra", "Sai"]] },
            { t: "choice", q: "Quem ensina na escola é o...", options: ["professor", "médico", "motorista"], a: 0 }
          ]},
          { id: "n2", titulo: "Artigos", questoes: [
            { t: "choice", q: "Completa: ___ caderno é novo.", options: ["O", "A", "As"], a: 0 },
            { t: "choice", q: "Completa: ___ professora chegou.", options: ["A", "O", "Os"], a: 0 },
            { t: "choice", q: "Completa com artigo indefinido: Vi ___ cão na rua.", options: ["um", "o", "as"], a: 0 },
            { t: "choice", q: "Qual é o plural de «o livro»?", options: ["os livros", "a livro", "um livro"], a: 0 },
            { t: "choice", q: "«Uma» e «um» são artigos...", options: ["indefinidos", "definidos"], a: 0 }
          ]}
        ]},
        { id: "u3", titulo: "Corpo humano", niveis: [
          { id: "n1", titulo: "Pronomes possessivos", questoes: [
            { t: "choice", q: "Completa: Esta é ___ mão. (de mim)", options: ["a minha", "a tua", "a dele"], a: 0 },
            { t: "choice", q: "Completa: Esse é ___ livro. (de ti)", options: ["o teu", "o meu", "o dela"], a: 0 },
            { t: "choice", q: "Completa: O Tito perdeu ___ caderno. (dele)", options: ["o seu", "o meu", "o teu"], a: 0 },
            { t: "match", q: "Liga a pessoa ao possessivo.", pairs: [["Eu", "meu"], ["Tu", "teu"], ["Ele", "dele"]] },
            { t: "choice", q: "Completa: Estas são ___ orelhas. (de mim)", options: ["as minhas", "os meus", "a minha"], a: 0 }
          ]},
          { id: "n2", titulo: "Nomes e adjectivos", questoes: [
            { t: "choice", q: "Completa: A menina é ___.", options: ["bonita", "bonito", "bonitos"], a: 0 },
            { t: "choice", q: "Completa: Os meninos são ___.", options: ["altos", "alto", "alta"], a: 0 },
            { t: "choice", q: "Qual é o feminino de «menino»?", options: ["menina", "meninos", "meninho"], a: 0 },
            { t: "choice", q: "Qual é o plural de «mão»?", options: ["mãos", "mães", "manos"], a: 0 },
            { t: "input", q: "Qual é o plural de «pé»?", a: "pés" }
          ]}
        ]},
        { id: "u4", titulo: "Saúde e higiene", niveis: [
          { id: "n1", titulo: "Pronomes demonstrativos", questoes: [
            { t: "choice", q: "Para algo que está perto de mim digo...", options: ["este", "aquele", "esse"], a: 0 },
            { t: "choice", q: "Para algo que está longe dos dois digo...", options: ["aquele", "este", "esta"], a: 0 },
            { t: "choice", q: "Completa: ___ sabão está na minha mão.", options: ["Este", "Aquela", "Aqueles"], a: 0 },
            { t: "match", q: "Liga a distância ao pronome.", pairs: [["Perto de mim", "este"], ["Perto de ti", "esse"], ["Longe dos dois", "aquele"]] },
            { t: "choice", q: "Completa: ___ água está limpa.", options: ["Esta", "Este", "Estes"], a: 0 }
          ]},
          { id: "n2", titulo: "Compreender o texto", questoes: [
            { t: "choice", q: "Devemos lavar as mãos antes de...", options: ["comer", "dormir a sesta", "correr"], a: 0 },
            { t: "choice", q: "A Lila escova os dentes de manhã e à noite. Quantas vezes por dia?", options: ["2", "1", "3"], a: 0 },
            { t: "choice", q: "Para não adoecer devemos beber água...", options: ["limpa", "do charco", "suja"], a: 0 },
            { t: "choice", q: "O Tito cortou o dedo. Deve procurar...", options: ["o hospital", "a machamba", "o mercado"], a: 0 },
            { t: "drag", q: "Arrasta o sabão para o que ele serve.", chip: "🧼", zones: ["Lavar as mãos", "Comer"], a: 0 }
          ]}
        ]},
        { id: "u5", titulo: "Ambiente", niveis: [
          { id: "n1", titulo: "Verbos ser e estar", questoes: [
            { t: "choice", q: "Completa: A árvore ___ grande.", options: ["é", "são", "estão"], a: 0 },
            { t: "choice", q: "Completa: As flores ___ bonitas.", options: ["são", "é", "está"], a: 0 },
            { t: "choice", q: "Completa: O Tito ___ na machamba agora.", options: ["está", "é", "eram"], a: 0 },
            { t: "choice", q: "Ontem eu ___ na escola.", options: ["estive", "estou", "estarei"], a: 0 },
            { t: "choice", q: "Amanhã nós ___ no campo.", options: ["estaremos", "estivemos", "estamos"], a: 0 }
          ]},
          { id: "n2", titulo: "Cuidar do ambiente", questoes: [
            { t: "choice", q: "O lixo deve ser posto...", options: ["no caixote", "no chão", "no rio"], a: 0 },
            { t: "choice", q: "Cortar árvores sem plantar outras faz...", options: ["mal ao ambiente", "bem ao ambiente"], a: 0 },
            { t: "choice", q: "A água do rio serve para...", options: ["beber e regar", "deitar lixo"], a: 0 },
            { t: "match", q: "Liga cada palavra ao seu grupo.", pairs: [["Baobá", "árvore"], ["Zambeze", "rio"], ["Leão", "animal"]] },
            { t: "input", q: "Completa: Devemos ___ árvores para ter sombra.", a: "plantar" }
          ]}
        ]},
        { id: "u6", titulo: "Comunidade", niveis: [
          { id: "n1", titulo: "Pronomes indefinidos", questoes: [
            { t: "choice", q: "Completa: ___ os alunos chegaram.", options: ["Todos", "Toda", "Todas"], a: 0 },
            { t: "choice", q: "Completa: ___ as meninas cantaram.", options: ["Todas", "Todos", "Todo"], a: 0 },
            { t: "choice", q: "«Ninguém faltou» quer dizer que faltaram...", options: ["zero pessoas", "muitas pessoas"], a: 0 },
            { t: "choice", q: "Completa: ___ pessoa trouxe água.", options: ["Alguma", "Alguns", "Todos"], a: 0 },
            { t: "choice", q: "O contrário de «todos» é...", options: ["nenhum", "muitos", "alguns"], a: 0 }
          ]},
          { id: "n2", titulo: "Fábula e conto", questoes: [
            { t: "choice", q: "Numa fábula, quem costuma falar?", options: ["os animais", "só as pessoas", "as pedras"], a: 0 },
            { t: "choice", q: "A lição que uma fábula ensina chama-se...", options: ["moral", "título", "início"], a: 0 },
            { t: "choice", q: "Um conto começa muitas vezes por...", options: ["«Era uma vez»", "«Fim»", "«Adeus»"], a: 0 },
            { t: "choice", q: "A lebre e a tartaruga: quem ganhou a corrida?", options: ["a tartaruga", "a lebre"], a: 0 },
            { t: "choice", q: "Essa fábula ensina que devemos ser...", options: ["persistentes", "preguiçosos", "distraídos"], a: 0 }
          ]}
        ]}
      ]
    }
  ]
};
