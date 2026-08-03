/* ============================================================
   SOMARA — Conteúdo (1ª classe)
   Estrutura: curso (disciplina) → unidade → nível → questão.
   Tipos: "count" (contar emoji×n), "choice" (escolha; a = índice),
   "input" (escrever), "match" (ligar pares), "drag" (arrastar; a = índice da zona certa).
   Português pré-Acordo (pré-1997).

   Conteúdo BASEADO NO CURRÍCULO REAL da 1ª classe moçambicana —
   extraído (texto real, não OCR) de "Matemática 1.ª classe" e
   "Língua Portuguesa 1.ª classe" (INDE/MINEDH, distribuição gratuita).
   Segue a sequência real dos manuais: em Matemática, Vocabulário
   Básico (quantidade → tamanho → posição → distância) antes dos
   números; em Português, a ordem real de introdução das vogais
   (i, u, o, e, a) e consoantes (m, p, t, l, n). Tito e Lila são as
   personagens recorrentes do manual real.
   ============================================================ */
window.SOMARA_CONTENT = {
  cursos: [
    {
      id: "mat-1c", disciplina: "Matemática", classe: "1ª classe", tag: "MAT",
      units: [
        { id: "u1", titulo: "Vocabulário básico: quantidade", niveis: [
          { id: "n1", titulo: "Muito, pouco, mais e menos", questoes: [
            { t: "count", q: "Muitas ou poucas mangas? Conta.", emoji: "🥭", n: 6, options: ["Poucas", "Muitas"], a: 1 },
            { t: "count", q: "Muitos ou poucos cabritos? Conta.", emoji: "🐐", n: 2, options: ["Muitos", "Poucos"], a: 1 },
            { t: "choice", q: "🍊🍊 laranjas e 🍊🍊🍊🍊 laranjas. Onde há menos laranjas?", options: ["No primeiro grupo", "No segundo grupo"], a: 0 },
            { t: "choice", q: "🍈🍈🍈🍈🍈 papaias e 🍈🍈 papaias. Onde há mais papaias?", options: ["No primeiro grupo", "No segundo grupo"], a: 0 },
            { t: "choice", q: "🌼🌼🌼 flores e 🏺🏺 vasos. Há menos flores do que vasos?", options: ["Sim", "Não, há mais flores"], a: 1 },
            { t: "choice", q: "👧👧👧 meninas e 👦👦👦 meninos. Há tantas meninas como meninos?", options: ["Sim", "Não"], a: 0 }
          ]},
          { id: "n2", titulo: "Cheio, vazio, pôr e tirar", questoes: [
            { t: "choice", q: "Uma garrafa cheia de sumo e um cesto vazio. Qual está vazio?", options: ["A garrafa", "O cesto"], a: 1 },
            { t: "choice", q: "O Tito está a pôr água no tambor e a Lila está a tirar água do poço. Quem está a pôr água?", options: ["O Tito", "A Lila"], a: 0 },
            { t: "choice", q: "Se estás a aumentar a água do tambor, a água...", options: ["sobe", "desce"], a: 0 },
            { t: "choice", q: "Se estás a diminuir a água do tambor, a água...", options: ["sobe", "desce"], a: 1 },
            { t: "input", q: "Escreve: cheio ou ___ (o contrário de cheio)", a: "vazio" },
            { t: "input", q: "Escreve: pôr ou ___ (o contrário de pôr)", a: "tirar" }
          ]}
        ]},
        { id: "u2", titulo: "Vocabulário básico: tamanho", niveis: [
          { id: "n1", titulo: "Grande, pequeno, maior e menor", questoes: [
            { t: "choice", q: "Uma panela grande e uma panela pequena. Qual escolhes para cozinhar para toda a família?", options: ["A grande", "A pequena"], a: 0 },
            { t: "choice", q: "🐟 (peixe pequeno) e 🐠 (peixe maior). Qual é o peixe menor?", options: ["O primeiro", "O segundo"], a: 0 },
            { t: "choice", q: "⛵ barco pequeno e 🚢 barco grande. Pinta o maior — qual é?", options: ["O barco pequeno", "O barco grande"], a: 1 },
            { t: "choice", q: "🦆 pato grande e 🐤 pato pequeno. Circunda o maior pato — qual é?", options: ["O pato grande", "O pato pequeno"], a: 0 },
            { t: "input", q: "Escreve: maior ou ___ (o contrário de maior)", a: "menor" }
          ]},
          { id: "n2", titulo: "Comprido, largo, alto, grosso", questoes: [
            { t: "choice", q: "Uma corda comprida e um pau curto. Qual é comprida?", options: ["A corda", "O pau"], a: 0 },
            { t: "choice", q: "Uma tábua estreita e um caminho largo. Qual é largo?", options: ["A tábua", "O caminho"], a: 1 },
            { t: "choice", q: "Um coqueiro alto e uma casa baixa. Qual é alto?", options: ["O coqueiro", "A casa"], a: 0 },
            { t: "choice", q: "Uma gravata fina e um tronco grosso. Qual é grosso?", options: ["A gravata", "O tronco"], a: 1 },
            { t: "match", q: "Liga cada palavra ao seu contrário.", pairs: [["Comprido", "Curto"], ["Largo", "Estreito"], ["Alto", "Baixo"], ["Grosso", "Fino"]] }
          ]}
        ]},
        { id: "u3", titulo: "Noção de posição", niveis: [
          { id: "n1", titulo: "Frente, atrás, esquerda, direita", questoes: [
            { t: "choice", q: "🐤➡️🧒 O pato está à frente do menino. Quem está atrás?", options: ["O pato", "O menino"], a: 1 },
            { t: "choice", q: "🎈 à direita da menina e 🌳 à esquerda. Onde está a árvore?", options: ["À direita", "À esquerda"], a: 1 },
            { t: "choice", q: "O machimbombo está depois da paragem. Passou a paragem?", options: ["Sim, já passou", "Não, ainda não chegou"], a: 0 },
            { t: "choice", q: "O Tito está antes da Escola e depois do posto de saúde. Onde fica o posto de saúde?", options: ["Antes do Tito", "Depois do Tito"], a: 0 },
            { t: "input", q: "Escreve: à esquerda ou ___ (o contrário)", a: "à direita" }
          ]},
          { id: "n2", titulo: "Primeiro, último, meio, entre", questoes: [
            { t: "choice", q: "🥇🥈🥉 numa corrida — quem está em primeiro?", options: ["O atleta da frente", "O atleta de trás"], a: 0 },
            { t: "choice", q: "O Tito está entre a mãe e o pai. Quantas pessoas há de cada lado do Tito?", options: ["Uma de cada lado", "Duas de cada lado"], a: 0 },
            { t: "choice", q: "A bola está no meio do campo. Está mais perto de um dos lados?", options: ["Não, está no centro", "Sim, de um dos lados"], a: 0 },
            { t: "choice", q: "🦜🔲 O papagaio está dentro da gaiola. Está livre?", options: ["Sim", "Não, está dentro"], a: 1 },
            { t: "choice", q: "🏺➡️🌼 As flores estão fora do vaso. Onde estão as flores?", options: ["Dentro do vaso", "Fora do vaso"], a: 1 },
            { t: "choice", q: "O vaso está em cima da mesa. O que está em baixo, na mesma imagem?", options: ["Também o vaso", "Um animal, por exemplo"], a: 1 }
          ]}
        ]},
        { id: "u4", titulo: "Distância e direcção", niveis: [
          { id: "n1", titulo: "Perto, longe, aproximar e afastar", questoes: [
            { t: "choice", q: "O Tito está perto da Escola. A Lila está longe da Escola. Quem chega primeiro?", options: ["O Tito", "A Lila"], a: 0 },
            { t: "choice", q: "🐥🐔 O pintainho está perto da galinha e o cão está longe do osso. Quem está perto?", options: ["O pintainho", "O cão"], a: 0 },
            { t: "choice", q: "A Lila está a aproximar-se da Escola. Está a ficar mais perto ou mais longe?", options: ["Mais perto", "Mais longe"], a: 0 },
            { t: "choice", q: "O Tito está a afastar-se da Escola. Está a ficar mais perto ou mais longe?", options: ["Mais perto", "Mais longe"], a: 1 },
            { t: "choice", q: "🐄🐄 Os animais estão a aproximar-se do curral. O barco está a afastar-se do cais. O barco está a chegar ou a partir?", options: ["A chegar", "A partir"], a: 1 },
            { t: "input", q: "Escreve: aproximar ou ___ (o contrário)", a: "afastar" }
          ]}
        ]},
        { id: "u5", titulo: "Números 1 a 5", niveis: [
          { id: "n1", titulo: "Contar e ordenar até 5", questoes: [
            { t: "count", q: "Observa com atenção. Quantos há?", emoji: "⭐", n: 1, options: ["1", "2", "3"], a: 0 },
            { t: "count", q: "Observa com atenção. Quantos há?", emoji: "🔵", n: 3, options: ["2", "3", "4"], a: 1 },
            { t: "count", q: "Observa com atenção. Quantos há?", emoji: "🔵", n: 5, options: ["4", "5", "6"], a: 1 },
            { t: "input", q: "Escreve por ordem crescente: 2, 4, 1, 3, 5 → o menor primeiro é", a: "1" },
            { t: "choice", q: "Ordem decrescente de 4, 2, 5, 1, 3 — qual vem primeiro?", options: ["1", "3", "5"], a: 2 },
            { t: "choice", q: "Qual é o maior número: 3 ou 5?", options: ["3", "5"], a: 1 },
            { t: "choice", q: "Qual é o menor número: 2 ou 4?", options: ["2", "4"], a: 0 }
          ]},
          { id: "n2", titulo: "Somar e subtrair até 5", questoes: [
            { t: "input", q: "Um mais um é igual a dois. 1 + 1 = ?", a: "2" },
            { t: "input", q: "1 + 2 = ?", a: "3" },
            { t: "input", q: "2 + 2 = ?", a: "4" },
            { t: "input", q: "3 + 2 = ?", a: "5" },
            { t: "input", q: "Três menos um é igual a dois. 3 − 1 = ?", a: "2" },
            { t: "input", q: "5 − 2 = ?", a: "3" },
            { t: "input", q: "4 − 3 = ?", a: "1" }
          ]}
        ]},
        { id: "u6", titulo: "Espaço e forma", niveis: [
          { id: "n1", titulo: "Linhas e figuras geométricas", questoes: [
            { t: "choice", q: "Uma linha que começa e acaba no mesmo ponto, sem interrupção, é uma linha...", options: ["aberta", "fechada"], a: 1 },
            { t: "choice", q: "Uma linha que não volta ao ponto de partida é uma linha...", options: ["aberta", "fechada"], a: 0 },
            { t: "choice", q: "Uma estrada a direito é uma linha...", options: ["recta", "curva"], a: 0 },
            { t: "choice", q: "Um arco-íris é uma linha...", options: ["recta", "curva"], a: 1 },
            { t: "choice", q: "Uma bola tem a forma de um...", options: ["círculo", "triângulo"], a: 0 },
            { t: "choice", q: "Quantos lados tem um triângulo?", options: ["3", "4"], a: 0 },
            { t: "drag", q: "Arrasta a porta para a forma certa.", chip: "🚪", zones: ["Rectângulo", "Círculo", "Triângulo"], a: 0 }
          ]}
        ]},
        { id: "u7", titulo: "Números 6 a 10", niveis: [
          { id: "n1", titulo: "Contar 6 a 10", questoes: [
            { t: "count", q: "Observa com atenção e aprende o número 6.", emoji: "🥭", n: 6, options: ["5", "6", "7"], a: 1 },
            { t: "count", q: "Observa com atenção e aprende o número 8.", emoji: "🐐", n: 8, options: ["7", "8", "9"], a: 1 },
            { t: "count", q: "Observa com atenção e aprende o número 9.", emoji: "🌼", n: 9, options: ["8", "9", "10"], a: 1 },
            { t: "input", q: "Escreve o número: dez", a: "10" },
            { t: "choice", q: "Dez unidades formam uma...", options: ["dezena", "dúzia"], a: 0 },
            { t: "choice", q: "Qual é o maior: 7 ou 9?", options: ["7", "9"], a: 1 }
          ]},
          { id: "n2", titulo: "Somar e subtrair até 10", questoes: [
            { t: "input", q: "6 + 1 = ?", a: "7" },
            { t: "input", q: "5 + 4 = ?", a: "9" },
            { t: "input", q: "8 + 2 = ?", a: "10" },
            { t: "input", q: "9 − 1 = ?", a: "8" },
            { t: "input", q: "10 − 4 = ?", a: "6" },
            { t: "input", q: "7 − 3 = ?", a: "4" }
          ]}
        ]}
      ]
    },
    {
      id: "por-1c", disciplina: "Português", classe: "1ª classe", tag: "POR",
      units: [
        { id: "u1", titulo: "Escola: cumprimentar e identificar-se", niveis: [
          { id: "n1", titulo: "Cumprimentar e despedir-se", questoes: [
            { t: "choice", q: "É de manhã. Que cumprimento usas?", options: ["Bom dia!", "Boa noite!"], a: 0 },
            { t: "choice", q: "É de tarde. Que cumprimento usas?", options: ["Boa tarde!", "Bom dia!"], a: 0 },
            { t: "choice", q: "Vais dormir. O que dizes à mãe?", options: ["Boa noite, mãe!", "Bom dia, mãe!"], a: 0 },
            { t: "choice", q: "\"Como estás?\" — qual é a resposta correcta?", options: ["Eu estou bem, obrigado.", "Adeus, até amanhã."], a: 0 },
            { t: "choice", q: "Vais-te embora da escola. O que dizes?", options: ["Adeus, meninos!", "Bom dia, meninos!"], a: 0 },
            { t: "input", q: "Completa: \"Adeus, senhora professora, até ___!\"", a: "amanhã" }
          ]},
          { id: "n2", titulo: "Identificar-se e a escola", questoes: [
            { t: "choice", q: "\"Eu chamo-me Rosa. E tu, como te chamas?\" — como respondes ao apresentares-te?", options: ["Eu chamo-me...", "Bom dia!"], a: 0 },
            { t: "choice", q: "Quem ensina os alunos na sala de aula?", options: ["A professora", "A guarda"], a: 0 },
            { t: "choice", q: "Quem cuida da limpeza da escola?", options: ["A servente", "A directora"], a: 0 },
            { t: "choice", q: "Quem dirige a escola?", options: ["A directora", "A aluna"], a: 0 },
            { t: "match", q: "Liga cada pessoa à sua função na escola.", pairs: [["Professora", "Ensina na sala de aula"], ["Directora", "Dirige a escola"], ["Servente", "Limpa a escola"], ["Guarda", "Protege a escola"]] }
          ]}
        ]},
        { id: "u2", titulo: "Escola: tamanho e posição", niveis: [
          { id: "n1", titulo: "Grande, pequeno, magro, gordo", questoes: [
            { t: "choice", q: "🐈 gato magro e 🐈‍⬛ gato gordo. Marca o gato magro — qual é?", options: ["O primeiro", "O segundo"], a: 0 },
            { t: "choice", q: "Um pau grosso e um pau fino. Qual pintas se pedirem o grosso?", options: ["O grosso", "O fino"], a: 0 },
            { t: "choice", q: "Um lápis comprido e uma cana curta. Qual é comprido?", options: ["O lápis", "A cana"], a: 0 },
            { t: "choice", q: "Uma bola menor e um pato maior. Marca o maior — qual é?", options: ["A bola", "O pato"], a: 1 },
            { t: "choice", q: "Um objecto pesado e um objecto leve. Qual é mais fácil de levantar?", options: ["O pesado", "O leve"], a: 1 }
          ]},
          { id: "n2", titulo: "Dentro, fora, perto, longe", questoes: [
            { t: "choice", q: "\"Nós estamos dentro da escola.\" — onde estão?", options: ["Dentro", "Fora"], a: 0 },
            { t: "choice", q: "\"Eu estou fora da escola.\" — onde está?", options: ["Dentro", "Fora"], a: 1 },
            { t: "choice", q: "\"Eu estou perto da carteira.\" — a que distância está?", options: ["Perto", "Longe"], a: 0 },
            { t: "choice", q: "\"Nós estamos longe da carteira.\" — a que distância estão?", options: ["Perto", "Longe"], a: 1 },
            { t: "choice", q: "O vaso está em cima da carteira. Onde está o vaso?", options: ["Em cima", "Em baixo"], a: 0 }
          ]}
        ]},
        { id: "u3", titulo: "As vogais: i, u, o", niveis: [
          { id: "n1", titulo: "A vogal i", questoes: [
            { t: "choice", q: "Qual destas letras é a vogal i?", options: ["i", "u"], a: 0 },
            { t: "choice", q: "IGREJA começa por qual vogal?", options: ["i", "e"], a: 0 },
            { t: "input", q: "Completa: (n)__ (menino pequeno, filho) → escreve a vogal que falta em \"f i lho\"", a: "i" },
            { t: "choice", q: "Qual destas é a letra I maiúscula?", options: ["I", "U"], a: 0 }
          ]},
          { id: "n2", titulo: "As vogais u e o", questoes: [
            { t: "choice", q: "UVA começa por qual vogal?", options: ["u", "o"], a: 0 },
            { t: "choice", q: "OVO começa por qual vogal?", options: ["o", "u"], a: 0 },
            { t: "input", q: "Completa: \"o vo\" (ovo) — falta a vogal", a: "o" },
            { t: "match", q: "Liga a letra maiúscula à minúscula.", pairs: [["U", "u"], ["O", "o"]] }
          ]}
        ]},
        { id: "u4", titulo: "As vogais: e, a — consolidação", niveis: [
          { id: "n1", titulo: "As vogais e e a", questoes: [
            { t: "choice", q: "ESCOLA começa por qual vogal?", options: ["e", "a"], a: 0 },
            { t: "choice", q: "ANA começa por qual vogal?", options: ["a", "e"], a: 0 },
            { t: "input", q: "Completa: \"Am_lia\" (nome próprio) — falta a vogal", a: "é" },
            { t: "match", q: "Liga a letra maiúscula à minúscula.", pairs: [["E", "e"], ["A", "a"]] }
          ]},
          { id: "n2", titulo: "Consolidação das 5 vogais", questoes: [
            { t: "input", q: "Completa a sequência: a, e, __, o, u", a: "i" },
            { t: "choice", q: "Quantas vogais existem no total?", options: ["5", "7"], a: 0 },
            { t: "choice", q: "Qual destas letras NÃO é vogal?", options: ["m", "e"], a: 0 },
            { t: "input", q: "Escreve a vogal que falta: \"p_to\" (ave doméstica)", a: "a" },
            { t: "input", q: "Escreve a vogal que falta: \"m_u\" (o gato faz este som)", a: "ia" }
          ]}
        ]},
        { id: "u5", titulo: "A letra M", niveis: [
          { id: "n1", titulo: "As sílabas mi, mu, mo, me, ma", questoes: [
            { t: "choice", q: "M + A = ?", options: ["MA", "AM"], a: 0 },
            { t: "choice", q: "M + I = ?", options: ["IM", "MI"], a: 1 },
            { t: "choice", q: "M + O = ?", options: ["MO", "OM"], a: 0 },
            { t: "input", q: "Junta: M + U", a: "MU" },
            { t: "match", q: "Liga cada sílaba ao seu som.", pairs: [["MA", "mã"], ["MI", "mi"], ["MU", "mu"], ["MO", "mo"]] }
          ]},
          { id: "n2", titulo: "Palavras e frases com M", questoes: [
            { t: "choice", q: "MA + MÃ = ?", options: ["MAMÃ", "MÃMA"], a: 0 },
            { t: "input", q: "Junta as sílabas: MA + LA", a: "MALA" },
            { t: "input", q: "Junta as sílabas: MO + LA", a: "MOLA" },
            { t: "choice", q: "\"É a ___.\" (mãe) — como se escreve a palavra que falta?", options: ["mamã", "miau"], a: 0 },
            { t: "choice", q: "\"O ___ mia.\" — que animal faz este som?", options: ["miau", "mamã"], a: 0 },
            { t: "input", q: "Completa a frase: \"Eu amo a ___.\" (mãe)", a: "mamã" }
          ]}
        ]},
        { id: "u6", titulo: "A letra P", niveis: [
          { id: "n1", titulo: "As sílabas pi, pu, po, pe, pa", questoes: [
            { t: "choice", q: "P + A = ?", options: ["PA", "AP"], a: 0 },
            { t: "choice", q: "P + I = ?", options: ["IP", "PI"], a: 1 },
            { t: "choice", q: "P + O = ?", options: ["PO", "OP"], a: 0 },
            { t: "input", q: "Junta: P + U", a: "PU" },
            { t: "match", q: "Liga cada sílaba ao seu som.", pairs: [["PA", "pá"], ["PI", "pi"], ["PU", "pu"], ["PO", "po"]] }
          ]},
          { id: "n2", titulo: "Palavras com P e M", questoes: [
            { t: "input", q: "Junta as sílabas: PA + TO", a: "PATO" },
            { t: "input", q: "Junta as sílabas: PI + PA", a: "PIPA" },
            { t: "input", q: "Junta as sílabas: MA + PA", a: "MAPA" },
            { t: "choice", q: "Qual destas é uma palavra de verdade?", options: ["PATO", "TOPA"], a: 0 },
            { t: "choice", q: "O animal pequeno que sai do ovo da galinha é o...", options: ["pinto", "pato"], a: 0 }
          ]}
        ]},
        { id: "u7", titulo: "As letras T e L", niveis: [
          { id: "n1", titulo: "As sílabas com T", questoes: [
            { t: "choice", q: "T + A = ?", options: ["TA", "AT"], a: 0 },
            { t: "choice", q: "T + I = ?", options: ["IT", "TI"], a: 1 },
            { t: "input", q: "Junta: T + E", a: "TE" },
            { t: "choice", q: "TIA começa pela sílaba...", options: ["TI", "TA"], a: 0 }
          ]},
          { id: "n2", titulo: "As sílabas com L", questoes: [
            { t: "choice", q: "L + A = ?", options: ["LA", "AL"], a: 0 },
            { t: "input", q: "Junta: L + I", a: "LI" },
            { t: "input", q: "Junta as sílabas: LU + A", a: "LUA" },
            { t: "input", q: "Junta as sílabas: TE + LA", a: "TELA" },
            { t: "choice", q: "BOLA termina na sílaba...", options: ["LA", "BO"], a: 0 }
          ]}
        ]}
      ]
    }
  ]
};
