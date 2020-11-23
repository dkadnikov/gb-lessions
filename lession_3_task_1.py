# Урок-3
# Задача-1

# Создать список и заполнить его элементами различных типов данных.
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


# Решение-задачи-1
print("Решение-задачи-1")
print("")
#
#def my_func(x, y):
#    try:
#        z = x / y
#        return z
#    except ValueError:
#        return "Введить только числа"
#    except ZeroDivisionError:
#        return "Ошибка деления на ноль. Вы ввели значение y = 0"
#    return res
#
#print(my_func((int(input("Введите значение переменной x ="))), (int(input("Введите значение переменной y =")))))


def dif_list(*args):
    try:
        argument_1 = int(input("Введите числитель = "))
        argument_2 = int(input("Введите знаменатель = "))
        res = argument_1 / argument_2
    except ValueError:
        return "Ошибка значения, вы ввели не число"
    except ZeroDivisionError:
        return "Ошибка деления на ноль, введите знаменатель отличный от нуля!"

    return res

print(f'Результат: {dif_list()}')