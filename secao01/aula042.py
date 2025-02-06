# TUPLAS - ENUMERATE (PARTE 2)

lista = ['Brayan', 'João', 'Pedro']

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)

print("=-" * 15)

for item in enumerate(lista):
    print(item)
    
print("=-" * 15)

lista_enumerada = list(enumerate(lista))
print(lista_enumerada)

print("=-" * 15)

for indice, nome in enumerate(lista):
    print(indice, nome)
    
print("=-" * 15)

for tupla_enumerada in enumerate(lista):
    print("FOR DA TUPLA: ")
    for valor in tupla_enumerada:
        print(f'\t{valor}')