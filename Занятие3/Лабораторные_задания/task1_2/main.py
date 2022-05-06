OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, 'w', encoding='utf8') as f:  # записать лесенку в файл
        for i in range(1, 11):
            f.write((' ' * (10 - i) + ('*' * i)) + '\n')


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
