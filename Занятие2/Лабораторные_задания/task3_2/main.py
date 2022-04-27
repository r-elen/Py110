def min_len_check(fn):
    def wrapper(arg):  # записать обертку для исходной функции
        fn(arg)
        if len(arg) < 10:
            raise ValueError("Строка слишком короткая")
        else:
            print("Все хорошо")
    return wrapper


@min_len_check  # задекорировать функцию
def some_func(str_arg: str):
    print(str_arg)


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо
    print("-----")
    some_func("Short str")  # ValueError("Строка слишком короткая")
