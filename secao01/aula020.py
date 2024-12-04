# INTRODUÇÃO AO TRY E EXCEPT (EXCEPTIONS)

numero = input("Vou dobrar o número que você digitou: ")

try:
    numero_float = float(numero)
    print(f'O dobro de {numero} é {numero_float * 2:.2f}')
except:
    print(f'{numero} não é um número.')
