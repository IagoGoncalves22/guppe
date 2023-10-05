"""
# Correto

texto: str

# Incorreto

texto:str

texto : str

# Correto

) -> str

# Incorreto

)->str

) ->str

# Correto

alinhamento: bool = True

# Incorreto

alinhamento:bool=True


"""


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()} ".center(50, '#')


print(cabecalho('Geek University'))

print(cabecalho(' Geek University', alinhamento=False))


print(cabecalho(' Geek University ', alinhamento=True)) # vai rodar porque string é True.
# Podemos fazer a checagem com o MyPy (terminal, mypy nome_do_arquivo.py)

# OBS: utilizar junto o Type Hinting e o MyPy para checar. Dar robustez e segurança ao programa.

