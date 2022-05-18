allGuests = {'Alisa' : {'aplle' : 5, 'sweet': 20},
             'John': {'sandwich': 4, 'aplle': 3},
             'Luise': {'cup': 4, 'cake': 3}}
def totalBrought(guests, item) :
    numBrought = 0
    for k, v in guests.items() :
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of brougt items:  ')
print(' - Aplle   ' + str(totalBrought(allGuests, 'aplle')))
print(' - Cup    ' + str(totalBrought(allGuests, 'cup')))
print(' - Sweet ' + str(totalBrought(allGuests, 'sweet')))
print(' - Sandwich  ' + str(totalBrought(allGuests, 'sandwich')))
print(' - Cake    ' + str(totalBrought(allGuests, 'cake')))
print(' - Burger    ' + str(totalBrought(allGuests, 'burger')))
