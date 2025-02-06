# Tratamento de Exceções


try:
    a = 10
    # b = 0
    print("Linha 1"[1000])
    c = a / b
except ZeroDivisionError as error:
    print(error)
except NameError as error:
    print(error)
except (TypeError, IndexError) as error:
    print("TypeError + IndexError")
    print('MSG:', error)
    print("Nome:", error.__class__.__name__)
except Exception:
    print("ERRO DESCONHECIDO!")


print("CONTINUAR")
