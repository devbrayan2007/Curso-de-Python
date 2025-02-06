# Try, Except, else e finally + Built-in Exceptions

try:
    print("ABRIR ARQUIVO")
    8 / 0
except ZeroDivisionError as error:
    print(error)
finally:
    print("FECHAR ARQUIVO")
