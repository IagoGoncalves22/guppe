"""
Loop for
Loop -> Estrutura de repetição
For -> Uma dessas estruturas

Python
for item in interavel:
 //execução do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplos de iteráveis:
- String
- Lista
- Range

nome = 'Geek university'
lista = [1,3,5,7,9]
numeros = range(1,10) # Temos que transformar em uma lista
# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

 # Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
     print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valof_final)
OBS: o valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - não

for numero in range(1,10):
    print(numero)


nome = 'Geek University'
lista = [1,3,5,7,9]
numeros = range(1,10) # Temos que transformar em uma lista


Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), (3,'k'), (4, ' '), (5, 'U')...)

for i, v in enumarate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)
for _, letra in enumerate(nome):
    print(letra)

OBS: quando não precisamos de um valor podemos utilizar o _

nome = 'Geek University'
lista = [1,3,5,7,9]
numeros = range(1,10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor[1])

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
    print(f'A soma é {soma}')

    nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

# Original: U+1F60D
# Modificado: U0001F60D

#emoji = 'U0001F60D'

for _ in range(3):
    for num in range(1,11):
        print('\U0001F60D' * num)






