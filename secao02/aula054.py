# *ARGS PARA QUANTIDADE DE ARGUMENTOS NÃO NOMEADOS (PARTE 1)

def soma(*args):
    total = 0
    for numero in args:
        print(f'Total: {total} + {numero}')
        total += numero
        print(f'Total: {total}')
    print(total)


soma(1, 2, 3, 4, 5, 6)
