# Урок-5
# Задача-7

# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

# Решение-задачи-7
import json

print("Решение-задачи-7\n")
profit_list = [{}, {}]
profit = 0
with open("lession-5-task-7.txt", "r", encoding="utf-8") as temp_file:
    for line in temp_file:
        name, form_company, proceeds, mat_losses = line.split()
        profit_list[0][name] = int(proceeds) - int(mat_losses)
# print(profit_list[0])
profit = [x for x in profit_list[0].values() if x >= 0]
profit = sum(profit)
# print(profit)
# profit = sum(profit_list[0].values())
# print(profit)
profit_list[1]['Средняя выручка / Average profit: '] = round(profit)
# print(profit_list)
with open("lession-5-task-7.json", "w", encoding="utf-8") as write_to_json:
    json.dump(profit_list, write_to_json, ensure_ascii=False)
