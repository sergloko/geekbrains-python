# -*- coding: cp1251 -*-
'''���������� ������� ����� Car. � ������� ������ ������ ���� ��������� ��������: speed, color, name, is_police (������).
� ����� ������: go, stop, turn(direction), ������� ������ ��������, ��� ������ �������, ������������, ��������� (����).
������� ��������� �������� �������: TownCar, SportCar, WorkCar, PoliceCar.
�������� � ������� ����� ����� show_speed, ������� ������ ���������� ������� �������� ����������.
��� ������� TownCar � WorkCar �������������� ����� show_speed. ��� �������� �������� ����� 60 (TownCar) � 40 (WorkCar)
������ ���������� ��������� � ���������� ��������
�������� ���������� �������, ��������� �������� ���������.
��������� ������ � ���������, �������� ���������. ��������� ����� ������� � ����� �������� ���������
'''
class Car:

    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} �������!'
    def stop(self):
        return f'{self.name} ������������'
    def turn(self, direction):
        if direction == '�������':
            return f'{self.name} ��������� �������'
        else:
            return f'{self.name} ��������� ������'
    def show_speed(self):
        return f'� {self.name} ������� �������� {self.speed}'

class TownCar(Car):
    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'� {self.name} �������� ���������'
        else:
            return f'� {self.name} ������� �������� {self.speed}'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'� {self.name} �������� ���������'
        else:
            return f'� {self.name} ������� �������� {self.speed}'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

audi = SportCar(100, '�����', 'Audi', False)
oka = TownCar(120, '�������', 'Oka', False)
lada = WorkCar(70, '���������', 'Lada', True)
ford = PoliceCar(110, '�����',  'Ford', True)
print(lada.turn('������'))
print(f'{oka.turn("�������")}, {audi.stop()}')
print(f'{lada.go()} {lada.show_speed()}')
print(f'{lada.name} {lada.color}')
print(f'{audi.name} ����������� ������? {audi.is_police}')
print(f'{lada.name}  ����������� ������? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.show_speed())