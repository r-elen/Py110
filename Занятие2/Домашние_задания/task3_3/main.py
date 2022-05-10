from collections.abc import Iterable


def output_gen_type(fn):
    def wrapper(*args, **kwargs):
        some_obj = fn(*args, **kwargs)
        for i in args:
            if not (isinstance(i, Iterable)):
                raise TypeError("Объект {i} не является итерируемым")
        return some_obj
    return wrapper


@output_gen_type
def return_gen(*args):
    return args


if __name__ == "__main__":
    print(return_gen('vyu'))
