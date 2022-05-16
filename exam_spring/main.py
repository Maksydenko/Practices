def is_int(answer):
    try:
        int(answer)
        return True
    except ValueError:
        return False

# Task 1

def original_lyrics(song_decoder):
    if len(song_decoder) > 200 or len(song_decoder.split()) > 1:
        print("You wrote more than 200 characters or more than 1 word")
    list_lyrics = song_decoder.split("WUB")
    for word in list_lyrics:
        if word == "":
            continue
        print(word, end=" ")
    return " — original lyrics"
song_decoder = input("Write the lyrics for the remix in one word \
(no more than 200 characters): ").upper()
print(original_lyrics(song_decoder))

# Task 2

def morse_number(number):
    if number < 0 or number > 9:
        return "Your number is less than 0 or greater than 9"
    morse_code = []
    max_morse = 5
    if 0 <= number <= 5:
        for dot in range(number):
            morse_code.append("•")
        if len(morse_code) < max_morse:
            for dash in range(max_morse - len(morse_code)):
                morse_code.append("—")
        for symbol in morse_code:
            print(symbol, end="")
    if 6 <= number <= 9:
        for dash in range(number - max_morse):
            morse_code.append("—")
        for dot in range(max_morse - len(morse_code)):
            morse_code.append("•")
        for symbol in morse_code:
            print(symbol, end="")
    return " — Morse code of your number"
number = int(input("Write a number from 0 to 9: "))
print(morse_number(number))

# Task 3

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

# Task 4

def even_odd(iq_test):
    if len(iq_test) <= 1:
        return "We can't solve this task"
    even_numbers, odd_numbers = 0, 0
    even_index, odd_index = 0, 0
    for index in range(len(iq_test)):
        if iq_test[index] % 2:
            even_numbers += 1
            even_index = index + 1
        else:
            odd_numbers += 1
            odd_index = index + 1
    if even_numbers != 1 and odd_numbers != 1:
        return "We can't solve this task"
    if even_numbers == 1:
        return even_index
    return odd_index

iq_test = []

while True:
    answer = input('Write a number (if you no longer want to write numbers, \
then write "."): ')
    if is_int(answer):
        iq_test.append(int(answer))
    elif str(answer) == ".":
        break
    else:
        continue
print(even_odd(iq_test))

# Task 5

def sorted_string(string):
    if len(string) > 9:
        return "You wrote more than 9 words"
    step = 0
    flag = True
    while flag:
        flag = False
        for word in range(len(string) - step - 1):
            for symbol1 in string[word]:
                if is_int(symbol1):
                    for symbol2 in string[word + 1]:
                        if is_int(symbol2):
                            if symbol1 > symbol2:
                                string[word], string[word + 1] = string[word + 1], string[word]
                                flag = True
        step += 1
    return string
string = input("Write words containing numbers from 1 to 9: ").split()
print(sorted_string(string))