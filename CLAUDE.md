# Regras deste repositório

## Tamanho do APK não é critério

**Não limitar assets, animações nem funcionalidades por causa do tamanho do
APK.** A prioridade é cobrir bem as necessidades de quem usa a app, mesmo que
isso a faça crescer.

Em concreto, nenhuma destas é razão válida para dizer que não:

- «o áudio ficaria pesado» — grava-se o áudio todo;
- «essa animação acrescenta megabytes» — faz-se a animação;
- «esse pacote engorda o APK» — usa-se o pacote se ele servir;
- «já vamos em X MB» — continua-se.

A optimização de tamanho fica para uma fase de lançamento futura, e será
decidida nessa altura. Até lá, não se corta nada por antecipação.

Isto **não** revoga duas coisas que continuam de pé, porque são outro
problema:

- **O custo dos dados de quem usa a app.** Em Lichinga paga-se ao megabyte, e
  isso vale para o que a app transfere *em uso* — sincronização, conteúdo
  remoto. Ver `lib/services/nuvem.dart`. O download único do APK é uma coisa;
  uma app que consome dados todos os dias é outra.
- **A fragilidade de cada dependência nova.** Um pacote a mais é mais uma
  coisa que pode partir numa actualização. Esse continua a ser um bom motivo
  para hesitar — o peso já não é.

O `compilar.sh` continua a dizer quantos MB tem o APK, e a dividir por
arquitectura quando se lhe pede (`./compilar.sh release abi`). Isso é
informação e é uma opção de entrega — não é um limite.
