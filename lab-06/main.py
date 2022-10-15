import string

# Task a

n = list(input("Write any symbols, but the first symbol must not be a \
space: ").lower())
m = []

for i in n:
    if i[0] == " ":
        print("The first character must not be a space")
        break

    if i == " ":
        break

    if i in string.punctuation:
        continue
    m.append(i)
print(set(m))

# Task b

number = int(input("Write the number of students: "))
new_data = dict()

while number > 0:
    data = input("Write student data (structure fields: surname, group, \
physics, algorithmization and programming, higher mathematics): ").split(", ")

    if (int(data[2]) + int(data[3]) + int(data[4])) / 3 > 75:
        new_data[data[0]] = data[1]
    number -= 1
print("Students with an average grade of more than 75 points and their \
groups:", new_data)
