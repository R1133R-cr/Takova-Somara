# -*- coding: utf-8 -*-
"""O curso de Educacao Visual e Oficios da 4a classe.

ESTE E O UNICO CURSO DA APP SEM MANUAL
======================================
Todos os outros dezanove saem de um livro escolar mocambicano que esta
guardado em disco e citado no cabecalho da ferramenta que os gerou. Este
nao.

Procurei o manual:
  - nao esta nas pastas de livros (4a classe tem Portugues, Matematica,
    Ciencias Naturais e Ciencias Sociais, e mais nada);
  - o indice de livros da 4a classe do cexatas lista as mesmas quatro;
  - o MozEstuda tem EV da 5a, da 6a e da 7a, e nao da 4a.

Nao encontrei. Por isso este curso e montado a partir de tres coisas que
existem, e a diferenca fica registada no proprio content.json, no campo
`fonte` -- para quem tropecar nele daqui a um ano saber o que tem nas maos
sem ter de ir ao historico do git.

De onde vem, entao
------------------
1. O PLANO CURRICULAR DO ENSINO PRIMARIO (MINEDH, Maio 2020) descreve a
   disciplina: "permite que o aluno desenvolva competencias em actividades
   tais como artesanato, culinaria, costura, jardinagem, agricultura,
   criacao de animais de pequena especie, caca e pesca, bem como observar,
   descobrir, imaginar e expressar".

2. Os LIVROS DA 5a E DA 6a, que tenho. O da 5a diz, na introducao, que vem
   "consolidar os conhecimentos adquiridos nas classes anteriores" -- e
   nomeia desenho, recorte, colagem e dobragem como ja conhecidos. Isso diz
   o que a 4a tera ensinado.

3. A COERENCIA DA PROGRESSAO. A 5a e oficio (barro, fibras, cestaria); a 6a
   e desenho, pintura e cor. A 4a e a entrada: seguranca, materiais,
   desenho simples e trabalhos de papel.

O que NAO tem, e porque
-----------------------
Nao tem teoria da cor. A 6a ensina-a formalmente e a 5a nao lhe toca; poe-la
na 4a faria a progressao 4a(cor) -> 5a(sem cor) -> 6a(cor), que nao faz
sentido nenhum. Sem livro, o mais honesto e seguir a forma das classes que
conheco.

Correr a partir de somara-flutter/:
    python tools/conteudo_ev4c.py            # so mostra
    python tools/conteudo_ev4c.py --gravar
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402

FONTE = (
    "Estrutura provisória, sem fonte confirmada. Não existe manual de "
    "Educação Visual da 4ª classe publicado. Montada a partir do Plano "
    "Curricular do Ensino Primário (MINEDH, 2020) e dos manuais da 5ª e "
    "da 6ª classes. Substituir quando o livro aparecer."
)

CURSO = {
    "id": "ev-4c",
    "disciplina": "Educação Visual e Ofícios",
    "abrev": "Ed. Visual",
    "classe": "4ª classe",
    "tag": "EV",
    "fonte": FONTE,
    "units": [
        # ---------------------------------------------------------------
        # 1: Higiene e seguranca -- abre todas as unidades dos livros da
        #    5a e da 6a, e por isso abre esta.
        # ---------------------------------------------------------------
        {
            "id": "u1",
            "titulo": "Higiene e segurança",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O espaço de trabalho",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Antes de começar um trabalho manual, deves:",
                            "options": [
                                "Juntar os materiais que vais precisar",
                                "Começar e ver o que falta depois",
                                "Esperar pelo professor",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "No fim do trabalho, a mesa fica:",
                            "options": [
                                "Limpa e arrumada",
                                "Como está",
                                "Só varrida no fim da semana",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para não sujar a mesa quando se pinta, põe-se:",
                            "options": [
                                "Papel ou jornal por baixo",
                                "Mais tinta",
                                "Um copo de água",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Depois de trabalhar com cola ou tinta, as mãos:",
                            "options": ["Lavam-se", "Limpam-se na roupa", "Ficam assim"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Usar as ferramentas",
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
                            "q": "A tesoura corta melhor quando está:",
                            "options": ["Afiada e limpa", "Enferrujada", "Molhada"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Não se deve correr na sala com:",
                            "options": [
                                "A tesoura na mão",
                                "O caderno na mão",
                                "O lápis no bolso",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Depois de usar, as ferramentas devem ser:",
                            "options": [
                                "Guardadas no seu lugar",
                                "Deixadas na mesa",
                                "Levadas para casa",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # 2: Desenho -- o que a 5a diz que a crianca ja traz
        # ---------------------------------------------------------------
        {
            "id": "u2",
            "titulo": "Desenho",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Com que se desenha",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Qual destes serve para desenhar?",
                            "options": ["O lápis de carvão", "A cola", "A tesoura"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Um lápis que risca fino está:",
                            "options": ["Bem afiado", "Rombo", "Partido"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para apagar um traço a lápis usa-se:",
                            "options": ["A borracha", "O dedo molhado", "A tesoura"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "O giz e o carvão vegetal servem para:",
                            "options": ["Riscar e desenhar", "Colar", "Medir"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Desenhar o que se vê",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Desenhar aquilo que se tem à frente chama-se desenho:",
                            "options": ["De observação", "Livre", "Com tema dado"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Quando desenhas o que te apetece, o desenho é:",
                            "options": ["Livre", "De observação", "Rigoroso"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Antes de desenhar o que vês, primeiro deves:",
                            "options": [
                                "Olhar com atenção",
                                "Começar logo pelo meio",
                                "Copiar do colega",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma ilustração serve para:",
                            "options": [
                                "Acompanhar e explicar um texto",
                                "Substituir o texto",
                                "Encher a folha",
                            ],
                            "a": 0,
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # 3: Trabalhos com papel
        # ---------------------------------------------------------------
        {
            "id": "u3",
            "titulo": "Trabalhos com papel",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "Recortar e colar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Antes de recortar, é bom:",
                            "options": [
                                "Marcar a linha com o lápis",
                                "Molhar o papel",
                                "Dobrar tudo primeiro",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Numa colagem, a cola põe-se:",
                            "options": [
                                "Pouca e bem espalhada",
                                "Muita, num monte",
                                "Nos dedos",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Uma colagem faz-se juntando:",
                            "options": [
                                "Pedaços de papel numa folha",
                                "Duas tintas",
                                "Dois lápis",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os restos de papel do recorte devem ir:",
                            "options": ["Para o lixo", "Para o chão", "Para a gaveta"],
                            "a": 0,
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Dobrar e picotar",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Na dobragem, o papel é:",
                            "options": [
                                "Dobrado, sem se cortar",
                                "Cortado ao meio",
                                "Colado",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Para a dobra ficar direita, passa-se:",
                            "options": [
                                "A unha por cima do vinco",
                                "Cola por cima",
                                "Água por cima",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Picotar é fazer no papel:",
                            "options": [
                                "Muitos furos pequenos seguidos",
                                "Uma dobra",
                                "Um risco a lápis",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada técnica ao que se faz ao papel.",
                            "pairs": [
                                ["Recorte", "Cortar"],
                                ["Dobragem", "Dobrar"],
                            ],
                        },
                    ],
                },
            ],
        },
        # ---------------------------------------------------------------
        # 4: Oficios da comunidade -- a lista de actividades e a do Plano
        #    Curricular, palavra por palavra
        # ---------------------------------------------------------------
        {
            "id": "u4",
            "titulo": "Ofícios da comunidade",
            "niveis": [
                {
                    "id": "n1",
                    "titulo": "O que se faz com as mãos",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Fazer cestos e esteiras com palha é:",
                            "options": ["Cestaria", "Costura", "Jardinagem"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Coser roupa com agulha e linha é:",
                            "options": ["Costura", "Cestaria", "Carpintaria"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Trabalhar a madeira é ofício de:",
                            "options": ["Carpinteiro", "Oleiro", "Pescador"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Tratar de uma horta é:",
                            "options": ["Jardinagem", "Olaria", "Tecelagem"],
                            "a": 0,
                        },
                        {
                            "t": "match",
                            "q": "Liga cada ofício ao que ele faz.",
                            "pairs": [
                                ["Cestaria", "Cestos e esteiras"],
                                ["Costura", "Roupa"],
                            ],
                        },
                    ],
                },
                {
                    "id": "n2",
                    "titulo": "Materiais da nossa terra",
                    "questoes": [
                        {
                            "t": "choice",
                            "q": "Com que material se fazem vasos e panelas de barro?",
                            "options": ["Argila", "Palha", "Linha"],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "A palha e o bambu servem para:",
                            "options": [
                                "Fazer cestos e esteiras",
                                "Fazer tinta",
                                "Fazer papel",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Reaproveitar um saco velho para fazer um trabalho é:",
                            "options": [
                                "Reciclar",
                                "Estragar",
                                "Desperdiçar",
                            ],
                            "a": 0,
                        },
                        {
                            "t": "choice",
                            "q": "Os materiais para os trabalhos manuais podem vir:",
                            "options": [
                                "Da natureza que temos à volta",
                                "Só da loja",
                                "Só da cidade",
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
    print(f"  FONTE: {FONTE}")
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

    onde = ids.index("cs-4c") + 1
    dados["cursos"].insert(onde, CURSO)

    audio.gravar_content(dados)
    audio.escrever_manifesto(manifesto)
    print(f"\n-- curso inserido, {feitos} audios gravados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
