"""
Decoradores (Decorators)

O que são decorators ?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntatc Sugar / Açucar Sintático)

/---------------------------------------\
             Function Decorator
/---------------------------------------\

-----------------------------------------
/ /---------------------------------------\
/ /           Função decorada             \\
/ /---------------------------------------\\
/-----------------------------------------\


.................................
# Sintax não recomendada (não funcionou inclusive)
# Decorators como funções (Sintaxe não recomendada / Sem açucar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
        return sendo
def saudacao():
    print('Seja bemvindo(a) à Geek University')

# Testando 1

# saudacao()

teste = seja_educado(saudacao)

# teste()

# Teste 2

def raiva():
    print('EU TE ODEIO!')

raiva_educada = seja_educado(raiva)

raiva_educada()

.........................
# OBS: Não é código funcional (não funciona), apenas ilustração

def checa_login():
    if not request.usuario:
        redirect('http://www.suarempresa.com.br/login')

def home(request):
    return 'Pode acessar home'

@checa_login
def servicos(request):
    return 'Pode acessar serviços'

def produtos(request):
    return 'Pode acessar protudos'

@chega_login
def admin (request):
    return 'Pode acessar admin'
.........................


# Decorators com Syntax Sugar (Açucar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

# Testando

apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir...')

dormir()


.........................

.........................

"""

# OBS: Não confunda Decorator com Decorator Function

