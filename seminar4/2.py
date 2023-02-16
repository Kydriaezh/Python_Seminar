# Пользователь вводит текст (строка). Определить, сколько различных слов содержится в этом тексте


string = input()
string = set(string.lower(). split())
print(len(string))