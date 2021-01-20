# -*- coding: cp1251 -*-
'''Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных
'''

class Date:
    def __init__(self,date):
        self.input_date = date

    def __str__(self):
        return f' Дата введена корректно.'

    @classmethod
    def get_number(cls,date: str):
        
        day, month, year = date.replace('-',' ').split()
        return int(day), int(month), int(year)


    @staticmethod
    def valid_date(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <=12:
                if 2020 >= year >= 0:
                    return f'Дата верна'
                else:
                    return f'Год введен неверно'
            else:
                return f'Месяц введен неверно'
        else:
            return f'День введен неверно'


date = '30-12-1989'
print(Date.get_number(date))
print(Date.get_number('33-14-2020'))
print(Date.valid_date(3, 1, 2020))
print(Date.valid_date(33, 14, 2021))