"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são testes unitários ?

Teste é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, móduloes, etc.

OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()


TestCase -> Casos de teste para sua unidade

# Conhecendo as assertions

Método                         checa que
assertEqual(a,b)               a == b
assertNotEqual(a, b)           a != b
assertTrue(x)                  x é verdadeiro
assertFalse(x)                 x é falso
assertIs(a, b)                 a é b
assertIsNot(a, b)              a não é b
assertIfNone(x)                x é None
assertIsNotNone(x)             x não é None
assertIn(a, b)                 a está em b
assertNotIn(a, b)              a não está em b
assertIsInstance(a, b)         a é instância de b
assertnotIsInstance(a, b)      a não é instância de b

Por convenção, todos os testes em um teste case, devem ter o seu nome iniciado com underline _

Para executar os testes com unittest

python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose

python nome_do_modulo -v

# Docstrings nos testes

Podemos acrescentar (e é recomendado) docstrings nos testes.



"""

# Prática - Utilizando a abordagem TDD

