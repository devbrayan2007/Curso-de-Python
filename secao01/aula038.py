# LISTAS - CUIDADOS COM TIPOS MUTÁVEIS (PARTE 5)

lista_a = ["Brayan", "João"]
lista_b = lista_a.copy() # Copiando listas

lista_a[0] = "Oi"
print(lista_a)
print(lista_b)