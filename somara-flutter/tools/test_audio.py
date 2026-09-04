"""Testes do modulo que faz o audio.

Correr a partir de somara-flutter/:
    python tools/test_audio.py

Nenhum destes testes grava audio -- sao todos sobre o que SE IA gravar.
Gravar levaria meia hora e precisaria de rede; e a decisao do texto que
esteve errada duas vezes, nao o motor de voz.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audio  # noqa: E402
from pronuncia import para_dizer  # noqa: E402


class OQueSeVaiDizer(unittest.TestCase):
    """`dito()` tem de aplicar as regras. E aqui que estava o defeito."""

    def test_aplica_as_unidades(self):
        self.assertEqual(
            audio.dito('Um quadrado tem 5 cm de lado.'),
            'Um quadrado tem 5 centímetros de lado.',
        )

    def test_aplica_os_sinais(self):
        self.assertEqual(audio.dito('2 + 1 = 3'), '2 mais 1 é igual a 3')
        self.assertEqual(audio.dito('2² × 2³'), '2² vezes 2³')

    def test_aplica_as_siglas(self):
        self.assertEqual(audio.dito('A SADC'), 'A ésse, á, dê, cê')

    def test_tira_os_emoji(self):
        self.assertEqual(audio.dito('Conta as maçãs 🍎🍎🍎'), 'Conta as maçãs')

    def test_nunca_devolve_o_texto_cru_quando_ha_regra(self):
        # O defeito, dito de outra maneira: o `materia.py` gravava isto tal
        # e qual. Se algum dia `dito` voltar a ser a identidade, este teste
        # cai.
        for ecra in ['2 + 1 = 3', '5 cm', 'A SADC', '48 : 6 = 8', '60 km/h']:
            self.assertNotEqual(audio.dito(ecra), ecra, msg=ecra)


class OsDoisNomes(unittest.TestCase):
    """O nome do ficheiro vem do ecra; o do manifesto vem do que se diz."""

    def test_o_ficheiro_nao_muda_com_a_pronuncia(self):
        ecra = 'Um quadrado tem 5 cm de lado.'
        # Mesmo que a regra de pronuncia mude amanha, o ficheiro e o mesmo.
        self.assertEqual(audio.nome_do_ficheiro(ecra), audio.sha(ecra) + '.mp3')
        self.assertNotEqual(audio.sha(ecra), audio.sha(audio.dito(ecra)))

    def test_o_manifesto_muda_com_a_pronuncia(self):
        ecra = '2 + 1 = 3'
        self.assertEqual(audio.sha(audio.dito(ecra)),
                         audio.sha('2 mais 1 é igual a 3'))


class OCurriculoInteiro(unittest.TestCase):
    """O que esta escrito no content.json e no manifesto bate certo."""

    @classmethod
    def setUpClass(cls):
        cls.dados = audio.carregar_content()
        cls.falas = audio.falas_do_curriculo(cls.dados)
        cls.manifesto = audio.ler_manifesto()

    def test_toda_a_fala_tem_ficheiro_no_disco(self):
        faltam = [f for f in self.falas if not (audio.AUDIO / f).exists()]
        self.assertEqual(faltam, [], 'audio declarado mas inexistente')

    def test_nenhum_ficheiro_esta_vazio(self):
        vazios = [f for f in self.falas
                  if (audio.AUDIO / f).stat().st_size < 1024]
        self.assertEqual(vazios, [], 'audio sem som la dentro')

    def test_o_manifesto_cobre_tudo(self):
        sem = [f for f in self.falas if f not in self.manifesto]
        self.assertEqual(sem, [], 'ficheiros sem registo no manifesto')

    def test_o_manifesto_bate_com_as_regras_de_hoje(self):
        # Este e o teste que o `compilar.sh` corre antes de compilar. Se
        # falhar, ha audio a dizer o que as regras ja nao mandam dizer.
        fora = [f for f, ecra in self.falas.items()
                if self.manifesto.get(f) != audio.sha(audio.dito(ecra))]
        self.assertEqual(
            fora[:10], [],
            f'{len(fora)} ficheiros desactualizados — regrava-os',
        )

    def test_a_materia_tem_o_nome_calculado_do_texto_limpo(self):
        # Convencao antiga que nao se pode partir: os 179 mp3 de aula foram
        # nomeados sobre o texto ja limpo, e nao sobre o bruto.
        import materia
        maus = []
        for curso in self.dados['cursos']:
            for u in curso['units']:
                for n in u['niveis']:
                    m = n.get('materia')
                    if m and m.get('audio'):
                        if materia.nome_da_materia(m) != m['audio']:
                            maus.append(m['audio'])
        self.assertEqual(maus, [], 'o nome da aula deixou de bater')


class AsFerramentasConcordam(unittest.TestCase):
    """Nenhuma ferramenta pode ter a sua propria ideia do que se diz."""

    def test_regravar_siglas_diz_o_mesmo_que_o_audio(self):
        from regravar_siglas import limpar as limpar_antigo
        dados = audio.carregar_content()
        for ecra in list(audio.falas_do_curriculo(dados).values())[:300]:
            self.assertEqual(audio.dito(ecra), limpar_antigo(para_dizer(ecra)),
                             msg=ecra[:60])


if __name__ == '__main__':
    unittest.main(verbosity=2)
