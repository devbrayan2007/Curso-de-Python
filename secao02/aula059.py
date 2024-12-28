# DICIONÁRIOS - PARTE 1

pessoa = {
    'nome': "Brayan",
    'sobrenome': "Campos",
    'idade': 18,
    'altura': 1.80,
    'endereço': [
        {'rua': 'Rua Violeta', 'numero': 4}
    ]
}

print(pessoa)
print(pessoa['nome'])

for chave in pessoa:
    print(chave, pessoa[chave])
