# EMPACOTAMENTO E DESENPACOTAMENTO DE DICIONÁRIOS + *ARGS E **KWARGS


pessoa = {
    'nome': "Brayan",
    'sobrenome': "Campos"
}

dados_pessoa = {
    'idade': 17,
    'altura': 1.80
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)


def argumento_nomeado(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)
    
argumento_nomeado(**pessoa_completa)

