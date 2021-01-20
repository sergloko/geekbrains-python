# -*- coding: cp1251 -*-
'''����������� ����� �����, �������-����������� �������� ������ ��������� ���� � ���� ������ ������� �����-�����-���.
� ������ ������ ����������� ��� ������. ������, � ����������� @classmethod, ������ ��������� �����, �����, ��� �
��������������� �� ��� � ���� ������. ������, � ����������� @staticmethod, ������ ��������� ��������� �����,
������ � ���� (��������, ����� � �� 1 �� 12). ��������� ������ ���������� ��������� �� �������� ������
'''

class Date:
    def __init__(self,date):
        self.input_date = date

    def __str__(self):
        return f' ���� ������� ���������.'

    @classmethod
    def get_number(cls,date: str):
        
        day, month, year = date.replace('-',' ').split()
        return int(day), int(month), int(year)


    @staticmethod
    def valid_date(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <=12:
                if 2020 >= year >= 0:
                    return f'���� �����'
                else:
                    return f'��� ������ �������'
            else:
                return f'����� ������ �������'
        else:
            return f'���� ������ �������'


date = '30-12-1989'
print(Date.get_number(date))
print(Date.get_number('33-14-2020'))
print(Date.valid_date(3, 1, 2020))
print(Date.valid_date(33, 14, 2021))