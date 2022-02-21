import random

# Task 1

def addRightDigit(d = random.randint(0, 10), k = 1000):
    if isinstance(d, int) and isinstance(k, int):
        return k * 10 + d
print(addRightDigit())

# Task 2

def numberPrefix(n = random.randint(1000, 100000), k = random.randint(1, 4)):
    if isinstance(n, int) and isinstance(k, int):
        return str(n)[:k]
print(numberPrefix())