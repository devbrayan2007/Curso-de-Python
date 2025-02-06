# raise - lançando exceções (erros)

def erroDividePorZero(d):
    if d == 0:
        raise ZeroDivisionError("Você está tentando dividir por zero")
    return True


def verificadorIntOuFloat(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float'
            f'"{tipo_n.__name__}" enviado'
        )
    return True


def divide(n, d):
    verificadorIntOuFloat(n)
    verificadorIntOuFloat(d)
    erroDividePorZero(d)
    return n / d


print(divide(8, 0))
