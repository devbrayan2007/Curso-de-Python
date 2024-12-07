cpf = '21193571707'

nineDigits = cpf[:9]
cont_1 = 10
result = 0

for digit in nineDigits:
    result += int(digit) * cont_1
    cont_1 -= 1
digit = ((result*10) % 11)
digit = digit if digit <= 9 else 0
print(f"PRIMEIRO DÍGITO GERADO DO CPF: {digit}")
