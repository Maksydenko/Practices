# First task

print('Hello world!')

# Second task

print('How are you?\nThis is my first practice\nThat\'s wonderful!')

# Third task

lenght = float(input('Write the length of the rectangle: '))
width = float(input('Write the width of the rectangle: '))

square = lenght * width

print('Square = ' + str(square))

# Fourth task

first = float(input('Write the first number: '))
second = float(input('Write the second number: '))

plus = first + second
multiply = first * second
minus = first - second
divide = first / second

print('Sum = ' + str(plus) + '; product = ' + str(multiply) + '; difference = ' + str(minus) + '; quotient = ' + str(divide))

# Fifth task

import math

radius = float(input('Write the radius of the circle: '))

diameter = radius * 2
circumference = diameter * math.pi
area = radius ** 2 * math.pi

print('Diameter = ' + str(diameter) + '; circumference = ' + str(circumference) + '; area = ' + str(area))

# Sixth task

number = int(input('Write the three-digit number: '))

if number > 999:
    print('Your number isn\'t three-digit')
elif number < 100:
    print('Your number isn\'t three-digit')
else:
    one = number // 100
    two = number // 10 % 10
    three = number % 10
    sum = one + two + three
    difference = one - two - three
    product = one * two * three
    print('Sum = ' + str(sum) + '; difference = ' + str(difference) + '; product = ' + str(product))
