def multiplier(*args):
    total = 1
    for number in args:
        print(f'Total: {total} x {number}')
        total *= number
        print(f'Total: {total}')
    print(f"Total da multiplicação: {total}")


multiplier(1, 2, 3, 4, 5)
