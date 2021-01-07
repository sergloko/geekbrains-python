'''Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка
'''
user_line = 0
try:
    with open('task1.txt' ,'a') as first_file:
        while user_line != '':
            user_line = input('Введите строку: ')
            print(user_line, file=first_file)
except IOError:
    print("Произошла ошибка ввода-вывода!")