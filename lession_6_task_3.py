# Урок-6
# Задача-3
#  Реализовать базовый класс Worker (работник), в котором определить атрибуты:
#  name, surname, position (должность), income (доход).
#  Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
#  оклад и премия, например, {"wage": wage, "bonus": bonus}.
#  Создать класс Position (должность) на базе класса Worker.
#  В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
#  дохода с учетом премии (get_total_income).
#  Проверить работу примера на реальных данных (создать экземпляры класса Position,
#  передать данные, проверить значения атрибутов, вызвать методы экземпляров).
#
# Решение-задачи-3
print("Решение-задачи-3")
print("")


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = 0
        self.bonus = 0
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


first_test = Position('Ivan', 'Bulochkin', 'Car Driver', 10000, 40000)
print(first_test.get_full_name())
print(first_test.position)
print(first_test.get_total_income())


