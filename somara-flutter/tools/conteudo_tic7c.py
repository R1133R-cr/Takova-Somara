# -*- coding: utf-8 -*-
"""O curso de TIC da 7a classe.

De onde vem
-----------
    "Programa de Ensino da Disciplina de Tecnologias de Informacao e
     Comunicacao -- 7a e 8a Classe", INDE/MINEDH, Maputo, Setembro de
     2024. Descarregado do educador.mozestuda.com.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

Uma disciplina pratica que na 7a classe e teorica -- e o programa diz
--------------------------------------------------------------------
O programa e explicito: "A disciplina das TIC tem como principal
caracteristica actividades praticas. Entretanto, a nivel da 7a classe,
cinge-se a teoria que servira de suporte para as actividades praticas as
quais o aluno sera submetido a partir da 10a classe."

Isso resolve a duvida que esta disciplina levantaria numa app: nao ha
aqui um computador para usar, e na 7a classe tambem nao ha na aula. O que
se pede e o vocabulario e os conceitos -- e e isso que o curso da.

As tres unidades tematicas, tal como o INDE as ordena
------------------------------------------------------
    1  TIC e Componentes Basicos de Sistemas Computacionais
    2  Comunicacao e Cidadania Digital
    3  Introducao a CiberSeguranca e Aplicacoes de TIC

Tres unidades, tres niveis cada.

Correr a partir de somara-flutter/:
    python tools/conteudo_tic7c.py            # so mostra
    python tools/conteudo_tic7c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino da Disciplina de Tecnologias de Informação e "
    "Comunicação, 7ª e 8ª Classe. INDE/MINEDH, Maputo, Setembro de 2024. "
    "As três unidades temáticas e os conteúdos são do programa, que diz "
    "expressamente que na 7ª classe a disciplina «cinge-se à teoria que "
    "servirá de suporte para as actividades práticas». Os exercícios "
    "foram escritos a partir dos conteúdos, porque um programa de ensino "
    "não traz exercícios e não há livro do aluno da 7ª classe publicado."
)

CURSO = {
    "id": "tic-7c",
    "disciplina": "TIC",
    "classe": "7ª classe",
    "tag": "TIC",
    "fonte": FONTE,
    "units": [
        {
            "id": "u1",
            "titulo": "As TIC e o computador",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O que são as TIC",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A sigla TIC quer dizer:",
                            "options": [
                                "Tecnologias de Informação e Comunicação",
                                "Técnicas de Informática e Cálculo",
                                "Trabalho, Investigação e Ciência",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As TIC servem sobretudo para:",
                            "options": [
                                "Tratar, guardar e transmitir informação",
                                "Fabricar máquinas agrícolas",
                                "Construir estradas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes NÃO é um dispositivo "
                                 "computacional?",
                            "options": [
                                "Uma enxada",
                                "Um smartphone",
                                "Uma calculadora científica",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "As TIC mudaram a sociedade sobretudo "
                                 "porque:",
                            "options": [
                                "Aproximaram as pessoas e aceleraram o acesso "
                                "à informação",
                                "Acabaram com o trabalho",
                                "Tornaram os livros inúteis",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Hardware e software",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Chama-se hardware:",
                            "options": [
                                "À parte física do computador, que se toca",
                                "Aos programas",
                                "Aos ficheiros guardados",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Chama-se software:",
                            "options": [
                                "Aos programas que dizem ao computador o que "
                                "fazer",
                                "Ao teclado e ao rato",
                                "Ao ecrã",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um dispositivo de entrada?",
                            "options": ["O teclado", "O monitor", "A impressora"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destes é um dispositivo de saída?",
                            "options": ["O monitor", "O rato", "O microfone"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O sistema operativo é um software:",
                            "options": [
                                "De propósito geral, que faz o computador "
                                "funcionar",
                                "De propósito específico",
                                "Que é hardware",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Cuidar dos dispositivos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As regras ergonómicas servem para:",
                            "options": [
                                "Evitar dores e lesões ao usar o computador",
                                "Fazer o computador correr mais depressa",
                                "Poupar electricidade",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao trabalhar ao computador, o ecrã deve "
                                 "ficar:",
                            "options": [
                                "À altura dos olhos, a cerca de um braço de "
                                "distância",
                                "Muito abaixo, para baixar a cabeça",
                                "O mais perto possível dos olhos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para proteger um computador da poeira e do "
                                 "calor, deve-se:",
                            "options": [
                                "Mantê-lo limpo e num local arejado",
                                "Tapá-lo com um pano enquanto trabalha",
                                "Pô-lo ao sol",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um equipamento informático velho e "
                                 "avariado deve:",
                            "options": [
                                "Ir para reciclagem própria de lixo "
                                "electrónico",
                                "Ser deitado no lixo comum",
                                "Ser queimado",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u2",
            "titulo": "Comunicação e cidadania digital",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Comunicar em rede",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A Internet é:",
                            "options": [
                                "Uma rede mundial que liga computadores entre "
                                "si",
                                "Um programa do computador",
                                "Um tipo de telemóvel",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Wi-Fi e Bluetooth são formas de ligação:",
                            "options": ["Sem fios", "Por cabo", "Por satélite"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um navegador, ou browser, serve para:",
                            "options": [
                                "Aceder a páginas da Internet",
                                "Escrever textos",
                                "Fazer contas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Nem tudo o que está na Internet é "
                                 "verdadeiro. Antes de acreditar, deve-se:",
                            "options": [
                                "Verificar a fonte e comparar com outras",
                                "Partilhar logo",
                                "Acreditar se tiver muitas partilhas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Cidadania digital",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Dados pessoais são:",
                            "options": [
                                "Informações que identificam uma pessoa",
                                "Ficheiros do sistema",
                                "Programas instalados",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Publicar uma fotografia de um colega sem "
                                 "lhe perguntar é:",
                            "options": [
                                "Uma violação da privacidade dele",
                                "Normal, se for engraçada",
                                "Permitido entre amigos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Se alguém te insultar ou ameaçar em linha, "
                                 "deves:",
                            "options": [
                                "Guardar a prova e contar a um adulto de "
                                "confiança",
                                "Responder da mesma maneira",
                                "Não fazer nada",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Copiar um texto da Internet e apresentá-lo "
                                 "como teu é:",
                            "options": [
                                "Plágio",
                                "Pesquisa",
                                "Citação",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "As TIC na aprendizagem",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma plataforma de apoio ao ensino serve "
                                 "para:",
                            "options": [
                                "Aceder a materiais e actividades de estudo",
                                "Jogar apenas",
                                "Comprar produtos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Usar o telemóvel para estudar é útil "
                                 "quando:",
                            "options": [
                                "Se procura informação com um objectivo claro",
                                "Se usa durante a aula sem autorização",
                                "Se copia tudo sem ler",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Jogos como a dama, o xadrez e o ntxuva "
                                 "ajudam a:",
                            "options": [
                                "Desenvolver o raciocínio e a estratégia",
                                "Perder tempo",
                                "Aprender a escrever",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um repositório de partilha de informação é:",
                            "options": [
                                "Um lugar em linha onde se guardam e "
                                "partilham materiais",
                                "Um tipo de computador",
                                "Uma rede sem fios",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        {
            "id": "u3",
            "titulo": "Cibersegurança e aplicações das TIC",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Senhas e controlo de acesso",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma senha segura deve:",
                            "options": [
                                "Ser longa, misturar letras e números e não "
                                "se partilhar",
                                "Ser a data de nascimento",
                                "Ser igual em todos os sítios",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Qual destas é a pior senha?",
                            "options": ["123456", "Ch7va#Lich", "Mz2024$xk"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Emprestar a tua senha a um colega:",
                            "options": [
                                "Põe em risco tudo o que está na tua conta",
                                "É seguro se for amigo",
                                "Não tem consequências",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Se receberes uma mensagem a pedir a tua "
                                 "senha, deves:",
                            "options": [
                                "Não responder: serviços sérios nunca a pedem",
                                "Responder depressa",
                                "Enviar só uma parte",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Proteger o dispositivo",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um vírus informático é:",
                            "options": [
                                "Um programa que danifica ou rouba dados",
                                "Uma peça avariada",
                                "Um tipo de ficheiro de texto",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Instalar aplicações só de lojas oficiais "
                                 "serve para:",
                            "options": [
                                "Reduzir o risco de instalar software malicioso",
                                "Poupar bateria",
                                "Ter mais espaço",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Deixar o Bluetooth sempre ligado e visível:",
                            "options": [
                                "Facilita ligações indesejadas ao teu aparelho",
                                "Melhora a segurança",
                                "Não tem risco nenhum",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Fazer cópias de segurança dos ficheiros "
                                 "serve para:",
                            "options": [
                                "Não perder o trabalho se o aparelho se "
                                "estragar",
                                "Deixar o aparelho mais rápido",
                                "Poupar dados móveis",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "As TIC no dia-a-dia",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "As TIC aplicadas à agricultura permitem, "
                                 "por exemplo:",
                            "options": [
                                "Consultar a previsão do tempo e preços de "
                                "mercado",
                                "Substituir a chuva",
                                "Dispensar a sementeira",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O dinheiro móvel, no telemóvel, permite:",
                            "options": [
                                "Enviar e receber dinheiro sem ir ao banco",
                                "Imprimir notas",
                                "Criar dinheiro novo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na saúde, as TIC ajudam sobretudo a:",
                            "options": [
                                "Guardar registos de doentes e ligar unidades "
                                "distantes",
                                "Substituir o médico",
                                "Curar doenças à distância sozinhas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A sigla STEM, ligada às TIC, junta:",
                            "options": [
                                "Ciências, Tecnologia, Engenharia e Matemática",
                                "Saúde, Trabalho, Escola e Música",
                                "Sociedade, Turismo, Economia e Meio ambiente",
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
