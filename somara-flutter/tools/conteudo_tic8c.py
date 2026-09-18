# -*- coding: utf-8 -*-
"""O curso de TIC da 8a classe -- o ultimo TIC do 1o ciclo.

De onde vem
-----------
    "Programa de Ensino de Tecnologias de Informacao e Comunicacao, 7a e
     8a Classe", INDE/MINEDH, Maputo, Setembro de 2024, 8a classe,
     pp. 26-33. Guardado em Documents\\planos da 5a classe\\Livros\\
     Programas INDE 1o Ciclo\\tic.pdf.

Programa e nao livro do aluno. Fica dito no campo `fonte`.

O programa e so da 7a e da 8a -- diz-o no titulo. A 9a nao tem TIC.

As tres unidades da 8a, pela ordem do programa
----------------------------------------------
    1  Componentes Basicos de Sistemas    classificacao de software;
       Computacionais                     software e direitos de autor;
                                          instalacao, virus, actualizacao
    2  Comunicacao e Cidadania Digital e  redes de computadores; servicos
       Introducao a CiberSeguranca        de rede e e-mail; nuvem;
                                          ciber-higiene e crime informatico
    3  Transaccoes electronicas e         transaccoes electronicas; a lei e
       Aplicacoes das TIC                 o comercio electronico; TIC na
                                          agricultura, na saude e no ambiente

Tres unidades, dez aulas.

As siglas
---------
"OSI" e "ATM" a voz leria como palavras. Ficam nas opcoes; nos
enunciados escreve-se "o modelo de sete camadas" e "a caixa automatica".
"E-mail" e "Wi-Fi" a voz diz bem e ficam.

Correr a partir de somara-flutter/:
    python tools/conteudo_tic8c.py            # so mostra
    python tools/conteudo_tic8c.py --gravar   # escreve e grava o audio
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Programa de Ensino de Tecnologias de Informação e Comunicação, 7ª e 8ª "
    "Classe. INDE/MINEDH, Maputo, Setembro de 2024, 8ª classe, pp. 26-33. "
    "As três unidades temáticas e os conteúdos são do programa; os "
    "exercícios foram escritos a partir deles, porque um programa de ensino "
    "não traz exercícios e não há livro do aluno da 8ª classe publicado."
)

CURSO = {
    "id": "tic-8c",
    "disciplina": "TIC",
    "classe": "8ª classe",
    "tag": "TIC",
    "fonte": FONTE,
    "units": [
        # ================================================================
        # 1  Componentes Basicos de Sistemas Computacionais
        # ================================================================
        {
            "id": "u1",
            "titulo": "Componentes básicos de sistemas computacionais",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "A classificação do software",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Sem software, o hardware:",
                            "options": [
                                "Não faz nada: é o software que lhe diz o "
                                "que fazer",
                                "Funciona na mesma",
                                "Fica mais rápido",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada software à sua classe.",
                            "pairs": [
                                ["Windows e Android", "Software operacional"],
                                ["Antivírus", "Software de protecção"],
                                ["Programa de contabilidade", "Software de gestão"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O sistema operativo é o software que:",
                            "options": [
                                "Arranca o computador e gere o hardware e "
                                "os outros programas",
                                "Só serve para jogar",
                                "Escreve cartas",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um controlador, ou driver, que faz a "
                                 "impressora funcionar é:",
                            "options": [
                                "Software básico",
                                "Software de gestão",
                                "Um vírus",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O software de gestão serve para:",
                            "options": [
                                "Organizar o trabalho de uma empresa ou "
                                "escola: contas, stocks, alunos",
                                "Proteger contra vírus",
                                "Arrancar o computador",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Software e direitos de autor",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Um programa de computador é obra de "
                                 "alguém e está protegido por:",
                            "options": [
                                "Direitos de autor",
                                "Nada: é de todos",
                                "A polícia de trânsito",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada tipo de software ao que ele "
                                 "permite.",
                            "pairs": [
                                ["Software livre", "Usar, estudar, alterar e partilhar"],
                                ["Software proprietário", "Usar só como o dono autoriza"],
                                ["Software comercial", "Usar depois de pagar a licença"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Copiar um programa pago e dá-lo a um "
                                 "amigo sem licença é:",
                            "options": [
                                "Pirataria: viola os direitos de autor",
                                "Partilha permitida",
                                "Software livre",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um software pode ser grátis e mesmo "
                                 "assim:",
                            "options": [
                                "Proprietário, se não se pode alterar nem "
                                "redistribuir",
                                "Só livre",
                                "Ilegal",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A licença de um software é:",
                            "options": [
                                "O acordo que diz o que se pode fazer com "
                                "ele",
                                "O preço do computador",
                                "A cor do ícone",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Instalar, proteger e actualizar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Antes de descarregar uma aplicação da "
                                 "Internet deve-se:",
                            "options": [
                                "Confirmar que vem da loja ou do sítio "
                                "oficial",
                                "Aceitar tudo sem ler",
                                "Desligar o antivírus",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um vírus informático é:",
                            "options": [
                                "Um programa malicioso que se copia e "
                                "estraga ou rouba dados",
                                "Uma doença do teclado",
                                "Uma actualização",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada passo da instalação de um "
                                 "antivírus à sua ordem.",
                            "pairs": [
                                ["Descarregar do sítio oficial", "Primeiro"],
                                ["Instalar e configurar", "Depois"],
                                ["Actualizar e analisar o disco", "Por fim"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Actualizar o software serve para:",
                            "options": [
                                "Corrigir erros e fechar falhas de "
                                "segurança",
                                "Ocupar mais espaço",
                                "Apagar os ficheiros",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma aplicação que pede acesso aos "
                                 "contactos, à câmara e às mensagens sem "
                                 "precisar deles:",
                            "options": [
                                "É suspeita: não se instala",
                                "É normal",
                                "É mais segura",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 2  Comunicacao e Cidadania Digital e Introducao a CiberSeguranca
        # ================================================================
        {
            "id": "u2",
            "titulo": "Comunicação, cidadania digital e cibersegurança",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Redes de computadores",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma rede de computadores é:",
                            "options": [
                                "Dois ou mais computadores ligados para "
                                "trocar dados",
                                "Um computador sozinho",
                                "Uma pasta de ficheiros",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A Internet nasceu de uma rede militar e "
                                 "universitária americana dos anos 60 e "
                                 "70 chamada:",
                            "options": ["ARPANET", "Wi-Fi", "Bluetooth"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada topologia à sua forma.",
                            "pairs": [
                                ["Estrela", "Todos ligados a um ponto central"],
                                ["Anel", "Cada um ligado ao seguinte, em círculo"],
                                ["Barramento", "Todos ligados a um só cabo"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O modelo de referência das redes em "
                                 "sete camadas chama-se:",
                            "options": ["Modelo OSI", "Modelo ATM", "Modelo USB"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada ligação ao seu tipo.",
                            "pairs": [
                                ["Wi-Fi", "Sem fios"],
                                ["Cabo de rede", "Com fios"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O aparelho que liga a rede da escola à "
                                 "Internet é:",
                            "options": ["O router", "O teclado", "A impressora"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Serviços de rede e correio electrónico",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada serviço de rede ao que ele faz.",
                            "pairs": [
                                ["Web", "Ver páginas no navegador"],
                                ["E-mail", "Enviar e receber mensagens"],
                                ["Transferência de ficheiros", "Enviar ficheiros entre computadores"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Num endereço de e-mail, o que vem "
                                 "depois da arroba é:",
                            "options": [
                                "O fornecedor do serviço",
                                "O nome da pessoa",
                                "A palavra-passe",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao usar o e-mail num computador da "
                                 "escola, no fim deve-se:",
                            "options": [
                                "Terminar a sessão",
                                "Deixar a conta aberta",
                                "Escrever a palavra-passe num papel colado "
                                "ao ecrã",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um e-mail de um desconhecido a pedir a "
                                 "palavra-passe ou dados do banco:",
                            "options": [
                                "É uma burla: não se responde nem se "
                                "clica nas ligações",
                                "Responde-se depressa",
                                "Reencaminha-se aos amigos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para enviar o mesmo e-mail a vários "
                                 "colegas usa-se:",
                            "options": [
                                "Vários destinatários, separados por "
                                "vírgulas",
                                "Vários computadores",
                                "Várias contas",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "Computação na nuvem",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Guardar ficheiros na nuvem é guardá-los:",
                            "options": [
                                "Em servidores na Internet, acessíveis de "
                                "qualquer aparelho",
                                "No céu",
                                "Só no telemóvel",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada operação na nuvem ao que ela é.",
                            "pairs": [
                                ["Upload", "Enviar um ficheiro para a nuvem"],
                                ["Download", "Trazer um ficheiro da nuvem"],
                                ["Partilhar", "Dar acesso a outra pessoa"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Uma vantagem da nuvem é:",
                            "options": [
                                "Se o telemóvel se perder, os ficheiros "
                                "continuam lá",
                                "Não precisar de Internet",
                                "Ser sempre grátis e sem limite",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma desvantagem da nuvem em Lichinga é:",
                            "options": [
                                "Precisa de Internet, e os dados pagam-se",
                                "Estraga o telemóvel",
                                "Apaga as fotografias",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Ao partilhar um ficheiro da nuvem "
                                 "deve-se:",
                            "options": [
                                "Dar acesso só a quem precisa",
                                "Tornar tudo público",
                                "Enviar a palavra-passe da conta",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n4",
                    "titulo": "Ciber-higiene e crime informático",
                    "questoes": [
                        {
                            "t": "match",
                            "q": "Liga cada conceito ao que ele é.",
                            "pairs": [
                                ["Ciberespaço", "O espaço das redes e da Internet"],
                                ["Cibercultura", "Os hábitos e valores de quem lá vive"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "Uma boa palavra-passe é:",
                            "options": [
                                "Comprida, com letras, números e sinais, e "
                                "diferente em cada conta",
                                "O nome da pessoa",
                                "Um, dois, três, quatro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma palavra-passe deve ter pelo menos "
                                 "oito caracteres. Se já tem 5, quantos "
                                 "faltam?",
                            "a": "3",
                        },
                        {
                            "t": "choice",
                            "q": "Ciber-higiene é:",
                            "options": [
                                "O conjunto de bons hábitos que mantêm as "
                                "contas e os aparelhos seguros",
                                "Limpar o ecrã com um pano",
                                "Lavar as mãos antes de usar o teclado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Entrar na conta de outra pessoa sem "
                                 "autorização ou roubar dados é:",
                            "options": [
                                "Crime informático, punido pela lei "
                                "moçambicana",
                                "Uma brincadeira",
                                "Permitido se for um amigo",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ================================================================
        # 3  Transaccoes electronicas e Aplicacoes das TIC
        # ================================================================
        {
            "id": "u3",
            "titulo": "Transacções electrónicas e aplicações das TIC",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Transacções electrónicas",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Uma transacção electrónica é:",
                            "options": [
                                "Um pagamento ou transferência feito por "
                                "meios digitais",
                                "Uma compra com dinheiro na mão",
                                "Uma carta pelo correio",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada meio ao que ele é.",
                            "pairs": [
                                ["M-Pesa e e-Mola", "Carteira móvel no telemóvel"],
                                ["ATM", "Caixa automática do banco"],
                                ["Cartão de débito", "Paga directamente da conta"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "O código secreto do cartão ou da "
                                 "carteira móvel:",
                            "options": [
                                "Nunca se diz a ninguém, nem a quem diz "
                                "ser do banco",
                                "Diz-se ao balconista",
                                "Escreve-se no cartão",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Na caixa automática, antes de sair "
                                 "deve-se:",
                            "options": [
                                "Levar o cartão e o dinheiro e conferir o "
                                "talão",
                                "Deixar o cartão lá dentro",
                                "Pedir ajuda a um desconhecido",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "input",
                            "q": "Uma mãe recebe 500 meticais na carteira "
                                 "móvel e paga 120 de electricidade. "
                                 "Quantos meticais lhe ficam?",
                            "a": "380",
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "A lei e o comércio electrónico",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Em Moçambique, as transacções "
                                 "electrónicas são reguladas pela Lei "
                                 "número 3 de 2017, de 9 de Janeiro, que:",
                            "options": [
                                "Dá valor legal aos documentos e "
                                "assinaturas electrónicos",
                                "Proíbe os pagamentos pelo telemóvel",
                                "Só fala de futebol",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Comércio electrónico é:",
                            "options": [
                                "Comprar e vender pela Internet",
                                "Vender no mercado da vila",
                                "Trocar produtos sem dinheiro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de comprar numa loja da Internet "
                                 "deve-se:",
                            "options": [
                                "Confirmar que a loja é conhecida e o "
                                "sítio é seguro",
                                "Pagar primeiro e ver depois",
                                "Enviar o cartão por mensagem",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma oferta na Internet que pede um "
                                 "pagamento adiantado para libertar um "
                                 "prémio é:",
                            "options": ["Uma burla", "Um bom negócio", "A lei"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Comprar pela Internet tem a vantagem de:",
                            "options": [
                                "Chegar a produtos que não há na vila",
                                "Ser sempre mais barato",
                                "Não precisar de pagar",
                            ],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n3",
                    "titulo": "As TIC na agricultura, na saúde e no ambiente",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "A e-Agricultura é:",
                            "options": [
                                "Usar as TIC para informar e ajudar os "
                                "camponeses",
                                "Plantar computadores",
                                "Vender telemóveis no campo",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada uso das TIC ao seu campo.",
                            "pairs": [
                                ["Mensagem com a previsão da chuva e o preço do milho", "Agricultura"],
                                ["Marcar consulta e lembrar a vacina pelo telemóvel", "Saúde"],
                                ["Satélite a vigiar queimadas e desflorestação", "Ambiente"],
                            ],
                        },
                        {
                            "t": "choice",
                            "q": "A e-Saúde permite:",
                            "options": [
                                "Guardar o registo do doente e falar com "
                                "o médico à distância",
                                "Curar sem médico",
                                "Vender medicamentos sem receita",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um aviso de ciclone enviado por "
                                 "mensagem a toda a província é as TIC:",
                            "options": [
                                "A ajudar na segurança face às alterações "
                                "climáticas",
                                "A causar o ciclone",
                                "A vender dados",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um camponês do Niassa que vê o preço do "
                                 "feijão em Maputo antes de vender:",
                            "options": [
                                "Vende melhor, porque sabe o mercado",
                                "Perde tempo",
                                "Não precisa da informação",
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
