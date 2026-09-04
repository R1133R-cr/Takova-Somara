"""Grava as vozes de festejo dos joguinhos.

Porque e que existem
--------------------
A pesquisa do Candy Crush mostrou uma coisa que se repete em todos os
jogos do genero: o elogio ESCALA com o feito. Nao ha uma voz -- ha uma
escada, e chegar ao topo dela e o que faz querer jogar outra vez. No
Candy Crush e "Sweet", "Tasty", "Divine", e a ultima exige trinta pecas
ou dez cascatas.

Aqui e a mesma ideia em portugues, com a mesma voz das licoes. Manter a
Raquel importa: a app inteira tem de soar a mesma pessoa, senao os
joguinhos parecem outra app colada por cima.

Um pouco mais depressa e mais aguda do que nas aulas -- sao exclamacoes,
nao explicacoes.

Correr a partir de somara-flutter/:
    python tools/vozes.py
"""

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "assets" / "som"

VOZ = "pt-PT-RaquelNeural"
TOM = "+30Hz"     # nas aulas e +25Hz; aqui um pouco mais acima
RITMO = "+6%"     # nas aulas e -5%; uma exclamacao nao se arrasta

# ficheiro -> o que se diz
FALAS = {
    "voz-boa.mp3": "Boa!",
    "voz-muito-bem.mp3": "Muito bem!",
    "voz-excelente.mp3": "Excelente!",
    "voz-fantastico.mp3": "Fantástico!",
    "voz-sequencia.mp3": "Que sequência!",
}


def gravar(texto: str, destino: Path) -> bool:
    r = subprocess.run(
        ["edge-tts", "--voice", VOZ, f"--pitch={TOM}", f"--rate={RITMO}",
         "--text", texto, "--write-media", str(destino)],
        capture_output=True,
    )
    return r.returncode == 0 and destino.exists() and destino.stat().st_size > 0


def main() -> int:
    DESTINO.mkdir(parents=True, exist_ok=True)
    for ficheiro, texto in FALAS.items():
        alvo = DESTINO / ficheiro
        if alvo.exists():
            print(f"   ja existia  {ficheiro}")
            continue
        if not gravar(texto, alvo):
            print(f"   FALHOU  {ficheiro}", file=sys.stderr)
            return 1
        print(f"   {alvo.stat().st_size:>6} bytes  {ficheiro}  ({texto})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
