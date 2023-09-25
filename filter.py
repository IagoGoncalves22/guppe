"""
Filter

filter() -> Serve para filtrar dadosd e uma determinada coleção.

"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parãmetros, sendo
# uma função e um iterável.

res = filter(lambda valor: valor > media, dados) # Retorna True or False - Maior que a média
# res = filter(lambda x: x < media, dados) # Retorna True or False Menor que a média
print(type(res))
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter()
# eles são excluídos da memória.

print(f'Novamente: {list(res)}') # Na segunda vez zera o valor, igual Map




