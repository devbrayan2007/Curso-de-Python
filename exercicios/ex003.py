num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

if num1 > num2:
    print(f'O maior número é {num1}')
elif num2 > num1:
    print(f'O maior número é {num2}')
else:
    print("Os números são iguais")
