# TIPOS PRIMITIVOS E SAÍDA DE DADOS

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
soma = n1 + n2
print(f'A soma entre {n1} e {n2} vale {soma}')

msg = str(input("Digite um valor: "))
print(type(msg))

verdade = bool(input("Informe um valor: "))
print(type(verdade))

n = input("Digite algo: ")
print(n.isnumeric()) # verifica se é numérico
print(n.isalpha()) # verifica se é alfabético
print(n.isalnum()) # verifica se é alfanumérico

