# -*- coding: cp1251 -*-
'''����������� ����� Road (������), � ������� ���������� ��������: length (�����), width (������).
�������� ������ ��������� ������ ������������ ��� �������� ���������� ������. �������� ������� �����������.
���������� ����� ������� ����� ��������, ������������ ��� �������� ����� ��������� �������.
������������ �������: �����*������*����� �������� ��� �������� ������ �� ����� ������ ���������, �������� � 1 ��*����� �� ������� �������.
��������� ������ ������.
��������: 20�*5000�*25��*5�� = 12500 �
'''
class Road:
    _lenght = float
    _width = float
    def __init__(self,length=1000,width=10):
        self._lenght = length
        self._width = width

    def Mass_calc(self):
        self._mass = self._lenght * self._width * 25 * 0.005
        print(f"����������� ����� ��������: {self._mass} ����")

while True:
        change_lenght = input('������� ����� �������: ')
        change_width = input('������� ������ �������: ')
        try:
            change_lenght = float(change_lenght)
            change_width = float(change_width)
            break
        except ValueError as e:
            print('������� �����')
massroad = Road(change_lenght,change_width)
massroad.Mass_calc()

