def list_comprehension(words: list) -> list:
    return [str.capitalize(word) for word in words]  # через list comprehension


def list_map(words: list) -> list:
    return list(map(str.capitalize, words))  # через map


def task():
    list_words = [
        "goldenROD",
        "puRPle",
        "sAlMoN",
        "TURQUOISE",
        "cYAN"
    ]

    print(list_comprehension(list_words))
    print(list_map(list_words))


if __name__ == "__main__":
    task()
