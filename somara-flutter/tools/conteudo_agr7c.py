# -*- coding: utf-8 -*-
"""O curso de Agropecuaria da 7a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Agropecuaria -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024.
     Descarregado do educador.mozestuda.com.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

Nove unidades no INDE, cinco no curso
--------------------------------------
    1  Introducao ao estudo de Agricultura
    2  Preparacao do Solo
    3  Propagacao de plantas
    4  Praticas Culturais
    5  Colheita e Armazenamento
    6  Introducao ao estudo da Pecuaria
    7  Criacao de galinhas
    8  Criacao de patos
    9  Criacao de perus

As tres ultimas sao a mesma coisa com tres aves: instalacao, alimentacao,
maneio, doencas. Juntam-se numa unidade de avicultura, com um nivel para
o que e comum e outro para o que distingue cada ave -- em vez de tres
unidades quase iguais. E a 2 junta-se a 3, porque preparar o terreno e
por la a planta sao o mesmo momento do trabalho.

    u1  1        conceito, importancia, sistemas agrarios
    u2  2 + 3    solo, preparacao, sementeira, propagacao
    u3  4        praticas culturais: rega, sacha, adubacao, pragas
    u4  5        colheita, secagem, armazenamento, perdas
    u5  6+7+8+9  pecuaria e criacao de galinhas, patos e perus

Correr a partir de somara-flutter/:
    python tools/conteudo_agr7c.py            # so mostra
    python tools/conteudo_agr7c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Agropecuária — Ensino "
    "Secundário, 1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024. As nove "
    "unidades do programa estão em cinco: a preparação do solo junta-se à "
    "propagação de plantas, e as três unidades de criação de aves — "
    "galinhas, patos e perus — juntam-se numa de avicultura, porque "
    "tratam do mesmo com três aves. Os exercícios foram escritos a partir "
    "dos conteúdos, porque um programa de ensino não traz exercícios e "
    "não há livro do aluno da 7ª classe publicado."
)

CURSO = {
    "id": "agr-7c",
    "disciplina": "Agropecuária",
    "classe": "7ª classe",
    "tag": "AGR",
    "fonte": FONTE,
    "units": [
        {
            "id": "u1",
            "titulo": "Introdução ao estudo da agricultura",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O que é a agricultura",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A agricultura é a actividade de:",
                            "options": [
                                "Cultivar plantas e criar animais",
                                "Vender produtos no mercado",
                                "Transportar mercadorias",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A agricultura é importante para Moçambique "
                                 "sobretudo porque:",
                            "options": [
                                "Garante alimento e emprego à maioria da "
                                "população",
                                "Só serve para exportar",
                                "Não tem importância económica",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Chama-se segurança alimentar a:",
                            "options": [
                                "Todos terem acesso a alimento suficiente e "
                                "seguro",
                                "Guardar as sementes num cofre",
                                "Vender toda a colheita",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A pecuária é a parte da agropecuária que "
                                 "trata:",
                            "options": [
                                "Da criação de animais",
                                "Do cultivo de cereais",
                                "Da venda de adubos",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Os sistemas agrários",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Na agricultura de subsistência, o que se "
                                 "produz destina-se sobretudo:",
                            "options": [
                                "Ao consumo da própria família",
                                "À exportação",
                                "À indústria",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No sistema de rendimento, o agricultor "
                                 "produz sobretudo para:",
                            "options": [
                                "Vender e obter lucro",
                                "Comer em casa",
                                "Oferecer aos vizinhos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O sistema agro-industrial caracteriza-se "
                                 "por:",
                            "options": [
                                "Grande escala, máquinas e ligação à "
                                "indústria",
                                "Enxada e trabalho familiar",
                                "Produzir só para a aldeia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A distribuição agro-ecológica das culturas "
                                 "explica porque:",
                            "options": [
                                "Cada cultura se dá melhor numa região do país",
                                "Todas as culturas crescem em todo o lado",
                                "As culturas não dependem do clima",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u2",
            "titulo": "O solo e a propagação de plantas",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Preparar o solo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Preparar o solo antes de semear serve "
                                 "para:",
                            "options": [
                                "Deixar a terra solta, limpa e pronta a "
                                "receber a semente",
                                "Endurecer a terra",
                                "Tirar toda a matéria orgânica",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A lavoura, ou primeira mobilização do "
                                 "solo, serve para:",
                            "options": [
                                "Revolver a terra e enterrar as ervas",
                                "Espalhar as sementes",
                                "Colher os frutos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A queimada como forma de limpar a "
                                 "machamba:",
                            "options": [
                                "Empobrece o solo e deve ser evitada",
                                "Melhora sempre o solo",
                                "Não tem efeito nenhum",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um solo com muita matéria orgânica é, em "
                                 "geral:",
                            "options": [
                                "Mais fértil",
                                "Menos fértil",
                                "Impróprio para cultivo",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Semear e propagar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A propagação por semente chama-se:",
                            "options": [
                                "Propagação sexuada",
                                "Propagação vegetativa",
                                "Enxertia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Plantar um pedaço de caule de mandioca "
                                 "para dar uma planta nova é:",
                            "options": [
                                "Propagação vegetativa",
                                "Propagação por semente",
                                "Sementeira directa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um viveiro serve para:",
                            "options": [
                                "Criar as plantas pequenas antes de as levar "
                                "para o campo",
                                "Guardar a colheita",
                                "Criar animais",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O compasso de sementeira é:",
                            "options": [
                                "A distância entre as plantas e entre as "
                                "linhas",
                                "A profundidade do sulco",
                                "A hora de semear",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Semear demasiado junto faz com que as "
                                 "plantas:",
                            "options": [
                                "Compitam por luz, água e nutrientes",
                                "Cresçam mais depressa",
                                "Dêem mais fruto",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u3",
            "titulo": "Práticas culturais",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Regar, sachar e adubar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Sachar a machamba serve para:",
                            "options": [
                                "Tirar as ervas daninhas e arejar o solo",
                                "Regar as plantas",
                                "Colher os frutos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As ervas daninhas prejudicam a cultura "
                                 "porque:",
                            "options": [
                                "Competem por água, luz e nutrientes",
                                "Dão sombra útil",
                                "Adubam o solo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A melhor altura para regar, em dias de "
                                 "muito calor, é:",
                            "options": [
                                "De manhã cedo ou ao fim da tarde",
                                "Ao meio-dia",
                                "Só quando a planta murchar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O estrume de curral é um adubo:",
                            "options": ["Orgânico", "Químico", "Mineral"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Pragas e doenças",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma praga agrícola é:",
                            "options": [
                                "Um organismo que ataca e prejudica a cultura",
                                "Uma doença do solo",
                                "Uma falta de chuva",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A rotação de culturas ajuda a controlar as "
                                 "pragas porque:",
                            "options": [
                                "Quebra o ciclo de vida dos que atacam sempre "
                                "a mesma planta",
                                "Mata todos os insectos",
                                "Aumenta o uso de pesticidas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao aplicar um pesticida, é obrigatório:",
                            "options": [
                                "Usar protecção e respeitar as instruções do "
                                "rótulo",
                                "Aplicar mais do que o indicado",
                                "Trabalhar contra o vento sem máscara",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Consociar culturas, como milho com feijão, "
                                 "ajuda porque:",
                            "options": [
                                "Aproveita melhor o terreno e protege o solo",
                                "Aumenta as pragas",
                                "Impede o crescimento das duas",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u4",
            "titulo": "Colheita e armazenamento",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A colheita",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Colher antes do ponto certo faz com que o "
                                 "produto:",
                            "options": [
                                "Fique de pior qualidade e se conserve mal",
                                "Dure mais tempo",
                                "Fique mais saboroso",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Depois de colhido, o milho deve primeiro:",
                            "options": [
                                "Ser bem seco",
                                "Ser guardado húmido",
                                "Ser lavado com água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Guardar grão húmido no celeiro provoca:",
                            "options": [
                                "Bolor e perda da colheita",
                                "Melhor conservação",
                                "Mais peso útil",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As perdas pós-colheita são:",
                            "options": [
                                "O que se estraga depois de colhido",
                                "O que não nasceu",
                                "O que se vendeu barato",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Armazenar bem",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um bom celeiro deve ser:",
                            "options": [
                                "Seco, arejado e protegido de roedores",
                                "Fechado e húmido",
                                "Aberto ao chão",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Levantar o celeiro do chão serve para:",
                            "options": [
                                "Impedir a humidade e a entrada de roedores",
                                "Facilitar a colheita",
                                "Poupar material",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O gorgulho é:",
                            "options": [
                                "Uma praga do grão armazenado",
                                "Uma doença das folhas",
                                "Um tipo de adubo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Guardar semente para a próxima campanha "
                                 "exige escolher:",
                            "options": [
                                "Os grãos maiores, sãos e bem secos",
                                "Os grãos partidos",
                                "Os grãos com bolor",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u5",
            "titulo": "Pecuária e criação de aves",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Introdução à pecuária",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A pecuária é a criação de animais para:",
                            "options": [
                                "Obter carne, leite, ovos e outros produtos",
                                "Companhia apenas",
                                "Transporte apenas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Chama-se maneio ao conjunto de:",
                            "options": [
                                "Cuidados diários com os animais",
                                "Doenças dos animais",
                                "Rações compradas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A vacinação dos animais serve para:",
                            "options": [
                                "Prevenir doenças",
                                "Os engordar",
                                "Aumentar a postura",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um animal doente deve ser:",
                            "options": [
                                "Separado dos outros e tratado",
                                "Mantido junto do rebanho",
                                "Vendido depressa",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Criar galinhas, patos e perus",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um bom galinheiro deve ser sobretudo:",
                            "options": [
                                "Seco, arejado e limpo",
                                "Húmido e fechado",
                                "Sem cobertura",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As galinhas criadas para pôr ovos "
                                 "chamam-se:",
                            "options": [
                                "Poedeiras",
                                "Frangos de corte",
                                "Pintos do dia",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A doença de Newcastle ataca sobretudo:",
                            "options": ["As aves", "Os bovinos", "As cabras"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O que os patos precisam e as galinhas não "
                                 "é:",
                            "options": [
                                "Acesso a água para nadar",
                                "Comida",
                                "Abrigo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Comparado com a galinha, o peru "
                                 "distingue-se por:",
                            "options": [
                                "Ser maior e demorar mais tempo a crescer",
                                "Crescer mais depressa",
                                "Pôr mais ovos por ano",
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
