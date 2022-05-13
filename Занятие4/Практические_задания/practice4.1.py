import re

text = "Everest is the largest mountain in the World"

print(re.findall(r'.', text))  # каждый символ
print(re.findall(r'\w', text))  # все кроме пробела
print(re.findall(r'\w+', text))  # все слова
print(re.findall(r'\w*', text))  # все слова c пустотами на месте пробелов
print(re.findall(r'\b[AaEeIiOoUuYy]\w+', text))  # слова c гласной
