number = input("Digite um número: ")


try:
    numberInt = int(input(number))
    evenOrOdd = numberInt % 2 == 0
    evenOrOddText = "ÍMPAR"
    
    if evenOrOdd:
        evenOrOddText = "PAR"
        
        print(f"O número {number} é {evenOrOddText}")
except:
    print("Você não digitou um número inteiro")
