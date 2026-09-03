"""Tira o texto de um PDF, sem instalar nada.

Porque e que isto existe
------------------------
O conteudo da Somara sai dos manuais escolares moçambicanos, e sao 30 PDFs.
Esta maquina nao tem `pdftoppm`, nem `pypdf`, nem pip para os instalar -- o
Python e uma versao embutida. Sem isto nao ha como ler um livro.

Como funciona
-------------
Um PDF guarda o texto dentro de fluxos comprimidos com zlib, e os pedacos
de texto entre parentesis. Descomprime-se, apanham-se os parentesis, e
tem-se o texto.

As duas armadilhas, ambas encontradas a marteladas:

1. Os acentos vem em ESCAPES OCTAIS -- `\\347` e o ç. Um parser que engula
   so um caracter a seguir a barra deixa "347" no meio da palavra e o texto
   sai ilegivel. So os digitos 0-7 contam: `\\9` nao e octal.

2. Muitos livros escrevem cada letra com o seu espacamento, e "Educação
   Visual" sai "E duc a ç ã o Visua l". Procurar a frase exacta nao
   encontra nada. Por isso o `procurar()` compara sem espacos e devolve o
   trecho original.

O que isto NAO faz: paginas digitalizadas como imagem nao teem texto
nenhum la dentro, e nenhum truque as le. Nesses casos devolve pouco ou
nada, e ve-se logo pelo tamanho do resultado.

Uso:
    python tools/ler_pdf.py <ficheiro.pdf> [palavra a procurar]
"""

import re
import sys
import zlib
from pathlib import Path

for _fluxo in (sys.stdout, sys.stderr):
    try:
        _fluxo.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:  # pragma: no cover
        pass

_BARRA = bytes([92])
_OCTAIS = [bytes([d]) for d in b"01234567"]
_ESCAPES = {b"n": 10, b"r": 13, b"t": 9, b"b": 8, b"f": 12}


def _strings_do_fluxo(b: bytes) -> list[bytes]:
    """Os pedacos entre parentesis, com os escapes resolvidos."""
    saida, i, n = [], 0, len(b)
    while i < n:
        if b[i:i + 1] != b"(":
            i += 1
            continue
        j, profundidade, buf = i + 1, 1, bytearray()
        while j < n and profundidade:
            c = b[j:j + 1]
            if c == _BARRA:
                seguinte = b[j + 1:j + 4]
                if seguinte[:1] in _OCTAIS:
                    k = 1
                    while k < 3 and seguinte[k:k + 1] in _OCTAIS:
                        k += 1
                    buf.append(int(seguinte[:k], 8) & 0xFF)
                    j += 1 + k
                    continue
                buf.append(_ESCAPES.get(seguinte[:1],
                                        seguinte[0] if seguinte else 32))
                j += 2
                continue
            if c == b"(":
                profundidade += 1
            elif c == b")":
                profundidade -= 1
                if not profundidade:
                    break
            buf += c
            j += 1
        saida.append(bytes(buf))
        i = j + 1
    return saida


def texto(caminho) -> str:
    """Todo o texto do PDF, numa linha so."""
    bruto = Path(caminho).read_bytes()
    partes = []
    for m in re.finditer(b"stream", bruto):
        inicio = bruto.find(b"\n", m.end()) + 1
        fim = bruto.find(b"endstream", inicio)
        if fim < 0:
            continue
        try:
            d = zlib.decompress(bruto[inicio:fim])
        except Exception:
            continue
        if b"Tj" in d or b"TJ" in d:
            partes.append(b" ".join(_strings_do_fluxo(d)))
    return re.sub(r"\s+", " ", b" ".join(partes).decode("latin-1", "replace"))


def procurar(t: str, chave: str, antes: int = 120, depois: int = 320,
             quantos: int = 5) -> list[str]:
    """Procura ignorando o espacamento entre letras.

    "Educacao Visual" tem de encontrar "E duc a ç ã o Visua l", que e como
    muitos destes livros escrevem.
    """
    comprimido = re.sub(r"\s+", "", t)
    posicoes = [i for i, c in enumerate(t) if not c.isspace()]
    alvo = re.sub(r"\s+", "", chave)
    achados = []
    for m in list(re.finditer(re.escape(alvo), comprimido, re.I))[:quantos]:
        a = posicoes[max(0, m.start() - antes)]
        b = posicoes[min(m.end() + depois, len(posicoes) - 1)]
        achados.append(re.sub(r"\s+", " ", t[a:b]))
    return achados


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__.strip().splitlines()[-1], file=sys.stderr)
        return 1
    t = texto(sys.argv[1])
    print(f"-- {len(t)} caracteres extraidos")
    if len(sys.argv) > 2:
        chave = sys.argv[2]
        achados = procurar(t, chave)
        print(f"-- '{chave}': {len(achados)} ocorrencias mostradas\n")
        for a in achados:
            print(f"  >> {a}\n")
    else:
        print(t[:3000])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
