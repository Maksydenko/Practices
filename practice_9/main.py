import numpy as np
import random

i = 0
j = 0
five = 0
matrix = np.random.randint(0, 15, (10, 20))

for i in range(10):
    for j in range(20):
        if matrix[i][j] == 5:
            five += 1
    if five >= 3:
        print(i)
    five = 0
print(matrix)