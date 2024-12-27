# *ARGS PARA QUANTIDADE DE ARGUMENTOS NÃO NOMEADOS (PARTE 2)

def soma(*args):
    total = 0
    for numero in args:
        print('Total', total, numero)
        total = total + numero
    print(total)


numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
soma_tot = soma(*numeros)
print(soma_tot)

print(sum(numeros))
