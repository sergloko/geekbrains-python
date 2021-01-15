# -*- coding: cp1251 -*-
'''����������� ������ ������� ���������� ������� ����� �� ������������ ������.
 �������� �������� (�����) ����� ������� � ������, ������� ����� ����� ������������ ��������.
 � ����� ������ � ���� ������� ��������� ������ � ������. � ���� ����� ������ ���������� ���������:
 ������ (��� ������) � ���� (��� �������). ��� ����� ���� ������� �����: V � H, ��������������.
��� ����������� ������� ����� �� ������� ���� ������ ������������ �������: ��� ������ (V/6.5 + 0.5),
 ��� ������� (2*H + 0.3). ��������� ������ ���� ������� �� �������� ������.
����������� ����� ������� ������� �����. ��������� �� �������� ���������� �� ���� ����� ������:
 ����������� ����������� ������ ��� �������� ������� �������, ��������� �� �������� ������ ���������� @property
'''
from abc import ABC, abstractmethod

class AbstractClothes(ABC):
    @abstractmethod
    def get_coat_consumption(self):
        pass

    @abstractmethod
    def get_suit_consumption(self):
        pass

    @abstractmethod
    def get_total_consumption(self):
        pass

class Clothers(AbstractClothes):
    def __init__(self,v,h):
        self.v = v
        self.h = h
        self.coat_consumption = self.v / 6.5 + 0.5
        self.suit_consumption = self.h * 2 + 0.3


    def get_coat_consumption(self):
        return str(f'������ ����� �� ������ = {self.coat_consumption:.2f}')


    def get_suit_consumption(self):
        return str(f'������ ����� �� ������ = {self.suit_consumption:.2f}')

    # @property
    def get_total_consumption(self):
        return str(f'������ ����� ��������� = {self.suit_consumption + self.coat_consumption:.2f}')

clothers = Clothers(5,7)

print(clothers.get_coat_consumption())
print(clothers.get_suit_consumption())
print(clothers.get_total_consumption())