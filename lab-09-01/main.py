import numpy as np
from random import randint
from time import perf_counter


# Bubble sort ascending

def bubble_ascending(array=np.random.randint(-1000, 1000, 10000)):
    # The ability to select input data
    # from the keyboard up to 30 output numbers
    answer = input('Do you want to write your numbers? \
Answer ("Yes" or "No"): ').upper()
    if answer == "YES":
        custom_array = []
        quantity = int(input("How many do you want to write your numbers? \
Answer (maximum 30): "))
        for i in range(quantity):
            number = int(input("Write your number: "))
            custom_array.append(number)
            array = np.append(array, number)

    # Bubble sort in ascending order
    start_time = perf_counter()
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        i += 1
    all_time = perf_counter() - start_time
    if answer == "YES":
        return "Your array: ", custom_array, "Sorted array: ", array, "Sorting time", all_time
    return "Sorted array: ", array, "Sorting time", all_time

print(bubble_ascending())


# Bubble sort descending

def bubble_descending(array=np.random.randint(-1000, 1000, 10000)):
    # The ability to select input data
    # from the keyboard up to 30 output numbers
    answer = input('Do you want to write your numbers? \
Answer ("Yes" or "No"): ').upper()
    if answer == "YES":
        custom_array = []
        quantity = int(input("How many do you want to write your numbers? \
Answer (maximum 30): "))
        for i in range(quantity):
            number = int(input("Write your number: "))
            custom_array.append(number)
            array = np.append(array, number)

    # Bubble sort in descending order
    start_time = perf_counter()
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        i += 1
    all_time = perf_counter() - start_time
    if answer == "YES":
        return "Your array: ", custom_array, "Sorted array: ", array, "Sorting time", all_time
    return "Sorted array: ", array, "Sorting time", all_time

print(bubble_descending())


# Selection sort ascending

def selection_ascending(array=np.random.randint(-1000, 1000, 10000)):
    # The ability to select input data
    # from the keyboard up to 30 output numbers
    answer = input('Do you want to write your numbers? \
Answer ("Yes" or "No"): ').upper()
    if answer == "YES":
        custom_array = []
        quantity = int(input("How many do you want to write your numbers? \
Answer (maximum 30): "))
        for i in range(quantity):
            number = int(input("Write your number: "))
            custom_array.append(number)
            array = np.append(array, number)

    # Selection sort in ascending order
    start_time = perf_counter()
    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    all_time = perf_counter() - start_time
    if answer == "YES":
        return "Your array: ", custom_array, "Sorted array: ", array, "Sorting time", all_time
    return "Sorted array: ", array, "Sorting time", all_time

print(selection_ascending())


# Selection sort descending

def selection_descending(array=np.random.randint(-1000, 1000, 10000)):
    # The ability to select input data
    # from the keyboard up to 30 output numbers
    answer = input('Do you want to write your numbers? \
Answer ("Yes" or "No"): ').upper()
    if answer == "YES":
        custom_array = []
        quantity = int(input("How many do you want to write your numbers? \
Answer (maximum 30): "))
        for i in range(quantity):
            number = int(input("Write your number: "))
            custom_array.append(number)
            array = np.append(array, number)

    # Selection sort in descending order
    start_time = perf_counter()
    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] > array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    all_time = perf_counter() - start_time
    if answer == "YES":
        return "Your array: ", custom_array, "Sorted array: ", array, "Sorting time", all_time
    return "Sorted array: ", array, "Sorting time", all_time

print(selection_descending())


# Insertion sort ascending

def insertion_ascending(array=np.random.randint(-1000, 1000, 10000)):
    # The ability to select input data
    # from the keyboard up to 30 output numbers
    answer = input('Do you want to write your numbers? \
Answer ("Yes" or "No"): ').upper()
    if answer == "YES":
        custom_array = []
        quantity = int(input("How many do you want to write your numbers? \
Answer (maximum 30): "))
        for i in range(quantity):
            number = int(input("Write your number: "))
            custom_array.append(number)
            array = np.append(array, number)

    # Insertion sort in ascending order
    start_time = perf_counter()
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    all_time = perf_counter() - start_time
    if answer == "YES":
        return "Your array: ", custom_array, "Sorted array: ", array, "Sorting time", all_time
    return "Sorted array: ", array, "Sorting time", all_time

print(insertion_ascending())


# Insertion sort descending

def insertion_descending(array=np.random.randint(-1000, 1000, 10000)):
    # The ability to select input data
    # from the keyboard up to 30 output numbers
    answer = input('Do you want to write your numbers? \
Answer ("Yes" or "No"): ').upper()
    if answer == "YES":
        custom_array = []
        quantity = int(input("How many do you want to write your numbers? \
Answer (maximum 30): "))
        for i in range(quantity):
            number = int(input("Write your number: "))
            custom_array.append(number)
            array = np.append(array, number)

    # Insertion sort in descending order
    start_time = perf_counter()
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] < key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    all_time = perf_counter() - start_time
    if answer == "YES":
        return "Your array: ", custom_array, "Sorted array: ", array, "Sorting time", all_time
    return "Sorted array: ", array, "Sorting time", all_time

print(insertion_descending())
