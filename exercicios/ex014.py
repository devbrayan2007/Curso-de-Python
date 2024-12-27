import random 
for _ in range(100):
    cpf = '211.935.717-07'.replace('.', '').replace('-', '')
    firstDigit = ''
    for i in range(10):
        firstDigit += str(random.randint(0,9))
    print(firstDigit)
    cont_1 = 10
    result = 0

    for digit in firstDigit:
        result += int(digit) * cont_1
        cont_1 -= 1
    digit = (result*10) % 11
    digit = digit if digit <= 9 else 0
    print(f"PRIMEIRO DÍGITO GERADO DO CPF: {digit}")

    secondDigit = ''
    cont_2 = 11
    result_2 = 0
    for digit_2 in secondDigit:
        result_2 += int(digit_2) * cont_2
        cont_2 -= 1
    digit_2 = (result_2 * 10) % 11
    digit_2 = digit_2 if digit_2 <= 9 else 0
    print(f"SEGUNDO DÍGITO GERADO DO CPF: {digit_2}")

    newCpf = f'{firstDigit}{digit}{digit_2}'

    if cpf == newCpf:
        print("CPF VÁLIDO!")
    else:
        print("CPF INVÁLIDO!")
