import random, sys

print('Stone, Scissors, Paper')

wins = 0
losses = 0
ties = 0

while True: # main game loop
    print('%s win, %s losses, %s ties' % (wins, losses,ties))
    while True: # move selection cycle
        print('Move selection: (s)tone, s(c)issors, (p)aper or ' + \
              '(e)xit')
        playerMove = input()
        if playerMove == 'e':
            sys.exit() #exit from the program
        if playerMove == 's' or playerMove == 'c' \
            or playerMove == 'p':
            break   # exit from the move selection
        print('Enter "s", "c", "p" or "e".')

    # Display user chose
    if playerMove == 's':
        print('Stone and ...')
    elif playerMove == 'c':
        print('Scissors and ...')
    elif playerMove == 'p':
        print('Paper and ...')

    # Display computer chose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 's'
        print('Stone')
    elif randomNumber == 2:
        computerMove = 'c'
        print('Scissors')
    elif randomNumber == 3:
        computerMove = 'p'
        print('Paper')

    # Display and accounting result
    if playerMove == computerMove:
        print('TIES!')
        ties = ties + 1
    elif playerMove == 's' and computerMove == 'c':
        print('!!!! YOU WIN !!!!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 's':
        print('!!!! YOU WIN !!!!')
        wins = wins + 1
    elif playerMove == 'c' and computerMove == 'p':
        print('!!!! YOU WIN !!!!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('you losses')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'c':
        print('you losses')
        losses = losses + 1
    elif playerMove == 'c' and computerMove == 's':
        print('you losses')
        losses = losses + 1