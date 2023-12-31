"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome,
ou seja, funções anônimas.

.........................

# Função em Python
def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))


# Expressão Lambda
lambda x: 3 * x + 1

# Como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1 # Não é a forma ideal de utilizar, aqui apenas exemplo

print(calc(4))
print(calc(7))

.........................

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
# strip() remove espaço do início e do fim da variávesl, não do meio.
# title() capitaliza a inicial da string deixando maiusculo

print(nome_completo('angelica', 'JOLIE'))
print(nome_completo('FELICITY      ', 'Jones '))


.........................

# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também.

amar = lambda: 'Como não amar Python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x1, ..., xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

#OBS: Se passarmos mais argumentos do que parâmetros  esperados teremos TypeError

.........................

# Outro exemplo

autores = ['Issac asimov', 'Ray Bradbury', 'Iago Gonçalves', 'Jaine Floriano', 'Frank Sinatra', 'Ronaldo Fenomeno'
           'Helen Paula', 'H. G. Weels']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

.........................

.........................

"""

# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função
def geradora_funcao_quadratica(a, b, c):
    """retorna a função f(x) = a*x**2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))
