import re


def task():
    word_list = [
        ",./ sdfsdf",
        "Ddfsdf",
        "@@##,sdfsdf",
        "123_sdfsdf",
        "123sdfsdf",
        ", s,dfsdf",
        "123, fewfew",
    ]

    two_char = re.compile(r'\b\w\w')  # составить регулярное выражение, которое находит первые две буквы слова

    for word in word_list:
        # print(re.findall(two_char, word))  # найти первые 2 буквы всех слов в строке
        print(two_char.findall(word))


if __name__ == "__main__":
    task()
