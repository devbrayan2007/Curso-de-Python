# DESEMPACOTAMENTO EM CHAMADAS DE FUNÇÕES

string = 'ABCD'
lista = ["Brayan", "Pedro", 1, 2, 3, "João"]
tupla = ("Python", "é", "legal")

p,b, *_, u = lista
print(p, u)

print(*lista)