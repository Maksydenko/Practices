# Task 1

str_1 = input("Write something to check the length: ")
print("Your string length:", len(str_1), "characters")

# Task 2

str_2 = input("Write something: ")

if len(str_2) < 2:
    print()
else:
    print(str_2[:2] + str_2[-2:])

# Task 3

str_3 = input("Write something: ")
print(str_3[0] + str_3[1:].replace(str_3[0], "$"))

# Task 4

str_4 = input("Write something: ")

if len(str_4) % 4:
    print("Your string length isn't a multiple of 4")
else:
    for i in reversed(str_4):
        print(i, end="")

# Task 5

words = sorted(input("\nWrite comma separated some words: ").split(", "))
print(words)
