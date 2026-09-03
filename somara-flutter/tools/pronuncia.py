"""Como se diz o que esta escrito.

O problema
----------
O texto no ecra e o texto que a Raquel le nao sao a mesma coisa. "SADC"
escreve-se assim e diz-se "esse-a-de-ce"; "5 MT" escreve-se assim e diz-se
"cinco meticais"; "seculo XV" diz-se "seculo quinze"; "5 cm" diz-se "cinco
centimetros". Sem isto, a app lia "sadec", "eme-te", "seculo xis-ve" e
"cinco ce-eme" -- e uma crianca que depende do audio para seguir a licao
ficava com a palavra errada na cabeca.

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

As UNIDADES de medida (cm, kg, L) sao o mesmo problema com outra saida: ai
a regra pode ser geral, mas so porque esta ancorada num numero. A razao
esta escrita por extenso onde a regra vive, mais abaixo.

Alterar isto obriga a regravar o audio afectado: correr
`python tools/regravar_siglas.py`.

Ha testes: `python tools/test_pronuncia.py`.
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

# A linha de preencher diz-se como uma PAUSA, e nao como nada.
#
# "Completa: A menina é ___." lido sem o espaco sai "completa, a menina e" e
# acaba. A crianca que nao le -- que e justamente quem depende do audio --
# nao fica a saber que ha ali um buraco para encher, nem onde ele esta.
#
# As reticencias sao o que o motor de voz entende como pausa, e sao o que
# esta gravado nos 43 ficheiros que ja existem: conferi um a um, e o
# tamanho bate ao byte com esta forma e nao com nenhuma outra. Nem com a
# resposta la dentro -- que seria pior do que o silencio, porque dava a
# solucao a quem estivesse a ouvir.
_BRANCO = re.compile(r'_{2,}')


# As unidades de medida, ditas por extenso.
#
# "5 cm" no ecra e "cinco centimetros" na voz. Sem isto a Raquel lia as
# letras -- "cinco ce-eme" -- e a crianca da 4a classe que esta a aprender
# o perimetro ouvia duas consoantes onde devia ouvir uma unidade.
#
# A lista tem as que aparecem hoje no curriculo (cm 20, km 9, kg 4, ml 3,
# m 3, g 3, L 3) e as restantes da mesma familia, para uma pergunta nova
# escrita amanha nao trazer o defeito de volta.
UNIDADES = {
    # comprimento
    'mm': ('milímetro', 'milímetros'),
    'cm': ('centímetro', 'centímetros'),
    'dm': ('decímetro', 'decímetros'),
    'km': ('quilómetro', 'quilómetros'),
    'm': ('metro', 'metros'),
    # massa
    'mg': ('miligrama', 'miligramas'),
    'kg': ('quilograma', 'quilogramas'),
    'g': ('grama', 'gramas'),
    't': ('tonelada', 'toneladas'),
    # capacidade
    'ml': ('mililitro', 'mililitros'),
    'dl': ('decilitro', 'decilitros'),
    'l': ('litro', 'litros'),
    'L': ('litro', 'litros'),
    # tempo
    'min': ('minuto', 'minutos'),
    'h': ('hora', 'horas'),
}

# Os simbolos mais compridos primeiro: sem isso o 'm' comia o inicio do
# 'mm' e o 'l' o do 'ml'.
_SIMBOLOS = sorted(UNIDADES, key=len, reverse=True)
_ALT = '|'.join(re.escape(s) for s in _SIMBOLOS)

# PORQUE E QUE A REGRA TEM DE ESTAR ANCORADA NUM NUMERO
#
# Um simbolo de unidade e quase sempre uma letra, e as letras soltas do
# Portugues da 1a classe sao lidas pela mesma voz. No curriculo estao:
#
#   M   13 vezes, e nenhuma e uma unidade -- "M + A = ?", "Sílabas com M"
#   L    7 vezes fora de numeros, todas a letra -- "L + A = ?"
#   T    6 vezes, a letra
#   l    2 vezes, a letra -- "as palavras terminadas em l trocam-no por is"
#   m    7 vezes fora de numeros, das quais "m.d.c." e "m.m.c."
#
# Uma regra que apanhasse letras soltas poria a voz a dizer "litro mais á
# igual a" onde esta escrito "L + A = ?", e "o metro ponto de ponto ce"
# onde esta "o m.d.c.". Por isso: so depois de um numero.
#
# O numero leva espacos de milhar ("1 000 m") e virgula decimal ("2,5 km").
_APOS_NUMERO = re.compile(
    rf'(?P<num>\d[\d  ]*(?:[.,]\d+)?)\s*(?P<sim>{_ALT})(?![\wº²³])'
)

# A unica excepcao ao numero: "Qual é o perímetro, em cm?" -- ali nao ha
# numero nenhum e e mesmo uma unidade. Sao 4 casos no curriculo, todos
# com cm.
#
# So vale para simbolos de duas letras ou mais, e a razao esta a dois
# centimetros daqui: "Termina em l?" e sobre a letra l.
_ALT_LONGOS = '|'.join(
    re.escape(s) for s in _SIMBOLOS if len(s) > 1
)
_APOS_EM = re.compile(rf'\bem (?P<sim>{_ALT_LONGOS})(?![\wº²³])')

# "60 km/h". Tem de sair antes do _BARRA, senao a barra vira virgula e a
# voz diz "sessenta quilómetros, agá".
_POR_HORA = re.compile(
    r'(?P<num>\d[\d  ]*(?:[.,]\d+)?)\s*km/h\b'
)

# Um so quando e mesmo um: "1 000" nao e "1".
_E_UM = re.compile(r'^0*1(?:[.,]0+)?$')


def nome_da_unidade(simbolo: str, plural: bool = False) -> str:
    """"cm" -> "centímetro". O nome por extenso de um simbolo de unidade."""
    return UNIDADES[simbolo][1 if plural else 0]


def _e_singular(numero: str) -> bool:
    return bool(_E_UM.match(numero.replace(' ', '').replace(' ', '')))


def dizer_unidades(texto: str) -> str:
    """Troca os simbolos de unidade pelo nome por extenso.

    So onde sao mesmo unidades: depois de um numero, ou depois de "em"
    quando o simbolo tem duas letras ou mais.
    """
    if not texto:
        return texto

    def por_hora(m):
        num = m.group('num').rstrip()
        unidade = 'quilómetro' if _e_singular(num) else 'quilómetros'
        return f'{num} {unidade} por hora'

    def depois_de_numero(m):
        num = m.group('num').rstrip()
        return f'{num} {nome_da_unidade(m.group("sim"), not _e_singular(num))}'

    fora = _POR_HORA.sub(por_hora, texto)
    fora = _APOS_NUMERO.sub(depois_de_numero, fora)
    # No "em cm" nao ha numero que diga o que fazer, e o plural e o que um
    # professor diz: "o perimetro, em centimetros".
    return _APOS_EM.sub(
        lambda m: f'em {nome_da_unidade(m.group("sim"), True)}', fora
    )


def dizer_sinais(texto: str) -> str:
    """Troca os sinais de contas pelo que se diz."""
    fora = _DIVISAO.sub(' a dividir por ', texto)
    fora = _BARRA.sub(', ', fora)
    # Antes de o `limpar` os apagar: e ele que varre os underscores, e sem
    # esta linha a pausa desaparecia com eles.
    fora = _BRANCO.sub('...', fora)
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
    # As unidades depois das siglas e antes dos sinais: depois das siglas
    # porque o "5 MT" ja virou "5 meticais" e nao ha 'm' solto para
    # apanhar; antes dos sinais porque o "km/h" tem de sair inteiro antes
    # de a barra virar virgula.
    fora = dizer_unidades(fora)
    # Os sinais de contas ficam para o fim: as trocas de cima podem deixar
    # numeros encostados a sinais que antes estavam separados por uma sigla.
    return dizer_sinais(fora)


def mexe_em(texto: str) -> bool:
    """Este texto precisa de tratamento?"""
    return bool(texto) and para_dizer(texto) != texto
