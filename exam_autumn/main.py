import math

# Task 1

for x in range(10, 300, 5):
    x / 10
    print((5 * x ** 2 - 3 * x) / math.sin(x))

# Task 2

diapason = input("Write through a comma from what to what number will be \
displayed odd numbers: ").split(", ")

for i in diapason:
    if int(i) % 2:
        print(i)

# Task 3

words = input("Write the words through a comma: ").lower().split(", ")
new_words = 0

for i in words:
    if i[0] == i[-1]:
        new_words += 1
print(new_words)

# Task 4

for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)