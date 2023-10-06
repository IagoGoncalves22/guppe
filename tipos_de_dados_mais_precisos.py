"""

int, str, float, List, Set, Dict, etc...

def dobro(valor: int) -> int:
    return valor * 2

print(dobro(8))
print(dobro(42))

.....................

Versões novas Python

- Literal type
- Union
- Final
- Typed dictionaries
- Protocols

......................

def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operacao inválida {operacao!r}')

# O mypy não pega o erro porque não distingue str - e +, entende tudo como string.

......................

......................

......................

"""

# Literal type

from typing import Literal

# def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
#    pass

def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operacao inválida {operacao!r}')


calcula_v2('+', 6, 4)
calcula_v2('-', 10, 2)
calcula_v2('*', 3, 5)





