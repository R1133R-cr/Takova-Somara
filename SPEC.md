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

> **Feito na 0.28.0.** 36 medalhas: 10 de escola, 4 de consistência e 24
> dos jogos. O que se decidiu ao escrever está no fim da secção.

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

### O que se decidiu ao escrever

- **Três das nove ideias do quadro ficaram de fora**, e é a limitação a
  registar: «primeira peça especial no Pomar», «Sopa sem uma letra errada» e
  «Crossmath difícil à primeira» precisam de contadores que os jogos ainda
  não guardam. As restantes seis famílias de condição saem de dados que já
  existiam. Entram quando o §4 (a Sorte) instrumentar os jogos — é o mesmo
  rastreio.
- **Em vez do golden, a faixa é varrida nos três tamanhos com o título mais
  comprido que existe.** Um golden fixa píxeis e parte-se a cada afinação de
  cor; o que aqui interessa é que o texto de «Uma disciplina do princípio ao
  fim» não saia do ecrã de 320. Há também um teste que prova a promessa do
  §2 — que um toque atrás da faixa continua a chegar ao botão que lá está.
- **Ao arrancar, avaliam-se as condições sem mostrar nada.** Quem já tinha
  meia classe feita quando esta versão chegou recebe as medalhas e os
  cristais que merecia, mas não leva com vinte faixas seguidas na cara.
- **A primeira unidade paga por dois caminhos**, e são dois de propósito: o
  marco do §6 paga a unidade *sem erros*, a medalha paga a *primeira*
  unidade. Uma primeira unidade perfeita vale 2 CC, no momento em que a
  criança mais precisa de sentir que aquilo dá alguma coisa.
- **Vinte e três das trinta e seis não pagam nada.** Uma medalha que paga
  sempre deixa de ser medalha e passa a salário.
- **A pista fica à vista mesmo depois de ganha.** Antes diz o que falta
  fazer; depois explica o que se fez.
- **Som novo, sintetizado** (`tools/sons.py`, `conquista()`). Distingue-se do
  som de nível pela forma e não pelo volume — sobe duas vezes e assenta num
  acorde maior. É a mesma criança na mesma sala, e uma fanfarra que
  sobressalte não festeja nada.
- **A faixa vive no `builder` do `MaterialApp`**, por cima do Navigator.
  Metida dentro de um ecrã não apareceria nas lições nem nos joguinhos, que
  é justamente onde as conquistas se ganham.

---

## 3. Tempo de jogo

> **Feito na 0.26.0.** Os valores propostos ficaram todos como estavam.
> Três pormenores foram decididos na escrita — ver o fim da secção.

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

### O que se decidiu ao escrever

- **A nuvem funde os dois números, não o saldo.** O plano dizia «o saldo
  sincroniza pelo maior». Ficar pelo maior *saldo* dava um buraco: jogar dez
  minutos, entrar na conta noutro aparelho, e os dez voltavam — o tecto
  diário passava a ser uma sugestão. Fica pelo maior o que se **ganhou** e
  pelo maior o que se **gastou**. O objectivo declarado («nunca se perde
  tempo ao trocar de telemóvel») cumpre-se para o tempo ganho a estudar, que
  é o que a criança trabalhou para ter.
- **O nível perfeito rende oito, não treze.** Os +8 substituem os +5; não se
  somam. A tabela podia ler-se das duas maneiras.
- **`inactive` não pára o relógio.** Só `paused`, `hidden` e `detached`. É a
  mesma linha que a música já usava, e pela mesma razão: a sombra do
  multitarefas e a barra de notificações meio aberta são transitórias, e o
  `resumed` que devolveria o relógio nem sempre chega.
- **Dentro do jogo o aviso só aparece no último minuto**, e ao acabar fica
  1,5 s a dizer porquê antes de fechar. Um relógio sempre à vista põe a
  criança a olhar para o tempo em vez de jogar; um jogo que desaparece sem
  explicação lê-se como avaria.
- **Um sítio só liga os jogos ao relógio.** O `RelogioDeJogo` envolve o que o
  botão dos Joguinhos abrir, e não os quatro ecrãs um a um: assim um quinto
  joguinho não pode nascer sem contar tempo.
- **O ciclo de vida saiu do `main.dart` para `services/ciclo_de_vida.dart`.**
  Enterrada num `State` privado, a ligação não tinha teste nenhum —
  apagavam-se-lhe duas linhas e a suite continuava verde com o relógio a
  correr de app fechada.

---

## 4. Sorte — a ajuda que se ganha a estudar

> **Feito na 0.29.0**, na Sopa e no Pomar. O que se decidiu ao escrever está
> no fim da secção.

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

### O que se decidiu ao escrever

- **A campanha semanal ainda não paga sortes**, porque não existe (§5). A
  única porta viva é a lição sem um único erro. A tabela fica como está e a
  segunda linha liga-se quando o §5 chegar.
- **A composição é uma jogada possível por tocar.** «Sete mangas em T» tem de
  virar algo que o código saiba encontrar: são as duas casas a trocar mais as
  casas que se juntariam. O `jogadasPossiveis()` é o `haJogada()` a dizer
  *quais* em vez de *se há*, e um teste exige que os dois nunca discordem —
  senão a Sorte diria «não há nada» num tabuleiro jogável.
- **Empates resolvem-se sempre da mesma maneira**: na Sopa fica a palavra
  mais comprida, no Pomar a composição maior. Sem um desempate fixo, dois
  telemóveis com o mesmo tabuleiro davam ajudas diferentes, e uma ajuda
  arbitrária não se percebe.
- **A fronteira das duas reacções do Pomar são cinco jogadas** [era proposto].
  Acima disso vibra, que é o que ensina; daí para baixo nasce um **embrulho**
  na peça que ela teria de mover — com duas jogadas no bolso, uma dica não
  salva ninguém. Um teste garante que a peça especial não estraga a jogada
  que estava a apontar.
- **Uma sorte que não encontra nada não se cobra.** Acontece pouco — uma sopa
  em que só falta a palavra por onde o dedo já passou — e cobrar por uma
  ajuda que não ajudou seria roubo.
- **O botão nunca desaparece**, mesmo com zero, e tocá-lo aí diz como se
  ganham. Escondê-lo tirava a existência da ajuda a quem nunca a teve, que é
  justamente quem precisa de saber que ela existe.
- **Na Sopa a palavra pisca e apaga-se, deixando a primeira letra marcada.**
  Deixá-la acesa era dá-la de bandeja; apagá-la sem rasto era gastar uma
  sorte por dois segundos de memória.
- **Duas medalhas do §2 entraram aqui**: «a tua primeira peça especial» e
  «sopa sem falhar uma letra». Da previsão anterior — de que as três
  entrariam com este passo — só estas duas se cumprem, e não pelo rastreio:
  precisaram de contadores próprios nos dois jogos. A do Crossmath continua
  por fazer, porque o Crossmath não foi tocado nesta fase.

---

## 5. Campanha semanal

> **Feito na 0.30.0.** Reutilizou-se o `lesson_screen` com `avulsas`, como o
> plano previa em alternativa. O que se decidiu ao escrever está no fim.

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

### O que se decidiu ao escrever

- **10 a 20 perguntas, não 15 a 20.** O mínimo desceu porque uma criança que
  fez dois níveis na semana passada tem quinze perguntas ao todo, e exigir
  quinze *depois* de tirar as repetidas deixava-a sem campanha nenhuma
  justamente na semana em que ela começou. Abaixo de dez não há campanha:
  prometer um desafio semanal e dar dois minutos de trabalho gasta a palavra
  por nada.
- **Os erros ficam por metade do máximo.** Uma criança com trinta erros por
  rever teria uma campanha só de erros e nunca reveria a matéria nova. O
  limite não morde quando não há matéria nova — aí os erros enchem o resto.
- **Faltava a data de cada nível.** O `progresso` guardava a nota e não o
  dia, e sem dia não há maneira de saber o que se estudou *na semana
  passada*. Entrou o `_estudadoEm`, que sincroniza ficando com a data mais
  recente de cada nível.
- **Recua no máximo duas semanas.** Se a semana passada não deu nada, tenta a
  anterior e pára. Puxar de um mês atrás já não é rever, é começar outra vez.
- **Gera-se uma vez por semana e não a cada toque.** Uma campanha que se
  refizesse à quarta-feira deixava de ter prazo, que é a única coisa que a
  define. O `_semanaVerificada` guarda que já se procurou material nesta
  semana, mesmo quando não se encontrou nenhum.
- **Uma ou duas sortes, e o degrau do meio é a 10% de erro.** «1 ou 2» ficava
  por decidir; duas para quem acertou quase tudo faz o esforço de acertar
  tudo valer mais do que o de passar à tangente.
- **Paga uma vez por semana.** Refazer a campanha não volta a pagar, e tê-la
  feito noutro telemóvel conta aqui — senão bastava repeti-la cinco vezes
  para encher as sortes.
- **O aviso é uma marca dourada no separador Praticar**, ao lado da vermelha
  dos Guardados. É onde o cartão vive, e é o primeiro da lista: enterrado
  debaixo do treino, passava a semana sem se ver.

---

## 6. Moedas e loja do Roby

> **Feito na 0.27.0.** Os preços e as regras de ganho ficaram como estavam
> propostos. O que se decidiu ao escrever está no fim da secção.

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

*(1 a 3 ficaram todos em `test/loja_test.dart`, um ficheiro só — são a mesma
funcionalidade e partem-se juntos.)*

### O que se decidiu ao escrever

- **23 poses à venda, não 24.** Copiaram-se 14 caras e 9 poses de corpo
  inteiro. Ficaram de fora as variantes `_b` e `_c` de expressões que a app
  já tem (orgulhoso, confuso, agradecido) — vender à criança uma segunda
  versão de uma cara que ela já tem não é colecção, é ruído. **+28,7 MB de
  assets**, ao abrigo da regra do `CLAUDE.md`.
- **Descodificação, não redimensionamento.** Os ficheiros são de 1254 px e
  ficam como estão. O que se acrescentou foi o `RobyImagem`, que descodifica
  ao tamanho do ecrã: uma grelha da loja com vinte poses em tamanho real
  mandava mais de cem megabytes de bitmap para a memória de um telemóvel de
  mil meticais. É um problema de memória em uso, não de peso do APK.
- **O ganho e o gasto guardam-se separados**, como na bolsa de tempo, e a
  nuvem funde os quatro totais pelo maior. Ficar pelo maior saldo dava a
  quem tivesse dois telemóveis uma máquina de cristais.
- **Os marcos já pagos ficam num conjunto.** `unidade:mat-1c:u1`,
  `semana:3`. Sem isso, refazer a última lição de uma unidade perfeita era
  um cristal de cada vez, e a criança que descobrisse isso nunca mais
  estudava. O conjunto serve também as conquistas do §2.
- **Um relógio só no `AppState`.** A sequência lia `DateTime.now()` e o marco
  da semana lia o relógio injectável: com um relógio falso as duas datas
  estavam em anos diferentes e o cristal da semana nunca chegava.
- **Não se vendem minutos com a bolsa no tecto do dia** — a compra é recusada
  com a razão escrita, e o dinheiro fica onde estava. Vender tempo que o
  tecto ia deitar fora seria vender nada; deixar a compra furar o tecto
  seria desfazer o §3.
- **Comprar uma cara veste-a logo**, e um segundo toque despe-a. Comprar e
  não ver nada mudar era o pior momento possível para pedir mais um toque.
- **A porta da loja está no Perfil**, com a carteira à vista. Não se
  acrescentou nada à barra de estado: com corações, XP, sequência e classe,
  a 320 dp já não cabe mais nada.
- **Ainda não há conquistas a pagar cristais** (§2 não existe). As duas
  fontes vivas são a unidade perfeita e cada sete dias seguidos.

---

## 7. Pomar — aleatoriedade honesta

> **Feito na 0.32.0.** O solucionador encontrou o defeito para que existia:
> **do nível 250 para cima o Pomar era impossível.** Ver o fim da secção.

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

### O que o solucionador encontrou

**Do nível 250 para cima, o Pomar era impossível.** O objectivo ia de 20 a
**140** peças e as jogadas de 25 a 12 — ou seja, quase doze peças por jogada
no último degrau. Uma jogada boa apanha cinco a sete. Medido com o jogador
guloso, que escolhe sempre a melhor troca visível:

| nível | objectivo | jogadas | ganhou |
|---|---|---|---|
| 100 | 59 | 21 | 10/10 |
| 250 | 96 | 17 | 6/10 |
| 500 | 125 | 14 | 2/10 |
| 750 | 136 | 12 | **0/10** |
| 1000 | 140 | 12 | **0/10** |

O tecto passou a **42**, que é o que um jogador guloso fecha em pouco mais de
metade das jogadas — deixando à criança a folga que ela precisa por não ser
uma máquina. Com isso, 10/10 em todos os degraus.

### Outros dois defeitos que apareceram pelo caminho

- **A escadaria pedia sete produtos e há seis.** Nada lia esse número, e por
  isso nada dava por ele; no dia em que o tabuleiro passasse a lê-lo, ia
  buscar um produto que não existe. Passou a 4→6, com um teste que o prende
  a quantos há.
- **O número de produtos só valia para o primeiro enchimento.** As peças que
  caíam a seguir vinham sempre das seis, e a baralhação também: um nível de
  quatro produtos passava a seis à primeira cascata, e a dificuldade do
  degrau desfazia-se sozinha na primeira jogada. O `produtos` passou a ser
  do **tabuleiro** e não de quem o cria.

### O que mais se decidiu

- **Não corre num isolate.** O §7 pedia-o «para não travar o ecrã»; mediu-se
  antes de o construir: gerar um tabuleiro provado dá ~1 ms, e o teste
  mantém-no abaixo dos 300 ms. Um isolate custava serializar o tabuleiro nos
  dois sentidos por uma latência que não existe.
- **O objectivo é o que fecha o nível, desde o degrau 1.** «Fazer muitos
  pontos» não é um objectivo que se possa provar ganhável, e sem isso não há
  solucionador nenhum a valer. Os pontos continuam à vista, mas o número que
  fecha o nível são as peças. A mecânica `objectivo` do §1 («objectivo em vez
  de pontos», marco 50) fica sem sentido próprio — o objectivo existe desde
  o princípio.
- **Ganhar sobe de degrau sozinho**, como na Sopa. **Perder não desce**: uma
  criança que falha o nível 40 tenta o 40 outra vez, e o painel do fim só
  aparece quando há mesmo uma decisão a tomar.
- **O placar passou a três números** — peças, pontos, jogadas — com as peças
  primeiro. Uma criança que olha para o número errado joga para o objectivo
  errado.

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

> **Feito na 0.31.0**, com as quatro. O desenho da subtracção aqui em baixo
> tem um erro de aritmética — está corrigido no código e explicado no fim
> da secção.

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

### O que se decidiu ao escrever

- **O desenho da subtracção do §9 está errado, e o código não o copiou.**
  Diz `5 ¹4 ¹3` para 643 − 287. As dezenas não valem 14: já tinham
  emprestado uma unidade às unidades antes de pedirem às centenas, e por
  isso valem 4 − 1 + 10 = **13**. Com 14 a conta não fecha. Há um teste que
  fixa o 13 e verifica que a ordem dá mesmo 5.
- **Não há botão de riscar.** O riscado é consequência do empréstimo, não
  uma decisão à parte: quem escreve o valor novo por cima já disse que
  aquela ordem mudou. Pedir as duas coisas era duas acções para uma ideia.
- **O modelo devolve a grelha inteira e o widget não sabe aritmética.**
  `GrelhaDaConta` diz que casinhas existem, onde ficam e o que devia estar
  em cada uma; o widget desenha. É o que permite testar as quatro operações
  em 4000 pares de números sem montar um ecrã.
- **Uma casinha de empréstimo leva dois algarismos** («13», «10») e só
  avança com os dois. Sem isso não havia maneira de a preencher.
- **O widget guarda o que se escreveu, em vez de o ler da propriedade.**
  Dois toques dentro do mesmo fotograma liam ambos o valor velho e o segundo
  algarismo apagava o primeiro — precisamente nas casinhas de empréstimo.
- **18 das 84 perguntas de aritmética viraram conta armada.** O critério é o
  do valor pedagógico e não o do número: **nada na 1ª classe** (aí aprendem-se
  os números até 20 e a ideia de juntar e tirar; a conta armada é matéria da
  2ª), nada com uma ordem só, e nada de `×10` ou `×100` — essas ensinam-se
  como regra, não como algoritmo, e armadas dariam duas linhas de zeros.
- **A conversão não obriga a regravar áudio.** O enunciado não muda: só muda
  a maneira de responder. O `--conferir` confirma os 1266 ficheiros.
- **A leitura do enunciado é verificada contra a resposta guardada.** Lê-se
  «Quanto é 48 : 6?», calcula-se, e compara-se com o que já lá estava. Se
  não bater, não se converte — foi assim que «Conta de 5 em 5: 5, 10, 15, ?»
  ficou de fora, apesar de ter dígitos e dois pontos.
- **Em vez do golden, a lição inteira é varrida nos três tamanhos com as
  quatro operações.** O risco não é a grelha sozinha: é a grelha mais o
  enunciado, mais o Roby, mais o teclado, na mesma coluna de 320 px. Uma
  conta que não caiba desliza na horizontal em vez de encolher abaixo dos
  44 px do alvo de toque.

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
