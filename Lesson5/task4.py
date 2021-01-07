'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл
'''
rus_dict = {'One':'Один','Two':'Два','Three':'Три','Four':'Четыре','Five':'Пять'}
str_list = []
try:
    with open("task4.txt") as f_third, open("task4_1.txt", 'w') as f_four:
        for line in f_third:
            key = line.split(' ',1)
            str_list.append(rus_dict[key[0]]+' ' + key[1])
        f_four.writelines(str_list)
except IOError:
    print("Произошла ошибка ввода-вывода!")