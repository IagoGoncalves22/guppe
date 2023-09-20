"""
Módulo Collections - Counter (Contador)

Collections - High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo
Collections Counter que é parecido com um dicionário. Contendo como chave
o elemento da lista passada como parâmetro e como valor a quantidade de
ocorrências desse elemento.

.......................

# Realizando o import
from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 45, 46, 46, 46, 59]

# Utilizando o Counter
res = Counter(lista)
print(type(res))

print(res)

# Veja que para cada elemento da lista, o Counter criou uma chave e
# colocou como valor a quantidade de ocorr~encias:
# Counter({1: 5, 2: 4, 3: 4, 4: 3, 46: 3, 45: 1, 59: 1})

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

.......................

.......................

.......................

.......................
"""

from collections import Counter

# Exemplo 3

texto = """ Python is a high-level, general-purpose programming language.
 Its design philosophy emphasizes code readability with the use of significant indentation.[34]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms,
including structured (particularly procedural), object-oriented and functional programming.
 It is often described as a "batteries included" language due to its comprehensive standard library.[35][36]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language
 and first released it in 1991 as Python 0.9.0.[37] Python 2.0 was released in 2000. Python 3.0, released
  in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18,
   released in 2020, was the last release of Python 2.[38]
   """

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrências no texto
print(res.most_common(5))
