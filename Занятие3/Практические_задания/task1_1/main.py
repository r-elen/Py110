def task():
    filename = "input.txt"
    with open(filename) as f:  # менеджер контекста открывает файл в режиме чтения в текстовом формате "rt"
        for line in f:  # файл является итератором, который построчно возвращает свое содержимое
            new_line = line.strip()  # c помощью метода строки strip очистить строку от непечатыемых символов
            print(new_line)


if __name__ == "__main__":
    task()
