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
    # Seculos em numeracao romana, SOLTOS -- sem a palavra "seculo" a
    # frente. A lista curta e de proposito: MIL, DIVIDIR e CIVIL tambem sao
    # feitos de letras romanas validas, e uma regra geral comia-os.
    #
    # Quando vem a seguir a "seculo" ou "seculos" ha uma regra melhor, que
    # nao precisa de lista nenhuma -- ver [dizer_seculos].
    'XV': 'quinze',
    'XIX': 'dezanove',
    'XX': 'vinte',
}

# Os seculos, quando a palavra "seculo" os anuncia.
#
# A Historia da 7a classe fala de reinos "do seculo IX ao XVII", da
# formacao do capitalismo "nos seculos XV-XVIII", da Grecia e de Roma. Sao
# muitos mais do que os tres da lista de cima, e por-los todos la seria
# perigoso: "MIL" e "CIVIL" tambem se leem como numeros romanos.
#
# Ancorada na palavra, a regra deixa de ter esse risco: so se toca no que
# vem LOGO A SEGUIR a "seculo" ou "seculos", e ai um numero romano e mesmo
# um numero romano. Apanha tambem o segundo numero de um intervalo --
# "seculo IX – XVII" --, que de outra maneira ficava por dizer.
#
# Em portugues os seculos leem-se em ordinal ate ao decimo e em cardinal a
# partir do decimo primeiro: "seculo nono", "seculo quinze".
_SECULOS = {
    'I': 'primeiro', 'II': 'segundo', 'III': 'terceiro', 'IV': 'quarto',
    'V': 'quinto', 'VI': 'sexto', 'VII': 'sétimo', 'VIII': 'oitavo',
    'IX': 'nono', 'X': 'décimo',
    'XI': 'onze', 'XII': 'doze', 'XIII': 'treze', 'XIV': 'catorze',
    'XV': 'quinze', 'XVI': 'dezasseis', 'XVII': 'dezassete',
    'XVIII': 'dezoito', 'XIX': 'dezanove', 'XX': 'vinte',
    'XXI': 'vinte e um',
}

# O grupo do meio é só a ligação, sem o segundo número lá dentro. Já
# esteve de outra maneira e o resultado foi "do século nono ao XVII
# dezassete": o número romano ficava, e a palavra vinha atrás dele.
_SECULO = re.compile(
    r'\b(séculos?)\s+([IVX]+)'
    r'(?:(\s*(?:[-–—]|a|e|até|ao)\s*)([IVX]+))?',
    re.IGNORECASE,
)


def dizer_seculos(texto: str) -> str:
    """"século IX" -> "século nono"; "séculos XV-XVIII" -> por extenso."""
    def um(m):
        palavra, primeiro, meio, segundo = m.group(1, 2, 3, 4)
        fora = f'{palavra} {_SECULOS.get(primeiro.upper(), primeiro)}'
        if segundo:
            # Um travessão entre dois séculos lê-se "a", e não em silêncio.
            ligacao = meio.strip()
            if ligacao in ('-', '–', '—', ''):
                ligacao = 'a'
            fora += f' {ligacao} {_SECULOS.get(segundo.upper(), segundo)}'
        return fora
    return _SECULO.sub(um, texto)

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

# Os simbolos da teoria de conjuntos, que entram na 7a classe.
#
# Nenhum destes se le sozinho. A Raquel diz "5 ∈ A" como "cinco a" -- come
# o simbolo em silencio, e a frase que sobra ate parece uma frase, o que e
# pior do que um erro audivel: quem depende do audio fica a ouvir uma coisa
# que faz sentido e esta errada.
#
# Escrevem-se por extenso e com espacos dos dois lados, para a voz nao os
# colar ao numero anterior.
CONJUNTOS = {
    '∈': ' pertence a ',
    '∉': ' não pertence a ',
    '⊂': ' está contido em ',
    '⊄': ' não está contido em ',
    '⊆': ' está contido ou é igual a ',
    '⊃': ' contém ',
    '∪': ' reunião ',
    '∩': ' intersecção ',
    '∅': ' conjunto vazio ',
    '≠': ' é diferente de ',
    '≤': ' é menor ou igual a ',
    '≥': ' é maior ou igual a ',
    # As letras dos conjuntos numericos. Le-se o NOME da letra: um aluno
    # que ouca "zê" sabe do que se trata, e um que ouca "z" nao ouve nada.
    'ℕ': ' ene ',
    'ℤ': ' zê ',
    'ℚ': ' quê ',
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
#
# ACRESCENTO: nao e so um numero que pode estar do lado esquerdo. No
# curriculo ha "___ : 5 = 6", "x : 4 = 12" e "(base × altura) : 2" -- tres
# divisoes que esta regra deixava passar por serem precedidas de um
# underscore, de uma letra e de um parentesis. Eram lidas como pontuacao,
# isto e, como uma pausa, e a conta desaparecia do audio.
#
# O que distingue continua a ser o espaco dos dois lados mais o algarismo a
# seguir: a pontuacao vulgar nao leva espaco antes dos dois pontos.
_DIVISAO = re.compile(r'(?<=\S) : (?=\d)')

# Fraccoes: "3/4" le-se "tres quartos", e nao "tres, quatro".
#
# Sem isto a barra caia na regra do _BARRA e virava virgula, e a app lia
# "Qual e maior: 1, 2 ou 1, 4?" -- duas listas de numeros onde estavam duas
# fraccoes. Sao 53 textos do curriculo, quase todos da 2a e da 3a classe,
# onde a crianca esta a aprender exactamente isto.
#
# Um a dois algarismos de cada lado, de proposito: assim um par de anos
# como "2024/2025" nao vira fraccao.
_FRACCAO = re.compile(r'\b(\d{1,2})/(\d{1,2})\b')

# Os nomes das partes. Ate ao decimo tem nome proprio; daí para cima diz-se
# "avos" -- 5/12 le-se "cinco doze avos".
_PARTES = {
    2: ('meio', 'meios'),
    3: ('terço', 'terços'),
    4: ('quarto', 'quartos'),
    5: ('quinto', 'quintos'),
    6: ('sexto', 'sextos'),
    7: ('sétimo', 'sétimos'),
    8: ('oitavo', 'oitavos'),
    9: ('nono', 'nonos'),
    10: ('décimo', 'décimos'),
}


def dizer_fraccoes(texto: str) -> str:
    """"3/4" -> "3 quartos". O numero fica em algarismos porque a voz
    ja o le bem; o que ela nao sabe e o nome da parte."""
    def uma(m):
        cima, baixo = int(m.group(1)), int(m.group(2))
        if baixo < 2:
            return m.group(0)
        singular, plural = _PARTES.get(baixo, (f'{baixo} avos', f'{baixo} avos'))
        return f'{cima} {singular if cima == 1 else plural}'
    return _FRACCAO.sub(uma, texto)

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
    # As fracções antes do _BARRA, que é quem transforma a barra em vírgula:
    # depois dele já não há barra nenhuma para reconhecer.
    fora = dizer_fraccoes(fora)
    fora = _BARRA.sub(', ', fora)
    # Antes de o `limpar` os apagar: e ele que varre os underscores, e sem
    # esta linha a pausa desaparecia com eles.
    fora = _BRANCO.sub('...', fora)
    # Os de conjuntos e os de contas não se pisam: "≠", "≤" e "≥" são cada
    # um o seu caracter, e não um "=" com um traço por cima. A ordem aqui é
    # só para ser sempre a mesma.
    for simbolo, palavra in CONJUNTOS.items():
        fora = fora.replace(simbolo, palavra)
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
    # Os séculos antes da lista das siglas: assim o "XV" de "século XV" já
    # foi dito por extenso e não chega à regra solta, e o "XVII" — que não
    # está na lista — também sai.
    fora = dizer_seculos(fora)
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
