# INTRODUÇÃO A FORMATAÇÃO DE STRINGS(F-STRINGS)

nome = "Brayan"
altura = 1.80
peso = 69.5

print(f'{nome} tem {altura:.2f}m de altura e pesa {peso}kg.')


# MÉTODO FORMAT

a = 'A'
b = 'B'
c = 1.1

formato = 'a = {nome1}, b = {nome2}, c = {nome3:.2f}'.format(
    nome1=a, # chamada por parâmetros nomeados
    nome2=b,
    nome3=c
    )
print(formato)