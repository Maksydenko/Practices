# Task 1

for i in range(1, 31):
    i *= i
    print(i)

# Task 2

exam_st_date = (11, 12, 2014)
print(f"The examination will start from: {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")

# Task 3

numbers = input("Write comma separated numbers: ")
numbers = numbers.split(", ")
numbers_tuple = tuple(numbers)
print(numbers, numbers_tuple)

# Task 4

list_1 = input("Write the first list: ").split()
list_2 = input("Write the second list: ").split()

if set(list_1) & set(list_2):
    print(True)
else:
    print(False)

# Task 5

number = [[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]
passengers = 0

for i in number:
    passengers += i[0] - i[1]
print(f"After all the stops, there are {passengers} passengers left on the bus")
