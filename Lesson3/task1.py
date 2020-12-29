"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль"""

while True:
    user_divider = input('Введите делитель: ')
    if not user_divider.isdigit():
        print("Вы ввели не число. Попробуйте снова: ")
    else:
        new_divider = int(user_divider)
        break
while True:
    user_dividend = input('Введите делимое: ')
    if not user_dividend.isdigit():
        print("Вы ввели не число. Попробуйте снова: ")
    elif int(user_dividend) == 0:
        print("На ноль делить нельзя! Попробуйте снова:")
    else:
        new_dividend = int(user_dividend)
        break


def first_division(divider, dividend):
    return divider / dividend

print(first_division(new_divider, new_dividend))