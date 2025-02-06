shoppingList = []
validOptions = 'IAL'

while True:
    userOption = input("Selecione uma opção [I]nserir [A]pagar [L]istar: ").upper()
     # INSERIR
    if userOption == 'I':
        shoppingList.append(input("Valor: "))
        print(shoppingList)
        # DELETAR
    elif userOption == 'A':
        for index, name in enumerate(shoppingList):
            print(index, name)
    
        deleteIndex = input("Informe o índice que deseja apagar: ")

        try: 
            deleteIndex  = int(deleteIndex)
            if 0 <= deleteIndex < len(shoppingList):
                shoppingList.pop(deleteIndex)
                print(f"VALOR DELETADO: {name}")
            else:
                print("Índice inválido!")
        except:
            print("ENTRADA INVÁLIDA!")
        # LISTAR
    elif userOption == 'L':
        if shoppingList == []:
            print("Lista vazia")
        else:
            print(shoppingList)
    if userOption == ' ':
        print("Você deixou campos vazios")
        continue
        
    elif userOption not in validOptions:
        print("Digite apenas os caracteres válidos!")
        continue
