def output_type_int(fn):
    def wrapper(*args, **kwargs):

        for i in args:
            if not isinstance(i, int):
                raise TypeError(f"{i} не является целым числом")
        return fn(*args, **kwargs)
    return wrapper


@output_type_int
def return_int(*args):
    return sum(args)


if __name__ == "__main__":
    print(return_int(84, 11, 102.2))
