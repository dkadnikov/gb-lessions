# Урок-2
# Задача-1

# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


# Решение-задачи-1
print("Решение-задачи-1")
print("")

name = "Elon"
surname = "Musk"
birthday_day = 28
bithday_month = "june"
birthday_year = 1971
age = 49
place_burn = "Pretoria"

about_list = [name, surname, birthday_day, birthday_year,  birthday_year, bithday_month, age, place_burn]
for i in about_list:
    print(f'{i} is {type(i)}')
