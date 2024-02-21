# Generate Random Number
from numpy import random

# int
x = random.randint(100)
print(x)

# float
x = random.rand()
print(x)

#array
# x=random.randint(100, size=(5))
# print(x)

# x = random.randint(100, size=(3, 5))
# print(x)

# x = random.rand(3, 5)
# print(x)

x = random.choice([3, 5, 7, 9])
print(x)