# -*- coding: cp1251 -*-
'''Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''
class Road:
    _lenght = float
    _width = float
    def __init__(self,length=1000,width=10):
        self._lenght = length
        self._width = width

    def Mass_calc(self):
        self._mass = self._lenght * self._width * 25 * 0.005
        print(f"Необходимая масса асфальта: {self._mass} тонн")

while True:
        change_lenght = input('Введите длину полотна: ')
        change_width = input('Введите ширину полотна: ')
        try:
            change_lenght = float(change_lenght)
            change_width = float(change_width)
            break
        except ValueError as e:
            print('Ожидаем число')
massroad = Road(change_lenght,change_width)
massroad.Mass_calc()

