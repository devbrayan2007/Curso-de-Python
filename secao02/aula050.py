# VALORES PADRÃO PARA PARÂMETROS EM FUNÇÕES NONETYPE E NONE

def soma(x, y, z=None):
    print(x + y)
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
