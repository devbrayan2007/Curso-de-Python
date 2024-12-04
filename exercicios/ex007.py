name = input("Informe seu nome: ")
sizeName = len(name)

if not name:
    print("Você digitou campos vazios.")
else:
    if sizeName > 1:
        if sizeName <= 4:
            print(f"Seu nome contém {len(name)} letras. NOME CURTO")
        elif sizeName >= 5 and sizeName <= 6:
            print(f'Seu nome contém {len(name)} letras. NOME NORMAL')
        elif sizeName > 6:
            print(f'Seu nome contém {len(name)} letras. NOME GRANDE')
    else:
        print("Digite mais de uma letra.")
