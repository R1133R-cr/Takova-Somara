/* ============================================================
   SOMARA — Conteúdo (1ª classe)
   Estrutura: curso (disciplina) → unidade → nível → questão.
   Tipos: "count" (contar emoji×n), "choice" (escolha; a = índice),
   "input" (escrever; comparação sem distinção de maiúsculas).
   Português pré-Acordo (pré-1997). Base: currículo da 1ª classe.
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
            { t: "choice", q: "Qual é o maior?", options: ["6", "8", "10"], a: 2 },
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
            { t: "choice", q: "Qual é o maior?", options: ["11", "18", "14"], a: 1 },
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
    }
  ]
};
