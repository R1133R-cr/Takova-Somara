"""Gera os sons da app.

Porque e que sao sintetizados aqui
----------------------------------
Na fase C a app estava muda -- sem som de toque, sem resposta ao acerto,
sem nada por tras. Um banco de sons comprado traz licencas para gerir e
ficheiros grandes; sintetizados aqui, cada som tem a licenca da propria
app, pesa uns kilobytes e pode ser afinado numa linha.

Duas escolhas que valem a pena explicar:

1. O som de erro NAO e desagradavel. E duas notas graves e macias, a
   descer. Uma criianca que erra ja se sente mal; um "erro" estridente
   ensina-lhe a ter medo de tentar.

2. O fundo e pentatonico e esparso. Numa escala pentatonica nao ha
   intervalos dissonantes, portanto o ciclo nunca soa errado por mais
   vezes que se repita -- e vai repetir-se centenas de vezes.

Sem dependencias: so `wave` e `math` da biblioteca padrao.

Correr a partir de somara-flutter/:
    python tools/sons.py
"""

import math
import struct
import wave
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "assets" / "som"

TAXA = 22050  # chega e sobra para isto, e ocupa metade de 44100


def nota(nome: str) -> float:
    """Frequencia de uma nota tipo 'C4', 'G#5'."""
    passos = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
    semitom = passos[nome[0]]
    resto = nome[1:]
    if resto.startswith("#"):
        semitom += 1
        resto = resto[1:]
    oitava = int(resto)
    # A4 = 440 Hz e o numero 69 em MIDI.
    midi = (oitava + 1) * 12 + semitom
    return 440.0 * 2 ** ((midi - 69) / 12)


def marimba(freq: float, dur: float, volume: float = 0.5, decaimento: float = 7.0):
    """Uma nota de timbre quente, tipo marimba: fundamental mais dois
    harmonicos que se apagam mais depressa do que ela."""
    n = int(TAXA * dur)
    for i in range(n):
        t = i / TAXA
        env = math.exp(-decaimento * t)
        # Ataque curto para nao estalar no inicio.
        if t < 0.005:
            env *= t / 0.005
        s = (
            math.sin(2 * math.pi * freq * t)
            + 0.34 * math.sin(2 * math.pi * freq * 2 * t) * math.exp(-decaimento * t)
            + 0.11 * math.sin(2 * math.pi * freq * 3.01 * t) * math.exp(-2 * decaimento * t)
        )
        yield s * env * volume


def somar(*vozes):
    """Mistura varias vozes, cada uma (atraso_em_segundos, gerador)."""
    faixas = []
    fim = 0
    for atraso, voz in vozes:
        amostras = list(voz)
        inicio = int(atraso * TAXA)
        faixas.append((inicio, amostras))
        fim = max(fim, inicio + len(amostras))

    saida = [0.0] * fim
    for inicio, amostras in faixas:
        for i, s in enumerate(amostras):
            saida[inicio + i] += s
    return saida


def gravar(nome: str, amostras, normalizar_para: float = 0.82):
    pico = max((abs(s) for s in amostras), default=0.0)
    if pico > 0:
        k = normalizar_para / pico
        amostras = [s * k for s in amostras]

    DESTINO.mkdir(parents=True, exist_ok=True)
    caminho = DESTINO / nome
    with wave.open(str(caminho), "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(TAXA)
        w.writeframes(
            b"".join(
                struct.pack("<h", int(max(-1.0, min(1.0, s)) * 32767)) for s in amostras
            )
        )
    print(f"   {caminho.stat().st_size:>7} bytes  {nome}")


# ---------------------------------------------------------------- os sons


def toque():
    """Toque num botao. Curto e discreto -- ouve-se dezenas de vezes por
    minuto, e qualquer coisa mais do que isto cansa."""
    return somar((0, marimba(nota("A5"), 0.09, 0.34, decaimento=34)))


def certo():
    """Acertou: duas notas a subir."""
    return somar(
        (0.00, marimba(nota("E5"), 0.36, 0.44)),
        (0.09, marimba(nota("B5"), 0.42, 0.40)),
    )


def errado():
    """Errou. Grave e macio, a descer -- nunca estridente."""
    return somar(
        (0.00, marimba(nota("F3"), 0.34, 0.40, decaimento=9)),
        (0.10, marimba(nota("D3"), 0.42, 0.34, decaimento=9)),
    )


def nivel():
    """Nivel concluido: um arpejo curto que sobe e assenta."""
    return somar(
        (0.00, marimba(nota("C5"), 0.5, 0.40)),
        (0.10, marimba(nota("E5"), 0.5, 0.40)),
        (0.20, marimba(nota("G5"), 0.5, 0.40)),
        (0.32, marimba(nota("C6"), 0.9, 0.46, decaimento=4)),
        (0.32, marimba(nota("E6"), 0.9, 0.22, decaimento=4)),
    )


def salto():
    """O Roby a saltar de casa. Um 'boing' curto: a frequencia sobe e
    volta a descer dentro da propria nota."""
    dur = 0.20
    n = int(TAXA * dur)
    base = nota("C4")
    amostras = []
    fase = 0.0
    for i in range(n):
        t = i / TAXA
        k = t / dur
        f = base * (1 + 1.5 * math.sin(math.pi * k))
        fase += 2 * math.pi * f / TAXA
        env = math.exp(-9 * t)
        if t < 0.004:
            env *= t / 0.004
        amostras.append(math.sin(fase) * env * 0.5)
    return amostras


def fundo():
    """A trilha de fundo: 24 segundos que dao a volta sem costura.

    Pentatonica de do maior, notas esparsas e um bordao muito baixo por
    baixo. Toca em ciclo horas a fio, por isso o que interessa aqui e ser
    esquecivel -- se der por si a trautea-la, esta alta de mais.
    """
    bpm = 66.0
    batida = 60.0 / bpm
    compassos = 8
    por_compasso = 4
    total_batidas = compassos * por_compasso
    dur = total_batidas * batida  # 8 x 4 x 0.909 = 29,1 s

    # Um padrao que nao repete de quatro em quatro batidas -- se repetisse,
    # dava por ela logo ao fim de um minuto.
    padrao = [
        "C4", None, "E4", None, "G4", None, "A4", None,
        "G4", None, "E4", None, "D4", None, "E4", None,
        "A4", None, "G4", None, "E4", None, "C4", None,
        "D4", None, "E4", None, "G4", None, None, None,
    ]

    vozes = []
    for i, nome in enumerate(padrao):
        if nome is None:
            continue
        vozes.append((i * batida, marimba(nota(nome), 1.6, 0.30, decaimento=3.2)))
        # Uma quinta acima, mais baixinha, de vez em quando.
        if i % 8 == 0:
            vozes.append(
                (i * batida + 0.02, marimba(nota(nome[0] + str(int(nome[1]) + 1)), 1.8, 0.10, decaimento=3.0))
            )

    misturado = somar(*vozes)

    # Bordao: duas oitavas graves muito baixas, so para o silencio nao ser
    # um buraco entre notas.
    n = int(dur * TAXA)
    if len(misturado) < n:
        misturado += [0.0] * (n - len(misturado))
    for i in range(n):
        t = i / TAXA
        misturado[i] += 0.055 * math.sin(2 * math.pi * nota("C3") * t)
        misturado[i] += 0.030 * math.sin(2 * math.pi * nota("G2") * t)

    # A costura do ciclo: o que sobrou a passar do fim volta para o
    # principio, para nao haver estalo nem silencio na emenda.
    cauda = misturado[n:]
    ciclo = misturado[:n]
    for i, s in enumerate(cauda):
        ciclo[i] += s

    # Entrada e saida muito curtas, por seguranca.
    fade = int(0.02 * TAXA)
    for i in range(fade):
        k = i / fade
        ciclo[i] *= k
        ciclo[n - 1 - i] *= k

    return ciclo


def main():
    print("-- a sintetizar")
    gravar("toque.wav", toque(), normalizar_para=0.55)
    gravar("certo.wav", certo(), normalizar_para=0.72)
    gravar("errado.wav", errado(), normalizar_para=0.62)
    gravar("nivel.wav", nivel(), normalizar_para=0.80)
    gravar("salto.wav", salto(), normalizar_para=0.7)
    gravar("fundo.wav", fundo(), normalizar_para=0.62)
    print("-- feito")


if __name__ == "__main__":
    main()
