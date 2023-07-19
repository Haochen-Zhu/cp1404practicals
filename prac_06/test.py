x: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(x)
print(x[::2])
print(x[::3])
print(x[10:40:6])

letters = list("things need to be done!")
print(letters)

import random

LENGTH_OF_INT = 10
MINIMUM = 0
MAXIMUM = 10

list1 = []
for i in range(LENGTH_OF_INT):
    number = random.randint(MINIMUM, MAXIMUM)
    list1.append(number)
numbers = random.sample(list1, 6)
print(list1)
print(numbers)
