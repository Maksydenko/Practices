import math

# Task 1

a = float(input("Write the value of a: "))
b = float(input("Write the value of b: "))
a, b = b, a
print(f"{a=}, {b=}")

# Task 2

average = (a + b) / 2
print("Average:", average)
geometric_mean = math.sqrt(a * b)
print("Geometric mean:", geometric_mean)

# Task 3

x = int(input("Write the number: "))
y = 0

while x > 0:
    y *= 10
    y += x % 10
    x = x // 10
print(y)

# Task 4

second = int(input("Write seconds: "))
hour = second // 3600
minute = (second - hour * 3600) // 60
print("Hours:", hour, "; minutes:", minute)

# Task 5

corner = (hour + minute / 60 + second / 3600) % 12 * 30
print("Corner:", corner)

# Task 6

x = int(input("Write the number: "))

if x % 2:
    print("The number is odd")
else:
    print("The number is even")

if x % 5 == 0 and x % 2:
    print("The number ends with the digit 5")
else:
    print("The number doesn't end with the digit 5")

# Task 7

day = int(input("Write the day: "))

if day == range(1, 366, 7):
    print("It's Monday")
elif day == range(2, 366, 7):
    print("It's Tuesday")
elif day == range(3, 366, 7):
    print("It's Wednesday")
elif day == range(4, 366, 7):
    print("It's Thursday")
elif day == range(5, 366, 7):
    print("It's Friday")
elif day == range(6, 366, 7):
    print("It's Saturday")
else:
    print("It's Sunday")

# Task 8

a = float(input("Write the fractional number a:"))
b = float(input("Write the fractional number b:"))
c = float(input("Write the fractional number c:"))
discriminant = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(discriminant)) / (2 * a)
x2 = (-b * math.sqrt(discriminant)) / (2 * a)

if x1 // 1 != x1 or x2 // 1 != x2:
    print("Equation ax² + bx + c has fractional roots")
else:
    print("Equation ax² + bx + c hasn't fractional roots")
