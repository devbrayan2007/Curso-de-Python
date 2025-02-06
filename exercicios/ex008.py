name = "Brayan"
sizeName = len(name)

index = 0
newName = ''
while index < sizeName:
    letter = name[index]
    newName += f'*{letter}'
    index += 1
    
newName += '*'
print(newName)
    
