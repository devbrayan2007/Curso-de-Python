# INTRODUÇÃO A FUNÇÃO LAMBDA + LIST.SORT E SORTED


lista = [
    {'nome': "Brayan", 'sobrenome': "Campos"},
    {'nome': "Pedro", 'sobrenome': "Henrique"},
    {'nome': "João", 'sobrenome': "Pedro"},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item : item['nome'])
l2 = sorted(lista, key=lambda item : item['sobrenome'])

exibir(l1)
exibir(l2)
