from random import randint

answer = randint(1, 1000)
reply = int(input('enter number '))

while answer != reply:
    if answer > reply:
        print('enter more number ')
    elif answer < reply:
        print('enter less number ')
    else:

        break


    reply = int(input('enter number ' ))

input('you win ')


