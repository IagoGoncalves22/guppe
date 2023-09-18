"""
Dicionários

OBS: Em algumas linguagens de programção, os dicionários Python são conhecidos
por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

OBS: Sobre dicionários:
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

....................

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai',}

print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

....................

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

# OBS: KeyError, caso tentarmos utilizar uma chave que não existe.

# Forma 2 - Acessando via get - Recomendado.

print(paises.get('br'))
print(paises.get('ru'))



# Caso o get não encontre o objeto com a chave informada será retornado o valor
# None e não será gerado keyerror

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')


# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('py', 'Não encontrato')

print(f'encontrei o país {pais}')

....................

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai',}

# Podemos verificar se determinada chave encontra-se em um difionário

print('br' in paises) # True, chave existe
print('ru' in paises) # False, chave não existe
print('Estados Unidos' in paises) # False, não busca pelo valor

if 'ru' in paises:
    russia = paises['ru']

....................

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean),
# inclusive lista, tupla, dicionário, como chaves de dicionários.

# Tuplas por exemplo são bastrante interessantes de serem utilizadas como
# chave de dicionários pois as mesmas são imutáveis.

localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova Yorke',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

....................

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 200, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}  # receita.update({'mai': 500})

receita.update(novo_dado)

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# CONCLUSÃO 1: A forma de acicionar novos elementos ou atualizar
# dados em um dicionário é a mesma.

# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.
....................

....................

....................

....................

....................

"""

