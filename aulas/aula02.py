# OPERADORES ARITMÉTICOS
'''
nome = str(input("Qual é o seu nome? "))
print(f'É um prazer de te conhecer {nome:20}!')
print(f'É um prazer de te conhecer {nome:>20}!')
print(f'É um prazer de te conhecer {nome:<20}!')
print(f'É um prazer de te conhecer {nome:^20}!')
print(f'É um prazer de te conhecer {nome:=^20}!')
'''

n1 = int(input("Informe um valor: "))
n2 = int(input("Informe outro valor: "))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
divisao_inteira = n1 // n2
resto = n1 % n2

print(f'A soma vale {soma}')
print(f'A subtração vale {subtracao}')
print(f'A multiplicação vale {multiplicacao}')
print(f'A divisão vale {divisao:.2f}')
print(f'A potência vale {potencia}')
print(f'A divisão inteira vale {divisao_inteira}')
print(f'O resto da divisão vale {resto}')

