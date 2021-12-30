import math

# Task 1

x = int(input("Write the value x: "))
y = int(input("Write the value y: "))
z = int(input("Write the value z: "))

if x % 2:
    print("x is odd")
else:
    print("x is even")

if x % 20:
    print("x isn't a multiple of 20")
else:
    print("x is a multiple of 20")

if x and y >= 0:
    print("x and y are both positive")
else:
    print("x and y aren't both positive")

if x and y >= 0 or x and y < 0:
    print("x and y have the same sign")
else:
    print("x and y haven't the same sign")

if x >= 0 and y < 0 or x < 0 and y >= 0:
    print("x and y have different signs")
else:
    print("x and y haven't different signs")

if x == y and x == z:
    print("All three names are bound to equal values")
else:
    print("All three names aren't bound to equal values")

if x != y and x != z and y != z:
    print("All three names are bound to different values")
else:
    print("All three names aren't bound to different values")

if x == y and x != z or x == z and x != y or y == z and y != x:
    print("Two variables store the same value, but the third one is different")
else:
    print('"Two variables store the same value, but the third one is different" \
- this statement is incorrect')

# Task 2

x1 = int(input("Write the value x1: "))
y1 = int(input("Write the value y1: "))
x2 = int(input("Write the value x2: "))
y2 = int(input("Write the value y2: "))

print(f"The distance between these points: \
{math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)}")

print("The slope of the line from the first point to the second:", 
(y2 - y1) / (x2 - x1))

if x1 and x2 == 0:
    print("Both points lie on the same line Oy from the origin")
elif y1 and y2 == 0:
    print("Both points lie on the same line Oy from the origin")
elif x1 and x2 and y1 and y2 == 0:
    print("Both points lie on the point (0; 0)")
else:
    print('"Both points lie on the same line from the origin" \
- this statement is incorrect')

print("The first point is above the second:", y1 > y2)

if x1 and y1 > 0:
    print("The first point lies in the first quadrant")
elif x1 < 0 < y1:
    print("The first point lies in the second quadrant")
elif x1 and y1 < 0:
    print("The first point lies in the third quadrant")
elif x1 > 0 > y1:
    print("The first point lies in the fourth quadrant")
else:
    print("The first point lies on the coordinate axes")

if x1 and x2 and y1 and y2 > 0:
    print("The two points lie in the first quadrant")
elif x1 and x2 < 0 < y1 and y2:
    print("The two points lie in the second quadrant")
elif x1 and x2 and y1 and y2 < 0:
    print("The two points lie in the third quadrant")
elif x1 and x2 > 0 > y1 and y2:
    print("The two points lie in the fourth quadrant")
else:
    print("The two points don't lie in the same quadrant")
