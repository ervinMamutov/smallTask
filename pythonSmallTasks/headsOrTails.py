import random

numberOfStreaks = 0
data = []
for experimentNumber in range(10000):
    a = random.randint(0, 1)
    data.append(a)
#print(data)

print(len(data))

i = 0
k = 0
s = 0

while i < len(data):

    if data[i] < 1:

        k += 1
        if k % 6 == 0:
            numberOfStreaks += 1
        else:
            s = 0

    if data[i] > 0:

        s += 1
        if s % 6 == 0:
            numberOfStreaks += 1
        else:
            k = 0
    i += 1


print('Вероятность появления серии: %s%%' % (numberOfStreaks / 100))