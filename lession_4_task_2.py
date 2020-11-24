# Урок-4
# Задача-2

# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

# Решение-задачи-2
print("Решение-задачи-2")
print("")
#my_list = [1, 2, 3, 4, 5, 6, 7, 33, 90]
#my_new_list = [el+10 for el in my_list]
# my_new_list_2 = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
#print(my_list)
#print(my_new_list)
# print(my_new_list_2)

my_list = [3, 20, 9, 5, 1, 8, 11, 6, 15]
print(my_list)
my_list_new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(my_list_new)
