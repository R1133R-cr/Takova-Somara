# -*- coding: utf-8 -*-
"""O curso de Educacao Visual da 7a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Educacao Visual -- Ensino
     Secundario -- 1o Ciclo", INDE/MINEDH, Maputo, Setembro de 2024.
     Descarregado do educador.mozestuda.com.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

A quarta Educacao Visual da app -- e a primeira com fonte
----------------------------------------------------------
As da 4a, 5a e 6a classes vieram de manuais escolares, e a da 4a nem
isso: e o unico curso da app montado SEM documento nenhum, e esta marcado
como provisorio. Esta tem programa oficial.

As cinco unidades tematicas, tal como o INDE as ordena
-------------------------------------------------------
    1  Introducao ao estudo da Arte             definicao, formas de
                                                expressao, artistas
                                                mocambicanos
    2  Suportes e Materiais                     caderno de esbocos, gode,
                                                quadro de cartao, relevo
    3  Materiais e Tecnicas de Expressao        suportes, riscadores,
       Grafica                                  desenho, pintura, tecnica
                                                mista
    4  Comunicacao Visual                       codigos visuais, cartazes,
                                                banda desenhada
    5  Desenho Geometrico                       normalizacao, esquadria,
                                                legenda, letras

O que uma app nao consegue avaliar nesta disciplina
----------------------------------------------------
Metade do programa e FAZER: produzir um caderno de esbocos, um gode de
material reciclavel, um quadro em relevo, um painel colectivo. Isso
avalia-se com o trabalho na mao, e nao com uma pergunta de escolha
multipla.

O que aqui se avalia e o SABER que sustenta o fazer: que material serve
para que, que tecnica se chama como, que regra de seguranca se aplica,
que artista fez o que. E a mesma limitacao que a Educacao Visual do
primario ja tinha, e continua dita.

Correr a partir de somara-flutter/:
    python tools/conteudo_ev7c.py            # so mostra
    python tools/conteudo_ev7c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Educação Visual — Ensino "
    "Secundário, 1º Ciclo. INDE/MINEDH, Maputo, Setembro de 2024. As "
    "cinco unidades temáticas e os conteúdos são do programa. Metade "
    "deste programa é produzir trabalhos com as mãos, e isso avalia-se "
    "com o trabalho à frente; aqui avalia-se o saber que o sustenta. Os "
    "exercícios foram escritos a partir dos conteúdos, porque um programa "
    "de ensino não traz exercícios e não há livro do aluno da 7ª classe "
    "publicado."
)

CURSO = {
    "id": "ev-7c",
    "disciplina": "Educação Visual",
    "classe": "7ª classe",
    "tag": "EV",
    "abrev": "Ed. Visual",
    "fonte": FONTE,
    "units": [
        {
            "id": "u1",
            "titulo": "Introdução ao estudo da Arte",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O que é a Arte",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Arte é sobretudo:",
                            "options": [
                                "Uma forma de o ser humano se exprimir e "
                                "comunicar",
                                "Um passatempo sem utilidade",
                                "Uma cópia exacta da realidade",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas NÃO é uma forma de expressão "
                                 "artística?",
                            "options": [
                                "A contabilidade",
                                "A escultura",
                                "A pintura",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A cerâmica é a arte de trabalhar:",
                            "options": ["A argila", "A madeira", "O metal"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A arquitectura é a arte de:",
                            "options": [
                                "Conceber edifícios e espaços",
                                "Pintar quadros",
                                "Fazer música",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Artistas moçambicanos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Malangatana Valente Ngwenya ficou "
                                 "conhecido sobretudo como:",
                            "options": ["Pintor", "Músico", "Escritor"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Alberto Chissano destacou-se na:",
                            "options": ["Escultura", "Pintura", "Fotografia"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Reinata Sadimba é conhecida pelo seu "
                                 "trabalho em:",
                            "options": ["Cerâmica", "Arquitectura", "Música"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "José Forjaz é um nome ligado à:",
                            "options": ["Arquitectura", "Escultura", "Pintura"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada artista à sua forma de expressão.",
                            "pairs": [
                                ["Malangatana", "Pintura"],
                                ["Chissano", "Escultura"],
                            ],
                        },
                    ],
                },
            ],
        },
        {
            "id": "u2",
            "titulo": "Suportes e materiais",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O caderno de esboços e o godê",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um caderno de esboços serve para:",
                            "options": [
                                "Registar ideias e experiências gráficas",
                                "Passar os trabalhos a limpo",
                                "Guardar as notas dos testes",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um godê é um recipiente que serve para:",
                            "options": [
                                "Preparar e misturar tintas",
                                "Guardar lápis",
                                "Medir ângulos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Fazer um godê com tampas de plástico "
                                 "usadas é um exemplo de:",
                            "options": [
                                "Reaproveitamento de material",
                                "Desperdício",
                                "Desenho geométrico",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O cartão é muito usado como suporte "
                                 "porque:",
                            "options": [
                                "É resistente, barato e fácil de encontrar",
                                "É o único material que existe",
                                "Não se pode pintar",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "O relevo e a segurança no trabalho",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um quadro em relevo distingue-se de um "
                                 "quadro pintado porque:",
                            "options": [
                                "Tem partes salientes que se sentem ao toque",
                                "É sempre maior",
                                "Não tem cor",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma composição abstracta é aquela que:",
                            "options": [
                                "Não representa objectos reconhecíveis",
                                "Copia a realidade tal como é",
                                "Só usa uma cor",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao usar cola de secagem rápida, deve-se:",
                            "options": [
                                "Trabalhar em local arejado e não tocar nos "
                                "olhos",
                                "Cheirar de perto para testar",
                                "Aquecer a embalagem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Depois de um trabalho de recorte e "
                                 "colagem, deve-se:",
                            "options": [
                                "Arrumar as ferramentas e limpar o espaço",
                                "Deixar tudo como está",
                                "Guardar a tesoura aberta",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u3",
            "titulo": "Materiais e técnicas de expressão gráfica",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Suportes e riscadores",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Qual destes é um suporte, e não um "
                                 "riscador?",
                            "options": ["A cartolina", "O lápis", "O carvão"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um riscador?",
                            "options": ["O giz", "O papel", "A parede"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O carvão é apreciado no desenho porque:",
                            "options": [
                                "Dá traços intensos e esbate-se com facilidade",
                                "Nunca suja as mãos",
                                "É o mais fino de todos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Escolher o material certo para um trabalho "
                                 "depende:",
                            "options": [
                                "Do resultado que se quer obter",
                                "Só do preço",
                                "Só do tamanho do papel",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "As técnicas de expressão gráfica",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O desenho de observação é aquele que se "
                                 "faz:",
                            "options": [
                                "Olhando para o objecto real",
                                "De memória",
                                "Copiando de um livro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O pontilhismo é uma técnica em que a "
                                 "imagem se forma com:",
                            "options": [
                                "Pequenos pontos de cor",
                                "Linhas contínuas",
                                "Manchas sopradas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na pintura soprada, a tinta espalha-se:",
                            "options": [
                                "Com o sopro, muitas vezes através de uma "
                                "palhinha",
                                "Com o pincel apenas",
                                "Com os dedos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A técnica mista consiste em:",
                            "options": [
                                "Combinar vários materiais e técnicas no "
                                "mesmo trabalho",
                                "Usar só lápis de cor",
                                "Misturar duas cores",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um painel colectivo é um trabalho:",
                            "options": [
                                "Feito por várias pessoas em conjunto",
                                "Feito por uma pessoa só",
                                "Feito apenas com fotografias",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u4",
            "titulo": "Comunicação visual",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Códigos visuais",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A comunicação visual transmite mensagens "
                                 "através:",
                            "options": [
                                "De imagens, sinais e símbolos",
                                "Apenas da palavra escrita",
                                "Apenas do som",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um sinal de trânsito é um exemplo de:",
                            "options": [
                                "Código visual",
                                "Banda desenhada",
                                "Técnica mista",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um ícone é um sinal que:",
                            "options": [
                                "Se parece com aquilo que representa",
                                "Não tem relação com o que representa",
                                "Só se usa em texto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um bom código visual deve ser:",
                            "options": [
                                "Simples e compreendido à primeira",
                                "Complicado, para chamar a atenção",
                                "Sempre a preto e branco",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Cartazes e banda desenhada",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um cartaz eficaz tem:",
                            "options": [
                                "Pouco texto, imagem forte e letra legível ao "
                                "longe",
                                "Muito texto pequeno",
                                "Imagens sem relação com a mensagem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na banda desenhada, o texto do que uma "
                                 "personagem diz aparece:",
                            "options": [
                                "Num balão",
                                "No título",
                                "Na legenda do autor",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Cada quadrado de uma banda desenhada "
                                 "chama-se:",
                            "options": ["Vinheta", "Balão", "Painel colectivo"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um cartaz sobre igualdade de género serve "
                                 "para:",
                            "options": [
                                "Fazer pensar e mudar comportamentos",
                                "Decorar a parede apenas",
                                "Vender um produto",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u5",
            "titulo": "Desenho geométrico",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A normalização",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "O desenho geométrico serve sobretudo para:",
                            "options": [
                                "Representar objectos com rigor e medidas",
                                "Exprimir emoções",
                                "Pintar paisagens",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A normalização no desenho técnico serve "
                                 "para:",
                            "options": [
                                "Que todos entendam o desenho da mesma "
                                "maneira",
                                "Tornar o desenho mais bonito",
                                "Poupar papel",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A esquadria de uma folha de desenho é:",
                            "options": [
                                "A moldura traçada junto às margens",
                                "Um instrumento de medida",
                                "O título do trabalho",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A legenda de uma folha de desenho técnico "
                                 "contém:",
                            "options": [
                                "A identificação do trabalho e de quem o fez",
                                "Um desenho decorativo",
                                "As cores usadas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Letras e algarismos normalizados",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As letras do desenho técnico devem ser:",
                            "options": [
                                "Simples, iguais e fáceis de ler",
                                "Decoradas e diferentes umas das outras",
                                "Escritas à pressa",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa folha de desenho técnico, a legenda "
                                 "coloca-se normalmente:",
                            "options": [
                                "No canto inferior direito",
                                "No meio da folha",
                                "Fora da esquadria",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Escrever à mão livre num desenho técnico, "
                                 "sem respeitar a normalização:",
                            "options": [
                                "Torna o desenho difícil de interpretar",
                                "Não tem importância",
                                "Melhora a leitura",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de começar um desenho técnico, a "
                                 "primeira coisa a traçar é:",
                            "options": [
                                "A esquadria",
                                "A legenda",
                                "O desenho em si",
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
