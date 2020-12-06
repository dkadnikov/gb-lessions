# Урок-7
# Задача-3
#
# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
#
# Решение-задачи-3
print("Решение-задачи-3", '\n')


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return (f'Результат -  {self.quantity * "*"}\n')

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return Cell(self.quantity - other.quantity) \
            if (self.quantity - other.quantity) > 0 \
            else print('Отрицательный результат тоже результат!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(12)
cells2 = Cell(15)
print(f'Колличество клекток в одной ячейке: {cells1}')
print(f'Колличество клекток в другой ячейке: {cells2}')
print(f'Операция сложения: {cells1 + cells2}')
print(f'Операция вычитания: {cells1 - cells2}')
print(f'Операция деления: {cells1 / cells2}')

# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
print(cells1.make_order(5))
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
print(cells2.make_order(5))


