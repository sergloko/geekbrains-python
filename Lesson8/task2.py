# -*- coding: cp1251 -*-
'''�������� ����������� �����-����������, �������������� �������� ������� �� ����. ��������� ��� ������ �� ������,
�������� �������������. ��� ����� ������������� ���� � �������� �������� ��������� ������ ���������
���������� ��� �������� � �� ����������� � �������
'''
class DelZero(Exception):
    def __init__(self,div):
        self.dividend = div

divider = input("������� ��������: ")
dividend = input("������� �������: ")
try:
    divider = int(divider)
    dividend = int(dividend)
    if dividend == 0:
        raise DelZero("�� ���� ������ ������!")
except ValueError:
    print("�� ����� �� �����")
except DelZero as err:
    print(err)
else:
    print(f"��� ������. ���� �����: {divider / dividend}")
