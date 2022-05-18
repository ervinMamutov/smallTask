from random import randint

def guess(youNumber):

answer = randint(1, 1000)

while answer != youNumber:
    if answer > reply:
        print('enter more number ')
    elif answer < reply:
        print('enter less number ')
    else:

        break


    reply = int(input('enter number ' ))

input('you win ')


youNumber = int(input('enter number '))