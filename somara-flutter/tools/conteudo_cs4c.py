# -*- coding: utf-8 -*-
"""O curso de Ciencias Sociais da 4a classe.

De onde vem
-----------
Do "Caderno de Actividades de Ciencias Sociais da 4a Classe", MINEDH/MEC
2025, guardado em

    Documents\\planos da 5a classe\\Livros\\4a Classe\\
    CS da 4a Classe MINEDH-MEC 2025 (mozestuda).pdf
    sha1 4f02e8dc5213...

AVISO SOBRE A FONTE: o MozEstuda e um portal privado, nao e o MINEDH. Ver
o cabecalho do conteudo_por4c.py, onde isto esta escrito por extenso.

Cinco unidades tematicas, como no livro: Familia, Comunidade, Escola,
Provincia, Educacao Social e Financeira. As tres primeiras sao as mesmas
do Portugues da mesma classe -- e assim que o II ciclo esta organizado, e
por isso a crianca reconhece o tema quando muda de disciplina.

As definicoes sao as do livro e nao aproximacoes:
  planicie   altitude INFERIOR a 200 metros
  planalto   altitude SUPERIOR a 200 metros
  clima      o que se repete por 30 anos ou mais
  tempo      o estado do ar num certo momento e lugar
  afluente   rio pequeno que termina num maior

Numeros e definicoes deste genero sao faceis de escrever de cor e de
escrever mal. Estes foram lidos no livro, um a um.

Correr a partir de somara-flutter/:
    python tools/conteudo_cs4c.py            # so mostra
    python tools/conteudo_cs4c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

CURSO = {
    "id": "cs-4c",
    "disciplina": "Ciências Sociais",
    # Sem isto a pastilha da barra de disciplinas mostra o nome inteiro e
    # nao cabe num telemovel de 320. Ha um teste que o recusa, e apanhou-me
    # a esquecer-me disto.
    "abrev": "C. Sociais",
    "classe": "4ª classe",
    "tag": "CS",
    "units": [
        # ---------------------------------------------------------------
        # Unidade Tematica 1: Familia  (livro, pp. 7-17)
        # ---------------------------------------------------------------
        {
            "id": "u1",
            "titulo": "Família",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A família e os parentescos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A família é um conjunto de pessoas unidas por:",
                            "options": [
                                "Laço de sangue, matrimónio ou adopção",
                                "Viverem na mesma rua",
                                "Trabalharem no mesmo sítio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A família formada por pai, mãe e filhos chama-se:",
                            "options": ["Nuclear", "Monoparental", "Alargada"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A família em que só um dos pais cria os filhos chama-se:",
                            "options": ["Monoparental", "Nuclear", "Alargada"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os pais do meu pai e os pais da minha mãe são os meus:",
                            "options": ["Avós", "Tios", "Primos"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada parente à sua definição.",
                            "pairs": [
                                ["Tios", "Os irmãos do meu pai e da minha mãe"],
                                ["Avós", "Os pais do meu pai e da minha mãe"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Viver em família",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Quando há um desentendimento em casa, o melhor é:",
                            "options": [
                                "Conversar e resolver sem violência",
                                "Bater primeiro",
                                "Não falar mais com ninguém",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A árvore genealógica serve para:",
                            "options": [
                                "Mostrar os parentes de uma família",
                                "Medir a altura das árvores",
                                "Contar o dinheiro da casa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Cada membro da família tem:",
                            "options": [
                                "Deveres e obrigações",
                                "Só direitos",
                                "Nada a fazer",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os ritos e as cerimónias da família passam:",
                            "options": [
                                "De geração para geração",
                                "De um país para outro",
                                "De uma escola para outra",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Direitos e deveres da criança",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Qual destes é um direito da criança?",
                            "options": [
                                "Ter um nome",
                                "Faltar à escola",
                                "Trabalhar o dia todo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um dever da criança?",
                            "options": [
                                "Respeitar os mais velhos",
                                "Ter uma habitação",
                                "Ter uma nacionalidade",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Brincar é, para a criança:",
                            "options": ["Um direito", "Um dever", "Um castigo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Cidadania é o conjunto de:",
                            "options": [
                                "Direitos e deveres para participar na sociedade",
                                "Ruas de uma cidade",
                                "Pessoas que vivem numa casa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada um ao seu lugar.",
                            "pairs": [
                                ["À saúde", "Direito"],
                                ["Proteger o ambiente", "Dever"],
                            ],
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # Unidade Tematica 2: Comunidade  (livro, pp. 18-29)
        # ---------------------------------------------------------------
        {
            "id": "u2",
            "titulo": "Comunidade",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Tipos de comunidade",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A comunidade formada por quem vive no campo é:",
                            "options": ["Rural", "Urbana", "Religiosa"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A comunidade formada por quem vive na cidade é:",
                            "options": ["Urbana", "Rural", "Educativa"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Usos e costumes são práticas transmitidas:",
                            "options": [
                                "De geração para geração",
                                "Pela rádio",
                                "Pelos livros da escola",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A comunidade de quem faz parte do ambiente escolar é:",
                            "options": ["Educativa", "Religiosa", "Rural"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Lendas e contos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A lenda serve para explicar:",
                            "options": [
                                "Acontecimentos misteriosos",
                                "Contas de somar",
                                "Regras da escola",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na lenda misturam-se:",
                            "options": [
                                "Factos reais e fantasias",
                                "Só factos reais",
                                "Só números",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O conto é uma história transmitida:",
                            "options": [
                                "Dos mais velhos para os mais novos",
                                "Só por escrito",
                                "Só na escola",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O conto que quer transmitir uma lição moral é o:",
                            "options": ["Infantil", "De humor", "Realista"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada conto ao que ele faz.",
                            "pairs": [
                                ["Conto realista", "Narra situações reais"],
                                ["Conto de humor", "Diverte quem ouve"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Línguas e respeito",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Numa comunidade moçambicana fala-se:",
                            "options": [
                                "Português e línguas moçambicanas",
                                "Só português",
                                "Só uma língua",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Perante alguém diferente de nós, devemos:",
                            "options": [
                                "Respeitar a diferença",
                                "Afastar-nos",
                                "Rir dela",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A agricultura, a pesca e o comércio são:",
                            "options": [
                                "Actividades económicas da comunidade",
                                "Jogos tradicionais",
                                "Tipos de família",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A dança e a música tradicional fazem parte:",
                            "options": [
                                "Da cultura da comunidade",
                                "Do regulamento da escola",
                                "Da divisão administrativa",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # Unidade Tematica 3: Escola  (livro, pp. 30-37)
        # ---------------------------------------------------------------
        {
            "id": "u3",
            "titulo": "Escola",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A minha escola",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O livro diz que a escola é a nossa:",
                            "options": ["Segunda casa", "Primeira casa", "Última casa"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O regulamento interno da escola serve para:",
                            "options": [
                                "Dizer as regras que se cumprem na escola",
                                "Contar a história da escola",
                                "Marcar as férias",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para a escola estar limpa e organizada é preciso que:",
                            "options": [
                                "Os alunos ajudem na limpeza e conservação",
                                "Só o director trate disso",
                                "Ninguém entre nas salas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um conflito na escola resolve-se:",
                            "options": [
                                "Conversando, sem violência",
                                "À força",
                                "Fugindo da escola",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # Unidade Tematica 4: Provincia  (livro, pp. 38-61)
        # ---------------------------------------------------------------
        {
            "id": "u4",
            "titulo": "Província",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A província e o poder",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Moçambique está dividido em:",
                            "options": [
                                "Províncias, distritos, postos administrativos e localidades",
                                "Só províncias",
                                "Só cidades e aldeias",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quem dirige todos os assuntos de um distrito é o:",
                            "options": [
                                "Administrador do Distrito",
                                "Governador da Província",
                                "Presidente do Município",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O Conselho Autárquico é o órgão executivo do:",
                            "options": ["Município", "Distrito", "País"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O Representante de Estado numa província é nomeado:",
                            "options": [
                                "Pelo Presidente",
                                "Pelo povo",
                                "Pela escola",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Relevo, clima e rios",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Relevo são as diferentes formas como:",
                            "options": [
                                "A Terra se apresenta",
                                "A chuva cai",
                                "As pessoas falam",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As principais formas de relevo são:",
                            "options": [
                                "Planícies, planaltos e montanhas",
                                "Rios, lagos e mares",
                                "Cidades, vilas e aldeias",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Abaixo de quantos metros de altitude é uma planície?",
                            "a": "200",
                        },
                        {
                            "t": "choice",
                            "q": "O clima é o estado do tempo que se repete durante:",
                            "options": [
                                "30 anos ou mais",
                                "Uma semana",
                                "Um ano",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um rio pequeno que termina num rio maior chama-se:",
                            "options": ["Afluente", "Foz", "Nascente"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um rio de Moçambique?",
                            "options": ["Zambeze", "Nilo", "Congo"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Transportes e segurança",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Antes de atravessar a estrada devemos:",
                            "options": [
                                "Olhar para os dois lados",
                                "Correr depressa",
                                "Fechar os olhos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os sinais de trânsito servem para:",
                            "options": [
                                "Dar segurança a quem anda na estrada",
                                "Enfeitar a estrada",
                                "Marcar as províncias",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um meio de transporte?",
                            "options": ["O comboio", "O telefone", "A carta"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas acções degrada o ambiente?",
                            "options": [
                                "Queimar a floresta",
                                "Plantar árvores",
                                "Apanhar o lixo",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # Unidade Tematica 5: Educacao Social e Financeira (pp. 62-63+)
        # ---------------------------------------------------------------
        {
            "id": "u5",
            "titulo": "Educação Social e Financeira",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Necessidades, desejos e poupança",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Necessidade é tudo o que:",
                            "options": [
                                "É indispensável para a nossa vida",
                                "Nos apetece ter",
                                "Custa mais dinheiro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Comprar comida para casa é:",
                            "options": ["Uma necessidade", "Um desejo", "Uma poupança"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quando temos pouco dinheiro, primeiro pagamos:",
                            "options": [
                                "As necessidades",
                                "Os desejos",
                                "O que for mais caro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Poupar é:",
                            "options": [
                                "Guardar dinheiro para depois",
                                "Gastar tudo hoje",
                                "Pedir emprestado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada gasto ao que ele é.",
                            "pairs": [
                                ["Remédio para a febre", "Necessidade"],
                                ["Brinquedo novo", "Desejo"],
                            ],
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

    # A seguir ao cn-4c, para a 4a classe ficar com a mesma ordem da 5a e
    # da 6a: Matematica, Portugues, Ciencias Naturais, Ciencias Sociais.
    onde = ids.index("cn-4c") + 1
    dados["cursos"].insert(onde, CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta ao tools/materia_texto.py e corre "
          "python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
