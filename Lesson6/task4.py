# -*- coding: cp1251 -*-
'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат
'''
class Car:

    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала!'
    def stop(self):
        return f'{self.name} остановилась'
    def turn(self, direction):
        if direction == 'направо':
            return f'{self.name} повернула направо'
        else:
            return f'{self.name} повернула налево'
    def show_speed(self):
        return f'У {self.name} текущая скорость {self.speed}'

class TownCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'У {self.name} скорость превышена'
        else:
            return f'У {self.name} текущая скорость {self.speed}'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'У {self.name} скорость превышена'
        else:
            return f'У {self.name} текущая скорость {self.speed}'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

audi = SportCar(100, 'Белая', 'Audi', False)
oka = TownCar(120, 'Красная', 'Oka', False)
lada = WorkCar(70, 'Малиновая', 'Lada', True)
ford = PoliceCar(110, 'Синий',  'Ford', True)
print(lada.turn('налево'))
print(f'{oka.turn("направо")}, {audi.stop()}')
print(f'{lada.go()} {lada.show_speed()}')
print(f'{lada.name} {lada.color}')
print(f'{audi.name} полицейская машина? {audi.is_police}')
print(f'{lada.name}  полицейская машина? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.show_speed())