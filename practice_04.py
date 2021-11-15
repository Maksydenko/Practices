# Task 1

a = float(input("Write the first number: "))
b = float(input("Write the second number: "))
c = float(input("Write the third number: "))
d = float(input("Write the fourth number: "))

if a > b and a > c and a > d:
    print(f"{a} is the largest")
elif b > c and b > d:
    print(f"{b} is the largest")
elif c > d:
    print(f"{c} is the largest")
else:
    print(f"{d} is the largest")

# Task 2

year = int(input("Write year: "))

if (year % 400 == 0 or year % 100 != 0) and year % 4 == 0:
    print("This year has 366 days")
else:
    print("This year has 365 days")

# Task 3

a = float(input("Write the first side of the triangle: "))
b = float(input("Write the second side of the triangle: "))
c = float(input("Write the third side of the triangle: "))

if a + b > c and a + c > b and b + c > a:
    print("The triangle exists")
else:
    print("The triangle doesn't exist")

# Task 4

for i in range(1, 101):
    if i % 7:
        continue
    print(i)

# Task 5

n = int(input("Write the value n: "))

factorial = 1

while n > 1:
    factorial *= n
    n -= 1

print(f"Factorial n: {factorial}")

# Task 6

width = int(input("Write an odd number: "))

half = width // 2

if width % 2:
    for i in range(half):
        sand = "*" * (width - (i * 2))
        print(sand.center(width))
    print("*".center(width))
    for i in range(1, half + 1):
        sand = "*" * ((i * 2) + 1)
        print(sand.center(width))
else:
    print("You wrote an even number")

# Task 7

for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)