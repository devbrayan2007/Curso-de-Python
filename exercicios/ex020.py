import copy
import random
from time import sleep


produtos = [
    {'nome': "Arroz", 'preço': 10.00},
    {'nome': "Feijão", 'preço': 20.00},
    {'nome': "Café", 'preço': 30.00},
    {'nome': "Leite", 'preço': 15.00},
    {'nome': "Ovo", 'preço': 25.00},
]

novos_produtos = copy.deepcopy(produtos)

def aumentar_preco():
    print("=== === === === === === === === === === === === === === === ===")
    novos_produtos[0]['preço']  = round(novos_produtos[0]['preço'] * (1 + 10 / 100), 2)
    novos_produtos[1]['preço']  = round(novos_produtos[1]['preço'] * (1 + 10 / 100), 2)
    novos_produtos[2]['preço']  = round(novos_produtos[2]['preço'] * (1 + 10 / 100), 2)
    novos_produtos[3]['preço']  = round(novos_produtos[3]['preço'] * (1 + 10 / 100), 2)
    novos_produtos[4]['preço']  = round(novos_produtos[4]['preço'] * (1 + 10 / 100), 2)

    for produto in novos_produtos:
        print(produto)

    print("=== === === === === === === === === === === === === === === ===")

    return "FIM DA EXECUÇÃO"


def ordenar_produtos_por_nome():
    produtos.sort(key =lambda item : item['nome'], reverse=True)

    print("=-=-=-=-=-=-=-=-=- PRODUTOS ORDENADOS POR NOME -=-=-=-=-=-=-=-=")
    for produto in produtos:
        print(f'{produto['nome']}')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    return "FIM DA EXECUÇÃO"


def ordenar_produtos_por_preco():
    novos_produtos.sort(key=lambda item : item['preço'], reverse=True)
    
    print("=-=-=-=-=-=-=-=-=- PRODUTOS ORDENADOS POR PREÇO -=-=-=-=-=-=-=-=")
    for produto in novos_produtos:
        print(f'R${produto['preço']}')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    return "FIM DA EXECUÇÃO"


print(aumentar_preco())
print(ordenar_produtos_por_nome())
print(ordenar_produtos_por_preco())


# AŔEA DE ADMINISTRADOR DO SISTEMA
admin = input("Você é administrador? ")
codigo_produto = random.randint(0, 99999)
if admin == 'S':
    print("ÁREA DO ADMINISTRADOR DO SISTEMA")
    while True:
        nome_usuario_admin = input("Digite o nome de usuário: ")
        senha_usuario_admin = input("Digite sua senha: ")
        if nome_usuario_admin == "Brayan" and senha_usuario_admin =="23012007":
            print(f"BEM-VINDO DE VOLTA {nome_usuario_admin}!")
            break
        else:
            print("NOME OU SENHA INCORRETOS")
            nome_usuario_admin = input("Digite o nome de usuário: ")
            senha_usuario_admin = input("Digite sua senha: ")
    # MENU DE OPÇÕES DO ADMIN
    print("Oque deseja fazer?")
    print("1 - ADICIONAR PRODUTO")
    print("2 - EXCLUIR PRODUTO")
    print("3 - ALTERAR PREÇO")
    print("4 - VISUALIZAR PRODUTO")
    print("5 - SAIR DO PROGRAMA")
    while True:
        try:
            opcao_usuario = int(input("Informe sua opção: "))
        except ValueError as error:
            print("ERROR: ",error)
        try:      
            # OPÇÃO 1
            if opcao_usuario == 1:
                nome_produto = input("Digite o nome do produto: ")
                preco_produto = float(input("Preço do produto: R$"))
                produtos.append({'nome': nome_produto, 'preço': preco_produto})
                print(f'PRODUTO {nome_produto} ADICIONADO COM SUCESSO!')
                print(f'CÓDIGO DO COMPROVANTE {codigo_produto}')
                print(produtos)
            elif opcao_usuario == 2:
                print("CARREGANDO PRODUTOS CADASTRADOS...")
                sleep(0.5)
                for produto in produtos:
                    print(produto)
                def deletar_produto(nome_prod):
                    global produtos
                    produtos = [p for p in produtos if p['nome'].lower() != nome_prod.lower()]
                    print("Lista atualizada de produtos:")
                    for p in produtos:
                        print(f" - {p['nome']} | {p['preço']}")
                print("Lista de produtos disponíveis:")
                for p in produtos:
                    print(f"- {p['nome']} | R$ {p['preço']}")
                    
                remover_produto = input("Digite o nome do produto que deseja deletar: ")
                deletar_produto(remover_produto)
                    
                    
        except ValueError:
            print("Preço inválido. Tente novamente!")
            
elif admin == 'N':
    print("FIM DO PROGRAMA!")
else:
    print("Você está digitando um caracter inválido! - APENAS S OU N")
