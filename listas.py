"""
Listas
............................
Listas em Python funcionam como vetores/matrizes (arrays) em outras
linguagens, com a diferença de serem DINÂMICO e também de podermos colocar
QUALQUER tipo de dado.

- Dinâmico: não possui tamanho fixo; Ou seja, podemos criar listas e
adicionarmos elementos enquanto tiver memória disponível.

- Qualquer tipo de dado: não possuem tipo de dado fixo. Podemos colocar qualquer
tipo de dado.

As listas em Python são representadas por colchetes: []
............................
# Podemos facilmente checar se determinado valor está contido na lista

num = 11

if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)
............................
# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))
............................
# Adicionar elementos em listas
# Para adicionar elementos em listas, utilizamos append

print(lista1)
lista1.append(42)
print(lista1)

............................
# OBS: com append só consguimos adicionar um elemento por vez
# mas é possível adicionar uma lista

lista1.append([8,3,1]) # Coloca a lista como elemento único (sublista)
print(lista1)

if [8,3,1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional a lista
print(lista1)

............................

............................

............................

............................
"""
type([])

lista1 = [1,99,4,27,15,22,3,1,44,42,27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')







