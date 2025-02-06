# INTRODUÇÃO ÀS FUNÇÕES

def function():
    print("Hello, World!")


function()


def imprimir(a, b, c):
    print(a, b, c)


imprimir(1, 2, 3)


def nomeUser(nome='Sem nome'):
    print(f'Olá, {nome}!')


nomeUser("Brayan")
nomeUser()


def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end='')
    print(resultado)


multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
