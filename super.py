""""
POO - O método super()

O método super() se refere a supere classe.

"""

class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'Este {self.__nome} fala {som}')

class Gato(Animal):

    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie) # Não recomendado
        super().__init__(nome, especie) # Recomendado
        super().faz_som('Miaaaauuuuuuuuuu')
        self.__raca = raca

felix = Gato('Felix', 'Felino', 'Angorá')

felix.faz_som('Miau')
