# -*- coding: utf-8 -*-
"""O curso de Educacao Fisica da 8a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Educacao Fisica -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024,
     8a classe, pp. 23-32. Guardado em Documents\\planos da 5a classe\\
     Livros\\Programas INDE 1o Ciclo\\educacao-fisica.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As cinco unidades da 8a, pela ordem do plano tematico
-----------------------------------------------------
    I    Dancas e Jogos Educativos   jogos tradicionais; dancas e
                                     coreografia
    II   Ginastica                   capacidades motoras; salto a corda;
                                     ginastica artistica de solo
    III  Atletismo                   resistencia; estafetas; salto em
                                     comprimento
    V    Basquetebol                 ataque; defesa; regras
    VI   Futebol                     desmarcacao, proteccao de bola, jogo

(A numeracao salta o IV porque o programa numera as unidades de todo o
ciclo e o Andebol, que e a IV, e da 7a.)  A tabela da p. 23 distribui
as cinco pelos tres trimestres, com a Ginastica e as Dancas a
repetirem-se.

Cinco unidades, nove aulas.

O que se pergunta
-----------------
Educacao Fisica e correr e jogar, e uma app nao corre. Pergunta-se o
que o corpo precisa de saber antes: as regras, a tecnica, a seguranca,
o que cada capacidade motora e. E o mesmo criterio da 7a.

Correr a partir de somara-flutter/:
    python tools/conteudo_edf8c.py            # so mostra
    python tools/conteudo_edf8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Educação Física — Ensino "
    "Secundário, 1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, 8ª "
    "classe, pp. 23-32. As cinco unidades temáticas e os conteúdos são do "
    "programa; os exercícios foram escritos a partir deles, porque um "
    "programa de ensino não traz exercícios e não há livro do aluno da 8ª "
    "classe publicado."
)

CURSO = {
    "id": "edf-8c",
    "disciplina": "Educação Física",
    "classe": "8ª classe",
    "tag": "EDF",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # I  Dancas e Jogos Educativos
        # ================================================================
        {
            "id": "u1",
            "titulo": "Danças e jogos educativos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Os jogos da comunidade",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Antes de jogar um jogo tradicional com "
                                 "a turma, quem o conhece deve:",
                            "options": [
                                "Explicar as regras de forma clara, para "
                                "todos perceberem",
                                "Começar a jogar sem dizer nada",
                                "Guardar as regras para si",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada jogo ao valor que ele "
                                 "trabalha.",
                            "pairs": [
                                ["Jogo em que só se ganha em equipa", "Ajuda mútua"],
                                ["Jogo em que se espera a vez", "Respeito"],
                                ["Jogo em que se aceita perder", "Tolerância"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Um jogo sobre poupar água ou apagar a "
                                 "luz é um jogo:",
                            "options": [
                                "De reflexão sobre a poupança",
                                "De força",
                                "Sem regras",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Nos jogos, rapazes e raparigas:",
                            "options": [
                                "Jogam juntos e com os mesmos direitos",
                                "Jogam sempre separados",
                                "Só os rapazes jogam",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de um jogo no campo, confere-se se "
                                 "o chão tem pedras ou buracos para:",
                            "options": [
                                "Prevenir acidentes",
                                "Ganhar mais depressa",
                                "Correr menos",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Danças tradicionais e coreografia",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma coreografia é:",
                            "options": [
                                "A sequência de passos e movimentos de uma "
                                "dança, montada de propósito",
                                "O nome do tambor",
                                "O lugar onde se dança",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para montar uma coreografia começa-se "
                                 "por:",
                            "options": [
                                "Aprender os passos básicos da dança",
                                "Fazer os passos mais difíceis",
                                "Escolher a roupa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Dançar ao ritmo do tambor desenvolve a:",
                            "options": [
                                "Coordenação motora e rítmica",
                                "Força dos braços apenas",
                                "Velocidade da corrida",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada dança à zona de Moçambique de "
                                 "onde vem.",
                            "pairs": [
                                ["Nhau", "Niassa e Tete"],
                                ["Mapiko", "Cabo Delgado"],
                                ["Xigubo", "Sul"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Dançar as danças da comunidade na "
                                 "escola serve para:",
                            "options": [
                                "Resgatar e guardar os valores culturais",
                                "Esquecer a tradição",
                                "Fazer barulho",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # II  Ginastica
        # ================================================================
        {
            "id": "u2",
            "titulo": "Ginástica",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Capacidades motoras e salto à corda",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada capacidade motora ao que ela "
                                 "é.",
                            "pairs": [
                                ["Força", "Vencer uma resistência"],
                                ["Flexibilidade", "Mover as articulações ao máximo"],
                                ["Equilíbrio", "Manter o corpo sem cair"],
                                ["Coordenação", "Juntar bem vários movimentos"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Para medir a corda de saltar, passa-se "
                                 "por baixo dos pés e as pontas devem "
                                 "chegar:",
                            "options": ["Às axilas", "Aos joelhos", "Ao chão"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No salto à corda, os movimentos "
                                 "aprendem-se:",
                            "options": [
                                "Primeiro parado e depois em deslocamento",
                                "Logo a correr",
                                "Só de olhos fechados",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "No exercício de dois alunos com uma "
                                 "corda, quantos saltam com a mesma corda "
                                 "ao mesmo tempo?",
                            "a": "2",
                        },
                        {
                            "t": "choice",
                            "q": "Quando a turma é grande e há pouco "
                                 "material, a aula de ginástica faz-se:",
                            "options": [
                                "Em circuito, com estações e grupos a "
                                "rodar",
                                "Todos ao mesmo tempo na mesma corda",
                                "Sem exercícios",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Ginástica artística de solo",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada posição de equilíbrio à sua "
                                 "descrição.",
                            "pairs": [
                                ["Avião", "Um pé no chão, tronco à frente, braços abertos"],
                                ["Ponte", "Barriga para cima, mãos e pés no chão"],
                                ["Espargata", "Pernas abertas em linha até ao chão"],
                            ],
                        },
                        {
                            "t": "input",
                            "q": "Numa posição de equilíbrio deve-se "
                                 "aguentar parado alguns segundos. Se se "
                                 "aguenta 3 segundos no avião e 5 na "
                                 "ponte, quantos segundos parado ao todo?",
                            "a": "8",
                        },
                        {
                            "t": "choice",
                            "q": "Ao fazer a ponte ou a espargata, o "
                                 "colega que ajuda serve para:",
                            "options": [
                                "Segurar e evitar lesões",
                                "Empurrar com força",
                                "Ver e rir",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes dos saltos e voltas no solo faz-se "
                                 "sempre:",
                            "options": [
                                "Aquecimento",
                                "Uma refeição pesada",
                                "Um banho frio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Fazer ginástica a pares desenvolve:",
                            "options": [
                                "A cooperação e a interajuda",
                                "A competição a todo o custo",
                                "O medo",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # III  Atletismo
        # ================================================================
        {
            "id": "u3",
            "titulo": "Atletismo",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Resistência e estafetas",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Na 8ª classe, a corrida de resistência "
                                 "vai até quantos minutos sem parar?",
                            "a": "10",
                        },
                        {
                            "t": "choice",
                            "q": "Na corrida de resistência em grupo, o "
                                 "ritmo é marcado por:",
                            "options": [
                                "O aluno mais lento, para ninguém ficar "
                                "para trás",
                                "O aluno mais rápido",
                                "O professor a correr à frente",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na corrida de estafetas, o testemunho "
                                 "passa-se:",
                            "options": [
                                "Dentro de uma zona marcada, sem parar de "
                                "correr",
                                "Em qualquer sítio, parado",
                                "Atirando-o ao ar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A transmissão do testemunho por baixo "
                                 "aprende-se primeiro:",
                            "options": [
                                "A andar, depois em corrida lenta, depois "
                                "a correr",
                                "Logo à velocidade máxima",
                                "Sem testemunho",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma equipa de estafetas tem 4 corredores "
                                 "e cada um corre 100 metros. Quantos "
                                 "metros corre a equipa?",
                            "a": "400",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Salto em comprimento",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada fase do salto em comprimento à "
                                 "sua ordem.",
                            "pairs": [
                                ["Corrida de balanço", "Primeira"],
                                ["Chamada", "Segunda"],
                                ["Voo", "Terceira"],
                                ["Queda", "Quarta"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A chamada é:",
                            "options": [
                                "O impulso com um pé na tábua, antes do "
                                "voo",
                                "O grito do professor",
                                "A queda na areia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na técnica engrupada, durante o voo o "
                                 "saltador:",
                            "options": [
                                "Encolhe os joelhos ao peito",
                                "Estica-se todo para trás",
                                "Fica de pé no ar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A caixa de saltos deve estar:",
                            "options": [
                                "Com areia solta e sem pedras nem objectos",
                                "Com pedras para marcar",
                                "Cheia de água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O salto aprende-se primeiro:",
                            "options": [
                                "Sem corrida de balanço, e só depois com "
                                "ela",
                                "Com a corrida mais longa possível",
                                "De costas",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # V  Basquetebol
        # ================================================================
        {
            "id": "u4",
            "titulo": "Basquetebol",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O ataque: passe, drible e lançamento",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada passe à sua descrição.",
                            "pairs": [
                                ["Passe de peito", "Sai do peito, directo ao colega"],
                                ["Passe picado", "Bate no chão antes de chegar"],
                                ["Passe de ombro", "Com uma mão, por cima do ombro"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "No basquetebol, para avançar com a bola "
                                 "na mão é preciso:",
                            "options": [
                                "Driblar: bater a bola no chão",
                                "Correr com a bola agarrada",
                                "Dar pontapés na bola",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O drible de protecção usa-se quando:",
                            "options": [
                                "Um adversário está perto e se guarda a "
                                "bola com o corpo",
                                "Não há ninguém à volta",
                                "Se quer lançar de longe",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A posição de tripla ameaça é a de quem "
                                 "tem a bola e pode:",
                            "options": [
                                "Passar, driblar ou lançar",
                                "Só passar",
                                "Só correr",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "No lançamento na passada, depois de "
                                 "pegar a bola no drible, quantos apoios "
                                 "se podem dar antes de saltar?",
                            "a": "2",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A defesa e o jogo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A equipa que tem a bola:",
                            "options": [
                                "Ataca",
                                "Defende",
                                "Descansa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tarefa à equipa que a faz.",
                            "pairs": [
                                ["Manter a posse e lançar ao cesto", "Quem ataca"],
                                ["Recuperar a bola e proteger o cesto", "Quem defende"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Na posição básica defensiva, o jogador "
                                 "fica:",
                            "options": [
                                "Com os joelhos flectidos e os braços "
                                "abertos, entre o adversário e o cesto",
                                "De pé, direito e parado",
                                "Sentado no chão",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Defender o jogador sem bola chama-se:",
                            "options": [
                                "Sobremarcação e ajuda",
                                "Pressão",
                                "Lançamento",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Nos jogos reduzidos de basquetebol na "
                                 "aula, quantos alunos há no mínimo em "
                                 "cada equipa?",
                            "a": "3",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # VI  Futebol
        # ================================================================
        {
            "id": "u5",
            "titulo": "Futebol",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Desmarcar, proteger a bola e jogar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Desmarcar-se é:",
                            "options": [
                                "Sair de perto do adversário para receber "
                                "a bola",
                                "Ficar parado ao lado do adversário",
                                "Sair do campo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ocupar o espaço de forma equilibrada é:",
                            "options": [
                                "A equipa espalhar-se pelo campo em vez de "
                                "correr toda atrás da bola",
                                "Todos irem à bola",
                                "Ficarem todos na baliza",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A finta serve para:",
                            "options": [
                                "Enganar o adversário e passar por ele",
                                "Parar o jogo",
                                "Pedir substituição",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Proteger a bola é:",
                            "options": [
                                "Pôr o corpo entre a bola e o adversário",
                                "Agarrar a bola com as mãos",
                                "Chutar a bola para fora",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Num jogo formal de futebol, quantos "
                                 "jogadores tem cada equipa em campo, "
                                 "contando o guarda-redes?",
                            "a": "11",
                        },
                        {
                            "t": "choice",
                            "q": "Quando o capitão da equipa decide, os "
                                 "colegas:",
                            "options": [
                                "Respeitam a decisão e jogam em conjunto",
                                "Discutem até o jogo acabar",
                                "Abandonam o campo",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
    ],
}


def main() -> int:
    gravar = "--gravar" in sys.argv
    dados = audio.carregar_content()
    ids = [c["id"] for c in dados["cursos"]]

    if CURSO["id"] in ids:
        print(f"o curso {CURSO['id']} ja esta no content.json", file=sys.stderr)
        return 1

    unidades = len(CURSO["units"])
    niveis = sum(len(u["niveis"]) for u in CURSO["units"])
    perguntas = sum(len(n["questoes"])
                    for u in CURSO["units"] for n in u["niveis"])
    print(f"{CURSO['disciplina']} da {CURSO['classe']}")
    print(f"  {unidades} unidades, {niveis} niveis, {perguntas} perguntas")
    for u in CURSO["units"]:
        print(f"   {u['id']}  {u['titulo']}")
        for n in u["niveis"]:
            tipos = sorted({q["t"] for q in n["questoes"]})
            print(f"       {n['id']}  {n['titulo']:<40}"
                  f"{len(n['questoes'])}q  {tipos}")

    if not gravar:
        print("\n(so leitura -- corre com --gravar)")
        return 0

    manifesto = audio.ler_manifesto()
    feitos = 0
    for u in CURSO["units"]:
        for n in u["niveis"]:
            for q in n["questoes"]:
                ficheiro = audio.nome_do_ficheiro(q["q"])
                q["audio"] = ficheiro
                if (audio.AUDIO / ficheiro).exists() and \
                        manifesto.get(ficheiro) == audio.sha(audio.dito(q["q"])):
                    continue
                if not audio.gravar(q["q"], ficheiro, manifesto):
                    print(f"FALHOU o audio de {q['q'][:50]}", file=sys.stderr)
                    audio.escrever_manifesto(manifesto)
                    return 1
                feitos += 1
                print(f"   {(audio.AUDIO / ficheiro).stat().st_size:>6} bytes"
                      f"  {ficheiro}")

    # A seguir ao ultimo curso da 8a que ja la esteja.
    onde = max(i for i, c in enumerate(dados["cursos"])
               if c["classe"] == "8ª classe") + 1
    dados["cursos"].insert(onde, CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta as entradas ao tools/materia_texto.py "
          "e corre python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
