"""
1

x = [1.0, 2.0, 3.0]

for n in x:
    a = (1 / n)
    print(a)

2

somelist = [(1, 2), (3, 7), (9, 5)]
result = 0

for x, y in somelist:
    result = result + (x * y)
    print(result)

3

x = [1, 2, 3, 4]
x_squared = []
for item in x:
    x_squared.append(item * item)
print(x_squared)

4
x_squared = (item for item in range(1, 100) if item % 2 > 0)
for squared in x_squared:
    print(squared)

    """
x_squared_dict = {item: item ** 3 for item in range(11, 16)}
print(x_squared_dict)