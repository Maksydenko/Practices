def myFac(n):
    if n < 0:
        return "You wrote the number less than zero"
    if n == 0:
        return 1
    else:
        return n * myFac(n - 1)
fac = int(input("Write the number: "))
print(myFac(fac))