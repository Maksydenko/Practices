import numpy as np
import random

# Task 1

arr = []

for i in range(5):
    arr.append(int(input("Write a number: ")))
print(arr, np.mean(arr))

# Task 2

x = []

for i in range(5):
    x.append(int(input("Write the number: ")))
print(np.square(x), np.sqrt(x))

# Task 3

sur = []

for i in range(5):
    sur.append(input("Write the surname: "))
print(np.row_stack(sur[::-1]))

# Task 4

sur = []

for i in range(5):
    np.array(sur.append(input("Write the surname: ").title()))
letter = input("Write the letter: ").upper()

for i in sur:
    if i[0] == letter:
        print(i)

# Task 5

a = np.random.randint(-128, 128, 7)
print(a, a * 2)