import numpy as np
import random


def myFac(fac):
    if fac < 0:
        return "You wrote the number less than zero"
    if fac == 0:
        return 1
    else:
        return fac * myFac(fac - 1)
fac = int(input("Write the number: "))
print(myFac(fac))