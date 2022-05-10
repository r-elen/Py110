import time


def work_time(fn):
    def wrapper(*args, **kwargs):
        t = time.time()
        result = fn(*args, **kwargs)
        dt = time.time() - t
        print(f'Время работы {dt:.2f}')
        return result
    return wrapper


def geom_progress(b, q):
    while True:
        yield b
        b = b * q


# def get_sum(iter_, desired_sum):


@work_time
def task():
    my_count = geom_progress(1, 0.5)
    # for _ in range(5):
    #     print(next(my_count))
    n = 0
    sum_ = 0
    while sum_ < 2.000001:
        x = next(my_count)
        sum_ += x
        n += 1
        print(f'{n}, {sum_:.10f}')


if __name__ == "__main__":
    task()
