# -*- coding: cp1251 -*-
#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
try:
    with open('task5.txt', 'w') as f_five:
        user_data = input('Введите цифры через пробел: ')
        f_five.writelines(user_data)
        user_num = user_data.split()
        print(sum(map(int,user_num)))
except IOError:
    print("Произошла ошибка ввода-вывода!")