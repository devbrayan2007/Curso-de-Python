def oddOrEvenNumberChecker(number):
    if number % 2 == 0:
        return print(f'O número {number} é PAR!')
    else:
        return print(f'O número {number} é ÍMPAR!')
    

oddOrEvenNumberChecker(number=int(input("Informe um número: ")))
