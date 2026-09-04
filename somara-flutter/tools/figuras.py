"""Poe uma figura nas perguntas de geometria que falam de uma.

O problema
----------
"Um quadrado tem 5 cm de lado. Qual e o perimetro?" nao mostrava quadrado
nenhum. A crianca tinha de o imaginar antes de poder pensar nele -- e a de
4a classe que ainda esta a aprender o que e um perimetro nao tem essa
imagem na cabeca para invocar.

Pior: havia uma pergunta impossivel. "Quantos lados tem esta figura?"
mostrava quatro reguas (emoji) e a resposta certa era 4. Nao ha figura
nenhuma, so reguas repetidas.

Como e que as medidas sao encontradas
-------------------------------------
Por padroes explicitos e nao por adivinhacao. Cada padrao aqui foi escrito
depois de ler a pergunta que ele apanha; nenhum e generico. Uma regra
esperta que apanhasse "todos os numeros seguidos de cm" poria uma figura
em perguntas que nao falam de figura nenhuma.

Correr a partir de somara-flutter/:
    python tools/figuras.py            # so mostra
    python tools/figuras.py --gravar
"""

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CONTENT = RAIZ / "assets" / "content.json"

# (padrao, funcao que devolve o dicionario da figura)
#
# A ordem conta: os mais especificos primeiro, para "rectangulo de 8 por 3"
# nao ser apanhado pelo padrao do lado unico.
PADROES = [
    # "Um rectangulo tem 8 cm de comprimento e 3 cm de largura"
    (re.compile(r'rect[âa]ngulo tem (\d+)\s*cm de comprimento e (\d+)\s*cm de largura',
                re.I),
     lambda m: {'forma': 'rectangulo', 'a': int(m[1]), 'b': int(m[2])}),

    # "Um rectangulo tem 6 cm por 4 cm"
    (re.compile(r'rect[âa]ngulo tem (\d+)\s*cm por (\d+)\s*cm', re.I),
     lambda m: {'forma': 'rectangulo', 'a': int(m[1]), 'b': int(m[2])}),

    # "Um triangulo tem base 10 cm e altura 6 cm"
    (re.compile(r'tri[âa]ngulo tem base (\d+)\s*cm e altura (\d+)\s*cm', re.I),
     lambda m: {'forma': 'triangulo', 'a': int(m[1]), 'b': int(m[2])}),

    # "Um quadrado tem 5 cm de lado"
    (re.compile(r'quadrado tem (\d+)\s*cm de lado', re.I),
     lambda m: {'forma': 'quadrado', 'a': int(m[1])}),

    # "Uma circunferencia tem raio de 5 cm"
    (re.compile(r'circunfer[êe]ncia tem raio de (\d+)\s*cm', re.I),
     lambda m: {'forma': 'circulo', 'a': int(m[1])}),

    # "O volume de um cubo de aresta 3 cm"
    (re.compile(r'cubo de aresta (\d+)\s*cm', re.I),
     lambda m: {'forma': 'cubo', 'a': int(m[1])}),
]

# A pergunta que nao tinha figura nenhuma e precisava de uma.
#
# Era do tipo "count": mostrava o emoji da regua repetido quatro vezes e
# perguntava quantos lados tem "esta figura". Passa a escolha multipla com
# um quadrado desenhado -- e ai a pergunta faz sentido.
CONSERTOS = {
    'Quantos lados tem esta figura?': {
        't': 'choice',
        'options': ['3', '4', '5'],
        'a': 1,
        'figura': {'forma': 'quadrado', 'a': 4, 'unidade': ''},
        'remover': ['emoji', 'n'],
    },
}


def figura_para(texto: str):
    for padrao, faz in PADROES:
        m = padrao.search(texto)
        if m:
            return faz(m)
    return None


def main() -> int:
    gravar = "--gravar" in sys.argv
    dados = json.loads(CONTENT.read_text(encoding="utf-8"))

    postas, consertadas = [], []

    for curso in dados["cursos"]:
        for u in curso["units"]:
            for n in u["niveis"]:
                for q in n["questoes"]:
                    texto = q.get("q", "")

                    conserto = CONSERTOS.get(texto)
                    if conserto:
                        if gravar:
                            for chave in conserto.get('remover', []):
                                q.pop(chave, None)
                            for k, v in conserto.items():
                                if k != 'remover':
                                    q[k] = v
                        consertadas.append(f"{curso['id']}/{n['id']}: {texto}")
                        continue

                    fig = figura_para(texto)
                    if fig:
                        if gravar:
                            q["figura"] = fig
                        postas.append(f"{curso['id']}/{n['id']}: {texto[:60]}"
                                      f"\n        -> {fig}")

    print(f"figuras a por: {len(postas)}")
    for x in postas:
        print(f"   {x}")
    print(f"\nperguntas consertadas: {len(consertadas)}")
    for x in consertadas:
        print(f"   {x}")

    if not gravar:
        print("\n(so leitura -- corre com --gravar)")
        return 0

    CONTENT.write_text(
        json.dumps(dados, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    print("\n-- content.json gravado")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
