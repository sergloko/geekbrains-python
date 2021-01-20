# -*- coding: cp1251 -*-
'''����������� ������ ��������� � ������������ �������. �������� ����� ������������ �����, ���������� ����������
������� �������� � ��������� ����������� �����. ��������� ������ �������, ������ ���������� ������
(����������� �����) � �������� �������� � ��������� ��������� �����������.
��������� ������������ ����������� ����������
'''
class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}'

    def __add__(self, other):
        return ComplexNumber(self.number + other.number)

    def __mul__(self, other):
        return ComplexNumber(self.number * other.number)

x = ComplexNumber(20)
y = ComplexNumber(30)
print(f'��������� �������� ��������: {x+y}')
print(f'��������� �������� ���������: {x*y}')