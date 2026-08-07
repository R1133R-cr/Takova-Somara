import 'dart:convert';
import 'package:flutter_test/flutter_test.dart';
import 'package:somara/models/content.dart';
import 'package:somara/services/conteudo_remoto.dart';

/// A validação é a única coisa entre um ficheiro publicado por engano e
/// todas as apps instaladas. Se deixar passar lixo, não há como desfazer:
/// a app deixa de abrir e já não se actualiza a si própria.
///
/// Por isso estes testes atacam-na com conteúdo estragado de propósito.
void main() {
  /// Currículo mínimo que deve passar. Os testes partem daqui e estragam
  /// uma coisa de cada vez.
  Map<String, dynamic> valido({int versao = 20260808, int niveis = 4}) => {
        'versao': versao,
        'cursos': [
          {
            'id': 'mat-1c',
            'disciplina': 'Matemática',
            'classe': '1ª classe',
            'units': [
              {
                'id': 'u1',
                'titulo': 'Contar',
                'niveis': [
                  for (var i = 0; i < niveis; i++)
                    {
                      'id': 'n$i',
                      'titulo': 'Nível $i',
                      'questoes': [
                        {
                          't': 'choice',
                          'q': 'Qual é maior?',
                          'options': ['3', '7'],
                          'a': 1,
                        },
                      ],
                    },
                ],
              },
            ],
          },
        ],
      };

  Conteudo ler(Map<String, dynamic> j) => Conteudo.deTexto(json.encode(j));

  test('conteúdo bom e mais recente é aceite', () {
    expect(ConteudoRemoto.validar(ler(valido()), 20260807), isNull);
  });

  group('recusa por não valer a pena trocar', () {
    test('versão igual à que já se tem', () {
      final p = ConteudoRemoto.validar(ler(valido(versao: 20260807)), 20260807);
      expect(p, contains('não é mais recente'));
    });

    test('versão mais antiga — protege de uma reversão acidental', () {
      final p = ConteudoRemoto.validar(ler(valido(versao: 20260101)), 20260807);
      expect(p, contains('não é mais recente'));
    });
  });

  group('recusa por estar estragado', () {
    test('sem cursos nenhuns', () {
      final j = valido()..['cursos'] = [];
      expect(ConteudoRemoto.validar(ler(j), 0), contains('sem cursos'));
    });

    test('curso com poucos níveis daria um mapa deserto', () {
      expect(ConteudoRemoto.validar(ler(valido(niveis: 2)), 0),
          contains('níveis'));
    });

    test('nível sem perguntas', () {
      final j = valido();
      (((j['cursos'] as List)[0]['units'] as List)[0]['niveis'] as List)[0]
          ['questoes'] = [];
      expect(ConteudoRemoto.validar(ler(j), 0), contains('sem perguntas'));
    });

    test('pergunta sem enunciado', () {
      final j = valido();
      (((j['cursos'] as List)[0]['units'] as List)[0]['niveis'] as List)[0]
          ['questoes'][0]['q'] = '   ';
      expect(ConteudoRemoto.validar(ler(j), 0), contains('sem enunciado'));
    });

    test('resposta a apontar para uma opção que não existe', () {
      // O erro mais fácil de cometer a editar à mão, e o que rebentaria a
      // lição a meio, com a criança à frente.
      final j = valido();
      (((j['cursos'] as List)[0]['units'] as List)[0]['niveis'] as List)[0]
          ['questoes'][0]['a'] = 9;
      expect(ConteudoRemoto.validar(ler(j), 0), contains('fora das opções'));
    });

    test('escolha com uma só opção', () {
      final j = valido();
      (((j['cursos'] as List)[0]['units'] as List)[0]['niveis'] as List)[0]
          ['questoes'][0]['options'] = ['3'];
      expect(ConteudoRemoto.validar(ler(j), 0), contains('duas opções'));
    });

    test('curso sem disciplina', () {
      final j = valido();
      (j['cursos'] as List)[0]['disciplina'] = '';
      expect(ConteudoRemoto.validar(ler(j), 0), contains('sem disciplina'));
    });
  });

  group('texto que nem sequer se lê', () {
    test('ficheiro truncado a meio do descarregamento', () {
      final inteiro = json.encode(valido());
      final cortado = inteiro.substring(0, inteiro.length ~/ 2);
      expect(() => Conteudo.deTexto(cortado), throwsA(anything));
    });

    test('não é JSON', () {
      expect(() => Conteudo.deTexto('<html>404 not found</html>'),
          throwsA(anything));
    });

    test('tipo de pergunta que a app não conhece', () {
      // Acontece se o conteúdo for adiante da app instalada. Tem de recusar,
      // senão a lição rebenta ao chegar a essa pergunta.
      final j = valido();
      (((j['cursos'] as List)[0]['units'] as List)[0]['niveis'] as List)[0]
          ['questoes'][0]['t'] = 'desenhar';
      expect(() => ler(j), throwsA(isA<FormatException>()));
    });
  });

  test('o conteúdo que vai dentro da app passa na sua própria validação', () async {
    // Guarda contra publicarmos nós um ficheiro que a app recusaria.
    TestWidgetsFlutterBinding.ensureInitialized();
    final c = await Conteudo.carregar();
    expect(c.versao, greaterThan(0), reason: 'conteúdo sem número de versão');
    expect(ConteudoRemoto.validar(c, c.versao - 1), isNull);
  });
}
