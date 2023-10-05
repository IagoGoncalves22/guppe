import time
from threading import Thread

CONTADOR = 50000000

def contagem_regressiva(n):
    while n > 0:
        n -= 1

ti = Thread(target=contagem_regressiva, args=(CONTADOR//2,))
t2 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))

inicio = time.time()
ti.start()
t2.start()
ti.join()
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}') # 4.845216989517212

# OBS: mesmo utilizando muiltthread, não dá muita diferença de otimização, devido GIL


