"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo já exista gera FileExistsError.
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e Escrita. (Temos o controle do cursor).

#OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
será adicionado ao final dor arquivo. Com o modo 'a', não controlamos o cursos.

http://docs.python./3/library/functions.html#open

..........................

# Exemplo x

try:
    with open('university.txt', 'w') as arquivo:
        arquivo.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Arquivo já existe')

..........................

# Exemplo a

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

..........................

..........................

..........................

"""

with open('outro.txt', 'r+') as arquivo:
    arquivo.write('Adicionar\n')
    arquivo.seek(11)
    arquivo.write('Nova linha.\n')
    arquivo.seek(32)
    arquivo.write('Mais uma linha.\n')

