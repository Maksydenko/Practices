import numpy as np
import random


# Task 1

def maxNum(array):
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
print("The maximum number is", maxNum(array))


# Task 2

def myConc(num1, num2, line):
    sum = num1 + num2
    return line + str(sum)
num1 = int(input("Write the first number: "))
num2 = int(input("Write the second number: "))
line = input("Write the text: ")
print(myConc(num1, num2, line))


# Task 3

def myRect(length, width):
    for i in range(width):
        print("*" * length)
    return myRect
length = int(input("The length of the rectangle: "))
width = int(input("The width of the rectangle: "))
print(myRect(length, width))


# Task 4

def lineSearch(array, num):
    i = 0
    while i < len(array) and array[i] != num:
        i += 1
    if i == len(array):
        return -1
    else:
        return "Element", num, "found at position", i
array = np.random.randint(0, 50, 25)
num = int(input("Write the number which you want to find: "))
print(lineSearch(array, num))


# Task 5

def numWords(words):
    num = len(words.split())
    return num
words = input("Write the text: ")
print(numWords(words))
