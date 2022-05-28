import math

# Task 1

print("Hello world!")

# Task 2

print("How are you?\nThis is my first practice\nThat's wonderful!")

# Task 3

lenght = float(input("Write the length of the rectangle: "))
width = float(input("Write the width of the rectangle: "))
square = lenght * width
print("Square:", square)

# Task 4

first = float(input("Write the first number: "))
second = float(input("Write the second number: "))
sum = first + second
product = first * second
difference = first - second
quotient = first / second
print("Sum:", sum, "; product:", product,
    "; difference:", difference, "; quotient:", quotient)

# Task 5

radius = float(input("Write the radius of the circle: "))
diameter = radius * 2
circumference = diameter * math.pi
area = radius ** 2 * math.pi
print("Diameter:", diameter, "; circumference:", circumference,
    "; area:", area)

# Task 6

number = int(input("Write the three-digit number: "))

if 99 < number < 1000:
    one = number // 100
    two = number // 10 % 10
    three = number % 10
    sum = one + two + three
    difference = one - two - three
    product = one * two * three
    print("Sum:", sum, "; difference:", difference, "; product:", product)
else:
    print("Your number isn't three-digit")
