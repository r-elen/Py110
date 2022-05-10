def geom_progress(b, q):
    while True:
        yield b
        b = b * q


if __name__ == "__main__":
    my_count = geom_progress(1, 0.5)
    for _ in range(5):
        print(next(my_count))

    # sum_ = 0
    # while sum_ < 1.8:
    #     sum += next(my_count)
