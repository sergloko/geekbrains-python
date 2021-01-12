# -*- coding: cp1251 -*-
'''Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра
'''
class Stationery:

    def __init__(self,title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки.'

class Pen(Stationery):

    def __init__(self,title):
        super().__init__(title)

    def draw(self):
        return f'Вы выбрали {self.title}. Запуск отрисовки ручки.'

class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы выбрали {self.title}. Запуск отрисовки карандаша.'

class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы выбрали {self.title}. Запуск отрисовки маркера.'

pens = Pen('Ручка')
pencils = Pencil('Карандаш')
handles = Handle('Маркер')
print(pens.draw())
print(pencils.draw())
print(handles.draw())