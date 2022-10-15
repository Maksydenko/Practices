from random import randint
from pickle import dump, load

with open("f.txt", "wb+") as my_f:
    length = 10
    numbers = []

    for i in range(length):
        number = randint(-10, 10)
        numbers.append(str(number) + "\n")
    dump(numbers, my_f)

    with open("g.txt", "wb+") as my_g:
        numbers = []

        for i in range(length):
            number = randint(-10, 10)
            numbers.append(str(number) + "\n")
        dump(numbers, my_g)

with open("h.txt", "wb+") as my_h:
    subtraction = []

    with open("f.txt", "rb") as my_f:
        with open("g.txt", "rb") as my_g:
            numbers_f = load(my_f)
            numbers_g = load(my_g)

            for index in range(length):
                subtraction.append(str(int(numbers_f[index]) -
                                       int(numbers_g[index])) + "\n")
            dump(subtraction, my_h)
            my_h.seek(0)

            for number in load(my_h):
                print(number, end="")
