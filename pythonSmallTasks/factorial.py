import random

def fact(n):
    """factorial calculation"""
    r = 1
    while n > 0:
        r = r * n
        n = n - 1
    return r

def exponentiation(x, y):
    r = 1
    while y > 0:
        r = r * x
        y = y - 1
    return r

def maximum(*numbers):
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
        return maxnum

label = '''
    1. factorial
    2. exponentiation
    3. maximum
    
'''

comand = input('what do you want to calculate: \n'
               ' 1. factorial \n '
               '2. exponentiation \n '
               '3. maximum \n '
               'enter comand ' )

while comand != '0':
    if comand == '1':
        n = int(input('enter volue '))
        print(fact(n))

    elif comand == '2':
        x = int(input('enter first volue '))
        y = int(input('enter second volue '))
        print(exponentiation(x, y))

    elif comand == '3':
        numbers = []
        n = int(input('enter number of elements '))
        for i in 5:
            numbers = [numbers.append(random.randint(1, 1000))]
        print(numbers)

        """
        numbers = []
        n = int(input('enter the number of elements'))
        choice = input('do you prefea do you prefer to fill in manually? Yes/No ')
        if choice == 'Y':
            while n > 0:
                a = (int(input('enter ')))
                numbers = numbers.append(a)
                n = n - 1
        else:
            while n > 0:
                numbers = numbers.append(random.randint(1, 1000))

    print(maximum(numbers))
"""



