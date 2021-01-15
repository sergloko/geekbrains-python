# -*- coding: cp1251 -*-
'''Реализовать проект расчета суммарного расхода ткани на производство одежды.
 Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
 размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
 для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
 реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property
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
        return str(f'Расход ткани на пальто = {self.coat_consumption:.2f}')


    def get_suit_consumption(self):
        return str(f'Расход ткани на костюм = {self.suit_consumption:.2f}')

    # @property
    def get_total_consumption(self):
        return str(f'Расход ткани суммарный = {self.suit_consumption + self.coat_consumption:.2f}')

clothers = Clothers(5,7)

print(clothers.get_coat_consumption())
print(clothers.get_suit_consumption())
print(clothers.get_total_consumption())