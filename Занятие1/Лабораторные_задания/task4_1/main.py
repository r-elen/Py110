from itertools import count


def task():
    counter = count(100, 10)

    # распечатать с столбик первые 10 чисел бесконечного итератора
    for _ in range(10):
        print((next(counter)))


if __name__ == "__main__":
    task()
