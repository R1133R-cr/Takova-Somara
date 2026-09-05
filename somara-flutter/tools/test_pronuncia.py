"""Testes do que a Raquel diz a partir do que esta escrito.

Correr a partir de somara-flutter/:
    python tools/test_pronuncia.py

Nao usa pytest de proposito: o Python desta maquina e uma versao embutida
sem pip, e um teste que nao corre nao serve para nada.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pronuncia import (  # noqa: E402
    CONJUNTOS,
    dizer_unidades,
    nome_da_unidade,
    para_dizer,
)


class SimbolosDeUnidade(unittest.TestCase):
    """"cm" tem de virar "centimetro", nao "ce-eme".

    O defeito: a voz lia os simbolos letra a letra. "5 cm" saia "cinco
    ce-eme" e a crianca da 4a classe que esta a aprender o perimetro ouvia
    duas consoantes em vez de uma unidade.
    """

    def test_comprimento(self):
        self.assertEqual(nome_da_unidade('mm'), 'milímetro')
        self.assertEqual(nome_da_unidade('cm'), 'centímetro')
        self.assertEqual(nome_da_unidade('dm'), 'decímetro')
        self.assertEqual(nome_da_unidade('m'), 'metro')
        self.assertEqual(nome_da_unidade('km'), 'quilómetro')

    def test_massa(self):
        self.assertEqual(nome_da_unidade('mg'), 'miligrama')
        self.assertEqual(nome_da_unidade('g'), 'grama')
        self.assertEqual(nome_da_unidade('kg'), 'quilograma')
        self.assertEqual(nome_da_unidade('t'), 'tonelada')

    def test_capacidade(self):
        self.assertEqual(nome_da_unidade('ml'), 'mililitro')
        self.assertEqual(nome_da_unidade('dl'), 'decilitro')
        self.assertEqual(nome_da_unidade('l'), 'litro')
        self.assertEqual(nome_da_unidade('L'), 'litro')


class NoMeioDaFrase(unittest.TestCase):
    """O simbolo so se expande onde e mesmo uma unidade."""

    def test_depois_de_um_numero(self):
        self.assertEqual(dizer_unidades('5 cm'), '5 centímetros')
        self.assertEqual(dizer_unidades('250 g'), '250 gramas')
        self.assertEqual(dizer_unidades('300 ml'), '300 mililitros')
        self.assertEqual(dizer_unidades('2,5 km'), '2,5 quilómetros')

    def test_um_fica_no_singular(self):
        # "um centimetros" seria erro de portugues numa app que ensina
        # portugues.
        self.assertEqual(dizer_unidades('1 cm'), '1 centímetro')
        self.assertEqual(dizer_unidades('1 kg'), '1 quilograma')
        # Mas "1 000" nao e "1".
        self.assertEqual(dizer_unidades('1 000 m'), '1 000 metros')

    def test_colado_ao_numero(self):
        self.assertEqual(dizer_unidades('5cm'), '5 centímetros')

    def test_depois_de_em(self):
        # "Qual e o perimetro, em cm?" -- aqui nao ha numero antes, e mesmo
        # assim e uma unidade. Sao 4 casos no curriculo, todos com cm.
        self.assertEqual(
            dizer_unidades('Qual é o perímetro, em cm?'),
            'Qual é o perímetro, em centímetros?',
        )
        self.assertEqual(
            dizer_unidades('Qual é a área, em cm quadrados?'),
            'Qual é a área, em centímetros quadrados?',
        )

    def test_por_hora(self):
        # A barra ficaria ", " e a voz dizia "sessenta ce-eme, aga".
        self.assertEqual(para_dizer('60 km/h'), '60 quilómetros por hora')


class OQueNaoSeToca(unittest.TestCase):
    """As letras do Portugues da 1a classe nao sao unidades.

    Esta e a razao pela qual a regra tem de estar ancorada no numero. O
    curriculo tem 13 ocorrencias da letra M, 7 do L e 2 do l minusculo, e
    nenhuma delas e uma unidade. Uma regra que apanhasse letras soltas
    poria a voz a dizer "litro mais a igual a" onde esta "L + A = ?".
    """

    def test_letras_isoladas_da_1a_classe(self):
        for texto in [
            'Sílabas com L e T',
            'M + A = ?',
            'Escreve: L + I',
            'O L e o T também formam sílabas.',
            'G',
            'M',
        ]:
            self.assertEqual(
                dizer_unidades(texto), texto,
                msg=f'mexeu numa letra: {texto!r}',
            )

    def test_licao_dos_plurais(self):
        # "Termina em l?" é sobre a letra l, e cai mesmo ao lado da regra
        # do "em <simbolo>".
        t = 'Termina em l? Troca por is.'
        self.assertEqual(dizer_unidades(t), t)
        t2 = ('O plural forma-se quase sempre com s. Mas as palavras '
              'terminadas em l trocam-no por is.')
        self.assertEqual(dizer_unidades(t2), t2)

    def test_maximo_divisor_comum(self):
        t = 'O m.d.c. é o maior divisor comum de os dois.'
        self.assertEqual(dizer_unidades(t), t)
        t2 = 'O m.m.c. é o menor múltiplo comum.'
        self.assertEqual(dizer_unidades(t2), t2)

    def test_metical_continua_a_ser_metical(self):
        # MT ja era tratado, e nao pode ser apanhado pela regra nova.
        self.assertEqual(para_dizer('Tens 5 MT.'), 'Tens 5 meticais.')


class OQueJaFuncionava(unittest.TestCase):
    """A regra nova nao pode desfazer as que ja la estavam."""

    def test_siglas(self):
        self.assertEqual(para_dizer('A SADC'), 'A ésse, á, dê, cê')

    def test_sinais_de_contas(self):
        self.assertEqual(para_dizer('2 + 1 = 3'), '2 mais 1 é igual a 3')
        self.assertEqual(para_dizer('48 : 6 = 8'),
                         '48 a dividir por 6 é igual a 8')
        self.assertEqual(para_dizer('3 × 4'), '3 vezes 4')
        self.assertEqual(para_dizer('10 − 2'), '10 menos 2')

    def test_dois_pontos_de_pontuacao_nao_sao_divisao(self):
        self.assertEqual(para_dizer('Conta assim: 10 e 20'),
                         'Conta assim: 10 e 20')

    def test_a_letra_x_de_peixes(self):
        self.assertEqual(para_dizer('Quantos peixes?'), 'Quantos peixes?')

    def test_o_hifen_de_contam_se(self):
        self.assertEqual(para_dizer('Contam-se os dedos.'),
                         'Contam-se os dedos.')


class OCurriculoInteiro(unittest.TestCase):
    """Passar o content.json todo pela regra e ver o que ela mexe.

    Um teste de unidade prova que a regra faz o que se pediu. Este prova
    que ela nao faz mais nada -- que e onde estava o perigo.
    """

    @classmethod
    def setUpClass(cls):
        import json
        raiz = Path(__file__).resolve().parent.parent
        dados = json.loads(
            (raiz / 'assets' / 'content.json').read_text(encoding='utf-8'))
        cls.textos = []
        chaves = ('q', 'a', 'explica', 'exemplo', 'lembra', 'titulo',
                  'face', 'options')

        def colher(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k in chaves:
                        if isinstance(v, str):
                            cls.textos.append(v)
                        elif isinstance(v, list):
                            cls.textos.extend(
                                [x for x in v if isinstance(x, str)])
                        else:
                            colher(v)
                    else:
                        colher(v)
            elif isinstance(o, list):
                for x in o:
                    colher(x)

        colher(dados)

    def test_nenhuma_letra_solta_vira_unidade(self):
        proibidas = ['litro', 'metro', 'grama', 'tonelada']
        for t in self.textos:
            dito = dizer_unidades(t)
            if dito == t:
                continue
            # Se mexeu, tem de haver um numero ou um "em" antes do sitio
            # onde mexeu. Basta procurar se o texto original tinha digitos
            # ou a palavra "em" seguida de simbolo de duas letras.
            import re
            tem_numero = bool(re.search(r'\d', t))
            tem_em = bool(re.search(r'\bem (mm|cm|dm|km|mg|kg|ml|dl)\b', t))
            self.assertTrue(
                tem_numero or tem_em,
                msg=f'expandiu sem numero nem "em": {t!r} -> {dito!r}',
            )
            for p in proibidas:
                if p in dito and p not in t:
                    self.assertTrue(
                        tem_numero or tem_em,
                        msg=f'inventou "{p}" em {t!r}',
                    )

    def test_as_licoes_de_letras_ficam_intactas(self):
        for t in self.textos:
            # Textos que sao claramente sobre letras: curtos, com "+" de
            # silaba ou a falar de silabas.
            if 'ílaba' in t or ('+' in t and '=' in t and len(t) < 25):
                self.assertEqual(
                    dizer_unidades(t), t,
                    msg=f'mexeu numa lição de letras: {t!r}')


class OsEspacosParaPreencher(unittest.TestCase):
    """A linha de preencher diz-se como pausa, e nao como nada.

    "Completa: A menina e ___." lido sem o espaco sai "completa, a menina e"
    e acaba ali. A crianca que nao le -- que e justamente quem depende do
    audio -- nao fica a saber que ha um buraco para encher, nem onde.

    Isto nao foi inventado agora: e o que ja estava gravado nos 43
    ficheiros com espacos, desde sempre. Conferi-os um a um contra
    gravacoes novas, e o tamanho bate ao byte com as reticencias e com mais
    nenhuma forma -- nem com a resposta la dentro, que era a hipotese que
    era preciso excluir.
    """

    def test_o_espaco_vira_pausa(self):
        self.assertEqual(para_dizer('Completa: A menina é ___.'),
                         'Completa: A menina é ....')
        self.assertEqual(para_dizer('Um quadrado tem __ lados iguais.'),
                         'Um quadrado tem ... lados iguais.')

    def test_entre_numeros_tambem(self):
        self.assertEqual(para_dizer('Qual símbolo completa? 45 __ 54'),
                         'Qual símbolo completa? 45 ... 54')

    def test_nunca_diz_a_resposta(self):
        # Dizer a resposta em voz alta era pior do que o silencio: dava a
        # solucao a quem estivesse a ouvir em vez de a ler.
        dito = para_dizer('Completa: A menina é ___.')
        for palavra in ('bonita', 'alta', 'boa'):
            self.assertNotIn(palavra, dito)

    def test_um_underscore_solto_nao_e_espaco(self):
        self.assertEqual(para_dizer('o ficheiro a_b'), 'o ficheiro a_b')


class Conjuntos(unittest.TestCase):
    """Os simbolos que entram na 7a classe.

    A voz comia-os em silencio: "5 ∈ A" saia "cinco a". Um erro que nao se
    ouve e pior do que um que se ouca -- a frase que sobra ate parece uma
    frase, e quem depende do audio nao tem como desconfiar.
    """

    def test_pertence(self):
        self.assertEqual(para_dizer('5 ∈ A'), '5 pertence a A')

    def test_nao_pertence(self):
        self.assertEqual(para_dizer('7 ∉ B'), '7 não pertence a B')

    def test_contido(self):
        self.assertEqual(para_dizer('A ⊂ B'), 'A está contido em B')

    def test_reuniao_e_interseccao(self):
        self.assertEqual(para_dizer('A ∪ B'), 'A reunião B')
        self.assertEqual(para_dizer('A ∩ B'), 'A intersecção B')

    def test_as_letras_dos_conjuntos_dizem_o_nome(self):
        # "z" nao se ouve; "zê" ouve-se.
        self.assertEqual(para_dizer('o conjunto ℤ'), 'o conjunto zê')

    def test_nenhum_simbolo_fica_por_dizer(self):
        for simbolo in CONJUNTOS:
            self.assertNotIn(simbolo, para_dizer(f'x {simbolo} y'),
                             f'o {simbolo} passou em silencio')


class Fraccoes(unittest.TestCase):
    """A barra da fraccao nao e uma virgula.

    Eram 53 textos do curriculo, quase todos da 2a e da 3a classe -- onde a
    crianca esta a aprender exactamente isto -- lidos como duas listas de
    numeros: "Qual e maior: 1, 2 ou 1, 4?".
    """

    def test_as_partes_tem_nome(self):
        self.assertEqual(para_dizer('3/4 do bolo'), '3 quartos do bolo')
        self.assertEqual(para_dizer('2/3 das mangas'), '2 terços das mangas')

    def test_o_singular_concorda(self):
        self.assertEqual(para_dizer('1/2 do bolo'), '1 meio do bolo')
        self.assertEqual(para_dizer('1/10 do total'), '1 décimo do total')

    def test_acima_do_decimo_diz_avos(self):
        self.assertEqual(para_dizer('5/12 do bolo'), '5 12 avos do bolo')

    def test_um_par_de_anos_nao_e_fraccao(self):
        # O travao dos dois algarismos existe para isto.
        self.assertEqual(para_dizer('o ano 2024/2025'), 'o ano 2024, 2025')


class DivisaoComDoisPontos(unittest.TestCase):
    """A divisao nao e so entre dois algarismos.

    O curriculo tinha tres contas escritas com um underscore, uma letra e um
    parentesis do lado esquerdo. A regra antiga so olhava para algarismos, e
    por isso liam-se como pontuacao -- ou seja, como uma pausa. A conta
    desaparecia do audio sem deixar rasto.
    """

    def test_depois_de_um_algarismo(self):
        self.assertIn('a dividir por', para_dizer('48 : 6 = 8'))

    def test_depois_de_uma_letra(self):
        self.assertIn('a dividir por', para_dizer('x : 4 = 12'))

    def test_depois_de_um_espaco_por_preencher(self):
        self.assertIn('a dividir por', para_dizer('___ : 5 = 6'))

    def test_depois_de_um_parentesis(self):
        self.assertIn('a dividir por', para_dizer('(base × altura) : 2'))

    def test_a_pontuacao_normal_fica_quieta(self):
        # Sem espaco antes dos dois pontos nao ha divisao nenhuma.
        self.assertEqual(para_dizer('Nota: 5 pontos'), 'Nota: 5 pontos')


if __name__ == '__main__':
    unittest.main(verbosity=2)
