a = int(input('enter a '))
b = int(input('enter b '))

assert a == 0, 'error'
try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print('dont divisin by zero')




