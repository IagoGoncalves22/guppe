"""
Filter

filter() -> Serve para filtrar dadosd e uma determinada coleção.

....................

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

....................

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))

....................

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

# res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(None, paises)
res = filter(lambda pais: pais != '', paises)

print(list(res))

....................

# A diferena entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto
# mapeando a função para cada elemento do iterável.

# Filter() -> Recebe dois parãmetros, uma função e um iterável e retorna um objeto
# filtrando apenas os elementos de acordo com a função.

....................

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos!", "Eu adoro pizza"]},
    {"username": "Carla", "tweets": ["Eu amo meus gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachoorro", "Eu vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Filtrar os usuários que estão inativos no Twiter

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

....................

....................

....................

....................

"""
# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que
# cada nome tenha menos de 5 caracteres.

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)


