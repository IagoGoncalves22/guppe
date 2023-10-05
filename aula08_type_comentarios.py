import math

def circunferencia(raio):
    # type: (float) -> float # é importante entender, não é recomendado
    return 2 * math.pi * raio

# print(circunferencia(8))

# print(circunferencia('geek')) # Errado

def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

# cabecalho(texto=43, alinhamento='geek') # mypy vai dar erro

def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool

): # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

cabecalho2(texto='42', alinhamento=False)

nome = 'Geek University' # type: str

