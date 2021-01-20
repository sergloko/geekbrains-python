# -*- coding: cp1251 -*-
'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой
'''
class DelZero(Exception):
    def __init__(self,div):
        self.dividend = div

divider = input("Введите делитель: ")
dividend = input("Введите делимое: ")
try:
    divider = int(divider)
    dividend = int(dividend)
    if dividend == 0:
        raise DelZero("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except DelZero as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {divider / dividend}")
