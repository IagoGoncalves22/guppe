"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os -> Operating System - Sistema Operacional

....................

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente.
# Retorna o path (caminho) absoluto
print(os.getcwd()) # C:\Users\Iago Gonçalves - Dev\PycharmProjects\guppe

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd()) # C:\Users\Iago Gonçalves - Dev\PycharmProjects

os.chdir('..')

print(os.getcwd()) # C:\Users\Iago Gonçalves - Dev

os.chdir('..')

print(os.getcwd()) # C:\Users

os.chdir('..')

print(os.getcwd()) # C:\

os.chdir('..')

print(os.getcwd()) # C:\

....................

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('/home/geek')) # True

....................

# OBS para usuários Windows
# Se você, infelizmente, estiver utilizando um computador com windows.
# Terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('C:\\Users\\geek')) # True

....................

# Podemos identificar o sistema operacional com o módulo os

print(os.name) # posix (Linux e Mac), nt (Windows)


....................

# Podemos ter mais detalhes no sistema operacional
print(os.uname())

....................

print(sys.platform)

....................

# '/home/geek/workspace/sistema'

print(os.getcwd()) #

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd())

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório
# atual e o segundo o diretório que será juntado ao atual.

....................

# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir(''))


....................

....................

"""

# Fazer o import
import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir()

arquivos = list(scanner)

# print(arquivos)

# print(dir(arquivos[0])

print(arquivos[0].inode()) # ??
print(arquivos[0].is_dir()) # É um diretório? False
print(arquivos[0].is_file()) # É um arquivo True
print(arquivos[0].is_symlink()) # É um link ? False
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) # Caminho até o arquivo
print(arquivos[0].stat()) # Estatísticas...

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim
# quando abrimos um arquivo.

scanner.close()

