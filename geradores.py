"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterador é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Exmpressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

................................................................................
/ Funções                               / Generator Functions                  /
............................. ..................................................
/ utilizam return                      / utilizam yield                        /
................................................................................
/ retorna uma vez                     / podem utilizar yield multiplas vezes   /
................................................................................
/ quando executa, retorna um valor   / quanto excecutada, retorna um generator /
................................................................................

....................

# Exemplo Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Um Generator Function não é um Generator. Ela gera um generator.

gen = conta_ate(10)

for num in gen:
    print(num)



gen = conta_ate(5)

# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

....................


print(next(gen)) # 1

print('Geek') # apenas para dar espaço, demonstração sequência

for num in gen:
    print(num)


....................

....................

....................


"""

# Exemplo Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Um Generator Function não é um Generator. Ela gera um generator.

gen = list(conta_ate(10))

print(gen)
