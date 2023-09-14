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

"""

nome = 'Geek university'
lista = [1,3,5,7,9]
numeros = range(1,10) # Temos que transformar em uma lista
# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

 # Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
     print(numero)
