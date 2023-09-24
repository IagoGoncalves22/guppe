"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas processadas a
partir de outro iterável.

# Sintax da List Comprehension

[ dado for dado in iterável ]

.....................

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

Para entende rmelhor o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10


res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]

print(res)

.....................

# List Comprehension versos Loop

# Loop

numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in numeros:
    numeros_dobrado = numero * 2
    numeros_dobrados.append((numeros_dobrado))

print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros]) # Poderoso (coisa do Python Avançado)

.....................

.....................

.....................

.....................
"""

# outros exemplos

# 1

nome = 'Geek University'

print([letra.upper() for letra in nome])

# 2

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['Maria', 'Julia', 'Pedro', 'Guilherme', 'Vanessa']

print([caixa_alta(amigo) for amigo in amigos])

# 3

print(numero * 3 for numero in range(1, 10))

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])





