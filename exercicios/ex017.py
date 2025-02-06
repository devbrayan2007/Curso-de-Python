def createMultiplier(multiply):
    def multiplication(number):
        return number * multiply
    return multiplication


fold = createMultiplier(2)
triple = createMultiplier(3)
quadruple = createMultiplier(4)

print(fold(2))
print(triple(3))
print(quadruple(4))
