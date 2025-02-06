# Generator expression, iterables e iterators


iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()
generator = (n for n in range(1000))

print(generator)
print(next(generator))

