# Introdução ás Generators Functions

def generator(n=0):
    yield 1  # Pausar
    print("Continuando...")
    yield 2  # Pausar
    print("Continuando...")
    yield 3  # Pausar
    print("Vou terminar")
    return "ACABOU"


gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))

gen = generator(n=0)

for n in gen:
    print(n)


def generator(n=0, max=10):
    while True:
        yield n
        n += 1
    
        if n >= max:
            return


gen = generator(max=10)
for n in gen:
    print(n)
