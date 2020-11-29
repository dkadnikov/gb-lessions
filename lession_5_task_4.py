# Урок-5
# Задача-4

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

# Решение-задачи-4
print("Решение-задачи-4")
dictionary = {'One':'Один','Two':'Два','Three':'Три','Four':'Четыре', 'Five':'Пять', 'Six':'Шесть' }
check_list = []
result = []
with open('lession-5-task-4.txt', "r", encoding="utf-8") as temp_file:
    for i in temp_file:
        line = i.split(' - ')
        print(line)
        if line[0] in dictionary:
            word_to_check = dictionary[line[0]]
            result.append(word_to_check + ' - ' + line[1])
    print(result)
with open('lession-5-task-4-new.txt', "w", encoding="utf-8") as print_result:
    print_result.writelines(result)




