from string import printable, digits, ascii_letters
from random import choice


def random_string():
    my_string = ""

    for symbol in range(64):
        my_string += choice(printable)
    return my_string

with open("f.txt", "w+") as my_f:
    my_f.write(random_string())

    with open("g.txt", "w+") as my_g:
        my_f.seek(0)

        for symbol in my_f.read():
            if symbol in digits:
                my_g.write(symbol)
        my_g.seek(0)
        print(my_g.read())

    with open("my_h.txt", "w+") as my_h:
        my_f.seek(0)

        for symbol in my_f.read():
            if symbol in ascii_letters:
                my_h.write(symbol)
        my_h.seek(0)
        print(my_h.read())
