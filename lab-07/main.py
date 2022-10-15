import numpy as np

# Task 1

number = int(input("Write the number of elements in a linear array: "))
x = []

for i in range(number):
    x.append(int(input("Write the array element: ")))
print(x[::-1])

# Task 2

array = np.eye(3)

for i in range(3):
    for j in range(3):
        array[i][j] = int(input("Write the array element: "))
print(array.transpose())

# Task 3

array_1 = np.eye(3)
array_2 = np.eye(3)

for i in range(3):
    for j in range(3):
        array_1[i][j] = int(input("Write the element of the first array: "))

for i in range(3):
    for j in range(3):
        array_2[i][j] = int(input("Write the element of the second array: "))
print(array_1.dot(array_2))

# Task 4

array = np.eye(4)

for i in range(4):
    for j in range(4):
        array[i][j] = int(input("Write the array element: "))

        if array[i][j] < 0:
            array[i][j] = 0
print(array)