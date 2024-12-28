# DICIONÁRIOS - PARTE 2

pessoa = {}

pessoa['nome'] = "Brayan"

print(pessoa)

# Criando chaves dinâmicas

chave = 'nome'
pessoa[chave] = "Brayan"

print(pessoa[chave])

# Deletando chaves

pessoa['sobrenome'] = "Campos"

del pessoa['sobrenome']
print(pessoa)

# Verificando se a chave existe

if pessoa.get('sobrenome') is None:
    print("Não existe!")
else:
    print(pessoa['sobrenome'])

