# Task 1

str_1 = input("Write something with quotes: ")
str_2 = ""

for i in str_1:
    if i == "'":
        str_2 += '"'
    elif i == '"':
        str_2 += "'"
    else:
        str_2 += i
print(str_2)

# Task 2

palindrome = input("Write something to check the palindrome: ")
print(palindrome == palindrome[::-1])

# Task 3

str_3 = input("Write something: ")
splitter = " "
str_4 = []

while str_3.find(splitter) > -1:
    splitter_index = str_3.find(splitter)
    str_4.append(str_3[0:splitter_index])
    str_3 = str_3[splitter_index + len(splitter):]
str_4.append(str_3)
print(str_4)

# Task 4

words = input("Write something to check the longest word: ").split()
max_length = 0

for i in words:
    if len(i) > max_length:
        max_length = len(i)
        max_word = i
print(max_word)

# Task 5

int_1 = input("Write a positive integer: ")
sum = 0

if int(int_1) > 0:
    for i in int_1:
        if int(i) % 2 != 0:
            sum += int(i)
    print(sum)
else:
    print("Your number isn't positive")

# Task 6

int_2 = str(bin(int(input("Write an integer"))))[2:]
sum = 0

for i in int_2:
    sum += int(i)
print(sum)

# Task 7

directions = input("Write directions separated by commas \
(NORTH, SOUTH, WEST, EAST): ").upper().split(", ")
north = south = west = east = 0
new_directions = []

for i in directions:
    if i == "NORTH":
        north += 1
    elif i == "SOUTH":
        south += 1
    elif i == "WEST":
        west += 1
    else:
        east += 1

if north > south:
    north -= south
    new_directions += ["NORTH"] * north
else:
    south -= north
    new_directions += ["SOUTH"] * south

if west > east:
    west -= east
    new_directions += ["WEST"] * west
else:
    east -= west
    new_directions += ["EAST"] * east

print(new_directions)

# Task 8

words = input("Write a comma-separated list of words \
from the game Shiritori: ").lower().split(", ")
shiritori = []

for i in range(len(words)):
    if words[i] == "":
        break
    shiritori.append(words[i])

    if i < len(words) - 1 and words[i + 1] != "":
        if words[i][-1] != words[i + 1][0]:
            break
print(shiritori)
