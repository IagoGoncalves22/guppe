"""
Documentando funções com Docstrings

OBS: Podemos ter acesso à documentação de uma função em Python utilizando a
propriedade especial __doc__

Podemos ainda faer acesso à documentação com a função help()

"""

# Exemplos

def diz_oi():
    """Uma função simples que retorna a string Oi!"""
    return 'Oi!'

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' à 'potencia' informada
    :param numero: que desejamos gerar o exponencial
    :param potencial: Potênciqa que queremos gerar o exponencial. Por parão é 2
    :return: Retorna o exponeicial de  'numero' por 'porencia'
    """
    return numero ** potencia

