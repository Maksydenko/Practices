# Task 1: Construct these numeric values

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

# Task 2: Type Conversation

a1 = str(123)
b1 = int(a1)

c1 = float(a1)

d1 = 12.345
e1 = int(d1)

# Task 3: Digits of a Number

card_number = int(input("Write your credit card number: "))

if card_number > 9999999999999999:
    print("The wrong card number is specified")
elif card_number < 1000000000000000:
    print("The wrong card number is specified")
else:
    digit_one = card_number // 1000 % 10
    digit_two = card_number // 100 % 10
    digit_three = card_number // 10 % 10
    digit_four = card_number % 10
    print("The last 4 digits of a credit card: " + str(digit_one) + str(digit_two) + str(digit_three) + str(digit_four))

number = int(input("Write the three-digit number: "))

if number > 999:
    print("Your number isn't three-digit")
elif number < 100:
    print("Your number isn't three-digit")
else:
    first_digit = number // 100
    second_digit = number // 10 % 10
    third_digit = number % 10
    sum = first_digit + second_digit + third_digit
    print("The sum of the digits of a three-digit number: " + str(sum))
    
