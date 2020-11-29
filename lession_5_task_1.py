# Урок-5
# Задача-1

# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

# Решение-задачи-1
print("Решение-задачи-1")
print("")

my_list = []
while True:
    line = input("Введите данные для записи в файл (Для окончания ввода введите Q): ")
    if line == 'Q':
        print(my_list)
    if line == 'q':
        print(my_list)
        exit()
    else:
        new_line = line + '\n'
        my_list.append(new_line)

    with open("lession-5-task-1.txt", "w", encoding="utf-8") as temp_file:
        temp_file.writelines(my_list)
