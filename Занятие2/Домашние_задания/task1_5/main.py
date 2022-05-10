import random
from string import ascii_lowercase, ascii_uppercase, digits


def gen(collect, n=10):
    while True:
        yield ''.join(random.sample(collect, n))


def passw_gen(n=10):
    """
    Password generator

    :param n: num count
    :return: password str
    """
    collect = ascii_lowercase + ascii_uppercase + digits + "_-^"
    while True:
        yield ''.join(random.sample(collect, n))


if __name__ == "__main__":
    # print(next(gen(ascii_lowercase)))
    # print(next(gen(ascii_uppercase)))
    # print(next(gen(digits)))
    print(next(passw_gen(10)))
