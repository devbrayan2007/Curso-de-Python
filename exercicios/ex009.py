print("\033[1;34mCALCULADORA 1.0 EM PYTHON")
while True:
    n1 = input("\033[1;35mDigite um número: ")
    n2 = input("Digite outro número: ")
    operation = input("Digite o operador ( + - * /): ")
    
    validNumbers = None
    n1Float = 0
    n2Float = 0
    
    try:
        n1Float = float(n1)
        n2Float = float(n2)
        validNumbers = True
    except:
        validNumbers = None
        
    if validNumbers is None:
        print('\033[1;31mUm ou ambos os números digitados são inválidos.')
        continue
    
    permittedOperators = '+-*/'
    
    if operation not in permittedOperators:
        print("Operador inválido!")
        continue
    
    if len(operation) > 1:
        print('\033[1;31mDigite apenas um operador.')
        continue
    
    print("\033[1;32mRealizando sua conta...")
    if operation == '+':
        print(f'{n1Float} + {n2Float} = {n1Float + n2Float}')
    elif operation == '-':
        print(f'{n1Float} - {n2Float} = {n1Float - n2Float}')
    elif operation == '*':
        print(f'{n1Float} * {n2Float} = {n1Float * n2Float}')
    elif operation == '/':
        print(f'{n1Float} / {n2Float} = {n1Float / n1Float}')
    else:
        print("erro!")
    
    output = input('\033[1;37mSair do programa? [S]im [N]ão ').lower().startswith('s')
    
    if output is True:
        print("\033[1;36mVolte sempre!")
        break
 