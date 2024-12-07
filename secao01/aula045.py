# LISTAS DENTRO DE LISTAS

salas = [
    ["Brayan", "Pedro",],
    
    ["Lucas", ],
    
    ["João", "Pedro", "Henrique"]
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])

print("-="*15)

for sala in salas:
    for item in sala:
        print(item)
        