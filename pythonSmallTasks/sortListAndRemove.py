import random

data = []

for item in range(100):
    a = random.randint(0, 100)
    data.append(a)

#enterValue = int(input('enter value '))
enterValue = random.randint(0, 100)
print('item', enterValue)

print('lise befor remove', data)

print('number of elements in the list ', data.count(enterValue))
if data.count(enterValue) > 1:
    #if enterValue in data:
    data.remove(enterValue)
else:
    print('don\'t remove item')

print('list after remove', data)

