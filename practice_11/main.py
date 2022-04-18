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

def sortArray(array):
    new_array = array.ravel()
    old_array = []
    for i in new_array:
        old_array.append(i)
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(len(new_array) - i - 1):
            if new_array[j] > new_array[j + 1]:
                new_array[j], new_array[j + 1] = new_array[j + 1], new_array[j]
                flag = True
    x = 0
    for i in range(len(old_array)):
        if old_array[i] == new_array[-1]:
            x = i
            break
    return x
rand = random.randint(1, 5)
array = np.random.randint(-50, 50, (rand, rand))
print("Index maximum number:", sortArray(array))
