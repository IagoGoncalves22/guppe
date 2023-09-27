"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erros geradas para
execução do nosso código.

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe, ou seja, você
escreveu algo que o Python não reconhece como parte da linguagem.

Exemplos SyntaxError

a)

def funcao:
    print('Geek University')

b)

def = 1

c)

:return

d)


.......................

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

a)

print(geek)

b)

geek()
.......................

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

a)

print(len(5))

b)

print('Geek' + [])

c)

d)

..................

4 - IndexError

a)

lista = ['Geek']
print(lista[10])

b)

lista = ['Geek']
print(lista[10][5])

.................

5 - ValueError -> Ocorre uando uma função/operação, built-in (integrada) recebe
um argumento com tipo correto mas valor inapropriado.

# Exemplos

a)

print(int('Geek'))
.................

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave
que não existe.

Exemplos KeyError:

a)

dic = {}
print(dic['geek'])

b)

.................

7 - AttributeError -> Ocorre quando uma variável não tem um atributo /função.

Exemplos AttributeError

a)

tupla = [11, 2, 31, 4]
print(tupla.sort())

.................

8 - IdentationError -> Ocorre quando não respeitamos a indentaão do Python
que é de 4 espaços.

Exemplo:

a)

def nova():
print('Geek')

b)

for i in range(10):
i + 1

.................

OBS: Exceptions e Erros são sinônimos na programação.

.................
"""

# Exemplos

for i in range(10):
i + 1



