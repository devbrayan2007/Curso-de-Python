# ESTRUTURAS DE REPETIÇÃO - USANDO FUNÇÕES DO WHILE NO FOR (PARTE 9)

for i in range(10):
    if i == 2:
        print("Pulando o 2...")
        continue
    if i == 8:
        print("Seu else não executará!")
        break
        
    for j in range(1, 3):
        print(i, j)
else:
    print("For completo com sucesso!")
        