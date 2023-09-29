"""
Sistema de Arquivos - Manipulação

................

# Arquivo
# Descobrindo se um arquivo ou diretório existe
print(os.path.exists('arquivo.txt')) # False
print(os.path.exists('frutas.txt')) # True

.................

# Diretório

# Paths relativos
print(os.path.exists('geek')) # True
print(os.path.exists('geek/university')) # True
print(os.path.exists('geek/university/geek3.py')) # True
print(os.path.exists('outro')) # False

# Paths absolutos
print(os.path.exists('/home/geek/university')) # False
print(os.path.exists('/home/geek/Imagem')) # False

................

# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3

with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

................

# Criando arquivos

os.mknod("arquivo-teste4.txt") # AttributeError: module 'os' has no attribute 'mknod'

os.mknod('/home/geek/university.txt') # AttributeError: module 'os' has no attribute 'mknod'

# OBS: Se você estiver utilizando no Mac OS, pode haver  um erro de PermissionError.

# OBS: Criando um arquivo via mknod() se o arquivo já existir temos o erro FileExistError


................

# Criando diretórios - únicos (um a um)

# Path Relativo
os.mkdir('templates')

# Path Absoluto
os.mkdir('/home/geek/templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista,
# teremos FileExistError

................

os.mkdir('/etc/templates')

# OBS: Se não tivermos permissão para criar o diretóri teremos PermissionError

................

# Criando multi-diretórios (árvore de diretórios)
os.makedirs('templates/geek/university')

# OBS: Se já existir, teremos um FileError

................

os.makedirs('templete2/novo2/outro2', exist_ok=True)
................

"""

# Fazer o import

import os

os.rename('templete2', 'geek2')

# OBS: Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

