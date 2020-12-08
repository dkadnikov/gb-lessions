# Урок-8
# Задача-3
# Создайте собственный класс-исключение,
# который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
#  Класс-исключение должен контролировать типы данных элементов списка.
#
# Решение-задачи-3
print("Решение-задачи-3", '\n')


class CheckNum:
    def __init__(self, *args):
        self.dif_list = []

    def input_int(self):

        while True:
            try:
                val = int(input('Введите значения и нажимайте Ввод (Для выхода просто нажмите Ввод) -'))
                self.dif_list.append(val)
                print(f'Текущий список - {self.dif_list} \n ')
            except:
                print(f"Недопустимое значение ввода")
                stop = input(f'Повторить вввод? Y/N ')

                if stop == 'Y' or stop == 'y':
                    print(try_except.input_int())
                elif stop == 'N' or stop == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = CheckNum(1)
print(try_except.input_int())