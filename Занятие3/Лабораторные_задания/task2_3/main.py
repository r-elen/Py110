import json


def task():
    filename = "input.json"
    with open(filename) as f:  # считать содержимое JSON файла
        json_file = json.load(f)

    return max(json_file, key=lambda item: item["score"])  # найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
