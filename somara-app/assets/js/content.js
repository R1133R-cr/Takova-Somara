/* ============================================================
   SOMARA — Conteúdo (protótipo)
   Estrutura: curso (disciplina) → unidade → nível → exercício.
   Cursos: Matemática e Português, 1ª classe.
   Tipos: "count" (contar objectos), "choice" (escolha), "input"
   (escrever a resposta — texto ou número).
   Português pré-Acordo (pré-1997). Base: manuais da 1ª classe.
   ============================================================ */
window.SOMARA_CONTENT = {
  cursos: [
    {
      id: "mat-1c", disciplina: "Matemática", classe: "1ª classe", tag: "MAT",
      units: [
        { id: "u1", titulo: "Contar até 10", niveis: [
          { id: "n1", titulo: "Números 1 a 5", questoes: [
            { t: "count", q: "Quantas maçãs há?", emoji: "🍎", n: 3, options: ["2","3","4"], a: 1 },
            { t: "count", q: "Quantas estrelas há?", emoji: "⭐", n: 5, options: ["4","5","6"], a: 1 },
            { t: "choice", q: "Que número vem depois do 3?", options: ["2","4","5"], a: 1 },
            { t: "count", q: "Quantos peixes há?", emoji: "🐟", n: 2, options: ["1","2","3"], a: 1 },
            { t: "choice", q: "Qual destes é o número quatro?", options: ["3","4","6"], a: 1 }
          ]},
          { id: "n2", titulo: "Números 6 a 10", questoes: [
            { t: "count", q: "Quantas flores há?", emoji: "🌼", n: 7, options: ["6","7","8"], a: 1 },
            { t: "choice", q: "O número antes do 10 é...", options: ["8","9","11"], a: 1 },
            { t: "count", q: "Quantas bolas há?", emoji: "⚽", n: 9, options: ["8","9","10"], a: 1 },
            { t: "input", q: "Escreve o número: seis", a: "6" },
            { t: "choice", q: "Qual é o maior?", options: ["6","8","10"], a: 2 }
          ]}
        ]},
        { id: "u2", titulo: "Juntar (somar)", niveis: [
          { id: "n1", titulo: "Somar até 5", questoes: [
            { t: "count", q: "1 🍎 e mais 1 🍎. Quantas maçãs?", emoji: "🍎", n: 2, options: ["1","2","3"], a: 1 },
            { t: "choice", q: "Quanto é 2 + 1?", options: ["2","3","4"], a: 1 },
            { t: "choice", q: "Quanto é 2 + 2?", options: ["3","4","5"], a: 1 },
            { t: "input", q: "3 + 1 = ?", a: "4" },
            { t: "input", q: "1 + 4 = ?", a: "5" }
          ]},
          { id: "n2", titulo: "Somar até 10", questoes: [
            { t: "choice", q: "Quanto é 4 + 3?", options: ["6","7","8"], a: 1 },
            { t: "choice", q: "Quanto é 5 + 5?", options: ["9","10","11"], a: 1 },
            { t: "input", q: "6 + 2 = ?", a: "8" },
            { t: "input", q: "3 + 4 = ?", a: "7" },
            { t: "choice", q: "Qual soma dá 9?", options: ["4 + 4","5 + 4","6 + 4"], a: 1 }
          ]}
        ]},
        { id: "u3", titulo: "Tirar (subtrair)", niveis: [
          { id: "n1", titulo: "Subtrair até 5", questoes: [
            { t: "choice", q: "Tinhas 3 🍬 e comeste 1. Quantos ficam?", options: ["1","2","3"], a: 1 },
            { t: "choice", q: "Quanto é 4 − 2?", options: ["1","2","3"], a: 1 },
            { t: "input", q: "5 − 1 = ?", a: "4" },
            { t: "input", q: "3 − 3 = ?", a: "0" },
            { t: "choice", q: "Quanto é 5 − 4?", options: ["0","1","2"], a: 1 }
          ]},
          { id: "n2", titulo: "Subtrair até 10", questoes: [
            { t: "choice", q: "Quanto é 8 − 3?", options: ["4","5","6"], a: 1 },
            { t: "input", q: "10 − 4 = ?", a: "6" },
            { t: "input", q: "9 − 5 = ?", a: "4" },
            { t: "choice", q: "Qual conta dá 2?", options: ["7 − 4","7 − 5","7 − 6"], a: 1 },
            { t: "input", q: "10 − 10 = ?", a: "0" }
          ]}
        ]},
        { id: "u4", titulo: "Desafio final", niveis: [
          { id: "n1", titulo: "Mistura", questoes: [
            { t: "choice", q: "Quanto é 6 + 3?", options: ["8","9","10"], a: 1 },
            { t: "input", q: "9 − 2 = ?", a: "7" },
            { t: "count", q: "Quantos corações há?", emoji: "❤️", n: 8, options: ["7","8","9"], a: 1 },
            { t: "choice", q: "Quanto é 7 + 2?", options: ["8","9","10"], a: 1 },
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
            { t: "choice", q: "Qual destas letras é uma vogal?", options: ["b","a","t"], a: 1 },
            { t: "choice", q: "Qual NÃO é uma vogal?", options: ["e","i","m"], a: 2 },
            { t: "input", q: "Completa: A, E, __ , O, U", a: "i" },
            { t: "choice", q: "Quantas vogais existem?", options: ["3","5","7"], a: 1 },
            { t: "choice", q: "A palavra UVA começa por...", options: ["U","V","A"], a: 0 }
          ]},
          { id: "n2", titulo: "Vogais nas palavras", questoes: [
            { t: "choice", q: "ASA começa por...", options: ["A","S"], a: 0 },
            { t: "choice", q: "Qual palavra começa por E?", options: ["Bola","Escola","Casa"], a: 1 },
            { t: "input", q: "Completa com a vogal: ov_ (ovo)", a: "o" },
            { t: "choice", q: "IGREJA começa por...", options: ["I","G"], a: 0 },
            { t: "choice", q: "Qual palavra começa por O?", options: ["Ovo","Pato","Uva"], a: 0 }
          ]}
        ]},
        { id: "u2", titulo: "Sílabas com M", niveis: [
          { id: "n1", titulo: "ma, me, mi, mo, mu", questoes: [
            { t: "choice", q: "M + A = ?", options: ["MA","AM","MO"], a: 0 },
            { t: "choice", q: "M + I = ?", options: ["IM","MI","MU"], a: 1 },
            { t: "input", q: "Escreve: M + O", a: "MO" },
            { t: "choice", q: "Que sílaba está em MALA?", options: ["MA","ME","MU"], a: 0 },
            { t: "choice", q: "MOTA começa pela sílaba...", options: ["MU","MO","MI"], a: 1 }
          ]},
          { id: "n2", titulo: "Formar palavras", questoes: [
            { t: "choice", q: "MA + LA = ?", options: ["MALA","LAMA","MELA"], a: 0 },
            { t: "choice", q: "MA + PA = ?", options: ["PAMA","MAPA","APAM"], a: 1 },
            { t: "input", q: "Junta as sílabas: ME + SA", a: "MESA" },
            { t: "choice", q: "Qual é uma palavra de verdade?", options: ["MAMÃ","AMÃM","MÃAM"], a: 0 },
            { t: "choice", q: "MI + MO forma...", options: ["MIMO","MOMI"], a: 0 }
          ]}
        ]},
        { id: "u3", titulo: "Primeiras palavras", niveis: [
          { id: "n1", titulo: "Reconhecer palavras", questoes: [
            { t: "choice", q: "Qual palavra tem 3 letras?", options: ["SOL","CASA","PATO"], a: 0 },
            { t: "choice", q: "O contrário de 'grande' é...", options: ["pequeno","alto","gordo"], a: 0 },
            { t: "choice", q: "Que animal faz 'miau'?", options: ["cão","gato","boi"], a: 1 },
            { t: "input", q: "Escreve a palavra: c-a-s-a", a: "CASA" },
            { t: "choice", q: "Qual palavra está bem escrita?", options: ["bola","balo","obla"], a: 0 }
          ]}
        ]}
      ]
    }
  ]
};
