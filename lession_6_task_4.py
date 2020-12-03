# Урок-6
# Задача-4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте
# в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и
# WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
#
# Решение-задачи-4
print("Решение-задачи-4")
print("")

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        # if self.speed >= 0:
            return f'Автомобиль {self.name} начала движение'

    def stop(self):
        # if self.speed <=0:
            return f'Автомобиль {self.name} закончила движение'

    def turn_left(self):
        return f'Автомобиль {self.name} повернул налево'

    def turn_right(self):
        return f'Автомобиль {self.name} повернул направо'

    def show_speed(self):
        return f'Скорость автомобиля {self.name} - {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Автомобиль {self.name} превысил разрешенную скорость'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print (f'Скорость автомобиля {self.name} - {self.speed}')
        # return f'Скорость автомобиля WorkCar - {self.speed}'

        if self.speed > 40:
            return f'Автомобиль {self.name} превысил разрешенную скорость'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


skoda = TownCar(61, "yellow", "skoda octavia", "Нет")
konigseig = SportCar(100, "white", "konigseig agera", "Нет")
vw = WorkCar(45, "white", "vw Caddy", "Нет")
bmw = PoliceCar(120, "white", "bmw M5", "Да")

print(skoda.show_speed())
print(konigseig.show_speed())
print(vw.show_speed())
print(bmw.show_speed())
print()
print(skoda.turn_left())
print(konigseig.turn_right())
print()
print(vw.stop())
print(vw.go())
print()
print(f'Автомобиль {bmw.name} полицеский? - {bmw.is_police}')
print(f'Автомобиль {vw.name} полицеский? - {vw.is_police}')

