import math

# Task 1

print("Hello world!")

# Task 2

print("How are you?\n\
This is my first practice\n\
That's wonderful!")

# Task 3

lenght = float(input("Write the length of the rectangle: "))
width = float(input("Write the width of the rectangle: "))
print(f"Square: {lenght * width}")

# Task 4

first = float(input("Write the first number: "))
second = float(input("Write the second number: "))
print(f"Sum: {first + second}; product: {first * second}; \
difference: {first - second}; \quotient: {first / second}")

# Task 5

radius = float(input("Write the radius of the circle: "))
print(f"Diameter: {radius * 2};circumference: {radius * 2 * math.pi}; \
area: {radius ** 2 * math.pi}")

# Task 6

number = int(input("Write the three-digit number: "))

if 99 < number < 1000:
    one = number // 100
    two = number // 10 % 10
    three = number % 10
    sum = one + two + three
    difference = one - two - three
    product = one * two * three
    print(f"Sum: {one + two + three}; difference: {one - two - three}; \
product: {one * two * three}")
else:
    print("Your number isn't three-digit")
