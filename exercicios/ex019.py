def firstDuplicate(listNumbers):
    numbersSeen = set()

    for number in listNumbers:
        if number in numbersSeen:
            return f'Duplicate number: {number}'
        numbersSeen.add(number)
    return "Value not found!"


listOfListOfIntegers = [
    [1, 2, 3, 3, 4, 5, 6, 8, 9, 9, 10],
    [30, 21, 34, 12, 0, 17, 99, 20, 10],
    [60, 56, 100, 100, 12, 5, 0, 5, 2],
    [9, 2, 1, 3, 8, 6, 4, 0, 13, 22, 5],
    [0, 1, 2, 3, 3, 4, 6, 7, 8, 6, 10]
]

print(firstDuplicate(listOfListOfIntegers[0]))
print(firstDuplicate(listOfListOfIntegers[1]))
print(firstDuplicate(listOfListOfIntegers[2]))
print(firstDuplicate(listOfListOfIntegers[3]))
print(firstDuplicate(listOfListOfIntegers[4]))
