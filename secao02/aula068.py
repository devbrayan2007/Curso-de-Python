# EXEMPLO DE USO DO SET

letras = set()

while True:
    letra = input("Digite: ")
    letras.add(letra.lower())

    if 's' in letras:
        print("PARABÉNS!")
        break
    print(letras)
