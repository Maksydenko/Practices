import random

# Task 1

def addRightDigit(d = random.randint(0, 10), k = 1000):
    return k * 10 + d
print(addRightDigit())

# Task 2

def numberPrefix(n = random.randint(1000, 100000), k = random.randint(1, 4)):
    return str(n)[:k]
print(numberPrefix())