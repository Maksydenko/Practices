# Task 1

string_1 = input("Write something: ")
print(f"Your string length: {len(string_1)} characters")

# Task 2

string_2 = input("Write something: ")

if len(string_2) < 2:
    print()
else:
    print(string_2[:2] + string_2[-2:])

# Task 3

string_3 = input("Write something: ")
print(string_3[0] + string_3[1:].replace(string_3[0], "$"))

# Task 4

string_4 = input("Write something: ")

if len(string_4) % 4:
    print("Your string length isn't a multiple of 4")
else:
    for i in range(-1, -1 * len(string_4) - 1, -1):
        print(string_4[i], end="")

# Task 5

words = input("Write comma separated some words: ")
print(sorted(words.split(", ")))
