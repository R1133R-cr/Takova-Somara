# -*- coding: utf-8 -*-
"""O curso de Portugues da 4a classe.

De onde vem
-----------
Do "Caderno de Actividades de Lingua Portuguesa da 4a Classe", MINEDH/MEC
2025, descarregado do MozEstuda e guardado em

    Documents\\planos da 5a classe\\Livros\\4a Classe\\
    Portugues da 4a Classe MINEDH-MEC 2025 (mozestuda).pdf
    sha1 5587fdaf70c6...

O livro diz de si proprio, na introducao: "O Ministerio da Educacao e
Desenvolvimento Humano (MINEDH) elaborou este Caderno de Actividades de
Lingua Portuguesa (...) Os conteudos foram seleccionados com base no
programa de ensino; estao organizados por unidades tematicas."

AVISO SOBRE A FONTE: o MozEstuda e um portal privado, nao e o MINEDH. O
livro rotula-se oficial e a estrutura interna bate certo com o Plano
Curricular do Ensino Primario (MINEDH, Maio 2020), mas quem quiser dar
isto por oficial tem de o confirmar na fonte do ministerio.

Porque e que as unidades sao tematicas e nao gramaticais
--------------------------------------------------------
O curso da 5a classe esta organizado por materia gramatical -- "Nomes e
adjectivos", "Pronomes", "A frase". Este segue as nove unidades TEMATICAS
do livro: Familia, Escola, Comunidade, Ambiente, Corpo Humano, Saude e
Higiene, Meios de Transporte, Comunicacao, A nossa provincia.

E como o II ciclo esta organizado, e a gramatica entra dentro do tema --
as preposicoes aparecem na unidade da Comunidade porque e ali que o livro
as poe. Uma crianca que abra a app a seguir a aula reconhece o sitio onde
esta.

Onde entra na lista de cursos
-----------------------------
Entre o mat-4c e o cn-4c, para a 4a classe ficar com a mesma ordem de
disciplinas da 5a e da 6a: Matematica, Portugues, Ciencias Naturais,
Ciencias Sociais.

Correr a partir de somara-flutter/:
    python tools/conteudo_por4c.py            # so mostra
    python tools/conteudo_por4c.py --gravar   # escreve e grava o audio

A materia de cada nivel vive no tools/materia_texto.py, como a de todos os
outros cursos, e e o tools/materia.py que a prende ao content.json.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

CURSO = {
    "id": "por-4c",
    "disciplina": "Português",
    "classe": "4ª classe",
    "tag": "POR",
    "units": [
        # ---------------------------------------------------------------
        # Unidade Tematica 1: Familia  (livro, pp. 7-19)
        # ---------------------------------------------------------------
        {
            "id": "u1",
            "titulo": "Família",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Falar com cortesia",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Os princípios de cortesia servem para:",
                            "options": [
                                "Falarmos com delicadeza e respeito",
                                "Falarmos mais depressa",
                                "Falarmos mais alto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa conversa, devemos:",
                            "options": [
                                "Esperar pela nossa vez de falar",
                                "Falar por cima dos outros",
                                "Mudar de assunto a toda a hora",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como falas com a tua professora?",
                            "options": [
                                "Bom dia, senhora professora!",
                                "Olá, tu!",
                                "Anda cá!",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Olá, amiga! Estás bem?» é linguagem:",
                            "options": [
                                "Informal, entre amigos",
                                "Formal, de respeito",
                                "Escrita, de livro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada pessoa à forma de tratamento certa.",
                            "pairs": [
                                ["A professora", "Senhora professora"],
                                ["A tua amiga", "Tu"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Nomes comuns e próprios",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Os nomes comuns designam:",
                            "options": [
                                "Seres de uma mesma espécie",
                                "Uma só pessoa, com nome dela",
                                "Acções que se fazem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas palavras é um nome próprio?",
                            "options": ["Manica", "cidade", "província"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os nomes próprios escrevem-se sempre:",
                            "options": [
                                "Com letra inicial maiúscula",
                                "Com letra inicial minúscula",
                                "Todos em maiúsculas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Escreve o feminino de \"irmão\".",
                            "a": "irmã",
                        },
                        {
                            "t": "match",
                            "q": "Liga cada nome comum ao seu plural.",
                            "pairs": [
                                ["irmã", "irmãs"],
                                ["homem", "homens"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Nomes terminados em ão",
                    "questoes": [
                        {
                            "t": "input",
                            "q": "Escreve o plural de \"pão\".",
                            "a": "pães",
                        },
                        {
                            "t": "input",
                            "q": "Escreve o plural de \"mão\".",
                            "a": "mãos",
                        },
                        {
                            "t": "choice",
                            "q": "Qual é o plural de \"coração\"?",
                            "options": ["Corações", "Coraçãos", "Coração"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os nomes terminados em ão fazem o plural:",
                            "options": [
                                "De várias maneiras",
                                "Sempre com ãos",
                                "Sempre com ães",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # Unidade Tematica 2: Escola  (livro, pp. 20-30)
        # ---------------------------------------------------------------
        {
            "id": "u2",
            "titulo": "Escola",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Tipos de frase",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«A Lurdes gosta de aprender.» é uma frase:",
                            "options": [
                                "Declarativa",
                                "Interrogativa",
                                "Exclamativa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Fecha a porta, Tânia!» é uma frase:",
                            "options": [
                                "Imperativa",
                                "Declarativa",
                                "Interrogativa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Ah! Que presente bonito!» é uma frase:",
                            "options": [
                                "Exclamativa",
                                "Imperativa",
                                "Declarativa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A frase interrogativa serve para:",
                            "options": [
                                "Fazer perguntas",
                                "Dar uma ordem",
                                "Contar uma história",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada frase à sua intenção.",
                            "pairs": [
                                ["Declarativa", "Informar ou contar"],
                                ["Imperativa", "Dar uma ordem"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Sujeito e predicado",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Na frase «O Gabriel vive numa casa bonita.», o sujeito é:",
                            "options": ["O Gabriel", "vive", "numa casa bonita"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O predicado da frase diz:",
                            "options": [
                                "O que o sujeito faz",
                                "Quem pratica a acção",
                                "Onde a acção acontece",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um texto narrativo conta:",
                            "options": [
                                "Uma história, real ou imaginária",
                                "Como se faz uma coisa",
                                "Uma lista de palavras",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A introdução de uma narrativa responde a:",
                            "options": [
                                "Quando? Onde? Quem?",
                                "Quanto custa?",
                                "Porquê não?",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # Unidade Tematica 3: Comunidade  (livro, pp. 31-39)
        # ---------------------------------------------------------------
        {
            "id": "u3",
            "titulo": "Comunidade",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Preposições",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As preposições servem para:",
                            "options": [
                                "Ligar elementos da frase",
                                "Contar quantos há",
                                "Dar nome às pessoas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na frase «A Célia vai à machamba com a avó.», a preposição é:",
                            "options": ["com", "Célia", "machamba"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas palavras é uma preposição?",
                            "options": ["sobre", "casa", "correr"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As preposições são palavras:",
                            "options": [
                                "Invariáveis",
                                "Que mudam de género",
                                "Que mudam de número",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Completa com a contracção de \"de\" e \"o\": O livro ___ Armando.",
                            "a": "do",
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # Unidade Tematica 4: Ambiente  (livro, pp. 40-51)
        # ---------------------------------------------------------------
        {
            "id": "u4",
            "titulo": "Ambiente",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Tempos dos verbos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "«Ontem eu estudei.» O verbo está no:",
                            "options": [
                                "Pretérito perfeito",
                                "Presente",
                                "Futuro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Amanhã nós plantaremos árvores.» O verbo está no:",
                            "options": ["Futuro", "Presente", "Pretérito"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Escreve o verbo \"ir\" na 1ª pessoa do singular do presente: eu ___.",
                            "a": "vou",
                        },
                        {
                            "t": "choice",
                            "q": "O verbo \"ser\" é um verbo:",
                            "options": ["Irregular", "Regular", "Invariável"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Pontuação e nomes colectivos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Que sinal se põe no fim de uma pergunta?",
                            "options": [
                                "Ponto de interrogação",
                                "Ponto final",
                                "Vírgula",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um conjunto de árvores chama-se:",
                            "options": ["Floresta", "Árvores", "Madeira"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um nome colectivo designa:",
                            "options": [
                                "Um conjunto de seres da mesma espécie",
                                "Um só ser",
                                "Uma acção",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Pertencem à mesma família de palavras:",
                            "options": [
                                "Terra, terreno, enterrar",
                                "Terra, casa, chuva",
                                "Terra, correr, bonito",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # Unidade Tematica 5: Corpo Humano  (livro, pp. 52-55)
        # ---------------------------------------------------------------
        {
            "id": "u5",
            "titulo": "Corpo Humano",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A frase simples",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma frase simples tem:",
                            "options": [
                                "Um só verbo principal",
                                "Sempre dois verbos",
                                "Nenhum verbo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas é uma frase simples?",
                            "options": [
                                "A Maria lavou as mãos.",
                                "A Maria lavou as mãos e comeu o pão.",
                                "As mãos limpas.",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Toda a frase começa com:",
                            "options": [
                                "Letra maiúscula",
                                "Letra minúscula",
                                "Um número",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Quantos verbos principais tem uma frase simples?",
                            "a": "1",
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # Unidade Tematica 6: Saude e Higiene  (livro, pp. 56-60)
        # ---------------------------------------------------------------
        {
            "id": "u6",
            "titulo": "Saúde e Higiene",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Pronomes possessivos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Completa: Esta é ___ mão. (de mim)",
                            "options": ["a minha", "a tua", "a sua"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Completa: Esse é ___ livro. (de ti)",
                            "options": ["o teu", "o meu", "o nosso"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os pronomes possessivos dizem:",
                            "options": [
                                "De quem é a coisa",
                                "Onde está a coisa",
                                "Quantas coisas há",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Escreve no plural: a minha mão fica as ___ mãos.",
                            "a": "minhas",
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # Unidade Tematica 7: Meios de Transporte  (livro, pp. 61-64)
        # ---------------------------------------------------------------
        {
            "id": "u7",
            "titulo": "Meios de Transporte",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Advérbios de tempo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Qual destas palavras é um advérbio de tempo?",
                            "options": ["ontem", "devagar", "aqui"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na frase «O comboio chegou cedo.», o advérbio é:",
                            "options": ["cedo", "comboio", "chegou"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os advérbios de tempo dizem:",
                            "options": [
                                "Quando a acção acontece",
                                "Onde a acção acontece",
                                "Como a acção acontece",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«De manhã» é uma:",
                            "options": [
                                "Locução adverbial de tempo",
                                "Preposição",
                                "Nome próprio",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # Unidade Tematica 8: Comunicacao  (livro, pp. 65-70)
        # ---------------------------------------------------------------
        {
            "id": "u8",
            "titulo": "Comunicação",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Meios de comunicação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Qual destes é um meio de comunicação?",
                            "options": ["A rádio", "A enxada", "A panela"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um postal serve para:",
                            "options": [
                                "Mandar uma mensagem curta a alguém",
                                "Guardar dinheiro",
                                "Medir o tempo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na frase «A Ana escreveu depressa.», o advérbio de modo é:",
                            "options": ["depressa", "escreveu", "Ana"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os advérbios de modo dizem:",
                            "options": [
                                "Como a acção acontece",
                                "Quando acontece",
                                "Onde acontece",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada advérbio ao que ele diz.",
                            "pairs": [
                                ["ontem", "Quando"],
                                ["devagar", "Como"],
                            ],
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # Unidade Tematica 9: A nossa provincia  (livro, p. 71+)
        # ---------------------------------------------------------------
        {
            "id": "u9",
            "titulo": "A nossa província",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Advérbios de negação",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Qual destas palavras é um advérbio de negação?",
                            "options": ["não", "sim", "talvez"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Como se nega a frase «Eu fui à escola.»?",
                            "options": [
                                "Eu não fui à escola.",
                                "Eu fui à escola sim.",
                                "Fui eu à escola?",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "«Nunca» é um advérbio de:",
                            "options": ["Negação", "Lugar", "Modo"],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Nega esta frase com uma só palavra: Ela ___ chegou.",
                            "a": "não",
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
            tipos = [q["t"] for q in n["questoes"]]
            print(f"       {n['id']}  {n['titulo']:<32}"
                  f"{len(n['questoes'])}q  {tipos}")

    if not gravar:
        print("\n(so leitura -- corre com --gravar)")
        return 0

    # O audio: uma gravacao por pergunta, com o nome calculado do enunciado
    # e o texto dito ja com as regras aplicadas -- e o audio.py que trata
    # disso, e e por isso que aqui nao se decide nada sobre pronuncia.
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

    # Entre o mat-4c e o cn-4c, para a 4a classe ficar com a mesma ordem de
    # disciplinas da 5a e da 6a.
    onde = ids.index("cn-4c")
    dados["cursos"].insert(onde, CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta as entradas ao tools/materia_texto.py "
          "e corre python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
