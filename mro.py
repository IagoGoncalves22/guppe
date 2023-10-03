"""
POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem e Método), é a ordem de execução dos métodos
(quem será executado primeiro).

Em Python, a gente pode conferir a ordem de execução dos métodos de três formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help

"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando. '

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar! '

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando. '

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'

class Pinguim(Terrestre, Aquatico):
    # class Pinguim(Aquatico, Terrestre) / Altera a ordem/prioridade da herança

    def __init__(self, nome):
        super().__init__(nome)

# Testando

tux = Pinguim('Tux')
print(tux.cumprimentar()) # Eu sou o Tux da terra! / Eu sou o Tux do Mar Method Resolution Order - MRO

# Pinguim(Terrestre, Aquatico) está sendo herdado
# Eu sou o Tux da terra!

# class Pinguim(Aquatico, Terrestre) se alterar a ordem, altera o critério da herança
# Eu sou o Tux do Mar!