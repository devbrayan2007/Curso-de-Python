hours = input("Que horas são? ")

try:
    hoursInt = int(hours)
    
    if hoursInt >= 0 and hoursInt <= 11:
        print("Bom dia!")
    elif hoursInt >= 12 and hoursInt <= 17:
        print("Boa tarde!")
    elif hoursInt >= 18 and hoursInt <= 23:
        print("Boa noite!")
    else:
        print("HORÁRIO INEXISTENTE!")
except: 
    print("Por favor, digite apenas números inteiros")
