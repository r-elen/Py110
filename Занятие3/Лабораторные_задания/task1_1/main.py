INPUT_FILE = "input.txt"


def task() -> None:
    with open("input.txt") as f:  # открыть указатель на файл
        for line in f:  # файл является итератором, который работает с циклом for в построчном режиме
            print(line.rstrip())


if __name__ == "__main__":
    task()
