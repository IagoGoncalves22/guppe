"""
Módulo Collections: ordered Dict

# em um dicionário, a ordem de inserção dos elementos não é garantida
dicionario = {'a': 1, 'b': 2, 'c':3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

orderedDict -> É um dicionário, que nos garante a ordem dos elementos.

# Fazendo import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c':3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

"""
from collections import OrderedDict

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # True -> as ordens dos elementos não importa par ao dicionário

# Ordered Dict

odict1 = OrderedDict({'a':1, 'b': 2})
odict2 = OrderedDict({'b':2, 'a': 1})

print(odict1 == odict2) # False -> Já que a ordem dos elementos importa para o Ordered Dict





