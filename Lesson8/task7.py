# -*- coding: cp1251 -*-
'''Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата
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
print(f'Результат операции сложения: {x+y}')
print(f'Результат операции умножения: {x*y}')