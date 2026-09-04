# SPEC — Progressão e gamificação da Somara

Especificação escrita a partir de uma entrevista, para ser implementada numa
sessão nova. **Nada disto está construído.** O que existe hoje está descrito na
secção «Ponto de partida», e serve para se ver o que é novo e o que é alteração.

Onde uma decisão foi tomada na entrevista, está marcada **[decidido]**. Onde eu
proponho um valor que ninguém escolheu, está marcada **[proposto]** — esses são
os que convém rever antes de construir.

---

## Ponto de partida — o que a app já tem

| | |
|---|---|
| Conteúdo | 21 cursos, 227 níveis, 1060 perguntas, 1266 ficheiros de áudio |
| Progressão | XP (10 por acerto), corações (5, repostos ao dia), sequência de dias |
| Mapa | «amarelinha» por disciplina — `map_screen.dart` |
| Exercícios | 5 tipos: `choice`, `input`, `match`, `drag`, `count` |
| Joguinhos | Crossmath, Pomar, Sopa de letras, Memória — sem níveis, sessão avulsa |
| Roby | 13 poses estáticas em `assets/img/`, mais 65 por usar em `Features/roby_assets 2.0/` |
| Voz | `pt-PT-RaquelNeural`, pré-gravada por `tools/audio.py` |

**A voz da Raquel É a voz do Roby** [decidido]. Não há voz separada nem se cria
uma nesta fase.

---

## 1. Escadaria dos jogos — nível 1 a 1000

**[decidido] Cada jogo tem a sua escadaria.** Não há nível global do aluno; o XP
e a amarelinha do currículo ficam como estão. Quatro escadarias independentes:
Crossmath, Pomar, Sopa, Memória.

### Como cresce a dificuldade

**[decidido] Parâmetros que apertam, mais mecânicas novas em marcos.**

A dificuldade tem duas camadas. A **base** cresce continuamente com uma função
suave; as **mecânicas** entram de 25 em 25 níveis [proposto] e nunca saem.

```
dificuldade(n) = base(n) + mecânicas(n)
base(n)        = 1 - exp(-n / 260)      # 0 → 1, cresce depressa no início
```

A escolha da curva importa: aos 100 níveis está a ~32% da dificuldade máxima,
aos 500 a ~85%, e do 700 ao 1000 quase não cresce. Uma criança que jogue muito
não bate num muro; uma que jogue pouco sente progresso desde cedo.

| jogo | parâmetro que cresce | do nível 1 | ao nível 1000 |
|---|---|---|---|
| Pomar | produtos distintos | 4 | 7 |
| | jogadas dadas | 25 | 12 |
| | objectivo (peças a colher) | 20 | 140 |
| Sopa | lado da grelha | 7 | 14 |
| | palavras escondidas | 4 | 10 |
| | direcções permitidas | 2 (→ ↓) | 8 (todas, incl. invertidas) |
| Crossmath | tecto dos números | 20 | 999 |
| | células em branco | 2 | 6 |
| | operações na grelha | + − | + − × : |
| Memória | pares | 4 | 12 |
| | tempo até virar de volta | 1,2 s | 0,5 s |

### Mecânicas por marco [proposto]

| nível | Pomar | Sopa | Crossmath | Memória |
|---|---|---|---|---|
| 25 | peças presas em gelo (2 colheitas) | palavras ao contrário | uma célula dá duas equações | cartas que só viram uma vez |
| 50 | objectivo em vez de pontos | grelha com buracos | número negativo no resultado | um par a três (trio) |
| 75 | peças que caem e tapam | palavra escondida por pista, não por lista | uma equação errada de propósito | cartas que trocam de sítio |
| 100 | tempo limitado, opcional | duas categorias misturadas | grelha 4×4 | duas cartas iguais que não são par |
| … | repete o ciclo com combinações | | | |

Do nível 100 em diante o gerador **combina** mecânicas já introduzidas em vez de
inventar novas — é o que dá variedade sem trabalho infinito.

### Ficheiros

- **novo** `lib/models/escadaria.dart` — a curva, a tabela de parâmetros por jogo,
  e `paramsPara(Jogo, int nivel)`
- **novo** `lib/models/mecanica.dart` — o `enum` das mecânicas e em que nível entram
- alterar `lib/models/pomar.dart`, `sopa.dart`, `crossmath.dart`, `memoria.dart` —
  os geradores passam a receber os parâmetros em vez de os terem fixos
- alterar `lib/state/app_state.dart` — guardar o nível de cada jogo
- alterar `lib/screens/joguinhos_screen.dart` — mostrar o nível em vez das
  dificuldades fixas («Fácil/Médio/Difícil» desaparece)

### Verificação ponta-a-ponta

1. `escadaria_test.dart`: para os 1000 níveis de cada jogo, os parâmetros ficam
   dentro dos limites e **nunca descem** ao subir de nível.
2. Para uma amostra de 50 níveis por jogo, gerar o tabuleiro e provar que é
   **resolvível** (ver §7 para o Pomar; a Sopa já tem `sopa_test.dart`).
3. No emulador: abrir cada jogo, ver o número do nível, jogar, ver o número subir.
4. Golden do ecrã dos joguinhos com os quatro níveis diferentes.

---

## 2. Conquistas

**[decidido] Três famílias**, e a de «descoberta» fica de fora:

| família | exemplos |
|---|---|
| **Marcos de estudo** | terminar uma unidade; terminar uma disciplina; terminar uma classe; nível sem erro nenhum; acertar uma pergunta que estava em Guardados |
| **Marcos dos jogos** | nível 10, 50, 100, 250, 500, 1000 de cada jogo; primeira peça especial no Pomar; Sopa sem uma letra errada; Crossmath difícil à primeira |
| **Consistência** | 3 dias seguidos; 1 semana; 1 mês; estudar antes de jogar 5 dias a fio |

### Como aparece — estilo Mario, não popup

**[decidido]** Uma faixa que **desliza de cima**, ocupa um terço do ecrã e
sai sozinha ao fim de ~3 s. Nunca pede «OK».

```
┌──────────────────────────────────────┐
│  [Roby com medalha]                  │   ← 02_expressoes_poses ou
│                                      │     01_icones_interface/13_roby_conquista
│  C O N Q U I S T A                   │   ← letra a letra, ~40 ms cada
│  Uma semana seguida!                 │
│  ★ +1 CC                             │
└──────────────────────────────────────┘
```

Som próprio (novo, em `tools/sons.py`), leve haptic, e o Roby entra a saltar. A
lição **não pára**: a faixa passa por cima e a criança continua.

### Histórico

**[decidido]** Ficam num histórico do aluno, no separador **Perfil**: uma grelha
de medalhas, as ganhas a cores e as por ganhar em silhueta com a pista do que
falta. É o mesmo sítio onde a colecção do Roby vai viver (§6).

### Ficheiros

- **novo** `lib/models/conquista.dart` — catálogo, condições, estado
- **novo** `lib/widgets/faixa_conquista.dart` — a faixa Mario
- **novo** `lib/screens/conquistas_screen.dart` — o histórico
- alterar `lib/state/app_state.dart` — avaliar condições e persistir
- alterar `lib/screens/perfil_screen.dart` — entrada para o histórico
- alterar `lib/services/nuvem.dart` — as conquistas sincronizam, e **nunca
  desaparecem** numa fusão (só se acrescentam, como o resto do progresso)

### Verificação ponta-a-ponta

1. `conquista_test.dart`: cada condição dispara uma vez e só uma; recarregar a
   app não volta a disparar.
2. Fusão na nuvem: um telemóvel com A e B, outro com B e C → ficam A, B e C.
3. Golden da faixa.
4. Emulador: terminar um nível sem erro, ver a faixa entrar e sair sem tocar.

---

## 3. Tempo de jogo

**[decidido] Bolsa diária pequena que o estudo enche.**

| | valor | |
|---|---|---|
| de graça, por dia | **10 min** | [proposto] |
| por nível de lição concluído | **+5 min** | [proposto] |
| por nível com 100% de acertos | **+8 min** | [proposto] |
| tecto diário | **60 min** | [proposto] — para a app não substituir a escola |
| quando acaba | os quatro joguinhos fecham; o estudo continua sempre aberto | |

O ecrã dos joguinhos mostra sempre os minutos que restam. Quando chegam a zero,
os cartões ficam apagados com uma linha: **«Estuda um nível e ganhas mais cinco
minutos.»** — com botão que leva ao mapa.

O relógio corre **só dentro de um jogo**, e pára ao sair, ao minimizar a app e
quando o ecrã se apaga. À meia-noite local repõe-se a bolsa de graça.

**O estudo nunca é bloqueado por isto.** Corações e tempo de jogo são coisas
separadas: os corações limitam os exercícios, o tempo limita os jogos.

### Ficheiros

- **novo** `lib/models/bolsa_de_tempo.dart` — saldo, ganhos, reposição diária
- alterar `lib/state/app_state.dart` — persistir e repor
- alterar `lib/screens/joguinhos_screen.dart` — mostrar saldo, fechar quando zero
- alterar os quatro ecrãs de jogo — arrancar e parar o relógio no `initState`/`dispose`
- alterar `lib/services/nuvem.dart` — o saldo sincroniza pelo **maior**, como o
  resto (nunca se perde tempo ao trocar de telemóvel)

### Verificação ponta-a-ponta

1. `bolsa_test.dart`: relógio falso — 10 min iniciais, gasta 4, resta 6; terminar
   nível dá +5; tecto trava aos 60; à meia-noite repõe.
2. O relógio **não corre** com a app minimizada (teste com `AppLifecycleState`).
3. Emulador: gastar a bolsa até zero, ver os cartões apagados e a mensagem,
   estudar um nível, ver os joguinhos reabrirem.

---

## 4. Sorte — a ajuda que se ganha a estudar

**[decidido, ideia do utilizador]** Um botão **«Sorte»** dentro dos jogos, que
mostra quantas estão disponíveis.

### O rastreio, comum aos dois jogos

O sistema segue o que a criança **tocou** durante o nível. Ao pedir sorte,
escolhe entre o que ela **não** tocou — porque é aí que ela está encalhada.

### O que a Sorte faz em cada jogo

**Sopa de letras** — revela a palavra menos tocada: as letras acendem por um
instante e apagam-se, deixando a primeira letra marcada.

**Pomar** — o sistema procura uma composição por tocar (por exemplo sete mangas
em T) e faz **uma de duas coisas** [decidido]:
- a composição **vibra**, a mostrar que é a peça essencial para acabar o nível; ou
- gera ali uma **peça especial** capaz de limpar aquela composição de uma vez.

Qual das duas depende de quantas jogadas restam [proposto]: com folga, vibra
(ensina); com poucas jogadas, dá a peça (salva).

**Crossmath e Memória** — sem Sorte nesta fase (§ fora do âmbito).

### Como se ganham

| acção | sortes |
|---|---|
| terminar uma lição **sem erros** | **1**, sempre |
| terminar a campanha semanal com menos de 30% de erro | **1 ou 2** |

**[proposto]** Tecto de 5 sortes acumuladas, para não se juntarem cinquenta e a
ajuda deixar de valer nada.

### Ficheiros

- **novo** `lib/models/sorte.dart` — saldo, ganhos, tecto
- **novo** `lib/models/rastreio.dart` — o que foi tocado no nível actual
- alterar `lib/models/pomar.dart` — achar composições por tocar
- alterar `lib/models/sopa.dart` — achar a palavra menos tocada
- alterar `pomar_screen.dart` e `sopa_screen.dart` — o botão e as animações
- alterar `lib/screens/lesson_screen.dart` — atribuir a sorte no fim de uma
  lição sem erros

### Verificação ponta-a-ponta

1. `sorte_test.dart`: lição sem erros dá exactamente 1; com um erro dá 0; o tecto
   trava aos 5.
2. `rastreio_test.dart`: num tabuleiro fabricado com uma composição intocada e
   outra tocada, a Sorte escolhe a intocada.
3. Emulador: acabar uma lição a 100%, ver o contador subir, entrar no Pomar,
   carregar em Sorte, ver a composição vibrar.

---

## 5. Campanha semanal

**[decidido]** Um conjunto de **15 a 20 perguntas** [proposto] gerado à
**segunda-feira**, disponível até domingo. Puxa de duas fontes:

- o que a criança **estudou** nessa semana;
- o que ela **errou** (a lista de Guardados).

Acabar com **menos de 30% de erro** dá 1 ou 2 sortes. É revisão espaçada
disfarçada de desafio, e é o único sítio da app com prazo.

Se a criança não estudou nada nessa semana, a campanha puxa da semana anterior;
se não houver nada, não aparece.

### Ficheiros

- **novo** `lib/models/campanha.dart` — geração, janela de datas, avaliação
- **novo** `lib/screens/campanha_screen.dart` (ou reutilizar `lesson_screen` com
  `avulsas`, que já serve exactamente para isto)
- alterar `lib/screens/home_shell.dart` — o aviso de campanha por fazer

### Verificação ponta-a-ponta

1. `campanha_test.dart`: com relógio falso, a campanha de segunda inclui o que se
   estudou na semana anterior; à segunda seguinte é outra; 29% de erro dá sortes,
   31% não dá.
2. Emulador: estudar três níveis, avançar o relógio para segunda, abrir a
   campanha e ver as perguntas certas lá.

---

## 6. Moedas e loja do Roby

**[decidido, ideia do utilizador] Duas moedas:**

| | nome | vale | compra |
|---|---|---|---|
| **GC** | Gold Coin | pouco | minutos de jogo |
| **CC** | Cristal Coin | muito | minutos e horas, assets do Roby, e músicas (trilhas futuras, para trocar o ambiente da app) |

### Como se ganham [decidido]

- **GC**: cada nível de lição concluído, **5 a 15** conforme os acertos [proposto]
- **CC**: só em marcos raros — unidade sem erros, semana seguida de estudo,
  conquista. Cerca de **1 CC por semana de trabalho a sério** [proposto]

### Preços [proposto]

| item | preço |
|---|---|
| +5 minutos | 20 GC |
| +30 minutos | 3 CC |
| expressão ou pose do Roby | 2 a 5 CC |
| trilha sonora (quando existirem) | 8 CC |

### O que está à venda — e o que existe mesmo

**Levantamento feito no repositório.** Os assets do Roby estão em
`Features/roby_assets 2.0/` — **78 PNGs, todos sem fundo**. A app usa **13**.

| pasta | ficheiros | serve para a loja? |
|---|---|---|
| `01_icones_interface/` | 35 | **em parte** — `13_roby_conquista` para a faixa; os restantes são ícones de UI, não colecionáveis |
| `02_expressoes_poses/expressoes/` | 27 | **sim, directamente** — pensativo, surpreso, zangado, assustado, determinado, tímido, cansado, nervoso, agradecido (3), confuso (2), orgulhoso (2), empático, inspirado, entediado, a piscar, sereno |
| `02_expressoes_poses/poses/` | 10 | **sim, directamente** — a estudar, a correr, a votar, a usar telemóvel, ideia brilhante, a ajudar colega, a dar boas-vindas, a liderar reunião, a formar-se |
| `03_character_sheet/` | 6 | **não** — são vistas de referência de ~2,5 MB, para desenhar, não para mostrar |

**Dá para construir a loja hoje, sem arte nova:** 37 expressões e poses
colecionáveis, das quais 24 nunca foram vistas na app. A mecânica é **troca de
asset inteiro** — a pose desbloqueada passa a aparecer no mapa, no perfil e no
fim das lições.

**O que precisaria de me fornecer, se quiser mais:**
1. **Acessórios sobrepostos** (chapéu, capulana, mochila, óculos) — PNGs
   transparentes **já alinhados** com `00_roby_pose_principal.png`, com o mesmo
   tamanho de tela e um ponto de ancoragem fixo. Sem isso não há sobreposição
   possível: o character sheet é um PNG achatado, sem camadas.
2. **Fundos** para o cartão do perfil, se quiser cenários a comprar.
3. **Trilhas sonoras** em `.mp3`, para a parte de música do CC.

**Nada disto exige rigging 3D nem modelo 3D** — não há e não é preciso.

### Ficheiros

- **novo** `lib/models/carteira.dart` — GC, CC, ganhos, gastos
- **novo** `lib/models/coleccao.dart` — que poses estão desbloqueadas
- **novo** `lib/screens/loja_screen.dart`
- alterar `lib/widgets/roby.dart` — o `enum RobyPose` cresce dos 13 para os 37,
  e passa a saber quais estão bloqueadas
- copiar os 24 PNGs de `Features/roby_assets 2.0/` para `assets/img/`
- alterar `lib/services/nuvem.dart` — carteira e colecção sincronizam

### Verificação ponta-a-ponta

1. `carteira_test.dart`: um nível a 100% dá o máximo de GC; comprar minutos tira
   GC e acrescenta tempo; comprar sem saldo é recusado.
2. `coleccao_test.dart`: cada pose à venda tem ficheiro no disco (o teste falha se
   alguém puser à venda uma pose que não existe).
3. Fusão na nuvem: colecções diferentes nos dois telemóveis → união, nunca perda.
4. Emulador: comprar uma pose, vê-la aparecer no fim da lição seguinte.

---

## 7. Pomar — aleatoriedade honesta

**[decidido] Sorteio limpo, com solução garantida.** Nada de afinar a favor nem
contra. Duas garantias, verificadas **antes** de o tabuleiro ser mostrado:

1. **há sempre pelo menos uma jogada possível** — já existe hoje, com baralhação
   automática quando não há;
2. **o nível é resolvível dentro das jogadas dadas** — um solucionador joga o
   tabuleiro por simulação antes de o entregar; se não fechar o objectivo em ≤80%
   das jogadas [proposto], sorteia-se outro.

O solucionador não precisa de ser óptimo — basta ser uma heurística gulosa que
prove que **um jogador razoável consegue**. Corre num isolate para não travar o
ecrã.

> A criança nunca perde por azar, e nunca ganha por pena. Numa app de escola,
> ensinar que o esforço conta é o que interessa.

### Ficheiros

- alterar `lib/models/pomar.dart` — `Pomar.gerar(nivel)` com as garantias
- **novo** `lib/models/pomar_solucionador.dart`

### Verificação ponta-a-ponta

1. `pomar_test.dart`: 200 tabuleiros sorteados em níveis espalhados — todos com
   jogada possível e todos resolvidos pelo solucionador.
2. Medir o tempo de geração: **< 300 ms** no pior nível, num telemóvel barato.
3. Emulador: jogar dez níveis seguidos sem encontrar um impossível.

---

## 8. Sopa de letras — progressão automática e banco moçambicano

> **Feito na 0.25.0.** A tabela e a lista de categorias abaixo foram
> actualizadas para os números que o código dá mesmo — ver a nota no fim
> da secção.

**[decidido] Sai o botão «jogar outra vez».** Ao encontrar a última palavra:
celebração curta (~1,5 s) e o **nível seguinte carrega sozinho**. Sai-se pela
seta de voltar, como em todo o lado.

### Banco de palavras [decidido: cresce com o nível, por categorias]

| nível | palavras | grelha |
|---|---|---|
| 1 | 4 | 7×7 |
| 25 | 5 | 8×8 |
| 100 | 6 | 9×9 |
| 300 | 8 | 12×12 |
| 600 | 10 | 13×13 |
| 1000 | 10 | 14×14 |

**Categorias, que rodam** — objectos concretos do quotidiano moçambicano:

| categoria | exemplos |
|---|---|
| Casa | lata, mesa, cama, porta, balde, esteira, candeeiro |
| Cozinha | panela, prato, colher, sal, arroz, óleo, farinha |
| Escola | livro, lápis, caderno, quadro, giz, mochila, régua |
| Mercado | banana, tomate, peixe, carvão, capulana, metical |
| Transporte | chapa, bicicleta, camião, barco, comboio, estrada |
| Animais | cabrito, galinha, vaca, cão, peixe, formiga |
| Corpo | mão, perna, cabeça, olho, dente, joelho |
| Campo | machamba, enxada, milho, mandioca, chuva, sol |
| Moçambique | Maputo, Beira, Nampula, Niassa, Tete, Lichinga, Pemba |

Regras do banco: **sem acentos** (a grelha é de maiúsculas simples), 3 a 10
letras, e nenhuma palavra repetida dentro do mesmo nível. A categoria de cada
nível é determinada pelo número do nível — o mesmo nível dá sempre a mesma
categoria, para dois telemóveis mostrarem o mesmo.

### Ficheiros

- alterar `lib/models/sopa.dart` — categorias, banco novo, parâmetros por nível
- alterar `lib/screens/sopa_screen.dart` — tirar o botão, encadear níveis

### Verificação ponta-a-ponta

1. `sopa_test.dart`: em 100 níveis sorteados, todas as palavras cabem na grelha e
   são encontráveis; nenhuma repetida; nenhuma com acentos.
2. O nível N dá sempre a mesma categoria (determinismo).
3. Emulador: acabar um nível e ver o seguinte entrar sem se tocar em nada.

### O que mudou entre o plano e o código

- **Nove categorias, não oito.** Entrou «Moçambique» — as províncias e as
  cidades. É a única em que a palavra ensina alguma coisa além de si mesma.
- **A grelha cresce mais depressa do que esta tabela dizia.** A tabela acima
  foi escrita à mão antes da curva existir; agora sai da [curva] do §1 e é
  esta. Nada se decidiu de novo — corrigiu-se a aritmética.
- **O ponto 3 também está coberto por teste.** O `sopa_ecra_test.dart`
  arrasta o dedo por cima de todas as palavras de um nível e confirma que o
  degrau sobe sozinho; o emulador passa a ser confirmação, não a única prova.

---

## 9. Exercício em grelha — as quatro operações

**[decidido] As quatro operações**, e **[decidido] a criança escreve também o
transporte**.

Este é o exercício mais pesado da especificação, e o que mais valor traz: passa a
treinar o **método** que a escola ensina, e não só a resposta.

### Adição

```
      ¹  ¹          ← casinhas do "vai um", preenchidas pela criança
      2  4  7
  +   1  8  5
  ─────────────
      4  3  2       ← casinhas do resultado, preenchidas pela criança
```

### Subtracção com empréstimo

```
      5  ¹4  ¹3     ← o dígito riscado e o emprestado por cima
      6  4  3
  −   2  8  7
  ─────────────
      3  5  6
```

O dígito de onde se empresta aparece **riscado** e o novo valor por cima, tal
como se faz no caderno.

### Multiplicação

Produtos parciais, um por linha, com o deslocamento à esquerda visível:

```
         2  4
  ×         1  3
  ──────────────
         7  2      ← 24 × 3
      2  4  ·      ← 24 × 1, deslocado
  ──────────────
      3  1  2
```

### Divisão

Disposição da chave, com abaixamentos:

```
     1  4  4  │  1  2
  −  1  2     │ ─────
  ─────────   │  1  2
        2  4  │
     −  2  4  │
     ─────────│
           0  │
```

**A divisão é a mais difícil das quatro** e deve ser a última a construir-se.

### Validação [decidido]

Ao carregar em Verificar:
- **verde** nos dígitos certos;
- **vermelho** nos errados;
- os transportes são validados **junto com** o resultado — errar o transporte e
  acertar o resultado conta como certo, mas o transporte fica assinalado.

### Regras de interface

- Uma casinha de cada vez, com cursor visível; o teclado numérico existente
  (`lib/widgets/teclado_numerico.dart`) serve, com um botão a mais para riscar.
- Preenche-se **da direita para a esquerda** — é a ordem do algoritmo. Saltar não
  é proibido, mas o cursor avança sozinho para a esquerda.
- Numa grelha de 4 dígitos, no telemóvel de 320 dp, cada casinha tem no mínimo
  **44×44 dp** (o alvo de toque mínimo). Acima de 5 dígitos a grelha desliza na
  horizontal em vez de encolher.
- O enunciado lido em voz alta continua a existir: a Raquel diz «duzentos e
  quarenta e sete mais cento e oitenta e cinco».

### Onde substitui a escolha múltipla

Em **Matemática**, nas perguntas cuja resposta é uma operação armada. As
perguntas de conceito («o perímetro de uma figura é:») ficam em escolha múltipla.

### Ficheiros

- alterar `lib/models/content.dart` — tipo de questão novo `grelha`, com
  operandos, operação e resultado esperado
- **novo** `lib/widgets/grelha_operacao.dart` — o desenho e a interacção
- **novo** `lib/models/algoritmo_escrito.dart` — calcula os transportes esperados,
  para os poder validar
- alterar `lib/screens/lesson_screen.dart` — encaminhar o tipo novo
- **novo** `tools/grelhas.py` — converter perguntas de Matemática existentes

### Verificação ponta-a-ponta

1. `algoritmo_test.dart`: para 1000 pares de números, os transportes calculados
   batem com o algoritmo escrito (comparados com uma implementação de referência).
2. `grelha_test.dart`: preencher certo dá tudo verde; um dígito errado dá esse a
   vermelho e os outros a verde.
3. `ecras_test.dart`: a grelha de 4 dígitos cabe em 320×640 sem transbordar.
4. Golden das quatro operações.
5. Emulador: resolver uma adição com transporte, de ponta a ponta.

---

## 10. Exercícios interactivos — Ciências Naturais e Sociais

**[decidido] As quatro famílias entram**, por esta ordem de construção:

### a) Arrastar para um cenário
Um fundo desenhado e peças para largar no sítio certo. É o mais versátil.
- **CN**: montar o circuito eléctrico (pilha, fios, lâmpada); montar a cadeia
  alimentar; pôr os órgãos no corpo; as partes da planta
- **CS**: marcar as províncias no mapa de Moçambique; pôr os rios no sítio

O cenário é **desenhado em código** (`CustomPainter`), como as figuras de
geometria e as manchas de cor já são — nasce dos dados, não de um ficheiro.

### b) Ordenar uma sequência
Arrastar passos para a ordem certa.
- **CN**: o ciclo da água; como se formam as montanhas; tratar a água para beber;
  da semente à planta
- **CS**: acontecimentos históricos por data; do menor ao maior na divisão
  administrativa (povoação → localidade → posto → distrito → província)

### c) Jogos de palavras do conteúdo
Sopa de letras e palavras cruzadas feitas com o **vocabulário da unidade que a
criança acabou de estudar** — os rios de Moçambique, os direitos da criança, as
partes da planta. Reaproveita a Sopa que já existe, com um banco vindo do
`content.json`.

### d) Classificar em grupos
Arrastar para caixas: vertebrado ou invertebrado; natural ou artificial; direito
ou dever; rural ou urbano; necessidade ou desejo.

### Ficheiros

- alterar `lib/models/content.dart` — tipos `cenario`, `sequencia`, `grupos`
- **novo** `lib/widgets/cenario_interactivo.dart`
- **novo** `lib/widgets/ordenar_passos.dart`
- **novo** `lib/widgets/classificar_grupos.dart`
- **novo** `lib/painters/` — os fundos desenhados (circuito, corpo, mapa)
- **novo** `tools/conteudo_interactivo.py`

### Verificação ponta-a-ponta

1. Um teste por tipo: largar certo → certo; largar trocado → errado.
2. `ecras_test.dart` nos três tamanhos para cada tipo.
3. Goldens do circuito e do mapa.
4. Emulador: montar o circuito eléctrico e ver a lâmpada acender.

---

## 11. Roby vivo

**[decidido]** A voz do Roby **é a da Raquel** e assim fica. Nada de voz nova.

### a) Animação entre poses
A troca de pose deixa de ser um corte: o Roby salta, roda ou encolhe-e-cresce
entre uma e outra. Feito por código sobre os PNGs que já existem — zero arte
nova.

### b) Reage ao que se faz
Muda de expressão em tempo real, com as 24 expressões por usar:

| momento | expressão |
|---|---|
| criança hesita >8 s | `pensativo` / `curioso` |
| 3 acertos seguidos | `empolgado` |
| 5 acertos seguidos | `orgulhoso_b` |
| resta 1 coração | `nervoso` |
| erro repetido na mesma pergunta | `empatico` |
| fim de sessão longa | `cansado` |
| campanha semanal por fazer | `a piscar` |

### c) Conquista estilo Mario
Ver §2.

### Ficheiros

- alterar `lib/widgets/roby.dart` — `RobyPose` cresce; animação de transição
- **novo** `lib/widgets/roby_reactivo.dart` — decide a expressão pelo estado
- copiar os PNGs em falta para `assets/img/`

### Verificação ponta-a-ponta

1. `roby_test.dart`: cada estado devolve a expressão esperada; toda a pose
   referida existe em disco.
2. Golden da faixa de conquista e de três transições.
3. Emulador: acertar três seguidas e ver o Roby mudar.

---

## 12. Ideias adoptadas

**[decidido] Entram três:**

### Corrida de cálculo rápido — quinto joguinho
Contas de cabeça contra o relógio, com tema local: o **chapa** que apanha
passageiros (somar), o **mercado** que dá troco (subtrair), o saco de arroz
dividido por famílias. Sessões de 60 s. Tem a sua escadaria como os outros.
- **novo** `lib/models/corrida.dart`, `lib/screens/corrida_screen.dart`

### Baú ao terminar um bloco
Ao acabar uma **unidade**, abre-se um baú com um prémio sorteado: GC, uma sorte,
ou uma expressão do Roby. Dá razão para acabar a unidade e não só o nível.
Sorteio **honesto e visível** — as probabilidades ficam escritas no código e num
teste.
- **novo** `lib/widgets/bau.dart`

### Modo aventura narrativo
Uma história que atravessa as disciplinas — o Roby a preparar uma viagem pelo
país, e cada disciplina dá uma peça. **É a que mais conteúdo novo exige** (texto,
ilustração e voz) e deve ser a **última** a construir-se.
- **novo** `lib/models/aventura.dart`, `tools/conteudo_aventura.py`

### Considerada e deixada de fora

**Mapa de Moçambique como trilha de progressão** — substituir a fita da
amarelinha pelo país, de Maputo ao Rovuma. Boa ideia, mas é a mudança visual mais
pesada da lista e mexe no ecrã que já funciona. Fica registada para uma fase
futura.

---

## Fora do âmbito desta fase

Escrito para não haver dúvida depois:

- **Ranking entre alunos.** O `ranking_screen.dart` fica como está. A trilha é
  pessoal; não se comparam crianças.
- **Compra com dinheiro real.** As CC ganham-se, não se compram. A porta fica
  aberta na arquitectura da carteira, mas não se constrói nada.
- **Sorte no Crossmath e na Memória.** Só Pomar e Sopa nesta fase.
- **Acessórios sobrepostos ao Roby.** Precisa de arte que não existe (ver §6).
- **Trilhas sonoras compráveis.** A carteira prevê o preço; os ficheiros não
  existem.
- **Modelo ou rigging 3D.** Não há e não é preciso: tudo é composição 2D.
- **Multiplicação e divisão na grelha antes de a adição e a subtracção estarem
  a funcionar no telemóvel de uma criança a sério.**
- **Mapa de Moçambique como trilha.**

---

## Ordem de construção sugerida

Cada linha é uma versão entregável, com APK e testes verdes.

| # | o quê | porquê primeiro |
|---|---|---|
| 1 | Escadaria + parâmetros por nível (§1) | tudo o resto pendura-se aqui |
| 2 | Bolsa de tempo (§3) | liga estudo a jogo, e é pequeno |
| 3 | Carteira GC/CC + baú (§6, §12) | dá sentido a terminar níveis |
| 4 | Conquistas + faixa Mario + histórico (§2) | é o que se vê e o que anima |
| 5 | Sopa: progressão automática e banco novo (§8) | jogo mais simples de converter |
| 6 | Sorte + rastreio (§4) e campanha semanal (§5) | dependem de 1 e 5 |
| 7 | Pomar: escadaria, mecânicas e solucionador (§7) | o mais pesado dos jogos |
| 8 | Grelha: adição e subtracção (§9) | o de maior valor pedagógico |
| 9 | Roby vivo (§11) e loja (§6) | polimento sobre o que já existe |
| 10 | Ciências interactivas (§10) | quatro tipos, um de cada vez |
| 11 | Grelha: multiplicação e divisão (§9) | os mais difíceis |
| 12 | Corrida de cálculo (§12) | jogo novo, independente |
| 13 | Modo aventura (§12) | exige conteúdo novo em quantidade |

---

## Regras que valem para tudo isto

Herdadas do que o repositório já pratica, e que a implementação deve respeitar:

1. **O tamanho do APK não é critério** (ver `CLAUDE.md`). O custo dos **dados em
   uso** continua a ser.
2. **Todo o áudio novo passa por `tools/audio.py`**, que aplica as regras de
   pronúncia. O `compilar.sh` recusa-se a compilar se algum ficheiro estiver
   desactualizado.
3. **Cada ecrã novo entra no `ecras_test.dart`**, nos três tamanhos — 320×640 é o
   Android barato que ainda se vende em Moçambique.
4. **Nada que se sincronize pode encolher numa fusão.** Conquistas, colecção,
   carteira e níveis dos jogos juntam-se pelo maior, como o progresso já faz.
5. **Ortografia anterior ao Acordo de 1990**, como o resto do conteúdo.
6. **Cada funcionalidade tem um passo de verificação no emulador**, e não só
   testes — três das últimas versões tiveram defeitos que só se viam a olhar.
