""""
Por que testar nosso código?

Testes Automatizados!

         Aplicação web
....................................
/         frontend e backend       /
------------------------------------
/        Testes automatizados      /
------------------------------------

Por que testar nosso código?
    - Reduzir bugs (problemas) no código existente;
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recurso antigo;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos;
    - Testes garantem que a refatoração que costumamos a fazer não tragam novos bugs (problemas);

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então você escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso);
    - Então refatora o código para realizar a funcionalidade e tesva novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento de TDD são quse como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;



"""

class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')

felix = Gato('Felix')

felix.miar()

print(felix.nome)
