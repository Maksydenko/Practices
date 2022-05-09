import numpy as np
import random


# Task 1

def max_num(array):
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        i += 1
    return array[-1]
array = np.random.randint(-50, 50, 25)
print("The maximum number is", max_num(array))


# Task 2

def my_conc(num1, num2, line):
    sum = num1 + num2
    return line + str(sum)
num1 = int(input("Write the first number: "))
num2 = int(input("Write the second number: "))
line = input("Write the text: ")
print(my_conc(num1, num2, line))


# Task 3

def my_rect(length, width):
    for i in range(width):
        print("*" * length)
    return my_rect
length = int(input("The length of the rectangle: "))
width = int(input("The width of the rectangle: "))
print(my_rect(length, width))


# Task 4

def line_search(array, num):
    i = 0
    while i < len(array) and array[i] != num:
        i += 1
    if i == len(array):
        return -1
    else:
        return "Element", num, "found at position", i
array = np.random.randint(0, 50, 25)
num = int(input("Write the number which you want to find: "))
print(line_search(array, num))


# Task 5

def numWords(words):
    num = len(words.split())
    return num
words = input("Write the text: ")
print(numWords(words))
