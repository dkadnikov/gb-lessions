# Урок-5
# Задача-5

# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# Решение-задачи-5
import random
print("Решение-задачи-5\n")
# я подумал, что задать просто список файлов - было бы скучно, по этому вот ->
temp_list = int(random.random() * 1E50)
temp_list = str(temp_list)
print(f'Я сгенерировал число - {temp_list}')

with open('lession-5-task-5.txt', "w", encoding="utf-8") as temp_file_container:
    temp_list = [str(i) for i in temp_list]
    temp_list = ' '.join(temp_list)
    print(f'Вот что я записал в файл: {temp_list}')
    temp_file_container.writelines(temp_list)
with open('lession-5-task-5.txt', "r", encoding="utf-8") as sym_number:
    total = 0
    for i in sym_number:
        i = i.split(' ')
        for n in i:
            total += int(n)
    print(f'Сумма чисел в файле (разделенных пробелом) = {total}')
