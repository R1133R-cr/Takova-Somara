# -*- coding: utf-8 -*-
"""O curso de Educacao Fisica da 7a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Educacao Fisica -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024.
     Descarregado do educador.mozestuda.com.

As cinco unidades tematicas da 7a classe, tal como o INDE as distribui
pelos tres trimestres:

    Io    Ginastica, Atletismo, Opcional
    IIo   Ginastica, Andebol, Dancas e Jogos Educativos
    IIIo  Futebol, Opcional, Dancas e Jogos Educativos

Juntas, sem repetir: Ginastica, Atletismo, Andebol, Futebol, Dancas e
Jogos Educativos. Cinco unidades de dois niveis.

A disciplina que uma app menos consegue dar, e fica dito
---------------------------------------------------------
Educacao Fisica faz-se com o corpo. Nenhuma pergunta de escolha multipla
substitui correr, saltar ou passar uma bola, e nao e isso que este curso
tenta.

O que aqui se ensina e o que se aprende NA SALA e vale no campo: as
regras dos jogos, os nomes dos gestos tecnicos, o aquecimento antes do
esforco, o que fazer numa lesao, porque e que a agua importa. E o
conhecimento que faz um aluno perceber o treino em vez de o imitar -- e e
tambem o que sai nos testes escritos da disciplina.

Correr a partir de somara-flutter/:
    python tools/conteudo_edf7c.py            # so mostra
    python tools/conteudo_edf7c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Educação Física — Ensino "
    "Secundário, 1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024. As "
    "unidades são as do programa da 7ª classe, reunidas sem repetir as "
    "que voltam em mais de um trimestre. Educação Física faz-se com o "
    "corpo e nenhuma pergunta substitui isso; aqui avalia-se o que se "
    "aprende na sala e vale no campo — regras, gestos técnicos, "
    "aquecimento, socorro e hidratação. Os exercícios foram escritos a "
    "partir dos conteúdos, porque um programa de ensino não traz "
    "exercícios e não há livro do aluno da 7ª classe publicado."
)

CURSO = {
    "id": "edf-7c",
    "disciplina": "Educação Física",
    "classe": "7ª classe",
    "tag": "EDF",
    "abrev": "Ed. Física",
    "fonte": FONTE,
    "units": [
        {
            "id": "u1",
            "titulo": "Ginástica",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Aquecer antes de trabalhar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O aquecimento antes do exercício serve "
                                 "sobretudo para:",
                            "options": [
                                "Preparar os músculos e evitar lesões",
                                "Cansar antes de começar",
                                "Ganhar pontos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O retorno à calma, no fim da aula, serve "
                                 "para:",
                            "options": [
                                "Baixar aos poucos o ritmo do corpo",
                                "Aumentar o esforço no fim",
                                "Poupar tempo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Durante o exercício, deve-se beber água:",
                            "options": [
                                "Em pequenas quantidades e com regularidade",
                                "Só no fim, de uma vez",
                                "Nunca, para não ter cãibras",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de fazer ginástica num colchão, "
                                 "deve-se:",
                            "options": [
                                "Verificar se o espaço está livre e seguro",
                                "Começar logo, para não perder tempo",
                                "Fazer o exercício mais difícil primeiro",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Elementos da ginástica de solo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O rolamento à frente executa-se apoiando "
                                 "primeiro:",
                            "options": [
                                "As mãos no solo e enrolando a cabeça para "
                                "dentro",
                                "A cabeça directamente no solo",
                                "As costas de uma vez",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na ginástica, o equilíbrio melhora quando:",
                            "options": [
                                "A base de apoio é mais larga e o centro de "
                                "gravidade mais baixo",
                                "Se fecham os olhos",
                                "Se levantam os braços ao máximo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A ajuda de um colega durante um exercício "
                                 "de ginástica serve para:",
                            "options": [
                                "Dar segurança e corrigir o movimento",
                                "Fazer o exercício por ele",
                                "Ganhar mais pontos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A flexibilidade trabalha-se sobretudo com:",
                            "options": [
                                "Alongamentos regulares",
                                "Corridas de velocidade",
                                "Levantamento de pesos",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u2",
            "titulo": "Atletismo",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Corridas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Nas corridas de velocidade, a partida "
                                 "faz-se normalmente:",
                            "options": [
                                "De blocos, em posição baixa",
                                "De pé, parado",
                                "A andar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa corrida de estafetas, o que passa de "
                                 "atleta para atleta é:",
                            "options": ["O testemunho", "A bola", "O dorsal"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa corrida de fundo, o atleta deve:",
                            "options": [
                                "Gerir o esforço ao longo de toda a prova",
                                "Correr ao máximo desde o início",
                                "Parar de vez em quando",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A corrida de barreiras exige sobretudo:",
                            "options": [
                                "Ritmo e coordenação entre passadas e salto",
                                "Apenas força nos braços",
                                "Apenas resistência",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Saltos e lançamentos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "No salto em comprimento, a marca que conta "
                                 "é:",
                            "options": [
                                "A mais próxima da tábua deixada na queda",
                                "O ponto de chamada",
                                "O ponto mais distante da caixa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As quatro fases do salto em comprimento "
                                 "são:",
                            "options": [
                                "Corrida, chamada, voo e queda",
                                "Partida, corrida, salto e paragem",
                                "Aquecimento, corrida, salto e descanso",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No lançamento do peso, o peso é:",
                            "options": [
                                "Empurrado a partir do ombro",
                                "Atirado por cima da cabeça",
                                "Lançado com as duas mãos de baixo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de um lançamento, é obrigatório:",
                            "options": [
                                "Confirmar que a zona de queda está livre",
                                "Correr o mais depressa possível",
                                "Fechar os olhos",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u3",
            "titulo": "Andebol",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "As regras do andebol",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Quantos jogadores de campo tem uma equipa "
                                 "de andebol, sem contar o guarda-redes?",
                            "a": "6",
                        },
                        {
                            "t": "choice",
                            "q": "Com a bola na mão, um jogador de andebol "
                                 "pode dar no máximo:",
                            "options": ["Três passos", "Cinco passos", "Um passo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A área de baliza do andebol só pode ser "
                                 "ocupada:",
                            "options": [
                                "Pelo guarda-redes",
                                "Por dois defesas",
                                "Por qualquer jogador",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Jogar a bola com o pé, no andebol, é:",
                            "options": [
                                "Falta",
                                "Permitido",
                                "Permitido só ao guarda-redes na sua área",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Gestos técnicos do andebol",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O drible, no andebol, é:",
                            "options": [
                                "Bater a bola no chão com uma mão",
                                "Correr com a bola presa",
                                "Passar a bola com o pé",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O passe de ombro serve sobretudo para:",
                            "options": [
                                "Enviar a bola ao longe com precisão",
                                "Passar a um colega ao lado",
                                "Marcar golo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O remate em suspensão faz-se:",
                            "options": [
                                "Com o corpo no ar, antes de tocar o solo",
                                "Sentado",
                                "Com os dois pés no chão",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na defesa, o objectivo principal é:",
                            "options": [
                                "Impedir o remate e recuperar a bola",
                                "Empurrar o adversário",
                                "Sair da área",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u4",
            "titulo": "Futebol",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "As regras do futebol",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Quantos jogadores tem em campo, ao mesmo "
                                 "tempo, uma equipa de futebol de onze?",
                            "a": "11",
                        },
                        {
                            "t": "choice",
                            "q": "Só um jogador pode tocar a bola com as "
                                 "mãos dentro da sua área:",
                            "options": [
                                "O guarda-redes",
                                "O capitão",
                                "O defesa central",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quando a bola sai pela linha lateral, o "
                                 "jogo recomeça com:",
                            "options": [
                                "Um lançamento de linha lateral",
                                "Um pontapé de canto",
                                "Um pontapé de baliza",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O cartão vermelho significa que o jogador:",
                            "options": [
                                "Está expulso e sai do jogo",
                                "Está advertido",
                                "Vai bater um penálti",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Gestos técnicos do futebol",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Para um passe curto e rasteiro, usa-se "
                                 "sobretudo:",
                            "options": [
                                "A parte interna do pé",
                                "A ponta do pé",
                                "O calcanhar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A recepção da bola faz-se melhor:",
                            "options": [
                                "Amortecendo com o pé ou o peito",
                                "Parando a bola com a mão",
                                "Deixando a bola bater e seguir",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A condução de bola consiste em:",
                            "options": [
                                "Levar a bola em corrida, com toques curtos",
                                "Chutar a bola para a frente e correr atrás",
                                "Segurar a bola nas mãos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma entrada com os pitons em cima do "
                                 "adversário é:",
                            "options": [
                                "Falta grave, que pode dar cartão",
                                "Jogada normal",
                                "Permitida se for na área",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u5",
            "titulo": "Danças e jogos educativos",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "As danças tradicionais moçambicanas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As danças tradicionais moçambicanas são "
                                 "importantes porque:",
                            "options": [
                                "Preservam a cultura e juntam a comunidade",
                                "Substituem o desporto",
                                "Só servem para as festas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O Mapiko é uma dança tradicional "
                                 "associada sobretudo:",
                            "options": [
                                "Ao povo Maconde, no norte de Moçambique",
                                "Ao sul do país",
                                "À cidade de Maputo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa dança de grupo, o mais importante é:",
                            "options": [
                                "Acompanhar o ritmo em conjunto",
                                "Dançar mais depressa do que os outros",
                                "Ficar à frente",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A dança desenvolve sobretudo:",
                            "options": [
                                "A coordenação, o ritmo e a expressão",
                                "Apenas a força",
                                "Apenas a velocidade",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Jogos educativos e desportivismo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um jogo educativo serve para:",
                            "options": [
                                "Aprender e cooperar enquanto se joga",
                                "Escolher os melhores alunos",
                                "Passar o tempo sem objectivo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O «ntxuva» é:",
                            "options": [
                                "Um jogo tradicional moçambicano de tabuleiro",
                                "Uma dança do norte",
                                "Um desporto olímpico",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Perder um jogo com desportivismo quer "
                                 "dizer:",
                            "options": [
                                "Aceitar o resultado e cumprimentar o "
                                "adversário",
                                "Culpar o árbitro",
                                "Não voltar a jogar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Se um colega se magoar durante o jogo, "
                                 "deve-se:",
                            "options": [
                                "Parar o jogo e chamar o professor",
                                "Continuar a jogar",
                                "Levantá-lo à força",
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
    if CURSO["id"] in [c["id"] for c in dados["cursos"]]:
        print(f"o curso {CURSO['id']} ja esta no content.json", file=sys.stderr)
        return 1

    niveis = sum(len(u["niveis"]) for u in CURSO["units"])
    perguntas = sum(len(n["questoes"])
                    for u in CURSO["units"] for n in u["niveis"])
    print(f"{CURSO['disciplina']} da {CURSO['classe']}: "
          f"{len(CURSO['units'])} unidades, {niveis} niveis, "
          f"{perguntas} perguntas")

    if not gravar:
        print("(so leitura -- corre com --gravar)")
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

    dados["cursos"].append(CURSO)
    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"-- curso inserido, {feitos} audios gravados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
