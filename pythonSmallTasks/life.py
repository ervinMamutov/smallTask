import random, time, copy
WIDTH = 60
HEIGHT = 20

# Creating a list of lists for cells
nextCells = []
for x in range(WIDTH):
    column = []     # creating new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')      # adding a living cell
        else:
            column.append(' ')      # adding a death cell
    nextCells.append(column)        # variable nextCells including
                                    # list of columns

while True:         # general program's loop
    print('\n\n\n\n\n')     #separate each step with newlines
    currentCells = copy.deepcopy(nextCells)

    # displaing the current cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')       #dispalaing # or spacebar
        print()         # displaying a new symbol in the end

    # Calculation of cells in the next step
    # based on the cells of the current step
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Getting neighboring coordinates
            # Expression '% WIDTH' ensures that value
            #leftCoord is always between 0 and Width - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            beloveCoord = (y + 1) % HEIGHT

            # Calculation of the number of living neighboring cells
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1   # living neighboring cells in the left top
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1       # living neighboring cells top
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1       # living neighboring cells right top
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1       # living neighboring cells left
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1       # living neighboring cells right
            if currentCells[leftCoord][beloveCoord] == '#':
                numNeighbors += 1       # living neighboring cells left up
            if currentCells[rightCoord][beloveCoord] == '#':
                numNeighbors += 1       # living neighborning cells right up

            # Changing cells based on the rules of the game "Life"
            if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with two or three live
                # neighbors stay alive
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with three living neighbors come to life
                nextCells[x][y] = '#'
            else:
                # All other cells die or remain dead
                nextCells[x][y] = ' '
    time.sleep(1)  # add a second pause, to reduce flicker



