# Урок-5
# Задача-3

# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

# Решение-задачи-3
print("Решение-задачи-3")

with open('lession-5-task-3.txt', "r", encoding="utf-8") as temp_file:
    familia = []
    oklad = []
    new_list = temp_file.read().split('\n')
    for i in new_list:
        i = i.split()
        if int(i[1]) < 20000:
            oklad.append(i[0])
        familia.append(i[1])
print(f'Оклад меньше 20.000 у - {", ".join(oklad)}\n'
      f'Cредний оклад всех сотрудников {sum(map(int, familia)) / len(familia)} у.е. ')


