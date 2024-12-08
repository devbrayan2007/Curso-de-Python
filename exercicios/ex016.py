def oddOrEvenChecker(number):
    if number % 2 == 0:
        return print(f"O número {number} é PAR!")
    return print(f"O número {number} é ÍMPAR!")


oddOrEvenChecker(number=int(input("Digite um número: ")))
