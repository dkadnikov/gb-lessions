# Урок-5
# Задача-2

# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# Решение-задачи-2
print("Решение-задачи-2")
lines = 0
words = 0
letters = 0
with open("lession-5-task-2.txt", "r", encoding="utf-8") as temp_file:
    for line in temp_file:
        lines += 1
        pos = 'out'
print(f'В проанализированном файле - {lines} строк.')

with open("lession-5-task-2.txt", "r", encoding="utf-8") as temp_file:
    lines = temp_file.readlines()
    for index, value in enumerate(lines):
        words = len(value.split())
        print('Строка номер {} содержит {} слов.'.format(index + 1, words))