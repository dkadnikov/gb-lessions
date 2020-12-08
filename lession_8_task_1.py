# Урок-8
# Задача-1
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

#
# Решение-задачи-1
print("Решение-задачи-1", '\n')


class Data:
    def __init__(self, get_data):
        self.get_data = str(get_data)

    @classmethod
    def extract_dmy(cls, get_data):
        extracted_data = []

        for i in get_data.split():
            if i != '-': extracted_data.append(i)
            #if i !=':': extracted_data.append(i)
            #if i !='.':extracted_data.append(i)
        return int(extracted_data[0]), int(extracted_data[1]), int(extracted_data[2])

    @staticmethod
    def date_validator(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Все данные введены верно'
                else:
                    return f'Введен неверный год'
            else:
                return f'Введен неверный месяц'
        else:
            return f'Введен неверный день'

    def __str__(self):
        return f'Сегодня {Data.extract_dmy(self.get_data)}'

date_today = Data('08 - 12 - 2020')
print(date_today)
print()
print(Data.date_validator(18,12,2021))
print(date_today.date_validator(11,13,2018))
print(date_today.date_validator(33,12,2010))

