# Урок-8
# Задача-2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.
#
# Решение-задачи-2
print("Решение-задачи-2", '\n')

class DivisionByZeroError:
    def __init__(self, numerator, denominator):
        self.divider = numerator
        self.denominator = denominator

    @staticmethod
    def intdiv(numerator, denominator):
        try:
            return (numerator / denominator)
        except:
            return (f"WARNING - dividing by zero")


div = DivisionByZeroError(2, 5)
print(DivisionByZeroError.intdiv(2, 0))
print(DivisionByZeroError.intdiv(2, 0.1))
print(div.intdiv(2, 5))
print(div.intdiv(2, 0))