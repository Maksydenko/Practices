import numpy as np
import random

i = 0
j = 0
five = 0
matrix = np.random.randint(0, 15, (10, 20))

while i < len(matrix):
    while j < len(matrix[i]):
        if matrix[i][j] == 5:
            five += 1
        j += 1
    if five >= 3:
        print(i)
    i += 1
    j = 0
    five = 0
print(matrix)