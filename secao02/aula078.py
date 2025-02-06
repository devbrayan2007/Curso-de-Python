# Dir, hasattr e getattr

string = "Brayan"
metodo = 'upper'

if hasattr(string, 'upper'):
    print("Existe upper")
    print(getattr(string, metodo)())
else:
    print("Não existe o método", metodo)
