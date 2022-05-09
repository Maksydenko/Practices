import numpy as np
from random import randint


# Task 1

def my_fac(fac):
    if fac < 0:
        return "You wrote the number less than zero"
    if fac == 0:
        return 1
    else:
        return fac * my_fac(fac - 1)
fac = int(input("Write the number: "))
print(my_fac(fac))


# Task 2

def digital_root(num):
    if 0 < num < 10:
        return num
    summ = 0
    if num >= 10:
        for i in str(num):
            summ += int(i)
        return digital_root(summ)
    else:
        return "You wrote the number less than zero"
num = int(input("White the number: "))
print(digital_root(num))


# Task 3

def max_index(array, rand):
    max, x, y = array[0, 0], 0, 0
    for i in range(rand):
        for j in range(rand):
            if array[i, j] > max:
                max, x, y = array[i, j], i, j
    return x, y
rand = randint(1, 5)
array = np.random.randint(-50, 50, (rand, rand))
print(array, "\nIndex maximum number:", max_index(array, rand))