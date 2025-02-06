# DICIONÁRIOS - PARTE 5


p1 = {
    'nome': "Brayan",
    'sobrenome': "Campos"
}

nome = p1.pop('nome')
print(nome)
print(p1)

ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

p1.update({
    'nome': "Pedro",
    'idade': 19
})
print(p1)
