"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

...................

# Refaturando uma função

def quadrado(numero):
    # return numero * numero
    return numero ** 2
print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

print(quadrado()) # TypeError

...................

# Refatorando a função

def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}')

cantar_parabens('Marcos')

...................

# Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada
# em uma função quantos parãmetros forem necessários. Eles são separados por vírcula.

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(5, 4, 'Python '))

# OBS: Se a gente informar um número erado de parâmetro ou argumento, temos TypeError

# print(soma(2, 3, 4)) # TypeError - Passando argumentos a mais
# print(soma(4)) # TypeError - Passando argumentos a menos
...................

...................

"""

# Nomeando parâmetros

# def nome_completo(string1, string2):
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome}'

print(nome_completo('Angelina', "Jolie"))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmetros importa!