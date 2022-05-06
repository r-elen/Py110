INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, encoding="utf-8") as f:  # перезаписать содержимое одного файла в другой
        list_lines = list(map(str.upper, f))

    with open(OUTPUT_FILE, 'w', encoding="utf-8") as out_f:
        out_f.writelines(list_lines)


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
