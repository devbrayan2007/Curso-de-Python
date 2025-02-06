# Tratamento de Exceções  -Parte 1

try:
    a = 10
    b = 0
    print("Linha 1"[1000])
    c = a / b
except ZeroDivisionError:
    print("ERRO! NÚMERO DIVIDIDO POR ZERO")
except NameError:
    print("Nome 'b' não está definido")
except (TypeError, IndexError):
    print("TypeError + IndexError")
except Exception:
    print("ERRO DESCONHECIDO!")


print("CONTINUAR")
