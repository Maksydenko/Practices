# Task 1

a = 0
print(a)

b = 0.0
print(b)

c = 101
print(c)

d = 1000.0
print(d)

e = float(1e3)
print(e)

f = 7
print(f)
g = -7
print(g)
h = 0
print(h)

j = 2 + (f - 6) / g * 9
print(j)
k = 5 ** h - (9 + f * -3)
print(k)

l = 3.2
print(l)
m = -11.15
print(m)
n = 14.6
print(n)

o = 19 - m + 14 ** 2
print(o)
p = 3 * n // (9 + l)
print(p)

q = (f + l) / 2 - h
print(q)
r = 9 + m - (g % 3) + n
print(r)

s = float(f) / g
print(s)

# Task 2

a1 = str(123)

b1 = int(a1)
print(b1)

c1 = float(a1)
print(c1)

d1 = 12.345

e1 = int(d1)
print(e1)

# Task 3

card_number = int(input("Write your credit card number: "))

if 999999999999999 < card_number < 10000000000000000:
    print(f"The last 4 digits of a credit card: {card_number // 1000 % 10}\
{card_number // 100 % 10}{card_number // 10 % 10}{card_number % 10}")
else:
    print("The wrong card number is specified")
    
number = int(input("Write the three-digit number: "))

if 99 < number < 1000:
    digit_1 = number // 100
    digit_2 = number // 10 % 10
    digit_3 = number % 10
    print(f"The sum of the digits of a three-digit number: \
{digit_1 + digit_2 + digit_3}")
else:
    print("Your number isn't three-digit")
