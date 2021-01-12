# -*- coding: cp1251 -*-
'''����������� ����� Stationery (������������ ��������������). ���������� � ��� ������� title (��������) � ����� draw (���������).
����� ������� ��������� ������� ���������.� ������� ��� �������� ������ Pen (�����), Pencil (��������), Handle (������).
� ������ �� ������� ����������� ��������������� ������ draw. ��� ������� �� ������� ����� ������ �������� ���������� ���������.
������� ���������� ������� � ���������, ��� ������� ��������� ����� ��� ������� ����������
'''
class Stationery:

    def __init__(self,title):
        self.title = title

    def draw(self):
        return f'������ ���������.'

class Pen(Stationery):

    def __init__(self,title):
        super().__init__(title)

    def draw(self):
        return f'�� ������� {self.title}. ������ ��������� �����.'

class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'�� ������� {self.title}. ������ ��������� ���������.'

class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'�� ������� {self.title}. ������ ��������� �������.'

pens = Pen('�����')
pencils = Pencil('��������')
handles = Handle('������')
print(pens.draw())
print(pencils.draw())
print(handles.draw())