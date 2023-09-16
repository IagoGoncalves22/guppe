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
# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial, o mesmo será desclocado para direita
lista1.insert(2, 'Novo Valor')
print(lista1)

............................
# Podemos facilmente juntar duas listas
# lista6 = lista1 + lista2
lista1.extend(lista2)
print(lista1)
............................
# Podemos facilmente inverter uma lista utilizando reverse

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[:: -1])
print(lista2[:: -1])
............................
# Copiar uma lista

lista6 = lista2.copy()
print(lista6)
............................
# Podemos contar quantos elementos existem dentro da lista
print(len(lista1))
print(len(lista2))

............................
# Podemos remover facilmente o último elemento dentro da lista
# OBS: O pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita deste índice serão deslocados para esquerda
# OBS: Se ão houver elemento no índice informado, teremos o erro IndexError.
lista5.pop(2)
print(lista5)

............................
# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)
............................
# Podemos facilmente repetir elementos em uma lista
nova = [1,2,3]
print(nova)
nova = nova * 3
print(nova)

............................
# Podemos facilmente converter uma string para uma lista

# Exemplo 1
# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2
curso = 'programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')

............................
# Convertendo uma lista em uma string

lista6 = ['programação', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: Peça a lista6, colca espaço em cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Peça a lista6, colca $ em cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

............................
# Podemos realmente colocar qualquer tipo de dado em uma lista inclusive misturando esses dados

lista6 = [1,2.34, True, 'Geek', 'd', [1,2,3], 453656456]
print(lista6)
print(type(lista6))

............................
# Iterando sobre listas

# Exemplo 1 utilizando for

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

............................
# Utilizando variáveis em listas
numeros = [1,2,3,4,5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)
............................
# Fazemos acesso aos slementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

# Fazemos acesso aos slementos de forma indexada inversa

print(cores[-1]) # branco
print(cores[-2]) # azul
print(cores[-3]) # amarelo
print(cores[-4]) # verde
print(cores[-5]) # erro pois não existe a posição -5


for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
............................
# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

............................
type([])

lista1 = [1,99,4,27,15,22,3,1,44,42,27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')
............................
# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)
............................

............................

............................

............................

............................

............................

............................

............................
"""





