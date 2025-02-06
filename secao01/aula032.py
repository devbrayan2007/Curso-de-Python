# ESTRUTURAS DE REPETIÇÃO - USO DO RANGE NO FOR (PARTE 8)

numeros = range(10)

for numero in numeros:
    print(numero)
    
# FUNCIONALIDADE DO FOR:
texto = iter("Brayan").__iter__()
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

print("=" * 20)


texto2 = "Brayan" # iterável
iterador = iter(texto2) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break