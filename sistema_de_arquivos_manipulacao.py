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

# OBS: Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek.txt')

# Renomear arquivos e diretórios

# Arquivos
os.rename('frutas.txt', 'cesta.txt')

................

# ATANÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório
# eles não vão para a lixeira. Eles somem.

# Removendo arquivos.
os.remove('geek.txt')

# OBS: Se você estiver no windows e o arquivo que você deletar estiver em uso, você terá
# um erro.

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError.

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um isADirectoryError

................

# Removendo diretórios

os.rmdir('templates')

# OBS: Se o diretório tiver qualquer couteúdo teremos um OSError

# OBS: Se o diretório não existir teremos um FileNotFoundError


................

# Removendo uma árvore de arquivos
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)
    if not arquivo.is_file():
        os.rmdir(arquivo.path)

................

# Podemos remover uma árvore de diretórios vazios

os.removedirs('geek2/mais')

# Se algum dos diretórios contiver arquivos ou outro diretório, o processo para.

................

sudo apt-get install lsb-core
................

# ATENÇÃO: Ao remover arquivos e diretórios com Python eles não vão para lixeira. Deleta definitivo.

# Importando a biblioteca send2trash (envia arquivos e diretórios para lixeira)
from send2trash import send2trash

os.remove('cesta1.txt') # Não vai para a lixeira. É deletado.

send2trash('cesta2.txt') # Vai para lixeira. Pode ser restaurado.

# OBS: Se o arquivo não existir, teremos OSError

................

from send2trash import send2trash

send2trash('teste')

................

# Criando um diretório temporário

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporário.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
        input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele
# criando um arquivo para escrevermos um texto. No final, usamos um input
# só para mantermos os arquivos temprorários 'vivos' dentro dos blocos with.

# OBS: possivelmente, o código acima não irá funcionar se você estiver utilizando o windows.
# Por conta desse sistema trabalhar de forma diferente com os arquivos temporários.

................

# Criando um arquivo temporário

with tempfile.SpooledTemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos b.

................

# Sem o bloco with

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

................

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()

https://docs.python.org/3/library/os.html?highlight=os#module-os
................

................

"""

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile


