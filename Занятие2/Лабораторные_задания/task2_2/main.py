from itertools import count


# def count_(start_number: float = 1, step: float = 1):
#     for i in count(start_number, step):  # написать функцию-генератор возвращающую целые числа
#         yield i


def count_2(start_number: float = 1, step: float = 1):
    while True:
        yield start_number
        start_number += step


if __name__ == "__main__":
    my_count = count_2(10, 0.5)
    for _ in range(10):
        print(next(my_count))
