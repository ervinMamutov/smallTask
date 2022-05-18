import pprint
massage = ' It was a bright cold day in Aprel, and the clocks were striking thirteen.'
count = {}

for character in massage:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

pprint.pprint(count)