# DICIONÁRIOS - PARTE 3


pessoa = {
    'nome': "Brayan",
    'sobrenome': "Campos"
}

print(pessoa.__len__())

print(pessoa.keys())

for chave in pessoa:
    print(chave)

print(pessoa.values())

for valor in pessoa.values():
    print(valor)

print(pessoa.items())

for chave, valor in pessoa.items():
    print(chave, valor)


pessoa.setdefault('idade', 'Chave inexistente')
print(pessoa['idade'])
