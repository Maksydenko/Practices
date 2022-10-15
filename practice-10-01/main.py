import numpy as np
from random import randint


# Task 1

def sort_array(array):
    i = 0
    flag = True

    while flag:
        flag = False

        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        i += 1
    return array
number = int(input("Write the number of array elements: "))
array = np.random.randint(-10, 10, number)
print(sort_array(array), "\nMaximum is", sort_array(array)[-1], "in",
      len(array) - 1, "\nMinimum is", sort_array(array)[0])


# Task 2

def sort_half(array):
    full_len = len(array)
    half_len = len(array) // 2

    for i in range(half_len - 1):
        min = i

        for j in range(i + 1, half_len):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    for i in range(half_len, full_len - 1):
        min = i

        for j in range(i + 1, full_len):
            if array[j] > array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array
array = np.random.randint(-10, 10, 10)
print(sort_half(array))


# Task 3

def sort_zeros(array):
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    zeros = 0

    for i in range(len(array)):
        if array[i] == 0:
            zeros += 1

            while array[i - 1] != 0 and i != 0:
                print(array)
                array[i], array[i - 1] = array[i - 1], array[i]
                i -= 1
    return array[zeros:]
array = np.random.randint(-2, 5, 20)
print(sort_zeros(array))