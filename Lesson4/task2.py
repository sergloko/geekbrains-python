# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123]
from random import randint
def find(iter):
    """ Ищет большие числа в списке
    :param iterable: списой целых чисел
    """
    temp = iter[0]

    for i in iter:
        if i > temp:
            yield i

        temp = i

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
    my_list.append(randint(1,100))
    i += 1
print(my_list)
generator = find(my_list)
print(list(generator))