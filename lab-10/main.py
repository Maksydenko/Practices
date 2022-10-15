# Task 1

def is_int(answer):
    try:
        int(answer)
        return True
    except ValueError:
        return False


def reverse_sequence(custom_list):
    if not custom_list:
        return []
    return [custom_list.pop()] + reverse_sequence(custom_list)

custom_list = []

while True:
    answer = input('Write a number (if you no longer want to write numbers, \
then write "."): ')

    if is_int(answer):
        custom_list.append(int(answer))
    elif str(answer) == ".":
        break
    else:
        continue
print(reverse_sequence(custom_list))

# Task 2

def prime_number(number, divider):
    if divider > 1:
        if number % divider:
            return prime_number(number, divider - 1)
        return "Your number isn't prime"
    elif number < 2:
        return "Your number isn't prime"
    return "Your number is prime"
number = input("Write the number: ")
number, divider = int(number), int(number) - 1
print(prime_number(number, divider))

# Task 3

hexadecimal_number = lambda number: number.hex()
number = float(input("Write the number: "))
print(hexadecimal_number(number))