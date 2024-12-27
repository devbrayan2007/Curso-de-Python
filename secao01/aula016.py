# OPERADORES LÓGICOS

# AND

entrada = input('[E]ntrar [S]air: ')
senha = input('Digite sua senha: ')

senha_permitida = '1234'

if entrada == 'E' and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    

print(True and True and True)
print(True and False and True)
print(True and 0 and True)

if 0 and 1:
    print(True and 1) # Retorna nada
    
    
print("=-" * 20)

# OR

entrada2 = input('[E]ntrar [S]air: ')
senha2 = input('Senha: ') or 'Sem senha'

senha_permitida2 = '123456'

if (entrada2 == 'E' or entrada2 == 'e') and senha2 == senha_permitida2:
    print('Entrar')
else:
    print('Sair')

print("=-" * 20)


# NOT

senha3 = input('Senha: ')

if not senha3:
    print('Você não digitou nada.')
    

print("=-" * 20)
    
# IN

nome = "Brayan"
print(nome[2])

print('a' in nome)

# NOT IN

print('yan' not in nome)
