begin = 1
end = 1000

while True:
    offer = int((begin+end)/2)
    value = input(f'enter {offer} ')
    if value == '+':
        begin = offer + 1
    elif value == '-':
        end = offer - 1
    else:
        break
