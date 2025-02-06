nome = input("\033[1;33mInforme seu nome: ")
idade = input("Informe sua idade: ")

if not nome or not idade:
    print('\033[1;31mDesculpe, você deixou campos vazios. :(')
else:
    print(f'\033[1;32mBEM-VINDO(A) A VERIFICAÇÃO DE NOMES {nome}!')
    print('\033[1;35m=-' * 15)
    print(f"\033[1;36mSeu nome é {nome}")
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
    print('\033[1;35m=-' * 15)
    print("\033[1;32mVOLTE SEMPRE!!! ;)")

