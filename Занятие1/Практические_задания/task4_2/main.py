from itertools import count

#
# def func_(x):
#     return x % 2 == 0


def task():
    iterator_numbers = count(1, 1)
    # numbers = [i ** 2 for i in iterator_numbers if i % 2 == 0]  # заменить на map и filter
    numbers = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, iterator_numbers))

    for _ in range(10):  # напечатать первые 10 чисел
        print(next(numbers))  # с помощью next получать следующий элемент от итератора


if __name__ == "__main__":
    task()
