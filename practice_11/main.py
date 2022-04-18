import numpy as np
import random


# Task 1

def myFac(fac):
    if fac < 0:
        return "You wrote the number less than zero"
    if fac == 0:
        return 1
    else:
        return fac * myFac(fac - 1)
fac = int(input("Write the number: "))
print(myFac(fac))


# Task 2

def digitalRoot(num):
    if 0 < num < 10:
        return num
    summ = 0
    if num >= 10:
        for i in str(num):
            summ += int(i)
        return digitalRoot(summ)
    else:
        return "You wrote the number less than zero"
num = int(input("White the number: "))
print(digitalRoot(num))


# Task 3

def maxIndex(array, rand):
    max, x, y = array[0, 0], 0, 0
    for i in range(rand):
        for j in range(rand):
            if array[i, j] > max:
                max, x, y = array[i, j], i, j
    return x, y
rand = random.randint(1, 5)
array = np.random.randint(-50, 50, (rand, rand))
print(array)
print("Index maximum number:", maxIndex(array, rand))
