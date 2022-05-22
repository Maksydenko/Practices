def sort_numbers(lines):
    i = 0
    flag = True
    while flag:
        flag = False
        for j in range(len(lines) - i - 1):
            if lines[j].split(", ")[0] > lines[j + 1].split(", ")[0]:
                lines[j], lines[j + 1] = lines[j + 1], lines[j]
                flag = True
        i += 1
    return lines

try:
    with open("my_text.txt") as my_file:
        sort_lines = []
        for line in sort_numbers(my_file.readlines()):
            if line[-1] != "\n":
                line = line + "\n"
            sort_lines.append(line)
    with open("my_text.txt", "w+") as my_file:
        my_file.writelines(sort_lines)
        my_file.seek(0)
        print(my_file.read())
except FileNotFoundError as fnfe:
    print(fnfe)
