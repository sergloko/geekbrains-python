# -*- coding: cp1251 -*-
'''����������� ������� ����� Worker (��������), � ������� ���������� ��������: name, surname, position (���������), income (�����).
��������� ������� ������ ���� ���������� � ��������� �� �������, ���������� ��������: ����� � ������, ��������, {"wage": wage, "bonus": bonus}.
������� ����� Position (���������) �� ���� ������ Worker.
� ������ Position ����������� ������ ��������� ������� ����� ���������� (get_full_name) � ������ � ������ ������ (get_total_income).
��������� ������ ������� �� �������� ������
(������� ���������� ������ Position, �������� ������, ��������� �������� ���������, ������� ������ �����������)
'''
class Worker:
    def __init__(self,name,surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 200000, "bonus": 50000}

class Position(Worker):
    def __init__(self,name,surname,position,wage,bonus):
        super().__init__(name,surname,position,wage,bonus)
    def get_full_name(self):
        return self.position + ' ' + self.name + ' ' + self.surname
    def get_total_income(self):
        return self._income.get('wage')+self._income.get('bonus')

staff = Position('����', 'Petrov', 'DevOps-�������', 200000, 50000)
print(staff.get_full_name())
print(staff.position)
print(staff.get_total_income())
