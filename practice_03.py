# Task 1

print([i for i in range(1, 10)])

# Task 2

print([i for i in range(9, 0, -1)])

# Task 3

print([i for i in range(5, 14, 2)])

# Task 4

sum = 0

while True:
    x = float(input("Write the number: "))
    sum += x
    if x == 0:
        break
print(f"Sum: {sum}")

# Task 5

x = int(input("Write the number: "))
y = 0

while x > 0:
    y *= 10
    y += x % 10
    x = x // 10
print(y)

# Task 6

number = int(input("Write the number: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= number
print(f"Factorial: {factorial}")
