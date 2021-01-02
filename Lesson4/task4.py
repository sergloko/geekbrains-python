'''Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]'''
from random import randint
while True:
    inp_count = input('Введите количество элементов: ')
    if not inp_count.isdigit():
        print("Вы ввели не число. Попробуйте снова: ")
    else:
        count = int(inp_count)
        break
my_list = []
i = 1
while i <= count:
    my_list.append(randint(1,20))
    i += 1
print(my_list)
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)