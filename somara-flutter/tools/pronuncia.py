"""Como se diz o que esta escrito.

O problema
----------
O texto no ecra e o texto que a Raquel le nao sao a mesma coisa. "SADC"
escreve-se assim e diz-se "esse-a-de-ce"; "5 MT" escreve-se assim e diz-se
"cinco meticais"; "seculo XV" diz-se "seculo quinze". Sem isto, a app lia
"sadec", "eme-te" e "seculo xis-ve" -- e uma crianca que depende do audio
para seguir a licao ficava com a palavra errada na cabeca.

Porque e uma lista e nao uma regra
----------------------------------
A tentacao e soletrar tudo o que esteja em maiusculas. Seria desastroso:
o Portugues da 1a classe esta cheio de silabas e palavras em maiusculas --
MA, PA, LA, BOLA, CASA, PATO, MALA. Soletrar "bê-ó-éle-á" a quem esta a
aprender a ler "BOLA" e o contrario de ensinar.

Tres tratamentos, escolhidos um a um:

  SOLETRAR  as siglas que em portugues se dizem letra a letra
  DIZER     as abreviaturas que valem uma palavra inteira
  DEIXAR    tudo o resto -- incluindo as siglas que ja se dizem como
            palavra (ONU, FRELIMO) e todo o Portugues da 1a classe

Alterar isto obriga a regravar o audio afectado: correr
`python tools/regravar_siglas.py`.
"""

import re

# Nomes das letras em portugues. Escritos por extenso e nao separados por
# pontos porque assim a pronuncia fica garantida: sao palavras normais, e
# nao dependem de o motor de voz adivinhar que aquilo e para soletrar.
LETRAS = {
    'A': 'á', 'B': 'bê', 'C': 'cê', 'D': 'dê', 'E': 'é', 'F': 'éfe',
    'G': 'gê', 'H': 'agá', 'I': 'i', 'J': 'jota', 'K': 'cá', 'L': 'éle',
    'M': 'éme', 'N': 'éne', 'O': 'ó', 'P': 'pê', 'Q': 'quê', 'R': 'érre',
    'S': 'ésse', 'T': 'tê', 'U': 'u', 'V': 'vê', 'W': 'dâblio', 'X': 'xis',
    'Y': 'ípsilon', 'Z': 'zê',
}

# Siglas que em portugues se dizem letra a letra.
SOLETRAR = ['SADC', 'CPLP', 'HIV', 'UA']

# Abreviaturas e numeros que valem uma palavra.
#
# O MT e o caso com mais peso de todos: sao 68 ocorrencias, quase todas na
# Matematica da 1a classe, onde a crianca esta a aprender dinheiro. Ler
# "eme-te" em vez de "meticais" estragava a licao inteira.
DIZER = {
    'MT': 'meticais',
    # Seculos em numeracao romana. So estes tres aparecem no curriculo; a
    # lista curta e de proposito, para nao apanhar por engano palavras
    # como MIL ou DIVIDIR que tambem sao letras romanas validas.
    'XV': 'quinze',
    'XIX': 'dezanove',
    'XX': 'vinte',
}

# Siglas que ja se dizem como palavra e portanto nao se tocam. Estao aqui
# escritas so para ficar registado que a decisao foi tomada e nao esquecida.
DEIXAR_COMO_ESTA = ['ONU', 'FRELIMO', 'PIN']


# Os sinais de contas, ditos como um professor os diria.
#
# O que se escreve nao e o que se le: "2 + 1 = 3" no ecra e "dois mais um
# e igual a tres" na voz. Sem isto a Raquel lia "dois um tres" -- os
# sinais eram saltados, e a conta que a crianca ouvia nao era conta
# nenhuma.
#
# Cada um destes foi escolhido depois de contar o que existe mesmo no
# curriculo, e ha dois que NAO se tocam:
#
#   'x' (U+0078)  aparece 176 vezes, e e a letra de "peixes"
#   '-' (U+002D)  aparece 220 vezes, e e o hifen de "contam-se"
#
# O sinal de multiplicar e o '×' (U+00D7) e o de menos e o '−' (U+2212).
# Trocar um pelo outro poria a voz a dizer "peivezes".
SINAIS = {
    '+': ' mais ',
    '−': ' menos ',    # sinal de menos, nao o hifen
    '×': ' vezes ',    # sinal de multiplicar, nao a letra x
    '=': ' é igual a ',
    '%': ' por cento',
    '<': ' é menor que ',
    '>': ' é maior que ',
}

# A divisao neste curriculo escreve-se com dois pontos, como nas escolas
# portuguesas: "48 : 6 = 8". Mas os dois pontos sao tambem pontuacao
# vulgar -- 533 ocorrencias, quase todas a abrir uma frase.
#
# Estar entre numeros nao chega para distinguir: em "10% de 500: 500 : 100"
# os dois estao, e so o segundo e divisao. O que os separa e o espaco. A
# convencao tipografica -- espaco dos dois lados na divisao, nenhum antes
# na pontuacao -- verificou-se em todo o curriculo: 16 divisoes com
# espacos, 9 pontuacoes sem, e nenhuma excepcao.
_DIVISAO = re.compile(r'(?<=\d) : (?=\d)')

# A barra separa palavras numa lista para ordenar ("bola / a / é"). Nao e
# divisao: le-se como uma pausa, para as palavras nao virem coladas.
_BARRA = re.compile(r'\s*/\s*')


def dizer_sinais(texto: str) -> str:
    """Troca os sinais de contas pelo que se diz."""
    fora = _DIVISAO.sub(' a dividir por ', texto)
    fora = _BARRA.sub(', ', fora)
    for sinal, palavra in SINAIS.items():
        fora = fora.replace(sinal, palavra)
    # Sobrou espaco a dobrar de tantas trocas.
    return re.sub(r'\s+', ' ', fora).strip()


def soletrar(sigla: str) -> str:
    """"SADC" -> "ésse, á, dê, cê" — com virgulas para a voz respirar
    entre as letras em vez de as atropelar."""
    return ', '.join(LETRAS.get(c, c) for c in sigla)


# Frases em que a sigla e NOMEADA em vez de usada.
#
# "O metical escreve-se MT" esta a ensinar a abreviatura -- ali "MT" e o
# proprio simbolo, e ler "escreve-se meticais" desfaz a licao. Nestes
# casos soletra-se, mesmo tratando-se de uma abreviatura que noutro sitio
# se diria por extenso.
_NOMEIA = re.compile(
    r'(escreve-se|escrevem-se|abrevia-se|chama-se|significa)\s+'
    r'([A-Z]{2,})'
)


def para_dizer(texto: str) -> str:
    """O texto tal como deve ser lido em voz alta."""
    if not texto:
        return texto
    # Primeiro as frases que nomeiam a sigla: depois de soletrada, ela
    # deixa de casar com as regras gerais e fica protegida delas.
    fora = _NOMEIA.sub(lambda m: f'{m.group(1)} {soletrar(m.group(2))}', texto)
    # As mais compridas primeiro: sem isso, o XX comia o inicio do XIX.
    for sigla in sorted(SOLETRAR, key=len, reverse=True):
        fora = re.sub(rf'\b{sigla}\b', soletrar(sigla), fora)
    for sigla, palavra in sorted(DIZER.items(), key=lambda x: -len(x[0])):
        fora = re.sub(rf'\b{sigla}\b', palavra, fora)
    # Os sinais de contas ficam para o fim: as trocas de cima podem deixar
    # numeros encostados a sinais que antes estavam separados por uma sigla.
    return dizer_sinais(fora)


def mexe_em(texto: str) -> bool:
    """Este texto precisa de tratamento?"""
    return bool(texto) and para_dizer(texto) != texto
