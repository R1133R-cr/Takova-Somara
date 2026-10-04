# As personagens da Somara

Isto não é uma nota interna: é a **encomenda de quem vai desenhar**. Cada
ficha traz o que faz falta para desenhar a personagem sem perguntar nada —
espécie, história, carácter, roupa, objectos, cores — e o que faz falta para
a escrever sem a trair: como fala, o que diz quando a criança acerta e
quando erra, e o que nunca faz.

Os desenhos ainda não existem. As fichas vêm primeiro de propósito: um
desenho feito antes de se saber quem é a personagem fica bonito e fica
errado, e depois já custa dinheiro mudá-lo.

## A espinha: a viagem da matilha do Roby

Um **capítulo por classe**. O Roby e a matilha atravessam o país de classe
em classe, e em cada uma há mais alguém que sabe uma coisa que eles não
sabem.

- **1ª à 3ª classe** — só o Roby. Nesta idade a criança está a aprender a
  ler e a contar, e três personagens novas em cada ecrã seriam ruído. O
  nível final de cada classe é uma história só, que junta tudo.
- **4ª classe em diante** — entram os **professores-animais**, um por
  disciplina. Aparecem na disciplina deles e em mais nenhuma.
- **Quem platina** — quem fecha uma classe a cem por cento — abre o
  **caderno do avô**, um capítulo a mais que não se compra nem se desbloqueia
  por anúncio.

## O elenco

| Personagem | Espécie | Onde entra | Ficha |
|---|---|---|---|
| **Roby** | mabeco | em toda a app, da 1ª à 9ª | [roby](roby.md) |
| **Mestre Escamas** | pangolim | Matemática | [escamas](escamas.md) |
| **Avó Coruja** | coruja | Português | [coruja](coruja.md) |
| **Lolo** | camaleão | Ciências Naturais, Biologia | [lolo](lolo.md) |
| **Avô Nzou** | elefante | Ciências Sociais, História | [nzou](nzou.md) |
| **Dona Águia** | águia-pesqueira | Geografia | [aguia](aguia.md) |
| **Andorinha** | andorinha | Inglês | [andorinha](andorinha.md) |
| **Garça Nyanja** | garça-branca | Francês | [garca](garca.md) |
| **Eco** | morcego | Física | [eco](eco.md) |
| **Tia Formiga** | formiga | Química | [formiga](formiga.md) |
| **Pintinha** | borboleta | Educação Visual, e Visual e Ofícios | [pintinha](pintinha.md) |
| **Impala Veloz** | impala | Educação Física | [impala](impala.md) |
| **Mãe Galinha-do-mato** | galinha-do-mato | Agropecuária | [galinha](galinha.md) |
| **Tecelã** | aranha | TIC | [tecela](tecela.md) |
| **Hiena Ri-Ri** | hiena | nas histórias, de capítulo em capítulo | [riri](riri.md) |

Catorze animais e um protagonista, para dezasseis disciplinas. Três
partilhas, e cada uma tem razão:

- **Lolo** faz as Ciências Naturais do primário *e* a Biologia do
  secundário, porque é a mesma matéria a crescer.
- **Avô Nzou** faz as Ciências Sociais *e* a História, pela mesma razão.
- **Pintinha** faz a Educação Visual e a Educação Visual e Ofícios, que são
  o mesmo nome em duas fases do currículo.

O Inglês e o Francês **não** se partilham, e isto foi discutido: na 8ª e na
9ª classe o aluno tem as duas disciplinas no mesmo ano, e a mesma ave nas
duas lê-se como descuido e não como ideia. Por isso há uma andorinha e uma
garça — as duas viajantes, cada uma com a sua.

## Regras que valem para todas

Estas não se negociam por personagem. São o que faz a app ser de escola e
não de rede social.

1. **Nenhuma ri de um erro da criança.** Nenhuma, em nenhum momento. A
   Hiena Ri-Ri ri de tudo e de si própria — da criança, nunca; é o fio da
   história dela, e está explicado na ficha.
2. **Nenhuma dá a resposta.** Dão o caminho: o que olhar, por onde começar,
   o que já se sabe que ajuda. A resposta é da criança.
3. **Nenhuma fala da escola como castigo**, nem trata estudar como preço a
   pagar para jogar.
4. **Nenhuma diz à criança que não sabe, nem que é lenta.** Não existem as
   palavras «burro», «fácil» («isto é fácil» diz à criança que o problema é
   ela) nem «outra vez» em tom de queixa.
5. **Falam português de Moçambique**, e tratam a criança por tu.
6. **As falas são curtas.** Duas linhas num ecrã de 320 px de largura —
   cerca de 90 caracteres. O que não cabe, não se diz.
7. **São todas bichos destas terras.** Nenhum animal que uma criança do
   Niassa não possa ver, ou de que não possa ouvir falar em casa.
8. **Têm todas um defeito**, e o defeito aparece. Uma personagem que só
   acerta não ensina nada a quem erra.

## Quando os desenhos chegarem

Os ficheiros entram em `assets/img/` com este nome:

```
personagem-<slug>-<pose>.png
```

O `slug` é o nome do ficheiro da ficha (`escamas`, `coruja`, `lolo`…). As
quatro poses que fazem falta a todas, por esta ordem de prioridade:

| pose | quando aparece |
|---|---|
| `neutro` | a apresentar-se, e nos sítios onde só faz falta a cara |
| `a-explicar` | na matéria, ao lado da aula |
| `a-animar` | quando a criança acerta |
| `a-pensar` | quando a criança erra — a pensar *com* ela, nunca a julgar |

O Roby já tem trinta e oito poses em `assets/img/roby-*.png` e não segue
este nome: fica como está, porque mudar o nome dos ficheiros dele obrigava a
mexer em meia app para não ganhar nada.

O nome de cada personagem vive em [`lib/models/personagens.dart`](../../lib/models/personagens.dart),
e há um teste que não deixa entrar uma disciplina nova sem personagem. Até
os desenhos existirem, nada disto aparece no ecrã — mostrar o Mestre Escamas
com a cara do Roby ensinaria a criança a ligar o nome à cara errada, e isso
depois não se desfaz.

## O que falta decidir

- **Os nomes nas línguas do Niassa.** «Nzou» é elefante em várias línguas
  bantu da região e «nyanja» é lago, mas quem confirma isso são falantes de
  yao, de nyanja e de macua — não eu. Se os colegas professores preferirem
  outros nomes, trocam-se: as fichas é que são o trabalho, os nomes mudam-se
  numa linha.
- **A voz.** Para já a app tem uma voz só, a mesma em tudo
  (`pt-PT-RaquelNeural`). Dar voz própria a catorze personagens é outra
  conversa, e grande.
