import timeit
import numpy as np
from random import randint

# Setup code for performance evaluation indicators
setup_code = """
import numpy as np
from random import randint
"""


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
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        i += 1
    if answer == "YES":
        return "Your array: ", custom_array, "\nSorted array: ", array
    return "Sorted array: ", array
# Performance evaluation indicators
bubble1_code = """
def bubble_ascending(array=np.random.randint(-1000, 1000, 10000)):
    # Bubble sort in ascending order
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        i += 1
"""
time_bubble1 = timeit.timeit(setup=setup_code,
                             stmt=bubble1_code,
                             number=10)

print(bubble_ascending(), "\nFunction execution time:", time_bubble1)


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
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        i += 1
    if answer == "YES":
        return "Your array: ", custom_array, "\nSorted array: ", array
    return "Sorted array: ", array
# Performance evaluation indicators
bubble2_code = """
def bubble_ascending(array=np.random.randint(-1000, 1000, 10000)):
    # Bubble sort in descending order
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        i += 1
"""
time_bubble2 = timeit.timeit(setup=setup_code,
                             stmt=bubble2_code,
                             number=10)

print(bubble_descending(), "\nFunction execution time:", time_bubble2)


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
    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    if answer == "YES":
        return "Your array: ", custom_array, "\nSorted array: ", array
    return "Sorted array: ", array
# Performance evaluation indicators
selection1_code = """
def selection_ascending(array=np.random.randint(-1000, 1000, 10000)):
    # Selection sort in ascending order
    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
"""
time_selection1 = timeit.timeit(setup=setup_code,
                                stmt=selection1_code,
                                number=10)

print(selection_ascending(), "\nFunction execution time:", time_selection1)


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
    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] > array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    if answer == "YES":
        return "Your array: ", custom_array, "\nSorted array: ", array
    return "Sorted array: ", array
# Performance evaluation indicators
selection2_code = """
def selection_descending(array=np.random.randint(-1000, 1000, 10000)):
    # Selection sort in ascending order
    for i in range(len(array) - 1):
        min = i
        for j in range(i + 1, len(array)):
            if array[j] > array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
"""
time_selection2 = timeit.timeit(setup=setup_code,
                                stmt=selection2_code,
                                number=10)

print(selection_descending(), "\nFunction execution time:", time_selection2)


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
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    if answer == "YES":
        return "Your array: ", custom_array, "\nSorted array: ", array
    return "Sorted array: ", array
# Performance evaluation indicators
insertion1_code = """
def insertion_ascending(array=np.random.randint(-1000, 1000, 10000)):
    # Insertion sort in ascending order
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
"""
time_insertion1 = timeit.timeit(setup=setup_code,
                                stmt=insertion1_code,
                                number=10)

print(insertion_ascending(), "\nFunction execution time:", time_insertion1)


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
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] < key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    if answer == "YES":
        return "Your array: ", custom_array, "\nSorted array: ", array
    return "Sorted array: ", array
# Performance evaluation indicators
insertion2_code = """
def insertion_descending(array=np.random.randint(-1000, 1000, 10000)):
    # Insertion sort in ascending order
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] < key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
"""
time_insertion2 = timeit.timeit(setup=setup_code,
                                stmt=insertion2_code,
                                number=10)

print(insertion_descending(), "\nFunction execution time:", time_insertion2)
