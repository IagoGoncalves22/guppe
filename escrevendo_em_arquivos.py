"""
Escrevendo em arquivos


# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele.
Apenas ler. Da mesma forma, se abrirmos um arquivo para escrita, não podemos ler
apenas escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir ele será
criado. Caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma
todo o conteúdo do arquivo anterior é perdido.

# Exemplo de escrita - modo 'w' - write (escrita)

.......................

# Forma Pythônica
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.')

.......................

# Forma tradicional de escrita em arquivo (Não Pythônico)
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')

arquivo.close()


.......................

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek' * 1000)


.......................

.......................
"""

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

