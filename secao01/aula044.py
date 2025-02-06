# MÉTODOS DA STRING - SPLIT, STRIP E JOIN

frase = " Hello,  World!"
lista_palavras = frase.split()
print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    lista_palavras[i] = lista_palavras[i].strip()

print(lista_palavras)


frases_unidas = '-'.join('abc')
print(frases_unidas)