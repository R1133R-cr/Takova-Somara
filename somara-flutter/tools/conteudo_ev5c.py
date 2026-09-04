# -*- coding: utf-8 -*-
"""O curso de Educacao Visual e Oficios da 5a classe.

De onde vem
-----------
Do livro "EVO -- Educacao Visual e Oficios da 5a Classe", 2023, em

    Documents\\planos da 5a classe\\Livros\\5a classe\\
    EV _ Oficios da 5a Classe 2023 (MozEstuda.com).pdf

AVISO SOBRE A FONTE: o MozEstuda e um portal privado, nao e o MINEDH. Ver
o cabecalho do conteudo_por4c.py.

O que distingue esta da 6a classe
---------------------------------
A da 6a e sobretudo desenho, pintura e COR. Esta e sobretudo OFICIO:
modelagem em barro, tecelagem, cestaria -- o trabalho das maos que se faz
nas zonas rurais de Mocambique.

E por isso NAO tem perguntas de cor, apesar de a maquinaria de mostrar cor
ja estar construida e ser tentador usa-la. Procurei no livro: "cores
primarias" zero ocorrencias, "circulo cromatico" zero. A teoria da cor
entra na 6a classe, e poe-la aqui era inventar curriculo -- que e
exactamente o que descarregar os livros serviu para evitar.

O que o livro ensina, e esta aqui
---------------------------------
    modelagem   dar forma a uma materia-prima modelavel
    moldagem    reproduzir um objecto atraves de um MOLDE
    o barro     limpar, peneirar, misturar com agua, amassar, conservar
    fibras      naturais (algodao, sisal, la, linho)
                artificiais (nylon, acrilico)
                reciclaveis (fios de sacos e de cintas de embalagens)
    cestaria    palha, bambu, fitas de plastico -- cestos, chapeus,
                peneiras, esteiras

Os passos de preparar o barro sao do livro, pela ordem em que la estao. A
ordem importa: barro que nao foi peneirado tem pedras, e barro que nao foi
amassado cola-se as maos.

Correr a partir de somara-flutter/:
    python tools/conteudo_ev5c.py            # so mostra
    python tools/conteudo_ev5c.py --gravar
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

CURSO = {
    "id": "ev-5c",
    "disciplina": "Educação Visual e Ofícios",
    "abrev": "Ed. Visual",
    "classe": "5ª classe",
    "tag": "EV",
    "units": [
        # ---------------------------------------------------------------
        # 1: Desenho e Pintura
        # ---------------------------------------------------------------
        {
            "id": "u1",
            "titulo": "Desenho e Pintura",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Higiene e segurança",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Antes da aula de desenho, deves verificar se:",
                            "options": [
                                "Tens os lápis afiados",
                                "O quadro está limpo",
                                "Há luz na sala",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de pintar, a mesa deve ser:",
                            "options": [
                                "Forrada, para não se sujar",
                                "Molhada",
                                "Encostada à parede",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O espaço de trabalho limpa-se:",
                            "options": [
                                "Constantemente, e fica pronto para a aula seguinte",
                                "Uma vez por mês",
                                "Só quando o professor manda",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os materiais de uma actividade juntam-se:",
                            "options": [
                                "Antes de a começar",
                                "A meio, quando faltarem",
                                "No fim",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Tipos de desenho",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Desenhar aquilo que se tem à frente chama-se desenho:",
                            "options": ["De observação", "Com tema dado", "Livre"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quando o professor diz o assunto, o desenho é:",
                            "options": ["Com tema dado", "De observação", "Livre"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma ilustração serve para:",
                            "options": [
                                "Acompanhar e explicar um texto",
                                "Substituir o texto",
                                "Decorar a capa apenas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um painel colectivo é feito:",
                            "options": [
                                "Por vários alunos, em conjunto",
                                "Por um aluno só",
                                "Pelo professor",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # 2: Impressao, recorte e dobragem
        # ---------------------------------------------------------------
        {
            "id": "u2",
            "titulo": "Impressão, recorte e dobragem",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Imprimir e estampar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um carimbo serve para:",
                            "options": [
                                "Repetir o mesmo desenho muitas vezes",
                                "Cortar o papel em tiras",
                                "Colar duas folhas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Estampar é passar um desenho:",
                            "options": [
                                "De uma superfície para outra",
                                "De uma cor para outra",
                                "De um livro para a cabeça",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um carimbo pode fazer-se com:",
                            "options": [
                                "Uma batata cortada ao meio",
                                "Uma folha de papel",
                                "Um copo de água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de estampar põe-se por baixo:",
                            "options": [
                                "Uma protecção, para não sujar a mesa",
                                "Mais tinta",
                                "Nada",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Recortar, colar e dobrar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Ao passar a tesoura a um colega, seguras:",
                            "options": [
                                "Pelas pontas, dando-lhe o cabo",
                                "Pelo cabo, dando-lhe as pontas",
                                "Atiras devagar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na dobragem, o papel é:",
                            "options": [
                                "Dobrado, sem se cortar",
                                "Cortado ao meio",
                                "Molhado primeiro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Picotar é fazer no papel:",
                            "options": [
                                "Muitos furos pequenos seguidos",
                                "Um corte só",
                                "Uma dobra ao meio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa colagem, a cola põe-se:",
                            "options": [
                                "Pouca e bem espalhada",
                                "Muita, aos montes",
                                "Só num canto",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # 3: Modelagem
        # ---------------------------------------------------------------
        {
            "id": "u3",
            "titulo": "Modelagem",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Modelar e moldar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Modelagem é a técnica que permite:",
                            "options": [
                                "Dar forma a uma matéria-prima modelável",
                                "Cortar madeira",
                                "Tecer fios",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Moldagem é reproduzir um objecto através de:",
                            "options": ["Um molde", "Um desenho", "Uma fotografia"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual é a vantagem da modelagem?",
                            "options": [
                                "Vê-se o objecto de todos os lados",
                                "É mais rápida que o desenho",
                                "Não suja as mãos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antigamente, a modelagem fazia-se sobretudo com:",
                            "options": ["Barro", "Plástico", "Vidro"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada técnica ao que ela faz.",
                            "pairs": [
                                ["Modelagem", "Dar forma"],
                                ["Moldagem", "Reproduzir com molde"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Preparar o barro",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Para tirar as pedras do barro, usa-se:",
                            "options": ["Uma rede, para peneirar", "Água a ferver", "Cola"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Depois de misturar o barro com água, é preciso:",
                            "options": [
                                "Amassar, até a massa ficar homogénea",
                                "Deixar secar ao sol",
                                "Pintar logo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Amassa-se o barro até ele:",
                            "options": [
                                "Não se colar às mãos",
                                "Ficar muito mole",
                                "Ficar duro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para o barro não secar até ao próximo trabalho, guarda-se:",
                            "options": [
                                "Num plástico",
                                "Ao sol",
                                "Num prato aberto",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # 4: Tecelagem e cestaria
        # ---------------------------------------------------------------
        {
            "id": "u4",
            "titulo": "Tecelagem e cestaria",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "As fibras",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As fibras naturais são as que:",
                            "options": [
                                "Se extraem da natureza",
                                "Se fazem na fábrica",
                                "Se compram na loja",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas é uma fibra natural?",
                            "options": ["Sisal", "Nylon", "Acrílico"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O nylon é uma fibra:",
                            "options": ["Artificial", "Natural", "Reciclável"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os fios dos sacos de comida, reaproveitados, são fibras:",
                            "options": ["Recicláveis", "Naturais", "Artificiais"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada fibra ao seu tipo.",
                            "pairs": [
                                ["Algodão", "Natural"],
                                ["Nylon", "Artificial"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Tecer e entrelaçar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Tecer é:",
                            "options": [
                                "Entrelaçar fios",
                                "Colar fios",
                                "Cortar fios",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A cestaria usa o mesmo processo da tecelagem:",
                            "options": [
                                "Entrelaçar",
                                "Modelar",
                                "Estampar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes materiais se usa na cestaria?",
                            "options": ["A palha", "O barro", "O gesso"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um produto de cestaria?",
                            "options": ["Uma peneira", "Um vaso de barro", "Um postal"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A tecelagem é muito usada, sobretudo:",
                            "options": [
                                "Nas zonas rurais",
                                "Nas fábricas da cidade",
                                "Nas escolas",
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

    niveis = sum(len(u["niveis"]) for u in CURSO["units"])
    perguntas = sum(len(n["questoes"])
                    for u in CURSO["units"] for n in u["niveis"])
    print(f"{CURSO['disciplina']} da {CURSO['classe']}")
    print(f"  {len(CURSO['units'])} unidades, {niveis} niveis, {perguntas} perguntas")
    for u in CURSO["units"]:
        print(f"   {u['id']}  {u['titulo']}")
        for n in u["niveis"]:
            print(f"       {n['id']}  {n['titulo']:<26}{len(n['questoes'])}q")

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

    onde = ids.index("cs-5c") + 1
    dados["cursos"].insert(onde, CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    print("Falta a materia: acrescenta ao tools/materia_texto.py e corre "
          "python tools/materia.py --gravar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
