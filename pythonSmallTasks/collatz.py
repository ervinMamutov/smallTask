import sys


def collatz(number):
    if number % 2 == 0:
        return number // 2
    if number % 2 == 1:
        return 3 * number + 1


a = input('Enter value ')

try:
    a = int(a)
    while True:
        b = collatz(a)
        if a > 1:
            print('value', a)
            a = b
        else:
            print('Finish')
            break




except ValueError:
    print('repeat enter value')


#print(a)

