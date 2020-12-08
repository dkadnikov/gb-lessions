# Урок-8
# Задача-4-5-6
#
# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать
# строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте
# «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
#
# Решение-задачи-4-5-6
print("Решение-задачи-4-5-6", '\n')

class Storage:

    def __init__(self, name, price, amount, model, *args):
        self.name = name
        self.price = price
        self.amount = amount
        self.model = model
        self.storage_full = []
        self.storage = []
        self.storage_cell = {'Модель': self.name, 'Цена за ед, руб.': self.price, 'Кол-во, шт.': self.amount}

    def __str__(self):
        return f'Модель: {self.name} цена {self.price} кол-во {self.amount}'

    # @classmethod
    # @staticmethod
    def get_param(self):
        try:
            cell = input(f'Введите модель ')
            cell_price = int(input(f'Введите цену за ед в рублях '))
            cell_amount = int(input(f'Введите количество, шт. '))
            unique = {'Модель устройства': cell, 'Цена за ед, руб.': cell_price, 'Количество, шт.': cell_amount}
            self.storage_cell.update(unique)
            self.storage.append(self.storage_cell)
            print(f'Текущий список -\n {self.storage}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.storage_full.append(self.storage)
            print(f'Весь склад -\n {self.storage_full}')
            return f'Выход'
        else:
            return Storage.get_param(self)


class Printer(Storage):
    def return_printer_model(self):
        return f'Модель устройства {self.name} -  {self.model} '


class Scanner(Storage):
    def return_scanner_model(self):
        return f'Модель устройства {self.name} -  {self.model} '

class Xerox(Storage):
    def return_xerox_model(self):
        return f'Модель устройства {self.name} -  {self.model} '

cell_one = Printer('Kiosera', 100, 200, 'K100')
cell_two = Scanner('Epson', 200, 300, 'n550')
cell_three = Xerox('Xerox', 300, 400, 'KS1200')
print()
print(cell_one.get_param())
print(cell_two.get_param())
print(cell_three.get_param())
print()
print(cell_one.return_printer_model())
print(cell_two.return_scanner_model())
print(cell_three.return_xerox_model())
