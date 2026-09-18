# -*- coding: utf-8 -*-
"""O curso de Educacao Fisica da 9a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Educacao Fisica -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024,
     9a classe, pp. 33-40. Guardado em Documents\\planos da 5a classe\\
     Livros\\Programas INDE 1o Ciclo\\educacao-fisica.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

As cinco unidades da 9a, pela ordem do plano tematico
-----------------------------------------------------
    I    Dancas e jogos educativos   jogos recreativos; dancas africanas
    I    Ginastica                   geral e artistica; acrobatica
    III  Atletismo                   resistencia e barreiras; salto em
                                     altura
    VI   Futebol                     guarda-redes e jogo
    VII  Voleibol                    ataque; defesa e regras

(O programa numera as unidades do ciclo inteiro, e por isso salta
numeros; o Voleibol e novo na 9a, e o Basquetebol, que foi da 8a, sai.)

Cinco unidades, nove aulas. O criterio e o da 7a e da 8a: pergunta-se o
que o corpo precisa de saber antes -- regras, tecnica, seguranca.

Correr a partir de somara-flutter/:
    python tools/conteudo_edf9c.py            # so mostra
    python tools/conteudo_edf9c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Educação Física — Ensino "
    "Secundário, 1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024, 9ª "
    "classe, pp. 33-40. As cinco unidades temáticas e os conteúdos são do "
    "programa; os exercícios foram escritos a partir deles, porque um "
    "programa de ensino não traz exercícios e não há livro do aluno da 9ª "
    "classe publicado."
)

CURSO = {
    "id": "edf-9c",
    "disciplina": "Educação Física",
    "classe": "9ª classe",
    "tag": "EDF",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # I  Dancas e jogos educativos
        # ================================================================
        {
            "id": "u1",
            "titulo": "Danças e jogos educativos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Os jogos recreativos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O fartlek é uma corrida em que:",
                            "options": [
                                "Se muda de ritmo, ora depressa, ora "
                                "devagar, pelo terreno",
                                "Se corre sempre à mesma velocidade",
                                "Se corre para trás",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Correr 100 metros de mãos dadas com a "
                                 "turma é um jogo que treina:",
                            "options": [
                                "O espírito de equipa e a cooperação",
                                "A força de um aluno só",
                                "A velocidade individual",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Num jogo matemático, cada equipa corre "
                                 "até ao número que é a soma de 7 e 8. A "
                                 "que número correm?",
                            "a": "15",
                        },
                        {
                            "t": "choice",
                            "q": "Um jogo educativo sobre casamentos "
                                 "prematuros serve para:",
                            "options": [
                                "Pensar e conversar sobre o assunto a "
                                "brincar",
                                "Ridicularizar os colegas",
                                "Ganhar pontos sem regras",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de ensinar um jogo aos colegas, "
                                 "deve-se:",
                            "options": [
                                "Explicar as regras de forma clara, para "
                                "todos saberem o que fazer",
                                "Começar sem dizer nada",
                                "Mudar as regras a meio",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "As danças africanas",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada dança ao país de onde vem.",
                            "pairs": [
                                ["Marrabenta", "Moçambique"],
                                ["Semba", "Angola"],
                                ["Funaná", "Cabo Verde"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A marrabenta nasceu:",
                            "options": [
                                "No sul de Moçambique, à volta de Maputo",
                                "No Brasil",
                                "Em Portugal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O kuduro é uma dança de:",
                            "options": ["Angola", "Moçambique", "Cabo Verde"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Dançar as danças africanas na escola "
                                 "serve para:",
                            "options": [
                                "Conhecer e guardar a cultura dos povos "
                                "africanos",
                                "Esquecer a tradição",
                                "Só fazer exercício",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para dançar bem uma dança africana, "
                                 "primeiro:",
                            "options": [
                                "Ouve-se o ritmo e aprendem-se os passos "
                                "básicos",
                                "Faz-se a coreografia final",
                                "Escolhe-se a roupa",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # I  Ginastica
        # ================================================================
        {
            "id": "u2",
            "titulo": "Ginástica",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Ginástica geral e artística",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Na 9ª classe, combinam-se pelo menos "
                                 "quantos exercícios de salto à corda em "
                                 "grupo?",
                            "a": "4",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada elemento da ginástica de solo "
                                 "ao que ele é.",
                            "pairs": [
                                ["Rolamento para a frente", "Rolar sobre as costas, com o queixo ao peito"],
                                ["Vela", "Deitado, pernas e tronco esticados para cima"],
                                ["Roda", "Apoio das mãos, uma a uma, com as pernas a passar por cima"],
                                ["Pino", "Equilíbrio de pernas para o ar, apoiado nas mãos"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "No rolamento para a frente, o queixo "
                                 "vai:",
                            "options": [
                                "Encostado ao peito, para proteger o "
                                "pescoço",
                                "Levantado para trás",
                                "Virado para o lado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No pino, na fase de aprendizagem:",
                            "options": [
                                "Um colega ajuda a segurar as pernas no "
                                "fim",
                                "Faz-se sozinho logo da primeira vez",
                                "Faz-se no cimento",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Trabalhar por estações, na aula de "
                                 "ginástica, é:",
                            "options": [
                                "Dividir a turma em grupos que rodam por "
                                "exercícios diferentes",
                                "Todos a fazer o mesmo ao mesmo tempo",
                                "Esperar numa estação de comboio",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Ginástica acrobática",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada papel na ginástica acrobática "
                                 "ao aluno que o faz.",
                            "pairs": [
                                ["Base, em baixo", "O mais pesado e forte"],
                                ["Volante, em cima", "O mais leve"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O volante, quando sobe, nunca põe os "
                                 "pés:",
                            "options": [
                                "No meio da coluna do base, nos rins",
                                "Nos ombros do base",
                                "Nas coxas do base",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O base deve ter sempre:",
                            "options": [
                                "As costas direitas e a barriga contraída",
                                "As costas curvadas",
                                "Os joelhos soltos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Na acrobática, uma figura de trio tem "
                                 "quantos alunos?",
                            "a": "3",
                        },
                        {
                            "t": "choice",
                            "q": "Na acrobática, primeiro está:",
                            "options": [
                                "A segurança: pegas firmes e um ajudante "
                                "a ver",
                                "A dificuldade do exercício",
                                "A rapidez",
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
                    "titulo": "Resistência e barreiras",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "O teste de Cooper é uma corrida sem "
                                 "parar durante quantos minutos?",
                            "a": "12",
                        },
                        {
                            "t": "choice",
                            "q": "O teste de Cooper mede:",
                            "options": [
                                "A resistência: a distância que se corre "
                                "no tempo dado",
                                "A força dos braços",
                                "A flexibilidade",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada fase da corrida de barreiras "
                                 "à sua ordem.",
                            "pairs": [
                                ["Partida", "Primeira"],
                                ["Aproximação à primeira barreira", "Segunda"],
                                ["Transposição das barreiras", "Terceira"],
                                ["Corrida depois da última barreira", "Quarta"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Nas barreiras, aprende-se primeiro:",
                            "options": [
                                "Com obstáculos no chão, e depois cada vez "
                                "mais altos",
                                "Com as barreiras no máximo",
                                "Sem barreiras nunca",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Na 9ª classe, cada aluno deve transpor "
                                 "no mínimo quantas barreiras à altura do "
                                 "joelho?",
                            "a": "3",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O salto em altura",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada fase do salto em altura à sua "
                                 "ordem.",
                            "pairs": [
                                ["Corrida de balanço", "Primeira"],
                                ["Chamada", "Segunda"],
                                ["Transposição da fasquia", "Terceira"],
                                ["Queda", "Quarta"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Na técnica de tesoura, as pernas passam "
                                 "a fasquia:",
                            "options": [
                                "Uma de cada vez, como as lâminas de uma "
                                "tesoura",
                                "As duas juntas",
                                "De cabeça para baixo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No salto em altura, começa-se:",
                            "options": [
                                "Com a fasquia baixa, e sobe-se aos poucos",
                                "Com a fasquia no máximo",
                                "Sem fasquia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os exercícios do abecedário da corrida "
                                 "fazem-se:",
                            "options": [
                                "No início de todas as aulas de atletismo",
                                "Só no fim do ano",
                                "Nunca",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A fasquia no salto em altura deve ser:",
                            "options": [
                                "Leve e fácil de cair, para ninguém se "
                                "magoar",
                                "Um pau pesado e fixo",
                                "Um arame",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # VI  Futebol
        # ================================================================
        {
            "id": "u4",
            "titulo": "Futebol",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O guarda-redes e o jogo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O guarda-redes pode agarrar a bola com "
                                 "as mãos:",
                            "options": [
                                "Só dentro da sua grande área",
                                "Em todo o campo",
                                "Nunca",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um bom guarda-redes coloca-se:",
                            "options": [
                                "Entre a bola e o centro da baliza",
                                "Sempre encostado a um poste",
                                "Fora da área",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quando o árbitro decide:",
                            "options": [
                                "Respeita-se a decisão e continua-se a "
                                "jogar",
                                "Discute-se até ele mudar",
                                "Sai-se do campo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um bom plano de jogo:",
                            "options": [
                                "Dá um papel a cada jogador da equipa",
                                "Põe todos atrás da bola",
                                "Deixa os mais fracos de fora",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Num jogo formal de futebol, cada parte "
                                 "dura quantos minutos?",
                            "a": "45",
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # VII  Voleibol
        # ================================================================
        {
            "id": "u5",
            "titulo": "Voleibol",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Serviço, passe e remate",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "No voleibol, quantos jogadores tem cada "
                                 "equipa em campo?",
                            "a": "6",
                        },
                        {
                            "t": "input",
                            "q": "Quantos toques pode dar uma equipa na "
                                 "bola antes de a passar para o outro lado?",
                            "a": "3",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada gesto do voleibol ao que ele "
                                 "é.",
                            "pairs": [
                                ["Serviço", "O primeiro batimento, que põe a bola em jogo"],
                                ["Passe", "Toque por cima, com as pontas dos dedos das duas mãos"],
                                ["Remate", "O ataque forte, a bater a bola para o campo do outro"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "No serviço por baixo, a bola bate-se:",
                            "options": [
                                "Com a mão, de baixo para cima, à frente "
                                "do corpo",
                                "Com o pé",
                                "Com a cabeça",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na aula, a rede pode baixar-se para:",
                            "options": [
                                "Todos conseguirem passar a bola por cima",
                                "Ninguém jogar",
                                "Ficar mais difícil",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Manchete, bloco e regras",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A manchete usa-se para receber:",
                            "options": [
                                "Bolas baixas, com os antebraços juntos",
                                "Bolas altas, com os dedos",
                                "Bolas no chão, com o pé",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O bloco faz-se:",
                            "options": [
                                "Junto à rede, saltando de braços "
                                "erguidos contra o remate",
                                "No fundo do campo",
                                "Sentado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No voleibol, a bola não pode:",
                            "options": [
                                "Ser agarrada nem conduzida: só batida",
                                "Passar por cima da rede",
                                "Ser servida",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Num set de voleibol, ganha a equipa que "
                                 "chega primeiro a quantos pontos, com "
                                 "dois de vantagem?",
                            "a": "25",
                        },
                        {
                            "t": "choice",
                            "q": "No voleibol, a equipa ganha:",
                            "options": [
                                "Cooperando: ninguém faz os três toques "
                                "sozinho",
                                "Com um jogador a fazer tudo",
                                "Sem passar a bola",
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

    # A seguir ao ultimo curso da 9a que ja la esteja.
    onde = max(i for i, c in enumerate(dados["cursos"])
               if c["classe"] == "9ª classe") + 1
    dados["cursos"].insert(onde, CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta as entradas ao tools/materia_texto.py "
          "e corre python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
