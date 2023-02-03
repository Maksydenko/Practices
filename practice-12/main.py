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


def sortFile(file_path):
    try:
        with open(file_path) as file:
            sort_lines = []

            for line in sort_numbers(file.readlines()):
                if line[-1] != "\n":
                    line = line + "\n"
                sort_lines.append(line)

        with open(file_path, "w+") as file:
            file.writelines(sort_lines)
            file.seek(0)
            print(file.read())
    except FileNotFoundError as fnfe:
        print(fnfe)
